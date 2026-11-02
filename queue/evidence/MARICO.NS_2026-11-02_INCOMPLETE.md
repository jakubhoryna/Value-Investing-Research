# MARICO.NS — Marico Limited — INCOMPLETE evidence (ANALYSE 2026-11-02)

Resume record (README §5). No grade, no verdict. This run resumed the partial record of 2026-10-31 and stopped on a data-access gap before any figure could be re-opened.

## 1. Header

- Key MARICO.NS · job ANALYSE · D 2026-11-02 · T 2353 · base sha ec9d2d4893fb8560bfc5e4e3ebf1dd3d7bceec50 · live model_version v4.8.0 · produced_by ROUTINE
- Prior memo: none (no `memos/MARICO.NS/` or `archive/memos/MARICO.NS/`; no register row named Marico). Prior memo `model_version`: none.
- **Named gap: data access: marico.com HTTP 406, price endpoint HTTP 429.** This is not a budget gap: the group build was not reached.
- Resumes: queue/evidence/MARICO.NS_2026-10-31_INCOMPLETE.md (partial 2026-10-31, group build exceeds budget). That record stays, with its item table, readings settled and scope still owed; nothing in it was re-opened or changed by this run.

## 2. Hosts tried (2026-11-02, about 22:55–23:05 UTC)

| host / document | request | result |
|---|---|---|
| marico.com/investorspdf/ — AR FY2017, FY2019, FY2020, FY2021, FY2022, FY2023, FY2024, FY2025, FY2026; MBL AR 2025-26 (the files the 2026-10-31 record cites) | plain curl GET | HTTP 406 "Request was blocked due to suspicious behavior" on every file. The 2026-10-31 run fetched the same files without a block. Not bypassed. |
| marico.com/investorspdf/Marico_Annual_Report_FY26.pdf | WebFetch | reached, but the PDF is over the tool's 10 MB limit; no text returned |
| bseindia.com/bseplus/AnnualReport/531642/5316420318.pdf (AR FY2017-18) | plain curl GET | HTTP 200, 8.4 MB (saved to /tmp only; not read: FY2017–FY2018 alone cannot complete the record) |
| api.bseindia.com AnnualReport_New (index of BSE annual-report attachments for FY2021+) | plain curl GET | HTTP 403 Access Denied (Akamai) |
| nsearchives.nseindia.com (FY2026 Ind AS integrated-filing iXBRL, results of 5 May 2026) | plain curl GET, HTTP/2 and HTTP/1.1 | stream reset / empty reply |
| www.nseindia.com/api/annual-reports | plain curl GET | timed out with no bytes |
| query1.finance.yahoo.com/v8/finance/chart/MARICO.NS | plain curl GET | HTTP 429 Too Many Requests; px, px_date and the endpoint currency not recorded |

No header was altered to get past a block.

## 3. Item table

No figure was re-opened at a primary source this run, so none is added. The 2026-10-31 record's item table stands as written there, every row with its document and place.

| item | FY | value | unit | source |
|---|---|---|---|---|
| — | — | — | — | no new figure (all primaries blocked; see §2) |

## 4. Readings settled

Unchanged from the 2026-10-31 record (group: India and International segments plus Marico Bangladesh Limited, 90%, a material controlled listed subsidiary on a venue the price endpoint does not serve, so ungradeable; lens STD; draft Gate-0 sentence; acquisition stop live). None was re-read on the live rules this run.

## 5. Scope still owed

- [ ] Retrieve the annual reports FY2017–FY2026 and MBL's FY2026 report: marico.com/investorspdf/ (blocked 2026-11-02, worked 2026-10-31), or the BSE/NSE copies if their indexes become reachable.
- [ ] One GET to the price endpoint for MARICO.NS (currency, exchangeName, close and date).
- [ ] Then the whole checklist of the 2026-10-31 record, §5, in its order: re-open the governing figures; B1 FY2016–FY2026; note 13(b); P20, G6/P31 and lease tests; B4 and the Appendix D blocks; Appendix E (pay, holdings, WEOMA trust, acquisition worksheet, allocation table); Appendix F.

*Framework output, not investment advice.*
