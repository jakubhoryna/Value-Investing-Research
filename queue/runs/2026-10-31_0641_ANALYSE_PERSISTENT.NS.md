# Run note — ANALYSE PERSISTENT.NS — 2026-10-31 0641

- Job: ANALYSE · Key: PERSISTENT.NS · D: 2026-10-31 · T: 0641
- Base sha: e6a1d5bc6bfaf8851be98404700844a6bac80b01
- model_version: v4.8.0 (guard live; canary refused)
- Status: finished — AVOID (Future + SF)

**Pick.** `▶ Group dependencies`: the ABBN.SW and ATCO-B.ST lines already carry `memo exists` in a pending row (TCS.NS), and the INVE-B.ST and DKSH.SW lines are `parent re-run owed`. In DRAFT_QUEUE, TCS.NS has a pending row. PERSISTENT.NS is the first qualifying `[ ]` line, with no name or ISIN (INE262H01021) match in memos, archive or register.

**Written.** Memo v1 `memos/PERSISTENT.NS/` (lint-memo OK; body 781 words); row file `queue/rows/2026-10-31_0641_ANALYSE_PERSISTENT.NS.md` (lint-row OK); this note.

**Result.** Past STRONG (18.8% ROCE; FCFROCE 12.4%, maint. = all capex), Future WEAK (three units, none with an evidenced moat; Hi-Tech `customer conc.`, a named FY2025 customer of 26% of the unit; S = 1.00), SF FAIL (CEO pay INR 3,885.77m FY2026 = 26.1% of FCF, trailing 36.0%: proportionality strike), EXPENSIVE (TTM MCap/FCF 74.1, EV/OI 45.5). Trigger INR 653.3 against px 6,048.00.

**Failures.** persistent.com/investors/annual-report-2020/ redirects to a bot check (302, rdwr/perfdrive); FY2016–FY2019 came from the audited statement PDFs instead. P20 tier 2 was not built (home-CPI series not retrieved), so all capex is used, which reads harsh.

**P14.** 3 exploratory searches, plus 4 URL probes; 12 primary documents and the quote are uncounted.

**Needs Jakub.** Nagarro SE takeover pending closing: acquisition stop owed at closing (TODO addition).
