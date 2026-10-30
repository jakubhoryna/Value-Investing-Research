#!/usr/bin/env python3
"""Tests for routines/tools/gsc_weekly.py (unittest, fixtures inline).

Run:  python3 routines/tools/test_gsc_weekly.py
Exit code 0 = all pass. The end-to-end cases read this repository's own git history at fixed commits
and are skipped when those commits are absent (a shallow clone); every GitHub page they need is a
fixture written to a temporary fetch folder (the tool never talks to GitHub).

Covers: the title grammar and the routine status classification, regions, the register diff, queue
and TODO parsing (open items, the over-cap lines routed below the 7-entry block, Jakub's logged
HOLD and deferral decisions, delistings awaiting RETIRED), the window (the most recent Sunday 08:30
Prague at or before the run, catch-ups, both DST changes, the published test), the report-date
rules, the cron expander, the schedule-health input (array and object forms, QUEUE-SEED, bad input
reported under Fix), the retired-ground matcher and its one lens, the pending overlay, memo-history
classification, the weekly series (import week, first MODEL appearance, carried weeks, partial last
week), the offline fetch loader (pages, duplicates, merged_by, the needs-Jakub comments), the
attention lists (held SELL-FLAG pending in Decide, HOLD and deferral in Know, over-cap items, held
PRs with gsc-automerge's reason, every SWEEP held-zone change and every BUY in Decide, stopped,
blocked, INCOMPLETE and abandoned runs and workflow failures in Fix), the register-basis WATCH
re-test count, a re-opened run counted once, the comparable held-PR wait, the dataset schema, the
deterministic summary and lint-summary (exactly six sentences, the takeaway's headline numbers against
the kpis, advice words, private figures), the notification line, dash-writes (and its clock bound), the
published test's upper bound, an incomplete fetch refused, held zones compared by their zone word, private
figures scrubbed from copied text, outputs refused inside the repository, byte-identical re-renders
except generated_at, and that the tool's own source passes the routine guard hook's code scan.
v4.8.0: INTAKE's weekly alarm in the window object (the Monday run at or after 06:00 Prague after an
unpublished week, across both DST changes; meta_ok), the shallow-clone refusal on a real depth-1 clone
and WEEKLY.md's step-1 unshallow fetch healing it, the last-run duration and the likely no-op run under
Fix (and the optional fired_at/finished_at), and version-generic re-test blocks with partial lines.
"""
import collections
import copy
import datetime
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from decimal import Decimal

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gsc_weekly as gw  # noqa: E402

REPO = os.environ.get("GSC_REPO") or os.path.dirname(os.path.dirname(HERE))
TOOL = os.path.join(HERE, "gsc_weekly.py")
gw.load_tools(REPO)
UTC = datetime.timezone.utc
TMP = tempfile.mkdtemp(prefix="gsc-weekly-test-")

# The routine schedule as an attended session read it on 2026-10-19 (list_triggers), in the array
# form WEEKLY writes: (name, job, cron, enabled, sprint, last status, fired_at, failure_reason).
HEALTH_ROWS = (
    ("GSC INTAKE", "INTAKE", "CRON_TZ=Europe/Prague 0 6 * * *", True, False, "SUCCEEDED", "2026-10-19T04:03:36Z", ""),
    ("GSC ANALYSE", "ANALYSE", "CRON_TZ=Europe/Prague 30 21,23 * * 0-4", True, False, "SUCCEEDED",
     "2026-10-19T19:30:33Z", ""),
    ("GSC REVIEW", "REVIEW", "CRON_TZ=Europe/Prague 10 6,21 * * 1-5", True, False, "SUCCEEDED", "2026-10-19T19:12:04Z",
     ""),
    ("GSC SWEEP", "SWEEP", "CRON_TZ=Europe/Prague 30 6 * * 6", True, False, "FAILED", "2026-10-17T04:33:20Z",
     "USAGE_LIMIT_REACHED"),
    ("GSC QUEUE-SEED", "QUEUE-SEED", "CRON_TZ=Europe/Prague 20 6 * * 1,4", True, False, "SUCCEEDED",
     "2026-10-19T04:20:37Z", ""),
    ("GSC SPRINT INTAKE - Sat 18:00", "INTAKE", "CRON_TZ=Europe/Prague 0 18 * * 6", True, True, "FAILED",
     "2026-10-17T16:05:44Z", "USAGE_LIMIT_REACHED"),
    ("GSC SPRINT ANALYSE A - Fri", "ANALYSE", "CRON_TZ=Europe/Prague 0 18-23 * * 5", True, True, "FAILED",
     "2026-10-16T21:02:36Z", "USAGE_LIMIT_REACHED"),
    ("GSC SPRINT ANALYSE B - Fri", "ANALYSE", "CRON_TZ=Europe/Prague 40 18-23 * * 5", True, True, "FAILED",
     "2026-10-16T21:41:01Z", "USAGE_LIMIT_REACHED"),
    ("GSC SPRINT REVIEW - Fri", "REVIEW", "CRON_TZ=Europe/Prague 20 22,23 * * 5", True, True, "FAILED",
     "2026-10-16T21:20:23Z", "USAGE_LIMIT_REACHED"),
    ("GSC SPRINT ANALYSE A - Sat", "ANALYSE", "CRON_TZ=Europe/Prague 26 * * * 6", True, True, "FAILED",
     "2026-10-17T21:26:56Z", "USAGE_LIMIT_REACHED"),
    ("GSC SPRINT ANALYSE B - Sat", "ANALYSE", "CRON_TZ=Europe/Prague 40 * * * 6", True, True, "FAILED",
     "2026-10-17T21:40:56Z", "USAGE_LIMIT_REACHED"),
    ("GSC SPRINT REVIEW - Sat", "REVIEW", "CRON_TZ=Europe/Prague 20 * * * 6", True, True, "FAILED",
     "2026-10-17T21:20:24Z", "USAGE_LIMIT_REACHED"),
    ("GSC SPRINT ANALYSE A - Sun", "ANALYSE", "CRON_TZ=Europe/Prague 0 0-7 * * 0", True, True, "FAILED",
     "2026-10-18T05:02:17Z", "USAGE_LIMIT_REACHED"),
    ("GSC SPRINT ANALYSE B - Sun", "ANALYSE", "CRON_TZ=Europe/Prague 40 0-7 * * 0", True, True, "FAILED",
     "2026-10-18T05:40:47Z", "USAGE_LIMIT_REACHED"),
    ("GSC SPRINT REVIEW - Sun", "REVIEW", "CRON_TZ=Europe/Prague 20 0-7 * * 0", True, True, "FAILED",
     "2026-10-18T05:21:07Z", "USAGE_LIMIT_REACHED"),
)
HEALTH_DOC = [{"name": n, "job": j, "cron": c, "enabled": e, "sprint": s,
               "last_run": {"status": st, "fired_at": f, "failure_reason": r}}
              for n, j, c, e, s, st, f, r in HEALTH_ROWS]
HEALTH = os.path.join(TMP, "health.json")
with open(HEALTH, "w", encoding="utf-8") as _fh:
    json.dump(HEALTH_DOC, _fh)


def when(text):
    return gw.parse_when(text)


def run_main(argv):
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        code = gw.main(argv)
    return code, out.getvalue(), err.getvalue()


def raw_pr(n, title, created, merged=None, closed=None, head=None, merge_sha=None, updated=None):
    """One PR as GitHub's pulls list prints it (the fields the tool reads)."""
    return {"number": n, "state": "closed" if (merged or closed) else "open", "title": title,
            "created_at": created, "updated_at": updated or merged or closed or created,
            "closed_at": closed or merged, "merged_at": merged,
            "head": {"ref": head or "claude/gsc-x-%d" % n, "sha": "h%d" % n}, "base": {"ref": "main"},
            "merge_commit_sha": merge_sha, "user": {"login": "jakubhoryna"}, "draft": False}


def write_fetch(folder, pulls, details=None, issues=None, comments=None, page_size=100):
    """A fetch folder as WEEKLY step 4 writes it: pulls_{p}.json pages, pull_{n}.json details, an
    issues page and a comments page."""
    os.makedirs(folder, exist_ok=True)
    pages = [pulls[i:i + page_size] for i in range(0, len(pulls), page_size)] or [[]]
    for p, page in enumerate(pages, start=1):
        with open(os.path.join(folder, "pulls_%d.json" % p), "w", encoding="utf-8") as fh:
            json.dump(page, fh)
    for n, merged_by in (details or {}).items():
        with open(os.path.join(folder, "pull_%d.json" % n), "w", encoding="utf-8") as fh:
            json.dump({"number": n, "merged_by": merged_by}, fh)
    if issues is not None:
        with open(os.path.join(folder, "issues_1.json"), "w", encoding="utf-8") as fh:
            json.dump(issues, fh)
    if comments is not None:
        with open(os.path.join(folder, "comments_1.json"), "w", encoding="utf-8") as fh:
            json.dump(comments, fh)
    return folder


BOT = {"login": "github-actions[bot]", "type": "Bot"}
JAKUB = {"login": "jakubhoryna", "type": "User"}


class TitleGrammarTests(unittest.TestCase):
    def test_analyse_verdict_with_pr_suffix(self):
        p = gw.parse_title("GSC ANALYSE CNR.TO 2026-10-18 — AVOID (Past + Future) (#141)")
        self.assertEqual((p["job"], p["key"], p["date"], p["pr"]), ("ANALYSE", "CNR.TO", "2026-10-18", 141))
        self.assertEqual((p["kind"], p["verdict"], p["gates"], p["was"]), ("verdict", "AVOID", "Past + Future", ""))
        self.assertFalse(p["held"])
        self.assertNotIn("#", p["title"])

    def test_held_review_without_verdict_change(self):
        p = gw.parse_title("HELD · GSC REVIEW TROW 2026-10-19 — AVOID (Past + Future + SF); v4.6.0 re-test, G6 "
                           "pairing above the P31 line (classes 32–40% of assets), zone SELL-FLAG SR2 held (#147)")
        self.assertTrue(p["held"])
        self.assertEqual((p["job"], p["key"], p["verdict"], p["gates"], p["was"]),
                         ("REVIEW", "TROW", "AVOID", "Past + Future + SF", ""))
        self.assertTrue(gw.held_for_jakub(p))

    def test_review_verdict_change(self):
        p = gw.parse_title("GSC REVIEW DOV 2026-10-14 — DNAF (Gate 0); was WATCH, Climate & Sustainability "
                           "Technologies mixing refrigeration fails the one-level decomposition")
        self.assertEqual((p["verdict"], p["gates"], p["was"]), ("DNAF", "Gate 0", "WATCH"))
        self.assertTrue(gw.held_for_jakub(p))

    def test_tags_incomplete_stopped(self):
        p = gw.parse_title("GSC REVIEW COLO-B.CO 2026-10-15 [abandoned]")
        self.assertEqual((p["job"], p["key"], p["tag"], p["kind"]), ("REVIEW", "COLO-B.CO", "abandoned", ""))
        p = gw.parse_title("GSC INTAKE 2026-10-19 — register v318 (2 rows) [superseded]")
        self.assertEqual((p["tag"], p["kind"], p["register_version"], p["rows"]), ("superseded", "intake", "v318", "2"))
        p = gw.parse_title("GSC REVIEW COLO-B.CO 2026-10-15 — INCOMPLETE (method re-test exceeds budget) (#144)")
        self.assertEqual((p["kind"], p["gap"], p["pr"]), ("incomplete", "method re-test exceeds budget", 144))
        p = gw.parse_title("GSC ANALYSE XYZ.L 2026-10-19 — stopped: no listed security")
        self.assertEqual((p["kind"], p["reason"]), ("stopped", "no listed security"))
        self.assertTrue(gw.held_for_jakub(p))

    def test_keyless_attended_revert(self):
        p = gw.parse_title("GSC SEED 2026-10-15 — 0 new · 8 decay findings · restock 0 (#139)")
        self.assertEqual((p["job"], p["key"], p["kind"], p["pr"]), ("SEED", "", "seed", 139))
        self.assertTrue(gw.held_for_jakub(p))
        p = gw.parse_title("GSC: MODEL v4.6.0 — Gate 0 as best description (#146)")
        self.assertEqual((p["job"], p["kind"], p["model_version"], p["pr"]), ("attended", "model", "v4.6.0", 146))
        self.assertFalse(gw.held_for_jakub(p))
        p = gw.parse_title('Revert "GSC ANALYSE ABC 2026-10-01 — WATCH (Cheapness)"')
        self.assertEqual(p["job"], "revert")

    def test_norm_key(self):
        self.assertEqual(gw.norm_key("CCL.B.TO"), gw.norm_key("CCL-B.TO"))


def core_row(**over):
    row = {"key": "TST", "px": "9", "px_unit": "USD", "trigger": "10", "core_unit": "m",
           "core_shares_diluted": "100", "core_ratio": "1", "core_fx": "1", "core_oi": "-", "core_debt_eq": "0",
           "core_cash": "0", "core_fcf": "-", "core_fcf_basis": "-", "core_credit": "0"}
    row.update(over)
    return row


class StatusTests(unittest.TestCase):
    def test_bands(self):
        self.assertEqual(gw.shortlist_status(core_row(px="10"))[0], "IN RANGE")
        self.assertEqual(gw.shortlist_status(core_row(px="11"))[0], "NEAR")        # exactly +10%
        self.assertEqual(gw.shortlist_status(core_row(px="12")), ("FAR", Decimal("0.2")))
        self.assertEqual(gw.shortlist_status(core_row(core_oi="10"))[0], "NEAR")   # strict line holds it out

    def test_no_trigger_is_nm(self):
        self.assertEqual(gw.shortlist_status(core_row(trigger="-")), ("n.m.", None))
        self.assertEqual(gw.shortlist_status(core_row(px="-")), ("n.m.", None))


class RegionTests(unittest.TestCase):
    def test_report_regions(self):
        self.assertEqual(gw.region_of("AAPL"), ("US", "North America"))
        self.assertEqual(gw.region_of("CCL-B.TO"), ("Canada", "North America"))
        self.assertEqual(gw.region_of("GSK.L"), ("UK", "UK"))
        self.assertEqual(gw.region_of("SAP.DE"), ("Germany", "Western Europe ex-UK"))
        self.assertEqual(gw.region_of("ATCO-B.ST"), ("Sweden", "Nordics"))
        self.assertEqual(gw.region_of("CDR.WA"), ("Poland", "CEE"))
        self.assertEqual(gw.region_of("7309.T"), ("Japan", "Japan"))
        self.assertEqual(gw.region_of("2330.TW"), ("Taiwan", "Greater China"))
        self.assertEqual(gw.region_of("0700.HK"), ("Hong Kong", "Greater China"))
        self.assertEqual(gw.region_of("005930.KS"), ("South Korea", "Korea"))
        self.assertEqual(gw.region_of("COH.AX"), ("Australia", "Other"))

    def test_every_region_is_listed(self):
        for region in gw.REGION_OF_COUNTRY.values():
            self.assertIn(region, gw.REPORT_REGIONS)


def reg_row(key, section, verdict, sf="PASS", sf_reason="n.m.", memo_date="2026-10-01"):
    return {"key": key, "company": key + " Inc.", "section": section, "verdict": verdict, "past": "ADEQUATE",
            "past_reason": "12% ROCE", "future": "ADEQUATE", "future_reason": "n.m.", "sf": sf,
            "sf_reason": sf_reason, "memo_date": memo_date}


class RegisterDiffTests(unittest.TestCase):
    def test_diff(self):
        old = [reg_row("A", "WATCH", "WATCH"), reg_row("B", "AVOID-1", "AVOID", sf="FAIL", sf_reason="buybacks"),
               reg_row("D", "DNAF", "DNAF")]
        new = [reg_row("A", "AVOID-1", "AVOID", sf="FAIL", sf_reason="buybacks", memo_date="2026-10-15"),
               reg_row("B", "AVOID-1", "AVOID", sf="FAIL", sf_reason="compensation"), reg_row("E", "WATCH", "WATCH")]
        d = gw.register_diff(old, new)
        self.assertEqual(([x["key"] for x in d["added"]], [x["key"] for x in d["removed"]],
                          [x["key"] for x in d["changed"]], [x["key"] for x in d["regraded"]]),
                         (["E"], ["D"], ["A"], ["B"]))


