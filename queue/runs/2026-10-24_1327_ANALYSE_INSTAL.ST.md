# Run note — ANALYSE INSTAL.ST — 2026-10-24 1327

- job: ANALYSE · key: INSTAL.ST (Instalco AB (publ), ISIN SE0017483506)
- D: 2026-10-24 · T: 1327 (Europe/Prague)
- base sha: 8c471de884be690d16bd29187ca34853aba2783a · model_version: v4.6.1
- status: complete

**Preflight.** Guard live (canary refused, hook files tracked, routine environment confirmed); ledger loaded; one repository; repo private.

**Pick.** The two `▶ Group dependencies` lines (ABB, ATCO-B.ST) already carry a pending `memo exists` record (row file 2026-10-24_0641_ANALYSE_ETON); BLD and EEX are claimed by open PRs; ETON through SDIP-B.ST have pending rows. INSTAL.ST was the first eligible queue line. No prior memo or register row on name or ISIN.

**Written.** Memo `memos/INSTAL.ST/INSTAL.ST_2026-10-24_GSC.md` (v1, AVOID: Past + Future + SF); row file `queue/rows/2026-10-24_1327_ANALYSE_INSTAL.ST.md`; this note. No evidence files existed for the key.

**Sources.** Ten annual reports (2016–2025), three interim reports (Q4 2024, Q1 2025, Q3 2026) and one presentation from instalco.se; one price-endpoint call; 0 of ~5 exploratory searches.

**Gaps (memo Appendix A).** TTM capex and financial income not split in the Q3 2026 interim (TTM FCF = CFO less net other investing); FY2015 share count not comparable (per-share series from FY2016); other executives' pay printed only in aggregate (INDETERMINATE (a), part of the SF flag pair); profit share bought with minority buy-outs not printed; allocation test INDETERMINATE (b).

**Needs Jakub.** One IDEAS candidate in the row file: whether minority buy-outs in subsidiaries are deals under the acquisition stop (it decides one of the two SF flags here; Past and Future fail on their own). The PR is in an auto-merge class (ANALYSE AVOID).
