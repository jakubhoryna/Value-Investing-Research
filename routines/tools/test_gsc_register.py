#!/usr/bin/env python3
"""Tests for routines/tools/gsc_register.py (unittest, fixtures inline).

Run:  python3 routines/tools/test_gsc_register.py
Exit code 0 = all pass. The check() cases build a throwaway git repo.

Covers: lean render (sections, order, legend, removed parts), cell rendering
and reasons, the AVOID gate split, the MODEL 7.1b formulas (TROW at its
memo price, minor units, ADR ratio, FX, n.m. and '-'), apply of SWEEP rows
(every skip rule, FX, held last zone check) and of ANALYSE/REVIEW rows (held
flag read-only), row-from-memo normalisation and BACKFILL notes, lint-memo,
the next_review_short parser, endpoint symbols, determinism, check() against
a real git tree, the 7.1a suffix table in model/MODEL.md, that the tool's
own source passes the routine guard hook's code scan, and the one-time
rebuild (legacy register -> register.csv: sections, the held record, the
register-held DNAF, SWEEP and memo prices with minor units, the operative
trigger parser, memo multiples, assisted core numbers validated against
the memo, reasons with quote and vocabulary checks, determinism, check()
on the output, and re-reading the report's own assisted appendix).
MODEL v4.5.0 lens set (J1-J13) as revised by round 2 (2026-10-07): the lens
columns holding_keys and core_credit with their legacy defaults, the
constant credit (V14) and the leg round trip to 8.0 and 7.0, group reason
prefixes (unit, sub) and the new tokens (alignment; pledging retired), one
lint-memo failure per lens rule (lens STD/FI, FI n.m. fields, credits, the
B4 Division table and Holding credits tokens, retired fields, the J1
OI-basis grammar), the SWEEP's last zone check on a changed held zone, and
check()'s parent-stale LIST finding. Round 2 R10/R1/R6/R7: the lean-2
header and both older headers read with their defaults, the 3- and 5-year
averaged multiples (formula, render, SWEEP, check, metrics), status_hint's
strict line on every key, trigger_basis and the held trigger = ADD band,
the Future concentration caveat, the lint of the ten new fields (the
trigger as the no-cash bound, the P28 down-year basis, the P20 FCF basis
and the all-capex order), the no-cash band parser and the one-time
retrigger. v4.5.2: lint-row (the row file against its name, its title and
the exact row-from-memo --table print, read as gsc-automerge reads it).
v4.5.3: check() does not recompute a Gate-0 DNAF row's n.m. multiples
(MODEL 6.4) while validate_row still governs its fields. v4.6.0: the SF
token `reinvestment` (G4) after `distributions`; the RETIRED register state
(G5): retire and retire --undo (the row restored exactly as apply writes
it), every refusal (held, already retired, a bad date or source, the entry
cap), apply refused for a RETIRED key and a memo never carrying RETIRED,
the validate_row rules, the section last and its counts only while a
RETIRED row exists (a register without one renders byte for byte as
before, the repository's own register included), check() not recomputing
its multiples, SWEEP and sweep-scope leaving it out, and position,
retrigger and the one-time rebuild never re-writing it; retire refusing a
last trading day after today (the system date, injected in tests);
retire --undo rebuilding from the one file in memos/{KEY}/ (a memo landed
or moved after retirement), refusing a folder that does not hold exactly
one memo; a parent whose holding_keys names a RETIRED key listed once
('holding HKEY retired — re-test the parent'), a RETIRED parent never; and
the Future tokens `unit dependency` (an undescribed material unit, new) and
`sub dependency` (MODEL v4.6.0 section 7.1). v4.8.0 (IDEAS C9): lint-memo's
roce_worst and fcfroce_worst - required from v4.8.0 only, their form, roce_worst
equal to the past_reason level at its precision, the P2/P3 floors of a STRONG or
ADEQUATE Past, n.m. under FI and in a Gate-0 memo, no register column - and
MODEL section 6.1 listing both before past_reason once MODEL.md is at v4.8.0.
"""
import contextlib
import datetime
import io
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import time
import unittest

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import gsc_register as r  # noqa: E402

TOOL = os.path.join(HERE, "gsc_register.py")


# ------------------------------------------------------------------ fixtures

TROW_FM = {
    "ticker": "TROW", "company": "T. Rowe Price Group, Inc.", "exchange": "NASDAQ",
    "isin": "US74144T1088", "currency": "USD", "memo_date": "2026-10-03", "memo_version": "v5",
    "model_version": "v4.5.0", "price_at_memo": "$104.62", "mcap_at_memo": "$22.3B",
    "verdict": "WATCH", "quality_past": "ADEQUATE", "quality_future": "ADEQUATE", "sf": "PASS",
    "cheapness": "FAIR", "window": '"FY2016–FY2025 (10y)"',
    "trigger_band": '"CHEAP < ≈ $55.5 (MCap/FCF binds both EV variants; no P12)"',
    "next_review": '"Q3 2026 results 30 Oct 2026; FY2026 10-K (~Feb 2027)"',
    "position": "HELD", "avg_cost": "$10.00", "zone": "HOLD", "add_band": "55.5",
    "sell_flag_line": "268.6",
    "aliases": "n.m.", "px": "104.62", "px_unit": "USD", "px_date": "2026-10-02", "trigger": "55.5",
    "mcap_fcf": "15.1", "ev_oi": "10.9", "ev_oi_all_cash": "9.0",
    "trigger_basis": "no-cash", "mcap_fcf_3y": "15.9", "mcap_fcf_5y": "17.2", "ev_oi_3y": "11.7", "ev_oi_5y": "12.6",
    "lens": "STD", "holding_keys": "n.m.", "core_credit": "0",
    "core_period": '"FY2025; BS 2026-06-30"', "core_currency": "USD", "core_unit": "m",
    "core_shares_diluted": "213.316", "core_debt_eq": "1620.9", "core_cash": "4188.3",
    "core_oi": "2188.8", "core_oi_basis": "FY2025 J1", "core_fcf": "1479.2",
    "core_fcf_basis": "FY2025 CFO − maint. capex (= all capex)",
    "core_oi_3y": "2050.4", "core_oi_5y": "1900", "core_fcf_3y": "1400", "core_fcf_5y": "1300",
    "core_fcf_all": "1479.2", "core_fx": "1", "core_fx_date": "2026-10-02",
    "core_ratio": "1", "past_reason": "23.9% ROCE", "future_reason": "n.m.", "sf_reason": "buybacks",
    "next_review_short": "2026-10-30",
}


def memo_text(fm, drop=(), **over):
    fields = dict(fm)
    fields.update(over)
    lines = ["---"] + ["%s: %s" % (k, v) for k, v in fields.items() if k not in drop] + ["---", "",
                                                                                      "# Memo body", ""]
    return "\n".join(lines)


def csv_row(key, verdict="WATCH", past="STRONG", future="ADEQUATE", sf="PASS", ev_oi="10.0", **over):
    gates = r.gates_failed(past, future, sf)
    row = {name: r.NM for name in r.CSV_HEADER}
    row.update({
        "key": key, "company": "%s Inc." % key, "isin": r.OWED, "aliases": r.NM,
        "section": r.section_for(verdict, gates) or r.OWED, "verdict": verdict, "gates_failed": str(gates),
        "past": past, "past_reason": r.OWED, "future": future, "future_reason": r.OWED,
        "sf": sf, "sf_reason": r.OWED, "memo_path": "memos/%s/%s_2026-09-01_GSC.md" % (key, key),
        "memo_date": "2026-09-01", "memo_version": "v1", "model_version": "v4.5.0",
        "px": "100", "px_unit": "USD", "px_date": "2026-08-31", "px_source": "memo", "trigger": "80",
        "mcap_fcf": "12.0", "ev_oi": ev_oi, "ev_oi_all_cash": ev_oi, "next_review_short": "Feb 2027",
        "held": "false", "core_source": r.OWED,
    })
    for name in r.CORE_FIELDS:
        row[name] = r.OWED
    row.update(r.LENS_DEFAULTS)
    row.update(r.R10_DEFAULTS)
    row["trigger_basis"] = "no-cash"            # a v4.5.0 row prints the no-cash bound (R10)
    row.update(over)
    return row


def held_core(row):
    """TROW-like core numbers on a csv row."""
    row.update({"core_period": "FY2025", "core_currency": "USD", "core_unit": "m",
                "core_shares_diluted": "213.316", "core_debt_eq": "1620.9", "core_cash": "4188.3",
                "core_oi": "2188.8", "core_oi_basis": "FY2025 reported", "core_fcf": "1479.2",
                "core_fcf_basis": "FY2025 CFO - capex", "core_fx": "1", "core_fx_date": "2026-10-02",
                "core_ratio": "1", "core_source": "memo"})
    return row


def remove_tree(path):
    """Remove a throwaway root. On Windows a git child or a virus scanner can hold a file
    for a moment after a test ends (the one unreproduced error of the round-2 review, N8),
    so retry briefly and never fail a test over its own temp-directory cleanup."""
    def writable(func, p, _exc):
        os.chmod(p, stat.S_IWRITE)
        func(p)
    for _attempt in range(5):
        try:
            shutil.rmtree(path, onerror=writable)
            return
        except OSError:
            time.sleep(0.2)
    shutil.rmtree(path, ignore_errors=True)


class TempRoot:
    """A throwaway repository root (optionally a git repo)."""

    def __init__(self, files, git=False):
        self.path = tempfile.mkdtemp(prefix="gsc_register_test_")
        for rel, text in files.items():
            full = os.path.join(self.path, rel)
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(text)
        if git:
            self.git("init", "-q")
            self.git("config", "user.email", "t@example.invalid")
            self.git("config", "user.name", "t")
            self.git("config", "core.autocrlf", "false")
            self.git("add", "-A")
            self.git("commit", "-q", "-m", "base")

    def git(self, *args):
        return subprocess.run(["git", "-C", self.path] + list(args), check=True, capture_output=True)

    def read(self, rel):
        with open(os.path.join(self.path, rel), encoding="utf-8", newline="") as fh:
            return fh.read()

    def write(self, rel, text):
        full = os.path.join(self.path, rel)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8", newline="") as fh:
            fh.write(text)

    def close(self):
        remove_tree(self.path)


