#!/usr/bin/env python3
"""Plain-Python tests for gsc_automerge.py and gsc_gh.py (no pytest, no network).

A throwaway git repo stands in for the workflow's checkout: `main` holds a
small register (written by routines/tools/gsc_register.py), memos, the queue
and the archive; each PR is a commit built with git plumbing and published as
refs/pull/{n}/head. `git fetch` is intercepted and turned into update-ref, so
the classifier runs its real git commands, and the trusted checker
(gsc_guard_check.evaluate) runs for real. GitHub is a fake transport that
records every call.

Run:  python3 .github/workflows/test_gsc_automerge.py
Prints one PASS/FAIL line per case; the exit code is the number of failures.
test_gsc_notify.py imports the fixtures below.
"""
import datetime
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import urllib.parse

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gsc_automerge as am  # noqa: E402
import gsc_gh  # noqa: E402
import gsc_guard_check as chk  # noqa: E402

try:
    sys.stdout.reconfigure(errors="backslashreplace")
except AttributeError:
    pass

TOOL = chk.register_tool()
if TOOL is None:
    raise SystemExit("cannot load routines/tools/gsc_register.py")

REPO = "jakubhoryna/Value-Investing-Model"
NOW = datetime.datetime(2026, 10, 6, 6, 40, tzinfo=datetime.timezone.utc)
D = "2026-10-06"
RESULTS = []


def record(name, ok, detail=""):
    RESULTS.append(ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("" if ok or not detail else "  -- " + str(detail)[:400]))


# ---------------------------------------------------------------- content

def memo_text(key, verdict, date, past="ADEQUATE", future="ADEQUATE", sf="PASS", position="—",
              past_reason="20% ROCE", future_reason="n.m.", sf_reason="n.m.", px="110", trigger="100",
              summary=None, version="v1"):
    summary = summary or "%s is a %s: the gates hold and the price sits above the band. More detail follows." % (
        key, verdict)
    return ("---\nticker: %s\ncompany: Company %s\nmemo_date: %s\nmemo_version: %s\nverdict: %s\n"
            "quality_past: %s\nquality_future: %s\nsf: %s\npast_reason: %s\nfuture_reason: %s\nsf_reason: %s\n"
            "px: %s\npx_unit: USD\ntrigger: %s\nposition: %s\n---\n\n# %s — Company %s: GSC Memo\n\n"
            "## 1. Verdict\n\n%s\n\n## 2. Understanding\n\nText.\n\n*Framework output, not investment advice.*\n"
            % (key, key, date, version, verdict, past, future, sf, past_reason, future_reason, sf_reason, px,
               trigger, position, key, key, summary))


def row_text(job, key, title, verdict=None, row_type=None, held="false", date=D, memo=None):
    """A row file whose tables are the register tool's row-from-memo --table
    print for its memo (v4.5.2 lint-row), with the Verdict cell set to
    `verdict` (a differing cell is a mismatch fixture)."""
    memo_path = "memos/%s/%s_%s_GSC.md" % (key, key, date)
    lines = ["---", "row_type: %s" % (row_type or job), "key: %s" % key, "company: Company %s" % key,
             "isin: n/a", "memo_path: %s" % memo_path, "run_date: %s" % date,
             "run_time: %s" % {"ANALYSE": "2130", "REVIEW": "0610"}[job],
             "held: %s" % held, "pr_title: %s" % title, "---", "## Register row (new)"]
    if verdict:
        row = TOOL.row_from_memo(memo_path, memo or memo_text(key, verdict, date), [])
        cells = TOOL.master_cells(row)
        cells[TOOL.MASTER_COLUMNS.index("Verdict")] = verdict
        lines += [TOOL.table_line(TOOL.MASTER_COLUMNS), "|" + "---|" * len(TOOL.MASTER_COLUMNS),
                  TOOL.table_line(cells)]
        if row["held"] == "true":
            lines += ["## Portfolio row", TOOL.table_line(TOOL.PORTFOLIO_COLUMNS),
                      "|" + "---|" * len(TOOL.PORTFOLIO_COLUMNS), TOOL.table_line(TOOL.portfolio_cells(row))]
    else:
        lines.append("none")
    lines += ["## Queue update", "none", "## TODO additions", "none", ""]
    return "\n".join(lines)


def reg_row(key, verdict, past="ADEQUATE", future="ADEQUATE", sf="PASS", px="110", trigger="100", held=False,
            zone="n.m.", memo_date="2026-09-01"):
    nm, owed = "n.m.", "-"
    gates = TOOL.gates_failed(past, future, sf)
    row = {name: owed for name in TOOL.CSV_HEADER}
    row.update(TOOL.LENS_DEFAULTS)
    row.update(TOOL.R10_DEFAULTS)
    row["trigger_basis"] = "no-cash"            # a v4.5.0 row prints the no-cash bound (round 2, R10)
    row.update({
        "key": key, "company": "Company %s" % key, "aliases": nm, "verdict": verdict, "gates_failed": str(gates),
        "section": TOOL.section_for(verdict, gates), "past": past, "future": future, "sf": sf,
        "past_reason": "20% ROCE" if past != "WEAK" else "ROCE decline",
        "future_reason": "breadth" if future == "WEAK" else nm, "sf_reason": "buybacks" if sf == "FAIL" else nm,
        "memo_path": "memos/%s/%s_%s_GSC.md" % (key, key, memo_date), "memo_date": memo_date,
        "memo_version": "v1", "model_version": "v4.5.0", "px": px, "px_unit": "USD", "px_date": "2026-10-02",
        "px_source": "memo", "trigger": trigger, "next_review_short": "Nov 2026",
        "held": "true" if held else "false", "zone": zone if held else nm,
        "add_band": nm, "sell_line": nm, "last_zone_check": "2026-10-02" if held else nm,
        "avg_cost": "10 USD" if held else nm, "core_source": owed,
    })
    if verdict == "DNAF":
        row.update({"past": nm, "future": nm, "sf": nm, "past_reason": nm, "gates_failed": "0",
                    "section": "DNAF", "trigger": nm, "next_review_short": nm})
    problems = TOOL.validate_row(row)
    if problems:
        raise SystemExit("bad fixture row %s: %s" % (key, problems))
    return row


REG_ROWS = [
    reg_row("HLD", "WATCH", held=True, zone="HOLD", memo_date="2026-08-01"),
    reg_row("HLX", "AVOID", future="WEAK", sf="FAIL", held=True, zone="SELL-FLAG SR2", memo_date="2026-08-02"),
    reg_row("WAT1", "WATCH", px="110", trigger="100", memo_date="2026-09-05"),
    reg_row("WAT2", "WATCH", px="95", trigger="100", memo_date="2026-09-06"),
    reg_row("WAT3", "WATCH", px="-", trigger="n.m.", memo_date="2026-09-07"),
    reg_row("REV", "WATCH", memo_date="2026-09-01"),
    reg_row("AVO", "AVOID", past="WEAK", memo_date="2026-09-02"),
    reg_row("DNF", "DNAF", memo_date="2026-09-03"),
]


def register_files(rows, version, date):
    csv_text = TOOL.csv_text(rows)
    parsed, _ = TOOL.read_csv_text(csv_text)
    return csv_text, TOOL.render(parsed, version, date)


REG_CSV, REG_MD = register_files(REG_ROWS, "v1", "2026-10-05")
TODO = ("# GSC Work Queue — TODO.md (v41 · 2026-10-06)\n\n## ▶ Review requests (SWEEP)\n\n## ▶ IDEAS candidates "
        "(attended triage)\n\n## ▶ Open items (register)\n\n*Rule line.*\n\n- **HLX (held) SELL-FLAG** — decision "
        "pending.\n- **ABB — pending re-key** — user call.\n\n## ▶ Routed by INTAKE 2026-10-05\n\n- `X` — item\n")
BASE_FILES = {
    "register.csv": REG_CSV,
    "_REGISTER.md": REG_MD,
    "model/MODEL.md": "---\nmodel_version: v4.5.0\n---\n# MODEL\n",
    "queue/TODO.md": TODO,
    "queue/DRAFT_QUEUE.md": "# DRAFT_QUEUE (v6 · 2026-10-06)\n- [ ] NEW — New Co\n",
    "queue/rows/README.md": "rows\n",
    "queue/rows/2026-10-05_2139_ANALYSE_OLD.md": "---\nrow_type: ANALYSE\n---\n",
    "queue/evidence/NEW_draft-evidence_2026-09-01.md": "evidence\n",
    "archive/registers/2026/REGISTER_v0_2026-10-01.md": "old\n",
    "archive/queue/TODO_v40_2026-10-05.md": "old\n",
    "archive/memos/REV/REV_2026-06-01_GSC.md": memo_text("REV", "WATCH", "2026-06-01"),
    "memos/HLD/HLD_2026-08-01_GSC.md": memo_text("HLD", "WATCH", "2026-08-01", position="HELD"),
    "memos/HLX/HLX_2026-08-02_GSC.md": memo_text("HLX", "AVOID", "2026-08-02", position="HELD"),
    "memos/WAT1/WAT1_2026-09-05_GSC.md": memo_text("WAT1", "WATCH", "2026-09-05"),
    "memos/REV/REV_2026-09-01_GSC.md": memo_text("REV", "WATCH", "2026-09-01", version="v2"),
    "memos/AVO/AVO_2026-09-02_GSC.md": memo_text("AVO", "AVOID", "2026-09-02", past="WEAK"),
    "memos/BUYK/BUYK_2026-09-04_GSC.md": memo_text("BUYK", "BUY", "2026-09-04"),
    "memos/PRU/PRU_2026-09-03_GSC.md": memo_text("PRU", "pending", "2026-09-03"),
}


