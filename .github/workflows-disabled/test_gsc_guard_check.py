#!/usr/bin/env python3
"""Plain-python tests for gsc_guard_check.py (no pytest, no git needed).

Run:  python3 .github/workflows/test_gsc_guard_check.py
Prints one PASS/FAIL line per case. Exit code = number of failed cases
(0 = all pass).

Covers: every correct run per job (expect OK), every known violation
(expect failure), keys with dots and hyphens, the REVIEW prior-memo move and
the memo-folder checks (MODEL v4.5.0), the register.csv twin and its
snapshot pair (lockstep, header, row count, rendering by the register tool),
the -z name-status parser, make_tree_lookup(), make_text_lookup(), and main()
end to end with a fake git. MODEL v4.5.2: every added row file passes the
tool's lint-row at the PR head; the cases read consistent row and memo
fixtures (fixture_text) unless they pass their own texts.
"""
import contextlib
import io
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gsc_guard_check as g  # noqa: E402

reg = g.register_tool()   # routines/tools/gsc_register.py, as the checker loads it
if reg is None:
    raise SystemExit("cannot load routines/tools/gsc_register.py")

try:
    sys.stdout.reconfigure(errors="backslashreplace")
except AttributeError:
    pass

RESULTS = []


def record(name, ok, detail=""):
    RESULTS.append(ok)
    line = ("PASS  " if ok else "FAIL  ") + name
    if not ok and detail:
        line += "  -- " + detail
    print(line)


def E(*lines):
    """E("A path", "D path") -> [("A", "path"), ("D", "path")]"""
    return [tuple(line.split(" ", 1)) for line in lines]


def tree_lookup_for(trees):
    """Fake tree_lookup: trees[(side, folder)] -> basenames; a missing folder
    is []; side 'main' falls back to 'base' (main has not moved); a value of
    None means git could not list it."""
    def lookup(side, folder):
        if (side, folder) in trees:
            names = trees[(side, folder)]
        elif side == "main" and ("base", folder) in trees:
            names = trees[("base", folder)]
        else:
            names = []
        return None if names is None else sorted(names)
    return lookup


def case(name, branch, title, entries, expect, base="main", blobs=None, msg=None, trees=None, no_tree=False,
         texts=None, no_text=False):
    """expect: 'ok', 'fail' or 'skip'. msg: a substring one error must contain.
    trees: {(side, folder): [basenames]} for the memo-folder checks; no_tree
    passes no tree_lookup at all (the checker must fail closed). texts:
    {(side, path): text} for the register checks (default: a consistent
    register.csv / _REGISTER.md pair at the head); no_text passes no
    text_lookup at all."""
    table = blobs or {}
    text_table = INTAKE_TEXTS if texts is None else texts

    def lookup(side, path):
        return table.get((side, path))

    def text_lookup(side, path):
        text = text_table.get((side, path))
        if text is None and texts is None and side == "head":
            text = fixture_text(path)
        return text

    try:
        errors = g.evaluate(branch, title, base, "main", entries, lookup,
                            None if no_tree else tree_lookup_for(trees or {}),
                            None if no_text else text_lookup)
    except Exception as exc:
        record(name, False, "raised %r" % exc)
        return
    if expect == "skip":
        ok = errors is None
    elif expect == "ok":
        ok = errors == []
    else:
        ok = bool(errors) and (msg is None or any(msg in e for e in errors))
    record(name, ok, "expected %s%s, got %r" % (expect, " (%r)" % msg if msg else "", errors))


# ------------------------------------------------------------ run values

D = "2026-10-04"
T = "2250"

AN_CGNX = "claude/gsc-analyse-CGNX-%s-%s" % (D, T)
AN_7309 = "claude/gsc-analyse-7309.T-%s-%s" % (D, T)
AN_ATCO = "claude/gsc-analyse-ATCO-B.ST-%s-%s" % (D, T)
AN_CARL = "claude/gsc-analyse-CARL-B.CO-%s-%s" % (D, T)
AN_KEYLESS = "claude/gsc-analyse-%s-%s" % (D, T)
RV_TROW = "claude/gsc-review-TROW-%s-%s" % (D, T)
RV_HFG = "claude/gsc-review-HFG.DE-%s-%s" % (D, T)
SWEEP = "claude/gsc-sweep-2026-10-03-0700"
SEED = "claude/gsc-seed-2026-10-05-0800"
INTAKE = "claude/gsc-intake-2026-10-04-0650"

ANALYSE_CGNX_FULL = E(
    "A memos/CGNX/CGNX_2026-10-04_GSC.md",
    "A queue/rows/2026-10-04_2250_ANALYSE_CGNX.md",
    "A queue/runs/2026-10-04_2250_ANALYSE_CGNX.md",
    "D queue/evidence/CGNX_draft-evidence_2026-09.md",
)

INTAKE_SNAPSHOT = "archive/registers/2026/REGISTER_v304_2026-10-03.md"
INTAKE_CSV_SNAPSHOT = "archive/registers/2026/REGISTER_v304_2026-10-03.csv"
INTAKE_TODO_ARCHIVE = "archive/queue/TODO_v36_2026-10-02.md"
INTAKE_DQ_ARCHIVE = "archive/queue/DRAFT_QUEUE_v12_2026-10-01.md"
PROPOSAL = "2026-10-03_0800_QUEUE-SEED.md"
INTAKE_FULL = E(
    "M _REGISTER.md",
    "M register.csv",
    "A " + INTAKE_CSV_SNAPSHOT,
    "M queue/TODO.md",
    "M queue/DRAFT_QUEUE.md",
    "A " + INTAKE_SNAPSHOT,
    "A " + INTAKE_TODO_ARCHIVE,
    "A " + INTAKE_DQ_ARCHIVE,
    "A archive/queue/proposals/" + PROPOSAL,
    "D queue/proposals/" + PROPOSAL,
    "D queue/rows/2026-10-03_2250_ANALYSE_7309.T.md",
    "D queue/rows/2026-10-03_2310_REVIEW_ATCO-B.ST.md",
    "D queue/rows/2026-10-03_2330_ANALYSE_CARL-B.CO.md",
    "D queue/rows/2026-10-03_0700_SWEEP.md",
    "D queue/rows/2026-10-03_2250_ANALYSE.md",
    "A queue/runs/2026-10-04_0650_INTAKE.md",
)
INTAKE_BLOBS = {
    ("base", "_REGISTER.md"): "blob-register-v304",
    ("head", INTAKE_SNAPSHOT): "blob-register-v304",
    ("base", "register.csv"): "blob-csv-v304",
    ("head", INTAKE_CSV_SNAPSHOT): "blob-csv-v304",
    ("base", "queue/TODO.md"): "blob-todo-v36",
    ("head", INTAKE_TODO_ARCHIVE): "blob-todo-v36",
    ("base", "queue/DRAFT_QUEUE.md"): "blob-dq-v12",
    ("head", INTAKE_DQ_ARCHIVE): "blob-dq-v12",
    ("base", "queue/proposals/" + PROPOSAL): "blob-proposal",
    ("head", "archive/queue/proposals/" + PROPOSAL): "blob-proposal",
}


def without(entries, *drop):
    return [e for e in entries if " ".join(e) not in drop]


def reg_row(key, ev_oi, **over):
    """A valid register.csv row (WATCH, no core numbers)."""
    row = {name: reg.NM for name in reg.CSV_HEADER}
    row.update({"key": key, "company": key + " Inc.", "isin": reg.OWED, "aliases": reg.NM, "section": "WATCH",
                "verdict": "WATCH", "gates_failed": "0", "past": "STRONG", "past_reason": "20.0% ROCE",
                "future": "ADEQUATE", "future_reason": reg.NM, "sf": "PASS", "sf_reason": reg.NM,
                "memo_path": "memos/%s/%s_2026-09-01_GSC.md" % (key, key), "memo_date": "2026-09-01",
                "memo_version": "v1", "model_version": "v4.5.0", "px": "100", "px_unit": "USD",
                "px_date": "2026-08-31", "px_source": "memo", "trigger": "80", "mcap_fcf": "12.0",
                "ev_oi": ev_oi, "ev_oi_all_cash": ev_oi, "next_review_short": "Feb 2027", "held": "false",
                "core_source": reg.OWED})
    for name in reg.CORE_FIELDS:
        row[name] = reg.OWED
    row.update(reg.LENS_DEFAULTS)
    row.update(reg.R10_DEFAULTS)
    row["trigger_basis"] = "no-cash"            # a v4.5.0 row prints the no-cash bound (round 2, R10)
    row.update(over)
    return row


REG_ROWS = [reg_row("CGNX", "9.5"), reg_row("TROW", "10.9"), reg_row("7309.T", "n.m.")]
INTAKE_CSV = reg.csv_text(REG_ROWS)
INTAKE_MD = reg.render(REG_ROWS, "v305", "2026-10-04")
INTAKE_TEXTS = {("head", "register.csv"): INTAKE_CSV, ("head", "_REGISTER.md"): INTAKE_MD}


# Row and memo fixtures (MODEL v4.5.2 lint-row): a keyed ANALYSE or REVIEW row
# is a WATCH verdict row whose table is the tool's print for its memo; a
# keyless ANALYSE row is a QUEUE row; a SWEEP row carries its portfolio table.
def fixture_memo(key, date):
    return ("---\nticker: %s\ncompany: %s Corp\nmemo_date: %s\nmemo_version: v1\nmodel_version: v4.5.2\n"
            "verdict: WATCH (fixture)\nposition: —\n---\n# memo\n" % (key, key, date))


