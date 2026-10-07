#!/usr/bin/env python3
"""GSC register tool: the only place register numbers are computed (MODEL v4.5.0, sections 7.1, 7.1b, 7.2).

register.csv, beside _REGISTER.md, is the machine twin of the register: every
register column plus the core numbers, one line per key. _REGISTER.md is
rendered from it and is never edited by hand. INTAKE and every attended
register write run this tool; ANALYSE and REVIEW run its lint-memo and lint-row
checks.

Subcommands
  render --version vN --date D       write _REGISTER.md from register.csv
  row-from-memo MEMO [--table]       print the register row a memo yields
  apply --row ROWFILE | --memo MEMO  apply one queue row file (or, attended, one memo) to register.csv
  position KEY --held true|false [--avg-cost TEXT]
                                     attended position event: the only change to the held flag
  rekey OLD NEW                      RECONCILE re-key: the row follows the renamed memo folder
  metrics KEY PX [--fx RATE]         both primaries and their 3- and 5-year readings, the
                                     trigger distance and status_hint (IN RANGE / NEAR / FAR;
                                     MODEL 8.3: IN RANGE needs MCap/FCF <= 8 and EV/OI no-cash
                                     <= 7 at PX wherever the core numbers establish them), and
                                     held distances at PX (a held trigger is the ADD band, P21)
  sweep-scope                        the keys a SWEEP prices, with endpoint symbols (and
                                     holding_keys)
  check [--base REV] [--tree REV]    INTAKE step 7: register integrity
  lint-memo MEMO                     the v4.5.0 front-matter re-measure
  lint-row ROWFILE                   a row file against its name, its title and what
                                     row-from-memo --table prints for its memo (v4.5.2)
  rebuild --base REV --out DIR [--assisted FILE] [--version vN --date D]
                                     attended, one-time: the lean register from the outgoing
                                     legacy register and the memos its rows cite
  retrigger --date D [--version vN] [--assisted FILE] [--block FILE]
                                     attended, one-time (round 2, R10): every row whose trigger
                                     is the pre-R10 all-cash reading takes the memo's own
                                     printed no-cash bound (memo wins); unresolved rows keep
                                     trigger_basis all-cash and are listed; writes register.csv
                                     (lean-2, from the current or an older header) and the
                                     report archive/registers/{YYYY}/RETRIGGER_v{N}-to-v{N+1}_{D}.md
Common option: --root DIR (default: the repository that holds this file).

Python 3.8+, standard library only, no network. Git is used read-only
(`git show`, `git ls-tree`). Writes only register.csv, _REGISTER.md, the
retrigger report and the paths given with --out or --block. The same inputs
give byte-identical outputs: UTF-8, LF line ends, no BOM. Exit codes: 0 ok,
1 a check failed, 2 bad input.
"""
import argparse
import csv
import io
import itertools
import json
import os
import re
import subprocess
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

sys.dont_write_bytecode = True

# ------------------------------------------------------------------ constants

CSV_HEADER = [
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
# MODEL v4.5.0 section 6.1 lens fields kept in register.csv (`lens` lives in the memo only).
# Round 2 (R2-R5, V14): one constant credit, the material listed holdings at their own
# buy-line value (no market price moves it). Legacy defaults: no holding read, no credit.
LENS_DEFAULTS = {"holding_keys": "n.m.", "core_credit": "0"}
LENSES = ("STD", "FI")
# Round 2 (R10, R1, R6): the trigger basis, the latest-FY all-capex FCF beside the
# maintenance-capex core_fcf, and the 3- and 5-year averages with their multiples. A row
# read from an older header, or built from a memo written before v4.5.0, carries the
# pre-R10 all-cash trigger and owes the rest ('-') until its next memo.
TRIGGER_BASES = ("no-cash", "all-cash")
AVG_CORE = ("core_oi_3y", "core_oi_5y", "core_fcf_3y", "core_fcf_5y")
AVG_MULTIPLES = ("mcap_fcf_3y", "mcap_fcf_5y", "ev_oi_3y", "ev_oi_5y")
R10_FIELDS = ("trigger_basis", "core_fcf_all") + AVG_CORE + AVG_MULTIPLES
R10_DEFAULTS = dict([("trigger_basis", "all-cash")] + [(name, "-") for name in R10_FIELDS[1:]])
# Fields of the lean-1 register (MODEL v4.5.0 before round 2) that round 2 retired.
RETIRED_FIELDS = ("sotp_keys", "core_credit_fix", "core_credit_mkt", "core_credit_px")
SECTION_ORDER = ("BUY", "WATCH", "AVOID-1", "AVOID-2", "DNAF")
SECTION_TITLES = {
    "BUY": "BUY",
    "WATCH": "WATCH",
    "AVOID-1": "AVOID - one gate failed",
    "AVOID-2": "AVOID - two or more gates failed",
    "DNAF": "DNAF",
}
MASTER_COLUMNS = ["Ticker", "Company", "Memo date", "Ver", "Verdict", "Past", "Future", "SF",
                  "Px", "Trigger", "MCap/FCF", "EV/OI", "MCap/FCF 3y · 5y", "EV/OI 3y · 5y", "Next review"]
PORTFOLIO_COLUMNS = ["Ticker", "Zone", "Px", "ADD band", "Sell line", "Last zone check", "Next review"]
REGISTER_FILE = "_REGISTER.md"
CSV_FILE = "register.csv"
REGISTER_TITLE = "GSC Register — Master Watchlist"
REGISTER_FORMAT = "lean-2 (MODEL v4.5.0)"
LEGEND = (
    "Grades carry their deciding reason · Px and Trigger in the listing's quote unit "
    "(register.csv px_unit) · Trigger: the no-cash bound, the strict all-pass line (register.csv "
    "trigger_basis; all-cash marks an older reading until the next memo) · MCap/FCF and EV/OI "
    "(no-cash, strict) at the Px shown · 3y · 5y: the same multiples on 3- and 5-year average OI and "
    "FCF · n.m. not meaningful · - backfill owed.",
    "Px: the latest SWEEP close for held, BUY, WATCH and one-gate AVOID (memo price until a SWEEP prices "
    "the key's line; register.csv px_source); memo price otherwise. Rows come from current memos; the "
    "memo wins (MODEL §7.1).",
)

NM = "n.m."            # not meaningful
OWED = "-"             # not established: backfill owed
CELL_CAP = 160
VERDICTS = ("BUY", "WATCH", "AVOID", "DNAF")
GRADES = ("STRONG", "ADEQUATE", "WEAK")
SF_GRADES = ("PASS", "FAIL")
CHEAPNESS = ("CHEAP", "FAIR", "EXPENSIVE")
ZONE_RE = re.compile(r"^(ADD|HOLD|SELL-FLAG)( SR[1-3])?$")
ZONE_WORD_RE = re.compile(r"^\W*(ADD|HOLD|SELL-FLAG)\b")
SCALE = {"k": Decimal(10) ** 3, "m": Decimal(10) ** 6, "bn": Decimal(10) ** 9}
# Minor quote units: unit -> (major currency, units per major).
MINOR_UNITS = {"GBp": ("GBP", 100), "ZAc": ("ZAR", 100), "ILA": ("ILS", 100), "KWF": ("KWD", 1000)}

# MODEL section 7.1a suffix table: suffix -> default quote unit. px_unit is
# always the price endpoint's own `currency`; this default only flags surprises.
SUFFIX_UNITS = {
    "TO": "CAD", "V": "CAD", "CN": "CAD", "NE": "CAD",
    "PA": "EUR", "AS": "EUR", "BR": "EUR", "LS": "EUR", "IR": "EUR", "MI": "EUR", "MC": "EUR",
    "DE": "EUR", "VI": "EUR", "HE": "EUR", "AT": "EUR", "TL": "EUR", "RG": "EUR", "VS": "EUR",
    "SW": "CHF", "ST": "SEK", "CO": "DKK", "OL": "NOK", "IC": "ISK", "L": "GBp", "WA": "PLN",
    "PR": "CZK", "BD": "HUF", "RO": "RON", "IS": "TRY", "TA": "ILA", "SR": "SAR", "AE": "AED",
    "QA": "QAR", "KW": "KWF", "JO": "ZAc", "NS": "INR", "BO": "INR", "T": "JPY", "HK": "HKD",
    "SS": "CNY", "SZ": "CNY", "TW": "TWD", "TWO": "TWD", "KS": "KRW", "KQ": "KRW", "SI": "SGD",
    "JK": "IDR", "BK": "THB", "KL": "MYR", "VN": "VND", "AX": "AUD", "NZ": "NZD", "SA": "BRL",
    "MX": "MXN", "BA": "ARS", "SN": "CLP", "CL": "COP",
}

# Reason vocabulary (MODEL section 7.1). At most three words each; a group Future or SF
# reason (R3, R5) may carry one prefix (unit, sub) within those three words. A Past reason
# never does: Past is graded once, on the consolidated or look-through record, never as a
# weighted grade (round-2 review fix B1, 2026-10-07), so `dependency` (an ungradeable listed
# subsidiary or holding) is a Future token.
PAST_REASONS = ("ROCE decline", "FCFROCE", "leverage", "losses", "growth", "record-limited", "capital")
PAST_LEVEL_RE = re.compile(r"^\d{1,3}(\.\d)?% (ROCE|ROE)$")
FUTURE_REASONS = ("breadth", "customer conc.", "supplier conc.", "funding conc.", "no moat", "moat eroding",
                  "2+ forces", "forces: customers", "forces: suppliers", "forces: substitutes",
                  "forces: entrants", "dependency")
# R7: a Future ADEQUATE carried with a concentration flag prints the flag as its caveat;
# every other ADEQUATE, and every STRONG, prints the grade alone (n.m.).
FUTURE_CAVEATS = ("customer conc.", "supplier conc.")
# R8: pledges and insider sales are no flag (P23 is the alignment call); `alignment` is a
# single flag that fails at strike-logic step 3 (FAIL only), as are `flag pair` and `inherited`.
SF_REASONS = ("compensation", "director pay", "buybacks", "acquisitions", "distributions", "RPT",
              "control", "dilution", "alignment", "flag pair", "inherited")
SF_FAIL_ONLY = ("alignment", "flag pair", "inherited")
REASON_PREFIX_RE = re.compile(r"^(unit|sub) (.+)$")

KEY_RE = re.compile(r"^[A-Za-z0-9._-]+$", re.ASCII)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$", re.ASCII)
NUM_RE = re.compile(r"^-?\d+(\.\d+)?$", re.ASCII)
MULT_RE = re.compile(r"^-?\d+\.\d$", re.ASCII)
VER_RE = re.compile(r"^v\d+$", re.ASCII)
UNIT_RE = re.compile(r"^[A-Z]{2}[A-Za-z]$", re.ASCII)
CCY_RE = re.compile(r"^[A-Z]{3}$", re.ASCII)
ISIN_RE = re.compile(r"^[A-Z]{2}[A-Z0-9]{9}\d$", re.ASCII)
NEXT_REVIEW_RE = re.compile(r"^(\d{4}-\d{2}-\d{2}|Q[1-4] \d{4}|[A-Z][a-z]{2} \d{4}|n\.m\.)$", re.ASCII)
PX_SOURCE_RE = re.compile(r"^(memo|SWEEP \d{4}-\d{2}-\d{2})$", re.ASCII)
MEMO_PATH_RE = re.compile(r"^memos/(?P<dir>[A-Za-z0-9._-]+)/(?P<key>[A-Za-z0-9._-]+)_"
                          r"(?P<date>\d{4}-\d{2}-\d{2})_GSC\.md$", re.ASCII)
FM_LINE_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):[ \t]*(.*?)[ \t]*$")
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

# Memo front matter added at v4.5.0 (MODEL section 6.1), in template order.
NEW_MEMO_FIELDS = (
    "aliases", "px", "px_unit", "px_date", "trigger", "mcap_fcf", "ev_oi", "ev_oi_all_cash",
    "trigger_basis", "mcap_fcf_3y", "mcap_fcf_5y", "ev_oi_3y", "ev_oi_5y",
    "lens", "holding_keys", "core_credit",
    "core_period", "core_currency", "core_unit", "core_shares_diluted", "core_debt_eq", "core_cash",
    "core_oi", "core_oi_basis", "core_fcf", "core_fcf_basis",
    "core_oi_3y", "core_oi_5y", "core_fcf_3y", "core_fcf_5y", "core_fcf_all",
    "core_fx", "core_fx_date", "core_ratio",
    "past_reason", "future_reason", "sf_reason", "next_review_short",
)
CORE_FIELDS = ("core_period", "core_currency", "core_unit", "core_shares_diluted", "core_debt_eq",
               "core_cash", "core_oi", "core_oi_basis", "core_fcf", "core_fcf_basis", "core_fx",
               "core_fx_date", "core_ratio")
CORE_NUMBERS = ("core_shares_diluted", "core_debt_eq", "core_cash", "core_oi", "core_fcf",
                "core_fx", "core_ratio")
MULTIPLES = ("mcap_fcf", "ev_oi", "ev_oi_all_cash")
# Fields a Gate-0 (DNAF) memo may set to n.m. (MODEL section 6.4).
DNAF_NM_FIELDS = set(CORE_FIELDS) | set(MULTIPLES) | set(R10_FIELDS) | {
    "trigger", "past_reason", "future_reason", "sf_reason", "px", "px_unit", "px_date",
    "next_review_short", "quality_past", "quality_future", "sf", "cheapness", "lens"}
# MODEL section 6.1 core_oi_basis and core_fcf_basis grammar for memos at v4.5.0 or later:
# '{period} {line}' then any of the tags, each at most once; and the labels that never name
# an operating-income line (every memo). OI_P (the SOTP perimeter) retired in round 2.
BASIS_PERIOD = r"(?:FY\d{4}|TTM Q[1-4]-\d{4}|LTM Q[1-4]-\d{4}|(?P<avg>FY\d{4}[–-]FY\d{4} avg))"
OI_BASIS_RE = re.compile(r"^%s (?P<line>J1|OI_P|NI basis)(?P<tags>(?: · [^·]+)*)$" % BASIS_PERIOD)
FCF_BASIS_RE = re.compile(r"^%s (?:CFO [−-] maint\. capex \((?P<maint>disclosed|constructed|= all capex)\)|"
                          r"(?P<ni>NI basis))(?P<tags>(?: · [^·]+)*)$" % BASIS_PERIOD)
OI_BASIS_TAGS = ("lease-capitalised", "down-year avg", "fin. income out")
FCF_BASIS_TAGS = ("down-year avg", "fin. income out")
DOWN_YEAR_TAG = "down-year avg"
OI_BASIS_LINES = {"STD": ("J1",), "FI": ("NI basis",)}
OI_BASIS_BANNED_RE = re.compile(r"(?i)\badjusted\b|\bunderlying\b|before special|\bex-\w")
GROUP_B4_RE = re.compile(r"(?m)^[ \t>#*_|-]*B4 Division table")


class ToolError(Exception):
    """Bad input or a failed rule; the message is printed and the tool exits 2."""


# ------------------------------------------------------------------ small helpers

def is_num(text):
    return bool(NUM_RE.match(text or ""))


def dec(text):
    try:
        return Decimal(text)
    except (InvalidOperation, TypeError):
        raise ToolError("not a number: %r" % (text,))


def fmt1(value):
    """One decimal, half up; never '-0.0'."""
    q = value.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
    text = format(q, "f")
    return "0.0" if text == "-0.0" else text


def fmt_pct(value):
    q = (value * 100).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
    text = format(q, "f")
    return ("+" if q > 0 else "") + ("0.0" if text == "-0.0" else text) + "%"


def unit_major(px_unit):
    """(major currency, minor factor) of a quote unit."""
    if px_unit in MINOR_UNITS:
        major, factor = MINOR_UNITS[px_unit]
        return major, Decimal(factor)
    return px_unit, Decimal(1)


def endpoint_symbol(key):
    """The price endpoint's symbol for a key: a US class-share dot becomes a
    hyphen (BRK.B -> BRK-B); exchange suffixes stay (INVE-B.ST, 2330.TW)."""
    if "." in key:
        stem, suffix = key.rsplit(".", 1)
        if suffix not in SUFFIX_UNITS and "." not in stem:
            return stem + "-" + suffix
    return key


def key_suffix(key):
    if "." in key:
        suffix = key.rsplit(".", 1)[1]
        if suffix in SUFFIX_UNITS:
            return suffix
    return ""


def cell_text(value):
    return str(value).replace("|", "\\|")


def reason_base(value):
    """(prefix, token) of a section 7.1 reason: 'unit 8% ROCE' -> ('unit', '8% ROCE')."""
    m = REASON_PREFIX_RE.match(value or "")
    return (m.group(1), m.group(2)) if m else ("", value or "")


def reason_ok(kind, value):
    """A section 7.1 reason (kind past, future or sf): one vocabulary token,
    optionally after one group prefix (unit, sub; never on a Past reason), at
    most three words."""
    if len((value or "").split()) > 3:
        return False
    prefix, token = reason_base(value)
    if kind == "past":
        return not prefix and (token in PAST_REASONS or bool(PAST_LEVEL_RE.match(token)))
    return token in (FUTURE_REASONS if kind == "future" else SF_REASONS)


def model_at_least(version, target=(4, 5, 0)):
    """True when a model_version text such as 'v4.5.0' is at or above target."""
    m = re.match(r"^v?(\d+)\.(\d+)(?:\.(\d+))?", (version or "").strip())
    if not m:
        return False
    return (int(m.group(1)), int(m.group(2)), int(m.group(3) or 0)) >= target


def add_months(day, months):
    """YYYY-MM-DD plus whole months, the day clamped to the month's end."""
    year, month, dom = (int(x) for x in day.split("-"))
    month += months
    year += (month - 1) // 12
    month = (month - 1) % 12 + 1
    last = 31 if month in (1, 3, 5, 7, 8, 10, 12) else 30 if month != 2 else (
        29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28)
    return "%04d-%02d-%02d" % (year, month, min(dom, last))


def review_last_day(short):
    """The latest calendar day a next_review_short token can mean: the date
    itself, the month's or the quarter's last day; None for n.m. or '-'."""
    if DATE_RE.match(short or ""):
        return short
    m = re.match(r"^Q([1-4]) (\d{4})$", short or "")
    if m:
        return add_months("%s-%02d-31" % (m.group(2), int(m.group(1)) * 3), 0)
    m = re.match(r"^([A-Z][a-z]{2}) (\d{4})$", short or "")
    if m and m.group(1) in MONTHS:
        return add_months("%s-%02d-31" % (m.group(2), MONTHS.index(m.group(1)) + 1), 0)
    return None


def run_git(root, args):
    """Read-only git call; (returncode, stdout bytes)."""
    try:
        proc = subprocess.run(["git", "-C", root] + list(args), stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, check=False)
    except OSError as exc:
        return 127, ("%s" % exc).encode()
    return proc.returncode, proc.stdout


def read_repo_text(root, rel, rev=None):
    """A repo file as text: from the working tree, or from `git show REV:path`
    (always when rev is given; as a fallback when the working-tree file cannot
    be opened, e.g. a Windows reserved name such as CON)."""
    if rev is None:
        try:
            with open(os.path.join(root, rel), "rb") as fh:
                return fh.read().decode("utf-8")
        except OSError:
            rev = "HEAD"
    rc, out = run_git(root, ["show", "%s:%s" % (rev, rel)])
    if rc != 0:
        raise ToolError("cannot read %s (working tree or git %s)" % (rel, rev))
    return out.decode("utf-8")


def parse_front_matter(text):
    """Flat `key: value` front matter between the first two '---' lines.
    Values may be double- or single-quoted; an unquoted value loses a trailing
    ' # comment'. Returns {} when there is no front matter."""
    text = text.replace("\r\n", "\n").lstrip("﻿")
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}
    fm = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fm
        m = FM_LINE_RE.match(line)
        if not m:
            continue
        name, value = m.group(1), m.group(2)
        if len(value) >= 2 and value[0] == '"' and value.endswith('"'):
            value = value[1:-1].replace('\\"', '"').replace("\\\\", "\\")
        elif len(value) >= 2 and value[0] == "'" and value.endswith("'"):
            value = value[1:-1].replace("''", "'")
        else:
            value = re.sub(r"\s+#.*$", "", value)
        fm[name] = value.strip()
    return {}


def first_token(value):
    """'FAIL (capital allocation ADVERSE)' -> 'FAIL'; 'n/a — not assessed' -> 'n.m.'."""
    value = (value or "").strip()
    if not value:
        return ""
    if value.lower().startswith(("n/a", "n.m", "—", "-")):
        return NM
    if value.upper().startswith("DO NOT ANALYSE"):
        return "DNAF"
    return re.split(r"[\s(;,]", value, 1)[0].upper()


def sections_of(text):
    """{'## Heading text': [lines]} for a Markdown file (level-2 headings)."""
    out, current = {}, None
    for line in text.replace("\r\n", "\n").split("\n"):
        if line.startswith("## "):
            current = line[3:].strip()
            out[current] = []
        elif current is not None:
            out[current].append(line)
    return out


def table_rows(lines):
    """Markdown table rows -> list of dicts keyed by the lower-cased header."""
    rows, header = [], None
    for line in lines:
        s = line.strip()
        if not s.startswith("|"):
            if header is not None and s:
                break
            continue
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", s.strip("|"))]
        if header is None:
            header = [c.lower() for c in cells]
            continue
        if all(re.match(r"^:?-+:?$", c) for c in cells if c):
            continue
        rows.append(dict(zip(header, cells)))
    return rows


# ------------------------------------------------------------------ metrics (section 7.1b)

def per_share_factor(core, px_unit, fx=None):
    """ps(v) = v x factor (MODEL section 7.1b), or None when the inputs are not established."""
    if not px_unit or px_unit in (OWED, NM):
        return None
    unit = core.get("core_unit", OWED)
    needed = [core.get(name, OWED) for name in ("core_shares_diluted", "core_ratio")]
    rate = fx if fx is not None else core.get("core_fx", OWED)
    if unit not in SCALE or not all(is_num(v) for v in needed) or not is_num(rate):
        return None
    shares, ratio = dec(needed[0]), dec(needed[1])
    if shares <= 0 or ratio <= 0 or dec(rate) <= 0:
        return None
    _major, minor = unit_major(px_unit)
    return SCALE[unit] * dec(rate) * minor * ratio / (shares * Decimal(10) ** 6)


def credit_value(core):
    """The credit in core_unit (MODEL section 7.1b, round 2 V14): core_credit, a
    constant - the material listed holdings at their own buy-line value, which no
    market price moves. A missing field counts as the legacy default (no credit);
    None when the credit is owed ('-') or not a plain number."""
    value = core.get("core_credit", "0")
    if value in (None, ""):
        return Decimal(0)
    if not is_num(value):
        return None
    return dec(value)


def compute_metrics(core, px, px_unit, fx=None):
    """MCap/FCF, EV/OI no-cash and EV/OI all-cash at price px (in px_unit).

    core: the core_ fields as strings. fx: an override for core_fx (a fresher
    rate for the same pair). The constant credit (MODEL section 7.1b, V14)
    reduces the MCap and both EVs; with no credit the formulas are the plain
    ones. Returns three strings: one decimal, 'n.m.' or '-'.
    """
    out = {name: OWED for name in MULTIPLES}
    if not is_num(px):
        return out
    factor = per_share_factor(core, px_unit, fx)
    if factor is None:
        return out
    price = dec(px)
    credit = credit_value(core)
    if credit is None:
        return out
    credit = credit * factor

    def per_share(name):
        value = core.get(name, OWED)
        if value == NM:
            return NM
        if not is_num(value):
            return OWED
        return dec(value) * factor

    fcf = per_share("core_fcf")
    if fcf == NM or (fcf != OWED and fcf <= 0):
        out["mcap_fcf"] = NM
    elif fcf != OWED:
        out["mcap_fcf"] = "0.0" if price - credit <= 0 else fmt1((price - credit) / fcf)
    oi, debt, cash = per_share("core_oi"), per_share("core_debt_eq"), per_share("core_cash")
    if oi == NM or (oi != OWED and oi <= 0):
        out["ev_oi"] = out["ev_oi_all_cash"] = NM
    elif oi != OWED and debt not in (OWED, NM):
        out["ev_oi"] = fmt1((price + debt - credit) / oi)
        if cash not in (OWED, NM):
            out["ev_oi_all_cash"] = fmt1((price + debt - cash - credit) / oi)
    return out


def compute_avg_metrics(core, px, px_unit, fx=None):
    """The averaged readings (MODEL section 7.1b, R10): MCap/FCF and EV/OI no-cash
    at price px on the 3-year and on the 5-year average OI and FCF, with the same
    formulas and credit as the primaries (core_oi_3y / core_fcf_3y, then the 5y
    pair, in place of core_oi / core_fcf). Under FI core_oi_3y is n.m. (EV/OI
    n.m.) and core_fcf_3y the average NI basis (MCap/NI). Returns four strings."""
    out = {}
    for years in ("3y", "5y"):
        probe = dict(core)
        probe["core_oi"] = core.get("core_oi_" + years, OWED)
        probe["core_fcf"] = core.get("core_fcf_" + years, OWED)
        m = compute_metrics(probe, px, px_unit, fx)
        out["mcap_fcf_" + years] = m["mcap_fcf"]
        out["ev_oi_" + years] = m["ev_oi"]
    return out


def fcf_leg_established(row):
    """True when the row's MCap/FCF counts toward the strict line (MODEL section 8.3
    step 3, R6): core_fcf on a P20 maintenance-capex tag, or any FI row (core_oi n.m.:
    the MCap/NI leg, which capex never touches). A pre-R6 FCF - all capex, or a basis
    the register does not record - may overstate MCap/FCF, so its breach is not
    established (round-2 review fix, 2026-10-07)."""
    if row.get("core_oi") == NM:
        return True
    m = FCF_BASIS_RE.match(row.get("core_fcf_basis") or "")
    return bool(m and m.group("maint"))