# ---------------------------------------------------------------- git fixture

def remove_tree(path):
    def make_writable(func, p, _exc):
        os.chmod(p, stat.S_IWRITE)
        func(p)
    try:
        shutil.rmtree(path, onerror=make_writable)
    except OSError:
        pass


class Repo:
    """A bare-bones clone: main, refs/remotes/origin/main and refs/pull/{n}/head."""

    def __init__(self, files=None):
        self.path = tempfile.mkdtemp(prefix="gsc_automerge_test_")
        self.index = os.path.join(self.path, "fixture.index")
        self.git("init", "-q")
        self.git("config", "core.autocrlf", "false")
        self.main = self.commit(None, files or BASE_FILES, "GSC: fixture main", "2026-09-30T00:00:00Z")
        self.set_main(self.main)
        self.calls = []

    def git(self, *args, data=None, env=None):
        proc = subprocess.run(["git", "-C", self.path] + list(args), input=data, capture_output=True,
                              env=env, check=False)
        if proc.returncode != 0:
            raise RuntimeError("git %s failed: %s" % (" ".join(args), proc.stderr.decode("utf-8", "replace")))
        return proc.stdout.decode("utf-8", "replace").strip()

    def commit(self, parent, changes, message="GSC: fixture", date="2026-10-06T05:00:00Z"):
        env = dict(os.environ, GIT_INDEX_FILE=self.index, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@example.com",
                   GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@example.com", GIT_AUTHOR_DATE=date,
                   GIT_COMMITTER_DATE=date)
        if parent:
            self.git("read-tree", parent, env=env)
        else:
            self.git("read-tree", "--empty", env=env)
        for path, content in changes.items():
            if content is None:
                self.git("update-index", "--force-remove", "--", path, env=env)
            else:
                blob = self.git("hash-object", "-w", "--stdin", data=content.encode("utf-8"))
                self.git("update-index", "--add", "--cacheinfo", "100644,%s,%s" % (blob, path), env=env)
        tree = self.git("write-tree", env=env)
        args = ["commit-tree", tree, "-m", message] + (["-p", parent] if parent else [])
        return self.git(*args, env=env)

    def set_main(self, sha):
        """Move main and, as a fetch would, refs/remotes/origin/main."""
        self.git("update-ref", "refs/heads/main", sha)
        self.git("update-ref", am.MAIN, sha)
        self.main = sha

    def advance_main(self, changes, message="GSC: moved main (#99)", date="2026-10-06T06:00:00Z"):
        self.set_main(self.commit(self.main, changes, message, date))
        return self.main

    def runner(self):
        """git(args) -> (rc, stdout) for the classifier; fetch becomes update-ref."""
        def run(args):
            args = list(args)
            self.calls.append(args)
            if args and args[0] == "fetch":
                src, dst = args[-1].lstrip("+").split(":", 1)
                if src == "refs/heads/main":
                    src = "refs/heads/main"
                proc = subprocess.run(["git", "-C", self.path, "rev-parse", "--verify", "--quiet", src],
                                      capture_output=True, check=False)
                if proc.returncode != 0:
                    return 128, b""
                subprocess.run(["git", "-C", self.path, "update-ref", dst, proc.stdout.decode().strip()],
                               capture_output=True, check=True)
                return 0, b""
            proc = subprocess.run(["git", "-C", self.path] + args, capture_output=True, check=False)
            return proc.returncode, proc.stdout
        return run

    def close(self):
        remove_tree(self.path)


# ---------------------------------------------------------------- fake GitHub

def iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


class FakeGitHub:
    """Transport for gsc_gh.Gh: answers the allowlisted REST calls from memory."""

    def __init__(self):
        self.prs, self.issues, self.comments = {}, {}, {}
        self.runs = {"gsc-guard.yml": [], "gsc-automerge.yml": [], "gsc-notify.yml": []}
        self.jobs, self.run_by_id = {}, {}
        self.calls, self.merge_script, self.after_merge_call = [], {}, {}
        self.fail_get = set()
        self.next_id = 5000
        self.reruns, self.dispatches = [], []
        self.now = NOW

    # -- setup
    def add_run(self, sha, conclusion="success", status="completed", attempt=1, created="2026-10-06T05:10:00Z",
                job_conclusion="same", with_job=True, workflow="gsc-guard.yml", started=None, updated=None,
                event=None):
        self.next_id += 1
        event = event or ("pull_request_target" if workflow == "gsc-guard.yml" else "workflow_run")
        run = {"id": self.next_id, "status": status, "conclusion": conclusion if status == "completed" else None,
               "run_attempt": attempt, "created_at": created, "head_sha": sha, "event": event,
               "run_started_at": started or created, "updated_at": updated or created}
        self.runs[workflow].append(run)
        self.run_by_id[run["id"]] = run
        jc = run["conclusion"] if job_conclusion == "same" else job_conclusion
        self.jobs[run["id"]] = [{"name": "guard", "conclusion": jc}] if with_job else []
        return run

    def add_issue(self, title, state="open", login=gsc_gh.BOT, created="2026-10-05T06:31:00Z", pr=False):
        number = 900 + len(self.issues)
        issue = {"number": number, "title": title, "state": state, "user": {"login": login}, "created_at": created,
                 "body": ""}
        if pr:
            issue["pull_request"] = {}
        self.issues[number] = issue
        self.comments.setdefault(number, [])
        return issue

    # -- transport
    def __call__(self, method, url, headers, body):
        prefix = gsc_gh.API + "repos/%s/" % REPO
        if not url.startswith(prefix):
            raise AssertionError("request outside the repo: %s" % url)
        rel = url[len(prefix):]
        path, _, query = rel.partition("?")
        q = dict(urllib.parse.parse_qsl(query))
        data = json.loads(body.decode("utf-8")) if body else None
        self.calls.append((method, path, data))
        status, payload = self.route(method, path, q, data)
        return status, {}, (json.dumps(payload).encode("utf-8") if payload is not None else b"")

    def route(self, method, path, q, data):
        parts = path.split("/")
        if method == "GET" and path in self.fail_get:
            return 500, {"message": "boom"}
        if method == "GET" and path == "pulls":
            prs = list(self.prs.values())
            if q.get("state") == "open":
                prs = [p for p in prs if p["state"] == "open"]
            if q.get("sort") == "updated":
                prs.sort(key=lambda p: p.get("updated_at", ""), reverse=True)
            return 200, prs
        if method == "GET" and parts[0] == "pulls" and len(parts) == 2:
            pr = self.prs.get(int(parts[1]))
            return (200, pr) if pr else (404, {"message": "Not Found"})
        if method == "PUT" and parts[0] == "pulls" and parts[2:] == ["merge"]:
            n = int(parts[1])
            script = self.merge_script.get(n) or []
            status, message = script.pop(0) if script else (200, "merged")
            if n in self.after_merge_call:
                self.after_merge_call[n]()
            if status == 200:
                self.prs[n]["state"] = "closed"
                self.prs[n]["merged"] = True
                return 200, {"merged": True, "sha": "f" * 40}
            return status, {"message": message}
        if method == "GET" and parts[:2] == ["actions", "workflows"] and parts[3:] == ["runs"]:
            runs = list(self.runs.get(parts[2], []))
            if "event" in q:
                runs = [r for r in runs if r["event"] == q["event"]]
            if "head_sha" in q:
                runs = [r for r in runs if r["head_sha"] == q["head_sha"]]
            if "created" in q:
                since = q["created"].lstrip(">=")
                runs = [r for r in runs if r["created_at"] >= since]
            return 200, {"total_count": len(runs), "workflow_runs": runs}
        if method == "GET" and path == "actions/runs":
            runs = [r for wf in self.runs.values() for r in wf]
            if "created" in q:
                since = q["created"].lstrip(">=")
                runs = [r for r in runs if r["created_at"] >= since]
            return 200, {"total_count": len(runs), "workflow_runs": runs}
        if method == "GET" and parts[:2] == ["actions", "runs"] and len(parts) == 4 and parts[3] == "jobs":
            return 200, {"jobs": self.jobs.get(int(parts[2]), [])}
        if method == "GET" and parts[:2] == ["actions", "runs"] and len(parts) == 3:
            run = self.run_by_id[int(parts[2])]
            if run["status"] == "in_progress":       # one poll later it is done
                run["status"], run["conclusion"] = "completed", "success"
                self.jobs[run["id"]] = [{"name": "guard", "conclusion": "success"}]
                return 200, dict(run, status="in_progress", conclusion=None)
            return 200, run
        if method == "POST" and parts[:2] == ["actions", "runs"] and parts[3:] == ["rerun"]:
            run = self.run_by_id[int(parts[2])]
            run["status"], run["conclusion"], run["run_attempt"] = "in_progress", None, run["run_attempt"] + 1
            self.reruns.append(run["id"])
            return 201, {}
        if method == "POST" and path == "actions/workflows/gsc-automerge.yml/dispatches":
            self.dispatches.append(data)
            self.add_run("d" * 40, workflow="gsc-automerge.yml", event="workflow_dispatch", created=iso(self.now))
            return 204, None
        if method == "GET" and path == "issues":
            issues = list(self.issues.values())
            if q.get("state", "open") != "all":
                issues = [i for i in issues if i["state"] == q.get("state", "open")]
            if q.get("creator"):
                issues = [i for i in issues if i["user"]["login"] == q["creator"]]
            issues.sort(key=lambda i: i["created_at"], reverse=True)
            return 200, issues
        if parts[0] == "issues" and len(parts) == 2 and method == "GET":
            issue = self.issues.get(int(parts[1]))
            return (200, issue) if issue else (404, {"message": "Not Found"})
        if parts[0] == "issues" and len(parts) == 2 and method == "PATCH":
            self.issues[int(parts[1])].update(data)
            return 200, self.issues[int(parts[1])]
        if method == "POST" and path == "issues":
            number = 900 + len(self.issues)
            issue = {"number": number, "title": data["title"], "body": data.get("body", ""), "state": "open",
                     "user": {"login": gsc_gh.BOT}, "created_at": iso(self.now), "assignees": data.get("assignees")}
            self.issues[number] = issue
            self.comments[number] = []
            return 201, issue
        if parts[0] == "issues" and parts[2:] == ["comments"]:
            number = int(parts[1])
            if method == "GET":
                since = q.get("since", "")
                return 200, [c for c in self.comments.get(number, []) if c["updated_at"] >= since]
            if method == "POST":
                comment = {"id": len(self.calls), "body": data["body"], "created_at": iso(self.now),
                           "updated_at": iso(self.now)}
                self.comments.setdefault(number, []).append(comment)
                return 201, comment
        raise AssertionError("unexpected call %s %s" % (method, path))

    # -- views
    def puts(self):
        return [(p, d) for m, p, d in self.calls if m == "PUT"]

    def posted_comments(self):
        return [d["body"] for m, p, d in self.calls if m == "POST" and p.endswith("/comments")]


