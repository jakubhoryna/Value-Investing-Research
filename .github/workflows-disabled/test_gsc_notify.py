#!/usr/bin/env python3
"""Plain-Python tests for gsc_notify.py (no pytest, no network).

Uses the fixtures of test_gsc_automerge.py: a throwaway git repo for main and
a fake GitHub transport that records every call.

Run:  python3 .github/workflows/test_gsc_notify.py
Prints one PASS/FAIL line per case; the exit code is the number of failures.
"""
import datetime
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gsc_gh  # noqa: E402
import gsc_notify as nt  # noqa: E402
import test_gsc_automerge as t  # noqa: E402

UTC = datetime.timezone.utc
record = t.record
MAINT = nt.MAINTENANCE_CRONS[0]


def at(text):
    return datetime.datetime.fromisoformat(text).replace(tzinfo=UTC)


class Clock:
    """Fake monotonic clock that sleep() advances."""

    def __init__(self):
        self.value = 0.0
        self.slept = []

    def __call__(self):
        return self.value

    def sleep(self, seconds):
        self.slept.append(seconds)
        self.value += seconds


def fixture(now, files=None, needs=True):
    fx = t.Fixture(files)
    if not needs:
        fx.gh.issues.clear()
    fx.gh.now = now
    fx.ctx.now = lambda: now
    return fx


def run(fx, now, env, clock=None):
    clock = clock or Clock()
    fx.gh.now = now
    return nt.main(env, gh=fx.client, git=fx.repo.runner(), sleep=clock.sleep, now=lambda: now, clock=clock)


def writes(fx, since=0):
    return [(m, p) for m, p, _d in fx.gh.calls[since:] if m != "GET"]


def no_mention(texts):
    return not any(gsc_gh.MENTION_RE.search(x or "") for x in texts)


# ---------------------------------------------------------------- cases

def window_cases():
    for when, expected, label in (
            ("2026-10-06T04:30:00", True, "Tue 04:30Z = 06:30 CEST: acts"),
            ("2026-10-06T04:29:00", False, "Tue 04:29Z = 06:29 CEST: too early"),
            ("2026-10-06T05:30:00", True, "Tue 05:30Z = 07:30 CEST: inside (the dispatch dedupe stops it)"),
            ("2026-10-06T09:30:00", True, "Tue 09:30Z = 11:30 CEST: a late start still acts"),
            ("2026-10-06T18:59:00", True, "Tue 18:59Z = 20:59 CEST: last minute of the window"),
            ("2026-10-06T19:00:00", False, "Tue 19:00Z = 21:00 CEST: window closed"),
            ("2026-10-06T22:30:00", False, "Wed 00:30 CEST: before the new day's 06:30"),
            ("2026-10-26T04:30:00", False, "Mon 26 Oct 04:30Z = 05:30 CET: quiet window, no-op"),
            ("2026-10-26T05:30:00", True, "Mon 26 Oct 05:30Z = 06:30 CET: acts"),
            ("2026-10-26T19:59:00", True, "Mon 26 Oct 19:59Z = 20:59 CET: inside"),
            ("2026-10-26T20:00:00", False, "Mon 26 Oct 20:00Z = 21:00 CET: window closed"),
            ("2026-10-25T04:30:00", False, "Sun 25 Oct (DST end day) 04:30Z = 05:30 CET: no-op"),
            ("2026-10-25T05:30:00", True, "Sun 25 Oct (DST end day) 05:30Z = 06:30 CET: acts"),
            ("2027-03-28T04:30:00", True, "Sun 28 Mar 2027 (DST start day) 04:30Z = 06:30 CEST: acts"),
            ("2027-03-28T03:30:00", False, "Sun 28 Mar 2027 03:30Z = 05:30 CEST: quiet window, no-op")):
        record("maintenance window: " + label, nt.maintenance_in_window(at(when)) is expected)
    # Every minute-30 tick of a whole day, in CET, in CEST and on both DST change days:
    # the window acts only at 06:30 <= Prague < 21:00, never in 02:00-06:00.
    bad = []
    for day in ("2026-01-14", "2026-07-15", "2026-10-25", "2027-03-28"):
        for minute in range(0, 24 * 60, 10):
            when = at(day + "T00:00:00") + datetime.timedelta(minutes=minute)
            local = when.astimezone(nt.PRAGUE)
            want = (6, 30) <= (local.hour, local.minute) < (21, 0)
            if nt.maintenance_in_window(when) is not want or (want and 2 <= local.hour < 6):
                bad.append("%s -> %s" % (when.isoformat(), local.strftime("%H:%M")))
    record("maintenance window: exactly 06:30-21:00 Prague all day, DST change days included", not bad, bad[:5])
    record("maintenance window: today's start and end are Prague 06:30 and 21:00",
           nt.maintenance_start(at("2026-10-25T12:00:00")).strftime("%H:%M %Z") == "06:30 CET"
           and nt.maintenance_end(at("2026-10-24T12:00:00")).strftime("%H:%M %Z") == "21:00 CEST",
           (nt.maintenance_start(at("2026-10-25T12:00:00")), nt.maintenance_end(at("2026-10-24T12:00:00"))))
    record("no digest code left: the module has no digest entry point",
           not any(hasattr(nt, name) for name in ("run_digest", "build_digest", "in_window", "pick_task",
                                                  "digest_title")))


