#!/usr/bin/env python3
"""GSC weekly report tool v1.1 (MODEL v4.6.1, sections 7.4 and 8.7 items 11-12; the WEEKLY job; v1.1 for MODEL v4.8.0).

One report a week of what the system did and what waits for Jakub, in place of the retired morning
digest and the retired per-event notifications. It renders eleven flat JSON datasets for the private
weekly page (the weekly_page config entry); only the WEEKLY routine publishes them. Generated, never
committed. The report recommends nothing: zones, flags and distances are framework arithmetic.

Subcommands (Python 3.11+, standard library only; exit 0 ok, 1 lint or check failed, 2 bad input):

  window --at ISO [--meta-at ISO|-] [--meta-by TEXT|-]
        Prints one JSON object: since and until (the seven Prague days ending at the most recent
        Sunday 08:30 Europe/Prague at or before --at, computed in local time, so a week with a DST
        change lasts 167 or 169 hours and every catch-up of the same week prints the same window),
        period (its label), details_since (since minus 14 days, UTC, the GitHub time format) and
        run (--at). With --meta-at and --meta-by (the weekly page's datasets/meta 'updated' fields,
        '-' when missing; the routines pass 'other' for a writer that is not the routine and '-' for an
        at that is not an ISO time, never the raw text, which the guard hook refuses) it adds published: true when by is 'GSC WEEKLY routine' and at lies
        between until and five minutes after --at (a stamp after the run, such as a mistyped run
        time, never counts: it would silence every later week; the next run overwrites it);
        meta_ok: true when at is an ISO time and by is given (a stamp INTAKE could read); and alarm
        (INTAKE's weekly watchdog, MODEL v4.8.0): true only when the week is not published and --at
        is on the Prague day after until's (the Monday) at or after 06:00 Prague, so one INTAKE run
        a week can raise it (the Saturday sprint and the Tuesday-to-Sunday runs never do).

  render --repo-dir DIR --ref REF --since ISO --until ISO --fetch-dir DIR [--health-json FILE]
         --out-dir DIR [--out-md FILE] [--out-json FILE] [--allow-stale-ref]
        Offline. Reads git (log, ls-tree, show, cat-file; read only), the files at REF, the GitHub
        pages the routine fetched into --fetch-dir and the optional schedule health; it never talks
        to GitHub or the network itself. A shallow repository is refused first (exit 2, 'shallow
        clone: run git fetch --unshallow origin main …'): the report reads the ref's whole history. Writes one dataset file per dataset id (DATASET_IDS) into
        --out-dir, summary.json included (the tool's own deterministic sentences), and
        notification.txt (the one-line WEEKLY notification). --out-md and --out-json add a readable
        report and a full JSON dump for attended checks. Refuses (exit 2) an output inside the
        repository, a stale ref (a PR merged inside the window after the ref's last commit whose
        merge commit the ref lacks) unless --allow-stale-ref, bad fetch pages, and an incomplete
        fetch: a PR merged in [since - 7 d, until) without its pull_{n}.json, or the needs-Jakub
        issue listed without a comments page.
        --fetch-dir holds the raw GitHub pages, read as data:
          pulls_{p}.json     pages of pulls?state=all (required, at least one);
          pull_{n}.json      pulls/{n} of each merged PR updated since details_since (merged_by);
          issues_{p}.json    pages of the issues the workflows opened (optional);
          comments_{p}.json  pages of the comments on the standing issue 'GSC - needs Jakub' since
                             details_since (required when issues_{p}.json lists that issue; an
                             empty page is fine: the hold reasons and workflow failures).
        --health-json: the routine list as WEEKLY read it (a JSON array of {name, job, cron,
        enabled, sprint, last_run}, or an object with such a 'triggers' array); an unreadable file
        is reported under Fix and never stops the render.

  lint-summary --datasets DIR --in FILE [--apply]
        Checks Claude's summary sentences: a JSON array of exactly six {order, kind, text}, one per
        slot of the page (SUMMARY_SLOTS: takeaway, decide, fix, fix, know, know); order 1..6; each
        text one line, at most 300 characters, no '#'; no advice words (buy or sell outside the
        framework's BUY and SELL-FLAG, a price target) and no private figure (PRIVATE_RE); every
        number in a text appears in the other ten datasets, and in the takeaway a number next to a
        headline phrase (memos merged, new WATCH, IN RANGE, NEAR, WATCH) equals its kpis value. Exit
        0 and, with --apply, replace summary.json with the sentences; otherwise exit 1 and leave
        summary.json (the tool's own) untouched.

  dash-writes --datasets DIR --blobs FILE --versions FILE --at ISO --out FILE
        Builds the one ArtifactData batch that repoints the page's datasets: one 'update' per
        dataset id, pinned with if_version, data {source: {kind 'file', url, name '{id}.json',
        format 'json'}, updated: {at, by 'GSC WEEKLY routine'}}, meta last. --blobs maps each id to
        its uploaded asset url ('/_blob/' plus 32 lower-case hex digits, all distinct); --versions
        maps each id to the dataset document's current version (a positive integer); --at is the
        run start, never more than five minutes after the clock. Writes --out and prints the array.

Window and states. The window is [since, until): a commit or PR event belongs to it when
since <= time < until. The report date is the Prague date of (until - 1 s); every Px age and
'days since' counts to that date, never to the wall clock. The start state is the last
first-parent commit before since, the end state the last one before until.

Pending overlay. Every queue/rows/*.md row file on the ref is merged and not yet applied by INTAKE.
Each ANALYSE/REVIEW row whose memo is the key's current memo marks its register row 'pending:
VERDICT (memo DATE)', the verdict read from the memo's front matter (memo wins). Headline counts
show register and after-pending values; the WATCH re-test count is on the register basis, with the
after-pending figure in its note.

Retired grounds. RETIRED_GATE0_GROUNDS encodes the Gate-0 DNAF grounds MODEL v4.6.0 retired; a
DNAF memo below that version whose section-1 ground matches is flagged 'retired ground - re-run
owed, not a live verdict'. Start, end and prior figures are all read with the lens of the MODEL
live at the end of the window. A DNAF row whose key has an open item for a delisting awaiting
retirement is classed 'awaiting RETIRED'. DNAF not live = retired grounds + awaiting RETIRED.

Attention lists. Decide (only Jakub can act: held SELL-FLAGs without a logged decision, open items
that ask for his call, those over the 7-entry cap included, routine PRs held for his merge, every
SWEEP held-zone change and every BUY), Fix (the system: stopped, blocked, INCOMPLETE and abandoned
runs, stale prices, schedule failures, workflow failures, finished routine PRs waiting) and Know
(the rest, including a held SELL-FLAG whose open item logs his HOLD decision or a deferral), each
ranked by severity, then oldest first.

Held zones. A held zone changes when its zone word (ADD, HOLD, SELL-FLAG) changes; a relabelled
reason is no change. Before register.csv existed (v307) the register gives no start zones.

Privacy. Every text field of the datasets passes scrub_private, which replaces a price after '@',
average cost, cost basis, position size and core numbers with '[private]': open items and PR
outcomes are copied as written.

Conventions. Times print in Europe/Prague (EU rule: UTC+2 from the last Sunday of March 01:00 UTC
to the last Sunday of October 01:00 UTC, else UTC+1; no tz database needed). PRs print as 'PR n',
never with a hash sign. The report is private to Jakub: it may carry held names, zones and open
items, never average cost, position size or core numbers. Every figure is computed from git, the
files at the ref, the fetched pages or the health input; one that cannot be derived is null.
A re-render of the same inputs is byte-identical except for meta.generated_at.

v1.1 (MODEL v4.8.0). window prints meta_ok and alarm for INTAKE's weekly watchdog; render refuses a shallow
clone first; the schedule health reads each routine's last-run duration and lists a likely no-op run under Fix
(a run that SUCCEEDED in under 120 s with no PR of its job from its fire to 10 min after it finished; for SEED and
SWEEP also none open at the fire; never WEEKLY); the re-test blocks are read by version
('▶ Method re-tests vX.Y.Z', any version), and a line marked ' — partial {date}' counts open and is listed.

Helpers come from gsc_register.py (CSV and front-matter reading, status_hint for IN RANGE / NEAR
/ FAR under MODEL section 8.3 step 3, section_for, review_last_day, batch_show) and gsc_site.py
(listing countries, memo sections, the business sentence, distance), the sibling tools in the
same folder, imported read-only. This file names no framework path and no GitHub client on
purpose: the routine guard hook scans the code of every script a routine runs.
"""
import argparse
import collections
import datetime
import json
import os
import re
import statistics
import subprocess
import sys
from decimal import Decimal, ROUND_HALF_UP

sys.dont_write_bytecode = True

TOOL_VERSION = "1.1"
TOOL = "gsc_weekly.py v" + TOOL_VERSION
UTC = datetime.timezone.utc
ONE_SECOND = datetime.timedelta(seconds=1)
DAYS = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
MODEL_PATH = "/".join(("model", "MODEL.md"))      # read only
MODEL_PATHS = (MODEL_PATH, "instructions/MODEL.md")   # the live MODEL's path, then its pre-v4.2.1 path
JOBS = ("ANALYSE", "REVIEW", "SWEEP", "SEED", "INTAKE")      # the jobs that open PRs
HEALTH_JOBS = JOBS + ("WEEKLY",)                             # the jobs a schedule-health entry may name
ANALYTIC_JOBS = ("ANALYSE", "REVIEW")
VERDICTS = ("BUY", "WATCH", "AVOID", "DNAF")
SHORTLIST_N = 10
GLANCE_DECIDE = 5           # 'At a glance' shows at most this many Decide items ...
GLANCE_FIX = 3              # ... and this many Fix items: 2 headline lines + 2 list heads + 8 = 12 lines
OPEN_PR_AGE = datetime.timedelta(hours=24)       # INTAKE's stall watchdog: a finished routine PR older than this
STALL_COUNT = 15                                 # ... and the count above which it records a stall
RUNNING_AGE = datetime.timedelta(hours=6)        # INTAKE closes a [running] PR older than this as abandoned
RELIABLE_PX_DAYS = 7        # a shortlist row is 'reliable' only with a Px at most this old at the report date
# This report's own routine-health thresholds: SWEEP_STALE (SWEEP runs weekly), ROUTINE_GAP, and the
# register lag (row files merged more than ROWS_WAITING ago while no INTAKE merged for INTAKE_STALL).
SWEEP_STALE = datetime.timedelta(days=8)
ROUTINE_GAP = datetime.timedelta(hours=48)
INTAKE_STALL = datetime.timedelta(hours=30)
ROWS_WAITING = datetime.timedelta(hours=6)
USAGE_LIMIT = "USAGE_LIMIT_REACHED"
# Likely no-op runs (MODEL v4.8.0): a routine whose last run SUCCEEDED in under NOOP_SECONDS and opened no PR of
# its job from its fire to NOOP_GRACE after it finished (a session without the repository ends this way). The
# jobs that open a PR on every working run; WEEKLY opens none and INTAKE's weekly watchdog covers it. SEED and
# SWEEP stop at once, legitimately, while a PR of their job is still open at the fire.
NOOP_SECONDS = 120
NOOP_GRACE = datetime.timedelta(minutes=10)
NOOP_JOBS = ("ANALYSE", "REVIEW", "SWEEP", "INTAKE", "SEED")
NOOP_OPEN_PR_JOBS = ("SWEEP", "SEED")
SEVERITIES = ("high", "medium", "low")
# gsc-automerge's first merge (PR 92, 2026-10-08 00:59 Prague): a routine PR merged by Jakub that was
# opened before it waited under the pre-auto-merge regime, so the held-PR wait compares only PRs
# opened at or after this instant.
AUTOMERGE_START = datetime.datetime(2026, 10, 7, 22, 59, 46, tzinfo=UTC)
# A single commit that adds at least this many memos is an import (the 2026-W27 seed), not research.
IMPORT_MIN_MEMOS = 20

# ------------------------------------------------------------------ the weekly page (MODEL section 7.4)
WEEKLY_PAGE_URL = "https://claude.ai/artifact/6L264JT8pg5vuia9dUrcuj"
DATASET_IDS = ("summary", "meta", "kpis", "attention", "shortlist", "changes", "weekly", "pipeline", "coverage",
               "backlog", "held")
WEEKLY_BY = "GSC WEEKLY routine"
BLOB_URL_RE = re.compile(r"/_blob/[0-9a-f]{32}")             # used with fullmatch
ISO_TS_RE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2}(?:\.\d{1,6})?)?(?:Z|[+-]\d{2}:\d{2})")
NOTICE_FILE = "notification.txt"
NOTICE_MAX = 200
# The page's summary card shows six sentences in fixed slots: the takeaway, one Decide, two Fix, two Know.
SUMMARY_SLOTS = ("takeaway", "decide", "fix", "fix", "know", "know")
SUMMARY_KINDS = ("takeaway", "decide", "fix", "know")
SUMMARY_MAX_CHARS = 300
# The needs-Jakub issue the workflows keep, and their comment forms there (MODEL section 8.7 items 10-11):
# 'PR n held - reason' (an @mention prefix before the v4.8.0 workflow release) and '<workflow> ... failed: ...'.
NEEDS_TITLE = "GSC - needs Jakub"
HOLD_COMMENT_RE = re.compile(r"^(?:@[\w-]+\s+)?PR (?P<pr>\d+) held - (?P<reason>[^\n]*)")
FAIL_COMMENT_RE = re.compile(r"^(?:@[\w-]+\s+)?(?P<what>gsc-(?:automerge|notify)\b[^\n:]*failed): (?P<why>[^\n]*)")

# ------------------------------------------------------------------ retired Gate-0 grounds
# MODEL v4.6.0 (change log 'v4.6.0 CHANGE LOG (2026-10-15)', G2 'Retired:' list; section 2 Gate 0:
# 'Reporting structure is never a ground') retired these Gate-0 DNAF grounds:
#   - the irreducible-unit test (two sub-businesses each >= 10% of a unit differing in industry or
#     paying customer), i.e. the v4.5.x one-level decomposition, with 'a group never bypasses the
#     one-level decomposition';
#   - its J13 limb (sub-businesses named by the filer without their shares);
#   - the categorical material-'Other' fail (and the v4.5.1 sub-business definitions);
#   - the holdings-cycle fail;
#   - the R4 too-hard pile (R4(a)-(c): a bank or insurer outside FI, a group with a material
#     non-captive insurer or deposit-funded bank, a company mostly of unlisted stakes).
# The only Gate-0 FAIL left is P30 (incomprehension or obfuscation of more than half of revenue).
# A DNAF memo written under a MODEL below RETIRED_GATE0_VERSION whose section-1 ground matches one
# of the patterns is flagged once that version is live: 'retired ground - re-run owed, not a live
# verdict' (its re-run is listed in queue/TODO.md '▶ Method re-tests v4.6.0').
RETIRED_GATE0_VERSION = "v4.6.0"
RETIRED_GATE0_GROUNDS = (
    ("irreducible unit (one-level decomposition)",
     re.compile(r"(?i)\bone-level decomposition\b|\birreducible\b")),
    ("J13 limb (named without shares)",
     re.compile(r"(?i)\bwithout (?:their |the |printed )?shares\b|\bshares not (?:given|printed|shown|disclosed|stated)\b"
                r"|\bJ13\b")),
    ("material Other",
     re.compile(r"(?i)\bmaterial\s+[\"“”'‘’]?other\b|\bmaterial residual\b")),
    ("R4 too-hard pile",
     re.compile(r"(?i)\btoo[ -]hard\b|\bR4\s*\(\s*[a-c]\s*\)")),
    ("holdings cycle",
     re.compile(r"(?i)\bholdings?[ -]cycle\b|\bcycle of (?:cross-)?holdings\b|\bcross-holdings?\b")),
)
RETIRED_FLAG = "retired ground — re-run owed, not a live verdict"

# Title grammar (the routine README, section 1).
PR_NUM_SUFFIX_RE = re.compile(r"\s*\(#(\d+)\)\s*$")
PR_TAG_RE = re.compile(r"\s*\[(running|abandoned|superseded|fixing)\]\s*$")
REVERT_RE = re.compile(r'^Revert "(?P<title>.*)"\s*$')
MODEL_TITLE_RE = re.compile(r"^GSC: MODEL (?P<version>v\d+\.\d+\.\d+)\b")
TITLE_HEAD_RE = re.compile(r"^(?P<held>HELD · )?GSC (?P<job>ANALYSE|REVIEW|SEED|SWEEP|INTAKE)"
                           r"(?: (?P<key>[A-Za-z0-9._-]+))? (?P<date>\d{4}-\d{2}-\d{2})(?P<rest>.*)$")
VERDICT_OUT_RE = re.compile(r"^(?P<verdict>BUY|WATCH|AVOID|DNAF)(?: \((?P<gates>[^)]*)\))?(?:; (?P<moved>.*))?$")
WAS_RE = re.compile(r"^was (?P<old>BUY|WATCH|AVOID|DNAF)\b")
INCOMPLETE_RE = re.compile(r"^INCOMPLETE \((?P<gap>.*)\)$")
STOP_RE = re.compile(r"^(?P<kind>stopped|blocked): (?P<reason>.*)$")
SWEEP_OUT_RE = re.compile(r"^(?P<priced>\d+)/(?P<total>\d+) priced\b")
INTAKE_OUT_RE = re.compile(r"^(?:register v(?P<version>\d+)|no register change) \((?P<rows>\d+) rows?\)")

MEMO_NAME_RE = re.compile(r"^(?P<key>[A-Za-z0-9._-]+)_(?P<date>\d{4}-\d{2}-\d{2})_GSC\.md$")
# A memo add in a commit whose subject reads like a re-key, rename, migration or RECONCILE, while
# the parent tree already holds a memo of the same key or date, is a move (MODEL section 7.1a).
MOVE_SUBJECT_RE = re.compile(r"(?i)\bre-?key|\brenam|\bmigrat|\bRECONCILE\b|\bdate correction\b")
EVIDENCE_INCOMPLETE_RE = re.compile(r"^queue/evidence/(?P<key>[A-Za-z0-9._-]+)_(?P<date>\d{4}-\d{2}-\d{2})"
                                    r"_INCOMPLETE\.md$")
SWEEP_ROW_RE = re.compile(r"^queue/rows/\d{4}-\d{2}-\d{2}_\d{4}_SWEEP\.md$")
VERSION_RE = re.compile(r"v?(\d+)\.(\d+)(?:\.(\d+))?")
WATCH_SPLIT_RE = re.compile(r"\bWATCH (\d+)\b")
DATE_IN_BRACKETS_RE = re.compile(r"\[([^\[\]]*?\d{4}-\d{2}-\d{2}[^\[\]]*)\]")
ISO_DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
OPEN_ITEM_RE = re.compile(r"^- \*\*(?P<head>.+?)\*\*\s*(?P<body>.*)$")
USER_CALL_RE = re.compile(r"(?i)\buser (?:call|decision)\b|\bdecision (?:pending|deferred)\b|\battended\b")

# Report regions of a listing country (the key's suffix; a bare key is a US line): this report's
# own grouping, a definition and not data. Any country not named here is 'Other'.
REPORT_REGIONS = ("North America", "UK", "Western Europe ex-UK", "Nordics", "CEE", "Japan", "Greater China",
                  "Korea", "Other")
REGION_OF_COUNTRY = {
    "US": "North America", "Canada": "North America",
    "UK": "UK",
    "Ireland": "Western Europe ex-UK", "France": "Western Europe ex-UK", "Netherlands": "Western Europe ex-UK",
    "Belgium": "Western Europe ex-UK", "Portugal": "Western Europe ex-UK", "Italy": "Western Europe ex-UK",
    "Spain": "Western Europe ex-UK", "Germany": "Western Europe ex-UK", "Austria": "Western Europe ex-UK",
    "Switzerland": "Western Europe ex-UK", "Greece": "Western Europe ex-UK",
    "Sweden": "Nordics", "Denmark": "Nordics", "Norway": "Nordics", "Finland": "Nordics", "Iceland": "Nordics",
    "Poland": "CEE", "Czechia": "CEE", "Hungary": "CEE", "Romania": "CEE", "Estonia": "CEE", "Latvia": "CEE",
    "Lithuania": "CEE",
    "Japan": "Japan",
    "China": "Greater China", "Hong Kong": "Greater China", "Taiwan": "Greater China",
    "South Korea": "Korea",
}
SECTIONS = ("BUY", "WATCH", "AVOID-1", "AVOID-2", "DNAF", "RETIRED")

reg = None      # gsc_register.py (the sibling register tool), loaded by load_tools()
site = None     # gsc_site.py (the sibling register page generator)


class ToolError(Exception):
    """Bad input; the message is printed and the tool exits 2."""


def load_tools(repo_dir):
    """Import gsc_register and gsc_site from the repository's tools folder (read-only use)."""
    global reg, site
    if reg is not None and site is not None:
        return
    tools = os.path.join(os.path.abspath(repo_dir), "routines", "tools")
    if not os.path.isfile(os.path.join(tools, "gsc_register.py")):
        raise ToolError("gsc_register.py not found in %s" % tools)
    if tools not in sys.path:
        sys.path.insert(0, tools)
    import gsc_register   # noqa: E402
    import gsc_site       # noqa: E402
    reg, site = gsc_register, gsc_site


# ------------------------------------------------------------------ time

def last_sunday(year, month):
    day = datetime.date(year, month, 31)
    return day - datetime.timedelta(days=(day.weekday() + 1) % 7)


def prague_offset(moment):
    """UTC offset of Europe/Prague at an aware instant (EU summer-time rule)."""
    utc = moment.astimezone(UTC)
    start = datetime.datetime.combine(last_sunday(utc.year, 3), datetime.time(1, 0), UTC)
    end = datetime.datetime.combine(last_sunday(utc.year, 10), datetime.time(1, 0), UTC)
    return datetime.timedelta(hours=2 if start <= utc < end else 1)


def to_prague(moment):
    utc = moment.astimezone(UTC)
    return utc.astimezone(datetime.timezone(prague_offset(utc)))


def prague_date(moment):
    return to_prague(moment).date()


def local_to_utc(naive, tz="Europe/Prague"):
    """The UTC instant of a naive wall-clock time in tz (Europe/Prague or UTC). In the autumn
    repeated hour the first (summer-time) instant is taken; a time in the spring gap gives None."""
    if tz != "Europe/Prague":
        return naive.replace(tzinfo=UTC)
    for hrs in (2, 1):
        off = datetime.timedelta(hours=hrs)
        candidate = (naive - off).replace(tzinfo=UTC)
        if prague_offset(candidate) == off:
            return candidate
    return None


def parse_when(text):
    """An aware UTC datetime from ISO text ('Z' or an offset; a naive time is Prague local)."""
    value = (text or "").strip()
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    try:
        moment = datetime.datetime.fromisoformat(value)
    except ValueError:
        raise ToolError("not an ISO time: %r (give an explicit time; 'now' is not accepted)" % text)
    if moment.tzinfo is None:
        found = local_to_utc(moment)
        return found if found is not None else (moment - datetime.timedelta(hours=1)).replace(tzinfo=UTC)
    return moment.astimezone(UTC)


def parse_gh_time(value):
    if not value:
        return None
    return parse_when(value)


def report_date_of(until):
    """The report date: the Prague date of (until - 1 s)."""
    return prague_date(until - ONE_SECOND)


def fmt_when(moment, year=False):
    """'Mon 19 Oct 23:15' in Prague ('Mon 19 Oct 2026 23:15' with year); 'n/a' for None."""
    if moment is None:
        return "n/a"
    p = to_prague(moment)
    return "%s %d %s%s %02d:%02d" % (DAYS[p.weekday()], p.day, MONTHS[p.month - 1],
                                     (" %d" % p.year) if year else "", p.hour, p.minute)


def fmt_day(day, year=False):
    if day is None:
        return "n/a"
    return "%s %d %s%s" % (DAYS[day.weekday()], day.day, MONTHS[day.month - 1], (" %d" % day.year) if year else "")


def period_label(since, until):
    """'Mon 12 Oct – Mon 19 Oct 2026': the first and the last Prague day of [since, until)."""
    first, last = prague_date(since), report_date_of(until)
    if first == last:
        return fmt_day(first, True)
    if first.year == last.year:
        return "%s – %s" % (fmt_day(first), fmt_day(last, True))
    return "%s – %s" % (fmt_day(first, True), fmt_day(last, True))


def iso_week_label(since, until):
    """'2026-W42' when [since, until) is exactly one ISO week in Prague (Monday 00:00 to the next
    Monday 00:00); None otherwise."""
    p, q = to_prague(since), to_prague(until)
    midnight = datetime.time(0, 0)
    if p.weekday() == 0 and p.time() == midnight and q.time() == midnight \
            and q.date() == p.date() + datetime.timedelta(days=7):
        year, week, _ = p.date().isocalendar()
        return "%d-W%02d" % (year, week)
    return None


def iso_week(day):
    year, week, _ = day.isocalendar()
    return "%d-W%02d" % (year, week)


def iso_prague(moment):
    return to_prague(moment).isoformat() if moment is not None else None


def fmt_span(delta):
    """'7 d 23 h 41 min' style; minutes only below one hour."""
    total = int(delta.total_seconds() // 60)
    days, rem = divmod(total, 1440)
    hrs, minutes = divmod(rem, 60)
    parts = []
    if days:
        parts.append("%d d" % days)
    if hrs or days:
        parts.append("%d h" % hrs)
    parts.append("%d min" % minutes)
    return " ".join(parts)


def hours(delta):
    return (Decimal(int(delta.total_seconds())) / Decimal(3600)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)


def q1(value):
    """A Decimal rounded half up to one decimal; None stays None."""
    if value is None:
        return None
    return Decimal(value).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)