class Fixture:
    def __init__(self, files=None, mode="on"):
        self.repo = Repo(files)
        self.gh = FakeGitHub()
        self.client = gsc_gh.Gh("t0ken", REPO, transport=self.gh, allow_merge=True, allow_actions=True)
        self.slept = []
        self.ctx = am.Ctx(self.client, git=self.repo.runner(), repo=REPO, mode=mode, now=lambda: NOW,
                          sleep=self.slept.append, log=lambda line: None)
        self.needs = self.gh.add_issue(gsc_gh.NEEDS_TITLE, created="2026-10-01T05:40:00Z")

    def pr(self, n, branch, title, changes, guard="success", base=None, created="2026-10-06T05:00:00Z",
           updated=None, repo_name=REPO, base_ref="main"):
        sha = self.repo.commit(base or self.repo.main, changes, "%s (PR %d)" % (title, n))   # one sha per PR
        self.repo.git("update-ref", "refs/pull/%d/head" % n, sha)
        pr = {"number": n, "state": "open", "title": title, "mergeable": True,
              "head": {"ref": branch, "sha": sha, "repo": {"full_name": repo_name}},
              "base": {"ref": base_ref, "repo": {"full_name": REPO}},
              "created_at": created, "updated_at": updated or created}
        self.gh.prs[n] = pr
        if guard:
            self.gh.add_run(sha, conclusion=guard)
        return pr

    def decide(self, pr):
        return am.decide(self.ctx, pr)

    def close(self):
        self.repo.close()


# ---------------------------------------------------------------- PR builders

def analyse_changes(key="NEW", verdict="WATCH", title=None, time_="2130", memo_verdict=None, cell=None,
                    row_held="false", position="—", row_type=None, extra=None, row_title=None):
    title = title or "GSC ANALYSE %s %s — %s (Cheapness)" % (key, D, verdict)
    memo = memo_text(key, memo_verdict or verdict, D, position=position)
    changes = {
        "memos/%s/%s_%s_GSC.md" % (key, key, D): memo,
        "queue/rows/%s_%s_ANALYSE_%s.md" % (D, time_, key): row_text("ANALYSE", key, row_title or title,
                                                                      cell or verdict, row_type, row_held,
                                                                      memo=memo),
        "queue/runs/%s_%s_ANALYSE_%s.md" % (D, time_, key): "run note\n",
    }
    changes.update(extra or {})
    return title, changes


def review_changes(key="REV", prior="2026-09-01", verdict="WATCH", moved="band unchanged", gate="", held_prefix=False,
                   time_="0610", memo_verdict=None, extra=None, position="—", row_held="false", move=True):
    title = "%sGSC REVIEW %s %s — %s%s; %s" % ("HELD · " if held_prefix else "", key, D, verdict,
                                              " (%s)" % gate if gate else "", moved)
    prior_path = "memos/%s/%s_%s_GSC.md" % (key, key, prior)
    memo = memo_text(key, memo_verdict or verdict, D, position=position, version="v3")
    changes = {
        "memos/%s/%s_%s_GSC.md" % (key, key, D): memo,
        "queue/rows/%s_%s_REVIEW_%s.md" % (D, time_, key): row_text("REVIEW", key, title, verdict, held=row_held,
                                                                     memo=memo),
        "queue/runs/%s_%s_REVIEW_%s.md" % (D, time_, key): "run note\n",
    }
    if move:
        changes[prior_path] = None
        changes["archive/" + prior_path] = BASE_FILES[prior_path]
    changes.update(extra or {})
    return title, changes


def sweep_changes(zones=None, title=None, time_="0630"):
    zones = zones if zones is not None else {"HLD": "HOLD", "HLX": "SELL-FLAG (SR2) — unchanged"}
    title = title or "GSC SWEEP %s — 5/5 priced · 0 in range · 0 stale" % D
    table = ["## Portfolio table", "", "| Ticker | Avg cost | Current | Zone (ADD / HOLD / SELL-FLAG) | Distance to "
             "ADD band | Distance to sell-flag line |", "|---|---|---|---|---|---|"]
    table += ["| %s | $10 | $11 | %s | n.m. | n.m. |" % (k, z) for k, z in zones.items()]
    row = "\n".join(["---", "row_type: SWEEP", "run_date: %s" % D, "run_time: %s" % time_, "pr_title: %s" % title,
                     "---"] + table +
                    ["## Price/ordering refresh", "| Key | Px | Px unit | Close date | Source |", "|---|---|---|---|---|",
                     "| WAT1 | 111 | USD | 2026-10-02 | Yahoo |", ""])
    return title, {"queue/rows/%s_%s_SWEEP.md" % (D, time_): row, "queue/runs/%s_%s_SWEEP.md" % (D, time_): "note\n"}


def intake_changes(time_="0602", title=None):
    title = title or "GSC INTAKE %s — register v2 (1 rows)" % D
    rows = [dict(r) for r in REG_ROWS]
    for r in rows:
        if r["key"] == "WAT1":
            r["px"] = "112"
    csv_text, md = register_files(rows, "v2", D)
    return title, {
        "register.csv": csv_text, "_REGISTER.md": md,
        "archive/registers/2026/REGISTER_v1_2026-10-05.md": REG_MD,
        "archive/registers/2026/REGISTER_v1_2026-10-05.csv": REG_CSV,
        "queue/rows/2026-10-05_2139_ANALYSE_OLD.md": None,
        "queue/runs/%s_%s_INTAKE.md" % (D, time_): "run note\n",
    }


def br(job, key, time_):
    return "claude/gsc-%s-%s%s-%s" % (job, key + "-" if key else "", D, time_)


# ---------------------------------------------------------------- cases

def expect(name, outcome, kind, code=None):
    ok = outcome.kind == kind and (code is None or outcome.code == code)
    record(name, ok, "got %r" % (outcome,))


