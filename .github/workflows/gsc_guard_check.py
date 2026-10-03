#!/usr/bin/env python3
"""gsc-guard write-contract checker. Run by .github/workflows/gsc-guard.yml.

Inputs (environment, set by the workflow): HEAD_REF, HEAD_SHA, BASE_REF,
DEFAULT_BRANCH, PR_TITLE. The workflow has already fetched the PR head to
refs/remotes/pr/head and the default branch to refs/remotes/origin/<default>.
This script makes the diff itself:

    git -c core.quotePath=false diff --name-status --no-renames -z \
        origin/<default>...refs/remotes/pr/head

Result:
  exit 0  not a routine PR ("not a routine PR - skipped"), or a routine PR
          whose every change fits its job's write contract ("OK - ...").
  exit 1  one "::error::" line per violation, then a summary line.

The rules are routines/README.md section 3 (v2 spec section 6). classify(),
check() and evaluate() take plain values, so test_gsc_guard_check.py can call
them without git. Run the tests with:
    python3 .github/workflows/test_gsc_guard_check.py
"""
import datetime
import os
import re
import subprocess
import sys
from fnmatch import fnmatchcase

JOBS = ("analyse", "review", "seed", "sweep", "intake")
KEY_REQUIRED = {"review"}
KEY_FORBIDDEN = {"seed", "sweep", "intake"}

# claude/gsc-{job}-[{KEY}-]{YYYY-MM-DD}-{HHMM}. Used with fullmatch, so the
# date and time are anchored at the end and a KEY may contain '-' and '.'.
BRANCH_RE = re.compile(
    r"claude/gsc-(?P<job>analyse|review|seed|sweep|intake)-"
    r"(?:(?P<key>[A-Za-z0-9._-]+)-)?"
    r"(?P<date>\d{4}-\d{2}-\d{2})-(?P<time>\d{4})",
    re.ASCII,
)
TITLE_RE = re.compile(r"^(HELD · )?GSC (ANALYSE|REVIEW|SEED|SWEEP|INTAKE)\b")
BRANCH_SHAPE = "claude/gsc-{job}-[{KEY}-]{YYYY-MM-DD}-{HHMM}"

LOCKED_TOP = {"model", "routines", ".claude", ".github"}
BANNED_NAMES = {"claude.md", "claude.local.md", "agents.md", "readme.md"}

MEMO_RE = re.compile(
    r"memos/(?P<dir>[A-Za-z0-9._-]+)/(?P<key>[A-Za-z0-9._-]+)_(?P<date>\d{4}-\d{2}-\d{2})_GSC\.md",
    re.ASCII,
)
SNAPSHOT_RE = re.compile(
    r"registers/(?P<folder>\d{4})/REGISTER_v\d+_(?P<date>(?P<year>\d{4})-\d{2}-\d{2})\.md",
    re.ASCII,
)
# Versions may be dotted (DRAFT_QUEUE has been v1.1); the blob check still
# requires a byte copy of the outgoing file.
TODO_ARCHIVE_RE = re.compile(r"queue/archive/TODO_v\d+(?:\.\d+)*_\d{4}-\d{2}-\d{2}\.md", re.ASCII)
DRAFT_QUEUE_ARCHIVE_RE = re.compile(r"queue/archive/DRAFT_QUEUE_v\d+(?:\.\d+)*_\d{4}-\d{2}-\d{2}\.md", re.ASCII)
PROPOSAL_ARCHIVE_RE = re.compile(r"queue/archive/proposals/(?P<name>[^/]+\.md)")
INTAKE_MODIFIABLE = ("_REGISTER.md", "queue/TODO.md", "queue/DRAFT_QUEUE.md")

HEAD_REV = "refs/remotes/pr/head"


# ---------------------------------------------------------------- helpers

def printable(text):
    """Escape control characters so a file name can never start a new log
    line, and break the legacy '##[' command prefix, which the runner reads
    anywhere in a line. Neither can then inject a workflow command."""
    out = []
    for ch in str(text):
        code = ord(ch)
        if code < 0x20 or code == 0x7F or 0x80 <= code < 0xA0:
            out.append("\\x%02x" % code)
        elif ch in "  ":
            out.append("\\u%04x" % code)
        else:
            out.append(ch)
    return "".join(out).replace("##[", "#\\#[")


