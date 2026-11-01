# Run note — ANALYSE ABBOTINDIA.NS — 2026-11-01 2332

- Job: ANALYSE · Key: ABBOTINDIA.NS · D: 2026-11-01 · T: 2332
- Base sha: 7f1253bbad673cafdf80a2efb839cac2d62b1746
- model_version: v4.8.0 (guard live; canary refused)
- Status: finished — INCOMPLETE (data access: price endpoint HTTP 429)

**Pick.** `▶ Group dependencies`: ABBN.SW and ATCO-B.ST carry pending `memo exists` lines (TCS.NS row); the other lines are `parent re-run owed`. DRAFT_QUEUE: TCS.NS through ELGIEQUIP.NS and CRISIL.NS have pending rows; SUNDRMFAST.NS is claimed by open PR #360 (`[running]`, left to INTAKE's abandoned-claim rule). ABBOTINDIA.NS is the first qualifying `[ ]` line, with no name or ISIN (INE358A01014) match in memos, archive or register.

**Written.** `queue/evidence/ABBOTINDIA.NS_2026-11-01_INCOMPLETE.md` (every gate input with its primary source, readings settled, scope owed); row file `queue/rows/2026-11-01_2332_ANALYSE_ABBOTINDIA.NS.md`; this note. No memo.

**Why INCOMPLETE.** The price endpoint (query1, and query2 once) answered HTTP 429 on 27 tries over about 35 minutes, the last 20 at one-minute intervals. Without px and the endpoint's currency the cheapness leg and the machine fields cannot be written. The full analysis was otherwise done; the record carries it.

**Retrieval.** BSE served every annual report used (AR17, AR18, AR20, AR22, AR24, AR25, AR26). AR17 and AR18 text layers are font-garbled; their statements were read from page images. Nothing circumvented.

**P14.** 1 exploratory operation (screener.in, to locate the BSE annual-report links). Primary documents and the quote endpoint are uncounted.

**Needs Jakub.**
- Nothing to decide. A later ANALYSE needs only the quote; if 429s persist across runs, the routine client may be rate-limited on the endpoint.
- Two IDEAS candidates in the row file (reciprocal group service charges before P27; parent-held brand rights at no price).