TODO_TEXT = """# TODO

## ▶ IDEAS candidates (attended triage)

- 2026-10-05 · X ANALYSE — a question

## ▶ Open items (register)

*intro*

- **HFG.DE (held) SELL-FLAG (SR2, re-affirmed v5 2026-10-08; v4 2026-10-03)** — decision deferred to FY2026 results (~Mar 2027) [user, 2026-08-18]; flag stands.
- **NOVO-B.CO (held) SELL-FLAG (SR2, v9 2026-09-13)** — user decision pending; log the decision here [2026-09-13].
- **ABB — pending re-key (§7.1a)** — target `ABBNY` — user call, then RECONCILE renames memos [2026-09-11].
- **EA — retire (§7.1 RETIRED, v4.6.0)** — retire by an attended register commit [2026-10-06; rewritten 2026-10-15].
- **BOX — register-integrity hold (register v313)** — the next BOX REVIEW writes the ISIN [2026-10-08].

## ▶ Method re-tests v4.6.0

**Held — first.**

- `6383.T` — memo v2 DNAF → run the full analysis
- `DPLM.L` — memo v1
  - sub-bullet `NOT.A.KEY` stays out

## ▶ Method re-tests v4.5.0

- `6383.T` — repeat in the older block
- `NVS` — worth test

## ▶ Routed by INTAKE 2026-10-19, register v318

- `XYZ` — routed, not a head block
"""



# The v4.8.0 release block, read first, with a line a run left part-done (MODEL v4.8.0 two-run resume), an
# unversioned block (not a re-test block) and a future version.
TODO_V480 = """## ▶ Method re-tests v4.8.0

*intro*

- `KSPI` — customer funds net out as NIBCL — partial 2026-11-01 (queue/evidence/KSPI_2026-11-01_INCOMPLETE.md)
- `PYPL` — customer funds — partial 2026-11-02
- `6383.T` — growth n.m.: endpoint read governs

## ▶ Method re-tests (draft, no version)

- `NOPE` — not a release block

## ▶ Method re-tests v10.0.0

- `ZZZ` — a future release

"""


class QueueAndTodoTests(unittest.TestCase):
    def test_blocks_and_retests(self):
        self.assertEqual([t for t, _b in gw.todo_blocks(TODO_TEXT)],
                         ["▶ IDEAS candidates (attended triage)", "▶ Open items (register)",
                          "▶ Method re-tests v4.6.0", "▶ Method re-tests v4.5.0"])
        self.assertEqual(gw.retest_keys(TODO_TEXT)["▶ Method re-tests v4.6.0"], ["6383.T", "DPLM.L"])
        self.assertEqual(dict(gw.retest_lines(TODO_TEXT)), {"▶ Method re-tests v4.6.0": 2,
                                                            "▶ Method re-tests v4.5.0": 2})
        lists = gw.retest_lists_of(TODO_TEXT)
        self.assertEqual(gw.retest_owed(lists, "6383.T", "v4.5.1"), ["v4.6.0"])
        self.assertEqual(gw.retest_owed(lists, "NVS", "v4.5.3"), [])          # v4.5.0 block already run
        self.assertEqual(gw.retest_note(lists, "NVS", "v4.5.3"), "re-test done, line clears at INTAKE")

    def test_version_generic_blocks_and_partial_lines(self):
        text = TODO_TEXT.replace("## ▶ Method re-tests v4.6.0", TODO_V480 + "## ▶ Method re-tests v4.6.0")
        titles = [t for t, _b in gw.todo_blocks(text)]
        self.assertEqual(titles[2:], ["▶ Method re-tests v4.8.0", "▶ Method re-tests (draft, no version)",
                                      "▶ Method re-tests v10.0.0", "▶ Method re-tests v4.6.0",
                                      "▶ Method re-tests v4.5.0"])
        keys = gw.retest_keys(text)
        self.assertEqual(list(keys), ["▶ Method re-tests v4.8.0", "▶ Method re-tests v10.0.0",
                                      "▶ Method re-tests v4.6.0", "▶ Method re-tests v4.5.0"])  # no version: no block
        self.assertEqual(keys["▶ Method re-tests v4.8.0"], ["KSPI", "PYPL", "6383.T"])
        # a partial line is open: it counts in its block and stays owed
        self.assertEqual(dict(gw.retest_lines(text))["▶ Method re-tests v4.8.0"], 3)
        self.assertEqual(gw.retest_partial(text)["▶ Method re-tests v4.8.0"],
                         [("KSPI", "2026-11-01", "queue/evidence/KSPI_2026-11-01_INCOMPLETE.md"),
                          ("PYPL", "2026-11-02", None)])
        self.assertEqual(gw.retest_partial(text)["▶ Method re-tests v4.6.0"], [])
        lists = gw.retest_lists_of(text)
        self.assertEqual(lists["6383.T"], ["v4.8.0", "v4.6.0", "v4.5.0"])
        self.assertEqual(gw.retest_owed(lists, "6383.T", "v4.6.0"), ["v4.8.0"])
        self.assertEqual(gw.retest_owed(lists, "KSPI", "v4.6.0"), ["v4.8.0"])
        self.assertEqual(gw.retest_owed(lists, "KSPI", "v4.8.0"), [])
        self.assertEqual(gw.retest_note(lists, "PYPL", "v4.7.0"), "re-test v4.8.0 owed")
        self.assertEqual(gw.retest_owed(lists, "ZZZ", "v4.8.0"), ["v10.0.0"])
        self.assertNotIn("NOPE", lists)

    def test_open_items(self):
        items = [gw.parse_open_item(x) for x in gw.todo_block(TODO_TEXT, "▶ Open items (register)")]
        by = {i["key"]: i for i in items}
        self.assertTrue(by["HFG.DE"]["held"] and by["HFG.DE"]["sell_flag"] and by["HFG.DE"]["deferred"])
        self.assertEqual(by["HFG.DE"]["since"], "2026-08-18")
        self.assertEqual((by["NOVO-B.CO"]["since"], by["NOVO-B.CO"]["deferred"]), ("2026-09-13", False))
        self.assertTrue(by["ABB"]["user_call"] and not by["ABB"]["held"])
        self.assertEqual(by["EA"]["since"], "2026-10-06")
        self.assertTrue(by["EA"]["user_call"])                 # an attended commit: only Jakub runs one
        self.assertFalse(by["BOX"]["user_call"])               # a routine REVIEW clears it
        self.assertNotIn("**", by["ABB"]["text"])



class TimeAndWindowTests(unittest.TestCase):
    def test_eu_summer_time_edges(self):
        h = datetime.timedelta(hours=1)
        self.assertEqual(gw.prague_offset(datetime.datetime(2026, 10, 25, 0, 59, tzinfo=UTC)), 2 * h)
        self.assertEqual(gw.prague_offset(datetime.datetime(2026, 10, 25, 1, 0, tzinfo=UTC)), h)
        self.assertEqual(gw.prague_offset(datetime.datetime(2026, 3, 29, 1, 0, tzinfo=UTC)), 2 * h)

    def test_parse_when_explicit_only(self):
        want = datetime.datetime(2026, 10, 11, 22, 0, tzinfo=UTC)
        self.assertEqual(when("2026-10-12T00:00+02:00"), want)
        self.assertEqual(when("2026-10-12T00:00"), want)                       # naive = Prague local
        self.assertEqual(when("2026-10-11T22:00:00Z"), want)
        with self.assertRaises(gw.ToolError):
            when("now")

    def test_report_date_is_until_minus_one_second(self):
        self.assertEqual(gw.report_date_of(when("2026-10-20T00:00+02:00")), datetime.date(2026, 10, 19))
        self.assertEqual(gw.report_date_of(when("2026-10-19T23:59+02:00")), datetime.date(2026, 10, 19))
        self.assertEqual(gw.report_date_of(when("2026-10-20T00:00:01+02:00")), datetime.date(2026, 10, 20))

    def test_period_and_iso_week_labels(self):
        since = when("2026-10-12T00:00+02:00")
        self.assertEqual(gw.period_label(since, when("2026-10-20T00:00+02:00")), "Mon 12 Oct – Mon 19 Oct 2026")
        self.assertIsNone(gw.iso_week_label(since, when("2026-10-20T00:00+02:00")))       # 8 days
        self.assertEqual(gw.iso_week_label(since, when("2026-10-19T00:00+02:00")), "2026-W42")
        self.assertEqual(gw.period_label(since, when("2026-10-19T00:00+02:00")), "Mon 12 Oct – Sun 18 Oct 2026")
        self.assertIsNone(gw.iso_week_label(when("2026-10-13T00:00+02:00"), when("2026-10-20T00:00+02:00")))
        # across the autumn DST change the ISO week is still 7 Prague days (169 real hours)
        self.assertEqual(gw.iso_week_label(when("2026-10-19T00:00+02:00"), when("2026-10-26T00:00+01:00")), "2026-W43")
        self.assertEqual(gw.period_label(when("2026-12-28T00:00"), when("2027-01-04T00:00")),
                         "Mon 28 Dec 2026 – Sun 3 Jan 2027")

    def test_format(self):
        self.assertEqual(gw.fmt_when(datetime.datetime(2026, 10, 19, 21, 15, tzinfo=UTC)), "Mon 19 Oct 23:15")
        self.assertEqual(gw.fmt_span(datetime.timedelta(days=3, minutes=23)), "3 d 0 h 23 min")



class CronTests(unittest.TestCase):
    WEEK = (when("2026-10-12T00:00+02:00"), when("2026-10-19T00:00+02:00"))      # W42, no DST change
    PERIOD = (when("2026-10-12T00:00+02:00"), when("2026-10-20T00:00+02:00"))
    # (cron, fires in W42, fires in the 8-day report period)
    HEALTH_EXPECTED = {
        "CRON_TZ=Europe/Prague 0 6 * * *": (7, 8),
        "CRON_TZ=Europe/Prague 30 21,23 * * 0-4": (10, 12),
        "CRON_TZ=Europe/Prague 10 6,21 * * 1-5": (10, 12),
        "CRON_TZ=Europe/Prague 30 6 * * 6": (1, 1),
        "CRON_TZ=Europe/Prague 20 6 * * 1,4": (2, 3),
        "CRON_TZ=Europe/Prague 0 18 * * 6": (1, 1),
        "CRON_TZ=Europe/Prague 0 18-23 * * 5": (6, 6),
        "CRON_TZ=Europe/Prague 40 18-23 * * 5": (6, 6),
        "CRON_TZ=Europe/Prague 20 22,23 * * 5": (2, 2),
        "CRON_TZ=Europe/Prague 26 * * * 6": (24, 24),
        "CRON_TZ=Europe/Prague 40 * * * 6": (24, 24),
        "CRON_TZ=Europe/Prague 20 * * * 6": (24, 24),
        "CRON_TZ=Europe/Prague 0 0-7 * * 0": (8, 8),
        "CRON_TZ=Europe/Prague 40 0-7 * * 0": (8, 8),
        "CRON_TZ=Europe/Prague 20 0-7 * * 0": (8, 8),
    }

    def test_fields(self):
        self.assertEqual(gw.cron_field("*/15", 0, 59), {0, 15, 30, 45})
        self.assertEqual(gw.cron_field("1-5", 0, 7), {1, 2, 3, 4, 5})
        self.assertEqual(gw.cron_field("5/20", 0, 59), {5, 25, 45})
        self.assertEqual(gw.parse_cron("0 0 * * 7")["dow"], {0})                  # 7 is Sunday
        self.assertEqual(gw.parse_cron("0 0 * * *")["tz"], "UTC")
        for bad in ("0 24 * * *", "x 0 * * *", "0 0 * *", "CRON_TZ=America/New_York 0 0 * * *", "*/0 0 * * *"):
            with self.assertRaises(gw.ToolError, msg=bad):
                gw.parse_cron(bad)

    def test_health_expressions_dst_free_week(self):
        crons = {t["cron"] for t in HEALTH_DOC}
        self.assertEqual(crons, set(self.HEALTH_EXPECTED))
        for expr, (week, period) in self.HEALTH_EXPECTED.items():
            self.assertEqual(len(gw.cron_fires(expr, *self.WEEK)), week, expr)
            self.assertEqual(len(gw.cron_fires(expr, *self.PERIOD)), period, expr)
            # a DST-free week before gives the same count
            self.assertEqual(len(gw.cron_fires(expr, when("2026-10-05T00:00+02:00"), when("2026-10-12T00:00+02:00"))),
                             week, expr)

    def test_prague_wall_clock(self):
        fires = gw.cron_fires("CRON_TZ=Europe/Prague 0 6 * * *", when("2026-10-12T00:00+02:00"),
                              when("2026-10-13T00:00+02:00"))
        self.assertEqual(fires, [datetime.datetime(2026, 10, 12, 4, 0, tzinfo=UTC)])
        fires = gw.cron_fires("CRON_TZ=Europe/Prague 0 6 * * *", when("2026-11-02T00:00+01:00"),
                              when("2026-11-03T00:00+01:00"))
        self.assertEqual(fires, [datetime.datetime(2026, 11, 2, 5, 0, tzinfo=UTC)])
        utc = gw.cron_fires("0 6 * * *", when("2026-10-12T00:00Z"), when("2026-10-13T00:00Z"))
        self.assertEqual(utc, [datetime.datetime(2026, 10, 12, 6, 0, tzinfo=UTC)])

    def test_inclusive_exclusive_bounds(self):
        expr = "CRON_TZ=Europe/Prague 0 6 * * *"
        self.assertEqual(len(gw.cron_fires(expr, when("2026-10-12T06:00+02:00"), when("2026-10-13T06:00+02:00"))), 1)

    def test_dst_edges(self):
        # autumn: the repeated 02:30 fires once; spring: the missing 02:30 does not fire
        self.assertEqual(len(gw.cron_fires("CRON_TZ=Europe/Prague 30 2 * * *", when("2026-10-24T00:00+02:00"),
                                           when("2026-10-27T00:00+01:00"))), 3)
        self.assertEqual(len(gw.cron_fires("CRON_TZ=Europe/Prague 30 2 * * *", when("2026-03-28T00:00+01:00"),
                                           when("2026-03-31T00:00+02:00"))), 2)
        self.assertEqual(len(gw.cron_fires("CRON_TZ=Europe/Prague 0 * * * *", when("2026-10-25T00:00+02:00"),
                                           when("2026-10-26T00:00+01:00"))), 24)
        self.assertEqual(len(gw.cron_fires("CRON_TZ=Europe/Prague 0 * * * *", when("2026-03-29T00:00+01:00"),
                                           when("2026-03-30T00:00+02:00"))), 23)

    def test_dom_dow_or(self):
        fires = gw.cron_fires("0 0 13 * 5", when("2026-11-01T00:00Z"), when("2026-12-01T00:00Z"))
        days = sorted({f.day for f in fires})
        self.assertEqual(days, [6, 13, 20, 27])          # Fridays 6, 13, 20, 27 and the 13th (a Friday)
        fires = gw.cron_fires("0 0 1 * 1", when("2026-11-01T00:00Z"), when("2026-11-10T00:00Z"))
        self.assertEqual(sorted({f.day for f in fires}), [1, 2, 9])

    def test_health_view(self):
        h = gw.health_view(gw.load_health(HEALTH), *self.PERIOD)
        self.assertEqual((h["by_job"]["ANALYSE"]["scheduled_base"], h["by_job"]["ANALYSE"]["scheduled_sprint"]), (12, 76))
        self.assertEqual((h["by_job"]["REVIEW"]["scheduled_base"], h["by_job"]["REVIEW"]["scheduled_sprint"]), (12, 34))
        self.assertEqual((h["by_job"]["INTAKE"]["scheduled_base"], h["by_job"]["INTAKE"]["scheduled_sprint"]), (8, 1))
        self.assertEqual(h["by_job"]["SWEEP"]["usage_limit"], 1)
        self.assertEqual(len(h["failures"]), 11)
        self.assertEqual(gw.fires_between(h, when("2026-10-15T21:12+02:00"), when("2026-10-18T21:36+02:00"), False), 9)



RETIRED_POSITIVE = {      # memo section-1 grounds copied from the memos at d989ade
    "6383.T": "one-level decomposition: a material \"Other\" unit",
    "BNZL.L": "one-level decomposition: the North America unit combines sub-businesses that differ in paying "
              "customer, named by the filer without their shares",
    "BRK.B": "too hard, R4(b): material non-captive licensed insurers; the Manufacturing unit is also irreducible",
    "DOV": "one-level decomposition: the material Climate & Sustainability Technologies and Engineered Products units "
           "are irreducible",
    "RSW.L": "one-level decomposition: a material residual unit that mixes industries",
    "ANDR.VI": "one-level decomposition: two material units each combine sub-businesses with different paying "
               "customers, shares not given",
}
RETIRED_NEGATIVE = (
    # SYAB.DE memo section 1 (no listed security; DNAF before RETIRED existed)
    "SYNLAB AG — Munich-based European clinical-laboratory and medical-diagnostics group (FY2024 revenue €2.62bn, "
    "sourced) — has no publicly tradeable security.",
    # EA memo section 1 (an AVOID memo)
    "Two gates fail independently, and the stock is contractually leaving the market anyway.",
    # a v4.6.0 P30 ground
    "P30 obfuscation: no segment, product or customer disclosure describes more than half of revenue",
    # a WATCH memo's verdict line
    "All three gates pass; the price is above the trigger.",
)


