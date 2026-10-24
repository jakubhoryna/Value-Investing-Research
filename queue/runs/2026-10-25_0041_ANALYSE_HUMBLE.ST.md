# Run note — ANALYSE HUMBLE.ST — 2026-10-25 00:41

- Job: ANALYSE · Key: HUMBLE.ST (Humble Group AB (publ), ISIN SE0006261046)
- D: 2026-10-25 · T: 0041 (Europe/Prague)
- Base sha: 48c1e9e7a5cc80863fc54660f2b6ae729a1b7777 · model_version read: v4.6.1
- Status: finished — AVOID (Past + Future + SF), PR #266

**Pick.** `▶ Group dependencies`: ABB and ATCO-B.ST skipped (pending `Group dependency` lines in the BUFAB.ST row). Queue: BLD and EEX claimed by open PRs; BUFAB.ST to EMBRAC-B.ST pending rows or claims; BERNER-B.ST and BICO.ST open PRs. HUMBLE.ST was the first eligible line. Size check: MCap ≈ SEK 2,463m ≈ EUR 221m, above the queue's EUR 200m exclusion.

**Written.** Memo `memos/HUMBLE.ST/HUMBLE.ST_2026-10-25_GSC.md` (v1), row file `queue/rows/2026-10-25_0041_ANALYSE_HUMBLE.ST.md`, this note. No evidence files existed for the key.

**Failed / unretrieved.**
- Statistics Sweden API (api.scb.se) returned "Bad Request" for the CPI annual-average table; one search returned monthly rates only. P20 constructed tier not built: tier 3 (all capex) used in every year (harsher).
- Bayn Europe AB annual reports for FY2016–FY2017 not on the filer's mfn/Cision archive (one search). These are pre-group parent-only years, read as history-limited predecessor years outside the consolidated record (memo Appendix A gives the reasoning).
- Budget: 3 of ~5 exploratory searches; 1 WebFetch to scb.se (404).

**Needs Jakub.**
- Confirm the history-limited reading of FY2016–FY2018 (Bayn Europe AB standalone, before consolidated accounts began with FY2019 comparatives); the verdict does not depend on it.