def fixture_row(path, table=True):
    m = reg.ROW_FILE_RE.match(path)
    date, time, job, key = m.group("date"), m.group("time"), m.group("job"), m.group("key")
    if job == "SWEEP":
        return ("---\nrow_type: SWEEP\nrun_date: %s\nrun_time: %s\nheld: false\npr_title: GSC SWEEP %s — "
                "1/1 priced · fixture\n---\n## Portfolio table\n| Ticker | Avg cost | Current | Zone | "
                "Distance to ADD band | Distance to sell-flag line |\n|---|---|---|---|---|---|\n"
                "| HFG.DE | 10 | 12 | HOLD | 20%% | 30%% |\n" % (date, time, date))
    if key is None:
        return ("---\nrow_type: QUEUE\nrun_date: %s\nrun_time: %s\npr_title: GSC ANALYSE %s — queue "
                "exhausted\n---\n## Queue update\nnone\n" % (date, time, date))
    memo = "memos/%s/%s_%s_GSC.md" % (key, key, date)
    row = reg.row_from_memo(memo, fixture_memo(key, date), [])
    lines = [reg.table_line(reg.MASTER_COLUMNS), "|" + "---|" * len(reg.MASTER_COLUMNS),
             reg.table_line(reg.master_cells(row))]
    return ("---\nrow_type: %s\nkey: %s\ncompany: %s Corp\nmemo_path: %s\nrun_date: %s\nrun_time: %s\n"
            "held: false\npr_title: GSC %s %s %s — WATCH (fixture)\n---\n## Register row (new)\n%s\n"
            "## Replaces\nnew name\n" % (job, key, key, memo, date, time, job, key, date,
                                            "\n".join(lines if table else lines[2:])))


def fixture_text(path):
    """A consistent fixture for an added row file or its memo, else None."""
    if reg.ROW_FILE_RE.match(path):
        return fixture_row(path)
    m = reg.MEMO_PATH_RE.match(path)
    return fixture_memo(m.group("key"), m.group("date")) if m else None


# REVIEW (MODEL v4.5.0): the new memo plus the move of its one prior memo to
# archive/memos/{KEY}/ (a delete plus a byte-identical add, same filename).
TROW_PRIOR = "TROW_2026-09-08_GSC.md"
TROW_NEW = "TROW_2026-10-04_GSC.md"
REVIEW_TROW_MOVE = E(
    "D memos/TROW/" + TROW_PRIOR,
    "A archive/memos/TROW/" + TROW_PRIOR,
)
REVIEW_TROW_FULL = E(
    "A memos/TROW/" + TROW_NEW,
    "A queue/rows/2026-10-04_2250_REVIEW_TROW.md",
    "A queue/runs/2026-10-04_2250_REVIEW_TROW.md",
    "D queue/evidence/TROW_2026-09-08_v4-REVIEW-draft.md",
) + REVIEW_TROW_MOVE
REVIEW_TROW_BLOBS = {
    ("base", "memos/TROW/" + TROW_PRIOR): "blob-trow-v5",
    ("head", "archive/memos/TROW/" + TROW_PRIOR): "blob-trow-v5",
}
REVIEW_TROW_TREES = {
    ("base", "memos/TROW"): [TROW_PRIOR],
    ("head", "memos/TROW"): [TROW_NEW],
}
HFG_PRIOR = "HFG.DE_2026-08-31_GSC.md"
HFG_NEW = "HFG.DE_2026-10-04_GSC.md"
REVIEW_HFG_FULL = E(
    "A memos/HFG.DE/" + HFG_NEW,
    "D memos/HFG.DE/" + HFG_PRIOR,
    "A archive/memos/HFG.DE/" + HFG_PRIOR,
    "A queue/rows/2026-10-04_2250_REVIEW_HFG.DE.md",
    "A queue/runs/2026-10-04_2250_REVIEW_HFG.DE.md",
)
REVIEW_HFG_BLOBS = {
    ("base", "memos/HFG.DE/" + HFG_PRIOR): "blob-hfg-v3",
    ("head", "archive/memos/HFG.DE/" + HFG_PRIOR): "blob-hfg-v3",
}
REVIEW_HFG_TREES = {
    ("base", "memos/HFG.DE"): [HFG_PRIOR],
    ("head", "memos/HFG.DE"): [HFG_NEW],
}


# ================================================================ OK runs

# ANALYSE
case("ANALYSE full memo + row + run note + evidence deletion", AN_CGNX,
     "GSC ANALYSE CGNX 2026-10-04 — BUY", ANALYSE_CGNX_FULL, "ok")
case("ANALYSE claim stub only ([running])", AN_ATCO, "GSC ANALYSE ATCO-B.ST 2026-10-04 [running]",
     E("A queue/runs/2026-10-04_2250_ANALYSE_ATCO-B.ST.md"), "ok")
case("ANALYSE full memo, dotted key 7309.T", AN_7309, "GSC ANALYSE 7309.T 2026-10-04 — WATCH", E(
    "A memos/7309.T/7309.T_2026-10-04_GSC.md",
    "A queue/rows/2026-10-04_2250_ANALYSE_7309.T.md",
    "A queue/runs/2026-10-04_2250_ANALYSE_7309.T.md",
    "D queue/evidence/7309.T_draft-evidence_2026-09.md",
), "ok")
case("ANALYSE full memo, hyphen key ATCO-B.ST", AN_ATCO, "GSC ANALYSE ATCO-B.ST 2026-10-04 — AVOID", E(
    "A memos/ATCO-B.ST/ATCO-B.ST_2026-10-04_GSC.md",
    "A queue/rows/2026-10-04_2250_ANALYSE_ATCO-B.ST.md",
    "A queue/runs/2026-10-04_2250_ANALYSE_ATCO-B.ST.md",
), "ok")
case("ANALYSE INCOMPLETE (evidence draft kept), key CARL-B.CO", AN_CARL,
     "GSC ANALYSE CARL-B.CO 2026-10-04 — INCOMPLETE", E(
         "A queue/evidence/CARL-B.CO_2026-10-04_INCOMPLETE.md",
         "A queue/rows/2026-10-04_2250_ANALYSE_CARL-B.CO.md",
         "A queue/runs/2026-10-04_2250_ANALYSE_CARL-B.CO.md",
     ), "ok")
case("ANALYSE PRIOR (row + run note only)", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — PRIOR", E(
    "A queue/rows/2026-10-04_2250_ANALYSE_CGNX.md",
    "A queue/runs/2026-10-04_2250_ANALYSE_CGNX.md",
), "ok")
case("ANALYSE re-keyed after claim (memo key != branch key)",
     "claude/gsc-analyse-RDSA.AS-%s-%s" % (D, T), "GSC ANALYSE RDSA.AS 2026-10-04 — WATCH", E(
         "A memos/SHEL.L/SHEL.L_2026-10-04_GSC.md",
         "A queue/rows/2026-10-04_2250_ANALYSE_SHEL.L.md",
         "A queue/runs/2026-10-04_2250_ANALYSE_RDSA.AS.md",
         "D queue/evidence/RDSA.AS_draft-evidence_2026-09.md",
     ), "ok")
case("ANALYSE re-keyed INCOMPLETE (no memo): row and evidence under the resolved key",
     "claude/gsc-analyse-RDSA.AS-%s-%s" % (D, T), "GSC ANALYSE RDSA.AS 2026-10-04 — INCOMPLETE", E(
         "A queue/rows/2026-10-04_2250_ANALYSE_SHEL.L.md",
         "A queue/evidence/SHEL.L_2026-10-04_INCOMPLETE.md",
         "A queue/runs/2026-10-04_2250_ANALYSE_RDSA.AS.md",
     ), "ok")
case("ANALYSE queue exhausted, run note only", AN_KEYLESS, "GSC ANALYSE 2026-10-04 — queue exhausted",
     E("A queue/runs/2026-10-04_2250_ANALYSE.md"), "ok")
case("ANALYSE queue exhausted, with keyless QUEUE row", AN_KEYLESS, "GSC ANALYSE 2026-10-04 — queue exhausted", E(
    "A queue/rows/2026-10-04_2250_ANALYSE.md",
    "A queue/runs/2026-10-04_2250_ANALYSE.md",
), "ok")

# REVIEW
case("REVIEW memo + prior moved to archive/memos + row + run note + evidence deletion", RV_TROW,
     "GSC REVIEW TROW 2026-10-04 — AVOID; Past ROCE re-test", REVIEW_TROW_FULL, "ok",
     blobs=REVIEW_TROW_BLOBS, trees=REVIEW_TROW_TREES)
case("REVIEW of a held name (HELD · title), dotted key HFG.DE, prior moved", RV_HFG,
     "HELD · GSC REVIEW HFG.DE 2026-10-04 — WATCH; zone SELL-FLAG", REVIEW_HFG_FULL, "ok",
     blobs=REVIEW_HFG_BLOBS, trees=REVIEW_HFG_TREES)
case("REVIEW move: archive/memos/{KEY}/ already holds older versions", RV_TROW,
     "GSC REVIEW TROW 2026-10-04 — AVOID; v6", REVIEW_TROW_FULL, "ok",
     blobs=REVIEW_TROW_BLOBS,
     trees={**REVIEW_TROW_TREES, ("base", "archive/memos/TROW"): ["TROW_2026-06-10_GSC.md",
                                                                  "TROW_2026-07-04_GSC.md"]})
case("REVIEW claim stub, HELD [running]", RV_HFG, "HELD · GSC REVIEW HFG.DE 2026-10-04 [running]",
     E("A queue/runs/2026-10-04_2250_REVIEW_HFG.DE.md"), "ok")
case("REVIEW INCOMPLETE", RV_TROW, "GSC REVIEW TROW 2026-10-04 — INCOMPLETE", E(
    "A queue/evidence/TROW_2026-10-04_INCOMPLETE.md",
    "A queue/rows/2026-10-04_2250_REVIEW_TROW.md",
    "A queue/runs/2026-10-04_2250_REVIEW_TROW.md",
), "ok")

# SWEEP, SEED
case("SWEEP row + run note", SWEEP, "GSC SWEEP 2026-10-03 — 14 prices, 2 review requests", E(
    "A queue/rows/2026-10-03_0700_SWEEP.md",
    "A queue/runs/2026-10-03_0700_SWEEP.md",
), "ok")
case("SEED proposal + run note", SEED, "GSC SEED 2026-10-05 — 10 candidates", E(
    "A queue/proposals/2026-10-05_0800_QUEUE-SEED.md",
    "A queue/runs/2026-10-05_0800_SEED.md",
), "ok")