def guard_prs(fx):
    def pr(n, title, conclusion, attempt=1, updated="2026-10-06T01:00:00Z", runs=True, status="completed",
           created="2026-10-06T05:10:00Z"):
        sha = ("%040d" % n)
        fx.gh.prs[n] = {"number": n, "state": "open", "title": title, "mergeable": True,
                        "head": {"ref": "claude/gsc-analyse-K%d-2026-10-05-2130" % n, "sha": sha,
                                 "repo": {"full_name": t.REPO}},
                        "base": {"ref": "main", "repo": {"full_name": t.REPO}},
                        "created_at": "2026-10-05T19:30:00Z", "updated_at": updated}
        if runs:
            fx.gh.add_run(sha, conclusion, attempt=attempt, status=status, created=created)
        return n
    done = "GSC ANALYSE K%d 2026-10-05 — WATCH (Cheapness)"
    pr(1, done % 1, "cancelled")
    pr(2, done % 2, "timed_out")
    pr(3, done % 3, "startup_failure")
    pr(4, done % 4, "failure")
    pr(5, done % 5, "cancelled", attempt=2)
    pr(6, "GSC ANALYSE K6 2026-10-05 [running]", "cancelled")
    pr(7, done % 7, None, runs=False)                                   # guard never ran, 3 h 30 min old
    pr(8, done % 8, None, runs=False, updated="2026-10-06T04:00:00Z")   # only 30 min old
    pr(9, done % 9, None, status="queued", created="2026-10-06T02:00:00Z")        # queued for 2 h 30 min
    pr(10, done % 10, None, status="in_progress", created="2026-10-06T04:20:00Z")  # running for 10 min
    pr(11, "GSC ANALYSE K11 2026-10-05 — WATCH (@octocat Cheapness)", None, runs=False)   # a mention in a title