def mcap_fcf_breach(mcap_fcf):
    """True when an MCap/FCF reading fails the strict line: n.m. (no FCF leg) or above 8.0."""
    return mcap_fcf == NM or bool(MULT_RE.match(mcap_fcf) and Decimal(mcap_fcf) > 8)


def strict_failures(row, px, fx=None):
    """The strict all-pass line at px (MODEL section 8.3 step 3, R10): the primaries
    the core numbers establish that fail it - MCap/FCF above 8.0 (or n.m.: no FCF
    leg; counted only where fcf_leg_established) and EV/OI no-cash above 7.0 (or
    n.m. on a non-positive OI; under FI, where core_oi is n.m., the MCap/NI leg
    alone). [] when every established primary passes or none is established ('-')."""
    m = compute_metrics(row, px, row.get("px_unit", OWED), fx)
    fails = []
    if fcf_leg_established(row) and mcap_fcf_breach(m["mcap_fcf"]):
        fails.append("MCap/FCF %s" % m["mcap_fcf"])
    if row.get("core_oi") != NM and (m["ev_oi"] == NM or (MULT_RE.match(m["ev_oi"]) and Decimal(m["ev_oi"]) > 7)):
        fails.append("EV/OI no-cash %s" % m["ev_oi"])
    return fails


def status_hint(row, px, fx=None, rows_by_key=None, holding_px=None, as_of=None):
    """(status, distance) of a key at px against its trigger (MODEL section 8.3
    step 3): IN RANGE at or under the trigger, NEAR within 10%, FAR beyond;
    'n.m.' without a numeric trigger. A key whose core numbers establish the
    primaries is IN RANGE only if MCap/FCF <= 8 and EV/OI no-cash <= 7 both hold
    at px (R10: the strict line; it also covers a row still carrying a pre-R10
    all-cash trigger; the MCap/FCF leg counts only on a P20 basis, R6). Holding credits are a constant (V14), so no holding's own
    price enters: rows_by_key, holding_px and as_of are accepted and unused."""
    trigger = row.get("trigger", OWED)
    if not is_num(px) or not is_num(trigger) or dec(trigger) <= 0:
        return NM, None
    dist = dec(px) / dec(trigger) - 1
    status = "IN RANGE" if dist <= 0 else ("NEAR" if dist <= Decimal("0.10") else "FAR")
    if status == "IN RANGE" and strict_failures(row, px, fx):
        status = "NEAR"
    return status, dist


# ------------------------------------------------------------------ rows

def gates_failed(past, future, sf):
    return int(past == "WEAK") + int(future == "WEAK") + int(sf == "FAIL")


def section_for(verdict, gates):
    if verdict == "AVOID":
        return "AVOID-1" if gates == 1 else ("AVOID-2" if gates >= 2 else "")
    return verdict if verdict in VERDICTS else ""


def grade_cell(grade, reason, sf=False):
    has_reason = reason not in ("", OWED, NM)
    if sf and grade == "PASS" and has_reason:
        return "PASS CAUTION · %s" % reason
    return "%s · %s" % (grade, reason) if has_reason else grade


def pair_cell(a, b):
    """'{3y} · {5y}' (each side a multiple or n.m.); '-' when both are owed."""
    if a == OWED and b == OWED:
        return OWED
    return "%s · %s" % (a, b)


def master_cells(row):
    return [row["key"], row["company"], row["memo_date"], row["memo_version"], row["verdict"],
            grade_cell(row["past"], row["past_reason"]),
            grade_cell(row["future"], row["future_reason"]),
            grade_cell(row["sf"], row["sf_reason"], sf=True),
            row["px"], row["trigger"], row["mcap_fcf"], row["ev_oi"],
            pair_cell(row["mcap_fcf_3y"], row["mcap_fcf_5y"]), pair_cell(row["ev_oi_3y"], row["ev_oi_5y"]),
            row["next_review_short"]]


def portfolio_cells(row):
    return [row["key"], row["zone"], row["px"], row["add_band"], row["sell_line"],
            row["last_zone_check"], row["next_review_short"]]


def table_line(cells):
    return "| " + " | ".join(cell_text(c) for c in cells) + " |"


def sort_key(row):
    """EV/OI ascending, then n.m., then '-'; ties by key. DNAF by key."""
    if row["section"] == "DNAF":
        return (SECTION_ORDER.index("DNAF"), 0, Decimal(0), row["key"])
    rank = SECTION_ORDER.index(row["section"]) if row["section"] in SECTION_ORDER else len(SECTION_ORDER)
    value = row.get("ev_oi", OWED)
    if MULT_RE.match(value or ""):
        return (rank, 0, Decimal(value), row["key"])
    return (rank, 1 if value == NM else 2, Decimal(0), row["key"])


def canonical(rows):
    return sorted(rows, key=sort_key)


def validate_row(row):
    """Field rules for one register.csv row; returns a list of problems."""
    p = []
    key = row.get("key", "")
    for name in CSV_HEADER:
        value = row.get(name)
        if value is None or value == "":
            p.append("%s: empty (write '-' for owed, 'n.m.' for not meaningful)" % name)
        elif "\n" in value or "\r" in value:
            p.append("%s: line break inside a value" % name)
    if p:
        return p
    if not KEY_RE.match(key):
        p.append("key: not a section 7.1a key")
    verdict = row["verdict"]
    dnaf = verdict == "DNAF"
    if verdict not in VERDICTS:
        p.append("verdict: %r is not one of %s" % (verdict, "/".join(VERDICTS)))
    for name, allowed in (("past", GRADES), ("future", GRADES), ("sf", SF_GRADES)):
        if row[name] not in allowed and not (dnaf and row[name] == NM):
            p.append("%s: %r is not one of %s" % (name, row[name], "/".join(allowed)))
    gates = gates_failed(row["past"], row["future"], row["sf"])
    if row["gates_failed"] != str(gates):
        p.append("gates_failed: %s, but the grades give %d" % (row["gates_failed"], gates))
    section = section_for(verdict, gates)
    if verdict == "AVOID" and gates == 0:
        p.append("verdict AVOID with no failed gate (register-integrity breach)")
    elif verdict in ("BUY", "WATCH") and gates:
        p.append("verdict %s with %d failed gate(s) breaks the section 2 verdict mapping" % (verdict, gates))
    if section and row["section"] != section:
        p.append("section: %s, but verdict and gates give %s" % (row["section"], section))
    for name, kind in (("past_reason", "past"), ("future_reason", "future"), ("sf_reason", "sf")):
        value = row[name]
        if value in (OWED, NM):
            continue
        if not reason_ok(kind, value):
            p.append("%s: %r is not in the section 7.1 reason vocabulary" % (name, value))
    p += future_reason_problems(row["future"], row["future_reason"])
    m = MEMO_PATH_RE.match(row["memo_path"])
    if not m or m.group("dir") != key or m.group("key") != key or m.group("date") != row["memo_date"]:
        p.append("memo_path: %r is not memos/%s/%s_{memo_date}_GSC.md" % (row["memo_path"], key, key))
    if not DATE_RE.match(row["memo_date"]):
        p.append("memo_date: not YYYY-MM-DD")
    if row["memo_version"] != OWED and not VER_RE.match(row["memo_version"]):
        p.append("memo_version: %r is not a bare vN" % row["memo_version"])
    if row["isin"] != OWED and not ISIN_RE.match(row["isin"]):
        p.append("isin: %r is not an ISIN" % row["isin"])
    for name in ("px", "trigger", "add_band", "sell_line"):
        value = row[name]
        if value not in (OWED, NM) and not is_num(value):
            p.append("%s: %r is not a plain number" % (name, value))
    if row["px_unit"] not in (OWED, NM) and not UNIT_RE.match(row["px_unit"]):
        p.append("px_unit: %r is not a quote unit" % row["px_unit"])
    for name in ("px_date", "core_fx_date"):
        if row[name] not in (OWED, NM) and not DATE_RE.match(row[name]):
            p.append("%s: not YYYY-MM-DD" % name)
    if row["px_source"] != OWED and not PX_SOURCE_RE.match(row["px_source"]):
        p.append("px_source: %r is not 'memo' or 'SWEEP YYYY-MM-DD'" % row["px_source"])
    for name in MULTIPLES + AVG_MULTIPLES:
        if row[name] not in (OWED, NM) and not MULT_RE.match(row[name]):
            p.append("%s: %r is not a one-decimal multiple" % (name, row[name]))
    for name in AVG_CORE + ("core_fcf_all",):
        if row[name] not in (OWED, NM) and not is_num(row[name]):
            p.append("%s: %r is not a plain number, n.m. or -" % (name, row[name]))
        elif is_num(row[name]) and decimals(row[name]) > MAX_DECIMALS:
            p.append("%s: %r has more than %d decimal places" % (name, row[name], MAX_DECIMALS))
    basis = row["trigger_basis"]
    if basis not in TRIGGER_BASES and not (dnaf and basis == NM):
        p.append("trigger_basis: %r is not one of %s" % (basis, "/".join(TRIGGER_BASES)))
    elif basis == "all-cash" and model_at_least(row["model_version"]):
        p.append("trigger_basis: all-cash, but a memo written under MODEL %s prints the no-cash bound as its "
                 "trigger (R10)" % row["model_version"])
    if row["next_review_short"] != OWED and not NEXT_REVIEW_RE.match(row["next_review_short"]):
        p.append("next_review_short: %r is not YYYY-MM-DD, Qn YYYY, Mon YYYY or n.m." % row["next_review_short"])
    if row["held"] not in ("true", "false"):
        p.append("held: %r is not true/false" % row["held"])
    elif row["held"] == "true":
        if row["zone"] != OWED and not ZONE_RE.match(row["zone"]):
            p.append("zone: %r is not ADD/HOLD/SELL-FLAG [SRn]" % row["zone"])
        if row["last_zone_check"] != OWED and not DATE_RE.match(row["last_zone_check"]):
            p.append("last_zone_check: not YYYY-MM-DD")
        if basis == "no-cash" and is_num(row["trigger"]) and is_num(row["add_band"]) and \
                dec(row["trigger"]) != dec(row["add_band"]):
            p.append("add_band: %s, but a held trigger at the no-cash bound is the ADD band (P21, R10): trigger %s"
                     % (row["add_band"], row["trigger"]))
    else:
        for name in ("zone", "add_band", "sell_line", "last_zone_check", "avg_cost"):
            if row[name] != NM:
                p.append("%s: %r on a name that is not held (write n.m.)" % (name, row[name]))
    if row["core_unit"] not in (OWED, NM) and row["core_unit"] not in SCALE:
        p.append("core_unit: %r is not k, m or bn" % row["core_unit"])
    if row["core_currency"] not in (OWED, NM) and not CCY_RE.match(row["core_currency"]):
        p.append("core_currency: %r is not an ISO code" % row["core_currency"])
    for name in CORE_NUMBERS:
        if row[name] not in (OWED, NM) and not is_num(row[name]):
            p.append("%s: %r is not a plain number" % (name, row[name]))
    for name in ("px", "trigger", "add_band", "sell_line") + CORE_NUMBERS:
        if is_num(row[name]) and decimals(row[name]) > MAX_DECIMALS:
            p.append("%s: %r has more than %d decimal places (floating-point noise; write the source's "
                     "precision)" % (name, row[name], MAX_DECIMALS))
    if row["core_source"] not in ("memo", "rebuild", "rebuild-assisted", OWED):
        p.append("core_source: %r is not memo, rebuild, rebuild-assisted or -" % row["core_source"])
    p += validate_lens_fields(row)
    return p


def future_reason_problems(grade, reason):
    """MODEL section 7.1 (R7): a Future STRONG prints the grade alone (n.m.); an
    ADEQUATE prints n.m. or the concentration flag it carries as its caveat
    (customer conc. / supplier conc., a group prefix allowed); '-' is owed."""
    if reason in (OWED, NM) or grade not in ("STRONG", "ADEQUATE"):
        return []
    if grade == "ADEQUATE" and reason_base(reason)[1] in FUTURE_CAVEATS and len(reason.split()) <= 3:
        return []
    if grade == "STRONG":
        return ["future_reason: %r, but Future STRONG prints the grade alone: write n.m." % reason]
    return ["future_reason: %r, but a Future ADEQUATE prints n.m. or its concentration caveat (%s)"
            % (reason, " / ".join(FUTURE_CAVEATS))]


def validate_lens_fields(fields):
    """holding_keys and core_credit (MODEL sections 6.1, 7.1b; round 2, V14), for a
    register.csv row or memo front matter ('-' = owed is accepted here; lint-memo
    refuses it in a memo)."""
    p = []
    keys = fields.get("holding_keys", NM)
    if keys not in (NM, OWED) and not all(KEY_RE.match(k.strip()) for k in keys.split(";")):
        p.append("holding_keys: %r is not n.m. or ';'-separated section 7.1a keys" % keys)
    credit = fields.get("core_credit", LENS_DEFAULTS["core_credit"])
    if credit != OWED:
        if not is_num(credit):
            p.append("core_credit: %r is not a plain number (0 when there is no credit)" % (credit,))
        elif decimals(credit) > MAX_DECIMALS:
            p.append("core_credit: %r has more than %d decimal places" % (credit, MAX_DECIMALS))
        elif dec(credit) < 0:
            p.append("core_credit: %s is negative (a holding credit is never negative, V14)" % credit)
    return p


# ------------------------------------------------------------------ register.csv I/O

# The two headers register.csv carried before lean-2 (an older revision read for
# comparison): before the v4.5.0 lens columns, and lean-1 with the retired SOTP columns.
LEGACY_HEADER = CSV_HEADER[:CSV_HEADER.index("core_source") + 1]
LEAN1_HEADER = LEGACY_HEADER + list(RETIRED_FIELDS)
LEGACY_HEADERS = (LEGACY_HEADER, LEAN1_HEADER)


def from_legacy(row):
    """A row read under an older header, in lean-2 form: the lens columns at their
    legacy defaults (lean-1's sotp_keys becomes holding_keys and its credits one
    constant, fix + mkt, the credit at the price it was struck at) and the round-2
    columns at theirs (an all-cash trigger, every average owed)."""
    out = {name: row[name] for name in LEGACY_HEADER}
    out.update(LENS_DEFAULTS)
    if "sotp_keys" in row:
        out["holding_keys"] = row["sotp_keys"] or NM
        fix, mkt = row.get("core_credit_fix", "0"), row.get("core_credit_mkt", "0")
        out["core_credit"] = plain(dec(fix) + dec(mkt)) if is_num(fix) and is_num(mkt) else OWED
    out.update(R10_DEFAULTS)
    return out


def read_csv_text(text, label=CSV_FILE, legacy_ok=False):
    """(rows, problems). The header must be exact. legacy_ok: a register.csv
    written under an older header (LEGACY_HEADERS: an older revision read for
    comparison - a check base, a merge base, a digest's first parent - or the
    attended retrigger's landing read) is read in lean-2 form (from_legacy)."""
    if legacy_ok:
        first = text.lstrip("﻿").split("\n", 1)[0].rstrip("\r")
        header = next((h for h in LEGACY_HEADERS if first == ",".join(h)), None)
        if header is not None:
            rows, problems = [], []
            reader = csv.reader(io.StringIO(text.lstrip("﻿").replace("\r\n", "\n"), newline=""))
            next(reader)
            for number, cells in enumerate(reader, start=2):
                if len(cells) != len(header):
                    raise ToolError("%s line %d: %d fields, expected %d" % (label, number, len(cells),
                                                                           len(header)))
                rows.append(from_legacy(dict(zip(header, cells))))
            return rows, problems
    problems = []
    if text.startswith("﻿"):
        problems.append("%s: starts with a BOM" % label)
        text = text[1:]
    if "\r" in text:
        problems.append("%s: CR line ends (LF only)" % label)
        text = text.replace("\r\n", "\n")
    if text and not text.endswith("\n"):
        problems.append("%s: no final line end" % label)
    reader = csv.reader(io.StringIO(text, newline=""))
    try:
        header = next(reader)
    except StopIteration:
        raise ToolError("%s is empty" % label)
    if header != CSV_HEADER:
        raise ToolError("%s: header is not the section 7.1b header (%d columns, expected %d)"
                        % (label, len(header), len(CSV_HEADER)))
    rows = []
    for number, cells in enumerate(reader, start=2):
        if len(cells) != len(CSV_HEADER):
            raise ToolError("%s line %d: %d fields, expected %d" % (label, number, len(cells), len(CSV_HEADER)))
        rows.append(dict(zip(CSV_HEADER, cells)))
    return rows, problems


def load_csv(root):
    path = os.path.join(root, CSV_FILE)
    try:
        with open(path, "rb") as fh:
            data = fh.read()
    except OSError:
        raise ToolError("%s not found under %s" % (CSV_FILE, root))
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        raise ToolError("%s is not UTF-8" % CSV_FILE)
    return read_csv_text(text)


