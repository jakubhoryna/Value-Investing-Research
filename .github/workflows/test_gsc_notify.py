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
import gsc_automerge as am  # noqa: E402
import gsc_gh  # noqa: E402
import gsc_notify as nt  # noqa: E402
import test_gsc_automerge as t  # noqa: E402

UTC = datetime.timezone.utc
record = t.record


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
    return nt.main(env, gh=fx.client, git=fx.repo.runner(), sleep=clock.sleep, now=lambda: now, clock=clock)


def digests_posted(fx):
    return [d for m, p, d in fx.gh.calls if m == "POST" and p == "issues"]


# ---------------------------------------------------------------- cases

def window_cases():
    for when, expected, label in (
            ("2026-10-06T06:30:00", True, "Tue 06:30Z = 08:30 CEST: post"),
            ("2026-10-06T07:30:00", True, "Tue 07:30Z = 09:30 CEST: inside the window (the dedupe stops it)"),
            ("2026-10-26T06:30:00", False, "Mon 26 Oct 06:30Z = 07:30 CET: too early"),
            ("2026-10-26T07:30:00", True, "Mon 26 Oct 07:30Z = 08:30 CET: post"),
            ("2026-10-31T08:45:00", True, "Sat 31 Oct 08:45Z = 09:45 CET: post"),
            ("2026-10-31T07:45:00", False, "Sat 31 Oct 07:45Z = 08:45 CET: too early"),
            ("2027-03-29T06:30:00", True, "Mon 29 Mar 2027 06:30Z = 08:30 CEST again: post"),
            ("2026-10-06T09:31:00", False, "Tue 09:31Z = 11:31 CEST: past the 3 h window")):
        record("window: " + label, nt.in_window(at(when)) is expected)
    for when, expected, label in (
            ("2026-10-06T04:30:00", True, "Tue 04:30Z = 06:30 CEST: maintenance runs"),
            ("2026-10-06T05:30:00", True, "Tue 05:30Z = 07:30 CEST: inside (the dispatch dedupe stops it)"),
            ("2026-10-26T04:30:00", False, "Mon 26 Oct 04:30Z = 05:30 CET: quiet window, no-op"),
            ("2026-10-26T05:30:00", True, "Mon 26 Oct 05:30Z = 06:30 CET: maintenance runs"),
            ("2026-10-06T06:31:00", False, "Tue 06:31Z = 08:31 CEST: past the 2 h window")):
        record("maintenance window: " + label, nt.maintenance_in_window(at(when)) is expected)
    for schedule, task, want in (("30 4,5 * * *", "", "maintenance"), ("30 6,7,8 * * 1-5", "", "digest"),
                                 ("45 7,8,9 * * 0,6", "maintenance", "digest"), ("", "maintenance", "maintenance"),
                                 ("", "", "digest"), ("", "weird", "digest")):
        record("task: schedule %r task %r -> %s" % (schedule, task, want),
               nt.pick_task({"EVENT_SCHEDULE": schedule, "TASK": task}) == want)
    names = []
    for day in range(5, 12):          # Mon 5 Oct .. Sun 11 Oct 2026
        p = at("2026-10-%02dT10:00:00" % day).astimezone(nt.PRAGUE)
        names.append(nt.digest_title(p, 7, 1, False))
    record("title: one per weekday, ASCII hyphen",
           names == ["GSC digest %s %d Oct - 7 merged, 1 needs you" % (d, n)
                     for d, n in zip(("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"), range(5, 12))], names)
    record("title: STALL prefix", nt.digest_title(at("2026-10-06T07:00:00").astimezone(nt.PRAGUE), 0, 2, True)
           == "STALL - GSC digest Tue 6 Oct - 0 merged, 2 needs you")


