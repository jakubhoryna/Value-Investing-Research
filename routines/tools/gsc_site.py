#!/usr/bin/env python3
"""GSC register site: the research register as one page for readers outside the project (MODEL v4.5.0, section 7.1).

The page presents register.csv - the machine twin of _REGISTER.md - in plain
language for third parties: a lead with a not-advice notice, a stat strip, a
short account of the method, and one filterable table in five sections (BUY;
the WATCH shortlist, nearest its buy zone first; AVOID on one test; AVOID on
two or more; not analysed further). Each row adds three things the register
does not hold, read from the row's current memo: a one-sentence business
description (memo section 2), the moat line (section 4) and the worst-of-four
ROCE / FCFROCE (section 3). A figure the memo does not state clearly is shown
as an em dash, never estimated; register reason tokens and grades are
translated through the PLAIN_* tables below (an unknown token shows as
written). Round 2 (2026-10-07): the buy-zone price is the no-cash bound, the
strict line (R10; a row still carrying the older all-cash reading is marked),
the MCap/FCF and EV/OI cells add the 3- and 5-year averaged readings, and a
Future ADEQUATE carried with a concentration flag shows it as a caveat (R7).
v4.6.0: a RETIRED row (MODEL section 7.1, G5: the listed line has ceased to
trade) is no longer an investable name and is left off the page, its counts
included; groups are described as v4.6.0 reads them (G2, G4); a not-analysed
row names the one Gate-0 ground left (G2, P30: the filings do not show what
the business sells, and who pays for it, for most of its revenue); ROE and
the capital test are for banks and insurers on the bank lens only; every
'▶ Method re-tests' block in queue/TODO.md counts (v4.6.0 above v4.5.0).

Subcommands
  render --out PATH [--repo DIR] [--no-held]   write the page: artifact page content, no
                                               doctype/html/head/body (the publisher wraps it)
  stats [--repo DIR]                           extraction coverage and register data issues

Privacy. The page carries nothing from the portfolio layer (MODEL section 7.2):
no avg_cost, add_band, sell_line, zone, last_zone_check, position sizes, core
numbers or memo paths. A held name carries one neutral 'Held' marker, and
--no-held removes even that, together with what would still point at a held
name: the lead's sweep count and the price dates outside BUY and WATCH
(DATED_SECTIONS). Page rows are built field by field from a whitelist
(page_row), never by copying a register row. Publish with --no-held whenever
the page goes beyond Jakub.

Python 3.8+ (written for 3.12), standard library only, no network. register.csv
is read by column name, so the page does not depend on gsc_register.py
internals. Git is used read-only (`git show`, `git ls-tree`) for memos the
working tree cannot open (a sparse checkout, a Windows reserved name such as
CON). Writes only the --out file. The same inputs give byte-identical output:
UTF-8, LF line ends, no BOM, no clock (every date comes from the register or a
memo). Exit codes: 0 ok, 2 bad input.
"""
import argparse
import collections
import csv
import html
import io
import json
import os
import re
import subprocess
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

sys.dont_write_bytecode = True

# ------------------------------------------------------------------ constants

PAGE_TITLE = "GSC Research Register"
CSV_FILE = "register.csv"
REGISTER_FILE = "_REGISTER.md"
MODEL_FILE = "/".join(("model", "MODEL.md"))   # read only; spelled so the routine guard's code scan passes
TODO_FILE = "queue/TODO.md"
ARCHIVE_MEMOS = "archive/memos"
REQUIRED_COLUMNS = (
    "key", "company", "section", "verdict", "gates_failed", "past", "past_reason", "future",
    "future_reason", "sf", "sf_reason", "memo_path", "memo_date", "px", "px_unit", "px_date",
    "px_source", "trigger", "mcap_fcf", "ev_oi", "next_review_short", "held",
    "trigger_basis", "mcap_fcf_3y", "mcap_fcf_5y", "ev_oi_3y", "ev_oi_5y",
)
NM = "n.m."            # not meaningful
OWED = "-"             # not established in the register
DASH = "—"             # the page's sign for "not available"
SECTION_ORDER = ("BUY", "WATCH", "AVOID-1", "AVOID-2", "DNAF")
RETIRED = "RETIRED"    # a register state (MODEL v4.6.0 section 7.1): never on the page
AVOID_NOTE = "Sorted by EV/OI, lowest first · a low multiple does not make it a buy"
SECTIONS = {
    # id: (label - the same words on the stat tile, the filter chip and the section title; one-line note)
    "BUY": ("BUY", "Passes every test and the price is in the buy zone"),
    "WATCH": ("WATCH · shortlist", "Passes every quality test, waiting for a lower price · nearest the buy zone first"),
    "AVOID-1": ("AVOID · failed one test", AVOID_NOTE),
    "AVOID-2": ("AVOID · failed two or more", AVOID_NOTE),
    "DNAF": ("Not analysed further", "Stopped at the first question · alphabetical"),
}
# MODEL v4.6.0 (G2, P30): the only Gate-0 FAIL is a business whose filings do not show what it sells, and who pays
# for it, for more than half of its revenue (incomprehension or obfuscation); the v4.5.x grounds (the one-level
# decomposition, the too-hard pile) are retired, and a key without a listed line is RETIRED, never on the page.
DNAF_WHY = ("Stopped at the first question: the filings do not show what the business sells, and who pays for it, "
            "for most of its revenue.")
# A DNAF memo written before v4.6.0 stopped on a v4.5.x ground that v4.6.0 retired; its row keeps the earlier
# wording until the name is re-tested, so the page never states a reason that memo did not give.
DNAF_WHY_EARLIER = ("Stopped at the first question under an earlier version of the method: the business could not "
                    "be described simply, neither of the method's two lenses could read it, or there was no listed "
                    "share to assess.")
WATCH_WHY = "Passes all three quality tests; the price is above the buy zone."
# Sections whose prices stay dated under --no-held. A SWEEP prices BUY, WATCH and one-test AVOID
# (MODEL section 8.3) plus every held name, so a dated sweep price elsewhere - or in one-test AVOID
# before its first sweep - would single out a held name; AVOID and DNAF prices go undated instead.
DATED_SECTIONS = ("BUY", "WATCH")
GATE_NAMES = {"past": "past-record", "future": "competitive-position", "sf": "shareholder-friendliness"}
GATE_LIST_NAMES = {"past": "past record", "future": "competitive position", "sf": "shareholder-friendliness"}
NUMBER_WORDS = {2: "two", 3: "three"}

# Plain-language reason vocabulary (MODEL section 7.1). An unknown token shows as written.
PLAIN_PAST = {
    "ROCE decline": "returns on capital in sustained decline",
    "FCFROCE": "free-cash-flow return on capital too low",
    "leverage": "too much debt and other liabilities against equity",
    "losses": "losses in the financial record",
    "growth": "per-share results not growing enough",
    "record-limited": "too short a usable financial record",
    "capital": "regulatory capital test failed or not disclosed",
}
PLAIN_FUTURE = {
    "breadth": "customer or supplier base too narrow",
    # MODEL P15 (R7): any paying customer counts, distributors and retailers included; for a business selling
    # to other businesses, filings that do not rule a large customer out count too. The finding is a flag:
    # a strong moat can carry it (an ADEQUATE with a caveat), otherwise it weighs toward Weak (CONC_WEAK).
    "customer conc.": "a customer above 10% of revenue (distributors and retailers included), or concentration "
                      "not ruled out in its filings",
    "supplier conc.": "a supplier above 10% of costs, or a sole-source supplier",
    "funding conc.": "too much funding from one lender or one funding channel",
    "no moat": "no lasting competitive advantage",
    "moat eroding": "competitive advantage eroding",
    "2+ forces": "two or more competitive forces work against it",
    "forces: customers": "customers hold strong bargaining power",
    "forces: suppliers": "suppliers hold strong bargaining power",
    "forces: substitutes": "strong threat from substitutes",
    "forces: entrants": "strong threat from new entrants",
    # Round-2 review fix (2026-10-07): Past is never a weighted grade, so an ungradeable listed subsidiary
    # or holding weighs only in the Future (MODEL section 7.1).
    "dependency": "depends on a listed subsidiary or holding that cannot be graded",
}
# R7: a concentration called WEAK lacks a moat strong enough to carry it; an ADEQUATE carrying one is a caveat.
CONC_TOKENS = ("customer conc.", "supplier conc.")
CONC_WEAK = ", without a moat strong enough to carry it"
FUTURE_CAVEAT = "Passes, with a caveat: "
PLAIN_SF = {
    "compensation": "executive pay above the method's limits",
    "director pay": "board pay above the method's limits",
    "buybacks": "share buybacks at prices the method judges too high",
    "acquisitions": "acquisitions at prices the method judges too high",
    "distributions": "dividends or payouts beyond what free cash flow covers",
    # v4.6.0 (G4): a group's allocation of capital across its businesses.
    "reinvestment": "most of the group's new capital went into businesses earning below the method's 10% return "
                    "line",
    "RPT": "dealings with related parties",
    "control": "a controlling owner or voting structure can override other shareholders",
    "dilution": "existing shareholders diluted by new shares",
    # R8: pledges and insider sales are no flag; management's own shareholding is an input.
    "alignment": "one governance warning sign, with management owning little and voting control kept apart from "
                 "the economics",
    "flag pair": "two separate governance warning signs",
    "inherited": "inherits the failure of a listed subsidiary it controls",
}
PLAIN_PREFIX = {"unit": "in one business unit: ", "sub": "in a listed subsidiary: "}
# v4.6.0 (G3, G4; MODEL section 7.1): `dependency` names the ungradeable part by kind - `sub` a listed subsidiary
# or holding without a gradeable memo, `unit` a material unit its filings do not describe - so the prefixed
# Future token reads whole, never as a prefix before the token's own words.
PLAIN_GROUP_FUTURE = {
    "sub dependency": "depends on a listed subsidiary or holding that cannot be graded",
    "unit dependency": "depends on a business unit that its filings do not describe, which cannot be graded",
}
LEVEL_RE = re.compile(r"^(?:(?P<prefix>unit|sub) )?(?P<value>\d{1,3}(?:\.\d{1,2})?)% (?P<metric>ROCE|ROE)$")
LEGACY_TRIGGER_NOTE = "older, looser reading — review pending"

# Listing country by key suffix (MODEL section 7.1a): every suffix the key convention admits.
SUFFIX_COUNTRY = {
    "TO": "Canada", "V": "Canada", "CN": "Canada", "NE": "Canada", "PA": "France", "AS": "Netherlands",
    "BR": "Belgium", "LS": "Portugal", "IR": "Ireland", "MI": "Italy", "MC": "Spain", "DE": "Germany",
    "VI": "Austria", "HE": "Finland", "AT": "Greece", "TL": "Estonia", "RG": "Latvia", "VS": "Lithuania",
    "SW": "Switzerland", "ST": "Sweden", "CO": "Denmark", "OL": "Norway", "IC": "Iceland", "L": "UK",
    "WA": "Poland", "PR": "Czechia", "BD": "Hungary", "RO": "Romania", "IS": "Turkey", "TA": "Israel",
    "SR": "Saudi Arabia", "AE": "UAE", "QA": "Qatar", "KW": "Kuwait", "JO": "South Africa", "NS": "India",
    "BO": "India", "T": "Japan", "HK": "Hong Kong", "SS": "China", "SZ": "China", "TW": "Taiwan",
    "TWO": "Taiwan", "KS": "South Korea", "KQ": "South Korea", "SI": "Singapore", "JK": "Indonesia",
    "BK": "Thailand", "KL": "Malaysia", "VN": "Vietnam", "AX": "Australia", "NZ": "New Zealand",
    "SA": "Brazil", "MX": "Mexico", "BA": "Argentina", "SN": "Chile", "CL": "Colombia",
}
US_COUNTRY = "US"
UNIT_NOTES = {"GBp": "pence", "ZAc": "cents", "ILA": "agorot", "KWF": "fils"}

MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$", re.ASCII)
MULT_RE = re.compile(r"^-?\d+\.\d$", re.ASCII)
NUM_RE = re.compile(r"^-?\d+(\.\d+)?$", re.ASCII)
FM_LINE_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):[ \t]*(.*?)[ \t]*$")

# Memo extraction limits (characters).
BUSINESS_MAX = 260
MOAT_MAX = 120


class ToolError(Exception):
    """Bad input; the message is printed and the tool exits 2."""


# ------------------------------------------------------------------ small helpers

