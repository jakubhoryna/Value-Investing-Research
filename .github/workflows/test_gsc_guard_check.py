#!/usr/bin/env python3
"""Plain-python tests for gsc_guard_check.py (no pytest, no git needed).

Run:  python3 .github/workflows/test_gsc_guard_check.py
Prints one PASS/FAIL line per case. Exit code = number of failed cases
(0 = all pass).

Covers: every correct run per job (expect OK), every known violation
(expect failure), keys with dots and hyphens, the -z name-status parser,
and main() end to end with a fake git.
"""
import contextlib
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gsc_guard_check as g  # noqa: E402

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


def case(name, branch, title, entries, expect, base="main", blobs=None, msg=None):
    """expect: 'ok', 'fail' or 'skip'. msg: a substring one error must contain."""
    table = blobs or {}

    def lookup(side, path):
        return table.get((side, path))

    try:
        errors = g.evaluate(branch, title, base, "main", entries, lookup)
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

INTAKE_SNAPSHOT = "registers/2026/REGISTER_v304_2026-10-03.md"
INTAKE_TODO_ARCHIVE = "queue/archive/TODO_v36_2026-10-02.md"
INTAKE_DQ_ARCHIVE = "queue/archive/DRAFT_QUEUE_v12_2026-10-01.md"
PROPOSAL = "2026-10-03_0800_QUEUE-SEED.md"
INTAKE_FULL = E(
    "M _REGISTER.md",
    "M queue/TODO.md",
    "M queue/DRAFT_QUEUE.md",
    "A " + INTAKE_SNAPSHOT,
    "A " + INTAKE_TODO_ARCHIVE,
    "A " + INTAKE_DQ_ARCHIVE,
    "A queue/archive/proposals/" + PROPOSAL,
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
    ("base", "queue/TODO.md"): "blob-todo-v36",
    ("head", INTAKE_TODO_ARCHIVE): "blob-todo-v36",
    ("base", "queue/DRAFT_QUEUE.md"): "blob-dq-v12",
    ("head", INTAKE_DQ_ARCHIVE): "blob-dq-v12",
    ("base", "queue/proposals/" + PROPOSAL): "blob-proposal",
    ("head", "queue/archive/proposals/" + PROPOSAL): "blob-proposal",
}


def without(entries, *drop):
    return [e for e in entries if " ".join(e) not in drop]


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
case("REVIEW memo + row + run note + evidence deletion", RV_TROW, "GSC REVIEW TROW 2026-10-04 — HOLD", E(
    "A memos/TROW/TROW_2026-10-04_GSC.md",
    "A queue/rows/2026-10-04_2250_REVIEW_TROW.md",
    "A queue/runs/2026-10-04_2250_REVIEW_TROW.md",
    "D queue/evidence/TROW_2026-09-08_v4-REVIEW-draft.md",
), "ok")
case("REVIEW of a held name (HELD · title), dotted key HFG.DE", RV_HFG,
     "HELD · GSC REVIEW HFG.DE 2026-10-04 — SELL-FLAG", E(
         "A memos/HFG.DE/HFG.DE_2026-10-04_GSC.md",
         "A queue/rows/2026-10-04_2250_REVIEW_HFG.DE.md",
         "A queue/runs/2026-10-04_2250_REVIEW_HFG.DE.md",
     ), "ok")
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
case("INTAKE year-end snapshot in the outgoing date's year folder",
     "claude/gsc-intake-2026-01-02-0650", "GSC INTAKE 2026-01-02 — register v290", E(
         "M _REGISTER.md",
         "A registers/2025/REGISTER_v289_2025-12-31.md",
         "A queue/runs/2026-01-02_0650_INTAKE.md",
     ), "ok", blobs={("base", "_REGISTER.md"): "r289", ("head", "registers/2025/REGISTER_v289_2025-12-31.md"): "r289"})
case("INTAKE DRAFT_QUEUE archive with a dotted version (v1.1)", INTAKE, "GSC INTAKE 2026-10-04 — DRAFT_QUEUE v2", E(
    "M queue/DRAFT_QUEUE.md",
    "A queue/archive/DRAFT_QUEUE_v1.1_2026-10-03.md",
    "D queue/rows/2026-10-03_2250_ANALYSE.md",
    "A queue/runs/2026-10-04_0650_INTAKE.md",
), "ok", blobs={("base", "queue/DRAFT_QUEUE.md"): "blob-dq-v1.1",
                ("head", "queue/archive/DRAFT_QUEUE_v1.1_2026-10-03.md"): "blob-dq-v1.1"})

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
     ANALYSE_CGNX_FULL + E("A memos/SYM/SYM_2026-10-04_GSC.md"), "fail", msg="memo paths in one")
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
case("ANALYSE keyless branch writes a keyed row", AN_KEYLESS, "GSC ANALYSE 2026-10-04 — queue exhausted",
     E("A queue/rows/2026-10-04_2250_ANALYSE_CGNX.md"), "fail", msg="not in the ANALYSE write contract")
case("ANALYSE modifies the register", AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY",
     ANALYSE_CGNX_FULL + E("M _REGISTER.md"), "fail", msg="not in the ANALYSE write contract")
case("REVIEW memo for another key", RV_TROW, "GSC REVIEW TROW 2026-10-04 — HOLD",
     E("A memos/NKE/NKE_2026-10-04_GSC.md"), "fail", msg="REVIEW memo must be for the branch key")
case("REVIEW overwrites a prior memo", RV_TROW, "GSC REVIEW TROW 2026-10-04 — HOLD",
     E("M memos/TROW/TROW_2026-09-08_GSC.md"), "fail", msg="may only add a new memo")
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
     [("R100", "queue/proposals/%s -> queue/archive/proposals/%s" % (PROPOSAL, PROPOSAL))], "fail",
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
     blobs={**INTAKE_BLOBS, ("head", "queue/archive/proposals/" + PROPOSAL): "blob-edited"}, msg="not a byte copy")
case("INTAKE archives a proposal without deleting it", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     without(INTAKE_FULL, "D queue/proposals/" + PROPOSAL), "fail", blobs=INTAKE_BLOBS,
     msg="is not deleted in this PR")
case("INTAKE snapshot in the wrong year folder", INTAKE, "GSC INTAKE 2026-10-04 — register v305",
     E("A registers/2025/REGISTER_v304_2026-10-03.md"), "fail", blobs=INTAKE_BLOBS, msg="snapshot folder")
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

# check() called directly with the documented signature
try:
    direct = g.check("sweep", E("A queue/rows/2026-10-03_0700_SWEEP.md"),
                     {"key": None, "date": "2026-10-03", "time": "0700"}, lambda side, path: None)
    record("check(): direct call, SWEEP row", direct == [], repr(direct))
except Exception as exc:
    record("check(): direct call, SWEEP row", False, "raised %r" % exc)


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


def fake_git(diff, blobs, head_sha=HEAD):
    def git(args):
        args = list(args)
        if args[0] == "merge-base":
            return 0, (MB + "\n").encode()
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
main_case("main: ANALYSE full run is OK",
          env_for(AN_CGNX, "GSC ANALYSE CGNX 2026-10-04 — BUY"),
          fake_git(diff_bytes(ANALYSE_CGNX_FULL), {}), 0, must=("OK —",))
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
          fake_git(b"R100\0queue/proposals/a.md\0queue/archive/proposals/a.md\0", {}), 1,
          must=("status R100 is not allowed",))
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
