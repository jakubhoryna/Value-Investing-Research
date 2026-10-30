#!/usr/bin/env python3
"""gsc-notify: the daily maintenance run and the standing 'GSC - needs Jakub'
record issue (MODEL v4.8.0 §8.7 items 10 and 12). Run by
.github/workflows/gsc-notify.yml. The workflow keeps its v4.5.0 name, but since
v4.8.0 it notifies no one: the morning digest is retired, and routine outcomes
reach Jakub in the WEEKLY routine's report (MODEL §8.7 item 11).

Inputs (environment): GH_TOKEN (the per-run GITHUB_TOKEN), REPO, GSC_AUTOMERGE
(logged only) and EVENT_SCHEDULE (the cron that fired; empty on a manual
dispatch).

Maintenance, once per Prague day and late-tolerant (MODEL §8.7 items 10 and
12). GitHub starts scheduled runs late and drops some: from 2026-10-08 it
started one run per cron line per day, 4-8 h late, so the v4.5.0 window
(06:30-08:30) never acted. Five cron lines now fire a day (MAINTENANCE_CRONS)
and the Prague clock decides: a scheduled run acts only when 06:30 <= Prague
time < 21:00 and gsc-automerge has not been dispatched since 06:30 Prague today. The dispatch is the run's
last write, so a run that fails before it is retried by the next tick, and a
later tick the same day exits with GETs only. A manual dispatch skips both
tests. The window opens after INTAKE's 06:00 start and never reaches into the
02:00-06:00 quiet window: each merge wakes the routine session watching that
PR.

It ensures the needs-Jakub issue (created once, unassigned); re-runs guard
runs that GitHub cancelled, timed out or failed to start (attempt 1 only, at
most 20 per run, never a 'failure') on open finished routine PRs, then polls
them together for at most 6 minutes; records a finished routine PR whose head
sha has no non-skipped guard run after 1 h ('guard-missing') or whose guard
run has been queued or running for more than 1 h ('guard-stuck'); then
dispatches gsc-automerge for a full merge sweep (a re-run started with
GITHUB_TOKEN fires no workflow_run).

Comments go only to the needs-Jakub issue, one per (PR, head sha, code), and
are a record, not a ping: they @mention no one (gsc_gh.py neutralises and
refuses mentions) and never write '#n' (V4: open PRs are 'PR n' with a search
link). A failed run posts one dated record comment per Prague day.

Python 3.11+ standard library only. Tests: test_gsc_notify.py.
"""
import datetime
import os
import sys
import time

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import gsc_automerge as am  # noqa: E402
import gsc_gh  # noqa: E402

PRAGUE = gsc_gh.prague_tz()
UTC = datetime.timezone.utc
# Must equal the workflow's cron lines, in order (test_gsc_workflows.py checks it). One
# line per tick: GitHub has started at most one run per cron line per day. 04:30 UTC is
# 06:30 CEST and 05:30 UTC is 06:30 CET (the other one of that pair is 05:30 CET, before
# the window, or 07:30 CEST, a spare); the spares at 08:30, 11:30 and 14:30 UTC (10:30,
# 13:30, 16:30 CEST; 09:30, 12:30, 15:30 CET) still land inside the window when GitHub
# starts them 10, 7 or 4 hours late.
MAINTENANCE_CRONS = ("30 4 * * *", "30 5 * * *", "30 8 * * *", "30 11 * * *", "30 14 * * *")
MAINTENANCE_AT = (6, 30)
MAINTENANCE_UNTIL = (21, 0)
GUARD_MISSING_AGE = datetime.timedelta(hours=1)
GUARD_STUCK_AGE = datetime.timedelta(hours=1)
MAX_RERUNS = 20
POLL_EVERY = 20
POLL_TOTAL = 360


# ---------------------------------------------------------------- time

def iso(dt):
    return dt.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_iso(value):
    if not value:
        return None
    try:
        return datetime.datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(UTC)
    except ValueError:
        return None


def _prague_at(now, hour_minute):
    """Today's hour:minute Europe/Prague (the Prague date of `now`) as an aware datetime."""
    p = now.astimezone(PRAGUE)
    return p.replace(hour=hour_minute[0], minute=hour_minute[1], second=0, microsecond=0)


def maintenance_start(now):
    """Today's 06:30 Europe/Prague."""
    return _prague_at(now, MAINTENANCE_AT)


def maintenance_end(now):
    """Today's 21:00 Europe/Prague (exclusive)."""
    return _prague_at(now, MAINTENANCE_UNTIL)


def maintenance_in_window(now):
    """06:30 <= Prague time < 21:00: never in the 02:00-06:00 quiet window."""
    return maintenance_start(now) <= now.astimezone(PRAGUE) < maintenance_end(now)


def age_text(delta):
    hours = delta.total_seconds() / 3600
    return "%.0f h" % hours if hours < 48 else "%.1f d" % (hours / 24)


def finished(title):
    t = (title or "").rstrip()
    return not t.endswith("[running]") and not t.endswith("[fixing]")


# ---------------------------------------------------------------- maintenance