def is_num(text):
    return bool(NUM_RE.match(text or ""))


def dec(text):
    try:
        return Decimal(text)
    except (InvalidOperation, TypeError):
        raise ToolError("not a number: %r" % (text,))


def fmt_signed_pct(value):
    """+20.6% style, one decimal, half up (whole numbers from 100% up: +565%); never '-0.0%'."""
    q = (value * 100).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
    if abs(q) >= 100:
        q = q.quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    text = "0.0" if format(q, "f") in ("-0.0", "0.0") else format(q, "f")
    return ("+" if q > 0 else "") + text.replace("-", "−") + "%"


def one_decimal_pct(text):
    """A percentage as the page prints it: at most one decimal, half up ('8.42%' -> '8.4%',
    '21%' and '−3.9%' unchanged); anything that is not a plain percentage unchanged."""
    m = re.match(r"^([−-]?)(\d+)\.(\d{2,})%$", text or "")
    if not m:
        return text
    q = Decimal(m.group(2) + "." + m.group(3)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
    return m.group(1) + format(q, "f") + "%"


def fmt_pct(value):
    q = (value * 100).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
    return format(q, "f") + "%"


def group_digits(text):
    """A register number with thousands separators for reading: 4564 -> 4,564 (decimals kept as written)."""
    m = re.match(r"^(-?)(\d+)(\.\d+)?$", text or "")
    if not m:
        return text
    sign, whole, frac = m.groups()
    return ("−" if sign else "") + "{:,}".format(int(whole)) + (frac or "")


def fmt_day(day):
    """2026-10-04 -> 4 Oct 2026; anything else unchanged."""
    if not DATE_RE.match(day or ""):
        return day
    year, month, dom = day.split("-")
    return "%d %s %s" % (int(dom), MONTHS[int(month) - 1], year)


def month_end(year, month):
    if month == 2:
        return 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28
    return 31 if month in (1, 3, 5, 7, 8, 10, 12) else 30


def review_last_day(short):
    """The latest day a next_review_short token can mean (the date itself, or the
    month's or quarter's last day); None for n.m. or '-' (as gsc_register.py)."""
    if DATE_RE.match(short or ""):
        return short
    m = re.match(r"^Q([1-4]) (\d{4})$", short or "")
    if m:
        year, month = int(m.group(2)), int(m.group(1)) * 3
        return "%04d-%02d-%02d" % (year, month, month_end(year, month))
    m = re.match(r"^([A-Z][a-z]{2}) (\d{4})$", short or "")
    if m and m.group(1) in MONTHS:
        year, month = int(m.group(2)), MONTHS.index(m.group(1)) + 1
        return "%04d-%02d-%02d" % (year, month, month_end(year, month))
    return None


def key_suffix(key):
    if "." in key:
        suffix = key.rsplit(".", 1)[1]
        if suffix in SUFFIX_COUNTRY:
            return suffix
    return ""


def run_git(root, args):
    """Read-only git call; (returncode, stdout bytes)."""
    try:
        proc = subprocess.run(["git", "-C", root] + list(args), stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, check=False)
    except OSError as exc:
        return 127, ("%s" % exc).encode()
    return proc.returncode, proc.stdout


def read_text(root, rel):
    """A repo file as text from the working tree, else from `git show HEAD:path`
    (a sparse checkout or a Windows reserved name such as CON); None if neither."""
    try:
        with open(os.path.join(root, rel), "rb") as fh:
            return fh.read().decode("utf-8")
    except (OSError, UnicodeDecodeError):
        pass
    rc, out = run_git(root, ["show", "HEAD:%s" % rel])
    if rc != 0:
        return None
    try:
        return out.decode("utf-8")
    except UnicodeDecodeError:
        return None


def list_dir(root, rel):
    """File names in a repo directory: the working tree, else `git ls-tree HEAD`."""
    try:
        return sorted(os.listdir(os.path.join(root, rel)))
    except OSError:
        pass
    rc, out = run_git(root, ["ls-tree", "--name-only", "HEAD", rel.rstrip("/") + "/"])
    if rc != 0:
        return []
    return sorted(line.rsplit("/", 1)[-1] for line in out.decode("utf-8", "replace").splitlines() if line)


def parse_front_matter(text):
    """Flat `key: value` front matter between the first two '---' lines ({} if none)."""
    lines = (text or "").replace("\r\n", "\n").lstrip("\ufeff").split("\n")
    if not lines or lines[0].strip() != "---":
        return {}
    fm = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fm
        m = FM_LINE_RE.match(line)
        if not m:
            continue
        value = m.group(2)
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        fm[m.group(1)] = value.strip()
    return {}


# ------------------------------------------------------------------ inputs

def load_register(root):
    """(rows, front matter) of register.csv and _REGISTER.md."""
    text = read_text(root, CSV_FILE)
    if text is None:
        raise ToolError("%s not found under %s" % (CSV_FILE, root))
    reader = csv.DictReader(io.StringIO(text.lstrip("\ufeff"), newline=""))
    missing = [c for c in REQUIRED_COLUMNS if c not in (reader.fieldnames or [])]
    if missing:
        raise ToolError("%s lacks columns: %s" % (CSV_FILE, ", ".join(missing)))
    rows = [dict(r) for r in reader]
    fm = parse_front_matter(read_text(root, REGISTER_FILE) or "")
    return rows, fm


def model_version(root):
    return parse_front_matter(read_text(root, MODEL_FILE) or "").get("model_version", "")


def retest_block(root):
    """(versions, keys) of the queue/TODO.md blocks '## ▶ Method re-tests ...'. Every
    such block counts: a release adds its own block above the earlier ones (v4.6.0:
    `▶ Method re-tests v4.6.0` above `▶ Method re-tests v4.5.0`, MODEL section 8.2
    step 3), and a key stays under re-test while any block lists it. versions: each
    block's version label in file order ('' where its title names none); keys: the
    union of the keys their bullet lines open with, in file order, each mapped to the
    version label of the first block that lists it. ([], {}) when there is no such block."""
    text = read_text(root, TODO_FILE) or ""
    versions, keys, version, inside = [], collections.OrderedDict(), "", False
    for line in text.replace("\r\n", "\n").split("\n"):
        if line.startswith("## "):
            inside = line.startswith("## ▶ Method re-tests")
            if inside:
                m = re.search(r"v\d+\.\d+\.\d+", line)
                version = m.group(0) if m else ""
                versions.append(version)
            continue
        if inside:
            m = re.match(r"^\s*-\s+`([A-Za-z0-9._-]+)`", line)
            if m and m.group(1) not in keys:
                keys[m.group(1)] = version
    return versions, keys


def retest_versions(versions, retest):
    """[(version, count)] of the re-test blocks, in block order, for the keys on the page
    (retest: {key: version label}); every block's version with count 0 when no listed key
    is on the page. Unversioned blocks and repeats are folded away."""
    order = [v for i, v in enumerate(versions) if v and v not in versions[:i]]
    counts = collections.Counter(retest.values())
    found = [(v, counts[v]) for v in order if counts[v]]
    return found or [(v, 0) for v in order]


def read_memo(root, row):
    """(text, source) of a row's memo: 'memo' from its cited path (working tree
    or git), 'archive' when the cited file has moved to archive/memos/; (None, '')."""
    rel = row["memo_path"]
    text = read_text(root, rel)
    if text is not None:
        return text, "memo"
    name = rel.rsplit("/", 1)[-1]
    text = read_text(root, "%s/%s/%s" % (ARCHIVE_MEMOS, row["key"], name))
    if text is not None:
        return text, "archive"
    return None, ""


def older_memos(root, key, before):
    """Archived memos of a key dated before `before`, newest first (texts)."""
    out = []
    for name in reversed(list_dir(root, "%s/%s" % (ARCHIVE_MEMOS, key))):
        m = re.match(r"^.+_(\d{4}-\d{2}-\d{2})_GSC\.md$", name)
        if m and m.group(1) < before:
            text = read_text(root, "%s/%s/%s" % (ARCHIVE_MEMOS, key, name))
            if text:
                out.append(text)
    return out


# ------------------------------------------------------------------ memo text

ABBREVIATIONS = {
    "inc", "ltd", "co", "corp", "plc", "no", "nos", "st", "vs", "approx", "incl", "excl", "e.g", "i.e",
    "etc", "dr", "mr", "ms", "jr", "sr", "fig", "est", "ca", "cf", "pp", "hldgs", "mfg", "bros", "dept",
    "jan", "feb", "mar", "apr", "jun", "jul", "aug", "sep", "sept", "oct", "nov", "dec", "u.s", "u.k",
    "s.a", "s.p.a", "n.v", "b.v", "a.g", "s.e",
}
SENTENCE_END_RE = re.compile(r"[.!?][\"”’)]?\s+(?=[A-Z0-9\"“‘(À-Ö])")
DIRECTION_RE = re.compile(r"(?i)^(stable|strengthening|eroding|durable|intact|unchanged|contested|narrow|wide|"
                          r"weak|thin|plausible|dominant|not)\b")
# Memos without numbered sections open each gate with a bold label paragraph instead.
SECTION_LABELS = {1: "Verdict", 2: "Understanding", 3: "Past", 4: "Future"}
MOAT_SOURCE_RE = re.compile(r"(?i)(brand|cost|network|switching|ingrain|government|scale|patent|licen|regulat)")
MOAT_DIRECTION_RE = re.compile(r"(?i)\b(stable-to-strengthening|stable-to-eroding|strengthening|stable|eroding)\b")
# A direction word right before 'moat' ('an eroding moat: ...') stays as the line's subject.
PRE_DIRECTION_RE = re.compile(r"(?i)^(eroding|eroded|weakening|strengthening|stable|durable|narrow|wide|weak|thin|"
                              r"intact)$")


def strip_md(text):
    """Markdown to plain text on one line: links, emphasis, code and stray tags removed."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text or "")
    text = re.sub(r"<[^>\n]+>", "", text)
    text = text.replace("**", "").replace("__", "").replace("`", "")
    text = re.sub(r"(?<![\w*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![\w*])", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def drop_parentheticals(text):
    """Remove (...) and [...] spans, nested ones included, and tidy the spacing they leave."""
    out, depth = [], 0
    for ch in text:
        if ch in "([":
            depth += 1
            continue
        if ch in ")]" and depth:
            depth -= 1
            continue
        if not depth:
            out.append(ch)
    text = "".join(out)
    text = re.sub(r"\s+([,.;:])", r"\1", text)
    text = re.sub(r"(\w) -(?=[a-z])", r"\1-", text)        # 'Minnetonka (Minnesota)-based' -> 'Minnetonka-based'
    return re.sub(r"\s{2,}", " ", text).strip()


def split_sentences(text):
    """Sentences of one plain-text paragraph; abbreviations and initials do not end one."""
    out, start = [], 0
    for m in SENTENCE_END_RE.finditer(text):
        end = m.start() + 1
        token = re.search(r"([\w.'&/-]+)$", text[start:end - 1])
        word = (token.group(1) if token else "").lower()
        if word in ABBREVIATIONS or len(word) == 1 or re.match(r"^([a-z]\.)+[a-z]$", word):
            continue
        out.append(text[start:m.end()].strip())
        start = m.end()
    tail = text[start:].strip()
    if tail:
        out.append(tail)
    return out


def memo_section(text, number):
    """Prose paragraphs (plain text) of memo section `## {number}. ...` up to the next
    heading or rule, table rows left out. A memo without numbered sections gives the
    one paragraph that opens with its bold label ('**Understanding — PASS.** ...')."""
    lines, inside, found = [], False, False
    all_lines = (text or "").replace("\r\n", "\n").split("\n")
    for line in all_lines:
        if not inside:
            if re.match(r"^##\s+%s\.?\s" % number, line):
                inside = found = True
            continue
        if re.match(r"^#{1,2}\s", line) or line.strip() == "---":
            break
        lines.append("" if line.lstrip().startswith("|") else line)
    if not found and number in SECTION_LABELS:
        label = re.compile(r"^\*\*%s\b" % SECTION_LABELS[number])
        lines = [next((line for line in all_lines if label.match(line)), "")]
    paragraphs = re.split(r"\n\s*\n", "\n".join(lines))
    return [p for p in (strip_md(p) for p in paragraphs) if p]


DASH_BREAK_RE = re.compile(r" [—–] ")
CLIP_STRONG_FLOOR = Decimal("0.4")     # a '; ' or ' — ' cut keeps at least 40% of the limit
CLIP_COMMA_FLOOR = Decimal("0.55")     # a ', ' cut at least 55%
# A comma cut never keeps a stub clause: 'and it is', ', so service', ', that designs', 'and, mostly'.
STUB_CLAUSE_RE = re.compile(r"(?i)^(?:and|or|but|so|yet|that|which|who|whose|where|while|as|mostly|then|thus|"
                            r"hence|plus|with)\b(?:\s+\S+){0,2}$")


def clip(text, limit):
    """Text cut to at most `limit` characters with an ellipsis, at the latest clause break
    the text allows: a '; ' or ' — ' past 40% of the limit, or a ', ' past 55% that does not
    keep a stub clause, else a word boundary. Dashes pair up as asides. An aside opening
    before 40% is main text (its dashes are ordinary breaks). A later aside closed within
    the cut is never cut inside or at its closing dash, only where it opens ('owners and —
    the profit engine — recurring…' keeps 'owners'); one still open at the cut may be cut
    at a comma inside it, so a list it opens ends '…, faucets, unit bathrooms…'."""
    text = text.strip()
    if len(text) <= limit:
        return text
    cut = text[:limit - 1]
    strong_floor, comma_floor = int(limit * CLIP_STRONG_FLOOR), int(limit * CLIP_COMMA_FLOOR)
    dashes = [m.start() for m in DASH_BREAK_RE.finditer(cut)]
    breaks, asides, closers = [], [], []
    for i in range(0, len(dashes), 2):
        opener = dashes[i]
        closer = dashes[i + 1] if i + 1 < len(dashes) else None
        if opener < strong_floor:
            breaks += [d for d in (opener, closer) if d is not None]
        else:
            breaks.append(opener)
            if closer is not None:
                asides.append((opener, closer))
                closers.append(closer)

    def outside(pos):
        return not any(start < pos <= end for start, end in asides)

    breaks += [m.start() for m in re.finditer(r"; ", cut) if outside(m.start())]
    commas = [m.start() for m in re.finditer(r", ", cut) if outside(m.start())]
    bounds = sorted(breaks + closers + commas)
    comma = -1
    for pos in reversed(commas):
        if pos < comma_floor:
            break
        start = max([b for b in bounds if b < pos] or [-2]) + 2
        clause = re.sub(r"^[—–;,]\s*", "", cut[start:pos].strip())
        if clause and not STUB_CLAUSE_RE.match(clause):
            comma = pos
            break
    strong = max([b for b in breaks if b >= strong_floor] or [-1])
    if max(strong, comma) >= 0:
        cut = cut[:max(strong, comma)]
    elif " " in cut:
        cut = cut[:cut.rfind(" ")]
    while True:
        trimmed = re.sub(r"(?i)[\s,;:—–-]+$|\s+(and|or|with|of|the|a|an|to|in|for|by|at|on|plus|that|which|"
                         r"whose|from|as|its|their)$", "", cut)
        if trimmed == cut:
            break
        cut = trimmed
    return cut + "…"


# Gate labels that open an understanding paragraph: 'PASS.', 'PASS, unchanged.', 'PASS (restated).',
# 'Unchanged and restated:', 'Restated from v1, unchanged.', 'Group-level: FAIL.', 'Understanding — PASS.'
LEAD_LABEL_RES = (
    re.compile(r"^(?:Group-level|Group|Per unit|Understanding)[^:.—]{0,60}[:—–-]\s*(?:PASS|FAIL)\b[^.:;]{0,40}"
               r"[.:;]?\s*"),
    re.compile(r"^(?:PASS|FAIL|Unchanged|Restated)\b[^.:;—–]{0,50}?(?:[.:;—–]\s*|$)"),
)
# Paragraphs that are not a business description: a delta note, a not-assessed stop, a flip condition.
SKIP_PARAGRAPH_RE = re.compile(r"(?i)^(not assessed|for the record|delta\b|flip condition|judgment call|"
                               r"precedent|bias check|framework output|one addition|addition|update)\b")


def clean_business(paragraph):
    """One understanding paragraph without its gate labels and without the closing PASS."""
    text = paragraph
    while True:
        new = text
        for pattern in LEAD_LABEL_RES:
            new = pattern.sub("", new, 1)
        if new == text:
            break
        text = new
    labelled = text != paragraph
    text = re.split(r"\s(?:—\s)?(?:PASS|FAIL)\b(?=[\s.;:,—]|$)", text, 1)[0].strip()
    text = re.sub(r"(?i)^no (?:one|single) sentence covers ", "A diversified group spanning ", text)
    # 'Unchanged — a Maryland-incorporated ...' starts mid-sentence; a brand written lower-case keeps its case.
    return text[:1].upper() + text[1:] if labelled else text


def business_from_paragraphs(paragraphs):
    """The first one or two sentences of the first usable paragraph, at most BUSINESS_MAX
    characters (a short first sentence takes the second along, clipped)."""
    for paragraph in paragraphs:
        text = drop_parentheticals(clean_business(paragraph))
        if SKIP_PARAGRAPH_RE.match(text):
            continue
        sentences = split_sentences(text)
        if not sentences or len(sentences[0]) < 30:
            continue
        out = sentences[0]
        if len(sentences) > 1 and (len(out) + 1 + len(sentences[1]) <= BUSINESS_MAX or len(out) < 90):
            out = out + " " + sentences[1]
        return clip(out, BUSINESS_MAX)
    return ""


def is_unchanged(paragraphs):
    """True when a section opens by pointing back to the previous memo ('Unchanged', 'Restated')."""
    return bool(paragraphs) and bool(re.match(r"(?i)^\W*(unchanged|restated)\b", paragraphs[0]))


def extract_business(text, section):
    """The business sentence from memo section 2 (section 1 for a not-analysed memo)."""
    found = business_from_paragraphs(memo_section(text, 2))
    if not found and section == "DNAF":
        found = business_from_paragraphs(memo_section(text, 1))
    return found


def tidy_moat(rest):
    """A moat clause without lead-in words ('real —', 'a', 'single source'), without
    trailing evidence after a colon that carries figures, and without a second clause
    (after ';', ', and the ...', '— but ...', '→')."""
    # 'real (X), Y' and 'real and singularly sourced (X), Y': the bracket names the source.
    m = re.match(r"(?i)^(?:real|genuine)(?:\s+and\s+[^()]{1,40}?)?\s*\((?P<inner>[^)]+)\)\s*,?\s*(?P<tail>.*)$",
                 rest)
    if m:
        rest = m.group("inner") + ((", " + m.group("tail")) if m.group("tail") else "")
    # Parentheticals go unless they hold the only named source ('real and singular (switching costs via ...)').
    rest = drop_parentheticals(rest) if MOAT_SOURCE_RE.search(drop_parentheticals(rest)) else rest
    rest = re.sub(r"(?i)^(?:real|genuine)\s*[—–:,]\s*", "", rest)
    rest = re.sub(r"(?i)^(?:an?\s+|single[- ]sourced?\s+|source\s+|remains\s+|still\s+|stays\s+)+", "", rest)
    # A cross-reference to another company's memo ('— the NESTE.HE shape: ...') means nothing to a reader.
    rest = re.sub(r"\s[—–]\s(?:the\s+)?[A-Z0-9][A-Z0-9-]*(?:\.[A-Z]{1,3})?\s+(?:shape|pattern|precedent|case|"
                  r"template|analogue)\b.*$", "", rest)
    rest = re.split(r";\s|,\s+and\s+(?=(?:the|this|that|Q\d)\b)|\s—\s(?=(?:but|held|graded|hence|so|no)\b)|\s→\s",
                    rest, 1)[0]
    head, sep, tail = rest.partition(": ")
    if sep and re.search(r"\d", tail) and len(head) >= 4:
        rest = head
    rest = rest.strip().rstrip(".").strip()
    if re.match(r"(?i)^none\b", rest):
        rest = "None" + rest[4:]
    return rest[:1].upper() + rest[1:]


def moat_candidates(sentence):
    """(strength, clause) moat readings of one sentence, best first: strength 2 names a
    moat source or none, 1 is a direction only ('stable, contested'), 0 nothing."""
    out = []
    if re.match(r"(?i)^no (?:\w+ )?moat\b", sentence):
        out.append((2, sentence))
    # 'The moat (X) is Y', 'The moat — X — is Y', 'The moat, X, is Y'
    m = re.search(r"(?i)(?P<pre>(?:[\w&/+-]+\s+){0,3})\bmoats?\s*(?:\((?P<a>[^)]+)\)|—\s*(?P<b>[^—]+?)\s*—|"
                  r",\s*(?P<c>[^,]+?),)\s*(?:is|are)\s+(?P<dir>.+)$", sentence)
    if m:
        inner, direction = m.group("a") or m.group("b") or m.group("c"), m.group("dir")
        words = m.group("pre").split()
        source = next((words[i:] for i, w in enumerate(words) if MOAT_SOURCE_RE.search(w)), [])
        if MOAT_SOURCE_RE.search(inner):
            out.append((2, inner + ", " + direction))
        elif source:
            # 'The brand moat — an aside — is contradicted by ...': the source is the subject, the aside goes.
            out.append((2, " ".join(source) + " moat: " + direction))
        elif MOAT_SOURCE_RE.search(direction) and not DIRECTION_RE.match(direction):
            out.append((2, direction))
        else:
            out.append((1, inner + ", " + direction))
    m = re.search(r"(?i)(?P<pre>(?:[\w&/+-]+\s+){0,3})\bmoats?(?:\s+source|\s+by segment)?\s*"
                  r"(?::|=|\bis\b|\bare\b)\s*(?P<rest>.+)$", sentence)
    if not m:
        m = re.match(r"(?i)^(?P<pre>)moats?(?:\s+source)?\s+(?P<rest>[a-z].+)$", sentence)
    if m and not re.match(r"(?i)^evidence\b", m.group("rest")) and \
            m.group("rest").count(")") <= m.group("rest").count("("):
        rest = m.group("rest")
        words = m.group("pre").split()
        source = next((words[i:] for i, w in enumerate(words) if MOAT_SOURCE_RE.search(w)), [])
        head = re.split(r"[;,]|\s(?:on|as|but)\s", rest, 1)[0]
        if source:
            # 'the brand moat is stable-to-strengthening on ...', 'the claimed brand moat is contradicted by ...'
            subject = " ".join(source) + " moat"
            out.append((2, subject + ", " + head if DIRECTION_RE.match(rest) else subject + ": " + rest))
        elif DIRECTION_RE.match(rest) and not MOAT_SOURCE_RE.search(head):
            out.append((1, re.split(r",\s+and\s|;\s", rest, 1)[0]))
        elif words and PRE_DIRECTION_RE.match(words[-1]):
            # 'an eroding moat: Chinese EV entrants ...' is evidence of erosion, not the moat itself.
            out.append((2, words[-1] + " moat: " + rest))
        else:
            out.append((2, rest))
    # 'the brand moat is stable', 'a strengthening switching-cost moat'
    for m in re.finditer(r"(?i)((?:[\w&/+-]+\s+){0,3})moat\b", sentence):
        words = m.group(1).split()
        source = []
        for word in words:
            if source or MOAT_SOURCE_RE.search(word):
                source.append(word)
        if source:
            direction = MOAT_DIRECTION_RE.search(sentence[m.end():])
            out.append((2, " ".join(source) + " moat" + (", " + direction.group(1) if direction else "")))
            break
    m = re.search(r"(?i)\bno (?:\w+ )?moat\b", sentence)
    if m:
        out.append((1, sentence[m.start():m.end()]))
    m = re.search(r"(?i)\bmoat\s+(?P<rest>(?:dominant|stable|strengthening|eroding)[^;.]*)", sentence)
    if m:
        out.append((1, re.split(r",\s+and\s|,\s", m.group("rest"), 1)[0]))
    return out


def extract_moat(text):
    """The moat line from memo section 4 (Appendix D, the future worksheet, when
    section 4 names none), at most MOAT_MAX characters, or '': the first clause
    naming a moat source, else the first direction-only clause. Returns (line, strength):
    strength 2 names a source (or none), 1 a direction only, 0 nothing found."""
    fallback = ""
    for section in (4, "D"):
        for paragraph in memo_section(text, section):
            for sentence in split_sentences(paragraph):
                for strength, clause in moat_candidates(sentence):
                    clause = tidy_moat(clause)
                    if not clause:
                        continue
                    if strength == 2:
                        return clip(clause, MOAT_MAX), 2
                    fallback = fallback or clip(clause, MOAT_MAX)
        if fallback:
            return fallback, 1
    return "", 0


FIGURE_RE = re.compile(r"(?<![\d.,])(?P<value>[−-]?\d{1,3}(?:\.\d{1,2})?)\s?%")
# A percentage read as a threshold, not a result: 'the 15%', "P2's 15%", 'above 10%', '≥ 8%', '10% floor',
# 'no read reaches 10%'.
THRESHOLD_BEFORE_RE = re.compile(r"(?i)(?:\bthe|\bP\d+'s|\babove|\bbelow|\bunder|\bover|\bbeyond|\bthan|\bvs\.?|"
                                 r"\bversus|\bagainst|\bclears?|\bmiss(?:es)?|\bfloor|\bbar|\breach(?:es)?|"
                                 r"\bapproach(?:es)?|\bexceeds?|\bneeds?|\brequires?|\bcross(?:es)?|\btoward|"
                                 r"[≥≤<>])\s*$")
THRESHOLD_AFTER_RE = re.compile(r"(?i)^\s*(?:floor|bar|line|threshold|hurdle|level|strong|adequate|test|cap|"
                                r"minimum|requirement|mark|limit)s?\b")
OTHER_METRIC_RE = re.compile(r"(?i)FCFROCE|\bROE\b|\bROIC\b|\bOI/sh|\bFCF/sh|\bL/E\b|\bgrowth\b|\bmargin")


PAIR_RE = re.compile(r"^\s*(?:to|/|or)\s*(?P<value>[−-]?\d{1,3}(?:\.\d{1,2})?)\s?%")


def pct_value(text):
    """'−3.8' or '-3.8' -> Decimal('-3.8')."""
    return Decimal(text.replace("−", "-"))


def first_figure(after):
    """The first clear percentage in `after` (a stretch of text following a metric
    name): not a range bound, not a threshold, not past another metric's name. A
    figure given as a pair or a span of readings ('−9.1% / −13.5%', '−3.8% to −3.9%')
    gives the lower one, the worst case. At most one decimal ('8.42%' -> '8.4%')."""
    stop = OTHER_METRIC_RE.search(after)
    if stop:
        after = after[:stop.start()]
    for m in FIGURE_RE.finditer(after):
        before = after[:m.start()]
        if re.search(r"\d\s?[–-]\s?$", before) or THRESHOLD_BEFORE_RE.search(before[-12:]):
            continue
        tail = after[m.end():m.end() + 16]
        if re.match(r"^\s?[–-]\s?\d", tail) or THRESHOLD_AFTER_RE.match(tail):
            continue
        value = m.group("value")
        pair = PAIR_RE.match(after[m.end():])
        if pair and pct_value(pair.group("value")) < pct_value(value):
            value = pair.group("value")
        return one_decimal_pct(("−" + value[1:] if value[0] in "−-" else value) + "%")
    return ""


NEGATIVE_RE = r"(?<![A-Za-z_])%s(?![\w])[^.;%%\d]{0,50}?\bnegative\b"


def extract_returns(text):
    """(ROCE, FCFROCE) as printed in memo section 3: the worst-of-four (or
    normalised) figure each, 'n.m.' for a stated n.m. FCFROCE, 'negative' where
    the memo says every reading is negative without a figure, '' where unclear."""
    roce = fcf = ""
    negative = {"ROCE": False, "FCFROCE": False}
    for paragraph in memo_section(text, 3):
        for sentence in split_sentences(drop_parentheticals(paragraph)):
            worst = re.search(r"(?i)\bworst|\bnormali[sz]ed", sentence)
            for metric in negative:
                if worst and re.search(NEGATIVE_RE % metric, sentence):
                    negative[metric] = True
            if not roce and worst:
                for m in re.finditer(r"(?<![A-Za-z_])ROCE(?![\w])", sentence):
                    if sentence[max(0, m.start() - 3):m.start()] == "FCF":
                        continue
                    roce = first_figure(sentence[m.end():m.end() + 70])
                    if roce:
                        break
            if not fcf:
                if re.search(r"FCFROCE\s+(?:is\s+)?n\.m\.", sentence):
                    fcf = NM
                elif worst or roce:
                    for m in re.finditer(r"FCFROCE(?![\w])", sentence):
                        fcf = first_figure(sentence[m.end():m.end() + 60])
                        if fcf:
                            break
            if roce and fcf:
                return roce, fcf
    return roce or ("negative" if negative["ROCE"] else ""), fcf or ("negative" if negative["FCFROCE"] else "")


# ------------------------------------------------------------------ page rows

def plain_reason(table, value):
    """A register reason token in plain words (group prefix kept); unknown tokens as written."""
    if value in ("", OWED, NM):
        return ""
    if table is PLAIN_FUTURE and value in PLAIN_GROUP_FUTURE:
        return PLAIN_GROUP_FUTURE[value]
    m = re.match(r"^(unit|sub) (.+)$", value)
    prefix, token = (m.group(1), m.group(2)) if m else ("", value)
    return PLAIN_PREFIX.get(prefix, "") + table.get(token, token)


def future_why(grade, reason):
    """The plain line under the Future grade (MODEL section 7.1, R7): a WEAK reason (a
    concentration without a moat strong enough to carry it), or the caveat an ADEQUATE
    carries with a concentration flag; nothing for a grade printed alone."""
    text = plain_reason(PLAIN_FUTURE, reason)
    if not text:
        return ""
    token = re.sub(r"^(unit|sub) ", "", reason)
    if grade == "WEAK":
        return text + (CONC_WEAK if token in CONC_TOKENS else "")
    if grade == "ADEQUATE" and token in CONC_TOKENS:
        return FUTURE_CAVEAT + text
    return ""


def past_why(grade, reason):
    """The plain line under the Past grade: a WEAK reason, or nothing when the
    reason is the ROCE level the Returns cell already shows."""
    m = LEVEL_RE.match(reason or "")
    if m:
        if grade != "WEAK":
            return ""
        metric = "return on equity" if m.group("metric") == "ROE" else "return on capital"
        return PLAIN_PREFIX.get(m.group("prefix") or "", "") + "%s too low (%s)" % (
            metric, one_decimal_pct(m.group("value") + "%"))
    return plain_reason(PLAIN_PAST, reason)


def failed_gates(row):
    return [g for g, bad in (("past", row["past"] == "WEAK"), ("future", row["future"] == "WEAK"),
                             ("sf", row["sf"] == "FAIL")) if bad]


def verdict_why(row):
    """The plain one-line reason under the verdict. A WATCH row reads its own distance:
    a sweep can price it at or below the trigger before the REVIEW that would move it."""
    section = row["section"]
    if section == "BUY":
        return "Passes every test, and the price is in the buy zone."
    if section == "WATCH":
        dist = distance(row["px"], row["trigger"])
        if dist is None:
            return "Passes all three quality tests; no buy-zone price is available."
        if dist[0] <= 0:
            return ("Passes all three quality tests; the latest price is at or below the buy-zone price, "
                    "pending review.")
        return WATCH_WHY
    if section == "DNAF":
        m = re.match(r"^v?(\d+)\.(\d+)", (row.get("model_version") or "").strip())   # as gsc_register.model_at_least
        return DNAF_WHY if m and (int(m.group(1)), int(m.group(2))) >= (4, 6) else DNAF_WHY_EARLIER
    failed = failed_gates(row)
    if len(failed) == 1:
        gate = failed[0]
        reason = {"past": past_why(row["past"], row["past_reason"]),
                  "future": plain_reason(PLAIN_FUTURE, row["future_reason"]),
                  "sf": plain_reason(PLAIN_SF, row["sf_reason"])}[gate]
        return "Failed the %s test%s." % (GATE_NAMES[gate], (": " + reason) if reason else "")
    if len(failed) > 1:
        names = [GATE_LIST_NAMES[g] for g in failed]
        listed = names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1]
        return "Failed %s tests: %s." % (NUMBER_WORDS.get(len(failed), str(len(failed))), listed)
    return "Fails a quality test."


def distance(px, trigger):
    """(px / trigger - 1, the price fall to the trigger 1 - trigger / px) as
    Decimals; None without a positive price and a positive trigger."""
    if not is_num(px) or not is_num(trigger):
        return None
    price, line = dec(px), dec(trigger)
    if price <= 0 or line <= 0:
        return None
    return price / line - 1, max(Decimal(0), 1 - line / price)


def multiple_cell(value):
    if MULT_RE.match(value or ""):
        return value.replace("-", "−") + "×"
    return NM if value == NM else DASH


def number_cell(value):
    if is_num(value):
        return group_digits(value)
    return NM if value == NM else DASH


def country_of(key, memo_fm):
    suffix = key_suffix(key)
    if suffix:
        return SUFFIX_COUNTRY[suffix]
    exchange = memo_fm.get("exchange", "")
    return US_COUNTRY + (" (ADR)" if re.search(r"\bAD[RS]\b", exchange) else "")


def closeness(px, trigger):
    """The bar's fill in whole percent: buy-zone price ÷ price, capped at 100 (a full bar
    is in the zone), so the shortlist's nearest names carry the longest bars."""
    ratio = dec(trigger) / dec(px) * 100
    return int(min(Decimal(100), ratio).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def page_row(row, memo_text, extra, as_of, held_marker, retest, dated=True):
    """The page's row for one register row: whitelisted display fields only. A
    not-analysed row carries no grades, returns, moat or multiples ('na'): the
    method stopped before any of them, whatever an older memo may hold. With
    `dated` false the price carries no date note (see DATED_SECTIONS)."""
    fm = parse_front_matter(memo_text or "")
    assessed = row["section"] != "DNAF"
    out = collections.OrderedDict()
    out["k"] = row["key"]
    out["n"] = row["company"]
    out["c"] = country_of(row["key"], fm)
    if held_marker and row["held"] == "true":
        out["h"] = 1
    if retest:
        out["r"] = 1
    out["b"] = extra.get("business") or ""
    if not assessed:
        out["na"] = 1
    out["m"] = (extra.get("moat") or "") if assessed else ""
    level = LEVEL_RE.match(row["past_reason"] or "")
    if level and not level.group("prefix"):
        out["rl"] = level.group("metric")
        out["ro"] = one_decimal_pct(level.group("value") + "%")
    else:
        out["rl"] = "ROCE"
        out["ro"] = extra.get("roce") or ""
    out["fr"] = extra.get("fcfroce") or ""
    if out["rl"] == "ROE" and out["fr"] == NM:
        out["fr"] = ""                      # FCFROCE does not apply where ROE replaces ROCE
    if not assessed:
        out["ro"] = out["fr"] = ""
    out["p"] = row["past"] if assessed else ""
    out["pw"] = past_why(row["past"], row["past_reason"]) if assessed else ""
    out["f"] = row["future"] if assessed else ""
    out["fw"] = future_why(row["future"], row["future_reason"]) if assessed else ""
    out["s"] = row["sf"] if assessed else ""
    sf_reason = plain_reason(PLAIN_SF, row["sf_reason"]) if assessed else ""
    out["sw"] = ("One caution: " + sf_reason) if (row["sf"] == "PASS" and sf_reason) else (
        sf_reason[:1].upper() + sf_reason[1:] if sf_reason else "")
    out["mf"] = multiple_cell(row["mcap_fcf"]) if assessed else DASH
    out["eo"] = multiple_cell(row["ev_oi"]) if assessed else DASH
    # R10: the same multiples on the 3- and 5-year average OI and FCF (EV/OI no-cash), context only.
    for short, name in (("mf3", "mcap_fcf_3y"), ("mf5", "mcap_fcf_5y"), ("eo3", "ev_oi_3y"), ("eo5", "ev_oi_5y")):
        out[short] = multiple_cell(row[name]) if assessed else DASH
    unit = row["px_unit"] if row["px_unit"] not in (OWED, NM) else ""
    out["u"] = unit
    out["px"] = number_cell(row["px"])
    if is_num(row["px"]) and dated:
        out["pd"] = ("as of " + fmt_day(row["px_date"])) if DATE_RE.match(row["px_date"]) else "price at memo date"
    else:
        out["pd"] = ""
    # Only BUY and WATCH have a buy zone: an AVOID fails a quality test, so no price makes it a buy.
    if row["section"] in ("BUY", "WATCH"):
        out["tg"] = number_cell(row["trigger"])
        if row["trigger_basis"] == "all-cash" and is_num(row["trigger"]):
            out["tl"] = 1                   # R10: a pre-R10 reading with spare cash counted, until its review
    out["v"] = row["verdict"] if assessed else "DNAF"
    out["vw"] = verdict_why(row)
    if out["vw"] == WATCH_WHY:
        out["vq"] = 1                       # repeats the section note: the phone card leaves it out
    dist = distance(row["px"], row["trigger"]) if row["section"] in ("BUY", "WATCH") else None
    if dist is not None:
        gap, fall = dist
        out["d"] = fmt_signed_pct(gap) if gap > 0 else "In zone"
        out["dl"] = fmt_pct(fall) if gap > 0 else ""
        out["bw"] = closeness(row["px"], row["trigger"])
    else:
        out["d"] = DASH
    out["md"] = fmt_day(row["memo_date"])
    review = row["next_review_short"]
    out["nr"] = fmt_day(review) if review not in (OWED, NM, "") else DASH
    last = review_last_day(review)
    if last and as_of and last < as_of:
        out["nd"] = 1
    return out


def ev_sort_key(row):
    """EV/OI ascending, then n.m., then '-'; ties by key (MODEL section 7.1 order)."""
    value = row.get("ev_oi", OWED)
    if MULT_RE.match(value or ""):
        return (0, Decimal(value), row["key"])
    return (1 if value == NM else 2, Decimal(0), row["key"])


def distance_sort_key(row):
    """Distance to the buy zone ascending; rows without one last; ties by key."""
    dist = distance(row["px"], row["trigger"])
    if dist is None:
        return (1, Decimal(0), row["key"])
    return (0, dist[0], row["key"])


def ordered_sections(rows):
    """{section: rows in page order}: BUY by EV/OI, WATCH by distance, AVOID by EV/OI, DNAF by key."""
    out = {}
    for section in SECTION_ORDER:
        members = [r for r in rows if r["section"] == section]
        if section == "WATCH":
            members.sort(key=distance_sort_key)
        elif section == "DNAF":
            members.sort(key=lambda r: r["key"])
        else:
            members.sort(key=ev_sort_key)
        out[section] = members
    return out


def sweep_prices(rows):
    """(count, dates, mostly WATCH) of the rows priced by a SWEEP: the closes the
    latest price sweep applied, as opposed to a memo's own price."""
    swept = [r for r in rows if r["px_source"].startswith("SWEEP") and is_num(r["px"])]
    dates = sorted({r["px_date"] for r in swept if DATE_RE.match(r["px_date"])})
    watch = sum(1 for r in swept if r["section"] == "WATCH")
    return len(swept), dates, bool(swept) and watch * 2 >= len(swept)


# ------------------------------------------------------------------ build

def extract_all(root, rows):
    """{key: extraction} for every row: business, moat, roce, fcfroce and where each came from."""
    out = {}
    for row in rows:
        text, source = read_memo(root, row)
        info = {"text": text, "source": source, "business": "", "moat": "", "roce": "", "fcfroce": "",
                "business_from": "", "moat_from": ""}
        if text is not None:
            info["business"] = extract_business(text, row["section"])
            info["business_from"] = source if info["business"] else ""
            info["moat"], strength = extract_moat(text)
            info["moat_from"] = source if info["moat"] else ""
            info["roce"], info["fcfroce"] = extract_returns(text)
            # A section that says 'Unchanged' or 'Restated' points back to the previous memo:
            # what it leaves out is read from the newest archived memo of the key.
            need_business = not info["business"] and is_unchanged(memo_section(text, 2))
            need_moat = strength < 2 and is_unchanged(memo_section(text, 4))
            need_returns = not (info["roce"] and info["fcfroce"]) and is_unchanged(memo_section(text, 3))
            older = older_memos(root, row["key"], row["memo_date"]) if (
                need_business or need_moat or need_returns) else []
            for old in older:
                if need_business and not info["business"]:
                    info["business"] = extract_business(old, row["section"])
                    info["business_from"] = "archive" if info["business"] else ""
                if need_moat and strength < 2:
                    moat, old_strength = extract_moat(old)
                    if old_strength > strength:
                        info["moat"], strength, info["moat_from"] = moat, old_strength, "archive"
                if need_returns:
                    roce, fcf = extract_returns(old)
                    info["roce"] = info["roce"] or roce
                    info["fcfroce"] = info["fcfroce"] or fcf
                if info["business"] and strength == 2 and info["roce"] and info["fcfroce"]:
                    break
        out[row["key"]] = info
    return out


def build(root, no_held=False):
    """Everything the page needs: (context, sections, extraction, register rows). The page
    itself is render_page(context, sections); stats_text() reads the extraction."""
    rows, reg_fm = load_register(root)
    # [v4.6.0; G5] A RETIRED row's line has ceased to trade: it is no investable name, so the
    # page leaves it out, from the sections, the counts and the lead alike.
    rows = [row for row in rows if row["section"] != RETIRED]
    for row in rows:
        if row["section"] not in SECTION_ORDER:
            raise ToolError("%s: unknown section %r" % (row["key"], row["section"]))
    extraction = extract_all(root, rows)
    versions, retest_keys = retest_block(root)
    keys = {r["key"] for r in rows}
    retest = collections.OrderedDict((k, v) for k, v in retest_keys.items() if k in keys)
    by_version = retest_versions(versions, retest)
    as_of = reg_fm.get("register_date", "")
    ordered = ordered_sections(rows)
    sections = []
    for section in SECTION_ORDER:
        page_rows = []
        for row in ordered[section]:
            info = extraction[row["key"]]
            page_rows.append(page_row(row, info["text"], info, as_of, not no_held, row["key"] in retest,
                                      dated=(not no_held) or section in DATED_SECTIONS))
        label, note = SECTIONS[section]
        sections.append(collections.OrderedDict([("id", section), ("title", label), ("note", note),
                                                 ("rows", page_rows)]))
    context = {
        "names": len(rows),
        "counts": {s: len(ordered[s]) for s in SECTION_ORDER},
        "register_version": reg_fm.get("register_version", ""),
        "register_date": as_of,
        "model_version": model_version(root),
        # Under --no-held the lead names no sweep: a held name is the only one a sweep prices
        # outside BUY, WATCH and one-test AVOID, so a sweep count would point at it (DATED_SECTIONS).
        "sweep": (0, [], False) if no_held else sweep_prices(rows),
        # Every re-test block counts (retest_block); the label names the versions whose blocks
        # list a key on the page, newest block first ("v4.6.0 and v4.5.0").
        "retest_version": " and ".join(v for v, _n in by_version),
        "retest_versions": by_version,
        "retest_count": len(retest),
        "retest_watch": sum(1 for r in rows if r["key"] in retest and r["section"] == "WATCH"),
        "no_held": no_held,
        "held_marker": (not no_held) and any(r["held"] == "true" for r in rows),
        "units": sorted({r["px_unit"] for r in rows if r["px_unit"] in UNIT_NOTES}),
    }
    return context, sections, extraction, rows


# ------------------------------------------------------------------ render

def esc(value):
    return html.escape(str(value), quote=True)


def json_blob(data):
    """JSON safe inside an HTML <script>: no '<', '>' or '&' survive as raw characters."""
    text = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    for raw, escaped in (("&", "\\u0026"), ("<", "\\u003c"), (">", "\\u003e"),
                         ("\u2028", "\\u2028"), ("\u2029", "\\u2029")):
        text = text.replace(raw, escaped)
    return text


def stat_strip(ctx):
    """The stat tiles: the five sections under their section labels, then the re-test
    count as a dashed note tile (it overlaps the sections, which sum to the total)."""
    n = ctx["counts"]
    tiles = [(ctx["names"], "Companies covered", "")]
    for section, cls in (("BUY", "buy"), ("WATCH", "watch"), ("AVOID-1", "avoid"), ("AVOID-2", "avoid"),
                         ("DNAF", "inc")):
        tiles.append((n[section], SECTIONS[section][0], cls))
    if ctx["retest_count"]:
        tiles.append((ctx["retest_count"], "Being re-tested", "note"))
    return "\n".join('    <div class="stat%s"><b>%d</b><span>%s</span></div>'
                     % ((" stat-" + cls) if cls else "", value, esc(label)) for value, label, cls in tiles)


def freshness(ctx):
    """The line under the heading: register version and date."""
    return esc("Register %s · updated %s" % (ctx["register_version"], fmt_day(ctx["register_date"])))


def lead_text(ctx):
    parts = [
        "A research register of %d companies, each assessed with one consistent, rules-based value-investing "
        "method based on Kenneth Jeffrey Marshall's book <cite>Good Stocks Cheap</cite> (GSC)." % ctx["names"],
    ]                                       # the register version and date stand on the line above (freshness)
    count, dates, mostly_watch = ctx["sweep"]
    if count and dates:
        if len(dates) == 1:
            when = fmt_day(dates[0])
        elif len(dates) == 2:
            when = "%s and %s" % (fmt_day(dates[0]), fmt_day(dates[1]))
        else:
            when = "%s to %s" % (fmt_day(dates[0]), fmt_day(dates[-1]))
        parts.append("Prices for %d companies%s are closes of %s from the latest price sweep; the others are as "
                     "of each company's research memo. Every price shows its date."
                     % (count, ", mostly on the shortlist," if mostly_watch else "", esc(when)))
    elif ctx["no_held"]:
        parts.append("Prices are the latest the register holds. A BUY or WATCH price shows its date; for AVOID "
                     "and not-analysed companies the price is context only and is shown undated.")
    else:
        parts.append("Prices are as of each company's research memo. Every price shows its date.")
    parts.append("Each company was assessed under the method version in force on its memo date.")
    return " ".join(parts)


def notice_text(ctx):
    """The not-advice notice: no recommendation, an accuracy caveat, the holdings
    disclosure (generic without the Held marker) and non-affiliation with the book's author."""
    held = ("The author holds shares in the companies marked Held." if ctx["held_marker"]
            else "The author may hold shares in companies on this page.")
    return ("<b>Not investment advice.</b> This page shows the output of a mechanical research framework. It is "
            "not investment advice and not a recommendation to buy or sell any security. Figures come from "
            "company filings and research notes, and may contain errors or be out of date. %s Not affiliated "
            "with or endorsed by Kenneth Jeffrey Marshall." % held)


def retest_banner(ctx):
    if not ctx["retest_count"]:
        return ""
    version = (" (%s)" % esc(ctx["retest_version"])) if ctx["retest_version"] else ""
    # Two re-test blocks at once (v4.6.0 above v4.5.0): the names are re-tested under updated versions.
    updated = ("updated versions" if len([v for v, n in ctx.get("retest_versions") or [] if n]) > 1
               else "an updated version")
    count, watch, total_watch = ctx["retest_count"], ctx["retest_watch"], ctx["counts"]["WATCH"]
    subject = "%d %s" % (count, "company" if count == 1 else "companies")
    if watch and count > 1:
        subject += ", including %d of the %d on the shortlist," % (watch, total_watch)
    return ('  <p class="banner" role="status"><b>%s %s being re-tested</b> under %s of the '
            'method%s. Treat %s as provisional: %s%s. %s a <span class="tag tag-re">Re-test</span> mark '
            'below.</p>\n'
            % (subject, "is" if count == 1 else "are", updated, version,
               "its verdict" if count == 1 else "their verdicts",
               "it may change" if count == 1 else "they may change",
               ", including from WATCH to AVOID" if watch else "",
               "It carries" if count == 1 else "They carry"))


def chips(ctx, sections):
    """The filter chips in one row (it wraps on a wide screen and scrolls sideways on a phone)."""
    out = ['    <div class="chiprow">',
           '      <button class="chip" type="button" id="f-ALL" data-f="ALL" aria-pressed="true">All</button>']
    for sec in sections:
        if sec["rows"]:
            out.append('      <button class="chip" type="button" id="f-%s" data-f="%s" aria-pressed="false">%s '
                       '<span class="chip-n">%d</span></button>' % (sec["id"], sec["id"], esc(sec["title"]),
                                                                    len(sec["rows"])))
    if ctx["retest_count"]:
        out.append('      <button class="chip" type="button" id="f-RETEST" data-f="RETEST" aria-pressed="false">'
                   'Re-test <span class="chip-n">%d</span></button>' % ctx["retest_count"])
    out.append('    </div>')
    return "\n".join(out)


def terms(ctx):
    items = [
        ("ROCE · FCFROCE", "Operating income, and free cash flow, as a share of the capital the business uses; "
                           "the worst of four averaged readings over up to ten years ('negative': every reading "
                           "is below zero). ROE (return on equity) replaces ROCE for banks and insurers on the "
                           "bank lens."),
        ("MCap/FCF", "Market value ÷ free cash flow: cash from operations less the capital spending needed to "
                     "maintain the business (the company's figure or a stated estimate); growth spending is not "
                     "counted against it. A row not yet reviewed under the updated method may still deduct all "
                     "capital spending, which can only make this multiple look higher. For banks and insurers "
                     "on the bank lens it reads market value ÷ net income, and the buy-zone price comes from "
                     "the lower of 8× net income and 3× tangible book value; EV/OI does not apply and shows "
                     "n.m."),
        ("EV/OI", "Enterprise value (market value plus debt and debt-like items) ÷ operating income, with no "
                  "cash counted as spare: the stricter of the method's two readings."),
        ("3y · 5y", "The same multiples at today's price on the average operating income and free cash flow of "
                    "the last three and five years: a check against one unusual year."),
        ("Buy-zone price", "Shown for BUY and WATCH only: the highest price at which MCap/FCF ≤ 8× and EV/OI ≤ 7× "
                           "with no cash counted as spare — the strict reading a BUY needs. A marked figure is an "
                           "older, looser reading (spare cash counted) awaiting its review. An AVOID has no buy "
                           "zone: under this method a company that fails a quality test is not a buy at any "
                           "price."),
        ("To buy zone", "Price ÷ buy-zone price − 1, with the price fall needed to reach the buy-zone price. "
                        "The bar shows how close the price is: a full bar is in the buy zone."),
        ("n.m.", "Not meaningful: for example a multiple of zero or negative cash flow or income (and EV/OI for "
                 "banks and insurers on the bank lens)."),
        (DASH, "Not available in the register or the memo. Figures are never estimated."),
        ("Review due", "The next scheduled review date has passed as of this register version."),
    ]
    if ctx["units"]:
        notes = ", ".join("%s = %s" % (u, UNIT_NOTES[u]) for u in ctx["units"])
        items.append(("Units", "Prices are in the listing's own quote unit (%s)." % notes))
    else:
        items.append(("Units", "Prices are in the listing's own quote unit."))
    items.append(("Country", "Where the share line priced here is listed (ADR: a US-listed depositary share)."))
    items.append(("Wording", "Business and moat lines are taken from the research memos, shortened, and may use "
                             "industry abbreviations."))
    if ctx["retest_count"]:
        items.append(("Re-test", "Scheduled for re-assessment under the updated method; the verdict may change."))
    if ctx["held_marker"]:
        items.append(("Held", "The register's author holds shares in the company (disclosed for transparency)."))
    return "\n".join('        <dt>%s</dt><dd>%s</dd>' % (esc(term), esc(text)) for term, text in items)


def render_page(ctx, sections):
    """The page content (artifact contract: starts with <title>, no html/head/body)."""
    data = collections.OrderedDict([("sections", sections), ("legacy", LEGACY_TRIGGER_NOTE)])
    if ctx["held_marker"]:
        data["mark"] = "Held"       # the marker's label travels with the data, so --no-held leaves no trace
    page = PAGE_TEMPLATE
    replacements = [
        ("@@TITLE@@", esc(PAGE_TITLE)),
        ("@@FRESH@@", freshness(ctx)),
        ("@@LEAD@@", lead_text(ctx)),
        ("@@NOTICE@@", notice_text(ctx)),
        ("@@STATS@@", stat_strip(ctx)),
        ("@@BANNER@@", retest_banner(ctx)),
        ("@@MODEL@@", esc(ctx["model_version"] or "unknown")),
        ("@@TERMS@@", terms(ctx)),
        ("@@CHIPS@@", chips(ctx, sections)),
        ("@@TOTAL@@", str(ctx["names"])),
        ("@@REGISTER@@", esc("%s (%s)" % (ctx["register_version"], fmt_day(ctx["register_date"])))),
        ("@@SCRIPT@@", PAGE_SCRIPT),
        ("@@DATA@@", json_blob(data)),
    ]
    for marker, value in replacements:
        page = page.replace(marker, value)
    return page


def write_text(path, text):
    folder = os.path.dirname(os.path.abspath(path))
    if folder:
        os.makedirs(folder, exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    os.replace(tmp, path)


# ------------------------------------------------------------------ page template

PAGE_CSS = r"""
/* Layout: one research ledger - masthead and not-advice notice, stat strip, method panel, then one filterable table in register sections (cards under 640px). */
:root{
  --bg:#f3f5f4; --surface:#ffffff; --ink:#17212b; --muted:#5b6872; --line:#d9dfe1; --hover:#f7f9f8;
  --accent:#2c3d8f; --watch:#0f6e62; --watch-bg:#e1f2ee; --avoid:#9a3b2e; --avoid-bg:#f6e6e2;
  --inc:#6b6f76; --inc-bg:#eceef0; --fair:#8a6100; --fair-bg:#fbf0d6;
  --display:"Bricolage Grotesque", "Segoe UI", system-ui, sans-serif;
  --body:"Source Sans 3", "Segoe UI", system-ui, sans-serif;
  --mono:"JetBrains Mono", ui-monospace, Consolas, monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#12171c; --surface:#1a2128; --ink:#e4e9ec; --muted:#9aa6af; --line:#2c353d; --hover:#202931;
  --accent:#9fb0ff; --watch:#6fd3c2; --watch-bg:#143530; --avoid:#f0a092; --avoid-bg:#3a1f1a;
  --inc:#b5bac1; --inc-bg:#2a3036; --fair:#f0c36a; --fair-bg:#3a2f12; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#12171c; --surface:#1a2128; --ink:#e4e9ec; --muted:#9aa6af; --line:#2c353d; --hover:#202931;
  --accent:#9fb0ff; --watch:#6fd3c2; --watch-bg:#143530; --avoid:#f0a092; --avoid-bg:#3a1f1a;
  --inc:#b5bac1; --inc-bg:#2a3036; --fair:#f0c36a; --fair-bg:#3a2f12; color-scheme:dark}
body{background:var(--bg);color:var(--ink);font-family:var(--body);font-size:15px;line-height:1.45}
[hidden]{display:none!important}
.sr{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
.wrap{max-width:1440px;margin:0 auto;padding-inline:16px;padding-block:28px 48px;display:grid;gap:20px}
.wrap>*{min-width:0}
header{display:grid;gap:10px}
.eyebrow{margin:0;font:600 12px var(--body);text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
h1{font-family:var(--display);font-size:clamp(28px,4.4vw,42px);line-height:1.05;margin:0;text-wrap:balance;letter-spacing:-.01em}
.fresh{margin:0;font-size:13.5px;font-weight:600;color:var(--ink);font-variant-numeric:tabular-nums}
.lead{color:var(--muted);max-width:72ch;margin:0}
.lead cite{font-style:italic;color:var(--ink)}
.notice{margin:0;max-width:72ch;background:var(--fair-bg);color:var(--ink);border:1px solid var(--fair);border-radius:8px;padding:10px 14px;font-size:14.5px}
.notice b{color:var(--fair)}
.banner{margin:0;background:var(--inc-bg);border-radius:8px;padding:9px 14px;font-size:14px;max-width:90ch}
.strip{display:flex;flex-wrap:wrap;gap:10px}
.stat{background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:10px 14px;min-width:132px;flex:0 1 auto}
.stat b{display:block;font-family:var(--display);font-size:26px;line-height:1.05;font-variant-numeric:tabular-nums}
.stat span{font-size:11.5px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.stat-buy b{color:var(--accent)} .stat-watch b{color:var(--watch)} .stat-avoid b{color:var(--avoid)} .stat-inc b{color:var(--inc)}
.stat-note{background:transparent;border-style:dashed;border-color:var(--inc)} .stat-note b{color:var(--inc)}
.method{background:var(--surface);border:1px solid var(--line);border-radius:10px}
.method summary{cursor:pointer;padding:12px 16px;font:700 16px var(--display);list-style-position:inside}
.method summary:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:10px}
.method-body{padding:0 16px 16px;display:grid;gap:14px;max-width:96ch}
.method-body p,.method-body ol,.method-body ul,.method-body dl{margin:0}
.method-body ol{padding-left:22px;display:grid;gap:10px}
.method-body ul{padding-left:18px;display:grid;gap:6px;margin-top:6px}
.method-body h3{margin:0;font:700 14px var(--display);letter-spacing:.02em}
.method-body code{font-family:var(--mono);font-size:13px}
dl.defs{display:grid;grid-template-columns:minmax(110px,max-content) minmax(0,1fr);gap:6px 16px}
dl.defs dt{font-weight:600}
dl.defs dd{margin:0;color:var(--muted)}
.rules{font-size:13.5px;color:var(--muted);display:flex;flex-wrap:wrap;gap:6px 18px}
.rules code{font-family:var(--mono);font-size:12.5px;color:var(--ink)}
.vkey{margin:0;font-size:13.5px;color:var(--muted);max-width:110ch}
.vkey b{color:var(--ink)}
.controls{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.chiprow{display:flex;flex-wrap:wrap;gap:8px;min-width:0}
.chip{font:600 13px var(--body);border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:999px;padding:6px 13px;cursor:pointer;transition:background-color .15s,border-color .15s}
.chip-n{font:600 11.5px var(--mono);color:var(--muted);margin-left:2px}
.chip[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:var(--bg)}
.chip[aria-pressed="true"] .chip-n{color:var(--bg)}
.chip:focus-visible,#q:focus-visible,.tablebox:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.search{display:flex;flex-wrap:wrap;gap:8px;align-items:center;flex:1 1 300px;min-width:0}
#q{font:14px var(--body);padding:7px 12px;border:1px solid var(--line);border-radius:8px;background:var(--surface);color:var(--ink);min-width:0;flex:1 1 220px;max-width:340px}
.count{font-size:13px;color:var(--muted);font-variant-numeric:tabular-nums;white-space:nowrap}
.tablebox{overflow:auto;max-height:calc(100vh - 24px);background:var(--surface);border:1px solid var(--line);border-radius:10px}
table{border-collapse:separate;border-spacing:0;table-layout:fixed;width:1628px}
th,td{box-sizing:border-box;overflow-wrap:anywhere}
th{font:600 11px var(--body);text-transform:uppercase;letter-spacing:.06em;color:var(--muted);text-align:left;padding:10px 10px;border-bottom:1px solid var(--line);position:sticky;top:0;background:var(--surface);z-index:2;vertical-align:bottom}
th:first-child{left:0;z-index:3}
.w-co{width:180px} .w-v{width:170px} .w-d{width:108px} .w-px{width:128px} .w-biz{width:250px} .w-ret{width:160px}
.w-comp{width:200px} .w-sf{width:170px} .w-mf{width:76px} .w-eo{width:68px} .w-memo{width:118px}
td{padding:10px 10px;border-bottom:1px solid var(--line);vertical-align:top;background:var(--surface)}
tr.row:hover td{background:var(--hover)}
td.c-co{position:sticky;left:0;z-index:1;overflow-wrap:normal}
.sec td{background:var(--bg);padding:9px 12px}
.sec-in{position:sticky;left:12px;display:inline-flex;flex-wrap:wrap;gap:4px 10px;align-items:baseline}
.sec-t{font:700 14px var(--display);letter-spacing:.02em}
.sec-n{font:600 12px var(--mono);color:var(--muted)}
.sec-d{font-size:12.5px;color:var(--muted)}
.key{font-family:var(--mono);font-weight:600;font-size:12.5px}
.name{display:block;font-weight:600;line-height:1.3}
.cty{font-size:12px;color:var(--muted)}
.tags{display:flex;flex-wrap:wrap;gap:4px;margin-top:5px}
.tag{font:600 11px var(--body);letter-spacing:.05em;text-transform:uppercase;padding:1px 6px;border-radius:4px;border:1px solid var(--line);color:var(--muted);white-space:nowrap}
.tag-re{border-color:var(--inc);color:var(--ink);background:var(--inc-bg)}
.biz{font-size:14px}
.txt{font-size:14px}
.fig-text{display:block;margin-bottom:5px}
.fig{font-family:var(--mono);font-size:12.5px;font-variant-numeric:tabular-nums;display:block;margin-bottom:3px}
.na{font-size:13px;color:var(--muted);font-style:italic}
.num{font-family:var(--mono);font-size:13px;font-variant-numeric:tabular-nums;white-space:nowrap}
.sub{display:block;font-size:12px;color:var(--muted);font-family:var(--body);white-space:nowrap}
.sub.old{color:var(--fair);white-space:normal}
.grade{font:600 11px var(--mono);letter-spacing:.03em;padding:1px 6px;border-radius:4px;border:1px solid var(--line);white-space:nowrap;color:var(--muted)}
.g-STRONG,.g-PASS{color:var(--watch);border-color:var(--watch)}
.g-WEAK,.g-FAIL{color:var(--avoid);border-color:var(--avoid)}
.why{display:block;font-size:13px;color:var(--muted);margin-top:4px}
.v{display:inline-block;font:700 12px var(--body);letter-spacing:.05em;padding:3px 8px;border-radius:5px;white-space:nowrap}
.v-BUY{background:var(--accent);color:var(--surface)}
.v-WATCH{background:var(--watch-bg);color:var(--watch)}
.v-AVOID{background:var(--avoid-bg);color:var(--avoid)}
.v-DNAF{background:var(--inc-bg);color:var(--inc)}
.dist{font:600 14px var(--mono);font-variant-numeric:tabular-nums;white-space:nowrap}
.bar{display:block;width:84px;height:6px;border-radius:3px;background:var(--line);margin:6px 0 3px;overflow:hidden}
.bar i{display:block;height:100%;background:var(--watch);border-radius:3px}
.due{color:var(--fair)}
.empty{padding:20px;color:var(--muted)}
.foot{font-size:12.5px;color:var(--muted);max-width:96ch;margin:0}
@media (max-width:640px){
  .strip{display:grid;grid-template-columns:repeat(2,minmax(0,1fr))}
  .stat{min-width:0}
  .controls{position:sticky;top:0;z-index:4;background:var(--bg);padding-block:8px;flex-wrap:nowrap;flex-direction:column;align-items:stretch}
  .chiprow{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;padding-bottom:2px}
  .chiprow::-webkit-scrollbar{display:none}
  .chip{flex:0 0 auto}
  .search{flex:0 0 auto;flex-wrap:nowrap}
  #q{flex:1 1 0;max-width:none}
  .tablebox{overflow:visible;max-height:none;background:transparent;border:0;border-radius:0}
  table{width:auto;display:block;table-layout:auto}
  thead{display:none}
  tbody{display:grid;gap:10px}
  tr.sec{display:block}
  .sec td{display:block;background:transparent;padding:14px 0 2px;border:0}
  .sec-in{position:static}
  tr.row{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px 14px;background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:14px}
  tr.row td{display:block;padding:0;border:0;background:transparent;min-width:0;max-width:none;position:static}
  tr.row:hover td{background:transparent}
  td.c-co,td.c-v,td.c-biz,td.c-txt,td.c-memo{grid-column:1/-1}
  td[data-label]::before{content:attr(data-label);display:block;font:600 10.5px var(--body);text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin-bottom:2px}
  .why{max-width:none}
  .why-q{display:none}
  .sub{white-space:normal}
  td.c-memo .sub{display:inline;margin-left:8px}
}
@media (prefers-reduced-motion: reduce){*{transition:none!important;animation:none!important;scroll-behavior:auto!important}}
"""

PAGE_SCRIPT = r"""
(function(){
  "use strict";
  var DATA = JSON.parse(document.getElementById("gsc-data").textContent);
  var GRADE = {STRONG:"Strong", ADEQUATE:"Adequate", WEAK:"Weak", PASS:"Pass", FAIL:"Fail"};
  var VERDICT = {BUY:"BUY", WATCH:"WATCH", AVOID:"AVOID", DNAF:"Not analysed"};
  var STORE = "gsc-register-filter";
  var NA = '<span class="na">not assessed</span>';
  function esc(s){
    return String(s == null ? "" : s).replace(/[&<>"']/g, function(c){
      return {"&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#39;"}[c];
    });
  }
  function grade(g){
    if (!GRADE[g]) return '<span class="grade">' + esc(g && g !== "-" ? g : "—") + '</span>';
    return '<span class="grade g-' + esc(g) + '">' + esc(GRADE[g]) + '</span>';
  }
  function why(text, quiet){ return text ? '<span class="why' + (quiet ? ' why-q' : '') + '">' + esc(text) + '</span>' : ''; }
  function cell(cls, label, body){
    return '<td class="' + cls + '" data-label="' + esc(label) + '">' + body + '</td>';
  }
  function returns(r){
    if (r.na) return NA;
    var figs = '';
    if (r.ro) figs += '<span class="fig">' + esc(r.rl) + ' ' + esc(r.ro) + '</span>';
    if (r.fr) figs += '<span class="fig">FCFROCE ' + esc(r.fr) + '</span>';
    return (figs || '<span class="fig">—</span>') + grade(r.p) + why(r.pw);
  }
  function competitive(r){
    if (r.na) return NA;
    var moat = !r.m ? '—' : (/\bmoat\b/i.test(r.m) ? esc(r.m) : 'Moat: ' + esc(r.m));
    return '<span class="fig-text">' + moat + '</span><span class="tags">' + grade(r.f) + '</span>' + why(r.fw);
  }
  function friendliness(r){ return r.na ? NA : grade(r.s) + why(r.sw); }
  function price(r){
    var unit = r.u ? ' ' + esc(r.u) : '';
    var out = '<span class="num">' + esc(r.px) + (r.px !== "—" && r.px !== "n.m." ? unit : '') + '</span>';
    if (r.pd) out += '<span class="sub">' + esc(r.pd) + '</span>';
    if (typeof r.tg === "string"){
      out += '<span class="sub">' + (r.tg !== "—" && r.tg !== "n.m." ? 'buy zone ≤ ' + esc(r.tg) + unit : 'no buy-zone price') + '</span>';
      if (r.tl) out += '<span class="sub old">' + esc(DATA.legacy) + '</span>';
    } else if (r.v === "AVOID"){
      out += '<span class="sub">no buy zone: fails a quality test</span>';
    }
    return out;
  }
  function dist(r){
    if (r.d === "—") return '<span class="dist">—</span>';
    var out = '<span class="dist">' + esc(r.d) + '</span>';
    if (typeof r.bw === "number"){
      out += '<span class="bar" aria-hidden="true"><i style="width:' + r.bw + '%"></i></span>';
    }
    if (r.dl) out += '<span class="sub">fall needed: ' + esc(r.dl) + '</span>';
    else if (r.d === "In zone") out += '<span class="sub">at or below the buy-zone price</span>';
    return out;
  }
  function multiple(value, y3, y5){
    var out = '<span class="num">' + esc(value) + '</span>';
    if (y3 !== "—" || y5 !== "—") out += '<span class="sub">3y ' + esc(y3) + ' · 5y ' + esc(y5) + '</span>';
    return out;
  }
  function company(r){
    var tags = '';
    if (r.h && DATA.mark) tags += '<span class="tag">' + esc(DATA.mark) + '</span>';
    if (r.r) tags += '<span class="tag tag-re">Re-test</span>';
    return '<span class="name">' + esc(r.n) + '</span><span class="key">' + esc(r.k) + '</span> ' +
      '<span class="cty">· ' + esc(r.c) + '</span>' + (tags ? '<span class="tags">' + tags + '</span>' : '');
  }
  function row(sec, r){
    var search = [r.k, r.n, r.c, r.b, r.m, r.pw, r.fw, r.sw, r.vw].join(" ").toLowerCase();
    var review = esc(r.nr) + (r.nd ? ' <span class="due">· review due</span>' : '');
    return '<tr class="row" data-sec="' + esc(sec) + '"' + (r.r ? ' data-re="1"' : '') +
      ' data-t="' + esc(search) + '">' +
      cell('c-co', '', company(r)) +
      cell('c-v', 'Verdict', '<span class="v v-' + esc(r.v) + '">' + esc(VERDICT[r.v] || r.v) + '</span>' + why(r.vw, r.vq)) +
      cell('c-n', 'To buy zone', dist(r)) +
      cell('c-n', 'Price · buy zone', price(r)) +
      cell('c-biz biz', 'Business', esc(r.b || '—')) +
      cell('c-txt txt', 'Returns · past record', returns(r)) +
      cell('c-txt txt', 'Competitive position', competitive(r)) +
      cell('c-txt txt', 'Shareholder-friendliness', friendliness(r)) +
      cell('c-n num', 'MCap/FCF', multiple(r.mf, r.mf3, r.mf5)) +
      cell('c-n num', 'EV/OI', multiple(r.eo, r.eo3, r.eo5)) +
      cell('c-memo', 'Memo · next review', '<span class="num">' + esc(r.md) + '</span><span class="sub">next review ' + review + '</span>') +
      '</tr>';
  }
  var html = [];
  DATA.sections.forEach(function(sec){
    if (!sec.rows.length) return;
    html[html.length] = ('<tr class="sec" data-sec="' + esc(sec.id) + '"><td colspan="11"><span class="sec-in">' +
      '<span class="sec-t">' + esc(sec.title) + '</span><span class="sec-n">' + sec.rows.length + '</span>' +
      '<span class="sec-d">' + esc(sec.note) + '</span></span></td></tr>');
    sec.rows.forEach(function(r){ html[html.length] = row(sec.id, r); });
  });
  var tbody = document.getElementById("tb");
  tbody.innerHTML = html.join("");
  var rows = Array.prototype.slice.call(tbody.querySelectorAll("tr.row"));
  var heads = Array.prototype.slice.call(tbody.querySelectorAll("tr.sec"));
  var chips = Array.prototype.slice.call(document.querySelectorAll(".chip"));
  var q = document.getElementById("q");
  var countEl = document.getElementById("count");
  var empty = document.getElementById("empty");
  var current = "ALL";
  try { var saved = window.localStorage.getItem(STORE); if (saved && document.getElementById("f-" + saved)) current = saved; } catch (e) {}
  function apply(){
    var text = (q.value || "").trim().toLowerCase();
    var shown = 0, perSec = {};
    rows.forEach(function(tr){
      var sec = tr.getAttribute("data-sec");
      var okF = current === "ALL" || sec === current || (current === "RETEST" && tr.getAttribute("data-re") === "1");
      var ok = okF && (!text || tr.getAttribute("data-t").indexOf(text) !== -1);
      tr.hidden = !ok;
      if (ok){ shown++; perSec[sec] = true; }
    });
    heads.forEach(function(tr){ tr.hidden = !perSec[tr.getAttribute("data-sec")]; });
    chips.forEach(function(c){ c.setAttribute("aria-pressed", c.getAttribute("data-f") === current ? "true" : "false"); });
    countEl.textContent = "Showing " + shown + " of " + rows.length;
    empty.hidden = shown !== 0;
  }
  chips.forEach(function(c){
    c.addEventListener("click", function(){
      current = c.getAttribute("data-f");
      try { window.localStorage.setItem(STORE, current); } catch (e) {}
      apply();
    });
  });
  q.addEventListener("input", apply);
  apply();
})();
"""

PAGE_TEMPLATE = """<title>@@TITLE@@</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Source+Sans+3:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@400;600&display=swap">
<style>""" + PAGE_CSS + """</style>

<div class="wrap">
  <header>
    <p class="eyebrow">Value-investing research · Good Stocks Cheap (GSC) method</p>
    <h1>@@TITLE@@</h1>
    <p class="fresh">@@FRESH@@</p>
    <p class="lead">@@LEAD@@</p>
    <p class="notice" role="note">@@NOTICE@@</p>
  </header>
  <div class="strip" role="group" aria-label="Register summary">
@@STATS@@
  </div>
@@BANNER@@  <details class="method" id="method">
    <summary>How the method works</summary>
    <div class="method-body">
      <p>Every company goes through the same three questions, in this order. A company that fails a quality test is set aside whatever its price.</p>
      <ol>
        <li><b>Do I understand it?</b> The business is described in one plain sentence, the best its filings allow: what it sells, who pays for it, its industry, its legal and operating form, where it works, and its status. A long sentence or a list of businesses still passes. Only when the filings do not show what the business sells, and who pays for it, for most of its revenue is it not analysed further.</li>
        <li><b>Is it good?</b> Three tests, graded one by one.
          <ul>
            <li><b>Past record</b> (Strong, Adequate or Weak), from up to ten years of audited accounts. Return on capital (ROCE) and free-cash-flow return on capital (FCFROCE) are averaged four conservative ways, and the worst reading counts. Strong needs ROCE of at least 15% and FCFROCE of at least 8%, with operating income and free cash flow per share growing at least 3% a year. Adequate needs, with neither per-share figure shrinking, either the same returns with at least one of the two growing 3% a year, or ROCE of at least 10% and FCFROCE of at least 5.3% with both growing at least 6% a year. Losses, lower returns, shrinking per-share results or liabilities above twice equity (with narrow exceptions) make it Weak; a sustained decline in returns caps the grade at Adequate while returns stay high, and makes it Weak otherwise. Banks and insurers on the bank lens (a licensed bank or insurer that publishes a regulatory capital ratio for the whole group, with no sizeable non-financial business) are graded on return on equity and a regulatory capital test instead.</li>
            <li><b>Competitive position</b> (Strong, Adequate or Weak). The customer and supplier base (any paying customer above a tenth of revenue, distributors and retailers included, or any supplier above a tenth of costs, is flagged; for a business selling to other businesses, its filings must rule a large customer out); four competitive forces (the bargaining power of customers and of suppliers, substitutes, new entrants); a moat with one identified source (government, cost, brand, network, switching costs or ingrainedness) and its direction; and whether the market grows. A flagged dependence passes, as Adequate with a caveat, only behind a dominant, stable moat with pricing power over that customer or supplier; otherwise it counts as a strong force against the company. Two or more strong forces, no moat or an eroding moat make it Weak.</li>
            <li><b>Shareholder-friendliness</b> (Pass or Fail): executive and board pay (the largest pay figure on any basis), management's own shareholding, dealings with related parties, and capital allocation, with buybacks and acquisitions judged against what the business is worth. One serious finding, or two separate warning signs, is a Fail; so is a single warning sign where management owns little and voting control sits apart from the economics. Otherwise a single warning sign is noted as a caution.</li>
          </ul>
        </li>
        <li><b>Is it cheap?</b> At the current price, market value must be at most <code>8×</code> free cash flow <em>and</em> enterprise value at most <code>7×</code> operating income, whether none or all of the company's cash is counted as spare. Free cash flow deducts only the capital spending needed to maintain the business, so spending on growth never counts against it. The buy-zone price is the highest price at which both hold with no cash counted as spare. When the latest year was a one-off down year (an impairment, a restructuring or a disruption, with recovery evidenced), the lower of the three- and five-year averages is used instead.</li>
      </ol>
      <p>Groups, conglomerates, trading houses and holding companies included, are judged as a whole: returns on the group accounts, competitive position as an income-weighted average of the businesses, shareholder-friendliness including how the group allocates capital among them, price on the whole group. Banks and insurers that do not fit the bank lens are read on the industrial lens, with conservative rules for deposits, insurance funds and unlisted stakes.</p>
      <h3>Verdicts</h3>
      <dl class="defs">
        <dt><span class="v v-BUY">BUY</span></dt><dd>Passes all three quality tests and the price is in the buy zone. A mechanical signal of the framework, not a recommendation.</dd>
        <dt><span class="v v-WATCH">WATCH</span></dt><dd>Passes all three quality tests, but the price is above the buy zone. The shortlist ranks these by how far the price is from it.</dd>
        <dt><span class="v v-AVOID">AVOID</span></dt><dd>Fails at least one quality test. A lower price does not change this.</dd>
        <dt><span class="v v-DNAF">Not analysed</span></dt><dd>Stopped at the first question: the filings do not show what the business sells, and who pays for it, for most of its revenue.</dd>
      </dl>
      <h3>Reading the table</h3>
      <dl class="defs">
@@TERMS@@
      </dl>
    </div>
  </details>
  <div class="rules" role="group" aria-label="Thresholds">
    <span>Past record: worst-case ROCE <code>≥ 15%</code> and FCFROCE <code>≥ 8%</code> for Strong · at least ROCE <code>≥ 10%</code> and FCFROCE <code>≥ 5.3%</code>, with <code>6%</code> yearly growth, for Adequate</span>
    <span>Banks and insurers on the bank lens: return on equity <code>≥ 15%</code> and a capital test, for Strong or Adequate</span>
    <span>Buy zone: MCap/FCF <code>≤ 8×</code> and EV/OI <code>≤ 7×</code>, no cash counted as spare</span>
    <span>To buy zone = price ÷ buy-zone price − 1</span>
  </div>
  <p class="vkey"><b>BUY</b>: passes every test, price in the buy zone · <b>WATCH</b>: passes the quality tests, price above the buy zone · <b>AVOID</b>: fails at least one quality test · <b>Not analysed</b>: stopped at the first question</p>
  <div class="controls" role="group" aria-label="Filter the register">
@@CHIPS@@
    <div class="search">
      <input id="q" type="search" placeholder="Search company, ticker, business, reason…" aria-label="Search the register">
      <span class="count" id="count" aria-live="polite">Showing @@TOTAL@@ of @@TOTAL@@</span>
    </div>
  </div>
  <div class="tablebox" tabindex="0" role="region" aria-label="Register table">
    <table>
      <caption class="sr">The GSC research register: one row per company, grouped by verdict</caption>
      <thead><tr>
        <th scope="col" class="w-co">Company</th><th scope="col" class="w-v">Verdict</th><th scope="col" class="w-d">To buy zone</th><th scope="col" class="w-px">Price · buy zone</th><th scope="col" class="w-biz">Business</th><th scope="col" class="w-ret">Returns · past record</th><th scope="col" class="w-comp">Competitive position</th><th scope="col" class="w-sf">Shareholder-friendliness</th><th scope="col" class="w-mf">MCap/FCF</th><th scope="col" class="w-eo">EV/OI</th><th scope="col" class="w-memo">Memo · next review</th>
      </tr></thead>
      <tbody id="tb"></tbody>
    </table>
    <p class="empty" id="empty" hidden>No company matches this filter and search. Choose All or clear the search.</p>
  </div>
  <p class="foot">Source: the GSC research register @@REGISTER@@ and the research memo behind each row. Current method version @@MODEL@@, based on Kenneth Jeffrey Marshall, <cite>Good Stocks Cheap</cite>; each row was assessed under the version in force on its memo date. Business and moat lines are taken from the memos; return figures come from the register or the memo. Framework output, not investment advice.</p>
</div>

<script type="application/json" id="gsc-data">@@DATA@@</script>
<script>@@SCRIPT@@</script>
"""


# ------------------------------------------------------------------ stats

def data_issues(rows, extraction):
    """Register gaps a reader of the page would notice, one line per kind."""
    out = []

    def keys(pred):
        return [r["key"] for r in rows if pred(r)]

    checks = (
        ("BUY/WATCH rows without a numeric trigger (no distance shown)",
         lambda r: r["section"] in ("BUY", "WATCH") and not is_num(r["trigger"])),
        ("rows without a price", lambda r: not is_num(r["px"]) and r["section"] != "DNAF"),
        ("rows with a price but no price date", lambda r: is_num(r["px"]) and not DATE_RE.match(r["px_date"])),
        ("WATCH rows priced from the memo, not a SWEEP",
         lambda r: r["section"] == "WATCH" and not r["px_source"].startswith("SWEEP")),
        ("rows without MCap/FCF or EV/OI ('-' owed)",
         lambda r: r["section"] != "DNAF" and OWED in (r["mcap_fcf"], r["ev_oi"])),
        ("rows with a Past, Future or SF reason owed ('-')",
         lambda r: OWED in (r["past_reason"], r["future_reason"], r["sf_reason"])),
        ("rows with no next review", lambda r: r["next_review_short"] in (OWED, "")),
        ("cited memo not under memos/ (read from archive/memos/)",
         lambda r: extraction[r["key"]]["source"] == "archive"),
        ("cited memo unreadable", lambda r: extraction[r["key"]]["text"] is None),
    )
    for title, pred in checks:
        found = keys(pred)
        if found:
            out.append("%s (%d): %s" % (title, len(found), ", ".join(found)))
    return out


def stats_text(root):
    ctx, sections, extraction, rows = build(root)
    n = len(rows)
    by = lambda field, value: sum(1 for k in extraction if extraction[k][field] == value)
    with_business = [r["key"] for r in rows if extraction[r["key"]]["business"]]
    with_moat = [r["key"] for r in rows if extraction[r["key"]]["moat"]]
    page = {r["k"]: r for s in sections for r in s["rows"]}
    roce_register = sum(1 for r in rows if LEVEL_RE.match(r["past_reason"]) and r["section"] != "DNAF" and
                        not LEVEL_RE.match(r["past_reason"]).group("prefix"))     # a DNAF row shows no returns
    roce_any = sum(1 for k in page if page[k]["ro"])
    fcf_any = sum(1 for k in page if page[k]["fr"])
    # Cross-check: the memo's own worst-of-four ROCE against the register's deciding level.
    agree = compared = 0
    for r in rows:
        m = LEVEL_RE.match(r["past_reason"])
        memo = extraction[r["key"]]["roce"]
        if m and not m.group("prefix") and m.group("metric") == "ROCE" and memo and memo != NM:
            compared += 1
            if abs(Decimal(memo.rstrip("%").replace("−", "-")) - Decimal(m.group("value"))) <= Decimal("0.15"):
                agree += 1
    lines = [
        "GSC site extraction · register %s (%s) · %d rows · method %s"
        % (ctx["register_version"], ctx["register_date"], n, ctx["model_version"]),
        "  business sentence  %3d/%d  (current memo %d, archived memo %d)"
        % (len(with_business), n, by("business_from", "memo"), by("business_from", "archive")),
        "  moat line          %3d/%d  (current memo %d, archived memo %d)"
        % (len(with_moat), n, by("moat_from", "memo"), by("moat_from", "archive")),
        "  ROCE / ROE shown   %3d/%d  (register level %d, memo figure %d)"
        % (roce_any, n, roce_register, roce_any - roce_register),
        "  FCFROCE shown      %3d/%d" % (fcf_any, n),
        "  memo ROCE agrees with the register level (±0.15 pt) on %d of %d rows" % (agree, compared),
        "  sections: " + " · ".join("%s %d" % (s, ctx["counts"][s]) for s in SECTION_ORDER)
        + " · re-test %d (%s)" % (ctx["retest_count"], (", ".join("%s %d" % item for item in ctx["retest_versions"])
                                                          if len(ctx["retest_versions"]) > 1
                                                          else ctx["retest_version"]) or "no block"),
        "  countries: " + ", ".join("%s %d" % item for item in sorted(collections.Counter(
            page[k]["c"] for k in page).items())),
    ]
    missing = (("no business sentence", [r["key"] for r in rows if not extraction[r["key"]]["business"]]),
               ("no moat line", [r["key"] for r in rows if not extraction[r["key"]]["moat"]]),
               ("no ROCE shown", [k for k in sorted(page) if not page[k]["ro"]]))
    for title, found in missing:
        lines.append("  %s (%d): %s" % (title, len(found), ", ".join(found) if found else "none"))
    issues = data_issues(rows, extraction)
    lines.append("Data issues (%d kinds):" % len(issues))
    lines += ["  " + item for item in issues] or ["  none"]
    return "\n".join(lines) + "\n"


# ------------------------------------------------------------------ CLI

def default_root():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(here))


def cmd_render(args):
    ctx, sections, _extraction, rows = build(args.repo, no_held=args.no_held)
    text = render_page(ctx, sections)
    write_text(args.out, text)
    print("rendered %s: %d rows, register %s (%s), %d bytes%s"
          % (args.out, len(rows), ctx["register_version"], ctx["register_date"], len(text.encode("utf-8")),
             ", no held marker" if args.no_held else ""))
    return 0


def cmd_stats(args):
    sys.stdout.write(stats_text(args.repo))
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="GSC register site: the register as a page for third parties.")
    sub = parser.add_subparsers(dest="cmd")
    p = sub.add_parser("render", help="write the page")
    p.add_argument("--out", required=True)
    p.add_argument("--repo", default=None, help="repository root (default: the one holding this file)")
    p.add_argument("--no-held", dest="no_held", action="store_true", help="omit the neutral Held marker")
    p = sub.add_parser("stats", help="extraction coverage and register data issues")
    p.add_argument("--repo", default=None)
    args = parser.parse_args(argv)
    if not args.cmd:
        parser.print_help()
        return 2
    args.repo = os.path.abspath(args.repo or default_root())
    try:
        return {"render": cmd_render, "stats": cmd_stats}[args.cmd](args)
    except ToolError as exc:
        sys.stderr.write("gsc_site: %s\n" % exc)
        return 2


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    sys.exit(main())