def has_control(text):
    return any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text)


def seg_match(path, pattern):
    """Glob match segment by segment: '*' never crosses '/'."""
    path_parts = path.split("/")
    pattern_parts = pattern.split("/")
    if len(path_parts) != len(pattern_parts):
        return False
    return all(fnmatchcase(p, q) for p, q in zip(path_parts, pattern_parts))


def parse_name_status_z(data):
    """Parse `git diff --name-status -z` output into [(status, path), ...].

    Format: STATUS NUL PATH NUL ..., e.g. b"A\\0queue/runs/x.md\\0".
    R and C lines carry two paths; they come back as "old -> new" (the
    checker rejects those statuses anyway). Raises ValueError on a
    truncated stream.
    """
    if isinstance(data, (bytes, bytearray)):
        text = bytes(data).decode("utf-8", "replace")
    else:
        text = data
    fields = text.split("\0")
    if fields and fields[-1] == "":
        fields.pop()
    entries = []
    i = 0
    while i < len(fields):
        status = fields[i]
        if not status:
            raise ValueError("empty status field at position %d" % i)
        npaths = 2 if status[0] in "RC" else 1
        if i + npaths >= len(fields):
            raise ValueError("status %r at position %d has no path" % (status, i))
        paths = fields[i + 1:i + 1 + npaths]
        if any(p == "" for p in paths):
            raise ValueError("empty path after status %r at position %d" % (status, i))
        entries.append((status, " -> ".join(paths)))
        i += 1 + npaths
    return entries


# ---------------------------------------------------------- classification

def parse_branch(head_ref):
    """Return (info, error). info = {'job', 'key', 'date', 'time'} or None."""
    m = BRANCH_RE.fullmatch(head_ref or "")
    if not m:
        return None, ("head branch '%s' is not a routine branch name (expected %s, job one of %s)"
                      % (head_ref, BRANCH_SHAPE, ", ".join(JOBS)))
    job, key, date, time = m.group("job", "key", "date", "time")
    try:
        datetime.date(int(date[0:4]), int(date[5:7]), int(date[8:10]))
    except ValueError:
        return None, "head branch '%s': %s is not a valid date" % (head_ref, date)
    if int(time[:2]) > 23 or int(time[2:]) > 59:
        return None, "head branch '%s': %s is not a valid HHMM time" % (head_ref, time)
    if job in KEY_REQUIRED and key is None:
        return None, "head branch '%s': a %s branch must carry the KEY" % (head_ref, job)
    if job in KEY_FORBIDDEN and key is not None:
        return None, "head branch '%s': a %s branch must not carry a KEY (found '%s')" % (head_ref, job, key)
    return {"job": job, "key": key, "date": date, "time": time}, None


def classify(head_ref, title):
    """Return (routine, info, errors).

    routine: True if the head ref starts with 'claude/gsc' or the title
             starts with 'GSC {JOB}' / 'HELD · GSC {JOB}'.
    info:    parsed branch {'job', 'key', 'date', 'time'}, or None when the
             branch name is not a valid routine branch.
    errors:  branch-name and title problems (empty for a clean routine PR).
    """
    head_ref = head_ref or ""
    title = title or ""
    title_m = TITLE_RE.match(title)
    if not head_ref.startswith("claude/gsc") and not title_m:
        return False, None, []
    errors = []
    info, branch_error = parse_branch(head_ref)
    if branch_error:
        errors.append(branch_error)
    if title_m is None:
        errors.append("title '%s' does not start with 'GSC {JOB}' or 'HELD · GSC {JOB}' "
                      "(JOB one of ANALYSE, REVIEW, SEED, SWEEP, INTAKE)" % title)
    elif info is not None and title_m.group(2) != info["job"].upper():
        errors.append("title job %s does not match branch job '%s'" % (title_m.group(2), info["job"]))
    return True, info, errors


# ------------------------------------------------------------------ rules