def flag(ctx, pr, sha, code, text):
    """One needs-Jakub record comment per (PR, head sha, code); no @mention."""
    n = int(pr["number"])
    marker = "<!-- gsc-hold pr=%d sha=%s code=%s -->" % (n, sha[:7], code)
    body = "PR %d held - %s\n%s\nOpen: %s\n%s" % (
        n, text, gsc_gh.no_hash_ref(pr.get("title") or ""), gsc_gh.search_link(ctx.repo, n), marker)
    gsc_gh.post_needs_comment(ctx.gh, body, marker, pr.get("created_at"))


def maintenance_due(ctx, now):
    """(True, '') when a scheduled maintenance should run now, else (False, why)."""
    if not maintenance_in_window(now):
        return False, "outside the 06:30-21:00 window (Prague %s)" % now.astimezone(PRAGUE).strftime("%a %H:%M")
    start = iso(maintenance_start(now))
    runs = ctx.gh.get_all("actions/workflows/gsc-automerge.yml/runs?event=workflow_dispatch&created=%%3E%%3D%s"
                          "&per_page=100" % start, key="workflow_runs", limit=2)
    if runs:
        return False, "gsc-automerge already dispatched since 06:30 today (run %s)" % runs[0].get("id")
    return True, ""


def run_maintenance(ctx, clock=time.monotonic, scheduled=True):
    now = ctx.now()
    if scheduled:
        due, why = maintenance_due(ctx, now)
        if not due:
            ctx.log("maintenance: %s - nothing to do" % why)
            return 0
    gsc_gh.ensure_needs_issue(ctx.gh)
    reruns = []
    for pr in ctx.gh.get_all("pulls?state=open&base=main&per_page=100"):
        if gsc_gh.routine_kind(pr) is None or not finished(pr.get("title")):
            continue
        sha = (pr.get("head") or {}).get("sha") or ""
        state, run = am.guard_state(ctx.gh, sha)
        if state == "retry" and len(reruns) < MAX_RERUNS:
            ctx.gh.request("POST", "actions/runs/%d/rerun" % int(run["id"]))
            reruns.append(int(run["id"]))
            ctx.log("maintenance: re-ran guard run %s (PR %s, %s)" % (run["id"], pr["number"], run.get("conclusion")))
        elif state == "none":
            updated = parse_iso(pr.get("updated_at"))
            if updated is not None and now - updated > GUARD_MISSING_AGE:
                flag(ctx, pr, sha, "guard-missing", "the guard never ran on its head sha %s" % sha[:7])
        elif state == "pending" and run is not None:
            created = parse_iso(run.get("created_at"))
            if created is not None and now - created > GUARD_STUCK_AGE:
                flag(ctx, pr, sha, "guard-stuck", "its guard run %s on head sha %s has been %s for %s"
                     % (run.get("id"), sha[:7], run.get("status") or "unfinished", age_text(now - created)))
    # A re-run started with GITHUB_TOKEN fires no workflow_run: poll them together.
    start = clock()
    pending = list(reruns)
    while pending and clock() - start < POLL_TOTAL:
        ctx.sleep(POLL_EVERY)
        pending = [rid for rid in pending if (ctx.gh.get("actions/runs/%d" % rid) or {}).get("status") != "completed"]
    if pending:
        ctx.log("maintenance: %d re-run(s) still running after %d s" % (len(pending), POLL_TOTAL))
    # The dispatch is the last write: it is also the per-day dedupe marker (maintenance_due).
    ctx.gh.request("POST", "actions/workflows/gsc-automerge.yml/dispatches", {"ref": "main"})
    ctx.log("maintenance: %d re-run(s); gsc-automerge dispatched" % len(reruns))
    return 0


# ---------------------------------------------------------------- main

def main(env=None, gh=None, git=None, sleep=None, now=None, clock=time.monotonic):
    env = os.environ if env is None else env
    repo = env.get("REPO", "")
    # The workflow's only job holds actions: write (guard re-runs, the gsc-automerge dispatch).
    gh = gh or gsc_gh.Gh(env.get("GH_TOKEN", ""), repo, allow_actions=True)
    ctx = am.Ctx(gh, git=git, repo=repo, mode=am.read_mode(env.get("GSC_AUTOMERGE")), now=now, sleep=sleep,
                 log=lambda line: print("gsc-notify: " + am.chk.printable(line)))
    scheduled = bool((env.get("EVENT_SCHEDULE") or "").strip())
    try:
        return run_maintenance(ctx, clock, scheduled=scheduled)
    except Exception as exc:  # one dated record comment per Prague day, no @mention
        ctx.log("maintenance failed: %s" % type(exc).__name__)
        try:
            day = ctx.now().astimezone(PRAGUE)
            marker = "<!-- gsc-hold pr=0 sha=0000000 code=notify-error-%s -->" % day.strftime("%Y-%m-%d")
            start = day.replace(hour=0, minute=0, second=0, microsecond=0)
            gsc_gh.post_needs_comment(gh, "gsc-notify maintenance failed: %s\n%s"
                                      % (type(exc).__name__, marker), marker, iso(start))
        except Exception:
            pass
        return 1


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(errors="backslashreplace")
    except AttributeError:
        pass
    sys.exit(main())