def run_classifier_cases():
    fx = Fixture()
    try:
        n = 10

        def nxt():
            nonlocal n
            n += 1
            return n

        # ---- MERGE classes
        for verdict in ("WATCH", "AVOID", "DNAF"):
            title, ch = analyse_changes(verdict=verdict, title="GSC ANALYSE NEW %s — %s (Past + SF)" % (D, verdict))
            expect("merge: ANALYSE %s" % verdict, fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch)),
                   am.MERGE, "verdict")
        title, ch = analyse_changes(extra={"queue/evidence/NEW_draft-evidence_2026-09-01.md": None})
        expect("merge: ANALYSE WATCH deleting its draft evidence",
               fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch)), am.MERGE)
        title = "GSC ANALYSE NEW %s — INCOMPLETE (P1 window: FY2015 not retrieved)" % D
        ch = {"queue/evidence/NEW_%s_INCOMPLETE.md" % D: "gaps\n",
              "queue/rows/%s_2130_ANALYSE_NEW.md" % D: row_text("ANALYSE", "NEW", title, row_type="INCOMPLETE"),
              "queue/runs/%s_2130_ANALYSE_NEW.md" % D: "note\n"}
        expect("merge: ANALYSE INCOMPLETE", fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch)),
               am.MERGE, "incomplete")
        title = "GSC ANALYSE NEW %s — prior found (REVIEW)" % D
        ch = {"queue/rows/%s_2130_ANALYSE_NEW.md" % D: row_text("ANALYSE", "NEW", title, row_type="PRIOR"),
              "queue/runs/%s_2130_ANALYSE_NEW.md" % D: "note\n"}
        expect("merge: ANALYSE prior found", fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch)),
               am.MERGE, "prior")
        title = "GSC ANALYSE %s — queue exhausted" % D
        expect("merge: ANALYSE queue exhausted (run note only)",
               fx.decide(fx.pr(nxt(), br("analyse", None, "2130"), title,
                               {"queue/runs/%s_2130_ANALYSE.md" % D: "note\n"})), am.MERGE, "exhausted")
        expect("merge: ANALYSE queue exhausted with a QUEUE row",
               fx.decide(fx.pr(nxt(), br("analyse", None, "2130"), title,
                               {"queue/runs/%s_2130_ANALYSE.md" % D: "note\n",
                                "queue/rows/%s_2130_ANALYSE.md" % D: "---\nrow_type: QUEUE\nrun_date: %s\n"
                                "run_time: 2130\npr_title: %s\n---\n## Queue update\n" % (D, title)})),
               am.MERGE, "exhausted")
        title, ch = review_changes()
        expect("merge: REVIEW same verdict with the prior-memo move",
               fx.decide(fx.pr(nxt(), br("review", "REV", "0610"), title, ch)), am.MERGE, "verdict")
        title, ch = review_changes(gate="Cheapness", moved="band ≈ $59 → $61")
        expect("merge: REVIEW title with a gate bracket",
               fx.decide(fx.pr(nxt(), br("review", "REV", "0610"), title, ch)), am.MERGE)
        title = "GSC REVIEW REV %s — INCOMPLETE (roll-up exceeds budget)" % D
        ch = {"queue/evidence/REV_%s_INCOMPLETE.md" % D: "gaps\n",
              "queue/rows/%s_0610_REVIEW_REV.md" % D: row_text("REVIEW", "REV", title, row_type="INCOMPLETE"),
              "queue/runs/%s_0610_REVIEW_REV.md" % D: "note\n"}
        expect("merge: REVIEW INCOMPLETE", fx.decide(fx.pr(nxt(), br("review", "REV", "0610"), title, ch)),
               am.MERGE, "incomplete")
        title, ch = sweep_changes()
        expect("merge: SWEEP, held zones unchanged", fx.decide(fx.pr(nxt(), br("sweep", None, "0630"), title, ch)),
               am.MERGE, "sweep")
        title, ch = intake_changes()
        expect("merge: INTAKE with an unmoved base", fx.decide(fx.pr(nxt(), br("intake", None, "0602"), title, ch)),
               am.MERGE, "intake")

        # ---- HOLD reasons
        title, ch = analyse_changes(verdict="BUY", title="GSC ANALYSE NEW %s — BUY (all gates)" % D)
        expect("hold: ANALYSE BUY", fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch)),
               am.HOLD_NOTIFY, "buy")
        title, ch = review_changes(key="BUYK", prior="2026-09-04", verdict="BUY")
        ch["archive/memos/BUYK/BUYK_2026-09-04_GSC.md"] = BASE_FILES["memos/BUYK/BUYK_2026-09-04_GSC.md"]
        expect("hold: REVIEW BUY (same verdict)", fx.decide(fx.pr(nxt(), br("review", "BUYK", "0610"), title, ch)),
               am.HOLD_NOTIFY, "buy")
        title, ch = review_changes(key="HLD", prior="2026-08-01", held_prefix=True, position="HELD")
        ch["archive/memos/HLD/HLD_2026-08-01_GSC.md"] = BASE_FILES["memos/HLD/HLD_2026-08-01_GSC.md"]
        expect("hold: HELD by title prefix", fx.decide(fx.pr(nxt(), br("review", "HLD", "0610"), title, ch)),
               am.HOLD_NOTIFY, "held")
        title, ch = review_changes(key="HLD", prior="2026-08-01")
        ch["archive/memos/HLD/HLD_2026-08-01_GSC.md"] = BASE_FILES["memos/HLD/HLD_2026-08-01_GSC.md"]
        expect("hold: HELD by the register's Portfolio (no prefix, row and memo silent)",
               fx.decide(fx.pr(nxt(), br("review", "HLD", "0610"), title, ch)), am.HOLD_NOTIFY, "held")
        title, ch = analyse_changes(row_held="true")
        expect("hold: HELD by the row's held: true", fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch)),
               am.HOLD_NOTIFY, "held")
        title, ch = analyse_changes(position="HELD")
        expect("hold: HELD by the memo's position", fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch)),
               am.HOLD_NOTIFY, "held")
        # Decision 1: any HELD name is held, also on the no-verdict outcomes.
        for prefix, row_held, label in ((True, "false", "title prefix"), (False, "true", "row held: true only"),
                                        (False, "false", "register Portfolio only")):
            title = "%sGSC REVIEW HLD %s — INCOMPLETE (FY2025 10-K not retrieved)" % ("HELD · " if prefix else "", D)
            ch = {"queue/evidence/HLD_%s_INCOMPLETE.md" % D: "gaps\n",
                  "queue/rows/%s_0610_REVIEW_HLD.md" % D: row_text("REVIEW", "HLD", title, row_type="INCOMPLETE",
                                                                   held=row_held),
                  "queue/runs/%s_0610_REVIEW_HLD.md" % D: "note\n"}
            expect("hold: HELD REVIEW INCOMPLETE (%s)" % label,
                   fx.decide(fx.pr(nxt(), br("review", "HLD", "0610"), title, ch)), am.HOLD_NOTIFY, "held")
        title = "GSC ANALYSE NEW %s — INCOMPLETE (P1 window: FY2015 not retrieved)" % D
        ch = {"queue/evidence/NEW_%s_INCOMPLETE.md" % D: "gaps\n",
              "queue/rows/%s_2130_ANALYSE_NEW.md" % D: row_text("ANALYSE", "NEW", title, row_type="INCOMPLETE",
                                                                held="true"),
              "queue/runs/%s_2130_ANALYSE_NEW.md" % D: "note\n"}
        expect("hold: ANALYSE INCOMPLETE with the row's held: true",
               fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch)), am.HOLD_NOTIFY, "held")
        title = "GSC ANALYSE NEW %s — prior found (REVIEW)" % D
        ch = {"queue/rows/%s_2130_ANALYSE_NEW.md" % D: row_text("ANALYSE", "NEW", title, row_type="PRIOR",
                                                                held="true"),
              "queue/runs/%s_2130_ANALYSE_NEW.md" % D: "note\n"}
        expect("hold: ANALYSE prior found with the row's held: true",
               fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch)), am.HOLD_NOTIFY, "held")
        title, ch = review_changes(verdict="AVOID", gate="Past", moved="was WATCH, ROCE decline")
        expect("hold: REVIEW verdict change", fx.decide(fx.pr(nxt(), br("review", "REV", "0610"), title, ch)),
               am.HOLD_NOTIFY, "verdict-change")
        title, ch = review_changes(key="PRU", prior="2026-09-03")
        ch["archive/memos/PRU/PRU_2026-09-03_GSC.md"] = BASE_FILES["memos/PRU/PRU_2026-09-03_GSC.md"]
        expect("hold: REVIEW prior verdict unknown", fx.decide(fx.pr(nxt(), br("review", "PRU", "0610"), title, ch)),
               am.HOLD_NOTIFY, "prior-unknown")
        title, ch = review_changes(moved="was AVOID, band unchanged")
        expect("hold: 'was X' in the title but the verdict did not change",
               fx.decide(fx.pr(nxt(), br("review", "REV", "0610"), title, ch)), am.HOLD_NOTIFY, "mismatch")
        title = "GSC SEED %s — 4 new · 1 decay findings · restock 4" % D
        expect("hold: every SEED", fx.decide(fx.pr(nxt(), br("seed", None, "0620"), title,
                                                   {"queue/proposals/%s_0620_QUEUE-SEED.md" % D: "p\n",
                                                    "queue/runs/%s_0620_SEED.md" % D: "n\n"})),
               am.HOLD_NOTIFY, "seed")
        title, ch = sweep_changes(zones={"HLD": "ADD", "HLX": "SELL-FLAG (SR2)"})
        o = fx.decide(fx.pr(nxt(), br("sweep", None, "0630"), title, ch))
        expect("merge: SWEEP with a held zone change (J11)", o, am.MERGE, "sweep")
        record("merge: the held zone change is carried as a note for the job summary",
               o.note == "held zone changes (digest): HLD HOLD → ADD", repr(o.note))
        title, ch = sweep_changes(zones={"HLD": "HOLD"})
        expect("hold: SWEEP missing a held name's zone", fx.decide(fx.pr(nxt(), br("sweep", None, "0630"), title, ch)),
               am.HOLD_NOTIFY, "held-missing")
        title, ch = sweep_changes(zones={"HLD": "—", "HLX": "SELL-FLAG (SR2)"})
        expect("hold: SWEEP whose held Zone cell is '—' (no zone word)",
               fx.decide(fx.pr(nxt(), br("sweep", None, "0630"), title, ch)), am.HOLD_NOTIFY, "held-missing")

        # ---- title states and grammar
        title, ch = analyse_changes()
        for suffix, kind, code in ((" [running]", am.WAIT, "running"), (" [fixing]", am.HOLD, "fixing"),
                                   (" [abandoned]", am.HOLD_NOTIFY, "title-state"),
                                   (" [superseded]", am.HOLD_NOTIFY, "title-state")):
            t = ("GSC ANALYSE NEW %s" % D) + suffix
            expect("title %s" % suffix.strip(), fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"), t, ch)),
                   kind, code)
        for outcome in ("stopped: guard off", "blocked: main moved twice"):
            t = "GSC INTAKE %s — %s" % (D, outcome)
            expect("title — %s" % outcome, fx.decide(fx.pr(nxt(), br("intake", None, "0602"), t,
                                                           {"queue/runs/%s_0602_INTAKE.md" % D: "n\n"})),
                   am.HOLD_NOTIFY, "stopped")
        title, ch = analyse_changes(title="GSC ANALYSE NEW %s — looks fine" % D)
        expect("hold: title outside the grammar", fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch)),
               am.HOLD_NOTIFY, "title-grammar")
        title, ch = analyse_changes(title="GSC ANALYSE OTHER %s — WATCH (Cheapness)" % D)
        expect("hold: title key differs from the branch key",
               fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch)), am.HOLD_NOTIFY, "title-branch")
        title, ch = analyse_changes(memo_verdict="AVOID")
        # v4.5.2: the write-contract re-check runs lint-row first, so a verdict mismatch holds as 'contract'.
        o = fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch))
        expect("hold: title verdict differs from the memo (lint-row)", o, am.HOLD_NOTIFY, "contract")
        record("hold text names lint-row", "lint-row" in o.text, o.text)
        title, ch = analyse_changes(cell="AVOID")
        expect("hold: memo verdict differs from the row cell (lint-row)",
               fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch)), am.HOLD_NOTIFY, "contract")
        title, ch = analyse_changes(row_title="GSC ANALYSE NEW %s — WATCH (something else)" % D)
        expect("hold: row pr_title differs from the live title",
               fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch)), am.HOLD_NOTIFY, "mismatch")
        title = "GSC ANALYSE NEW %s — WATCH (Cheapness)" % D
        ch = {"memos/NEWX/NEWX_%s_GSC.md" % D: memo_text("NEWX", "WATCH", D),
              "queue/rows/%s_2130_ANALYSE_NEWX.md" % D: row_text("ANALYSE", "NEWX", title, "WATCH"),
              "queue/runs/%s_2130_ANALYSE_NEWX.md" % D: "note\n"}
        expect("hold: re-key (memo under another key)", fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"),
                                                                         title, ch)), am.HOLD_NOTIFY, "rekey")

        # ---- unexpected files / contract
        title, ch = analyse_changes(extra={"queue/runs/%s_2130_ANALYSE.md" % D: "extra\n"})
        expect("hold: an extra run note", fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch)),
               am.HOLD_NOTIFY, "unexpected-files")
        title, ch = analyse_changes(extra={"queue/evidence/NEW_%s_INCOMPLETE.md" % D: "x\n"})
        expect("hold: a verdict PR that also adds INCOMPLETE evidence",
               fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch)), am.HOLD_NOTIFY, "unexpected-files")
        title, ch = analyse_changes(extra={"queue/evidence/OTHER_%s_INCOMPLETE.md" % D: "x\n"})
        expect("hold: an evidence file of another key (contract)",
               fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch)), am.HOLD_NOTIFY, "contract")
        title, ch = review_changes(move=False)
        expect("hold: a REVIEW without the move pair (contract)",
               fx.decide(fx.pr(nxt(), br("review", "REV", "0610"), title, ch)), am.HOLD_NOTIFY, "contract")
        title, ch = analyse_changes(extra={"memos/AVO/AVO_2026-09-02_GSC.md": None})
        expect("hold: an ANALYSE deleting a memo (contract)",
               fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch)), am.HOLD_NOTIFY, "contract")
        title, ch = analyse_changes(extra={"notes.txt": "x\n"})
        expect("hold: evaluate() error -> contract", fx.decide(fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch)),
               am.HOLD_NOTIFY, "contract")

        # ---- guard selection on the exact head sha
        title, ch = analyse_changes()
        pr = fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch, guard=None)
        fx.gh.add_run(pr["head"]["sha"], "success", created="2026-10-06T05:10:00Z")
        fx.gh.add_run(pr["head"]["sha"], "skipped", created="2026-10-06T05:20:00Z")
        expect("guard: newest skipped, older success -> merge", fx.decide(pr), am.MERGE)
        pr = fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch, guard=None)
        fx.gh.add_run(pr["head"]["sha"], "success", created="2026-10-06T05:10:00Z")
        fx.gh.add_run(pr["head"]["sha"], "failure", created="2026-10-06T05:20:00Z")
        expect("guard: newest non-skipped run failed -> hold", fx.decide(pr), am.HOLD_NOTIFY, "guard-failed")
        pr = fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch, guard="cancelled")
        expect("guard: cancelled on attempt 1 -> wait", fx.decide(pr), am.WAIT, "guard-retry")
        pr = fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch, guard=None)
        fx.gh.add_run(pr["head"]["sha"], "cancelled", attempt=2)
        expect("guard: cancelled on attempt 2 -> hold", fx.decide(pr), am.HOLD_NOTIFY, "guard-cancelled")
        pr = fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch, guard=None)
        fx.gh.add_run(pr["head"]["sha"], "startup_failure", with_job=False)
        expect("guard: startup_failure without a job -> wait", fx.decide(pr), am.WAIT, "guard-retry")
        pr = fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch, guard=None)
        fx.gh.add_run(pr["head"]["sha"], "success", with_job=False)
        expect("guard: run 'success' without a guard job -> hold (no fall-back)", fx.decide(pr), am.HOLD_NOTIFY,
               "guard-failed")
        pr = fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch, guard=None)
        fx.gh.add_run(pr["head"]["sha"], None, status="in_progress")
        expect("guard: a run in progress -> wait", fx.decide(pr), am.WAIT, "guard-pending")
        pr = fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch, guard="skipped")
        expect("guard: only skipped runs -> wait", fx.decide(pr), am.WAIT, "guard-none")
        pr = fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch, guard=None)
        fx.gh.add_run(pr["head"]["sha"], "success", attempt=2)
        expect("guard: a successful re-run (attempt 2) -> merge", fx.decide(pr), am.MERGE)
        pr = fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch, guard=None)
        fx.gh.add_run(pr["head"]["sha"], "success", job_conclusion="skipped")
        expect("guard: a skipped job is never read as success (V1)", fx.decide(pr), am.WAIT, "guard-none")
        pr = fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch, guard=None)
        expect("guard: no run yet -> wait", fx.decide(pr), am.WAIT, "guard-none")

        # ---- head handling and main-state checks
        pr = fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch)
        fx.repo.git("update-ref", "refs/pull/%d/head" % pr["number"], fx.repo.main)
        expect("head: fetched head differs from pr.head.sha -> wait", fx.decide(pr), am.WAIT, "head-moved")
        base = fx.repo.main
        fx.repo.advance_main({"queue/rows/2026-10-06_0005_ANALYSE_NEW.md": "---\nrow_type: INCOMPLETE\n---\n"})
        pr = fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch, base=base)
        expect("main: a row for the key landed after the base -> hold", fx.decide(pr), am.HOLD_NOTIFY,
               "key-moved-on-main")
        fx.repo.advance_main({"memos/NEW/NEW_2026-10-05_GSC.md": memo_text("NEW", "AVOID", "2026-10-05")})
        pr = fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch, base=base)
        o = fx.decide(pr)
        record("main: a second ANALYSE of the same key -> hold", o.kind == am.HOLD_NOTIFY
               and o.code in ("contract", "key-moved-on-main"), repr(o))
        fx.repo.set_main(base)
        rtitle, rch = review_changes()
        fx.repo.advance_main({"memos/REV/REV_2026-09-01_GSC.md": None,
                              "archive/memos/REV/REV_2026-09-01_GSC.md": BASE_FILES["memos/REV/REV_2026-09-01_GSC.md"],
                              "memos/REV/REV_2026-10-05_GSC.md": memo_text("REV", "WATCH", "2026-10-05")})
        pr = fx.pr(nxt(), br("review", "REV", "0610"), rtitle, rch, base=base)
        o = fx.decide(pr)
        record("main: a stale REVIEW after a merged REVIEW -> hold", o.kind == am.HOLD_NOTIFY
               and o.code in ("contract", "key-moved-on-main"), repr(o))
        fx.repo.set_main(base)

        # ---- INTAKE base check, one case per INTAKE_BASE_PATHS entry, plus a deletion
        record("INTAKE_BASE_PATHS is the agreed list", chk.INTAKE_BASE_PATHS == (
            "_REGISTER.md", "register.csv", "queue/TODO.md", "queue/DRAFT_QUEUE.md", "archive/registers/",
            "archive/queue/"), repr(chk.INTAKE_BASE_PATHS))
        moves = {"_REGISTER.md": REG_MD + "\n", "register.csv": REG_CSV.replace("Nov 2026", "Dec 2026", 1),
                 "queue/TODO.md": TODO + "- `Y` — item\n", "queue/DRAFT_QUEUE.md": "# DRAFT_QUEUE (v7)\n",
                 "archive/registers/": ("archive/registers/2026/REGISTER_v1b_2026-10-06.md", "x\n"),
                 "archive/queue/": ("archive/queue/TODO_v41_2026-10-06.md", "x\n")}
        ititle, ich = intake_changes()
        for path in chk.INTAKE_BASE_PATHS:
            change = moves[path]
            fx.repo.advance_main({change[0]: change[1]} if isinstance(change, tuple) else {path: change})
            pr = fx.pr(nxt(), br("intake", None, "0602"), ititle, ich, base=base)
            expect("INTAKE base moved: %s" % path, fx.decide(pr), am.HOLD, "intake-base")
            fx.repo.set_main(base)
        fx.repo.advance_main({"memos/WAT1/WAT1_2026-09-05_GSC.md": None}, 'Revert "GSC ANALYSE WAT1 …" (#98)')
        pr = fx.pr(nxt(), br("intake", None, "0602"), ititle, ich, base=base)
        expect("INTAKE: a memo deleted on main since the base (revert) -> hold", fx.decide(pr), am.HOLD, "intake-base")
        fx.repo.set_main(base)
        fx.repo.advance_main({"memos/AVO/AVO_2026-09-02_GSC.md": None,
                              "archive/memos/AVO/AVO_2026-09-02_GSC.md": BASE_FILES["memos/AVO/AVO_2026-09-02_GSC.md"],
                              "memos/AVO/AVO_2026-10-06_GSC.md": memo_text("AVO", "AVOID", D)})
        pr = fx.pr(nxt(), br("intake", None, "0602"), ititle, ich, base=base)
        expect("INTAKE: a REVIEW's memo move on main is not a deletion -> merge", fx.decide(pr), am.MERGE, "intake")
        fx.repo.set_main(base)
        # The real case: a full REVIEW memo shares little text with its prior, so
        # git can pair the prior only with its archive copy (exact rename).
        rolled = "---\nticker: AVO\nverdict: AVOID\n---\n" + "".join(
            "Line %d of a full roll-up memo, rewritten from the primary documents.\n" % i for i in range(400))
        fx.repo.advance_main({"memos/AVO/AVO_2026-09-02_GSC.md": None,
                              "archive/memos/AVO/AVO_2026-09-02_GSC.md": BASE_FILES["memos/AVO/AVO_2026-09-02_GSC.md"],
                              "memos/AVO/AVO_2026-10-06_GSC.md": rolled})
        pr = fx.pr(nxt(), br("intake", None, "0602"), ititle, ich, base=base)
        expect("INTAKE: a REVIEW's move with a dissimilar new memo is not a deletion -> merge", fx.decide(pr),
               am.MERGE, "intake")
        fx.repo.set_main(base)
        fx.repo.advance_main({"memos/REV/REV_2026-09-01_GSC.md": None,
                              "memos/REV/REV_2026-10-05_GSC.md": rolled.replace("AVO", "REV")})
        pr = fx.pr(nxt(), br("intake", None, "0602"), ititle, ich, base=base)
        expect("INTAKE: a memo replaced on main without its archive copy -> hold", fx.decide(pr), am.HOLD,
               "intake-base")
        fx.repo.set_main(base)
        seeded = fx.repo.advance_main({"queue/proposals/2026-10-05_0620_QUEUE-SEED.md": "proposal\n"},
                                      "GSC SEED 2026-10-05 — 2 new (#97)")
        fx.repo.advance_main({"queue/proposals/2026-10-05_0620_QUEUE-SEED.md": None}, 'Revert "GSC SEED …" (#96)')
        pr = fx.pr(nxt(), br("intake", None, "0602"), ititle, ich, base=seeded)
        expect("INTAKE: a SEED proposal reverted on main since the base -> hold", fx.decide(pr), am.HOLD,
               "intake-base")
        fx.repo.set_main(base)

        # ---- ignored and mismatched PRs
        ignored = [fx.pr(nxt(), "claude/fix-something", "GSC: fix", {"queue/runs/x.md": "x\n"}),
                   fx.pr(nxt(), br("analyse", "NEW", "2130"), title, ch, repo_name="someone/fork"),
                   fx.pr(nxt(), "claude/attended-x", "GSC ANALYSE NEW %s — WATCH (Cheapness)" % D, ch)]
        record("ignored: non-routine, fork head and attended branch with a routine title",
               all(gsc_gh.routine_kind(p) is None for p in ignored))
        pr = fx.pr(nxt(), br("analyse", "NEW", "2130"), "GSC: a routine branch with an attended title", ch)
        expect("hold: routine branch with a non-routine title", fx.decide(pr), am.HOLD_NOTIFY, "title-branch")
        pr = fx.pr(nxt(), "claude/gsc-analyse-NEW-2026-13-06-2130", title, ch)
        expect("hold: routine-looking branch with a bad date", fx.decide(pr), am.HOLD_NOTIFY, "title-branch")

        # ---- real PR titles (#45, #73, #74, #76, #79, #80, #81) parse
        real = [
            "GSC ANALYSE ACAST.ST 2026-10-04 — INCOMPLETE (P1 window: FY2015–FY2019 statements not retrieved)",
            "GSC INTAKE 2026-10-05 — no register change (0 rows)",
            "GSC REVIEW INVE-B.ST 2026-10-05 — WATCH; band ≈ SEK 294 → 318, cheapness FAIR, P19 flag retired",
            "GSC SWEEP 2026-10-05 — 90/90 priced · 0 in range · 0 stale",
            "GSC ANALYSE SPX.L 2026-10-05 — AVOID (Past)",
            "GSC INTAKE 2026-10-06 — register v307 (1 rows)",
            "GSC REVIEW BABA 2026-10-06 — AVOID (Past + Future + SF); was WATCH, pre-v3 re-test; band ≈ $59 → $14.4",
            "GSC ANALYSE METSO.HE 2026-10-04 — WATCH (EXPENSIVE; Past ADEQUATE, history-limited)",
            "GSC ANALYSE 6324.T 2026-10-04 — AVOID (Past WEAK + Future WEAK + SF FAIL)",
        ]
        parsed = [am.parse_title(t) for t in real]
        record("grammar: the real routine titles parse", all(parsed), [t for t, p in zip(real, parsed) if not p])
        record("grammar: BABA reads as AVOID, was WATCH", parsed[6]["verdict"] == "AVOID" and parsed[6]["old"] == "WATCH")
        record("grammar: a REVIEW without '; what moved' fails", am.parse_title("GSC REVIEW X %s — WATCH" % D) is None)
        record("grammar: queue exhausted needs a keyless title",
               am.parse_title("GSC ANALYSE X %s — queue exhausted" % D) is None)
    finally:
        fx.close()