def global_problems(status, path):
    """Rules that apply to every routine PR, whatever the job."""
    if status not in ("A", "M", "D"):
        return ["status %s is not allowed (only A, M, D)" % status]
    problems = []
    segments = path.split("/")
    if has_control(path):
        problems.append("control character in the file name")
    if segments[0].lower() in LOCKED_TOP:
        problems.append("framework-locked path (model/, routines/, .claude/, .github/)")
    if any(s.startswith(".") for s in segments):
        problems.append("hidden path segment (a folder or file name starting with '.')")
    if segments[-1].lower() in BANNED_NAMES:
        problems.append("file name not allowed in a routine PR (CLAUDE.md, CLAUDE.local.md, AGENTS.md, README.md)")
    if not path.endswith(".md"):
        problems.append("only .md files are allowed")
    return problems


def split_global(entries):
    """Return (errors, clean_entries): entries that break a global rule are
    reported and left out of the job rules."""
    errors, clean = [], []
    for status, path in entries:
        problems = global_problems(status, path)
        if problems:
            errors.extend("%s %s: %s" % (status, path, p) for p in problems)
        else:
            clean.append((status, path))
    return errors, clean


def _check_analyse_review(job, entries, date, time, branch_key):
    word = job.upper()
    errors = []
    memo_entries = [(s, p) for s, p in entries if p.startswith("memos/")]
    other = [(s, p) for s, p in entries if not p.startswith("memos/")]
    if len(memo_entries) > 1:
        errors.append("%d memo paths in one %s PR: a run writes at most one memo" % (len(memo_entries), word))
    memo_key = None
    for status, path in memo_entries:
        m = MEMO_RE.fullmatch(path)
        if status != "A":
            errors.append("%s %s: a routine may only add a new memo, never change or delete one" % (status, path))
        elif not m or m.group("dir") != m.group("key"):
            errors.append("A %s: a memo must be memos/{KEY}/{KEY}_%s_GSC.md" % (path, date))
        elif m.group("date") != date:
            errors.append("A %s: memo date %s is not the run date %s from the branch" % (path, m.group("date"), date))
        elif branch_key is None:
            errors.append("A %s: a keyless ANALYSE branch (queue exhausted) may not add a memo" % path)
        elif job == "review" and m.group("key") != branch_key:
            errors.append("A %s: a REVIEW memo must be for the branch key %s" % (path, branch_key))
        elif len(memo_entries) == 1:
            memo_key = m.group("key")

    # K in {branch key, memo key}: the memo key may differ after a re-key (MODEL 7.1a).
    keys = []
    for k in (branch_key, memo_key):
        if k and k not in keys:
            keys.append(k)
    # A re-keyed ANALYSE run with no memo (INCOMPLETE) names its row and
    # evidence file by the resolved key (routines/ANALYSE.md step 5). Take
    # that key from the run's single keyed ANALYSE row. It allows adds only:
    # without a memo, no evidence of the resolved key may be deleted.
    deletable = ["queue/evidence/%s_*.md" % k for k in keys]
    if job == "analyse" and branch_key is not None and not memo_entries:
        row_re = re.compile(r"queue/rows/%s_%s_ANALYSE_(?P<key>[A-Za-z0-9._-]+)\.md"
                            % (re.escape(date), re.escape(time)), re.ASCII)
        row_keys = [m.group("key") for m in (row_re.fullmatch(p) for s, p in other if s == "A") if m]
        if len(row_keys) == 1 and row_keys[0] not in keys:
            keys.append(row_keys[0])
    added = {"queue/runs/%s_%s_%s.md" % (date, time, word)}
    if job == "analyse":
        added.add("queue/rows/%s_%s_ANALYSE.md" % (date, time))
    for k in keys:
        added.add("queue/rows/%s_%s_%s_%s.md" % (date, time, word, k))
        added.add("queue/runs/%s_%s_%s_%s.md" % (date, time, word, k))
        added.add("queue/evidence/%s_%s_INCOMPLETE.md" % (k, date))
    scope = "key %s" % " / ".join(keys) if keys else "no key"
    for status, path in other:
        if status == "A" and path in added:
            continue
        if status == "D" and any(seg_match(path, pattern) for pattern in deletable):
            continue
        errors.append("%s %s: not in the %s write contract for this branch (%s, run %s %s)"
                      % (status, path, word, scope, date, time))
    return errors


def _check_exact(job, entries, allowed_added):
    errors = []
    for status, path in entries:
        if status == "A" and path in allowed_added:
            continue
        errors.append("%s %s: not in the %s write contract (a %s run may only add %s)"
                      % (status, path, job.upper(), job.upper(), " and ".join(sorted(allowed_added))))
    return errors


