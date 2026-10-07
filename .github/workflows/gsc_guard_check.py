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

The rules are routines/README.md section 3 (v2 spec section 6). Every job:
archive/ is append-only (adds only) and the retired registers/ and
queue/archive/ paths are rejected (MODEL v4.5.0 section 7.5). Memo folders
(MODEL v4.5.0 sections 6, 6.6, 7.4a): memos/{KEY}/ holds exactly one file, the
current memo. A REVIEW that adds memos/K/K_D_GSC.md moves its one prior
memos/K/K_P_GSC.md (P before D) unchanged to archive/memos/K/ in the same PR;
nothing else moves a memo. ANALYSE is only for a key with no memos/K/ and no
archive/memos/K/. The folder checks list trees at the merge base, at the PR
head and on the current default branch (tree_lookup); without a listing they
fail closed. The register (MODEL v4.5.0 section 7.1): INTAKE modifies
_REGISTER.md and its machine twin register.csv together, with a byte-copy
snapshot pair (.md and .csv, same N and date); the head register.csv must
carry the tool's header and one data row per names_total, and _REGISTER.md
must be exactly its rendering by routines/tools/gsc_register.py from this
checkout (text_lookup; fails closed without it). No other job and no other
path may hold a .csv. Every row file an ANALYSE, REVIEW or SWEEP PR adds must
pass the tool's lint-row at the PR head (MODEL v4.5.2: its name, title and
verdicts, and for a verdict row the exact row-from-memo --table print of its
memo; text_lookup, fails closed without it). classify(), check() and evaluate() take plain values, so
test_gsc_guard_check.py can call them without git. Run the tests with:
    python3 .github/workflows/test_gsc_guard_check.py