def run_held_zone_cases():
    # J11: a register zone of '-' (owed) with a sweep zone word is a change, not a hold;
    # only the SWEEP's own cell decides 'held-missing'.
    rows = [reg_row("HLD", "WATCH", held=True, zone="-", memo_date="2026-08-01")] + REG_ROWS[1:]
    csv_text, md = register_files(rows, "v1", "2026-10-05")
    files = dict(BASE_FILES, **{"register.csv": csv_text, "_REGISTER.md": md})
    fx = Fixture(files)
    try:
        title, ch = sweep_changes()
        o = fx.decide(fx.pr(70, br("sweep", None, "0630"), title, ch))
        expect("merge: register zone '-' with a sweep zone HOLD (J11)", o, am.MERGE, "sweep")
        record("note: '-' → HOLD listed for the digest", o.note == "held zone changes (digest): HLD - → HOLD", o.note)
    finally:
        fx.close()
    fx = Fixture()
    try:
        title, ch = sweep_changes(zones={"HLD": "ADD", "HLX": "SELL-FLAG (SR2)"})
        fx.pr(71, br("sweep", None, "0630"), title, ch)
        results = am.sweep(fx.ctx)
        text = am.summary(results, "on")
        record("summary: a merged SWEEP lists its held zone changes in the job summary",
               results and results[0][1].kind == "MERGED" and "HLD HOLD → ADD" in text
               and [p for p, _d in fx.gh.puts()] == ["pulls/71/merge"] and not fx.gh.posted_comments(), text)
    finally:
        fx.close()