def csv_text(rows):
    buf = io.StringIO(newline="")
    writer = csv.writer(buf, lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
    writer.writerow(CSV_HEADER)
    for row in canonical(rows):
        writer.writerow([row[name] for name in CSV_HEADER])
    return buf.getvalue()


def write_text(path, text):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    os.replace(tmp, path)


# ------------------------------------------------------------------ render

def render(rows, version, date):
    """The complete _REGISTER.md for these rows. Raises ToolError on a breach."""
    if not VER_RE.match(version or ""):
        raise ToolError("--version must be vN (got %r)" % (version,))
    if not DATE_RE.match(date or ""):
        raise ToolError("--date must be YYYY-MM-DD (got %r)" % (date,))
    errors, seen = [], set()
    for row in rows:
        if row["key"] in seen:
            errors.append("%s: duplicate key" % row["key"])
        seen.add(row["key"])
        errors += ["%s: %s" % (row["key"], e) for e in validate_row(row)]
        if row.get("section") not in SECTION_ORDER:
            errors.append("%s: unknown section %r" % (row["key"], row.get("section")))
    if errors:
        raise ToolError("register.csv breaks the section 7.1 rules:\n  " + "\n  ".join(errors))
    rows = canonical(rows)
    by_section = {s: [r for r in rows if r["section"] == s] for s in SECTION_ORDER}
    held = sorted((r for r in rows if r["held"] == "true"), key=lambda r: r["key"])
    for row in rows:
        cells = master_cells(row) + (portfolio_cells(row) if row["held"] == "true" else [])
        for cell in cells:
            if len(cell_text(cell)) > CELL_CAP:
                errors.append("%s: cell over %d characters: %r" % (row["key"], CELL_CAP, cell[:60]))
    if errors:
        raise ToolError("register cells break the section 7.1 cap:\n  " + "\n  ".join(errors))
    n = {s: len(by_section[s]) for s in SECTION_ORDER}
    avoid = n["AVOID-1"] + n["AVOID-2"]
    split = "BUY %d · WATCH %d · AVOID %d (one gate %d · two+ %d) · DNAF %d" % (
        n["BUY"], n["WATCH"], avoid, n["AVOID-1"], n["AVOID-2"], n["DNAF"])
    out = [
        "---",
        "register_title: %s" % REGISTER_TITLE,
        "register_version: %s" % version,
        "register_date: %s" % date,
        'register_format: "%s"' % REGISTER_FORMAT,
        'data: "register.csv — every column plus core numbers (MODEL §7.1b)"',
        'archive: "archive/registers/{YYYY}/ — one verbatim snapshot per outgoing version, .md and .csv"',
        "names_total: %d" % len(rows),
        'verdict_split: "%s"' % split,
        "portfolio_names: %d" % len(held),
        'ordering: "v4.5.0 — PORTFOLIO → BUY → WATCH → AVOID one gate → AVOID two+ → DNAF; '
        'EV/OI ascending, n.m. then - last; DNAF alphabetical"',
        "---",
        "",
        "# %s (%s · %s)" % (REGISTER_TITLE, version, date),
        "",
        LEGEND[0],
        LEGEND[1],
        "",
        "## PORTFOLIO (%d)" % len(held),
        "",
    ]
    if held:
        out.append(table_line(PORTFOLIO_COLUMNS))
        out.append("|" + "---|" * len(PORTFOLIO_COLUMNS))
        out += [table_line(portfolio_cells(r)) for r in held]
    else:
        out.append("None.")
    for section in SECTION_ORDER:
        out += ["", "## %s (%d)" % (SECTION_TITLES[section], n[section]), ""]
        if by_section[section]:
            out.append(table_line(MASTER_COLUMNS))
            out.append("|" + "---|" * len(MASTER_COLUMNS))
            out += [table_line(master_cells(r)) for r in by_section[section]]
        else:
            out.append("None.")
    return "\n".join(out) + "\n"


def register_front_matter(root, rev=None):
    text = read_repo_text(root, REGISTER_FILE, rev)
    return parse_front_matter(text), text


# ------------------------------------------------------------------ memo -> row

def memo_number(fm, name, notes, key):
    """A machine number field from memo front matter: the plain number, 'n.m.',
    or '-' (missing or not plain: backfill owed, reported)."""
    value = fm.get(name)
    if value is None or value == "":
        notes.append("BACKFILL %s %s" % (key, name))
        return OWED
    if value == NM or is_num(value):
        return value
    notes.append("BACKFILL %s %s (not a plain number: %r)" % (key, name, value[:60]))
    return OWED


def memo_text_field(fm, name, notes, key):
    value = fm.get(name)
    if value is None or value == "":
        notes.append("BACKFILL %s %s" % (key, name))
        return OWED
    return value


def lens_fields_from_memo(row, fm, notes, key):
    """holding_keys and core_credit from memo front matter (MODEL v4.5.0 section
    6.1, round 2). A memo written before the lens fields existed, or under the
    lean-1 fields that round 2 retired, has no credit here: the legacy defaults,
    no backfill owed. A field the memo states but not as a plain value is owed
    ('-', reported)."""
    for name in LENS_DEFAULTS:
        value = fm.get(name)
        if value is None or value == "":
            row[name] = LENS_DEFAULTS[name]
            continue
        if name == "holding_keys":
            row[name] = NM if value in ("—", "none", NM) else value
        else:
            row[name] = value if is_num(value) else OWED
        if row[name] == OWED:
            notes.append("BACKFILL %s %s (not a plain number: %r)" % (key, name, value[:60]))
    problems = validate_lens_fields(row)
    if problems:
        for name in LENS_DEFAULTS:
            row[name] = OWED
        notes.append("BACKFILL %s lens fields: %s" % (key, "; ".join(problems)))


def r10_fields_from_memo(row, fm, notes, key):
    """The round-2 fields (R10, R1, R6) from memo front matter: trigger_basis, the
    latest-FY all-capex FCF, the 3- and 5-year averages and their multiples at
    the row's px (a multiple the memo does not print is recomputed). A memo
    written before v4.5.0 carries none of them: the legacy defaults (all-cash,
    '-'), no backfill owed. A v4.5.0 memo that lacks one, or states it but not
    as a plain value, owes it ('-', reported)."""
    current = model_at_least(row["model_version"])
    if not current and not any(fm.get(name) for name in R10_FIELDS):
        row.update(R10_DEFAULTS)
        return
    basis = fm.get("trigger_basis") or ""
    if basis in TRIGGER_BASES or (basis == NM and row["verdict"] == "DNAF"):
        row["trigger_basis"] = basis
    else:
        row["trigger_basis"] = R10_DEFAULTS["trigger_basis"]
        notes.append("BACKFILL %s trigger_basis%s" % (key, (" (not no-cash or all-cash: %r)" % basis[:60])
                                                       if basis else ""))
    for name in ("core_fcf_all",) + AVG_CORE:
        row[name] = memo_number(fm, name, notes, key)
    computed = compute_avg_metrics(row, row["px"], row["px_unit"])
    for name in AVG_MULTIPLES:
        value = fm.get(name)
        if value == NM or MULT_RE.match(value or ""):
            row[name] = value
        else:
            row[name] = computed[name]
            notes.append("BACKFILL %s %s%s" % (key, name, " (recomputed from core numbers)"
                                               if computed[name] != OWED else ""))


def row_from_memo(memo_path, text, notes):
    """The register.csv row a memo's front matter yields (memo wins). Held
    fields come from the memo here; apply() keeps the register's own held
    flag and position record."""
    m = MEMO_PATH_RE.match(memo_path)
    if not m or m.group("dir") != m.group("key"):
        raise ToolError("%s is not memos/{KEY}/{KEY}_{date}_GSC.md" % memo_path)
    key = m.group("key")
    fm = parse_front_matter(text)
    if not fm:
        raise ToolError("%s has no front matter" % memo_path)
    if fm.get("ticker", key) != key:
        notes.append("NOTE %s ticker %r differs from the memo folder; the folder key is used"
                      % (key, fm.get("ticker")))
    row = {name: OWED for name in CSV_HEADER}
    row["key"] = key
    row["company"], note = company_note(fm.get("company") or OWED)
    if note:
        notes.append("NORMALISED %s company: note %r dropped from the cell (lines and former names belong in "
                      "aliases:)" % (key, note[:60]))
    isin = (fm.get("isin") or "").strip()
    row["isin"] = isin if ISIN_RE.match(isin) else OWED
    if row["isin"] == OWED:
        notes.append("BACKFILL %s isin (%s)" % (key, isin or "missing"))
    aliases = fm.get("aliases")
    if aliases is None or aliases == "":
        notes.append("BACKFILL %s aliases" % key)
    else:
        row["aliases"] = NM if aliases in ("—", NM, "none") else aliases
    for name, src in (("verdict", "verdict"), ("past", "quality_past"), ("future", "quality_future"),
                      ("sf", "sf")):
        raw = fm.get(src, "")
        token = first_token(raw)
        if token != raw:
            notes.append("NORMALISED %s %s: %r -> %r" % (key, src, raw[:60], token))
        row[name] = token or OWED
    gates = gates_failed(row["past"], row["future"], row["sf"])
    row["gates_failed"] = str(gates)
    row["section"] = section_for(row["verdict"], gates) or OWED
    for name in ("past_reason", "future_reason", "sf_reason"):
        row[name] = memo_text_field(fm, name, notes, key)
    row["memo_path"] = memo_path
    row["memo_date"] = m.group("date")
    if fm.get("memo_date") and fm.get("memo_date") != m.group("date"):
        notes.append("NOTE %s memo_date %s differs from the file name date %s; the file name is used"
                     % (key, fm.get("memo_date"), m.group("date")))
    version = re.match(r"^v\d+", fm.get("memo_version", ""))
    row["memo_version"] = version.group(0) if version else OWED
    if version and version.group(0) != fm.get("memo_version"):
        notes.append("NORMALISED %s memo_version: %r -> %r" % (key, fm.get("memo_version", "")[:60],
                                                               version.group(0)))
    row["model_version"] = (fm.get("model_version") or OWED).split()[0]
    row["px"] = memo_number(fm, "px", notes, key)
    row["px_unit"] = memo_text_field(fm, "px_unit", notes, key)
    row["px_date"] = memo_text_field(fm, "px_date", notes, key)
    row["px_source"] = "memo"
    row["trigger"] = memo_number(fm, "trigger", notes, key)
    for name in CORE_FIELDS:
        if name in CORE_NUMBERS:
            row[name] = memo_number(fm, name, notes, key)
        else:
            row[name] = memo_text_field(fm, name, notes, key)
    row["core_source"] = "memo" if all(row[n] != OWED for n in CORE_FIELDS) else OWED
    lens_fields_from_memo(row, fm, notes, key)
    r10_fields_from_memo(row, fm, notes, key)
    computed = compute_metrics(row, row["px"], row["px_unit"])
    for name in MULTIPLES:
        value = fm.get(name)
        if value == NM or MULT_RE.match(value or ""):
            row[name] = value
        else:
            row[name] = computed[name]
            notes.append("BACKFILL %s %s%s" % (key, name, " (recomputed from core numbers)"
                                               if computed[name] != OWED else ""))
    row["next_review_short"] = memo_text_field(fm, "next_review_short", notes, key)
    held = first_token(fm.get("position", "")) == "HELD"
    row["held"] = "true" if held else "false"
    if held:
        row["zone"] = memo_text_field(fm, "zone", notes, key)
        row["add_band"] = memo_number(fm, "add_band", notes, key)
        row["sell_line"] = memo_number(fm, "sell_flag_line", notes, key)
        row["last_zone_check"] = row["px_date"]
        row["avg_cost"] = fm.get("avg_cost") or OWED
    else:
        for name in ("zone", "add_band", "sell_line", "last_zone_check", "avg_cost"):
            row[name] = NM
    return row


def legacy_fill(row, text, old, notes):
    """A memo written before MODEL v4.5.0 carries no machine fields (no `px`).
    Fill what the one-time rebuild reads from such memos - the price
    statement, the trigger band, the worst-of-four level, the next-review
    text and the multiples the memo prints at its own price - never guessed;
    the rest stays '-'. Returns the notes without the BACKFILL lines of the
    fields it filled, plus one LEGACY line."""
    key = row["key"]
    fm = parse_front_matter(text)
    filled = []
    old = old or {}
    if row["isin"] == OWED:
        token = ((fm.get("isin") or "").strip().split() or [""])[0]
        if ISIN_RE.match(token):
            row["isin"] = token
            filled.append("isin")
    if row["aliases"] == OWED and old.get("aliases") not in (None, OWED):
        row["aliases"] = old["aliases"]
        filled.append("aliases")
    dnaf = row["verdict"] == "DNAF"
    quote_unit = old.get("px_unit") if UNIT_RE.match(old.get("px_unit") or "") else default_unit(key)
    memo_px, memo_unit, memo_day, _how = parse_memo_price(fm.get("price_at_memo", ""), key, fm.get("currency", ""),
                                                          quote_unit)
    memo_q = None
    if memo_px is not None and memo_unit:
        memo_q, _conv = to_quote_unit(memo_px, memo_unit, quote_unit)
    if memo_q is not None:
        row["px"], row["px_unit"], row["px_source"] = plain(memo_q), quote_unit, "memo"
        filled += ["px", "px_unit"]
        if memo_day:
            row["px_date"] = memo_day
            filled.append("px_date")
    if dnaf:
        row["trigger"] = row["next_review_short"] = NM
        for name in MULTIPLES + ("past_reason", "future_reason", "sf_reason"):
            if row[name] == OWED:
                row[name] = NM
        filled += ["trigger", "next_review_short"] + list(MULTIPLES)
    else:
        value, unit, how = operative_trigger(fm.get("trigger_band", ""), key, memo_unit)
        if how == "n.m.":
            row["trigger"] = NM
            filled.append("trigger")
        elif value is not None and row["px_unit"] != OWED:
            q, _conv = to_quote_unit(value, unit, row["px_unit"])
            if q is not None:
                row["trigger"] = plain(q)
                filled.append("trigger")
        if row["next_review_short"] == OWED:
            short = parse_next_review_short(fm.get("next_review", ""), row["memo_date"])
            if short != OWED:
                row["next_review_short"] = short
                filled.append("next_review_short")
        if memo_q is not None and row["core_source"] == OWED:
            printed = memo_multiples(text)
            for name in MULTIPLES:
                if printed.get(name) not in (None, OWED):
                    row[name] = printed[name]
                    filled.append(name)
        if row["past_reason"] == OWED and row["past"] in ("STRONG", "ADEQUATE"):
            level, _quote = past_level(text)
            if level:
                row["past_reason"] = level
                filled.append("past_reason")
        if row["future_reason"] == OWED and row["future"] in ("STRONG", "ADEQUATE"):
            row["future_reason"] = NM
            filled.append("future_reason")
        if row["sf_reason"] == OWED and row["sf"] == "PASS":
            sf_text = (fm.get("sf") or "").lower()
            if not (re.search(r"caution|\b[1-9] flag|flag pair", sf_text) and not re.search(r"\b0 flags?\b", sf_text)):
                row["sf_reason"] = NM
                filled.append("sf_reason")
    kept = [n for n in notes if not any(n == "BACKFILL %s %s" % (key, f) or n.startswith("BACKFILL %s %s " % (key, f))
                                        for f in filled)]
    kept.append("LEGACY %s memo has no v4.5.0 machine fields (model_version %s); read from its text as the "
                "one-time rebuild does: %s" % (key, row["model_version"], ", ".join(sorted(set(filled))) or "nothing"))
    return kept


def keep_position(new, old):
    """The held flag and position record are read-only for apply: they change
    only through an attended position event (MODEL section 7.3)."""
    notes = []
    held = old["held"] if old else "false"
    if new["held"] != held:
        notes.append("HELD-MISMATCH %s memo position says %s, register held=%s; register kept "
                     "(open item for Jakub)" % (new["key"], "HELD" if new["held"] == "true" else "not held", held))
    if held == "true":
        new["avg_cost"] = old["avg_cost"]
        if new["held"] != "true":
            # The memo has no position fields: keep the register's record.
            for name in ("zone", "add_band", "sell_line", "last_zone_check"):
                new[name] = old[name]
        else:
            # The memo wins on zone and lines; the last zone check is the later date.
            old_check, new_check = old["last_zone_check"], new["last_zone_check"]
            if DATE_RE.match(old_check) and (not DATE_RE.match(new_check) or old_check > new_check):
                new["last_zone_check"] = old_check
    else:
        for name in ("zone", "add_band", "sell_line", "last_zone_check", "avg_cost"):
            new[name] = NM
    new["held"] = held
    return notes


# ------------------------------------------------------------------ apply

def parse_row_file(text):
    fm = parse_front_matter(text)
    if not fm.get("row_type"):
        raise ToolError("row file has no row_type in its front matter")
    return fm, sections_of(text)


def apply_sweep(rows_by_key, fm, sections):
    run_date = fm.get("run_date", "")
    if not DATE_RE.match(run_date):
        raise ToolError("SWEEP row file: run_date %r is not YYYY-MM-DD" % run_date)
    refresh = None
    for title, lines in sections.items():
        if title.lower().startswith("price/ordering refresh"):
            refresh = table_rows(lines)
    if refresh is None:
        raise ToolError("SWEEP row file has no '## Price/ordering refresh' section")
    fx = {}
    for title, lines in sections.items():
        if title.lower() == "fx":
            for r in table_rows(lines):
                pair, rate, day = r.get("pair", ""), r.get("rate", ""), r.get("date", "")
                if re.match(r"^[A-Z]{3}/[A-Z]{3}$", pair) and is_num(rate) and DATE_RE.match(day):
                    fx[pair] = (rate, day)
    sweep_zones = sweep_portfolio_zones(sections)
    changes, skips = [], []
    for r in refresh:
        key = r.get("key", "").strip("` ")
        px, unit, close = r.get("px", ""), r.get("px unit", ""), r.get("close date", "")
        row = rows_by_key.get(key)
        if row is None:
            skips.append({"key": key, "reason": "not in the register"})
            continue
        if not is_num(px) or not DATE_RE.match(close):
            skips.append({"key": key, "reason": "Px %r or close date %r unparseable" % (px, close)})
            continue
        if row["section"] in ("AVOID-2", "DNAF") and row["held"] != "true":
            skips.append({"key": key, "reason": "out of SWEEP scope (%s, never refreshed)" % row["section"]})
            continue
        adopted = False
        if row["px_unit"] == OWED and UNIT_RE.match(unit):
            # A row with no quote unit yet (a legacy memo without one) takes the
            # endpoint's currency, which is what px_unit means (MODEL section 7.1a).
            row["px_unit"], adopted = unit, True
        if unit != row["px_unit"]:
            skips.append({"key": key, "reason": "unit mismatch: sweep %r, register px_unit %r" % (unit, row["px_unit"])})
            continue
        if DATE_RE.match(row["px_date"]) and close <= row["px_date"]:
            skips.append({"key": key, "reason": "close %s not later than the register's px_date %s"
                          % (close, row["px_date"])})
            continue
        if row["px_source"] == "memo" and row["memo_date"] > close:
            skips.append({"key": key, "reason": "row comes from a memo dated %s, after the close %s"
                          % (row["memo_date"], close)})
            continue
        old = dict(row)
        row["px"], row["px_date"], row["px_source"] = px, close, "SWEEP %s" % run_date
        major, _minor = unit_major(row["px_unit"])
        rate = None
        if row["core_currency"] not in (OWED, NM) and row["core_currency"] != major:
            pair = "%s/%s" % (row["core_currency"], major)
            if pair in fx and (not DATE_RE.match(row["core_fx_date"]) or fx[pair][1] > row["core_fx_date"]):
                row["core_fx"], row["core_fx_date"] = fx[pair]
                rate = fx[pair][0]
        row.update(compute_metrics(row, px, row["px_unit"], rate))
        row.update(compute_avg_metrics(row, px, row["px_unit"], rate))
        change = {"key": key, "old": table_line(master_cells(old)), "new": table_line(master_cells(row))}
        notes = []
        if adopted:
            notes.append("px_unit was '-': the endpoint currency %s adopted" % unit)
        if row["held"] == "true":
            # MODEL section 7.2 (J11): the date moves only when the sweep's zone equals the
            # Portfolio Zone; a changed held zone keeps it (review request; morning digest).
            reg = ZONE_WORD_RE.match(row["zone"] or "")
            swept = sweep_zones.get(key)
            if reg and swept == reg.group(1):
                row["last_zone_check"] = close
            else:
                notes.append("held zone: sweep %s, Portfolio %s - Last zone check %s kept (a REVIEW sets the "
                             "zone; reported in the digest)" % (swept or "missing", row["zone"],
                                                                 row["last_zone_check"]))
        if notes:
            change["note"] = "; ".join(notes)
        changes.append(change)
    return changes, skips


def sweep_portfolio_zones(sections):
    """{key: zone word} from a SWEEP row file's '## Portfolio table' (the Zone
    cell starts with the zone word; the routines README, section 4)."""
    heading = next((h for h in sections if h.lower().startswith("portfolio table")), None)
    zones = {}
    for row in table_rows(sections.get(heading, [])) if heading else []:
        col = next((c for c in row if c.startswith("zone")), None)
        key = re.split(r"[\s(]", (row.get("ticker") or "").strip().strip("`"), 1)[0]
        m = ZONE_WORD_RE.match(row.get(col) or "") if col else None
        if key and m:
            zones[key] = m.group(1)
    return zones


def load_rows_by_key(root):
    rows, problems = load_csv(root)
    if problems:
        raise ToolError("; ".join(problems))
    return {r["key"]: r for r in rows}


def save_rows(root, rows_by_key):
    write_text(os.path.join(root, CSV_FILE), csv_text(list(rows_by_key.values())))


def apply_memo(root, memo_rel):
    """Attended register write for one memo (ANALYSE or REVIEW): the same as
    applying a row file whose memo_path is memo_rel."""
    m = MEMO_PATH_RE.match(memo_rel)
    if not m:
        raise ToolError("%s is not memos/{KEY}/{KEY}_{date}_GSC.md" % memo_rel)
    rows_by_key = load_rows_by_key(root)
    row_type = "REVIEW" if m.group("key") in rows_by_key else "ANALYSE"
    return apply_row(root, None, {"row_type": row_type, "memo_path": memo_rel}, rows_by_key)


def apply_row(root, row_rel, fm=None, rows_by_key=None):
    if rows_by_key is None:
        rows_by_key = load_rows_by_key(root)
    sections = {}
    if fm is None:
        fm, sections = parse_row_file(read_repo_text(root, row_rel))
    row_type = fm["row_type"].upper()
    report = {"row": row_rel or "memo %s" % fm.get("memo_path"), "row_type": row_type,
              "changes": [], "skips": [], "notes": []}
    if row_type in ("ANALYSE", "REVIEW"):
        memo_rel = fm.get("memo_path", "")
        memo_text = read_repo_text(root, memo_rel)
        new = row_from_memo(memo_rel, memo_text, report["notes"])
        old = rows_by_key.get(new["key"])
        if not parse_front_matter(memo_text).get("px"):
            report["notes"] = legacy_fill(new, memo_text, old, report["notes"])
        if old is None and row_type == "REVIEW":
            report["notes"].append("NOTE %s REVIEW row for a key not in the register: added" % new["key"])
        if old is not None and row_type == "ANALYSE":
            report["notes"].append("NOTE %s ANALYSE row for a key already in the register: replaced "
                                   "(memo wins)" % new["key"])
        memo_held = new["held"] == "true"
        report["notes"] += keep_position(new, old)
        if (new["held"] == "true" and not memo_held and new["trigger_basis"] == "no-cash"
                and is_num(new["trigger"]) and is_num(new["add_band"])
                and dec(new["add_band"]) != dec(new["trigger"])):
            # P21 (R10): a held name's ADD band is its operative trigger, the no-cash bound. The
            # memo prints no position fields, so the band follows its trigger; zone and sell
            # line stay the register's until a held memo sets them.
            report["notes"].append("NOTE %s ADD band %s follows the memo's no-cash trigger %s (P21, R10)"
                                   % (new["key"], new["add_band"], new["trigger"]))
            new["add_band"] = new["trigger"]
        problems = validate_row(new)
        if new["section"] not in SECTION_ORDER:
            problems.append("no register section for verdict %r" % new["verdict"])
        if problems:
            raise ToolError("%s: the memo yields an invalid row: %s" % (memo_rel, "; ".join(problems)))
        rows_by_key[new["key"]] = new
        report["changes"].append({"key": new["key"],
                                  "old": table_line(master_cells(old)) if old else "new name",
                                  "new": table_line(master_cells(new))})
    elif row_type == "SWEEP":
        report["changes"], report["skips"] = apply_sweep(rows_by_key, fm, sections)
    elif row_type in ("INCOMPLETE", "PRIOR", "QUEUE"):
        report["notes"].append("no register change (%s)" % row_type)
    else:
        raise ToolError("unknown row_type %r" % row_type)
    if report["changes"]:
        save_rows(root, rows_by_key)
    return report


def set_position(root, key, held, avg_cost=None):
    """Attended position event (MODEL section 7.3): the only way the held flag
    and avg_cost change. Zone and lines come from the current memo when it is
    a held memo, else '-' until the next REVIEW."""
    rows_by_key = load_rows_by_key(root)
    row = rows_by_key.get(key)
    if row is None:
        raise ToolError("%s is not in register.csv" % key)
    old = dict(row)
    notes = []
    if held:
        if not avg_cost:
            raise ToolError("a held position needs --avg-cost (number and currency, e.g. '10.00 USD')")
        memo = row_from_memo(row["memo_path"], read_repo_text(root, row["memo_path"]), [])
        row["held"], row["avg_cost"] = "true", avg_cost
        if memo["held"] == "true":
            for name in ("zone", "add_band", "sell_line", "last_zone_check"):
                row[name] = memo[name]
        else:
            for name in ("zone", "add_band", "sell_line", "last_zone_check"):
                row[name] = OWED
            notes.append("BACKFILL %s zone, add_band, sell_line: the current memo is not a held memo; "
                         "the next REVIEW sets them" % key)
    else:
        row["held"] = "false"
        for name in ("zone", "add_band", "sell_line", "last_zone_check", "avg_cost"):
            row[name] = NM
    problems = validate_row(row)
    if problems:
        raise ToolError("%s: %s" % (key, "; ".join(problems)))
    save_rows(root, rows_by_key)
    return {"key": key, "old": table_line(portfolio_cells(old)) if old["held"] == "true" else "not held",
            "new": table_line(portfolio_cells(row)) if row["held"] == "true" else "not held", "notes": notes}


def rekey(root, old_key, new_key):
    """RECONCILE re-key (MODEL section 7.1a): the register row follows the
    renamed memo folder; the old key joins aliases."""
    if not KEY_RE.match(new_key or ""):
        raise ToolError("%r is not a section 7.1a key" % new_key)
    rows_by_key = load_rows_by_key(root)
    row = rows_by_key.pop(old_key, None)
    if row is None:
        raise ToolError("%s is not in register.csv" % old_key)
    if new_key in rows_by_key:
        raise ToolError("%s is already in register.csv" % new_key)
    row["key"] = new_key
    row["memo_path"] = "memos/%s/%s_%s_GSC.md" % (new_key, new_key, row["memo_date"])
    aliases = [a.strip() for a in row["aliases"].split(";") if a.strip() not in ("", OWED, NM)]
    if old_key not in aliases:
        aliases.append(old_key)
    row["aliases"] = "; ".join(aliases)
    problems = validate_row(row)
    if problems:
        raise ToolError("%s: %s" % (new_key, "; ".join(problems)))
    rows_by_key[new_key] = row
    save_rows(root, rows_by_key)
    return {"old_key": old_key, "new_key": new_key, "memo_path": row["memo_path"], "aliases": row["aliases"]}


# ------------------------------------------------------------------ check (INTAKE step 7)

def legacy_register_keys(text):
    """Keys of a register file (lean or legacy): the first token of the first
    cell of every table row that is not a header or separator."""
    keys = set()
    for line in text.replace("\r\n", "\n").split("\n"):
        s = line.strip()
        if not s.startswith("|"):
            continue
        first = s.strip("|").split("|", 1)[0].strip()
        if not first or first == "Ticker" or re.match(r"^:?-+:?$", first):
            continue
        token = first.split()[0].strip("*`")
        if KEY_RE.match(token):
            keys.add(token)
    return keys


def memo_tree(root, tree):
    """{folder key: [file names]} for memos/ at a git revision, or None."""
    rc, out = run_git(root, ["ls-tree", "-r", "--name-only", "-z", tree, "--", "memos"])
    if rc != 0:
        return None
    folders = {}
    for path in out.decode("utf-8", "replace").split("\0"):
        parts = path.split("/")
        if len(parts) == 3 and parts[0] == "memos":
            folders.setdefault(parts[1], []).append(parts[2])
    return folders


def holding_findings(rows, register_date):
    """LIST findings (never breaches; MODEL section 2 Group dependencies, P26):
    'parent stale' - a listed subsidiary or holding named in a row's
    holding_keys has no register row, a memo that is not current (more than
    15 months older than the register date, or written under a MODEL version
    below v4.5.0) or a memo newer than the parent's. REVIEW takes it at
    priority 1c (REVIEW playbook, step 2). Round 2 (V14) retired the
    credit-heavy review: a credit no longer moves with any market price."""
    out = []
    by_key = {r["key"]: r for r in rows}
    dated = bool(DATE_RE.match(register_date or ""))
    for row in rows:
        keys = row.get("holding_keys", NM)
        if keys in (NM, OWED):
            continue
        for holding in [k.strip() for k in keys.split(";") if k.strip()]:
            other = by_key.get(holding)
            if other is None:
                out.append("%s: parent stale - holding %s has no register row (group dependency)"
                           % (row["key"], holding))
                continue
            if not model_at_least(other.get("model_version")) or (
                    dated and DATE_RE.match(other["memo_date"] or "")
                    and other["memo_date"] < add_months(register_date, -15)):
                out.append("%s: parent stale - holding %s memo %s %s is not current (P26)"
                           % (row["key"], holding, other["memo_date"], other.get("model_version")))
            if other["memo_date"] > row["memo_date"]:
                out.append("%s: parent stale - holding %s memo %s is newer than this memo %s"
                           % (row["key"], holding, other["memo_date"], row["memo_date"]))
    return out


def check(root, base=None, tree="HEAD"):
    """INTAKE step 7. Returns (breaches, listed, counts)."""
    breaches, listed = [], []
    rows, problems = load_csv(root)
    breaches += problems
    seen = set()
    for row in rows:
        if row["key"] in seen:
            breaches.append("%s: duplicate key in register.csv" % row["key"])
        seen.add(row["key"])
        breaches += ["%s: %s" % (row["key"], e) for e in validate_row(row)]
        if row["core_source"] != OWED and is_num(row["px"]):
            # Every row with core numbers: exact after a SWEEP or the rebuild (the tool
            # recomputed them); a memo's own print at its own price within lint-memo's 0.1.
            # The averaged readings (R10) recompute the same way from the average core numbers.
            computed = compute_metrics(row, row["px"], row["px_unit"])
            computed.update(compute_avg_metrics(row, row["px"], row["px_unit"]))
            exact = row["px_source"].startswith("SWEEP") or row["core_source"] != "memo"
            for name in MULTIPLES + AVG_MULTIPLES:
                if computed[name] == row[name] or (
                        not exact and MULT_RE.match(computed[name]) and MULT_RE.match(row[name])
                        and abs(Decimal(computed[name]) - Decimal(row[name])) <= Decimal("0.1")):
                    continue
                breaches.append("%s: %s %s does not recompute from the core numbers at Px %s (%s)"
                                % (row["key"], name, row[name], row["px"], computed[name]))
    if [r["key"] for r in rows] != [r["key"] for r in canonical(rows)]:
        breaches.append("register.csv rows are not in rendered order (section, EV/OI, key)")
    fm, md_text = register_front_matter(root)
    version, date = fm.get("register_version", ""), fm.get("register_date", "")
    try:
        rendered = render(rows, version, date)
        if rendered != md_text.replace("\r\n", "\n"):
            breaches.append("_REGISTER.md is not the rendering of register.csv (re-run render; "
                            "never edit the register by hand)")
    except ToolError as exc:
        breaches.append("render failed: %s" % exc)
    changed, base_rows = set(r["key"] for r in rows), None
    if base:
        rc, out = run_git(root, ["show", "%s:%s" % (base, CSV_FILE)])
        if rc == 0:
            base_rows, _ = read_csv_text(out.decode("utf-8"), "%s:%s" % (base, CSV_FILE), legacy_ok=True)
            old = {r["key"]: r for r in base_rows}
            changed = set(r["key"] for r in rows if old.get(r["key"]) != r)
            outgoing = set(old)
        else:
            rc, out = run_git(root, ["show", "%s:%s" % (base, REGISTER_FILE)])
            if rc != 0:
                breaches.append("cannot read the outgoing register at %s" % base)
                outgoing = set()
            else:
                outgoing = legacy_register_keys(out.decode("utf-8"))
            changed = set()
            listed.append("no register.csv at %s: no row counts as changed (first lean version)" % base)
        missing = sorted(outgoing - seen)
        if missing:
            breaches.append("keys of the outgoing register missing: %s" % ", ".join(missing))
    isins = {}
    for row in rows:
        if row["isin"] != OWED:
            isins.setdefault(row["isin"], []).append(row["key"])
    for isin, keys in sorted(isins.items()):
        if len(keys) > 1:
            msg = "duplicate ISIN %s: %s" % (isin, ", ".join(sorted(keys)))
            (breaches if changed & set(keys) else listed).append(msg)
    folders = memo_tree(root, tree)
    if folders is None:
        breaches.append("cannot list memos/ at %s" % tree)
        folders = {}
    for key, files in sorted(folders.items()):
        if len(files) != 1:
            msg = "memos/%s/ holds %d files" % (key, len(files))
            (breaches if key in changed else listed).append(msg)
    for row in rows:
        name = row["memo_path"].rsplit("/", 1)[-1]
        files = folders.get(row["key"], [])
        if name not in files:
            msg = "%s: memo_path %s is not in memos/ at %s" % (row["key"], row["memo_path"], tree)
            (breaches if row["key"] in changed else listed).append(msg)
        elif len(files) == 1 and files[0] != name:
            msg = "%s: register memo date %s differs from the current memo %s" % (row["key"], row["memo_date"], files[0])
            (breaches if row["key"] in changed else listed).append(msg)
    listed += holding_findings(rows, date)
    counts = {s: sum(1 for r in rows if r["section"] == s) for s in SECTION_ORDER}
    counts["names_total"] = len(rows)
    counts["held"] = sum(1 for r in rows if r["held"] == "true")
    counts["changed"] = len(changed) if base else "n/a (no --base)"
    counts["rows_with_owed_fields"] = sum(1 for r in rows if OWED in (r[n] for n in CSV_HEADER))
    return breaches, listed, counts


# ------------------------------------------------------------------ lint-memo (MODEL section 6.1)

def first_number(text, upper=False):
    """The first number in a price or band statement (thousands separators
    dropped). upper=True: the upper bound when it opens a range or a slash
    pair (section 7.1 operative trigger, IDEAS C4)."""
    m = re.search(r"(\d[\d,]*(?:\.\d+)?)(?:\s*[–/-]\s*[^\d\s(]{0,3}\s*(\d[\d,]*(?:\.\d+)?))?", text or "")
    if not m:
        return None
    value = (m.group(2) if upper and m.group(2) else m.group(1)).replace(",", "")
    try:
        return Decimal(value)
    except InvalidOperation:
        return None


def section_text(text, prefix):
    """The lines of the first '## {prefix}...' section of a memo, joined ('' when absent)."""
    return "\n".join(next((lines for title, lines in sections_of(text).items() if title.startswith(prefix)), []))


def basis_tags(m):
    """The ' · '-separated tags of an OI_BASIS_RE or FCF_BASIS_RE match, in order."""
    return [t.strip() for t in (m.group("tags") or "").split(" · ") if t.strip()]


def lint_lens(fm, text, lens, nm_ok, warns):
    """The MODEL v4.5.0 lens checks of lint-memo (sections 2 Gate 0 and Gate 2,
    6.1, 6.3, 7.1b; round 2: R2-R5, V14; J1). Returns failures; appends warnings."""
    fails = []
    if lens not in LENSES and not nm_ok("lens"):
        fails.append("lens: %r is not one of %s (n.m. only in a Gate-0 DNAF memo; SOTP and SOTP-DOUBT retired "
                     "in round 2: R2-R5)" % (lens, "/".join(LENSES)))
    if model_at_least(fm.get("model_version")):
        retired = [name for name in RETIRED_FIELDS if name in fm]
        if retired:
            fails.append("%s: retired field (round 2: R2–R5, V14); a memo carries holding_keys and core_credit"
                         % ", ".join(retired))
    fails += validate_lens_fields(fm)
    credit, keys = fm["core_credit"], fm["holding_keys"]
    credited = is_num(credit) and dec(credit) > 0
    if credited and keys == NM:
        fails.append("holding_keys: n.m., but core_credit is %s: name the material listed holdings credited (V14)"
                     % credit)
    if credited and lens != "STD":
        fails.append("core_credit: %s, but lens is %s: holding credits exist only under STD (V14)" % (credit, lens))
    if keys not in (NM, OWED) and not GROUP_B4_RE.search(text):
        fails.append("holding_keys: %r, but the memo lacks a line starting 'B4 Division table' (MODEL section 6.3)"
                     % keys)
    if credited and not re.search(r"Holding credits", section_text(text, "F.")):
        fails.append("core_credit: %s, but '## F.' lacks the 'Holding credits' table (MODEL section 6.3)" % credit)
    if lens == "FI":
        for name in ("core_oi", "core_debt_eq", "core_cash"):
            if fm[name] != NM:
                fails.append("%s: %r — under the FI lens it is n.m. (core_fcf carries the NI basis)" % (name, fm[name]))
    return fails + lint_bases(fm, lens, nm_ok)


def min_rule(fm, name, averages, label):
    """P28: a down-year reading takes the lower of the 3- and 5-year averages exactly."""
    values = [fm.get(n, "") for n in averages]
    if not all(is_num(v) for v in values):
        return ["%s: ' · down-year avg', but %s are not both numbers (P28)" % (label, " and ".join(averages))]
    low = min(dec(v) for v in values)
    if not is_num(fm[name]) or dec(fm[name]) != low:
        return ["%s: ' · down-year avg', so %s is the lower of %s exactly (%s), not %s (P28)"
                % (label, name, " and ".join(averages), plain(low), fm[name])]
    return []


def lint_bases(fm, lens, nm_ok):
    """core_oi_basis (J1; every memo: no adjusted line) and, for memos at v4.5.0 or
    later, the section 6.1 grammar of both bases with the P28 down-year rules (R1)
    and the P20 maintenance-capex FCF basis beside the all-capex reading (R6)."""
    fails = []
    current = model_at_least(fm.get("model_version"))
    basis = fm["core_oi_basis"]
    if not nm_ok("core_oi_basis"):
        m = OI_BASIS_RE.match(basis) if current else None
        tags = basis_tags(m) if m else []
        if OI_BASIS_BANNED_RE.search(basis):
            fails.append("core_oi_basis: %r names an adjusted line; OI is the lowest reported operating subtotal (J1)"
                         % basis)
        elif not current:
            pass
        elif not m or any(t not in OI_BASIS_TAGS for t in tags) or len(set(tags)) != len(tags):
            fails.append("core_oi_basis: %r is not '{FY####|TTM Qn-YYYY|LTM Qn-YYYY|FY####–FY#### avg} {J1|NI basis}"
                         "[ · lease-capitalised][ · down-year avg][ · fin. income out]' (MODEL section 6.1)" % basis)
        elif m.group("line") == "OI_P":
            fails.append("core_oi_basis: %r — OI_P (the SOTP perimeter) is retired (round 2: R2–R5): a group reads "
                         "its consolidated J1" % basis)
        elif lens in OI_BASIS_LINES and m.group("line") not in OI_BASIS_LINES[lens]:
            fails.append("core_oi_basis: line %r does not fit lens %s (%s)" % (
                m.group("line"), lens, " or ".join(OI_BASIS_LINES[lens])))
        elif m.group("line") == "J1":
            down = DOWN_YEAR_TAG in tags
            if m.group("avg") and not down:
                fails.append("core_oi_basis: %r — an average period on J1 is the P28 down-year reading only: tag it "
                             "' · down-year avg' (an FI P1 average is an NI basis)" % basis)
            elif down and not m.group("avg"):
                fails.append("core_oi_basis: %r — ' · down-year avg' reads an 'FY####–FY#### avg' period (P28)" % basis)
            elif down:
                fails += min_rule(fm, "core_oi", ("core_oi_3y", "core_oi_5y"), "core_oi_basis")
    fbasis = fm["core_fcf_basis"]
    if current and not nm_ok("core_fcf_basis"):
        m = FCF_BASIS_RE.match(fbasis)
        tags = basis_tags(m) if m else []
        if not m or any(t not in FCF_BASIS_TAGS for t in tags) or len(set(tags)) != len(tags):
            fails.append("core_fcf_basis: %r is not '{period} CFO − maint. capex ({disclosed|constructed|= all capex})"
                         "[ · down-year avg][ · fin. income out]' or, under FI, '{period} NI basis' (MODEL section 6.1, "
                         "R6)" % fbasis)
        elif (lens == "FI") != bool(m.group("ni")):
            fails.append("core_fcf_basis: %r does not fit lens %s (FI: '{period} NI basis'; STD: '{period} CFO − maint. "
                         "capex (…)')" % (fbasis, lens))
        elif m.group("ni"):
            # FI: '{period} NI basis[ · down-year avg]'; the P1 average needs no tag, the P28 one does.
            if any(t != DOWN_YEAR_TAG for t in tags):
                fails.append("core_fcf_basis: %r — an FI NI basis takes only ' · down-year avg'" % fbasis)
            elif tags and not m.group("avg"):
                fails.append("core_fcf_basis: %r — ' · down-year avg' reads an 'FY####–FY#### avg' period (P28)" % fbasis)
            elif tags:
                fails += min_rule(fm, "core_fcf", ("core_fcf_3y", "core_fcf_5y"), "core_fcf_basis")
        else:
            down = DOWN_YEAR_TAG in tags
            if m.group("avg") and not down:
                fails.append("core_fcf_basis: %r — an average period is the P28 down-year reading only: tag it "
                             "' · down-year avg'" % fbasis)
            elif down and not m.group("avg"):
                fails.append("core_fcf_basis: %r — ' · down-year avg' reads an 'FY####–FY#### avg' period (P28)" % fbasis)
            elif down:
                fails += min_rule(fm, "core_fcf", ("core_fcf_3y", "core_fcf_5y"), "core_fcf_basis")
            elif is_num(fm["core_fcf_all"]) and is_num(fm["core_fcf"]):
                every, maint = dec(fm["core_fcf_all"]), dec(fm["core_fcf"])
                if m.group("maint") == "= all capex" and every != maint:
                    fails.append("core_fcf_all: %s, but core_fcf_basis says maintenance capex = all capex, so it equals "
                                 "core_fcf %s (P20)" % (fm["core_fcf_all"], fm["core_fcf"]))
                elif every > maint:
                    fails.append("core_fcf_all: %s is above core_fcf %s: maintenance capex never exceeds all capex, so "
                                 "the all-capex reading is the lower one (P20, R6)" % (fm["core_fcf_all"], fm["core_fcf"]))
    return fails


def lint_r10(fm, lens, nm_ok, held):
    """The round-2 machine fields of a memo at v4.5.0 or later (MODEL section 6.1;
    R10, R1, R6): trigger_basis no-cash; the averages and the all-capex FCF as
    numbers or n.m.; the averaged multiples recomputing to 0.1 at px; the trigger
    as the strict all-pass line; a held name's ADD band equal to its trigger."""
    fails = []
    if fm["trigger_basis"] != "no-cash" and not nm_ok("trigger_basis"):
        fails.append("trigger_basis: %r — the operative trigger is the no-cash bound, the strict all-pass line "
                     "(write no-cash; R10)" % fm["trigger_basis"])
    for name in AVG_CORE + ("core_fcf_all",):
        value = fm[name]
        if value != NM and not is_num(value):
            fails.append("%s: %r is not a plain number or n.m." % (name, value))
        elif lens == "FI" and name in ("core_oi_3y", "core_oi_5y", "core_fcf_all") and value != NM:
            fails.append("%s: %r — under the FI lens it is n.m." % (name, value))
    computed = compute_avg_metrics(fm, fm["px"], fm["px_unit"])
    for name in AVG_MULTIPLES:
        printed, again = fm[name], computed[name]
        if nm_ok(name) or (printed == NM and again == NM):
            continue
        if MULT_RE.match(printed) and MULT_RE.match(again):
            if abs(Decimal(printed) - Decimal(again)) > Decimal("0.1"):
                fails.append("%s: printed %s, recomputed %s from the average core numbers at px %s"
                             % (name, printed, again, fm["px"]))
            continue
        fails.append("%s: printed %r, recomputed %r from the average core numbers" % (name, printed, again))
    if is_num(fm["trigger"]) and not nm_ok("trigger"):
        at = compute_metrics(fm, fm["trigger"], fm["px_unit"])
        mf, eo = at["mcap_fcf"], at["ev_oi"]
        if OWED not in (mf, eo):
            mf_ok = bool(MULT_RE.match(mf)) and Decimal(mf) <= Decimal("8.1")
            if lens == "FI":
                if not mf_ok:
                    fails.append("trigger: %s is not the FI band's line: at it MCap/NI is %s (above 8.0; R10, P25)"
                                 % (fm["trigger"], mf))
            else:
                eo_ok = bool(MULT_RE.match(eo)) and Decimal(eo) <= Decimal("7.1")
                binds = mf_ok and eo_ok and (Decimal(mf) >= Decimal("7.9") or Decimal(eo) >= Decimal("6.9"))
                if not binds:
                    fails.append("trigger: %s is not the no-cash bound (R10): at it MCap/FCF is %s and EV/OI no-cash %s; "
                                 "the strict all-pass line has both within 8.0 and 7.0 and the binding one at its "
                                 "threshold" % (fm["trigger"], mf, eo))
    if held and is_num(fm["trigger"]) and is_num(fm.get("add_band", "")) and dec(fm["add_band"]) != dec(fm["trigger"]):
        fails.append("add_band: %s, but a held name's ADD band is its trigger, the no-cash bound %s (P21, R10)"
                     % (fm["add_band"], fm["trigger"]))
    return fails


def lint_memo(memo_rel, text):
    """(failures, warnings) for the v4.5.0 machine fields of one memo."""
    fails, warns = [], []
    fm = parse_front_matter(text)
    if not fm:
        return ["no front matter"], warns
    _name, note = company_note(fm.get("company", ""))
    if note:
        warns.append("company carries the note %r: lines, venues and former names go in aliases: (the register "
                      "drops the note)" % note[:60])
    verdict = fm.get("verdict", "")
    dnaf = verdict == "DNAF"
    for name in NEW_MEMO_FIELDS + ("ticker", "company", "memo_date", "memo_version", "verdict",
                                   "quality_past", "quality_future", "sf", "cheapness"):
        if fm.get(name) in (None, ""):
            fails.append("%s: missing" % name)
    if fails:
        return fails, warns
    for name, value in fm.items():
        if value == OWED and name in NEW_MEMO_FIELDS:
            fails.append("%s: '-' (not established); a full memo establishes every field or the run "
                         "is INCOMPLETE" % name)

    def nm_ok(name):
        return dnaf and fm[name] == NM and name in DNAF_NM_FIELDS

    m = MEMO_PATH_RE.match(memo_rel)
    if m and (fm["ticker"] != m.group("key") or fm["memo_date"] != m.group("date")):
        fails.append("ticker/memo_date %s/%s do not match the file name" % (fm["ticker"], fm["memo_date"]))
    if not VER_RE.match(fm["memo_version"]):
        fails.append("memo_version: %r is not a bare vN" % fm["memo_version"])
    if verdict not in VERDICTS:
        fails.append("verdict: %r is not one word of %s" % (verdict, "/".join(VERDICTS)))
    for name, allowed in (("quality_past", GRADES), ("quality_future", GRADES), ("sf", SF_GRADES),
                          ("cheapness", CHEAPNESS)):
        if fm[name] not in allowed and not nm_ok(name):
            fails.append("%s: %r is not one word of %s" % (name, fm[name], "/".join(allowed)))
    past, future, sf = fm["quality_past"], fm["quality_future"], fm["sf"]
    gates = gates_failed(past, future, sf)
    if verdict == "AVOID" and gates == 0:
        fails.append("verdict AVOID with no failed gate")
    if verdict in ("BUY", "WATCH") and gates:
        fails.append("verdict %s with %d failed gate(s)" % (verdict, gates))
    # Reasons (section 7.1 vocabulary, <= 3 words).
    for name in ("past_reason", "future_reason", "sf_reason"):
        if len(fm[name].split()) > 3:
            fails.append("%s: %r is longer than three words" % (name, fm[name]))
    pr, fr, sr = fm["past_reason"], fm["future_reason"], fm["sf_reason"]
    lens = fm["lens"]
    if not nm_ok("past_reason"):
        if past in ("STRONG", "ADEQUATE") and not PAST_LEVEL_RE.match(pr):
            fails.append("past_reason: %r — Past %s states its worst-of-four level, e.g. '28%% ROCE'" % (pr, past))
        elif past == "WEAK" and not reason_ok("past", pr):
            fails.append("past_reason: %r is not in the Past vocabulary" % pr)
    if not nm_ok("future_reason"):
        if future in ("STRONG", "ADEQUATE") and fr != NM:
            # R7: an ADEQUATE carried with a concentration flag names it; every other prints the grade alone.
            fails += future_reason_problems(future, fr)
        elif future == "WEAK" and not reason_ok("future", fr):
            fails.append("future_reason: %r is not in the Future vocabulary" % fr)
    if not nm_ok("sf_reason"):
        if sf == "FAIL" and not reason_ok("sf", sr):
            fails.append("sf_reason: %r is not in the SF vocabulary" % sr)
        elif sf == "PASS" and sr != NM and (not reason_ok("sf", sr) or reason_base(sr)[1] in SF_FAIL_ONLY):
            fails.append("sf_reason: %r — a PASS writes n.m., or a caution in the SF vocabulary (%s fail only)"
                         % (sr, ", ".join(SF_FAIL_ONLY)))
    # Reason forms (MODEL section 7.1, round 2): a unit/sub prefix is a group reason (R3,
    # R5: the memo prints the B4 Division table); '{x}% ROE' is the FI lens (or a group
    # part read on FI, with its prefix).
    group = bool(GROUP_B4_RE.search(text))
    for name, value in (("past_reason", pr), ("future_reason", fr), ("sf_reason", sr)):
        prefix, _token = reason_base(value)
        if prefix and not group:
            fails.append("%s: %r carries the group prefix %r, but the memo prints no 'B4 Division table' (a group "
                         "memo, R3/R5)" % (name, value, prefix))
    if PAST_LEVEL_RE.match(pr):
        measure = pr.split()[-1]
        if lens == "FI" and measure == "ROCE":
            fails.append("past_reason: %r — the FI lens grades ROE (P24): write '{x}%% ROE'" % pr)
        elif lens != "FI" and measure == "ROE":
            fails.append("past_reason: %r — ROE is the FI lens; lens %s grades ROCE (a group's Past is one "
                         "consolidated or look-through record)" % (pr, lens))
    # Price, trigger and units.
    unit = fm["px_unit"]
    if not nm_ok("px_unit") and not UNIT_RE.match(unit):
        fails.append("px_unit: %r is not the price endpoint's currency code" % unit)
    for name in ("px", "trigger"):
        if not is_num(fm[name]) and not (name == "trigger" and fm[name] == NM) and not nm_ok(name):
            fails.append("%s: %r is not a plain number in px_unit" % (name, fm[name]))
    for name in ("px_date", "core_fx_date"):
        if not DATE_RE.match(fm[name]) and not nm_ok(name):
            fails.append("%s: %r is not YYYY-MM-DD" % (name, fm[name]))
    if not NEXT_REVIEW_RE.match(fm["next_review_short"]):
        fails.append("next_review_short: %r is not YYYY-MM-DD, Qn YYYY, Mon YYYY or n.m." % fm["next_review_short"])
    suffix = key_suffix(fm["ticker"])
    default_unit = SUFFIX_UNITS.get(suffix, "USD")
    if UNIT_RE.match(unit) and unit != default_unit:
        warns.append("px_unit %s differs from the %s default %s: confirm it is the endpoint's currency"
                     % (unit, "." + suffix if suffix else "US-line", default_unit))
    # Core numbers.
    if fm["core_unit"] not in SCALE and not nm_ok("core_unit"):
        fails.append("core_unit: %r is not k, m or bn" % fm["core_unit"])
    if not CCY_RE.match(fm["core_currency"]) and not nm_ok("core_currency"):
        fails.append("core_currency: %r is not an ISO code" % fm["core_currency"])
    for name in CORE_NUMBERS:
        value = fm[name]
        if nm_ok(name) or (lens == "FI" and name in ("core_oi", "core_debt_eq", "core_cash") and value == NM):
            continue
        if not is_num(value):
            fails.append("%s: %r is not a plain number" % (name, value))
        elif name in ("core_shares_diluted", "core_fx", "core_ratio") and dec(value) <= 0:
            fails.append("%s: must be positive" % name)
        elif name == "core_cash" and dec(value) < 0:
            fails.append("core_cash: negative")
    if UNIT_RE.match(unit) and CCY_RE.match(fm["core_currency"]) and is_num(fm["core_fx"]):
        major, _minor = unit_major(unit)
        if major == fm["core_currency"] and dec(fm["core_fx"]) != 1:
            fails.append("core_fx: %s, but px_unit %s and core_currency %s are the same currency: core_fx "
                         "is the major-unit rate (1); the minor factor applies separately"
                         % (fm["core_fx"], unit, fm["core_currency"]))
    # Self-consistency (section 6.1): the multiples recompute from the core numbers at px.
    if not dnaf or all(fm[n] != NM for n in MULTIPLES):
        computed = compute_metrics(fm, fm["px"], unit)
        for name in MULTIPLES:
            printed, again = fm[name], computed[name]
            if printed == NM and again == NM:
                continue
            if MULT_RE.match(printed) and MULT_RE.match(again):
                if abs(Decimal(printed) - Decimal(again)) > Decimal("0.1"):
                    fails.append("%s: printed %s, recomputed %s from the core numbers at px %s"
                                 % (name, printed, again, fm["px"]))
                continue
            fails.append("%s: printed %r, recomputed %r from the core numbers" % (name, printed, again))
    fails += lint_lens(fm, text, lens, nm_ok, warns)
    held = first_token(fm.get("position", "")) == "HELD"
    if model_at_least(fm.get("model_version")):
        fails += lint_r10(fm, lens, nm_ok, held)
    # The readable statements agree with the machine values (warnings: free text).
    if is_num(fm["px"]):
        stated = first_number(fm.get("price_at_memo", ""))
        px = dec(fm["px"])
        if stated is None or not any(abs(stated * f - px) <= px * Decimal("0.005") for f in (1, 100, 1000)):
            warns.append("px %s does not match price_at_memo %r" % (fm["px"], fm.get("price_at_memo", "")[:60]))
    if is_num(fm["trigger"]):
        # R10: the band prints the operative trigger, the no-cash bound, first (or labels it no-cash).
        band = fm.get("trigger_band", "")
        stated = [first_number(band), no_cash_figure(band, fm["ticker"], None)[0]]
        trig = dec(fm["trigger"])
        if not any(isinstance(s, Decimal) and abs(s * f - trig) <= trig * Decimal("0.01")
                   for s in stated for f in (1, 100, 1000)):
            warns.append("trigger %s does not match the no-cash bound trigger_band states first %r"
                         % (fm["trigger"], band[:60]))
    if fm["aliases"] in ("—", "none", "None"):
        fails.append("aliases: write n.m. when there are none")
    elif fm["aliases"] != NM and ("|" in fm["aliases"] or len(fm["aliases"]) > CELL_CAP):
        fails.append("aliases: no '|' and at most %d characters ('n.m.' when none)" % CELL_CAP)
    # Held names: the position fields are machine values too.
    if held:
        if not ZONE_RE.match(fm.get("zone", "")):
            fails.append("zone: %r is not ADD/HOLD/SELL-FLAG [SRn]" % fm.get("zone"))
        for name in ("add_band", "sell_flag_line"):
            value = fm.get(name, "")
            if not (is_num(value) or value == NM):
                fails.append("%s: %r is not a number in px_unit or n.m." % (name, value))
    return fails, warns


# ------------------------------------------------------------------ lint-row (README section 4) [v4.5.2]

ROW_FILE_RE = re.compile(r"^queue/rows/(?P<date>\d{4}-\d{2}-\d{2})_(?P<time>\d{4})_(?P<job>ANALYSE|REVIEW|SWEEP)"
                         r"(?:_(?P<key>[A-Za-z0-9._-]+))?\.md$", re.ASCII)
# The row types a row file may carry, by its file name (README section 4).
ROW_TYPES_BY_FILE = {("ANALYSE", True): ("ANALYSE", "INCOMPLETE", "PRIOR"),
                     ("REVIEW", True): ("REVIEW", "INCOMPLETE"),
                     ("ANALYSE", False): ("QUEUE",),
                     ("SWEEP", False): ("SWEEP",)}
PASTE_HINT = "paste every line row-from-memo --table prints: header, separator, row"


def row_file_verdict(text):
    """The Verdict cell's first word under '## Register row (new)', read the way
    gsc-automerge reads it (the table's header line names the columns); None
    when the table has no Verdict column or no data row."""
    rows = table_rows(sections_of(text or "").get("Register row (new)", []))
    if not rows or "verdict" not in rows[0]:
        return None
    return first_token(rows[0]["verdict"]) or None


def title_verdict(title):
    """First word of a finished title's outcome ('GSC ANALYSE K D — WATCH (…)' -> 'WATCH')."""
    _head, sep, outcome = (title or "").partition(" — ")
    return first_token(outcome) if sep else ""


def _table_lines(lines):
    return [s.strip() for s in lines if s.strip().startswith("|")]


def _table_problems(name, got, want):
    """Why a pasted table differs from the printed one, or [] when it is the print."""
    if got == want:
        return []
    if not got:
        return ["## %s: no table (%s)" % (name, PASTE_HINT)]
    if got[0] != want[0]:
        if got[0] == want[-1]:
            return ["## %s: the header and separator lines are missing (%s)" % (name, PASTE_HINT)]
        return ["## %s: the first line is not the header row-from-memo --table prints (%s)" % (name, PASTE_HINT)]
    if len(got) < 2 or got[1] != want[1]:
        return ["## %s: the separator line under the header is missing or changed (%s)" % (name, PASTE_HINT)]
    if len(got) != len(want):
        return ["## %s: %d table lines, row-from-memo --table prints %d" % (name, len(got), len(want))]
    have, need = table_rows(got)[0], table_rows(want)[0]
    cols = [c for c in [h.strip() for h in want[0].strip("|").split("|")] if have.get(c.lower()) != need.get(c.lower())]
    return ["## %s: cells differ from row-from-memo --table: %s (never type a row by hand)"
            % (name, ", ".join(cols) or "spacing")]


def lint_row(row_rel, text, read_memo):
    """Failures of one row file against its file name and, for a verdict row,
    against what row-from-memo --table prints for its memo (README section 4).
    read_memo(path) returns the memo text or None. The verdict check reads the
    file the way gsc-automerge does (MODEL section 8.7 item 10)."""
    fails = []
    m = ROW_FILE_RE.match(row_rel)
    if not m:
        return ["%s is not a row file name (queue/rows/{D}_{T}_{JOB}[_{KEY}].md)" % row_rel]
    fm = parse_front_matter(text or "")
    if not fm:
        return ["no front matter (the --- block of README section 4)"]
    key, job = m.group("key"), m.group("job")
    row_type = fm.get("row_type", "")
    allowed = ROW_TYPES_BY_FILE[(job, key is not None)]
    if row_type not in allowed:
        fails.append("row_type: %r; this file name takes %s" % (row_type, " or ".join(allowed)))
    for name, want in (("run_date", m.group("date")), ("run_time", m.group("time"))):
        if fm.get(name) != want:
            fails.append("%s: %r differs from the file name (%s)" % (name, fm.get(name), want))
    if key is not None and fm.get("key") != key:
        fails.append("key: %r differs from the file name (%s)" % (fm.get("key"), key))
    title = fm.get("pr_title", "")
    if not re.match(r"^(HELD · )?GSC %s\b" % job, title):
        fails.append("pr_title: %r does not start 'GSC %s' (it equals the final PR title)" % (title[:80], job))
    held = fm.get("held")
    if held is not None and held not in ("true", "false"):
        fails.append("held: %r is not true or false" % held)
    sections = sections_of(text)

    if row_type == "SWEEP":
        heading = next((h for h in sections if h.lower().startswith("portfolio table")), None)
        rows = table_rows(sections.get(heading, [])) if heading else []
        head = list(rows[0]) if rows else []
        if not heading:
            fails.append("## Portfolio table is missing (every held name, README section 4)")
        elif not ("ticker" in head and any(c.startswith("zone") for c in head)):
            fails.append("## Portfolio table: needs its header line with the Ticker and Zone columns")
        return fails
    if row_type not in ("ANALYSE", "REVIEW"):
        return fails

    memo_path = fm.get("memo_path", "")
    mm = MEMO_PATH_RE.match(memo_path)
    if not mm or mm.group("dir") != mm.group("key") or mm.group("date") != m.group("date"):
        fails.append("memo_path: %r is not memos/{KEY}/{KEY}_%s_GSC.md" % (memo_path, m.group("date")))
        return fails
    memo_text = read_memo(memo_path)
    if memo_text is None:
        fails.append("memo_path: cannot read %s" % memo_path)
        return fails
    try:
        row = row_from_memo(memo_path, memo_text, [])
    except ToolError as exc:
        fails.append("memo_path: %s" % exc)
        return fails
    want = [table_line(MASTER_COLUMNS), "|" + "---|" * len(MASTER_COLUMNS), table_line(master_cells(row))]
    fails += _table_problems("Register row (new)", _table_lines(sections.get("Register row (new)", [])), want)
    got_p = _table_lines(sections.get("Portfolio row", []))
    if row["held"] == "true":
        want_p = [table_line(PORTFOLIO_COLUMNS), "|" + "---|" * len(PORTFOLIO_COLUMNS),
                  table_line(portfolio_cells(row))]
        fails += _table_problems("Portfolio row", got_p, want_p)
    elif got_p:
        fails.append("## Portfolio row: the memo is not held, so row-from-memo --table prints none")
    # The three verdicts gsc-automerge compares: the row table's, the memo's and the title's.
    cell_v, memo_v, title_v = row_file_verdict(text), first_token(row["verdict"]), title_verdict(title)
    if not (cell_v == memo_v == title_v):
        fails.append("verdicts differ: row table %s, memo %s, pr_title %s (gsc-automerge would hold the PR)"
                     % (cell_v or "?", memo_v or "?", title_v or "?"))
    return fails


# ------------------------------------------------------------------ next_review_short helper

def parse_next_review_short(text, after=None):
    """Earliest dated token of a free-text next_review: 'YYYY-MM-DD',
    'Qn YYYY', 'Mon YYYY', 'n.m.' (event-only) or '-' (unparseable). With
    after (YYYY-MM-DD, the memo date), tokens before it are past events the
    text mentions, not the next review, and are skipped."""
    text = text or ""
    months = "|".join(MONTHS)
    floor = after if after and DATE_RE.match(after) else "0000-00-00"
    dates = ["%s-%02d-%02d" % (m.group(3), MONTHS.index(m.group(2)) + 1, int(m.group(1)))
             for m in re.finditer(r"\b(\d{1,2}) (%s)[a-z]* (\d{4})\b" % months, text)]
    dates += [m.group(0) for m in re.finditer(r"\b\d{4}-\d{2}-\d{2}\b", text)]
    dates = [d for d in dates if d >= floor]
    if dates:
        return min(dates)
    month_years = [(int(m.group(2)), MONTHS.index(m.group(1)), "%s %s" % (m.group(1), m.group(2)))
                   for m in re.finditer(r"\b(%s)[a-z]* (\d{4})\b" % months, text)]
    month_years = [t for t in month_years if "%04d-%02d" % (t[0], t[1] + 1) >= floor[:7]]
    if month_years:
        return min(month_years)[2]
    quarters = [(int(m.group(2) if len(m.group(2)) == 4 else "20" + m.group(2)), int(m.group(1)))
                for m in re.finditer(r"\bQ([1-4])\s*'?(\d{4}|\d{2})\b", text)]
    quarters = [q for q in quarters if "%04d-%02d" % (q[0], q[1] * 3) >= floor[:7]]
    if quarters:
        year, quarter = min(quarters)
        return "Q%d %d" % (quarter, year)
    if re.search(r"(?i)\b(event only|re-listing|terminal)\b", text):
        return NM
    return OWED


# ------------------------------------------------------------------ rebuild (one-time, attended)
#
# The 2026 switch to the lean register (MODEL v4.5.0 section 7.1b): register.csv
# and a lean _REGISTER.md built from the outgoing (pre-lean) register and the
# memo each of its rows cites. Every value comes from a memo, the outgoing
# register or the last applied SWEEP row file, or from the attended assisted
# file, where every value carries a verbatim memo quote. Nothing is invented:
# a value no source establishes is '-' and becomes a backfill line.

REBUILD_RULES = (
    "Never invent a number: a value no source establishes is '-' (backfill owed).",
    "Keys, sections and the held flag come from the outgoing register; identity, grades, verdict "
    "and memo date from the memo each row cites (memo wins), enums normalised to their first token. "
    "A DNAF row the register made terminal after its memo (a delisting) keeps DNAF and is listed.",
    "Px: held, BUY, WATCH and one-gate AVOID rows that the last applied SWEEP priced carry that "
    "close when the outgoing register shows it; every other row carries the memo's price. A price "
    "on another line or in another currency than the key's quote unit is '-' and listed.",
    "Trigger: the memo's operative trigger (section 7.1, IDEAS C4 and C6) in the quote unit; an "
    "assisted value overrides the parser; a trigger in another currency is '-'.",
    "Core numbers: only from the assisted file; each number must be a number of its verbatim memo "
    "quote, that number in another scale, a signed sum of the quote's numbers (a debt build) or a "
    "quotient or product of two of them (with the memo price and 1, 7, 8 as operands), at most six "
    "decimals; and only those whose multiples reproduce the memo's own printed multiples within 5% "
    "at the memo price (a memo that prints its current multiples on another share count or balance "
    "sheet than its band differs by a few per cent). Every row whose recomputed multiples differ "
    "from the print by more than 0.1 at the memo price is listed.",
    "Multiples: recomputed from accepted core numbers at the Px shown; without them, the memo's "
    "printed multiples when Px is the memo price; otherwise '-'. DNAF rows print n.m.",
    "Reasons: Past STRONG or ADEQUATE prints the worst-of-four level found in the memo; WEAK, FAIL "
    "and an SF caution only from the assisted file (section 7.1 vocabulary).",
)

NUM_TEXT = r"\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?"
CURRENCY_TOKENS = (
    (r"US\$", "USD"), (r"HK\$", "HKD"), (r"NT\$", "TWD"), (r"A\$", "AUD"), (r"C\$", "CAD"),
    (r"NZ\$", "NZD"), (r"S\$", "SGD"), (r"R\$", "BRL"), (r"\$", "USD"), (r"€", "EUR"), (r"£", "GBP"),
    (r"₩", "KRW"), (r"₪", "ILS"), (r"¥", "YEN"), (r"₹", "INR"), (r"zł", "PLN"),
    (r"\b(?:USD|EUR|GBP|GBp|GBX|CHF|SEK|DKK|NOK|ISK|PLN|CZK|HUF|RON|TRY|ILS|ILA|ZAR|ZAc|JPY|CNY|RMB|"
     r"HKD|TWD|KRW|SGD|INR|IDR|THB|MYR|AUD|NZD|CAD|BRL|MXN|ARS|CLP|SAR|AED|QAR|KWD|KWF)\b", None),
)
CURRENCY_RE = "|".join("(?:%s)" % pattern for pattern, _unit in CURRENCY_TOKENS)
MONEY_RE = re.compile(r"(?P<cur>%s)?\s?[~≈]?\s?(?P<num>%s)(?P<p>p\b)?" % (CURRENCY_RE, NUM_TEXT))
DAY_MONTH_RE = re.compile(r"\b(\d{1,2})(?:\s?[–-]\s?\d{1,2})?(?:\s|-)(%s)[a-z]*\.?,?(?:\s|-)(\d{4})\b"
                          % "|".join(MONTHS))
MONTH_DAY_RE = re.compile(r"\b(%s)[a-z]*\.? (\d{1,2}),? (\d{4})\b" % "|".join(MONTHS))
ISO_DATE_RE = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
PAST_LEVEL_TEXT_RE = re.compile(
    r"[Ww]orst[- ]of[- ](?:the[- ])?four[^%\n]{0,24}?\b(ROCE|ROE)\b[^%\n\d]{0,24}?(\d{1,3}(?:\.\d+)?)\s?%")
FCF_LEG_RE = re.compile(r"(?:MCap\s?/\s?FCF|FCF)[ -]leg[^0-9;()]{0,14}?(?P<cur>%s)?\s?(?P<num>%s)(?P<p>p\b)?"
                        r"(?P<range>\s?(?:–|-|/)\s?(?:%s)?\s?(?:%s))?(?:\s(?P<cls>[A-Z])\b)?"
                        % (CURRENCY_RE, NUM_TEXT, CURRENCY_RE, NUM_TEXT))
ASSISTED_FIELDS = set(CORE_FIELDS) | {"past_reason", "future_reason", "sf_reason", "trigger",
                                      "next_review_short", "px_unit", "aliases", "printed_mcap_fcf", "printed_ev_oi",
                                      "printed_ev_oi_all_cash"}
QUOTE_OPTIONAL = {"core_period", "core_currency", "core_unit", "core_oi_basis", "core_fcf_basis",
                  "core_fx_date", "next_review_short"}


def plain(value):
    """A Decimal as a plain number string: no exponent, no trailing zeros."""
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def currency_of(token, key):
    """The currency code a price token names (None when it names none)."""
    if not token:
        return None
    token = token.strip()
    for pattern, unit in CURRENCY_TOKENS:
        if re.fullmatch(pattern, token):
            if unit is None:
                unit = {"RMB": "CNY", "GBX": "GBp"}.get(token, token)
            if unit == "YEN":
                return "CNY" if key_suffix(key) in ("SS", "SZ") else "JPY"
            return unit
    return None


def default_unit(key):
    return SUFFIX_UNITS.get(key_suffix(key), "USD")


def to_quote_unit(value, unit, quote_unit):
    """(value, unit) moved to the quote unit when it is the same currency in
    another scale (GBP -> GBp x100, ILS -> ILA x100, ZAR -> ZAc x100, KWD ->
    KWF x1000). Returns (None, reason) when the currencies differ."""
    if unit == quote_unit:
        return value, None
    major, factor = unit_major(quote_unit)
    if unit == major:
        return value * factor, "%s -> %s x%s" % (unit, quote_unit, factor)
    if quote_unit == major and unit in MINOR_UNITS and MINOR_UNITS[unit][0] == major:
        return value / Decimal(MINOR_UNITS[unit][1]), "%s -> %s /%s" % (unit, quote_unit, MINOR_UNITS[unit][1])
    return None, "%s is not the quote unit %s" % (unit, quote_unit)


def first_date(text):
    """The first close date a price statement names, as YYYY-MM-DD (a day range
    gives its last day), or None."""
    found = []
    for m in DAY_MONTH_RE.finditer(text or ""):
        day = re.search(r"(\d{1,2})\D*$", m.group(0).split(m.group(2))[0]).group(1)
        found.append((m.start(), "%s-%02d-%02d" % (m.group(3), MONTHS.index(m.group(2)) + 1, int(day))))
    for m in MONTH_DAY_RE.finditer(text or ""):
        found.append((m.start(), "%s-%02d-%02d" % (m.group(3), MONTHS.index(m.group(1)) + 1, int(m.group(2)))))
    for m in ISO_DATE_RE.finditer(text or ""):
        found.append((m.start(), m.group(0)))
    return min(found)[1] if found else None


def money_tokens(text, key):
    """[(value, unit)] of every number in a price statement, with the currency
    named just before it (a code before a dollar sign wins: 'CAD $78.60'), a
    pence suffix, or a code right after it; unit None when none is named."""
    out = []
    for m in MONEY_RE.finditer(text):
        unit = "GBp" if m.group("p") else currency_of(m.group("cur"), key)
        if m.group("cur") and m.group("cur").strip() == "$":
            before = re.search(r"\b([A-Z]{3})\s?$", text[:m.start()])
            if before and currency_of(before.group(1), key):
                unit = currency_of(before.group(1), key)
        if unit is None:
            after = re.match(r"\s?(%s)" % CURRENCY_RE, text[m.end():])
            unit = currency_of(after.group(1), key) if after else None
        out.append((dec(m.group("num").replace(",", "")), unit))
    return out


def parse_memo_price(text, key, currency_field="", quote_unit=None):
    """The memo's price statement as (value, unit, date, note): the first
    number and the currency named with it; when that is not the key's quote
    currency, a later price in it (the key's own line, e.g. 'UNA €53.53; ULVR
    £45.64'); a bare number takes the memo's currency field when that is the
    quote currency. value None when there is no listed price."""
    text = (text or "").strip()
    quote_unit = quote_unit or default_unit(key)
    if not text or re.match(r"(?i)n/?a\b|none\b|—", text):
        return None, None, None, "no listed price"
    tokens = money_tokens(text, key)
    if not tokens:
        return None, None, None, "no number"
    value, unit = tokens[0]
    day = first_date(text)
    if unit is None or to_quote_unit(value, unit, quote_unit)[0] is None:
        for later_value, later_unit in tokens[1:]:
            if later_unit and to_quote_unit(later_value, later_unit, quote_unit)[0] is not None:
                return later_value, later_unit, day, "the key's line is the later %s %s in the statement" % (
                    later_unit, plain(later_value))
    if unit is None:
        field = currency_of((currency_field or "").split()[0] if currency_field else "", key)
        if field in (unit_major(quote_unit)[0], quote_unit):
            return value, field, day, "bare number; unit from the memo's currency field"
        return value, None, day, "bare number; currency field %r is not the quote currency" % (currency_field[:30],)
    return value, unit, day, None


def class_letter(key):
    """The share-class letter of a dual-class key (EPI-A.ST -> 'A'), else ''."""
    stem = key.rsplit(".", 1)[0] if key_suffix(key) else key
    m = re.search(r"-([A-Z])$", stem)
    return m.group(1) if m else ""


VARIANT_LABEL = r"(?:\s?\(?(?:no[- ]cash|all[- ]cash(?:[- ]excess)?|nc|ac|conservative|cons\.?)\)?)?"
LEG_RE = re.compile(r"(?P<cur>%s)?\s?(?P<lo>%s)(?P<p>p\b)?%s(?:\s?(?:–|-|/|to)\s?[≈~]?\s?(?:%s)?\s?(?P<hi>%s)"
                    r"(?P<p2>p\b)?%s)?(?:\s(?P<cls>[A-Z])\b)?"
                    % (CURRENCY_RE, NUM_TEXT, VARIANT_LABEL, CURRENCY_RE, NUM_TEXT, VARIANT_LABEL))
CHEAP_LEAD_RE = re.compile(r"CHEAP\b[\s<≈≤~:=]*(?:below|under)?[\s<≈≤~]*")
NM_BAND_RE = re.compile(r"(?i)^\s*(?:n\.m\.|n/a\b|none\b|no cheap band|no positive|no usable|unattainable)"
                        r"|CHEAP\s+n\.m\.|\bunattainable\b")


def operative_trigger(band, key, memo_unit):
    """(value, unit, how) of a memo's trigger_band (MODEL section 7.1): the first
    headline CHEAP figure; a range or a slash pair gives its upper bound (IDEAS
    C4b); a split dual-line band gives the key's line (C4a); an FCF leg inside
    the pair caps the upper bound (C6); a legacy memo's stated anchor price
    stands (the substitution rule and its NAV/P-B anchors were retired at MODEL
    v4.5.0, J2/J4; only memos written before it print one, until their REVIEW).
    value None: n.m. (how 'n.m.') or not parsed (how says why)."""
    band = (band or "").replace("**", "").replace("`", "")
    letter = class_letter(key)
    leg, legs = None, []
    for lead in CHEAP_LEAD_RE.finditer(band):
        m = LEG_RE.match(band, lead.end())
        if not m:
            continue
        legs = [m]
        while m.group("cls"):
            sep = re.match(r"\s?/\s?", band[m.end():])
            nxt = LEG_RE.match(band, m.end() + sep.end()) if sep else None
            if not nxt or not nxt.group("cls"):
                break
            legs.append(nxt)
            m = nxt
        break
    if not legs:
        anchor = re.search(r"(?i)\b(?:gauge|anchor)\b", band)
        if anchor and not re.match(r"(?i)\s*n\.m\.", band):
            for m in MONEY_RE.finditer(band, anchor.end()):
                unit = "GBp" if m.group("p") else currency_of(m.group("cur"), key)
                if unit:
                    return dec(m.group("num").replace(",", "")), unit, "legacy anchor (retired v4.5.0)"
        if NM_BAND_RE.search(band):
            return None, None, "n.m."
        return None, None, "no CHEAP figure and no anchor price"
    leg = legs[0]
    if letter and any(m.group("cls") for m in legs):
        named = [m for m in legs if m.group("cls") == letter]
        if not named:
            return None, None, "split dual-line band has no %s leg" % letter
        leg = named[0]
    unit = "GBp" if (leg.group("p") or leg.group("p2")) else currency_of(leg.group("cur"), key)
    if unit is None:
        first_cur = MONEY_RE.search(band)
        unit = currency_of(first_cur.group("cur"), key) if first_cur and first_cur.group("cur") else memo_unit
    lo = dec(leg.group("lo").replace(",", ""))
    how = "single"
    value = lo
    if leg.group("hi"):
        hi = dec(leg.group("hi").replace(",", ""))
        if hi >= lo:
            value, how = hi, "range upper bound"
        else:
            how = "single (second figure below the first)"
    if how == "range upper bound":
        for f in FCF_LEG_RE.finditer(band):
            if re.search(r"(?i)strict\W*$", band[max(0, f.start() - 8):f.start()]):
                continue
            if f.group("range") or (letter and f.group("cls") and f.group("cls") != letter):
                continue
            fcf = dec(f.group("num").replace(",", ""))
            f_unit = "GBp" if f.group("p") else currency_of(f.group("cur"), key) or unit
            if f_unit == unit and lo < fcf < value:
                value, how = fcf, "FCF leg inside the pair caps the upper bound (C6)"
            break
    if letter and leg.group("cls"):
        how += "; %s line (C4a)" % letter
    return value, unit, how


# The no-cash bound a memo prints (round 2, R10; the one-time retrigger and lint-memo's
# readable-statement warning). Only an explicit label counts: 'no-cash', 'nc' or
# 'no-excess-cash'. 'Conservative EV' is not one - memos use it for either variant.
NC_LABEL_RE = re.compile(r"(?i)no[- ](?:excess[- ])?cash|(?<![\w-])nc(?![\w-])")
NC_PAIR_AFTER_RE = re.compile(r"(?P<cur>%s)?\s?[≈~]?\s?(?P<a>%s)(?P<pa>p\b)?\s?(?:–|-|/)\s?[≈~]?\s?(?:%s)?\s?(?:%s)"
                              r"(?:p\b)?\s+(?:no[- ]cash|nc)\s?/\s?(?:all[- ]cash|ac)\b"
                              % (CURRENCY_RE, NUM_TEXT, CURRENCY_RE, NUM_TEXT))
NC_PAIR_BEFORE_RE = re.compile(r"(?<![\w-])(?:no[- ]cash|nc)\s?/\s?(?:all[- ]cash|ac)\s+[≈~]?\s?(?P<cur>%s)?\s?"
                               r"(?P<a>%s)(?P<pa>p\b)?\s?/\s?(?:%s)?\s?(?:%s)" % (CURRENCY_RE, NUM_TEXT, CURRENCY_RE,
                                                                                  NUM_TEXT))
NC_FIGURE_AFTER_RE = re.compile(r"(?P<cur>%s)?\s?[≈~]?\s?(?P<a>%s)(?P<pa>p\b)?\s+no[- ]cash\b" % (CURRENCY_RE, NUM_TEXT))
NC_FIGURE_BEFORE_RE = re.compile(r"(?<![\w-])no[- ]cash\s+(?:EV\s?/\s?OI\s+)?(?:legs?\s+)?[≈~]?\s?(?P<cur>%s)?\s?"
                                 r"(?P<a>%s)(?![\d.,])(?P<pa>p\b)?(?!\s?[×x%%])" % (CURRENCY_RE, NUM_TEXT))
# A no-cash bound printed n.m. (the EV/OI no-cash leg admits no positive price, so no price
# passes both variants): 'n.m./$21.7 (no-cash/all-cash' or 'no-cash n.m.' (BABA, review fix
# of 2026-10-07: the v310 pass read it as unlabelled).
NC_NM_RE = re.compile(r"(?i)n\.m\.\s?/\s?[≈~]?\s?(?:%s)?\s?(?:%s)(?:p\b)?\s*\(?\s?(?:no[- ]cash|nc)\s?/\s?"
                      r"(?:all[- ]cash|ac)\b|(?<![\w-])(?:no[- ]cash|nc)\s?/\s?(?:all[- ]cash|ac)\s+[≈~]?\s?n\.m\.|"
                      r"n\.m\.\s+\(?no[- ]cash\b|(?<![\w-])no[- ]cash\s+(?:EV\s?/\s?OI\s+)?(?:legs?\s+)?n\.m\."
                      % (CURRENCY_RE, NUM_TEXT))
# A labelled figure that is not the strict line: an allowance edge, a TTM or reference reading.
NC_SKIP_RE = re.compile(r"(?i)P12|\bedge\b|TTM|reference|backvalued|\balt\b|cross-check|x-check|run-rate")
BOTH_VARIANTS_RE = re.compile(r"(?i)\bboth (?:EV(?:/OI)? )?variants\b")
FCF_BINDS_RE = re.compile(r"(?i)^\W*(?:binding:\s*)?MCap\s?/\s?FCF\b|MCap\s?/\s?FCF(?: leg)?[^;()]{0,30}?\bbinds?\b|"
                          r"\bFCF leg binds\b|binding:\s*MCap\s?/\s?FCF")
FCF_LEG_SKIP_RE = re.compile(r"(?i)strict|all[- ]capex|reference|normali[sz]ed|TTM|alt\b|P12")


def figure_unit(m, key, fallback):
    """The unit of a figure match: pence suffix, its own currency token, else fallback."""
    if m.group("pa"):
        return "GBp"
    return currency_of(m.group("cur"), key) if m.group("cur") else fallback


def no_cash_figure(band, key, memo_unit, quote_unit=None):
    """(value, unit, how) of the no-cash bound a memo's trigger_band prints (MODEL
    section 7.1 operative trigger, R10: the lower of the FCF leg and the EV/OI
    no-cash leg). Read, in this order: the headline CHEAP figure or pair when it
    is labelled no-cash (a pair's lower bound); else a headline figure that the
    FCF leg binds, with any figure labelled no-cash elsewhere in the band (or
    alone when the band says it binds both variants); else the lowest figure
    labelled no-cash anywhere in the band. A printed single FCF leg (not strict,
    all-capex, reference or P12) in the same unit caps it. value None: no
    labelled figure (how says why). With quote_unit, a headline in another
    currency gives way to an alternative rendering in the quote unit. value NM: the
    band prints the no-cash bound as n.m. (no positive price passes the strict line)."""
    band = (band or "").replace("**", "").replace("`", "")
    letter = class_letter(key)
    lead = CHEAP_LEAD_RE.search(band)
    if not lead:
        return None, None, "no CHEAP figure"
    leg = LEG_RE.match(band, lead.end())
    if not leg:
        # A currency sign the tool does not know ('₸38,604'): the figure in it has no unit.
        sign = re.match(r"[^\d\s(]{1,3}(?=\d)", band[lead.end():])
        leg = LEG_RE.match(band, lead.end() + sign.end()) if sign else None
    if not leg:
        return None, None, "no CHEAP figure"
    end = leg.end()
    unit = "GBp" if (leg.group("p") or leg.group("p2")) else currency_of(leg.group("cur"), key)
    if unit is None:
        first_cur = MONEY_RE.search(band)
        unit = currency_of(first_cur.group("cur"), key) if first_cur and first_cur.group("cur") else memo_unit
    if quote_unit and (unit is None or to_quote_unit(Decimal(1), unit, quote_unit)[0] is None):
        alt = re.match(r"\s?[≈~=]\s?", band[end:])
        nxt = LEG_RE.match(band, end + alt.end()) if alt else None
        if nxt and nxt.group("cur") and currency_of(nxt.group("cur"), key) and \
                to_quote_unit(Decimal(1), currency_of(nxt.group("cur"), key), quote_unit)[0] is not None:
            leg, end, unit = nxt, nxt.end(), currency_of(nxt.group("cur"), key)
    if letter and leg.group("cls") and leg.group("cls") != letter:
        return None, None, "the headline figure is the %s line, not %s" % (leg.group("cls"), letter)
    lo = dec(leg.group("lo").replace(",", ""))
    hi = dec(leg.group("hi").replace(",", "")) if leg.group("hi") else None
    if hi is not None:
        # 'HKD 14.8 / EUR 1.66' is one figure in two currencies, not a pair.
        other = re.search(CURRENCY_RE, band[leg.end("lo"):leg.start("hi")])
        if other and currency_of(other.group(0), key) not in (None, unit):
            hi = None
    window = re.split(r";| — ", band[end:end + 100], 1)[0]
    labelled = bool(NC_LABEL_RE.search(leg.group(0) + window))
    figures = []
    for regex in (NC_PAIR_AFTER_RE, NC_PAIR_BEFORE_RE, NC_FIGURE_AFTER_RE, NC_FIGURE_BEFORE_RE):
        for m in regex.finditer(band, end):
            if NC_SKIP_RE.search(band[max(0, m.start() - 30):m.start()].split(";")[-1]):
                continue
            if figure_unit(m, key, unit) == unit:
                figures.append(dec(m.group("a").replace(",", "")))
    fcf_head = hi is None and bool(FCF_BINDS_RE.search(window))
    nm_bound = [m for m in NC_NM_RE.finditer(band, end)
                if not NC_SKIP_RE.search(band[max(0, m.start() - 30):m.start()].split(";")[-1])]
    if not labelled and nm_bound:
        return NM, None, "the no-cash bound prints n.m. (no positive price passes both EV variants)"
    if labelled:
        value = min(lo, hi) if hi is not None else lo
        how = "headline %s labelled no-cash" % ("pair, lower bound" if hi is not None else "figure")
    elif fcf_head and figures:
        value, how = min([lo] + figures), "headline FCF leg with the EV/OI no-cash figure %s" % plain(min(figures))
    elif hi is None and BOTH_VARIANTS_RE.search(band) and re.search(r"(?i)\bbind", band):
        value, how = lo, "headline figure binds both EV variants"
    elif figures:
        value, how = min(figures), "figure labelled no-cash in the band"
    else:
        return None, None, "no figure labelled no-cash"
    for f in FCF_LEG_RE.finditer(band):
        if FCF_LEG_SKIP_RE.search(band[max(0, f.start() - 30):f.start()]) or f.group("range"):
            continue
        if letter and f.group("cls") and f.group("cls") != letter:
            continue
        fcf = dec(f.group("num").replace(",", ""))
        f_unit = "GBp" if f.group("p") else currency_of(f.group("cur"), key) or unit
        if f_unit == unit and fcf < value:
            value, how = fcf, how + "; the printed FCF leg %s binds below it" % plain(fcf)
    return value, unit, how


def past_level(text):
    """'{x}% ROCE' (or ROE) from the memo's worst-of-four statement, else None."""
    sections = sections_of(text)
    ordered = [lines for title, lines in sections.items() if title.startswith("3.")]
    ordered += [text.replace("\r\n", "\n").split("\n")]
    for lines in ordered:
        m = PAST_LEVEL_TEXT_RE.search("\n".join(lines).replace("**", ""))
        if m:
            level = Decimal(m.group(2)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
            return "%s%% %s" % (plain(level), m.group(1)), m.group(0)
    return None, None


def memo_multiples(text):
    """The memo's own printed primaries from its section 6 table: one-decimal
    strings, 'n.m.' or '-'."""
    out = {name: OWED for name in MULTIPLES}
    section = None
    for title, lines in sections_of(text).items():
        if title.startswith("6."):
            section = lines
    if section is None:
        return out
    rows = []
    for line in section:
        s = line.strip()
        if s.startswith("|"):
            cells = [c.strip().replace("**", "") for c in s.strip("|").split("|")]
            if len(cells) >= 2 and not re.match(r"^:?-+:?$", cells[0]) and cells[0].lower() != "metric":
                rows.append(cells)

    def values(cell):
        first = re.split(r";|\(\s*(?:TTM|LTM)|\bTTM\b|\bLTM\b", cell, 1)[0]
        found = [Decimal(v) for v in re.findall(r"(\d+(?:\.\d+)?)\s?×", first)]
        if not found:
            bare = re.match(r"^\s*(\d+(?:\.\d+)?)\s*(?:/\s*(\d+(?:\.\d+)?))?\s*(?:\(|$)", first)
            if bare:
                found = [Decimal(v) for v in bare.groups() if v]
        return found

    def is_nm(cell):
        return bool(re.match(r"(?i)\s*(n\.m\.|n/m|neg)", cell))

    def current(cells):
        """(values, n.m.) of the first value cell after the label (a threshold cell is skipped)."""
        for cell in cells[1:]:
            if re.match(r"\s*[≤<≥>]", cell):
                continue
            found = values(cell)
            if found:
                return found, cell
            if is_nm(cell):
                return [], cell
        return [], ""

    # MCap/FCF: a strict (all-capex) row first, else the first row that is not
    # a P20 maintenance reading; table order is the memo's own (its operative
    # basis comes first, TTM/LTM included).
    mf = [r for r in rows if re.search(r"MCap\s?/\s?FCF", r[0])]
    strict = [r for r in mf if re.search(r"(?i)all[- ]capex|strict", r[0])]
    plain_rows = [r for r in mf if not re.search(r"(?i)maint|P20", r[0])]
    mf = strict or plain_rows or mf
    if mf:
        found, cell = current(mf[0])
        if found:
            out["mcap_fcf"] = fmt1(found[0])
        elif is_nm(cell):
            out["mcap_fcf"] = NM
    # EV/OI: the first row printing a pair, else the first two single-valued
    # rows, in table order. No-cash EV is never below all-cash EV, so a pair is
    # read max -> no-cash, min -> all-cash whatever the memo calls its variants.
    ev = [r for r in rows if re.search(r"EV\s?/\s?(OI|operating)", r[0], re.I)]
    nc = ac = None
    singles = []
    for r in ev:
        label = r[0].lower()
        found, cell = current(r)
        if not found:
            if is_nm(cell) and not singles:
                out["ev_oi"] = out["ev_oi_all_cash"] = NM
                break
            continue
        if len(found) >= 2 and not singles:
            nc, ac = max(found[0], found[1]), min(found[0], found[1])
            break
        singles.append((found[0], label + " " + cell.lower()))
        if len(singles) == 2:
            break
    if nc is None and len(singles) == 2:
        nc, ac = max(singles[0][0], singles[1][0]), min(singles[0][0], singles[1][0])
    elif nc is None and len(singles) == 1:
        value, label = singles[0]
        if re.search(r"all[- ]?cash|cash[- ]excess|cash excess", label) and not re.search(r"no[- ]cash|no cash", label):
            ac = value
        elif re.search(r"\bboth\b", label):
            nc = ac = value
        else:
            nc = value
            if not re.search(r"no[- ]?cash|no cash", label):
                out["_ev_single"] = True
    if nc is not None:
        out["ev_oi"] = fmt1(nc)
    if ac is not None:
        out["ev_oi_all_cash"] = fmt1(ac)
        out.pop("_ev_single", None)
    return out


def norm_text(text):
    return re.sub(r"\s+", " ", (text or "").replace("**", "").replace("`", "")).strip()


# ------------------------------------------------------------------ rebuild: inputs

def legacy_register(text):
    """(master, portfolio, front matter) of a pre-lean register: master is an
    ordered {key: {'section', 'cells', 'ticker'}}; portfolio {key: cells}."""
    master, portfolio, section = {}, {}, None
    lines = text.replace("\r\n", "\n").split("\n")
    blocks = []
    for line in lines:
        h = re.match(r"^#{2,3} (Portfolio|BUY|WATCH|AVOID|DNAF)\b", line)
        if h:
            section = h.group(1).upper()
            blocks.append((section, []))
            continue
        if line.startswith("## ") and not h:
            section = None
        if section and blocks:
            blocks[-1][1].append(line)
    for section, block in blocks:
        for cells in table_rows(block):
            ticker = cells.get("ticker", "")
            key = ticker.split()[0].strip("*`") if ticker.split() else ""
            if not KEY_RE.match(key):
                continue
            if section == "PORTFOLIO":
                portfolio[key] = cells
            else:
                master[key] = {"section": section, "cells": cells, "ticker": ticker}
    return master, portfolio, parse_front_matter(text)


VENUE_WORDS = ("SIX", "LSE", "TSX", "NYSE", "Nasdaq", "NASDAQ", "B3", "Oslo", "OTC", "Xetra", "Euronext")


def clean_alias(item, key):
    """One alias without venue words ('NOVN SIX' -> 'NOVN'); None when nothing
    names a line, a retired key or another name of the company ('SIX',
    'ADR 1:1', '~10:1')."""
    words = [w for w in item.split() if w.rstrip(":") not in VENUE_WORDS]
    text = " ".join(words).strip(" ;,")
    named = [w for w in words if re.fullmatch(r"[A-Z0-9][A-Za-z0-9.&/-]+", w) and w not in ("ADR", "ADRs")]
    if not named or not text or text == key:
        return None
    return text


def ticker_aliases(key, ticker):
    """Aliases from a legacy Ticker cell's parenthetical: 'X (A; was B)' -> 'A; B';
    venue words are not aliases (decision 9)."""
    m = re.search(r"\((.*)\)", ticker)
    if not m:
        return NM
    items = []
    for part in m.group(1).split(";"):
        part = re.sub(r"^\s*was\s+", "", part).strip()
        for item in (clean_alias(p, key) for p in part.split(" / ")):
            if item and item not in items:
                items.append(item)
    return "; ".join(items) if items else NM


# A company cell names the company only: a trailing note on lines, venues or
# former names belongs in aliases: (MODEL section 6.1, decision 9).
COMPANY_NOTE_RE = re.compile(r"\s*\(([^()]*(?:\bADRs?\b|\bNYSE\b|\bOslo:|\bB3:|\bformerly\b|\bf/k/a\b|\buntil \d{4}"
                             r"|\bdual-listing\b|\b[A-Z] shares\b|\bClass [A-Z]\b|\bpreferred\b)[^()]*)\)\s*$")


def company_note(company):
    """(name, note): the company name without a trailing line/venue/former-name note."""
    m = COMPANY_NOTE_RE.search(company or "")
    if not m:
        return company, None
    return company[:m.start()].rstrip(), m.group(1).strip()


def batch_show(root, rev, paths):
    """{path: text} for repo files at rev, read in one `git cat-file --batch`;
    a missing path is absent from the result."""
    paths = list(paths)
    if not paths:
        return {}
    data = "".join("%s:%s\n" % (rev, p) for p in paths).encode("utf-8")
    try:
        proc = subprocess.run(["git", "-C", root, "cat-file", "--batch"], input=data,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    except OSError as exc:
        raise ToolError("git cat-file failed: %s" % exc)
    if proc.returncode != 0:
        raise ToolError("git cat-file failed at %s" % rev)
    out, pos, result = proc.stdout, 0, {}
    for path in paths:
        nl = out.index(b"\n", pos)
        header = out[pos:nl].split()
        if len(header) < 3 or header[1] == b"missing":
            pos = nl + 1
            continue
        size = int(header[2])
        result[path] = out[nl + 1:nl + 1 + size].decode("utf-8")
        pos = nl + 1 + size + 1
    return result


def tree_paths(root, rev, prefix):
    rc, out = run_git(root, ["ls-tree", "-r", "-z", "--name-only", rev, "--", prefix])
    if rc != 0:
        raise ToolError("cannot list %s at %s" % (prefix, rev))
    return [p for p in out.decode("utf-8").split("\0") if p]


def last_applied_sweep(root, base):
    """(path, commit, text) of the newest SWEEP row file added on base's history
    and already consumed (absent at base), or (None, None, None)."""
    rc, out = run_git(root, ["log", "--format=%x01%H", "--name-only", "--diff-filter=A", base, "--",
                             "queue/rows"])
    if rc != 0:
        raise ToolError("cannot read the history of queue/rows at %s" % base)
    present = set(tree_paths(root, base, "queue/rows"))
    for chunk in out.decode("utf-8").split("\x01")[1:]:
        lines = [x for x in chunk.split("\n") if x.strip()]
        commit, files = lines[0].strip(), lines[1:]
        for path in sorted(files, reverse=True):
            if path.endswith("_SWEEP.md") and path not in present:
                text = batch_show(root, commit, [path]).get(path)
                if text is not None:
                    return path, commit, text
    return None, None, None


def sweep_prices(text):
    """{key: (px, unit, close_date)} from a SWEEP row file: the key's own line
    only (old 'Price table' with an Instrument column, or the v4.5.0 refresh
    table). Closes on another line or converted between currencies are left
    out and returned in the second dict with the reason."""
    fm = parse_front_matter(text)
    prices, skipped = {}, {}
    for title, lines in sections_of(text).items():
        low = title.lower()
        if not (low.startswith("price table") or low.startswith("price/ordering refresh")):
            continue
        for row in table_rows(lines):
            key = row.get("key", "").strip("`* ")
            if not KEY_RE.match(key):
                continue
            instrument = row.get("instrument", key).split()[0] if row.get("instrument", key).split() else ""
            unit = row.get("ccy", row.get("px unit", ""))
            close = row.get("close", row.get("px", ""))
            day = row.get("close date", "")
            if instrument.upper() != endpoint_symbol(key).upper():
                skipped.setdefault(key, "SWEEP priced %s, not the key's line" % instrument)
                continue
            converted = re.match(r"^([A-Za-z]{3})\s?→", unit)
            if converted:
                # 'CHF→USD' / 'CHF 70.00 → $84.23': the key's own close is the first figure.
                first = MONEY_RE.search(close)
                if first and currency_of(first.group("cur"), key) == converted.group(1):
                    unit, close = converted.group(1), first.group("num")
            if not UNIT_RE.match(unit) or not DATE_RE.match(day):
                skipped.setdefault(key, "SWEEP close %r %r is not a plain quote" % (unit, close))
                continue
            m = re.match(r"^\s*(%s)\s*(?:\((%s)\))?\s*$" % (NUM_TEXT, NUM_TEXT), close)
            if not m:
                skipped.setdefault(key, "SWEEP close %r unparseable" % close)
                continue
            value = dec(m.group(1).replace(",", ""))
            if m.group(2):
                precise = dec(m.group(2).replace(",", ""))
                if abs(precise - value) <= value * Decimal("0.005"):
                    value = precise
            prices[key] = (plain(value), unit, day)
            skipped.pop(key, None)
    return prices, skipped, fm.get("run_date", "")


def read_assisted(text):
    """Rows of the assisted file: CSV `key,field,value,quote`. A Markdown file
    is read from its first ```csv fenced block (the REBUILD report appendix)."""
    if "```csv" in text:
        text = text.split("```csv", 1)[1].split("```", 1)[0].lstrip("\n")
    reader = csv.reader(io.StringIO(text.replace("\r\n", "\n"), newline=""))
    header = next(reader, None)
    if header != ["key", "field", "value", "quote"]:
        raise ToolError("assisted file header must be key,field,value,quote (got %r)" % (header,))
    rows = []
    for number, cells in enumerate(reader, start=2):
        if not cells:
            continue
        if len(cells) != 4:
            raise ToolError("assisted file line %d: %d fields, expected 4" % (number, len(cells)))
        key, field, value, quote = (c.strip() for c in cells)
        if field not in ASSISTED_FIELDS:
            raise ToolError("assisted file line %d: field %r is not assisted" % (number, field))
        rows.append({"line": number, "key": key, "field": field, "value": value, "quote": quote})
    return rows


def assisted_text(rows):
    buf = io.StringIO(newline="")
    writer = csv.writer(buf, lineterminator="\n")
    writer.writerow(["key", "field", "value", "quote"])
    for r in rows:
        writer.writerow([r["key"], r["field"], r["value"], r["quote"]])
    return buf.getvalue()


# Decision 9 (never invent a number): every numeric assisted value must follow
# from the numbers in its own memo quote - the number itself, the number in
# another scale (k/m/bn, minor units), a signed sum of quoted numbers (a debt
# build: borrowings + leases + NCI), or a quotient or product of two of them
# (an EV difference over a price, an inverse FX rate, a leg over its 7x/8x
# threshold). The memo price (price_at_memo) and the constants 1, 7 and 8 are
# operands too. Anything else is rejected, never used.
TRACE_SCALES = (1000.0, 0.001, 1000000.0, 0.000001, 100.0, 0.01)
TRACE_CONSTANTS = (1.0, 7.0, 8.0)
MAX_DECIMALS = 6


def quoted_numbers(text):
    """The numbers of a memo passage, in order, without duplicates; a number
    written with a sign attached ('−47.2m') also counts as negative."""
    out = []
    for m in re.finditer(r"([−-]?)(%s)" % NUM_TEXT, norm_text(text)):
        try:
            value = float(m.group(2).replace(",", ""))
        except ValueError:
            continue
        for v in ((value, -value) if m.group(1) else (value,)):
            if v not in out:
                out.append(v)
    return out


def trace_value(value, quote, extra=()):
    """How `value` follows from the numbers in `quote` (plus `extra` operands):
    'quoted', 'scaled', 'sum of n', 'quotient' or 'product'; None when it does not."""
    v = float(value)
    tol = max(0.0005, abs(v) * 0.00001)

    def near(x):
        return abs(x - v) <= tol
    nums = quoted_numbers(quote)
    if any(near(n) for n in nums):
        return "quoted"
    if any(near(n * s) for n in nums for s in TRACE_SCALES):
        return "scaled"
    widest = 6 if len(nums) <= 12 else 4 if len(nums) <= 20 else 3
    for k in range(2, min(widest, len(nums)) + 1):
        for combo in itertools.combinations(nums, k):
            for signs in itertools.product((1, -1), repeat=k):
                if near(sum(sg * c for sg, c in zip(signs, combo))):
                    return "sum of %d" % k
    operands = nums + [float(x) for x in extra if x not in nums] + list(TRACE_CONSTANTS)
    for scale in (1.0, 0.001, 1000.0):
        for a in operands:
            for b in operands:
                if b and near(a / b * scale):
                    return "quotient"
                if near(a * b * scale):
                    return "product"
    return None


def decimals(text):
    return len(text.split(".", 1)[1]) if "." in text else 0


# ------------------------------------------------------------------ rebuild: one row

def validate_core(core, memo_px, memo_unit, printed):
    """Accept core numbers per field: a field stands only when a memo multiple
    it feeds reproduces the printed value within 5% at the memo price. Returns
    (accepted core dict, report string)."""
    computed = compute_metrics(core, plain(memo_px), memo_unit)
    ok, checks = {}, []
    numeric = [n for n in MULTIPLES if MULT_RE.match(printed[n] or "")]
    for name in MULTIPLES:
        p, c = printed[name], computed[name]
        if MULT_RE.match(p or "") and MULT_RE.match(c or ""):
            ratio = Decimal(c) / Decimal(p) if Decimal(p) else Decimal(0)
            ok[name] = Decimal("0.95") <= ratio <= Decimal("1.05") if Decimal(p) else False
        elif p == NM and c == NM:
            ok[name] = True
        else:
            ok[name] = False
        checks.append("%s %s/%s %s" % (name, c, p, "ok" if ok[name] else "no"))
    single = printed.get("_ev_single") and MULT_RE.match(printed["ev_oi"] or "") and (
        not ok["ev_oi"] or (MULT_RE.match(computed["ev_oi_all_cash"] or "") and MULT_RE.match(computed["ev_oi"] or "")
                            and abs(Decimal(computed["ev_oi_all_cash"]) - Decimal(printed["ev_oi"])) <= Decimal("0.1")
                            < abs(Decimal(computed["ev_oi"]) - Decimal(printed["ev_oi"]))))
    if single and MULT_RE.match(computed["ev_oi_all_cash"] or "") and MULT_RE.match(printed["ev_oi"] or ""):
        if Decimal("0.95") <= Decimal(computed["ev_oi_all_cash"]) / Decimal(printed["ev_oi"]) <= Decimal("1.05"):
            # A single EV/OI printed without its variant label is the all-cash reading here.
            ok["ev_oi"] = ok["ev_oi_all_cash"] = True
            checks.append("the single unlabelled EV/OI %s is the all-cash reading" % printed["ev_oi"])
    reproduced = [n for n in numeric if ok[n]]
    accepted = {name: OWED for name in CORE_FIELDS}
    if len(numeric) >= 2 and len(reproduced) < 2:
        return accepted, "rejected (%s)" % "; ".join(checks)
    if not any(ok.values()):
        return accepted, "rejected (%s)" % "; ".join(checks)
    keep = {"core_period", "core_currency", "core_unit", "core_shares_diluted", "core_fx", "core_fx_date",
            "core_ratio"}
    if ok["mcap_fcf"]:
        keep |= {"core_fcf", "core_fcf_basis"}
    if ok["ev_oi"]:
        keep |= {"core_oi", "core_oi_basis", "core_debt_eq"}
        if ok["ev_oi_all_cash"]:
            keep.add("core_cash")
    elif ok["ev_oi_all_cash"] and core.get("core_oi") == NM:
        keep |= {"core_oi", "core_oi_basis"}
    elif ok["ev_oi_all_cash"] and printed["ev_oi"] == OWED:
        # The memo prints only the all-cash reading; its quoted debt and cash stand together.
        keep |= {"core_oi", "core_oi_basis", "core_debt_eq", "core_cash"}
    for name in keep:
        accepted[name] = core.get(name, OWED)
    return accepted, "accepted %s (%s)" % (
        ", ".join(sorted(n for n in keep if n in CORE_NUMBERS and accepted[n] != OWED)), "; ".join(checks))


def rebuild_row(key, entry, memo_path, memo_text, held_cells, sweep, assisted, notes, pending):
    """One register.csv row from the outgoing register entry, its memo, the
    applied SWEEP and the assisted rows for the key. notes collects
    (kind, text) report lines."""
    fm = parse_front_matter(memo_text)
    cells = entry["cells"]
    log = []
    m = MEMO_PATH_RE.match(memo_path)
    row = {name: OWED for name in CSV_HEADER}
    row.update(LENS_DEFAULTS)          # the legacy memos the rebuild reads carry no lens fields
    row.update(R10_DEFAULTS)           # nor the round-2 fields: an all-cash trigger, averages owed
    row["key"] = key
    row["company"], company_extra = company_note(fm.get("company") or cells.get("company") or OWED)
    if company_extra:
        notes.append(("normalised", "%s company: note %r dropped from the cell (aliases from the assisted file)"
                      % (key, company_extra[:70])))
    raw_isin = (fm.get("isin") or "").strip()
    token = raw_isin.split()[0] if raw_isin else ""
    row["isin"] = token if ISIN_RE.match(token) else OWED
    if row["isin"] == OWED:
        notes.append(("isin", "%s: ISIN not established in the memo (%s)" % (key, raw_isin[:70] or "no isin field")))
    row["aliases"] = ticker_aliases(key, entry["ticker"])
    for name, src in (("verdict", "verdict"), ("past", "quality_past"), ("future", "quality_future"), ("sf", "sf")):
        raw = fm.get(src, "")
        value = first_token(raw)
        if value != raw:
            notes.append(("normalised", "%s %s: %r -> %r" % (key, src, raw[:70], value)))
        row[name] = value or OWED
    legacy_verdict = first_token(cells.get("verdict", ""))
    if legacy_verdict == "DNAF" and row["verdict"] != "DNAF":
        notes.append(("held-dnaf", "%s: the register made the row DNAF after its memo (%s); the memo says %s. "
                      "DNAF kept; a Gate-0 memo is owed (register-integrity hold)" % (
                          key, cells.get("verdict", "")[:60], row["verdict"])))
        row["verdict"] = "DNAF"
    gates = gates_failed(row["past"], row["future"], row["sf"])
    row["gates_failed"] = str(gates)
    row["section"] = section_for(row["verdict"], gates) or OWED
    dnaf = row["verdict"] == "DNAF"
    row["memo_path"] = memo_path
    row["memo_date"] = m.group("date")
    version = re.match(r"^v\d+", fm.get("memo_version", ""))
    if version:
        row["memo_version"] = version.group(0)
        if version.group(0) != fm.get("memo_version"):
            notes.append(("normalised", "%s memo_version: %r -> %r" % (key, fm.get("memo_version", "")[:60],
                                                                        version.group(0))))
    elif VER_RE.match(cells.get("ver", "")):
        row["memo_version"] = cells["ver"]
        notes.append(("normalised", "%s memo_version: none in the memo; register Ver %s used" % (key, cells["ver"])))
    row["model_version"] = (fm.get("model_version") or OWED).split()[0]
    if pending:
        notes.append(("pending", "%s: the register cites %s; a pending row moves it to %s at the next INTAKE"
                      % (key, memo_path, pending)))
    # Price, unit and date.
    quote_unit = default_unit(key)
    by_field = {}
    for a in assisted:
        by_field.setdefault(a["field"], []).append(a)
    if "aliases" in by_field:
        items = [] if row["aliases"] in (NM, OWED) else row["aliases"].split("; ")
        for item in (x.strip() for x in by_field["aliases"][0]["value"].split(";")):
            if item and item != key and item not in items:
                items.append(item)
        row["aliases"] = "; ".join(items) if items else NM
    if "px_unit" in by_field:
        quote_unit = by_field["px_unit"][0]["value"]
        notes.append(("px", "%s: quote unit %s from the price endpoint (%s), not the suffix default %s" % (
            key, quote_unit, by_field["px_unit"][0]["quote"][:80], default_unit(key))))
    memo_px, memo_unit, memo_day, how = parse_memo_price(fm.get("price_at_memo", ""), key, fm.get("currency", ""),
                                                         quote_unit)
    if how and memo_px is not None and memo_unit and "later" in how:
        notes.append(("px", "%s: %s" % (key, how)))
    memo_q = None
    if memo_px is not None and memo_unit:
        memo_q, conv = to_quote_unit(memo_px, memo_unit, quote_unit)
        if conv and memo_q is not None:
            notes.append(("converted", "%s memo price %s %s -> %s %s" % (key, plain(memo_px), memo_unit,
                                                                         plain(memo_q), quote_unit)))
    in_scope = row["section"] in ("BUY", "WATCH", "AVOID-1") or bool(held_cells)
    sweep_prices_by_key, sweep_skipped, sweep_date = sweep
    px_cell = cells.get("px @ memo", "")
    used_sweep = False
    if in_scope and key in sweep_prices_by_key:
        spx, sunit, sday = sweep_prices_by_key[key]
        y, mo, d = sday.split("-")
        shown = "%d %s %s" % (int(d), MONTHS[int(mo) - 1], y)
        if shown in px_cell and sunit == quote_unit:
            row["px"], row["px_unit"], row["px_date"] = spx, sunit, sday
            row["px_source"] = "SWEEP %s" % sweep_date
            used_sweep = True
        else:
            notes.append(("px", "%s: SWEEP %s close %s %s %s not used (register Px cell %r)" % (
                key, sweep_date, sunit, spx, sday, px_cell[:50])))
    elif in_scope and key in sweep_skipped:
        notes.append(("px", "%s: %s; the memo price is used" % (key, sweep_skipped[key])))
    if not used_sweep:
        row["px_source"] = "memo"
        if memo_q is not None:
            row["px"], row["px_unit"] = plain(memo_q), quote_unit
            row["px_date"] = memo_day or OWED
            if memo_day is None:
                notes.append(("px", "%s: memo price %r has no close date" % (key, fm.get("price_at_memo", "")[:60])))
        else:
            row["px_unit"] = quote_unit
            notes.append(("px", "%s: memo price %r is not on the key's line or unit (%s): Px owed" % (
                key, fm.get("price_at_memo", "")[:60], how or ("%s vs %s" % (memo_unit, quote_unit)))))
    # Trigger.
    if dnaf:
        row["trigger"] = NM
    else:
        t_value, t_unit, t_how = operative_trigger(fm.get("trigger_band", ""), key, memo_unit)
        if "trigger" in by_field:
            a = by_field["trigger"][0]
            row["trigger"] = a["value"]
            notes.append(("trigger", "%s: assisted trigger %s (parser: %s)" % (
                key, a["value"], plain(t_value) if t_value is not None else t_how)))
        elif t_how == "n.m.":
            row["trigger"] = NM
        elif t_value is None:
            notes.append(("trigger", "%s: trigger not parsed (%s): owed" % (key, t_how)))
        else:
            q, conv = to_quote_unit(t_value, t_unit, quote_unit)
            if q is None:
                notes.append(("trigger", "%s: trigger %s %s is not in the quote unit %s: owed" % (
                    key, plain(t_value), t_unit, quote_unit)))
            else:
                row["trigger"] = plain(q)
                if "C6" in t_how or "C4a" in t_how or "anchor" in t_how:
                    notes.append(("trigger", "%s: %s -> %s" % (key, t_how, row["trigger"])))
        dist = re.match(r"^\s*([+−-]?\d+)%", cells.get("dist %", "").replace("−", "-"))
        if dist and is_num(row["trigger"]) and used_sweep:
            implied = dec(row["px"]) / (1 + Decimal(dist.group(1)) / 100)
            if abs(implied / dec(row["trigger"]) - 1) > Decimal("0.02"):
                notes.append(("trigger-diff", "%s: trigger %s; the outgoing register's Dist %s implies about %s "
                              "(memo wins)" % (key, row["trigger"], cells.get("dist %"), plain(implied.quantize(
                                  Decimal("0.01"))))))
    # Core numbers (assisted only) and multiples.
    printed = memo_multiples(memo_text)
    for name in MULTIPLES:
        if "printed_" + name in by_field:
            a = by_field["printed_" + name][0]
            printed[name] = a["value"] if a["value"] in (OWED, NM) else fmt1(dec(a["value"]))
            printed.pop("_ev_single", None)
            notes.append(("core", "%s: the memo prints %s %s (assisted read: %r)" % (
                key, name, printed[name], a["quote"][:60])))
    core_in = {name: by_field[name][0]["value"] for name in CORE_FIELDS if name in by_field}
    if core_in and not dnaf:
        memo_quote_unit = quote_unit if memo_q is not None else None
        if memo_quote_unit is None or row["px_unit"] != memo_quote_unit:
            notes.append(("core", "%s: core numbers not validated: the memo price is not on the key's unit" % key))
        else:
            accepted, how = validate_core(core_in, memo_q, quote_unit, printed)
            for name in CORE_FIELDS:
                row[name] = accepted[name]
            if any(row[n] != OWED for n in CORE_NUMBERS):
                row["core_source"] = "rebuild-assisted"
            derived = []
            for name in CORE_NUMBERS:
                if row[name] in (OWED, NM) or name in by_field and by_field[name][0]["quote"] in ("", "-"):
                    continue
                quoted = norm_text(by_field[name][0]["quote"]).replace(",", "")
                if not re.search(r"(?<![\d.])%s(?![\d])" % re.escape(row[name]), quoted):
                    derived.append(name)
            if derived:
                how += "; derived from the quoted figures (not printed as such): %s" % ", ".join(derived)
            notes.append(("core", "%s: %s" % (key, how)))
            if row["core_source"] != OWED:
                at_memo = compute_metrics(row, plain(memo_q), quote_unit)
                pairs = [(n, n) for n in MULTIPLES]
                if printed.get("_ev_single") and MULT_RE.match(printed["ev_oi"] or "") and all(
                        MULT_RE.match(at_memo[n] or "") for n in ("ev_oi", "ev_oi_all_cash")):
                    # One unlabelled EV/OI: it is whichever reading it is closer to.
                    p = Decimal(printed["ev_oi"])
                    closer = min(("ev_oi", "ev_oi_all_cash"), key=lambda n: abs(Decimal(at_memo[n]) - p))
                    pairs = [("mcap_fcf", "mcap_fcf"), (closer, "ev_oi")]
                gaps = ["%s %s vs %s" % (n, at_memo[n], printed[q]) for n, q in pairs
                        if MULT_RE.match(at_memo[n] or "") and MULT_RE.match(printed[q] or "")
                        and abs(Decimal(at_memo[n]) - Decimal(printed[q])) > Decimal("0.1")]
                if gaps:
                    notes.append(("print-diff", "%s: at the memo price the accepted core numbers give %s (memo "
                                  "print)" % (key, "; ".join(gaps))))
    if dnaf:
        for name in MULTIPLES:
            row[name] = NM
    elif row["core_source"] != OWED:
        row.update(compute_metrics(row, row["px"], row["px_unit"]))
    elif row["px_source"] == "memo" and is_num(row["px"]):
        for name in MULTIPLES:
            row[name] = printed[name]
    # Reasons.
    for name in ("past_reason", "future_reason", "sf_reason"):
        if name in by_field:
            row[name] = by_field[name][0]["value"]
    if row["past_reason"] == OWED and row["past"] in ("STRONG", "ADEQUATE"):
        level, quote = past_level(memo_text)
        if level:
            row["past_reason"] = level
            log.append("past %s from %r" % (level, quote[:60]))
    if row["future_reason"] == OWED and row["future"] in ("STRONG", "ADEQUATE"):
        row["future_reason"] = NM
    if row["sf_reason"] == OWED and row["sf"] == "PASS":
        sf_text = (fm.get("sf", "") + " " + cells.get("sf", "")).lower()
        caution = re.search(r"caution|\b[1-9] flag|flag pair", sf_text) and not re.search(r"\b0 flags?\b", sf_text)
        if not caution:
            row["sf_reason"] = NM
    if dnaf:
        for name in ("past_reason", "future_reason", "sf_reason"):
            if row[name] == OWED:
                row[name] = NM
    # Next review.
    if dnaf:
        row["next_review_short"] = NM
    elif "next_review_short" in by_field:
        row["next_review_short"] = by_field["next_review_short"][0]["value"]
    else:
        row["next_review_short"] = parse_next_review_short(fm.get("next_review", ""), row["memo_date"])
    # Position (held names): from the outgoing Portfolio table.
    for name in ("zone", "add_band", "sell_line", "last_zone_check", "avg_cost"):
        row[name] = NM
    row["held"] = "false"
    if held_cells:
        row["held"] = "true"
        position_from_register(row, held_cells, notes)
    if log:
        notes.append(("source", "%s: %s" % (key, "; ".join(log))))
    return row


def position_from_register(row, cells, notes):
    """Zone, ADD band, sell line, last zone check and avg cost of a held name
    from its outgoing Portfolio-table cells (numbers in the key's quote unit)."""
    key, unit = row["key"], row["px_unit"]
    zone = cells.get("zone", "").replace("*", "")
    m = re.match(r"\s*(ADD|HOLD|SELL-FLAG)\b(?:\s*\((SR[1-3])\b)?", zone)
    row["zone"] = (m.group(1) + (" " + m.group(2) if m.group(2) else "")) if m else OWED

    def line_value(text):
        text = text.replace("*", "")
        if re.match(r"(?i)\s*(n/a|n\.m\.)", text):
            return NM
        mm = MONEY_RE.search(text)
        if not mm:
            return OWED
        cur = "GBp" if mm.group("p") else currency_of(mm.group("cur"), key)
        value = dec(mm.group("num").replace(",", ""))
        q, _conv = to_quote_unit(value, cur or unit, unit)
        return plain(q) if q is not None else OWED

    add_cell = [v for k, v in cells.items() if k.startswith("add band")]
    sell_cell = [v for k, v in cells.items() if k.startswith("sell")]
    row["add_band"] = line_value(add_cell[0]) if add_cell else OWED
    row["sell_line"] = line_value(sell_cell[0]) if sell_cell else OWED
    check = cells.get("last zone check", "")
    iso = ISO_DATE_RE.search(check)
    close = re.search(r"\((\d{1,2}) (%s)[a-z]* close\)" % "|".join(MONTHS), check)
    if iso and close:
        row["last_zone_check"] = "%s-%02d-%02d" % (iso.group(1), MONTHS.index(close.group(2)) + 1, int(close.group(1)))
    elif iso:
        row["last_zone_check"] = iso.group(0)
    else:
        row["last_zone_check"] = OWED
    cost = cells.get("avg cost", "")
    mm = MONEY_RE.search(cost)
    if mm and currency_of(mm.group("cur"), key):
        rest = cost[mm.end():].strip()
        row["avg_cost"] = "%s %s%s" % (mm.group("num").replace(",", ""), currency_of(mm.group("cur"), key),
                                       (" " + rest) if rest else "")
    else:
        row["avg_cost"] = OWED
    notes.append(("position", "%s: zone %s · ADD band %s · sell line %s · last zone check %s · avg cost %s "
                  "(from the outgoing Portfolio table)" % (key, row["zone"], row["add_band"], row["sell_line"],
                                                          row["last_zone_check"], row["avg_cost"])))


# ------------------------------------------------------------------ rebuild: driver

def rebuild(root, base, assisted_path=None, version=None, date=None):
    """The rebuild's outputs: (register.csv text, _REGISTER.md text, report
    text, backfill block text, rows)."""
    rc, out = run_git(root, ["rev-parse", "--verify", base + "^{commit}"])
    if rc != 0:
        raise ToolError("cannot resolve --base %s" % base)
    base = out.decode().strip()
    old_text = batch_show(root, base, [REGISTER_FILE]).get(REGISTER_FILE)
    if old_text is None:
        raise ToolError("no %s at %s" % (REGISTER_FILE, base))
    master, portfolio, old_fm = legacy_register(old_text)
    if not master:
        raise ToolError("the register at %s has no legacy master table (already lean?)" % base)
    old_version = old_fm.get("register_version", "")
    if not VER_RE.match(old_version):
        raise ToolError("outgoing register_version %r is not vN" % old_version)
    version = version or "v%d" % (int(old_version[1:]) + 1)
    date = date or old_fm.get("register_date", "")
    memo_files = set(tree_paths(root, base, "memos")) | set(tree_paths(root, base, "archive/memos"))
    pending_rows = {p: t for p, t in batch_show(root, base, tree_paths(root, base, "queue/rows")).items()
                    if p.endswith(".md")}
    pending_memo = {}
    for path, text in pending_rows.items():
        rfm = parse_front_matter(text)
        mm = MEMO_PATH_RE.match(rfm.get("memo_path", ""))
        if mm and rfm.get("row_type", "").upper() in ("ANALYSE", "REVIEW"):
            pending_memo[mm.group("key")] = rfm["memo_path"]
    memo_paths = {}
    for key, entry in master.items():
        day = entry["cells"].get("memo date", "")
        path = "memos/%s/%s_%s_GSC.md" % (key, key, day)
        if path in memo_files:
            memo_paths[key] = (path, path, None)
        elif "archive/" + path in memo_files and key in pending_memo:
            memo_paths[key] = (path, "archive/" + path, pending_memo[key])
        else:
            raise ToolError("%s: the register cites %s, which is neither a current memo nor an archived one "
                            "with a pending row" % (key, path))
    texts = batch_show(root, base, sorted(src for _p, src, _q in memo_paths.values()))
    sweep_path, sweep_commit, sweep_text = last_applied_sweep(root, base)
    sweep = sweep_prices(sweep_text) if sweep_text else ({}, {}, "")
    assisted_rows, assisted_problems = [], []
    if assisted_path:
        with open(assisted_path, "rb") as fh:
            assisted_raw = fh.read().decode("utf-8")
        assisted_rows = read_assisted(assisted_raw)
    by_key, memo_prices, traced = {}, {}, {}
    for a in assisted_rows:
        if a["key"] not in master:
            assisted_problems.append("line %d: %s is not a register key" % (a["line"], a["key"]))
            continue
        _p, src, _q = memo_paths[a["key"]]
        memo_norm = norm_text(texts[src])
        if a["field"] == "px_unit":
            if not UNIT_RE.match(a["value"]) or not a["quote"].startswith("endpoint "):
                assisted_problems.append("line %d: %s px_unit needs a quote unit and the endpoint evidence "
                                         "('endpoint YYYY-MM-DD: currency …')" % (a["line"], a["key"]))
                continue
        elif a["quote"] in ("", "-"):
            if a["field"] not in QUOTE_OPTIONAL and not (a["field"] in ("core_fx", "core_ratio") and a["value"] == "1") \
                    and not (a["field"].startswith("printed_") and a["value"] == OWED):
                assisted_problems.append("line %d: %s %s has no memo quote" % (a["line"], a["key"], a["field"]))
                continue
        elif norm_text(a["quote"]) not in memo_norm:
            assisted_problems.append("line %d: %s %s quote not found in %s: %r" % (
                a["line"], a["key"], a["field"], src, a["quote"][:60]))
            continue
        problems = []
        if a["field"] in ("past_reason", "future_reason", "sf_reason"):
            probe = {name: NM for name in CSV_HEADER}
            probe.update({"key": a["key"], a["field"]: a["value"]})
            kind = {"past_reason": "past", "future_reason": "future", "sf_reason": "sf"}[a["field"]]
            if not reason_ok(kind, a["value"]):
                problems.append("not in the Past vocabulary" if kind == "past" else "not in the section 7.1 vocabulary")
        elif a["field"] in CORE_NUMBERS or a["field"] == "trigger":
            if not (is_num(a["value"]) or a["value"] == NM):
                problems.append("not a plain number")
        elif a["field"].startswith("printed_"):
            if not (is_num(a["value"]) or a["value"] in (NM, OWED)):
                problems.append("not a multiple, n.m. or -")
        elif a["field"] == "core_unit" and a["value"] not in SCALE:
            problems.append("core_unit is not k, m or bn")
        elif a["field"] == "core_currency" and not CCY_RE.match(a["value"]):
            problems.append("core_currency is not an ISO code")
        elif a["field"] == "next_review_short" and not NEXT_REVIEW_RE.match(a["value"]):
            problems.append("next_review_short pattern")
        elif a["field"] == "aliases" and any(clean_alias(x, a["key"]) != x.strip()
                                             for x in a["value"].split(";")):
            problems.append("an alias is empty, the key itself or a bare venue or ratio")
        if (a["field"] in CORE_NUMBERS or a["field"] == "trigger" or a["field"].startswith("printed_")) \
                and is_num(a["value"]) and not problems:
            if decimals(a["value"]) > MAX_DECIMALS:
                problems.append("more than %d decimal places (write the memo's own precision)" % MAX_DECIMALS)
            elif a["quote"] not in ("", "-"):
                if a["key"] not in memo_prices:
                    memo_prices[a["key"]] = quoted_numbers(parse_front_matter(texts[src]).get("price_at_memo", ""))
                how = trace_value(a["value"], a["quote"], memo_prices[a["key"]])
                if how is None:
                    problems.append("not a number of its quote, nor a unit scaling, sum or quotient of the "
                                    "quote's numbers")
                else:
                    traced[how.split()[0]] = traced.get(how.split()[0], 0) + 1
        if problems:
            assisted_problems.append("line %d: %s %s %r: %s" % (a["line"], a["key"], a["field"], a["value"],
                                                               "; ".join(problems)))
            continue
        if any(b["field"] == a["field"] for b in by_key.get(a["key"], [])):
            assisted_problems.append("line %d: %s %s given twice; the first stands" % (a["line"], a["key"], a["field"]))
            continue
        by_key.setdefault(a["key"], []).append(a)
    notes, rows = [], []
    for key, entry in master.items():
        path, src, pending = memo_paths[key]
        rows.append(rebuild_row(key, entry, path, texts[src], portfolio.get(key), sweep, by_key.get(key, []),
                                notes, pending))
    errors = []
    for row in rows:
        errors += ["%s: %s" % (row["key"], e) for e in validate_row(row)]
    if errors:
        raise ToolError("the rebuild yields invalid rows:\n  " + "\n  ".join(errors))
    missing_portfolio = sorted(set(portfolio) - set(master))
    if missing_portfolio:
        raise ToolError("portfolio keys missing from the master table: %s" % ", ".join(missing_portfolio))
    csv_out = csv_text(rows)
    md_out = render(rows, version, date)
    report = rebuild_report(rows, notes, assisted_problems, assisted_rows, base, old_version, version, date,
                            sweep_path, sweep_commit, old_fm, traced)
    backfill = backfill_block(rows, version, date)
    return csv_out, md_out, report, backfill, rows


def owed_fields(row):
    return [name for name in CSV_HEADER if row[name] == OWED and name not in ("core_source",)]


BACKFILL_FIELDS = (("isin", "ISIN"), ("px", "Px"), ("px_date", "Px date"), ("trigger", "trigger"),
                   ("past_reason", "Past reason"), ("future_reason", "Future reason"), ("sf_reason", "SF reason"),
                   ("next_review_short", "next review"), ("memo_version", "Ver"))
CORE_SHORT = (("core_shares_diluted", "shares"), ("core_debt_eq", "debt-eq"), ("core_cash", "cash"),
              ("core_oi", "OI"), ("core_fcf", "FCF"), ("core_fx", "FX"))


def backfill_items(row):
    """The register-visible fields a row still owes (descriptive core labels
    and the model version are left to the next REVIEW memo, not listed)."""
    items = [label for name, label in BACKFILL_FIELDS if row[name] == OWED]
    if row["px"] != OWED and row["px_source"] == "memo" and (row["held"] == "true" or row["section"] in ("BUY", "WATCH")):
        # In SWEEP scope but memo-priced: the last SWEEP did not price the key's own line.
        items.append("Px on the key's line (the last SWEEP did not price it)")
    skip = {"core_debt_eq", "core_cash"} if row["core_oi"] == NM else set()
    core = [label for name, label in CORE_SHORT if row[name] == OWED and name not in skip]
    if core:
        items.append("core numbers (%s)" % ", ".join(core) if len(core) < len(CORE_SHORT) else "core numbers")
    return items


def backfill_block(rows, version, date):
    """The TODO head block listing every in-scope key with an owed field."""
    lines = ["## ▶ Backfill owed — register rebuild %s (%s)" % (version, date), "",
             "*Register values the lean rebuild could not establish from a memo, the outgoing register or the last "
             "SWEEP (MODEL §7.1b; never invented). Held, BUY, WATCH and one-gate AVOID keys, one line each; the "
             "next REVIEW memo fills them, or an attended pass with a memo quote. Descriptive core labels "
             "(period, bases) are left to the next REVIEW.*", ""]
    in_scope = [r for r in canonical(rows) if r["held"] == "true" or r["section"] in ("BUY", "WATCH", "AVOID-1")]
    for row in in_scope:
        items = backfill_items(row)
        if items:
            lines.append("- `%s` — backfill: %s — fill at next REVIEW or attended pass" % (row["key"], ", ".join(items)))
    others = [r for r in rows if r not in in_scope and backfill_items(r)]
    lines.append("- AVOID two-or-more-gate and DNAF rows: %d keys with owed values, never priced — filled by each "
                 "name's next REVIEW memo; list in the REBUILD report." % len(others))
    return "\n".join(lines) + "\n"


def rebuild_report(rows, notes, problems, assisted_rows, base, old_version, version, date, sweep_path,
                   sweep_commit, old_fm, traced=None):
    by_kind = {}
    for kind, text in notes:
        by_kind.setdefault(kind, []).append(text)
    n = {s: sum(1 for r in rows if r["section"] == s) for s in SECTION_ORDER}
    in_scope = [r for r in rows if r["held"] == "true" or r["section"] in ("BUY", "WATCH", "AVOID-1")]
    with_core = [r for r in in_scope if r["core_source"] != OWED]
    full_core = [r for r in in_scope if all(r[c] != OWED for c in CORE_NUMBERS)]
    numeric_ev = [r for r in rows if r["section"] == "WATCH" and r["ev_oi"] != OWED]
    out = [
        "# Lean register rebuild — %s → %s (%s)" % (old_version, version, date),
        "",
        "One-time switch to the lean register (MODEL v4.5.0 §7.1, §7.1b), written by `gsc_register.py rebuild "
        "--base %s`. The outgoing register is archived byte for byte as `REGISTER_%s_%s.md` beside this report."
        % (base, old_version, old_fm.get("register_date", "")),
        "",
        "## Rules",
        "",
    ]
    out += ["%d. %s" % (i + 1, rule) for i, rule in enumerate(REBUILD_RULES)]
    out += [
        "",
        "## Inputs",
        "",
        "- Base: `%s` — outgoing register %s (%s), %s names." % (base, old_version, old_fm.get("register_date", ""),
                                                                 old_fm.get("names_total", "?")),
        "- Last applied SWEEP: `%s` (added in %s)." % (sweep_path or "none", (sweep_commit or "-")[:12]),
        "- Assisted file: %d rows (embedded below); %d rejected." % (len(assisted_rows), len(problems)),
        "- Assisted numbers traced to their memo quote: %s." % (" · ".join(
            "%s %d" % (k, (traced or {}).get(k, 0)) for k in ("quoted", "scaled", "sum", "quotient", "product"))),
        "",
        "## Counts",
        "",
        "| Measure | Value |",
        "|---|---|",
        "| Names | %d |" % len(rows),
        "| Split | BUY %d · WATCH %d · AVOID %d (one gate %d · two+ %d) · DNAF %d |" % (
            n["BUY"], n["WATCH"], n["AVOID-1"] + n["AVOID-2"], n["AVOID-1"], n["AVOID-2"], n["DNAF"]),
        "| Held | %d |" % sum(1 for r in rows if r["held"] == "true"),
        "| In SWEEP scope (held, BUY, WATCH, one-gate AVOID) | %d |" % len(in_scope),
        "| In scope with core numbers (any) | %d (%s) |" % (len(with_core), fmt_share(len(with_core), len(in_scope))),
        "| In scope with every core number | %d (%s) |" % (len(full_core), fmt_share(len(full_core), len(in_scope))),
        "| WATCH rows with EV/OI shown (number or n.m.) | %d of %d |" % (len(numeric_ev), n["WATCH"]),
        "| Rows with at least one owed field | %d |" % sum(1 for r in rows if owed_fields(r)),
        "",
    ]
    sections = (
        ("held-dnaf", "Register-held DNAF rows (register-integrity hold)"),
        ("pending", "Rows citing an archived memo (pending row at the base)"),
        ("normalised", "Normalisations"),
        ("converted", "Unit conversions"),
        ("px", "Price notes"),
        ("trigger", "Trigger notes"),
        ("trigger-diff", "Trigger differences against the outgoing register"),
        ("core", "Core-number validation"),
        ("print-diff", "Recomputed multiples more than 0.1 from the memo's print at the memo price (basis "
                       "differences inside the memo; check at the next REVIEW)"),
        ("position", "Held positions"),
        ("isin", "ISIN gaps"),
        ("source", "Past level sources"),
    )
    for kind, title in sections:
        items = by_kind.get(kind, [])
        out += ["## %s (%d)" % (title, len(items)), ""]
        out += ["- %s" % cell_text(t) for t in items] if items else ["None."]
        out.append("")
    out += ["## Assisted rows rejected (%d)" % len(problems), ""]
    out += ["- %s" % cell_text(p) for p in problems] if problems else ["None."]
    out += ["", "## Owed fields per key", "", "| Key | Section | Px source | Core | Owed |", "|---|---|---|---|---|"]
    for row in canonical(rows):
        owed = owed_fields(row)
        out.append(table_line([row["key"], row["section"] + (" · held" if row["held"] == "true" else ""),
                               row["px_source"], row["core_source"], ", ".join(owed) if owed else "none"]))
    out += ["", "## Appendix — assisted file (verbatim)", "",
            "Each row carries a verbatim memo quote; the rebuild re-checks every quote and every core number.", "",
            "```csv", assisted_text(assisted_rows).rstrip("\n"), "```", ""]
    return "\n".join(out)


def fmt_share(part, whole):
    return "%d%%" % int(round(100.0 * part / whole)) if whole else "n/a"


# ------------------------------------------------------------------ retrigger (one-time, attended; round 2, R10)
#
# Before round 2 the operative trigger was the looser all-cash reading (capped by the
# FCF leg); R10 makes it the no-cash bound, the strict all-pass line. Every row read
# under the old rule carries trigger_basis all-cash. This pass re-reads each such row
# from its own current memo (memo wins): a held name takes its ADD band (P21: the
# ADD band is the no-cash bound), every other row the figure its trigger_band labels
# no-cash, capped by a printed FCF leg; trigger = min(old trigger, that figure). A
# row the parser cannot read keeps all-cash and is listed for an attended pass with
# a verbatim memo quote (--assisted) or its next memo. Nothing is invented.

RETRIGGER_RULES = (
    "Scope: rows whose trigger_basis is all-cash (the pre-R10 reading). A numeric trigger is re-read; an n.m. "
    "trigger is n.m. under both readings (no positive all-cash price means no no-cash one) and takes no-cash; an "
    "owed trigger ('-') stays as it is.",
    "Held names: the ADD band is the operative trigger, the no-cash bound (P21), so a numeric ADD band is the new "
    "trigger; an ADD band above the old trigger is listed, never used.",
    "Every other row: the figure the memo's trigger_band labels no-cash ('no-cash', 'nc', 'no-excess-cash'; "
    "'conservative' is not a label, memos use it for either variant) - the headline figure or pair when labelled "
    "(a pair's lower bound), a headline the FCF leg binds together with any labelled EV/OI no-cash figure (or alone "
    "when the band says it binds both variants), else the lowest labelled figure; allowance edges, TTM and reference "
    "readings never count. A printed single FCF leg (not strict, all-capex or a reference) caps it. The new "
    "trigger is the lower of the old trigger and that figure: the old one already carries the FCF leg (MODEL "
    "section 7.1), and the no-cash bound is never above the all-cash one.",
    "An assisted value (key,trigger,value,quote) overrides the parser: the quote must be verbatim in the memo and "
    "the value a number of it (the rebuild's discipline).",
    "The new trigger stands only when the core numbers, where established, give EV/OI no-cash <= 7.1 or MCap/FCF "
    "<= 8.1 at it (a memo band on another basis than the core numbers passes on one leg); otherwise the row keeps "
    "all-cash and is listed.",
    "The memo wins: a figure in another currency than the quote unit is not converted; such a row is listed.",
)


def read_retrigger_assisted(text):
    """Rows of a retrigger assisted file: CSV key,field,value,quote with field
    'trigger' (a Markdown file is read from its first ```csv block)."""
    rows = read_assisted(text)
    for a in rows:
        if a["field"] != "trigger":
            raise ToolError("retrigger assisted file line %d: field %r (only trigger)" % (a["line"], a["field"]))
    return rows


def retrigger_accepts(row, value):
    """(ok, reading) of the core-number check at a candidate trigger."""
    at = compute_metrics(row, plain(value), row["px_unit"])
    mf, eo = at["mcap_fcf"], at["ev_oi"]
    reading = "MCap/FCF %s · EV/OI no-cash %s" % (mf, eo)
    if mf == OWED and eo == OWED:
        return True, "core numbers not established"
    ok = (MULT_RE.match(eo) and Decimal(eo) <= Decimal("7.1")) or (MULT_RE.match(mf) and Decimal(mf) <= Decimal("8.1"))
    return bool(ok), reading


def retrigger_rows(root, rows, assisted_rows=()):
    """Apply the retrigger rules to rows (lean-2 dicts, changed in place). Returns
    (resolved, unresolved, nm_rows, rejected): lists of dicts for the report."""
    by_key = {}
    rejected = []
    for a in assisted_rows:
        by_key.setdefault(a["key"], []).append(a)
    keys = {r["key"] for r in rows}
    for key in sorted(by_key):
        if key not in keys:
            rejected += ["line %d: %s is not a register key" % (a["line"], key) for a in by_key[key]]
    resolved, unresolved, nm_rows = [], [], []
    for row in canonical(rows):
        if row["trigger_basis"] != "all-cash":
            continue
        key = row["key"]
        if row["trigger"] == NM:
            row["trigger_basis"] = "no-cash"
            nm_rows.append(key)
            continue
        if not is_num(row["trigger"]):
            continue
        old = dec(row["trigger"])
        value, how, quote = None, "", ""
        memo_text = read_repo_text(root, row["memo_path"])
        held_band = row["held"] == "true" and is_num(row["add_band"])
        for a in by_key.get(key, [])[:1]:
            if held_band:
                rejected.append("line %d: %s is held with an ADD band, which is its trigger (P21)" % (a["line"], key))
            elif not is_num(a["value"]) or decimals(a["value"]) > MAX_DECIMALS:
                rejected.append("line %d: %s trigger %r is not a plain number" % (a["line"], key, a["value"]))
            elif not a["quote"] or norm_text(a["quote"]) not in norm_text(memo_text):
                rejected.append("line %d: %s trigger quote not found in %s: %r" % (a["line"], key, row["memo_path"],
                                                                                   a["quote"][:60]))
            elif trace_value(a["value"], a["quote"]) is None:
                rejected.append("line %d: %s trigger %s is not a number of its quote" % (a["line"], key, a["value"]))
            else:
                value, how, quote = dec(a["value"]), "assisted", a["quote"]
        for a in by_key.get(key, [])[1:]:
            rejected.append("line %d: %s trigger given twice; the first stands" % (a["line"], key))
        if held_band:
            value, how = dec(row["add_band"]), "held: the ADD band (P21)"
            if value > old:
                unresolved.append({"key": key, "row": row, "reason": "ADD band %s above the trigger %s"
                                   % (row["add_band"], row["trigger"])})
                continue
        if value is None:
            fm = parse_front_matter(memo_text)
            band = fm.get("trigger_band", "")
            figure, unit, why = no_cash_figure(band, key, None, row["px_unit"])
            if figure is None:
                unresolved.append({"key": key, "row": row, "reason": why, "band": band})
                continue
            if figure == NM:
                row["trigger"], row["trigger_basis"] = NM, "no-cash"
                resolved.append({"key": key, "row": row, "old": plain(old), "new": NM, "how": why,
                                 "reading": "no positive price"})
                continue
            converted, _conv = to_quote_unit(figure, unit, row["px_unit"]) if unit else (None, None)
            if converted is None:
                unresolved.append({"key": key, "row": row, "band": band, "reason": "the no-cash figure %s %s is not in "
                                   "the quote unit %s" % (plain(figure), unit or "(no unit)", row["px_unit"])})
                continue
            value, how, quote = converted, why, band
        new = min(old, value)
        ok, reading = retrigger_accepts(row, new)
        if not ok:
            unresolved.append({"key": key, "row": row, "band": quote, "reason": "rejected by the core numbers at %s "
                               "(%s; %s)" % (plain(new), reading, how)})
            continue
        row["trigger"] = row["trigger"] if new == old else plain(new)
        row["trigger_basis"] = "no-cash"
        resolved.append({"key": key, "row": row, "old": plain(old), "new": row["trigger"], "how": how,
                         "reading": reading})
    rejected.sort(key=lambda text: int(re.match(r"line (\d+)", text).group(1)))
    return resolved, unresolved, nm_rows, rejected


def retrigger_block(unresolved, rows, version, date):
    """The TODO head block for the rows the pass could not resolve."""
    scope = [u for u in unresolved if u["row"]["held"] == "true" or u["row"]["section"] in ("BUY", "WATCH", "AVOID-1")]
    lines = ["## ▶ Backfill owed — retrigger %s (%s)" % (version, date), "",
             "*Rows whose trigger is still the pre-R10 all-cash reading (register.csv trigger_basis all-cash): the "
             "memo prints no no-cash bound the tool can read (MODEL §7.1 operative trigger, R10). The next REVIEW "
             "memo sets it, or an attended `retrigger --assisted` pass with a verbatim memo quote. Held, BUY, WATCH "
             "and one-gate AVOID keys, one line each; SWEEP's strict status (IN RANGE needs EV/OI no-cash ≤ 7 at "
             "Px, and MCap/FCF ≤ 8 where `core_fcf_basis` is a P20 maintenance-capex tag; a pre-R6 FCF breach is "
             "not established, MODEL §8.3 step 3) covers them meanwhile.*", ""]
    for u in scope:
        lines.append("- `%s` — trigger %s (all-cash): %s — fill at next REVIEW or attended pass"
                     % (u["key"], u["row"]["trigger"], u["reason"]))
    if not scope:
        lines.append("None.")
    others = len(unresolved) - len(scope)
    lines.append("- AVOID two-or-more-gate and DNAF rows: %d keys still at all-cash, never priced — set by each "
                 "name's next REVIEW memo; list in the RETRIGGER report." % others)
    return "\n".join(lines) + "\n"


def retrigger_report(resolved, unresolved, nm_rows, rejected, assisted_rows, rows, old_version, version, date,
                     block):
    n_all = len(resolved) + len(unresolved)
    lowered = [r for r in resolved if r["new"] != r["old"] and is_num(r["new"])]
    by_how = {}
    for r in resolved:
        kind = "assisted" if r["how"] == "assisted" else ("held ADD band" if r["how"].startswith("held") else "memo")
        by_how[kind] = by_how.get(kind, 0) + 1
    falls = sorted(Decimal(r["new"]) / Decimal(r["old"]) - 1 for r in lowered)
    median = falls[len(falls) // 2] if falls else Decimal(0)
    out = [
        "# Trigger re-read (R10) — register %s → %s (%s)" % (old_version, version, date),
        "",
        "One-time attended pass of MODEL v4.5.0 round 2 (R10: the operative trigger is the no-cash bound, the strict "
        "all-pass line), written by `gsc_register.py retrigger`. Rows come from each current memo (memo wins); the "
        "register version %s is rendered after it." % version,
        "",
        "## Rules",
        "",
    ]
    out += ["%d. %s" % (i + 1, rule) for i, rule in enumerate(RETRIGGER_RULES)]
    out += [
        "",
        "## Counts",
        "",
        "| Measure | Value |",
        "|---|---|",
        "| Rows | %d |" % len(rows),
        "| Rows with a numeric all-cash trigger | %d |" % n_all,
        "| Resolved | %d (memo %d · held ADD band %d · assisted %d) |" % (
            len(resolved), by_how.get("memo", 0), by_how.get("held ADD band", 0), by_how.get("assisted", 0)),
        "| Resolved with a lower trigger | %d (median change %s) |" % (len(lowered), fmt_pct(median)),
        "| Resolved at the same figure | %d |" % (len(resolved) - len(lowered)),
        "| Unresolved: kept all-cash, listed | %d |" % len(unresolved),
        "| n.m. trigger, set to no-cash | %d |" % len(nm_rows),
        "| Rows with trigger_basis no-cash after the pass | %d |" % sum(1 for r in rows if r["trigger_basis"] == "no-cash"),
        "",
        "## Resolved (%d)" % len(resolved),
        "",
        "| Key | Section | Old | New | Change | Read | At the new trigger |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in resolved:
        change = ("same" if r["new"] == r["old"] else "no price" if not is_num(r["new"])
                  else fmt_pct(Decimal(r["new"]) / Decimal(r["old"]) - 1))
        out.append(table_line([r["key"], r["row"]["section"] + (" · held" if r["row"]["held"] == "true" else ""),
                               r["old"], r["new"], change, r["how"], r["reading"]]))
    out += ["", "## Unresolved — kept all-cash (%d)" % len(unresolved), "",
            "| Key | Section | Trigger | Reason | trigger_band |", "|---|---|---|---|---|"]
    for u in unresolved:
        out.append(table_line([u["key"], u["row"]["section"] + (" · held" if u["row"]["held"] == "true" else ""),
                               u["row"]["trigger"], u["reason"], norm_text(u.get("band", ""))[:160]]))
    out += ["", "## n.m. triggers set to no-cash (%d)" % len(nm_rows), "",
            ", ".join(nm_rows) if nm_rows else "None.", "",
            "## Assisted rows rejected (%d)" % len(rejected), ""]
    out += ["- %s" % cell_text(p) for p in rejected] if rejected else ["None."]
    out += ["", "## Backfill block (for queue/TODO.md)", "", "```markdown", block.rstrip("\n"), "```", "",
            "## Appendix — assisted file (verbatim)", "", "```csv", assisted_text(assisted_rows).rstrip("\n"), "```", ""]
    return "\n".join(out)


def retrigger(root, date, version=None, assisted_path=None):
    """The one-time R10 pass: (rows, report text, block text, report path).
    register.csv is read in its current or an older header and returned in
    lean-2 form; the caller writes it."""
    if not DATE_RE.match(date or ""):
        raise ToolError("--date must be YYYY-MM-DD (got %r)" % (date,))
    try:
        with open(os.path.join(root, CSV_FILE), "rb") as fh:
            text = fh.read().decode("utf-8")
    except (OSError, UnicodeDecodeError):
        raise ToolError("%s not found or not UTF-8 under %s" % (CSV_FILE, root))
    rows, problems = read_csv_text(text, legacy_ok=True)
    if problems:
        raise ToolError("; ".join(problems))
    fm, _md = register_front_matter(root)
    old_version = fm.get("register_version", "")
    if not VER_RE.match(old_version):
        raise ToolError("_REGISTER.md register_version %r is not vN" % old_version)
    version = version or "v%d" % (int(old_version[1:]) + 1)
    if not VER_RE.match(version):
        raise ToolError("--version must be vN (got %r)" % (version,))
    assisted_rows = []
    if assisted_path:
        with open(assisted_path, "rb") as fh:
            assisted_rows = read_retrigger_assisted(fh.read().decode("utf-8"))
    resolved, unresolved, nm_rows, rejected = retrigger_rows(root, rows, assisted_rows)
    errors = []
    for row in rows:
        errors += ["%s: %s" % (row["key"], e) for e in validate_row(row)]
    if errors:
        raise ToolError("the retrigger yields invalid rows:\n  " + "\n  ".join(errors))
    block = retrigger_block(unresolved, rows, version, date)
    report = retrigger_report(resolved, unresolved, nm_rows, rejected, assisted_rows, rows, old_version, version,
                              date, block)
    path = os.path.join(root, "archive", "registers", date[:4],
                        "RETRIGGER_%s-to-%s_%s.md" % (old_version, version, date))
    return rows, report, block, path


# ------------------------------------------------------------------ CLI

def default_root():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(here))


def cmd_render(args):
    rows, problems = load_csv(args.root)
    if problems:
        raise ToolError("; ".join(problems))
    text = render(rows, args.version, args.date)
    write_text(args.out or os.path.join(args.root, REGISTER_FILE), text)
    print("rendered %s %s: %d rows" % (args.version, args.date, len(rows)))
    return 0


def cmd_row_from_memo(args):
    notes = []
    row = row_from_memo(args.memo.replace("\\", "/"), read_repo_text(args.root, args.memo.replace("\\", "/")), notes)
    if args.table:
        print(table_line(MASTER_COLUMNS))
        print("|" + "---|" * len(MASTER_COLUMNS))
        print(table_line(master_cells(row)))
        if row["held"] == "true":
            print()
            print(table_line(PORTFOLIO_COLUMNS))
            print("|" + "---|" * len(PORTFOLIO_COLUMNS))
            print(table_line(portfolio_cells(row)))
    else:
        buf = io.StringIO(newline="")
        writer = csv.writer(buf, lineterminator="\n")
        writer.writerow(CSV_HEADER)
        writer.writerow([row[n] for n in CSV_HEADER])
        sys.stdout.write(buf.getvalue())
    for note in notes:
        sys.stderr.write(note + "\n")
    return 0


def cmd_apply(args):
    if bool(args.row) == bool(args.memo):
        raise ToolError("apply takes exactly one of --row ROWFILE or --memo MEMO")
    if args.row:
        report = apply_row(args.root, args.row.replace("\\", "/"))
    else:
        report = apply_memo(args.root, args.memo.replace("\\", "/"))
    print(json.dumps(report, ensure_ascii=False, indent=1))
    return 0


def cmd_position(args):
    report = set_position(args.root, args.key, args.held == "true", args.avg_cost)
    print(json.dumps(report, ensure_ascii=False, indent=1))
    return 0


def cmd_rekey(args):
    print(json.dumps(rekey(args.root, args.old, args.new), ensure_ascii=False, indent=1))
    return 0


def cmd_metrics(args):
    rows, _problems = load_csv(args.root)
    row = {r["key"]: r for r in rows}.get(args.key)
    if row is None:
        raise ToolError("%s is not in register.csv" % args.key)
    if not is_num(args.px):
        raise ToolError("PX must be a plain number in px_unit %s" % row["px_unit"])
    out = compute_metrics(row, args.px, row["px_unit"], args.fx)
    avg = compute_avg_metrics(row, args.px, row["px_unit"], args.fx)
    print("%s at %s %s: MCap/FCF %s · EV/OI no-cash %s · EV/OI all-cash %s"
          % (args.key, args.px, row["px_unit"], out["mcap_fcf"], out["ev_oi"], out["ev_oi_all_cash"]))
    print("  3y: MCap/FCF %s · EV/OI %s · 5y: MCap/FCF %s · EV/OI %s"
          % (avg["mcap_fcf_3y"], avg["ev_oi_3y"], avg["mcap_fcf_5y"], avg["ev_oi_5y"]))
    status, dist = status_hint(row, args.px, args.fx)
    notes = []
    fails = strict_failures(row, args.px, args.fx)
    if status == "NEAR" and dist is not None and dist <= 0 and fails:
        notes.append("strict line fails at PX: %s (MODEL 8.3)" % ", ".join(fails))
    if dist is not None and dist <= 0 and not fcf_leg_established(row) and mcap_fcf_breach(out["mcap_fcf"]):
        notes.append("MCap/FCF %s on a pre-R6 FCF basis, not tested (MODEL 8.3, R6)" % out["mcap_fcf"])
    if row["trigger_basis"] == "all-cash" and is_num(row["trigger"]):
        notes.append("an older all-cash trigger, re-read at the next memo (R10)")
    print("  trigger %s · distance %s · status_hint %s%s"
          % (row["trigger"], fmt_pct(dist) if dist is not None else NM, status,
             (" (%s)" % "; ".join(notes)) if notes else ""))
    if row["held"] == "true":
        px = dec(args.px)
        if row["trigger_basis"] == "no-cash":
            print("  held: trigger = ADD band (P21, R10)")
        # One sign convention for every distance metrics prints: Px / line - 1, as the trigger's.
        for label, name in (("ADD band", "add_band"), ("sell line", "sell_line")):
            line = row[name]
            print("  distance to %s %s: %s" % (label, line, fmt_pct(px / dec(line) - 1)
                                               if is_num(line) and dec(line) > 0 else line))
    return 0


def cmd_sweep_scope(args):
    rows, _problems = load_csv(args.root)
    out = io.StringIO(newline="")
    writer = csv.writer(out, lineterminator="\n")
    writer.writerow(["key", "endpoint_symbol", "px_unit", "section", "held", "px", "px_date", "trigger",
                     "core_currency", "holding_keys"])
    for row in canonical(rows):
        if row["held"] == "true" or row["section"] in ("BUY", "WATCH", "AVOID-1"):
            writer.writerow([row["key"], endpoint_symbol(row["key"]), row["px_unit"], row["section"],
                             row["held"], row["px"], row["px_date"], row["trigger"], row["core_currency"],
                             row["holding_keys"]])
    sys.stdout.write(out.getvalue())
    return 0


def cmd_check(args):
    breaches, listed, counts = check(args.root, args.base, args.tree)
    print("register check: " + " · ".join("%s %s" % (k, v) for k, v in counts.items()))
    for line in listed:
        print("LIST    " + line)
    for line in breaches:
        print("BREACH  " + line)
    print("%d breach(es), %d listed finding(s)" % (len(breaches), len(listed)))
    return 1 if breaches else 0


def cmd_rebuild(args):
    csv_out, md_out, report, backfill, rows = rebuild(args.root, args.base, args.assisted, args.version, args.date)
    os.makedirs(args.out, exist_ok=True)
    fm = parse_front_matter(md_out)
    old = legacy_register(batch_show(args.root, args.base, [REGISTER_FILE])[REGISTER_FILE])[2]
    name = "REBUILD_lean_%s-to-%s_%s.md" % (old.get("register_version"), fm["register_version"], fm["register_date"])
    for fname, text in ((CSV_FILE, csv_out), (REGISTER_FILE, md_out), (name, report), ("backfill_block.md", backfill)):
        write_text(os.path.join(args.out, fname), text)
    print("rebuilt %s %s: %d rows -> %s (%s, %s, %s, backfill_block.md)" % (
        fm["register_version"], fm["register_date"], len(rows), args.out, CSV_FILE, REGISTER_FILE, name))
    return 0


def cmd_retrigger(args):
    rows, report, block, path = retrigger(args.root, args.date, args.version, args.assisted)
    if os.path.exists(path):
        raise ToolError("%s exists: the archive is append-only (the pass ran for this version)" % path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    write_text(os.path.join(args.root, CSV_FILE), csv_text(rows))
    write_text(path, report)
    if args.block:
        write_text(args.block, block)
    counts = [line for line in report.split("\n") if line.startswith("| Resolved |") or line.startswith("| Unresolved")]
    print("retrigger: %s; register.csv written (%s); report %s%s" % (
        " · ".join(c.strip("| ").replace(" | ", " ") for c in counts), REGISTER_FORMAT,
        os.path.relpath(path, args.root).replace("\\", "/"), "; block %s" % args.block if args.block else ""))
    return 0


def cmd_lint_memo(args):
    rel = args.memo.replace("\\", "/")
    fails, warns = lint_memo(rel, read_repo_text(args.root, rel))
    for w in warns:
        print("WARN  " + w)
    for f in fails:
        print("FAIL  " + f)
    print("lint-memo %s: %s" % (rel, "FAIL (%d)" % len(fails) if fails else "OK"))
    return 1 if fails else 0


def cmd_lint_row(args):
    rel = args.row.replace("\\", "/")

    def read_memo(path):
        try:
            return read_repo_text(args.root, path)
        except ToolError:
            return None
    fails = lint_row(rel, read_repo_text(args.root, rel), read_memo)
    for f in fails:
        print("FAIL  " + f)
    print("lint-row %s: %s" % (rel, "FAIL (%d)" % len(fails) if fails else "OK"))
    return 1 if fails else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="GSC register tool (MODEL v4.5.0, sections 7.1, 7.1b).")
    parser.add_argument("--root", default=None, help="repository root (default: the one holding this file)")
    sub = parser.add_subparsers(dest="cmd")
    p = sub.add_parser("render")
    p.add_argument("--version", required=True)
    p.add_argument("--date", required=True)
    p.add_argument("--out")
    p = sub.add_parser("row-from-memo")
    p.add_argument("memo")
    p.add_argument("--table", action="store_true")
    p = sub.add_parser("apply")
    p.add_argument("--row")
    p.add_argument("--memo")
    p = sub.add_parser("position")
    p.add_argument("key")
    p.add_argument("--held", required=True, choices=("true", "false"))
    p.add_argument("--avg-cost", dest="avg_cost")
    p = sub.add_parser("rekey")
    p.add_argument("old")
    p.add_argument("new")
    p = sub.add_parser("metrics")
    p.add_argument("key")
    p.add_argument("px")
    p.add_argument("--fx")
    p.add_argument("--date", help="YYYY-MM-DD: the run date (accepted; round 2 retired the holding price check)")
    sub.add_parser("sweep-scope")
    p = sub.add_parser("check")
    p.add_argument("--base")
    p.add_argument("--tree", default="HEAD")
    p = sub.add_parser("lint-memo")
    p.add_argument("memo")
    p = sub.add_parser("lint-row")
    p.add_argument("row")
    p = sub.add_parser("rebuild")
    p.add_argument("--base", required=True)
    p.add_argument("--assisted")
    p.add_argument("--out", required=True)
    p.add_argument("--version")
    p.add_argument("--date")
    p = sub.add_parser("retrigger")
    p.add_argument("--date", required=True)
    p.add_argument("--version")
    p.add_argument("--assisted")
    p.add_argument("--block")
    args = parser.parse_args(argv)
    if not args.cmd:
        parser.print_help()
        return 2
    args.root = os.path.abspath(args.root or default_root())
    handler = {"render": cmd_render, "row-from-memo": cmd_row_from_memo, "apply": cmd_apply,
               "position": cmd_position, "rekey": cmd_rekey, "metrics": cmd_metrics,
               "sweep-scope": cmd_sweep_scope, "check": cmd_check, "lint-memo": cmd_lint_memo,
               "lint-row": cmd_lint_row,
               "rebuild": cmd_rebuild, "retrigger": cmd_retrigger}[args.cmd]
    try:
        return handler(args)
    except ToolError as exc:
        sys.stderr.write("gsc_register: %s\n" % exc)
        return 2


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    sys.exit(main())
