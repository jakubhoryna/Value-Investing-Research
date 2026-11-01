# Run note — ANALYSE CRISIL.NS — 2026-11-01 2132

- Job: ANALYSE · Key: CRISIL.NS · D: 2026-11-01 · T: 2132
- Base sha: 131f28ea32208e317ac9a90739a94959ad3144fc
- model_version: v4.8.0 (guard live; canary refused)
- Status: finished — INCOMPLETE (group build exceeds budget), first overrun

**Pick.** `▶ Group dependencies`: ABBN.SW and ATCO-B.ST already carry pending `memo exists` lines in the TCS.NS row; the other lines are `parent re-run owed`. DRAFT_QUEUE: TCS.NS through ELGIEQUIP.NS have pending rows; SUNDRMFAST.NS is claimed by open PR #360 (`[running]`, left to INTAKE's abandoned-claim rule). CRISIL.NS is the first qualifying `[ ]` line. No name or ISIN (INE007A01025) match in memos, archive or register.

**Written.** `queue/evidence/CRISIL.NS_2026-11-01_INCOMPLETE.md` (resumable record: sources, item table with page locations FY2015–FY2025, readings settled, scope owed); row file `queue/rows/2026-11-01_2132_ANALYSE_CRISIL.NS.md`; this note. No memo.

**Why INCOMPLETE.** CRISIL is a group of two material units (Ratings services 29.5% of FY2025 revenue; Research, Analytics and Solutions 70.5%). The run also found a G6 class above the P31 line (CARE Ratings and unquoted equity stakes, 10.7% of total assets at FY2025) and a pre-Ind AS 116 lease test owed for FY2016–FY2019. B1–B4 on both G6 readings, the two Appendix D blocks, the allocation table and Appendix E could not be finished inside the time budget, so research stopped early enough to write the record.

**Retrieval.** BSE serves every annual report used (AR17, AR19, AR21, AR23, AR24, AR25); no blocks. The quote endpoint answered (NSI, INR, close 4,516.60 on 2026-10-30).

**P14.** 1 exploratory operation (screener.in page to locate the BSE annual-report links). Primary documents and the quote endpoint are uncounted.

**Needs Jakub.** Nothing; the next ANALYSE resumes from the record. One IDEAS candidate in the row file (common-control customer aggregation).