def run_sweep_cases():
    # ---- modes, merge call, dedupe, ordering, exceptions (through sweep() and main())
    def eligible(fx, n, key="NEW", time_="2130"):
        title, ch = analyse_changes(key=key, time_=time_)
        return fx.pr(n, br("analyse", key, time_), title, ch)

    for raw, merges in ((None, 0), ("", 0), ("ON ", 0), ("ON", 0), ("off", 0), ("garbage", 0), ("dry-run", 0),
                        ("on", 1)):
        fx = Fixture()
        try:
            eligible(fx, 20)
            title, ch = analyse_changes(key="NEW2", verdict="BUY", title="GSC ANALYSE NEW2 %s — BUY (all)" % D)
            fx.pr(21, br("analyse", "NEW2", "2130"), title, ch)
            env = {"REPO": REPO, "EVENT_NAME": "workflow_dispatch"}
            if raw is not None:
                env["GSC_AUTOMERGE"] = raw
            rc = am.main(env, gh=fx.client, git=fx.repo.runner(), sleep=fx.slept.append, now=lambda: NOW)
            comments = fx.gh.posted_comments()
            want_comments = 0 if am.read_mode(raw) == "off" else 1
            record("mode %r: %d merge(s), %d comment(s)" % (raw, merges, want_comments),
                   rc == 0 and len(fx.gh.puts()) == merges and len(comments) == want_comments,
                   "rc %s, puts %s, comments %s" % (rc, fx.gh.puts(), comments))
        finally:
            fx.close()

    fx = Fixture()
    try:
        pr = eligible(fx, 30)
        stitle, sch = sweep_changes(title="GSC SWEEP %s — 5/5 priced · 1 in range · 0 stale" % D)
        fx.pr(31, br("sweep", None, "0630"), stitle, sch)
        results = am.sweep(fx.ctx)
        puts = fx.gh.puts()
        record("merge call: squash, sha pinned, '{title} (#n)'",
               ("pulls/30/merge", {"merge_method": "squash", "sha": pr["head"]["sha"],
                                   "commit_title": pr["title"] + " (#30)"}) in puts, puts)
        record("merge call: a title with '—' and '·' keeps them",
               any(d["commit_title"] == stitle + " (#31)" for _p, d in puts), puts)
        record("merge order: SWEEP before ANALYSE", [p for p, _d in puts] == ["pulls/31/merge", "pulls/30/merge"], puts)
        record("after each merge main is fetched again",
               sum(1 for c in fx.repo.calls if c[:1] == ["fetch"] and "main" in c[-1]) >= 2)
    finally:
        fx.close()

    fx = Fixture()
    try:
        ititle, ich = intake_changes()
        fx.pr(40, br("intake", None, "0602"), ititle, ich)
        stitle, sch = sweep_changes()
        fx.pr(41, br("sweep", None, "0630"), stitle, sch)
        rtitle, rch = review_changes()
        fx.pr(42, br("review", "REV", "0610"), rtitle, rch)
        eligible(fx, 39)
        am.sweep(fx.ctx)
        record("sweep order: INTAKE, SWEEP, REVIEW, ANALYSE",
               [p for p, _d in fx.gh.puts()] == ["pulls/40/merge", "pulls/41/merge", "pulls/42/merge",
                                                 "pulls/39/merge"], fx.gh.puts())
    finally:
        fx.close()

    # Merge refusals.
    for script, mergeable, kind, code, label in (
            ([(405, "Base branch was modified")], None, "MERGED", None, "405 then mergeable null -> retry once, merged"),
            ([(405, "Base branch was modified"), (405, "Base branch was modified")], None, am.WAIT, "merge-retry",
             "405 twice with mergeable null -> wait, no comment"),
            ([(405, "Pull Request is not mergeable")], False, am.HOLD_NOTIFY, "merge-refused",
             "405 with mergeable false -> hold"),
            ([(422, "Head sha mismatch")], None, am.HOLD_NOTIFY, "merge-refused", "422 -> hold")):
        fx = Fixture()
        try:
            pr = eligible(fx, 50)
            fx.gh.merge_script[50] = list(script)
            pr["mergeable"] = mergeable
            results = am.sweep(fx.ctx)
            o = results[0][1]
            ok = o.kind == kind and (code is None or o.code == code)
            if code == "merge-retry":
                ok = ok and not fx.gh.posted_comments() and fx.slept == [10]
            if kind == "MERGED":
                ok = ok and fx.slept == [10]
            record("merge: " + label, ok, "%r slept %s" % (o, fx.slept))
        finally:
            fx.close()
    fx = Fixture()
    try:
        pr = eligible(fx, 51)
        fx.gh.merge_script[51] = [(409, "Head branch was modified")]

        def move_head():
            pr["head"]["sha"] = "0" * 40
        fx.gh.after_merge_call[51] = move_head
        o = am.sweep(fx.ctx)[0][1]
        record("merge: 409 with a moved head -> wait", o.kind == am.WAIT and o.code == "head-moved", repr(o))
    finally:
        fx.close()
    fx = Fixture()
    try:
        pr = eligible(fx, 52)
        decided = fx.decide(pr)
        fx.gh.prs[52]["title"] = pr["title"] + " [fixing]"      # Jakub retitles between decide and merge
        o = am.merge(fx.ctx, pr, decided)
        record("merge: a retitle after decide -> no PUT, wait for the next event",
               decided.kind == am.MERGE and o.kind == am.WAIT and not fx.gh.puts(), "%r %r" % (decided, o))
    finally:
        fx.close()

    # Dedupe, no '#n', exceptions, workflow_run scope.
    fx = Fixture()
    try:
        title, ch = analyse_changes(verdict="BUY", title="GSC ANALYSE NEW %s — BUY (all gates; PR#12)" % D)
        fx.pr(60, br("analyse", "NEW", "2130"), title, ch)
        am.sweep(fx.ctx)
        am.sweep(fx.ctx)
        comments = fx.gh.posted_comments()
        record("comment dedupe: the same (PR, sha, reason) posts once", len(comments) == 1, comments)
        record("comment: names 'PR 60', never '#60' or '#12', with a search link and the marker",
               comments and "PR 60 held - BUY NEW" in comments[0] and "#6" not in comments[0]
               and "#1" not in comments[0] and "pulls?q=is%3Apr+is%3Aopen+60" in comments[0]
               and "<!-- gsc-hold pr=60 sha=" in comments[0] and comments[0].startswith("@jakubhoryna"), comments)
    finally:
        fx.close()

    fx = Fixture()
    try:
        eligible(fx, 70)
        eligible(fx, 71, key="NEW3")
        fx.gh.fail_get.add("pulls/70")
        results = am.sweep(fx.ctx)
        by = {pr["number"]: o for pr, o in results}
        record("exception in one PR: it is held and notified, the other still merges",
               by[70].kind == am.HOLD_NOTIFY and by[70].code == "automerge-exception" and by[71].kind == "MERGED"
               and [p for p, _d in fx.gh.puts()] == ["pulls/71/merge"] and len(fx.gh.posted_comments()) == 1,
               "%r %r %s" % (by.get(70), by.get(71), fx.gh.puts()))
    finally:
        fx.close()

    fx = Fixture()
    try:
        a = eligible(fx, 80, key="NEWA")
        eligible(fx, 81, key="NEWB")
        fx.gh.prs[81]["updated_at"] = "2026-10-06T03:00:00Z"     # 3 h 40 min old: left to the daily sweep
        eligible(fx, 82, key="NEWC")
        fx.gh.prs[82]["updated_at"] = "2026-10-06T06:30:00Z"     # 10 min old: swept too
        env = {"REPO": REPO, "GSC_AUTOMERGE": "on", "EVENT_NAME": "workflow_run",
               "TRIGGER_BRANCH": a["head"]["ref"]}
        rc = am.main(env, gh=fx.client, git=fx.repo.runner(), sleep=fx.slept.append, now=lambda: NOW)
        record("workflow_run: the triggering PR, then only recently updated PRs",
               rc == 0 and [p for p, _d in fx.gh.puts()] == ["pulls/80/merge", "pulls/82/merge"], fx.gh.puts())
    finally:
        fx.close()

    fx = Fixture()
    try:
        eligible(fx, 90)
        fx.gh.fail_get.add("pulls")
        rc = am.main({"REPO": REPO, "GSC_AUTOMERGE": "on", "EVENT_NAME": "workflow_dispatch"}, gh=fx.client,
                     git=fx.repo.runner(), sleep=fx.slept.append, now=lambda: NOW)
        comments = fx.gh.posted_comments()
        record("listing fails: exit 1, no merge, one dated error comment",
               rc == 1 and not fx.gh.puts() and len(comments) == 1 and "automerge-error-2026-10-06" in comments[0],
               "rc %s %s" % (rc, comments))
    finally:
        fx.close()

    # Allowlist across everything recorded above is checked per fixture here.
    fx = Fixture()
    try:
        for n, key in ((95, "NEWD"), (96, "NEWE")):
            eligible(fx, n, key=key)
        title, ch = analyse_changes(key="NEWF", verdict="BUY", title="GSC ANALYSE NEWF %s — BUY (x)" % D)
        fx.pr(97, br("analyse", "NEWF", "2130"), title, ch)
        am.sweep(fx.ctx)
        bad = [(m, p) for m, p, _d in fx.gh.calls
               if (m == "PATCH" and p.startswith("pulls")) or (m == "POST" and p.startswith("issues/9")
                                                               and int(p.split("/")[1]) in fx.gh.prs)
               or any(w in p for w in ("labels", "reviews", "requested_reviewers", "assignees"))]
        record("calls never PATCH a PR, comment on a PR, label, review or assign", not bad, bad)
    finally:
        fx.close()


