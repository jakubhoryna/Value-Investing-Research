#!/usr/bin/env python3
"""gsc-automerge: squash-merges finished routine PRs in a merge class
(MODEL v4.5.0 §8.7 item 10). Run by .github/workflows/gsc-automerge.yml.

Inputs (environment): GH_TOKEN (the per-run GITHUB_TOKEN), REPO, GSC_AUTOMERGE
(off | dry-run | on; anything else, including unset, is off), EVENT_NAME and
TRIGGER_BRANCH (the guard run's head branch on a workflow_run event).

decide(ctx, pr) is the classifier; it never merges and never comments, so the
digest (gsc_notify.py) imports it to list what needs Jakub. Outcomes:
  MERGE        finished, guard success on the exact head sha, contract clean,
               in a merge class: ANALYSE WATCH/AVOID/DNAF, INCOMPLETE, prior
               found, queue exhausted; REVIEW with the prior memo's verdict
               (INCOMPLETE included); SWEEP, held-zone changes included (J11:
               the changes go to the job summary and the morning digest);
               INTAKE whose base has not moved on main.
  WAIT         silent; a later event retries ([running], guard not finished,
               an incident-cancelled guard run on attempt 1, head moved).
  HOLD         silent ([fixing] is Jakub's; an INTAKE whose base moved is
               superseded by the next INTAKE, F2).
  HOLD_NOTIFY  one comment on the standing 'GSC - needs Jakub' issue per
               (PR, head sha, reason): BUY, HELD name in an ANALYSE or REVIEW,
               verdict change, every SEED, guard not success, title/memo/row
               mismatch, unexpected files, re-key, a SWEEP whose portfolio
               table lacks a held name or a held name's zone word
               ('held-missing'), stopped/blocked, a refused merge, an
               exception.
Fail closed: any doubt holds the PR. The merge is pinned to the head sha that
passed (`sha=`), titled '{PR title} (#n)'. Never comments on, labels,
reviews, edits or closes a PR (each would wake the routine's session).

PR content is read with git as data (cat-file, diff, ls-tree); nothing from
a PR is executed. Python 3.11+ standard library only.
Tests: python3 .github/workflows/test_gsc_automerge.py
"""
import datetime
import os
import re
import subprocess
import sys
import time

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import gsc_guard_check as chk  # noqa: E402  (trusted sibling on the default branch)
import gsc_gh  # noqa: E402

MAIN = "refs/remotes/origin/main"
MODES = ("off", "dry-run", "on")
VERDICTS = ("BUY", "WATCH", "AVOID", "DNAF")
MERGE, WAIT, HOLD, HOLD_NOTIFY = "MERGE", "WAIT", "HOLD", "HOLD_NOTIFY"
JOB_ORDER = {"INTAKE": 0, "SWEEP": 1, "REVIEW": 2, "ANALYSE": 3, "SEED": 4}
RETRYABLE = ("cancelled", "timed_out", "startup_failure")
# INTAKE deletion check (INTAKE.md step 8): both sides of every move INTAKE or
# REVIEW makes are listed, so a move reads as a rename and never as a deletion.
DELETION_PATHS = ("queue/rows", "queue/proposals", "memos", "archive/memos", "archive/queue/proposals")
# On a workflow_run event the triggering PR is decided first; other open
# routine PRs updated within RECENT are then swept while the run is younger
# than BUDGET seconds (a pending run replaced by concurrency loses little).
RECENT = datetime.timedelta(hours=2)
BUDGET = 40.0

TITLE_RE = re.compile(
    r"^(?P<held>HELD · )?GSC (?P<job>ANALYSE|REVIEW|SEED|SWEEP|INTAKE)"
    r"(?: (?P<key>[A-Za-z0-9._-]+))? (?P<date>\d{4}-\d{2}-\d{2})(?: — (?P<outcome>.+))?$")
ANALYSE_VERDICT_RE = re.compile(r"^(?P<v>BUY|WATCH|AVOID|DNAF) \(.+\)$")
REVIEW_VERDICT_RE = re.compile(r"^(?P<v>BUY|WATCH|AVOID|DNAF)(?: \(.*?\))?; (?P<moved>.+)$")
WAS_RE = re.compile(r"^was (?P<old>BUY|WATCH|AVOID|DNAF)\b")
INCOMPLETE_RE = re.compile(r"^INCOMPLETE \(.+\)$")
PRIOR_RE = re.compile(r"^prior found \(REVIEW\)$")
EXHAUSTED_RE = re.compile(r"^queue exhausted$")
SWEEP_RE = re.compile(r"^\d+/\d+ priced · .+$")
INTAKE_RE = re.compile(r"^(?:register v\d+|no register change) \(\d+ rows?\)$")
STOP_RE = re.compile(r" — (?:stopped|blocked):")
ZONE_WORD_RE = re.compile(r"^\W*(ADD|HOLD|SELL-FLAG)\b")


