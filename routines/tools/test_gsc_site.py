#!/usr/bin/env python3
"""Tests for routines/tools/gsc_site.py (unittest, fixtures inline).

Run:  python3 routines/tools/test_gsc_site.py
Exit code 0 = all pass. Each page test builds a throwaway repository folder
(register.csv, _REGISTER.md, model/MODEL.md, queue/TODO.md, memos and one
archived memo); no git is needed for it.

Covers: determinism (two renders and two CLI runs give identical bytes), the
privacy whitelist (no avg_cost, zone, ADD band, sell line, last zone check,
core number or memo path of a held fixture reaches the page; --no-held removes
the Held marker, its legend line, the holdings sentence of the notice, the
lead's sweep count and the AVOID / not-analysed price dates), HTML escaping of
hostile names and memo text, section membership and counts against
register.csv, the stat strip and the re-test banner (only the '▶ Method
re-tests' blocks count, only keys in the register), distance arithmetic and the
closeness bar, the WATCH reason read from its own distance, buy-zone prices on
BUY and WATCH only, not-analysed rows without grades, returns or multiples,
page order (WATCH by distance, AVOID by EV/OI with n.m. then '-' last), the
artifact page contract (starts with <title>, no html/head/body, no host but
Google Fonts, the token blocks for both themes, localStorage only inside try,
the [hidden] rule the phone cards need, the column order, the notice and the
footer), memo extraction on three memo styles (label stripping,
parentheticals, an 'Unchanged' memo read through its archived predecessor,
ranges and thresholds skipped, a stated negative return, the worse figure of a
pair, one decimal), moat-line repairs (direction before 'moat', a source
before an aside, 'Remains', a cross-reference to another memo, 'real and ...
(source)'), clause-aware clipping, the plain-language reason tables, and that
the tool's own source passes the routine guard hook's code scan. A smoke test
renders the real register when it is present, with and without the Held
marker. v4.6.0: RETIRED rows (G5) stay off the page, its sections, counts and
lead; the plain words for `reinvestment` (G4) and for `unit dependency` and
`sub dependency` (G3, G4); the groups paragraph without the retired too-hard
pile (G2); the one Gate-0 ground left (G2, P30) in the not-analysed reason,
its definition and the first question, and ROE for banks and insurers on the
bank lens only; every '▶ Method re-tests' block counts, the v4.6.0 block
above the v4.5.0 one (the union of their keys, each under its first block's
version), on the page, the banner and stats.
"""
import collections
import contextlib
import io
import json
import os
import re
import shutil
import sys
import tempfile
import unittest
from decimal import Decimal
from html.parser import HTMLParser

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import gsc_site as s  # noqa: E402

TOOL = os.path.join(HERE, "gsc_site.py")

# ------------------------------------------------------------------ fixtures

HEADER = [
    "key", "company", "isin", "aliases", "section", "verdict", "gates_failed",
    "past", "past_reason", "future", "future_reason", "sf", "sf_reason",
    "memo_path", "memo_date", "memo_version", "model_version",
    "px", "px_unit", "px_date", "px_source", "trigger", "mcap_fcf", "ev_oi", "ev_oi_all_cash",
    "next_review_short", "held", "zone", "add_band", "sell_line", "last_zone_check", "avg_cost",
    "core_period", "core_currency", "core_unit", "core_shares_diluted", "core_debt_eq", "core_cash",
    "core_oi", "core_oi_basis", "core_fcf", "core_fcf_basis", "core_fx", "core_fx_date",
    "core_ratio", "core_source",
    "holding_keys", "core_credit",
    "trigger_basis", "core_fcf_all", "core_oi_3y", "core_oi_5y", "core_fcf_3y", "core_fcf_5y",
    "mcap_fcf_3y", "mcap_fcf_5y", "ev_oi_3y", "ev_oi_5y",
]
HOSTILE = '<script>alert("x")</script> & Co'

# Distinctive portfolio-layer and core values that must never reach the page.
SECRET = {"avg_cost": "12345.67 USD", "zone": "SELL-FLAG SR2", "add_band": "11111.1", "sell_line": "22222.2",
          "last_zone_check": "2026-09-09", "core_fcf": "777777", "core_oi": "888888", "core_debt_eq": "999999",
          "core_oi_3y": "666661", "core_fcf_all": "555551"}


def row(key, section, **kw):
    """One register.csv row with neutral defaults."""
    verdict = {"AVOID-1": "AVOID", "AVOID-2": "AVOID"}.get(section, section)
    base = {name: "n.m." for name in HEADER}
    base.update({
        "key": key, "company": key + " Corporation", "isin": "-", "aliases": "n.m.", "section": section,
        "verdict": verdict, "gates_failed": "0", "past": "ADEQUATE", "past_reason": "12.5% ROCE",
        "future": "ADEQUATE", "future_reason": "n.m.", "sf": "PASS", "sf_reason": "n.m.",
        "memo_path": "memos/%s/%s_2026-09-01_GSC.md" % (key, key), "memo_date": "2026-09-01",
        "memo_version": "v1", "model_version": "v4.4.1", "px": "100", "px_unit": "USD",
        "px_date": "2026-10-02", "px_source": "SWEEP 2026-10-05", "trigger": "50", "mcap_fcf": "12.0",
        "ev_oi": "10.0", "ev_oi_all_cash": "9.5", "next_review_short": "Feb 2027", "held": "false",
        "core_period": "FY2025", "core_currency": "USD", "core_unit": "m", "core_shares_diluted": "10",
        "core_debt_eq": "1", "core_cash": "1", "core_oi": "10", "core_oi_basis": "FY2025 J1", "core_fcf": "8",
        "core_fcf_basis": "FY2025", "core_fx": "1", "core_fx_date": "n.m.", "core_ratio": "1",
        "core_source": "memo", "holding_keys": "n.m.", "core_credit": "0", "trigger_basis": "no-cash",
        "core_fcf_all": "8", "core_oi_3y": "-", "core_oi_5y": "-", "core_fcf_3y": "-", "core_fcf_5y": "-",
        "mcap_fcf_3y": "-", "mcap_fcf_5y": "-", "ev_oi_3y": "-", "ev_oi_5y": "-",
    })
    if section == "AVOID-1":
        base.update({"past": "WEAK", "past_reason": "ROCE decline", "gates_failed": "1", "px_source": "memo"})
    if section == "AVOID-2":
        base.update({"past": "WEAK", "past_reason": "8.4% ROCE", "future": "WEAK", "future_reason": "2+ forces",
                     "gates_failed": "2", "px_source": "memo"})
    if section == "DNAF":
        base.update({"past": "n.m.", "past_reason": "n.m.", "future": "n.m.", "sf": "n.m.", "px": "-",
                     "trigger": "n.m.", "mcap_fcf": "n.m.", "ev_oi": "n.m.", "next_review_short": "n.m.",
                     "px_source": "memo", "px_date": "-"})
    base.update(kw)
    return base


def memo(key, sections, front=None):
    fm = {"ticker": key, "exchange": "NYSE", "memo_date": "2026-09-01", "verdict": "WATCH"}
    fm.update(front or {})
    lines = ["---"] + ["%s: %s" % item for item in fm.items()] + ["---", "", "# %s — memo" % key, ""]
    for number, body in sections:
        lines += ["## %s" % number, "", body, ""]
    lines += ["*Framework output, not investment advice.*", "", "---", "", "# APPENDIX", "",
              "## D. Future-performance worksheet", "", "Forces as above.", ""]
    return "\n".join(lines)


MEMO_AAA = memo("AAA", [
    ("1. Verdict", "Understanding PASS, Past STRONG — **WATCH**."),
    ("2. Understanding", "PASS, unchanged. AAA Corporation brews, bottles and distributes its own beer brands "
                         "(Faxe, Albani, Lapin Kulta) and licensed partner brands, selling mainly to grocery "
                         "retailers in Denmark and Finland. It is a mid-cap acquirer. **PASS.**"),
    ("3. Quality — past record", "Worst-of-four normalized ROCE **16.3%** (end-period, with cash; range "
                                 "16.3–18.5%), FCFROCE **12.0%** (range 12.0–13.5%). Both clear the 15%/8% lines."),
    ("4. Quality — future", "Breadth PASS. Forces: one strong. Moat: **Brand**, through local brands with "
                            "distribution depth in small markets. It is **stable**."),
], {"position": "HELD", "avg_cost": SECRET["avg_cost"], "zone": SECRET["zone"]})