# INTAKE
case("INTAKE full: snapshot, TODO + DRAFT_QUEUE archives, proposal move, row deletions",
     INTAKE, "GSC INTAKE 2026-10-04 — register v305", INTAKE_FULL, "ok", blobs=INTAKE_BLOBS)
case("INTAKE queue-only (no register change, no snapshot)", INTAKE, "GSC INTAKE 2026-10-04 — TODO v37", E(
    "M queue/TODO.md",
    "A " + INTAKE_TODO_ARCHIVE,
    "D queue/rows/2026-10-03_2250_ANALYSE.md",
    "A queue/runs/2026-10-04_0650_INTAKE.md",
), "ok", blobs=INTAKE_BLOBS)
case("INTAKE year-end snapshot pair in the outgoing date's year folder",
     "claude/gsc-intake-2026-01-02-0650", "GSC INTAKE 2026-01-02 — register v290", E(
         "M _REGISTER.md",
         "M register.csv",
         "A archive/registers/2025/REGISTER_v289_2025-12-31.md",
         "A archive/registers/2025/REGISTER_v289_2025-12-31.csv",
         "A queue/runs/2026-01-02_0650_INTAKE.md",
     ), "ok", blobs={("base", "_REGISTER.md"): "r289", ("head", "archive/registers/2025/REGISTER_v289_2025-12-31.md"): "r289",
                     ("base", "register.csv"): "c289", ("head", "archive/registers/2025/REGISTER_v289_2025-12-31.csv"): "c289"})
case("INTAKE DRAFT_QUEUE archive with a dotted version (v1.1)", INTAKE, "GSC INTAKE 2026-10-04 — DRAFT_QUEUE v2", E(
    "M queue/DRAFT_QUEUE.md",
    "A archive/queue/DRAFT_QUEUE_v1.1_2026-10-03.md",
    "D queue/rows/2026-10-03_2250_ANALYSE.md",
    "A queue/runs/2026-10-04_0650_INTAKE.md",
), "ok", blobs={("base", "queue/DRAFT_QUEUE.md"): "blob-dq-v1.1",
                ("head", "archive/queue/DRAFT_QUEUE_v1.1_2026-10-03.md"): "blob-dq-v1.1"})

# register.csv twin (MODEL v4.5.0 section 7.1)
def texts_with(**over):
    table = dict(INTAKE_TEXTS)
    for name, text in over.items():
        table[("head", {"csv": "register.csv", "md": "_REGISTER.md"}[name])] = text
    return table


case("INTAKE register.md without register.csv fails", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     without(INTAKE_FULL, "M register.csv"), "fail", blobs=INTAKE_BLOBS, msg="change together")
case("INTAKE register.csv without _REGISTER.md fails", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     without(INTAKE_FULL, "M _REGISTER.md"), "fail", blobs=INTAKE_BLOBS, msg="change together")
case("INTAKE register change without the .csv snapshot fails", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     without(INTAKE_FULL, "A " + INTAKE_CSV_SNAPSHOT), "fail", blobs=INTAKE_BLOBS, msg="found 1 .md, 0 .csv")
case("INTAKE register change without any snapshot fails", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     without(INTAKE_FULL, "A " + INTAKE_CSV_SNAPSHOT, "A " + INTAKE_SNAPSHOT), "fail", blobs=INTAKE_BLOBS,
     msg="found 0 .md, 0 .csv")
case("INTAKE snapshot pair without a register change fails", INTAKE, "GSC INTAKE 2026-10-04 — TODO v37",
     without(INTAKE_FULL, "M _REGISTER.md", "M register.csv"), "fail", blobs=INTAKE_BLOBS,
     msg="without a register change")
case("INTAKE .csv snapshot is not a byte copy", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     INTAKE_FULL, "fail", blobs={**INTAKE_BLOBS, ("head", INTAKE_CSV_SNAPSHOT): "blob-edited"},
     msg="register.csv snapshot is not a byte copy")
case("INTAKE .csv snapshot in the wrong year folder", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     without(INTAKE_FULL, "A " + INTAKE_CSV_SNAPSHOT) + E("A archive/registers/2025/REGISTER_v304_2026-10-03.csv"),
     "fail", blobs=INTAKE_BLOBS, msg="snapshot folder 2025")
case("INTAKE .md and .csv snapshots of different versions", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     without(INTAKE_FULL, "A " + INTAKE_CSV_SNAPSHOT) + E("A archive/registers/2026/REGISTER_v303_2026-10-03.csv"),
     "fail", blobs={**INTAKE_BLOBS, ("head", "archive/registers/2026/REGISTER_v303_2026-10-03.csv"): "blob-csv-v304"},
     msg="share N and date")
case("INTAKE .md and .csv snapshots of different dates", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     without(INTAKE_FULL, "A " + INTAKE_CSV_SNAPSHOT) + E("A archive/registers/2026/REGISTER_v304_2026-10-02.csv"),
     "fail", blobs={**INTAKE_BLOBS, ("head", "archive/registers/2026/REGISTER_v304_2026-10-02.csv"): "blob-csv-v304"},
     msg="share N and date")
case("INTAKE register.csv with a wrong header fails", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     INTAKE_FULL, "fail", blobs=INTAKE_BLOBS,
     texts=texts_with(csv=INTAKE_CSV.replace("key,company,", "ticker,company,", 1)), msg="7.1b header")
case("INTAKE register.csv row count differs from names_total", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     INTAKE_FULL, "fail", blobs=INTAKE_BLOBS,
     texts=texts_with(md=INTAKE_MD.replace("names_total: 3", "names_total: 4")), msg="names_total is 4")
case("INTAKE _REGISTER.md hand-edited (not the rendering of register.csv)", INTAKE,
     "GSC INTAKE 2026-10-04 — register v305", INTAKE_FULL, "fail", blobs=INTAKE_BLOBS,
     texts=texts_with(md=INTAKE_MD.replace("| CGNX Inc. |", "| Cognex |")), msg="not the rendering")
case("INTAKE register.csv with an invalid row (AVOID without a failed gate)", INTAKE,
     "GSC INTAKE 2026-10-04 — register v305", INTAKE_FULL, "fail", blobs=INTAKE_BLOBS,
     texts=texts_with(csv=reg.csv_text(REG_ROWS[:2] + [reg_row("BAD", "5.0", verdict="AVOID", section="AVOID-1")])),
     msg="no failed gate")
case("INTAKE register.csv with CR line ends fails", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     INTAKE_FULL, "fail", blobs=INTAKE_BLOBS, texts=texts_with(csv=INTAKE_CSV.replace("\n", "\r\n")),
     msg="CR line ends")
case("INTAKE register change without a text lookup fails closed", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     INTAKE_FULL, "fail", blobs=INTAKE_BLOBS, no_text=True, msg="unverifiable")
case("INTAKE adds register.csv (only M is allowed)", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     without(INTAKE_FULL, "M register.csv") + E("A register.csv"), "fail", blobs=INTAKE_BLOBS,
     msg="not in the INTAKE write contract")
case("INTAKE deletes register.csv", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     E("D register.csv"), "fail", blobs=INTAKE_BLOBS, msg="INTAKE may delete only")
case("ANALYSE touches register.csv", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — WATCH (Cheapness)",
     ANALYSE_CGNX_FULL + E("M register.csv"), "fail", msg="not in the ANALYSE write contract")
case("REVIEW touches register.csv", RV_TROW, "GSC REVIEW TROW 2026-10-04 — WATCH; v6",
     E("M register.csv", "A queue/runs/2026-10-04_2250_REVIEW_TROW.md"), "fail",
     msg="not in the REVIEW write contract")
case("SWEEP touches register.csv", SWEEP, "GSC SWEEP 2026-10-03 — 90/95 priced",
     E("A queue/rows/2026-10-03_0700_SWEEP.md", "M register.csv"), "fail", msg="not in the SWEEP write contract")
case("SEED adds a register .csv snapshot", SEED, "GSC SEED 2026-10-05 — 3 new",
     E("A queue/proposals/2026-10-05_0800_QUEUE-SEED.md",
       "A archive/registers/2026/REGISTER_v304_2026-10-03.csv"), "fail", msg="not in the SEED write contract")
case("a .csv anywhere else fails (queue/)", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     E("A queue/runs/x.csv"), "fail", msg="only .md files")
case("a .csv anywhere else fails (memos/)", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — WATCH (Cheapness)",
     E("A memos/CGNX/CGNX.csv"), "fail", msg="only .md files")
case("a .csv snapshot outside archive/registers/ fails", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     E("A archive/queue/REGISTER_v304_2026-10-03.csv"), "fail", msg="only .md files")

saved_path, saved_tool = g.TOOL_PATH, list(g._TOOL)
g.TOOL_PATH, g._TOOL[:] = os.path.join(os.path.dirname(g.TOOL_PATH), "missing_tool.py"), []
case("INTAKE register change fails closed when the register tool cannot load", INTAKE,
     "GSC INTAKE 2026-10-04 — register v305", INTAKE_FULL, "fail", blobs=INTAKE_BLOBS, msg="cannot load")
g.TOOL_PATH, g._TOOL[:] = saved_path, saved_tool

# Non-routine PRs are skipped (pass)
case("attended framework PR is skipped", "claude/model-v4.4.0-routines", "MODEL v4.4.0 — routines migration",
     E("M model/MODEL.md", "A .claude/hooks/gsc_guard.py"), "skip")
case("non-routine PR to another base is still skipped", "jakub/notes", "Notes", E("A x.txt"), "skip",
     base="claude/other")

# ============================================================ violations

# ANALYSE / REVIEW key binding
case("ANALYSE deletes another key's evidence", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     ANALYSE_CGNX_FULL + E("D queue/evidence/SYM_draft-evidence_2026-09.md"), "fail",
     msg="not in the ANALYSE write contract")
