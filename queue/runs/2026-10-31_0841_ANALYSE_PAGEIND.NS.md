# Run note — ANALYSE PAGEIND.NS — 2026-10-31 0841

- Job: ANALYSE · Key: PAGEIND.NS · D: 2026-10-31 · T: 0841
- Base sha: f54620ade3edd581e67f3023e77c68af7c47df5d
- model_version: v4.8.0 (guard live; canary refused)
- Status: finished — AVOID (Future)

**Pick.** `▶ Group dependencies`: ABBN.SW and ATCO-B.ST carry `memo exists` in a pending row (TCS.NS); the INVE-B.ST and DKSH.SW lines are `parent re-run owed`. In DRAFT_QUEUE, TCS.NS, PERSISTENT.NS, TITAN.NS and MARICO.NS have pending rows (the TCS.NS and MARICO.NS partials are dated today, so not taken). PAGEIND.NS is the first qualifying `[ ]` line, with no name or ISIN (INE761H01022) match in memos, archive or register.

**Written.** Memo v1 `memos/PAGEIND.NS/` (lint-memo OK; body 734 words); row file `queue/rows/2026-10-31_0841_ANALYSE_PAGEIND.NS.md` (lint-row OK); this note.

**Result.** Past STRONG (40.7% ROCE; FCFROCE 25.3%, maint. = all capex), Future WEAK (customer conc.: FY2026 top-ten dealers ≈ 21% of revenue with no statement ruling out one above 10%; supplier conc.: the Jockey licence, to 2040, underpins nearly all revenue, no printed price terms or market share, and the licensor owns the brand), SF PASS (hairiest pay INR 102.45m, 1.6% of FCF; ALIGNED), EXPENSIVE (MCap/FCF 59.8, EV/OI 38.6). Trigger INR 4,566.8 against px 34,150.

**Retrieval.** BSE's AnnualReport archive serves FY2016–FY2020 by the `{scrip}03{YY}.pdf` pattern (FY2021 on: 404); pageind.com's investor page lists every annual report from 2020-21 as CDN PDFs. Quote from the endpoint (2026-10-30 bar had no close; 2026-10-29 close used).

**Failures.** None blocking. P20 tier 2 not built (home-CPI series not retrieved): all capex used, which reads harsh.

**P14.** 0 exploratory searches; 11 BSE URL probes, 2 IR index pages and 10 primary documents, uncounted.

**Needs Jakub.** Nothing.