def run_main(argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = r.main(argv)
    return code, out.getvalue(), err.getvalue()


# ------------------------------------------------------------------ tests

class RenderTests(unittest.TestCase):
    def rows(self):
        return [
            csv_row("ZZZ", ev_oi="9.5"), csv_row("AAA", ev_oi="9.5"), csv_row("MMM", ev_oi=r.NM),
            csv_row("NNN", ev_oi=r.OWED), csv_row("BBB", ev_oi="12.0"),
            csv_row("AV1", verdict="AVOID", past="WEAK", past_reason="ROCE decline", ev_oi="5.0"),
            csv_row("AV2", verdict="AVOID", past="WEAK", future="WEAK", ev_oi="3.0"),
            csv_row("DNB", verdict="DNAF", past=r.NM, future=r.NM, sf=r.NM, ev_oi=r.NM),
            csv_row("DNA", verdict="DNAF", past=r.NM, future=r.NM, sf=r.NM, ev_oi=r.NM),
            held_core(csv_row("HLD", held="true", zone="HOLD", add_band="55.5", trigger="55.5", sell_line="268.6",
                              last_zone_check="2026-10-02", avg_cost="10.00 USD", ev_oi="10.9")),
        ]

    def test_sections_order_and_headings(self):
        text = r.render(self.rows(), "v308", "2026-10-07")
        heads = [l for l in text.split("\n") if l.startswith("## ")]
        self.assertEqual(heads, ["## PORTFOLIO (1)", "## BUY (0)", "## WATCH (6)",
                                 "## AVOID - one gate failed (1)", "## AVOID - two or more gates failed (1)",
                                 "## DNAF (2)"])
        watch = text.split("## WATCH (6)")[1].split("## AVOID")[0]
        order = [l.split("|")[1].strip() for l in watch.split("\n") if l.startswith("| ") and "Ticker" not in l]
        self.assertEqual(order, ["AAA", "ZZZ", "HLD", "BBB", "MMM", "NNN"])
        dnaf = text.split("## DNAF (2)")[1]
        self.assertLess(dnaf.index("| DNA |"), dnaf.index("| DNB |"))
        self.assertIn("## BUY (0)\n\nNone.", text)

    def test_front_matter_and_removed_parts(self):
        text = r.render(self.rows(), "v308", "2026-10-07")
        self.assertIn("names_total: 10\n", text)
        self.assertIn('verdict_split: "BUY 0 · WATCH 6 · AVOID 2 (one gate 1 · two+ 1) · DNAF 2"', text)
        self.assertIn("portfolio_names: 1\n", text)
        self.assertNotIn("Dist", text)
        self.assertNotIn("## Change log", text)
        self.assertNotIn("## Open items", text)
        body = text.split("---\n", 2)[2]
        legend = [l for l in body.split("\n\n")[1].split("\n") if l]
        self.assertTrue(legend[0].startswith("Grades carry"), legend)
        self.assertEqual(len(legend), 2)
        self.assertTrue(text.endswith("\n") and "\r" not in text and not text.startswith("﻿"))

    def test_portfolio_row(self):
        text = r.render(self.rows(), "v308", "2026-10-07")
        self.assertIn("| HLD | HOLD | 100 | 55.5 | 268.6 | 2026-10-02 | Feb 2027 |", text)

    def test_breaches(self):
        rows = self.rows() + [csv_row("AAA")]
        with self.assertRaises(r.ToolError):
            r.render(rows, "v308", "2026-10-07")
        bad = csv_row("AVX", verdict="AVOID")
        bad["section"] = "AVOID-1"
        with self.assertRaises(r.ToolError):
            r.render([bad], "v308", "2026-10-07")
        long_name = csv_row("LNG", company="X" * 161)
        with self.assertRaises(r.ToolError):
            r.render([long_name], "v308", "2026-10-07")
        with self.assertRaises(r.ToolError):
            r.render(self.rows(), "308", "2026-10-07")

    def test_determinism(self):
        rows = self.rows()
        self.assertEqual(r.render(rows, "v1", "2026-10-10"), r.render(list(reversed(rows)), "v1", "2026-10-10"))
        self.assertEqual(r.csv_text(rows), r.csv_text(list(reversed(rows))))
        self.assertNotIn("\r", r.csv_text(rows))

    def test_render_lean2_fifteen_columns_and_legend(self):
        rows = self.rows()
        rows[0].update({"mcap_fcf_3y": "9.4", "mcap_fcf_5y": "10.1", "ev_oi_3y": "8.8", "ev_oi_5y": r.NM})
        text = r.render(rows, "v310", "2026-10-07")
        self.assertIn('register_format: "lean-2 (MODEL v4.5.0)"', text)
        header = "| Ticker | Company | Memo date | Ver | Verdict | Past | Future | SF | Px | Trigger | MCap/FCF | " \
                 "EV/OI | MCap/FCF 3y · 5y | EV/OI 3y · 5y | Next review |"
        self.assertIn(header + "\n|" + "---|" * 15 + "\n", text)
        self.assertIn("| 12.0 | 9.5 | 9.4 · 10.1 | 8.8 · n.m. | Feb 2027 |", text)    # ZZZ
        self.assertIn("| 12.0 | 9.5 | - | - | Feb 2027 |", text)                       # AAA: averages owed
        legend = [line for line in text.split("\n") if line.startswith("Grades carry")][0]
        self.assertIn("3y · 5y: the same multiples on 3- and 5-year average OI and FCF", legend)
        self.assertIn("Trigger: the no-cash bound, the strict all-pass line", legend)


class CellTests(unittest.TestCase):
    def test_grade_cells(self):
        self.assertEqual(r.grade_cell("PASS", r.NM, sf=True), "PASS")
        self.assertEqual(r.grade_cell("PASS", "buybacks", sf=True), "PASS CAUTION · buybacks")
        self.assertEqual(r.grade_cell("FAIL", "compensation", sf=True), "FAIL · compensation")
        self.assertEqual(r.grade_cell("WEAK", r.OWED), "WEAK")
        self.assertEqual(r.grade_cell("STRONG", "28% ROCE"), "STRONG · 28% ROCE")

    def test_gate_split(self):
        self.assertEqual(r.section_for("AVOID", 1), "AVOID-1")
        self.assertEqual(r.section_for("AVOID", 2), "AVOID-2")
        self.assertEqual(r.section_for("AVOID", 3), "AVOID-2")
        self.assertEqual(r.section_for("AVOID", 0), "")
        row = csv_row("X", verdict="AVOID")
        self.assertTrue(any("no failed gate" in p for p in r.validate_row(row)))
        row = csv_row("Y", verdict="WATCH", past="WEAK")
        self.assertTrue(any("verdict mapping" in p for p in r.validate_row(row)))

    def test_reason_vocabulary(self):
        self.assertEqual(r.validate_row(csv_row("A", past_reason="28% ROCE")), [])
        self.assertTrue(r.validate_row(csv_row("A", past_reason="great returns")))
        self.assertTrue(r.validate_row(csv_row("A", sf_reason="bad CEO")))
        # R8: pledges are no flag (P23 is the alignment call); `alignment` is a single flag that fails.
        for value in ("alignment", "sub alignment"):
            self.assertEqual(r.validate_row(csv_row("A", verdict="AVOID", sf="FAIL", sf_reason=value)), [], value)
        self.assertNotIn("pledging", r.SF_REASONS)
        self.assertTrue(r.validate_row(csv_row("A", verdict="AVOID", sf="FAIL", sf_reason="pledging")))
        notes = []
        row = r.row_from_memo("memos/TROW/TROW_2026-10-03_GSC.md",
                              memo_text(TROW_FM, sf="FAIL", verdict="AVOID", sf_reason="pledging"), notes)
        self.assertTrue(any("sf_reason" in p for p in r.validate_row(row)))

    def test_v450_tokens_and_group_prefixes(self):
        # Review fix B1 (2026-10-07): Past is never a weighted grade, so a Past reason takes no group
        # prefix and `dependency` (an ungradeable subsidiary or holding) is a Future token.
        ok = [("past_reason", "capital"), ("future_reason", "sub dependency"), ("future_reason", "dependency"),
              ("future_reason", "funding conc."), ("future_reason", "unit forces: customers"),
              ("future_reason", "sub funding conc."), ("sf_reason", "inherited"), ("sf_reason", "sub flag pair")]
        for name, value in ok:
            self.assertEqual(r.validate_row(csv_row("A", past="WEAK", verdict="AVOID", **{name: value})
                                            if name == "past_reason" else
                                            csv_row("A", future="WEAK", verdict="AVOID", **{name: value})
                                            if name == "future_reason" else
                                            csv_row("A", **{name: value})), [], (name, value))
        # Round 2 retired the finance part (R2: captives are consolidated): 'fin.' is no prefix.
        bad = [("past_reason", "unit sub 8% ROCE"), ("past_reason", "group 8% ROCE"), ("past_reason", "fin. capital"),
               ("past_reason", "fin. 9.5% ROE"), ("past_reason", "sub dependency"), ("past_reason", "dependency"),
               ("past_reason", "unit 8% ROCE"), ("past_reason", "sub 9.5% ROE"), ("past_reason", "unit ROCE decline"),
               ("future_reason", "fin. funding conc."),
               ("future_reason", "unit forces: customers today"), ("sf_reason", "sub inherited flag pair"),
               ("sf_reason", "fin.inherited")]
        for name, value in bad:
            self.assertTrue(r.validate_row(csv_row("A", **{name: value})), (name, value))

    def test_future_concentration_caveat_vocabulary(self):
        # R7: an ADEQUATE carried with a concentration flag prints it; STRONG prints the grade alone.
        for value in (r.NM, r.OWED, "customer conc.", "supplier conc.", "unit customer conc."):
            self.assertEqual(r.validate_row(csv_row("A", future="ADEQUATE", future_reason=value)), [], value)
        for value in ("breadth", "no moat", "funding conc."):
            problems = r.validate_row(csv_row("A", future="ADEQUATE", future_reason=value))
            self.assertTrue(any("concentration caveat" in p for p in problems), (value, problems))
        problems = r.validate_row(csv_row("A", future="STRONG", future_reason="customer conc."))
        self.assertTrue(any("STRONG prints the grade alone" in p for p in problems), problems)
        self.assertEqual(r.validate_row(csv_row("A", future="STRONG", future_reason=r.NM)), [])
        fails, _ = r.lint_memo(LintTests.PATH, memo_text(TROW_FM, future_reason="customer conc."))
        self.assertEqual(fails, [])
        for value in ("breadth", "funding conc."):
            fails, _ = r.lint_memo(LintTests.PATH, memo_text(TROW_FM, future_reason=value))
            self.assertTrue(any("concentration caveat" in f for f in fails), (value, fails))
        fails, _ = r.lint_memo(LintTests.PATH, memo_text(TROW_FM, quality_future="STRONG",
                                                         future_reason="supplier conc."))
        self.assertTrue(any("STRONG prints the grade alone" in f for f in fails), fails)

    def test_validate_trigger_basis_and_held_trigger_equals_add_band(self):
        self.assertEqual(r.validate_row(csv_row("A")), [])                                       # v4.5.0, no-cash
        self.assertTrue(any(p.startswith("trigger_basis: 'cash' is not one of no-cash/all-cash")
                            for p in r.validate_row(csv_row("A", trigger_basis="cash"))))
        self.assertTrue(any(p.startswith("trigger_basis: all-cash, but a memo written under MODEL v4.5.0")
                            for p in r.validate_row(csv_row("A", trigger_basis="all-cash"))))
        self.assertEqual(r.validate_row(csv_row("A", trigger_basis="all-cash", model_version="v4.4.1")), [])
        self.assertEqual(r.validate_row(csv_row("D", verdict="DNAF", past=r.NM, future=r.NM, sf=r.NM,
                                                trigger_basis=r.NM)), [])
        self.assertTrue(r.validate_row(csv_row("A", trigger_basis=r.NM)))                       # n.m. only for DNAF
        held = dict(zone="HOLD", sell_line="200", last_zone_check="2026-10-02", avg_cost="10 USD", held="true")
        self.assertEqual(r.validate_row(csv_row("H", trigger="80", add_band="80.0", **held)), [])
        problems = r.validate_row(csv_row("H", trigger="80", add_band="75", **held))
        self.assertTrue(any(p.startswith("add_band: 75, but a held trigger at the no-cash bound is the ADD band")
                            for p in problems), problems)
        # A pre-R10 all-cash row may still differ from its ADD band (the no-cash bound) until retrigger.
        self.assertEqual(r.validate_row(csv_row("H", trigger="80", add_band="75", trigger_basis="all-cash",
                                                model_version="v4.4.1", **held)), [])
        self.assertEqual(r.validate_row(csv_row("H", trigger="80", add_band=r.NM, **held)), [])
        for name, value in (("mcap_fcf_3y", "9.45"), ("ev_oi_5y", "x"), ("core_oi_3y", "1e3"), ("core_fcf_all", "abc")):
            self.assertTrue(any(p.startswith(name) for p in r.validate_row(csv_row("A", **{name: value}))), name)
        self.assertEqual(r.validate_row(csv_row("A", mcap_fcf_3y=r.NM, ev_oi_5y="12.0", core_oi_3y="-4.5",
                                                core_fcf_all=r.NM)), [])

    def test_pair_cell_and_master_columns(self):
        self.assertEqual(r.pair_cell("9.4", "10.1"), "9.4 · 10.1")
        self.assertEqual(r.pair_cell(r.OWED, r.OWED), r.OWED)
        self.assertEqual(r.pair_cell(r.NM, "12.0"), "n.m. · 12.0")
        self.assertEqual(r.pair_cell("8.0", r.OWED), "8.0 · -")
        self.assertEqual(len(r.MASTER_COLUMNS), 15)
        self.assertEqual(r.MASTER_COLUMNS[10:14], ["MCap/FCF", "EV/OI", "MCap/FCF 3y · 5y", "EV/OI 3y · 5y"])
        cells = r.master_cells(csv_row("A", mcap_fcf_3y="9.4", mcap_fcf_5y="10.1", ev_oi_3y=r.NM, ev_oi_5y="12.0"))
        self.assertEqual(cells[12:14], ["9.4 · 10.1", "n.m. · 12.0"])
        self.assertEqual(r.master_cells(csv_row("B"))[12:14], [r.OWED, r.OWED])


class FormulaTests(unittest.TestCase):
    def test_trow_at_memo_price(self):
        row = held_core(csv_row("TROW"))
        self.assertEqual(r.compute_metrics(row, "104.62", "USD"),
                         {"mcap_fcf": "15.1", "ev_oi": "10.9", "ev_oi_all_cash": "9.0"})

    def base(self, **over):
        core = {"core_unit": "m", "core_shares_diluted": "100", "core_debt_eq": "0", "core_cash": "0",
                "core_oi": "100", "core_fcf": "100", "core_fx": "1", "core_ratio": "1"}
        core.update(over)
        return core

    def test_minor_units(self):
        # FCF per share = 1 major unit = 100 minor; price 1000 minor -> 10.0x.
        for unit in ("GBp", "ZAc", "ILA"):
            self.assertEqual(r.compute_metrics(self.base(), "1000", unit)["mcap_fcf"], "10.0", unit)
        self.assertEqual(r.compute_metrics(self.base(), "10000", "KWF")["mcap_fcf"], "10.0")
        self.assertEqual(r.compute_metrics(self.base(), "10", "USD")["mcap_fcf"], "10.0")

    def test_adr_ratio_fx_and_scale(self):
        self.assertEqual(r.compute_metrics(self.base(core_ratio="2"), "10", "USD")["mcap_fcf"], "5.0")
        self.assertEqual(r.compute_metrics(self.base(core_fx="1.25"), "10", "USD")["mcap_fcf"], "8.0")
        self.assertEqual(r.compute_metrics(self.base(), "10", "USD", fx="2")["mcap_fcf"], "5.0")
        self.assertEqual(r.compute_metrics(self.base(core_unit="bn", core_shares_diluted="1000"), "10", "USD")
                         ["mcap_fcf"], "0.1")
        self.assertEqual(r.compute_metrics(self.base(core_debt_eq="500", core_cash="200"), "10", "USD"),
                         {"mcap_fcf": "10.0", "ev_oi": "15.0", "ev_oi_all_cash": "13.0"})

    def test_nm_and_owed(self):
        self.assertEqual(r.compute_metrics(self.base(core_fcf="-5"), "10", "USD")["mcap_fcf"], r.NM)
        self.assertEqual(r.compute_metrics(self.base(core_oi="0"), "10", "USD")["ev_oi"], r.NM)
        self.assertEqual(r.compute_metrics(self.base(core_oi=r.NM), "10", "USD")["ev_oi_all_cash"], r.NM)
        self.assertEqual(r.compute_metrics(self.base(core_cash=r.OWED), "10", "USD")["ev_oi_all_cash"], r.OWED)
        self.assertEqual(r.compute_metrics(self.base(core_fx=r.OWED), "10", "USD"),
                         {"mcap_fcf": r.OWED, "ev_oi": r.OWED, "ev_oi_all_cash": r.OWED})
        self.assertEqual(r.compute_metrics(self.base(), r.OWED, "USD")["ev_oi"], r.OWED)

    def test_rounding_half_up(self):
        self.assertEqual(r.fmt1(r.Decimal("10.25")), "10.3")
        self.assertEqual(r.fmt1(r.Decimal("-0.04")), "0.0")

    def test_zero_credits_reproduce_the_plain_formulas(self):
        plain = held_core(csv_row("TROW"))
        for name in r.LENS_DEFAULTS:
            plain.pop(name)
        with_defaults = dict(plain, **r.LENS_DEFAULTS)
        self.assertEqual(r.compute_metrics(plain, "104.62", "USD"),
                         {"mcap_fcf": "15.1", "ev_oi": "10.9", "ev_oi_all_cash": "9.0"})
        self.assertEqual(r.compute_metrics(with_defaults, "104.62", "USD"), r.compute_metrics(plain, "104.62", "USD"))

    def credit(self, **over):
        # ps: FCF 1, OI 1, debt 2, cash 0.5 and a holding credit of 8 (V14: the holdings' own buy-line value).
        core = self.base(core_debt_eq="200", core_cash="50", core_credit="800")
        core.update(over)
        return core

    def test_constant_credit(self):
        # Round 2 (V14): the credit is a constant; no market price - the parent's or a holding's - moves it.
        self.assertEqual(r.compute_metrics(self.credit(), "20", "USD"),
                         {"mcap_fcf": "12.0", "ev_oi": "14.0", "ev_oi_all_cash": "13.5"})
        self.assertEqual(r.compute_metrics(self.credit(), "10", "USD"),
                         {"mcap_fcf": "2.0", "ev_oi": "4.0", "ev_oi_all_cash": "3.5"})
        self.assertEqual(r.compute_metrics(self.credit(), "40", "USD")["mcap_fcf"], "32.0")
        self.assertEqual(r.credit_value({"core_credit": "800"}), r.Decimal("800"))
        self.assertEqual(r.credit_value({}), 0)
        self.assertIsNone(r.credit_value({"core_credit": r.OWED}))
        self.assertFalse(hasattr(r, "holding_check") or hasattr(r, "credit_at") or hasattr(r, "credit_share"))

    def test_credit_above_mcap_and_nm(self):
        core = self.credit(core_credit="5000")
        self.assertEqual(r.compute_metrics(core, "10", "USD")["mcap_fcf"], "0.0")
        self.assertEqual(r.compute_metrics(self.credit(core_oi="-1"), "10", "USD")["ev_oi"], r.NM)
        self.assertEqual(r.compute_metrics(self.credit(core_fcf="0"), "10", "USD")["mcap_fcf"], r.NM)
        self.assertEqual(r.compute_metrics(self.credit(core_credit=r.OWED), "10", "USD"),
                         {"mcap_fcf": r.OWED, "ev_oi": r.OWED, "ev_oi_all_cash": r.OWED})
        # FI: core_oi n.m. (MCap/FCF reads MCap/NI).
        fi = self.base(core_oi=r.NM, core_debt_eq=r.NM, core_cash=r.NM)
        self.assertEqual(r.compute_metrics(fi, "10", "USD"), {"mcap_fcf": "10.0", "ev_oi": r.NM,
                                                               "ev_oi_all_cash": r.NM})

    def test_legs_round_trip_to_8_and_7(self):
        # MODEL section 2 Gate 2 with holding credits: P_FCF = (8 FCF + C) / N, P_nc = (7 OI - D + C) / N,
        # P_ac = P_nc + K / N; at each the matching multiple is exactly its threshold.
        core = self.credit()
        at = lambda x: r.compute_metrics(core, "%.6f" % x, "USD")
        self.assertEqual(at(8 * 1 + 8)["mcap_fcf"], "8.0")
        self.assertEqual(at(7 * 1 - 2 + 8)["ev_oi"], "7.0")
        self.assertEqual(at(7 * 1 - 2 + 8 + 0.5)["ev_oi_all_cash"], "7.0")

    def test_avg_metrics_formula(self):
        core = self.base(core_debt_eq="200", core_cash="50", core_oi_3y="80", core_oi_5y="50", core_fcf_3y="125",
                         core_fcf_5y="100")
        # ps: OI 3y 0.8, 5y 0.5; FCF 3y 1.25, 5y 1; debt 2 (EV/OI no-cash only).
        self.assertEqual(r.compute_avg_metrics(core, "10", "USD"),
                         {"mcap_fcf_3y": "8.0", "mcap_fcf_5y": "10.0", "ev_oi_3y": "15.0", "ev_oi_5y": "24.0"})
        # The same constant credit as the primaries: 8 per share.
        credited = dict(core, core_credit="800")
        self.assertEqual(r.compute_avg_metrics(credited, "10", "USD"),
                         {"mcap_fcf_3y": "1.6", "mcap_fcf_5y": "2.0", "ev_oi_3y": "5.0", "ev_oi_5y": "8.0"})
        # FI: OI averages n.m. (EV/OI n.m.), FCF averages are the NI basis (MCap/NI).
        fi = self.base(core_oi=r.NM, core_debt_eq=r.NM, core_cash=r.NM, core_oi_3y=r.NM, core_oi_5y=r.NM,
                       core_fcf_3y="125", core_fcf_5y="100")
        self.assertEqual(r.compute_avg_metrics(fi, "10", "USD"),
                         {"mcap_fcf_3y": "8.0", "mcap_fcf_5y": "10.0", "ev_oi_3y": r.NM, "ev_oi_5y": r.NM})
        # Owed averages stay owed; a record shorter than five years writes the 5y side n.m.
        self.assertEqual(r.compute_avg_metrics(self.base(), "10", "USD"),
                         {"mcap_fcf_3y": r.OWED, "mcap_fcf_5y": r.OWED, "ev_oi_3y": r.OWED, "ev_oi_5y": r.OWED})
        short = dict(core, core_oi_5y=r.NM, core_fcf_5y=r.NM)
        self.assertEqual(r.compute_avg_metrics(short, "10", "USD"),
                         {"mcap_fcf_3y": "8.0", "mcap_fcf_5y": r.NM, "ev_oi_3y": "15.0", "ev_oi_5y": r.NM})
        # A negative average is n.m. like a negative latest year.
        self.assertEqual(r.compute_avg_metrics(dict(core, core_fcf_3y="-5"), "10", "USD")["mcap_fcf_3y"], r.NM)

    def test_status_hint_credited_key_ignores_any_holding_price(self):
        # Round 2 (V14): the holding price check retired; a credited key at or under its trigger is
        # IN RANGE when its primaries pass there, whatever any holding's own price or memo.
        parent = dict(self.credit(), key="PAR", px_unit="USD", trigger="12", holding_keys="HLD1",
                      core_oi="200", core_debt_eq="0")
        holding = csv_row("HLD1", px="190", trigger="100", model_version="v4.4.1")
        self.assertEqual(r.compute_metrics(parent, "12", "USD")["ev_oi"], "2.0")
        for rows in ({"PAR": parent, "HLD1": holding}, {"PAR": parent}, None):
            self.assertEqual(r.status_hint(parent, "12", rows_by_key=rows, holding_px={"HLD1": "500"},
                                           as_of="2027-12-02")[0], "IN RANGE")

    def test_status_hint(self):
        row = held_core(csv_row("TROW", trigger="55.5"))
        self.assertEqual(r.status_hint(row, "55.5")[0], "IN RANGE")
        self.assertEqual(r.status_hint(row, "60")[0], "NEAR")
        self.assertEqual(r.status_hint(row, "70")[0], "FAR")
        self.assertEqual(r.status_hint(dict(row, trigger=r.NM), "60"), (r.NM, None))
        # A credit key at its trigger but failing a primary there is NEAR at most (MODEL 8.3 step 3).
        credit = dict(self.credit(), px_unit="USD", trigger="17")
        self.assertEqual(r.compute_metrics(credit, "17", "USD")["mcap_fcf"], "9.0")
        self.assertEqual(r.status_hint(credit, "17")[0], "NEAR")
        self.assertEqual(r.status_hint(credit, "12")[0], "IN RANGE")
        self.assertEqual(r.status_hint(dict(credit, trigger="9"), "11")[0], "FAR")

    def test_status_hint_strict_line_every_key(self):
        # R10: every key whose core numbers establish the primaries is IN RANGE only if MCap/FCF <= 8 and
        # EV/OI no-cash <= 7 at Px - a legacy all-cash trigger under its trigger with EV/OI no-cash 7.3 is NEAR.
        legacy = dict(self.base(core_debt_eq="30", core_cash="500"), key="OLD", px_unit="USD", trigger="7.5",
                      trigger_basis="all-cash")
        self.assertEqual(r.compute_metrics(legacy, "7", "USD"),
                         {"mcap_fcf": "7.0", "ev_oi": "7.3", "ev_oi_all_cash": "2.3"})
        self.assertEqual(r.status_hint(legacy, "7"), ("NEAR", r.Decimal("7") / r.Decimal("7.5") - 1))
        self.assertEqual(r.status_hint(legacy, "6.5")[0], "IN RANGE")
        self.assertEqual(r.strict_failures(legacy, "7"), ["EV/OI no-cash 7.3"])
        # A negative FCF on a P20 maintenance-capex basis has no FCF leg: never in range.
        self.assertEqual(r.status_hint(dict(legacy, core_fcf="-5", core_fcf_basis="FY2025 CFO − maint. capex (constructed)"), "6")[0], "NEAR")
        # A pre-R6 FCF (all capex, or a basis the register does not record) may overstate MCap/FCF:
        # its breach is not established, so EV/OI no-cash decides (review fix, 2026-10-07; R6).
        for basis in ("FY2025 CFO - capex", "FY2025 CFO − all capex (strict)", r.OWED, None):
            row = dict(legacy, core_fcf="-5", core_fcf_basis=basis)
            self.assertEqual(r.status_hint(row, "6")[0], "IN RANGE", basis)
            self.assertEqual(r.strict_failures(row, "6"), [], basis)
        p20 = dict(legacy, core_fcf="50", core_fcf_basis="FY2025 CFO − maint. capex (= all capex)")
        self.assertEqual(r.strict_failures(p20, "6"), ["MCap/FCF 12.0"])
        self.assertFalse(r.fcf_leg_established(dict(legacy, core_fcf_basis="FY2025 CFO − capex")))
        # FI: core_oi n.m.; the MCap/NI leg alone decides.
        fi = dict(self.base(core_oi=r.NM, core_debt_eq=r.NM, core_cash=r.NM), px_unit="USD", trigger="9")
        self.assertEqual(r.status_hint(fi, "8")[0], "IN RANGE")
        self.assertEqual(r.status_hint(fi, "8.5")[0], "NEAR")
        # Without established core numbers the plain distance rule stands.
        self.assertEqual(r.status_hint(csv_row("NOC", trigger="80"), "79")[0], "IN RANGE")


class SweepApplyTests(unittest.TestCase):
    def setUp(self):
        rows = [
            held_core(csv_row("TROW", held="true", zone="HOLD", add_band="55.5", trigger="55.5", sell_line="268.6",
                              last_zone_check="2026-10-02", avg_cost="10.00 USD", px="104.62",
                              px_date="2026-10-02", memo_date="2026-10-03", ev_oi="10.9",
                              memo_path="memos/TROW/TROW_2026-10-03_GSC.md")),
            csv_row("AV2", verdict="AVOID", past="WEAK", future="WEAK"),
            csv_row("OLD", px_date="2026-10-03"),
            csv_row("NEW", memo_date="2026-10-04", memo_path="memos/NEW/NEW_2026-10-04_GSC.md"),
            csv_row("GBX", px_unit="GBp"),
            held_core(csv_row("EUR", px_unit="USD", core_currency="EUR", core_fx="1.05",
                              core_fx_date="2026-09-30")),
            csv_row("OK1"),
        ]
        rows[5]["core_currency"] = "EUR"
        self.root = TempRoot({"register.csv": r.csv_text(rows)})
        self.root.write("queue/rows/2026-10-04_0630_SWEEP.md", "\n".join([
            "---", "row_type: SWEEP", "run_date: 2026-10-04", "run_time: 0630", "---",
            "## Price/ordering refresh", "| Key | Px | Px unit | Close date | Source |", "|---|---|---|---|---|",
            "| TROW | 100.00 | USD | 2026-10-03 | endpoint |",
            "| AV2 | 50 | USD | 2026-10-03 | endpoint |",
            "| OLD | 101 | USD | 2026-10-03 | endpoint |",
            "| NEW | 102 | USD | 2026-10-03 | endpoint |",
            "| GBX | 1.50 | GBP | 2026-10-03 | endpoint |",
            "| EUR | 110 | USD | 2026-10-03 | endpoint |",
            "| OK1 | 99.5 | USD | 2026-10-03 | endpoint |",
            "| GONE | 5 | USD | 2026-10-03 | endpoint |",
            "## FX", "| Pair | Rate | Date |", "|---|---|---|", "| EUR/USD | 1.10 | 2026-10-03 |",
            "## Review requests", "none", ""]))

    def portfolio(self, zone):
        """The SWEEP row file with a '## Portfolio table' giving TROW's zone cell."""
        text = self.root.read("queue/rows/2026-10-04_0630_SWEEP.md")
        table = "\n".join(["## Portfolio table", "| Ticker | Avg cost | Current | Zone (ADD / HOLD / SELL-FLAG) | "
                           "Distance to ADD band | Distance to sell-flag line |", "|---|---|---|---|---|---|",
                           "| TROW | $10.00 | $100.00 | %s | +80.2%% | -62.8%% |" % zone, ""])
        self.root.write("queue/rows/2026-10-04_0630_SWEEP.md", text.replace("## Price/ordering refresh",
                                                                             table + "## Price/ordering refresh"))

    def tearDown(self):
        self.root.close()

    def test_apply_sweep(self):
        self.portfolio("HOLD — unchanged")
        report = r.apply_row(self.root.path, "queue/rows/2026-10-04_0630_SWEEP.md")
        skips = {s["key"]: s["reason"] for s in report["skips"]}
        self.assertIn("out of SWEEP scope", skips["AV2"])
        self.assertIn("not later than", skips["OLD"])
        self.assertIn("after the close", skips["NEW"])
        self.assertIn("unit mismatch", skips["GBX"])
        self.assertIn("not in the register", skips["GONE"])
        self.assertEqual(sorted(c["key"] for c in report["changes"]), ["EUR", "OK1", "TROW"])
        rows = {x["key"]: x for x in r.load_csv(self.root.path)[0]}
        trow = rows["TROW"]
        self.assertEqual((trow["px"], trow["px_date"], trow["px_source"]), ("100.00", "2026-10-03", "SWEEP 2026-10-04"))
        self.assertEqual(trow["last_zone_check"], "2026-10-03")
        self.assertEqual(trow["zone"], "HOLD")
        self.assertEqual(trow["mcap_fcf"], "14.4")
        self.assertEqual((rows["EUR"]["core_fx"], rows["EUR"]["core_fx_date"]), ("1.10", "2026-10-03"))
        self.assertEqual(rows["OK1"]["mcap_fcf"], r.OWED)
        self.assertEqual(rows["AV2"]["px"], "100")

    def test_changed_or_missing_held_zone_keeps_last_zone_check(self):
        # MODEL 7.2 (J11): a SWEEP zone that differs from the Portfolio Zone, or a held name the
        # sweep did not list, moves Px but never the last zone check.
        for zone in ("SELL-FLAG (SR1)", None):
            self.tearDown()
            self.setUp()
            if zone:
                self.portfolio(zone)
            report = r.apply_row(self.root.path, "queue/rows/2026-10-04_0630_SWEEP.md")
            trow = {x["key"]: x for x in r.load_csv(self.root.path)[0]}["TROW"]
            self.assertEqual((trow["px"], trow["last_zone_check"], trow["zone"]), ("100.00", "2026-10-02", "HOLD"))
            note = [c.get("note", "") for c in report["changes"] if c["key"] == "TROW"][0]
            self.assertIn("sweep %s, Portfolio HOLD" % ("SELL-FLAG" if zone else "missing"), note)

    def test_apply_sweep_recomputes_averaged_multiples(self):
        rows = {x["key"]: x for x in r.load_csv(self.root.path)[0]}
        rows["TROW"].update({"core_oi_3y": "2050.4", "core_oi_5y": "1900", "core_fcf_3y": "1400", "core_fcf_5y": "1300",
                             "mcap_fcf_3y": "15.9", "mcap_fcf_5y": "17.2", "ev_oi_3y": "11.7", "ev_oi_5y": "12.6"})
        self.root.write("register.csv", r.csv_text(list(rows.values())))
        report = r.apply_row(self.root.path, "queue/rows/2026-10-04_0630_SWEEP.md")
        trow = {x["key"]: x for x in r.load_csv(self.root.path)[0]}["TROW"]
        self.assertEqual([trow[n] for n in r.AVG_MULTIPLES], ["15.2", "16.4", "11.2", "12.1"])
        self.assertEqual({n: trow[n] for n in r.AVG_MULTIPLES}, r.compute_avg_metrics(trow, "100.00", "USD"))
        change = [c for c in report["changes"] if c["key"] == "TROW"][0]
        self.assertIn("| 15.9 · 17.2 | 11.7 · 12.6 |", change["old"])
        self.assertIn("| 15.2 · 16.4 | 11.2 · 12.1 |", change["new"])
        ok1 = {x["key"]: x for x in r.load_csv(self.root.path)[0]}["OK1"]
        self.assertEqual([ok1[n] for n in r.AVG_MULTIPLES], [r.OWED] * 4)    # no core numbers: still owed

    def test_not_written_without_changes(self):
        self.root.write("queue/rows/2026-10-04_0700_ANALYSE.md",
                        "---\nrow_type: QUEUE\nrun_date: 2026-10-04\n---\n## Queue update\nnone\n")
        before = self.root.read("register.csv")
        report = r.apply_row(self.root.path, "queue/rows/2026-10-04_0700_ANALYSE.md")
        self.assertEqual(report["changes"], [])
        self.assertEqual(self.root.read("register.csv"), before)


class MemoApplyTests(unittest.TestCase):
    def setUp(self):
        held = held_core(csv_row("TROW", held="true", zone="HOLD", add_band="55.5", trigger="55.5", sell_line="268.6",
                                 last_zone_check="2026-10-04", avg_cost="10.00 USD",
                                 memo_path="memos/TROW/TROW_2026-07-31_GSC.md", memo_date="2026-07-31"))
        self.root = TempRoot({
            "register.csv": r.csv_text([held, csv_row("OTHER")]),
            "memos/TROW/TROW_2026-10-03_GSC.md": memo_text(TROW_FM),
            "memos/NEWCO/NEWCO_2026-10-05_GSC.md": memo_text(TROW_FM, ticker="NEWCO", memo_date="2026-10-05",
                                                             memo_version="v1"),
            "memos/LEFT/LEFT_2026-10-05_GSC.md": memo_text(TROW_FM, drop=("position", "zone"),
                                                           ticker="LEFT", memo_date="2026-10-05"),
        })
        for name, memo in (("REVIEW_TROW", "memos/TROW/TROW_2026-10-03_GSC.md"),
                           ("ANALYSE_NEWCO", "memos/NEWCO/NEWCO_2026-10-05_GSC.md")):
            self.root.write("queue/rows/2026-10-05_2130_%s.md" % name,
                            "---\nrow_type: %s\nmemo_path: %s\nrun_date: 2026-10-05\n---\n"
                            % (name.split("_")[0], memo))

    def tearDown(self):
        self.root.close()

    def test_review_of_held_name(self):
        report = r.apply_row(self.root.path, "queue/rows/2026-10-05_2130_REVIEW_TROW.md")
        rows = {x["key"]: x for x in r.load_csv(self.root.path)[0]}
        trow = rows["TROW"]
        self.assertEqual(trow["held"], "true")
        self.assertEqual(trow["avg_cost"], "10.00 USD")
        self.assertEqual(trow["memo_path"], "memos/TROW/TROW_2026-10-03_GSC.md")
        self.assertEqual(trow["last_zone_check"], "2026-10-04")
        self.assertEqual((trow["mcap_fcf"], trow["ev_oi"], trow["ev_oi_all_cash"]), ("15.1", "10.9", "9.0"))
        self.assertEqual(trow["sf_reason"], "buybacks")
        self.assertEqual(trow["core_source"], "memo")
        self.assertEqual(report["changes"][0]["key"], "TROW")
        self.assertEqual(r.validate_row(trow), [])

    def test_held_flag_is_read_only(self):
        report = r.apply_row(self.root.path, "queue/rows/2026-10-05_2130_ANALYSE_NEWCO.md")
        rows = {x["key"]: x for x in r.load_csv(self.root.path)[0]}
        self.assertEqual(rows["NEWCO"]["held"], "false")
        self.assertEqual(rows["NEWCO"]["zone"], r.NM)
        self.assertTrue(any(n.startswith("HELD-MISMATCH NEWCO") for n in report["notes"]))

    def test_attended_apply_memo_position_rekey(self):
        code, out, _err = run_main(["--root", self.root.path, "apply", "--memo", "memos/TROW/TROW_2026-10-03_GSC.md"])
        self.assertEqual(code, 0, out)
        self.assertEqual(json.loads(out)["row_type"], "REVIEW")
        # A sale clears the held flag; a purchase sets it with avg cost and the memo's zone.
        report = r.set_position(self.root.path, "TROW", False)
        self.assertEqual(report["new"], "not held")
        rows = {x["key"]: x for x in r.load_csv(self.root.path)[0]}
        self.assertEqual((rows["TROW"]["held"], rows["TROW"]["zone"], rows["TROW"]["avg_cost"]),
                         ("false", r.NM, r.NM))
        with self.assertRaises(r.ToolError):
            r.set_position(self.root.path, "TROW", True)
        r.set_position(self.root.path, "TROW", True, "90.00 USD")
        rows = {x["key"]: x for x in r.load_csv(self.root.path)[0]}
        self.assertEqual((rows["TROW"]["held"], rows["TROW"]["zone"], rows["TROW"]["avg_cost"]),
                         ("true", "HOLD", "90.00 USD"))
        # Re-key: the row follows the memo folder and the old key joins aliases.
        report = r.rekey(self.root.path, "OTHER", "OTHER.DE")
        rows = {x["key"]: x for x in r.load_csv(self.root.path)[0]}
        self.assertNotIn("OTHER", rows)
        self.assertEqual(rows["OTHER.DE"]["memo_path"], "memos/OTHER.DE/OTHER.DE_2026-09-01_GSC.md")
        self.assertEqual(rows["OTHER.DE"]["aliases"], "OTHER")
        with self.assertRaises(r.ToolError):
            r.rekey(self.root.path, "OTHER.DE", "TROW")
        code, _out, err = run_main(["--root", self.root.path, "apply"])
        self.assertEqual(code, 2)

    def test_memo_without_position_keeps_record(self):
        notes = []
        new = r.row_from_memo("memos/LEFT/LEFT_2026-10-05_GSC.md",
                              self.root.read("memos/LEFT/LEFT_2026-10-05_GSC.md"), notes)
        old = dict(new, held="true", zone="SELL-FLAG SR2", add_band=r.NM, sell_line="14.1",
                   last_zone_check="2026-10-01", avg_cost="10.00 EUR")
        notes += r.keep_position(new, old)
        self.assertEqual((new["held"], new["zone"], new["sell_line"]), ("true", "SELL-FLAG SR2", "14.1"))
        self.assertTrue(any("HELD-MISMATCH" in n for n in notes))


class RowFromMemoTests(unittest.TestCase):
    def test_normalisation_and_backfill(self):
        text = memo_text({"ticker": "APH", "company": "Amphenol", "isin": "n/a — not found",
                          "memo_date": "2026-08-01", "memo_version": "v2 (REVIEW)", "model_version": "v4.0.0",
                          "verdict": "AVOID (SF FAIL)", "quality_past": "STRONG", "quality_future": "STRONG",
                          "sf": "FAIL (capital allocation ADVERSE)", "position": "—"})
        notes = []
        row = r.row_from_memo("memos/APH/APH_2026-08-01_GSC.md", text, notes)
        self.assertEqual((row["verdict"], row["sf"], row["section"], row["memo_version"]),
                         ("AVOID", "FAIL", "AVOID-1", "v2"))
        self.assertTrue(any(n.startswith("NORMALISED APH sf") for n in notes))
        self.assertIn("BACKFILL APH px", notes)
        self.assertIn("BACKFILL APH core_oi", notes)
        self.assertEqual(row["px"], r.OWED)
        self.assertEqual(row["isin"], r.OWED)
        self.assertEqual(row["held"], "false")

    def test_header_lean2_columns(self):
        # Round 2: holding_keys and core_credit replace the four SOTP columns; the ten R10 fields follow.
        self.assertEqual(r.CSV_HEADER[-12:], ["holding_keys", "core_credit"] + list(r.R10_FIELDS))
        for name in r.RETIRED_FIELDS:
            self.assertNotIn(name, r.CSV_HEADER)
        self.assertEqual(r.LENSES, ("STD", "FI"))
        self.assertEqual(r.R10_DEFAULTS["trigger_basis"], "all-cash")
        self.assertEqual({r.R10_DEFAULTS[n] for n in r.R10_FIELDS[1:]}, {r.OWED})

    def test_lens_fields_legacy_defaults_and_carried(self):
        legacy = {k: v for k, v in TROW_FM.items() if k not in ("lens",) + tuple(r.LENS_DEFAULTS)}
        notes = []
        row = r.row_from_memo("memos/TROW/TROW_2026-10-03_GSC.md", memo_text(legacy), notes)
        self.assertEqual([row[n] for n in r.LENS_DEFAULTS], ["n.m.", "0"])
        self.assertFalse(any("credit" in n or "holding_keys" in n for n in notes), notes)
        # A lean-1 memo's retired fields are not read: no credit, no backfill.
        lean1 = dict(legacy, sotp_keys="AZN", core_credit_fix="300", core_credit_mkt="900", core_credit_px="104.62")
        row = r.row_from_memo("memos/TROW/TROW_2026-10-03_GSC.md", memo_text(lean1), [])
        self.assertEqual([row[n] for n in r.LENS_DEFAULTS], ["n.m.", "0"])
        fm = dict(TROW_FM, holding_keys="AZN; SEB-A.ST", core_credit="900")
        row = r.row_from_memo("memos/TROW/TROW_2026-10-03_GSC.md", memo_text(fm), [])
        self.assertEqual([row[n] for n in r.LENS_DEFAULTS], ["AZN; SEB-A.ST", "900"])
        self.assertEqual(r.validate_row(row), [])
        notes = []
        row = r.row_from_memo("memos/TROW/TROW_2026-10-03_GSC.md", memo_text(dict(fm, core_credit="abc")), notes)
        self.assertEqual(row["core_credit"], r.OWED)
        self.assertTrue(any(n.startswith("BACKFILL TROW core_credit") for n in notes), notes)
        self.assertEqual(r.validate_row(row), [])
        notes = []
        row = r.row_from_memo("memos/TROW/TROW_2026-10-03_GSC.md", memo_text(dict(fm, core_credit="-5")), notes)
        self.assertEqual(row["core_credit"], r.OWED)
        self.assertTrue(any(n.startswith("BACKFILL TROW lens fields") and "negative" in n for n in notes), notes)

    def test_r10_fields_from_memo(self):
        notes = []
        row = r.row_from_memo("memos/TROW/TROW_2026-10-03_GSC.md", memo_text(TROW_FM), notes)
        self.assertEqual([row[n] for n in r.R10_FIELDS],
                         ["no-cash", "1479.2", "2050.4", "1900", "1400", "1300", "15.9", "17.2", "11.7", "12.6"])
        self.assertEqual(notes, [])
        # A memo written before v4.5.0: the legacy defaults, no backfill owed.
        old = {k: v for k, v in TROW_FM.items() if k not in r.R10_FIELDS}
        notes = []
        row = r.row_from_memo("memos/TROW/TROW_2026-10-03_GSC.md", memo_text(old, model_version="v4.4.1"), notes)
        self.assertEqual([row[n] for n in r.R10_FIELDS], [r.R10_DEFAULTS[n] for n in r.R10_FIELDS])
        self.assertEqual(notes, [])
        self.assertEqual(r.validate_row(row), [])
        # A v4.5.0 memo that omits them owes them; a missing multiple is recomputed.
        notes = []
        row = r.row_from_memo("memos/TROW/TROW_2026-10-03_GSC.md",
                              memo_text(TROW_FM, drop=("core_fcf_all", "ev_oi_5y", "trigger_basis")), notes)
        self.assertEqual((row["core_fcf_all"], row["ev_oi_5y"], row["trigger_basis"]), (r.OWED, "12.6", "all-cash"))
        for needle in ("BACKFILL TROW core_fcf_all", "BACKFILL TROW ev_oi_5y (recomputed from core numbers)",
                       "BACKFILL TROW trigger_basis"):
            self.assertIn(needle, notes)
        self.assertTrue(any(p.startswith("trigger_basis: all-cash") for p in r.validate_row(row)))

    def test_table_output(self):
        root = TempRoot({"memos/TROW/TROW_2026-10-03_GSC.md": memo_text(TROW_FM)})
        try:
            code, out, _err = run_main(["--root", root.path, "row-from-memo",
                                        "memos/TROW/TROW_2026-10-03_GSC.md", "--table"])
        finally:
            root.close()
        self.assertEqual(code, 0)
        self.assertIn("| TROW | T. Rowe Price Group, Inc. | 2026-10-03 | v5 | WATCH | ADEQUATE · 23.9% ROCE | "
                      "ADEQUATE | PASS CAUTION · buybacks | 104.62 | 55.5 | 15.1 | 10.9 | 15.9 · 17.2 | 11.7 · 12.6 | "
                      "2026-10-30 |", out)
        self.assertIn("| TROW | HOLD | 104.62 | 55.5 | 268.6 | 2026-10-02 | 2026-10-30 |", out)


class LintTests(unittest.TestCase):
    PATH = "memos/TROW/TROW_2026-10-03_GSC.md"

    def lint(self, **over):
        drop = over.pop("drop", ())
        return r.lint_memo(self.PATH, memo_text(TROW_FM, drop=drop, **over))

    def test_clean_memo(self):
        fails, warns = self.lint()
        self.assertEqual(fails, [])
        self.assertEqual(warns, [])

    def test_failures(self):
        cases = [
            ({"drop": ("core_cash",)}, "core_cash: missing"),
            ({"verdict": "WATCH (FAIR)"}, "verdict"),
            ({"sf": "PASS (1 flag)"}, "sf:"),
            ({"memo_version": "v5 (REVIEW)"}, "memo_version"),
            ({"ev_oi": "12.0"}, "ev_oi: printed 12.0"),
            ({"mcap_fcf": "n.m."}, "mcap_fcf"),
            ({"px": "$104.62"}, "px:"),
            ({"core_debt_eq": "-"}, "core_debt_eq: '-'"),
            ({"past_reason": "high returns"}, "past_reason"),
            ({"future_reason": "breadth"}, "future_reason"),
            ({"sf_reason": "too many buybacks here"}, "sf_reason"),
            ({"next_review_short": "Q3'26"}, "next_review_short"),
            ({"aliases": "—"}, "aliases"),
            ({"zone": "HOLD (fine)"}, "zone"),
            ({"add_band": "< ≈ $55.5"}, "add_band"),
            ({"core_fx": "100"}, "core_fx"),
            ({"px_unit": "US$"}, "px_unit"),
            ({"quality_past": "WEAK"}, "verdict WATCH with 1 failed gate"),
        ]
        for over, needle in cases:
            fails, _warns = self.lint(**dict(over))
            self.assertTrue(any(needle in f for f in fails), "%r -> %r" % (over, fails))

    def test_sf_pass_never_carries_a_fail_only_token(self):
        # R8: `alignment`, `flag pair` and `inherited` fail at strike-logic step 3; a PASS never carries them.
        for token in ("alignment", "flag pair", "inherited"):
            fails, _ = self.lint(sf_reason=token)
            self.assertTrue(any(f.startswith("sf_reason: %r — a PASS writes n.m." % token) for f in fails),
                            (token, fails))
            fails, _ = self.lint(sf="FAIL", verdict="AVOID", sf_reason=token)
            self.assertEqual(fails, [], token)
        fails, _ = self.lint(sf="FAIL", verdict="AVOID", sf_reason="pledging")
        self.assertTrue(any("not in the SF vocabulary" in f for f in fails), fails)

    def test_minor_unit_same_currency(self):
        fm = dict(TROW_FM, px="1898.5", px_unit="GBp", core_currency="GBP", core_fx="100",
                  price_at_memo="1,898.5p", trigger="1500", trigger_band='"CHEAP < ≈ 1,500p"')
        fails, _ = r.lint_memo(self.PATH, memo_text(fm))
        self.assertTrue(any("major-unit rate" in f for f in fails), fails)

    def test_warnings(self):
        fails, warns = self.lint(price_at_memo="$99.00", px_unit="EUR")
        self.assertEqual(fails, [])
        self.assertTrue(any("price_at_memo" in w for w in warns))
        self.assertTrue(any("US-line default USD" in w for w in warns))
        # R10: the band states the no-cash bound first, or labels it no-cash.
        for band in ('"CHEAP < ≈ $55.5 no-cash / ≈ $64.0 all-cash (context)"',
                     '"CHEAP < ≈ $61–64 (P12 edge); no-cash ≈ $55.5"'):
            _fails, warns = self.lint(trigger_band=band)
            self.assertFalse(any(w.startswith("trigger 55.5") for w in warns), (band, warns))
        _fails, warns = self.lint(trigger_band='"CHEAP < ≈ $64.0 (all-cash)"')
        self.assertTrue(any(w.startswith("trigger 55.5 does not match") for w in warns), warns)

    def test_dnaf_gate0(self):
        fm = {k: "n.m." for k in TROW_FM if k in r.DNAF_NM_FIELDS}
        base = dict(TROW_FM, verdict="DNAF", position="—")
        base.update(fm)
        base["next_review_short"] = "n.m."
        fails, _ = r.lint_memo(self.PATH, memo_text(base, drop=("zone", "add_band", "sell_flag_line")))
        self.assertEqual(fails, [])
        self.assertTrue(set(r.R10_FIELDS) <= r.DNAF_NM_FIELDS)          # a section 6.4 memo writes n.m. for all ten

    FI = {"lens": "FI", "core_oi": "n.m.", "core_debt_eq": "n.m.", "core_cash": "n.m.", "ev_oi": "n.m.",
          "ev_oi_all_cash": "n.m.", "core_oi_basis": "FY2025 NI basis", "past_reason": "23.9% ROE",
          "core_fcf_basis": "FY2025 NI basis", "core_oi_3y": "n.m.", "core_oi_5y": "n.m.", "core_fcf_all": "n.m.",
          "ev_oi_3y": "n.m.", "ev_oi_5y": "n.m."}

    def test_fi_lens(self):
        fails, _ = self.lint(**self.FI)
        self.assertEqual(fails, [])
        fails, _ = self.lint(**dict(self.FI, core_oi="2188.8"))
        self.assertTrue(any(f.startswith("core_oi: '2188.8' — under the FI lens") for f in fails), fails)
        fails, _ = self.lint(**dict(self.FI, past_reason="23.9% ROCE"))
        self.assertTrue(any("FI lens grades ROE" in f for f in fails), fails)
        fails, _ = self.lint(**dict(self.FI, core_fcf_all="1479.2", core_oi_3y="2050.4"))
        self.assertTrue(any(f.startswith("core_fcf_all: '1479.2' — under the FI lens it is n.m.") for f in fails), fails)
        self.assertTrue(any(f.startswith("core_oi_3y: '2050.4' — under the FI lens it is n.m.") for f in fails), fails)
        fails, _ = self.lint(**dict(self.FI, core_fcf_basis="FY2025 CFO − maint. capex (disclosed)"))
        self.assertTrue(any("does not fit lens FI" in f for f in fails), fails)
        # The FI trigger is the P25 band's line: MCap/NI at it within 8.0 (the book leg may bind lower).
        fails, _ = self.lint(**dict(self.FI, trigger="50", add_band="50"))
        self.assertEqual(fails, [])
        fails, _ = self.lint(**dict(self.FI, trigger="60", add_band="60"))
        self.assertTrue(any(f.startswith("trigger: 60 is not the FI band's line") for f in fails), fails)
        # The retired substitution rule: an STD memo never writes core_oi n.m.
        fails, _ = self.lint(core_oi="n.m.", ev_oi="n.m.", ev_oi_all_cash="n.m.")
        self.assertTrue(any(f.startswith("core_oi: 'n.m.' is not a plain number") for f in fails), fails)

    GROUP_BODY = ("\n## B. Financial record\n\nB4 Division table (filer segments, weights, Future grades)\n"
                  "\n## F. Valuation math\n\nHolding credits: AZN at its own buy line, after tax.\n")

    def group(self, body=None, **over):
        fm = dict(TROW_FM, holding_keys="AZN", core_credit="500", core_oi_basis="FY2025 J1 · fin. income out",
                  future_reason="unit customer conc.")
        fm.update(over)
        for name, value in r.compute_metrics(fm, fm["px"], fm["px_unit"]).items():
            fm[name] = over.get(name, value)
        for name, value in r.compute_avg_metrics(fm, fm["px"], fm["px_unit"]).items():
            fm[name] = over.get(name, value)
        if "trigger" not in over:
            # The credited no-cash bound: P_FCF = (8 FCF + C) / N, P_nc = (7 OI - D + C) / N.
            n, credit = r.dec(fm["core_shares_diluted"]), r.dec(fm["core_credit"])
            p_fcf = (8 * r.dec(fm["core_fcf"]) + credit) / n
            p_nc = (7 * r.dec(fm["core_oi"]) - r.dec(fm["core_debt_eq"]) + credit) / n
            fm["trigger"] = fm["add_band"] = r.plain(min(p_fcf, p_nc).quantize(r.Decimal("0.01")))
        return r.lint_memo(self.PATH, memo_text(fm) + (self.GROUP_BODY if body is None else body))

    def test_group_memo(self):
        # Round 2 (R2-R5, V14): groups are STD (or FI) with holding_keys and one constant credit.
        fails, warns = self.group()
        self.assertEqual(fails, [], warns)
        for body, needle in ((self.GROUP_BODY.replace("B4 Division table", "B4 Part records"), "'B4 Division table'"),
                             (self.GROUP_BODY.replace("Holding credits", "Credits"), "'Holding credits' table")):
            fails, _ = self.group(body)
            self.assertTrue(any(needle in f for f in fails), (needle, fails))
        for lens in ("SOTP", "SOTP-DOUBT"):
            fails, _ = self.group(lens=lens)
            self.assertTrue(any(f.startswith("lens: %r is not one of STD/FI" % lens) for f in fails), (lens, fails))
        fails, _ = self.group(lens="FI")
        self.assertTrue(any("holding credits exist only under STD" in f for f in fails), fails)
        # A v4.5.0 memo carrying a retired lean-1 field fails.
        for name, value in (("sotp_keys", "AZN"), ("core_credit_px", "104.62"), ("core_credit_mkt", "0")):
            fails, _ = self.group(**{name: value})
            self.assertTrue(any(f.startswith(name) and "retired field (round 2: R2–R5, V14)" in f for f in fails),
                            (name, fails))
        # A group prefix needs the group's B4 Division table; 'fin.' retired.
        fails, _ = self.group(body="\n## F. Valuation math\n\nHolding credits.\n", holding_keys="n.m.", core_credit="0")
        self.assertTrue(any("carries the group prefix 'unit'" in f for f in fails), fails)
        # Past is one consolidated or look-through record (review fix B1): never a prefix, never ROE on STD.
        for value in ("sub 9.5% ROE", "unit 23.9% ROCE", "fin. 9.5% ROE", "9.5% ROE"):
            fails, _ = self.group(past_reason=value)
            self.assertTrue(any("past_reason" in f for f in fails), (value, fails))

    def test_lens_and_credit_failures(self):
        cases = [
            ({"lens": "BANK"}, "lens: 'BANK' is not one of"),
            ({"lens": "n.m."}, "lens: 'n.m.'"),
            ({"core_credit": "-5"}, "core_credit: -5 is negative"),
            ({"core_credit": "100"}, "holding_keys: n.m., but core_credit is 100"),
            ({"core_credit": "abc"}, "core_credit: 'abc' is not a plain number"),
            ({"holding_keys": "AZN; bad key"}, "holding_keys: 'AZN; bad key'"),
            ({"holding_keys": "AZN"}, "lacks a line starting 'B4 Division table'"),
            ({"future_reason": "unit customer conc."}, "carries the group prefix 'unit'"),
            ({"past_reason": "unit 23.9% ROCE"}, "Past %s states its worst-of-four level" % "ADEQUATE"),
            ({"past_reason": "23.9% ROE"}, "ROE is the FI lens"),
            ({"core_oi_basis": "FY2025 ex-impairment"}, "names an adjusted line"),
            ({"core_oi_basis": "FY2025 adjusted EBIT"}, "names an adjusted line"),
            ({"core_oi_basis": "FY2025 reported"}, "is not '{FY####"),
            ({"core_oi_basis": "FY2025 OI_P"}, "OI_P (the SOTP perimeter) is retired"),
            ({"core_oi_basis": "FY2025 NI basis"}, "line 'NI basis' does not fit lens STD"),
            ({"core_oi_basis": "FY2025 J1 · lease-capitalised · lease-capitalised"}, "is not '{FY####"),
        ]
        for over, needle in cases:
            fails, _warns = self.lint(**dict(over))
            self.assertTrue(any(needle in f for f in fails), "%r -> %r" % (over, fails))

    def test_fi_average(self):
        fails, _ = self.lint(**dict(self.FI, core_oi_basis="FY2016–FY2025 avg NI basis"))
        self.assertEqual(fails, [])
        fails, _ = self.lint(core_oi_basis="FY2016–FY2025 avg J1")
        self.assertTrue(any("an average period on J1 is the P28 down-year reading only" in f for f in fails), fails)
        # FI FCF basis: '{period} NI basis[ · down-year avg]'; tagged, core_fcf is the lower average exactly.
        fi_down = dict(self.FI, core_fcf_basis="FY2021–FY2025 avg NI basis · down-year avg", core_fcf="1300",
                       mcap_fcf="17.2", trigger="48.8", add_band="48.8")
        fails, _ = self.lint(**fi_down)
        self.assertEqual(fails, [])
        fails, _ = self.lint(**dict(fi_down, core_fcf="1400", mcap_fcf="15.9", trigger="52.5", add_band="52.5"))
        self.assertTrue(any("so core_fcf is the lower of core_fcf_3y and core_fcf_5y exactly (1300)" in f
                            for f in fails), fails)
        fails, _ = self.lint(**dict(self.FI, core_fcf_basis="FY2025 NI basis · fin. income out"))
        self.assertTrue(any("an FI NI basis takes only ' · down-year avg'" in f for f in fails), fails)

    def test_legacy_oi_basis_only_blacklisted(self):
        fails, _ = self.lint(model_version="v4.4.1", core_oi_basis="FY2025 reported")
        self.assertEqual(fails, [])
        fails, _ = self.lint(model_version="v4.4.1", core_oi_basis="FY2025 underlying")
        self.assertTrue(any("names an adjusted line" in f for f in fails), fails)

    def test_lint_requires_r10_fields(self):
        for name in r.R10_FIELDS:
            fails, _ = self.lint(drop=(name,))
            self.assertIn("%s: missing" % name, fails)
        for name in ("core_oi_3y", "core_fcf_all"):
            fails, _ = self.lint(**{name: "-"})
            self.assertTrue(any(f.startswith("%s: '-' (not established)" % name) for f in fails), (name, fails))
            fails, _ = self.lint(**{name: "about 2000"})
            self.assertTrue(any(f.startswith("%s: 'about 2000' is not a plain number or n.m." % name) for f in fails),
                            (name, fails))
        fails, _ = self.lint(trigger_basis="all-cash")
        self.assertTrue(any(f.startswith("trigger_basis: 'all-cash' — the operative trigger is the no-cash bound")
                            for f in fails), fails)
        fails, _ = self.lint(ev_oi_3y="12.0")
        self.assertTrue(any(f.startswith("ev_oi_3y: printed 12.0, recomputed 11.7") for f in fails), fails)
        fails, _ = self.lint(mcap_fcf_5y="n.m.")
        self.assertTrue(any(f.startswith("mcap_fcf_5y: printed 'n.m.', recomputed '17.2'") for f in fails), fails)
        # A record shorter than five years: n.m. on both sides of the 5y readings.
        fails, _ = self.lint(core_oi_5y="n.m.", core_fcf_5y="n.m.", mcap_fcf_5y="n.m.", ev_oi_5y="n.m.")
        self.assertEqual(fails, [])
        # Under v4.4.1 (a memo written before round 2 is never linted under it) the fields are only present.
        fails, _ = self.lint(model_version="v4.4.1", trigger_basis="all-cash", ev_oi_3y="99.0")
        self.assertEqual(fails, [])

    def test_lint_trigger_is_the_no_cash_bound(self):
        # TROW: MCap/FCF binds at 55.5 (8.0), EV/OI no-cash 6.1 there; all-cash ~ would be looser.
        self.assertEqual(self.lint()[0], [])
        cases = [("64", "MCap/FCF is 9.2"),        # the all-cash EV/OI leg: MCap/FCF fails at it
                 ("50", "MCap/FCF is 7.2")]        # below the line: nothing binds there
        for trigger, needle in cases:
            fails, _ = self.lint(trigger=trigger, add_band=trigger)
            self.assertTrue(any(f.startswith("trigger: %s is not the no-cash bound (R10)" % trigger) and needle in f
                                for f in fails), (trigger, fails))
        fails, _ = self.lint(trigger="55.4", add_band="55.4")      # within 0.1 of the threshold
        self.assertEqual(fails, [])
        fails, _ = self.lint(trigger="n.m.", add_band="n.m.")
        self.assertEqual(fails, [])
        # A held name's ADD band is its trigger (P21, R10).
        fails, _ = self.lint(add_band="54")
        self.assertTrue(any(f.startswith("add_band: 54, but a held name's ADD band is its trigger") for f in fails), fails)
        fails, _ = self.lint(add_band="54", position="—", drop=("zone", "sell_flag_line"))
        self.assertEqual(fails, [])

    def test_lint_down_year_basis(self):
        # P28 (R1): the averaged reading is tagged, reads an average period and is the lower average exactly.
        down = {"core_oi_basis": "FY2021–FY2025 avg J1 · down-year avg", "core_oi": "1900",
                "core_fcf_basis": "FY2021–FY2025 avg CFO − maint. capex (constructed) · down-year avg",
                "core_fcf": "1300"}
        fm = dict(TROW_FM, **down)
        for name, value in r.compute_metrics(fm, fm["px"], fm["px_unit"]).items():
            down[name] = value
        p_fcf = 8 * r.dec("1300") / r.dec("213.316")
        p_nc = (7 * r.dec("1900") - r.dec("1620.9")) / r.dec("213.316")
        down["trigger"] = down["add_band"] = r.plain(min(p_fcf, p_nc).quantize(r.Decimal("0.1")))
        fails, _ = self.lint(**down)
        self.assertEqual(fails, [])
        cases = [
            ({"core_oi": "2050.4"}, "core_oi_basis: ' · down-year avg', so core_oi is the lower of core_oi_3y and "
                                    "core_oi_5y exactly (1900), not 2050.4 (P28)"),
            ({"core_oi_5y": "n.m."}, "core_oi_basis: ' · down-year avg', but core_oi_3y and core_oi_5y are not both"),
            ({"core_oi_basis": "FY2021–FY2025 avg J1"}, "an average period on J1 is the P28 down-year reading only"),
            ({"core_oi_basis": "FY2025 J1 · down-year avg"}, "' · down-year avg' reads an 'FY####–FY#### avg' period"),
            ({"core_fcf": "1400"}, "so core_fcf is the lower of core_fcf_3y and core_fcf_5y exactly (1300)"),
            ({"core_fcf_basis": "FY2021–FY2025 avg CFO − maint. capex (constructed)"},
             "core_fcf_basis: 'FY2021–FY2025 avg CFO − maint. capex (constructed)' — an average period is the P28"),
        ]
        for over, needle in cases:
            fails, _ = self.lint(**dict(down, **over))
            self.assertTrue(any(needle in f for f in fails), "%r -> %r" % (over, fails))

    def test_lint_fcf_basis_grammar_and_all_capex_order(self):
        # R6: FCF is CFO − maintenance capex (P20 basis named); the all-capex reading is the lower one.
        for basis in ("FY2025 CFO − maint. capex (disclosed)", "FY2025 CFO - maint. capex (constructed)",
                      "TTM Q2-2026 CFO − maint. capex (constructed) · fin. income out"):
            fails, _ = self.lint(core_fcf_basis=basis, core_fcf_all="1300")
            self.assertEqual(fails, [], basis)
        for basis in ("FY2025 CFO − capex", "FY2025 levered FCF", "FY2025 CFO − maint. capex (D&A)",
                      "FY2025 CFO − maint. capex (disclosed) · lease-capitalised"):
            fails, _ = self.lint(core_fcf_basis=basis)
            self.assertTrue(any(f.startswith("core_fcf_basis: %r is not" % basis) for f in fails), (basis, fails))
        fails, _ = self.lint(core_fcf_basis="FY2025 CFO − maint. capex (disclosed)", core_fcf_all="1500")
        self.assertTrue(any(f.startswith("core_fcf_all: 1500 is above core_fcf 1479.2") for f in fails), fails)
        fails, _ = self.lint(core_fcf_all="1300")      # '= all capex': the two readings are one
        self.assertTrue(any("maintenance capex = all capex, so it equals core_fcf" in f for f in fails), fails)
        fails, _ = self.lint(core_fcf_basis="FY2025 NI basis")
        self.assertTrue(any("does not fit lens STD" in f for f in fails), fails)
        # Before v4.5.0 the FCF basis is free text.
        fails, _ = self.lint(model_version="v4.4.1", core_fcf_basis="FY2025 levered FCF")
        self.assertEqual(fails, [])


class LintRowTests(unittest.TestCase):
    """lint-row (v4.5.2): the PR 87 failure (a table pasted without its header) and its neighbours."""
    MEMO = "memos/TROW/TROW_2026-10-03_GSC.md"
    ROW = "queue/rows/2026-10-03_2250_REVIEW_TROW.md"
    TITLE = "HELD · GSC REVIEW TROW 2026-10-03 — WATCH; zone HOLD"

    def tables(self, fm=None):
        root = TempRoot({self.MEMO: memo_text(fm or TROW_FM)})
        try:
            code, out, _err = run_main(["--root", root.path, "row-from-memo", self.MEMO, "--table"])
        finally:
            root.close()
        self.assertEqual(code, 0)
        master, _, portfolio = out.strip("\n").partition("\n\n")
        return master, portfolio

    def row_text(self, master=None, portfolio=None, **fm):
        m, p = self.tables()
        front = {"row_type": "REVIEW", "key": "TROW", "company": "T. Rowe Price Group, Inc.",
                 "memo_path": self.MEMO, "run_date": "2026-10-03", "run_time": "2250", "held": "true",
                 "pr_title": self.TITLE}
        front.update(fm)
        lines = ["---"] + ["%s: %s" % kv for kv in front.items()] + ["---", "## Register row (new)",
                                                                     m if master is None else master]
        lines += ["## Replaces", "| TROW | ... |", "## Portfolio row", p if portfolio is None else portfolio,
                  "## Queue update", "none"]
        return "\n".join(lines) + "\n"

    def lint(self, text, rel=None, memo=None):
        memo_text_ = memo_text(TROW_FM) if memo is None else memo
        return r.lint_row(rel or self.ROW, text, lambda path: memo_text_ if path == self.MEMO else None)

    def test_the_printed_tables_pass(self):
        self.assertEqual(self.lint(self.row_text()), [])
        root = TempRoot({self.MEMO: memo_text(TROW_FM), self.ROW: self.row_text()})
        try:
            code, out, _err = run_main(["--root", root.path, "lint-row", self.ROW])
        finally:
            root.close()
        self.assertEqual(code, 0, out)
        self.assertIn("lint-row %s: OK" % self.ROW, out)

    def test_header_missing_is_the_pr87_case(self):
        master, _ = self.tables()
        text = self.row_text(master=master.split("\n")[2])
        fails = self.lint(text)
        self.assertTrue(any("header and separator lines are missing" in f for f in fails), fails)
        self.assertTrue(any(f.startswith("verdicts differ: row table ?, memo WATCH, pr_title WATCH") for f in fails),
                        fails)
        # gsc-automerge reads the same cell the same way: no Verdict column, so no verdict.
        self.assertIsNone(r.row_file_verdict(text))
        self.assertEqual(r.row_file_verdict(self.row_text()), "WATCH")
        root = TempRoot({self.MEMO: memo_text(TROW_FM), self.ROW: text})
        try:
            code, out, _err = run_main(["--root", root.path, "lint-row", self.ROW])
        finally:
            root.close()
        self.assertEqual(code, 1)
        self.assertIn("FAIL (2)", out)

    def test_separator_missing_or_cells_edited(self):
        master, portfolio = self.tables()
        lines = master.split("\n")
        fails = self.lint(self.row_text(master="\n".join([lines[0], lines[2]])))
        self.assertTrue(any("separator line" in f for f in fails), fails)
        fails = self.lint(self.row_text(master=master.replace("| 55.5 |", "| 55.6 |", 1)))
        self.assertEqual(fails, ["## Register row (new): cells differ from row-from-memo --table: Trigger "
                                 "(never type a row by hand)"])
        fails = self.lint(self.row_text(portfolio=portfolio.split("\n")[2]))
        self.assertTrue(any(f.startswith("## Portfolio row: the header and separator") for f in fails), fails)
        fails = self.lint(self.row_text(portfolio=""))
        self.assertTrue(any(f.startswith("## Portfolio row: no table") for f in fails), fails)

    def test_unheld_memo_prints_no_portfolio_row(self):
        fm = dict(TROW_FM, position="—")
        master, portfolio = self.tables(fm)
        self.assertEqual(portfolio, "")
        text = self.row_text(master=master, held="false")
        fails = self.lint(text, memo=memo_text(fm))
        self.assertEqual(fails, ["## Portfolio row: the memo is not held, so row-from-memo --table prints none"])

    def test_title_and_front_matter(self):
        fails = self.lint(self.row_text(pr_title="GSC REVIEW TROW 2026-10-03 — AVOID; was WATCH"))
        self.assertEqual(fails, ["verdicts differ: row table WATCH, memo WATCH, pr_title AVOID "
                                 "(gsc-automerge would hold the PR)"])
        fails = self.lint(self.row_text(run_time="2251", key="TROW.X", row_type="ANALYSE", held="yes"))
        self.assertEqual(len(fails), 4, fails)
        fails = self.lint(self.row_text(memo_path="memos/TROW/TROW_2026-10-02_GSC.md"))
        self.assertTrue(fails and fails[0].startswith("memo_path:"), fails)
        self.assertTrue(r.lint_row(self.ROW, self.row_text(), lambda path: None)[0].startswith(
            "memo_path: cannot read"))
        self.assertTrue(self.lint(self.row_text(), memo="")[0].endswith("has no front matter"))
        self.assertEqual(self.lint("no front matter\n"), ["no front matter (the --- block of README section 4)"])
        self.assertTrue(self.lint(self.row_text(), rel="queue/rows/TROW.md")[0].endswith("[_{KEY}].md)"))

    def test_other_row_types(self):
        inc = ("---\nrow_type: INCOMPLETE\nkey: TROW\nrun_date: 2026-10-03\nrun_time: 2250\nheld: true\n"
               "pr_title: HELD · GSC REVIEW TROW 2026-10-03 — INCOMPLETE (dependency: AZN)\n---\n"
               "## Group dependency\n`AZN` — holding of TROW, memo missing\n")
        self.assertEqual(self.lint(inc), [])
        queue = ("---\nrow_type: QUEUE\nrun_date: 2026-10-03\nrun_time: 2250\n"
                 "pr_title: GSC ANALYSE 2026-10-03 — queue exhausted\n---\n## Queue update\nnone\n")
        self.assertEqual(self.lint(queue, rel="queue/rows/2026-10-03_2250_ANALYSE.md"), [])
        self.assertTrue(self.lint(queue)[0].startswith("row_type: 'QUEUE'; this file name takes REVIEW"))
        sweep = ("---\nrow_type: SWEEP\nrun_date: 2026-10-03\nrun_time: 0700\n"
                 "pr_title: GSC SWEEP 2026-10-03 — 9/9 priced · 0 review requests\n---\n"
                 "## Portfolio table\n| Ticker | Avg cost | Current | Zone (ADD / HOLD / SELL-FLAG) |\n"
                 "|---|---|---|---|\n| TROW | 10.00 | 104.62 | HOLD |\n")
        sweep_rel = "queue/rows/2026-10-03_0700_SWEEP.md"
        self.assertEqual(self.lint(sweep, rel=sweep_rel), [])
        headless = sweep.replace("| Ticker | Avg cost | Current | Zone (ADD / HOLD / SELL-FLAG) |\n|---|---|---|---|\n", "")
        self.assertEqual(self.lint(headless, rel=sweep_rel),
                         ["## Portfolio table: needs its header line with the Ticker and Zone columns"])
        self.assertEqual(self.lint(sweep.split("## Portfolio table")[0], rel=sweep_rel),
                         ["## Portfolio table is missing (every held name, README section 4)"])


class ParserTests(unittest.TestCase):
    def test_next_review_short(self):
        cases = {
            "Q3'26 29 Oct 2026": "2026-10-29",
            "FY2026 10-K (~Feb 2027)": "Feb 2027",
            "Decision pending (user); 9M 4 Nov 2026; AR-2026 3 Feb 2027": "2026-11-04",
            "Re-listing/IPO event only": r.NM,
            "Q3'26 results": "Q3 2026",
            "when the CEO leaves": r.OWED,
        }
        for text, want in cases.items():
            self.assertEqual(r.parse_next_review_short(text), want, text)

    def test_endpoint_symbol(self):
        self.assertEqual(r.endpoint_symbol("BRK.B"), "BRK-B")
        self.assertEqual(r.endpoint_symbol("INVE-B.ST"), "INVE-B.ST")
        self.assertEqual(r.endpoint_symbol("2330.TW"), "2330.TW")
        self.assertEqual(r.endpoint_symbol("AAPL"), "AAPL")
        self.assertEqual(r.endpoint_symbol("6488.TWO"), "6488.TWO")

    def test_front_matter(self):
        fm = r.parse_front_matter('---\na: "x # y"\nb: plain # note\nc: \'it\'\'s\'\n---\nbody')
        self.assertEqual(fm, {"a": "x # y", "b": "plain", "c": "it's"})
        self.assertEqual(r.parse_front_matter("no front matter"), {})


class CheckTests(unittest.TestCase):
    def build(self, rows, md=None, extra=None):
        files = {"register.csv": r.csv_text(rows),
                 "_REGISTER.md": md if md is not None else r.render(rows, "v10", "2026-10-07")}
        for row in rows:
            files[row["memo_path"]] = "---\nticker: %s\n---\n" % row["key"]
        files.update(extra or {})
        return TempRoot(files, git=True)

    def test_clean_register_passes(self):
        root = self.build([csv_row("AAA"), csv_row("BBB", ev_oi="8.0")])
        try:
            breaches, listed, counts = r.check(root.path, base="HEAD")
        finally:
            root.close()
        self.assertEqual(breaches, [])
        self.assertEqual(counts["names_total"], 2)

    def test_crlf_working_tree_passes(self):
        rows = [csv_row("AAA")]
        root = self.build(rows, md=r.render(rows, "v10", "2026-10-07").replace("\n", "\r\n"))
        try:
            breaches, _listed, _counts = r.check(root.path)
        finally:
            root.close()
        self.assertEqual(breaches, [])

    def test_hand_edit_and_missing_key(self):
        rows = [csv_row("AAA"), csv_row("BBB")]
        root = self.build(rows)
        try:
            md = root.read("_REGISTER.md").replace("| AAA Inc. |", "| AAA Corp |")
            root.write("_REGISTER.md", md)
            root.write("register.csv", r.csv_text([rows[0]]))
            breaches, _listed, _counts = r.check(root.path, base="HEAD")
        finally:
            root.close()
        self.assertTrue(any("not the rendering" in b for b in breaches), breaches)
        self.assertTrue(any("missing: BBB" in b for b in breaches), breaches)

    def test_memo_folder_findings(self):
        rows = [csv_row("AAA"), csv_row("BBB")]
        extra = {"memos/BBB/BBB_2026-07-01_GSC.md": "old\n"}
        root = self.build(rows, extra=extra)
        try:
            breaches, listed, _ = r.check(root.path, base="HEAD")
            # Unchanged rows: listed, not breaches.
            self.assertEqual(breaches, [])
            self.assertTrue(any("memos/BBB/ holds 2 files" in x for x in listed), listed)
            # A changed row with a two-file folder is a breach.
            changed = dict(rows[1], next_review_short="Mar 2027")
            root.write("register.csv", r.csv_text([rows[0], changed]))
            root.write("_REGISTER.md", r.render([rows[0], changed], "v10", "2026-10-07"))
            breaches, listed, _ = r.check(root.path, base="HEAD")
        finally:
            root.close()
        self.assertTrue(any("memos/BBB/ holds 2 files" in b for b in breaches), breaches)

    def test_sweep_multiples_must_recompute(self):
        row = held_core(csv_row("TROW", px="104.62", px_source="SWEEP 2026-10-04", ev_oi="10.9",
                                mcap_fcf="15.1", ev_oi_all_cash="9.1"))
        root = self.build([row])
        try:
            breaches, _listed, _ = r.check(root.path)
        finally:
            root.close()
        self.assertTrue(any("ev_oi_all_cash 9.1 does not recompute" in b for b in breaches), breaches)

    def test_every_row_with_core_numbers_recomputes(self):
        # A memo-priced rebuild row is exact; a memo's own print at its own price may sit 0.1 off.
        rebuilt = dict(held_core(csv_row("TROW", px="104.62", ev_oi="10.9", mcap_fcf="15.1",
                                         ev_oi_all_cash="9.2")), core_source="rebuild-assisted")
        memo = held_core(csv_row("TRW2", px="104.62", ev_oi="10.9", mcap_fcf="15.1", ev_oi_all_cash="9.1",
                                 memo_path="memos/TRW2/TRW2_2026-09-01_GSC.md"))
        root = self.build([rebuilt, memo])
        try:
            breaches, _listed, _ = r.check(root.path)
        finally:
            root.close()
        self.assertTrue(any(b.startswith("TROW: ev_oi_all_cash 9.2 does not recompute") for b in breaches), breaches)
        self.assertFalse(any(b.startswith("TRW2:") for b in breaches), breaches)

    def test_check_breach_when_ev_oi_3y_does_not_recompute(self):
        avg = {"core_oi_3y": "2050.4", "core_oi_5y": "1900", "core_fcf_3y": "1400", "core_fcf_5y": "1300",
               "mcap_fcf_3y": "15.9", "mcap_fcf_5y": "17.2", "ev_oi_3y": "11.7", "ev_oi_5y": "12.6"}
        swept = held_core(csv_row("TROW", px="104.62", px_source="SWEEP 2026-10-04", ev_oi="10.9", mcap_fcf="15.1",
                                  ev_oi_all_cash="9.0", **dict(avg, ev_oi_3y="11.6")))
        memo = held_core(csv_row("TRW2", px="104.62", ev_oi="10.9", mcap_fcf="15.1", ev_oi_all_cash="9.0",
                                 memo_path="memos/TRW2/TRW2_2026-09-01_GSC.md", **dict(avg, ev_oi_3y="11.6")))
        far = held_core(csv_row("TRW3", px="104.62", ev_oi="10.9", mcap_fcf="15.1", ev_oi_all_cash="9.0",
                                memo_path="memos/TRW3/TRW3_2026-09-01_GSC.md", **dict(avg, ev_oi_5y="13.0")))
        root = self.build([swept, memo, far])
        try:
            breaches, _listed, _ = r.check(root.path)
        finally:
            root.close()
        # Exact after a SWEEP; a memo's own print within 0.1.
        self.assertTrue(any(b.startswith("TROW: ev_oi_3y 11.6 does not recompute") for b in breaches), breaches)
        self.assertFalse(any(b.startswith("TRW2:") for b in breaches), breaches)
        self.assertTrue(any(b.startswith("TRW3: ev_oi_5y 13.0 does not recompute from the core numbers at Px 104.62 "
                                         "(12.6)") for b in breaches), breaches)

    def test_dnaf_row_multiples_are_not_recomputed(self):
        # [v4.5.3] A Gate-0 DNAF memo sets its core numbers and multiples to n.m. (MODEL 6.4), as
        # row-from-memo prints for 6383.T: core_source memo at a numeric memo Px. check() does not
        # recompute them; a non-DNAF row with a wrong multiple still breaches, and validate_row
        # still governs the DNAF row's fields.
        nm = dict((name, r.NM) for name in r.CORE_FIELDS + r.MULTIPLES + r.R10_FIELDS)
        nm.update(next_review_short=r.NM, trigger=r.NM)
        gate = csv_row("GATE", verdict="DNAF", past=r.NM, future=r.NM, sf=r.NM, px="5875", px_unit="JPY",
                       core_source="memo", memo_path="memos/GATE/GATE_2026-09-01_GSC.md", **nm)
        bad = dict(gate, key="GAT2", memo_path="memos/GAT2/GAT2_2026-09-01_GSC.md", mcap_fcf="12")
        wrong = held_core(csv_row("TRW2", px="104.62", ev_oi="10.9", mcap_fcf="15.1", ev_oi_all_cash="9.5",
                                  memo_path="memos/TRW2/TRW2_2026-09-01_GSC.md"))
        self.assertEqual(r.validate_row(gate), [])
        self.assertEqual(r.compute_metrics(gate, gate["px"], gate["px_unit"])["mcap_fcf"], r.OWED)
        # render() refuses GAT2, so _REGISTER.md renders the valid rows; check() reads register.csv.
        root = self.build([gate, bad, wrong], md=r.render([gate, wrong], "v10", "2026-10-07"))
        try:
            breaches, _listed, _ = r.check(root.path, base="HEAD")
        finally:
            root.close()
        self.assertFalse(any(b.startswith("GATE:") for b in breaches), breaches)
        self.assertFalse(any("does not recompute" in b for b in breaches if not b.startswith("TRW2:")), breaches)
        self.assertIn("GAT2: mcap_fcf: '12' is not a one-decimal multiple", breaches)
        self.assertTrue(any(b.startswith("TRW2: ev_oi_all_cash 9.5 does not recompute") for b in breaches),
                        breaches)

    def test_holding_findings_are_listed_not_breaches(self):
        parent = held_core(csv_row("PAR", holding_keys="HLD1; GONE", core_credit="12000",
                                   memo_date="2026-03-01", memo_path="memos/PAR/PAR_2026-03-01_GSC.md",
                                   px="104.62"))
        parent.update(r.compute_metrics(parent, "104.62", "USD"))
        holding = csv_row("HLD1", memo_date="2026-09-01")
        root = self.build([parent, holding])
        try:
            breaches, listed, _ = r.check(root.path, base="HEAD")
            code, out, _err = run_main(["--root", root.path, "check", "--base", "HEAD"])
        finally:
            root.close()
        self.assertEqual(breaches, [])
        self.assertTrue(any(x.startswith("PAR: parent stale - holding HLD1 memo 2026-09-01") for x in listed), listed)
        self.assertTrue(any(x.startswith("PAR: parent stale - holding GONE has no register row (group dependency)")
                            for x in listed), listed)
        # V14: a credit no longer moves with any price, so the credit-heavy review retired.
        self.assertFalse(any("credit-heavy" in x for x in listed), listed)
        self.assertEqual(code, 0, out)
        self.assertIn("LIST    PAR: parent stale", out)

    def test_holding_without_a_current_memo_is_listed(self):
        # P26: a dependency memo is current only when no more than 15 months old and
        # written under MODEL v4.5.0 or later (REVIEW priority 1c reads this LIST line).
        rows = [csv_row("PAR", holding_keys="OLDV; OLDD; OK1", memo_date="2026-09-01"),
                csv_row("OLDV", memo_date="2026-08-01", model_version="v4.4.0"),
                csv_row("OLDD", memo_date="2025-06-30", model_version="v4.5.0"),
                csv_row("OK1", memo_date="2025-07-15", model_version="v4.5.0")]
        listed = r.holding_findings(rows, "2026-10-07")
        self.assertIn("PAR: parent stale - holding OLDV memo 2026-08-01 v4.4.0 is not current (P26)", listed)
        self.assertIn("PAR: parent stale - holding OLDD memo 2025-06-30 v4.5.0 is not current (P26)", listed)
        self.assertFalse(any("holding OK1" in x for x in listed), listed)
        # Without a register date only the model version can be tested.
        undated = r.holding_findings(rows, "")
        self.assertTrue(any("holding OLDV" in x and "not current" in x for x in undated), undated)
        self.assertFalse(any("holding OLDD" in x for x in undated), undated)

    def test_base_with_the_pre_lens_header(self):
        # An outgoing register.csv with no lens columns reads at the legacy defaults.
        rows = [csv_row("AAA", model_version="v4.4.1", trigger_basis="all-cash"),
                csv_row("BBB", ev_oi="8.0", model_version="v4.4.1", trigger_basis="all-cash")]
        root = self.build(rows)
        try:
            legacy = [",".join(r.LEGACY_HEADER)] + [
                ",".join(row[n] for n in r.LEGACY_HEADER) for row in r.read_csv_text(r.csv_text(rows))[0]]
            root.write("register.csv", "\n".join(legacy) + "\n")
            root.git("add", "-A")
            root.git("commit", "-q", "-m", "pre-lens header")
            root.write("register.csv", r.csv_text(rows))
            breaches, _listed, counts = r.check(root.path, base="HEAD")
            with self.assertRaises(r.ToolError):
                r.read_csv_text("\n".join(legacy) + "\n")
        finally:
            root.close()
        self.assertEqual(breaches, [])
        self.assertEqual(counts["changed"], 0)

    def test_legacy_header_reads_with_r10_defaults(self):
        # Both older headers read in lean-2 form (a check base, a merge base, the retrigger's landing read):
        # lean-1's sotp_keys becomes holding_keys and its credits one constant; the R10 columns default.
        rows = [csv_row("AAA", model_version="v4.4.1", trigger_basis="all-cash")]
        lean1 = r.LEAN1_HEADER
        values = dict(rows[0], sotp_keys="HLD1", core_credit_fix="300", core_credit_mkt="500",
                      core_credit_px="20")
        text = ",".join(lean1) + "\n" + ",".join(values[n] for n in lean1) + "\n"
        got, problems = r.read_csv_text(text, legacy_ok=True)
        self.assertEqual(problems, [])
        self.assertEqual(list(got[0]), r.CSV_HEADER)
        self.assertEqual((got[0]["holding_keys"], got[0]["core_credit"]), ("HLD1", "800"))
        self.assertEqual({n: got[0][n] for n in r.R10_FIELDS}, r.R10_DEFAULTS)
        pre = ",".join(r.LEGACY_HEADER) + "\n" + ",".join(values[n] for n in r.LEGACY_HEADER) + "\n"
        got, _ = r.read_csv_text(pre, legacy_ok=True)
        self.assertEqual(dict(got[0]), dict(rows[0], **r.R10_DEFAULTS))
        with self.assertRaises(r.ToolError):
            r.read_csv_text(text)                       # the working register must be lean-2
        # check --base against a lean-1 base: the rows read equal, so none counts as changed.
        root = self.build(rows)
        try:
            root.write("register.csv", ",".join(lean1) + "\n" + ",".join(dict(rows[0], sotp_keys="n.m.",
                       core_credit_fix="0", core_credit_mkt="0", core_credit_px="n.m.")[n] for n in lean1) + "\n")
            root.git("add", "-A")
            root.git("commit", "-q", "-m", "lean-1 header")
            root.write("register.csv", r.csv_text(rows))
            breaches, _listed, counts = r.check(root.path, base="HEAD")
        finally:
            root.close()
        self.assertEqual(breaches, [])
        self.assertEqual(counts["changed"], 0)

    def test_legacy_outgoing_register(self):
        legacy = "| Ticker | Company |\n|---|---|\n| AAA (was AA) | A |\n| CCC | C |\n"
        rows = [csv_row("AAA")]
        root = self.build(rows, extra={})
        try:
            root.git("rm", "-q", "register.csv")
            root.write("_REGISTER.md", legacy)
            root.git("add", "-A")
            root.git("commit", "-q", "-m", "legacy")
            root.write("register.csv", r.csv_text(rows))
            root.write("_REGISTER.md", r.render(rows, "v10", "2026-10-07"))
            breaches, listed, _ = r.check(root.path, base="HEAD")
        finally:
            root.close()
        self.assertTrue(any("missing: CCC" in b for b in breaches), breaches)
        self.assertTrue(any("first lean version" in x for x in listed), listed)


class FrameworkTests(unittest.TestCase):
    def test_model_suffix_table_matches_tool(self):
        """MODEL 7.1a lists every suffix the tool knows, with the same unit."""
        with open(os.path.join(REPO, "model", "MODEL.md"), encoding="utf-8") as fh:
            text = fh.read()
        block = text.split("**Every exchange the price endpoint serves is admissible", 1)[1]
        block = block.split("\n\n**", 1)[0]
        found = {}
        import re
        for line in block.split("\n"):
            if not line.startswith("|") or "`." not in line:
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            for i in range(0, len(cells) - 2, 3):
                suffix = cells[i].strip("`")
                if suffix.startswith("."):
                    found[suffix[1:]] = re.sub(r"[^A-Za-z]", "", cells[i + 2])
        self.assertEqual(found, r.SUFFIX_UNITS)

    def test_model_names_the_tool_header_fields_and_parameters(self):
        """MODEL 7.1 prints the master header the tool renders; 6.1 lists every memo machine field and no
        retired one; section 3 carries P20 (maintenance capex) and P28 (one-off down year)."""
        import re
        with open(os.path.join(REPO, "model", "MODEL.md"), encoding="utf-8") as fh:
            text = fh.read()
        self.assertIn("| " + " | ".join(r.MASTER_COLUMNS) + " |", text)
        self.assertEqual([n for n in r.NEW_MEMO_FIELDS if not re.search(r"(?m)^%s:" % n, text)], [])
        self.assertEqual([n for n in r.RETIRED_FIELDS if re.search(r"(?m)^%s:" % n, text)], [])
        self.assertRegex(text, r"(?m)^\|P20 *\|Maintenance-capex")
        self.assertRegex(text, r"(?m)^\|P28 *\|One-off down year")

    def test_source_passes_the_routine_hook_scan(self):
        hooks = os.path.join(REPO, ".claude", "hooks")
        sys.path.insert(0, hooks)
        try:
            import gsc_guard
        finally:
            sys.path.remove(hooks)
        with open(TOOL, encoding="utf-8") as fh:
            source = fh.read()
        gsc_guard.Guard({"cwd": REPO}).check_code(source)   # raises Blocked if the hook would refuse it
        self.assertIsNone(gsc_guard.LOCKED_FRAG_RE.search(source))

    def test_metrics_prints_status_hint(self):
        root = TempRoot({"register.csv": r.csv_text([held_core(csv_row("TROW", trigger="55.5"))])})
        try:
            code, out, _err = run_main(["--root", root.path, "metrics", "TROW", "50"])
            dated, _o, _e = run_main(["--root", root.path, "metrics", "TROW", "50", "--date", "2026-10-06"])
            with self.assertRaises(SystemExit):           # round 2 retired the holding price check (V14)
                run_main(["--root", root.path, "metrics", "TROW", "50", "--holding", "HLD1=120"])
        finally:
            root.close()
        self.assertEqual((code, dated), (0, 0))
        self.assertIn("trigger 55.5 · distance -9.9% · status_hint IN RANGE", out)
        # R10: at or under the trigger but failing the strict line at Px is NEAR, with the failing primary.
        legacy = held_core(csv_row("OLD", trigger="70", trigger_basis="all-cash", model_version="v4.4.1"))
        p20 = dict(legacy, key="P20", core_fcf_basis="FY2025 CFO − maint. capex (constructed)")
        root = TempRoot({"register.csv": r.csv_text([legacy, p20])})
        try:
            code, out, _err = run_main(["--root", root.path, "metrics", "P20", "60"])
            code2, out2, _err = run_main(["--root", root.path, "metrics", "OLD", "60"])
        finally:
            root.close()
        self.assertEqual((code, code2), (0, 0))
        self.assertIn("trigger 70 · distance -14.3% · status_hint NEAR (strict line fails at PX: MCap/FCF 8.7 "
                      "(MODEL 8.3); an older all-cash trigger, re-read at the next memo (R10))", out)
        # A pre-R6 FCF basis: the MCap/FCF breach is noted, not tested (R6), so EV/OI no-cash 6.6 decides.
        self.assertIn("trigger 70 · distance -14.3% · status_hint IN RANGE (MCap/FCF 8.7 on a pre-R6 FCF basis, "
                      "not tested (MODEL 8.3, R6); an older all-cash trigger, re-read at the next memo (R10))", out2)
        rows = [held_core(csv_row("TROW", trigger="55.5", holding_keys="HLD1", core_credit="0")),
                csv_row("HLD1", px="90", trigger="100")]
        root = TempRoot({"register.csv": r.csv_text(rows)})
        try:
            code, out, _err = run_main(["--root", root.path, "sweep-scope"])
        finally:
            root.close()
        self.assertEqual(code, 0)
        self.assertTrue(out.splitlines()[0].endswith(",core_currency,holding_keys"), out)
        self.assertIn("TROW,TROW,USD,WATCH,false,100,2026-08-31,55.5,USD,HLD1", out)

    def test_metrics_prints_averaged_readings(self):
        held = held_core(csv_row("TROW", held="true", zone="HOLD", trigger="55.5", add_band="55.5", sell_line="268.6",
                                 last_zone_check="2026-10-02", avg_cost="10.00 USD", core_oi_3y="2050.4",
                                 core_oi_5y="1900", core_fcf_3y="1400", core_fcf_5y="1300"))
        root = TempRoot({"register.csv": r.csv_text([held, csv_row("NOC")])})
        try:
            code, out, _err = run_main(["--root", root.path, "metrics", "TROW", "104.62"])
            code2, out2, _err = run_main(["--root", root.path, "metrics", "NOC", "90"])
        finally:
            root.close()
        self.assertEqual((code, code2), (0, 0))
        lines = out.splitlines()
        self.assertEqual(lines[0], "TROW at 104.62 USD: MCap/FCF 15.1 · EV/OI no-cash 10.9 · EV/OI all-cash 9.0")
        self.assertEqual(lines[1], "  3y: MCap/FCF 15.9 · EV/OI 11.7 · 5y: MCap/FCF 17.2 · EV/OI 12.6")
        self.assertIn("  held: trigger = ADD band (P21, R10)", lines)
        # Every distance metrics prints is Px / line - 1 (the trigger's convention).
        self.assertIn("  distance to ADD band 55.5: +88.5%", lines)
        self.assertIn("  distance to sell line 268.6: -61.0%", lines)
        self.assertIn("  trigger 55.5 · distance +88.5% · status_hint FAR", lines)
        self.assertIn("  3y: MCap/FCF - · EV/OI - · 5y: MCap/FCF - · EV/OI -", out2)
    def test_cli_exit_codes(self):
        root = TempRoot({})
        try:
            code, _out, err = run_main(["--root", root.path, "render", "--version", "v1", "--date", "2026-10-10"])
        finally:
            root.close()
        self.assertEqual(code, 2)
        self.assertIn("register.csv not found", err)


# ------------------------------------------------------------------ one-time lean rebuild

LEGACY_REGISTER = """---
register_title: GSC Register — Master Watchlist
register_version: v41
register_date: 2026-10-05
names_total: 5
---

# GSC Register — Master Watchlist (v41 · 2026-10-05)

## Portfolio table (HELD names — §7.2)

| Ticker | Entry date(s) | Avg cost | Verdict | Zone | ADD band (P21) | Sell-flag line (P9) | Last zone check | Next review |
|--------|---------------|----------|---------|------|----------------|---------------------|-----------------|-------------|
| HHH (size redacted) | n/a | $10.00 | WATCH | **HOLD** | < ≈ $55.5 — no-cash bound | ≈ $268.6 (+157%) | 2026-10-03 @ $104.62 (2 Oct close) | Q3 |

---

## Master table

### BUY (framework) — 0 names

None.

### WATCH — 3 names, ascending by Dist %

| Ticker | Company | Memo date | Ver | Verdict | Past | Future | SF | Px @ memo | Trigger band | Dist % | Next review / notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| HHH | H Corp | 2026-09-01 | v5 | WATCH | ADEQUATE | ADEQUATE | PASS (1 flag — cap-alloc CAUTION) | $104.62 (2 Oct 2026) | CHEAP < ≈ $55.5 | +89% | Q3 |
| AAA (was AA; AAX ADR 1:1) | A Corp | 2026-09-01 | v2 | WATCH | STRONG | ADEQUATE | PASS | $100.00 (2 Oct 2026) | CHEAP ≈ $60–80 | +25% | FY |
| EEE.L | E plc | 2026-09-01 | v1 | WATCH | ADEQUATE | ADEQUATE | PASS | £19.20 (1 Sep 2026) | CHEAP ≈ £9.08–10.08 | +90% | FY |

### AVOID — 2 names, alphabetical

| Ticker | Company | Memo date | Ver | Verdict | Past | Future | SF | Px @ memo | Trigger band | Dist % | Next review / notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BBB.DE | B Corp | 2026-09-01 | v1 | AVOID (Past WEAK) | WEAK | ADEQUATE | PASS | €40.00 | n.m. | — | FY |
| CCC | C Corp | 2026-09-01 | v1 | AVOID | WEAK | WEAK | FAIL | $10.00 | n.m. | — | FY |

### DNAF — 1 names

| Ticker | Company | Memo date | Ver | Verdict | Past | Future | SF | Px @ memo | Trigger band | Dist % | Next review / notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DDD | D Corp | 2026-09-01 | v1 | DNAF (delisted) | ADEQUATE | WEAK | FAIL | $210.00 cash | n.m. | — | Terminal |

---

## Open items

- none

## Change log
- v41 — test
"""


def legacy_memo(key, company, verdict, past, future, sf, price, band, s6, f_text="", s3="", s5="",
                next_review="FY2026 results (~Feb 2027)", extra=""):
    return ("---\nticker: %s\ncompany: %s\nisin: US0000000001 (tier-2 recall)\nmemo_date: 2026-09-01\n"
            "memo_version: v1\nmodel_version: v4.4.1\nprice_at_memo: %s\nverdict: %s\nquality_past: %s\n"
            "quality_future: %s\nsf: %s\ntrigger_band: \"%s\"\nnext_review: \"%s\"\nposition: —\n%s---\n\n"
            "# %s — memo\n\n## 1. Verdict\nText.\n\n## 3. Quality — past record\n%s\n\n## 4. Quality — future\nF.\n\n"
            "## 5. Shareholder-friendliness\n%s\n\n## 6. Price\n\n| Metric | Current | Threshold |\n|---|---|---|\n%s\n\n"
            "## 7. Risks\nR.\n\n# APPENDIX\n\n## F. Valuation math\n%s\n\n## G. Change log\nG.\n"
            % (key, company, price, verdict, past, future, sf, band, next_review, extra, key, s3, s5, s6, f_text))


SWEEP_ROW = """---
row_type: SWEEP
run_date: 2026-10-04
---
## Price table

| Key | Instrument | Venue | Ccy | Close | Close date | Source |
|---|---|---|---|---|---|---|
| HHH | HHH | NYSE | USD | 104.62 | 2026-10-02 | Yahoo |
| AAA | AAA | NYSE | USD | 100.00 | 2026-10-02 | Yahoo |
| EEE.L | EEE.L | LSE | GBp | 1,759.00 (1759) | 2026-10-05 | Yahoo |
"""


def rebuild_fixture():
    memos = {
        "memos/HHH/HHH_2026-09-01_GSC.md": legacy_memo(
            "HHH", "H Corp", "WATCH", "ADEQUATE", "ADEQUATE", "PASS (1 flag — capital-allocation CAUTION)",
            "$104.62 (close 2 Oct 2026)", "CHEAP < ≈ $55.5 (MCap/FCF binds)",
            "| MCap / FCF | 15.1× | ≤ 8 |\n| EV / OI (no-cash / all-cash) | 10.9× / 9.0× | ≤ 7 |",
            f_text="Shares 213.316m; FCF 1,479.2; OI 2,188.8; debt 1,620.9; cash 4,188.3.",
            s3="Worst-of-four normalized ROCE is 23.9% on every read.",
            s5="Capital allocation CAUTION: buybacks ran at 1.7–2.0× the band.",
            next_review="Q3 2026 results 30 Oct 2026; FY2026 10-K (~Feb 2027)"),
        "memos/AAA/AAA_2026-09-01_GSC.md": legacy_memo(
            "AAA", "A Corp", "WATCH", "STRONG", "ADEQUATE", "PASS", "$95.00 (close 31 Aug 2026)",
            "CHEAP ≈ $60–80 (EV/OI no-cash/all-cash; MCap/FCF leg ≈ $70 between)",
            "| MCap/FCF | 950 ÷ 100 | **9.5×** | ≤ 8 |\n| EV/OI | 9.4× / 9.2× (no-cash / all-cash) | ≤ 7 |",
            f_text="Price $95.00 × 10m = MCap $950m. Debt 50; cash 25. FCF 100; OI 106.4.",
            s3="Worst-of-four normalized ROCE 31.2% (end-of-period, with-cash).",
            next_review="Investor day 12 Mar 2026 done; FY2026 10-K (~Jan 2027)"),
        "memos/EEE.L/EEE.L_2026-09-01_GSC.md": legacy_memo(
            "EEE.L", "E plc", "WATCH", "ADEQUATE", "ADEQUATE", "PASS", "£19.20 (1,920p LSE, 1 Sep 2026)",
            "CHEAP below ≈ £9.08 (EV/OI no-cash binds)", "| MCap/FCF | 13.8× | ≤ 8 |"),
        "memos/BBB.DE/BBB.DE_2026-09-01_GSC.md": legacy_memo(
            "BBB.DE", "B Corp", "AVOID (Past WEAK)", "WEAK", "ADEQUATE", "PASS", "40.00",
            "n.m. — FY25 OI negative; restoring OI ≈ €50m",
            "| MCap/FCF | 12.0× | ≤ 8 |\n| EV/OI | n.m. (OI −€5m) | ≤ 7 |",
            s3="Worst-of-four normalized ROCE −2.0%; operating losses in four years.", extra="currency: EUR\n"),
        "memos/CCC/CCC_2026-09-01_GSC.md": legacy_memo(
            "CCC", "C Corp", "AVOID", "WEAK", "WEAK", "FAIL", "$10.00 (5 Sep 2026)", "moot — mech. CHEAP ≈ $2–4",
            "| MCap/FCF | 30.0× | ≤ 8 |", s3="Worst-of-four normalized ROCE 4.4%."),
        "memos/DDD/DDD_2026-09-01_GSC.md": legacy_memo(
            "DDD", "D Corp", "AVOID", "ADEQUATE", "WEAK", "FAIL", "$206.41 (close 10 Jul 2026)",
            "CHEAP < ≈ $38", "| MCap/FCF | 22.5× | ≤ 8 |"),
    }
    files = {"_REGISTER.md": LEGACY_REGISTER, "queue/rows/README.md": "rows\n"}
    files.update(memos)
    root = TempRoot(files, git=True)
    root.write("queue/rows/2026-10-04_0630_SWEEP.md", SWEEP_ROW)
    root.git("add", "-A")
    root.git("commit", "-q", "-m", "sweep")
    root.git("rm", "-q", "queue/rows/2026-10-04_0630_SWEEP.md")
    root.git("commit", "-q", "-m", "intake applied the sweep")
    return root


ASSISTED = """key,field,value,quote
AAA,core_shares_diluted,10,"Price $95.00 × 10m = MCap $950m"
AAA,core_debt_eq,50,"Debt 50; cash 25"
AAA,core_cash,25,"Debt 50; cash 25"
AAA,core_fcf,100,"FCF 100; OI 106.4"
AAA,core_oi,106.4,"FCF 100; OI 106.4"
AAA,core_unit,m,-
AAA,core_currency,USD,-
AAA,core_fx,1,-
AAA,core_fx_date,n.m.,-
AAA,core_ratio,1,-
HHH,core_shares_diluted,213.316,"Shares 213.316m"
HHH,core_debt_eq,9999,"debt 1,620.9"
HHH,core_cash,4188.3,"cash 4,188.3"
HHH,core_fcf,1479.2,"FCF 1,479.2"
HHH,core_oi,2188.8,"OI 2,188.8"
HHH,core_unit,m,-
HHH,core_currency,USD,-
HHH,core_fx,1,-
HHH,core_ratio,1,-
HHH,sf_reason,buybacks,"buybacks ran at 1.7–2.0× the band"
BBB.DE,past_reason,losses,"operating losses in four years"
CCC,past_reason,leverage,"this sentence is not in the memo"
CCC,future_reason,breadth,F.
CCC,sf_reason,greed,F.
"""


class RebuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = rebuild_fixture()
        assisted = os.path.join(cls.root.path, "assisted.csv")
        with open(assisted, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(ASSISTED)
        cls.assisted = assisted
        cls.out = r.rebuild(cls.root.path, "HEAD", assisted, None, "2026-10-06")
        cls.rows = {row["key"]: row for row in cls.out[4]}

    @classmethod
    def tearDownClass(cls):
        cls.root.close()

    def test_sections_split_and_held(self):
        rows = self.rows
        self.assertEqual([rows[k]["section"] for k in ("HHH", "AAA", "EEE.L", "BBB.DE", "CCC", "DDD")],
                         ["WATCH", "WATCH", "WATCH", "AVOID-1", "AVOID-2", "DNAF"])
        self.assertEqual(rows["HHH"]["held"], "true")
        self.assertEqual((rows["HHH"]["zone"], rows["HHH"]["add_band"], rows["HHH"]["sell_line"],
                          rows["HHH"]["last_zone_check"], rows["HHH"]["avg_cost"]),
                         ("HOLD", "55.5", "268.6", "2026-10-02", "10.00 USD"))
        md = self.out[1]
        self.assertIn("register_version: v42", md)
        self.assertIn('verdict_split: "BUY 0 · WATCH 3 · AVOID 2 (one gate 1 · two+ 1) · DNAF 1"', md)

    def test_register_held_dnaf_is_kept_and_reported(self):
        self.assertEqual(self.rows["DDD"]["verdict"], "DNAF")
        self.assertEqual(self.rows["DDD"]["trigger"], r.NM)
        self.assertEqual(self.rows["DDD"]["mcap_fcf"], r.NM)
        self.assertIn("DDD: the register made the row DNAF after its memo", self.out[2])

    def test_prices_from_the_applied_sweep_and_memo(self):
        aaa, eee, bbb = self.rows["AAA"], self.rows["EEE.L"], self.rows["BBB.DE"]
        self.assertEqual((aaa["px"], aaa["px_unit"], aaa["px_date"], aaa["px_source"]),
                         ("100", "USD", "2026-10-02", "SWEEP 2026-10-04"))
        # The register cell does not show the sweep date: the memo price stands, GBP -> GBp.
        self.assertEqual((eee["px"], eee["px_unit"], eee["px_source"]), ("1920", "GBp", "memo"))
        self.assertEqual((bbb["px"], bbb["px_unit"], bbb["px_date"]), ("40", "EUR", r.OWED))

    def test_aliases_isin_version_and_next_review(self):
        aaa = self.rows["AAA"]
        self.assertEqual(aaa["aliases"], "AA; AAX ADR 1:1")
        self.assertEqual(aaa["isin"], "US0000000001")
        self.assertEqual(aaa["memo_version"], "v1")
        self.assertEqual(aaa["next_review_short"], "Jan 2027")      # a past date the text mentions is skipped
        self.assertEqual(self.rows["DDD"]["next_review_short"], r.NM)

    def test_triggers(self):
        self.assertEqual(self.rows["AAA"]["trigger"], "70")          # C6: the FCF leg inside the pair caps it
        self.assertEqual(self.rows["EEE.L"]["trigger"], "908")       # £9.08 -> GBp
        self.assertEqual(self.rows["BBB.DE"]["trigger"], r.NM)
        self.assertEqual(self.rows["CCC"]["trigger"], "4")
        self.assertEqual(self.rows["HHH"]["trigger"], "55.5")

    def test_core_numbers_validated_against_the_memo(self):
        aaa = self.rows["AAA"]
        self.assertEqual(aaa["core_source"], "rebuild-assisted")
        # Recomputed at the SWEEP Px 100 from the accepted core numbers.
        self.assertEqual((aaa["mcap_fcf"], aaa["ev_oi"], aaa["ev_oi_all_cash"]), ("10.0", "9.9", "9.6"))
        hhh = self.rows["HHH"]
        # A wrong debt figure breaks both EV/OI readings: only MCap/FCF reproduces, so nothing stands.
        self.assertEqual(hhh["core_source"], r.OWED)
        self.assertEqual(hhh["mcap_fcf"], r.OWED)
        self.assertIn("HHH: rejected", self.out[2])

    def test_printed_multiples_when_px_is_the_memo_price(self):
        bbb = self.rows["BBB.DE"]
        self.assertEqual((bbb["mcap_fcf"], bbb["ev_oi"], bbb["ev_oi_all_cash"]), ("12.0", r.NM, r.NM))
        self.assertEqual(self.rows["EEE.L"]["mcap_fcf"], "13.8")

    def test_reasons(self):
        self.assertEqual(self.rows["HHH"]["past_reason"], "23.9% ROCE")
        self.assertEqual(self.rows["HHH"]["sf_reason"], "buybacks")
        self.assertEqual(self.rows["AAA"]["past_reason"], "31.2% ROCE")
        self.assertEqual(self.rows["AAA"]["future_reason"], r.NM)
        self.assertEqual(self.rows["AAA"]["sf_reason"], r.NM)
        self.assertEqual(self.rows["BBB.DE"]["past_reason"], "losses")
        self.assertEqual(self.rows["CCC"]["past_reason"], r.OWED)    # quote not in the memo
        self.assertEqual(self.rows["CCC"]["future_reason"], "breadth")
        self.assertEqual(self.rows["CCC"]["sf_reason"], r.OWED)      # not in the vocabulary
        report = self.out[2]
        self.assertIn("CCC past_reason quote not found", report)
        self.assertIn("CCC sf_reason 'greed': not in the section 7.1 vocabulary", report)

    def test_outputs_render_check_and_determinism(self):
        csv_out, md_out, report, backfill, _rows = self.out
        again = r.rebuild(self.root.path, "HEAD", self.assisted, None, "2026-10-06")
        self.assertEqual(again[:4], self.out[:4])
        self.assertTrue(csv_out.startswith(",".join(r.CSV_HEADER) + "\n"))
        self.assertNotIn("\r", csv_out + md_out + report + backfill)
        self.assertIn("```csv\nkey,field,value,quote\n", report)
        self.assertIn("- `HHH` — backfill: core numbers", backfill)
        self.root.write("register.csv", csv_out)
        self.root.write("_REGISTER.md", md_out)
        breaches, listed, counts = r.check(self.root.path, base="HEAD")
        self.assertEqual(breaches, [])
        self.assertEqual(counts["names_total"], 6)
        self.root.git("checkout", "-q", "--", "_REGISTER.md")

    def test_report_reads_its_own_appendix(self):
        report_path = os.path.join(self.root.path, "report.md")
        with open(report_path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(self.out[2])
        again = r.rebuild(self.root.path, "HEAD", report_path, None, "2026-10-06")
        self.assertEqual(again[0], self.out[0])


class RebuildParserTests(unittest.TestCase):
    def test_operative_trigger(self):
        cases = [
            ("CHEAP < ≈ $94–98 (EV/OI 7× ex-imp FY25 OI; P12 edge ≈$110)", "X", ("98", "USD")),
            ("CHEAP < ≈ €151 no-cash / ≈ €176 all-cash (EV/OI binding)", "X.PA", ("176", "EUR")),
            ("CHEAP ≈ €3.54 (no-cash) – €4.66 (all-cash) (EV/OI binds)", "X.MI", ("4.66", "EUR")),
            ("CHEAP ≈ SEK 54.2–63.7 A (EV/OI no-cash/all-cash; MCap/FCF leg SEK 60.3 A between)", "X-A.ST",
             ("60.3", "SEK")),
            ("CHEAP ≈ SEK 38.4–41.4 B / 43.5–46.9 A (EV/OI; MCap/FCF leg SEK 49.8 B)", "X-B.ST", ("41.4", "SEK")),
            ("CHEAP ≈ HKD 142–192 (EV/OI; strict-FCF leg ≈ HKD 168)", "X.HK", ("192", "HKD")),
            ("CHEAP < ≈ 377–496p (EV/OI nc/ac bind)", "X.L", ("496", "GBp")),
            ("No usable CHEAP trigger; operative gauge is P/B — ≈ ≤1.2× book ≈ $400", "X", ("400", "USD")),
            ("NI-proxy anchor: CHEAP < ≈ $4.75 (8× FY2025 NI)", "X", ("4.75", "USD")),
            ("CHEAP = EUR 38.80-66.51 (EV/OI 7x; MCap/FCF leg EUR 109.69)", "X.PA", ("66.51", "EUR")),
        ]
        for band, key, (value, unit) in cases:
            got_value, got_unit, _how = r.operative_trigger(band, key, None)
            self.assertEqual((r.plain(got_value), got_unit), (value, unit), band)
        for band in ("n.m. — FY25 OI −€347m; backvalued band ≈ €52", "CHEAP n.m. — EV/OI no-cash leg n.m.",
                     "Unattainable — EV/OI no-cash bound negative", "n.m. — NI-proxy anchor; no positive price"):
            self.assertEqual(r.operative_trigger(band, "X", None)[2], "n.m.", band)

    def test_memo_multiples(self):
        text = ("## 6. Price\n\n| Metric | Current | Threshold |\n|---|---|---|\n"
                "| MCap/FCF (maintenance, P20) | 22.3× | ≤ 8 |\n| MCap/FCF (all-capex, strict) | 35.8× | ≤ 8 |\n"
                "| EV/OI (consv) | 18.0× | ≤ 7 |\n| EV/OI (no-cash) | 19.3× | ≤ 7 |\n\n## 7. Risks\n")
        self.assertEqual(r.memo_multiples(text), {"mcap_fcf": "35.8", "ev_oi": "19.3", "ev_oi_all_cash": "18.0"})
        text = ("## 6. Price\n\n| Metric | Calc | Value |\n|---|---|---|\n| MCap/FCF | 446,922 ÷ 15,382 | **29.1×** |\n"
                "| EV/OI | n.m. (OI −€5m) | — |\n\n## 7. Risks\n")
        self.assertEqual(r.memo_multiples(text), {"mcap_fcf": "29.1", "ev_oi": r.NM, "ev_oi_all_cash": r.NM})

    def test_memo_price(self):
        self.assertEqual(r.parse_memo_price("CAD $78.60 (TSX, 14 Jul 2026)", "ENB.TO")[:3],
                         (r.dec("78.60"), "CAD", "2026-07-14"))
        value, unit, day, how = r.parse_memo_price("€53.53 (UNA 14 Jul 2026); ULVR £45.64; UL $61.16", "ULVR.L")
        self.assertEqual((value, unit, day), (r.dec("45.64"), "GBP", "2026-07-14"))
        self.assertIn("later", how)
        self.assertEqual(r.parse_memo_price("39.20", "FIE.DE", "EUR")[:2], (r.dec("39.20"), "EUR"))
        self.assertIsNone(r.parse_memo_price("n/a — delisted", "X")[0])
        self.assertEqual(r.to_quote_unit(r.dec("19.205"), "GBP", "GBp")[0], r.dec("1920.500"))
        self.assertIsNone(r.to_quote_unit(r.dec("1"), "EUR", "SEK")[0])

    def test_ticker_aliases(self):
        self.assertEqual(r.ticker_aliases("SDZ.SW", "SDZ.SW (SDZNY ADR 1:1; was SDZ)"), "SDZNY ADR 1:1; SDZ")
        self.assertEqual(r.ticker_aliases("1211.HK", "1211.HK (1211.HK / 002594.SZ; was BYD)"), "002594.SZ; BYD")
        self.assertEqual(r.ticker_aliases("CROX", "CROX"), r.NM)
        # Venue words and bare ratios are not aliases (decision 9).
        self.assertEqual(r.ticker_aliases("ROG.SW", "ROG.SW (SIX; RO bearer; RHHBY 8:1; ROG)"),
                         "RO bearer; RHHBY 8:1; ROG")
        self.assertEqual(r.ticker_aliases("NVS", "NVS (NOVN SIX; ADR 1:1)"), "NOVN")
        self.assertEqual(r.ticker_aliases("LISN.SW", "LISN.SW (SIX; PS LISP; ~10:1; LISN)"), "PS LISP; LISN")
        self.assertEqual(r.ticker_aliases("CSU.TO", "CSU.TO (TSX)"), r.NM)

    def test_company_note(self):
        self.assertEqual(r.company_note("Ambev S.A. (ADR; B3: ABEV3)"), ("Ambev S.A.", "ADR; B3: ABEV3"))
        self.assertEqual(r.company_note("Arq, Inc. (formerly Advanced Emissions Solutions, Inc.)"),
                         ("Arq, Inc.", "formerly Advanced Emissions Solutions, Inc."))
        self.assertEqual(r.company_note("ROCKWOOL A/S (B shares)"), ("ROCKWOOL A/S", "B shares"))
        for name in ("Essity Aktiebolag (publ)", "Keyence Corporation (株式会社キーエンス)", "T. Rowe Price Group, Inc."):
            self.assertEqual(r.company_note(name), (name, None))
        notes = []
        row = r.row_from_memo("memos/TROW/TROW_2026-10-03_GSC.md",
                              memo_text(TROW_FM, company="T. Rowe Price Group, Inc. (NYSE ADR 1:1)"), notes)
        self.assertEqual(row["company"], "T. Rowe Price Group, Inc.")
        self.assertTrue(any(n.startswith("NORMALISED TROW company") for n in notes), notes)
        _fails, warns = r.lint_memo("memos/TROW/TROW_2026-10-03_GSC.md",
                                    memo_text(TROW_FM, company="T. Rowe Price Group, Inc. (formerly X Corp)"))
        self.assertTrue(any(w.startswith("company carries the note") for w in warns), warns)


class TraceTests(unittest.TestCase):
    """Decision 9: an assisted number must follow from its own memo quote."""

    def test_traced_and_untraced(self):
        krn = ("bank debt 1,266 + other financial and lease liabilities 187,093 (52,982 current + 134,111 "
               "non-current, treated whole as debt-equivalent) + NCI 309")
        self.assertEqual(r.trace_value("188668", krn), "sum of 3")
        self.assertIsNone(r.trace_value("182741.8", krn))                 # the review's KRN.DE value
        self.assertEqual(r.trace_value("417053", "3,682,862 ÷ 417,053"), "quoted")
        self.assertEqual(r.trace_value("31.593072", "on 31,593.072k diluted shares"), "scaled")
        self.assertEqual(r.trace_value("1.09649", "Price HKD 461.60 → RMB 421.0 at 0.912 (assumption)"),
                         "quotient")                                       # an inverse FX rate
        self.assertEqual(r.trace_value("5345.82", "MCap SEK 940,063m", extra=(175.85,)), "quotient")
        self.assertEqual(r.trace_value("2925", "EV/OI nc (20,475 − 9,051 − 153)/2,990 = 377p"), "quotient")
        self.assertEqual(r.trace_value("-47.2", "MCap/FCF n.m. (FCF −47.2m)"), "quoted")
        self.assertIsNone(r.trace_value("489266.2", "7 × 18,897 − 19,833 − 9) / 880 = $127.8"))

    def test_rebuild_rejects_untraced_and_noisy_values(self):
        root = rebuild_fixture()
        try:
            assisted = os.path.join(root.path, "assisted.csv")
            with open(assisted, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(ASSISTED.replace("AAA,core_cash,25,", "AAA,core_cash,25.00000000001,"))
            out = r.rebuild(root.path, "HEAD", assisted, None, "2026-10-06")
            report = out[2]
            self.assertIn("HHH core_debt_eq '9999': not a number of its quote", report)
            self.assertIn("AAA core_cash '25.00000000001': more than 6 decimal places", report)
            self.assertIn("Assisted numbers traced to their memo quote: quoted", report)
            rows = {x["key"]: x for x in out[4]}
            self.assertEqual(rows["AAA"]["core_cash"], r.OWED)
        finally:
            root.close()

    def test_validate_row_rejects_float_noise(self):
        row = dict(held_core(csv_row("TROW")), core_debt_eq="1620.8999999999999")
        self.assertTrue(any("more than 6 decimal places" in p for p in r.validate_row(row)))
        self.assertEqual(r.validate_row(held_core(csv_row("TROW"))), [])

    def test_single_unlabelled_ev_oi_read_as_all_cash(self):
        # ROK: the memo prints one EV/OI (33.8) on EV net of cash; the no-cash
        # reading is 34.1 (within 5%), the all-cash one 33.8.
        core = {"core_unit": "m", "core_currency": "USD", "core_shares_diluted": "113.1", "core_debt_eq": "3704",
                "core_cash": "468", "core_oi": "1703", "core_fcf": "1358", "core_fx": "1", "core_ratio": "1",
                "core_period": "FY2025", "core_oi_basis": "-", "core_fcf_basis": "-", "core_fx_date": "n.m."}
        printed = {"mcap_fcf": "40.0", "ev_oi": "33.8", "ev_oi_all_cash": "-", "_ev_single": True}
        accepted, how = r.validate_core(core, r.dec("480.08"), "USD", printed)
        self.assertEqual((accepted["core_debt_eq"], accepted["core_cash"]), ("3704", "468"), how)
        self.assertIn("all-cash reading", how)


class LegacyApplyTests(unittest.TestCase):
    """INTAKE applies a row whose memo predates the v4.5.0 machine fields."""

    def setUp(self):
        legacy = legacy_memo(
            "AAA", "A Corp", "AVOID", "ADEQUATE", "ADEQUATE", "FAIL", "$95.00 (close 31 Aug 2026)",
            "CHEAP ≈ $60–80 (EV/OI no-cash/all-cash; MCap/FCF leg ≈ $70 between)",
            "| MCap/FCF | 950 ÷ 100 | **9.5×** | ≤ 8 |\n| EV/OI | 9.4× / 9.2× (no-cash / all-cash) | ≤ 7 |",
            s3="Worst-of-four normalized ROCE 31.2% (end-of-period, with-cash).",
            next_review="FY2026 10-K (~Jan 2027)")
        old = csv_row("AAA", aliases="AA", px_unit="USD", memo_path="memos/AAA/AAA_2026-08-01_GSC.md",
                      memo_date="2026-08-01")
        self.root = TempRoot({
            "register.csv": r.csv_text([old, csv_row("SPX", px_unit=r.OWED, px=r.OWED, px_date=r.OWED,
                                                     verdict="AVOID", past="WEAK", ev_oi=r.OWED, mcap_fcf=r.OWED)]),
            "memos/AAA/AAA_2026-09-01_GSC.md": legacy,
            "memos/NEW.L/NEW.L_2026-09-01_GSC.md": legacy.replace("ticker: AAA", "ticker: NEW.L").replace(
                "$95.00 (close 31 Aug 2026)", "£19.20 (1,920p LSE, 1 Sep 2026)").replace(
                "CHEAP ≈ $60–80 (EV/OI no-cash/all-cash; MCap/FCF leg ≈ $70 between)", "CHEAP below ≈ £9.08"),
        })
        self.root.write("queue/rows/2026-10-05_0610_REVIEW_AAA.md",
                        "---\nrow_type: REVIEW\nmemo_path: memos/AAA/AAA_2026-09-01_GSC.md\nrun_date: 2026-10-05\n---\n")
        self.root.write("queue/rows/2026-10-05_2130_ANALYSE_NEW.L.md",
                        "---\nrow_type: ANALYSE\nmemo_path: memos/NEW.L/NEW.L_2026-09-01_GSC.md\nrun_date: "
                        "2026-10-05\n---\n")

    def tearDown(self):
        self.root.close()

    def test_review_row_from_a_legacy_memo(self):
        report = r.apply_row(self.root.path, "queue/rows/2026-10-05_0610_REVIEW_AAA.md")
        aaa = {x["key"]: x for x in r.load_csv(self.root.path)[0]}["AAA"]
        self.assertEqual((aaa["px"], aaa["px_unit"], aaa["px_date"], aaa["px_source"]),
                         ("95", "USD", "2026-08-31", "memo"))
        self.assertEqual(aaa["trigger"], "70")
        self.assertEqual((aaa["mcap_fcf"], aaa["ev_oi"], aaa["ev_oi_all_cash"]), ("9.5", "9.4", "9.2"))
        self.assertEqual((aaa["next_review_short"], aaa["past_reason"], aaa["future_reason"]),
                         ("Jan 2027", "31.2% ROCE", r.NM))
        self.assertEqual((aaa["aliases"], aaa["isin"]), ("AA", "US0000000001"))
        self.assertEqual(aaa["sf_reason"], r.OWED)                         # a FAIL reason is never guessed
        notes = report["notes"]
        self.assertTrue(any(n.startswith("LEGACY AAA") for n in notes), notes)
        self.assertNotIn("BACKFILL AAA px", notes)
        self.assertIn("BACKFILL AAA sf_reason", notes)
        self.assertEqual(r.validate_row(aaa), [])

    def test_analyse_row_of_a_new_key_takes_the_suffix_unit(self):
        r.apply_row(self.root.path, "queue/rows/2026-10-05_2130_ANALYSE_NEW.L.md")
        new = {x["key"]: x for x in r.load_csv(self.root.path)[0]}["NEW.L"]
        self.assertEqual((new["px"], new["px_unit"], new["trigger"]), ("1920", "GBp", "908"))

    def test_sweep_adopts_the_endpoint_unit_of_a_row_without_one(self):
        self.root.write("queue/rows/2026-10-10_0630_SWEEP.md", "\n".join([
            "---", "row_type: SWEEP", "run_date: 2026-10-10", "---", "## Price/ordering refresh",
            "| Key | Px | Px unit | Close date | Source |", "|---|---|---|---|---|",
            "| SPX | 1234 | GBp | 2026-10-09 | endpoint |", ""]))
        report = r.apply_row(self.root.path, "queue/rows/2026-10-10_0630_SWEEP.md")
        spx = {x["key"]: x for x in r.load_csv(self.root.path)[0]}["SPX"]
        self.assertEqual((spx["px"], spx["px_unit"], spx["px_date"]), ("1234", "GBp", "2026-10-09"))
        self.assertIn("endpoint currency GBp adopted", report["changes"][0]["note"])

    def test_backfill_names_a_watch_row_the_sweep_did_not_price(self):
        row = csv_row("ROG.SW", px="327.3", px_unit="CHF", px_source="memo")
        self.assertIn("Px on the key's line (the last SWEEP did not price it)", r.backfill_items(row))
        row["px_source"] = "SWEEP 2026-10-05"
        self.assertNotIn("Px on the key's line (the last SWEEP did not price it)", r.backfill_items(row))


class NoCashParserTests(unittest.TestCase):
    """R10: the no-cash bound a memo's trigger_band prints (one-time retrigger; lint-memo warning)."""

    def test_labelled_figures(self):
        cases = [
            ("CHEAP ≈ €39.7–51.6 (EV/OI no-cash/all-cash, FY25 OI; MCap/FCF leg ≈ €56.7 non-binding)", "X.PA",
             ("39.7", "EUR")),
            ("CHEAP < ≈ €151 no-cash / ≈ €176 all-cash (EV/OI binding; MCap/FCF leg ≈ €231; no P12 edge)", "X.PA",
             ("151", "EUR")),
            ("CHEAP ≈ €3.54 (no-cash) – €4.66 (all-cash) (EV/OI binds; MCap/FCF leg ≈ €6.92)", "X.MI", ("3.54", "EUR")),
            ("CHEAP < ≈ ¥1,403 (MCap/FCF 8×, P20 maintenance-capex basis, FY3/26; both EV variants — FCF leg binds; "
             "EV/OI legs ≈ ¥2,342–3,344 no-cash/all-cash; strict all-capex FCF leg ≈ ¥244)", "6626.T", ("1403", "JPY")),
            ("CHEAP < ≈ €17.9 (MCap/FCF binds; EV/OI legs €19.5 no-cash / €23.9 all-cash; no P12)", "X.HE",
             ("17.9", "EUR")),
            ("CHEAP ≈ SEK 124 (binding: MCap/FCF, maintenance basis; EV/OI legs ≈ SEK 128 no-cash / 138 all-cash; "
             "strict all-capex ≈ SEK 99; no P12)", "X-B.ST", ("124", "SEK")),
            ("CHEAP < ≈ 377–496p (EV/OI no-cash/all-cash bind; MCap/FCF leg 662p above); no P12", "X.L", ("377", "GBp")),
            ("CHEAP ≈ $65.24–89.51 (EV/OI no-cash/all-cash, FY25 OI; MCap/FCF leg $83.00 between)", "X",
             ("65.24", "USD")),
            ("CHEAP ≈ $60–80 (EV/OI no-cash/all-cash; MCap/FCF leg ≈ $55)", "X", ("55", "USD")),
            ("CHEAP < ≈ DKK 34.5–35.3 (EV/OI no-cash / MCap-FCF all-cash; FY25 reported OI)", "X-B.CO", ("34.5", "DKK")),
            ("CHEAP < ≈ $152 (EV/OI no-cash binds; MCap/FCF leg ≈ $153 caps the all-cash reading; EV/OI all-cash "
             "leg ≈ $183; P12 edge ≈ $153)", "X", ("152", "USD")),
            ("CHEAP ≈ €48.6 (EV/OI no-excess-cash variant binds; EV/OI cash-deducted ≈ €55.6; MCap/FCF ≈ €56.3)",
             "X.DE", ("48.6", "EUR")),
            ("CHEAP < ≈ $55.5 (MCap/FCF binds both EV variants; EV/OI legs $64.2 no-cash / $83.9 all-cash; no P12)",
             "X", ("55.5", "USD")),
            ("CHEAP < ≈ PLN 4.98 (MCap/FCF binds both variants — all-capex FCF suppressed by the build-out; EV/OI "
             "legs PLN 14.09/15.07 no-cash/all-cash are context; no P12)", "X.WA", ("4.98", "PLN")),
            ("CHEAP ≈ SEK 54.2–63.7 A (EV/OI no-cash/all-cash); MCap/FCF leg ≈ SEK 60.3 A sits between", "X-A.ST",
             ("54.2", "SEK")),
            ("CHEAP < ≈ $88 (MCap/FCF binds; EV/OI legs ≈ $90–98 no-cash/all-cash; P12 edge ≈ $80 no-cash)", "X",
             ("88", "USD")),
            # One figure in two currencies is not a pair.
            ("CHEAP below ≈ HKD 14.8 / EUR 1.66 (binding: EV/OI, conservative no-cash-credit EV; MCap/FCF leg ≈ "
             "HKD 29.1)", "X.HK", ("14.8", "HKD")),
            ("CHEAP ≈ $141.0–175.4 (FCF leg $140.95 and EV/OI no-cash $141.07 effectively coincide; EV/OI all-cash "
             "$175.43; P12 edge $175.4)", "X", ("140.95", "USD")),
        ]
        for band, key, (value, unit) in cases:
            got_value, got_unit, how = r.no_cash_figure(band, key, None)
            self.assertEqual((r.plain(got_value) if got_value is not None else None, got_unit), (value, unit),
                             (band, how))

    def test_alternative_rendering_in_the_quote_unit(self):
        band = "CHEAP < ≈ ₸38,604–39,971 ≈ $84.86–87.87 (no-cash EV/OI 7× · all-cash MCap/FCF 8×; converge 3.5%)"
        value, unit, _how = r.no_cash_figure(band, "KSPX", None, "USD")
        self.assertEqual((r.plain(value), unit), ("84.86", "USD"))

    def test_unlabelled_bands_are_not_read(self):
        # 'Conservative EV' is no label (memos use it for either variant); an unlabelled EV/OI leg proves nothing.
        for band in ("CHEAP below ≈ €36 (binding: EV/OI on FY25 adj-EBIT, conservative EV; MCap/FCF leg ≈ €38; "
                     "reported-OI leg n.m.)",
                     "CHEAP ≈ CHF 103 (MCap/FCF binds; EV/OI leg ≈ CHF 123; no P12 — Past ADEQUATE)",
                     "CHEAP ≈ $67–75 (EV/OI conservative/all-cash, FY2025 basis; MCap/FCF leg ≈ $97)",
                     "CHEAP < ≈ $94.4–97.9 (EV/OI 7× ex-imp FY25 OI, converging 3.8%; FCF leg $110.0)",
                     "n.m. — FY25 OI negative; restoring OI ≈ €50m"):
            value, _unit, how = r.no_cash_figure(band, "X", None)
            self.assertIsNone(value, (band, how))


RT_DATE = "2026-10-07"


def retrigger_fixture(extra_rows=(), extra_files=None):
    """A lean-1 register (the landing read) with one row per retrigger path, its memos and _REGISTER.md v309."""
    def legacy(key, trigger, band, **over):
        row = csv_row(key, trigger=trigger, model_version="v4.4.1", trigger_basis="all-cash", **over)
        return row, "---\nticker: %s\nmodel_version: v4.4.1\ntrigger_band: \"%s\"\n---\n\n# %s\n" % (key, band, key)

    core = {"core_period": "FY2025", "core_currency": "USD", "core_unit": "m", "core_shares_diluted": "100",
            "core_debt_eq": "0", "core_cash": "0", "core_oi": "100", "core_oi_basis": "FY2025 reported",
            "core_fcf": "100", "core_fcf_basis": "FY2025 CFO - capex", "core_fx": "1", "core_fx_date": "n.m.",
            "core_ratio": "1", "core_source": "memo"}
    specs = [
        legacy("HLD", "97.9", "CHEAP < ≈ $94.4–97.9 (EV/OI 7× ex-imp FY25 OI, no-cash/all-cash)", held="true",
               zone="HOLD", add_band="94", sell_line="431", last_zone_check="2026-10-02", avg_cost="10.00 USD"),
        legacy("PAIR", "80", "CHEAP ≈ $60–80 (EV/OI no-cash/all-cash; MCap/FCF leg ≈ $90)"),
        legacy("FCFB", "55.5", "CHEAP < ≈ $55.5 (MCap/FCF binds both EV variants; EV/OI legs $64.2 no-cash / $83.9 "
                               "all-cash)"),
        legacy("CONX.DE", "36", "CHEAP below ≈ €36 (binding: EV/OI on FY25 adj-EBIT, conservative EV; MCap/FCF leg "
                                "≈ €38; reported-OI leg n.m.)", px_unit="EUR", verdict="AVOID", past="WEAK"),
        legacy("ASST.DE", "19.44", "CHEAP below ≈ €19.44 (binding: EV/OI, conservative EV; MCap/FCF leg ≈ €33.25)",
               px_unit="EUR"),
        legacy("CORE", "80", "CHEAP ≈ $60–80 (EV/OI no-cash/all-cash)", **core),
        legacy("GBX.L", "908", "CHEAP below ≈ £9.08 (binding: EV/OI, conservative no-cash EV; MCap/FCF leg ≈ £11.10)",
               px_unit="GBp"),
        legacy("NMT", r.NM, "n.m. — FY25 OI negative", verdict="AVOID", past="WEAK", future="WEAK"),
        legacy("OWD", r.OWED, "CHEAP ≈ $1–2 (EV/OI no-cash/all-cash)"),
    ] + list(extra_rows)
    rows = [row for row, _memo in specs]
    lean1 = r.LEAN1_HEADER
    lines = [",".join(lean1)]
    for row in rows:
        values = dict(row, sotp_keys=r.NM, core_credit_fix="0", core_credit_mkt="0", core_credit_px=r.NM)
        buf = io.StringIO(newline="")
        import csv as _csv
        _csv.writer(buf, lineterminator="").writerow([values[n] for n in lean1])
        lines.append(buf.getvalue())
    files = {"register.csv": "\n".join(lines) + "\n",
             "_REGISTER.md": "---\nregister_version: v309\nregister_date: 2026-10-07\n---\n\n# Register\n"}
    for row, memo in specs:
        files[row["memo_path"]] = memo
    files.update(extra_files or {})
    return TempRoot(files)


RT_ASSISTED = """key,field,value,quote
ASST.DE,trigger,19.44,"CHEAP below ≈ €19.44 (binding: EV/OI, conservative EV"
CONX.DE,trigger,36,"this sentence is not in the memo"
HLD,trigger,90,"CHEAP < ≈ $94.4–97.9"
"""


class RetriggerTests(unittest.TestCase):
    def run_pass(self, assisted=None):
        root = retrigger_fixture()
        try:
            path = None
            if assisted:
                path = os.path.join(root.path, "assisted.csv")
                with open(path, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(assisted)
            rows, report, block, report_path = r.retrigger(root.path, RT_DATE, assisted_path=path)
        finally:
            root.close()
        return {row["key"]: row for row in rows}, report, block, report_path

    def test_retrigger(self):
        rows, report, block, path = self.run_pass(RT_ASSISTED)
        got = {k: (rows[k]["trigger"], rows[k]["trigger_basis"]) for k in rows}
        self.assertEqual(got, {
            "HLD": ("94", "no-cash"),            # held: the ADD band (P21)
            "PAIR": ("60", "no-cash"),           # a labelled pair's lower bound
            "FCFB": ("55.5", "no-cash"),         # the FCF leg binds both variants: same figure, now no-cash
            "CONX.DE": ("36", "all-cash"),       # 'conservative EV' on adj-EBIT: listed, never guessed
            "ASST.DE": ("19.44", "no-cash"),     # assisted with a verbatim quote
            "CORE": ("80", "all-cash"),          # the core numbers reject 60 (EV/OI no-cash 60.0 there)
            "GBX.L": ("908", "no-cash"),         # £9.08 in GBp
            "NMT": (r.NM, "no-cash"),            # n.m. under both readings
            "OWD": (r.OWED, "all-cash"),         # nothing to re-read
        })
        self.assertTrue(path.replace("\\", "/").endswith("archive/registers/2026/RETRIGGER_v309-to-v310_2026-10-07.md"))
        self.assertIn("| Resolved | 5 (memo 3 · held ADD band 1 · assisted 1) |", report)
        self.assertIn("| Unresolved: kept all-cash, listed | 2 |", report)
        self.assertIn("| HLD | WATCH · held | 97.9 | 94 | -4.0% | held: the ADD band (P21) |", report)
        self.assertIn("CONX.DE | AVOID-1 | 36 | no figure labelled no-cash", report)
        self.assertIn("CORE | WATCH | 80 | rejected by the core numbers at 60 (MCap/FCF 60.0 · EV/OI no-cash 60.0;",
                      report)
        self.assertIn("line 3: CONX.DE trigger quote not found", report)
        self.assertIn("line 4: HLD is held with an ADD band, which is its trigger (P21)", report)
        self.assertIn("## ▶ Backfill owed — retrigger v310 (2026-10-07)", block)
        self.assertIn("- `CORE` — trigger 80 (all-cash): rejected by the core numbers", block)
        self.assertIn("- `CONX.DE` — trigger 36 (all-cash): no figure labelled no-cash", block)
        self.assertIn("```markdown\n" + block.rstrip("\n") + "\n```", report)
        for row in rows.values():
            self.assertEqual(r.validate_row(row), [], row["key"])

    def test_retrigger_is_deterministic_and_the_cli_writes_once(self):
        first = self.run_pass(RT_ASSISTED)
        self.assertEqual(self.run_pass(RT_ASSISTED)[1:3], first[1:3])
        root = retrigger_fixture()
        try:
            block = os.path.join(root.path, "block.md")
            code, out, err = run_main(["--root", root.path, "retrigger", "--date", RT_DATE, "--block", block])
            self.assertEqual(code, 0, err)
            self.assertIn("register.csv written (lean-2 (MODEL v4.5.0))", out)
            text = root.read("register.csv")
            self.assertTrue(text.startswith(",".join(r.CSV_HEADER) + "\n"))
            self.assertEqual(r.read_csv_text(text)[1], [])
            report = root.read("archive/registers/2026/RETRIGGER_v309-to-v310_2026-10-07.md")
            self.assertIn("| Resolved | 4 (memo 3 · held ADD band 1 · assisted 0) |", report)
            self.assertTrue(root.read("block.md").startswith("## ▶ Backfill owed — retrigger v310"))
            code, _out, err = run_main(["--root", root.path, "retrigger", "--date", RT_DATE])
            self.assertEqual(code, 2)
            self.assertIn("append-only", err)
            code, _out, err = run_main(["--root", root.path, "retrigger", "--date", "7 Oct"])
            self.assertEqual(code, 2)
        finally:
            root.close()

    def test_a_no_cash_bound_printed_nm(self):
        # Review fix (2026-10-07): BABA's band prints the EV/OI no-cash leg as n.m. ("EV/OI n.m./$21.7
        # (no-cash/all-cash"), so no positive price passes the strict line: the trigger is n.m., no-cash.
        band = ("CHEAP < ≈ $14.4 (MCap/FCF P20 maintenance basis binds); EV/OI n.m./$21.7 (no-cash/all-cash, FY26 OI); "
                "strict all-capex FCF leg n.m. — EXPENSIVE")
        self.assertEqual(r.no_cash_figure(band, "BAB", None)[:2], (r.NM, None))
        self.assertEqual(r.no_cash_figure("CHEAP ≈ $50 (MCap/FCF binds; EV/OI no-cash n.m., all-cash $61)", "X",
                                          None)[0], r.NM)
        # An n.m. that is not the strict line (a P12 edge) proves nothing.
        self.assertEqual(r.plain(r.no_cash_figure("CHEAP < ≈ $88 (MCap/FCF binds; EV/OI legs ≈ $90–98 "
                                                  "no-cash/all-cash; P12 edge n.m. no-cash)", "X", None)[0]), "88")
        row = csv_row("BAB", verdict="AVOID", past="WEAK", future="WEAK", trigger="14.4", model_version="v4.4.1",
                      trigger_basis="all-cash")
        root = retrigger_fixture(extra_rows=[(row, "---\nticker: BAB\ntrigger_band: \"%s\"\n---\n" % band)])
        try:
            rows, report, _block, _path = r.retrigger(root.path, RT_DATE)
        finally:
            root.close()
        bab = [x for x in rows if x["key"] == "BAB"][0]
        self.assertEqual((bab["trigger"], bab["trigger_basis"]), (r.NM, "no-cash"))
        self.assertIn("| BAB | AVOID-2 | 14.4 | n.m. | no price | the no-cash bound prints n.m.", report)
        self.assertIn("| Resolved with a lower trigger | 2 (median change -4.0%) |", report)   # n.m. is no change
        self.assertEqual(r.validate_row(bab), [])

    def test_held_add_band_above_the_trigger_is_listed(self):
        row = csv_row("UP", trigger="50", model_version="v4.4.1", trigger_basis="all-cash", held="true", zone="HOLD",
                      add_band="55", sell_line="200", last_zone_check="2026-10-02", avg_cost="40 USD")
        root = retrigger_fixture(extra_rows=[(row, "---\nticker: UP\ntrigger_band: \"CHEAP < ≈ $50\"\n---\n")])
        try:
            rows, report, _block, _path = r.retrigger(root.path, RT_DATE)
        finally:
            root.close()
        up = [x for x in rows if x["key"] == "UP"][0]
        self.assertEqual((up["trigger"], up["trigger_basis"]), ("50", "all-cash"))
        self.assertIn("ADD band 55 above the trigger 50", report)


class HeldBandTests(unittest.TestCase):
    def test_held_add_band_follows_a_memo_without_position_fields(self):
        # P21 (R10): a held name's ADD band is its no-cash trigger; a memo without position fields moves it.
        held = held_core(csv_row("LEFT", held="true", zone="HOLD", add_band="60", trigger="60", sell_line="268.6",
                                 last_zone_check="2026-10-04", avg_cost="10.00 USD",
                                 memo_path="memos/LEFT/LEFT_2026-07-31_GSC.md", memo_date="2026-07-31"))
        root = TempRoot({"register.csv": r.csv_text([held]),
                         "memos/LEFT/LEFT_2026-10-05_GSC.md": memo_text(TROW_FM, drop=("position", "zone"),
                                                                        ticker="LEFT", memo_date="2026-10-05")})
        try:
            report = r.apply_memo(root.path, "memos/LEFT/LEFT_2026-10-05_GSC.md")
            row = {x["key"]: x for x in r.load_csv(root.path)[0]}["LEFT"]
        finally:
            root.close()
        self.assertEqual((row["trigger"], row["add_band"], row["zone"], row["sell_line"]), ("55.5", "55.5", "HOLD",
                                                                                            "268.6"))
        self.assertIn("NOTE LEFT ADD band 60 follows the memo's no-cash trigger 55.5 (P21, R10)", report["notes"])


# ------------------------------------------------------------------ v4.6.0: reinvestment (G4), RETIRED (G5)

class PastLevelTests(unittest.TestCase):
    def test_worst_of_eight_is_read_like_worst_of_four(self):
        cases = [
            ("Worst-of-four normalized ROCE 31.2% (end-of-period, with-cash).", "31.2% ROCE"),
            ("Worst of eight normalized ROCE 5.17% (exclude-both governs; G6).", "5.2% ROCE"),
            ("The worst-of-eight ROCE is 4.03% on the include reading.", "4% ROCE"),
        ]
        for text, want in cases:
            self.assertEqual(r.past_level(text)[0], want, text)
        self.assertEqual(r.past_level("Worst of six normalized ROCE 9.0%."), (None, None))


class ReinvestmentTokenTests(unittest.TestCase):
    def test_reinvestment_follows_distributions(self):
        self.assertEqual(r.SF_REASONS.index("reinvestment"), r.SF_REASONS.index("distributions") + 1)
        self.assertNotIn("reinvestment", r.SF_FAIL_ONLY)
        self.assertEqual(r.validate_row(csv_row("A", sf_reason="reinvestment")), [])               # PASS caution
        self.assertEqual(r.validate_row(csv_row("A", verdict="AVOID", sf="FAIL", sf_reason="reinvestment")), [])
        self.assertEqual(r.grade_cell("PASS", "reinvestment", sf=True), "PASS CAUTION · reinvestment")
        for name, grade in (("past_reason", "past"), ("future_reason", "future")):
            row = csv_row("A", verdict="AVOID", **{grade: "WEAK", name: "reinvestment"})
            self.assertTrue(any("reason vocabulary" in p for p in r.validate_row(row)), name)
        self.assertEqual(r.lint_memo(LintTests.PATH, memo_text(TROW_FM, sf_reason="reinvestment"))[0], [])
        self.assertEqual(r.lint_memo(LintTests.PATH, memo_text(TROW_FM, sf="FAIL", verdict="AVOID",
                                                               sf_reason="reinvestment"))[0], [])


def retired_row(key, **over):
    """A RETIRED register row: the last memo's grades kept, Next review its last trading day."""
    base = dict(verdict="RETIRED", past="ADEQUATE", future="WEAK", sf="FAIL", past_reason="14.7% ROCE",
                future_reason="no moat", sf_reason="buybacks", ev_oi="22.5",
                next_review_short="retired 2026-08-04")
    base.update(over)
    return csv_row(key, **base)


GONE_MEMO = "memos/GONE/GONE_2026-10-03_GSC.md"


class RetiredTests(unittest.TestCase):
    def setUp(self):
        held = held_core(csv_row("TROW", held="true", zone="HOLD", add_band="55.5", trigger="55.5", sell_line="268.6",
                                 last_zone_check="2026-10-04", avg_cost="10.00 USD",
                                 memo_path="memos/TROW/TROW_2026-10-03_GSC.md", memo_date="2026-10-03"))
        self.root = TempRoot({
            "register.csv": r.csv_text([held, csv_row("OTHER")]),
            "memos/TROW/TROW_2026-10-03_GSC.md": memo_text(TROW_FM),
            GONE_MEMO: memo_text(TROW_FM, drop=("position", "zone", "add_band", "sell_flag_line", "avg_cost"),
                                 ticker="GONE", company="Gone Corp.", isin="US0000000001"),
        })
        r.apply_memo(self.root.path, GONE_MEMO)
        self.applied = self.rows()["GONE"]

    def tearDown(self):
        self.root.close()

    def rows(self):
        return {x["key"]: x for x in r.load_csv(self.root.path)[0]}

    def test_retire_and_undo_round_trip(self):
        report = r.retire(self.root.path, "GONE", "2026-08-04", "  Form 25,\n 2026-08-04 ")
        gone = self.rows()["GONE"]
        self.assertEqual((gone["verdict"], gone["section"], gone["next_review_short"]),
                         ("RETIRED", "RETIRED", "retired 2026-08-04"))
        self.assertEqual({n: v for n, v in gone.items() if gone[n] != self.applied[n]},
                         {"verdict": "RETIRED", "section": "RETIRED", "next_review_short": "retired 2026-08-04"})
        self.assertEqual(report["entry"], "GONE retired: RETIRED (was WATCH; last trading day 2026-08-04; "
                                          "source: Form 25, 2026-08-04)")
        self.assertIn("| WATCH |", report["old"])
        self.assertTrue(report["new"].endswith("| RETIRED | ADEQUATE · 23.9% ROCE | ADEQUATE | PASS CAUTION · buybacks "
                                               "| 104.62 | 55.5 | 15.1 | 10.9 | 15.9 · 17.2 | 11.7 · 12.6 | "
                                               "retired 2026-08-04 |"), report["new"])
        self.assertEqual([x["key"] for x in r.load_csv(self.root.path)[0]][-1], "GONE")     # the RETIRED rows last
        self.assertEqual(r.validate_row(gone), [])
        undo = r.unretire(self.root.path, "GONE")
        self.assertEqual(self.rows()["GONE"], self.applied)       # exactly the row apply wrote from the memo
        self.assertEqual(undo["changes"][0]["new"], r.table_line(r.master_cells(self.applied)))
        self.assertNotIn("RETIRED", r.render(list(self.rows().values()), "v2", "2026-10-15"))

    def test_retire_refusals_leave_the_register_alone(self):
        before = self.root.read("register.csv")
        cases = [(("NOPE", "2026-08-04", "x"), "not in register.csv"),
                 (("GONE", "2026-02-30", "x"), "last trading day as YYYY-MM-DD"),
                 (("GONE", "4 Aug 2026", "x"), "last trading day as YYYY-MM-DD"),
                 (("GONE", "2026-08-04", " \n "), "primary notice"),
                 (("TROW", "2026-08-04", "x"), "a held name is never retired"),
                 (("GONE", "2026-08-04", "x" * (r.ENTRY_CAP)), "shorten --source")]
        for args, needle in cases:
            with self.assertRaises(r.ToolError) as caught:
                r.retire(self.root.path, *args)
            self.assertIn(needle, str(caught.exception), args)
            self.assertEqual(self.root.read("register.csv"), before, args)
        with self.assertRaises(r.ToolError) as caught:
            r.unretire(self.root.path, "GONE")
        self.assertIn("is not RETIRED (verdict WATCH): nothing to undo", str(caught.exception))
        r.retire(self.root.path, "GONE", "2026-08-04", "x")
        after = self.root.read("register.csv")
        with self.assertRaises(r.ToolError) as caught:
            r.retire(self.root.path, "GONE", "2026-08-05", "y")
        self.assertIn("already RETIRED (retired 2026-08-04)", str(caught.exception))
        with self.assertRaises(r.ToolError) as caught:
            r.set_position(self.root.path, "GONE", True, "10.00 USD")
        self.assertIn("never held", str(caught.exception))
        self.assertEqual(self.root.read("register.csv"), after)

    def test_apply_refuses_a_retired_key(self):
        r.retire(self.root.path, "GONE", "2026-08-04", "x")
        before = self.root.read("register.csv")
        for row_type in ("ANALYSE", "REVIEW"):
            rel = "queue/rows/2026-10-05_2130_%s_GONE.md" % row_type
            self.root.write(rel, "---\nrow_type: %s\nmemo_path: %s\nrun_date: 2026-10-05\n---\n" % (row_type, GONE_MEMO))
            with self.assertRaises(r.ToolError) as caught:
                r.apply_row(self.root.path, rel)
            self.assertIn("GONE is RETIRED (retired 2026-08-04)", str(caught.exception))
            self.assertIn("`retire --undo --key GONE` first", str(caught.exception))
        code, _out, err = run_main(["--root", self.root.path, "apply", "--memo", GONE_MEMO])
        self.assertEqual(code, 2)
        self.assertIn("apply refuses %s" % GONE_MEMO, err)
        self.assertEqual(self.root.read("register.csv"), before)
        # A SWEEP leaves it out; a QUEUE row changes nothing.
        self.root.write("queue/rows/2026-10-06_0630_SWEEP.md", "\n".join([
            "---", "row_type: SWEEP", "run_date: 2026-10-06", "run_time: 0630", "---",
            "## Price/ordering refresh", "| Key | Px | Px unit | Close date | Source |", "|---|---|---|---|---|",
            "| GONE | 90 | USD | 2026-10-05 | endpoint |", ""]))
        report = r.apply_row(self.root.path, "queue/rows/2026-10-06_0630_SWEEP.md")
        self.assertEqual(report["skips"], [{"key": "GONE", "reason": "out of SWEEP scope (RETIRED, never refreshed)"}])
        self.assertEqual(self.root.read("register.csv"), before)

    def test_a_memo_never_carries_retired(self):
        text = memo_text(TROW_FM, drop=("position", "zone", "add_band", "sell_flag_line", "avg_cost"), ticker="NEWK",
                         verdict="RETIRED", next_review_short="retired 2026-08-04")
        self.root.write("memos/NEWK/NEWK_2026-10-03_GSC.md", text)
        with self.assertRaises(r.ToolError) as caught:
            r.apply_memo(self.root.path, "memos/NEWK/NEWK_2026-10-03_GSC.md")
        self.assertIn("a memo's verdict is one of BUY/WATCH/AVOID/DNAF", str(caught.exception))
        fails, _ = r.lint_memo("memos/NEWK/NEWK_2026-10-03_GSC.md", text)
        self.assertTrue(any(f.startswith("verdict: 'RETIRED' is not one word of BUY/WATCH/AVOID/DNAF") for f in fails),
                        fails)
        self.assertTrue(any(f.startswith("next_review_short: 'retired 2026-08-04'") for f in fails), fails)

    def test_retire_refuses_a_date_after_today(self):
        before = self.root.read("register.csv")
        with self.assertRaises(r.ToolError) as caught:
            r.retire(self.root.path, "GONE", "2026-10-16", "Form 25", today="2026-10-15")
        self.assertIn("--date 2026-10-16 is after today (2026-10-15)", str(caught.exception))
        self.assertIn("a delisting awaiting retirement", str(caught.exception))
        self.assertEqual(self.root.read("register.csv"), before)
        # The last trading day may be today itself.
        r.retire(self.root.path, "GONE", "2026-10-15", "Form 25", today="2026-10-15")
        self.assertEqual(self.rows()["GONE"]["next_review_short"], "retired 2026-10-15")
        r.unretire(self.root.path, "GONE")
        self.assertEqual(self.rows()["GONE"], self.applied)
        # The CLI reads the system date.
        tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).isoformat()
        code, _out, err = run_main(["--root", self.root.path, "retire", "--key", "GONE", "--date", tomorrow,
                                    "--source", "Form 25"])
        self.assertEqual(code, 2)
        self.assertIn("--date %s is after today (%s)" % (tomorrow, datetime.date.today().isoformat()), err)
        self.assertEqual(self.root.read("register.csv"), before)

    def test_undo_on_the_same_memo_keeps_every_other_field(self):
        """retire changes three fields; undo on the memo the key was retired on takes those three from that memo
        and keeps what the memo cannot give (a SWEEP Px and its source, rebuild core numbers, the trigger basis)."""
        rows = self.rows()
        swept = dict(rows["GONE"], px_date="2026-10-05", px_source="SWEEP 2026-10-05", core_source="rebuild-assisted")
        self.assertEqual(r.validate_row(swept), [])
        self.assertNotEqual((swept["px_date"], swept["px_source"], swept["core_source"]),
                            (self.applied["px_date"], self.applied["px_source"], self.applied["core_source"]))
        self.root.write("register.csv", r.csv_text([swept if x["key"] == "GONE" else x for x in rows.values()]))
        before = self.rows()["GONE"]
        r.retire(self.root.path, "GONE", "2026-08-04", "Form 25")
        report = r.unretire(self.root.path, "GONE")
        self.assertEqual(self.rows()["GONE"], before)
        self.assertIn("NOTE GONE restored from %s, the memo it was retired on: verdict WATCH, section WATCH and Next "
                      "review %s come from that memo (memo wins); every other field kept"
                      % (GONE_MEMO, before["next_review_short"]), report["notes"])
        self.assertEqual(report["changes"][0]["new"], r.table_line(r.master_cells(before)))

    def test_undo_takes_the_memo_verdict_over_a_register_hold(self):
        """A row held at DNAF against its memo's AVOID (EA, register v280) comes back at the memo's verdict: undo
        restores from the memo, never from the value retire overwrote, and its note says so."""
        rows = self.rows()
        # Grades kept (EA's own shape): the three fields come back from the memo, the rest stays.
        hold = dict(rows["GONE"], verdict="DNAF", section="DNAF", next_review_short="n.m.")
        self.assertEqual(r.validate_row(hold), [])
        self.root.write("register.csv", r.csv_text([hold if x["key"] == "GONE" else x for x in rows.values()]))
        r.retire(self.root.path, "GONE", "2026-08-04", "Form 25")
        report = r.unretire(self.root.path, "GONE")
        gone = self.rows()["GONE"]
        self.assertEqual(gone, dict(hold, verdict=self.applied["verdict"], section=self.applied["section"],
                                    next_review_short=self.applied["next_review_short"]))
        self.assertTrue(any("verdict %s" % self.applied["verdict"] in n and "memo wins" in n for n in report["notes"]))
        # Grades blanked by the hold: that row cannot carry the memo's verdict, so undo rebuilds it from the memo.
        blank = dict(hold, past="n.m.", future="n.m.", sf="n.m.", past_reason="n.m.", future_reason="n.m.",
                     sf_reason="n.m.", gates_failed="0")
        self.assertEqual(r.validate_row(blank), [])
        self.root.write("register.csv", r.csv_text([blank if x["key"] == "GONE" else x for x in rows.values()]))
        r.retire(self.root.path, "GONE", "2026-08-04", "Form 25")
        report = r.unretire(self.root.path, "GONE")
        self.assertEqual(self.rows()["GONE"], self.applied)
        self.assertTrue(any(n.startswith("NOTE GONE rebuilt from %s: the memo's verdict" % GONE_MEMO)
                            for n in report["notes"]), report["notes"])

    def test_undo_reads_the_current_memo_after_retirement(self):
        """retire --undo rebuilds from the one file in memos/GONE/, never from the memo_path the RETIRED row kept:
        here a REVIEW memo landed after the key was retired and its predecessor moved to archive/memos/GONE/."""
        r.retire(self.root.path, "GONE", "2026-08-04", "Form 25")
        newer = "memos/GONE/GONE_2026-10-10_GSC.md"
        text = memo_text(TROW_FM, drop=("position", "zone", "add_band", "sell_flag_line", "avg_cost"), ticker="GONE",
                         company="Gone Corp.", isin="US0000000001", memo_date="2026-10-10", memo_version="v6",
                         verdict="AVOID", quality_future="WEAK", future_reason="no moat")
        os.makedirs(os.path.join(self.root.path, "archive", "memos", "GONE"))
        os.replace(os.path.join(self.root.path, GONE_MEMO), os.path.join(self.root.path, "archive", GONE_MEMO))
        self.root.write(newer, text)
        self.assertEqual(self.rows()["GONE"]["memo_path"], GONE_MEMO)          # what the RETIRED row cites
        others = [x for k, x in self.rows().items() if k != "GONE"]
        report = r.unretire(self.root.path, "GONE")
        gone = self.rows()["GONE"]
        # Exactly the row apply --memo writes from that memo onto the register as it stood before retirement.
        twin = TempRoot({"register.csv": r.csv_text(others + [self.applied]), newer: text})
        try:
            r.apply_memo(twin.path, newer)
            expected = {x["key"]: x for x in r.load_csv(twin.path)[0]}["GONE"]
        finally:
            twin.close()
        self.assertEqual(gone, expected)
        self.assertEqual((gone["memo_path"], gone["memo_date"], gone["memo_version"], gone["verdict"],
                          gone["section"], gone["future_reason"]),
                         (newer, "2026-10-10", "v6", "AVOID", "AVOID-1", "no moat"))
        self.assertIn("NOTE GONE rebuilt from the current memo %s (the RETIRED row cited %s)" % (newer, GONE_MEMO),
                      report["notes"])
        self.assertEqual(report["changes"][0]["new"], r.table_line(r.master_cells(gone)))

    def test_undo_needs_exactly_one_memo_in_the_folder(self):
        r.retire(self.root.path, "GONE", "2026-08-04", "Form 25")
        before = self.root.read("register.csv")
        folder = os.path.join(self.root.path, "memos", "GONE")

        def refused(needle):
            with self.assertRaises(r.ToolError) as caught:
                r.unretire(self.root.path, "GONE")
            self.assertIn(needle, str(caught.exception))
            self.assertEqual(self.root.read("register.csv"), before)

        second = "memos/GONE/GONE_2026-10-10_GSC.md"
        self.root.write(second, memo_text(TROW_FM, ticker="GONE"))
        refused("memos/GONE/ holds 2 files (GONE_2026-10-03_GSC.md, GONE_2026-10-10_GSC.md): the current memo is "
                "the one file there")
        code, _out, err = run_main(["--root", self.root.path, "retire", "--undo", "--key", "GONE"])
        self.assertEqual(code, 2)
        self.assertIn("memos/GONE/ holds 2 files", err)
        os.remove(os.path.join(self.root.path, second))
        os.remove(os.path.join(self.root.path, GONE_MEMO))
        refused("memos/GONE/ holds 0 files: the current memo is the one file there")
        os.rmdir(folder)
        refused("memos/GONE/ holds 0 files")
        self.root.write("memos/GONE/notes.md", "x")
        refused("memos/GONE/notes.md is not memos/{KEY}/{KEY}_{date}_GSC.md for GONE")
        os.remove(os.path.join(folder, "notes.md"))
        self.root.write("memos/GONE/GON2_2026-10-03_GSC.md", memo_text(TROW_FM, ticker="GON2"))
        refused("memos/GONE/GON2_2026-10-03_GSC.md is not memos/{KEY}/{KEY}_{date}_GSC.md for GONE")

    def test_cli(self):
        code, out, err = run_main(["--root", self.root.path, "retire", "--key", "GONE", "--date", "2026-08-04",
                                   "--source", "Form 25"])
        self.assertEqual(code, 0, err)
        self.assertEqual(json.loads(out)["entry"],
                         "GONE retired: RETIRED (was WATCH; last trading day 2026-08-04; source: Form 25)")
        for argv, needle in ((["retire", "--key", "GONE", "--date", "2026-08-04"], "retire takes --key"),
                             (["retire", "--undo", "--key", "GONE", "--date", "2026-08-04"], "--undo takes only --key")):
            code, _out, err = run_main(["--root", self.root.path] + argv)
            self.assertEqual(code, 2, argv)
            self.assertIn(needle, err)
        code, out, err = run_main(["--root", self.root.path, "retire", "--undo", "--key", "GONE"])
        self.assertEqual(code, 0, err)
        self.assertEqual(json.loads(out)["row"], "retire --undo GONE")
        self.assertEqual(self.rows()["GONE"], self.applied)


class RetiredRowTests(unittest.TestCase):
    def test_validate_row_rules(self):
        self.assertEqual(r.section_for("RETIRED", 2), "RETIRED")
        self.assertEqual(r.validate_row(retired_row("A")), [])
        nm = retired_row("B", past=r.NM, future=r.NM, sf=r.NM, past_reason=r.NM, future_reason=r.NM,
                         sf_reason=r.NM, trigger_basis=r.NM, px=r.OWED, trigger=r.NM, mcap_fcf=r.NM, ev_oi=r.NM)
        self.assertEqual(r.validate_row(nm), [])                 # a Gate-0 memo's n.m. grades and basis stay
        bad = [(dict(next_review_short=r.NM), "reads 'retired YYYY-MM-DD'"),
               (dict(next_review_short="retired 2026-02-30"), "reads 'retired YYYY-MM-DD'"),
               (dict(next_review_short="2026-08-04"), "reads 'retired YYYY-MM-DD'"),
               (dict(held="true", zone="HOLD", add_band="80", sell_line="200", last_zone_check="2026-08-01",
                     avg_cost="50 USD"), "a held name is never retired"),
               (dict(gates_failed="1"), "gates_failed: 1, but the grades give 2"),
               (dict(section="DNAF"), "section: DNAF, but verdict and gates give RETIRED"),
               (dict(sf_reason="delisted"), "reason vocabulary")]
        for over, needle in bad:
            problems = r.validate_row(retired_row("C", **over))
            self.assertTrue(any(needle in p for p in problems), (over, problems))
        problems = r.validate_row(csv_row("D", next_review_short="retired 2026-08-04"))
        self.assertTrue(any("is not YYYY-MM-DD, Qn YYYY, Mon YYYY or n.m." in p for p in problems), problems)
        problems = r.validate_row(csv_row("E", verdict="GONE"))
        self.assertTrue(any("is not one of BUY/WATCH/AVOID/DNAF/RETIRED" in p for p in problems), problems)

    def test_render_order_counts_and_byte_identity_without_retired(self):
        rows = RenderTests().rows()
        plain = r.render(rows, "v308", "2026-10-07")
        self.assertNotIn("RETIRED", plain)
        self.assertIn('\nordering: "v4.5.0 — PORTFOLIO → BUY → WATCH → AVOID one gate → AVOID two+ → DNAF; EV/OI '
                      'ascending, n.m. then - last; DNAF alphabetical"\n', plain)
        both = rows + [retired_row("ZED"), retired_row("ABC", past=r.NM, future=r.NM, sf=r.NM, past_reason=r.NM,
                                                        future_reason=r.NM, sf_reason=r.NM)]
        text = r.render(both, "v308", "2026-10-07")
        heads = [l for l in text.split("\n") if l.startswith("## ")]
        self.assertEqual(heads[-2:], ["## DNAF (2)", "## RETIRED (2)"])
        tail = text.split("## RETIRED (2)")[1]
        self.assertLess(tail.index("| ABC |"), tail.index("| ZED |"))
        self.assertIn("names_total: 12\n", text)
        self.assertIn('verdict_split: "BUY 0 · WATCH 6 · AVOID 2 (one gate 1 · two+ 1) · DNAF 2 · RETIRED 2"', text)
        self.assertIn('\nordering: "v4.6.0 — PORTFOLIO → BUY → WATCH → AVOID one gate → AVOID two+ → DNAF → RETIRED; '
                      'EV/OI ascending, n.m. then - last; DNAF and RETIRED alphabetical"\n', text)
        # Everything else is the rendering without them, the RETIRED section appended last.
        body = lambda t: t.split("---\n", 2)[2]
        self.assertTrue(body(text).startswith(body(plain) + "\n## RETIRED (2)\n\n"), body(text)[-600:])
        self.assertEqual([x["key"] for x in r.canonical(both)][-2:], ["ABC", "ZED"])

    def test_the_repository_register_renders_byte_for_byte(self):
        """The committed _REGISTER.md is what this tool renders from the committed register.csv (the v4.5.x
        tool rendered it while no RETIRED row existed)."""
        csv_path, md_path = os.path.join(REPO, "register.csv"), os.path.join(REPO, "_REGISTER.md")
        if not (os.path.isfile(csv_path) and os.path.isfile(md_path)):
            self.skipTest("no register in this checkout")
        rows, problems = r.load_csv(REPO)
        self.assertEqual(problems, [])
        with open(md_path, "rb") as fh:
            md = fh.read().decode("utf-8").replace("\r\n", "\n")
        fm = r.parse_front_matter(md)
        self.assertEqual(r.render(rows, fm["register_version"], fm["register_date"]), md)

    def test_check_does_not_recompute_a_retired_row(self):
        gone = held_core(retired_row("GONE", px="104.62", mcap_fcf="15.1", ev_oi="10.9", ev_oi_all_cash="9.5",
                                     memo_path="memos/GONE/GONE_2026-09-01_GSC.md"))
        bad = dict(gone, key="GON2", memo_path="memos/GON2/GON2_2026-09-01_GSC.md", mcap_fcf="12")
        self.assertEqual(r.validate_row(gone), [])
        root = CheckTests().build([gone, bad], md=r.render([gone], "v10", "2026-10-07"))
        try:
            breaches, _listed, counts = r.check(root.path, base="HEAD")
        finally:
            root.close()
        self.assertFalse(any("does not recompute" in b for b in breaches), breaches)
        self.assertIn("GON2: mcap_fcf: '12' is not a one-decimal multiple", breaches)
        self.assertEqual(counts["RETIRED"], 2)

    def test_sweep_scope_position_retrigger_and_rebuild_leave_it(self):
        rows = [csv_row("LIVE"), retired_row("GONE")]
        root = TempRoot({"register.csv": r.csv_text(rows)})
        try:
            code, out, _err = run_main(["--root", root.path, "sweep-scope"])
        finally:
            root.close()
        self.assertEqual(code, 0)
        self.assertEqual([line.split(",")[0] for line in out.splitlines()[1:]], ["LIVE"])
        old = retired_row("OLDR", trigger="70", trigger_basis="all-cash", model_version="v4.4.1")
        self.assertEqual(r.validate_row(old), [])
        resolved, unresolved, nm_rows, _rejected = r.retrigger_rows("/nonexistent", [dict(old)])
        self.assertEqual((resolved, unresolved, nm_rows), ([], [], []))
        root = TempRoot({"_REGISTER.md": r.render([csv_row("LIVE"), retired_row("GONE")], "v10", "2026-10-07"),
                         "register.csv": r.csv_text([csv_row("LIVE"), retired_row("GONE")])}, git=True)
        try:
            with self.assertRaises(r.ToolError) as caught:
                r.rebuild(root.path, "HEAD")
        finally:
            root.close()
        self.assertIn("holds a RETIRED section", str(caught.exception))


class RetiredHoldingTests(unittest.TestCase):
    """MODEL v4.6.0 section 7.1 (G5) and section 2 Group dependencies (G4): a RETIRED holding is never reviewed, so
    its parent, not the holding, is the work item; a RETIRED parent is never re-run."""

    def test_a_retired_holding_lists_its_parent_once(self):
        rows = [csv_row("PAR", holding_keys="GONE; OLDV", memo_date="2026-09-01"),
                retired_row("GONE", memo_date="2026-09-20", model_version="v4.4.0",
                            memo_path="memos/GONE/GONE_2026-09-20_GSC.md", next_review_short="retired 2026-09-25"),
                csv_row("OLDV", memo_date="2026-08-01", model_version="v4.4.0"),
                retired_row("RPAR", holding_keys="OLDV; NOPE", memo_date="2026-01-01",
                            memo_path="memos/RPAR/RPAR_2026-01-01_GSC.md")]
        listed = r.holding_findings(rows, "2026-10-15")
        self.assertEqual([x for x in listed if "GONE" in x],
                         ["PAR: parent stale - holding GONE retired — re-test the parent"])
        self.assertIn("PAR: parent stale - holding OLDV memo 2026-08-01 v4.4.0 is not current (P26)", listed)
        self.assertFalse(any(x.startswith("RPAR:") for x in listed), listed)
        # The same holding, not RETIRED, reads as a stale memo (REVIEW would take the holding itself) and a newer one.
        live = r.holding_findings([rows[0], dict(rows[1], verdict="AVOID"), rows[2]], "2026-10-15")
        self.assertIn("PAR: parent stale - holding GONE memo 2026-09-20 v4.4.0 is not current (P26)", live)
        self.assertIn("PAR: parent stale - holding GONE memo 2026-09-20 is newer than this memo 2026-09-01", live)

    def test_check_lists_it_never_as_a_breach(self):
        rows = [csv_row("PAR", holding_keys="GONE", memo_date="2026-09-01"),
                retired_row("GONE", next_review_short="retired 2026-09-25")]
        root = CheckTests().build(rows)
        try:
            breaches, listed, _counts = r.check(root.path, base="HEAD")
            code, out, _err = run_main(["--root", root.path, "check", "--base", "HEAD"])
        finally:
            root.close()
        self.assertEqual(breaches, [])
        self.assertEqual([x for x in listed if "holding" in x],
                         ["PAR: parent stale - holding GONE retired — re-test the parent"])
        self.assertEqual(code, 0, out)
        self.assertIn("LIST    PAR: parent stale - holding GONE retired — re-test the parent", out)


    def test_a_parent_memo_after_the_last_trading_day_has_re_read_it(self):
        # The finding fires once: a parent memo dated after the holding's last trading day already re-read it,
        # so check does not re-queue the parent every day (no loop at REVIEW priority 1c).
        rows = [csv_row("PAR", holding_keys="GONE", memo_date="2026-10-01"),
                retired_row("GONE", next_review_short="retired 2026-09-25")]
        self.assertEqual([x for x in r.holding_findings(rows, "2026-10-15") if "GONE" in x], [])
        same_day = [dict(rows[0], memo_date="2026-09-25"), rows[1]]
        self.assertEqual([x for x in r.holding_findings(same_day, "2026-10-15") if "GONE" in x],
                         ["PAR: parent stale - holding GONE retired — re-test the parent"])


class DependencyTokenTests(unittest.TestCase):
    def test_unit_and_sub_dependency_are_future_reasons(self):
        # MODEL v4.6.0 section 7.1: `dependency` is an ungradeable part, printed `sub dependency` for a listed
        # subsidiary or holding and `unit dependency` for an undescribed material unit (new); never Past or SF.
        for value in ("unit dependency", "sub dependency", "dependency"):
            self.assertTrue(r.reason_ok("future", value), value)
            self.assertFalse(r.reason_ok("past", value), value)
            self.assertFalse(r.reason_ok("sf", value), value)
            self.assertEqual(r.validate_row(csv_row("A", verdict="AVOID", future="WEAK", future_reason=value)), [],
                             value)
            for name, grade in (("past_reason", "past"), ("sf_reason", "sf")):
                row = csv_row("A", verdict="AVOID", **{grade: "FAIL" if grade == "sf" else "WEAK", name: value})
                self.assertTrue(any("reason vocabulary" in p for p in r.validate_row(row)), (name, value))
            # An ADEQUATE prints a concentration caveat or nothing: an ungradeable part is no caveat.
            problems = r.validate_row(csv_row("A", future="ADEQUATE", future_reason=value))
            self.assertTrue(any("concentration caveat" in p for p in problems), (value, problems))
        for value in ("unit sub dependency", "units dependency", "unit dependency owed"):
            self.assertFalse(r.reason_ok("future", value), value)
        # A group memo (its B4 Division table) prints either; a memo that is no group carries no group prefix.
        for value in ("unit dependency", "sub dependency"):
            fails, warns = LintTests().group(verdict="AVOID", quality_future="WEAK", future_reason=value)
            self.assertEqual(fails, [], (value, warns))
        fails, _ = r.lint_memo(LintTests.PATH, memo_text(TROW_FM, verdict="AVOID", quality_future="WEAK",
                                                         future_reason="unit dependency"))
        self.assertTrue(any("carries the group prefix 'unit'" in f for f in fails), fails)

class ReturnFieldTests(unittest.TestCase):
    """MODEL v4.8.0 section 6.1 (IDEAS C9): roce_worst and fcfroce_worst, the governing levels (the lower
    window's worst-of-four, worst of eight under G6), required from v4.8.0 and absent before."""
    PATH = LintTests.PATH
    # TROW's memo of 2026-10-19 (section 3): 'Worst-of-eight ROCE is 22.9% (window) and 19.3% (five years) ...
    # FCFROCE ... is 12.7% and 13.7%' -> Past WEAK on growth; the governing levels are 19.3% and 12.7%.
    V480 = {"model_version": "v4.8.0", "verdict": "AVOID", "quality_past": "WEAK", "past_reason": "growth",
            "roce_worst": "19.3%", "fcfroce_worst": "12.7%"}

    def lint(self, drop=(), **over):
        fm = dict(TROW_FM, **self.V480)
        fm.update(over)
        return r.lint_memo(self.PATH, memo_text(fm, drop=drop))

    def test_required_from_v480_only(self):
        self.assertEqual(self.lint()[0], [])
        fails, _ = self.lint(drop=r.RETURN_FIELDS)
        self.assertEqual([f.split(":")[0] for f in fails], ["roce_worst", "fcfroce_worst"], fails)
        # A memo under an earlier MODEL carries neither field (memos are never edited in place).
        for version in ("v4.7.0", "v4.6.1", "v4.5.0"):
            fails, _ = self.lint(drop=r.RETURN_FIELDS, model_version=version)
            self.assertEqual(fails, [], version)
        self.assertEqual(r.RETURN_FIELDS, ("roce_worst", "fcfroce_worst"))
        self.assertFalse(set(r.RETURN_FIELDS) & set(r.CSV_HEADER))       # no register column (nothing consumes it)
        self.assertFalse(set(r.RETURN_FIELDS) & set(r.NEW_MEMO_FIELDS))  # not required of a v4.5.0-v4.7.x memo

    def test_forms(self):
        for value in ("19.3%", "-8.7%", "0.0%", "112.0%", "-61.1%", "n.m."):
            self.assertEqual(self.lint(roce_worst=value)[0], [], value)
        # One decimal, as MODEL section 5 rounds return ratios: never an integer or two decimals.
        for value in ("19.3", "19.3 %", "19.33%", "16.10%", "19%", "112%", "−8.7%", "+19.3%", "19,3%", "high",
                      "n/a"):
            fails, _ = self.lint(roce_worst=value)
            self.assertTrue(any(f.startswith("roce_worst: %r is not a percent" % value) for f in fails),
                            (value, fails))
        fails, _ = self.lint(fcfroce_worst="-")
        self.assertTrue(any(f.startswith("fcfroce_worst: '-' (not established)") for f in fails), fails)

    def test_roce_worst_is_the_past_reason_level(self):
        # DOV.MI's memo of 2026-10-26: 'The worst-of-eight ROCE is 8.0% over ten years and 6.8% over five'
        # -> past_reason '6.8% ROCE' (the lower window decides).
        dov = dict(past_reason="6.8% ROCE", fcfroce_worst="4.6%")
        self.assertEqual(self.lint(roce_worst="6.8%", **dov)[0], [])
        fails, _ = self.lint(roce_worst="8.0%", **dov)
        self.assertTrue(any(f.startswith("roce_worst: 8.0%, but past_reason prints '6.8% ROCE'") for f in fails),
                        fails)
        fails, _ = self.lint(roce_worst="n.m.", **dov)
        self.assertTrue(any(f.startswith("roce_worst: n.m., but past_reason prints the level") for f in fails), fails)
        # past_reason's own precision governs the comparison ('24% ROCE' is 23.9% rounded).
        self.assertEqual(self.lint(quality_past="ADEQUATE", verdict="WATCH", past_reason="24% ROCE",
                                   roce_worst="23.9%")[0], [])
        # A WEAK reason other than a level leaves roce_worst free (TROW: growth; ABCA.PA: losses at -61.1%).
        self.assertEqual(self.lint(past_reason="losses", roce_worst="-61.1%", fcfroce_worst="-7.2%")[0], [])

    def test_graded_levels_reach_their_floors(self):
        strong = dict(verdict="WATCH", quality_past="STRONG", past_reason="23.9% ROCE", roce_worst="23.9%")
        self.assertEqual(self.lint(fcfroce_worst="8.0%", **strong)[0], [])
        fails, _ = self.lint(fcfroce_worst="7.9%", **strong)
        self.assertTrue(any(f.startswith("fcfroce_worst: 7.9%, but Past STRONG needs a level of at least 8%")
                            for f in fails), fails)
        adequate = dict(verdict="WATCH", quality_past="ADEQUATE")
        self.assertEqual(self.lint(past_reason="10.0% ROCE", roce_worst="10.0%", fcfroce_worst="5.3%",
                                   **adequate)[0], [])
        fails, _ = self.lint(past_reason="9.9% ROCE", roce_worst="9.9%", fcfroce_worst="5.2%", **adequate)
        self.assertTrue(any(f.startswith("roce_worst: 9.9%, but Past ADEQUATE needs a level of at least 10%")
                            for f in fails), fails)
        self.assertTrue(any(f.startswith("fcfroce_worst: 5.2%, but Past ADEQUATE needs a level of at least 5.3%")
                            for f in fails), fails)
        fails, _ = self.lint(past_reason="12.0% ROCE", roce_worst="12.0%", fcfroce_worst="n.m.", **adequate)
        self.assertTrue(any(f.startswith("fcfroce_worst: n.m., but Past ADEQUATE") for f in fails), fails)

    def test_fi_lens_writes_nm(self):
        fi = dict(LintTests.FI, verdict="WATCH", quality_past="ADEQUATE")
        self.assertEqual(self.lint(roce_worst="n.m.", fcfroce_worst="n.m.", **fi)[0], [])
        fails, _ = self.lint(roce_worst="23.9%", fcfroce_worst="n.m.", **fi)
        self.assertTrue(any(f.startswith("roce_worst: 23.9% — under the FI lens it is n.m.") for f in fails), fails)

    def test_dnaf_gate0_writes_nm(self):
        fm = {k: "n.m." for k in TROW_FM if k in r.DNAF_NM_FIELDS}
        base = dict(TROW_FM, verdict="DNAF", position="—", model_version="v4.8.0", roce_worst="n.m.",
                    fcfroce_worst="n.m.")
        base.update(fm)
        base["next_review_short"] = "n.m."
        fails, _ = r.lint_memo(self.PATH, memo_text(base, drop=("zone", "add_band", "sell_flag_line")))
        self.assertEqual(fails, [])
        self.assertTrue(set(r.RETURN_FIELDS) <= r.DNAF_NM_FIELDS)
        # A Gate-0 memo grades no Past: a level in either field fails (MODEL section 6.4).
        for name in r.RETURN_FIELDS:
            fails, _ = r.lint_memo(self.PATH, memo_text(dict(base, **{name: "5.0%"}),
                                                        drop=("zone", "add_band", "sell_flag_line")))
            self.assertEqual(fails, ["%s: 5.0%% — a section 6.4 Gate-0 (DNAF) memo grades no Past: it writes "
                                     "n.m." % name], name)

    def test_model_lists_the_fields_from_v480(self):
        """MODEL section 6.1 lists both fields, before past_reason, once MODEL.md is at v4.8.0 or later."""
        import re
        with open(os.path.join(REPO, "model", "MODEL.md"), encoding="utf-8") as fh:
            text = fh.read()
        if not r.model_at_least(r.parse_front_matter(text).get("model_version"), r.RETURN_FIELDS_FROM):
            self.skipTest("MODEL.md is below v4.8.0")
        lines = {n: re.search(r"(?m)^%s:" % n, text) for n in r.RETURN_FIELDS + ("past_reason",)}
        self.assertTrue(all(lines.values()), lines)
        self.assertLess(lines["roce_worst"].start(), lines["fcfroce_worst"].start())
        self.assertLess(lines["fcfroce_worst"].start(), lines["past_reason"].start())


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=1).result
    sys.exit(len(result.failures) + len(result.errors))