"""
import datetime
import importlib.util
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
# Root archive/ tree (MODEL v4.5.0, section 7.5): append-only history that
# mirrors the live paths. registers/ and queue/archive/ are retired.
ARCHIVE_TOP = "archive"
RETIRED_TOP = ("registers/", "queue/archive/")
SNAPSHOT_RE = re.compile(
    r"archive/registers/(?P<folder>\d{4})/REGISTER_v(?P<n>\d+)_(?P<date>(?P<year>\d{4})-\d{2}-\d{2})\.md",
    re.ASCII,
)
# The register's machine twin (MODEL v4.5.0 section 7.1) and its snapshot.
REGISTER_CSV = "register.csv"
CSV_SNAPSHOT_RE = re.compile(
    r"archive/registers/(?P<folder>\d{4})/REGISTER_v(?P<n>\d+)_(?P<date>(?P<year>\d{4})-\d{2}-\d{2})\.csv",
    re.ASCII,
)
# Versions may be dotted (DRAFT_QUEUE has been v1.1); the blob check still
# requires a byte copy of the outgoing file.
TODO_ARCHIVE_RE = re.compile(r"archive/queue/TODO_v\d+(?:\.\d+)*_\d{4}-\d{2}-\d{2}\.md", re.ASCII)
DRAFT_QUEUE_ARCHIVE_RE = re.compile(r"archive/queue/DRAFT_QUEUE_v\d+(?:\.\d+)*_\d{4}-\d{2}-\d{2}\.md", re.ASCII)
PROPOSAL_ARCHIVE_RE = re.compile(r"archive/queue/proposals/(?P<name>[^/]+\.md)")
INTAKE_MODIFIABLE = ("_REGISTER.md", REGISTER_CSV, "queue/TODO.md", "queue/DRAFT_QUEUE.md")
# Paths whose movement on the default branch since an INTAKE PR's merge base
# makes that PR stale (gsc-automerge's INTAKE base check, MODEL v4.5.0 section
# 8.7 item 10): everything INTAKE reads to build a version or writes.
INTAKE_BASE_PATHS = ("_REGISTER.md", REGISTER_CSV, "queue/TODO.md", "queue/DRAFT_QUEUE.md",
                     "archive/registers/", "archive/queue/")
# routines/tools/gsc_register.py in this (trusted, default-branch) checkout.
TOOL_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                         "routines", "tools", "gsc_register.py")
_TOOL = []

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
    if not (path.endswith(".md") or path == REGISTER_CSV or CSV_SNAPSHOT_RE.fullmatch(path)):
        problems.append("only .md files are allowed (plus INTAKE's register.csv and its "
                        "archive/registers/{YYYY}/ .csv snapshot)")
    if segments[0].lower() == ARCHIVE_TOP and status != "A":
        problems.append("archive/ is append-only: a routine never modifies or deletes a file there (MODEL section 7.5)")
    if path.lower().startswith(RETIRED_TOP):
        problems.append("retired path: archives live under archive/ since MODEL v4.5.0 "
                        "(archive/registers/, archive/queue/)")
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


SIDE_NAMES = {"base": "the merge base", "head": "the PR head", "main": "the current default branch"}


def _list_dir(errors, tree_lookup, side, folder):
    """Sorted basenames directly under `folder` at `side` ('base', 'head' or
    'main'), or None after recording a fail-closed error (no lookup, or git
    could not list it)."""
    names = tree_lookup(side, folder) if tree_lookup is not None else None
    if names is None:
        errors.append("cannot list %s at %s; memo folder unverifiable" % (folder, SIDE_NAMES.get(side, side)))
    return names


def _check_review_move(errors, memo_path, memo_key, memo_dels, arch_adds, date, blob_lookup, tree_lookup):
    """A REVIEW that adds memos/K/K_D_GSC.md must move exactly its one prior
    memo memos/K/K_P_GSC.md (P before D) to archive/memos/K/ unchanged, in
    the same PR (MODEL v4.5.0 sections 6.6 and 7.4a). memos/K/ must hold only
    that prior at the merge base and on the current default branch, and only
    the new memo at the PR head."""
    folder = "memos/%s" % memo_key

    def is_prior(path):
        m = MEMO_RE.fullmatch(path)
        return bool(m) and m.group("dir") == memo_key and m.group("key") == memo_key and m.group("date") < date

    prior = [p for p in memo_dels if is_prior(p)]
    if len(memo_dels) != 1 or len(prior) != 1:
        errors.append("A %s: a REVIEW must move exactly its one prior memo %s/%s_{P}_GSC.md "
                      "(P before D) to archive/memos/%s/ in the same PR (found %d memo deletion(s): %s)"
                      % (memo_path, folder, memo_key, memo_key, len(memo_dels), ", ".join(memo_dels) or "none"))
        return
    deleted = prior[0]
    archived = "archive/" + deleted
    if arch_adds != [archived]:
        errors.append("D %s: the archived prior must be %s (same filename, nothing else under archive/; "
                      "found %s)" % (deleted, archived, ", ".join(arch_adds) or "none"))
        if archived not in arch_adds:
            return
    _same_blob(errors, blob_lookup, archived, deleted, "archived memo")
    prior_name = deleted.rsplit("/", 1)[1]
    for side in ("base", "main"):
        names = _list_dir(errors, tree_lookup, side, folder)
        if names is None:
            break
        if names != [prior_name]:
            if side == "base":
                errors.append("D %s: %s holds %d file(s) at the merge base (%s); a REVIEW moves exactly "
                              "one prior, so an attended clean-up comes first"
                              % (deleted, folder, len(names), ", ".join(names) or "none"))
            else:
                errors.append("D %s: %s on the current default branch holds %s, not this REVIEW's prior: "
                              "main moved for this key since the PR's base, so the REVIEW is stale"
                              % (deleted, folder, ", ".join(names) or "nothing"))
            break
    head = _list_dir(errors, tree_lookup, "head", folder)
    if head is not None and head != [memo_path.rsplit("/", 1)[1]]:
        errors.append("A %s: after the REVIEW %s must hold only the new memo (holds %s)"
                      % (memo_path, folder, ", ".join(head) or "nothing"))


def _check_analyse_review(job, entries, date, time, branch_key, blob_lookup=None, tree_lookup=None):
    word = job.upper()
    errors = []
    memo_adds = [p for s, p in entries if s == "A" and p.startswith("memos/")]
    memo_dels = [p for s, p in entries if s == "D" and p.startswith("memos/")]
    memo_mods = [p for s, p in entries if s == "M" and p.startswith("memos/")]
    arch_adds = [p for s, p in entries if s == "A" and p.lower().startswith(ARCHIVE_TOP + "/")]
    other = [(s, p) for s, p in entries
             if not p.startswith("memos/") and not p.lower().startswith(ARCHIVE_TOP + "/")]
    for path in memo_mods:
        errors.append("M %s: a routine never changes a memo (a REVIEW writes a new file and moves "
                      "the prior to archive/memos/)" % path)
    if len(memo_adds) > 1:
        errors.append("%d memos added in one %s PR: a run writes at most one memo" % (len(memo_adds), word))
    memo_key = None
    memo_path = None
    for path in memo_adds:
        m = MEMO_RE.fullmatch(path)
        if not m or m.group("dir") != m.group("key"):
            errors.append("A %s: a memo must be memos/{KEY}/{KEY}_%s_GSC.md" % (path, date))
        elif m.group("date") != date:
            errors.append("A %s: memo date %s is not the run date %s from the branch" % (path, m.group("date"), date))
        elif branch_key is None:
            errors.append("A %s: a keyless ANALYSE branch (queue exhausted) may not add a memo" % path)
        elif job == "review" and m.group("key") != branch_key:
            errors.append("A %s: a REVIEW memo must be for the branch key %s" % (path, branch_key))
        elif len(memo_adds) == 1:
            memo_key = m.group("key")
            memo_path = path

    # Memo moves (MODEL v4.5.0): only a REVIEW with its one valid new memo
    # moves the prior; ANALYSE is only for keys with no memo history at all.
    if job == "analyse":
        for path in memo_dels + arch_adds:
            status = "D" if path in memo_dels else "A"
            errors.append("%s %s: ANALYSE never moves or deletes a memo, and adds nothing under archive/"
                          % (status, path))
        if memo_key is not None:
            for folder in ("memos/%s" % memo_key, "archive/memos/%s" % memo_key):
                for side in ("base", "main"):
                    names = _list_dir(errors, tree_lookup, side, folder)
                    if names is None:
                        break
                    if names:
                        errors.append("A %s: %s already exists at %s (%d file(s)): this key is REVIEW "
                                      "territory, never a new ANALYSE"
                                      % (memo_path, folder, SIDE_NAMES[side], len(names)))
                        break
    elif memo_key is not None:
        _check_review_move(errors, memo_path, memo_key, memo_dels, arch_adds, date, blob_lookup, tree_lookup)
    elif not memo_adds:
        for path in memo_dels + arch_adds:
            status = "D" if path in memo_dels else "A"
            errors.append("%s %s: a REVIEW without a new memo (claim stub, INCOMPLETE) moves no memo"
                          % (status, path))
    else:
        for path in memo_dels + arch_adds:
            status = "D" if path in memo_dels else "A"
            errors.append("%s %s: a REVIEW moves its prior only alongside one valid new memo" % (status, path))

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
    if job == "analyse" and branch_key is not None and not memo_adds:
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


def _check_intake(entries, date, time, blob_lookup, text_lookup=None):
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
        m = None
        for regex, source, what in ((SNAPSHOT_RE, "_REGISTER.md", "register snapshot"),
                                    (CSV_SNAPSHOT_RE, REGISTER_CSV, "register.csv snapshot")):
            m = regex.fullmatch(path)
            if m:
                if m.group("folder") != m.group("year"):
                    errors.append("A %s: snapshot folder %s is not the year of its date %s"
                                  % (path, m.group("folder"), m.group("date")))
                else:
                    _same_blob(errors, blob_lookup, path, source, what)
                break
        if m:
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
        errors.append("A %s: not in the INTAKE write contract (allowed adds: %s, "
                      "archive/registers/{YYYY}/REGISTER_v{N}_{date}.md and .csv, "
                      "archive/queue/TODO_v{n}_{date}.md, archive/queue/DRAFT_QUEUE_v{n}_{date}.md, "
                      "archive/queue/proposals/{name}.md)" % (path, run_note))
    errors += _check_register_pair(entries, text_lookup)
    return errors


def register_tool():
    """routines/tools/gsc_register.py from this checkout (the default branch,
    so trusted), or None when it cannot be loaded. Loaded once; no byte-code
    is written."""
    if not _TOOL:
        module = None
        saved = sys.dont_write_bytecode
        sys.dont_write_bytecode = True
        try:
            spec = importlib.util.spec_from_file_location("gsc_register_tool", TOOL_PATH)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if not isinstance(getattr(module, "CSV_HEADER", None), list):
                module = None
        except Exception:  # fail closed: the caller reports it
            module = None
        finally:
            sys.dont_write_bytecode = saved
        _TOOL.append(module)
    return _TOOL[0]


def _first_lines(text, n=3):
    lines = [line.strip() for line in str(text).splitlines() if line.strip()]
    more = " (+%d more)" % (len(lines) - n) if len(lines) > n else ""
    return " ".join(lines[:n]) + more


def _check_register_pair(entries, text_lookup):
    """MODEL v4.5.0 section 7.1: _REGISTER.md and register.csv change together,
    with exactly one .md and one .csv snapshot of the same N and date, and the
    head files are what routines/tools/gsc_register.py renders."""
    errors = []
    modified = {p for s, p in entries if s == "M"}
    md_snaps = [m for m in (SNAPSHOT_RE.fullmatch(p) for s, p in entries if s == "A") if m]
    csv_snaps = [m for m in (CSV_SNAPSHOT_RE.fullmatch(p) for s, p in entries if s == "A") if m]
    md_changed, csv_changed = "_REGISTER.md" in modified, REGISTER_CSV in modified
    if not md_changed and not csv_changed:
        for m in md_snaps + csv_snaps:
            errors.append("A %s: a register snapshot without a register change" % m.group(0))
        return errors
    if md_changed != csv_changed:
        errors.append("M %s: _REGISTER.md and register.csv change together, with matching snapshots "
                      "(MODEL section 7.1; the register tool writes both)"
                      % ("_REGISTER.md" if md_changed else REGISTER_CSV))
    if len(md_snaps) != 1 or len(csv_snaps) != 1:
        errors.append("M _REGISTER.md: a register version adds exactly one .md and one .csv snapshot of the "
                      "outgoing version (found %d .md, %d .csv)" % (len(md_snaps), len(csv_snaps)))
    elif (md_snaps[0].group("n"), md_snaps[0].group("date")) != (csv_snaps[0].group("n"),
                                                                  csv_snaps[0].group("date")):
        errors.append("A %s: the .md and .csv snapshots must share N and date (%s)"
                      % (csv_snaps[0].group(0), md_snaps[0].group(0)))
    if not csv_changed:
        return errors
    csv_text = text_lookup("head", REGISTER_CSV) if text_lookup is not None else None
    md_text = text_lookup("head", "_REGISTER.md") if text_lookup is not None else None
    if csv_text is None or md_text is None:
        errors.append("M register.csv: cannot read register.csv and _REGISTER.md at the PR head; "
                      "register contents unverifiable")
        return errors
    tool = register_tool()
    if tool is None:
        errors.append("M register.csv: cannot load routines/tools/gsc_register.py from the default branch; "
                      "register contents unverifiable")
        return errors
    if csv_text.split("\n", 1)[0].rstrip("\r") != ",".join(tool.CSV_HEADER):
        errors.append("M register.csv: the first line is not the MODEL section 7.1b header")
        return errors
    try:
        rows, problems = tool.read_csv_text(csv_text)
    except tool.ToolError as exc:
        return errors + ["M register.csv: %s" % _first_lines(exc)]
    errors += ["M register.csv: %s" % p for p in problems]
    fm = tool.parse_front_matter(md_text)
    if fm.get("names_total") != str(len(rows)):
        errors.append("M register.csv: %d data rows, but _REGISTER.md names_total is %s"
                      % (len(rows), fm.get("names_total", "missing")))
    try:
        rendered = tool.render(rows, fm.get("register_version", ""), fm.get("register_date", ""))
    except tool.ToolError as exc:
        return errors + ["M register.csv: %s" % _first_lines(exc)]
    if rendered != md_text.replace("\r\n", "\n"):
        errors.append("M _REGISTER.md: not the rendering of register.csv by routines/tools/gsc_register.py "
                      "(never edit the register by hand)")
    return errors


def _check_row_files(entries, text_lookup):
    """Each added row file passes routines/tools/gsc_register.py lint-row at the
    PR head (MODEL v4.5.2), read with the default branch's tool; fails closed
    when the tool, the row file or the text lookup is missing. A path outside
    the row grammar is left to the write-contract check."""
    rows = [path for status, path in entries
            if status == "A" and seg_match(path, "queue/rows/*.md") and path != "queue/rows/README.md"]
    if not rows:
        return []
    tool = register_tool()
    if tool is None or not hasattr(tool, "lint_row"):
        return ["A %s: cannot load the lint-row check from routines/tools/gsc_register.py on the default branch"
                % rows[0]]
    if text_lookup is None:
        return ["A %s: no file reader for the lint-row check (fail closed)" % path for path in rows]
    errors = []
    for path in rows:
        if not tool.ROW_FILE_RE.match(path):
            continue
        text = text_lookup("head", path)
        if text is None:
            errors.append("A %s: cannot read the row file at the PR head" % path)
            continue
        for fail in tool.lint_row(path, text, lambda memo: text_lookup("head", memo)):
            errors.append("A %s: lint-row: %s" % (path, fail))
    return errors


def check(job, entries, branch_info, blob_lookup, tree_lookup=None, text_lookup=None):
    """Check a routine PR's changes against its job's write contract.

    job:         'analyse' | 'review' | 'seed' | 'sweep' | 'intake'
    entries:     [(status, path), ...] from parse_name_status_z()
    branch_info: {'key', 'date', 'time'} from the branch (parse_branch())
    blob_lookup: f(side, path) -> blob id or None; side 'base' = the merge
                 base of the default branch and the PR head, 'head' = the PR
                 head. Used by the INTAKE byte-copy checks and by REVIEW's
                 archived-prior byte copy.
    tree_lookup: f(side, folder) -> sorted basenames directly under folder
                 ([] when it does not exist), or None when it cannot be
                 listed; side 'base', 'head' or 'main' (the current default
                 branch). Used by the ANALYSE and REVIEW memo-folder checks,
                 which fail closed without it (see make_tree_lookup()).
    text_lookup: f(side, path) -> file text or None; side 'head'. Used by the
                 INTAKE register checks (register.csv and _REGISTER.md at the
                 PR head) and the row-file lint of ANALYSE, REVIEW and SWEEP
                 (the row file and its memo at the PR head), which fail closed
                 without it (make_text_lookup()).
    Returns a list of violation messages (empty = OK).
    """
    if job not in JOBS:
        return ["unknown routine job '%s'" % job]
    errors, clean = split_global(entries)
    date = branch_info["date"]
    time = branch_info["time"]
    key = branch_info.get("key")
    if job in ("analyse", "review"):
        errors += _check_analyse_review(job, clean, date, time, key, blob_lookup, tree_lookup)
        errors += _check_row_files(clean, text_lookup)
    elif job == "sweep":
        errors += _check_exact(job, clean, {"queue/rows/%s_%s_SWEEP.md" % (date, time),
                                            "queue/runs/%s_%s_SWEEP.md" % (date, time)})
        errors += _check_row_files(clean, text_lookup)
    elif job == "seed":
        errors += _check_exact(job, clean, {"queue/proposals/%s_%s_QUEUE-SEED.md" % (date, time),
                                            "queue/runs/%s_%s_SEED.md" % (date, time)})
    else:
        errors += _check_intake(clean, date, time, blob_lookup, text_lookup)
    return errors


def evaluate(head_ref, title, base_ref, default_branch, entries, blob_lookup, tree_lookup=None,
             text_lookup=None):
    """Full decision for one PR. Returns None for a non-routine PR (skip),
    else the list of violations (empty = OK). blob_lookup, tree_lookup and
    text_lookup are as in check(); without tree_lookup every ANALYSE or REVIEW
    memo fails closed, without text_lookup every INTAKE register change."""
    routine, info, errors = classify(head_ref, title)
    if not routine:
        return None
    errors = list(errors)
    if not default_branch or base_ref != default_branch:
        errors.append("routine PR targets '%s', not the default branch '%s'" % (base_ref, default_branch))
    if info is None:
        errors += split_global(entries)[0]
    else:
        errors += check(info["job"], entries, info, blob_lookup, tree_lookup, text_lookup)
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


def make_text_lookup(git, base_rev, head_rev):
    """File text via `git cat-file blob <rev>:<path>` ('base' or 'head');
    None when git fails or the file is not UTF-8."""
    def lookup(side, path):
        rev = base_rev if side == "base" else head_rev
        rc, out = git(["cat-file", "blob", "%s:%s" % (rev, path)])
        if rc != 0:
            return None
        try:
            return out.decode("utf-8")
        except UnicodeDecodeError:
            return None
    return lookup


def make_tree_lookup(git, base_rev, head_rev, main_rev=None):
    """Folder listings via `git ls-tree -z --name-only --full-tree <rev> -- <folder>/`.

    side 'base' -> base_rev, 'head' -> head_rev, 'main' -> main_rev (the
    current default branch; base_rev when not given). Returns the sorted
    basenames directly under the folder, [] when it does not exist, or None
    when git fails (the caller then fails closed). Results are cached."""
    revs = {"base": base_rev, "head": head_rev, "main": main_rev or base_rev}
    cache = {}

    def lookup(side, folder):
        rev = revs.get(side)
        if not rev:
            return None
        folder = folder.rstrip("/")
        if (rev, folder) not in cache:
            rc, out = git(["ls-tree", "-z", "--name-only", "--full-tree", rev, "--", folder + "/"])
            if rc != 0:
                cache[(rev, folder)] = None
            else:
                prefix = folder + "/"
                names = [item[len(prefix):] for item in out.decode("utf-8", "replace").split("\0")
                         if item.startswith(prefix) and len(item) > len(prefix)]
                cache[(rev, folder)] = sorted(names)
        names = cache[(rev, folder)]
        return None if names is None else list(names)
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
                      make_blob_lookup(git, merge_base, HEAD_REV),
                      make_tree_lookup(git, merge_base, HEAD_REV, base_rev),
                      make_text_lookup(git, merge_base, HEAD_REV))
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