case("ANALYSE deletes a multi-name evidence file", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     E("D queue/evidence/REVIEW-seeds_2026-09-09.md"), "fail", msg="not in the ANALYSE write contract")
case("ANALYSE adds a second memo", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     ANALYSE_CGNX_FULL + E("A memos/SYM/SYM_2026-10-04_GSC.md"), "fail", msg="memos added in one")
case("ANALYSE writes a SWEEP row", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     ANALYSE_CGNX_FULL + E("A queue/rows/2026-10-04_2250_SWEEP.md"), "fail",
     msg="not in the ANALYSE write contract")
case("ANALYSE row with the wrong time T", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     E("A queue/rows/2026-10-04_2251_ANALYSE_CGNX.md"), "fail", msg="not in the ANALYSE write contract")
case("ANALYSE memo dated off the run date", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     E("A memos/CGNX/CGNX_2026-10-03_GSC.md"), "fail", msg="memo date")
case("ANALYSE memo in another key's folder", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     E("A memos/CGNX/TROW_2026-10-04_GSC.md"), "fail", msg="a memo must be")
case("ANALYSE keyless branch adds a memo", AN_KEYLESS, "GSC ANALYSE 2026-10-04 — BUY",
     E("A memos/CGNX/CGNX_2026-10-04_GSC.md"), "fail", msg="keyless ANALYSE branch")
case("ANALYSE without memo writes two keyed rows", "claude/gsc-analyse-RDSA.AS-%s-%s" % (D, T),
     "GSC ANALYSE RDSA.AS 2026-10-04 — INCOMPLETE", E(
         "A queue/rows/2026-10-04_2250_ANALYSE_SHEL.L.md",
         "A queue/rows/2026-10-04_2250_ANALYSE_SYM.md",
     ), "fail", msg="not in the ANALYSE write contract")
case("ANALYSE re-keyed without memo deletes the resolved key's evidence",
     "claude/gsc-analyse-RDSA.AS-%s-%s" % (D, T), "GSC ANALYSE RDSA.AS 2026-10-04 — INCOMPLETE", E(
         "A queue/rows/2026-10-04_2250_ANALYSE_SHEL.L.md",
         "D queue/evidence/SHEL.L_draft-evidence_2026-09.md",
     ), "fail", msg="not in the ANALYSE write contract")
# v4.8.0 review: evidence leaves only alongside the name's memo (MODEL 8.7 item 4), never on INCOMPLETE.
case("REVIEW INCOMPLETE deletes the first resume record", RV_TROW, "GSC REVIEW TROW 2026-10-04 — INCOMPLETE", E(
    "A queue/evidence/TROW_2026-10-04_INCOMPLETE.md",
    "D queue/evidence/TROW_2026-10-01_INCOMPLETE.md",
    "A queue/rows/2026-10-04_2250_REVIEW_TROW.md",
    "A queue/runs/2026-10-04_2250_REVIEW_TROW.md",
), "fail", msg="not in the REVIEW write contract")
case("REVIEW claim stub deletes evidence", RV_HFG, "HELD · GSC REVIEW HFG.DE 2026-10-04 [running]", E(
    "A queue/runs/2026-10-04_2250_REVIEW_HFG.DE.md",
    "D queue/evidence/HFG.DE_draft-evidence_2026-09.md",
), "fail", msg="not in the REVIEW write contract")
case("ANALYSE INCOMPLETE deletes its own key's evidence", AN_CARL, "GSC ANALYSE CARL-B.CO 2026-10-04 — INCOMPLETE", E(
    "A queue/evidence/CARL-B.CO_2026-10-04_INCOMPLETE.md",
    "D queue/evidence/CARL-B.CO_2026-10-01_INCOMPLETE.md",
    "A queue/rows/2026-10-04_2250_ANALYSE_CARL-B.CO.md",
    "A queue/runs/2026-10-04_2250_ANALYSE_CARL-B.CO.md",
), "fail", msg="not in the ANALYSE write contract")
case("ANALYSE PRIOR deletes evidence", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — PRIOR", E(
    "A queue/rows/2026-10-04_2250_ANALYSE_CGNX.md",
    "A queue/runs/2026-10-04_2250_ANALYSE_CGNX.md",
    "D queue/evidence/CGNX_draft-evidence_2026-09.md",
), "fail", msg="not in the ANALYSE write contract")
case("ANALYSE keyless branch writes a keyed row", AN_KEYLESS, "GSC ANALYSE 2026-10-04 — queue exhausted",
     E("A queue/rows/2026-10-04_2250_ANALYSE_CGNX.md"), "fail", msg="not in the ANALYSE write contract")
case("ANALYSE modifies the register", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     ANALYSE_CGNX_FULL + E("M _REGISTER.md"), "fail", msg="not in the ANALYSE write contract")
case("REVIEW memo for another key", RV_TROW, "GSC REVIEW TROW 2026-10-04 — HOLD",
     E("A memos/NKE/NKE_2026-10-04_GSC.md"), "fail", msg="REVIEW memo must be for the branch key")
case("REVIEW overwrites a prior memo", RV_TROW, "GSC REVIEW TROW 2026-10-04 — HOLD",
     E("M memos/TROW/TROW_2026-09-08_GSC.md"), "fail", msg="a routine never changes a memo")
case("REVIEW writes a keyless ANALYSE row", RV_TROW, "GSC REVIEW TROW 2026-10-04 — HOLD",
     E("A queue/rows/2026-10-04_2250_ANALYSE.md"), "fail", msg="not in the REVIEW write contract")

# SWEEP / SEED
case("SWEEP adds a memo", SWEEP, "GSC SWEEP 2026-10-03 — 14 prices",
     E("A memos/CGNX/CGNX_2026-10-03_GSC.md"), "fail", msg="not in the SWEEP write contract")
case("SEED edits DRAFT_QUEUE directly", SEED, "GSC SEED 2026-10-05 — 10 candidates",
     E("M queue/DRAFT_QUEUE.md"), "fail", msg="not in the SEED write contract")
case("SEED run note under the QUEUE-SEED name", SEED, "GSC SEED 2026-10-05 — 10 candidates",
     E("A queue/runs/2026-10-05_0800_QUEUE-SEED.md"), "fail", msg="not in the SEED write contract")

# Global rules
case("nested CLAUDE.md in queue/rows", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     ANALYSE_CGNX_FULL + E("A queue/rows/CLAUDE.md"), "fail", msg="file name not allowed")
case("nested AGENTS.md in queue/runs", SWEEP, "GSC SWEEP 2026-10-03 — 14 prices",
     E("A queue/runs/AGENTS.md"), "fail", msg="file name not allowed")
case("lower-case claude.md", SEED, "GSC SEED 2026-10-05 — 10 candidates",
     E("A queue/proposals/claude.md"), "fail", msg="file name not allowed")
case("hidden .claude folder under queue/runs", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     E("A queue/runs/.claude/rules/x.md"), "fail", msg="hidden path segment")
case("evidence README deletion", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     ANALYSE_CGNX_FULL + E("D queue/evidence/README.md"), "fail", msg="file name not allowed")
case("rows README deletion by INTAKE", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     E("D queue/rows/README.md"), "fail", msg="file name not allowed")
case("non-.md file", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     E("A queue/evidence/CGNX_chart.png"), "fail", msg="only .md files")
case("locked path model/", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     E("M model/MODEL.md"), "fail", msg="framework-locked")
case("locked path routines/", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     E("M routines/INTAKE.md"), "fail", msg="framework-locked")
case("locked path .github/", SWEEP, "GSC SWEEP 2026-10-03 — 14 prices",
     E("A .github/workflows/x.md"), "fail", msg="framework-locked")
case("rename status is rejected", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     [("R100", "queue/proposals/%s -> archive/queue/proposals/%s" % (PROPOSAL, PROPOSAL))], "fail",
     msg="status R100 is not allowed")
case("type-change status is rejected", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     E("T queue/runs/2026-10-04_2250_ANALYSE_CGNX.md"), "fail", msg="status T is not allowed")
case("control character in a file name", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     [("A", "queue/runs/x\n::warning::y.md")], "fail", msg="control character")

# Classification: title, branch, base
case("title job differs from branch job (SEED branch, INTAKE title)", SEED, "GSC INTAKE 2026-10-05 [running]",
     E("M queue/DRAFT_QUEUE.md"), "fail", msg="does not match branch job")
case("HELD title job differs from branch job", RV_HFG, "HELD · GSC ANALYSE HFG.DE 2026-10-04 — HOLD",
     E("A queue/runs/2026-10-04_2250_REVIEW_HFG.DE.md"), "fail", msg="does not match branch job")
case("routine branch with a non-GSC title", AN_CGNX, "Add CGNX memo",
     ANALYSE_CGNX_FULL, "fail", msg="does not start with 'GSC")
case("GSC title on a non-gsc branch", "claude/sweep-2026-10-03", "GSC SWEEP 2026-10-03 — 14 prices",
     E("M _REGISTER.md"), "fail", msg="not a routine branch name")
case("base is not main", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     ANALYSE_CGNX_FULL, "fail", base="claude/gsc-analyse-CGNX-x", msg="targets")
case("malformed branch: queue-seed spelling", "claude/gsc-queue-seed-2026-10-05-0800",
     "GSC SEED 2026-10-05 — 10 candidates", E("A queue/runs/2026-10-05_0800_SEED.md"), "fail",
     msg="not a routine branch name")
case("malformed branch: no time", "claude/gsc-analyse-CGNX-2026-10-04",
     "GSC ANALYSE CGNX 2026-10-04 — BUY", ANALYSE_CGNX_FULL, "fail", msg="not a routine branch name")
case("malformed branch: month 13", "claude/gsc-analyse-CGNX-2026-13-04-2250",
     "GSC ANALYSE CGNX 2026-13-04 — BUY", E(), "fail", msg="not a valid date")
case("malformed branch: time 2460", "claude/gsc-analyse-CGNX-2026-10-04-2460",
     "GSC ANALYSE CGNX 2026-10-04 — BUY", E(), "fail", msg="not a valid HHMM")
case("malformed branch: keyless REVIEW", "claude/gsc-review-2026-10-04-2250",
     "GSC REVIEW 2026-10-04 — HOLD", E(), "fail", msg="must carry the KEY")