def _same_blob(errors, blob_lookup, added, source, what):
    head_blob = blob_lookup("head", added)
    base_blob = blob_lookup("base", source)
    if base_blob is None:
        errors.append("A %s: %s, but %s does not exist at the merge base" % (added, what, source))
    elif head_blob is None:
        errors.append("A %s: cannot read the added file at the PR head" % added)
    elif head_blob != base_blob:
        errors.append("A %s: %s is not a byte copy of %s at the merge base" % (added, what, source))


def _check_intake(entries, date, time, blob_lookup):
    errors = []
    deleted = {p for s, p in entries if s == "D"}
    run_note = "queue/runs/%s_%s_INTAKE.md" % (date, time)
    for status, path in entries:
        if status == "M":
            if path not in INTAKE_MODIFIABLE:
                errors.append("M %s: INTAKE may modify only %s" % (path, ", ".join(INTAKE_MODIFIABLE)))
            continue
        if status == "D":
            if not (seg_match(path, "queue/rows/*.md") or seg_match(path, "queue/proposals/*.md")):
                errors.append("D %s: INTAKE may delete only queue/rows/*.md and queue/proposals/*.md" % path)
            continue
        # status == "A"
        if path == run_note:
            continue
        m = SNAPSHOT_RE.fullmatch(path)
        if m:
            if m.group("folder") != m.group("year"):
                errors.append("A %s: snapshot folder %s is not the year of its date %s"
                              % (path, m.group("folder"), m.group("date")))
            else:
                _same_blob(errors, blob_lookup, path, "_REGISTER.md", "register snapshot")
            continue
        if TODO_ARCHIVE_RE.fullmatch(path):
            _same_blob(errors, blob_lookup, path, "queue/TODO.md", "TODO archive")
            continue
        if DRAFT_QUEUE_ARCHIVE_RE.fullmatch(path):
            _same_blob(errors, blob_lookup, path, "queue/DRAFT_QUEUE.md", "DRAFT_QUEUE archive")
            continue
        m = PROPOSAL_ARCHIVE_RE.fullmatch(path)
        if m:
            source = "queue/proposals/" + m.group("name")
            if source not in deleted:
                errors.append("A %s: an archived proposal must be moved, but %s is not deleted in this PR"
                              % (path, source))
            _same_blob(errors, blob_lookup, path, source, "archived proposal")
            continue
        errors.append("A %s: not in the INTAKE write contract (allowed adds: %s, registers/{YYYY}/REGISTER_v{N}_{date}.md, "
                      "queue/archive/TODO_v{n}_{date}.md, queue/archive/DRAFT_QUEUE_v{n}_{date}.md, "
                      "queue/archive/proposals/{name}.md)" % (path, run_note))
    return errors


def check(job, entries, branch_info, blob_lookup):
    """Check a routine PR's changes against its job's write contract.

    job:         'analyse' | 'review' | 'seed' | 'sweep' | 'intake'
    entries:     [(status, path), ...] from parse_name_status_z()
    branch_info: {'key', 'date', 'time'} from the branch (parse_branch())
    blob_lookup: f(side, path) -> blob id or None; side 'base' = the merge
                 base of the default branch and the PR head, 'head' = the PR
                 head. Used only by the INTAKE byte-copy checks.
    Returns a list of violation messages (empty = OK).
    """
    if job not in JOBS:
        return ["unknown routine job '%s'" % job]
    errors, clean = split_global(entries)
    date = branch_info["date"]
    time = branch_info["time"]
    key = branch_info.get("key")
    if job in ("analyse", "review"):
        errors += _check_analyse_review(job, clean, date, time, key)
    elif job == "sweep":
        errors += _check_exact(job, clean, {"queue/rows/%s_%s_SWEEP.md" % (date, time),
                                            "queue/runs/%s_%s_SWEEP.md" % (date, time)})
    elif job == "seed":
        errors += _check_exact(job, clean, {"queue/proposals/%s_%s_QUEUE-SEED.md" % (date, time),
                                            "queue/runs/%s_%s_SEED.md" % (date, time)})
    else:
        errors += _check_intake(clean, date, time, blob_lookup)
    return errors