def maintenance_cases():
    now = at("2026-10-06T04:30:00")          # 06:30 CEST
    fx = fixture(now, needs=False)
    try:
        guard_prs(fx)
        clock = Clock()
        rc = run(fx, now, {"REPO": t.REPO, "EVENT_SCHEDULE": MAINT}, clock)
        reran = sorted(fx.gh.run_by_id[rid]["head_sha"] for rid in fx.gh.reruns)
        record("maintenance: re-runs only cancelled, timed_out and startup_failure on attempt 1",
               rc == 0 and reran == ["%040d" % n for n in (1, 2, 3)], reran)
        record("maintenance: polls the re-runs together, then dispatches gsc-automerge on main",
               clock.slept == [nt.POLL_EVERY, nt.POLL_EVERY] and fx.gh.dispatches == [{"ref": "main"}]
               and [c[1] for c in fx.gh.calls if c[0] == "POST"][-1] == "actions/workflows/gsc-automerge.yml/dispatches",
               "slept %s dispatches %s" % (clock.slept, fx.gh.dispatches))
        comments = fx.gh.posted_comments()
        record("maintenance: guard-missing after 1 h only, guard-stuck after 1 h only",
               len(comments) == 3 and "PR 7 held - the guard never ran" in comments[0]
               and "PR 9 held - its guard run" in comments[1] and "code=guard-stuck" in comments[1]
               and "queued for 2 h" in comments[1] and "PR 11 held - the guard never ran" in comments[2]
               and not any("#7" in c or "#9" in c for c in comments)
               and not any("PR 8 " in c or "PR 10 " in c for c in comments), comments)
        record("maintenance: record comments start 'PR n held' and @mention no one (a title's '@x' neutralised)",
               all(c.startswith("PR ") for c in comments) and no_mention(comments) and "@jakubhoryna" not in
               "".join(comments) and "(@ octocat Cheapness)" in comments[2], comments)
        needs = [i for i in fx.gh.issues.values() if i["title"] == gsc_gh.NEEDS_TITLE]
        record("maintenance: the needs-Jakub issue is created once, unassigned, mentioning no one",
               len(needs) == 1 and needs[0]["assignees"] is None and no_mention([needs[0]["body"]])
               and [d for m, p, d in fx.gh.calls if m == "POST" and p == "issues"]
               == [{"title": gsc_gh.NEEDS_TITLE, "body": gsc_gh.NEEDS_BODY}], needs)
        record("maintenance: writes only issues/comments, re-runs and the dispatch; never a PR, never a PATCH",
               all(m == "POST" and (p == "issues" or p.endswith("/comments") or p.endswith("/rerun")
                                    or p == "actions/workflows/gsc-automerge.yml/dispatches")
                   for m, p in writes(fx)), writes(fx))
        calls = len(fx.gh.calls)
        rc = run(fx, at("2026-10-06T05:30:00"), {"REPO": t.REPO, "EVENT_SCHEDULE": MAINT}, Clock())
        record("maintenance: the 07:30 CEST tick the same morning does nothing (already dispatched today)",
               rc == 0 and len(fx.gh.dispatches) == 1 and len(fx.gh.reruns) == 3 and not writes(fx, calls),
               fx.gh.calls[calls:])
        calls = len(fx.gh.calls)
        rc = run(fx, at("2026-10-06T17:30:00"), {"REPO": t.REPO, "EVENT_SCHEDULE": MAINT}, Clock())
        record("maintenance: the 19:30 CEST spare the same day does nothing (per-day dedupe)",
               rc == 0 and len(fx.gh.dispatches) == 1 and not writes(fx, calls), fx.gh.calls[calls:])
        rc = run(fx, now, {"REPO": t.REPO}, Clock())
        needs = [i for i in fx.gh.issues.values() if i["title"] == gsc_gh.NEEDS_TITLE]
        record("maintenance: a manual run skips the window and the dedupe, and posts no second issue or comment",
               rc == 0 and len(fx.gh.dispatches) == 2 and len(needs) == 1 and len(fx.gh.posted_comments()) == 3)
        calls = len(fx.gh.calls)
        rc = run(fx, at("2026-10-07T04:30:00"), {"REPO": t.REPO, "EVENT_SCHEDULE": MAINT}, Clock())
        record("maintenance: the next day's 06:30 tick acts again (yesterday's dispatches do not count)",
               rc == 0 and len(fx.gh.dispatches) == 3 and ("POST", "actions/workflows/gsc-automerge.yml/dispatches")
               in writes(fx, calls), writes(fx, calls))
    finally:
        fx.close()

    # Late starts: GitHub started the morning ticks hours late or dropped them.
    late = at("2026-10-06T09:47:00")         # 11:47 CEST: the first tick that ran today
    fx = fixture(late)
    try:
        title, ch = t.analyse_changes()
        fx.pr(400, t.br("analyse", "NEW", "2130"), title, ch, guard="cancelled")
        fx.gh.add_run("e" * 40, workflow="gsc-automerge.yml", event="workflow_dispatch",
                      created="2026-10-05T17:40:00Z")          # yesterday's dispatch
        fx.gh.add_run("e" * 40, workflow="gsc-automerge.yml", event="workflow_dispatch",
                      created="2026-10-06T03:10:00Z")          # 05:10 today, before the window opened
        rc = run(fx, late, {"REPO": t.REPO, "EVENT_SCHEDULE": MAINT}, Clock())
        record("late start: the first tick at 11:47 Prague still re-runs and dispatches (earlier dispatches ignored)",
               rc == 0 and len(fx.gh.reruns) == 1 and fx.gh.dispatches == [{"ref": "main"}], writes(fx))
        calls = len(fx.gh.calls)
        rc = run(fx, at("2026-10-06T13:31:00"), {"REPO": t.REPO, "EVENT_SCHEDULE": MAINT}, Clock())
        record("late start: the next tick that day only reads", rc == 0 and len(fx.gh.dispatches) == 1
               and not writes(fx, calls), fx.gh.calls[calls:])
    finally:
        fx.close()
    fx = fixture(at("2026-10-06T19:10:00"))
    try:
        title, ch = t.analyse_changes()
        fx.pr(401, t.br("analyse", "NEW", "2130"), title, ch, guard="cancelled")
        rc = run(fx, at("2026-10-06T19:10:00"), {"REPO": t.REPO, "EVENT_SCHEDULE": MAINT}, Clock())
        record("late start: a tick that starts at 21:10 Prague does nothing (no API call at all)",
               rc == 0 and not fx.gh.calls and not fx.gh.dispatches, fx.gh.calls)
    finally:
        fx.close()

    quiet = at("2026-10-26T04:30:00")       # 05:30 CET: the winter tick inside the quiet window
    fx = fixture(quiet)
    try:
        title, ch = t.analyse_changes()
        fx.pr(402, t.br("analyse", "NEW", "2130"), title, ch, guard="cancelled")
        rc = run(fx, quiet, {"REPO": t.REPO, "EVENT_SCHEDULE": MAINT}, Clock())
        record("maintenance: the 05:30 CET tick is a no-op (no re-run, no dispatch, no API call)",
               rc == 0 and not fx.gh.reruns and not fx.gh.dispatches and not fx.gh.calls, fx.gh.calls)
        rc = run(fx, at("2026-10-26T05:30:00"), {"REPO": t.REPO, "EVENT_SCHEDULE": MAINT}, Clock())
        record("maintenance: the 06:30 CET tick acts", rc == 0 and len(fx.gh.reruns) == 1
               and fx.gh.dispatches == [{"ref": "main"}])
    finally:
        fx.close()

    now = at("2026-10-06T04:30:00")
    fx = fixture(now)
    try:
        for n in range(300, 325):
            sha = "%040d" % n
            fx.gh.prs[n] = {"number": n, "state": "open", "title": "GSC ANALYSE K%d 2026-10-05 — AVOID (Past)" % n,
                            "head": {"ref": "claude/gsc-analyse-K%d-2026-10-05-2130" % n, "sha": sha,
                                     "repo": {"full_name": t.REPO}},
                            "base": {"ref": "main", "repo": {"full_name": t.REPO}},
                            "created_at": "2026-10-05T19:30:00Z", "updated_at": "2026-10-05T20:30:00Z"}
            fx.gh.add_run(sha, "cancelled")
        clock = Clock()
        run(fx, now, {"REPO": t.REPO, "EVENT_SCHEDULE": MAINT}, clock)
        record("maintenance: at most 20 re-runs per run", len(fx.gh.reruns) == nt.MAX_RERUNS, len(fx.gh.reruns))
        record("maintenance: polling stays within 6 minutes", sum(clock.slept) <= nt.POLL_TOTAL, clock.slept)
    finally:
        fx.close()

    # Any schedule value runs maintenance (the digest crons and TASK are gone); no issue but the needs one.
    fx = fixture(now)
    try:
        rc = run(fx, now, {"REPO": t.REPO, "EVENT_SCHEDULE": "30 6,7,8 * * 1-5", "TASK": "digest"}, Clock())
        record("no digest: an old digest cron or TASK=digest runs maintenance and creates no issue",
               rc == 0 and fx.gh.dispatches == [{"ref": "main"}]
               and not [p for m, p in writes(fx) if p == "issues"], writes(fx))
    finally:
        fx.close()

    fx = fixture(now)
    try:
        fx.gh.fail_get.add("pulls")
        rc = run(fx, now, {"REPO": t.REPO, "EVENT_SCHEDULE": MAINT})
        comments = fx.gh.posted_comments()
        record("notify failure: exit 1 and one dated record comment, no @mention", rc == 1 and len(comments) == 1
               and comments[0].startswith("gsc-notify maintenance failed")
               and "notify-error-2026-10-06" in comments[0] and no_mention(comments), comments)
        rc = run(fx, now, {"REPO": t.REPO, "EVENT_SCHEDULE": MAINT})
        record("notify failure: the same day comments once", rc == 1 and len(fx.gh.posted_comments()) == 1)
        record("notify failure: no dispatch after a failure (the next tick retries)", not fx.gh.dispatches)
    finally:
        fx.close()


def main():
    window_cases()
    maintenance_cases()
    failed = t.RESULTS.count(False)
    print("\n%d case(s), %d failed" % (len(t.RESULTS), failed))
    return failed


if __name__ == "__main__":
    sys.exit(main())