MEMO_BBB = memo("BBB.DE", [
    ("1. Verdict", "| Understanding | Past |\n|---|---|\n| PASS | ADEQUATE |"),
    ("2. Understanding", "BBB AG is a Cologne-headquartered broadcaster (founded 1984) that sells audiences to "
                         "advertisers through free TV and streaming in Germany and France. **PASS.**"),
    ("3. Quality — past record", "Worst-of-four 10y normalized averages: ROCE 11.1%, FCFROCE 9.6% — above the "
                                 "P3 floor, well short of P2's 15%."),
    ("4. Quality — future", "Customer power STRONG. The moat (reach and brand in national free TV) is eroding."),
])

MEMO_DDD = memo("DDD.L", [
    ("2. Understanding", "Unchanged. **PASS.**"),
    ("3. Quality — past record", "WEAK. Normalized ROCE is negative on every construction; no read reaches 10%."),
    ("4. Quality — future", "No moat: a commodity product with many rivals."),
])
MEMO_DDD_OLD = memo("DDD.L", [
    ("2. Understanding", "DDD plc makes corrugated packaging for UK grocers from four mills. **PASS.**"),
])

MEMO_GGG = memo("GGG", [
    ("2. Understanding", 'GGG sells <img src=x onerror=alert(1)> widgets & "gadgets" to retailers in many '
                         "countries worldwide. **PASS.**"),
])


class Fixture:
    """A throwaway repository folder for the page tests."""

    def __init__(self, rows=None, files=None):
        self.path = tempfile.mkdtemp(prefix="gsc_site_")
        rows = rows if rows is not None else default_rows()
        buf = io.StringIO(newline="")
        import csv
        writer = csv.writer(buf, lineterminator="\n")
        writer.writerow(HEADER)
        for r in rows:
            writer.writerow([r[name] for name in HEADER])
        content = {
            "register.csv": buf.getvalue(),
            "_REGISTER.md": "---\nregister_title: GSC Register\nregister_version: v9\nregister_date: 2026-10-06\n"
                            "---\n\n# Register\n",
            "model/MODEL.md": "---\nmodel_version: v4.5.0\nmodel_date: 2026-10-06\n---\n\n# Model\n",
            "queue/TODO.md": "# TODO\n\n## ▶ Review requests\n\n- `CCC` — review\n\n"
                             "## ▶ Method re-tests v4.5.0\n\n*Intro.*\n\n**Held — first.**\n\n"
                             "- `AAA` — worth test → AVOID (60%).\n- `ZZZ` — not in the register.\n\n"
                             "## ▶ Other block\n\n- `BBB.DE` — not a re-test.\n",
            "memos/AAA/AAA_2026-09-01_GSC.md": MEMO_AAA,
            "memos/BBB.DE/BBB.DE_2026-09-01_GSC.md": MEMO_BBB,
            "memos/DDD.L/DDD.L_2026-09-01_GSC.md": MEMO_DDD,
            "archive/memos/DDD.L/DDD.L_2026-05-01_GSC.md": MEMO_DDD_OLD,
            "memos/GGG/GGG_2026-09-01_GSC.md": MEMO_GGG,
        }
        content.update(files or {})
        for rel, text in content.items():
            full = os.path.join(self.path, rel)
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(text)

    def close(self):
        shutil.rmtree(self.path, ignore_errors=True)


def default_rows():
    held = row("AAA", "WATCH", px="120", trigger="100", ev_oi="9.1", held="true", sf_reason="buybacks",
               past="STRONG", past_reason="21% ROCE", next_review_short="Aug 2026", **SECRET)
    return [
        held,
        row("BBB.DE", "WATCH", px="50", trigger="45", px_unit="EUR"),
        row("CCC", "WATCH", trigger="-"),
        row("DDD.L", "AVOID-1", ev_oi="n.m.", px_unit="GBp", px="4564", px_date="-"),
        row("EEE.ST", "AVOID-1", ev_oi="5.0", px_unit="SEK", sf="FAIL", sf_reason="flag pair", past="ADEQUATE",
            past_reason="12.5% ROCE"),
        row("FFF", "AVOID-1", ev_oi="-", future="WEAK", future_reason="moat gone", past="ADEQUATE",
            past_reason="12.5% ROCE"),
        row("GGG", "AVOID-2", company=HOSTILE),
        row("HHH", "DNAF"),
    ]


def render(fixture, no_held=False):
    ctx, sections, _extraction, _rows = s.build(fixture.path, no_held=no_held)
    return s.render_page(ctx, sections)


def page_data(page):
    blob = page.split('<script type="application/json" id="gsc-data">', 1)[1].split("</script>", 1)[0]
    return json.loads(blob)