def run_allowlist_cases():
    calls = []

    def transport(method, url, headers, body):
        calls.append((method, url))
        return 200, {}, b"{}"
    gh = gsc_gh.Gh("t0ken", REPO, transport=transport)
    forbidden = [
        ("PATCH", "pulls/5", {"title": "x"}), ("POST", "issues/5/comments", {"body": "x"}),
        ("POST", "issues/5/labels", {"labels": ["x"]}), ("POST", "pulls/5/reviews", {"event": "APPROVE"}),
        ("POST", "pulls/5/requested_reviewers", {"reviewers": ["x"]}),
        ("POST", "issues/5/assignees", {"assignees": ["x"]}), ("GET", "git/refs/heads/main", None),
        ("PUT", "contents/x.md", {"message": "x"}), ("POST", "graphql", {"query": "x"}),
        ("PUT", "pulls/5/merge", {"merge_method": "squash", "sha": "a" * 40, "commit_title": "x"}),
        ("POST", "actions/runs/5/rerun", None),
        ("POST", "actions/workflows/gsc-automerge.yml/dispatches", {"ref": "main"}),
        ("PATCH", "issues/5", {"state": "closed", "state_reason": "completed"}),
        ("POST", "issues", {"title": "anything", "body": "x"}),
        ("POST", "issues", {"title": gsc_gh.NEEDS_TITLE, "body": "x", "labels": ["x"]}),
        ("POST", "issues", {"title": gsc_gh.NEEDS_TITLE, "body": "x", "assignees": ["someone"]}),
        ("GET", "../other/repo", None), ("GET", "collaborators", None), ("DELETE", "issues/5", None),
        ("GET", "pulls?state=open/../x", None),
    ]
    for method, rel, fields in forbidden:
        try:
            gh.request(method, rel, fields)
            ok = False
        except gsc_gh.NotAllowed:
            ok = True
        record("allowlist: %s %s raises NotAllowed" % (method, rel), ok)
    merger = gsc_gh.Gh("t0ken", REPO, transport=transport, allow_merge=True)
    for fields in ({"merge_method": "merge", "sha": "a" * 40, "commit_title": "x"},
                   {"merge_method": "squash", "sha": "abc", "commit_title": "x"},
                   {"merge_method": "squash", "sha": "a" * 40, "commit_title": "x", "commit_message": "y"}):
        try:
            merger.request("PUT", "pulls/5/merge", fields)
            ok = False
        except gsc_gh.NotAllowed:
            ok = True
        record("allowlist: merge fields %s refused" % sorted(fields), ok)
    actions = gsc_gh.Gh("t0ken", REPO, transport=transport, allow_actions=True)
    try:
        actions.request("POST", "actions/workflows/gsc-automerge.yml/dispatches", {"ref": "dev"})
        ok = False
    except gsc_gh.NotAllowed:
        ok = True
    record("allowlist: dispatch on a ref other than main refused", ok)
    record("allowlist: nothing reached the network", not calls, calls)
    # The token never appears in an error.
    gh2 = gsc_gh.Gh("SECRET-t0ken", REPO, transport=lambda m, u, h, b: (403, {}, b'{"message": "denied"}'))
    try:
        gh2.get("pulls/1")
        msg = ""
    except gsc_gh.GhError as exc:
        msg = str(exc)
    record("errors carry status and path, never the token", "403" in msg and "SECRET" not in msg, msg)
    # Pagination follows only this repository.
    pages = {"p1": (200, {"Link": '<https://api.github.com/repos/%s/pulls?page=2>; rel="next"' % REPO}, b"[1]"),
             "p2": (200, {}, b"[2]")}
    seen = []

    def paged(method, url, headers, body):
        seen.append(url)
        return pages["p2" if "page=2" in url else "p1"]
    record("pagination: Link rel=next is followed",
           gsc_gh.Gh("t", REPO, transport=paged).get_all("pulls?state=open") == [1, 2], seen)
    evil = {"Link": '<https://api.github.com/repos/other/repo/pulls?page=2>; rel="next"'}
    try:
        gsc_gh.Gh("t", REPO, transport=lambda m, u, h, b: (200, evil, b"[1]")).get_all("pulls?state=open")
        ok = False
    except gsc_gh.NotAllowed:
        ok = True
    record("pagination: a next link to another repository is refused", ok)
    # GitHub may page by repository id and workflow id; the request is rebuilt
    # from the original path with the page number [v4.5.1].
    seen2 = []
    byid = {"Link": '<https://api.github.com/repositories/123/actions/workflows/456/runs?created=%3E%3D2026-10-01T00%3A00%3A00Z&per_page=100&page=2>; rel="next"'}

    def paged_id(method, url, headers, body):
        seen2.append(url)
        if "page=2" in url:
            return 200, {}, b'{"workflow_runs": [2]}'
        return 200, byid, b'{"workflow_runs": [1]}'
    got = gsc_gh.Gh("t", REPO, transport=paged_id).get_all(
        "actions/workflows/gsc-guard.yml/runs?created=%3E%3D2026-10-01T00:00:00Z&per_page=100", key="workflow_runs")
    record("pagination: a repositories/{id} next link is rebuilt on this repository's own path",
           got == [1, 2] and len(seen2) == 2
           and seen2[1] == "https://api.github.com/repos/%s/actions/workflows/gsc-guard.yml/runs"
                           "?created=%%3E%%3D2026-10-01T00:00:00Z&per_page=100&page=2" % REPO, seen2)
    nopage = {"Link": '<https://api.github.com/repositories/123/actions/runs?cursor=abc>; rel="next"'}
    try:
        gsc_gh.Gh("t", REPO, transport=lambda m, u, h, b: (200, nopage, b"[1]")).get_all("actions/runs?per_page=100")
        ok = False
    except gsc_gh.NotAllowed:
        ok = True
    record("pagination: a next link without a page number is refused", ok)
    # The needs-Jakub comment goes only to a verified issue.
    fake = FakeGitHub()
    fake.add_issue(gsc_gh.NEEDS_TITLE, login="someone")            # not the bot
    fake.add_issue("GSC ANALYSE X", pr=True)                          # a pull request
    gh3 = gsc_gh.Gh("t", REPO, transport=fake)
    number = gsc_gh.ensure_needs_issue(gh3)
    record("needs-Jakub issue: created once by the bot when none is verifiable",
           fake.issues[number]["user"]["login"] == gsc_gh.BOT and fake.issues[number]["assignees"] == ["jakubhoryna"]
           and gsc_gh.ensure_needs_issue(gh3) == number
           and sum(1 for m, p, _d in fake.calls if m == "POST" and p == "issues") == 1)
    try:
        gh3.close_digest(number)
        ok = False
    except gsc_gh.NotAllowed:
        ok = True
    record("close_digest refuses a non-digest issue", ok)


def main():
    run_allowlist_cases()
    run_classifier_cases()
    run_held_zone_cases()
    run_sweep_cases()
    failed = RESULTS.count(False)
    print("\n%d case(s), %d failed" % (len(RESULTS), failed))
    return failed


if __name__ == "__main__":
    sys.exit(main())