def median1(values):
    values = [Decimal(v) for v in values if v is not None]
    if not values:
        return None
    return q1(statistics.median(values))


# ------------------------------------------------------------------ cron

CRON_LIMITS = ((0, 59), (0, 23), (1, 31), (1, 12), (0, 7))
CRON_TZS = ("Europe/Prague", "UTC", "Etc/UTC")


def cron_field(text, lo, hi):
    """The set of values a cron field names: '*', 'n', 'a-b', lists of those, each with an
    optional '/step'."""
    values = set()
    for part in text.split(","):
        step = 1
        if "/" in part:
            part, raw = part.split("/", 1)
            if not raw.isdigit() or int(raw) < 1:
                raise ToolError("bad cron step %r" % text)
            step = int(raw)
        if part == "*":
            a, b = lo, hi
        elif re.match(r"^\d+-\d+$", part):
            a, b = (int(x) for x in part.split("-"))
        elif part.isdigit():
            a = int(part)
            b = hi if step > 1 else a
        else:
            raise ToolError("bad cron field %r" % text)
        if not lo <= a <= b <= hi:
            raise ToolError("cron field %r out of range %d-%d" % (text, lo, hi))
        values.update(range(a, b + 1, step))
    return values


def parse_cron(expr):
    """{tz, minute, hour, dom, month, dow, dom_restricted, dow_restricted} of a 5-field cron
    expression with an optional 'CRON_TZ=Zone ' prefix (Europe/Prague or UTC; default UTC).
    DOW 0 and 7 are Sunday."""
    text, tz = (expr or "").strip(), "UTC"
    m = re.match(r"^CRON_TZ=(\S+)\s+(.*)$", text)
    if m:
        tz, text = m.group(1), m.group(2).strip()
    if tz not in CRON_TZS:
        raise ToolError("cron time zone %r not supported (Europe/Prague or UTC)" % tz)
    fields = text.split()
    if len(fields) != 5:
        raise ToolError("cron %r: five fields expected" % expr)
    sets = [cron_field(f, lo, hi) for f, (lo, hi) in zip(fields, CRON_LIMITS)]
    return {"tz": "Europe/Prague" if tz == "Europe/Prague" else "UTC", "minute": sets[0], "hour": sets[1],
            "dom": sets[2], "month": sets[3], "dow": {d % 7 for d in sets[4]},
            "dom_restricted": not fields[2].startswith("*"), "dow_restricted": not fields[4].startswith("*")}


def cron_day_matches(spec, day):
    dom_ok = day.day in spec["dom"]
    dow_ok = (day.weekday() + 1) % 7 in spec["dow"]
    if spec["dom_restricted"] and spec["dow_restricted"]:
        return dom_ok or dow_ok          # Vixie cron: both restricted -> either
    return dom_ok and dow_ok


def cron_fires(expr, since, until):
    """Sorted UTC instants in [since, until) at which a cron expression fires, wall-clock times
    read in its CRON_TZ. A Prague time in the spring-forward gap does not fire; one in the
    autumn repeated hour fires once (the first instant)."""
    spec = parse_cron(expr)
    if spec["tz"] == "Europe/Prague":
        first, last = prague_date(since), prague_date(until)
    else:
        first, last = since.astimezone(UTC).date(), until.astimezone(UTC).date()
    fires, day = [], first
    while day <= last:
        if day.month in spec["month"] and cron_day_matches(spec, day):
            for hour in sorted(spec["hour"]):
                for minute in sorted(spec["minute"]):
                    moment = local_to_utc(datetime.datetime.combine(day, datetime.time(hour, minute)), spec["tz"])
                    if moment is not None and since <= moment < until:
                        fires.append(moment)
        day += datetime.timedelta(days=1)
    return sorted(fires)


# ------------------------------------------------------------------ titles and classification

def norm_key(key):
    """A key for matching across title and memo spellings ('CCL.B.TO' ~ 'CCL-B.TO')."""
    return (key or "").upper().replace("-", ".")


def version_tuple(text):
    m = VERSION_RE.search(text or "")
    if not m:
        return None
    return int(m.group(1)), int(m.group(2)), int(m.group(3) or 0)


def classify_outcome(job, outcome):
    """{kind, verdict, gates, moved, was, gap, reason, priced, total, register_version, rows} of a
    finished title's outcome (the routine README, section 1); kind '' for no outcome."""
    out = {"kind": "", "verdict": "", "gates": "", "moved": "", "was": "", "gap": "", "reason": "",
           "priced": "", "total": "", "register_version": "", "rows": ""}
    text = (outcome or "").strip()
    if not text:
        return out
    m = STOP_RE.match(text)
    if m:
        out.update(kind=m.group("kind"), reason=m.group("reason"))
        return out
    m = INCOMPLETE_RE.match(text)
    if m:
        out.update(kind="incomplete", gap=m.group("gap"))
        return out
    if job in ("ANALYSE", "REVIEW"):
        if text == "prior found (REVIEW)":
            out["kind"] = "prior"
            return out
        if text == "queue exhausted":
            out["kind"] = "exhausted"
            return out
        m = VERDICT_OUT_RE.match(text)
        if m:
            out.update(kind="verdict", verdict=m.group("verdict"), gates=m.group("gates") or "",
                       moved=m.group("moved") or "")
            w = WAS_RE.match(out["moved"])
            out["was"] = w.group("old") if w else ""
            return out
    elif job == "SWEEP":
        m = SWEEP_OUT_RE.match(text)
        if m:
            out.update(kind="sweep", priced=m.group("priced"), total=m.group("total"))
            return out
    elif job == "INTAKE":
        m = INTAKE_OUT_RE.match(text)
        if m:
            out.update(kind="intake", register_version=("v" + m.group("version")) if m.group("version") else "",
                       rows=m.group("rows"))
            return out
    elif job == "SEED":
        out["kind"] = "seed"
        return out
    out["kind"] = "other"
    return out


def parse_title(title):
    """A PR title or squash-commit subject read by the routine README's section 1 grammar.
    job: a routine job word, 'attended' (title 'GSC: …'), 'revert' or '' (anything else);
    tag: running | abandoned | superseded | fixing | ''; pr: the '(#n)' suffix of a commit subject."""
    t = (title or "").strip()
    out = {"title": t, "pr": None, "tag": "", "held": False, "job": "", "key": "", "date": "", "outcome": "",
           "model_version": ""}
    out.update(classify_outcome("", ""))
    m = PR_NUM_SUFFIX_RE.search(t)
    if m:
        out["pr"] = int(m.group(1))
        t = t[:m.start()]
        out["title"] = t
    m = REVERT_RE.match(t)
    if m:
        out.update(job="revert", kind="revert", reason=m.group("title"))
        return out
    m = PR_TAG_RE.search(t)
    if m:
        out["tag"] = m.group(1)
        t = t[:m.start()]
    if t.startswith("GSC: "):
        mm = MODEL_TITLE_RE.match(t)
        out.update(job="attended", kind="model" if mm else "attended", outcome=t[5:].strip(),
                   model_version=mm.group("version") if mm else "")
        return out
    m = TITLE_HEAD_RE.match(t)
    if not m:
        out["kind"] = "other"
        return out
    out.update(held=bool(m.group("held")), job=m.group("job"), key=m.group("key") or "", date=m.group("date"))
    rest = m.group("rest")
    if rest.startswith(" — "):
        out["outcome"] = rest[3:].strip()
        out.update(classify_outcome(out["job"], out["outcome"]))
    elif rest.strip():
        out["kind"] = "other"
    return out


def is_routine(parsed):
    return parsed["job"] in JOBS


def held_for_jakub(parsed):
    """True when a routine title is one gsc-automerge holds for Jakub on its face (MODEL
    section 8.7 item 10): HELD prefix, a BUY, a REVIEW verdict change, stopped or blocked,
    QUEUE-SEED, or a [fixing] tag. The rest of the item-10 list needs the PR's files and checks."""
    if not is_routine(parsed):
        return False
    return bool(parsed["held"] or parsed["kind"] in ("stopped", "blocked") or parsed["tag"] == "fixing"
                or parsed["job"] == "SEED" or parsed["verdict"] == "BUY"
                or (parsed["job"] == "REVIEW" and parsed["was"]))


# ------------------------------------------------------------------ shortlist status and regions

def shortlist_status(row):
    """(status, distance) of a register row at its own Px through the register tool's
    status_hint (MODEL section 8.3 step 3: IN RANGE at or under the trigger only if MCap/FCF <= 8
    and EV/OI no-cash <= 7 hold where the core numbers establish them; NEAR within 10%; FAR
    beyond; 'n.m.' without a numeric Px and a positive trigger, distance None)."""
    status, dist = reg.status_hint(row, row.get("px", "-"))
    if dist is None:
        return reg.NM, None
    return status, dist


def listing_country(key):
    suffix = site.key_suffix(key)
    return site.SUFFIX_COUNTRY[suffix] if suffix else site.US_COUNTRY


def region_of(key):
    """(listing country, report region) of a key: the region of its listing line (the key's
    suffix; a bare key is a US line, whatever the issuer's domicile)."""
    country = listing_country(key)
    return country, REGION_OF_COUNTRY.get(country, "Other")


# ------------------------------------------------------------------ register diff

DIFF_FIELDS = ("section", "verdict", "past", "past_reason", "future", "future_reason", "sf", "sf_reason")


def grade_text(row, gate):
    grade = row.get(gate, "")
    why = row.get(gate + "_reason", "")
    if why in ("", "-", "n.m."):
        return grade or "-"
    return "%s (%s)" % (grade, why)


def register_diff(old_rows, new_rows):
    """{added, removed, changed, regraded} between two register.csv row lists."""
    old = {r["key"]: r for r in old_rows}
    new = {r["key"]: r for r in new_rows}
    added = [{"key": k, "company": new[k]["company"], "section": new[k]["section"]} for k in sorted(set(new) - set(old))]
    removed = [{"key": k, "company": old[k]["company"], "section": old[k]["section"]}
               for k in sorted(set(old) - set(new))]
    changed, regraded = [], []
    for k in sorted(set(old) & set(new)):
        a, b = old[k], new[k]
        entry = {"key": k, "company": b["company"], "from_section": a["section"], "to_section": b["section"],
                 "from_verdict": a["verdict"], "to_verdict": b["verdict"],
                 "from": {g: grade_text(a, g) for g in ("past", "future", "sf")},
                 "to": {g: grade_text(b, g) for g in ("past", "future", "sf")},
                 "from_memo": a.get("memo_date", ""), "to_memo": b.get("memo_date", "")}
        if a["section"] != b["section"] or a["verdict"] != b["verdict"]:
            changed.append(entry)
        elif any(a.get(f, "") != b.get(f, "") for f in DIFF_FIELDS):
            regraded.append(entry)
    return {"added": added, "removed": removed, "changed": changed, "regraded": regraded}


# ------------------------------------------------------------------ queue files

def queue_markers(text):
    """Counter of DRAFT_QUEUE line markers under '## Queue' (the file header's grammar)."""
    counts = collections.Counter()
    inside = False
    for line in (text or "").replace("\r\n", "\n").split("\n"):
        if line.startswith("## "):
            inside = line.strip() == "## Queue"
            continue
        if not inside or not line.startswith("- ["):
            continue
        token = line[2:5]
        rest = line[5:].lstrip()
        if token == "[ ]":
            counts["open"] += 1
        elif token == "[x]":
            if rest.startswith("prior"):
                counts["prior"] += 1
            elif rest.startswith("retired"):
                counts["retired"] += 1
            elif rest.startswith("no listed security"):
                counts["no listed security"] += 1
            else:
                counts["done"] += 1
        elif token == "[-]":
            counts["rejected"] += 1
        elif token == "[!]":
            counts["stalled" if rest.startswith("stalled") else ("incomplete" if rest.startswith("incomplete")
                                                                 else "other")] += 1
        else:
            counts["other"] += 1
    return counts


def todo_blocks(text):
    """[(heading, bullet lines)] of the queue/TODO.md '## ▶ …' head blocks, file order,
    'Routed by …' blocks left out. A bullet is a line that opens with '- '."""
    blocks, current = [], None
    for line in (text or "").replace("\r\n", "\n").split("\n"):
        if line.startswith("## "):
            title = line[3:].strip()
            if title.startswith("▶") and not title.startswith("▶ Routed"):
                current = (title, [])
                blocks.append(current)
            else:
                current = None
            continue
        if current is not None and line.startswith("- "):
            current[1].append(line)
    return blocks


def todo_block(text, prefix):
    """The bullets of the first head block whose title starts with prefix ([] if none)."""
    for title, bullets in todo_blocks(text):
        if title.startswith(prefix):
            return bullets
    return []


# The release re-test blocks, any version (v4.5.0, v4.6.0, v4.8.0 read first, …): '▶ Method re-tests vX.Y.Z'.
RETEST_BLOCK_RE = re.compile(r"^▶ Method re-tests (v\d+\.\d+\.\d+)\b")
RETEST_KEY_RE = re.compile(r"^-\s+`([A-Za-z0-9._-]+)`")
# A re-test line a run left part-done (MODEL v4.8.0 two-run resume): ' — partial {D}', optionally followed by
# ' (queue/evidence/{KEY}_{D}_INCOMPLETE.md)'. The line stays open: it counts as owed and is listed as partial.
RETEST_PARTIAL_RE = re.compile(r" — partial (?P<date>\d{4}-\d{2}-\d{2})(?: \((?P<evidence>[^()\s]+)\))?")


def retest_blocks(text):
    """[(heading, version label, bullets)] of the '▶ Method re-tests vX.Y.Z' blocks, file order."""
    out = []
    for title, bullets in todo_blocks(text):
        m = RETEST_BLOCK_RE.match(title)
        if m:
            out.append((title, m.group(1), bullets))
    return out


def retest_keys(text):
    """{block heading: [keys]} of the '▶ Method re-tests …' blocks (keys as their bullets open)."""
    out = collections.OrderedDict()
    for title, _version, bullets in retest_blocks(text):
        keys = []
        for line in bullets:
            m = RETEST_KEY_RE.match(line)
            if m and m.group(1) not in keys:
                keys.append(m.group(1))
        out[title] = keys
    return out


def retest_lines(text):
    """{block heading: bullet count} of the '▶ Method re-tests …' blocks (a partial line counts: it is open)."""
    return collections.OrderedDict((t, len(b)) for t, _v, b in retest_blocks(text))


def retest_partial(text):
    """{block heading: [(key, date, evidence path or None)]} of the re-test lines marked ' — partial {D}'."""
    out = collections.OrderedDict()
    for title, _version, bullets in retest_blocks(text):
        found = []
        for line in bullets:
            k, m = RETEST_KEY_RE.match(line), RETEST_PARTIAL_RE.search(line)
            if k and m:
                found.append((k.group(1), m.group("date"), m.group("evidence")))
        out[title] = found
    return out


USER_MARK_RE = re.compile(r"^\s*user,\s*(\d{4}-\d{2}-\d{2})")
# Jakub's logged decision on a held SELL-FLAG line: 'decision HOLD [user, 2026-10-20]', 'HOLD confirmed
# [user, 2026-10-20]'; a deferral: 'decision deferred to FY2026 results (~Mar 2027) [user, 2026-08-18]'.
HOLD_DECISION_RE = re.compile(r"\bHOLD\b[^\[\]]{0,40}?\[user,\s*(\d{4}-\d{2}-\d{2})\]")
DEFERRAL_RE = re.compile(r"(?i)\bdecision deferred\b\s*(?P<to>[^\[\];]*?)\s*\[user,\s*(?P<date>\d{4}-\d{2}-\d{2})\]")
# An open item over the 7-entry cap, routed below the head block (MODEL section 7.1):
# - `KEY` — open item (over the 7-entry cap of `▶ Open items (register)`, routed here by …): text
OVER_CAP_RE = re.compile(r"^- `(?P<key>[A-Za-z0-9._-]+)` — open item \(over the 7-entry cap\b.*?\):\s*(?P<body>.*)$")
AWAITING_RETIRED_RE = re.compile(r"(?i)\bawaiting retirement\b|\bretire\b")


def parse_open_item(line, since_default=None):
    """One open item ('▶ Open items (register)' bullet, or an over-cap line): {key, held, sell_flag,
    user_call, deferred, deferred_on, deferred_to, hold_on, retire, over_cap, since, head, text}.
    since: the first date of the last [...] group that holds a date and is not a '[user, date]'
    decision mark, else the first date of the first such group (the item's own date), else
    since_default (an over-cap line: the date of the block it was routed to).
    hold_on: the date of Jakub's last logged HOLD decision; deferred_on / deferred_to: his deferral."""
    over = OVER_CAP_RE.match(line)
    if over:
        head, body = over.group("key"), over.group("body")
        text = body if body.startswith(head) else "%s — %s" % (head, body)
    else:
        m = OPEN_ITEM_RE.match(line)
        head = m.group("head") if m else ""
        text = line[2:].strip().replace("**", "")
    key_m = re.match(r"^`?([A-Za-z0-9._-]+)`?", head)
    groups = [g for g in DATE_IN_BRACKETS_RE.findall(line)]
    plain = [g for g in groups if not USER_MARK_RE.match(g)]
    pick = plain[-1] if plain else (groups[0] if groups else "")
    found = ISO_DATE_RE.search(pick)
    holds = HOLD_DECISION_RE.findall(line)
    deferral = DEFERRAL_RE.search(line)
    return {"key": key_m.group(1) if key_m else "", "held": "(held)" in head or "(held)" in text[:60],
            "sell_flag": "SELL-FLAG" in head or ("SELL-FLAG" in text[:80] and bool(over)),
            "user_call": bool(USER_CALL_RE.search(line)), "deferred": bool(deferral),
            "deferred_on": deferral.group("date") if deferral else None,
            "deferred_to": (deferral.group("to").strip() or None) if deferral else None,
            "hold_on": max(holds) if holds else None, "retire": bool(AWAITING_RETIRED_RE.search(text)),
            "over_cap": bool(over), "since": found.group(0) if found else since_default, "head": head,
            "text": text}


def held_status(item):
    """(decision, status) of a held name from its SELL-FLAG open item (or None): ('hold', 'held by your
    decision on D'), ('deferred', 'decision deferred by you to … on D'), ('pending', 'your decision
    pending') or (None, 'no open item')."""
    if item and item["hold_on"]:
        status = "held by your decision on %s" % item["hold_on"]
        if item["deferred"]:
            status += " (decision deferred %s on %s)" % (item["deferred_to"] or "", item["deferred_on"])
        return "hold", re.sub(r"\s+", " ", status)
    if item and item["deferred"]:
        return "deferred", re.sub(r"\s+", " ", "decision deferred by you %s on %s" % (item["deferred_to"] or "",
                                                                                     item["deferred_on"]))
    if item:
        return "pending", "your decision pending"
    return None, "no open item"


def over_cap_items(todo_text):
    """[(line, date)] of the open items over the 7-entry cap: lines anywhere in queue/TODO.md in the
    OVER_CAP_RE form, each with the first date of the '## ' heading it sits under (or None)."""
    out, date = [], None
    for line in (todo_text or "").replace("\r\n", "\n").split("\n"):
        if line.startswith("## "):
            found = ISO_DATE_RE.search(line)
            date = found.group(0) if found else None
        elif OVER_CAP_RE.match(line):
            out.append((line, date))
    return out


# ------------------------------------------------------------------ retired Gate-0 grounds

def verdict_ground(text):
    """The section-1 Verdict ground of a memo: the parenthesised reason after FAIL in its first
    paragraph ('Understanding FAIL (one-level decomposition: …) → …'), else that paragraph."""
    try:
        paras = site.memo_section(text or "", 1)
    except Exception:       # a memo the extractor cannot read gives no ground, never a stop
        paras = []
    if not paras:
        return ""
    return gate0_reason(paras[0]) or paras[0]


def retired_grounds(ground):
    """Names of the RETIRED_GATE0_GROUNDS a ground text matches, in constant order."""
    return [name for name, pattern in RETIRED_GATE0_GROUNDS if pattern.search(ground or "")]


def retired_check(fm, text, live_version):
    """{retired, grounds, ground} of a memo: retired is True for a DNAF memo written under a MODEL
    below RETIRED_GATE0_VERSION whose section-1 ground matches a retired ground, once the live
    MODEL is at or above that version."""
    verdict = reg.first_token((fm or {}).get("verdict") or "")
    out = {"retired": False, "grounds": [], "ground": ""}
    if verdict != "DNAF":
        return out
    out["ground"] = verdict_ground(text)
    memo_v, retire_v, live_v = (version_tuple((fm or {}).get("model_version", "")),
                                version_tuple(RETIRED_GATE0_VERSION), version_tuple(live_version or ""))
    if memo_v is None or memo_v >= retire_v or live_v is None or live_v < retire_v:
        return out
    out["grounds"] = retired_grounds(out["ground"])
    out["retired"] = bool(out["grounds"])
    return out


# ------------------------------------------------------------------ git

# A routine session starts from a shallow clone; the report reads the whole first-parent history of the ref
# (memo history, MODEL releases, the weekly series), so render refuses a shallow repository up front with one
# clear line (MODEL v4.8.0). The playbook path is built from parts: this file names no framework path.
WEEKLY_PLAYBOOK = "/".join(("routines", "WEEKLY.md"))
SHALLOW_ERROR = "shallow clone: run git fetch --unshallow origin main (%s step 1)" % WEEKLY_PLAYBOOK