class AutomergeError(Exception):
    """A step that cannot be completed; the PR is held (fail closed)."""


class Outcome:
    def __init__(self, kind, code="", text="", sha="", title="", job="", key="", note=""):
        self.kind, self.code, self.text = kind, code, text
        self.sha, self.title, self.job, self.key = sha, title, job, key
        self.note = note        # carried to the job summary through the merge (J11 zone changes)

    def __repr__(self):
        return "Outcome(%s, %s, %r)" % (self.kind, self.code, self.text)


def read_mode(value):
    """'on' or 'dry-run' only for exactly that value; anything else is off
    (fail closed: 'ON', ' on' and an unset variable all mean off)."""
    return value if value in ("on", "dry-run") else "off"


def quiet_git(args):
    """Run git; (returncode, stdout bytes). stderr is dropped: a missing path
    is an expected answer here, never a log line."""
    proc = subprocess.run(["git"] + list(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    return proc.returncode, proc.stdout


class Ctx:
    """Everything decide() needs; tests pass fakes for gh, git, clock and sleep."""

    def __init__(self, gh, git=None, repo="", mode="off", now=None, sleep=None, log=None, tool=None):
        self.gh = gh
        self.git = git or quiet_git
        self.repo = repo
        self.mode = mode
        self.now = now or (lambda: datetime.datetime.now(datetime.timezone.utc))
        self.sleep = sleep or time.sleep
        self.log = log or (lambda line: print("gsc-automerge: " + chk.printable(line)))
        self.tool = tool or chk.register_tool()
        self._held = None

    def main_moved(self):
        self._held = None


# ---------------------------------------------------------------- git and text

def git_ok(ctx, args, what):
    rc, out = ctx.git(args)
    if rc != 0:
        raise AutomergeError("%s failed (git %s, rc %s)" % (what, args[0], rc))
    return out


def rev_parse(ctx, rev):
    rc, out = ctx.git(["rev-parse", "--verify", "--quiet", rev])
    value = out.decode("ascii", "replace").strip()
    return value if rc == 0 and value else None


def show(ctx, rev, path):
    """File text at rev, or None when absent."""
    rc, out = ctx.git(["cat-file", "blob", "%s:%s" % (rev, path)])
    if rc != 0:
        return None
    return out.decode("utf-8", "replace")


def fetch_main(ctx):
    git_ok(ctx, ["fetch", "--no-tags", "origin", "+refs/heads/main:" + MAIN], "fetching main")
    ctx.main_moved()


def front_matter(ctx, text):
    return ctx.tool.parse_front_matter(text or "") if text else {}


def verdict_word(ctx, value):
    word = ctx.tool.first_token(value or "")
    return word if word in VERDICTS else None


def row_verdict_cell(ctx, text):
    """First word of the Verdict cell under '## Register row (new)'."""
    sections = ctx.tool.sections_of(text or "")
    rows = ctx.tool.table_rows(sections.get("Register row (new)", []))
    if not rows or "verdict" not in rows[0]:
        return None
    return verdict_word(ctx, rows[0]["verdict"])


def register_rows(ctx, rev):
    """{key: {'held', 'zone', 'verdict'}} from register.csv at rev, else from
    the _REGISTER.md tables; raises when neither can be read."""
    text = show(ctx, rev, chk.REGISTER_CSV)
    if text is not None:
        rows, _problems = ctx.tool.read_csv_text(text, legacy_ok=True)   # a merge base may predate the lens columns
        return {r["key"]: {"held": r["held"] == "true", "zone": r["zone"], "verdict": r["verdict"]}
                for r in rows}
    md = show(ctx, rev, "_REGISTER.md")
    if md is None:
        raise AutomergeError("cannot read the register at %s" % rev[:12])
    out = {}
    for heading, lines in ctx.tool.sections_of(md).items():
        portfolio = heading.lower().startswith("portfolio")
        for row in ctx.tool.table_rows(lines):
            cell = (row.get("ticker") or "").strip()
            key = re.split(r"[\s(]", cell, 1)[0] if cell else ""
            if not key:
                continue
            entry = out.setdefault(key, {"held": False, "zone": "n.m.", "verdict": None})
            if portfolio:
                entry["held"] = True
                entry["zone"] = row.get("zone", "-")
            elif row.get("verdict"):
                entry["verdict"] = verdict_word(ctx, row["verdict"])
    return out


def held_keys(ctx):
    if ctx._held is None:
        ctx._held = {k: v for k, v in register_rows(ctx, MAIN).items() if v["held"]}
    return ctx._held


# ---------------------------------------------------------------- titles

def title_state(title):
    t = (title or "").rstrip()
    if t.endswith("[running]"):
        return Outcome(WAIT, "running", "run still in progress")
    if t.endswith("[fixing]"):
        return Outcome(HOLD, "fixing", "yours, marked [fixing]")
    if t.endswith("[abandoned]") or t.endswith("[superseded]"):
        return Outcome(HOLD_NOTIFY, "title-state", "title ends %s" % t.rsplit(" ", 1)[-1])
    if STOP_RE.search(t):
        return Outcome(HOLD_NOTIFY, "stopped", "the run %s" % t.split(" — ", 1)[1][:160])
    return None


def parse_title(title):
    """{'held', 'job', 'key', 'date', 'outcome', 'kind', 'verdict', 'old'} for
    a finished title in the README §1 grammar, else None."""
    m = TITLE_RE.match(title or "")
    if not m or not m.group("outcome"):
        return None
    out = {"held": bool(m.group("held")), "job": m.group("job"), "key": m.group("key"),
           "date": m.group("date"), "outcome": m.group("outcome"), "verdict": None, "old": None}
    job, outcome, key = out["job"], out["outcome"], out["key"]
    kind = None
    if job == "ANALYSE" and key is None:
        kind = "exhausted" if EXHAUSTED_RE.match(outcome) else None
    elif job == "ANALYSE":
        v = ANALYSE_VERDICT_RE.match(outcome)
        if v:
            kind, out["verdict"] = "verdict", v.group("v")
        elif INCOMPLETE_RE.match(outcome):
            kind = "incomplete"
        elif PRIOR_RE.match(outcome):
            kind = "prior"
    elif job == "REVIEW" and key is not None:
        v = REVIEW_VERDICT_RE.match(outcome)
        if v:
            kind, out["verdict"] = "verdict", v.group("v")
            was = WAS_RE.match(v.group("moved"))
            out["old"] = was.group("old") if was else None
        elif INCOMPLETE_RE.match(outcome):
            kind = "incomplete"
    elif job == "SWEEP" and key is None:
        kind = "sweep" if SWEEP_RE.match(outcome) else None
    elif job == "INTAKE" and key is None:
        kind = "intake" if INTAKE_RE.match(outcome) else None
    elif job == "SEED" and key is None:
        kind = "seed" if outcome.strip() else None
    if kind is None:
        return None
    out["kind"] = kind
    return out


# ---------------------------------------------------------------- guard runs

def guard_state(gh, sha):
    """('success'|'retry'|'cancelled'|'failed'|'pending'|'none', run or None);
    for 'pending' the run is the oldest unfinished one.

    `created_at` order is event order. Every title change on an open PR either
    creates a non-skipped run or leaves a '[running]' title that title_state()
    holds, so the newest non-skipped run checked the live title. A re-run keeps
    its `created_at`, so a successful re-run counts. A skipped job is never read
    as success, and a completed run without a job named `guard` is 'failed'
    unless it never started (a renamed job must not fall back to the run's
    conclusion, which may be 'success' for a run whose only job was skipped)."""
    payload = gh.get("actions/workflows/gsc-guard.yml/runs?head_sha=%s&event=pull_request_target&per_page=50"
                     % sha)
    runs = list((payload or {}).get("workflow_runs") or [])
    unfinished = [r for r in runs if r.get("status") != "completed"]
    if unfinished:   # the oldest one, so maintenance can flag a stuck run
        return "pending", min(unfinished, key=lambda r: (r.get("created_at") or "", r.get("id") or 0))
    runs.sort(key=lambda r: (r.get("created_at") or "", r.get("id") or 0), reverse=True)
    for run in runs:
        if run.get("conclusion") == "skipped":
            continue
        jobs = (gh.get("actions/runs/%d/jobs?per_page=30" % int(run["id"])) or {}).get("jobs") or []
        guard = [j for j in jobs if j.get("name") == "guard"]
        if guard:
            conclusion = guard[0].get("conclusion")
            if conclusion == "skipped":
                continue
        elif run.get("conclusion") in RETRYABLE:
            conclusion = run.get("conclusion")       # a run that never started has no job
        else:
            conclusion = "no-guard-job"              # never read the run's own 'success' (fail closed)
        if conclusion == "success":
            return "success", run
        if conclusion in RETRYABLE:
            return ("retry" if int(run.get("run_attempt") or 1) == 1 else "cancelled"), run
        return "failed", run
    return "none", None


# ---------------------------------------------------------------- decide

def decide(ctx, listed):
    """The outcome for one open PR (never merges, never comments)."""
    n = int(listed["number"])
    pr = ctx.gh.get("pulls/%d" % n)
    title = pr.get("title") or ""
    sha = (pr.get("head") or {}).get("sha") or ""
    ref = (pr.get("head") or {}).get("ref") or ""

    def out(kind, code, text, job="", key=""):
        return Outcome(kind, code, text, sha=sha, title=title, job=job, key=key)

    if pr.get("state") != "open":
        return out(WAIT, "closed", "no longer open")
    routine = gsc_gh.routine_kind(pr)
    if routine is None:
        return out(WAIT, "not-routine", "not a routine PR")
    state = title_state(title)
    if state is not None:
        return out(state.kind, state.code, state.text)
    if routine == "mismatch":
        return out(HOLD_NOTIFY, "title-branch",
                   "branch and title do not form a routine pair (branch '%s')" % ref[:80])
    t = parse_title(title)
    if t is None:
        return out(HOLD_NOTIFY, "title-grammar", "the finished title is outside the routines/README.md §1 grammar")
    info, err = chk.parse_branch(ref)
    if err or info["job"].upper() != t["job"] or info["key"] != t["key"] or info["date"] != t["date"]:
        return out(HOLD_NOTIFY, "title-branch", "title job, key or date differs from the branch '%s'" % ref[:80],
                   job=t["job"], key=t["key"] or "")
    job, key, date, time_ = t["job"], t["key"], t["date"], info["time"]
    if job == "SEED":
        return out(HOLD_NOTIFY, "seed", "QUEUE-SEED proposals always need Jakub", job=job)

    # 2. The guard on the exact head sha.
    state, run = guard_state(ctx.gh, sha)
    if state == "pending":
        return out(WAIT, "guard-pending", "guard run in progress", job, key or "")
    if state == "none":
        return out(WAIT, "guard-none", "no guard run on the head sha yet", job, key or "")
    if state == "retry":
        return out(WAIT, "guard-retry", "guard run %s (attempt 1); the daily maintenance re-runs it"
                   % run.get("conclusion"), job, key or "")
    if state == "cancelled":
        return out(HOLD_NOTIFY, "guard-cancelled", "guard run %s again on attempt %s"
                   % (run.get("conclusion"), run.get("run_attempt")), job, key or "")
    if state == "failed":
        return out(HOLD_NOTIFY, "guard-failed", "guard check did not succeed on the head sha %s" % sha[:7],
                   job, key or "")

    # 3. Re-check with trusted code from the default branch.
    prref = "refs/remotes/pr/%d" % n
    git_ok(ctx, ["fetch", "--no-tags", "origin", "+refs/pull/%d/head:%s" % (n, prref)], "fetching the PR head")
    if rev_parse(ctx, prref) != sha:
        return out(WAIT, "head-moved", "the PR head moved", job, key or "")
    mb = git_ok(ctx, ["merge-base", MAIN, prref], "finding the merge base").decode("ascii").strip()
    raw = git_ok(ctx, ["-c", "core.quotePath=false", "diff", "--name-status", "--no-renames", "-z", mb, prref],
                 "diffing the PR")
    entries = chk.parse_name_status_z(raw)
    errors = chk.evaluate(ref, title, (pr.get("base") or {}).get("ref"), "main", entries,
                          chk.make_blob_lookup(ctx.git, mb, prref),
                          chk.make_tree_lookup(ctx.git, mb, prref, MAIN),
                          chk.make_text_lookup(ctx.git, mb, prref))
    if errors is None or errors:
        first = errors[0] if errors else "not classified as a routine PR"
        more = " (+%d more)" % (len(errors) - 1) if errors and len(errors) > 1 else ""
        return out(HOLD_NOTIFY, "contract", "write contract: %s%s" % (first[:220], more), job, key or "")

    # 4. Class rules.
    adds = {p for s, p in entries if s == "A"}
    dels = {p for s, p in entries if s == "D"}
    mods = {p for s, p in entries if s == "M"}
    ctxd = {"ctx": ctx, "t": t, "job": job, "key": key, "date": date, "time": time_, "mb": mb, "prref": prref,
            "adds": adds, "dels": dels, "mods": mods, "title": title, "out": out}
    if job == "SWEEP":
        return _sweep_rules(ctxd)
    if job == "INTAKE":
        return _intake_rules(ctxd)
    return _analyse_review_rules(ctxd)


def _unexpected(d, allowed_adds, allowed_dels=()):
    """Paths outside the class's exact file set."""
    extra = sorted("A " + p for p in d["adds"] - set(allowed_adds))
    extra += sorted("D " + p for p in d["dels"] - set(allowed_dels))
    extra += sorted("M " + p for p in d["mods"])
    return extra


def _files_hold(d, extra, job, key):
    return d["out"](HOLD_NOTIFY, "unexpected-files", "files outside the %s set: %s%s"
                    % (job, ", ".join(extra[:3]), " (+%d more)" % (len(extra) - 3) if len(extra) > 3 else ""),
                    job, key or "")


def _row(d, path):
    text = show(d["ctx"], d["prref"], path)
    return text, front_matter(d["ctx"], text)


def sweep_zone_cells(ctx, text):
    """{key: Zone cell text} from a SWEEP row file's '## Portfolio table'."""
    sections = ctx.tool.sections_of(text or "")
    heading = next((h for h in sections if h.lower().startswith("portfolio table")), None)
    cells = {}
    for row in ctx.tool.table_rows(sections.get(heading, [])) if heading else []:
        col = next((c for c in row if c.startswith("zone")), None)
        cell_key = re.split(r"[\s(]", (row.get("ticker") or "").strip().strip("`"), 1)[0]
        if cell_key:
            cells[cell_key] = (row.get(col) or "") if col else ""
    return cells


def held_zone_changes(held, cells):
    """(problem, changes) for the held names against a SWEEP's Zone cells: a
    held name missing from the table, or a Zone cell without a zone word, is a
    problem (a contract defect, MODEL §8.7 item 10); otherwise the list of
    'KEY Portfolio → sweep' changes (J11: they merge and go to the digest)."""
    changes = []
    for k, entry in sorted(held.items()):
        if k not in cells:
            return "held %s is missing from the SWEEP portfolio table" % k, []
        m = ZONE_WORD_RE.match(cells[k])
        if not m:
            return "held %s: the Zone cell %r has no zone word" % (k, cells[k][:40]), []
        reg = ZONE_WORD_RE.match(entry["zone"] or "")
        if not reg or reg.group(1) != m.group(1):
            changes.append("%s %s → %s" % (k, entry["zone"] or "-", m.group(1)))
    return None, changes


def _sweep_rules(d):
    ctx, date, time_, out = d["ctx"], d["date"], d["time"], d["out"]
    row_path = "queue/rows/%s_%s_SWEEP.md" % (date, time_)
    run_path = "queue/runs/%s_%s_SWEEP.md" % (date, time_)
    extra = _unexpected(d, {row_path, run_path})
    if extra or row_path not in d["adds"] or run_path not in d["adds"]:
        return _files_hold(d, extra or ["missing " + row_path], "SWEEP", "")
    text, fm = _row(d, row_path)
    if fm.get("row_type") != "SWEEP":
        return _files_hold(d, ["row_type %r" % fm.get("row_type")], "SWEEP", "")
    if fm.get("pr_title") != d["title"]:
        return out(HOLD_NOTIFY, "mismatch", "row pr_title differs from the live title", "SWEEP")
    # J11 (MODEL §8.7 item 10): a held-zone change merges ("it's just register") and is
    # reported in the job summary and the morning digest; only a held name missing from
    # the portfolio table, or a Zone cell without a zone word, holds the PR.
    problem, changes = held_zone_changes(held_keys(ctx), sweep_zone_cells(ctx, text))
    if problem:
        return out(HOLD_NOTIFY, "held-missing", problem, "SWEEP")
    o = out(MERGE, "sweep", "SWEEP", "SWEEP")
    if changes:
        o.note = "held zone changes (digest): " + ", ".join(changes)
    return o


def _intake_rules(d):
    ctx, mb, out = d["ctx"], d["mb"], d["out"]
    rc, _ = ctx.git(["diff", "--quiet", "--no-ext-diff", mb, MAIN, "--"] + list(chk.INTAKE_BASE_PATHS))
    if rc not in (0, 1):
        raise AutomergeError("INTAKE base check failed (git rc %s)" % rc)
    if rc == 1:
        return out(HOLD, "intake-base", "INTAKE base moved on main since its merge base; the first INTAKE "
                   "that finds it over 20 h old supersedes it (F2)", "INTAKE")
    # A revert or an attended clean-up deletes rows, proposals or memos on main
    # (critique 7): this INTAKE may have applied a file that is gone. A REVIEW's
    # move memos/K/f -> archive/memos/K/f does not count: both sides are in the
    # pathspec, so git pairs the byte-identical move as an exact rename however
    # different the new memo is (DELETION_PATHS).
    deleted = git_ok(ctx, ["diff", "-M", "--diff-filter=D", "--name-only", mb, MAIN, "--"] + list(DELETION_PATHS),
                     "checking deletions on main").decode("utf-8", "replace").split()
    if deleted:
        return out(HOLD, "intake-base", "rows, proposals or memos were deleted on main since its base (%s); the "
                   "first INTAKE that finds it over 20 h old supersedes it (F2)" % deleted[0], "INTAKE")
    return out(MERGE, "intake", "INTAKE", "INTAKE")


def _analyse_review_rules(d):
    ctx, t, job, key, date, time_, mb, out = (d["ctx"], d["t"], d["job"], d["key"], d["date"], d["time"],
                                               d["mb"], d["out"])
    kind = t["kind"]
    run_path = "queue/runs/%s_%s_%s%s.md" % (date, time_, job, "_" + key if key else "")
    if kind == "exhausted":
        row_path = "queue/rows/%s_%s_ANALYSE.md" % (date, time_)
        extra = _unexpected(d, {run_path, row_path})
        if extra or run_path not in d["adds"]:
            return _files_hold(d, extra or ["missing " + run_path], job, "")
        if row_path in d["adds"] and _row(d, row_path)[1].get("row_type") != "QUEUE":
            return _files_hold(d, ["row_type of " + row_path], job, "")
        return out(MERGE, "exhausted", "queue exhausted", job)

    # Key moved on main since the merge base (critique 2): another memo or row
    # for this key landed, so a clean squash could break the one-memo rule.
    rc, _ = ctx.git(["diff", "--quiet", "--no-ext-diff", mb, MAIN, "--", "memos/%s" % key, "archive/memos/%s" % key])
    if rc not in (0, 1):
        raise AutomergeError("key check failed (git rc %s)" % rc)
    added_rows = git_ok(ctx, ["log", "--format=", "--name-only", "--diff-filter=A", "%s..%s" % (mb, MAIN), "--",
                              "queue/rows/"], "listing rows added on main").decode("utf-8", "replace").split()
    row_re = re.compile(r"queue/rows/\d{4}-\d{2}-\d{2}_\d{4}_[A-Z]+_%s\.md" % re.escape(key))
    if rc == 1 or any(row_re.fullmatch(p) for p in added_rows):
        return out(HOLD_NOTIFY, "key-moved-on-main", "a memo or row for %s landed on main after this PR's base"
                   % key, job, key)

    memo_adds = sorted(p for p in d["adds"] if p.startswith("memos/"))
    for memo in memo_adds:
        m = chk.MEMO_RE.fullmatch(memo)
        if not m or m.group("key") != key or m.group("dir") != key:
            return out(HOLD_NOTIFY, "rekey", "memo %s is not under the branch key %s (re-key)" % (memo, key), job, key)
    row_path = "queue/rows/%s_%s_%s_%s.md" % (date, time_, job, key)
    row_text, row = _row(d, row_path)
    if row_path not in d["adds"] or not row:
        return _files_hold(d, ["missing " + row_path], job, key)
    if row.get("pr_title") != d["title"]:
        return out(HOLD_NOTIFY, "mismatch", "row pr_title differs from the live title", job, key)
    held = (t["held"] or (row.get("held") or "").strip().lower() == "true" or key in held_keys(ctx))
    evidence = {p for p in d["dels"] if re.fullmatch(r"queue/evidence/%s_[^/]+\.md" % re.escape(key), p)}

    if kind in ("incomplete", "prior"):
        want_type = "INCOMPLETE" if kind == "incomplete" else "PRIOR"
        allowed = {row_path, run_path}
        if kind == "incomplete":
            allowed.add("queue/evidence/%s_%s_INCOMPLETE.md" % (key, date))
        extra = _unexpected(d, allowed)
        if extra or not allowed <= d["adds"]:
            return _files_hold(d, extra or ["missing " + ", ".join(sorted(allowed - d["adds"]))], job, key)
        if row.get("row_type") != want_type:
            return out(HOLD_NOTIFY, "mismatch", "row_type %s, title says %s" % (row.get("row_type"), want_type),
                       job, key)
        if held:
            return out(HOLD_NOTIFY, "held", "held name %s (%s)" % (key, kind), job, key)
        return out(MERGE, kind, kind, job, key)

    # Verdict outcome.
    if len(memo_adds) != 1:
        return out(HOLD_NOTIFY, "mismatch", "a verdict title needs exactly one new memo (found %d)" % len(memo_adds),
                   job, key)
    memo = memo_adds[0]
    fm = front_matter(ctx, show(ctx, d["prref"], memo))
    memo_v = verdict_word(ctx, fm.get("verdict"))
    cell_v = row_verdict_cell(ctx, row_text)
    if row.get("row_type") != job or not (memo_v == t["verdict"] == cell_v):
        return out(HOLD_NOTIFY, "mismatch", "verdicts differ: title %s, memo %s, row %s"
                   % (t["verdict"], memo_v or "?", cell_v or "?"), job, key)
    if held or ctx.tool.first_token(fm.get("position") or "") == "HELD":
        return out(HOLD_NOTIFY, "held", "held name %s: %s" % (key, memo_v), job, key)
    if memo_v == "BUY":
        return out(HOLD_NOTIFY, "buy", "BUY %s" % key, job, key)
    allowed_adds = {memo, row_path, run_path}
    allowed_dels = set(evidence)
    if job == "REVIEW":
        priors = sorted(p for p in d["dels"] if p.startswith("memos/%s/" % key))
        if len(priors) != 1 or "archive/" + priors[0] not in d["adds"]:
            return _files_hold(d, ["the prior-memo move pair"], job, key)
        allowed_adds.add("archive/" + priors[0])
        allowed_dels.add(priors[0])
        prior_v = verdict_word(ctx, front_matter(ctx, show(ctx, mb, priors[0])).get("verdict"))
        if prior_v is None:
            prior_v = (register_rows(ctx, mb).get(key) or {}).get("verdict")
            prior_v = verdict_word(ctx, prior_v) if prior_v else None
        if prior_v is None:
            return out(HOLD_NOTIFY, "prior-unknown", "prior verdict of %s unknown" % key, job, key)
        if prior_v != memo_v:
            return out(HOLD_NOTIFY, "verdict-change", "verdict changed %s → %s" % (prior_v, memo_v), job, key)
        if t["old"] is not None:
            return out(HOLD_NOTIFY, "mismatch", "title says 'was %s' but the verdict is unchanged" % t["old"], job, key)
    extra = _unexpected(d, allowed_adds, allowed_dels)
    if extra:
        return _files_hold(d, extra, job, key)
    return out(MERGE, "verdict", "%s %s" % (job, memo_v), job, key)


# ---------------------------------------------------------------- act

def notify(ctx, pr, outcome):
    """One needs-Jakub comment per (PR, head sha, reason); none in mode off."""
    if ctx.mode == "off":
        return False
    n = int(pr["number"])
    sha7 = (outcome.sha or "0000000")[:7]
    marker = "<!-- gsc-hold pr=%d sha=%s code=%s -->" % (n, sha7, outcome.code)
    body = "@jakubhoryna PR %d held - %s\n%s\nOpen: %s\n%s" % (
        n, gsc_gh.no_hash_ref(outcome.text), gsc_gh.no_hash_ref(outcome.title or pr.get("title") or ""),
        gsc_gh.search_link(ctx.repo, n), marker)
    return gsc_gh.post_needs_comment(ctx.gh, body, marker, pr.get("created_at"))


def merge(ctx, pr, outcome):
    """Squash-merge pinned to outcome.sha (mode on only). Returns the final outcome."""
    n = int(pr["number"])
    title = "%s (#%d)" % (outcome.title, n)
    for attempt in (1, 2):
        # Re-read the PR just before each PUT: a '[fixing]' retitle or a push
        # since decide() read it means the next guard event decides again.
        live = ctx.gh.get("pulls/%d" % n) or {}
        if (live.get("state") != "open" or (live.get("head") or {}).get("sha") != outcome.sha
                or (live.get("title") or "") != outcome.title):
            return Outcome(WAIT, "head-moved", "title, head or state changed before the merge; the next event "
                           "decides", outcome.sha, outcome.title, outcome.job, outcome.key)
        try:
            ctx.gh.merge(n, outcome.sha, title)
            return Outcome("MERGED", outcome.code, "merged at %s" % outcome.sha[:7], outcome.sha, outcome.title,
                           outcome.job, outcome.key, outcome.note)
        except gsc_gh.GhError as exc:
            if exc.status in (405, 409):
                live = ctx.gh.get("pulls/%d" % n)
                if live.get("state") != "open" or (live.get("head") or {}).get("sha") != outcome.sha:
                    return Outcome(WAIT, "head-moved", "head moved or PR closed during the merge", outcome.sha,
                                   outcome.title, outcome.job, outcome.key)
                if live.get("mergeable") is False:
                    return Outcome(HOLD_NOTIFY, "merge-refused", "GitHub refused the merge (HTTP %s: %s); it does "
                                   "not merge cleanly" % (exc.status, exc.message), outcome.sha, outcome.title,
                                   outcome.job, outcome.key)
                if attempt == 1:
                    ctx.sleep(10)
                    continue
                return Outcome(WAIT, "merge-retry", "GitHub refused the merge twice (HTTP %s) while mergeability was "
                               "being computed; the next event retries" % exc.status, outcome.sha, outcome.title,
                               outcome.job, outcome.key)
            return Outcome(HOLD_NOTIFY, "merge-refused", "GitHub refused the merge (HTTP %s: %s)"
                           % (exc.status, exc.message), outcome.sha, outcome.title, outcome.job, outcome.key)


def candidates(ctx, only_branch=None):
    prs = [pr for pr in ctx.gh.get_all("pulls?state=open&base=main&per_page=100")
           if gsc_gh.routine_kind(pr) is not None]

    def order(pr):
        m = TITLE_RE.match(pr.get("title") or "")
        job = m.group("job") if m else "SEED"
        return (JOB_ORDER.get(job, 5), int(pr["number"]))
    prs.sort(key=order)
    if not only_branch:
        return prs, []
    first = [pr for pr in prs if (pr.get("head") or {}).get("ref") == only_branch]
    return first, [pr for pr in prs if pr not in first]


def _parse_time(value):
    try:
        return datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc)
    except (TypeError, ValueError):
        return None


def sweep(ctx, only_branch=None, clock=time.monotonic):
    """Decide and act on open routine PRs; returns [(pr, outcome)]."""
    start = clock()
    first, rest = candidates(ctx, only_branch)
    results = []
    recent = ctx.now() - RECENT
    for pr in first + rest:
        if pr in rest:
            updated = _parse_time(pr.get("updated_at"))
            if clock() - start > BUDGET or updated is None or updated < recent:
                continue
        try:
            outcome = decide(ctx, pr)
            if outcome.kind == MERGE:
                if ctx.mode == "on":
                    outcome = merge(ctx, pr, outcome)
                else:
                    outcome = Outcome(MERGE, outcome.code, "%s: would merge at %s" % (ctx.mode, outcome.sha[:7]),
                                      outcome.sha, outcome.title, outcome.job, outcome.key, outcome.note)
        except Exception as exc:  # fail closed for this PR, carry on with the others
            outcome = Outcome(HOLD_NOTIFY, "automerge-exception", "gsc-automerge could not evaluate it (%s)"
                              % type(exc).__name__, (pr.get("head") or {}).get("sha") or "", pr.get("title") or "")
        if outcome.kind == HOLD_NOTIFY:
            try:
                notify(ctx, pr, outcome)
            except Exception as exc:
                ctx.log("PR %s: needs-Jakub comment failed (%s)" % (pr["number"], type(exc).__name__))
        ctx.log("PR %s: %s %s - %s" % (pr["number"], outcome.kind, outcome.code, outcome.text))
        results.append((pr, outcome))
        if outcome.kind == "MERGED":
            fetch_main(ctx)
    return results


def summary(results, mode):
    lines = ["## gsc-automerge (%s)" % mode, "", "| PR | Class | Outcome | Reason |", "|---|---|---|---|"]
    for pr, o in results:
        cls = ("%s %s" % (o.job, o.key)).strip() or "-"
        reason = "%s: %s%s" % (o.code, o.text, ("; " + o.note) if getattr(o, "note", "") else "")
        lines.append("| PR %s | %s | %s | %s |" % (pr["number"], cls, o.kind, reason.replace("|", "/")))
    if not results:
        lines.append("| - | - | - | no open routine PR to decide |")
    return "\n".join(lines) + "\n"


def main(env=None, gh=None, git=None, sleep=None, now=None, clock=time.monotonic):
    env = os.environ if env is None else env
    mode = read_mode(env.get("GSC_AUTOMERGE"))
    repo = env.get("REPO", "")
    gh = gh or gsc_gh.Gh(env.get("GH_TOKEN", ""), repo, allow_merge=True)
    ctx = Ctx(gh, git=git, repo=repo, mode=mode, now=now, sleep=sleep)
    only = (env.get("TRIGGER_BRANCH") or "").strip() if env.get("EVENT_NAME") == "workflow_run" else ""
    ctx.log("mode %s, %s" % (mode, "triggered by branch " + only if only else "full sweep"))
    try:
        if ctx.tool is None:
            raise AutomergeError("cannot load routines/tools/gsc_register.py")
        fetch_main(ctx)
        results = sweep(ctx, only or None, clock)
    except Exception as exc:  # no merges past this point; tell Jakub once a day
        ctx.log("failed: %s" % type(exc).__name__)
        if mode != "off":
            try:
                local = ctx.now().astimezone(gsc_gh.prague_tz())
                day = local.strftime("%Y-%m-%d")
                start = local.replace(hour=0, minute=0, second=0, microsecond=0).astimezone(datetime.timezone.utc)
                marker = "<!-- gsc-hold pr=0 sha=0000000 code=automerge-error-%s -->" % day
                gsc_gh.post_needs_comment(gh, "@jakubhoryna gsc-automerge failed: %s\n%s"
                                          % (type(exc).__name__, marker), marker,
                                          start.strftime("%Y-%m-%dT%H:%M:%SZ"))
            except Exception:
                pass
        return 1
    path = env.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(summary(results, mode))
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(errors="backslashreplace")
    except AttributeError:
        pass
    sys.exit(main())