case("malformed branch: keyed SWEEP", "claude/gsc-sweep-TROW-2026-10-03-0700",
     "GSC SWEEP 2026-10-03 — 14 prices", E(), "fail", msg="must not carry a KEY")
case("malformed branch: claude/gscx prefix", "claude/gscx-analyse", "Fix", E(), "fail",
     msg="not a routine branch name")

# INTAKE byte copies and scope
case("INTAKE snapshot is not a byte copy of the outgoing register", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     INTAKE_FULL, "fail", blobs={**INTAKE_BLOBS, ("head", INTAKE_SNAPSHOT): "blob-edited"}, msg="not a byte copy")
case("INTAKE TODO archive is not a byte copy", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     INTAKE_FULL, "fail", blobs={**INTAKE_BLOBS, ("head", INTAKE_TODO_ARCHIVE): "blob-edited"}, msg="not a byte copy")
case("INTAKE DRAFT_QUEUE archive is not a byte copy", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     INTAKE_FULL, "fail", blobs={**INTAKE_BLOBS, ("head", INTAKE_DQ_ARCHIVE): "blob-edited"}, msg="not a byte copy")
case("INTAKE archived proposal rewritten", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     INTAKE_FULL, "fail",
     blobs={**INTAKE_BLOBS, ("head", "archive/queue/proposals/" + PROPOSAL): "blob-edited"}, msg="not a byte copy")
case("INTAKE archives a proposal without deleting it", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     without(INTAKE_FULL, "D queue/proposals/" + PROPOSAL), "fail", blobs=INTAKE_BLOBS,
     msg="is not deleted in this PR")
case("INTAKE snapshot in the wrong year folder", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     E("A archive/registers/2025/REGISTER_v304_2026-10-03.md"), "fail", blobs=INTAKE_BLOBS, msg="snapshot folder")
case("INTAKE modifies IDEAS", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     INTAKE_FULL + E("M queue/IDEAS.md"), "fail", blobs=INTAKE_BLOBS, msg="INTAKE may modify only")
case("INTAKE modifies a memo", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     E("M memos/TROW/TROW_2026-09-08_GSC.md"), "fail", blobs=INTAKE_BLOBS, msg="INTAKE may modify only")
case("INTAKE adds a memo", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     E("A memos/CGNX/CGNX_2026-10-04_GSC.md"), "fail", blobs=INTAKE_BLOBS,
     msg="not in the INTAKE write contract")
case("INTAKE deletes an evidence file", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     E("D queue/evidence/CGNX_draft-evidence_2026-09.md"), "fail", blobs=INTAKE_BLOBS,
     msg="INTAKE may delete only")
case("INTAKE run note with the wrong time", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     E("A queue/runs/2026-10-04_0700_INTAKE.md"), "fail", blobs=INTAKE_BLOBS,
     msg="not in the INTAKE write contract")

# Root archive/ (MODEL v4.5.0): append-only, retired registers/ and queue/archive/
case("INTAKE snapshot at the retired registers/ path", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     E("M _REGISTER.md", "A registers/2026/REGISTER_v304_2026-10-03.md"), "fail",
     blobs={**INTAKE_BLOBS, ("head", "registers/2026/REGISTER_v304_2026-10-03.md"): "blob-register-v304"},
     msg="retired path")
case("INTAKE TODO archive at the retired queue/archive/ path", INTAKE, "GSC INTAKE 2026-10-04 — TODO v37",
     E("M queue/TODO.md", "A queue/archive/TODO_v36_2026-10-02.md"), "fail",
     blobs={**INTAKE_BLOBS, ("head", "queue/archive/TODO_v36_2026-10-02.md"): "blob-todo-v36"},
     msg="retired path")
case("INTAKE proposal moved to the retired queue/archive/proposals/", INTAKE, "GSC INTAKE 2026-10-04 — TODO v37",
     E("D queue/proposals/" + PROPOSAL, "A queue/archive/proposals/" + PROPOSAL), "fail",
     blobs={**INTAKE_BLOBS, ("head", "queue/archive/proposals/" + PROPOSAL): "blob-proposal"},
     msg="retired path")
case("INTAKE adds an archived memo", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     E("A archive/memos/TROW/TROW_2026-09-08_GSC.md"), "fail", blobs=INTAKE_BLOBS,
     msg="not in the INTAKE write contract")
case("INTAKE deletes a register snapshot", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     INTAKE_FULL + E("D archive/registers/2026/REGISTER_v303_2026-10-03.md"), "fail", blobs=INTAKE_BLOBS,
     msg="append-only")
case("INTAKE rewrites a TODO archive", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     INTAKE_FULL + E("M archive/queue/TODO_v35_2026-10-01.md"), "fail", blobs=INTAKE_BLOBS,
     msg="append-only")
case("INTAKE deletes an archived proposal (mixed-case top folder)", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     E("D Archive/queue/proposals/" + PROPOSAL), "fail", blobs=INTAKE_BLOBS, msg="append-only")
case("REVIEW modifies an archived memo", RV_TROW, "GSC REVIEW TROW 2026-10-04 — HOLD",
     E("A memos/TROW/TROW_2026-10-04_GSC.md", "M archive/memos/TROW/TROW_2026-07-01_GSC.md"), "fail",
     msg="append-only")
case("REVIEW deletes an archived memo", RV_TROW, "GSC REVIEW TROW 2026-10-04 — HOLD",
     E("D archive/memos/TROW/TROW_2026-07-01_GSC.md"), "fail", msg="append-only")
case("ANALYSE adds a file under archive/", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     ANALYSE_CGNX_FULL + E("A archive/memos/CGNX/CGNX_2026-09-01_GSC.md"), "fail",
     msg="ANALYSE never moves or deletes a memo")
case("ANALYSE writes the retired registers/ path", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     E("A registers/2026/x.md"), "fail", msg="retired path")
case("SWEEP adds a file under archive/", SWEEP, "GSC SWEEP 2026-10-03 — 14 prices",
     E("A archive/x.md"), "fail", msg="not in the SWEEP write contract")
case("SEED archives its own proposal", SEED, "GSC SEED 2026-10-05 — 10 candidates",
     E("A archive/queue/proposals/2026-10-05_0800_QUEUE-SEED.md"), "fail", msg="not in the SEED write contract")


# REVIEW full memo and prior move (MODEL v4.5.0 sections 6.6, 7.4a; spec B 2.13)
case("REVIEW memo without moving the prior", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6",
     without(REVIEW_TROW_FULL, "D memos/TROW/" + TROW_PRIOR, "A archive/memos/TROW/" + TROW_PRIOR), "fail",
     blobs=REVIEW_TROW_BLOBS, trees={("base", "memos/TROW"): [TROW_PRIOR],
                                     ("head", "memos/TROW"): [TROW_PRIOR, TROW_NEW]},
     msg="must move exactly its one prior")
case("REVIEW deletes the prior but archives nothing", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6",
     without(REVIEW_TROW_FULL, "A archive/memos/TROW/" + TROW_PRIOR), "fail",
     blobs=REVIEW_TROW_BLOBS, trees=REVIEW_TROW_TREES, msg="the archived prior must be")
case("REVIEW INCOMPLETE moves the prior anyway (no new memo)", RV_TROW, "GSC REVIEW TROW 2026-10-04 — INCOMPLETE",
     E("A queue/evidence/TROW_2026-10-04_INCOMPLETE.md",
       "A queue/rows/2026-10-04_2250_REVIEW_TROW.md",
       "A queue/runs/2026-10-04_2250_REVIEW_TROW.md") + REVIEW_TROW_MOVE, "fail",
     blobs=REVIEW_TROW_BLOBS, trees=REVIEW_TROW_TREES, msg="moves no memo")
case("REVIEW archived prior is not a byte copy", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6",
     REVIEW_TROW_FULL, "fail", blobs={**REVIEW_TROW_BLOBS, ("head", "archive/memos/TROW/" + TROW_PRIOR): "edited"},
     trees=REVIEW_TROW_TREES, msg="not a byte copy")
case("REVIEW archived prior missing at the merge base", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6",
     REVIEW_TROW_FULL, "fail", blobs={("head", "archive/memos/TROW/" + TROW_PRIOR): "blob-trow-v5"},
     trees=REVIEW_TROW_TREES, msg="does not exist at the merge base")
case("REVIEW moves another key's memo", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6", E(
    "A memos/TROW/" + TROW_NEW,
    "D memos/NKE/NKE_2026-09-08_GSC.md",
    "A archive/memos/NKE/NKE_2026-09-08_GSC.md",
    "A queue/rows/2026-10-04_2250_REVIEW_TROW.md",
    "A queue/runs/2026-10-04_2250_REVIEW_TROW.md",
), "fail", blobs={("base", "memos/NKE/NKE_2026-09-08_GSC.md"): "n", ("head", "archive/memos/NKE/NKE_2026-09-08_GSC.md"): "n"},
     trees=REVIEW_TROW_TREES, msg="must move exactly its one prior")
case("REVIEW archives the prior under another filename", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6",
     without(REVIEW_TROW_FULL, "A archive/memos/TROW/" + TROW_PRIOR) + E("A archive/memos/TROW/TROW_2026-09-09_GSC.md"),
     "fail", blobs={**REVIEW_TROW_BLOBS, ("head", "archive/memos/TROW/TROW_2026-09-09_GSC.md"): "blob-trow-v5"},
     trees=REVIEW_TROW_TREES, msg="same filename")
case("REVIEW archives the prior into another key's archive folder", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6",
     without(REVIEW_TROW_FULL, "A archive/memos/TROW/" + TROW_PRIOR) + E("A archive/memos/NKE/" + TROW_PRIOR),
     "fail", blobs={**REVIEW_TROW_BLOBS, ("head", "archive/memos/NKE/" + TROW_PRIOR): "blob-trow-v5"},
     trees=REVIEW_TROW_TREES, msg="same filename")