def run_main(argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = s.main(argv)
    return code, out.getvalue(), err.getvalue()


# ------------------------------------------------------------------ tests

class PageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fx = Fixture()
        cls.page = render(cls.fx)
        cls.data = page_data(cls.page)
        cls.rows = {r["k"]: r for sec in cls.data["sections"] for r in sec["rows"]}

    @classmethod
    def tearDownClass(cls):
        cls.fx.close()

    def test_render_is_deterministic(self):
        self.assertEqual(render(self.fx), self.page)
        out = tempfile.mkdtemp(prefix="gsc_site_out_")
        try:
            paths = [os.path.join(out, name) for name in ("a.html", "b.html")]
            for path in paths:
                code, _out, err = run_main(["render", "--out", path, "--repo", self.fx.path])
                self.assertEqual(code, 0, err)
            with open(paths[0], "rb") as fa, open(paths[1], "rb") as fb:
                first, second = fa.read(), fb.read()
            self.assertEqual(first, second)
            self.assertEqual(first, self.page.encode("utf-8"))
            self.assertNotIn(b"\r\n", first)
            self.assertFalse(first.startswith(b"\xef\xbb\xbf"))
        finally:
            shutil.rmtree(out, ignore_errors=True)

    def test_privacy_no_portfolio_layer_or_core_numbers(self):
        for name, value in SECRET.items():
            self.assertNotIn(value, self.page, name)
            self.assertNotIn(value.split()[0], self.page, name)              # the number without its unit
        for word in ("avg_cost", "add_band", "sell_line", "last_zone_check", "core_", "memos/", "SELL-FLAG",
                     "12345", "HELD"):
            self.assertNotIn(word, self.page)
        allowed = {"k", "n", "c", "h", "r", "b", "na", "m", "rl", "ro", "fr", "p", "pw", "f", "fw", "s", "sw",
                   "mf", "eo", "mf3", "mf5", "eo3", "eo5", "u", "px", "pd", "tg", "tl", "v", "vw", "vq", "d", "dl",
                   "bw", "md", "nr", "nd"}
        for word in ("core_oi_3y", "core_fcf_all", "trigger_basis", "666661", "555551"):
            self.assertNotIn(word, self.page)
        for r in self.rows.values():
            self.assertLessEqual(set(r), allowed)

    def test_held_marker_and_no_held_flag(self):
        self.assertEqual(self.rows["AAA"].get("h"), 1)
        self.assertNotIn("h", self.rows["BBB.DE"])
        self.assertIn("<dt>Held</dt>", self.page)
        self.assertIn("The author holds shares in the companies marked Held.", self.page)
        bare = render(self.fx, no_held=True)
        self.assertNotIn('"h":', bare)
        self.assertNotIn("Held", bare)
        self.assertNotIn("held", bare.lower().replace("threshold", ""))
        self.assertIn("The author may hold shares in companies on this page.", bare)
        for name, value in SECRET.items():
            self.assertNotIn(value, bare, name)

    def test_no_held_names_no_sweep_and_dates_only_buy_and_watch_prices(self):
        # A sweep prices BUY, WATCH, one-test AVOID and every held name: under --no-held neither the
        # lead's sweep count nor a dated AVOID price may single out a held name.
        held_avoid = row("JJJ", "AVOID-2", held="true", px_source="SWEEP 2026-10-05", px_date="2026-10-05")
        fx = Fixture(rows=default_rows() + [held_avoid])
        try:
            full, bare = render(fx), render(fx, no_held=True)
        finally:
            fx.close()
        self.assertIn("from the latest price sweep", full)
        self.assertNotIn("sweep", bare)
        self.assertIn("A BUY or WATCH price shows its date; for AVOID and not-analysed companies the price is "
                      "context only and is shown undated.", bare)
        full_rows = {r["k"]: r for sec in page_data(full)["sections"] for r in sec["rows"]}
        bare_rows = {r["k"]: r for sec in page_data(bare)["sections"] for r in sec["rows"]}
        self.assertEqual(full_rows["JJJ"]["pd"], "as of 5 Oct 2026")
        self.assertEqual(full_rows["GGG"]["pd"], "as of 2 Oct 2026")
        for key in ("JJJ", "GGG", "DDD.L", "EEE.ST"):
            self.assertEqual(bare_rows[key]["pd"], "", key)
            self.assertEqual(bare_rows[key]["px"], full_rows[key]["px"], key)    # the price stays, undated
        self.assertEqual(bare_rows["BBB.DE"]["pd"], "as of 2 Oct 2026")          # WATCH stays dated
        self.assertNotIn("5 Oct 2026", bare)

    def test_hostile_text_is_escaped(self):
        self.assertNotIn("<script>alert", self.page)
        self.assertNotIn("<img", self.page)
        self.assertEqual(self.page.count("<script"), 2)          # the data blob and the page script
        self.assertEqual(self.rows["GGG"]["n"], HOSTILE)        # intact as data, escaped as markup
        self.assertIn("\\u003cscript\\u003e", self.page)
        self.assertIn("function esc(", self.page)
        self.assertNotIn("onerror", self.page)                     # memo markup is stripped, not passed on
        self.assertEqual(self.rows["GGG"]["b"], 'GGG sells widgets & "gadgets" to retailers in many countries '
                                                'worldwide.')
        self.assertIn("\\u0026 \\\"gadgets\\\"", self.page)

    def test_sections_and_counts_match_the_register(self):
        ids = [sec["id"] for sec in self.data["sections"]]
        self.assertEqual(ids, list(s.SECTION_ORDER))
        members = {sec["id"]: [r["k"] for r in sec["rows"]] for sec in self.data["sections"]}
        expected = {}
        for r in default_rows():
            expected.setdefault(r["section"], set()).add(r["key"])
        for section in s.SECTION_ORDER:
            self.assertEqual(set(members[section]), expected.get(section, set()), section)
        strip = self.page.split('<div class="strip"', 1)[1].split("</div>\n  </div>", 1)[0]
        numbers = [int(x) for x in re.findall(r"<b>(\d+)</b>", strip)]
        self.assertEqual(numbers, [8, 0, 3, 3, 1, 1, 1])   # covered, BUY, WATCH, AVOID-1, AVOID-2, DNAF, re-test
        self.assertEqual(self.rows["AAA"].get("r"), 1)       # in the re-test block
        self.assertNotIn("r", self.rows["BBB.DE"])           # listed in another block only
        plain = self.page.replace("<b>", "").replace("</b>", "")
        self.assertIn("1 company is being re-tested", plain)
        self.assertIn("Treat its verdict as provisional: it may change, including from WATCH to AVOID.", plain)
        # The section labels read the same on the stat tile, the chip and the section title.
        for section in s.SECTION_ORDER:
            label = s.esc(s.SECTIONS[section][0])
            self.assertIn("<span>%s</span>" % label, strip)
            self.assertEqual([sec["title"] for sec in self.data["sections"] if sec["id"] == section],
                             [s.SECTIONS[section][0]])
        self.assertIn('data-f="WATCH" aria-pressed="false">WATCH · shortlist <span class="chip-n">3</span>',
                      self.page)
        self.assertIn('<div class="stat stat-note"><b>1</b><span>Being re-tested</span></div>', self.page)

    def test_retest_banner_counts_the_shortlist(self):
        ctx = {"retest_count": 89, "retest_watch": 82, "retest_version": "v4.5.0",
               "counts": {"WATCH": 88}}
        banner = s.retest_banner(ctx).replace("<b>", "").replace("</b>", "")
        self.assertIn("89 companies, including 82 of the 88 on the shortlist, are being re-tested under an "
                      "updated version of the method (v4.5.0). Treat their verdicts as provisional: they may "
                      "change, including from WATCH to AVOID.", banner)
        ctx.update(retest_count=0)
        self.assertEqual(s.retest_banner(ctx), "")

    def test_distance_arithmetic(self):
        gap, fall = s.distance("118.09", "97.9")
        self.assertEqual(s.fmt_signed_pct(gap), "+20.6%")
        self.assertEqual(s.fmt_pct(fall), "17.1%")
        self.assertEqual(self.rows["AAA"]["d"], "+20.0%")      # 120 / 100 - 1
        self.assertEqual(self.rows["AAA"]["dl"], "16.7%")      # 1 - 100 / 120
        self.assertEqual(self.rows["AAA"]["bw"], 83)           # closeness: buy-zone price / price = 100 / 120
        self.assertEqual(self.rows["BBB.DE"]["d"], "+11.1%")
        self.assertEqual(self.rows["BBB.DE"]["bw"], 90)        # 45 / 50: nearer, so a longer bar
        self.assertEqual(self.rows["CCC"]["d"], s.DASH)
        self.assertNotIn("bw", self.rows["CCC"])
        self.assertEqual(s.distance("90", "100")[1], 0)
        self.assertIsNone(s.distance("-", "10"))
        self.assertIsNone(s.distance("10", "n.m."))
        self.assertIsNone(s.distance("10", "0"))
        self.assertEqual(self.rows["DDD.L"]["d"], s.DASH)     # AVOID: no buy-zone distance
        self.assertNotIn("bw", self.rows["DDD.L"])
        in_zone = s.page_row(row("III", "WATCH", px="40", trigger="50"), "", {}, "2026-10-06", True, False)
        self.assertEqual((in_zone["d"], in_zone["dl"], in_zone["bw"]), ("In zone", "", 100))   # capped full bar
        # Whole percent from 100% up; one decimal below; never '-0.0%'.
        self.assertEqual(s.fmt_signed_pct(Decimal("5.65")), "+565%")
        self.assertEqual(s.fmt_signed_pct(Decimal("0.9996")), "+100%")
        self.assertEqual(s.fmt_signed_pct(Decimal("0.999")), "+99.9%")
        self.assertEqual(s.fmt_signed_pct(Decimal("-0.0004")), "0.0%")
        self.assertIn("fall needed: ", s.PAGE_SCRIPT)

    def test_watch_reason_reads_its_own_distance(self):
        self.assertEqual(self.rows["AAA"]["vw"], s.WATCH_WHY)
        self.assertEqual(self.rows["AAA"]["vq"], 1)                  # repeats the section note: quiet on phones
        self.assertEqual(self.rows["CCC"]["vw"], "Passes all three quality tests; no buy-zone price is available.")
        self.assertNotIn("vq", self.rows["CCC"])
        in_zone = s.page_row(row("III", "WATCH", px="50", trigger="50"), "", {}, "2026-10-06", True, False)
        self.assertEqual(in_zone["vw"], "Passes all three quality tests; the latest price is at or below the "
                                        "buy-zone price, pending review.")
        self.assertNotIn("vq", in_zone)
        self.assertEqual(in_zone["d"], "In zone")

    def test_buy_zone_price_only_for_buy_and_watch(self):
        self.assertEqual(self.rows["AAA"]["tg"], "100")
        self.assertEqual(self.rows["CCC"]["tg"], s.DASH)                 # WATCH without a numeric trigger
        for key in ("DDD.L", "EEE.ST", "FFF", "GGG", "HHH"):
            self.assertNotIn("tg", self.rows[key], key)                   # AVOID and DNAF: no buy zone
        self.assertIn("no buy zone: fails a quality test", s.PAGE_SCRIPT)
        self.assertIn("no buy-zone price", s.PAGE_SCRIPT)
        self.assertNotIn("buy zone ≤ n.m.", s.PAGE_SCRIPT)

    def test_not_analysed_rows_carry_no_grades_returns_or_multiples(self):
        dnaf = self.rows["HHH"]
        self.assertEqual(dnaf["na"], 1)
        for field in ("p", "pw", "f", "fw", "s", "sw", "ro", "fr", "m"):
            self.assertEqual(dnaf[field], "", field)
        self.assertEqual((dnaf["mf"], dnaf["eo"], dnaf["d"]), (s.DASH, s.DASH, s.DASH))
        self.assertEqual(dnaf["v"], "DNAF")
        self.assertEqual(dnaf["vw"], s.DNAF_WHY_EARLIER)                 # a DNAF memo below v4.6.0
        # An older memo's grades and figures never reach a not-analysed row.
        old = s.page_row(row("KKK", "DNAF", past="ADEQUATE", past_reason="14.7% ROCE", future="WEAK",
                             sf="FAIL", sf_reason="control", mcap_fcf="12.0"), "", {"moat": "Brand", "roce": "9%"},
                         "2026-10-06", True, False)
        self.assertEqual((old["p"], old["f"], old["s"], old["ro"], old["m"], old["mf"]), ("", "", "", "", "", s.DASH))
        self.assertNotIn("na", self.rows["AAA"])
        self.assertIn("not assessed", s.PAGE_SCRIPT)

    def test_page_order(self):
        members = {sec["id"]: [r["k"] for r in sec["rows"]] for sec in self.data["sections"]}
        self.assertEqual(members["WATCH"], ["BBB.DE", "AAA", "CCC"])       # +11.1%, +20.0%, no trigger
        self.assertEqual(members["AVOID-1"], ["EEE.ST", "DDD.L", "FFF"])   # 5.0, n.m., -

    def test_artifact_page_contract(self):
        page = self.page
        self.assertTrue(page.startswith("<title>GSC Research Register</title>\n"))
        self.assertIsNone(re.search(r"(?i)<!doctype|</?(html|head|body)[\s>]", page))
        hosts = set(re.findall(r"https?://([^/\"'\s)]+)", page))
        self.assertLessEqual(hosts, {"fonts.googleapis.com", "fonts.gstatic.com"})
        self.assertNotIn("fetch(", page)
        self.assertNotIn("<img", page)
        style = page.split("<style>", 1)[1].split("</style>", 1)[0]
        self.assertTrue(re.match(r"\s*/\* Layout: [^\n]*\*/\s*:root\{", style))
        self.assertIn('@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){', style)
        self.assertIn(':root[data-theme="dark"]{', style)
        self.assertIn("body{background:var(--bg)", style)
        self.assertIn("prefers-reduced-motion", style)
        self.assertIn("tabular-nums", style)
        self.assertIn("padding-inline:16px", style)
        self.assertIn("@media (max-width:640px)", style)
        self.assertIn("overflow:auto", style)
        # Every color is a token: literal colors appear only inside the three token blocks.
        outside = re.sub(r":root\{[^}]*\}|:root:not\(\[data-theme=\"light\"\]\)\{[^}]*\}|"
                         r":root\[data-theme=\"dark\"\]\{[^}]*\}", "", style)
        self.assertIsNone(re.search(r"#[0-9a-fA-F]{3,8}\b|rgba?\(", outside))
        script = s.PAGE_SCRIPT
        for banned in ("alert(", "confirm(", "prompt(", "print(", "fetch(", "XMLHttpRequest", "style.display"):
            self.assertNotIn(banned, script)
        for m in re.finditer(r"localStorage", script):
            self.assertIn("try {", script[max(0, m.start() - 40):m.start()])
        self.assertIn(".hidden =", script)
        self.assertLess(len(page.encode("utf-8")), 2 * 1024 * 1024)
        self.assertIn("not investment advice", page)
        self.assertIn("Framework output, not investment advice.", page)
        self.assertIn("v4.5.0", page.split('<p class="foot">', 1)[1])

    def test_phone_cards_hide_filtered_rows(self):
        # The card CSS sets tr display:grid/block, which beats the browser's own [hidden] rule:
        # without this line a phone filter changes the count and hides nothing.
        style = self.page.split("<style>", 1)[1].split("</style>", 1)[0]
        self.assertIn("[hidden]{display:none!important}", style)
        phone = style.split("@media (max-width:640px){", 1)[1]
        self.assertIn(".strip{display:grid;grid-template-columns:repeat(2,minmax(0,1fr))}", phone)
        self.assertIn(".controls{position:sticky;top:0", phone)
        self.assertIn(".chiprow{flex-wrap:nowrap;overflow-x:auto", phone)    # one chip row, scrolled sideways
        self.assertIn(".why-q{display:none}", phone)
        self.assertIn('<div class="chiprow">', self.page)

    def test_reading_order_notice_and_footer(self):
        head = self.page.split("<thead>", 1)[1].split("</thead>", 1)[0]
        self.assertEqual(re.findall(r'<th scope="col" class="w-[a-z]+">([^<]+)</th>', head),
                         ["Company", "Verdict", "To buy zone", "Price · buy zone", "Business",
                          "Returns · past record", "Competitive position", "Shareholder-friendliness", "MCap/FCF",
                          "EV/OI", "Memo · next review"])
        cells = re.findall(r"cell\('([a-z -]+)', '([^']*)'", s.PAGE_SCRIPT)
        self.assertEqual([label for _cls, label in cells],
                         ["", "Verdict", "To buy zone", "Price · buy zone", "Business", "Returns · past record",
                          "Competitive position", "Shareholder-friendliness", "MCap/FCF", "EV/OI",
                          "Memo · next review"])
        self.assertIn('<p class="fresh">Register v9 · updated 6 Oct 2026</p>', self.page)
        self.assertIn("Good Stocks Cheap (GSC) method", self.page)
        notice = self.page.split('<p class="notice" role="note">', 1)[1].split("</p>", 1)[0]
        for words in ("Not investment advice.", "not a recommendation to buy or sell any security",
                      "may contain errors or be out of date", "Not affiliated with or endorsed by Kenneth Jeffrey "
                      "Marshall."):
            self.assertIn(words, notice)
        foot = self.page.split('<p class="foot">', 1)[1].split("</p>", 1)[0]
        self.assertIn("Current method version v4.5.0", foot)
        self.assertIn("each row was assessed under the version in force on its memo date", foot)
        self.assertIn("taken from the memos", foot)
        self.assertNotIn("quoted from", foot)
        self.assertIn('class="vkey"', self.page)
        self.assertIn('<div class="tablebox" tabindex="0" role="region" aria-label="Register table">', self.page)
        self.assertIn('<caption class="sr">', self.page)
        self.assertIn("A research register of 8 companies,", self.page)     # not 'listed': some have no share
        # The method panel and the thresholds state P3 in full: path (b) needs FCFROCE >= 5.3%.
        self.assertIn("ROCE of at least 10% and FCFROCE of at least 5.3% with both growing at least 6% a year",
                      self.page)
        self.assertIn("FCFROCE <code>≥ 5.3%</code>", self.page)
        self.assertIn("The buy-zone price is the highest price at which both hold with no cash counted as spare.",
                      self.page)
        self.assertNotIn("the looser reading)", self.page)

    def test_markup_is_balanced(self):
        class Checker(HTMLParser):
            VOID = {"link", "input", "br", "meta", "img", "hr"}

            def __init__(self):
                super().__init__(convert_charrefs=True)
                self.stack, self.errors, self.ids = [], [], []

            def handle_starttag(self, tag, attrs):
                self.ids += [v for k, v in attrs if k == "id"]
                if tag not in self.VOID:
                    self.stack.append(tag)

            def handle_endtag(self, tag):
                if not self.stack or self.stack[-1] != tag:
                    self.errors.append((tag, list(self.stack[-3:])))
                else:
                    self.stack.pop()

        for page in (self.page, render(self.fx, no_held=True)):
            checker = Checker()
            checker.feed(page)
            checker.close()
            self.assertEqual((checker.errors, checker.stack), ([], []))
            self.assertEqual(len(checker.ids), len(set(checker.ids)))

    def test_plain_language_reasons(self):
        self.assertEqual(self.rows["EEE.ST"]["sw"], "Two separate governance warning signs")
        self.assertNotIn("flag pair", self.page)
        self.assertEqual(self.rows["FFF"]["fw"], "moat gone")                 # unknown token as written
        self.assertEqual(self.rows["DDD.L"]["pw"], "returns on capital in sustained decline")
        self.assertEqual(self.rows["DDD.L"]["vw"], "Failed the past-record test: returns on capital in "
                                                   "sustained decline.")
        self.assertEqual(self.rows["GGG"]["vw"], "Failed two tests: past record and competitive position.")
        self.assertEqual(self.rows["GGG"]["pw"], "return on capital too low (8.4%)")
        self.assertEqual(s.past_why("WEAK", "sub 6.15% ROE"), "in a listed subsidiary: return on equity too low "
                                                              "(6.2%)")
        self.assertEqual(s.past_why("ADEQUATE", "12.5% ROCE"), "")           # the Returns cell shows the level
        # MODEL P15 (R7): silence on concentration counts for a business selling to businesses; any paying
        # customer counts, distributors and retailers included.
        self.assertEqual(s.plain_reason(s.PLAIN_FUTURE, "customer conc."),
                         "a customer above 10% of revenue (distributors and retailers included), or concentration "
                         "not ruled out in its filings")
        self.assertEqual(self.rows["AAA"]["sw"], "One caution: share buybacks at prices the method judges too high")
        self.assertEqual(s.plain_reason(s.PLAIN_PAST, "unit losses"), "in one business unit: losses in the "
                                                                       "financial record")
        self.assertEqual(self.rows["HHH"]["v"], "DNAF")
        self.assertEqual(self.rows["AAA"]["nd"], 1)                          # Aug 2026 < register date
        self.assertNotIn("nd", self.rows["BBB.DE"])
        self.assertEqual(self.rows["DDD.L"]["pd"], "price at memo date")
        self.assertEqual(self.rows["DDD.L"]["px"], "4,564")
        self.assertEqual(self.rows["BBB.DE"]["c"], "Germany")
        self.assertEqual(self.rows["DDD.L"]["c"], "UK")
        self.assertEqual(self.rows["EEE.ST"]["c"], "Sweden")
        self.assertIn("GBp = pence", self.page)


class ExtractionTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fx = Fixture()
        rows, _fm = s.load_register(cls.fx.path)
        cls.ex = s.extract_all(cls.fx.path, rows)

    @classmethod
    def tearDownClass(cls):
        cls.fx.close()

    def test_business_sentence(self):
        self.assertEqual(self.ex["AAA"]["business"],
                         "AAA Corporation brews, bottles and distributes its own beer brands and licensed partner "
                         "brands, selling mainly to grocery retailers in Denmark and Finland. It is a mid-cap "
                         "acquirer.")
        self.assertEqual(self.ex["BBB.DE"]["business"],
                         "BBB AG is a Cologne-headquartered broadcaster that sells audiences to advertisers "
                         "through free TV and streaming in Germany and France.")
        self.assertEqual(self.ex["DDD.L"]["business"],
                         "DDD plc makes corrugated packaging for UK grocers from four mills.")
        self.assertEqual(self.ex["DDD.L"]["business_from"], "archive")
        self.assertEqual(self.ex["EEE.ST"]["business"], "")                 # no memo on disk: em dash on the page
        long = "Foo makes " + ", ".join("widget type %d" % i for i in range(40)) + "."
        clipped = s.business_from_paragraphs([long])
        self.assertLessEqual(len(clipped), s.BUSINESS_MAX)
        self.assertTrue(clipped.endswith("…"))

    def test_moat_line(self):
        self.assertEqual(self.ex["AAA"]["moat"], "Brand, through local brands with distribution depth in small markets")
        self.assertEqual(self.ex["BBB.DE"]["moat"], "Reach and brand in national free TV, eroding")
        self.assertEqual(self.ex["DDD.L"]["moat"], "No moat: a commodity product with many rivals")
        self.assertEqual(s.extract_moat(memo("X", [("4. Quality — future", "The brand moat is stable-to-"
                                                     "strengthening on record sales of 12%.")]))[0],
                         "Brand moat, stable-to-strengthening")
        self.assertEqual(s.extract_moat(memo("X", [("4. Quality — future", "Moat stable, contested.")])),
                         ("Stable, contested", 1))

    def test_moat_line_repairs(self):
        def moat(sentence):
            return s.extract_moat(memo("X", [("4. Quality — future", sentence)]))[0]

        # A direction before 'moat' stays the subject: the evidence of erosion is not the moat itself.
        self.assertEqual(moat("Moat: an eroding moat: Chinese EV entrants taking its historic China profit pool."),
                         "Eroding moat: Chinese EV entrants taking its historic China profit pool")
        # 'The brand moat — an aside — is ...': the source before the aside stays the subject.
        self.assertEqual(moat("The brand moat — once the strongest in autos — is directly contradicted by years "
                              "of price-cutting."), "Brand moat: directly contradicted by years of price-cutting")
        self.assertEqual(moat("Moat: Remains Network/Cost — the edge plus the free-tier data flywheel — "
                              "strengthening."), "Network/Cost — the edge plus the free-tier data flywheel — "
                                                 "strengthening")
        # A cross-reference to another company's memo means nothing to a reader.
        self.assertEqual(moat("Moat: the development lead eroded into a commodity auction spread — the NESTE.HE "
                              "shape: no pricing power."), "The development lead eroded into a commodity auction "
                                                            "spread")
        self.assertEqual(moat("Moat: real and singularly sourced (switching costs via CUDA ingrainedness), dominant "
                              "today but eroding at the margins."),
                         "Switching costs via CUDA ingrainedness, dominant today but eroding at the margins")

    def test_clip_ends_on_a_whole_clause(self):
        # A closed aside late in the text is cut where it opens, never at its closing dash.
        self.assertEqual(s.clip("Finnish manufacturer and servicer of elevators, escalators and automatic building "
                                "doors; new equipment to developers and owners and — the profit engine — recurring "
                                "maintenance and modernisation on a large installed base across about seventy "
                                "countries worldwide.", 200),
                         "Finnish manufacturer and servicer of elevators, escalators and automatic building doors; "
                         "new equipment to developers and owners…")
        # A comma cut never keeps a stub clause (', that designs').
        self.assertEqual(s.clip("Kalmar Corporation is a Helsinki-headquartered Finnish company, listed since July "
                                "2024 and controlled through unlisted class A shares by three family companies, that "
                                "designs, assembles and services heavy material-handling machines for ports.", 200),
                         "Kalmar Corporation is a Helsinki-headquartered Finnish company, listed since July 2024 "
                         "and controlled through unlisted class A shares by three family companies…")
        # A list in an aside still open at the cut may end at one of its commas.
        self.assertEqual(s.clip("Beiersdorf is a Hamburg-headquartered, family-controlled manufacturer of "
                                "differentiated branded skin- and body-care products — NIVEA, Eucerin, Aquaphor, "
                                "La Prairie, Chantecaille, Coppertone — sold to grocery and drugstore chains.", 190),
                         "Beiersdorf is a Hamburg-headquartered, family-controlled manufacturer of differentiated "
                         "branded skin- and body-care products — NIVEA, Eucerin, Aquaphor, La Prairie, "
                         "Chantecaille…")
        # An aside opening early is main text: its closing dash is a clean break ('and it is,' is a stub).
        self.assertEqual(s.clip("Cost — leading-edge volume no rival can match spreads process R&D and tool fleets "
                                "over more wafers — and it is, by any measure, strengthening.", 120),
                         "Cost — leading-edge volume no rival can match spreads process R&D and tool fleets over "
                         "more wafers…")
        self.assertEqual(s.clip("Short enough.", 120), "Short enough.")
        for limit in (60, 120, 260):
            text = "Word " * 100
            self.assertLessEqual(len(s.clip(text, limit)), limit)

    def test_returns(self):
        self.assertEqual((self.ex["AAA"]["roce"], self.ex["AAA"]["fcfroce"]), ("16.3%", "12.0%"))
        self.assertEqual((self.ex["BBB.DE"]["roce"], self.ex["BBB.DE"]["fcfroce"]), ("11.1%", "9.6%"))
        self.assertEqual(self.ex["DDD.L"]["roce"], "negative")
        self.assertEqual(s.first_figure(" across bounds: 20.6–23.8% end, worst ≈ 20.6%"), "20.6%")
        self.assertEqual(s.first_figure(" clears the 10% floor"), "")
        self.assertEqual(s.first_figure(" is −1.3% and FCFROCE 3.9%"), "−1.3%")
        self.assertEqual(s.extract_returns(memo("X", [("3. Quality — past record",
                                                       "Substitution rule applied: ROE replaces ROCE, FCFROCE "
                                                       "n.m. Worst normalized ROE 12.3%.")])), ("", "n.m."))
        # A pair or a span of readings gives the worse one; at most one decimal.
        self.assertEqual(s.first_figure(" worst-of-four −3.8% to −3.9% across reads"), "−3.9%")
        self.assertEqual(s.first_figure(" is −9.1% / −13.5% on the two windows"), "−13.5%")
        self.assertEqual(s.first_figure(" is 12.0% or 11.2%"), "11.2%")
        self.assertEqual(s.first_figure(" of 8.42% at worst"), "8.4%")
        self.assertEqual((s.one_decimal_pct("8.45%"), s.one_decimal_pct("21%"), s.one_decimal_pct("negative")),
                         ("8.5%", "21%", "negative"))

    def test_page_prefers_the_register_level(self):
        fx = Fixture()
        try:
            page = render(fx)
        finally:
            fx.close()
        rows = {r["k"]: r for sec in page_data(page)["sections"] for r in sec["rows"]}
        self.assertEqual((rows["AAA"]["rl"], rows["AAA"]["ro"], rows["AAA"]["fr"]), ("ROCE", "21%", "12.0%"))
        self.assertEqual(rows["DDD.L"]["ro"], "negative")                    # register reason is not a level
        self.assertEqual(rows["CCC"]["ro"], "12.5%")                         # level, no memo


class RoundTwoTests(unittest.TestCase):
    """MODEL v4.5.0 round 2 on the page: the no-cash trigger (R10), the averaged readings, the concentration
    caveat (R7), groups and the too-hard pile (R3-R5), and the SF vocabulary (R8)."""

    @classmethod
    def setUpClass(cls):
        cls.fx = Fixture(rows=default_rows() + [
            row("LLL", "WATCH", trigger_basis="all-cash", trigger="80", px="90", mcap_fcf_3y="9.4", mcap_fcf_5y="10.1",
                ev_oi_3y="n.m.", ev_oi_5y="12.0"),
            row("MMM", "AVOID-1", trigger_basis="all-cash", future="ADEQUATE", sf="FAIL", sf_reason="alignment"),
            row("NNN", "WATCH", future_reason="customer conc."),
        ])
        cls.page = render(cls.fx)
        cls.rows = {r["k"]: r for sec in page_data(cls.page)["sections"] for r in sec["rows"]}

    @classmethod
    def tearDownClass(cls):
        cls.fx.close()

    def test_required_columns_r10(self):
        for name in ("trigger_basis", "mcap_fcf_3y", "mcap_fcf_5y", "ev_oi_3y", "ev_oi_5y"):
            self.assertIn(name, s.REQUIRED_COLUMNS)
        for name in ("core_oi_3y", "core_oi_5y", "core_fcf_3y", "core_fcf_5y", "core_fcf_all"):
            self.assertNotIn(name, s.REQUIRED_COLUMNS)              # the privacy whitelist: no core numbers
        old = ",".join(n for n in HEADER if n != "trigger_basis") + "\n"
        fx = Fixture(files={"register.csv": old})
        try:
            with self.assertRaises(s.ToolError) as caught:
                s.load_register(fx.path)
        finally:
            fx.close()
        self.assertIn("lacks columns: trigger_basis", str(caught.exception))

    def test_page_row_averaged_multiples(self):
        lll = self.rows["LLL"]
        self.assertEqual((lll["mf3"], lll["mf5"], lll["eo3"], lll["eo5"]), ("9.4×", "10.1×", "n.m.", "12.0×"))
        self.assertEqual((self.rows["AAA"]["mf3"], self.rows["AAA"]["eo5"]), (s.DASH, s.DASH))     # owed
        dnaf = s.page_row(row("KKK", "DNAF", mcap_fcf_3y="9.0"), "", {}, "2026-10-06", True, False)
        self.assertEqual([dnaf[n] for n in ("mf3", "mf5", "eo3", "eo5")], [s.DASH] * 4)
        self.assertIn("function multiple(value, y3, y5)", s.PAGE_SCRIPT)
        self.assertIn("3y ' + esc(y3) + ' · 5y ' + esc(y5)", s.PAGE_SCRIPT)
        self.assertIn('if (y3 !== "—" || y5 !== "—")', s.PAGE_SCRIPT)      # owed on both sides: no sub-line
        self.assertIn("cell('c-n num', 'MCap/FCF', multiple(r.mf, r.mf3, r.mf5))", s.PAGE_SCRIPT)
        self.assertIn("cell('c-n num', 'EV/OI', multiple(r.eo, r.eo3, r.eo5))", s.PAGE_SCRIPT)

    def test_legacy_trigger_marked(self):
        # R10: a BUY/WATCH trigger still on the pre-R10 all-cash reading is marked; its distance still shows.
        lll = self.rows["LLL"]
        self.assertEqual((lll["tl"], lll["tg"], lll["d"]), (1, "80", "+12.5%"))
        self.assertNotIn("tl", self.rows["BBB.DE"])                       # no-cash
        self.assertNotIn("tl", self.rows["MMM"])                          # AVOID: no buy zone at all
        self.assertNotIn("tg", self.rows["MMM"])
        owed = s.page_row(row("OWE", "WATCH", trigger_basis="all-cash", trigger="-"), "", {}, "2026-10-06", True,
                          False)
        self.assertNotIn("tl", owed)                                       # nothing to mark
        self.assertEqual(page_data(self.page)["legacy"], "older, looser reading — review pending")
        self.assertIn("if (r.tl) out += '<span class=\"sub old\">' + esc(DATA.legacy) + '</span>';", s.PAGE_SCRIPT)
        self.assertIn(".sub.old{color:var(--fair)", self.page)

    def test_terms_buy_zone_is_strict(self):
        terms = s.terms({"units": [], "retest_count": 0, "held_marker": False})
        self.assertIn("with no cash counted as spare — the strict reading a BUY needs. A marked figure is an older, "
                      "looser reading (spare cash counted) awaiting its review.", terms)
        self.assertIn("<dt>3y · 5y</dt><dd>The same multiples at today&#x27;s price on the average operating income "
                      "and free cash flow of the last three and five years: a check against one unusual year.</dd>",
                      terms)
        self.assertIn("less the capital spending needed to maintain the business (the company&#x27;s figure or a "
                      "stated estimate); growth spending is not counted against it. A row not yet reviewed under "
                      "the updated method may still deduct all capital spending, which can only make this multiple "
                      "look higher.", terms)
        self.assertIn("The buy-zone price is the highest price at which both hold with no cash counted as spare.",
                      self.page)
        self.assertIn("the lower of the three- and five-year averages is used instead", self.page)
        self.assertIn("EV/OI <code>≤ 7×</code>, no cash counted as spare", self.page)

    def test_future_caveat_plain_text(self):
        # R7: a concentration is a flag - a caveat under a strong moat, otherwise it weighs toward Weak.
        self.assertEqual(self.rows["NNN"]["fw"], "Passes, with a caveat: a customer above 10% of revenue "
                                                 "(distributors and retailers included), or concentration not ruled "
                                                 "out in its filings")
        self.assertEqual(s.future_why("WEAK", "supplier conc."), "a supplier above 10% of costs, or a sole-source "
                                                                 "supplier, without a moat strong enough to carry it")
        self.assertEqual(s.future_why("WEAK", "unit customer conc."),
                         "in one business unit: a customer above 10% of revenue (distributors and retailers "
                         "included), or concentration not ruled out in its filings, without a moat strong enough to "
                         "carry it")
        self.assertEqual(s.future_why("WEAK", "no moat"), "no lasting competitive advantage")
        self.assertEqual(s.future_why("WEAK", "funding conc."), "too much funding from one lender or one funding "
                                                                "channel")
        self.assertEqual((s.future_why("ADEQUATE", "n.m."), s.future_why("STRONG", "n.m.")), ("", ""))
        self.assertEqual(self.rows["BBB.DE"]["fw"], "")

    def test_groups_and_the_too_hard_pile(self):
        # R3-R5: groups judged as a whole; no holding company reads ROE. v4.6.0: conglomerates, trading houses
        # and holding companies are analysed at the parent, their allocation across the parts included (G4);
        # the R4 too-hard pile is retired (G2): a bank or insurer outside the bank lens is read on the
        # industrial lens.
        self.assertNotIn("some holding companies", self.page)
        self.assertIn("Groups, conglomerates, trading houses and holding companies included, are judged as a whole: "
                      "returns on the group accounts, competitive position as an income-weighted average of the "
                      "businesses, shareholder-friendliness including how the group allocates capital among them, "
                      "price on the whole group. Banks and insurers that do not fit the bank lens are read on the "
                      "industrial lens, with conservative rules for deposits, insurance funds and unlisted stakes.",
                      self.page)
        self.assertNotIn("neither lens can read, are not analysed further", self.page)
        self.assertEqual(s.PLAIN_FUTURE["dependency"], "depends on a listed subsidiary or holding that cannot be graded")
        self.assertNotIn("dependency", s.PLAIN_PAST)          # Past is never weighted (review fix B1)
        self.assertEqual(set(s.PLAIN_PREFIX), {"unit", "sub"})
        # v4.6.0 (G2, P30): the one Gate-0 ground left; the two-lens, no-listed-share and too-hard grounds retired.
        why = ("Stopped at the first question: the filings do not show what the business sells, and who pays for "
               "it, for most of its revenue.")
        self.assertEqual(s.DNAF_WHY, why)
        # Only a DNAF memo written under v4.6.0 or later stopped on that ground; an earlier one keeps its own.
        self.assertEqual(self.rows["HHH"]["vw"], s.DNAF_WHY_EARLIER)
        for version, want in (("v4.6.0", why), ("v4.10.2", why), ("v5.0.0", why), ("4.6.0", why), ("v4.6", why),
                              (" v4.6.1 ", why), ("v4.5.3", s.DNAF_WHY_EARLIER), ("4.5", s.DNAF_WHY_EARLIER),
                              ("v4.4.1", s.DNAF_WHY_EARLIER), ("-", s.DNAF_WHY_EARLIER), ("", s.DNAF_WHY_EARLIER)):
            self.assertEqual(s.verdict_why(row("NNN", "DNAF", model_version=version)), want, version)
        self.assertNotIn("filings do not show", s.DNAF_WHY_EARLIER)
        self.assertIn('<dt><span class="v v-DNAF">Not analysed</span></dt><dd>%s</dd>' % why, self.page)
        self.assertIn("<li><b>Do I understand it?</b> The business is described in one plain sentence, the best its "
                      "filings allow: what it sells, who pays for it, its industry, its legal and operating form, "
                      "where it works, and its status. A long sentence or a list of businesses still passes. Only "
                      "when the filings do not show what the business sells, and who pays for it, for most of its "
                      "revenue is it not analysed further.</li>", self.page)
        for retired in ("two lenses", "neither lens", "no listed share", "cannot be described simply",
                        "must fit one plain sentence", "not analysed further."):
            # The method text never states a retired ground; only an earlier DNAF row's own reason names one.
            page = self.page.replace("revenue is it not analysed further.", "").replace(
                json.dumps(s.DNAF_WHY_EARLIER, ensure_ascii=False)[1:-1], "")
            self.assertNotIn(retired, page, retired)
        # ROE and the capital test are for banks and insurers on the bank lens only; the rest read on STD.
        terms = s.terms({"units": [], "retest_count": 0, "held_marker": False})
        self.assertIn("ROE (return on equity) replaces ROCE for banks and insurers on the bank lens.", terms)
        self.assertIn("For banks and insurers on the bank lens it reads market value ÷ net income", terms)
        self.assertIn("(and EV/OI for banks and insurers on the bank lens)", terms)
        self.assertIn("Banks and insurers on the bank lens (a licensed bank or insurer that publishes a regulatory "
                      "capital ratio for the whole group, with no sizeable non-financial business) are graded on "
                      "return on equity and a regulatory capital test instead.", self.page)
        self.assertIn("<span>Banks and insurers on the bank lens: return on equity <code>≥ 15%</code> and a capital "
                      "test, for Strong or Adequate</span>", self.page)
        self.assertNotIn("replaces ROCE for banks and insurers.", terms)
        self.assertNotIn("<span>Banks and insurers: return on equity", self.page)
        # `dependency` reads whole with its prefix (MODEL section 7.1, v4.6.0): a listed part, or an undescribed unit.
        self.assertEqual(s.future_why("WEAK", "sub dependency"),
                         "depends on a listed subsidiary or holding that cannot be graded")
        self.assertEqual(s.future_why("WEAK", "unit dependency"),
                         "depends on a business unit that its filings do not describe, which cannot be graded")
        self.assertEqual(s.plain_reason(s.PLAIN_FUTURE, "unit breadth"),
                         "in one business unit: customer or supplier base too narrow")
        self.assertEqual(s.plain_reason(s.PLAIN_PAST, "unit dependency"), "in one business unit: dependency")

    def test_sf_vocabulary_matches_the_register_tool(self):
        import gsc_register
        self.assertEqual(set(s.PLAIN_SF), set(gsc_register.SF_REASONS))
        self.assertEqual(set(s.PLAIN_FUTURE), set(gsc_register.FUTURE_REASONS))
        self.assertEqual(self.rows["MMM"]["sw"], "One governance warning sign, with management owning little and "
                                                 "voting control kept apart from the economics")
        self.assertEqual(s.PLAIN_SF["inherited"], "inherits the failure of a listed subsidiary it controls")
        self.assertIn("so is a single warning sign where management owns little and voting control sits apart from "
                      "the economics. Otherwise a single warning sign is noted as a caution.", self.page)
        self.assertNotIn("pledg", self.page.lower())
        self.assertNotIn("pledg", render(self.fx, no_held=True).lower())


class RetiredTests(unittest.TestCase):
    """MODEL v4.6.0 section 7.1 (G5): a RETIRED row's listed line has ceased to trade; the page leaves it out."""

    def test_retired_rows_stay_off_the_page(self):
        gone = row("RRR", "RETIRED", verdict="RETIRED", company="Retired Holdings", past="ADEQUATE",
                   past_reason="14.7% ROCE", future="WEAK", future_reason="no moat", sf="FAIL", sf_reason="buybacks",
                   gates_failed="2", px_source="memo", next_review_short="retired 2026-08-04")
        fx = Fixture(rows=default_rows() + [gone], files={
            "memos/RRR/RRR_2026-09-01_GSC.md": memo("RRR", [("2. Understanding", "RRR sells retired widgets.")])})
        base = Fixture()
        try:
            page, plain = render(fx), render(base)
            ctx, sections, _extraction, rows = s.build(fx.path)
            code, out, err = run_main(["stats", "--repo", fx.path])
        finally:
            fx.close()
            base.close()
        self.assertEqual(page, plain)                       # byte for byte the page without the RETIRED row
        for text in ("RRR", "Retired Holdings", "retired widgets", "RETIRED", "retired 2026"):
            self.assertNotIn(text, page)
        self.assertEqual(ctx["names"], 8)
        self.assertEqual([sec["id"] for sec in sections], list(s.SECTION_ORDER))
        self.assertNotIn("RETIRED", s.SECTION_ORDER)
        self.assertNotIn("RRR", [r["key"] for r in rows])
        self.assertEqual(code, 0, err)
        self.assertIn("8 rows", out)

    def test_reinvestment_in_plain_words(self):
        self.assertEqual(s.plain_reason(s.PLAIN_SF, "reinvestment"),
                         "most of the group's new capital went into businesses earning below the method's 10% "
                         "return line")


TWO_BLOCKS = ("# TODO\n\n## ▶ Review requests\n\n- `DDD.L` — review\n\n"
              "## ▶ Method re-tests v4.6.0\n\n*Intro.*\n\n**Held — first.**\n\nNone.\n\n"
              "- `HHH` — DNAF on a retired ground → run the full analysis.\n"
              "- `AAA` — also in the v4.5.0 block.\n- `ZZZ` — not in the register.\n\n---\n\n"
              "## ▶ Method re-tests v4.5.0\n\n*Intro.*\n\n- `AAA` — worth test → AVOID (60%).\n"
              "  - `BBB.DE` — an indented line counts too.\n- `CCC` — R7.\n\n"
              "## ▶ Other block\n\n- `EEE.ST` — not a re-test.\n")


class RetestBlocksTests(unittest.TestCase):
    """MODEL v4.6.0 section 8.2 step 3: `▶ Method re-tests v4.6.0` sits above `▶ Method re-tests v4.5.0`, and both
    count: the union of their keys, each under the version of the first block that lists it."""

    def test_both_blocks_count(self):
        fx = Fixture(files={"queue/TODO.md": TWO_BLOCKS})
        try:
            versions, keys = s.retest_block(fx.path)
            ctx, sections, _extraction, _rows = s.build(fx.path)
            page = s.render_page(ctx, sections)
            code, out, err = run_main(["stats", "--repo", fx.path])
        finally:
            fx.close()
        self.assertEqual(versions, ["v4.6.0", "v4.5.0"])
        self.assertEqual(list(keys.items()), [("HHH", "v4.6.0"), ("AAA", "v4.6.0"), ("ZZZ", "v4.6.0"),
                                              ("BBB.DE", "v4.5.0"), ("CCC", "v4.5.0")])
        self.assertEqual((ctx["retest_count"], ctx["retest_watch"]), (4, 3))     # ZZZ is not in the register
        self.assertEqual(ctx["retest_versions"], [("v4.6.0", 2), ("v4.5.0", 2)])
        self.assertEqual(ctx["retest_version"], "v4.6.0 and v4.5.0")
        rows = {r["k"]: r for sec in page_data(page)["sections"] for r in sec["rows"]}
        self.assertEqual(sorted(k for k in rows if rows[k].get("r")), ["AAA", "BBB.DE", "CCC", "HHH"])
        plain = page.replace("<b>", "").replace("</b>", "")
        self.assertIn("4 companies, including 3 of the 3 on the shortlist, are being re-tested under updated "
                      "versions of the method (v4.6.0 and v4.5.0).", plain)
        self.assertIn('<div class="stat stat-note"><b>4</b><span>Being re-tested</span></div>', page)
        self.assertEqual(code, 0, err)
        self.assertIn("re-test 4 (v4.6.0 2, v4.5.0 2)", out)

    def test_a_block_without_register_keys_drops_out_of_the_label(self):
        todo = TWO_BLOCKS.replace("- `HHH` — DNAF on a retired ground → run the full analysis.\n", "").replace(
            "- `AAA` — also in the v4.5.0 block.\n", "")
        fx = Fixture(files={"queue/TODO.md": todo})
        try:
            ctx, sections, _extraction, _rows = s.build(fx.path)
            code, out, err = run_main(["stats", "--repo", fx.path])
        finally:
            fx.close()
        self.assertEqual(ctx["retest_versions"], [("v4.5.0", 3)])
        self.assertEqual(ctx["retest_version"], "v4.5.0")
        self.assertIn("are being re-tested under an updated version of the method (v4.5.0).",
                      s.retest_banner(ctx).replace("<b>", "").replace("</b>", ""))
        self.assertEqual(code, 0, err)
        self.assertIn("re-test 3 (v4.5.0)", out)
        self.assertEqual(s.retest_versions(["v4.6.0", "", "v4.6.0"], {}), [("v4.6.0", 0)])
        fx = Fixture(files={"queue/TODO.md": "# TODO\n\n## ▶ Other block\n\n- `AAA` — x\n"})
        try:
            self.assertEqual(s.retest_block(fx.path), ([], {}))
            code, out, err = run_main(["stats", "--repo", fx.path])
        finally:
            fx.close()
        self.assertIn("re-test 0 (no block)", out)

    def test_the_checkout_todo_counts_every_block(self):
        todo = os.path.join(REPO, "queue", "TODO.md")
        if not (os.path.isfile(todo) and os.path.isfile(os.path.join(REPO, "register.csv"))):
            self.skipTest("no queue/TODO.md or register.csv in this checkout")
        with open(todo, encoding="utf-8") as fh:
            text = fh.read()
        ctx, _sections, _extraction, rows = s.build(REPO)
        in_register = {r["key"] for r in rows}
        first = {}                                  # key -> the version of the first block listing it
        for title, block in re.findall(r"(?ms)^## ▶ Method re-tests([^\n]*)\n(.*?)(?=^## |\Z)", text):
            version = re.search(r"v\d+\.\d+\.\d+", title)
            for key in re.findall(r"(?m)^\s*-\s+`([A-Za-z0-9._-]+)`", block):
                if key in in_register:
                    first.setdefault(key, version.group(0) if version else "")
        self.assertEqual(ctx["retest_count"], len(first))
        self.assertEqual(dict(ctx["retest_versions"]),
                         {v: n for v, n in collections.Counter(first.values()).items() if v})


class CliTests(unittest.TestCase):

    def test_stats_reports_coverage_and_issues(self):
        fx = Fixture()
        try:
            code, out, err = run_main(["stats", "--repo", fx.path])
        finally:
            fx.close()
        self.assertEqual(code, 0, err)
        self.assertIn("business sentence    4/8", out)
        self.assertIn("BUY/WATCH rows without a numeric trigger (no distance shown) (1): CCC", out)
        self.assertIn("re-test 1 (v4.5.0)", out)

    def test_bad_register_exits_2(self):
        fx = Fixture(files={"register.csv": "key,company\nX,Y\n"})
        try:
            code, _out, err = run_main(["stats", "--repo", fx.path])
        finally:
            fx.close()
        self.assertEqual(code, 2)
        self.assertIn("lacks columns", err)

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


class RealRegisterTests(unittest.TestCase):
    """Smoke test on the repository's own register (skipped when it is absent)."""

    def test_real_register_renders_with_matching_sections(self):
        if not os.path.isfile(os.path.join(REPO, "register.csv")):
            self.skipTest("no register.csv")
        ctx, sections, _extraction, rows = s.build(REPO)
        page = s.render_page(ctx, sections)
        for sec in sections:
            self.assertEqual(len(sec["rows"]), sum(1 for r in rows if r["section"] == sec["id"]), sec["id"])
        self.assertEqual(sum(len(sec["rows"]) for sec in sections), len(rows))
        ctx_bare, sections_bare, _extraction, _rows = s.build(REPO, no_held=True)
        bare = s.render_page(ctx_bare, sections_bare)
        for r in rows:
            if r["held"] != "true":
                continue
            for text in (page, bare):
                # The ADD band often equals the operative trigger, which the page shows as the buy-zone price.
                for name in ("avg_cost", "add_band", "sell_line", "zone"):
                    value = r[name]
                    if value not in ("-", "n.m.", r["trigger"], r["px"]):
                        self.assertNotIn('"%s"' % s.group_digits(value), text, (r["key"], name))
                        self.assertNotIn('"%s"' % value, text, (r["key"], name))
                if r["avg_cost"] not in ("-", "n.m."):
                    self.assertNotIn(r["avg_cost"], text, r["key"])
                    # The bare number too, wherever it stands ('110.00' is not '10.00').
                    number = r["avg_cost"].split()[0]
                    self.assertIsNone(re.search(r"(?<![\d.,])%s(?![\d])" % re.escape(number), text),
                                      (r["key"], "avg_cost number"))
        self.assertNotIn("Held", bare)
        self.assertNotIn('"h":', bare)
        for sec in sections_bare:
            for r in sec["rows"]:
                if sec["id"] not in s.DATED_SECTIONS:
                    self.assertEqual(r["pd"], "", r["k"])
        self.assertLess(len(page.encode("utf-8")), 2 * 1024 * 1024)


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=1).result
    sys.exit(len(result.failures) + len(result.errors))