def memo(verdict, model, ground):
    fm = "---\nverdict: %s\nmodel_version: %s\nmemo_date: 2026-10-14\n---\n" % (verdict, model)
    return fm + "# X — X: GSC Memo\n\n## 1. Verdict\nUnderstanding FAIL (%s) → DO NOT ANALYSE FURTHER.\n\n## 2. " \
                "Understanding\nText.\n" % ground


class RetiredGroundTests(unittest.TestCase):
    def test_constant_is_documented(self):
        self.assertEqual(gw.RETIRED_GATE0_VERSION, "v4.6.0")
        self.assertEqual([n for n, _p in gw.RETIRED_GATE0_GROUNDS],
                         ["irreducible unit (one-level decomposition)", "J13 limb (named without shares)",
                          "material Other", "R4 too-hard pile", "holdings cycle"])

    def test_positive_grounds(self):
        want = {"6383.T": {"material Other"}, "BNZL.L": {"J13 limb (named without shares)"},
                "BRK.B": {"R4 too-hard pile"}, "RSW.L": {"material Other"},
                "ANDR.VI": {"J13 limb (named without shares)"}}
        for key, ground in RETIRED_POSITIVE.items():
            names = set(gw.retired_grounds(ground))
            if key != "BRK.B":
                self.assertIn("irreducible unit (one-level decomposition)", names, key)
            self.assertTrue(names >= want.get(key, set()), (key, names))
            check = gw.retired_check(gw.reg.parse_front_matter(memo("DNAF", "v4.5.3", ground)),
                                     memo("DNAF", "v4.5.3", ground), "v4.6.0")
            self.assertTrue(check["retired"], key)
        self.assertEqual(gw.retired_grounds("a cycle of holdings lets the controller vote group shares"),
                         ["holdings cycle"])

    def test_negative_grounds(self):
        for ground in RETIRED_NEGATIVE:
            self.assertEqual(gw.retired_grounds(ground), [], ground)
            text = memo("DNAF", "v4.5.3", ground)
            self.assertFalse(gw.retired_check(gw.reg.parse_front_matter(text), text, "v4.6.0")["retired"])

    def test_version_rules(self):
        ground = RETIRED_POSITIVE["DOV"]
        for verdict, model, live, want in (("DNAF", "v4.5.3", "v4.6.0", True),
                                           ("DNAF", "v4.6.0", "v4.6.0", False),     # written under the new rules
                                           ("DNAF", "v4.5.3", "v4.5.3", False),     # the ground was live then
                                           ("AVOID", "v4.5.3", "v4.6.0", False),    # not a DNAF memo
                                           ("DNAF", "", "v4.6.0", False)):          # no model_version
            text = memo(verdict, model, ground)
            self.assertEqual(gw.retired_check(gw.reg.parse_front_matter(text), text, live)["retired"], want,
                             (verdict, model, live))

    @unittest.skipUnless(os.path.exists(os.path.join(REPO, ".git")), "repository not present")
    def test_real_memos(self):
        repo = gw.Repo(REPO)
        sha = FIXED_SHA if have_commit(FIXED_SHA) else None
        if sha is None:
            self.skipTest("fixed commit not present")
        cases = {"memos/6383.T/6383.T_2026-10-08_GSC.md": True, "memos/BNZL.L/BNZL.L_2026-10-13_GSC.md": True,
                 "memos/BRK.B/BRK.B_2026-10-15_GSC.md": True, "memos/DOV/DOV_2026-10-14_GSC.md": True,
                 "memos/SYAB.DE/SYAB.DE_2026-07-23_GSC.md": False, "memos/EA/EA_2026-07-11_GSC.md": False,
                 "memos/CCL-B.TO/CCL-B.TO_2026-10-19_GSC.md": False}
        for path, want in cases.items():
            text = repo.show(sha, path)
            self.assertIsNotNone(text, path)
            self.assertEqual(gw.retired_check(gw.reg.parse_front_matter(text), text, "v4.6.0")["retired"], want, path)



class FakeRepo:
    """ls / batch / show over an in-memory tree, enough for pending_overlay."""

    def __init__(self, files):
        self.files = files

    def ls(self, sha, prefix):
        return sorted(p for p in self.files if p.startswith(prefix))

    def batch(self, sha, paths):
        return {p: self.files[p] for p in paths if p in self.files}

    def show(self, sha, path):
        return self.files.get(path)


def row_file(row_type, key, memo_path="", model="v4.5.3"):
    return "---\nrow_type: %s\nkey: %s\ncompany: %s Corp\nmemo_path: %s\nmodel_version: %s\npr_title: GSC %s %s\n" \
           "---\n## Register row (new)\n" % (row_type, key, key, memo_path, model, row_type, key)


def memo_text(verdict, past="ADEQUATE", future="ADEQUATE", sf="PASS", date="2026-10-14", model="v4.5.3",
              ground="one-level decomposition: the material X unit is irreducible"):
    return ("---\nverdict: %s\nquality_past: %s\nquality_future: %s\nsf: %s\nmemo_date: %s\nmodel_version: %s\n"
            "company: Co\n---\n## 1. Verdict\nUnderstanding FAIL (%s) → DO NOT ANALYSE FURTHER.\n" % (
                verdict, past, future, sf, date, model, ground))


class PendingOverlayTests(unittest.TestCase):
    def setUp(self):
        self.rows = [dict(reg_row("DOV", "WATCH", "WATCH"), held="false"),
                     dict(reg_row("BMI", "WATCH", "WATCH"), held="false"),
                     dict(reg_row("TROW", "AVOID-2", "AVOID"), held="true"),
                     dict(reg_row("COLO", "WATCH", "WATCH"), held="false"),
                     dict(reg_row("OLD", "WATCH", "WATCH"), held="false")]
        files = {
            "queue/rows/README.md": "framework",
            "queue/rows/2026-10-14_0611_REVIEW_DOV.md": row_file("REVIEW", "DOV", "memos/DOV/DOV_2026-10-14_GSC.md"),
            "queue/rows/2026-10-19_0611_REVIEW_BMI.md": row_file("REVIEW", "BMI", "memos/BMI/BMI_2026-10-19_GSC.md"),
            "queue/rows/2026-10-19_2112_REVIEW_TROW.md": row_file("REVIEW", "TROW", "memos/TROW/TROW_2026-10-19_GSC.md"),
            "queue/rows/2026-10-15_2111_REVIEW_COLO.md": row_file("INCOMPLETE", "COLO"),
            "queue/rows/2026-10-19_2131_ANALYSE_NEW.md": row_file("ANALYSE", "NEW", "memos/NEW/NEW_2026-10-19_GSC.md"),
            "queue/rows/2026-10-10_0611_REVIEW_OLD.md": row_file("REVIEW", "OLD", "memos/OLD/OLD_2026-10-10_GSC.md"),
            "queue/rows/2026-10-19_0700_SWEEP.md": "---\nrow_type: SWEEP\n---\n",
            "archive/memos/OLD/OLD_2026-10-10_GSC.md": memo_text("AVOID"),
        }
        self.memos = {
            "DOV": {"path": "memos/DOV/DOV_2026-10-14_GSC.md", "text": memo_text("DNAF")},
            "BMI": {"path": "memos/BMI/BMI_2026-10-19_GSC.md", "text": memo_text("AVOID", sf="FAIL", date="2026-10-19")},
            "TROW": {"path": "memos/TROW/TROW_2026-10-19_GSC.md",
                     "text": memo_text("AVOID", past="WEAK", future="WEAK", sf="FAIL", date="2026-10-19", model="v4.6.0")},
            "NEW": {"path": "memos/NEW/NEW_2026-10-19_GSC.md",
                    "text": memo_text("AVOID", past="WEAK", date="2026-10-19", model="v4.6.0")},
            "OLD": {"path": "memos/OLD/OLD_2026-10-12_GSC.md", "text": memo_text("WATCH", date="2026-10-12")},
        }
        for m in self.memos.values():
            m["fm"] = gw.reg.parse_front_matter(m["text"])
        self.overlay, self.keyless = gw.pending_overlay(FakeRepo(files), "x", self.rows, self.memos, "v4.6.0")

    def test_labels_and_states(self):
        o = self.overlay
        self.assertEqual(o["DOV"]["label"], "pending: DNAF (memo 2026-10-14)")
        self.assertTrue(o["DOV"]["changes"] and o["DOV"]["retired"])
        self.assertEqual((o["BMI"]["label"], o["BMI"]["section"], o["BMI"]["changes"]),
                         ("pending: AVOID (memo 2026-10-19)", "AVOID-1", True))
        self.assertEqual((o["TROW"]["section"], o["TROW"]["changes"]), ("AVOID-2", False))
        self.assertEqual((o["COLO"]["label"], o["COLO"]["changes"]), ("pending: INCOMPLETE (no memo)", False))
        self.assertTrue(o["NEW"]["new_key"])
        self.assertEqual(o["OLD"]["state"], "superseded")                 # its memo moved to archive/memos
        self.assertFalse(o["OLD"]["changes"])
        self.assertEqual([k["row_type"] for k in self.keyless], ["SWEEP"])

    def test_after_pending_counts(self):
        after = {r["key"]: r for r in gw.rows_after_pending(self.rows, self.overlay)}
        self.assertEqual(len(after), 6)
        self.assertEqual((after["DOV"]["section"], after["BMI"]["section"], after["NEW"]["section"]),
                         ("DNAF", "AVOID-1", "AVOID-1"))
        self.assertEqual(after["COLO"]["section"], "WATCH")
        self.assertEqual(sum(1 for r in after.values() if r["section"] == "WATCH"), 2)    # COLO, OLD


class MemoHistoryTests(unittest.TestCase):
    def commit(self, subject, raw, minute):
        return {"sha": "s%d" % minute, "when": datetime.datetime(2026, 8, 1, 0, minute, tzinfo=UTC),
                "subject": subject, "raw": raw}

    def test_classification(self):
        z = "0" * 40
        commits = [
            self.commit("GSC: ABC v1 AVOID", [("A", z, "b1", "memos/ABC_2026-07-01_GSC.md")], 1),
            self.commit("GSC: ABC v2 WATCH", [("A", z, "b2", "memos/ABC_2026-08-01_GSC.md")], 2),
            # path migration: the same blobs move into memos/{KEY}/
            self.commit("GSC: MODEL v4.2.1 (PATCH — paths)",
                        [("D", "b1", z, "memos/ABC_2026-07-01_GSC.md"), ("A", z, "b1", "memos/ABC/ABC_2026-07-01_GSC.md"),
                         ("D", "b2", z, "memos/ABC_2026-08-01_GSC.md"), ("A", z, "b2", "memos/ABC/ABC_2026-08-01_GSC.md")],
                        3),
            # re-key with an edited body (new blob), in its own commit
            self.commit("RECONCILE v4.1.0 §7.1a: re-key ABC -> ABC.DE (ABC_2026-08-01_GSC.md)",
                        [("A", z, "b3", "memos/ABC.DE/ABC.DE_2026-08-01_GSC.md")], 4),
            # a REVIEW moves the old memo to archive and adds a new one
            self.commit("GSC REVIEW ABC.DE 2026-09-01 — AVOID (SF) (#5)",
                        [("D", "b3", z, "memos/ABC.DE/ABC.DE_2026-08-01_GSC.md"),
                         ("A", z, "b3", "archive/memos/ABC.DE/ABC.DE_2026-08-01_GSC.md"),
                         ("A", z, "b4", "memos/ABC.DE/ABC.DE_2026-09-01_GSC.md")], 5),
            self.commit("GSC ANALYSE XYZ 2026-09-02 — DNAF (Gate 0) (#6)",
                        [("A", z, "b5", "memos/XYZ/XYZ_2026-09-02_GSC.md"), ("A", z, "b6", "queue/rows/r.md")], 6),
        ]
        events = gw.memo_history(commits)
        self.assertEqual([(e["key"], e["job"]) for e in events],
                         [("ABC", "ANALYSE"), ("ABC", "REVIEW"), ("ABC.DE", "REVIEW"), ("XYZ", "ANALYSE")])


HELD_LINES = {   # the held SELL-FLAG Open items as Jakub's decisions of 2026-10-20 log them
    "HFG.DE": "- **HFG.DE (held) SELL-FLAG (SR2, re-affirmed v5 2026-10-08 under the v4.5.0 method re-test; v4 "
              "2026-10-03)** — decision deferred to FY2026 results (~Mar 2027) [user, 2026-08-18]; HOLD confirmed "
              "[user, 2026-10-20]: flag acknowledged and the analysis agreed, no better business in sight; flag "
              "stands; log the decision + realised outcome here.",
    "NOVO-B.CO": "- **NOVO-B.CO (held) SELL-FLAG (SR2, v9 2026-09-13; re-affirmed v11 2026-10-08 — Future WEAK + SF "
                 "FAIL)** — decision HOLD [user, 2026-10-20]: flag acknowledged and the analysis agreed; held while no "
                 "better business is in sight; flag stands; log any change + realised outcome here [2026-09-13].",
    "CROX": "- **CROX (held) SELL-FLAG (SR2, v8 2026-10-07)** — user decision pending; log the decision + realised "
            "outcome here [2026-10-07].",
    "TROW": "- **TROW (held) SELL-FLAG (SR2, v6 routine 2026-10-08)** — decision deferred to Q4 results "
            "[user, 2026-10-21]; flag stands [2026-10-08].",
}
OVER_CAP = ("- `SYAB.DE` — open item (over the 7-entry cap of `▶ Open items (register)`, routed here by the MODEL "
            "v4.6.0 build): SYAB.DE — retire: delisting awaiting retirement (§7.1 RETIRED, v4.6.0) — Retire by an "
            "attended register commit.")


class OpenItemDecisionTests(unittest.TestCase):
    def test_hold_and_deferral(self):
        hfg = gw.parse_open_item(HELD_LINES["HFG.DE"])
        self.assertEqual((hfg["hold_on"], hfg["deferred_on"], hfg["since"]), ("2026-10-20", "2026-08-18", "2026-08-18"))
        self.assertEqual(hfg["deferred_to"], "to FY2026 results (~Mar 2027)")
        self.assertEqual(gw.held_status(hfg), ("hold", "held by your decision on 2026-10-20 (decision deferred to "
                                                       "FY2026 results (~Mar 2027) on 2026-08-18)"))
        novo = gw.parse_open_item(HELD_LINES["NOVO-B.CO"])
        self.assertEqual((novo["hold_on"], novo["deferred"], novo["since"]), ("2026-10-20", False, "2026-09-13"))
        self.assertEqual(gw.held_status(novo), ("hold", "held by your decision on 2026-10-20"))
        crox = gw.parse_open_item(HELD_LINES["CROX"])
        self.assertEqual((crox["hold_on"], crox["deferred"]), (None, False))
        self.assertEqual(gw.held_status(crox), ("pending", "your decision pending"))
        trow = gw.parse_open_item(HELD_LINES["TROW"])
        self.assertEqual(gw.held_status(trow), ("deferred", "decision deferred by you to Q4 results on 2026-10-21"))
        self.assertEqual(trow["since"], "2026-10-08")
        self.assertEqual(gw.held_status(None), (None, "no open item"))

    def test_hold_word_needs_a_user_mark(self):
        item = gw.parse_open_item("- **X (held) SELL-FLAG (SR2)** — the zone moved HOLD → SELL-FLAG [2026-10-01].")
        self.assertIsNone(item["hold_on"])

    def test_over_cap_lines(self):
        text = "## ▶ Open items (register)\n\n- **A — user call** [2026-10-01].\n\n## ▶ Routed by the MODEL v4.6.0 " \
               "build (2026-10-15)\n\n" + OVER_CAP + "\n- `X` — not an open item\n"
        lines = gw.over_cap_items(text)
        self.assertEqual(lines, [(OVER_CAP, "2026-10-15")])
        item = gw.parse_open_item(*lines[0])
        self.assertEqual((item["key"], item["over_cap"], item["retire"], item["since"]),
                         ("SYAB.DE", True, True, "2026-10-15"))
        self.assertTrue(item["text"].startswith("SYAB.DE — retire"))
        self.assertFalse(gw.parse_open_item("- **ABB — re-key** — bare `ABB` is a retired NYSE line [2026-09-11].")
                         ["retire"])