def need_full_history(repo_dir):
    """Refuse a shallow repository (ToolError SHALLOW_ERROR); a folder git cannot read is left to the render."""
    try:
        proc = subprocess.run(["git", "-C", repo_dir, "rev-parse", "--is-shallow-repository"],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    except OSError as exc:
        raise ToolError("git failed: %s" % exc)
    if proc.returncode == 0 and proc.stdout.decode("utf-8", "replace").strip() == "true":
        raise ToolError(SHALLOW_ERROR)


class Repo:
    def __init__(self, root):
        self.root = root
        self._show = {}
        self._ls = {}

    def git(self, args, data=None):
        try:
            proc = subprocess.run(["git", "-C", self.root, "-c", "core.quotePath=false"] + list(args),
                                  input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        except OSError as exc:
            raise ToolError("git failed: %s" % exc)
        if proc.returncode != 0:
            raise ToolError("git %s failed: %s" % (" ".join(args[:3]), proc.stderr.decode("utf-8", "replace").strip()))
        return proc.stdout.decode("utf-8", "replace")

    def resolve(self, ref):
        return self.git(["rev-parse", "--verify", ref + "^{commit}"]).strip()

    def show(self, sha, path):
        if sha is None:
            return None
        if (sha, path) not in self._show:
            try:
                self._show[(sha, path)] = self.git(["show", "%s:%s" % (sha, path)])
            except ToolError:
                self._show[(sha, path)] = None
        return self._show[(sha, path)]

    def ls(self, sha, prefix):
        if sha is None:
            return []
        if (sha, prefix) not in self._ls:
            out = self.git(["ls-tree", "-r", "-z", "--name-only", sha, "--", prefix])
            self._ls[(sha, prefix)] = sorted(p for p in out.split("\0") if p)
        return self._ls[(sha, prefix)]

    def history(self, ref):
        """[{sha, when, subject, raw: [(status, old blob, new blob, path)]}] of the ref's
        first-parent history, oldest first (one `git log --raw`; merges diffed against their
        first parent, no rename pairing)."""
        out = self.git(["log", "--first-parent", "--diff-merges=first-parent", "--no-renames", "--raw",
                        "--no-abbrev", "--format=%x1e%H%x1f%ct%x1f%s", ref])
        commits = []
        for chunk in out.split("\x1e")[1:]:
            head, _nl, body = chunk.partition("\n")
            parts = head.split("\x1f")
            if len(parts) != 3:
                continue
            raw = []
            for line in body.split("\n"):
                if not line.startswith(":") or "\t" not in line:
                    continue
                meta, path = line.split("\t", 1)
                fields = meta.split()
                if len(fields) >= 5:
                    raw.append((fields[4][0], fields[2], fields[3], path))
            commits.append({"sha": parts[0], "when": datetime.datetime.fromtimestamp(int(parts[1]), UTC),
                            "subject": parts[2], "raw": raw})
        commits.reverse()
        return commits

    def batch(self, sha, paths):
        return reg.batch_show(self.root, sha, paths)


def register_at(repo, sha):
    """(rows, front matter) of register.csv and _REGISTER.md at sha; ([], {}) when unreadable."""
    if sha is None:
        return [], {}
    text = repo.show(sha, "register.csv")
    rows = []
    if text is not None:
        try:
            rows, _problems = reg.read_csv_text(text, legacy_ok=True)
        except reg.ToolError:
            rows = []
    fm = reg.parse_front_matter(repo.show(sha, "_REGISTER.md") or "")
    return rows, fm


def model_version_at(repo, sha):
    """(model_version, model_date) of the MODEL at sha (MODEL_PATH, else its older path)."""
    for path in MODEL_PATHS:
        text = repo.show(sha, path)
        if text is not None:
            fm = reg.parse_front_matter(text)
            return fm.get("model_version", "") or "n/a", fm.get("model_date", "")
    return "n/a", ""


def current_memos(repo, sha):
    """{key: {path, fm, text}} of the current memo (the one file in memos/{KEY}/) at sha; a key
    whose folder holds more or fewer than one file is left out."""
    dirs = collections.defaultdict(list)
    for path in repo.ls(sha, "memos/"):
        parts = path.split("/")
        if len(parts) == 3:
            dirs[parts[1]].append(path)
    single = {k: v[0] for k, v in dirs.items() if len(v) == 1}
    texts = repo.batch(sha, sorted(single.values())) if sha else {}
    out = {}
    for key, path in single.items():
        text = texts.get(path, "")
        out[key] = {"path": path, "fm": reg.parse_front_matter(text), "text": text}
    return out


# ------------------------------------------------------------------ history: memo adds, weeks

def memo_history(commits):
    """One entry per memo file a first-parent commit added under memos/ that is not a move:
    {commit, key, date, path, job ('ANALYSE' for the first memo of a key, else 'REVIEW')}. A move is
    an add whose blob was seen before or is deleted in the same commit, an add of the same key and
    date that the commit deletes elsewhere (a path migration or date fix), or an add in a commit
    whose subject reads like a re-key, rename, migration or RECONCILE while the parent tree holds a
    memo of the same key or date (MODEL section 7.1a re-keys, the v4.2.1 and v4.5.0 migrations)."""
    seen_blobs, seen_keys, tree = set(), set(), {}
    events = []
    for c in commits:
        adds, dels = [], []
        for status, old, new, path in c["raw"]:
            m = MEMO_NAME_RE.match(path.rsplit("/", 1)[-1])
            if not m:
                continue
            item = (path, old if status == "D" else new, norm_key(m.group("key")), m.group("date"), m.group("key"))
            if status == "A":
                adds.append(item)
            elif status == "D":
                dels.append(item)
        del_blobs = {d[1] for d in dels}
        del_pairs = {(d[2], d[3]) for d in dels}
        tree_keys = {v[0] for v in tree.values()}
        tree_dates = {v[1] for v in tree.values()}
        renaming = bool(MOVE_SUBJECT_RE.search(c["subject"]))
        for path, blob, key, date, raw_key in adds:
            if path.startswith("memos/"):
                move = (blob in seen_blobs or blob in del_blobs or (key, date) in del_pairs
                        or (renaming and (key in tree_keys or date in tree_dates)))
                if not move:
                    events.append({"commit": c, "key": raw_key, "norm": key, "date": date, "path": path,
                                   "job": "REVIEW" if key in seen_keys else "ANALYSE"})
            seen_keys.add(key)
            seen_blobs.add(blob)
        for d in dels:
            tree.pop(d[0], None)
        for a in adds:
            tree[a[0]] = (a[2], a[3])
    return events


def model_releases(repo, commits):
    """[(when, sha, version, model_date, subject, first)] of every first-parent commit at which the
    MODEL version changed, oldest first. The first entry (first=True) is the MODEL's first appearance
    in the history, not a release."""
    out, last = [], None
    for c in commits:
        if not any(path in MODEL_PATHS for _s, _o, _n, path in c["raw"]):
            continue
        version, date = model_version_at(repo, c["sha"])
        if version != "n/a" and version != last:
            out.append((c["when"], c["sha"], version, date, c["subject"], not out))
            last = version
    return out


def live_model(releases, when):
    """The MODEL version live at an instant (the last version change at or before it)."""
    version = "n/a"
    for moment, _sha, ver, _date, _subject, _first in releases:
        if moment <= when:
            version = ver
    return version


def weekly_series(repo, commits, memo_events, releases, until):
    """One row per ISO week (Prague) from the first commit's week to the week of the report date:
    memo adds by job, INCOMPLETE runs, MODEL releases (the MODEL's first appearance not counted) and
    the register's WATCH and key counts at the week's last register commit. A week without a register
    commit carries the previous week's counts; notes name an import week (a commit adding at least
    IMPORT_MIN_MEMOS memos), an uncounted first appearance, a carried week and the last, partial week."""
    if not commits:
        return []
    first_day, last_day = prague_date(commits[0]["when"]), report_date_of(until)
    weeks = collections.OrderedDict()
    day = first_day - datetime.timedelta(days=first_day.weekday())
    while day <= last_day:
        weeks[iso_week(day)] = {"week": iso_week(day), "week_start": day.isoformat(), "analyse": 0, "review": 0,
                                "incomplete": 0, "model_releases": 0, "watch_end": None, "keys_end": None,
                                "note": None}
        day += datetime.timedelta(days=7)
    notes = collections.defaultdict(list)
    per_commit = collections.Counter(e["commit"]["sha"] for e in memo_events)
    imports = {}
    for e in memo_events:
        w = weeks.get(iso_week(prague_date(e["commit"]["when"])))
        if w is not None:
            w["analyse" if e["job"] == "ANALYSE" else "review"] += 1
            sha = e["commit"]["sha"]
            if per_commit[sha] >= IMPORT_MIN_MEMOS and sha not in imports:
                imports[sha] = w["week"]
                notes[w["week"]].append("Import: %d memos in one commit (%s), not research activity"
                                        % (per_commit[sha], sha[:7]))
    last_register = {}
    for c in commits:
        w = iso_week(prague_date(c["when"]))
        if w not in weeks:
            continue
        if parse_title(c["subject"])["kind"] == "incomplete":
            weeks[w]["incomplete"] += 1
        if any(path == "_REGISTER.md" for _s, _o, _n, path in c["raw"]):
            last_register[w] = c["sha"]
    for when, _sha, version, _d, _s, first in releases:
        w = weeks.get(iso_week(prague_date(when)))
        if w is None:
            continue
        if first:
            notes[w["week"]].append("first appearance of MODEL %s, not counted as a release" % version)
        else:
            w["model_releases"] += 1
    previous = None
    for w in weeks.values():
        sha = last_register.get(w["week"])
        if sha is not None:
            fm = reg.parse_front_matter(repo.show(sha, "_REGISTER.md") or "")
            split = WATCH_SPLIT_RE.search(fm.get("verdict_split", "") or "")
            total = (fm.get("names_total") or "").strip()
            w["watch_end"] = int(split.group(1)) if split else None
            w["keys_end"] = int(total) if total.isdigit() else None
            previous = w
        elif previous is not None:
            w["watch_end"], w["keys_end"] = previous["watch_end"], previous["keys_end"]
            notes[w["week"]].append("no register commit this week; counts carried from %s" % previous["week"])
    if weeks:
        last = list(weeks.values())[-1]
        end = to_prague(until)
        if end.time() != datetime.time(0, 0) or end.weekday() != 0:
            notes[last["week"]].append("partial week, to %s" % fmt_when(until))
    for w in weeks.values():
        if notes[w["week"]]:
            text = "; ".join(notes[w["week"]])
            w["note"] = text[:1].upper() + text[1:]
    return list(weeks.values())


# ------------------------------------------------------------------ PR snapshot

def lean_pr(pr):
    return collections.OrderedDict([
        ("number", pr.get("number")), ("state", pr.get("state")), ("title", pr.get("title")),
        ("created_at", pr.get("created_at")), ("updated_at", pr.get("updated_at")),
        ("closed_at", pr.get("closed_at")), ("merged_at", pr.get("merged_at")),
        ("head_ref", (pr.get("head") or {}).get("ref")), ("head_sha", (pr.get("head") or {}).get("sha")),
        ("base_ref", (pr.get("base") or {}).get("ref")), ("merge_commit_sha", pr.get("merge_commit_sha")),
        ("user", (pr.get("user") or {}).get("login")), ("draft", pr.get("draft")),
        ("merged_by", None), ("merged_by_type", None),
    ])


FETCH_PAGE_RE = re.compile(r"^(pulls|issues|comments)_(\d+)\.json$")
FETCH_DETAIL_RE = re.compile(r"^pull_(\d+)\.json$")


def read_json(path, what):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError) as exc:
        raise ToolError("%s %s: %s" % (what, path, exc))


def load_fetch(fetch_dir):
    """The PR snapshot from the raw GitHub pages the WEEKLY routine fetched into fetch_dir (the tool
    itself never talks to GitHub): {count, merged_by_fetched, pages, prs, needs_issue, issues_read,
    comments_read, comments}. prs are lean PR records sorted by number, merged_by taken from each
    pull_{n}.json; a PR seen on two pages (updated between the reads) keeps its newest copy.
    comments are the needs-Jakub issue comments ({created_at, body}), oldest first."""
    if not os.path.isdir(fetch_dir or ""):
        raise ToolError("--fetch-dir %s: not a folder" % fetch_dir)
    pages, details = collections.defaultdict(list), {}
    for name in sorted(os.listdir(fetch_dir)):
        m = FETCH_PAGE_RE.match(name)
        if m:
            pages[m.group(1)].append((int(m.group(2)), name))
            continue
        m = FETCH_DETAIL_RE.match(name)
        if m:
            details[int(m.group(1))] = name

    def rows(kind):
        out = []
        for _page, name in sorted(pages.get(kind, [])):
            data = read_json(os.path.join(fetch_dir, name), "fetch page")
            if not isinstance(data, list) or not all(isinstance(x, dict) for x in data):
                raise ToolError("fetch page %s: not a JSON array of objects" % name)
            out.extend(data)
        return out

    if not pages.get("pulls"):
        raise ToolError("--fetch-dir %s: no pulls_{p}.json page" % fetch_dir)
    by_number = {}
    for raw in rows("pulls"):
        n = raw.get("number")
        if not isinstance(n, int) or isinstance(n, bool):
            raise ToolError("fetch page: a PR without a number")
        pr = lean_pr(raw)
        old = by_number.get(n)
        if old is None or (pr["updated_at"] or "") >= (old["updated_at"] or ""):
            by_number[n] = pr
    detailed, detail_numbers = 0, []
    for n, name in sorted(details.items()):
        full = read_json(os.path.join(fetch_dir, name), "PR detail")
        if not isinstance(full, dict) or full.get("number", n) != n:
            raise ToolError("PR detail %s: not PR %d" % (name, n))
        pr = by_number.get(n)
        if pr is None:
            continue
        by = full.get("merged_by") or {}
        pr["merged_by"], pr["merged_by_type"] = by.get("login"), by.get("type")
        detailed += 1
        detail_numbers.append(n)
    issues = rows("issues")
    needs = sorted(i["number"] for i in issues if i.get("pull_request") is None and i.get("title") == NEEDS_TITLE
                   and isinstance(i.get("number"), int))
    comments, seen = [], set()
    for c in rows("comments"):
        cid = c.get("id")
        if cid is not None and cid in seen:
            continue
        seen.add(cid)
        comments.append({"created_at": c.get("created_at"), "body": c.get("body") or ""})
    comments.sort(key=lambda c: (c["created_at"] or "", c["body"]))
    return collections.OrderedDict([
        ("count", len(by_number)), ("merged_by_fetched", detailed), ("detail_numbers", detail_numbers),
        ("pages", len(pages["pulls"])),
        ("prs", [by_number[n] for n in sorted(by_number)]), ("needs_issue", needs[0] if needs else None),
        ("issues_read", bool(pages.get("issues"))), ("comments_read", bool(pages.get("comments"))),
        ("comments", comments)])


def check_fetch(doc, since, until):
    """Refuse (ToolError) a fetch that silently lost pages: a PR merged in [since - 7 d, until) (this
    week and the prior one, whose merger and held-PR wait the report reads) without its pull_{n}.json,
    or a listed 'GSC - needs Jakub' issue without a comments_{p}.json page (an empty page is fine)."""
    have = set(doc.get("detail_numbers") or [])
    lost = []
    for pr in doc.get("prs") or []:
        merged = parse_gh_time(pr.get("merged_at"))
        if merged is not None and since - datetime.timedelta(days=7) <= merged < until and pr["number"] not in have:
            lost.append(pr["number"])
    if lost:
        raise ToolError("fetch incomplete: no pull_{n}.json for merged PR%s %s (WEEKLY step 4, the merged_by "
                        "command)" % ("" if len(lost) == 1 else "s", ", ".join(str(n) for n in lost[:10])))
    if doc.get("needs_issue") is not None and not doc.get("comments_read"):
        raise ToolError("fetch incomplete: issue %s (%s) is listed but no comments_{p}.json page was fetched "
                        "(WEEKLY step 4, the comments command)" % (doc["needs_issue"], NEEDS_TITLE))


def hold_comments(doc, until):
    """({pr: (time, reason)} of the newest 'PR n held - reason' record before until,
    [(time, what, why)] of every workflow failure record) from the needs-Jakub comments."""
    holds, failures = {}, []
    for c in (doc or {}).get("comments") or []:
        when = parse_gh_time(c.get("created_at"))
        if when is None or when >= until:
            continue
        m = HOLD_COMMENT_RE.match(c["body"])
        if m:
            holds[int(m.group("pr"))] = (when, m.group("reason").strip())
            continue
        m = FAIL_COMMENT_RE.match(c["body"])
        if m:
            failures.append((when, m.group("what"), m.group("why").strip()))
    return holds, failures


# ------------------------------------------------------------------ the report window

WEEK_END = datetime.time(8, 30)          # the window ends on Sunday at 08:30 Europe/Prague
# INTAKE's weekly watchdog (MODEL v4.8.0): its Monday run at or after 06:00 Prague raises the alarm for a week
# whose report is not published; every other run (Sunday, the Saturday sprint, Tuesday to Sunday) stays quiet.
ALARM_AT = datetime.time(6, 0)
# The most a page stamp may run ahead of the run (window's published test) or a batch's --at ahead of the
# clock (dash-writes): a future stamp would make every later WEEKLY run read its week as published.
CLOCK_SKEW = datetime.timedelta(minutes=5)


def window_of(at):
    """(since, until) of the week a run at `at` reports: the seven Prague days ending at the most
    recent Sunday 08:30 Europe/Prague at or before it (local time, so DST-safe)."""
    local = to_prague(at)
    day = local.date() - datetime.timedelta(days=(local.weekday() - 6) % 7)
    until = local_to_utc(datetime.datetime.combine(day, WEEK_END))
    if until > at:
        day -= datetime.timedelta(days=7)
        until = local_to_utc(datetime.datetime.combine(day, WEEK_END))
    since = local_to_utc(datetime.datetime.combine(day - datetime.timedelta(days=7), WEEK_END))
    return since, until


def gh_time(moment):
    """The GitHub time format, UTC: '2026-10-04T06:30:00Z'."""
    return moment.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def alarm_day(at, until):
    """True for a run on the Prague day after until's (the Monday) at or after ALARM_AT Prague: the one INTAKE
    run a week that raises the weekly alarm (DST-safe: both sides are read in Prague local time)."""
    local = to_prague(at)
    return local.date() == prague_date(until) + datetime.timedelta(days=1) and local.time() >= ALARM_AT


def window_doc(at, meta_at=None, meta_by=None):
    """The 'window' command's object; 'published', 'meta_ok' and 'alarm' only when the meta fields are given.
    meta_ok: the stamp was readable (an ISO at and a non-empty by). alarm (INTAKE's weekly watchdog, MODEL
    v4.8.0): the week ending at until is not published and the run is its Monday run (alarm_day)."""
    since, until = window_of(at)
    out = collections.OrderedDict([
        ("since", iso_prague(since)), ("until", iso_prague(until)), ("period", period_label(since, until)),
        ("details_since", gh_time(since - datetime.timedelta(days=14))), ("run", iso_prague(at))])
    if meta_at is not None or meta_by is not None:
        stamp = None
        if meta_at not in (None, "", "-"):
            try:
                stamp = parse_when(meta_at)
            except ToolError:
                stamp = None
        # A stamp after the run (a mistyped run time) never counts: it would silence every later week.
        out["published"] = bool(meta_by == WEEKLY_BY and stamp is not None and until <= stamp <= at + CLOCK_SKEW)
        out["meta_ok"] = bool(stamp is not None and meta_by not in (None, "", "-"))
        out["alarm"] = bool(not out["published"] and alarm_day(at, until))
    return out


def merger_label(pr):
    """'gsc-automerge' for a bot merge, 'Jakub' for jakubhoryna, else the login; None unknown."""
    kind, login = pr.get("merged_by_type"), pr.get("merged_by")
    if kind == "Bot":
        return "gsc-automerge"
    if login == "jakubhoryna":
        return "Jakub"
    return login or None


# ------------------------------------------------------------------ memo events

def grade(fm, field):
    return reg.first_token(fm.get(field) or "") or "-"


def reason(fm, field):
    value = (fm.get(field) or "").strip()
    return "" if value in ("", "-", "n.m.", "—") else value


def deciding_reasons(fm, verdict, text):
    """The deciding reasons of a memo from its machine fields: the failed gates with their
    reason tokens (AVOID), the price against the trigger (WATCH, BUY), or the section-1 ground of a
    DNAF (Gate 0), clipped; '-' when none is stated."""
    if verdict == "AVOID":
        failed = []
        for label, field, bad, why in (("Past", "quality_past", "WEAK", "past_reason"),
                                       ("Future", "quality_future", "WEAK", "future_reason"),
                                       ("SF", "sf", "FAIL", "sf_reason")):
            if grade(fm, field) == bad:
                r = reason(fm, why)
                failed.append("%s %s%s" % (label, bad, (" (%s)" % r) if r else ""))
        return " + ".join(failed) or "-"
    if verdict in ("WATCH", "BUY"):
        px, trig, unit = fm.get("px", ""), fm.get("trigger", ""), fm.get("px_unit", "")
        dist = site.distance(px, trig)
        lead = "all three gates pass" + ("; in the buy zone" if verdict == "BUY" else "")
        if dist is None:
            return lead + "; trigger n/a"
        return "%s; Px %s vs trigger %s %s (%s)" % (lead, px, trig, unit, site.fmt_signed_pct(dist[0]))
    if verdict == "DNAF":
        paras = site.memo_section(text, 1)
        why = gate0_reason(paras[0]) if paras else ""
        return ("Gate 0: " + site.clip(why, 220)) if why else "Gate 0"
    return "-"


def gate0_reason(paragraph):
    """The reason a Gate-0 verdict paragraph gives in parentheses after FAIL
    ('Understanding FAIL (one-level decomposition: …) → DO NOT ANALYSE FURTHER'); '' if none."""
    m = re.search(r"\bFAIL\s*\(", paragraph or "")
    if not m:
        return ""
    depth, start = 1, m.end()
    for i in range(start, len(paragraph)):
        if paragraph[i] == "(":
            depth += 1
        elif paragraph[i] == ")":
            depth -= 1
            if depth == 0:
                return paragraph[start:i].strip()
    return ""


SENTENCE_LABEL_RE = re.compile(r"^(?:Group sentence|Group-level sentence|One sentence|Sentence)\s*[.:—–-]\s*")
NOT_A_BUSINESS_RE = re.compile(r"(?i)\bGate 0\b|\bfails?\b|\bFAIL\b|^(?:Sub-businesses|Units|Sectors)\b")


def understanding(text, verdict):
    """The memo's one-sentence business description (section 2) through gsc_site's extractor,
    with a leading 'Group sentence.' label removed first; '-' when the result is not cleanly a
    business sentence (under 40 characters, or a Gate-0 finding)."""
    try:
        paras = [SENTENCE_LABEL_RE.sub("", p, 1) for p in site.memo_section(text or "", 2)]
        found = site.business_from_paragraphs(paras)
        if not found and verdict == "DNAF":
            found = site.business_from_paragraphs(site.memo_section(text or "", 1)[1:])
    except Exception:       # a memo the extractor cannot read gives '-', never a stop
        found = ""
    if not found or len(found) < 40 or NOT_A_BUSINESS_RE.search(found):
        return "-"
    return found


def memo_events(repo, events, releases, held_keys, flag_model):
    """The memo adds of `events` (memo_history entries) enriched from the files: verdicts, the
    prior memo, grades, deciding reasons, the MODEL in force at the merge, and the retired-ground
    flag read against flag_model (the MODEL live at the end of the period: where things stand)."""
    out = []
    for h in events:
        c = h["commit"]
        parsed = parse_title(c["subject"])
        key, path = h["key"], h["path"]
        text = repo.show(c["sha"], path) or ""
        fm = reg.parse_front_matter(text)
        verdict = reg.first_token(fm.get("verdict") or "") or "n/a"
        parent = c["sha"] + "^1"
        prior_files = [p for p in repo.ls(parent, "memos/%s/" % key) if p.count("/") == 2]
        prior_fm, prior_path = {}, ""
        if len(prior_files) == 1:
            prior_path = prior_files[0]
            prior_fm = reg.parse_front_matter(repo.show(parent, prior_path) or "")
        new_key = h["job"] == "ANALYSE"
        position = (fm.get("position") or "").upper()
        held = parsed["held"] or position.startswith("HELD") or norm_key(key) in held_keys
        live = live_model(releases, c["when"])
        memo_model = fm.get("model_version", "")
        superseded = bool(version_tuple(memo_model) and version_tuple(live)
                          and version_tuple(memo_model) < version_tuple(live))
        prior_verdict = reg.first_token(prior_fm.get("verdict") or "") if prior_fm else ""
        flag = retired_check(fm, text, flag_model)
        out.append(collections.OrderedDict([
            ("key", key), ("title_key", parsed["key"]), ("company", fm.get("company", "") or "-"),
            ("job", h["job"]), ("title_job", parsed["job"]), ("new_key", new_key), ("verdict", verdict),
            ("prior_verdict", prior_verdict or None),
            ("prior_memo", prior_path), ("changed", bool(prior_verdict) and prior_verdict != verdict),
            ("past", grade(fm, "quality_past")), ("past_reason", reason(fm, "past_reason")),
            ("future", grade(fm, "quality_future")), ("future_reason", reason(fm, "future_reason")),
            ("sf", grade(fm, "sf")), ("sf_reason", reason(fm, "sf_reason")),
            ("deciding", deciding_reasons(fm, verdict, text)), ("understanding", understanding(text, verdict)),
            ("memo_path", path), ("memo_date", fm.get("memo_date", "")),
            ("memo_version", fm.get("memo_version", "")), ("memo_model", memo_model),
            ("live_model", live), ("superseded_model", superseded), ("retired", flag["retired"]),
            ("retired_grounds", flag["grounds"]),
            ("produced_by", fm.get("produced_by", "") or "attended"),
            ("held", held), ("zone", fm.get("zone", "") if held else ""),
            ("prior_zone", prior_fm.get("zone", "") if held else ""),
            ("px", fm.get("px", "")), ("px_unit", fm.get("px_unit", "")), ("trigger", fm.get("trigger", "")),
            ("outcome", parsed["outcome"]), ("moved", parsed["moved"]),
            ("pr", parsed["pr"]), ("sha", c["sha"]), ("merged", c["when"]),
        ]))
    return out


def sweep_zone_changes(repo, window):
    """Held-zone changes reported by SWEEP row files merged in the window: the row's Portfolio
    table zone word against the register's held zone at the commit's parent (J11)."""
    out = []
    for c in window:
        if c["parsed"]["job"] != "SWEEP":
            continue
        rows, _fm = register_at(repo, c["sha"] + "^1")
        held = {r["key"]: r for r in rows if r.get("held") == "true"}
        for status, path in c["changes"]:
            if status != "A" or not SWEEP_ROW_RE.match(path):
                continue
            sections = reg.sections_of(repo.show(c["sha"], path) or "")
            heading = next((h for h in sections if h.lower().startswith("portfolio table")), None)
            for row in reg.table_rows(sections.get(heading, [])) if heading else []:
                key = re.split(r"[\s(]", (row.get("ticker") or "").strip().strip("`"), maxsplit=1)[0]
                zone = next((row[col] for col in row if col.startswith("zone")), "")
                swept = reg.ZONE_WORD_RE.match(zone or "")
                if key not in held or not swept:
                    continue
                was = reg.ZONE_WORD_RE.match(held[key].get("zone") or "")
                if not was or was.group(1) != swept.group(1):
                    out.append({"key": key, "from": held[key].get("zone") or "-", "to": swept.group(1),
                                "source": "SWEEP %s" % c["parsed"]["date"], "pr": c["parsed"]["pr"],
                                "when": c["when"]})
    return out


# ------------------------------------------------------------------ pending overlay

def zone_word(zone):
    """The zone word of a held zone cell (ADD, HOLD or SELL-FLAG; MODEL section 7.2), else the cell's own
    text, '-' when empty: 'SELL-FLAG (SR2 — quality re-verdict …)' and 'SELL-FLAG SR2' are one zone."""
    text = (zone or "").strip()
    m = reg.ZONE_WORD_RE.match(text)
    return m.group(1) if m else (text or "-")


def memo_section_of(fm):
    """The register section a memo's verdict and grades give (gsc_register.section_for)."""
    verdict = reg.first_token(fm.get("verdict") or "")
    gates = reg.gates_failed(reg.first_token(fm.get("quality_past") or ""),
                             reg.first_token(fm.get("quality_future") or ""), reg.first_token(fm.get("sf") or ""))
    return reg.section_for(verdict, gates) or verdict


def pending_overlay(repo, sha, rows, memos, live_version):
    """{key: entry} of the row files on the ref at sha (merged, not yet applied by INTAKE), the
    last file per key winning, plus a list of keyless row files. An ANALYSE or REVIEW row whose
    memo_path is the key's current memo is 'pending' with that memo's verdict (front matter: the
    memo wins); one whose memo moved to archive/memos is 'superseded' (INTAKE applies only its
    queue update); one whose memo is missing is 'held back'. Other row types carry no verdict."""
    by_key = {r["key"]: r for r in rows}
    paths = [p for p in repo.ls(sha, "queue/rows/") if p.endswith(".md") and not p.endswith("README.md")]
    texts = repo.batch(sha, paths) if paths else {}
    out, keyless = collections.OrderedDict(), []
    for path in paths:
        fm = reg.parse_front_matter(texts.get(path, ""))
        row_type, key = fm.get("row_type", "") or "n/a", fm.get("key", "")
        entry = {"path": path, "file": path.rsplit("/", 1)[-1], "row_type": row_type, "key": key,
                 "company": fm.get("company", ""), "memo_path": fm.get("memo_path", ""),
                 "row_model": fm.get("model_version", ""), "pr_title": fm.get("pr_title", ""),
                 "state": row_type.lower(), "verdict": None, "section": None, "memo_date": None,
                 "memo_model": None, "fm": {}, "text": "", "register_verdict": None, "register_section": None,
                 "new_key": False, "changes": False, "retired": False, "label": ""}
        if not key:
            entry["label"] = "pending: %s row" % row_type
            keyless.append(entry)
            continue
        current = memos.get(key)
        if row_type in ("ANALYSE", "REVIEW"):
            if current and current["path"] == entry["memo_path"]:
                mfm = current["fm"]
                named = MEMO_NAME_RE.match(current["path"].rsplit("/", 1)[-1])
                date = mfm.get("memo_date", "") or (named.group("date") if named else "")
                entry.update(state="pending", verdict=reg.first_token(mfm.get("verdict") or "") or "n/a",
                             section=memo_section_of(mfm), memo_date=date, memo_model=mfm.get("model_version", ""),
                             fm=mfm, text=current["text"])
                entry["retired"] = retired_check(mfm, current["text"], live_version)["retired"]
                entry["label"] = "pending: %s (memo %s)" % (entry["verdict"], date or "n/a")
            elif entry["memo_path"] and entry["memo_path"].rsplit("/", 1)[-1] in {
                    p.rsplit("/", 1)[-1] for p in repo.ls(sha, "archive/memos/%s/" % key)}:
                entry.update(state="superseded", label="pending: superseded row (queue update only)")
            else:
                entry.update(state="held back", label="pending: held back (memo not current on the ref)")
        elif row_type == "INCOMPLETE":
            entry["label"] = "pending: INCOMPLETE (no memo)"
        else:
            entry["label"] = "pending: %s row" % row_type
        row = by_key.get(key)
        if row is not None:
            entry["register_verdict"], entry["register_section"] = row["verdict"], row["section"]
        entry["new_key"] = row is None and entry["state"] == "pending"
        entry["changes"] = entry["state"] == "pending" and row is not None and row["verdict"] != entry["verdict"]
        out[key] = entry
    return out, keyless


def rows_after_pending(rows, overlay):
    """The register rows with every pending verdict applied (section, verdict, memo date and MODEL
    from the pending memo), plus a minimal row per pending new key."""
    out = []
    for r in rows:
        p = overlay.get(r["key"])
        if p and p["state"] == "pending":
            nr = dict(r)
            nr.update(section=p["section"] or r["section"], verdict=p["verdict"], memo_date=p["memo_date"] or "",
                      model_version=p["memo_model"] or "")
            out.append(nr)
        else:
            out.append(r)
    for key, p in overlay.items():
        if p["state"] == "pending" and p["new_key"]:
            out.append({"key": key, "company": p["company"] or p["fm"].get("company", ""), "section": p["section"],
                        "verdict": p["verdict"], "memo_date": p["memo_date"] or "",
                        "model_version": p["memo_model"] or "", "held": "false", "next_review_short": "-"})
    return out


# ------------------------------------------------------------------ register state

def retest_lists_of(todo_text):
    lists = collections.defaultdict(list)       # {norm key: [block version labels]}
    for title, keys in retest_keys(todo_text).items():
        version = RETEST_BLOCK_RE.match(title).group(1)
        for k in keys:
            lists[norm_key(k)].append(version)
    return lists


def retest_owed(lists, key, memo_model):
    """'v4.6.0' style labels of the re-test blocks that list a key and are newer than the MODEL
    version its memo was written under: the re-test is still owed. A block at or below that
    version lists a re-test the memo already ran (its line clears when INTAKE applies the memo)."""
    have = version_tuple(memo_model)
    return [v for v in lists.get(norm_key(key), [])
            if version_tuple(v) is None or have is None or version_tuple(v) > have]


def retest_note(lists, key, memo_model):
    owed = retest_owed(lists, key, memo_model)
    if owed:
        return "re-test %s owed" % " + ".join(owed)
    if lists.get(norm_key(key)):
        return "re-test done, line clears at INTAKE"
    return ""


def overdue(row, as_of):
    """True when a row's next review (next_review_short: a date, month or quarter) ended before as_of."""
    last = reg.review_last_day(row.get("next_review_short", "") or "")
    return bool(last) and row.get("section") != "RETIRED" and datetime.date.fromisoformat(last) < as_of


def register_state(repo, sha, as_of, live_version):
    """Everything the report reads from one register state (the commit at sha) as of a Prague date."""
    rows, fm = register_at(repo, sha)
    memos = current_memos(repo, sha) if sha else {}
    todo = (repo.show(sha, "queue/TODO.md") if sha else "") or ""
    lists = retest_lists_of(todo)
    overlay, keyless = pending_overlay(repo, sha, rows, memos, live_version) if sha else ({}, [])
    after = rows_after_pending(rows, overlay)
    head_items = todo_block(todo, "▶ Open items (register)")
    over_cap = over_cap_items(todo)
    items = [parse_open_item(x) for x in head_items] + [parse_open_item(x, d) for x, d in over_cap]
    retire_keys = {norm_key(i["key"]) for i in items if i["key"] and i["retire"]}

    def memo_model(key, fallback):
        cur = memos.get(key)
        return cur["fm"].get("model_version", "") if cur else fallback

    shortlist = []
    for row in rows:
        if row["section"] not in ("WATCH", "BUY"):
            continue
        status, dist = shortlist_status(row)
        p = overlay.get(row["key"])
        age = None
        if reg.DATE_RE.match(row.get("px_date") or ""):
            age = (as_of - datetime.date.fromisoformat(row["px_date"])).days
        # One basis for the re-test debt: the register row's own MODEL (the memo INTAKE applied).
        owed = retest_owed(lists, row["key"], row.get("model_version", ""))
        owed_now = retest_owed(lists, row["key"], memo_model(row["key"], row.get("model_version", "")))
        note = retest_note(lists, row["key"], row.get("model_version", ""))
        if owed and not owed_now and p and p["state"] == "pending":
            note += "; done in the pending memo, clears at INTAKE"
        fall = site.distance(row.get("px", ""), row.get("trigger", ""))
        pending_change = bool(p and p["changes"])
        all_cash = row.get("trigger_basis") == "all-cash"
        shortlist.append(collections.OrderedDict([
            ("key", row["key"]), ("company", row["company"]), ("section", row["section"]),
            ("region", region_of(row["key"])[1]), ("px", row["px"]), ("px_unit", row["px_unit"]),
            ("px_date", row["px_date"]), ("px_age_d", age), ("px_source", row.get("px_source", "")),
            ("trigger", row["trigger"]), ("trigger_basis", row.get("trigger_basis", "")), ("distance", dist),
            ("needs_fall", fall[1] if fall else None),
            ("mcap_fcf", row["mcap_fcf"]), ("ev_oi", row["ev_oi"]), ("status", status),
            ("memo_date", row.get("memo_date", "")), ("model_version", row.get("model_version", "")),
            ("retest", owed), ("retest_note", note),
            ("all_cash", all_cash), ("pending", p["label"] if p else None), ("pending_change", pending_change),
            ("reliable", bool(not owed and not pending_change and not all_cash and age is not None
                              and age <= RELIABLE_PX_DAYS)),
            ("next_review", row.get("next_review_short", "")), ("held", row.get("held") == "true"),
        ]))
    ranked = sorted((r for r in shortlist if r["distance"] is not None and not r["pending_change"]),
                    key=lambda r: (r["distance"], r["key"]))
    pending_changes = [r for r in shortlist if r["pending_change"]]

    def dnaf_flags(source_rows, use_overlay):
        flags = collections.OrderedDict()
        for row in source_rows:
            if row["section"] != "DNAF":
                continue
            p = overlay.get(row["key"]) if use_overlay else None
            if p and p["state"] == "pending":
                mfm, text = p["fm"], p["text"]
            else:
                cur = memos.get(row["key"])
                mfm, text = (cur["fm"], cur["text"]) if cur else ({}, "")
            check = retired_check(mfm, text, live_version)
            check["awaiting_retired"] = bool(not check["retired"] and norm_key(row["key"]) in retire_keys)
            flags[row["key"]] = dict(check, memo_verdict=reg.first_token(mfm.get("verdict") or "") or "n/a",
                                     memo_model=mfm.get("model_version", "") or "n/a",
                                     memo_date=mfm.get("memo_date", "") or "n/a",
                                     pending=bool(p and p["state"] == "pending"))
        return flags

    def counts(source):
        c = collections.Counter(r["section"] for r in source)
        c["AVOID"] = sum(1 for r in source if r.get("verdict") == "AVOID")
        c["keys"] = len(source)
        return c

    watch_rows = [r for r in shortlist if r["section"] == "WATCH" and not r["pending_change"]]
    retest_union = {norm_key(k) for keys in retest_keys(todo).values() for k in keys}
    return {
        "sha": sha, "rows": rows, "fm": fm, "memos": memos, "todo": todo, "retest_lists": lists,
        "retest_blocks": retest_keys(todo), "retest_lines": retest_lines(todo), "retest_union": retest_union,
        "retest_partial": retest_partial(todo),
        "overlay": overlay, "keyless_rows": keyless, "after": after, "counts": counts(rows),
        "counts_after": counts(after), "shortlist": shortlist, "ranked": ranked,
        "pending_changes": pending_changes, "status_counts": collections.Counter(r["status"] for r in ranked),
        "dnaf": dnaf_flags(rows, False), "dnaf_after": dnaf_flags(after, True),
        "watch_owed": sorted(norm_key(r["key"]) for r in shortlist if r["section"] == "WATCH" and r["retest"]),
        "watch_owed_after": sorted(norm_key(r["key"]) for r in after if r["section"] == "WATCH"
                                   and retest_owed(lists, r["key"], r.get("model_version", ""))),
        "watch_distance_median": median1([r["distance"] * 100 for r in watch_rows if r["distance"] is not None]),
        "watch_age_median": median1([r["px_age_d"] for r in watch_rows if r["distance"] is not None
                                     and r["px_age_d"] is not None]),
        "overdue_all": sorted(r["key"] for r in rows if overdue(r, as_of)),
        "overdue_watch": sorted(r["key"] for r in rows if r["section"] == "WATCH" and overdue(r, as_of)),
        "queue": queue_markers((repo.show(sha, "queue/DRAFT_QUEUE.md") if sha else "") or ""),
        "open_items": head_items, "over_cap": [x for x, _d in over_cap], "items": items,
        "ideas": todo_block(todo, "▶ IDEAS candidates"),
        "blocks": collections.OrderedDict((t, len(b)) for t, b in todo_blocks(todo)),
        "proposals": [p for p in repo.ls(sha, "queue/proposals/") if not p.endswith("README.md")] if sha else [],
        "as_of": as_of, "live": live_version,
    }


# ------------------------------------------------------------------ health input

def load_health(path):
    """The routine schedule as WEEKLY read it (--health-json): a JSON array of {name, job, cron,
    enabled, sprint, last_run}, or an object {source, read_at, triggers: [...], disabled}. Returns
    {source, read_at, triggers, disabled}; a job 'QUEUE-SEED' reads as SEED. Bad input is a
    ToolError, which render reports under Fix instead of stopping."""
    doc = read_json(path, "--health-json")
    if isinstance(doc, list):
        doc = {"source": "list_triggers (WEEKLY)", "read_at": None, "triggers": doc, "disabled": None}
    if not isinstance(doc, dict) or not isinstance(doc.get("triggers"), list):
        raise ToolError("--health-json: a JSON array of routines, or an object with a 'triggers' array")
    triggers = []
    for t in doc["triggers"]:
        if not isinstance(t, dict):
            raise ToolError("--health-json: bad routine %r" % (t,))
        t = dict(t, job="SEED" if t.get("job") == "QUEUE-SEED" else t.get("job"))
        if not isinstance(t.get("last_run") or {}, dict):
            raise ToolError("--health-json: bad last_run of routine %r" % (t.get("name"),))
        last = dict(t.get("last_run") or {})
        if last:
            # list_triggers prints 'ROUTINE_RUN_STATUS_FAILED' and 'ROUTINE_RUN_FAILURE_REASON_USAGE_LIMIT_REACHED'
            # ('…_UNSPECIFIED' for none); the report reads the bare words.
            last["status"] = re.sub(r"^ROUTINE_RUN_STATUS_", "", str(last.get("status") or "")) or None
            reason = re.sub(r"^ROUTINE_RUN_FAILURE_REASON_", "", str(last.get("failure_reason") or ""))
            last["failure_reason"] = None if reason in ("", "UNSPECIFIED") else reason
            t["last_run"] = last
        if t["job"] not in HEALTH_JOBS or not isinstance(t.get("cron"), str) \
                or not isinstance(t.get("enabled"), bool) or not isinstance(t.get("sprint"), bool) \
                or not isinstance(t.get("last_run") or {}, dict):
            raise ToolError("--health-json: bad routine %r" % (t.get("name"),))
        # fired_at and finished_at are optional (an older health file has no finished_at); one given is a time.
        for field in ("fired_at", "finished_at"):
            value = (t.get("last_run") or {}).get(field)
            if value in (None, ""):
                continue
            try:
                if not isinstance(value, str):
                    raise ToolError("not text")
                parse_when(value)
            except ToolError:
                raise ToolError("--health-json: bad last_run %s %r of routine %r" % (field, value, t.get("name")))
        parse_cron(t["cron"])
        triggers.append(t)
    disabled = doc.get("disabled")
    if disabled is None:
        disabled = sorted(str(t.get("name", "")) for t in triggers if not t["enabled"])
    return {"source": doc.get("source") or "", "read_at": doc.get("read_at"), "triggers": triggers,
            "disabled": list(disabled)}


def health_view(doc, since, until):
    """Scheduled fires per trigger over [since, until) and per job (base, sprint), and the
    last-run failures; None without a health input."""
    if doc is None:
        return None
    triggers = []
    for t in doc["triggers"]:
        fires = cron_fires(t["cron"], since, until) if t["enabled"] else []
        last = t.get("last_run") or {}
        fired, finished = parse_gh_time(last.get("fired_at")), parse_gh_time(last.get("finished_at"))
        triggers.append(collections.OrderedDict([
            ("name", t.get("name", "")), ("job", t["job"]), ("cron", t["cron"]), ("enabled", t["enabled"]),
            ("sprint", t["sprint"]), ("fires", len(fires)), ("first_fire", fires[0] if fires else None),
            ("last_fire", fires[-1] if fires else None), ("last_status", last.get("status") or None),
            ("last_fired_at", fired), ("last_finished_at", finished),
            # the last run's duration in whole seconds; None without both times or when they run backwards
            ("last_duration_s", int((finished - fired).total_seconds())
             if fired is not None and finished is not None and finished >= fired else None),
            ("failure_reason", last.get("failure_reason") or None),
        ]))
    by_job = collections.OrderedDict()
    for job in HEALTH_JOBS:
        mine = [t for t in triggers if t["job"] == job and t["enabled"]]
        by_job[job] = {"scheduled_base": sum(t["fires"] for t in mine if not t["sprint"]),
                       "scheduled_sprint": sum(t["fires"] for t in mine if t["sprint"]),
                       "triggers": len(mine),
                       "usage_limit": sum(1 for t in mine if t["last_status"] == "FAILED"
                                          and t["failure_reason"] == USAGE_LIMIT)}
    failures = [t for t in triggers if t["last_status"] == "FAILED"]
    return {"source": doc.get("source", ""), "read_at": parse_gh_time(doc.get("read_at")),
            "triggers": triggers, "by_job": by_job, "failures": failures,
            "disabled": list(doc.get("disabled") or []), "doc": doc}


def noop_runs_of(health, pr_rows):
    """The routines whose last run was likely a no-op (MODEL v4.8.0): status SUCCEEDED, a duration under
    NOOP_SECONDS, a job in NOOP_JOBS (never WEEKLY), no routine PR of that job created from fired_at to
    finished_at + NOOP_GRACE, and, for SEED and SWEEP, no PR of that job open at fired_at. [] without a
    health input; a trigger without both times is never flagged."""
    if health is None:
        return []
    out = []
    for t in health["triggers"]:
        fired, finished, took = t["last_fired_at"], t["last_finished_at"], t.get("last_duration_s")
        if t["job"] not in NOOP_JOBS or t["last_status"] != "SUCCEEDED" or took is None or took >= NOOP_SECONDS:
            continue
        mine = [r for r in pr_rows if is_routine(r["parsed"]) and r["parsed"]["job"] == t["job"]]
        if any(r["created"] is not None and fired <= r["created"] <= finished + NOOP_GRACE for r in mine):
            continue
        if t["job"] in NOOP_OPEN_PR_JOBS and any(
                r["created"] is not None and r["created"] < fired and (r["closed"] is None or r["closed"] >= fired)
                for r in mine):
            continue
        out.append(t)
    return out


def fires_between(health, start, end, sprint=None, jobs=None):
    """Scheduled fires of the enabled triggers in [start, end), optionally by sprint flag and jobs."""
    if health is None:
        return None
    total = 0
    for t in health["doc"]["triggers"]:
        if not t["enabled"] or (sprint is not None and t["sprint"] != sprint) or (jobs and t["job"] not in jobs):
            continue
        total += len(cron_fires(t["cron"], start, end))
    return total


# ------------------------------------------------------------------ build

def build(repo_dir, ref, since, until, prs_doc, health_doc=None, allow_stale_ref=False, health_problem=None):
    load_tools(repo_dir)
    if until <= since:
        raise ToolError("--until must be after --since")
    need_full_history(repo_dir)
    repo = Repo(repo_dir)
    ref_sha = repo.resolve(ref)
    commits = repo.history(ref_sha)
    if not commits:
        raise ToolError("no commits on %s" % ref)
    ref_time = commits[-1]["when"]
    fp_shas = {c["sha"] for c in commits}
    before_since = [c for c in commits if c["when"] < since]
    before_until = [c for c in commits if c["when"] < until]
    if not before_until:
        raise ToolError("no commit on %s before --until" % ref)
    start, end = (before_since[-1] if before_since else None), before_until[-1]
    window = [c for c in commits if since <= c["when"] < until]
    for c in window:
        c["parsed"] = parse_title(c["subject"])
        c["changes"] = [(s, p) for s, _o, _n, p in c["raw"]]
    span = until - since
    prior_since = since - span
    report_date = report_date_of(until)
    start_date = report_date_of(since)

    # ---------------- PR snapshot and the stale-ref check
    if prs_doc is not None:
        check_fetch(prs_doc, since, until)
    prs = (prs_doc or {}).get("prs") or []
    pr_rows = []
    for pr in prs:
        pr_rows.append({"pr": pr, "parsed": parse_title(pr.get("title")), "created": parse_gh_time(pr.get("created_at")),
                        "merged": parse_gh_time(pr.get("merged_at")), "closed": parse_gh_time(pr.get("closed_at"))})

    def in_span(moment, a, b):
        return moment is not None and a <= moment < b

    def in_window(moment):
        return in_span(moment, since, until)

    stale = [r for r in pr_rows if in_window(r["merged"]) and r["merged"] > ref_time
             and (r["pr"].get("base_ref") in (None, "main"))
             and r["pr"].get("merge_commit_sha") not in fp_shas]
    if stale and not allow_stale_ref:
        r = max(stale, key=lambda x: x["merged"])
        raise ToolError("stale ref: %s = %s, last commit %s, is older than PR %s merged %s inside the window "
                        "(its merge commit is not on the ref). Fetch the ref again and render again, or "
                        "pass --allow-stale-ref." % (ref, ref_sha[:7], fmt_when(ref_time, True), r["pr"]["number"],
                                                     fmt_when(r["merged"], True)))

    # ---------------- history: memo adds, MODEL releases, weekly series
    hist_events = memo_history([c for c in commits if c["when"] < until])
    releases = model_releases(repo, [c for c in commits if c["when"] < until])
    live_start = live_model(releases, since - ONE_SECOND)
    live_end = live_model(releases, until - ONE_SECOND)
    timeline = [r for r in releases if since <= r[0] < until and not r[5]]
    weekly = weekly_series(repo, [c for c in commits if c["when"] < until], hist_events, releases, until)

    # ---------------- states (every retired-ground flag read with the lens live at the end)
    st = register_state(repo, start["sha"] if start else None, start_date, live_end)
    en = register_state(repo, end["sha"], report_date, live_end)
    held_start = {norm_key(r["key"]) for r in st["rows"] if r.get("held") == "true"}
    events = memo_events(repo, [h for h in hist_events if since <= h["commit"]["when"] < until], releases, held_start,
                         live_end)
    prior_start_rows = register_at(repo, next((c["sha"] for c in reversed(commits) if c["when"] < prior_since), None))[0]
    prior_events = memo_events(repo, [h for h in hist_events if prior_since <= h["commit"]["when"] < since], releases,
                               {norm_key(r["key"]) for r in prior_start_rows if r.get("held") == "true"}, live_end)
    for e in events:
        e["retest_end"] = retest_note(en["retest_lists"], e["key"], e["memo_model"])
        e["retest_owed"] = bool(retest_owed(en["retest_lists"], e["key"], e["memo_model"]))
    diff = register_diff(st["rows"], en["rows"])

    def new_watch(evts):
        return [e for e in evts if e["verdict"] == "WATCH" and e["prior_verdict"] != "WATCH"]

    # ---------------- PRs
    def open_at(r, moment):
        return r["created"] is not None and r["created"] < moment and (r["closed"] is None or r["closed"] >= moment)

    def job_bucket(parsed):
        if is_routine(parsed):
            return parsed["job"]
        return "attended" if parsed["job"] == "attended" else ("revert" if parsed["job"] == "revert" else "other")

    def run_id(r):
        """A run is its branch: a PR re-opened from the same run branch is the same run."""
        return r["pr"].get("head_ref") or "PR %s" % r["pr"].get("number")

    def pr_counts(a, b):
        buckets = list(JOBS) + ["attended", "revert", "other"]
        out = collections.OrderedDict((x, collections.Counter()) for x in buckets)
        runs = collections.defaultdict(set)
        for r in pr_rows:
            bucket = job_bucket(r["parsed"])
            if in_span(r["created"], a, b):
                out[bucket]["opened"] += 1
                runs[bucket].add(run_id(r))
            if in_span(r["merged"], a, b):
                out[bucket]["merged"] += 1
                kind = r["pr"].get("merged_by_type") or "n/a"
                out[bucket]["merged_by_" + ("bot" if kind == "Bot" else ("human" if kind == "User" else "n/a"))] += 1
            if in_span(r["closed"], a, b) and r["merged"] is None:
                out[bucket]["closed_unmerged"] += 1
            if open_at(r, b):
                out[bucket]["open_at_end"] += 1
        for bucket, ids in runs.items():
            out[bucket]["runs"] = len(ids)
        return out
    by_job_all = pr_counts(since, until)
    by_job = collections.OrderedDict((b, dict(c)) for b, c in by_job_all.items() if c)
    by_job_prior = pr_counts(prior_since, since)
    reopened = []
    by_run = collections.defaultdict(list)
    for r in pr_rows:
        if is_routine(r["parsed"]) and in_window(r["created"]):
            by_run[run_id(r)].append(r)
    for rid, group in sorted(by_run.items()):
        if len(group) > 1:
            group = sorted(group, key=lambda x: x["pr"]["number"])
            reopened.append({"run": rid, "prs": [x["pr"]["number"] for x in group], "key": group[-1]["parsed"]["key"]})

    holds, workflow_failures = hold_comments(prs_doc, until)
    open_old = [r for r in pr_rows if open_at(r, until) and until - r["created"] > OPEN_PR_AGE]
    finished_waiting = [r for r in open_old if is_routine(r["parsed"]) and r["parsed"]["tag"] not in ("running", "fixing")]
    running_old = [r for r in pr_rows if is_routine(r["parsed"]) and open_at(r, until) and r["parsed"]["tag"] == "running"
                   and until - r["created"] > RUNNING_AGE]
    held_prs = []
    for r in pr_rows:
        parsed = r["parsed"]
        if not is_routine(parsed):
            continue
        human = r["merged"] is not None and r["pr"].get("merged_by_type") == "User"
        face = held_for_jakub(parsed)
        recorded = r["pr"]["number"] in holds
        relevant = open_at(r, until) or in_window(r["merged"]) or in_window(r["closed"])
        if relevant and (face or (recorded and open_at(r, until)) or (human and in_window(r["merged"]))):
            if open_at(r, until):
                state = "open"
            elif r["merged"] is not None:
                state = "merged by %s" % (r["pr"].get("merged_by") or "n/a")
            else:
                state = "closed unmerged"
            wait = (r["merged"] - r["created"]) if (r["merged"] is not None and r["merged"] < until) \
                else (until - r["created"])
            why = []
            if parsed["held"]:
                why.append("HELD name")
            if parsed["job"] == "REVIEW" and parsed["was"]:
                why.append("verdict change (was %s)" % parsed["was"])
            if parsed["verdict"] == "BUY":
                why.append("BUY")
            if parsed["kind"] in ("stopped", "blocked"):
                why.append(parsed["kind"])
            if parsed["tag"] == "fixing":
                why.append("[fixing]")
            if parsed["job"] == "SEED":
                why.append("QUEUE-SEED (always held)")
            record = holds.get(r["pr"]["number"])
            if record:
                why.append("gsc-automerge: %s" % site.clip(record[1], 160))
            if not why:
                mismatch = next((e for e in events if e["pr"] == r["pr"]["number"] and e["title_key"]
                                 and e["title_key"] != e["key"]), None)
                if mismatch:
                    why.append("title key %s ≠ memo key %s (likely cause, inference)" % (mismatch["title_key"],
                                                                                        mismatch["key"]))
                else:
                    why.append("merged by a human; the title shows no hold reason")
            held_prs.append(collections.OrderedDict([
                ("number", r["pr"]["number"]), ("job", parsed["job"]), ("key", parsed["key"]),
                ("outcome", parsed["outcome"] or parsed["tag"]), ("kind", parsed["kind"]), ("state", state),
                ("why", ", ".join(why)), ("created", r["created"]), ("merged", r["merged"]),
                ("wait_hours", hours(wait)),
            ]))
    held_prs.sort(key=lambda h: (h["state"] != "open", h["created"] or since, h["number"]))

    stopped = [r for r in pr_rows if r["parsed"]["kind"] in ("stopped", "blocked")
               and (in_window(r["created"]) or in_window(r["closed"]) or open_at(r, until))]
    incomplete_prs = [r for r in pr_rows if r["parsed"]["kind"] == "incomplete"
                      and (in_window(r["merged"]) or in_window(r["closed"]) or open_at(r, until))]
    abandoned = [r for r in pr_rows if r["parsed"]["tag"] in ("abandoned", "superseded") and in_window(r["closed"])]
    merged_after_ref = [r for r in pr_rows if in_window(r["merged"]) and r["pr"].get("merge_commit_sha")
                        and r["pr"]["merge_commit_sha"] not in fp_shas]
    merged_after_until = [r for r in pr_rows if r["merged"] is not None and r["merged"] >= until]

    def latency(rows):
        values = sorted(hours(r["merged"] - r["created"]) for r in rows)
        if not values:
            return {"count": 0, "median_h": None, "max_h": None, "min_h": None}
        return {"count": len(values), "median_h": q1(statistics.median(values)), "max_h": values[-1],
                "min_h": values[0]}

    def routine_merged(a, b, kind):
        """Routine PRs merged in [a, b) by kind; Jakub's merges only of PRs opened once gsc-automerge
        ran (AUTOMERGE_START): the comparable held-PR waits."""
        return [r for r in pr_rows if is_routine(r["parsed"]) and in_span(r["merged"], a, b)
                and r["pr"].get("merged_by_type") == kind
                and (kind != "User" or (r["created"] is not None and r["created"] >= AUTOMERGE_START))]
    latency_bot = latency(routine_merged(since, until, "Bot"))
    latency_human = latency(routine_merged(since, until, "User"))
    latency_human_prior = latency(routine_merged(prior_since, since, "User"))
    merged_by_missing = [r for r in pr_rows if is_routine(r["parsed"]) and in_window(r["merged"])
                         and not r["pr"].get("merged_by_type")]

    created_routine = sorted(r["created"] for r in pr_rows if is_routine(r["parsed"]) and in_window(r["created"]))
    points = [since] + created_routine + [until]
    gap = max(((points[i + 1] - points[i], points[i], points[i + 1]) for i in range(len(points) - 1)),
              key=lambda g: g[0]) if prs else None
    day_grid = collections.OrderedDict()
    day = prague_date(since)
    while day <= report_date:
        day_grid[day.isoformat()] = collections.Counter()
        day += datetime.timedelta(days=1)
    for r in pr_rows:
        if is_routine(r["parsed"]) and in_window(r["created"]):
            d = prague_date(r["created"]).isoformat()
            if d in day_grid:
                day_grid[d][r["parsed"]["job"]] += 1

    # ---------------- schedule health
    health = health_view(health_doc, since, until)
    noop_runs = noop_runs_of(health, pr_rows) if prs_doc is not None else []
    gap_fires = None
    if gap is not None and health is not None:
        gap_fires = {"base": fires_between(health, gap[1], gap[2], False, JOBS),
                     "sprint": fires_between(health, gap[1], gap[2], True, JOBS)}

    # ---------------- runs, releases, evidence
    intakes = [c for c in window if c["parsed"]["job"] == "INTAKE"]
    last_run = collections.OrderedDict()
    for job in ("INTAKE", "SWEEP", "SEED", "ANALYSE", "REVIEW"):
        for c in reversed(before_until):
            p = parse_title(c["subject"])
            if p["job"] == job:
                last_run[job] = (c["when"], p["pr"], p["outcome"])
                break
    sweeps_ever = sum(1 for c in before_until if parse_title(c["subject"])["job"] == "SWEEP")
    evidence = []
    for c in window:
        for status, path in c["changes"]:
            m = EVIDENCE_INCOMPLETE_RE.match(path)
            if status == "A" and m:
                evidence.append({"key": m.group("key"), "date": m.group("date"), "path": path,
                                 "pr": c["parsed"]["pr"], "outcome": c["parsed"]["outcome"]})

    # Row files: when each pending one landed (its last add on the first-parent line).
    row_added = {}
    for c in before_until:
        for status, _o, _n, path in c["raw"]:
            if status == "A" and path.startswith("queue/rows/"):
                row_added[path] = c["when"]
    for entry in list(en["overlay"].values()) + en["keyless_rows"]:
        entry["merged"] = row_added.get(entry["path"])

    # ---------------- held zones: a SWEEP's change (J11) is Jakub's to read; a memo's is FYI
    zone_changes, seen_zone = [], set()
    for z in sweep_zone_changes(repo, window):
        zone_changes.append({"key": z["key"], "from": z["from"], "to": z["to"], "when": z["when"], "kind": "sweep",
                             "source": "%s (PR %s)" % (z["source"], z["pr"])})
        seen_zone.add((norm_key(z["key"]), zone_word(z["to"])))
    for e in events:
        if e["held"]:
            before = e["prior_zone"] or (({r["key"]: r for r in st["rows"]}).get(e["key"], {}).get("zone") or "")
            # the zone word decides (ADD, HOLD, SELL-FLAG): a relabelled reason is no change
            if e["zone"] and before and zone_word(e["zone"]) != zone_word(before):
                zone_changes.append({"key": e["key"], "from": before, "to": e["zone"], "when": e["merged"],
                                     "kind": "memo", "source": "%s memo %s (PR %s)" % (e["job"], e["memo_date"], e["pr"])})
                seen_zone.add((norm_key(e["key"]), zone_word(e["zone"])))
    start_by = {r["key"]: r for r in st["rows"]}
    end_by = {r["key"]: r for r in en["rows"]}
    # Without a start register (register.csv arrived with v307, 2026-10-07) there is nothing to compare.
    for key in sorted(set(k for k, r in end_by.items() if r.get("held") == "true" and start_by)
                      | set(k for k, r in start_by.items() if r.get("held") == "true")):
        a, b = start_by.get(key, {}), end_by.get(key, {})
        if zone_word(a.get("zone")) != zone_word(b.get("zone")) or a.get("held") != b.get("held"):
            if (norm_key(key), zone_word(b.get("zone"))) in seen_zone:
                continue
            zone_changes.append({"key": key, "from": "%s%s" % (a.get("zone") or "-", "" if a.get("held") == "true"
                                                               else " (not held)"),
                                 "to": "%s%s" % (b.get("zone") or "-", "" if b.get("held") == "true" else " (not held)"),
                                 "kind": "register",
                                 "source": "register %s → %s" % (st["fm"].get("register_version", "n/a"),
                                                                 en["fm"].get("register_version", "n/a")),
                                 "when": end["when"]})

    # ---------------- held names and their open items
    open_by_key = {}
    for item in en["items"]:
        if item["key"]:
            open_by_key.setdefault(norm_key(item["key"]), item)
    held_now = []
    for r in en["rows"]:
        if r.get("held") != "true":
            continue
        item = open_by_key.get(norm_key(r["key"]))
        p = en["overlay"].get(r["key"])
        flag_item = item if item and item["sell_flag"] else None
        decision, status = held_status(flag_item)
        held_now.append(collections.OrderedDict([
            ("key", r["key"]), ("company", r["company"]), ("verdict", r["verdict"]), ("section", r["section"]),
            ("zone", r.get("zone", "") or None), ("last_zone_check", r.get("last_zone_check", "") or None),
            ("open_since", flag_item["since"] if flag_item else None), ("status", status), ("decision", decision),
            ("memo_date", r.get("memo_date", "") or None), ("pending", p["label"] if p else None)]))

    # ---------------- verdict changes on WATCH / BUY / HELD names
    pr_by_number = {r["pr"]["number"]: r for r in pr_rows}
    watched_changes = []
    seen = set()
    for e in events:
        if e["changed"] and (e["prior_verdict"] in ("WATCH", "BUY") or e["held"]):
            merger = merger_label((pr_by_number.get(e["pr"]) or {}).get("pr") or {})
            watched_changes.append({"key": e["key"], "company": e["company"], "from": e["prior_verdict"],
                                    "to": e["verdict"], "held": e["held"], "when": e["merged"], "pr": e["pr"],
                                    "source": "%s merged %s by %s (PR %s)" % (e["job"], fmt_when(e["merged"]),
                                                                            merger or "n/a", e["pr"]),
                                    "why": e["deciding"], "memo_model": e["memo_model"], "retest": e["retest_end"],
                                    "retired": e["retired"]})
            seen.add(norm_key(e["key"]))
    for ch in diff["changed"]:
        if norm_key(ch["key"]) in seen:
            continue
        if ch["from_section"] in ("WATCH", "BUY") or norm_key(ch["key"]) in held_start:
            flag = en["dnaf"].get(ch["key"], {})
            watched_changes.append({"key": ch["key"], "company": ch["company"], "from": ch["from_verdict"],
                                    "to": ch["to_verdict"], "held": norm_key(ch["key"]) in held_start,
                                    "when": end["when"], "pr": None,
                                    "source": "register %s → %s (memo %s → %s)" % (
                                        st["fm"].get("register_version", "n/a"), en["fm"].get("register_version", "n/a"),
                                        ch["from_memo"], ch["to_memo"]),
                                    "why": "; ".join("%s %s" % (g, ch["to"][g]) for g in ("past", "future", "sf")),
                                    "memo_model": "", "retest": "", "retired": bool(flag.get("retired"))})

    superseded = [e for e in events if e["superseded_model"]]
    for e in superseded:
        e["on_retest_block"] = norm_key(e["key"]) in en["retest_union"]

    ctx = {
        "repo": repo, "ref": ref, "ref_sha": ref_sha, "ref_time": ref_time, "since": since, "until": until,
        "prior_since": prior_since, "report_date": report_date, "start_date": start_date,
        "period_label": period_label(since, until), "iso_week": iso_week_label(since, until),
        "start": start, "end": end, "window": window, "st": st, "en": en, "releases": releases,
        "timeline": timeline, "live_start": live_start, "live_end": live_end, "events": events,
        "prior_events": prior_events, "new_watch": new_watch(events), "new_watch_prior": new_watch(prior_events),
        "analyses": [e for e in events if e["job"] == "ANALYSE"], "reviews": [e for e in events if e["job"] == "REVIEW"],
        "verdict_mix": collections.Counter(e["verdict"] for e in events), "diff": diff, "weekly": weekly,
        "prs_doc": prs_doc, "pr_rows": pr_rows, "by_job": by_job, "by_job_all": by_job_all,
        "by_job_prior": by_job_prior, "reopened": reopened, "open_old": open_old,
        "finished_waiting": finished_waiting, "running_old": running_old, "held_prs": held_prs, "stopped": stopped,
        "incomplete_prs": incomplete_prs, "incomplete_merged": [c for c in window if c["parsed"]["kind"] == "incomplete"],
        "abandoned": abandoned, "merged_after_ref": merged_after_ref, "merged_after_until": merged_after_until,
        "stale": stale, "merged_by_missing": merged_by_missing, "latency_bot": latency_bot,
        "latency_human": latency_human, "latency_human_prior": latency_human_prior, "gap": gap, "gap_fires": gap_fires,
        "day_grid": day_grid, "health": health, "health_problem": health_problem, "noop_runs": noop_runs,
        "workflow_failures": [f for f in workflow_failures if in_window(f[0])], "holds": holds,
        "intakes": intakes, "last_run": last_run, "sweeps_ever": sweeps_ever, "evidence": evidence,
        "zone_changes": zone_changes, "held_now": held_now, "open_items_parsed": en["items"],
        "watched_changes": watched_changes, "superseded": superseded,
    }
    ctx["attention"] = attention(ctx)
    return ctx


# ------------------------------------------------------------------ attention lists

def px_date_profile(rows):
    """'2026-10-05 ×40, 2026-10-02 ×27, 2026-10-07 (HLMA.L), …': the Px dates of the rows, most
    common first, naming the keys of a date that at most two rows carry."""
    by_date = collections.defaultdict(list)
    for r in rows:
        by_date[r["px_date"] if reg.DATE_RE.match(r["px_date"] or "") else "no date"].append(r["key"])
    parts = []
    for date, keys in sorted(by_date.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        if len(keys) <= 2:
            parts.append("%s (%s)" % (date, ", ".join(sorted(keys))))
        else:
            parts.append("%s ×%d" % (date, len(keys)))
    return ", ".join(parts)


def attention(c):
    """{'Decide': [...], 'Fix': [...], 'Know': [...]}: each item {severity, item, detail, action,
    since (date or datetime or None)}, ranked by severity, then oldest first, then item."""
    decide, fix, know = [], [], []
    en, rd = c["en"], c["report_date"]

    def add(target, severity, item, detail, action, since):
        target.append({"severity": severity, "item": item, "detail": detail, "action": action, "since": since})

    def days_since(day_text):
        try:
            return (rd - datetime.date.fromisoformat(day_text)).days
        except (TypeError, ValueError):
            return None

    def age_text(day_text):
        age = days_since(day_text)
        return "%s (%s d at the report date)" % (day_text or "n/a", age if age is not None else "n/a")

    # ---------------- Decide: only Jakub can act.
    held_keys = {norm_key(h["key"]): h for h in c["held_now"]}
    for item in c["open_items_parsed"]:
        held = held_keys.get(norm_key(item["key"]))
        cap = " (over the 7-entry cap)" if item["over_cap"] else ""
        if item["held"] and item["sell_flag"]:
            zone = (held or {}).get("zone") or "SELL-FLAG"
            pend = (held or {}).get("pending")
            if item["hold_on"] or item["deferred"]:
                status = (held or {}).get("status") or "held by your decision"
                add(know, "low", "%s held %s — %s" % (item["key"], zone, status),
                    "Flag open since %s; last zone check %s%s. Open item: %s" % (
                        item["since"] or "n/a", (held or {}).get("last_zone_check") or "n/a",
                        ("; " + pend) if pend else "", site.clip(item["text"], 200)),
                    "None: your logged decision stands; log any change and the realised outcome in the Open "
                    "items line.", item["hold_on"] or item["deferred_on"] or item["since"])
            else:
                add(decide, "high", "%s held %s — your decision is pending" % (item["key"], zone),
                    "Pending since %s; last zone check %s%s. Open item: %s" % (
                        age_text(item["since"]), (held or {}).get("last_zone_check") or "n/a",
                        ("; " + pend) if pend else "", site.clip(item["text"], 200)),
                    "Decide on the flag and log the decision in the Open items line (MODEL §7.1, §8.7 item 11).",
                    item["since"])
        elif item["user_call"] or item["over_cap"]:
            add(decide, "medium", "%s — open item asks for your call%s" % (item["key"] or "-", cap),
                "Since %s. Open item: %s" % (age_text(item["since"]), site.clip(item["text"], 220)),
                "Make the call in an attended session (register writes via gsc_register.py only).", item["since"])
    for h in c["held_prs"]:
        if h["state"] == "open" and h["kind"] not in ("stopped", "blocked"):
            add(decide, "high", "PR %s %s held for your merge" % (
                h["number"], " ".join(x for x in (h["job"], h["key"]) if x)),
                "%s; why held: %s; waiting %s h at the end of the period." % (
                    site.clip(h["outcome"], 160) or "-", h["why"], h["wait_hours"]),
                "Review the PR and merge or close it (gsc-automerge holds it for you).", h["created"])
    for z in c["zone_changes"]:
        if z["kind"] == "sweep":
            add(decide, "high", "%s held zone %s → %s (SWEEP)" % (z["key"], z["from"], z["to"]),
                "%s; the SWEEP merged with it (J11) and raised a review request." % z["source"],
                "Read the zone change; the review request runs at REVIEW priority 1a (MODEL §7.2).", z.get("when"))
    buy_keys = set()
    for e in c["events"]:
        if e["verdict"] == "BUY":
            buy_keys.add(norm_key(e["key"]))
            add(decide, "high", "%s BUY (%s, memo %s)" % (e["key"], e["job"], e["memo_date"] or "n/a"),
                "%s; merged %s (%s)." % (e["deciding"], fmt_when(e["merged"]), pr_ref(e["pr"])),
                "Framework output, not advice: read the memo; position events are yours (MODEL §7.3).", e["merged"])
    for r in en["rows"]:
        if r["section"] == "BUY" and norm_key(r["key"]) not in buy_keys:
            add(decide, "medium", "%s is BUY in the register (memo %s)" % (r["key"], r.get("memo_date") or "n/a"),
                "Px %s %s (%s) vs trigger %s." % (r.get("px"), r.get("px_unit"), r.get("px_date"), r.get("trigger")),
                "Framework output, not advice: read the memo; position events are yours (MODEL §7.3).",
                r.get("memo_date") or None)

    # ---------------- Fix: the system.
    if c.get("health_problem"):
        add(fix, "low", "Schedule health unreadable", c["health_problem"],
            "None for the report; check the WEEKLY routine's schedule read.", None)
    h = c["health"]
    if h is not None:
        base_fail = [t for t in h["failures"] if not t["sprint"]]
        sprint_fail = [t for t in h["failures"] if t["sprint"]]
        for t in base_fail:
            add(fix, "high", "%s routine '%s': last run FAILED %s" % (t["job"], t["name"], t["failure_reason"] or "n/a"),
                "Fired %s, finished %s (only the last run per routine is visible in the schedule read)." % (
                    fmt_when(t["last_fired_at"], True), fmt_when(t["last_finished_at"])),
                "Check usage limits; re-fire the routine once capacity is back.", t["last_fired_at"])
        if sprint_fail:
            jobs = collections.Counter(t["job"] for t in sprint_fail)
            reasons = collections.Counter(t["failure_reason"] or "n/a" for t in sprint_fail)
            sprint_total = sum(1 for t in h["triggers"] if t["sprint"] and t["enabled"])
            fires = {j: h["by_job"][j]["scheduled_sprint"] for j in JOBS if h["by_job"][j]["scheduled_sprint"]}
            add(fix, "medium", "Sprint routines: %d of %d last runs FAILED (%s)" % (
                len(sprint_fail), sprint_total, ", ".join("%s %d" % kv for kv in sorted(reasons.items()))),
                "By job: %s; last runs %s – %s. Sprint fires scheduled in the period: %s. Only the last run per "
                "routine is visible." % (", ".join("%s %d" % kv for kv in sorted(jobs.items())),
                                         fmt_when(min(t["last_fired_at"] for t in sprint_fail if t["last_fired_at"])
                                                  if any(t["last_fired_at"] for t in sprint_fail) else None),
                                         fmt_when(max(t["last_fired_at"] for t in sprint_fail if t["last_fired_at"])
                                                  if any(t["last_fired_at"] for t in sprint_fail) else None),
                                         ", ".join("%s %d" % kv for kv in fires.items()) or "0"),
                "Disable or re-time the sprint routines, or raise the usage limit.",
                min((t["last_fired_at"] for t in sprint_fail if t["last_fired_at"]), default=None))
    for t in c.get("noop_runs") or []:
        add(fix, "medium" if t["sprint"] else "high", "%s routine '%s': likely no-op run" % (t["job"], t["name"]),
            "Last run SUCCEEDED in %d s (fired %s, finished %s); no %s PR was opened from its fire to %d min after it "
            "finished%s. A session that cannot see the repository ends this way (inference)." % (
                t["last_duration_s"], fmt_when(t["last_fired_at"], True), fmt_when(t["last_finished_at"]), t["job"],
                int(NOOP_GRACE.total_seconds() // 60),
                ", and none was open at its fire" if t["job"] in NOOP_OPEN_PR_JOBS else ""),
            "Check the routine's repository and environment in the Routines settings, then fire it once and watch "
            "for its PR.", t["last_fired_at"])
    sweep = c["last_run"].get("SWEEP")
    if sweep is None or c["until"] - sweep[0] > SWEEP_STALE:
        watch = [r for r in en["shortlist"] if r["section"] in ("WATCH", "BUY")]
        sweep_fail = [t for t in (h or {}).get("failures", []) if t["job"] == "SWEEP"]
        add(fix, "high", "SWEEP stale: no SWEEP merged for %s" % (fmt_span(c["until"] - sweep[0]) if sweep else "ever"),
            "Last SWEEP merged %s (PR %s; %d SWEEP%s merged ever). Px dates of the %d WATCH/BUY rows at the report "
            "date: %s; %d are over %d d old.%s" % (
                fmt_when(sweep[0], True) if sweep else "never", sweep[1] if sweep else "n/a", c["sweeps_ever"],
                "" if c["sweeps_ever"] == 1 else "s", len(watch), px_date_profile(watch) or "none",
                sum(1 for r in watch if r["px_age_d"] is None or r["px_age_d"] > RELIABLE_PX_DAYS), RELIABLE_PX_DAYS,
                (" The SWEEP routine's last run, %s, FAILED %s." % (fmt_when(sweep_fail[0]["last_fired_at"]),
                                                                    sweep_fail[0]["failure_reason"] or "n/a"))
                if sweep_fail else ""),
            "Get a SWEEP run through; until then every distance and status in the shortlist is that old.",
            sweep[0] if sweep else None)
    if c["gap"] is not None and c["gap"][0] > ROUTINE_GAP:
        g, gf = c["gap"], c["gap_fires"]
        add(fix, "medium", "Run gap: no routine PR for %s" % fmt_span(g[0]),
            "No routine PR opened from %s to %s%s." % (
                fmt_when(g[1]), fmt_when(g[2]),
                (" while %d base and %d sprint fires were scheduled in that span" % (gf["base"], gf["sprint"]))
                if gf else ""),
            "Check the routine runs in that span (usage limit, environment, claims).", g[1])
    for r in c["stopped"]:
        add(fix, "high", "%s run: %s (PR %s)" % (r["parsed"]["kind"].capitalize(),
                                               " ".join(x for x in (r["parsed"]["job"], r["parsed"]["key"]) if x),
                                               r["pr"]["number"]),
            "%s: %s; opened %s%s." % (r["parsed"]["kind"], r["parsed"]["reason"] or "-", fmt_when(r["created"]),
                                     "; open, held for your merge or close" if r["closed"] is None or r["closed"] >= c["until"]
                                     else ""),
            "Read the run's reason; unblock it, then merge or close the PR.", r["created"])
    for r in c["incomplete_prs"]:
        add(fix, "medium", "%s %s INCOMPLETE (PR %s)" % (r["parsed"]["key"] or "-", r["parsed"]["job"], r["pr"]["number"]),
            "%s; %s." % (r["parsed"]["gap"] or "-", ("merged %s" % fmt_when(r["merged"])) if r["merged"] is not None
                         else ("closed %s" % fmt_when(r["closed"]) if r["closed"] is not None else "open")),
            "An attended re-test or group build may be owed (see the row file's TODO addition).",
            r["merged"] or r["closed"] or r["created"])
    for r in c["abandoned"]:
        add(fix, "low", "%s %s %s (PR %s)" % (r["parsed"]["key"] or "-", r["parsed"]["job"], r["parsed"]["tag"],
                                             r["pr"]["number"]),
            "Closed %s; opened %s." % (fmt_when(r["closed"]), fmt_when(r["created"])),
            "None if a later run of the key finished; otherwise find out why the run stopped.", r["closed"])
    for when, what, why in c["workflow_failures"]:
        add(fix, "medium", "Workflow failure: %s" % what, "%s (recorded %s on '%s')." % (site.clip(why, 200),
                                                                                          fmt_when(when), NEEDS_TITLE),
            "Read the workflow run; re-run it once the cause is fixed.", when)
    pending_rows = [p for p in en["overlay"].values()] + en["keyless_rows"]
    if pending_rows:
        oldest = min((p["merged"] for p in pending_rows if p.get("merged")), default=None)
        intake = c["last_run"].get("INTAKE")
        waiting = [p for p in pending_rows if p.get("merged") and c["until"] - p["merged"] > ROWS_WAITING]
        lag = bool(waiting) and (intake is None or c["until"] - intake[0] > INTAKE_STALL)
        nxt = None
        if c["health"] is not None:
            nxt = min((f for t in c["health"]["doc"]["triggers"] if t["enabled"] and t["job"] == "INTAKE"
                       for f in cron_fires(t["cron"], c["until"], c["until"] + datetime.timedelta(days=2))),
                      default=None)
        changing = [p for p in en["overlay"].values() if p["changes"]]
        add(fix, "high" if lag else "low",
            "Register lag: %d merged row files not yet applied" % len(pending_rows),
            "%d change a register verdict (%s); %d add a new key; last INTAKE %s; %d waiting over 6 h%s%s." % (
                len(changing), ", ".join("%s %s → %s" % (p["key"], p["register_verdict"], p["verdict"])
                                         for p in changing) or "none",
                sum(1 for p in en["overlay"].values() if p["new_key"]),
                fmt_when(intake[0], True) if intake else "never", len(waiting),
                "; no INTAKE merged for over 30 h" if lag else "",
                ("; next INTAKE fire %s" % fmt_when(nxt, True)) if nxt else ""),
            "None if INTAKE runs on schedule; otherwise run INTAKE.", oldest)
    waiting = c["finished_waiting"]
    if len(waiting) > STALL_COUNT:
        add(fix, "high", "Stall: %d finished routine PRs waiting over 24 h" % len(waiting),
            "INTAKE's stall test (more than %d): %s." % (STALL_COUNT, ", ".join(pr_ref(r["pr"]["number"])
                                                                               for r in waiting[:20])
                                                        + (" …" if len(waiting) > 20 else "")),
            "Check gsc-automerge and the guard runs; merge or close the held ones.",
            min(r["created"] for r in waiting))
    held_open = {h["number"] for h in c["held_prs"] if h["state"] == "open"}
    stopped_open = {r["pr"]["number"] for r in c["stopped"]}
    for r in c["open_old"]:
        n = r["pr"]["number"]
        if n in held_open or n in stopped_open or (r in waiting and len(waiting) > STALL_COUNT):
            continue
        add(fix, "medium", "Open PR %s older than 24 h" % n,
            "%s (opened %s)." % (r["parsed"]["title"], fmt_when(r["created"])),
            "Find out why it has not finished or merged.", r["created"])
    for r in c["running_old"]:
        if r in c["open_old"]:
            continue
        add(fix, "low", "PR %s still [running] after 6 h" % r["pr"]["number"],
            "%s (opened %s); INTAKE closes it as [abandoned]." % (r["parsed"]["title"], fmt_when(r["created"])),
            "None: INTAKE's abandoned-claim sweep handles it.", r["created"])

    # ---------------- Know: for your information.
    for r in en["ranked"]:
        if r["status"] in ("IN RANGE", "NEAR"):
            add(know, "high" if r["status"] == "IN RANGE" else "medium", "%s %s" % (r["key"], r["status"]),
                "Px %s %s (%s, %s d old) vs trigger %s: %s%s." % (
                    r["px"], r["px_unit"], r["px_date"], r["px_age_d"], r["trigger"],
                    site.fmt_signed_pct(r["distance"]), "" if r["reliable"] else " (not reliable: see shortlist)"),
                "Framework status only (MODEL §8.3); a REVIEW confirms it.", r["px_date"])
    for w in c["watched_changes"]:
        sev = "high" if w["held"] else ("low" if w["retired"] else "medium")
        flag = (" — " + RETIRED_FLAG) if w["retired"] else ""
        add(know, sev, "%s %s → %s%s" % (w["key"], w["from"], w["to"], " (provisional)" if w["retired"] else ""),
            "%s; why: %s%s%s%s." % (w["source"], w["why"],
                                    ("; memo under MODEL %s" % w["memo_model"]) if w["memo_model"] else "",
                                    ("; " + w["retest"]) if w["retest"] else "", flag),
            "None: the re-run is queued (▶ Method re-tests)." if w["retired"] else "None (FYI).", w["when"])
    for z in c["zone_changes"]:
        if z["kind"] != "sweep":
            add(know, "medium", "%s held zone %s → %s" % (z["key"], z["from"], z["to"]), z["source"], "None (FYI).",
                z.get("when"))
    for e in c["superseded"]:
        if not e["on_retest_block"]:
            add(know, "low", "%s memo merged under a superseded MODEL" % e["key"],
                "%s written under %s, merged %s while %s was live; not on a ▶ Method re-tests block at the end." % (
                    e["verdict"], e["memo_model"], fmt_when(e["merged"]), e["live_model"]),
                "None: the live MODEL's rules apply at the key's next REVIEW (a run finishes under the version it "
                "read, MODEL §0).", e["merged"])
    ow = en["overdue_watch"]
    if ow:
        rows = {r["key"]: r for r in en["rows"]}
        due = sorted(((reg.review_last_day(rows[k].get("next_review_short", "")), k) for k in ow))
        add(know, "low", "%d WATCH reviews overdue" % len(ow),
            "Next review passed before %s: %s." % (rd.isoformat(), ", ".join(
                "%s (%s)" % (k, rows[k].get("next_review_short", "")) for _d, k in due)),
            "None: REVIEW picks overdue names by its own order.", due[0][0])
    for t in c["timeline"]:
        retired_n = sum(1 for f in en["dnaf_after"].values() if f["retired"])
        add(know, "low", "MODEL %s live from %s" % (t[2], fmt_when(t[0])),
            "%s; %d DNAF rows (incl. pending) now rest on grounds it retired." % (
                site.clip(PR_NUM_SUFFIX_RE.sub("", t[4]), 140), retired_n),
            "None: re-runs are queued in ▶ Method re-tests.", t[0])

    def sort_key(x):
        since = x["since"]
        if isinstance(since, datetime.datetime):
            stamp = since.astimezone(UTC).isoformat()
        elif since:
            stamp = str(since)
        else:
            stamp = "9999"
        return (SEVERITIES.index(x["severity"]), stamp, x["item"])
    return collections.OrderedDict([("Decide", sorted(decide, key=sort_key)), ("Fix", sorted(fix, key=sort_key)),
                                    ("Know", sorted(know, key=sort_key))])


# ------------------------------------------------------------------ datasets

def num(value):
    """A register or front-matter text as a JSON number (int when integral); None when not a number."""
    if isinstance(value, Decimal):
        d = value
    elif isinstance(value, (int, float)) and not isinstance(value, bool):
        d = Decimal(str(value))
    elif reg.is_num(value or ""):
        d = Decimal(value)
    else:
        return None
    if d == d.to_integral_value() and d.as_tuple().exponent >= 0:
        return int(d)
    return float(d)


def txt(value):
    """A text field for the datasets: None for '', '-' (owed) and 'n/a'; anything else as is."""
    value = (value or "").strip() if isinstance(value, str) else value
    return None if value in (None, "", "-", "n/a") else value


def iso_value(value):
    if isinstance(value, datetime.datetime):
        return iso_prague(value)
    if isinstance(value, datetime.date):
        return value.isoformat()
    return value or None


def dnaf_split(flags):
    """(retired, awaiting RETIRED keys, live) of a DNAF flag map: DNAF not live = retired grounds +
    awaiting RETIRED."""
    retired = sum(1 for f in flags.values() if f["retired"])
    awaiting = sorted(k for k, f in flags.items() if f.get("awaiting_retired"))
    return retired, awaiting, len(flags) - retired - len(awaiting)


def datasets(c, generated_at):
    """{dataset id: [flat row dicts]} for every DATASET_IDS entry but summary (see summary_rows)."""
    st, en = c["st"], c["en"]
    h = c["health"]
    out = collections.OrderedDict()
    lens = "read with the MODEL %s lens" % c["live_end"]

    # kpis
    analytic_open = sum(c["by_job_all"][j]["opened"] for j in ANALYTIC_JOBS)
    analytic_open_prior = sum(c["by_job_prior"][j]["opened"] for j in ANALYTIC_JOBS)
    analytic_runs = sum(c["by_job_all"][j]["runs"] for j in ANALYTIC_JOBS)
    reopened = [x for x in c["reopened"] if x["prs"] and any(
        pr["pr"]["number"] in x["prs"] and pr["parsed"]["job"] in ANALYTIC_JOBS for pr in c["pr_rows"])]
    base = sum(h["by_job"][j]["scheduled_base"] for j in ANALYTIC_JOBS) if h else None
    sprint = sum(h["by_job"][j]["scheduled_sprint"] for j in ANALYTIC_JOBS) if h else None
    retired_end, awaiting_end, live_end_n = dnaf_split(en["dnaf_after"])
    retired_start = sum(1 for f in st["dnaf_after"].values() if f["retired"])
    pw = "the preceding window of equal length"
    lh, lhp = c["latency_human"], c["latency_human_prior"]
    kpis = [
        ("Memos merged (period)", len(c["events"]), len(c["prior_events"]), "memos",
         "git: memo files added under memos/ in [since, until), moves and re-keys excluded; prior = " + pw),
        ("New WATCH (period)", len(c["new_watch"]), len(c["new_watch_prior"]), "memos",
         "memos merged with verdict WATCH whose prior memo was not WATCH; prior = " + pw),
        ("DNAF memos merged (period)", sum(1 for e in c["events"] if e["verdict"] == "DNAF"),
         sum(1 for e in c["prior_events"] if e["verdict"] == "DNAF"), "memos",
         "memos merged with verdict DNAF; prior = " + pw),
        ("DNAF memos merged on retired grounds (period)", sum(1 for e in c["events"] if e["retired"]),
         sum(1 for e in c["prior_events"] if e["retired"]), "memos",
         "DNAF memos merged in the period whose Gate-0 ground %s retired (%s), %s; prior = %s, read the "
         "same way" % (RETIRED_GATE0_VERSION, "; ".join(n for n, _p in RETIRED_GATE0_GROUNDS), lens, pw)),
        ("WATCH (register)", en["counts"]["WATCH"], st["counts"]["WATCH"], "keys",
         "register.csv section at the end; prior = at the start"),
        ("WATCH after pending rows", en["counts_after"]["WATCH"], st["counts_after"]["WATCH"], "keys",
         "register.csv with every merged, unapplied row file's memo verdict applied; prior = the same at the start"),
        ("BUY (register)", en["counts"]["BUY"], st["counts"]["BUY"], "keys", "register.csv section; prior = start"),
        ("IN RANGE", en["status_counts"]["IN RANGE"], st["status_counts"]["IN RANGE"], "keys",
         "status_hint at register Px (MODEL §8.3), WATCH/BUY rows, pending-change rows excluded; prior = start"),
        ("NEAR", en["status_counts"]["NEAR"], st["status_counts"]["NEAR"], "keys",
         "status_hint at register Px, WATCH/BUY rows, pending-change rows excluded; prior = start"),
        ("Keys in register", en["counts"]["keys"], st["counts"]["keys"], "keys", "register.csv rows; prior = start"),
        ("Keys after pending rows", en["counts_after"]["keys"], st["counts_after"]["keys"], "keys",
         "register.csv rows plus pending new keys; prior = start"),
        ("DNAF on retired grounds (incl. pending)", retired_end, retired_start, "keys",
         "register DNAF rows after pending whose memo is below %s and whose §1 ground %s retired, %s; prior = at "
         "the start, read the same way" % (RETIRED_GATE0_VERSION, RETIRED_GATE0_VERSION, lens)),
        ("DNAF after pending rows", en["counts_after"]["DNAF"], st["counts_after"]["DNAF"], "keys",
         "register DNAF rows with pending verdicts applied; prior = start. Of the %d at the end: %d on retired "
         "grounds, %d awaiting RETIRED%s, %d live Gate-0 verdicts" % (
             en["counts_after"]["DNAF"], retired_end, len(awaiting_end),
             (" (%s)" % ", ".join(awaiting_end)) if awaiting_end else "", live_end_n)),
        ("Re-test debt (distinct keys)", len(en["retest_union"]), len(st["retest_union"]), "keys",
         "keys on the queue/TODO.md ▶ Method re-tests blocks; prior = start"),
        ("Median WATCH distance to trigger", num(en["watch_distance_median"]), num(st["watch_distance_median"]), "%",
         "median of (Px ÷ trigger − 1) × 100 over priced WATCH rows, pending-change rows excluded; prior = start"),
        ("Median WATCH Px age", num(en["watch_age_median"]), num(st["watch_age_median"]), "days",
         "median days from px_date to the report date (%s) over priced WATCH rows, pending-change rows excluded; "
         "prior measured on %s, the day before the period" % (c["report_date"].isoformat(), c["start_date"].isoformat())),
        ("Analytic PRs opened (ANALYSE + REVIEW)", analytic_open, analytic_open_prior, "PRs",
         "PRs created in the period; %d PRs are %d runs%s; prior = %s" % (
             analytic_open, analytic_runs,
             (" (%s)" % "; ".join("PRs %s from one %s run" % (" and ".join(str(n) for n in x["prs"]), x["key"] or "-")
                                  for x in reopened)) if reopened else "", pw)),
        ("Analytic fires scheduled — base", base, None, "fires",
         "schedule read crons expanded over the period (current routine list assumed for the whole period); "
         "prior n/a"),
        ("Analytic fires scheduled — sprint", sprint, None, "fires", "as above, sprint routines; prior n/a"),
        ("Analytic runs per scheduled fire", num(q1(Decimal(analytic_runs) * 100 / (base + sprint)))
         if h and (base + sprint) else None, None, "%",
         ("%d analytic runs ÷ %d scheduled fires (%d base + %d sprint) × 100; current routine list assumed for "
          "the whole period" % (analytic_runs, base + sprint, base, sprint)) if h and (base + sprint) else
         "analytic runs ÷ scheduled fires × 100; n/a without a schedule read"),
        ("Held PR median wait", num(lh["median_h"]), num(lhp["median_h"]), "h",
         "routine PRs merged by Jakub in the period, created → merged, only PRs opened since gsc-automerge's first "
         "merge (PR 92, 2026-10-08)%s; prior = %s, the same way, null without a comparable merge" % (
             (": %d PRs, %s–%s h" % (lh["count"], lh["min_h"], lh["max_h"])) if lh["count"] else ": none", pw)),
    ]
    out["kpis"] = [collections.OrderedDict([("order", i + 1), ("metric", m), ("value", v), ("prior", p),
                                            ("unit", u), ("basis", b)]) for i, (m, v, p, u, b) in enumerate(kpis)]

    # attention
    rows, rank = [], 0
    for name, items in c["attention"].items():
        for x in items:
            rank += 1
            rows.append(collections.OrderedDict([("rank", rank), ("list", name), ("severity", x["severity"]),
                                                 ("item", x["item"]), ("detail", x["detail"]),
                                                 ("action", x["action"]), ("since", iso_value(x["since"]))]))
    out["attention"] = rows

    # shortlist
    out["shortlist"] = [collections.OrderedDict([
        ("key", r["key"]), ("company", r["company"]), ("region", r["region"]), ("px", num(r["px"])),
        ("px_unit", txt(r["px_unit"])), ("px_date", r["px_date"] if reg.DATE_RE.match(r["px_date"] or "") else None),
        ("px_age_d", r["px_age_d"]), ("trigger", num(r["trigger"])), ("trigger_basis", txt(r["trigger_basis"])),
        ("distance_pct", num(q1(r["distance"] * 100)) if r["distance"] is not None else None),
        ("needs_fall_pct", num(q1(r["needs_fall"] * 100)) if r["needs_fall"] is not None else None),
        ("mcap_fcf", num(r["mcap_fcf"])), ("ev_oi", num(r["ev_oi"])), ("status", r["status"]),
        ("memo_date", txt(r["memo_date"])), ("model_version", txt(r["model_version"])),
        ("retest_owed", bool(r["retest"])), ("all_cash_trigger", r["all_cash"]), ("pending", r["pending"]),
        ("reliable", r["reliable"]), ("next_review", txt(r["next_review"]))])
        for r in sorted(en["shortlist"], key=lambda r: (r["pending_change"], r["distance"] is None,
                                                        r["distance"] or 0, r["key"]))]

    # changes
    pr_by_number = {r["pr"]["number"]: r["pr"] for r in c["pr_rows"]}
    out["changes"] = [collections.OrderedDict([
        ("key", e["key"]), ("company", e["company"]), ("job", e["job"]),
        ("from_verdict", None if e["job"] == "ANALYSE" else e["prior_verdict"]), ("to_verdict", e["verdict"]),
        ("deciding", e["deciding"]), ("ground_retired", e["retired"]), ("model_version", txt(e["memo_model"])),
        ("merged_at", iso_prague(e["merged"])), ("merged_by", merger_label(pr_by_number.get(e["pr"]) or {})),
        ("pr", e["pr"])]) for e in c["events"]]

    out["weekly"] = [collections.OrderedDict(w) for w in c["weekly"]]

    # pipeline
    out["pipeline"] = []
    for job in JOBS:
        cnt = c["by_job_all"][job]
        hj = h["by_job"][job] if h else None
        out["pipeline"].append(collections.OrderedDict([
            ("job", job), ("scheduled_base", hj["scheduled_base"] if hj else None),
            ("scheduled_sprint", hj["scheduled_sprint"] if hj else None), ("prs_opened", cnt["opened"]),
            ("merged_auto", cnt["merged_by_bot"]), ("merged_jakub", cnt["merged_by_human"]),
            ("closed_unmerged", cnt["closed_unmerged"]),
            ("last_run_failed_usage_limit", hj["usage_limit"] if hj else None),
            ("triggers", hj["triggers"] if hj else None)]))

    # coverage
    total = len(en["rows"])
    cov = collections.OrderedDict((r, collections.Counter()) for r in REPORT_REGIONS)
    for row in en["rows"]:
        cnt = cov[region_of(row["key"])[1]]
        cnt["keys"] += 1
        cnt["watch"] += row["section"] == "WATCH"
        cnt["avoid"] += row["verdict"] == "AVOID"
        cnt["dnaf"] += row["section"] == "DNAF"
    out["coverage"] = [collections.OrderedDict([
        ("region", r), ("keys", n["keys"]), ("watch", n["watch"]), ("avoid", n["avoid"]), ("dnaf", n["dnaf"]),
        ("share_pct", num(q1(Decimal(n["keys"]) * 100 / total)) if total else None)]) for r, n in cov.items()]

    # backlog
    def lines(state, prefix):
        return next((n for t, n in state["retest_lines"].items() if t.startswith(prefix)), 0)
    st_pending = len(st["overlay"]) + len(st["keyless_rows"])
    en_pending = len(en["overlay"]) + len(en["keyless_rows"])
    blocks = sorted({t for t in list(st["retest_lines"]) + list(en["retest_lines"])},
                    key=lambda t: (version_tuple(t) or (0, 0, 0), t))
    def partial(state, title=None):
        return [x for t, xs in state["retest_partial"].items() if title is None or t == title for x in xs]

    def partial_note(title):
        found = partial(en, title)
        return ("; %d marked partial at the end, still open: %s" % (
            len(found), ", ".join("%s (%s)" % (k, d) for k, d, _e in found))) if found else ""
    backlog = [(block_label(t), lines(st, t), lines(en, t), "lines",
                "bullets in queue/TODO.md %s%s" % (t, partial_note(t))) for t in blocks]
    st_partial, en_partial = partial(st), partial(en)
    if st_partial or en_partial:
        backlog.append(("Re-test lines marked partial", len(st_partial), len(en_partial), "lines",
                        "▶ Method re-tests lines a run left part-done (' — partial {date}'), counted open above; end: "
                        + (", ".join("%s (%s%s)" % (k, d, (", " + e) if e else "") for k, d, e in en_partial)
                           or "none")))
    st_items, en_items = st["items"], en["items"]
    backlog += [
        ("Distinct re-test keys", len(st["retest_union"]), len(en["retest_union"]), "keys",
         "keys on any ▶ Method re-tests block"),
        ("WATCH keys owing a re-test", len(st["watch_owed"]), len(en["watch_owed"]), "keys",
         "WATCH rows on a ▶ Method re-tests block newer than their memo's MODEL, register basis (%d of the %d "
         "WATCH rows after pending)" % (len(en["watch_owed_after"]), en["counts_after"]["WATCH"])),
        ("DRAFT_QUEUE open candidates", st["queue"]["open"], en["queue"]["open"], "candidates",
         "queue/DRAFT_QUEUE.md '- [ ]' lines under ## Queue"),
        ("Register open items", len(st_items), len(en_items), "items",
         "open items in queue/TODO.md: the ▶ Open items (register) head block (capped at 7: %d at the end) plus "
         "the lines routed below it over the cap (%d at the end%s)" % (
             len(en["open_items"]), len(en["over_cap"]),
             (": " + ", ".join(i["key"] for i in en_items if i["over_cap"])) if en["over_cap"] else "")),
        ("IDEAS candidates awaiting triage", len(st["ideas"]), len(en["ideas"]), "candidates",
         "bullets in queue/TODO.md ▶ IDEAS candidates (attended triage)"),
        ("Overdue next reviews (all rows)", len(st["overdue_all"]), len(en["overdue_all"]), "rows",
         "next_review_short ended before the state's date (start %s, end %s)" % (c["start_date"], c["report_date"])),
        ("Overdue next reviews (WATCH)", len(st["overdue_watch"]), len(en["overdue_watch"]), "rows",
         "as above, WATCH rows"),
        ("Merged row files pending INTAKE", st_pending, en_pending, "files", "queue/rows/*.md on the ref, README aside"),
    ]
    out["backlog"] = [collections.OrderedDict([("item", i), ("start", s), ("end", e), ("unit", u), ("note", n)])
                      for i, s, e, u, n in backlog]

    out["held"] = [collections.OrderedDict([
        ("key", x["key"]), ("company", x["company"]), ("verdict", x["verdict"]), ("zone", txt(x["zone"])),
        ("last_zone_check", txt(x["last_zone_check"])), ("memo_date", txt(x["memo_date"])),
        ("open_since", x["open_since"]), ("status", x["status"])]) for x in c["held_now"]]

    out["meta"] = [collections.OrderedDict([
        ("period_label", c["period_label"] + ((" (%s)" % c["iso_week"]) if c["iso_week"] else "")),
        ("since", iso_prague(c["since"])), ("until", iso_prague(c["until"])),
        ("report_date", c["report_date"].isoformat()), ("ref_sha", c["ref_sha"]),
        ("ref_time", iso_prague(c["ref_time"])), ("register_from", st["fm"].get("register_version") or None),
        ("register_to", en["fm"].get("register_version") or None), ("model_live", c["live_end"]),
        ("decide", len(c["attention"]["Decide"])), ("fix", len(c["attention"]["Fix"])),
        ("know", len(c["attention"]["Know"])),
        ("generated_at", iso_prague(generated_at)), ("tool_version", TOOL_VERSION)])]
    return out


DATASET_SCHEMA = {
    "kpis": {"order": (int,), "metric": (str,), "value": (int, float, type(None)), "prior": (int, float, type(None)),
             "unit": (str,), "basis": (str,)},
    "attention": {"rank": (int,), "list": (str,), "severity": (str,), "item": (str,), "detail": (str,),
                  "action": (str,), "since": (str, type(None))},
    "shortlist": {"key": (str,), "company": (str,), "region": (str,), "px": (int, float, type(None)),
                  "px_unit": (str, type(None)), "px_date": (str, type(None)), "px_age_d": (int, type(None)),
                  "trigger": (int, float, type(None)), "trigger_basis": (str, type(None)),
                  "distance_pct": (int, float, type(None)), "needs_fall_pct": (int, float, type(None)),
                  "mcap_fcf": (int, float, type(None)), "ev_oi": (int, float, type(None)), "status": (str,),
                  "memo_date": (str, type(None)), "model_version": (str, type(None)), "retest_owed": (bool,),
                  "all_cash_trigger": (bool,), "pending": (str, type(None)), "reliable": (bool,),
                  "next_review": (str, type(None))},
    "changes": {"key": (str,), "company": (str,), "job": (str,), "from_verdict": (str, type(None)),
                "to_verdict": (str,), "deciding": (str,), "ground_retired": (bool,), "model_version": (str, type(None)),
                "merged_at": (str,), "merged_by": (str, type(None)), "pr": (int, type(None))},
    "weekly": {"week": (str,), "week_start": (str,), "analyse": (int,), "review": (int,), "incomplete": (int,),
               "model_releases": (int,), "watch_end": (int, type(None)), "keys_end": (int, type(None)),
               "note": (str, type(None))},
    "pipeline": {"job": (str,), "scheduled_base": (int, type(None)), "scheduled_sprint": (int, type(None)),
                 "prs_opened": (int,), "merged_auto": (int,), "merged_jakub": (int,), "closed_unmerged": (int,),
                 "last_run_failed_usage_limit": (int, type(None)), "triggers": (int, type(None))},
    "coverage": {"region": (str,), "keys": (int,), "watch": (int,), "avoid": (int,), "dnaf": (int,),
                 "share_pct": (int, float, type(None))},
    "backlog": {"item": (str,), "start": (int, type(None)), "end": (int,), "unit": (str,), "note": (str,)},
    "held": {"key": (str,), "company": (str,), "verdict": (str,), "zone": (str, type(None)),
             "last_zone_check": (str, type(None)), "memo_date": (str, type(None)), "open_since": (str, type(None)),
             "status": (str,)},
    "summary": {"order": (int,), "kind": (str,), "text": (str,)},
    "meta": {"period_label": (str,), "since": (str,), "until": (str,), "report_date": (str,), "ref_sha": (str,),
             "ref_time": (str,), "register_from": (str, type(None)), "register_to": (str, type(None)),
             "model_live": (str,), "decide": (int,), "fix": (int,), "know": (int,), "generated_at": (str,),
             "tool_version": (str,)},
}


def check_datasets(data):
    """Problems with the datasets against DATASET_SCHEMA (required keys, no extra keys, types;
    a bool never passes as a number); [] when clean."""
    problems = []
    for name, schema in DATASET_SCHEMA.items():
        rows = data.get(name)
        if not isinstance(rows, list):
            problems.append("%s: not a list" % name)
            continue
        for i, row in enumerate(rows):
            if set(row) != set(schema):
                problems.append("%s[%d]: keys %s" % (name, i, sorted(set(row) ^ set(schema))))
                continue
            for k, types in schema.items():
                v = row[k]
                if isinstance(v, bool) and bool not in types:
                    problems.append("%s[%d].%s: bool" % (name, i, k))
                elif not isinstance(v, types):
                    problems.append("%s[%d].%s: %r" % (name, i, k, type(v).__name__))
    return problems


# ------------------------------------------------------------------ summary, notification, page writes

NUMBER_RE = re.compile(r"\d+(?:[.,]\d+)*")


def number_corpus(data):
    """Every number token printed in the datasets other than summary (NUMBER_RE over their JSON)."""
    found = set()
    for name, rows in data.items():
        if name != "summary":
            found.update(NUMBER_RE.findall(json.dumps(rows, ensure_ascii=False)))
    return found


# A takeaway number next to one of these phrases must equal one of the named kpis values (a number that
# merely appears somewhere in the datasets is not enough for the headline figures).
KPI_PHRASES = (
    (re.compile(r"\b(\d+) memos? merged\b"), ("Memos merged (period)",)),
    (re.compile(r"\b(\d+) new WATCH\b"), ("New WATCH (period)",)),
    (re.compile(r"\b(\d+) (?:(?:names?|rows?|keys?) )?(?:(?:are|is) )?IN RANGE\b"), ("IN RANGE",)),
    (re.compile(r"\b(\d+) (?:(?:names?|rows?|keys?) )?(?:(?:are|is) )?NEAR\b"), ("NEAR",)),
    (re.compile(r"(?<!new )\b(\d+) WATCH\b|\bWATCH (?:at |of |is )?(\d+)\b"),
     ("WATCH (register)", "WATCH after pending rows")),
)
# Private figures (MODEL section 7.4): a price after '@' ('bought X @ 41.20'), average cost, cost basis,
# position size and core numbers, each with the figure that follows. The datasets replace them with
# '[private]' (scrub_private) and a summary sentence that carries one fails the lint.
PRIVATE_RE = re.compile(r"(?i)@\s*[$€£¥]?\s*\d[\d.,]*|\b(?:avg[_ ]?cost|average cost|cost basis|position size|"
                        r"core_[a-z0-9_]+)\b(?:\s*[:=]?\s*[$€£¥]?\s*\d[\d.,]*)?")
# Advice words: buy or sell in any but the framework's capitals (the BUY verdict, the SELL-FLAG zone);
# 'buy zone' is the register's name for the trigger band. Price targets never.
ADVICE_WORD_RE = re.compile(r"(?i)\b(?:buy|sell)(?:s|ing)?\b")
PRICE_TARGET_RE = re.compile(r"(?i)\bprice targets?\b|\btarget prices?\b")


def same_number(token, value):
    try:
        return Decimal(token.replace(",", "")) == Decimal(str(value))
    except Exception:          # a value that is no number
        return False


def sentence_problems(i, row, corpus, kpis=None):
    """Problems with summary sentence i (0-based) against its slot: the fields, order, kind, one plain
    line of at most SUMMARY_MAX_CHARS characters without '#', no advice words, every number in the
    corpus and, in the takeaway, the headline numbers equal to their kpis values ({metric: value})."""
    problems, where = [], "sentence %d" % (i + 1)
    if not isinstance(row, dict) or set(row) != {"order", "kind", "text"}:
        return ["%s: exactly the fields order, kind and text" % where]
    if row["order"] != i + 1 or isinstance(row["order"], bool):
        problems.append("%s: order must be %d" % (where, i + 1))
    if row["kind"] not in SUMMARY_KINDS:
        problems.append("%s: kind %r is not one of %s" % (where, row["kind"], ", ".join(SUMMARY_KINDS)))
    elif i < len(SUMMARY_SLOTS) and row["kind"] != SUMMARY_SLOTS[i]:
        problems.append("%s: kind must be %s (the page's slots: %s)" % (where, SUMMARY_SLOTS[i],
                                                                        ", ".join(SUMMARY_SLOTS)))
    text = row["text"]
    if not isinstance(text, str) or not text.strip():
        problems.append("%s: empty text" % where)
        return problems
    if len(text) > SUMMARY_MAX_CHARS:
        problems.append("%s: %d characters; at most %d" % (where, len(text), SUMMARY_MAX_CHARS))
    if "#" in text:
        problems.append("%s: '#' is not allowed (write 'PR n')" % where)
    if "\n" in text or "\r" in text:
        problems.append("%s: one line only" % where)
    advice = [m.group(0) for m in ADVICE_WORD_RE.finditer(text)
              if not m.group(0).isupper() and not re.match(r"(?i)[- ]zone\b", text[m.end():])]
    if PRIVATE_RE.search(text):
        problems.append("%s: a private figure (%s): never average cost, position size or core numbers" % (
            where, PRIVATE_RE.search(text).group(0)))
    if advice or PRICE_TARGET_RE.search(text):
        problems.append("%s: advice language (%s): say what happened; BUY and SELL-FLAG are framework words" % (
            where, ", ".join(advice + [m.group(0) for m in PRICE_TARGET_RE.finditer(text)])))
    missing = [n for n in NUMBER_RE.findall(text) if n not in corpus]
    if missing:
        problems.append("%s: number(s) not in the datasets: %s" % (where, ", ".join(missing)))
    if kpis is not None and i == 0:
        for pattern, metrics in KPI_PHRASES:
            for m in pattern.finditer(text):
                token = next(g for g in m.groups() if g is not None)
                if not any(same_number(token, kpis.get(metric)) for metric in metrics):
                    problems.append("%s: '%s' does not match kpis %s (%s)" % (
                        where, m.group(0), " or ".join(metrics),
                        ", ".join("n/a" if kpis.get(x) is None else str(kpis.get(x)) for x in metrics)))
    return problems


def lint_summary(rows, corpus, kpis=None):
    """Problems with summary sentences ([] when clean): a JSON array of exactly six {order, kind, text},
    one per slot of the page (SUMMARY_SLOTS, in order); each sentence as sentence_problems checks it.
    kpis ({metric: value}) adds the takeaway's headline check."""
    if not isinstance(rows, list) or not rows:
        return ["the summary must be a non-empty JSON array"]
    problems = []
    if len(rows) != len(SUMMARY_SLOTS):
        problems.append("%d sentences; exactly %d, one per slot of the page (%s)" % (
            len(rows), len(SUMMARY_SLOTS), ", ".join(SUMMARY_SLOTS)))
    for i, row in enumerate(rows):
        problems.extend(sentence_problems(i, row, corpus, kpis))
    return problems


def kpi_values(data):
    """{metric: value} of the kpis dataset (empty when missing)."""
    return {k.get("metric"): k.get("value") for k in data.get("kpis") or [] if isinstance(k, dict)}


def first_item(items, n=1):
    return "; ".join(site.clip(x["item"], 110) for x in items[:n])


def summary_rows(c, data):
    """The tool's own six sentences, one per SUMMARY_SLOTS slot, each passing lint_summary (a sentence
    that would not falls back to plain words for its slot)."""
    kpi = {k["metric"]: k["value"] for k in data["kpis"]}
    meta = data["meta"][0]
    decide, fix, know = c["attention"]["Decide"], c["attention"]["Fix"], c["attention"]["Know"]
    owed = next((b["end"] for b in data["backlog"] if b["item"] == "WATCH keys owing a re-test"), None)

    def num_text(value):
        return "n/a" if value is None else str(value)
    texts = [
        "%s: %s memos merged, %s new WATCH; %s IN RANGE and %s NEAR at register prices; WATCH %s in the register, "
        "%s after pending rows." % (meta["period_label"], num_text(kpi.get("Memos merged (period)")),
                                    num_text(kpi.get("New WATCH (period)")), num_text(kpi.get("IN RANGE")),
                                    num_text(kpi.get("NEAR")), num_text(kpi.get("WATCH (register)")),
                                    num_text(kpi.get("WATCH after pending rows"))),
        ("%d items wait for your decision, first: %s." % (len(decide), first_item(decide, 2))) if decide
        else "Nothing waits for your decision this week.",
        ("%d items to fix, first: %s." % (len(fix), first_item(fix))) if fix else "Nothing to fix this week.",
        ("Next to fix: %s." % first_item(fix[1:])) if len(fix) > 1 else (
            "Schedule health was not read this week." if c["health"] is None else "No other system issue."),
        "Register %s → %s under MODEL %s; %s keys owe a method re-test, %s of them WATCH rows (register basis)." % (
            meta["register_from"] or "n/a", meta["register_to"] or "n/a", meta["model_live"],
            num_text(kpi.get("Re-test debt (distinct keys)")), num_text(owed)),
        ("%d items for your information, first: %s." % (len(know), first_item(know, 2))) if know
        else "Nothing else to report.",
    ]
    fallback = ("See the period and versions above.", "See the Decide list.", "See the Fix list.",
                "See the Fix list.", "See the backlog.", "See the Know list.")
    corpus = number_corpus(data)
    rows = []
    for i, (kind, text) in enumerate(zip(SUMMARY_SLOTS, texts)):
        text = site.clip(re.sub(r"\s+", " ", text.replace("#", "")).strip(), SUMMARY_MAX_CHARS)
        row = collections.OrderedDict([("order", i + 1), ("kind", kind), ("text", text)])
        if sentence_problems(i, dict(row), corpus, kpi):
            row["text"] = fallback[i]
        rows.append(row)
    return rows


def notification_line(data):
    """The WEEKLY notification: 'GSC WEEKLY · {period} · {d} to decide · {f} to fix · {m} memos · {url}',
    one line, at most NOTICE_MAX characters, no '#'."""
    meta = data["meta"][0]
    memos = next((k["value"] for k in data["kpis"] if k["metric"] == "Memos merged (period)"), 0)
    line = "GSC WEEKLY · %s · %d to decide · %d to fix · %s memos · %s" % (
        meta["period_label"], meta["decide"], meta["fix"], memos, WEEKLY_PAGE_URL)
    if len(line) > NOTICE_MAX:
        line = line[:NOTICE_MAX - len(WEEKLY_PAGE_URL) - 3].rstrip() + " · " + WEEKLY_PAGE_URL
    return line.replace("#", "").replace("\n", " ")


def dash_writes(datasets_dir, blobs, versions, at, now=None):
    """The one ArtifactData batch for the weekly page: a pinned 'update' of source and updated per
    dataset id, meta last. Raises ToolError on any bad input, including an --at more than CLOCK_SKEW
    ahead of now (the clock, unless given)."""
    for name in DATASET_IDS:
        path = os.path.join(datasets_dir, name + ".json")
        rows = read_json(path, "dataset")
        if not isinstance(rows, list):
            raise ToolError("dataset %s: not a JSON array" % path)
    if not isinstance(blobs, dict) or set(blobs) != set(DATASET_IDS):
        raise ToolError("--blobs: exactly the ids %s" % ", ".join(DATASET_IDS))
    for name, url in blobs.items():
        if not isinstance(url, str) or not BLOB_URL_RE.fullmatch(url):
            raise ToolError("--blobs %s: %r is not '/_blob/' plus 32 lower-case hex digits" % (name, url))
    if len(set(blobs.values())) != len(blobs):
        raise ToolError("--blobs: the same url twice")
    if not isinstance(versions, dict) or set(versions) != set(DATASET_IDS):
        raise ToolError("--versions: exactly the ids %s" % ", ".join(DATASET_IDS))
    for name, version in versions.items():
        if not isinstance(version, int) or isinstance(version, bool) or version < 1:
            raise ToolError("--versions %s: %r is not a positive integer" % (name, version))
    if not isinstance(at, str) or not ISO_TS_RE.fullmatch(at):
        raise ToolError("--at %r: an ISO time with an offset, e.g. 2026-10-25T08:41:07+01:00" % (at,))
    now = now or datetime.datetime.now(UTC)
    if parse_when(at) > now + CLOCK_SKEW:
        raise ToolError("--at %s is after the clock (%s): the run start {RUN} is never in the future" % (
            at, iso_prague(now.replace(microsecond=0))))
    order = [d for d in DATASET_IDS if d != "meta"] + ["meta"]
    return [collections.OrderedDict([
        ("op", "update"), ("collection", "datasets"), ("doc_id", name),
        ("data", collections.OrderedDict([
            ("source", collections.OrderedDict([("kind", "file"), ("url", blobs[name]), ("name", name + ".json"),
                                                ("format", "json")])),
            ("updated", collections.OrderedDict([("at", at), ("by", WEEKLY_BY)]))])),
        ("if_version", versions[name])]) for name in order]


# ------------------------------------------------------------------ render

def cell(value):
    text = "n/a" if value is None else str(value)
    return text.replace("|", "\\|").replace("\n", " ").strip() or "-"


def table(headers, rows):
    lines = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    for row in rows:
        lines.append("| " + " | ".join(cell(v) for v in row) + " |")
    return lines


def pr_ref(number):
    return "PR %s" % number if number else "no PR"


def short(sha):
    return sha[:7] if sha else "n/a"


def arrow(a, b):
    a = "n/a" if a in (None, "") else a
    b = "n/a" if b in (None, "") else b
    return "%s → %s" % (a, b) if a != b else "%s (unchanged)" % a


def after(a, b):
    """'70 → 66 after pending' or '0' when equal."""
    return str(a) if a == b else "%s → %s after pending" % (a, b)


def block_label(title):
    text = title.replace("▶", "").strip().split(" (", 1)[0]
    return site.clip(text, 48)


def fmt_pct1(value):
    return "n/a" if value is None else "%s%%" % q1(value)


def since_text(value):
    if isinstance(value, datetime.datetime):
        return fmt_when(value, True)
    return value or "n/a"


def glance(c):
    """The 'At a glance' block: at most 12 lines."""
    en, st = c["en"], c["st"]
    ca, cr = en["counts_after"], en["counts"]
    dn_reg = sum(1 for f in en["dnaf"].values() if f["retired"])
    dn_after = sum(1 for f in en["dnaf_after"].values() if f["retired"])
    sc = en["status_counts"]
    mix = " · ".join("%s %d" % (v, c["verdict_mix"][v]) for v in VERDICTS if c["verdict_mix"][v]) or "none"
    changes = [w for w in c["watched_changes"]]
    provisional = sum(1 for w in changes if w["retired"])
    dnaf_period = sum(1 for e in c["events"] if e["verdict"] == "DNAF")
    dnaf_period_retired = sum(1 for e in c["events"] if e["retired"])
    lines = [
        "- **Register %s** (ref %s, %d pending row files): keys %s · WATCH %s · BUY %s · IN RANGE %d · NEAR %d · "
        "DNAF %d · %d on retired grounds (after pending %d · %d)." % (
            en["fm"].get("register_version", "n/a"), short(c["ref_sha"]),
            len(en["overlay"]) + len(en["keyless_rows"]), after(cr["keys"], ca["keys"]),
            after(cr["WATCH"], ca["WATCH"]), after(cr["BUY"], ca["BUY"]), sc["IN RANGE"], sc["NEAR"],
            cr["DNAF"], dn_reg, ca["DNAF"], dn_after),
        "- **Period:** %d memos merged (ANALYSE %d · REVIEW %d): %s%s; %d verdict changes on WATCH/BUY/HELD names, "
        "%d provisional (retired ground); new WATCH %d; MODEL %s." % (
            len(c["events"]), len(c["analyses"]), len(c["reviews"]), mix,
            (" · %d on retired grounds" % dnaf_period_retired) if dnaf_period else "", len(changes),
            provisional, len(c["new_watch"]), arrow(c["live_start"], c["live_end"])),
    ]
    decide, fix = c["attention"]["Decide"], c["attention"]["Fix"]
    shown = decide[:GLANCE_DECIDE]
    lines.append("- **Decide (%d)**%s:" % (len(decide), (" — top %d shown" % len(shown)) if len(shown) < len(decide)
                                           else "") if decide else "- **Decide:** nothing.")
    for x in shown:
        lines.append("  - [%s] %s (since %s)" % (x["severity"], x["item"], since_text(x["since"])))
    top = fix[:GLANCE_FIX]
    lines.append("- **Fix (%d)**%s:" % (len(fix), (" — top %d" % len(top)) if len(top) < len(fix) else "")
                 if fix else "- **Fix:** nothing.")
    for x in top:
        lines.append("  - [%s] %s" % (x["severity"], x["item"]))
    assert len(lines) <= 12
    return lines


def render_md(c):
    L = []
    st, en = c["st"], c["en"]
    s_ver, e_ver = st["fm"].get("register_version", "n/a"), en["fm"].get("register_version", "n/a")
    title = c["period_label"] + ((" (%s)" % c["iso_week"]) if c["iso_week"] else "")
    L.append("# GSC weekly report — %s" % title)
    L.append("")
    L.append("*%s · %s → %s Europe/Prague, until exclusive; report date %s · git at %s, the PR snapshot and the "
             "health input; n/a = not derivable. PRs are written 'PR n' on purpose (no GitHub cross-reference). "
             "Private: carries held names and zones. Framework output, not investment advice.*" % (
                 TOOL, fmt_when(c["since"], True), fmt_when(c["until"], True), c["report_date"].isoformat(),
                 short(c["ref_sha"])))
    L.append("")
    L.append("## At a glance")
    L.append("")
    L += glance(c)
    L.append("")

    # Attention lists
    for n, (name, blurb) in enumerate((("Decide", "only you can act"), ("Fix", "system health"),
                                       ("Know", "for your information")), start=1):
        items = c["attention"][name]
        L.append("## %d. %s — %s (%d)" % (n, name, blurb, len(items)))
        L.append("")
        if not items:
            L.append("Nothing.")
        for i, x in enumerate(items, start=1):
            detail = x["detail"].rstrip()
            if not detail.endswith((".", "…")):
                detail += "."
            L.append("%d. **[%s] %s** — %s *Action:* %s *Since:* %s." % (
                i, x["severity"], x["item"], detail, x["action"], since_text(x["since"])))
        L.append("")
        if name == "Decide":
            if c["held_now"]:
                L.append("**Held names** (register at the end; no cost or size in this report):")
                L.append("")
                L += table(("Key", "Verdict", "Zone", "Last zone check", "Flag open since", "Status", "Memo",
                            "Pending"),
                           [(h["key"], h["verdict"], h["zone"], h["last_zone_check"], h["open_since"] or "n/a",
                             h["status"], h["memo_date"], h["pending"] or "-") for h in c["held_now"]])
                L.append("")
            closed_held = [h for h in c["held_prs"] if h["state"] != "open"]
            if closed_held:
                L.append("**Held routine PRs resolved in the period** (%d; merged by a human or closed):"
                         % len(closed_held))
                L.append("")
                L += table(("PR", "Job", "Key", "Outcome", "State", "Why held", "Opened", "Wait h"),
                           [(h["number"], h["job"], h["key"] or "-", site.clip(h["outcome"], 110), h["state"], h["why"],
                             fmt_when(h["created"]), h["wait_hours"]) for h in closed_held])
                L.append("")
            L.append("**▶ Open items (register)** — queue/TODO.md head block at the end, bullets verbatim (%d):" %
                     len(en["open_items"]))
            L.append("")
            L += en["open_items"] or ["- none"]
            L.append("")

    # 4 header
    L.append("## 4. Header")
    L.append("")
    if c["timeline"]:
        model_text = "%s until %s · " % (c["live_start"], fmt_when(c["timeline"][0][0])) + " · ".join(
            "%s from %s" % (t[2], fmt_when(t[0])) for t in c["timeline"])
    else:
        model_text = "%s (whole period)" % c["live_end"]
    doc = c["prs_doc"] or {}
    h = c["health"]
    rows = [
        ("Period", "%s: %s → %s, until exclusive (%s); report date %s" % (
            title, fmt_when(c["since"], True), fmt_when(c["until"], True), fmt_span(c["until"] - c["since"]),
            c["report_date"].isoformat())),
        ("Ref", "%s = %s, last commit %s; end state %s (%s)" % (
            c["ref"], short(c["ref_sha"]), fmt_when(c["ref_time"], True), short(c["end"]["sha"]),
            fmt_when(c["end"]["when"]))),
        ("Start state", "%s, %s (last first-parent commit before the start)" % (
            short(c["start"]["sha"]) if c["start"] else "n/a", fmt_when(c["start"]["when"], True) if c["start"] else "n/a")),
        ("Commits in period", "%d first-parent" % len(c["window"])),
        ("Register", "%s (%s) → %s (%s)" % (s_ver, st["fm"].get("register_date", "n/a"), e_ver,
                                            en["fm"].get("register_date", "n/a"))),
        ("MODEL live", model_text),
        ("PR snapshot", "%s PRs from %s page(s); merged_by read for %s; needs-Jakub issue %s, %s comment(s) read" % (
            doc.get("count", "n/a"), doc.get("pages", "n/a"), doc.get("merged_by_fetched", "n/a"),
            ("number %s" % doc["needs_issue"]) if doc.get("needs_issue") else "not found",
            len(doc.get("comments") or []))),
        ("Health input", ("%d triggers (%d enabled, %d sprint), read %s; %s" % (
            len(h["triggers"]), sum(1 for t in h["triggers"] if t["enabled"]),
            sum(1 for t in h["triggers"] if t["sprint"]), fmt_when(h["read_at"], True), h["source"]))
         if h else "n/a (no --health-json)"),
        ("Merged after the ref or the period", "%d PR(s) merged at or after the end of the period%s" % (
            len(c["merged_after_until"]), (": " + ", ".join(pr_ref(r["pr"]["number"]) for r in c["merged_after_until"]))
            if c["merged_after_until"] else "")),
    ]
    L += table(("Item", "Value"), rows)
    L.append("")

    # 5 headline numbers
    sc_e, sc_s = en["status_counts"], st["status_counts"]
    ce, ca, cs = en["counts"], en["counts_after"], st["counts"]
    L.append("## 5. Headline numbers")
    L.append("")
    mix = " · ".join("%s %d" % (v, c["verdict_mix"][v]) for v in VERDICTS if c["verdict_mix"][v]) or "none"
    dn_e = sum(1 for f in en["dnaf"].values() if f["retired"])
    dn_a = sum(1 for f in en["dnaf_after"].values() if f["retired"])
    L += table(("Metric", "Start", "Register at end", "After pending rows", "Basis"), [
        ("Keys", cs["keys"], ce["keys"], ca["keys"], "register.csv rows; pending new keys added"),
        ("WATCH", cs["WATCH"], ce["WATCH"], ca["WATCH"], "section"),
        ("BUY", cs["BUY"], ce["BUY"], ca["BUY"], "section"),
        ("AVOID (one gate · two+)", "%d (%d · %d)" % (cs["AVOID"], cs["AVOID-1"], cs["AVOID-2"]),
         "%d (%d · %d)" % (ce["AVOID"], ce["AVOID-1"], ce["AVOID-2"]),
         "%d (%d · %d)" % (ca["AVOID"], ca["AVOID-1"], ca["AVOID-2"]), "verdict; sections AVOID-1 · AVOID-2"),
        ("DNAF", cs["DNAF"], ce["DNAF"], ca["DNAF"], "section"),
        ("DNAF on retired grounds", "n/a (%s not live)" % RETIRED_GATE0_VERSION
         if version_tuple(c["live_start"] or "") is None or version_tuple(c["live_start"]) < version_tuple(
             RETIRED_GATE0_VERSION) else sum(1 for f in st["dnaf_after"].values() if f["retired"]),
         dn_e, dn_a, "memo below %s, §1 ground matches RETIRED_GATE0_GROUNDS" % RETIRED_GATE0_VERSION),
        ("IN RANGE · NEAR · FAR (ranked WATCH/BUY)", "%d · %d · %d" % (sc_s["IN RANGE"], sc_s["NEAR"], sc_s["FAR"]),
         "%d · %d · %d" % (sc_e["IN RANGE"], sc_e["NEAR"], sc_e["FAR"]), "n/a",
         "status_hint at register Px; pending-change rows excluded"),
        ("Re-test debt, distinct keys", len(st["retest_union"]), len(en["retest_union"]), "n/a",
         "▶ Method re-tests blocks"),
    ])
    L.append("")
    L += table(("Period metric", "Value", "Prior window", "Basis"), [
        ("Memos merged", "%d (ANALYSE %d · REVIEW %d)" % (len(c["events"]), len(c["analyses"]), len(c["reviews"])),
         len(c["prior_events"]), "git memo adds, moves excluded"),
        ("Verdict mix of merged memos", mix, "-", "memo front matter"),
        ("Verdict changes among reviews", "%d of %d" % (sum(1 for e in c["reviews"] if e["changed"]),
                                                        len(c["reviews"])), "-", "prior memo → new memo"),
        ("Merged memos on a retired Gate-0 ground", sum(1 for e in c["events"] if e["retired"]), "-",
         "DNAF below %s once it is live" % RETIRED_GATE0_VERSION),
        ("Merged memos that still owe a method re-test", "%d of %d" % (
            sum(1 for e in c["events"] if e["retest_owed"]), len(c["events"])), "-", "re-test block newer than the memo"),
        ("New WATCH", len(c["new_watch"]), len(c["new_watch_prior"]), "verdict WATCH, prior not WATCH"),
        ("INCOMPLETE runs merged", len(c["incomplete_merged"]), "-", "commit titles"),
    ])
    L.append("")

    # 6 shortlist
    ranked = en["ranked"]
    top = ranked[:SHORTLIST_N]
    L.append("## 6. Shortlist — WATCH/BUY nearest the buy zone (top %d of %d ranked)" % (len(top), len(ranked)))
    L.append("")
    if top:
        L += table(("#", "Key", "Company", "Px", "Unit", "Px date (age d)", "Trigger", "Distance", "Needs fall",
                    "MCap/FCF", "EV/OI", "Status", "Reliable", "Note"),
                   [(i + 1, r["key"], site.clip(r["company"], 34), r["px"], r["px_unit"],
                     "%s (%s)" % (r["px_date"], r["px_age_d"] if r["px_age_d"] is not None else "n/a"),
                     r["trigger"] + (" (all-cash)" if r["all_cash"] else ""), site.fmt_signed_pct(r["distance"]),
                     fmt_pct1(r["needs_fall"] * 100) if r["needs_fall"] is not None else "n/a",
                     r["mcap_fcf"], r["ev_oi"], r["status"], "yes" if r["reliable"] else "no",
                     "; ".join(x for x in (r["retest_note"], "all-cash trigger (pre-R10)" if r["all_cash"] else "",
                                           r["pending"] or "") if x) or "-")
                    for i, r in enumerate(top)])
    else:
        L.append("No ranked WATCH or BUY row.")
    L.append("")
    if en["pending_changes"]:
        L.append("**Pending change** — WATCH/BUY rows whose merged, unapplied memo moves the verdict (out of the "
                 "ranking until INTAKE applies them, %d):" % len(en["pending_changes"]))
        L.append("")
        L += table(("Key", "Company", "Register", "Pending", "Retired ground", "Px (date)", "Trigger"),
                   [(r["key"], site.clip(r["company"], 34), r["section"], r["pending"],
                     "yes — " + RETIRED_FLAG if en["dnaf_after"].get(r["key"], {}).get("retired") else "no",
                     "%s (%s)" % (r["px"], r["px_date"]), r["trigger"]) for r in en["pending_changes"]])
        L.append("")
    ages = [r["px_age_d"] for r in ranked if r["px_age_d"] is not None]
    no_trigger = [r["key"] for r in en["shortlist"] if r["distance"] is None]
    L.append("Status per MODEL §8.3 step 3 (register tool `status_hint`). Distance = Px ÷ trigger − 1; needs fall = "
             "1 − trigger ÷ Px. Reliable = no re-test owed, no pending change, not an all-cash trigger and Px at most "
             "%d d old at the report date (%s): %d of %d ranked rows. Px ages across the ranked rows: newest %s d, "
             "oldest %s d. WATCH/BUY rows without a numeric trigger: %d%s. WATCH rows owing a re-test: %d of %d." % (
                 RELIABLE_PX_DAYS, c["report_date"].isoformat(), sum(1 for r in ranked if r["reliable"]), len(ranked),
                 min(ages) if ages else "n/a", max(ages) if ages else "n/a", len(no_trigger),
                 (" (%s)" % ", ".join(no_trigger)) if no_trigger else "", len(en["watch_owed"]), ce["WATCH"]))
    L.append("")

    # 7 pending overlay
    rows_all = list(en["overlay"].values()) + en["keyless_rows"]
    L.append("## 7. Merged, waiting for INTAKE (%d row files on the ref)" % len(rows_all))
    L.append("")
    if rows_all:
        L += table(("Row file", "Type", "Key", "Register", "Overlay", "Retired ground", "Landed", "PR title"),
                   [(p["file"], p["row_type"], p["key"] or "-",
                     "%s" % (p["register_verdict"] or ("new key" if p["new_key"] else "-")), p["label"],
                     "yes" if p["retired"] else "no", fmt_when(p.get("merged")), site.clip(p["pr_title"], 80))
                    for p in rows_all])
    else:
        L.append("None.")
    L.append("")
    if en["proposals"]:
        L.append("Proposal files waiting for INTAKE: " + ", ".join(p.rsplit("/", 1)[-1] for p in en["proposals"]) + ".")
        L.append("")

    # 8 register changes
    d = c["diff"]
    L.append("## 8. Register changes (%s → %s)" % (s_ver, e_ver))
    L.append("")
    L.append("Added %d · removed %d · verdict/section moved %d · regraded without a verdict move %d. The register "
             "lags merged memos until INTAKE applies their rows (section 7)." % (
                 len(d["added"]), len(d["removed"]), len(d["changed"]), len(d["regraded"])))
    L.append("")
    if d["changed"]:
        L += table(("Key", "Company", "Section", "Verdict", "Past", "Future", "SF", "Memo", "Flag"),
                   [(x["key"], site.clip(x["company"], 30), arrow(x["from_section"], x["to_section"]),
                     arrow(x["from_verdict"], x["to_verdict"]), arrow(x["from"]["past"], x["to"]["past"]),
                     arrow(x["from"]["future"], x["to"]["future"]), arrow(x["from"]["sf"], x["to"]["sf"]),
                     arrow(x["from_memo"], x["to_memo"]),
                     RETIRED_FLAG if en["dnaf"].get(x["key"], {}).get("retired") else "-") for x in d["changed"]])
        L.append("")
    if d["added"]:
        L.append("Added: " + " · ".join("`%s` %s%s" % (x["key"], x["section"],
                                                      " (retired ground)" if en["dnaf"].get(x["key"], {}).get("retired")
                                                      else "") for x in d["added"]) + ".")
        L.append("")
    if d["removed"]:
        L.append("Removed: " + " · ".join("`%s` (was %s)" % (x["key"], x["section"]) for x in d["removed"]) + ".")
        L.append("")
    if d["regraded"]:
        L.append("Regraded, verdict unchanged: " + " · ".join("`%s`" % x["key"] for x in d["regraded"]) + ".")
        L.append("")

    # 9 new analyses
    L.append("## 9. New analyses (%d)" % len(c["analyses"]))
    L.append("")
    if c["analyses"]:
        L += table(("Key", "Company", "Verdict", "Deciding reasons", "Flag", "Understanding (memo §2)", "MODEL",
                    "Merged"),
                   [(e["key"] + ("" if not e["title_key"] or e["title_key"] == e["key"] else " (title %s)" % e["title_key"]),
                     site.clip(e["company"], 34), e["verdict"], e["deciding"],
                     RETIRED_FLAG if e["retired"] else "-", e["understanding"], e["memo_model"],
                     "%s, %s" % (fmt_when(e["merged"]), pr_ref(e["pr"]))) for e in c["analyses"]])
    else:
        L.append("None.")
    L.append("")

    # 10 reviews
    L.append("## 10. Reviews (%d memos)" % len(c["reviews"]))
    L.append("")
    if c["reviews"]:
        L += table(("Key", "Company", "Prior → new", "Changed", "Deciding reasons", "Flag", "What moved (title)",
                    "MODEL", "Merged"),
                   [(e["key"] + (" (HELD)" if e["held"] else ""), site.clip(e["company"], 30),
                     "%s → %s" % (e["prior_verdict"] or "n/a", e["verdict"]), "yes" if e["changed"] else "no",
                     e["deciding"], RETIRED_FLAG if e["retired"] else (e["retest_end"] or "-"),
                     site.clip(e["moved"] or "-", 140), e["memo_model"],
                     "%s, %s" % (fmt_when(e["merged"]), pr_ref(e["pr"]))) for e in c["reviews"]])
    else:
        L.append("None.")
    L.append("")
    inc_reviews = [x for x in c["incomplete_merged"] if x["parsed"]["job"] == "REVIEW"]
    if inc_reviews:
        L.append("REVIEW runs merged INCOMPLETE (no memo): " + " · ".join(
            "`%s` (%s, %s)" % (x["parsed"]["key"], x["parsed"]["gap"], pr_ref(x["parsed"]["pr"])) for x in inc_reviews)
            + ".")
        L.append("")

    # 11 pipeline and routine health
    L.append("## 11. Pipeline and routine health")
    L.append("")
    if c["prs_doc"]:
        hj = (h or {}).get("by_job") or {}
        L += table(("Job", "Scheduled base", "Scheduled sprint", "Opened", "Merged", "by gsc-automerge", "by Jakub",
                    "by n/a", "Closed unmerged", "Open at end"),
                   [(job, hj.get(job, {}).get("scheduled_base", "n/a") if h else "n/a",
                     hj.get(job, {}).get("scheduled_sprint", "n/a") if h else "n/a",
                     counts.get("opened", 0), counts.get("merged", 0), counts.get("merged_by_bot", 0),
                     counts.get("merged_by_human", 0), counts.get("merged_by_n/a", 0),
                     counts.get("closed_unmerged", 0), counts.get("open_at_end", 0))
                    for job, counts in ((j, dict(c["by_job_all"][j])) for j in
                                        list(JOBS) + [b for b in c["by_job"] if b not in JOBS])])
        L.append("")
        L.append("Scheduled fires: each enabled trigger's cron from the health input expanded over the period in its "
                 "CRON_TZ (the trigger list as read at the health input's time is assumed for the whole period). "
                 "Opened: PRs created in the period (a run that ends before its claim opens no PR).")
        L.append("")
        lb, lh = c["latency_bot"], c["latency_human"]
        L.append("Routine PR created → merged: by gsc-automerge %d (median %s h, max %s h) · by Jakub %d (median %s h, "
                 "max %s h)." % (lb["count"], lb["median_h"] if lb["count"] else "n/a",
                                 lb["max_h"] if lb["count"] else "n/a", lh["count"],
                                 lh["median_h"] if lh["count"] else "n/a", lh["max_h"] if lh["count"] else "n/a"))
        if c["gap"]:
            g = c["gap"]
            L.append("Longest stretch without a new routine PR: %s → %s (%s)%s." % (
                fmt_when(g[1]), fmt_when(g[2]), fmt_span(g[0]),
                ("; fires scheduled in it: base %d, sprint %d" % (c["gap_fires"]["base"], c["gap_fires"]["sprint"]))
                if c["gap_fires"] else ""))
        L.append("")
        L += table(("Prague day",) + JOBS,
                   [(day + " " + DAYS[datetime.date.fromisoformat(day).weekday()],) + tuple(cnt.get(j, 0) for j in JOBS)
                    for day, cnt in c["day_grid"].items()])
        L.append("")
    else:
        L.append("PR snapshot not given: PR counts n/a.")
        L.append("")
    if h:
        L.append("**Trigger last runs** (health input; only the last run of each trigger is visible, so a failure "
                 "here says nothing about the earlier runs):")
        L.append("")
        L += table(("Trigger", "Job", "Sprint", "Cron", "Fires in period", "Last run", "Fired", "Took",
                    "Failure reason"),
                   [(t["name"], t["job"], "yes" if t["sprint"] else "no", t["cron"], t["fires"], t["last_status"],
                     fmt_when(t["last_fired_at"]),
                     ("%d s" % t["last_duration_s"]) if t.get("last_duration_s") is not None else "n/a",
                     t["failure_reason"] or "-") for t in h["triggers"]])
        L.append("")
        if h["disabled"]:
            L.append("Disabled triggers (not expanded): " + "; ".join(h["disabled"]) + ".")
            L.append("")
    wf = c["workflow_failures"]
    L.append("**Workflow failures recorded on '%s'** (%d): " % (NEEDS_TITLE, len(wf)) + (" · ".join(
        "%s %s: %s" % (fmt_when(w), what, site.clip(why, 120)) for w, what, why in wf) or "none") + ".")
    L.append("")
    inc = c["incomplete_prs"]
    L.append("**INCOMPLETE runs** (%d PR(s); evidence files added %d): " % (len(inc), len(c["evidence"])) + (
        " · ".join("`%s` %s — %s (%s)" % (r["parsed"]["key"] or "-", r["parsed"]["job"], r["parsed"]["gap"],
                                          pr_ref(r["pr"]["number"])) for r in inc) or "none") + ".")
    L.append("")
    L.append("**Abandoned / superseded** (%d): " % len(c["abandoned"]) + (
        " · ".join("`%s` %s %s, closed %s (%s)" % (r["parsed"]["key"] or "-", r["parsed"]["job"], r["parsed"]["tag"],
                                                   fmt_when(r["closed"]), pr_ref(r["pr"]["number"]))
                   for r in c["abandoned"]) or "none") + ".")
    L.append("")
    L.append("**INTAKE runs** (%d): " % len(c["intakes"]) + (" · ".join(
        "%s %s (%s rows, %s)" % (fmt_when(x["when"]), x["parsed"]["register_version"] or "no register change",
                                 x["parsed"]["rows"] or "n/a", pr_ref(x["parsed"]["pr"])) for x in c["intakes"])
        or "none") + "; register %s → %s." % (s_ver, e_ver))
    L.append("")
    lr = c["last_run"]
    L.append("**Last merged run per job (whole history, before the end of the period):** " + " · ".join(
        "%s %s (%d d before the report date, %s)" % (job, fmt_when(v[0], True),
                                                     (c["report_date"] - prague_date(v[0])).days, pr_ref(v[1]))
        for job, v in lr.items()) + ".")
    L.append("")
    if c["merged_after_ref"]:
        L.append("**Merged in the period but not on the ref** (rendered with --allow-stale-ref): " + " · ".join(
            "%s `%s` (%s)" % (pr_ref(r["pr"]["number"]), r["parsed"]["title"], fmt_when(r["merged"]))
            for r in c["merged_after_ref"]) + ".")
        L.append("")
    qs, qe = st["queue"], en["queue"]
    keys = [k for k in ("open", "done", "prior", "retired", "no listed security", "rejected", "incomplete",
                        "stalled", "other") if qs.get(k) or qe.get(k)]
    L.append("**Draft queue** (queue/DRAFT_QUEUE.md lines under ## Queue, start → end): " + " · ".join(
        "%s %s" % (k, arrow(str(qs.get(k, 0)), str(qe.get(k, 0)))) for k in keys) + ".")
    L.append("")
    bs, be = st["blocks"], en["blocks"]
    other_blocks = [t for t in list(be.keys()) + [t for t in bs if t not in be] if (bs.get(t, 0) or be.get(t, 0))]
    L.append("**TODO head blocks** (bullets, start → end): " + " · ".join(
        "%s %s" % (block_label(t), arrow(str(bs.get(t, 0)), str(be.get(t, 0)))) for t in other_blocks) + ".")
    L.append("")

    # 12 framework
    L.append("## 12. Framework")
    L.append("")
    if c["timeline"]:
        L += table(("Merged", "Version", "model_date", "Commit"),
                   [(fmt_when(t[0]), t[2], t[3], site.clip(PR_NUM_SUFFIX_RE.sub("", t[4]), 120)) for t in c["timeline"]])
    else:
        L.append("No MODEL release in the period (live: %s)." % c["live_end"])
    L.append("")
    flags = en["dnaf_after"]
    L.append("**DNAF rows after pending, by Gate-0 ground** (%d; %d on grounds %s retired: %s):" % (
        len(flags), sum(1 for f in flags.values() if f["retired"]), RETIRED_GATE0_VERSION,
        "; ".join(name for name, _p in RETIRED_GATE0_GROUNDS)))
    L.append("")
    L += table(("Key", "Memo", "Memo verdict", "MODEL", "Retired ground(s)", "Flag", "Ground (memo §1)"),
               [(k, f["memo_date"] + (" (pending)" if f["pending"] else ""), f["memo_verdict"], f["memo_model"],
                 ", ".join(f["grounds"]) or "-", RETIRED_FLAG if f["retired"] else "live verdict or not a Gate-0 memo",
                 site.clip(f["ground"], 120) or "-") for k, f in sorted(flags.items())])
    L.append("")
    if c["superseded"]:
        L.append("**Memos merged after a newer MODEL went live** (%d): " % len(c["superseded"]) + " · ".join(
            "`%s` %s under %s, merged %s under %s — %s" % (
                e["key"], e["verdict"], e["memo_model"], fmt_when(e["merged"]), e["live_model"],
                e["retest_end"] or "NOT on a re-test block") for e in c["superseded"]) + ".")
        L.append("")

    # 13 coverage
    L.append("## 13. Coverage (register at the end, by the region of the listing line)")
    L.append("")
    total = len(en["rows"])
    cov = collections.OrderedDict((r, collections.Counter()) for r in REPORT_REGIONS)
    countries = collections.Counter()
    for row in en["rows"]:
        country, region = region_of(row["key"])
        countries[country] += 1
        cov[region]["keys"] += 1
        cov[region][row["section"]] += 1
        cov[region]["AVOID"] += row["verdict"] == "AVOID"
    L += table(("Region", "Keys", "Share", "WATCH", "BUY", "AVOID", "DNAF"),
               [(r, n["keys"], fmt_pct1(Decimal(n["keys"]) * 100 / total) if total else "n/a", n["WATCH"], n["BUY"],
                 n["AVOID"], n["DNAF"]) for r, n in cov.items()]
               + [("Total", total, "100.0%" if total else "n/a", ce["WATCH"], ce["BUY"], ce["AVOID"], ce["DNAF"])])
    L.append("")
    L.append("By listing country (keys): " + " · ".join(
        "%s %d" % (k, v) for k, v in sorted(countries.items(), key=lambda kv: (-kv[1], kv[0]))) + ". Regions are "
        "this report's grouping of listing countries (a bare key is a US line, so a US-listed ADR counts as North "
        "America); Greece sits in Western Europe ex-UK, Australia and Israel in Other.")
    L.append("")

    # 14 backlog
    L.append("## 14. Backlog (start → end)")
    L.append("")
    data = datasets(c, c.get("generated_at") or c["until"])
    L += table(("Item", "Start", "End", "Unit", "Basis"),
               [(b["item"], b["start"], b["end"], b["unit"], b["note"]) for b in data["backlog"]])
    L.append("")
    L.append("*Framework output, not investment advice.*")
    return "\n".join(L) + "\n"


def jsonable(value):
    if isinstance(value, datetime.datetime):
        return iso_prague(value)
    if isinstance(value, datetime.date):
        return value.isoformat()
    if isinstance(value, Decimal):
        return num(value)
    if isinstance(value, dict):
        return collections.OrderedDict((str(k), jsonable(v)) for k, v in value.items())
    if isinstance(value, (list, tuple)):
        return [jsonable(v) for v in value]
    if isinstance(value, set):
        return [jsonable(v) for v in sorted(value)]
    return value


def render_json(c, generated_at):
    """The report as one JSON document: header, headline, attention, the overlay, events and every dataset."""
    st, en = c["st"], c["en"]
    data = collections.OrderedDict([
        ("tool", TOOL), ("generated_at", generated_at),
        ("header", collections.OrderedDict([
            ("period_label", c["period_label"]), ("iso_week", c["iso_week"]), ("since", c["since"]),
            ("until", c["until"]), ("until_exclusive", True), ("report_date", c["report_date"]),
            ("ref", c["ref"]), ("ref_sha", c["ref_sha"]), ("ref_time", c["ref_time"]),
            ("start_sha", c["start"]["sha"] if c["start"] else None), ("end_sha", c["end"]["sha"]),
            ("commits_in_period", len(c["window"])),
            ("register_start", st["fm"].get("register_version")), ("register_end", en["fm"].get("register_version")),
            ("model_start", c["live_start"]), ("model_end", c["live_end"]),
            ("model_releases", [{"when": t[0], "version": t[2], "model_date": t[3]} for t in c["timeline"]]),
            ("pr_snapshot", {k: (c["prs_doc"] or {}).get(k) for k in ("count", "pages", "merged_by_fetched",
                                                                       "needs_issue", "issues_read", "comments_read")}),
            ("retired_gate0", {"version": RETIRED_GATE0_VERSION,
                               "grounds": [{"name": n, "pattern": p.pattern} for n, p in RETIRED_GATE0_GROUNDS]}),
        ])),
        ("attention", c["attention"]),
        ("overlay", [{k: v for k, v in p.items() if k not in ("fm", "text")}
                     for p in list(en["overlay"].values()) + en["keyless_rows"]]),
        ("dnaf_after_pending", {k: {kk: vv for kk, vv in f.items()} for k, f in en["dnaf_after"].items()}),
        ("watched_changes", c["watched_changes"]),
        ("held_prs", c["held_prs"]),
        ("register_diff", c["diff"]),
        ("memo_events", c["events"]),
        ("datasets", datasets(c, generated_at)),
    ])
    return json.dumps(jsonable(data), ensure_ascii=False, indent=1) + "\n"


# ------------------------------------------------------------------ commands

def write_text(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def dump(rows):
    return json.dumps(rows, ensure_ascii=False, indent=1) + "\n"


def outside_repo(path, repo_dir, what):
    """Refuse an output path inside the repository (the report is generated, never committed)."""
    target, root = os.path.realpath(path), os.path.realpath(repo_dir)
    if target == root or target.startswith(root + os.sep):
        raise ToolError("%s %s is inside the repository; write it outside (e.g. /tmp/gsc-weekly)" % (what, path))
    return path


def repo_root():
    """The repository this tool sits in (two folders up), for the output check of the commands that
    take no --repo-dir."""
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def cmd_window(args):
    doc = window_doc(parse_when(args.at), args.meta_at, args.meta_by)
    print(json.dumps(doc, ensure_ascii=False))


def write_datasets(directory, data):
    os.makedirs(directory, exist_ok=True)
    for name in DATASET_IDS:
        write_text(os.path.join(directory, name + ".json"), dump(data[name]))


def scrub_private(data):
    """The datasets with every PRIVATE_RE figure in their text replaced by '[private]' (MODEL section
    7.4: the page never carries average cost, position size or core numbers, even where a copied open
    item or PR outcome would). Numbers, booleans and None pass unchanged."""
    def clean(value):
        if isinstance(value, str):
            return PRIVATE_RE.sub("[private]", value)
        if isinstance(value, list):
            return [clean(v) for v in value]
        if isinstance(value, dict):
            return collections.OrderedDict((k, clean(v)) for k, v in value.items())
        return value
    return collections.OrderedDict((name, clean(rows)) for name, rows in data.items())


def render_all(ctx, generated_at):
    """{dataset id: rows} in DATASET_IDS order, checked against DATASET_SCHEMA, and the notification line."""
    data = jsonable(datasets(ctx, generated_at))
    data["summary"] = jsonable(summary_rows(ctx, data))
    data = scrub_private(collections.OrderedDict((name, data[name]) for name in DATASET_IDS))
    problems = check_datasets(data)
    if problems:
        raise ToolError("dataset schema: " + "; ".join(problems[:5]))
    return data, notification_line(data)


def cmd_render(args):
    need_full_history(args.repo_dir)          # up front: the first line WEEKLY reports names the fix
    since, until = parse_when(args.since), parse_when(args.until)
    for path, what in ((args.out_dir, "--out-dir"), (args.out_md, "--out-md"), (args.out_json, "--out-json")):
        if path:
            outside_repo(path, args.repo_dir, what)
    prs_doc = load_fetch(args.fetch_dir)
    health_doc, health_problem = None, None
    if args.health_json:
        try:
            health_doc = load_health(args.health_json)
        except ToolError as exc:
            health_problem = str(exc)
    ctx = build(args.repo_dir, args.ref, since, until, prs_doc, health_doc, args.allow_stale_ref, health_problem)
    generated_at = datetime.datetime.now(UTC).replace(microsecond=0)
    ctx["generated_at"] = generated_at
    data, line = render_all(ctx, generated_at)
    write_datasets(args.out_dir, data)
    write_text(os.path.join(args.out_dir, NOTICE_FILE), line + "\n")
    if args.out_md:
        write_text(args.out_md, render_md(ctx))
    if args.out_json:
        write_text(args.out_json, render_json(ctx, generated_at))
    meta = data["meta"][0]
    print("%s: %d Decide, %d Fix, %d Know -> %s (%d datasets, %s)" % (
        meta["period_label"], meta["decide"], meta["fix"], meta["know"], args.out_dir, len(data), NOTICE_FILE))


def cmd_lint_summary(args):
    outside_repo(args.datasets, repo_root(), "--datasets")
    data = collections.OrderedDict()
    for name in DATASET_IDS:
        if name != "summary":
            data[name] = read_json(os.path.join(args.datasets, name + ".json"), "dataset")
    rows = read_json(args.input, "--in")
    problems = lint_summary(rows, number_corpus(data), kpi_values(data))
    if problems:
        for p in problems:
            print("lint: %s" % p)
        print("lint-summary: %d problem(s); summary.json left as rendered" % len(problems))
        return 1
    if args.apply:
        clean = [collections.OrderedDict([("order", r["order"]), ("kind", r["kind"]), ("text", r["text"])])
                 for r in rows]
        write_text(os.path.join(args.datasets, "summary.json"), dump(clean))
        print("lint-summary: ok; summary.json replaced with %d sentence(s)" % len(clean))
    else:
        print("lint-summary: ok (%d sentence(s))" % len(rows))
    return 0


def cmd_dash_writes(args):
    outside_repo(args.out, repo_root(), "--out")
    writes = dash_writes(args.datasets, read_json(args.blobs, "--blobs"), read_json(args.versions, "--versions"),
                         args.at)
    text = json.dumps(writes, ensure_ascii=False)
    write_text(args.out, text + "\n")
    print(text)


def main(argv=None):
    parser = argparse.ArgumentParser(description="GSC weekly report (v%s)" % TOOL_VERSION)
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("window", help="the report window of a run time")
    p.add_argument("--at", required=True)
    p.add_argument("--meta-at")
    p.add_argument("--meta-by")
    p.set_defaults(func=cmd_window)
    p = sub.add_parser("render", help="render the datasets offline")
    p.add_argument("--repo-dir", required=True)
    p.add_argument("--ref", default="origin/main")
    p.add_argument("--since", required=True)
    p.add_argument("--until", required=True)
    p.add_argument("--fetch-dir", required=True)
    p.add_argument("--health-json")
    p.add_argument("--out-dir", required=True)
    p.add_argument("--out-md")
    p.add_argument("--out-json")
    p.add_argument("--allow-stale-ref", action="store_true")
    p.set_defaults(func=cmd_render)
    p = sub.add_parser("lint-summary", help="check Claude's summary sentences")
    p.add_argument("--datasets", required=True)
    p.add_argument("--in", dest="input", required=True)
    p.add_argument("--apply", action="store_true")
    p.set_defaults(func=cmd_lint_summary)
    p = sub.add_parser("dash-writes", help="build the weekly page's dataset batch")
    p.add_argument("--datasets", required=True)
    p.add_argument("--blobs", required=True)
    p.add_argument("--versions", required=True)
    p.add_argument("--at", required=True)
    p.add_argument("--out", required=True)
    p.set_defaults(func=cmd_dash_writes)
    args = parser.parse_args(argv)
    try:
        if args.cmd == "render":
            load_tools(args.repo_dir)
        rc = args.func(args)
    except ToolError as exc:
        print("gsc_weekly: %s" % exc, file=sys.stderr)
        return 2
    return rc or 0


if __name__ == "__main__":
    sys.exit(main())