def gate_cases():
    fx = fixture(at("2026-10-06T06:30:00"))
    try:
        ctx = fx.ctx
        for fm, want in (
                ({"verdict": "AVOID", "quality_past": "WEAK", "past_reason": "ROCE decline",
                  "quality_future": "WEAK", "sf": "FAIL"}, "AVOID · Past WEAK · ROCE decline"),
                ({"verdict": "AVOID", "quality_past": "ADEQUATE", "quality_future": "WEAK", "future_reason": "breadth",
                  "sf": "PASS"}, "AVOID · Future WEAK · breadth"),
                ({"verdict": "AVOID", "quality_past": "STRONG", "quality_future": "STRONG", "sf": "FAIL",
                  "sf_reason": "n.m."}, "AVOID · SF FAIL · -"),
                ({"verdict": "AVOID", "quality_past": "WEAK"}, "AVOID · Past WEAK · -"),
                ({"verdict": "WATCH", "px": "118.09", "trigger": "97.9", "px_unit": "USD"},
                 "WATCH · Cheapness · Px 118.09 vs trigger 97.9 USD"),
                ({"verdict": "DNAF"}, "DNAF · Gate 0"), ({"verdict": "BUY"}, "BUY · all gates pass")):
            got = nt.deciding_gate(ctx, fm)
            record("deciding gate: %s" % want, got == want, got)
        text = t.memo_text("X", "WATCH", t.D, summary="**X** sells widgets at 12.5x earnings. It stays a WATCH.")
        record("summary: first sentence of '## 1. Verdict'", nt.first_sentence(ctx, text)
               == "X sells widgets at 12.5x earnings.", nt.first_sentence(ctx, text))
        long = t.memo_text("X", "WATCH", t.D, summary="word " * 80 + ".")
        record("summary: capped at 160 characters", len(nt.first_sentence(ctx, long)) == 160)
    finally:
        fx.close()


def merged_fixture(now):
    fx = fixture(now)
    repo = fx.repo
    repo.advance_main({"memos/NEW/NEW_2026-10-05_GSC.md": t.memo_text("NEW", "AVOID", "2026-10-05", past="WEAK",
                                                                       past_reason="ROCE decline"),
                       "queue/rows/2026-10-05_2130_ANALYSE_NEW.md": "row\n"},
                      "GSC ANALYSE NEW 2026-10-05 — AVOID (Past) (#77)", "2026-10-05T19:40:00Z")
    repo.advance_main({"memos/REV/REV_2026-09-01_GSC.md": None,
                       "archive/memos/REV/REV_2026-09-01_GSC.md": t.BASE_FILES["memos/REV/REV_2026-09-01_GSC.md"],
                       "memos/REV/REV_2026-10-06_GSC.md": t.memo_text("REV", "WATCH", t.D)},
                      "GSC REVIEW REV 2026-10-06 — WATCH; band unchanged (#81)", "2026-10-06T04:20:00Z")
    repo.advance_main({"memos/AVO/AVO_2026-09-02_GSC.md": None,
                       "archive/memos/AVO/AVO_2026-09-02_GSC.md": t.BASE_FILES["memos/AVO/AVO_2026-09-02_GSC.md"],
                       "memos/AVO/AVO_2026-10-06_GSC.md": t.memo_text("AVO", "DNAF", t.D)},
                      "GSC: AVO v2 DNAF (#78)", "2026-10-06T04:25:00Z")
    repo.advance_main({"memos/WAT1/WAT1_2026-09-05_GSC.md": None,
                       "memos/WAT1/WAT1_2026-09-04_GSC.md": t.memo_text("WAT1", "WATCH", "2026-09-04")},
                      'Revert "GSC REVIEW WAT1 2026-10-05 — WATCH; x (#70)" (#83)', "2026-10-06T04:30:00Z")
    repo.advance_main({"queue/runs/2026-10-06_0602_INTAKE.md": "n\n"},
                      "GSC INTAKE 2026-10-06 — register v2 (3 rows) (#80)", "2026-10-06T04:35:00Z")
    repo.advance_main({"queue/rows/2026-10-06_0630_SWEEP.md": "n\n"},
                      "GSC SWEEP 2026-10-06 — 5/5 priced · 0 in range · 0 stale (#84)", "2026-10-06T04:36:00Z")
    repo.advance_main({"queue/evidence/KARN_2026-10-06_INCOMPLETE.md": "n\n"},
                      "GSC ANALYSE KARN 2026-10-06 — INCOMPLETE (P1 window: FY2015 not retrieved) (#85)",
                      "2026-10-06T04:37:00Z")
    return fx


