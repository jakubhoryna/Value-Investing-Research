# Run note — ANALYSE BAJAJ-AUTO.NS — 2026-11-03 2332

- Job: ANALYSE · Key: BAJAJ-AUTO.NS (Bajaj Auto Limited, ISIN INE917I01010)
- D / T: 2026-11-03 / 2332 (Europe/Prague) · Base sha: 5152758b24e0006f02d019bcd78713f2939ebe5d
- model_version read: v4.8.0 · PR #373
- Status: finished — INCOMPLETE (group build exceeds budget), first overrun

**Pick.** Group dependency lines `ABBN.SW` and `ATCO-B.ST` were skipped: the pending CRISIL.NS row already records them (check d). `SUNDRMFAST.NS` was skipped as claimed (open PR #360 `[running]`, older than 6 hours; INTAKE's abandoned-claim rule applies). `CRISIL.NS` was skipped because a row is pending (check d). `BAJAJ-AUTO.NS` passed checks a–f.

**Written.** `queue/evidence/BAJAJ-AUTO.NS_2026-11-03_INCOMPLETE.md`, a resumable record: all eleven annual reports FY2016–FY2026 retrieved, with the cited ten-year consolidated record, the FY2026 segment and business-combination notes, investments, shares, buybacks, pay, holdings and the readings settled. Also `queue/rows/2026-11-03_2332_ANALYSE_BAJAJ-AUTO.NS.md` (row_type INCOMPLETE; queue line stays `[ ]` with a partial note) and this note. No memo.

**Why INCOMPLETE.** This is a group with three material parts: Automotive ex-KTM, Financing (Bajaj Auto Credit, captive per R2) and the controlled listed subsidiary Bajaj Mobility AG (KTM; 74.94% from 18 Nov 2025; no memo, so ungradeable). G6 sits above the P31 line (the PBAG associate is 7–14% of total assets), so both readings are needed over ten years. Add the R6 book rule, two buyback worth tables and the KTM acquisition stop, and the build does not fit one run.

**Failed hosts.** api.bseindia.com annual-report index (HTTP 403); bajajauto.com `/investors/annual-reports` (HTTP 404, JS-rendered site). investors.bajajauto.com and the bseindia.com `bseplus/AnnualReport` paths served the PDFs.

**P14.** 2 exploratory searches. Price endpoint, IR indexes and PDFs uncounted.

**Needs Jakub.**
- Nothing blocking. A later ANALYSE resumes the partial record. `BMAG.SW` (Bajaj Mobility) has no memo, and its own Past decides the KTM acquisition-stop reading: a TODO addition proposes an ANALYSE of it.
