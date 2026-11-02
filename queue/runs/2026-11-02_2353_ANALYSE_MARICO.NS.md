# Run note — ANALYSE MARICO.NS — 2026-11-02 2353

- Job: ANALYSE · Key: MARICO.NS · D: 2026-11-02 · T: 2353
- Base sha: ec9d2d4893fb8560bfc5e4e3ebf1dd3d7bceec50
- model_version: v4.8.0 (guard live; canary refused; repo private)
- Status: finished — INCOMPLETE (data access: marico.com HTTP 406, price endpoint HTTP 429)

**Pick.** `▶ Group dependencies`: ABBN.SW and ATCO-B.ST are pending in the TCS.NS row (check d); the INVE-B.ST and DKSH.SW lines are `parent re-run owed`. DRAFT_QUEUE partial lines first: TCS.NS has a pending row; MARICO.NS (partial 2026-10-31) qualifies: no memo or archive folder, no register name match, not claimed, no pending row, not held, no attended item.

**Written.** `queue/evidence/MARICO.NS_2026-11-02_INCOMPLETE.md` (hosts tried, scope owed; resumes the 2026-10-31 record, which stays); row file `queue/rows/2026-11-02_2353_ANALYSE_MARICO.NS.md`; this note. No memo.

**Failed.** marico.com/investorspdf/: HTTP 406 on every annual report (bot block; the 2026-10-31 run fetched them). WebFetch reached the FY2026 PDF but it exceeds 10 MB. api.bseindia.com annual-report index: HTTP 403. nsearchives.nseindia.com and nseindia.com/api: reset or timeout. query1.finance.yahoo.com: HTTP 429. Only the BSE FY2017-18 report came through, and that alone cannot complete the record. No header was altered to get past a block.

**P14.** 1 exploratory search (NSE archive copy of the annual report; none found). Primary retrievals uncounted.

**Needs Jakub.**
- If marico.com keeps blocking cloud IPs, MARICO.NS needs another document route or an attended run.