def digest_cases():
    now = at("2026-10-06T06:31:00")
    fx = merged_fixture(now)
    try:
        prev = fx.gh.add_issue("GSC digest Mon 5 Oct - 3 merged, 0 needs you", created="2026-10-05T06:31:00Z")
        old = fx.gh.add_issue("GSC digest Sun 4 Oct - 1 merged, 0 needs you", state="closed",
                              created="2026-10-04T07:46:00Z")
        foreign = fx.gh.add_issue("GSC digest Sat 3 Oct - 0 merged, 0 needs you", login="someone",
                                  created="2026-10-03T07:46:00Z")
        prlike = fx.gh.add_issue("GSC digest Fri 2 Oct - 0 merged, 0 needs you", pr=True,
                                 created="2026-10-02T06:31:00Z")
        # Open routine PRs: one held (BUY), one running, one [fixing], one waiting on its guard.
        title, ch = t.analyse_changes(key="NEWB", verdict="BUY", title="GSC ANALYSE NEWB %s — BUY (all)" % t.D)
        fx.pr(101, t.br("analyse", "NEWB", "2130"), title, ch)
        fx.pr(102, t.br("analyse", "NEWR", "2130"), "GSC ANALYSE NEWR %s [running]" % t.D, {"q/x.md": "x\n"},
              guard=None)
        fx.pr(103, t.br("analyse", "NEWF", "2130"), "GSC ANALYSE NEWF %s [fixing]" % t.D, {"q/y.md": "y\n"},
              guard=None)
        title, ch = t.analyse_changes(key="NEWW")
        fx.pr(104, t.br("analyse", "NEWW", "2130"), title, ch, guard=None)
        fx.gh.add_run("a" * 40, "success", created="2026-10-05T07:00:00Z")
        fx.gh.add_run("b" * 40, "skipped", created="2026-10-05T07:00:00Z")
        fx.gh.add_run("c" * 40, "failure", workflow="gsc-automerge.yml", created="2026-10-05T08:00:00Z")
        rc = run(fx, now, {"REPO": t.REPO, "GSC_AUTOMERGE": "On", "EVENT_SCHEDULE": "30 6,7,8 * * 1-5"})
        posts = digests_posted(fx)
        record("digest: posted once", rc == 0 and len(posts) == 1, "rc %s posts %s" % (rc, len(posts)))
        post = posts[0] if posts else {"title": "", "body": "", "assignees": None}
        body = post["body"]
        record("digest: title counts merged PRs and needs-you items",
               post["title"] == "GSC digest Tue 6 Oct - 7 merged, 2 needs you", post["title"])
        record("digest: assigned to and @mentioning jakubhoryna",
               post["assignees"] == ["jakubhoryna"] and body.startswith("@jakubhoryna"))
        heads = ["## Needs you", "## Merged since", "## Held zone changes (SWEEP)", "## WATCH nearest the buy zone",
                 "## INCOMPLETE and stopped runs", "## Health"]
        pos = [body.find(h) for h in heads]
        record("digest: sections in order", all(p >= 0 for p in pos) and pos == sorted(pos), pos)
        record("digest: needs-you lists the BUY hold and the [fixing] PR, not the running one",
               "PR 101 · ANALYSE NEWB — BUY NEWB" in body and "PR 103" in body and "yours, marked [fixing]" in body
               and "PR 102" not in body.split("## Health")[0])
        record("digest: open PRs are never '#n' and use the search link",
               "#101" not in body and "#103" not in body and "pulls?q=is%3Apr+is%3Aopen+101" in body)
        record("digest: register open items counted from the TODO head block",
               "Register open items: 2" in body and "queue/TODO.md#-open-items-register" in body)
        record("digest: merged memo rows (ANALYSE, REVIEW, attended) with deciding gates",
               "| NEW | Company NEW | ANALYSE | AVOID · Past WEAK · ROCE decline |" in body
               and "| REV | Company REV | REVIEW | WATCH · Cheapness · Px 110 vs trigger 100 USD |" in body
               and "| AVO | Company AVO | attended | DNAF · Gate 0 |" in body, body)
        merged_part = body.split("## Merged since")[1].split("## WATCH")[0]
        record("digest: a revert's re-added memo and archive/memos adds are not listed",
               "| WAT1 |" not in merged_part and merged_part.count("| REV |") == 1, merged_part)
        record("digest: merged items link the memo or the commit on main, never a PR (V4)",
               "/pull/" not in body and "https://github.com/%s/blob/" % t.REPO in body
               and "/memos/NEW/NEW_2026-10-05_GSC.md) |" in body and "https://github.com/%s/commit/" % t.REPO in body
               and "PR 84 · [commit](" in body, body)
        record("digest: no '#<digit>' anywhere in the body", not any(body[i + 1:i + 2].isdigit()
                                                                     for i, ch in enumerate(body) if ch == "#"))
        record("digest: SWEEP and INTAKE lines after the memos",
               "GSC SWEEP 2026-10-06 — 5/5 priced" in body and "GSC INTAKE 2026-10-06 — register v2 (3 rows)" in body)
        zones = body.split("## Held zone changes (SWEEP)")[1].split("##")[0]
        record("digest: a SWEEP without a held zone change -> '- none'", zones.strip() == "- none", zones)
        watch = body.split("## WATCH nearest the buy zone")[1].split("##")[0]
        record("digest: WATCH nearest from register.csv, in range first, n.m. skipped",
               watch.find("| WAT2 |") >= 0 and watch.find("| WAT2 |") < watch.find("| WAT1 |")
               and "WAT3" not in watch and "-5.0%" in watch, watch)
        record("digest: INCOMPLETE runs listed", "GSC ANALYSE KARN 2026-10-06 — INCOMPLETE" in body)
        health = body.split("## Health")[1]
        record("digest: health lines", "GSC_AUTOMERGE: off (value 'On' is not one of off, dry-run, on" in health
               and "success 2 · failure 0 · cancelled 0 · skipped 1" in health and "gsc-automerge runs failed: 1" in health
               and "1 running" in health and "Register v1 · 2026-10-05 on main · MODEL v4.5.0" in health
               and "Actions minutes this month (estimate)" in health and "last INTAKE merge 2 h ago" in health,
               health)
        record("digest: health carries the register page line (MODEL §7.4)",
               "\n- Register page: https://claude.ai/artifact/FnU69xTYSTMEjqHB21rVPs (private; refreshed by INTAKE)\n"
               in health and body.count("claude.ai/artifact/") == 1, health)
        record("digest: no STALL with a recent INTAKE and few waiting PRs", not post["title"].startswith("STALL"))
        calls = [(m, p) for m, p, _d in fx.gh.calls if m in ("POST", "PATCH") and p.startswith("issues")]
        record("digest: new digest created first, then the previous one closed",
               calls == [("POST", "issues"), ("PATCH", "issues/%d" % prev["number"])], calls)
        record("digest: never closes a foreign issue or a pull request",
               fx.gh.issues[foreign["number"]]["state"] == "open" and fx.gh.issues[prlike["number"]]["state"] == "open"
               and fx.gh.issues[old["number"]]["state"] == "closed")
        record("digest: never touches a pull request",
               not [c for c in fx.gh.calls if c[0] != "GET" and c[1].startswith("pulls")])
        # Same Prague day, second cron tick: dedupe.
        later = at("2026-10-06T07:30:00")
        fx.gh.now = later
        rc = run(fx, later, {"REPO": t.REPO, "GSC_AUTOMERGE": "on", "EVENT_SCHEDULE": "30 6,7,8 * * 1-5"})
        record("digest: the second tick the same day posts nothing", rc == 0 and len(digests_posted(fx)) == 1)
        rc = run(fx, later, {"REPO": t.REPO, "GSC_AUTOMERGE": "on", "TASK": "digest"})
        record("digest: a manual dispatch keeps the dedupe", rc == 0 and len(digests_posted(fx)) == 1)
    finally:
        fx.close()

    early = at("2026-10-26T06:30:00")
    fx = fixture(early)
    try:
        rc = run(fx, early, {"REPO": t.REPO, "EVENT_SCHEDULE": "30 6,7,8 * * 1-5"})
        record("digest: too early in CET posts nothing", rc == 0 and not digests_posted(fx))
        rc = run(fx, early, {"REPO": t.REPO, "TASK": "digest"})
        posts = digests_posted(fx)
        record("digest: a manual dispatch skips the window; no INTAKE in 30 h with a row waiting -> STALL",
               rc == 0 and len(posts) == 1 and posts[0]["title"].startswith("STALL - GSC digest Mon 26 Oct"),
               posts and posts[0]["title"])
    finally:
        fx.close()

    now = at("2026-10-06T06:31:00")
    fx = fixture(now)
    try:
        fx.repo.advance_main({"queue/rows/2026-10-05_2139_ANALYSE_OLD.md": None,
                              "queue/runs/2026-10-04_0602_INTAKE.md": "n\n"},
                             "GSC INTAKE 2026-10-04 — register v2 (1 rows) (#70)", "2026-10-04T04:10:00Z")
        rc = run(fx, now, {"REPO": t.REPO, "TASK": "digest"})
        posts = digests_posted(fx)
        record("digest: no INTAKE in 30 h but nothing waiting -> no STALL",
               rc == 0 and len(posts) == 1 and not posts[0]["title"].startswith("STALL"), posts and posts[0]["title"])
    finally:
        fx.close()
    fx = fixture(now)
    try:
        fx.repo.advance_main({"queue/rows/2026-10-05_2139_ANALYSE_OLD.md": None},
                             "GSC INTAKE 2026-10-04 — register v2 (1 rows) (#70)", "2026-10-04T04:10:00Z")
        fx.repo.advance_main({"queue/rows/2026-10-05_0310_REVIEW_REV.md": "row\n"},
                             "GSC REVIEW REV 2026-10-05 — WATCH; band unchanged (#71)", "2026-10-05T01:20:00Z")
        fx.repo.advance_main({"queue/rows/2026-10-06_0610_REVIEW_AVO.md": "row\n"},
                             "GSC REVIEW AVO 2026-10-06 — AVOID; band unchanged (#72)", "2026-10-06T04:30:00Z")
        rc = run(fx, now, {"REPO": t.REPO, "TASK": "digest"})
        posts = digests_posted(fx)
        body = posts[0]["body"] if posts else ""
        record("digest: no INTAKE in 30 h and a row merged > 6 h ago still waits -> STALL (a 2 h old row alone "
               "would not)", rc == 0 and len(posts) == 1 and posts[0]["title"].startswith("STALL")
               and "row files merged > 6 h ago wait on main: 1)" in body, posts and posts[0]["title"])
    finally:
        fx.close()

    now = at("2026-10-06T06:31:00")
    fx = fixture(now)
    try:
        fx.repo.advance_main({"queue/runs/x.md": "n\n"}, "GSC INTAKE 2026-10-06 — no register change (0 rows) (#80)",
                             "2026-10-06T04:10:00Z")
        for n in range(200, 216):
            fx.pr(n, "claude/gsc-seed-2026-10-0%d-0620" % (1 + n % 4),
                  "GSC SEED 2026-10-0%d — 1 new · 0 decay findings · restock 1" % (1 + n % 4), {"x%d.md" % n: "x\n"},
                  created="2026-10-02T05:00:00Z")
        rc = run(fx, now, {"REPO": t.REPO, "GSC_AUTOMERGE": "on", "EVENT_SCHEDULE": "30 6,7,8 * * 1-5"})
        posts = digests_posted(fx)
        record("digest: more than 15 finished routine PRs older than 24 h -> STALL",
               rc == 0 and posts and posts[0]["title"] == "STALL - GSC digest Tue 6 Oct - 1 merged, 16 needs you",
               posts and posts[0]["title"])
    finally:
        fx.close()

    # J11: a merged SWEEP's held zone change reaches Jakub here, read at its merge commit even
    # after INTAKE deleted the row file; never counted as needs-you; no '#n'.
    now = at("2026-10-06T06:31:00")
    fx = fixture(now)
    try:
        title, ch = t.sweep_changes(zones={"HLD": "ADD — in band", "HLX": "SELL-FLAG (SR2)"},
                                    title="GSC SWEEP 2026-10-06 — 5/5 priced · 0 in range · 0 stale")
        sweep_sha = fx.repo.advance_main(ch, title + " (#84)", "2026-10-06T04:36:00Z")
        fx.repo.advance_main({"queue/rows/2026-10-06_0630_SWEEP.md": None, "queue/runs/2026-10-06_0602_INTAKE.md": "n\n"},
                             "GSC INTAKE 2026-10-06 — register v2 (5 rows) (#86)", "2026-10-06T04:40:00Z")
        rc = run(fx, now, {"REPO": t.REPO, "GSC_AUTOMERGE": "on", "TASK": "digest"})
        posts = digests_posted(fx)
        body = posts[0]["body"] if posts else ""
        zones = body.split("## Held zone changes (SWEEP)")[1].split("##")[0] if body else ""
        record("digest: a held zone change from a merged SWEEP is listed (row file read at the merge commit)",
               rc == 0 and "| HLD | HOLD | ADD | $11 | 2026-10-06 · [commit](https://github.com/%s/commit/%s) |"
               % (t.REPO, sweep_sha) in zones and "HLX" not in zones, zones)
        record("digest: held zone changes are not needs-you; no '#<digit>'",
               posts and posts[0]["title"].endswith("0 needs you")
               and not any(body[i + 1:i + 2].isdigit() for i, ch in enumerate(body) if ch == "#"),
               posts and posts[0]["title"])
    finally:
        fx.close()

    # WATCH nearest: status_hint from the register tool. A key whose core numbers fail the strict
    # line at Px is NEAR even below its trigger (MODEL 8.3 step 3, R10); a credited key below its
    # trigger with both primaries passing is IN RANGE, whatever its holding's own price (V14).
    rows = [dict(r) for r in t.REG_ROWS]
    core = {"core_period": "FY2025", "core_currency": "USD", "core_unit": "m", "core_shares_diluted": "100",
            "core_debt_eq": "0", "core_cash": "0", "core_oi": "100", "core_oi_basis": "FY2025 J1",
            "core_fcf": "100", "core_fcf_basis": "FY2025 CFO − maint. capex (constructed)", "core_fx": "1",
            "core_fx_date": "2026-10-02", "core_ratio": "1", "core_source": "memo"}
    strict = t.reg_row("STR", "WATCH", px="95", trigger="100", memo_date="2026-09-08")
    strict.update(core)                  # MCap/FCF and EV/OI 95.0 at Px (a P20 FCF basis): the strict line fails
    credit = t.reg_row("CRD", "WATCH", px="95", trigger="100", memo_date="2026-09-09")
    credit.update(dict(core, holding_keys="WAT1", core_credit="9000"))   # WAT1 sits above its own trigger
    for row in (strict, credit):
        row.update(t.TOOL.compute_metrics(row, row["px"], "USD"))
    csv_text, md = t.register_files(rows + [strict, credit], "v1", "2026-10-05")
    files = dict(t.BASE_FILES, **{"register.csv": csv_text, "_REGISTER.md": md})
    fx = fixture(now, files)
    try:
        nearest = {r[0]: r for r in nt.watch_nearest(fx.ctx, limit=10)}
        record("WATCH nearest: a key below its trigger but failing the strict line is NEAR",
               nearest.get("STR", (None,) * 6)[5] == "NEAR" and nearest.get("WAT2", (None,) * 6)[5] == "IN RANGE"
               and nearest.get("WAT1", (None,) * 6)[5] == "NEAR", nearest)
        record("WATCH nearest: a credited key below its trigger is IN RANGE (no holding price check)",
               nearest.get("CRD", (None,) * 6)[5] == "IN RANGE", nearest)
    finally:
        fx.close()

    # Markdown fallback for the WATCH list (no register.csv on main).
    files = dict(t.BASE_FILES)
    files.pop("register.csv")
    fx = fixture(now, files)
    try:
        rows = nt.watch_nearest(fx.ctx)
        record("WATCH nearest: _REGISTER.md fallback", [r[0] for r in rows][:1] == ["WAT2"]
               and "WAT3" not in [r[0] for r in rows], rows)
    finally:
        fx.close()