case("REVIEW moves two prior memos", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6",
     REVIEW_TROW_FULL + E("D memos/TROW/TROW_2026-07-04_GSC.md", "A archive/memos/TROW/TROW_2026-07-04_GSC.md"),
     "fail", blobs={**REVIEW_TROW_BLOBS, ("base", "memos/TROW/TROW_2026-07-04_GSC.md"): "o",
                    ("head", "archive/memos/TROW/TROW_2026-07-04_GSC.md"): "o"},
     trees={("base", "memos/TROW"): ["TROW_2026-07-04_GSC.md", TROW_PRIOR], ("head", "memos/TROW"): [TROW_NEW]},
     msg="must move exactly its one prior")
case("REVIEW prior dated the run date (same-day supersession is attended only)", RV_TROW,
     "GSC REVIEW TROW 2026-10-04 — AVOID; v6", E(
         "A memos/TROW/" + TROW_NEW,
         "D memos/TROW/TROW_2026-10-04_GSC.md",
         "A archive/memos/TROW/TROW_2026-10-04_GSC.md",
         "A queue/rows/2026-10-04_2250_REVIEW_TROW.md",
         "A queue/runs/2026-10-04_2250_REVIEW_TROW.md",
     ), "fail", trees=REVIEW_TROW_TREES, msg="P before D")
case("REVIEW prior dated after the run date", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6", E(
    "A memos/TROW/" + TROW_NEW,
    "D memos/TROW/TROW_2026-10-05_GSC.md",
    "A archive/memos/TROW/TROW_2026-10-05_GSC.md",
), "fail", trees=REVIEW_TROW_TREES, msg="P before D")
case("REVIEW: memos/{KEY}/ holds two files at the merge base", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6",
     REVIEW_TROW_FULL, "fail", blobs=REVIEW_TROW_BLOBS,
     trees={("base", "memos/TROW"): ["TROW_2026-07-04_GSC.md", TROW_PRIOR], ("head", "memos/TROW"): [TROW_NEW]},
     msg="attended clean-up")
case("REVIEW: head folder keeps a second file", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6",
     REVIEW_TROW_FULL, "fail", blobs=REVIEW_TROW_BLOBS,
     trees={("base", "memos/TROW"): [TROW_PRIOR], ("head", "memos/TROW"): ["TROW_2026-07-04_GSC.md", TROW_NEW]},
     msg="must hold only the new memo")
case("REVIEW prior archived under a _superseded- name", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6",
     without(REVIEW_TROW_FULL, "A archive/memos/TROW/" + TROW_PRIOR)
     + E("A archive/memos/TROW/TROW_2026-09-08_GSC_superseded-v5.md"), "fail",
     blobs={**REVIEW_TROW_BLOBS, ("head", "archive/memos/TROW/TROW_2026-09-08_GSC_superseded-v5.md"): "blob-trow-v5"},
     trees=REVIEW_TROW_TREES, msg="same filename")
case("REVIEW deletes a _superseded- file from memos/", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6", E(
    "A memos/TROW/" + TROW_NEW,
    "D memos/TROW/TROW_2026-09-08_GSC_superseded-v5.md",
    "A archive/memos/TROW/TROW_2026-09-08_GSC_superseded-v5.md",
), "fail", trees=REVIEW_TROW_TREES, msg="must move exactly its one prior")
case("REVIEW modifies an archived memo next to a valid move", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6",
     REVIEW_TROW_FULL + E("M archive/memos/TROW/TROW_2026-07-04_GSC.md"), "fail",
     blobs=REVIEW_TROW_BLOBS, trees=REVIEW_TROW_TREES, msg="append-only")
case("REVIEW deletes an archived memo next to a valid move", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6",
     REVIEW_TROW_FULL + E("D archive/memos/TROW/TROW_2026-07-04_GSC.md"), "fail",
     blobs=REVIEW_TROW_BLOBS, trees=REVIEW_TROW_TREES, msg="append-only")
case("REVIEW adds a second file under archive/ next to a valid move", RV_TROW,
     "GSC REVIEW TROW 2026-10-04 — AVOID; v6",
     REVIEW_TROW_FULL + E("A archive/memos/TROW/TROW_2026-06-10_GSC.md"), "fail",
     blobs=REVIEW_TROW_BLOBS, trees=REVIEW_TROW_TREES, msg="nothing else under archive/")
case("REVIEW with no tree_lookup fails closed", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6",
     REVIEW_TROW_FULL, "fail", blobs=REVIEW_TROW_BLOBS, no_tree=True, msg="unverifiable")
case("REVIEW: git cannot list the folder at the PR head", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6",
     REVIEW_TROW_FULL, "fail", blobs=REVIEW_TROW_BLOBS,
     trees={**REVIEW_TROW_TREES, ("head", "memos/TROW"): None}, msg="unverifiable")
case("REVIEW is stale: another memo landed for the key on main", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6",
     REVIEW_TROW_FULL, "fail", blobs=REVIEW_TROW_BLOBS,
     trees={**REVIEW_TROW_TREES, ("main", "memos/TROW"): ["TROW_2026-10-03_GSC.md"]}, msg="REVIEW is stale")
case("REVIEW: git cannot list the folder on the current main", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6",
     REVIEW_TROW_FULL, "fail", blobs=REVIEW_TROW_BLOBS,
     trees={**REVIEW_TROW_TREES, ("main", "memos/TROW"): None}, msg="unverifiable")
case("REVIEW memo for another key plus a move", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6",
     E("A memos/NKE/NKE_2026-10-04_GSC.md") + REVIEW_TROW_MOVE, "fail", blobs=REVIEW_TROW_BLOBS,
     trees=REVIEW_TROW_TREES, msg="only alongside one valid new memo")
case("REVIEW adds two memos and moves the prior", RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6",
     REVIEW_TROW_FULL + E("A memos/TROW/TROW_2026-10-04b_GSC.md"), "fail", blobs=REVIEW_TROW_BLOBS,
     trees=REVIEW_TROW_TREES, msg="memos added in one")

# ANALYSE is for keys with no memo history (memos/ and archive/memos/)
case("ANALYSE memo for a key with archive/memos/{KEY}/ at the merge base", AN_CGNX,
     "GSC ANALYSE CGNX 2026-10-04 — WATCH (Cheapness)", ANALYSE_CGNX_FULL, "fail",
     trees={("base", "archive/memos/CGNX"): ["CGNX_2026-05-01_GSC.md"]}, msg="REVIEW territory")
case("ANALYSE memo for a key with memos/{KEY}/ at the merge base", AN_CGNX,
     "GSC ANALYSE CGNX 2026-10-04 — WATCH (Cheapness)", ANALYSE_CGNX_FULL, "fail",
     trees={("base", "memos/CGNX"): ["CGNX_2026-05-01_GSC.md"]}, msg="REVIEW territory")
case("ANALYSE memo for a key that landed on main since the PR's base", AN_CGNX,
     "GSC ANALYSE CGNX 2026-10-04 — WATCH (Cheapness)", ANALYSE_CGNX_FULL, "fail",
     trees={("main", "memos/CGNX"): ["CGNX_2026-10-04_GSC.md"]}, msg="the current default branch")
case("ANALYSE re-keyed memo checks the resolved key's folders", "claude/gsc-analyse-RDSA.AS-%s-%s" % (D, T),
     "GSC ANALYSE RDSA.AS 2026-10-04 — WATCH (Cheapness)", E(
         "A memos/SHEL.L/SHEL.L_2026-10-04_GSC.md",
         "A queue/rows/2026-10-04_2250_ANALYSE_SHEL.L.md",
         "A queue/runs/2026-10-04_2250_ANALYSE_RDSA.AS.md",
     ), "fail", trees={("base", "archive/memos/SHEL.L"): ["SHEL.L_2026-01-05_GSC.md"]}, msg="REVIEW territory")
case("ANALYSE deletes a memo", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     ANALYSE_CGNX_FULL + E("D memos/SYM/SYM_2026-09-01_GSC.md"), "fail", msg="ANALYSE never moves or deletes")
case("ANALYSE moves a memo to archive/memos/", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     E("D memos/SYM/SYM_2026-09-01_GSC.md", "A archive/memos/SYM/SYM_2026-09-01_GSC.md"), "fail",
     blobs={("base", "memos/SYM/SYM_2026-09-01_GSC.md"): "s", ("head", "archive/memos/SYM/SYM_2026-09-01_GSC.md"): "s"},
     msg="ANALYSE never moves or deletes")
case("ANALYSE with no tree_lookup fails closed", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     ANALYSE_CGNX_FULL, "fail", no_tree=True, msg="unverifiable")
case("ANALYSE without a memo needs no folder listing (INCOMPLETE)", AN_CARL,
     "GSC ANALYSE CARL-B.CO 2026-10-04 — INCOMPLETE (FY2021 annual report)", E(
         "A queue/evidence/CARL-B.CO_2026-10-04_INCOMPLETE.md",
         "A queue/rows/2026-10-04_2250_ANALYSE_CARL-B.CO.md",
         "A queue/runs/2026-10-04_2250_ANALYSE_CARL-B.CO.md",
     ), "ok", no_tree=True)
case("REVIEW INCOMPLETE needs no folder listing", RV_TROW, "GSC REVIEW TROW 2026-10-04 — INCOMPLETE (Q2 10-Q)", E(
    "A queue/evidence/TROW_2026-10-04_INCOMPLETE.md",
    "A queue/rows/2026-10-04_2250_REVIEW_TROW.md",
    "A queue/runs/2026-10-04_2250_REVIEW_TROW.md",
), "ok", no_tree=True)
case("SWEEP adds an archived memo", SWEEP, "GSC SWEEP 2026-10-03 — 14 prices",
     E("A archive/memos/TROW/" + TROW_PRIOR), "fail", msg="not in the SWEEP write contract")
case("SEED deletes a memo", SEED, "GSC SEED 2026-10-05 — 10 candidates",
     E("D memos/TROW/" + TROW_PRIOR), "fail", msg="not in the SEED write contract")
case("INTAKE moves a memo to archive/memos/", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     E("D memos/TROW/" + TROW_PRIOR, "A archive/memos/TROW/" + TROW_PRIOR), "fail", blobs=REVIEW_TROW_BLOBS,
     msg="INTAKE may delete only")