class WindowTests(unittest.TestCase):
    def test_sunday_anchor_and_catch_ups(self):
        want = (when("2026-10-18T08:30+02:00"), when("2026-10-25T08:30+01:00"))
        for at in ("2026-10-25T08:30+01:00", "2026-10-25T08:40+01:00", "2026-10-25T09:10+01:00", "2026-10-25T21:40+01:00",
                   "2026-10-26T06:40+01:00", "2026-10-31T23:59+01:00", "2026-11-01T08:29+01:00"):
            self.assertEqual(gw.window_of(when(at)), want, at)
        self.assertEqual(gw.window_of(when("2026-10-25T08:29+01:00")),
                         (when("2026-10-11T08:30+02:00"), when("2026-10-18T08:30+02:00")))
        # 08:40 written with the summer offset is 07:40 Prague on the change day: the week before
        self.assertEqual(gw.window_of(when("2026-10-25T08:40+02:00"))[1], when("2026-10-18T08:30+02:00"))

    def test_dst_weeks(self):
        since, until = gw.window_of(when("2026-10-25T08:40+01:00"))
        self.assertEqual(until - since, datetime.timedelta(hours=169))
        since, until = gw.window_of(when("2027-03-28T08:40+02:00"))
        self.assertEqual((since, until), (when("2027-03-21T08:30+01:00"), when("2027-03-28T08:30+02:00")))
        self.assertEqual(until - since, datetime.timedelta(hours=167))
        since, until = gw.window_of(when("2026-11-02T06:40+01:00"))
        self.assertEqual(until - since, datetime.timedelta(days=7))

    def test_window_doc_and_published(self):
        doc = gw.window_doc(when("2026-10-26T06:40+01:00"))
        self.assertEqual(doc, {"since": "2026-10-18T08:30:00+02:00", "until": "2026-10-25T08:30:00+01:00",
                               "period": "Sun 18 Oct – Sun 25 Oct 2026", "details_since": "2026-10-04T06:30:00Z",
                               "run": "2026-10-26T06:40:00+01:00"})
        self.assertNotIn("published", doc)
        at = when("2026-10-25T21:40+01:00")
        self.assertTrue(gw.window_doc(at, "2026-10-25T08:41:07+01:00", gw.WEEKLY_BY)["published"])
        self.assertTrue(gw.window_doc(at, "2026-10-25T07:30:00Z", gw.WEEKLY_BY)["published"])          # == until
        self.assertFalse(gw.window_doc(at, "2026-10-25T07:29:59Z", gw.WEEKLY_BY)["published"])
        self.assertFalse(gw.window_doc(at, "2026-10-25T08:41:07+01:00", "Claude (attended)")["published"])
        self.assertFalse(gw.window_doc(at, "-", "-")["published"])
        self.assertFalse(gw.window_doc(at, "not a time", gw.WEEKLY_BY)["published"])
        # a stamp after the run never counts: a mistyped {RUN} (a wrong year) would silence every later week
        self.assertFalse(gw.window_doc(at, "2027-10-25T08:41:07+01:00", gw.WEEKLY_BY)["published"])
        self.assertTrue(gw.window_doc(at, "2026-10-25T21:44:59+01:00", gw.WEEKLY_BY)["published"])    # within 5 min
        self.assertFalse(gw.window_doc(at, "2026-10-25T21:45:01+01:00", gw.WEEKLY_BY)["published"])
        self.assertFalse(gw.window_doc(when("2026-11-01T08:40+01:00"), "2027-10-25T08:41:07+01:00",
                                       gw.WEEKLY_BY)["published"])                                     # it heals
        code, out, _err = run_main(["window", "--at", "2026-10-25T21:40:00+01:00", "--meta-at",
                                    "2026-10-25T08:41:07+01:00", "--meta-by", gw.WEEKLY_BY])
        self.assertEqual((code, json.loads(out)["published"]), (0, True))
        code, _out, err = run_main(["window", "--at", "now"])
        self.assertEqual(code, 2)
        self.assertIn("not an ISO time", err)

    def alarm(self, at, meta_at="-", meta_by="-"):
        return gw.window_doc(when(at), meta_at, meta_by)["alarm"]

    def test_alarm_on_the_monday_after_a_missed_week(self):
        # the week Sun 25 Oct 08:30 – Sun 1 Nov 08:30 2026 (CET) with no report
        for at, want in (("2026-11-01T09:10+01:00", False),     # Sunday: WEEKLY's own day
                         ("2026-11-01T21:00+01:00", False),
                         ("2026-11-02T05:59+01:00", False),     # Monday before 06:00
                         ("2026-11-02T05:59:59+01:00", False),
                         ("2026-11-02T06:00+01:00", True),      # the Monday INTAKE
                         ("2026-11-02T06:03:41+01:00", True),
                         ("2026-11-02T05:00:00Z", True),        # 06:00 Prague written in UTC
                         ("2026-11-02T23:59+01:00", True),
                         ("2026-11-03T06:00+01:00", False),     # Tuesday: never again for that week
                         ("2026-11-07T18:00+01:00", False),     # the Saturday sprint INTAKE
                         ("2026-11-08T06:00+01:00", False)):    # Sunday daily INTAKE (before the new week's end)
            self.assertEqual(self.alarm(at), want, at)
        doc = gw.window_doc(when("2026-11-02T06:00+01:00"), "-", "-")
        self.assertEqual((doc["period"], doc["published"], doc["meta_ok"]),
                         ("Sun 25 Oct – Sun 1 Nov 2026", False, False))
        self.assertNotIn("alarm", gw.window_doc(when("2026-11-02T06:00+01:00")))      # WEEKLY step 2: no meta
        # a stamp from the week before is not this week's report
        self.assertTrue(self.alarm("2026-11-02T06:00+01:00", "2026-10-25T09:12:00+01:00", gw.WEEKLY_BY))

    def test_published_or_attended_stamp(self):
        mon = "2026-11-02T06:00+01:00"
        self.assertFalse(self.alarm(mon, "2026-11-01T09:14:02+01:00", gw.WEEKLY_BY))   # published Sunday
        self.assertFalse(self.alarm(mon, "2026-11-01T07:30:00Z", gw.WEEKLY_BY))        # stamp == until
        self.assertFalse(self.alarm(mon, "2026-11-02T06:04:59+01:00", gw.WEEKLY_BY))   # within 5 min of the run
        self.assertTrue(self.alarm(mon, "2026-11-01T09:14:02+01:00", "Claude (attended)"))   # attended stamp only
        self.assertTrue(self.alarm(mon, "2026-11-02T06:05:01+01:00", gw.WEEKLY_BY))    # a stamp after the run
        doc = gw.window_doc(when(mon), "2026-11-01T09:14:02+01:00", "Claude (attended)")
        self.assertEqual((doc["published"], doc["meta_ok"], doc["alarm"]), (False, True, True))
        doc = gw.window_doc(when(mon), "not a time", gw.WEEKLY_BY)
        self.assertEqual((doc["published"], doc["meta_ok"], doc["alarm"]), (False, False, True))
        self.assertFalse(gw.window_doc(when(mon), "2026-11-01T09:14:02+01:00", "-")["meta_ok"])
        self.assertTrue(gw.window_doc(when(mon), "2026-11-01T09:14:02+01:00", gw.WEEKLY_BY)["meta_ok"])
        self.assertFalse(gw.window_doc(when("2026-11-03T06:00+01:00"), "not a time", "-")["alarm"])

    def test_alarm_across_dst(self):
        # autumn: clocks went back on Sun 25 Oct 2026 (03:00 CEST -> 02:00 CET); the week ends 08:30 CET
        self.assertEqual(gw.window_doc(when("2026-10-26T06:00+01:00"), "-", "-")["until"], "2026-10-25T08:30:00+01:00")
        self.assertTrue(self.alarm("2026-10-26T06:00+01:00"))
        self.assertTrue(self.alarm("2026-10-26T05:00:00Z"))
        self.assertFalse(self.alarm("2026-10-26T04:59:59Z"))
        self.assertFalse(self.alarm("2026-10-26T06:00+02:00"))        # 05:00 CET written with the summer offset
        self.assertFalse(self.alarm("2026-10-25T21:40+01:00"))        # the Sunday catch-up's day
        # spring: clocks go forward on Sun 28 Mar 2027 (02:00 CET -> 03:00 CEST); the week ends 08:30 CEST
        self.assertEqual(gw.window_doc(when("2027-03-29T06:00+02:00"), "-", "-")["until"], "2027-03-28T08:30:00+02:00")
        self.assertTrue(self.alarm("2027-03-29T06:00+02:00"))
        self.assertTrue(self.alarm("2027-03-29T04:00:00Z"))
        self.assertFalse(self.alarm("2027-03-29T03:59:59Z"))
        self.assertTrue(self.alarm("2027-03-29T06:00+01:00"))         # 07:00 CEST
        self.assertFalse(self.alarm("2027-03-30T06:00+02:00"))
        self.assertFalse(self.alarm("2027-03-29T06:00+02:00", "2027-03-28T09:12:00+02:00", gw.WEEKLY_BY))

    def test_cli_alarm(self):
        code, out, _err = run_main(["window", "--at", "2026-11-02T06:01:12+01:00", "--meta-at", "-", "--meta-by", "-"])
        doc = json.loads(out)
        self.assertEqual((code, doc["published"], doc["meta_ok"], doc["alarm"]), (0, False, False, True))
        code, out, _err = run_main(["window", "--at", "2026-11-02T06:01:12+01:00", "--meta-at",
                                    "2026-11-01T09:14:02+01:00", "--meta-by", gw.WEEKLY_BY])
        self.assertEqual((code, json.loads(out)["alarm"]), (0, False))
        # v4.8.0 review: a writer other than the routine is passed as 'other' (INTAKE step 0, WEEKLY step 3):
        # a readable stamp, never published, so the Monday run alarms with 'no report'.
        code, out, _err = run_main(["window", "--at", "2026-11-02T06:01:12+01:00", "--meta-at",
                                    "2026-11-01T09:14:02+01:00", "--meta-by", "other"])
        doc = json.loads(out)
        self.assertEqual((code, doc["published"], doc["meta_ok"], doc["alarm"]), (0, False, True, True))


class HealthInputTests(unittest.TestCase):
    def test_array_form_and_queue_seed(self):
        doc = gw.load_health(HEALTH)
        self.assertEqual(len(doc["triggers"]), 15)
        self.assertEqual(sum(1 for t in doc["triggers"] if t["job"] == "SEED"), 1)
        self.assertEqual(doc["disabled"], [])

    def test_object_form_and_weekly_routine(self):
        path = os.path.join(TMP, "health_obj.json")
        rows = HEALTH_DOC + [{"name": "GSC WEEKLY", "job": "WEEKLY", "cron": "CRON_TZ=Europe/Prague 10 9 * * 0",
                              "enabled": True, "sprint": False, "last_run": None},
                             {"name": "GSC BURST", "job": "REVIEW", "cron": "0 0 * * *", "enabled": False,
                              "sprint": False, "last_run": None}]
        with open(path, "w", encoding="utf-8") as fh:
            json.dump({"source": "x", "read_at": "2026-10-19T21:30:00Z", "triggers": rows}, fh)
        doc = gw.load_health(path)
        self.assertEqual(doc["disabled"], ["GSC BURST"])
        h = gw.health_view(doc, when("2026-10-18T08:30+02:00"), when("2026-10-25T08:30+01:00"))
        self.assertEqual(h["by_job"]["WEEKLY"]["scheduled_base"], 1)
        self.assertNotIn("WEEKLY", [p for p in gw.JOBS])

    def test_list_triggers_status_words(self):
        path = os.path.join(TMP, "health_raw.json")
        rows = [{"name": "GSC SWEEP", "job": "SWEEP", "cron": "CRON_TZ=Europe/Prague 30 6 * * 6", "enabled": True,
                 "sprint": False, "last_run": {"status": "ROUTINE_RUN_STATUS_FAILED", "fired_at": "2026-10-17T04:33:20Z",
                                               "failure_reason": "ROUTINE_RUN_FAILURE_REASON_USAGE_LIMIT_REACHED"}},
                {"name": "GSC INTAKE", "job": "INTAKE", "cron": "CRON_TZ=Europe/Prague 0 6 * * *", "enabled": True,
                 "sprint": False, "last_run": {"status": "ROUTINE_RUN_STATUS_SUCCEEDED", "fired_at": "2026-10-20T04:03:29Z",
                                               "failure_reason": "ROUTINE_RUN_FAILURE_REASON_UNSPECIFIED"}},
                {"name": "GSC BURST", "job": "REVIEW", "cron": "CRON_TZ=Europe/Prague 5 0-3 8 10 *", "enabled": False,
                 "sprint": False, "last_run": None}]
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(rows, fh)
        doc = gw.load_health(path)
        self.assertEqual([(t["last_run"] or {}).get("status") for t in doc["triggers"]], ["FAILED", "SUCCEEDED", None])
        self.assertEqual(doc["triggers"][0]["last_run"]["failure_reason"], "USAGE_LIMIT_REACHED")
        self.assertIsNone(doc["triggers"][1]["last_run"]["failure_reason"])
        h = gw.health_view(doc, when("2026-10-18T08:30+02:00"), when("2026-10-25T08:30+01:00"))
        self.assertEqual(([t["name"] for t in h["failures"]], h["by_job"]["SWEEP"]["usage_limit"]), (["GSC SWEEP"], 1))
        self.assertEqual(doc["disabled"], ["GSC BURST"])

    def test_optional_run_times(self):
        doc = gw.load_health(HEALTH)                          # no finished_at at all: still read
        h = gw.health_view(doc, when("2026-10-18T08:30+02:00"), when("2026-10-25T08:30+01:00"))
        self.assertTrue(all(t["last_duration_s"] is None for t in h["triggers"]))
        path = os.path.join(TMP, "health_times.json")
        rows = [health_row("GSC INTAKE", "INTAKE", "SUCCEEDED", "2026-10-26T05:00:10Z", "2026-10-26T05:07:40Z"),
                health_row("GSC SWEEP", "SWEEP", "SUCCEEDED", "2026-10-24T04:30:00Z", None),
                health_row("GSC ODD", "REVIEW", "SUCCEEDED", "2026-10-24T04:30:00Z", "2026-10-24T04:29:00Z")]
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(rows, fh)
        h = gw.health_view(gw.load_health(path), when("2026-10-18T08:30+02:00"), when("2026-10-25T08:30+01:00"))
        self.assertEqual([t["last_duration_s"] for t in h["triggers"]], [450, None, None])
        for field, value in (("fired_at", "yesterday"), ("finished_at", "2026-13-01T00:00:00Z"), ("finished_at", 5)):
            bad = [dict(rows[0], last_run=dict(rows[0]["last_run"], **{field: value}))]
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(bad, fh)
            with self.assertRaises(gw.ToolError, msg=repr(value)) as caught:
                gw.load_health(path)
            self.assertIn("bad last_run " + field, str(caught.exception))

    def test_bad_input(self):
        for bad in ({"triggers": [{"name": "x", "job": "DIGEST", "cron": "0 0 * * *", "enabled": True,
                                   "sprint": False}]}, {"no": "triggers"}, "text",
                    [{"name": "x", "job": "INTAKE", "cron": "0 6 * * *", "enabled": True, "sprint": False,
                      "last_run": "FAILED"}],
                    [{"name": "x", "job": "INTAKE", "cron": "0 25 * * *", "enabled": True, "sprint": False}]):
            path = os.path.join(TMP, "health_bad.json")
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(bad, fh)
            with self.assertRaises(gw.ToolError, msg=repr(bad)):
                gw.load_health(path)


def health_row(name, job, status, fired, finished, sprint=False, cron="CRON_TZ=Europe/Prague 0 6 * * *"):
    """One routine as WEEKLY step 5 writes it, with the last run's fire and finish times."""
    return {"name": name, "job": job, "cron": cron, "enabled": True, "sprint": sprint,
            "last_run": {"status": status, "fired_at": fired, "finished_at": finished, "failure_reason": None}}


def pr_rows_of(prs):
    """The build's pr_rows from raw PRs."""
    return [{"pr": pr, "parsed": gw.parse_title(pr.get("title")), "created": gw.parse_gh_time(pr.get("created_at")),
             "merged": gw.parse_gh_time(pr.get("merged_at")), "closed": gw.parse_gh_time(pr.get("closed_at"))}
            for pr in prs]