def evaluate(head_ref, title, base_ref, default_branch, entries, blob_lookup):
    """Full decision for one PR. Returns None for a non-routine PR (skip),
    else the list of violations (empty = OK)."""
    routine, info, errors = classify(head_ref, title)
    if not routine:
        return None
    errors = list(errors)
    if not default_branch or base_ref != default_branch:
        errors.append("routine PR targets '%s', not the default branch '%s'" % (base_ref, default_branch))
    if info is None:
        errors += split_global(entries)[0]
    else:
        errors += check(info["job"], entries, info, blob_lookup)
    return errors


# ---------------------------------------------------------------- git I/O

def default_git(args):
    """Run git; return (returncode, stdout bytes)."""
    proc = subprocess.run(["git"] + list(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if proc.returncode != 0 and proc.stderr.strip():
        sys.stderr.write("git %s: %s\n" % (args[0], printable(proc.stderr.decode("utf-8", "replace").strip())))
    return proc.returncode, proc.stdout


def make_blob_lookup(git, base_rev, head_rev):
    """Blob ids via `git rev-parse --verify --quiet <rev>:<path>`."""
    def lookup(side, path):
        rev = base_rev if side == "base" else head_rev
        rc, out = git(["rev-parse", "--verify", "--quiet", "%s:%s" % (rev, path)])
        blob = out.decode("ascii", "replace").strip()
        return blob if rc == 0 and blob else None
    return lookup


def report(errors, label):
    if errors:
        for e in errors:
            print("::error::" + printable(e).replace("%", "%25"))
        print("gsc-guard: %d violation(s) in %s. Do not merge until each one is fixed or understood."
              % (len(errors), printable(label)))
        return 1
    print("OK — %s: every change fits the write contract." % printable(label))
    return 0


def main(env=None, git=None):
    env = os.environ if env is None else env
    git = default_git if git is None else git
    head_ref = env.get("HEAD_REF", "")
    head_sha = env.get("HEAD_SHA", "")
    base_ref = env.get("BASE_REF", "")
    default_branch = env.get("DEFAULT_BRANCH", "")
    title = env.get("PR_TITLE", "")

    routine, _info, _errors = classify(head_ref, title)
    if not routine:
        print("not a routine PR — skipped (branch '%s')" % printable(head_ref))
        return 0

    label = "routine PR from '%s'" % head_ref
    if not default_branch:
        return report(["DEFAULT_BRANCH is empty; cannot diff the PR"], label)
    base_rev = "refs/remotes/origin/" + default_branch

    if head_sha:
        rc, out = git(["rev-parse", "--verify", "--quiet", HEAD_REV])
        fetched = out.decode("ascii", "replace").strip()
        if rc != 0 or fetched != head_sha:
            return report(["PR head moved (event %s, fetched %s); re-run the check" % (head_sha, fetched or "none")],
                          label)

    rc, out = git(["merge-base", base_rev, HEAD_REV])
    merge_base = out.decode("ascii", "replace").strip()
    if rc != 0 or not merge_base:
        return report(["cannot find the merge base of origin/%s and the PR head" % default_branch], label)

    rc, out = git(["-c", "core.quotePath=false", "diff", "--name-status", "--no-renames", "-z",
                   "%s...%s" % (base_rev, HEAD_REV)])
    if rc != 0:
        return report(["git diff failed"], label)
    try:
        entries = parse_name_status_z(out)
    except ValueError as exc:
        return report(["cannot parse the git diff output: %s" % exc], label)

    print("Routine PR: branch '%s', title '%s', base '%s'"
          % (printable(head_ref), printable(title), printable(base_ref)))
    print("Changed paths, merge base %s ... PR head (%d):" % (merge_base[:12], len(entries)))
    for status, path in entries:
        print("  %s\t%s" % (status, printable(path)))

    errors = evaluate(head_ref, title, base_ref, default_branch, entries,
                      make_blob_lookup(git, merge_base, HEAD_REV))
    return report(errors or [], label)


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(errors="backslashreplace")
    except AttributeError:
        pass
    try:
        exit_code = main()
    except Exception as exc:  # fail closed, never a silent pass
        print("::error::gsc-guard checker crashed: " + printable(repr(exc)).replace("%", "%25"))
        exit_code = 1
    sys.exit(exit_code)