def maintenance_cases():
    maint = "30 4,5 * * *"
    now = at("2026-10-06T04:30:00")          # 06:30 CEST
    fx = fixture(now, needs=False)
    try:
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
        clock = Clock()
        rc = run(fx, now, {"REPO": t.REPO, "EVENT_SCHEDULE": maint}, clock)
        reran = sorted(fx.gh.run_by_id[rid]["head_sha"] for rid in fx.gh.reruns)
        record("maintenance: re-runs only cancelled, timed_out and startup_failure on attempt 1",
               rc == 0 and reran == ["%040d" % n for n in (1, 2, 3)], reran)
        record("maintenance: polls the re-runs together, then dispatches gsc-automerge on main",
               clock.slept == [nt.POLL_EVERY, nt.POLL_EVERY] and fx.gh.dispatches == [{"ref": "main"}]
               and [c[1] for c in fx.gh.calls if c[0] == "POST"][-1] == "actions/workflows/gsc-automerge.yml/dispatches",
               "slept %s dispatches %s" % (clock.slept, fx.gh.dispatches))
        comments = fx.gh.posted_comments()
        record("maintenance: guard-missing after 1 h only, guard-stuck after 1 h only",
               len(comments) == 2 and "PR 7 held - the guard never ran" in comments[0]
               and "PR 9 held - its guard run" in comments[1] and "code=guard-stuck" in comments[1]
               and "queued for 2 h" in comments[1] and not any("#7" in c or "#9" in c for c in comments)
               and not any("PR 8 " in c or "PR 10 " in c for c in comments), comments)
        needs = [i for i in fx.gh.issues.values() if i["title"] == gsc_gh.NEEDS_TITLE]
        record("maintenance: the needs-Jakub issue is created once, assigned",
               len(needs) == 1 and needs[0]["assignees"] == ["jakubhoryna"])
        later = at("2026-10-06T05:30:00")    # the 07:30 CEST tick of the same cron
        fx.gh.now = later
        calls = len(fx.gh.calls)
        rc = run(fx, later, {"REPO": t.REPO, "EVENT_SCHEDULE": maint}, Clock())
        record("maintenance: the second tick the same morning does nothing (gsc-automerge already dispatched)",
               rc == 0 and len(fx.gh.dispatches) == 1 and len(fx.gh.reruns) == 3
               and all(m == "GET" for m, _p, _d in fx.gh.calls[calls:]), fx.gh.calls[calls:])
        fx.gh.now = now
        rc = run(fx, now, {"REPO": t.REPO, "TASK": "maintenance"}, Clock())
        needs = [i for i in fx.gh.issues.values() if i["title"] == gsc_gh.NEEDS_TITLE]
        record("maintenance: a manual run skips the window and the dedupe, and posts no second issue or comment",
               rc == 0 and len(fx.gh.dispatches) == 2 and len(needs) == 1 and len(fx.gh.posted_comments()) == 2)
    finally:
        fx.close()

    quiet = at("2026-10-26T04:30:00")       # 05:30 CET: the winter tick inside the quiet window
    fx = fixture(quiet)
    try:
        title, ch = t.analyse_changes()
        fx.pr(400, t.br("analyse", "NEW", "2130"), title, ch, guard="cancelled")
        rc = run(fx, quiet, {"REPO": t.REPO, "EVENT_SCHEDULE": maint}, Clock())
        record("maintenance: the 05:30 CET tick is a no-op (no re-run, no dispatch, no API write)",
               rc == 0 and not fx.gh.reruns and not fx.gh.dispatches
               and all(m == "GET" for m, _p, _d in fx.gh.calls), fx.gh.calls)
    finally:
        fx.close()

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
        run(fx, now, {"REPO": t.REPO, "EVENT_SCHEDULE": "30 4,5 * * *"}, clock)
        record("maintenance: at most 20 re-runs per run", len(fx.gh.reruns) == nt.MAX_RERUNS, len(fx.gh.reruns))
        record("maintenance: polling stays within 6 minutes", sum(clock.slept) <= nt.POLL_TOTAL, clock.slept)
    finally:
        fx.close()

    fx = fixture(now)
    try:
        fx.gh.fail_get.add("pulls")
        rc = run(fx, now, {"REPO": t.REPO, "EVENT_SCHEDULE": "30 4,5 * * *"})
        comments = fx.gh.posted_comments()
        record("notify failure: exit 1 and one dated comment", rc == 1 and len(comments) == 1
               and "gsc-notify maintenance failed" in comments[0] and "notify-error-2026-10-06" in comments[0],
               comments)
        rc = run(fx, now, {"REPO": t.REPO, "EVENT_SCHEDULE": "30 4,5 * * *"})
        record("notify failure: the same day comments once", rc == 1 and len(fx.gh.posted_comments()) == 1)
    finally:
        fx.close()


def main():
    window_cases()
    gate_cases()
    digest_cases()
    maintenance_cases()
    failed = t.RESULTS.count(False)
    print("\n%d case(s), %d failed" % (len(t.RESULTS), failed))
    return failed


if __name__ == "__main__":
    sys.exit(main())