# Jakub's undo: a GitHub Revert PR is attended (its branch and title are not routine)
case("GitHub Revert of a routine REVIEW PR is not a routine PR", "revert-81-claude/gsc-review-BABA-2026-10-06-0611",
     'Revert "GSC REVIEW BABA 2026-10-06 — AVOID (Past + Future + SF); was WATCH"', E(
         "D memos/BABA/BABA_2026-10-06_GSC.md",
         "A memos/BABA/BABA_2026-07-02_GSC.md",
         "D archive/memos/BABA/BABA_2026-07-02_GSC.md",
         "D queue/rows/2026-10-06_0611_REVIEW_BABA.md",
     ), "skip")


# ======================================================== classify direct

def classify_case(name, ref, title, routine, job=None, key=None, clean=True):
    try:
        got_routine, info, errors = g.classify(ref, title)
    except Exception as exc:
        record(name, False, "raised %r" % exc)
        return
    ok = got_routine == routine
    if ok and routine and clean:
        ok = errors == [] and info is not None and info["job"] == job and info["key"] == key
    if ok and routine and not clean:
        ok = bool(errors)
    record(name, ok, "got %r" % ((got_routine, info, errors),))


classify_case("classify: key ATCO-B.ST", AN_ATCO, "GSC ANALYSE ATCO-B.ST 2026-10-04 [running]",
              True, "analyse", "ATCO-B.ST")
classify_case("classify: key 7309.T on REVIEW", "claude/gsc-review-7309.T-2026-10-04-2250",
              "GSC REVIEW 7309.T 2026-10-04 [running]", True, "review", "7309.T")
classify_case("classify: key CARL-B.CO", AN_CARL, "GSC ANALYSE CARL-B.CO 2026-10-04 [running]",
              True, "analyse", "CARL-B.CO")
classify_case("classify: keyless SWEEP", SWEEP, "GSC SWEEP 2026-10-03 [running]", True, "sweep", None)
classify_case("classify: keyless ANALYSE", AN_KEYLESS, "GSC ANALYSE 2026-10-04 [running]", True, "analyse", None)
classify_case("classify: abandoned title still routine", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 [abandoned]",
              True, "analyse", "CGNX")
classify_case("classify: attended PR is not routine", "claude/model-v4.4.0-routines", "MODEL v4.4.0", False)
classify_case("classify: queue-seed spelling is routine but malformed",
              "claude/gsc-queue-seed-2026-10-05-0800", "GSC SEED 2026-10-05 [running]", True, clean=False)

# Row files (MODEL v4.5.2): lint-row at the PR head
CGNX_ROW = "queue/rows/2026-10-04_2250_ANALYSE_CGNX.md"
CGNX_MEMO = "memos/CGNX/CGNX_2026-10-04_GSC.md"
CGNX_TITLE = "GSC ANALYSE CGNX 2026-10-04 — WATCH (fixture)"
ROW_TEXTS = {**INTAKE_TEXTS, ("head", CGNX_MEMO): fixture_memo("CGNX", D)}
case("ANALYSE row: the table pasted without its header and separator fails", AN_CGNX, CGNX_TITLE,
     ANALYSE_CGNX_FULL, "fail", texts={**ROW_TEXTS, ("head", CGNX_ROW): fixture_row(CGNX_ROW, table=False)},
     msg="lint-row: ## Register row (new): the header and separator lines are missing")
case("ANALYSE row: a hand-edited verdict cell fails", AN_CGNX, CGNX_TITLE, ANALYSE_CGNX_FULL, "fail",
     texts={**ROW_TEXTS, ("head", CGNX_ROW): fixture_row(CGNX_ROW).replace("| WATCH |", "| AVOID |")},
     msg="verdicts differ: row table AVOID, memo WATCH")
case("ANALYSE row: its memo unreadable at the head fails closed", AN_CGNX, CGNX_TITLE, ANALYSE_CGNX_FULL,
     "fail", texts={**INTAKE_TEXTS, ("head", CGNX_ROW): fixture_row(CGNX_ROW)}, msg="memo_path: cannot read")
case("ANALYSE row: unreadable at the head fails closed", AN_CGNX, CGNX_TITLE, ANALYSE_CGNX_FULL, "fail",
     texts=ROW_TEXTS, msg="cannot read the row file at the PR head")
case("ANALYSE row: the explicit fixtures pass", AN_CGNX, CGNX_TITLE, ANALYSE_CGNX_FULL, "ok",
     texts={**ROW_TEXTS, ("head", CGNX_ROW): fixture_row(CGNX_ROW)})
SWEEP_ROW = "queue/rows/2026-10-03_0700_SWEEP.md"
case("SWEEP row without its portfolio table fails", SWEEP, "GSC SWEEP 2026-10-03 — 14 prices, 2 review requests",
     E("A " + SWEEP_ROW, "A queue/runs/2026-10-03_0700_SWEEP.md"), "fail",
     texts={**INTAKE_TEXTS, ("head", SWEEP_ROW): fixture_row(SWEEP_ROW).split("## Portfolio table")[0]},
     msg="## Portfolio table is missing")

# check() called directly with the documented signature
FIXTURES = lambda side, path: fixture_text(path) if side == "head" else None  # noqa: E731
try:
    direct = g.check("sweep", E("A queue/rows/2026-10-03_0700_SWEEP.md"),
                     {"key": None, "date": "2026-10-03", "time": "0700"}, lambda side, path: None,
                     text_lookup=FIXTURES)
    record("check(): direct call, SWEEP row", direct == [], repr(direct))
except Exception as exc:
    record("check(): direct call, SWEEP row", False, "raised %r" % exc)
try:
    direct = g.check("review", REVIEW_TROW_FULL, {"key": "TROW", "date": D, "time": T},
                     lambda side, path: REVIEW_TROW_BLOBS.get((side, path)), tree_lookup_for(REVIEW_TROW_TREES),
                     FIXTURES)
    record("check(): direct call, REVIEW move with tree_lookup", direct == [], repr(direct))
except Exception as exc:
    record("check(): direct call, REVIEW move with tree_lookup", False, "raised %r" % exc)
try:
    direct = g.check("sweep", E("A queue/rows/2026-10-03_0700_SWEEP.md"),
                     {"key": None, "date": "2026-10-03", "time": "0700"}, lambda side, path: None)
    record("check(): a row file without text_lookup fails closed",
           any("fail closed" in e for e in direct), repr(direct))
except Exception as exc:
    record("check(): a row file without text_lookup fails closed", False, "raised %r" % exc)


# ===================================================== make_tree_lookup()

def tree_git(listing, calls):
    """Fake git for ls-tree: listing[(rev, folder)] -> full paths, or None for a git error."""
    def git(args):
        calls.append(list(args))
        if args[:4] != ["ls-tree", "-z", "--name-only", "--full-tree"] or args[5] != "--":
            return 1, b""
        rev, folder = args[4], args[6].rstrip("/")
        paths = listing.get((rev, folder), [])
        if paths is None:
            return 128, b""
        return 0, b"".join(p.encode() + b"\0" for p in paths)
    return git


def tree_case(name, fn):
    try:
        ok, detail = fn()
    except Exception as exc:
        ok, detail = False, "raised %r" % exc
    record(name, ok, detail)


def _tree_basic():
    calls = []
    look = g.make_tree_lookup(tree_git({("mb", "memos/TROW"): ["memos/TROW/TROW_2026-09-08_GSC.md"],
                                        ("hd", "memos/TROW"): ["memos/TROW/TROW_2026-10-04_GSC.md"]}, calls),
                              "mb", "hd")
    got = (look("base", "memos/TROW"), look("head", "memos/TROW"), look("base", "memos/NONE"))
    want = (["TROW_2026-09-08_GSC.md"], ["TROW_2026-10-04_GSC.md"], [])
    return got == want and calls[0][-1] == "memos/TROW/", "got %r, calls %r" % (got, calls)


def _tree_sorted_and_main():
    calls = []
    listing = {("mb", "memos/K"): ["memos/K/K_2026-09-01_GSC.md", "memos/K/K_2026-01-01_GSC.md"],
               ("om", "memos/K"): ["memos/K/K_2026-10-01_GSC.md"]}
    default_main = g.make_tree_lookup(tree_git(listing, calls), "mb", "hd")
    explicit_main = g.make_tree_lookup(tree_git(listing, calls), "mb", "hd", "om")
    got = (default_main("main", "memos/K"), explicit_main("main", "memos/K"))
    want = (["K_2026-01-01_GSC.md", "K_2026-09-01_GSC.md"], ["K_2026-10-01_GSC.md"])
    return got == want, "got %r" % (got,)


def _tree_error_and_cache():
    calls = []
    look = g.make_tree_lookup(tree_git({("mb", "memos/K"): None}, calls), "mb", "hd")
    first, second = look("base", "memos/K"), look("base", "memos/K/")
    unknown = look("other", "memos/K")
    return (first is None and second is None and unknown is None and len(calls) == 1,
            "got %r %r %r, %d git call(s)" % (first, second, unknown, len(calls)))


tree_case("make_tree_lookup: basenames per side; absent folder is []", _tree_basic)
tree_case("make_tree_lookup: sorted; 'main' defaults to the base rev", _tree_sorted_and_main)
tree_case("make_tree_lookup: git error is None (fail closed), cached", _tree_error_and_cache)


# ================================================================ parser

def parser_case(name, data, expected):
    try:
        got = g.parse_name_status_z(data)
    except Exception as exc:
        got = exc
    if expected is ValueError:
        ok = isinstance(got, ValueError)
    else:
        ok = got == expected
    record(name, ok, "got %r" % (got,))


parser_case("parse: 'A\\0path\\0'", b"A\0queue/runs/x.md\0", [("A", "queue/runs/x.md")])
parser_case("parse: several entries", b"M\0_REGISTER.md\0D\0queue/rows/a.md\0A\0queue/runs/b.md\0",
            [("M", "_REGISTER.md"), ("D", "queue/rows/a.md"), ("A", "queue/runs/b.md")])