# The smallest context attention() reads: nothing to report but what a test puts in.
ATTENTION_BASE = {
    "en": {"rows": [], "shortlist": [], "overlay": {}, "keyless_rows": [], "ranked": [], "overdue_watch": [],
           "dnaf_after": {}},
    "report_date": datetime.date(2026, 11, 1), "until": when("2026-11-01T08:30+01:00"), "held_now": [],
    "open_items_parsed": [], "held_prs": [], "zone_changes": [], "events": [], "health_problem": None, "health": None,
    "noop_runs": [], "last_run": {"SWEEP": (when("2026-10-31T07:00+01:00"), 302, "60/62 priced")}, "sweeps_ever": 1,
    "gap": None, "gap_fires": None, "stopped": [], "incomplete_prs": [], "abandoned": [], "workflow_failures": [],
    "finished_waiting": [], "open_old": [], "running_old": [], "watched_changes": [], "superseded": [], "timeline": [],
}


class NoopRunTests(unittest.TestCase):
    """A routine whose last run SUCCEEDED in under 120 s and opened no PR of its job (MODEL v4.8.0)."""
    PERIOD = (when("2026-10-25T08:30+01:00"), when("2026-11-01T08:30+01:00"))
    ROWS = [
        # flagged: 45 s, no ANALYSE PR (an INTAKE PR in its span does not count)
        health_row("GSC ANALYSE", "ANALYSE", "SUCCEEDED", "2026-10-29T20:30:20Z", "2026-10-29T20:31:05Z"),
        # not flagged: its REVIEW PR (a HELD one) opened 3 min after the fire
        health_row("GSC REVIEW", "REVIEW", "SUCCEEDED", "2026-10-29T05:10:00Z", "2026-10-29T05:10:50Z"),
        # not flagged: 120 s is not under 120 s; flagged: 119 s
        health_row("GSC INTAKE", "INTAKE", "SUCCEEDED", "2026-10-30T05:00:00Z", "2026-10-30T05:02:00Z"),
        health_row("GSC SPRINT INTAKE - Sat 18:00", "INTAKE", "SUCCEEDED", "2026-10-31T17:00:00Z",
                   "2026-10-31T17:01:59Z", sprint=True),
        # not flagged: a SWEEP PR was open at the fire (SWEEP stops at once, legitimately)
        health_row("GSC SWEEP", "SWEEP", "SUCCEEDED", "2026-10-31T05:30:00Z", "2026-10-31T05:30:40Z"),
        # flagged: the only SEED PR closed before the fire
        health_row("GSC QUEUE-SEED", "QUEUE-SEED", "SUCCEEDED", "2026-10-29T05:20:00Z", "2026-10-29T05:20:30Z"),
        # never flagged: WEEKLY opens no PR (INTAKE's watchdog covers it); FAILED runs are listed as failures
        health_row("GSC WEEKLY", "WEEKLY", "SUCCEEDED", "2026-11-01T08:10:00Z", "2026-11-01T08:10:20Z",
                   cron="CRON_TZ=Europe/Prague 10 9 * * 0"),
        health_row("GSC ANALYSE B", "ANALYSE", "FAILED", "2026-10-29T22:30:00Z", "2026-10-29T22:30:20Z"),
        # not flagged: no finish time (an older health file)
        health_row("GSC ANALYSE C", "ANALYSE", "SUCCEEDED", "2026-10-29T22:31:00Z", None),
        # grace: a REVIEW PR 9 min after the finish counts, one 11 min after does not
        health_row("GSC REVIEW B", "REVIEW", "SUCCEEDED", "2026-10-30T20:10:00Z", "2026-10-30T20:11:00Z"),
        health_row("GSC REVIEW C", "REVIEW", "SUCCEEDED", "2026-10-31T20:10:00Z", "2026-10-31T20:11:00Z"),
    ]
    PRS = [
        raw_pr(300, "GSC INTAKE 2026-10-29 — no register change (0 rows)", "2026-10-29T20:30:40Z",
               merged="2026-10-29T20:40:00Z"),
        raw_pr(301, "HELD · GSC REVIEW TROW 2026-10-29 — AVOID (Past); was AVOID", "2026-10-29T05:13:00Z"),
        raw_pr(302, "GSC SWEEP 2026-10-24 — 60/62 priced · 2 stale", "2026-10-24T05:35:00Z"),
        raw_pr(303, "GSC SEED 2026-10-26 — 12 candidates", "2026-10-26T05:25:00Z", closed="2026-10-27T10:00:00Z"),
        raw_pr(304, "GSC REVIEW BMI 2026-10-30 [running]", "2026-10-30T20:20:00Z"),
        raw_pr(305, "GSC REVIEW NMAN.ST 2026-10-31 [running]", "2026-10-31T20:22:00Z"),
    ]

    def flagged(self, rows=None, prs=None):
        path = os.path.join(TMP, "health_noop.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(rows or self.ROWS, fh)
        h = gw.health_view(gw.load_health(path), *self.PERIOD)
        return h, [t["name"] for t in gw.noop_runs_of(h, pr_rows_of(self.PRS if prs is None else prs))]

    def test_the_rule(self):
        h, names = self.flagged()
        self.assertEqual(names, ["GSC ANALYSE", "GSC SPRINT INTAKE - Sat 18:00", "GSC QUEUE-SEED", "GSC REVIEW C"])
        by = {t["name"]: t for t in h["triggers"]}
        self.assertEqual((by["GSC ANALYSE"]["last_duration_s"], by["GSC INTAKE"]["last_duration_s"],
                          by["GSC SPRINT INTAKE - Sat 18:00"]["last_duration_s"]), (45, 120, 119))
        # without the open SWEEP PR the quick SWEEP is flagged too
        _h, names = self.flagged(prs=[p for p in self.PRS if p["number"] != 302])
        self.assertIn("GSC SWEEP", names)
        # a SWEEP PR open at the fire spares SWEEP, never ANALYSE
        _h, names = self.flagged(prs=self.PRS + [raw_pr(306, "GSC ANALYSE ABC 2026-10-28 — WATCH (G3)",
                                                         "2026-10-28T20:00:00Z")])
        self.assertIn("GSC ANALYSE", names)
        self.assertEqual(gw.noop_runs_of(None, []), [])

    def test_fix_item(self):
        h, _names = self.flagged()
        ctx = {"health": h, "noop_runs": gw.noop_runs_of(h, pr_rows_of(self.PRS))}
        items = gw.attention(dict(ATTENTION_BASE, **ctx))["Fix"]
        noop = [x for x in items if x["item"].endswith("likely no-op run")]
        self.assertEqual([x["item"] for x in noop],          # high by fire time, then the sprint routine (medium)
                         ["SEED routine 'GSC QUEUE-SEED': likely no-op run",
                          "ANALYSE routine 'GSC ANALYSE': likely no-op run",
                          "REVIEW routine 'GSC REVIEW C': likely no-op run",
                          "INTAKE routine 'GSC SPRINT INTAKE - Sat 18:00': likely no-op run"])
        self.assertEqual(gw.attention(ATTENTION_BASE)["Fix"], [])
        first = noop[1]
        self.assertEqual(first["severity"], "high")
        self.assertIn("SUCCEEDED in 45 s", first["detail"])
        self.assertIn("no ANALYSE PR was opened from its fire to 10 min after it finished", first["detail"])
        seed = next(x for x in noop if x["item"].startswith("SEED"))
        self.assertIn("none was open at its fire", seed["detail"])
        self.assertEqual(noop[-1]["severity"], "medium")                      # a sprint routine


class WeeklySeriesTests(unittest.TestCase):
    def test_notes(self):
        z = "0" * 40

        def commit(sha, day, subject, raw):
            return {"sha": sha, "when": when(day), "subject": subject, "raw": raw}
        memo_adds = [("A", z, "b%d" % i, "memos/K%d_2026-07-01_GSC.md" % i) for i in range(25)]
        commits = [
            commit("a" * 40, "2026-06-30T12:00+02:00", "Seed vault", memo_adds + [("A", z, "r1", "_REGISTER.md")]),
            commit("b" * 40, "2026-07-07T12:00+02:00", "GSC: MODEL v3.2.0", [("A", z, "m1", gw.MODEL_PATH),
                                                                             ("M", "r1", "r2", "_REGISTER.md")]),
            commit("c" * 40, "2026-07-08T12:00+02:00", "GSC: MODEL v3.2.1", [("M", "m1", "m2", gw.MODEL_PATH)]),
            commit("d" * 40, "2026-07-21T12:00+02:00", "GSC: X v1 WATCH", [("A", z, "x1", "memos/X/X_2026-07-21_GSC.md"),
                                                                           ("M", "r2", "r3", "_REGISTER.md")]),
        ]
        files = {"_REGISTER.md": None}

        class Repo:
            def show(self, sha, path):
                if path == "_REGISTER.md":
                    n = {"a": 25, "b": 25, "d": 26}[sha[0]]
                    return "---\nverdict_split: WATCH %d · AVOID 1\nnames_total: %d\n---\n" % (n - 3, n)
                if path == gw.MODEL_PATH:
                    return "---\nmodel_version: %s\n---\n" % ("v3.2.0" if sha[0] == "b" else "v3.2.1")
                return None
        repo = Repo()
        releases = gw.model_releases(repo, commits)
        self.assertEqual([(r[2], r[5]) for r in releases], [("v3.2.0", True), ("v3.2.1", False)])
        events = gw.memo_history(commits)
        weeks = gw.weekly_series(repo, commits, events, releases, when("2026-07-26T08:30+02:00"))
        by = {w["week"]: w for w in weeks}
        self.assertEqual(list(by), ["2026-W27", "2026-W28", "2026-W29", "2026-W30"])
        self.assertEqual(by["2026-W27"]["analyse"], 25)
        self.assertIn("Import: 25 memos in one commit (aaaaaaa)", by["2026-W27"]["note"])
        self.assertEqual(by["2026-W28"]["model_releases"], 1)
        self.assertIn("First appearance of MODEL v3.2.0, not counted", by["2026-W28"]["note"])
        self.assertEqual((by["2026-W29"]["watch_end"], by["2026-W29"]["keys_end"]), (22, 25))
        self.assertIn("No register commit this week; counts carried from 2026-W28", by["2026-W29"]["note"])
        self.assertEqual((by["2026-W30"]["watch_end"], by["2026-W30"]["analyse"]), (23, 1))
        self.assertEqual(by["2026-W30"]["note"], "Partial week, to Sun 26 Jul 08:30")
        self.assertEqual(gw.live_model(releases, when("2026-07-07T13:00+02:00")), "v3.2.0")
        del files


class FetchLoaderTests(unittest.TestCase):
    def test_pages_details_and_comments(self):
        folder = os.path.join(TMP, "fetch_loader")
        pulls = [raw_pr(i, "GSC INTAKE 2026-10-01 — no register change (0 rows)", "2026-10-01T00:00:00Z",
                        merged="2026-10-01T01:00:00Z") for i in range(1, 103)]
        pulls.append(dict(raw_pr(5, "GSC INTAKE 2026-10-01 — newer copy", "2026-10-01T00:00:00Z",
                                 merged="2026-10-01T01:00:00Z"), updated_at="2026-10-02T00:00:00Z"))
        issues = [{"number": 84, "title": "GSC - needs Jakub", "pull_request": None},
                  {"number": 86, "title": "GSC digest Wed 7 Oct - 3 merged, 0 needs you", "pull_request": None},
                  {"number": 89, "title": "GSC - needs Jakub", "pull_request": {"url": "x"}}]
        comments = [{"id": 2, "created_at": "2026-10-19T04:25:53Z", "body": "@jakubhoryna PR 145 held - verdict changed"},
                    {"id": 1, "created_at": "2026-10-07T21:08:29Z", "body": "@jakubhoryna gsc-notify digest failed: X"},
                    {"id": 2, "created_at": "2026-10-19T04:25:53Z", "body": "@jakubhoryna PR 145 held - verdict changed"}]
        write_fetch(folder, pulls, details={101: BOT, 5: JAKUB, 999: BOT}, issues=issues, comments=comments)
        doc = gw.load_fetch(folder)
        self.assertEqual((doc["count"], doc["pages"], doc["merged_by_fetched"], doc["needs_issue"]), (102, 2, 2, 84))
        by = {p["number"]: p for p in doc["prs"]}
        self.assertEqual(by[5]["title"], "GSC INTAKE 2026-10-01 — newer copy")
        self.assertEqual((by[101]["merged_by_type"], by[5]["merged_by"]), ("Bot", "jakubhoryna"))
        self.assertEqual([p["number"] for p in doc["prs"]], sorted(by))
        self.assertEqual([c["created_at"] for c in doc["comments"]], ["2026-10-07T21:08:29Z", "2026-10-19T04:25:53Z"])
        holds, failures = gw.hold_comments(doc, when("2026-10-20T00:00+02:00"))
        self.assertEqual(holds[145][1], "verdict changed")
        self.assertEqual([(w, why) for _t, w, why in failures], [("gsc-notify digest failed", "X")])
        holds, _f = gw.hold_comments(doc, when("2026-10-19T00:00+02:00"))
        self.assertNotIn(145, holds)

    def test_hold_record_forms(self):
        for body, want in (("@jakubhoryna PR 87 held - verdicts differ\nGSC ANALYSE …", (87, "verdicts differ")),
                           ("PR 151 held - verdict changed DNAF → WATCH\nOpen: …", (151, "verdict changed DNAF → WATCH"))):
            m = gw.HOLD_COMMENT_RE.match(body)
            self.assertEqual((int(m.group("pr")), m.group("reason")), want)
        for body in ("gsc-automerge failed: HTTP 502", "gsc-notify maintenance failed: x",
                     "@jakubhoryna gsc-notify digest failed: NotAllowed"):
            self.assertTrue(gw.FAIL_COMMENT_RE.match(body), body)

    def test_incomplete_fetch_is_refused(self):
        folder = os.path.join(TMP, "fetch_incomplete")
        pulls = [raw_pr(7, "GSC SWEEP 2026-10-17 — 60/66 priced", "2026-10-17T05:00:00Z", merged="2026-10-17T06:00:00Z"),
                 raw_pr(8, "GSC REVIEW ABC 2026-10-09 — WATCH; v4.5.0 re-test", "2026-10-09T05:00:00Z",
                        merged="2026-10-09T06:00:00Z"),
                 raw_pr(6, "GSC INTAKE 2026-10-01 — no register change (0 rows)", "2026-10-01T04:00:00Z",
                        merged="2026-10-01T05:00:00Z"),
                 raw_pr(9, "GSC ANALYSE XYZ 2026-10-18 — WATCH (Cheapness)", "2026-10-18T07:00:00Z",
                        merged="2026-10-18T07:40:00Z")]
        since, until = when("2026-10-11T08:30+02:00"), when("2026-10-18T08:30+02:00")
        write_fetch(folder, pulls, details={})
        with self.assertRaises(gw.ToolError) as caught:         # a failed jq or gh in the merged_by loop
            gw.check_fetch(gw.load_fetch(folder), since, until)
        self.assertIn("no pull_{n}.json for merged PRs 7, 8", str(caught.exception))
        # PR 6 merged before since - 7 d and PR 9 after until need no detail
        write_fetch(folder, pulls, details={7: BOT, 8: JAKUB})
        gw.check_fetch(gw.load_fetch(folder), since, until)
        # the needs-Jakub issue listed, its comments page lost
        write_fetch(folder, pulls, details={7: BOT, 8: JAKUB}, issues=[{"number": 84, "title": "GSC - needs Jakub",
                                                                       "pull_request": None}])
        with self.assertRaises(gw.ToolError) as caught:
            gw.check_fetch(gw.load_fetch(folder), since, until)
        self.assertIn("issue 84 (GSC - needs Jakub) is listed but no comments_{p}.json", str(caught.exception))
        write_fetch(folder, pulls, details={7: BOT, 8: JAKUB}, comments=[])            # an empty page is fine
        gw.check_fetch(gw.load_fetch(folder), since, until)

    def test_bad_folders(self):
        with self.assertRaises(gw.ToolError):
            gw.load_fetch(os.path.join(TMP, "missing"))
        empty = os.path.join(TMP, "fetch_empty")
        os.makedirs(empty, exist_ok=True)
        with self.assertRaises(gw.ToolError):
            gw.load_fetch(empty)
        bad = os.path.join(TMP, "fetch_bad")
        os.makedirs(bad, exist_ok=True)
        with open(os.path.join(bad, "pulls_1.json"), "w", encoding="utf-8") as fh:
            fh.write("{\"message\": \"Forbidden\"}")
        with self.assertRaises(gw.ToolError):
            gw.load_fetch(bad)
        with open(os.path.join(bad, "pulls_1.json"), "w", encoding="utf-8") as fh:
            fh.write("[{\"title\": \"no number\"}]")
        with self.assertRaises(gw.ToolError):
            gw.load_fetch(bad)


class DatasetSchemaTests(unittest.TestCase):
    SPEC = {   # the fields the weekly page reads, as the 2026-10-20 datasets carry them (summary and held new)
        "summary": "order kind text",
        "kpis": "order metric value prior unit basis",
        "attention": "rank list severity item detail action since",
        "shortlist": "key company region px px_unit px_date px_age_d trigger trigger_basis distance_pct needs_fall_pct "
                     "mcap_fcf ev_oi status memo_date model_version retest_owed all_cash_trigger pending reliable "
                     "next_review",
        "changes": "key company job from_verdict to_verdict deciding ground_retired model_version merged_at merged_by pr",
        "weekly": "week week_start analyse review incomplete model_releases watch_end keys_end note",
        "pipeline": "job scheduled_base scheduled_sprint prs_opened merged_auto merged_jakub closed_unmerged "
                    "last_run_failed_usage_limit triggers",
        "coverage": "region keys watch avoid dnaf share_pct",
        "backlog": "item start end unit note",
        "held": "key company verdict zone last_zone_check memo_date open_since status",
        "meta": "period_label since until report_date ref_sha ref_time register_from register_to model_live decide fix "
                "know generated_at tool_version",
    }

    def test_schema_matches_the_spec(self):
        self.assertEqual(set(gw.DATASET_SCHEMA), set(self.SPEC))
        self.assertEqual(set(gw.DATASET_IDS), set(self.SPEC))
        for name, keys in self.SPEC.items():
            self.assertEqual(set(gw.DATASET_SCHEMA[name]), set(keys.split()), name)

    def test_checker_catches_bad_rows(self):
        good = {name: [] for name in gw.DATASET_SCHEMA}
        self.assertEqual(gw.check_datasets(good), [])
        row = {k: None for k in gw.DATASET_SCHEMA["coverage"]}
        row.update(region="UK", keys="19", watch=3, avoid=10, dnaf=True, share_pct=4.8)
        problems = gw.check_datasets(dict(good, coverage=[row]))
        self.assertTrue(any("keys" in p for p in problems) and any("dnaf: bool" in p for p in problems), problems)
        self.assertTrue(gw.check_datasets(dict(good, held=[{"key": "X"}])))

    def test_private_figures_are_scrubbed(self):
        data = {"attention": [{"rank": 1, "item": "ABC bought @ 41.20 (avg_cost 39.5)", "since": None}],
                "held": [{"status": "position size 3%", "zone": "SELL-FLAG"}],
                "backlog": [{"note": "core_fcf: 1,234.5 and cost basis $41", "end": 3}]}
        out = gw.scrub_private(data)
        self.assertEqual(out["attention"][0], {"rank": 1, "item": "ABC bought [private] ([private])", "since": None})
        self.assertEqual(out["held"][0], {"status": "[private]%", "zone": "SELL-FLAG"})
        self.assertEqual(out["backlog"][0], {"note": "[private] and [private]", "end": 3})
        for keep in ("@jakubhoryna PR 151 held - verdict changed", "SR1 also fires: sell line $45.07",
                     "buybacks 2.1% of the market cap", "Px 41.20 USD (2026-10-17) vs trigger 30.1"):
            self.assertEqual(gw.scrub_private({"x": [{"t": keep}]})["x"][0]["t"], keep)

    def test_num(self):
        self.assertEqual((gw.num("2449"), gw.num("2.99"), gw.num("-"), gw.num("n.m."), gw.num(Decimal("25.70"))),
                         (2449, 2.99, None, None, 25.7))
        self.assertIsInstance(gw.num("2449"), int)


def lint_data():
    return {"meta": [{"period_label": "Sun 18 Oct – Sun 25 Oct 2026", "model_live": "v4.6.0"}],
            "kpis": [{"metric": "Memos merged (period)", "value": 9, "prior": 18},
                     {"metric": "Median WATCH Px age", "value": 20.0}],
            "attention": [{"item": "PR 151 REVIEW 6383.T held for your merge"}]}


class SummaryLintTests(unittest.TestCase):
    def rows(self, *texts):
        return [{"order": i + 1, "kind": gw.SUMMARY_SLOTS[i], "text": t} for i, t in enumerate(texts)]

    def test_clean(self):
        corpus = gw.number_corpus(lint_data())
        rows = self.rows("Sun 18 Oct – Sun 25 Oct 2026: 9 memos, down from 18.", "PR 151 waits for you (6383.T).",
                         "Prices are 20.0 days old.", "Nothing else.", "MODEL v4.6.0 is live.", "Nothing new.")
        self.assertEqual(gw.lint_summary(rows, corpus), [])
        self.assertEqual(gw.lint_summary(rows, corpus, gw.kpi_values(lint_data())), [])
        # exactly six: the page has six fixed slots, and a short draft would leave the last ones empty
        self.assertIn("2 sentences; exactly 6", gw.lint_summary(rows[:2], corpus)[0])
        self.assertIn("5 sentences; exactly 6", gw.lint_summary(rows[:5], corpus)[0])
        # framework capitals and the buy zone are not advice; buybacks are not buy
        ok = self.rows("9 memos merged; none is BUY and the held SELL-FLAG stands.", "Nothing waits for you.",
                       "Buybacks are not counted; the nearest WATCH is far from the buy zone.", "Nothing.", "Nothing.",
                       "Nothing.")
        self.assertEqual(gw.lint_summary(ok, corpus, gw.kpi_values(lint_data())), [])

    def test_problems(self):
        corpus = gw.number_corpus(lint_data())
        cases = [
            (self.rows("10 memos merged."), "number(s) not in the datasets: 10"),
            (self.rows("Prices are 20 days old."), "not in the datasets: 20"),       # printed as 20.0
            (self.rows("See #151."), "'#' is not allowed"),
            (self.rows("x" * 301), "301 characters"),
            (self.rows("one\ntwo"), "one line only"),
            (self.rows("ok", "ok", "ok", "ok", "ok", "ok") + [{"order": 7, "kind": "know", "text": "ok"}],
             "7 sentences; exactly 6"),
            (self.rows("ok", "ok", "ok", "ok", "ok"), "5 sentences; exactly 6"),
            (self.rows("ok", "Buy PR 151's name now."), "advice language (Buy)"),
            (self.rows("ok", "ok", "ok", "ok", "Consider selling the held name."), "advice language (selling)"),
            (self.rows("ok", "A price target of 9 applies."), "advice language (price target)"),
            (self.rows("ok", "Bought it @ 20.0 last week."), "a private figure (@ 20.0)"),
            (self.rows("ok", "The avg_cost is 9."), "a private figure (avg_cost)"),
            ([{"order": 1, "kind": "decide", "text": "ok"}], "kind must be takeaway"),
            ([{"order": 2, "kind": "takeaway", "text": "ok"}], "order must be 1"),
            ([{"order": 1, "kind": "advice", "text": "ok"}], "kind 'advice'"),
            ([{"order": 1, "kind": "takeaway", "text": "ok", "extra": 1}], "exactly the fields"),
            ([{"order": 1, "kind": "takeaway", "text": " "}], "empty text"),
            ([], "non-empty JSON array"),
            ({"order": 1}, "non-empty JSON array"),
        ]
        for rows, needle in cases:
            problems = gw.lint_summary(rows, corpus)
            self.assertTrue(any(needle in p for p in problems), (needle, problems))

    def test_takeaway_headline_numbers_match_the_kpis(self):
        data = lint_data()
        data["kpis"] += [{"metric": "New WATCH (period)", "value": 0}, {"metric": "IN RANGE", "value": 0},
                         {"metric": "NEAR", "value": 1}, {"metric": "WATCH (register)", "value": 70},
                         {"metric": "WATCH after pending rows", "value": 66}]
        corpus, kpis = gw.number_corpus(data), gw.kpi_values(data)
        tail = ["ok"] * 5
        good = ("9 memos merged, 0 new WATCH; 0 IN RANGE and 1 NEAR; WATCH 70 in the register, 66 after "
                "pending rows; the 66 WATCH rows after pending.")
        self.assertEqual(gw.lint_summary(self.rows(good, *tail), corpus, kpis), [])
        # every number is in the corpus, but next to the wrong headline phrase
        for text, needle in (("18 memos merged.", "'18 memos merged' does not match kpis Memos merged (period) (9)"),
                             ("1 new WATCH.", "'1 new WATCH'"), ("1 IN RANGE.", "'1 IN RANGE'"),
                             ("0 names are NEAR.", "'0 names are NEAR'"), ("WATCH 9 in the register.", "'WATCH 9'"),
                             ("9 WATCH rows.", "'9 WATCH'")):
            problems = gw.lint_summary(self.rows(text, *tail), corpus, kpis)
            self.assertTrue(any(needle in p for p in problems), (text, problems))
        # only the takeaway slot is held to the headline figures; without kpis nothing is checked
        self.assertEqual(gw.lint_summary(self.rows("ok", "18 memos merged.", *tail[1:]), corpus, kpis), [])
        self.assertEqual(gw.lint_summary(self.rows("18 memos merged.", *tail), corpus), [])


class DashWritesTests(unittest.TestCase):
    def setUp(self):
        self.dir = os.path.join(TMP, "dash")
        os.makedirs(self.dir, exist_ok=True)
        for name in gw.DATASET_IDS:
            with open(os.path.join(self.dir, name + ".json"), "w", encoding="utf-8") as fh:
                json.dump([], fh)
        self.blobs = {name: "/_blob/%032x" % (i + 1) for i, name in enumerate(gw.DATASET_IDS)}
        self.versions = {name: i + 2 for i, name in enumerate(gw.DATASET_IDS)}

    NOW = datetime.datetime(2026, 10, 25, 7, 45, tzinfo=UTC)                 # 08:45 Prague, the run's clock

    def test_writes(self):
        writes = gw.dash_writes(self.dir, self.blobs, self.versions, "2026-10-25T08:41:07+01:00", now=self.NOW)
        self.assertEqual([w["doc_id"] for w in writes][-1], "meta")
        self.assertEqual(sorted(w["doc_id"] for w in writes), sorted(gw.DATASET_IDS))
        for w in writes:
            self.assertEqual(set(w), {"op", "collection", "doc_id", "data", "if_version"})
            self.assertEqual((w["op"], w["collection"]), ("update", "datasets"))
            self.assertEqual(w["data"], {"source": {"kind": "file", "url": self.blobs[w["doc_id"]],
                                                    "name": w["doc_id"] + ".json", "format": "json"},
                                         "updated": {"at": "2026-10-25T08:41:07+01:00", "by": "GSC WEEKLY routine"}})
            self.assertEqual(w["if_version"], self.versions[w["doc_id"]])

    def test_the_guard_accepts_the_batch(self):
        hooks = os.path.join(REPO, ".claude", "hooks")
        if not os.path.isfile(os.path.join(hooks, "gsc_guard.py")):
            self.skipTest("guard hook not in this checkout")
        sys.path.insert(0, hooks)
        try:
            import gsc_guard
        finally:
            sys.path.remove(hooks)
        if not hasattr(gsc_guard.Guard, "check_dataset_writes"):
            self.skipTest("guard without the weekly page rule")
        # the guard bounds updated.at by its own clock, so this batch is stamped now
        at = datetime.datetime.now(UTC).replace(microsecond=0).isoformat()
        writes = gw.dash_writes(self.dir, self.blobs, self.versions, at)
        gsc_guard.Guard({"cwd": REPO}).check_dataset_writes(json.loads(json.dumps(writes)))
        self.assertEqual((gsc_guard.WEEKLY_PAGE_URL, gsc_guard.WEEKLY_BY, tuple(gsc_guard.DATASET_IDS)),
                         (gw.WEEKLY_PAGE_URL, gw.WEEKLY_BY, gw.DATASET_IDS))
        # the guard reads each upload against the same fields the tool renders
        self.assertEqual(gsc_guard.DATASET_FIELDS, {k: set(v) for k, v in gw.DATASET_SCHEMA.items()})
        # and accepts the tool's notification line in both forms
        for line in ("GSC WEEKLY · Sun 18 Oct – Sun 25 Oct 2026 · 5 to decide · 6 to fix · 9 memos · " + gw.WEEKLY_PAGE_URL,
                     "GSC WEEKLY · Sun 27 Dec 2026 – Sun 3 Jan 2027 · 0 to decide · 0 to fix · 0 memos · "
                     + gw.WEEKLY_PAGE_URL):
            self.assertTrue(gsc_guard.PUSH_WEEKLY_RE.match(line), line)

    def test_refusals(self):
        bad = [
            (dict(self.blobs, kpis="/_blob/ABC"), self.versions, "2026-10-25T08:41:07+01:00"),
            (dict(self.blobs, kpis="/_blob/%032x\n" % 3), self.versions, "2026-10-25T08:41:07+01:00"),
            (dict(self.blobs, kpis=self.blobs["meta"]), self.versions, "2026-10-25T08:41:07+01:00"),
            ({k: v for k, v in self.blobs.items() if k != "held"}, self.versions, "2026-10-25T08:41:07+01:00"),
            (dict(self.blobs, extra="/_blob/%032x" % 99), self.versions, "2026-10-25T08:41:07+01:00"),
            (self.blobs, dict(self.versions, kpis=0), "2026-10-25T08:41:07+01:00"),
            (self.blobs, dict(self.versions, kpis=True), "2026-10-25T08:41:07+01:00"),
            (self.blobs, dict(self.versions, kpis="3"), "2026-10-25T08:41:07+01:00"),
            (self.blobs, self.versions, "2026-10-25 08:41"),
            (self.blobs, self.versions, "2026-10-25T08:41:07"),
            ([], self.versions, "2026-10-25T08:41:07+01:00"),
        ]
        for blobs, versions, at in bad:
            with self.assertRaises(gw.ToolError, msg=repr((blobs, versions, at))[:200]):
                gw.dash_writes(self.dir, blobs, versions, at, now=self.NOW)
        # a stamp ahead of the clock (a mistyped {RUN}) would make every later run read its week as published
        for at in ("2027-10-25T08:41:07+01:00", "2026-10-25T08:51:00+01:00"):
            with self.assertRaises(gw.ToolError) as caught:
                gw.dash_writes(self.dir, self.blobs, self.versions, at, now=self.NOW)
            self.assertIn("is after the clock", str(caught.exception))
        self.assertTrue(gw.dash_writes(self.dir, self.blobs, self.versions, "2026-10-25T08:49:59+01:00", now=self.NOW))
        os.remove(os.path.join(self.dir, "held.json"))
        with self.assertRaises(gw.ToolError):
            gw.dash_writes(self.dir, self.blobs, self.versions, "2026-10-25T08:41:07+01:00", now=self.NOW)

    def test_cli(self):
        blobs, versions = os.path.join(TMP, "blobs.json"), os.path.join(TMP, "versions.json")
        for path, data in ((blobs, self.blobs), (versions, self.versions)):
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(data, fh)
        out = os.path.join(TMP, "writes.json")
        code, printed, _err = run_main(["dash-writes", "--datasets", self.dir, "--blobs", blobs, "--versions", versions,
                                        "--at", "2026-10-18T08:41:07+02:00", "--out", out])
        self.assertEqual(code, 0, _err)
        code, _p, err = run_main(["dash-writes", "--datasets", self.dir, "--blobs", blobs, "--versions", versions,
                                  "--at", "2099-10-25T08:41:07+01:00", "--out", out])
        self.assertEqual(code, 2)
        self.assertIn("is after the clock", err)
        with open(out, encoding="utf-8") as fh:
            self.assertEqual(json.load(fh), json.loads(printed))
        code, _p, err = run_main(["dash-writes", "--datasets", self.dir, "--blobs", blobs, "--versions", versions,
                                  "--at", "2026-10-25T08:41:07+01:00", "--out", os.path.join(REPO, "writes.json")])
        self.assertEqual(code, 2)
        self.assertIn("inside the repository", err)


class GuardScanTests(unittest.TestCase):
    def test_source_passes_the_routine_hook_scan(self):
        hooks = os.path.join(REPO, ".claude", "hooks")
        if not os.path.isfile(os.path.join(hooks, "gsc_guard.py")):
            self.skipTest("guard hook not in this checkout")
        sys.path.insert(0, hooks)
        try:
            import gsc_guard
        finally:
            sys.path.remove(hooks)
        with open(TOOL, encoding="utf-8") as fh:
            source = fh.read()
        gsc_guard.Guard({"cwd": REPO}).check_code(source)   # raises Blocked if the hook would refuse it
        self.assertIsNone(gsc_guard.LOCKED_FRAG_RE.search(source))
        self.assertIsNone(gsc_guard.CODE_GHAPI_RE.search(source))
        self.assertIsNone(gsc_guard.CODE_PUSH_RE.search(source))
        self.assertLess(len(source.encode("utf-8")), 512 * 1024)        # the hook scans scripts up to 512 KB
        self.assertNotIn("subprocess.run([\"gh\"", source)


def git_in(folder, *args):
    return subprocess.run(["git", "-C", folder, "-c", "user.name=t", "-c", "user.email=t@example.com",
                           "-c", "commit.gpgsign=false"] + list(args), check=True, capture_output=True)


class ShallowCloneTests(unittest.TestCase):
    """A routine session starts from a shallow clone; render refuses one up front with one clear line, and
    WEEKLY.md's step-1 fetch (git fetch --unshallow origin main) heals it (MODEL v4.8.0)."""

    @classmethod
    def setUpClass(cls):
        base = tempfile.mkdtemp(prefix="shallow-", dir=TMP)
        cls.origin, cls.shallow, cls.full = (os.path.join(base, n) for n in ("origin", "shallow", "full"))
        os.makedirs(cls.origin)
        git_in(cls.origin, "init", "-q")
        git_in(cls.origin, "symbolic-ref", "HEAD", "refs/heads/main")
        for n in range(3):
            with open(os.path.join(cls.origin, "f.md"), "w", encoding="utf-8") as fh:
                fh.write("v%d\n" % n)
            git_in(cls.origin, "add", "f.md")
            git_in(cls.origin, "commit", "-q", "-m", "GSC: commit %d (#%d)" % (n, n + 1))
        url = "file://" + cls.origin
        subprocess.run(["git", "clone", "-q", "--depth", "1", url, cls.shallow], check=True, capture_output=True)
        subprocess.run(["git", "clone", "-q", url, cls.full], check=True, capture_output=True)

    def test_render_refuses_a_shallow_clone_first(self):
        self.assertEqual(git_in(self.shallow, "rev-parse", "--is-shallow-repository").stdout.strip(), b"true")
        with self.assertRaises(gw.ToolError) as caught:
            gw.need_full_history(self.shallow)
        self.assertEqual(str(caught.exception), gw.SHALLOW_ERROR)
        self.assertEqual(gw.SHALLOW_ERROR, "shallow clone: run git fetch --unshallow origin main "
                                           "(routines/WEEKLY.md step 1)")
        # the CLI: exit 2, and the first error line names the fix (WEEKLY's not-published reason)
        code, _out, err = run_main(["render", "--repo-dir", self.shallow, "--ref", "origin/main", "--since",
                                    "2026-10-25T08:30+01:00", "--until", "2026-11-01T08:30+01:00", "--fetch-dir",
                                    os.path.join(TMP, "no-such-fetch"), "--out-dir", os.path.join(TMP, "sh-out")])
        self.assertEqual(code, 2)
        self.assertEqual(err.splitlines()[0], "gsc_weekly: " + gw.SHALLOW_ERROR)
        with self.assertRaises(gw.ToolError) as caught:
            gw.build(self.shallow, "origin/main", when("2026-10-25T08:30+01:00"), when("2026-11-01T08:30+01:00"), None)
        self.assertEqual(str(caught.exception), gw.SHALLOW_ERROR)
        gw.need_full_history(self.full)                        # a full clone passes

    def test_the_weekly_step_1_fetch_heals_it(self):
        with open(os.path.join(REPO, "routines", "WEEKLY.md"), encoding="utf-8") as fh:
            playbook = fh.read()
        cmd = next(c for c in __import__("re").findall(r"`([^`\n]+)`", playbook)
                   if c.startswith('if [ "$(git rev-parse --is-shallow-repository)" = true ]'))
        fetch, _sep, switch = cmd.partition(" && ")
        self.assertTrue(switch.startswith('git switch --no-track -c "claude/gsc-weekly-{D}-{T}" origin/main'), switch)
        healed = os.path.join(os.path.dirname(self.shallow), "healed")
        subprocess.run(["git", "clone", "-q", "--depth", "1", "file://" + self.origin, healed], check=True,
                       capture_output=True)
        self.assertEqual(git_in(healed, "rev-list", "--count", "origin/main").stdout.strip(), b"1")
        subprocess.run(["bash", "-c", fetch], cwd=healed, check=True, capture_output=True)
        self.assertEqual(git_in(healed, "rev-parse", "--is-shallow-repository").stdout.strip(), b"false")
        self.assertEqual(git_in(healed, "rev-list", "--count", "origin/main").stdout.strip(), b"3")
        gw.need_full_history(healed)
        subprocess.run(["bash", "-c", fetch], cwd=healed, check=True, capture_output=True)   # a full clone: plain fetch


FIXED_SHA = "d989ade0ec1ca584713956ebfc66791fcf23d915"       # origin/main 2026-10-19 23:44 Prague (PR 149)
OLDER_SHA = "58df8c32872ba5b4626645594274b79a0ea72e97"       # one commit earlier (PR 139)
INTAKE_SHA = "e04d7d12d444832e2bf946e26eceadf941839cb4"      # origin/main 2026-10-20 06:08 Prague (PR 150)


def have_commit(sha):
    try:
        return subprocess.run(["git", "-C", REPO, "cat-file", "-e", sha + "^{commit}"],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0
    except OSError:
        return False


COLO_RUN = "claude/gsc-review-COLO-B.CO-2026-10-15-2111"
PULLS = [   # GitHub's pulls pages for the 12-19 Oct 2026 report period, reduced to the cases under test
    raw_pr(149, "GSC ANALYSE COH.AX 2026-10-19 — AVOID (Past)", "2026-10-19T21:31:00Z",
           merged="2026-10-19T21:44:53Z", merge_sha=FIXED_SHA),
    raw_pr(140, "GSC REVIEW COLO-B.CO 2026-10-15 [abandoned]", "2026-10-15T19:12:15Z",
           closed="2026-10-19T04:04:19Z", head=COLO_RUN),
    raw_pr(144, "GSC REVIEW COLO-B.CO 2026-10-15 — INCOMPLETE (method re-test exceeds budget)",
           "2026-10-19T04:06:30Z", merged="2026-10-19T04:06:55Z", head=COLO_RUN),
    raw_pr(145, "GSC REVIEW BMI 2026-10-19 — AVOID (SF); was WATCH, v4.5.0 re-test", "2026-10-19T04:25:00Z",
           merged="2026-10-19T21:11:06Z"),
    raw_pr(151, "GSC REVIEW 6383.T 2026-10-18 — WATCH; was DNAF, v4.6.0 re-test", "2026-10-18T04:11:52Z"),
    raw_pr(152, "GSC ANALYSE XYZ.L 2026-10-17 — stopped: no listed security", "2026-10-17T19:00:00Z"),
    raw_pr(120, "GSC REVIEW NMAN.ST 2026-10-08 — AVOID (Past); was WATCH", "2026-10-08T10:00:00Z",
           merged="2026-10-08T20:00:00Z"),
    raw_pr(88, "HELD · GSC REVIEW CROX 2026-10-07 — AVOID (Past + SF); was WATCH", "2026-10-07T21:47:22Z",
           merged="2026-10-08T11:58:40Z"),
]
DETAILS = {149: BOT, 144: BOT, 145: JAKUB, 120: JAKUB, 88: JAKUB}
ISSUES = [{"number": 84, "title": "GSC - needs Jakub", "pull_request": None}]
COMMENTS = [
    {"id": 1, "created_at": "2026-10-07T21:08:29Z", "body": "@jakubhoryna gsc-notify digest failed: NotAllowed"},
    {"id": 2, "created_at": "2026-10-15T10:00:00Z", "body": "gsc-automerge failed: HTTP 502 on the merge call\n<!-- x -->"},
    {"id": 3, "created_at": "2026-10-18T04:20:00Z", "body": "@jakubhoryna PR 151 held - verdict changed DNAF → WATCH\nx"},
]
SINCE, UNTIL = "2026-10-12T00:00+02:00", "2026-10-20T00:00+02:00"
FETCH = write_fetch(os.path.join(TMP, "fetch_w42"), PULLS, DETAILS, ISSUES, COMMENTS)


@unittest.skipUnless(have_commit(FIXED_SHA), "fixed commit not in the repository")
class EndToEndTests(unittest.TestCase):
    """The 12-19 Oct 2026 report period against the fixed ref; the hand-checked figures of the attended
    re-derivation of 2026-10-20 (WATCH re-test 63 on the register basis, retired-ground priors 5 and 5,
    nine open items with SYAB.DE and ROG.SW over the cap, DNAF 18 = 16 retired + 2 awaiting RETIRED)."""

    @classmethod
    def setUpClass(cls):
        cls.health = gw.load_health(HEALTH)
        cls.doc = gw.load_fetch(FETCH)
        cls.ctx = gw.build(REPO, FIXED_SHA, when(SINCE), when(UNTIL), cls.doc, cls.health)
        cls.gen = datetime.datetime(2026, 10, 20, 0, 30, tzinfo=UTC)
        cls.ctx["generated_at"] = cls.gen
        cls.data, cls.line = gw.render_all(cls.ctx, cls.gen)

    def kpi(self, metric):
        return next(k for k in self.data["kpis"] if k["metric"] == metric)

    def backlog(self, item):
        return next(b for b in self.data["backlog"] if b["item"] == item)

    def test_window_and_counts(self):
        c = self.ctx
        self.assertEqual((c["start"]["sha"][:7], c["report_date"]), ("bea519c", datetime.date(2026, 10, 19)))
        self.assertEqual((c["st"]["fm"]["register_version"], c["en"]["fm"]["register_version"]), ("v314", "v318"))
        self.assertEqual((len(c["events"]), len(c["analyses"]), len(c["reviews"])), (18, 10, 8))
        self.assertEqual(dict(c["verdict_mix"]), {"DNAF": 11, "AVOID": 7})
        self.assertEqual((c["live_start"], c["live_end"]), ("v4.5.3", "v4.6.0"))
        self.assertEqual(c["period_label"], "Mon 12 Oct – Mon 19 Oct 2026")

    def test_px_age_counts_to_the_report_date(self):
        by = {r["key"]: r for r in self.ctx["en"]["shortlist"]}
        self.assertEqual((by["INVE-B.ST"]["px_date"], by["INVE-B.ST"]["px_age_d"]), ("2026-10-05", 14))
        self.assertEqual((by["ABEV"]["px_date"], by["ABEV"]["px_age_d"]), ("2026-10-02", 17))

    def test_pending_overlay(self):
        en = self.ctx["en"]
        self.assertEqual(sorted(en["overlay"]), ["AME", "BMI", "BRK.B", "CCL-B.TO", "COH.AX", "COLO-B.CO", "DOV", "TROW"])
        self.assertEqual(sorted(r["key"] for r in en["pending_changes"]), ["AME", "BMI", "BRK.B", "DOV"])
        self.assertEqual((en["counts"]["WATCH"], en["counts_after"]["WATCH"]), (70, 66))
        self.assertEqual((en["counts"]["DNAF"], en["counts_after"]["DNAF"]), (15, 18))

    def test_retired_grounds_one_lens(self):
        self.assertEqual((self.kpi("DNAF memos merged on retired grounds (period)")["value"],
                          self.kpi("DNAF memos merged on retired grounds (period)")["prior"]), (11, 5))
        self.assertEqual((self.kpi("DNAF on retired grounds (incl. pending)")["value"],
                          self.kpi("DNAF on retired grounds (incl. pending)")["prior"]), (16, 5))
        dnaf = self.kpi("DNAF after pending rows")
        self.assertEqual((dnaf["value"], dnaf["prior"]), (18, 7))
        self.assertIn("16 on retired grounds, 2 awaiting RETIRED (EA, SYAB.DE), 0 live", dnaf["basis"])
        flags = self.ctx["en"]["dnaf_after"]
        self.assertTrue(flags["EA"]["awaiting_retired"] and flags["SYAB.DE"]["awaiting_retired"])
        self.assertFalse(flags["DOV"]["awaiting_retired"])

    def test_watch_retest_register_basis(self):
        b = self.backlog("WATCH keys owing a re-test")
        self.assertEqual((b["start"], b["end"]), (66, 63))
        self.assertIn("(59 of the 66 WATCH rows after pending)", b["note"])
        by = {r["key"]: r for r in self.data["shortlist"]}
        self.assertTrue(by["BMI"]["retest_owed"])                 # register basis: the applied memo is v4.4.x

    def test_open_items_over_the_cap(self):
        b = self.backlog("Register open items")
        self.assertEqual((b["start"], b["end"]), (8, 9))
        self.assertIn("SYAB.DE, ROG.SW", b["note"])

    def test_attention_lists(self):
        a = self.ctx["attention"]
        decide = [x["item"] for x in a["Decide"]]
        self.assertEqual([x.split()[0] for x in decide], ["NOVO-B.CO", "CROX", "TROW", "PR", "ABB", "EA", "ROG.SW",
                                                          "SYAB.DE"])
        self.assertIn("PR 151 REVIEW 6383.T held for your merge", decide)
        held_pr = next(x for x in a["Decide"] if x["item"].startswith("PR 151"))
        self.assertIn("gsc-automerge: verdict changed DNAF → WATCH", held_pr["detail"])
        self.assertFalse(any("152" in x or "HFG.DE" in x for x in decide))
        fix = " | ".join(x["item"] for x in a["Fix"])
        for needle in ("SWEEP stale", "USAGE_LIMIT_REACHED", "Run gap", "Register lag", "Stopped run: ANALYSE XYZ.L (PR 152)",
                       "COLO-B.CO REVIEW INCOMPLETE (PR 144)", "COLO-B.CO REVIEW abandoned (PR 140)",
                       "Workflow failure: gsc-automerge failed"):
            self.assertIn(needle, fix)
        self.assertNotIn("digest", fix.lower())
        know = [x["item"] for x in a["Know"]]
        self.assertIn("HFG.DE held SELL-FLAG SR2 — decision deferred by you to FY2026 results (~Mar 2027) on "
                      "2026-08-18", know)
        for items in a.values():
            sev = [gw.SEVERITIES.index(x["severity"]) for x in items]
            self.assertEqual(sev, sorted(sev))
        sweep = next(x for x in a["Fix"] if x["item"].startswith("SWEEP stale"))
        self.assertIn("1 SWEEP merged ever", sweep["detail"])
        self.assertIn("2026-10-05 ×", sweep["detail"])
        self.assertIn("2026-07-14 (ULVR.L)", sweep["detail"])

    def test_decide_and_fix_rules_on_injected_events(self):
        ctx = copy.copy(self.ctx)
        buy = dict(self.ctx["events"][0], key="TST", verdict="BUY", job="REVIEW", memo_date="2026-10-18",
                   deciding="all three gates pass; in the buy zone", pr=999)
        ctx["events"] = self.ctx["events"] + [buy]
        ctx["zone_changes"] = [{"key": "CROX", "from": "SELL-FLAG", "to": "HOLD", "kind": "sweep",
                                "source": "SWEEP 2026-10-17 (PR 998)", "when": when("2026-10-17T10:00+02:00")},
                               {"key": "TROW", "from": "HOLD", "to": "SELL-FLAG", "kind": "memo",
                                "source": "REVIEW memo 2026-10-19 (PR 147)", "when": when("2026-10-19T10:00+02:00")}]
        items = [gw.parse_open_item(HELD_LINES[k]) for k in ("HFG.DE", "NOVO-B.CO", "CROX", "TROW")]
        ctx["open_items_parsed"] = items
        held = []
        for h in self.ctx["held_now"]:
            item = next((i for i in items if i["key"] == h["key"]), None)
            decision, status = gw.held_status(item)
            held.append(dict(h, decision=decision, status=status))
        ctx["held_now"] = held
        a = gw.attention(ctx)
        decide = [x["item"] for x in a["Decide"]]
        self.assertIn("TST BUY (REVIEW, memo 2026-10-18)", decide)
        self.assertIn("CROX held zone SELL-FLAG → HOLD (SWEEP)", decide)
        self.assertIn("CROX held SELL-FLAG SR2 — your decision is pending", decide)
        self.assertFalse(any(x.startswith(("NOVO-B.CO", "HFG.DE", "TROW held SELL")) for x in decide), decide)
        know = [x["item"] for x in a["Know"]]
        self.assertIn("NOVO-B.CO held SELL-FLAG SR2 — held by your decision on 2026-10-20", know)
        self.assertIn("TROW held SELL-FLAG SR2 — decision deferred by you to Q4 results on 2026-10-21", know)
        self.assertTrue(any(x.startswith("HFG.DE held SELL-FLAG SR2 — held by your decision on 2026-10-20") for x in know))
        self.assertIn("TROW held zone HOLD → SELL-FLAG", know)

    def test_runs_and_held_wait(self):
        opened = self.kpi("Analytic PRs opened (ANALYSE + REVIEW)")
        self.assertEqual(opened["value"], 6)
        self.assertIn("6 PRs are 5 runs (PRs 140 and 144 from one COLO-B.CO run)", opened["basis"])
        runs = self.kpi("Analytic runs per scheduled fire")
        self.assertEqual(runs["value"], gw.num(gw.q1(Decimal(5) * 100 / 134)))
        self.assertIn("5 analytic runs ÷ 134 scheduled fires (24 base + 110 sprint)", runs["basis"])
        wait = self.kpi("Held PR median wait")
        self.assertEqual((wait["value"], wait["prior"]), (16.8, 10.0))        # PR 88 opened before gsc-automerge

    def test_datasets_summary_and_notification(self):
        data = self.data
        self.assertEqual(list(data), list(gw.DATASET_IDS))
        self.assertEqual(gw.check_datasets(data), [])
        self.assertEqual([r["kind"] for r in data["summary"]], list(gw.SUMMARY_SLOTS))
        self.assertEqual(gw.lint_summary(data["summary"], gw.number_corpus(data)), [])
        self.assertTrue(data["summary"][0]["text"].startswith("Mon 12 Oct – Mon 19 Oct 2026: 18 memos merged"))
        meta = data["meta"][0]
        self.assertEqual((meta["decide"], meta["fix"]), (len(self.ctx["attention"]["Decide"]),
                                                         len(self.ctx["attention"]["Fix"])))
        self.assertEqual(self.line, "GSC WEEKLY · Mon 12 Oct – Mon 19 Oct 2026 · %d to decide · %d to fix · 18 memos · "
                                    "%s" % (meta["decide"], meta["fix"], gw.WEEKLY_PAGE_URL))
        self.assertLessEqual(len(self.line), 200)
        self.assertNotIn("#", self.line)
        hooks = os.path.join(REPO, ".claude", "hooks")
        if os.path.isfile(os.path.join(hooks, "gsc_guard.py")):
            sys.path.insert(0, hooks)
            try:
                import gsc_guard
            finally:
                sys.path.remove(hooks)
            if hasattr(gsc_guard, "PUSH_WEEKLY_RE"):
                self.assertTrue(gsc_guard.PUSH_WEEKLY_RE.match(self.line), self.line)    # the guard's exact form
        held = {h["key"]: h for h in data["held"]}
        self.assertEqual(held["NOVO-B.CO"]["status"], "your decision pending")
        self.assertEqual(held["HFG.DE"]["open_since"], "2026-08-18")
        self.assertTrue(all("avg_cost" not in h and "size" not in h for h in data["held"]))
        weeks = {w["week"]: w for w in data["weekly"]}
        self.assertIn("Import: 46 memos in one commit (b382a33)", weeks["2026-W27"]["note"])
        self.assertEqual(weeks["2026-W28"]["model_releases"], 3)
        self.assertEqual((weeks["2026-W38"]["watch_end"], weeks["2026-W38"]["keys_end"]), (64, 322))
        self.assertEqual(sum(r["keys"] for r in data["coverage"]), 395)
        text = json.dumps(data, ensure_ascii=False)
        self.assertNotIn("avg_cost", text)
        self.assertNotIn("core_", text)

    def test_held_zone_changes_compare_the_zone_word(self):
        self.assertEqual([gw.zone_word(z) for z in ("SELL-FLAG (SR2 — quality re-verdict v11)", "SELL-FLAG SR2", " HOLD",
                                                     "ADD (in band)", "", None, "n/a")],
                         ["SELL-FLAG", "SELL-FLAG", "HOLD", "ADD", "-", "-", "n/a"])
        # 4-11 Oct: the CROX and TROW flags are real changes; NOVO-B.CO and HFG.DE were only relabelled (and
        # the week started before register.csv existed, so the register gives no start zones to compare)
        ctx = gw.build(REPO, FIXED_SHA, when("2026-10-04T08:30+02:00"), when("2026-10-11T08:30+02:00"), self.doc, None)
        self.assertEqual([(z["key"], z["from"], z["to"], z["kind"]) for z in ctx["zone_changes"]],
                         [("CROX", "HOLD", "SELL-FLAG SR2", "memo"), ("TROW", "HOLD", "SELL-FLAG SR2", "memo")])

    def test_copied_text_never_carries_a_private_figure(self):
        ctx = copy.copy(self.ctx)
        ctx["attention"] = {k: list(v) for k, v in self.ctx["attention"].items()}
        ctx["attention"]["Decide"].append({"severity": "medium", "item": "ABC — open item asks for your call",
                                           "detail": "Open item: ABC — bought 120 @ 41.20 on 2026-10-19, avg_cost "
                                                     "39.95 [user, 2026-10-19]", "action": "x", "since": None})
        data, _line = gw.render_all(ctx, self.gen)
        text = json.dumps(data, ensure_ascii=False)
        self.assertNotIn("41.20", text)
        self.assertNotIn("39.95", text)
        self.assertIn("bought 120 [private] on 2026-10-19, [private] [user, 2026-10-19]", text)

    def test_markdown(self):
        md = gw.render_md(self.ctx)
        self.assertTrue(md.startswith("# GSC weekly report — Mon 12 Oct – Mon 19 Oct 2026\n"))
        glance = md.split("## At a glance\n\n", 1)[1].split("\n\n", 1)[0].split("\n")
        self.assertLessEqual(len(glance), 12)
        self.assertIn("WATCH 70 → 66 after pending", glance[0])
        self.assertIsNone(gw.re.search(r"(?<![#\w&])#\d", md))                      # 'PR n', never a hash
        self.assertEqual(md, gw.render_md(self.ctx))
        self.assertNotIn("Digest", md)

    def test_json_is_deterministic_except_generated_at(self):
        later = datetime.datetime(2026, 10, 21, tzinfo=UTC)
        a = json.loads(gw.render_json(self.ctx, self.gen))
        b = json.loads(gw.render_json(self.ctx, later))
        self.assertNotEqual(a["generated_at"], b["generated_at"])
        for d in (a, b):
            d.pop("generated_at")
            d["datasets"]["meta"][0].pop("generated_at")
        self.assertEqual(a, b)

    def test_partial_retest_lines_are_listed_and_counted_open(self):
        self.assertFalse(any(b["item"] == "Re-test lines marked partial" for b in self.data["backlog"]))
        ctx = copy.copy(self.ctx)
        en = dict(self.ctx["en"])
        title = next(iter(en["retest_lines"]))
        en["retest_partial"] = collections.OrderedDict((t, []) for t in en["retest_lines"])
        en["retest_partial"][title] = [("KSPI", "2026-11-01", "queue/evidence/KSPI_2026-11-01_INCOMPLETE.md")]
        ctx["en"] = en
        data = gw.jsonable(gw.datasets(ctx, self.gen))
        self.assertEqual(gw.check_datasets(gw.scrub_private(collections.OrderedDict(
            (n, data[n] if n != "summary" else []) for n in gw.DATASET_IDS))), [])
        row = next(b for b in data["backlog"] if b["item"] == "Re-test lines marked partial")
        self.assertEqual((row["start"], row["end"]), (0, 1))
        self.assertIn("KSPI (2026-11-01, queue/evidence/KSPI_2026-11-01_INCOMPLETE.md)", row["note"])
        block = next(b for b in data["backlog"] if b["note"].startswith("bullets in queue/TODO.md " + title))
        self.assertEqual(block["end"], en["retest_lines"][title])                   # still counted
        self.assertIn("1 marked partial at the end, still open: KSPI (2026-11-01)", block["note"])

    def test_noop_run_from_the_health_input(self):
        rows = HEALTH_DOC + [health_row("GSC ANALYSE QUICK", "ANALYSE", "SUCCEEDED", "2026-10-16T19:30:00Z",
                                        "2026-10-16T19:30:40Z"),
                             health_row("GSC REVIEW QUICK", "REVIEW", "SUCCEEDED", "2026-10-19T04:05:00Z",
                                        "2026-10-19T04:06:00Z")]
        path = os.path.join(TMP, "health_e2e_noop.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(rows, fh)
        ctx = gw.build(REPO, FIXED_SHA, when(SINCE), when(UNTIL), self.doc, gw.load_health(path))
        # REVIEW QUICK opened PR 144 (COLO-B.CO) at 04:06:30Z, inside its span; ANALYSE QUICK opened nothing
        self.assertEqual([t["name"] for t in ctx["noop_runs"]], ["GSC ANALYSE QUICK"])
        fix = [x["item"] for x in ctx["attention"]["Fix"]]
        self.assertIn("ANALYSE routine 'GSC ANALYSE QUICK': likely no-op run", fix)
        self.assertEqual(self.ctx["noop_runs"], [])                                # no finish times: no flag
        md = gw.render_md(ctx)
        self.assertIn("| Took |", md)
        self.assertIn("| 40 s |", md)

    def test_bad_health_is_reported_not_fatal(self):
        ctx = gw.build(REPO, FIXED_SHA, when(SINCE), when(UNTIL), self.doc, None, False,
                       "--health-json x: bad routine 'y'")
        fix = [x for x in ctx["attention"]["Fix"] if x["item"] == "Schedule health unreadable"]
        self.assertEqual(len(fix), 1)
        data, _line = gw.render_all(ctx, self.gen)
        self.assertIsNone(next(k for k in data["kpis"] if k["metric"] == "Analytic runs per scheduled fire")["value"])

    @unittest.skipUnless(have_commit(OLDER_SHA), "older commit not in the repository")
    def test_stale_ref_is_refused(self):
        with self.assertRaises(gw.ToolError) as caught:
            gw.build(REPO, OLDER_SHA, when(SINCE), when(UNTIL), self.doc, self.health)
        self.assertIn("stale ref", str(caught.exception))
        ctx = gw.build(REPO, OLDER_SHA, when(SINCE), when(UNTIL), self.doc, self.health, allow_stale_ref=True)
        self.assertEqual([r["pr"]["number"] for r in ctx["merged_after_ref"]], [149])

    def test_cli_render_is_byte_identical_and_refuses_the_repo(self):
        outs = []
        for name in ("r1", "r2"):
            out = os.path.join(TMP, name)
            code, printed, err = run_main(["render", "--repo-dir", REPO, "--ref", FIXED_SHA, "--since", SINCE,
                                           "--until", UNTIL, "--fetch-dir", FETCH, "--health-json", HEALTH,
                                           "--out-dir", out])
            self.assertEqual(code, 0, err)
            self.assertIn("Mon 12 Oct – Mon 19 Oct 2026", printed)
            outs.append(out)
        names = sorted(os.listdir(outs[0]))
        self.assertEqual(names, sorted([n + ".json" for n in gw.DATASET_IDS] + [gw.NOTICE_FILE]))
        for name in names:
            with open(os.path.join(outs[0], name), encoding="utf-8") as fa, \
                    open(os.path.join(outs[1], name), encoding="utf-8") as fb:
                a, b = fa.read(), fb.read()
            if name == "meta.json":
                a, b = json.loads(a), json.loads(b)
                a[0].pop("generated_at")
                b[0].pop("generated_at")
            self.assertEqual(a, b, name)
        for bad_out in (REPO, os.path.join(REPO, "queue"), os.path.join(REPO, "x", "y")):
            code, _p, err = run_main(["render", "--repo-dir", REPO, "--ref", FIXED_SHA, "--since", SINCE, "--until",
                                      UNTIL, "--fetch-dir", FETCH, "--out-dir", bad_out])
            self.assertEqual(code, 2)
            self.assertIn("inside the repository", err)
        if have_commit(OLDER_SHA):
            code, _p, err = run_main(["render", "--repo-dir", REPO, "--ref", OLDER_SHA, "--since", SINCE, "--until",
                                      UNTIL, "--fetch-dir", FETCH, "--out-dir", os.path.join(TMP, "r3")])
            self.assertEqual(code, 2)
            self.assertIn("stale ref", err)

    def test_cli_lint_summary_apply(self):
        out = os.path.join(TMP, "lint")
        code, _p, err = run_main(["render", "--repo-dir", REPO, "--ref", FIXED_SHA, "--since", SINCE, "--until", UNTIL,
                                  "--fetch-dir", FETCH, "--out-dir", out])
        self.assertEqual(code, 0, err)
        summary = os.path.join(out, "summary.json")
        with open(summary, encoding="utf-8") as fh:
            tool_text = fh.read()
        draft = os.path.join(TMP, "summary_draft.json")
        bad = [{"order": 1, "kind": "takeaway", "text": "A week with 12345 memos."}]
        with open(draft, "w", encoding="utf-8") as fh:
            json.dump(bad, fh)
        code, printed, _e = run_main(["lint-summary", "--datasets", out, "--in", draft, "--apply"])
        self.assertEqual(code, 1)
        self.assertIn("12345", printed)
        with open(summary, encoding="utf-8") as fh:
            self.assertEqual(fh.read(), tool_text)
        good = [{"order": 1, "kind": "takeaway", "text": "18 memos merged; 0 new WATCH."},
                {"order": 2, "kind": "decide", "text": "PR 151 waits for your merge."},
                {"order": 3, "kind": "fix", "text": "No SWEEP merged this week."},
                {"order": 4, "kind": "fix", "text": "The sprint routines failed on the usage limit."},
                {"order": 5, "kind": "know", "text": "MODEL v4.6.0 is live."},
                {"order": 6, "kind": "know", "text": "Nothing else to report."}]
        wrong = [dict(good[0], text="12 memos merged; 0 new WATCH.")] + good[1:]       # 12 is in the corpus
        with open(draft, "w", encoding="utf-8") as fh:
            json.dump(wrong, fh)
        code, printed, _e = run_main(["lint-summary", "--datasets", out, "--in", draft, "--apply"])
        self.assertEqual(code, 1)
        self.assertIn("'12 memos merged' does not match kpis", printed)
        with open(summary, encoding="utf-8") as fh:
            self.assertEqual(fh.read(), tool_text)
        with open(draft, "w", encoding="utf-8") as fh:
            json.dump(good, fh)
        code, _p, _e = run_main(["lint-summary", "--datasets", out, "--in", draft])
        self.assertEqual(code, 0)
        with open(summary, encoding="utf-8") as fh:
            self.assertEqual(fh.read(), tool_text)                         # no --apply: untouched
        code, _p, _e = run_main(["lint-summary", "--datasets", out, "--in", draft, "--apply"])
        self.assertEqual(code, 0)
        with open(summary, encoding="utf-8") as fh:
            self.assertEqual(json.load(fh), good)


@unittest.skipUnless(have_commit(INTAKE_SHA), "INTAKE commit not in the repository")
class SundayWindowTests(unittest.TestCase):
    """The first WEEKLY window (Sun 18 Oct 08:30 – Sun 25 Oct 08:30, 169 h across the DST change) at the
    INTAKE commit of 20 Oct, with the same PR fixtures."""

    def test_render(self):
        since, until = gw.window_of(when("2026-10-25T08:40+01:00"))
        ctx = gw.build(REPO, INTAKE_SHA, since, until, gw.load_fetch(FETCH), None)
        data, line = gw.render_all(ctx, datetime.datetime(2026, 10, 25, 7, 41, tzinfo=UTC))
        meta = data["meta"][0]
        self.assertEqual((meta["period_label"], meta["report_date"], meta["register_to"]),
                         ("Sun 18 Oct – Sun 25 Oct 2026", "2026-10-25", "v319"))
        self.assertEqual(ctx["iso_week"], None)
        self.assertTrue(line.startswith("GSC WEEKLY · Sun 18 Oct – Sun 25 Oct 2026 · "))
        self.assertEqual(next(b for b in data["backlog"] if b["item"] == "Merged row files pending INTAKE")["end"], 0)
        self.assertEqual(data["weekly"][-1]["note"], "Partial week, to Sun 25 Oct 08:30")


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=1).result
    sys.exit(len(result.failures) + len(result.errors))