parser_case("parse: empty diff", b"", [])
parser_case("parse: no trailing NUL", b"A\0queue/runs/x.md", [("A", "queue/runs/x.md")])
parser_case("parse: path with space and tab", b"A\0queue/runs/a b\tc.md\0", [("A", "queue/runs/a b\tc.md")])
parser_case("parse: rename carries two paths", b"R100\0a.md\0b.md\0A\0c.md\0",
            [("R100", "a.md -> b.md"), ("A", "c.md")])
parser_case("parse: truncated stream raises", b"A\0", ValueError)
parser_case("parse: truncated rename raises", b"R100\0a.md\0", ValueError)
parser_case("parse: non-UTF-8 byte is replaced, not crashed", b"A\0queue/runs/\xff.md\0",
            [("A", "queue/runs/�.md")])


# ======================================================== main() end to end

MB = "ba5e000000000000000000000000000000000000"
HEAD = "feedface00000000000000000000000000000000"


def diff_bytes(entries):
    return b"".join(s.encode() + b"\0" + p.encode() + b"\0" for s, p in entries)


def fake_git(diff, blobs, head_sha=HEAD, trees=None, texts=None):
    """trees: {(side, folder): [basenames]} served to `git ls-tree` (side 'base'
    = the merge base, 'head' = the PR head, 'main' = origin/main, which falls
    back to 'base'); a value of None makes ls-tree fail. texts: {(side, path):
    text} served to `git cat-file blob` (default: the consistent register pair)."""
    trees = trees or {}
    fixtures = texts is None
    texts = INTAKE_TEXTS if texts is None else texts
    sides = {MB: "base", g.HEAD_REV: "head", "refs/remotes/origin/main": "main"}

    def git(args):
        args = list(args)
        if args[0] == "merge-base":
            return 0, (MB + "\n").encode()
        if args[0] == "ls-tree":
            side, folder = sides.get(args[4]), args[-1].rstrip("/")
            if side == "main" and ("main", folder) not in trees:
                side = "base"
            names = trees.get((side, folder), [])
            if side is None or names is None:
                return 128, b""
            return 0, b"".join(("%s/%s" % (folder, n)).encode() + b"\0" for n in names)
        if args[0] == "cat-file":
            rev, _, path = args[-1].partition(":")
            text = texts.get(("base" if rev == MB else "head", path))
            if text is None and fixtures and rev != MB:
                text = fixture_text(path)
            return (0, text.encode("utf-8")) if text is not None else (128, b"")
        if "diff" in args:
            return 0, diff
        if args[0] == "rev-parse":
            spec = args[-1]
            if ":" not in spec:
                return 0, (head_sha + "\n").encode()
            rev, _, path = spec.partition(":")
            blob = blobs.get(("base" if rev == MB else "head", path))
            return (0, (blob + "\n").encode()) if blob else (1, b"")
        return 1, b""
    return git


def no_git(args):
    raise AssertionError("git must not run for a non-routine PR")


def env_for(ref, title, base="main"):
    return {"HEAD_REF": ref, "HEAD_SHA": HEAD, "BASE_REF": base, "DEFAULT_BRANCH": "main", "PR_TITLE": title}


def main_case(name, env, git, expect_code, must=(), must_not_prefix=None, must_not=()):
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            code = g.main(env=env, git=git)
    except Exception as exc:
        record(name, False, "raised %r" % exc)
        return
    out = buf.getvalue()
    ok = code == expect_code and all(m in out for m in must) and not any(m in out for m in must_not)
    if ok and must_not_prefix:
        ok = not any(line.startswith(must_not_prefix) for line in out.splitlines())
    record(name, ok, "code %r, output %r" % (code, out))


main_case("main: attended PR skipped without running git",
          env_for("claude/model-v4.4.0-routines", "MODEL v4.4.0 — routines migration"), no_git, 0,
          must=("not a routine PR",))
main_case("main: INTAKE full run is OK",
          env_for(INTAKE, "GSC INTAKE 2026-10-04 — register v305"),
          fake_git(diff_bytes(INTAKE_FULL), INTAKE_BLOBS), 0, must=("OK —",))
main_case("main: INTAKE snapshot mismatch fails",
          env_for(INTAKE, "GSC INTAKE 2026-10-04 — register v305"),
          fake_git(diff_bytes(INTAKE_FULL), {**INTAKE_BLOBS, ("head", INTAKE_SNAPSHOT): "other"}), 1,
          must=("::error::", "not a byte copy"))
main_case("main: INTAKE with a hand-edited register fails (cat-file)",
          env_for(INTAKE, "GSC INTAKE 2026-10-04 — register v305"),
          fake_git(diff_bytes(INTAKE_FULL), INTAKE_BLOBS,
                   texts=texts_with(md=INTAKE_MD.replace("| TROW Inc. |", "| T. Rowe |"))), 1,
          must=("::error::", "not the rendering"))
main_case("main: INTAKE register unreadable at the head fails closed",
          env_for(INTAKE, "GSC INTAKE 2026-10-04 — register v305"),
          fake_git(diff_bytes(INTAKE_FULL), INTAKE_BLOBS, texts={}), 1,
          must=("::error::", "unverifiable"))
main_case("main: ANALYSE full run is OK",
          env_for(AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY"),
          fake_git(diff_bytes(ANALYSE_CGNX_FULL), {}), 0, must=("OK —",))
main_case("main: ANALYSE row pasted without its table header fails (the PR 87 case)",
          env_for(AN_CGNX, CGNX_TITLE),
          fake_git(diff_bytes(ANALYSE_CGNX_FULL), {},
                   texts={**ROW_TEXTS, ("head", CGNX_ROW): fixture_row(CGNX_ROW, table=False)}), 1,
          must=("::error::", "header and separator lines are missing"))
main_case("main: newline in a file name cannot inject a workflow command",
          env_for(AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY"),
          fake_git(b"A\0queue/runs/x\n::warning::pwned.md\0", {}), 1,
          must=("::error::", "control character"), must_not_prefix="::warning::")
main_case("main: '##[' in the PR title cannot inject a workflow command",
          env_for(AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY ##[warning]x"),
          fake_git(diff_bytes(ANALYSE_CGNX_FULL), {}), 0, must=("OK —",), must_not=("##[",))
main_case("main: '##[' in a file name cannot inject a workflow command",
          env_for(AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY"),
          fake_git(b"A\0queue/runs/##[stop-commands]tok.md\0", {}), 1,
          must=("::error::", "not in the ANALYSE write contract"), must_not=("##[",))
main_case("main: rename line from git fails",
          env_for(INTAKE, "GSC INTAKE 2026-10-04 — register v305"),
          fake_git(b"R100\0queue/proposals/a.md\0archive/queue/proposals/a.md\0", {}), 1,
          must=("status R100 is not allowed",))
main_case("main: deleting an archive/ file fails (append-only)",
          env_for(INTAKE, "GSC INTAKE 2026-10-04 — register v305"),
          fake_git(diff_bytes(INTAKE_FULL + E("D archive/registers/2026/REGISTER_v303_2026-10-03.md")),
                   INTAKE_BLOBS), 1,
          must=("::error::", "append-only"))
main_case("main: INTAKE snapshot at the retired registers/ path fails",
          env_for(INTAKE, "GSC INTAKE 2026-10-04 — register v305"),
          fake_git(diff_bytes(E("M _REGISTER.md", "A registers/2026/REGISTER_v304_2026-10-03.md",
                                "A queue/runs/2026-10-04_0650_INTAKE.md")),
                   {**INTAKE_BLOBS, ("head", "registers/2026/REGISTER_v304_2026-10-03.md"): "blob-register-v304"}),
          1, must=("::error::", "retired path"))
main_case("main: REVIEW with the prior moved to archive/memos is OK (ls-tree, rev-parse)",
          env_for(RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; Past ROCE re-test"),
          fake_git(diff_bytes(REVIEW_TROW_FULL), REVIEW_TROW_BLOBS, trees=REVIEW_TROW_TREES), 0, must=("OK —",))
main_case("main: REVIEW without the prior move fails",
          env_for(RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6"),
          fake_git(diff_bytes(without(REVIEW_TROW_FULL, "D memos/TROW/" + TROW_PRIOR,
                                      "A archive/memos/TROW/" + TROW_PRIOR)),
                   REVIEW_TROW_BLOBS, trees={("base", "memos/TROW"): [TROW_PRIOR],
                                             ("head", "memos/TROW"): [TROW_PRIOR, TROW_NEW]}), 1,
          must=("::error::", "must move exactly its one prior"))
main_case("main: REVIEW stale against origin/main fails",
          env_for(RV_TROW, "GSC REVIEW TROW 2026-10-04 — AVOID; v6"),
          fake_git(diff_bytes(REVIEW_TROW_FULL), REVIEW_TROW_BLOBS,
                   trees={**REVIEW_TROW_TREES, ("main", "memos/TROW"): ["TROW_2026-10-03_GSC.md"]}), 1,
          must=("::error::", "REVIEW is stale"))
main_case("main: ANALYSE for a key with archived memos fails",
          env_for(AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY"),
          fake_git(diff_bytes(ANALYSE_CGNX_FULL), {}, trees={("base", "archive/memos/CGNX"): ["CGNX_2026-05-01_GSC.md"]}),
          1, must=("::error::", "REVIEW territory"))
main_case("main: ls-tree failure fails closed",
          env_for(AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY"),
          fake_git(diff_bytes(ANALYSE_CGNX_FULL), {}, trees={("base", "memos/CGNX"): None}), 1,
          must=("::error::", "unverifiable"))
main_case("main: PR head moved fails",
          env_for(AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY"),
          fake_git(diff_bytes(ANALYSE_CGNX_FULL), {}, head_sha="0" * 40), 1, must=("PR head moved",))
main_case("main: base not main fails",
          env_for(AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY", base="claude/gsc-analyse-CGNX-x"),
          fake_git(diff_bytes(ANALYSE_CGNX_FULL), {}), 1, must=("targets",))


# ================================================================ summary

failures = RESULTS.count(False)
print("%d case(s), %d failed" % (len(RESULTS), failures))
sys.exit(min(failures, 255))
