# INCOMPLETE evidence: FERG, Ferguson Enterprises Inc., 2026-10-24

- run: ANALYSE routine, D 2026-10-24, T 0026, base 0bdeff810ead8118b9b7672b30c697a0c2280c45, MODEL v4.6.1
- identity: Ferguson Enterprises Inc. (Delaware; NYSE `FERG`), SEC CIK 2011641. It is the successor of Ferguson plc (Jersey; CIK 1832433, renamed Ferguson (Jersey) Ltd), which itself succeeded Wolseley plc (CIK 1139313); the redomicile to the US closed on 1 Aug 2024 (Form 8-K12B). ISIN: n/a — not established this run. Prior check: no `company:` line in `memos/` or `archive/memos/` names Ferguson or Wolseley, and `register.csv` has no such row.
- **No verdict.** The data-completeness gate (README §5, D3) stopped the run before any gate was called.

## Why INCOMPLETE: named gap (record-limited FY2016–FY2019)

The fiscal year ended 31 July until FY2025; the company then moved to a 31 December year end (Form 10-KT for the five months 1 Aug–31 Dec 2025). The P1 window is FY2016–FY2025 (years ending 31 July), with 11 balance sheets from 31 Jul 2015. These years exist and were audited, so they are not history-limited: Ferguson plc / Wolseley plc published full annual reports for each of them.

| Needed | Status | Where it exists |
|---|---|---|
| FY2020–FY2025 statements, US GAAP (income statement and cash flow; balance sheets from 31 Jul 2021) | **retrieved**: SEC XBRL companyfacts, CIKs 1832433 and 2011641 (10-K FY2022, FY2023, FY2024, FY2025; 10-KT TP2025) | sec.gov |
| FY2019 income statement and cash flow; balance sheets 31 Jul 2018–31 Jul 2021, IFRS | partly retrieved (XBRL headline lines of the FY2021 Form 20-F; see below) | Form 20-F FY2021 |
| Balance sheets 31 Jul 2015–31 Jul 2020 at the line level (NIBCL build), US GAAP or IFRS | **not retrieved** | Annual Reports and Accounts 2016–2020; Form 20-F FY2021 |
| FY2016–FY2018 statements | **not retrieved** | Annual Reports and Accounts 2016–2018 (FY2016 and probably FY2017 presented in GBP; FY2018 in USD: revenue $20,752m per the FY2018 results announcement) |
| Undiscounted operating-lease commitment schedules for FY2015–FY2019 (P18: pre-IFRS 16 years; IFRS 16 adopted for FY2020) | **not retrieved** | the leases note of each annual report. The FY2018 results announcement (investegate.co.uk) carries the primary statements but no commitment schedule, only rental expense lines. US GAAP operating lease liabilities were 1,090 at 31 Jul 2021 against total assets of 13,709 (8.0%), and 1,814 against 17,729 at 31 Jul 2025 (10.2%): the 10% P18 test cannot be settled for the earlier years without the schedules. |
| Restated continuing-operations perimeter for FY2016–FY2019 | **not retrieved** | Nordic businesses sold in FY2018–FY2019 and the UK business sold in January 2021 (FY2021) are discontinued operations; each year's report restates its comparatives. |

The memo cannot be written without these inputs: B1–B3 need eleven balance sheets and ten years of OI and maintenance-capex FCF on one perimeter, with P18 capitalisation in every pre-adoption year (MODEL §2·1A Leases). Gates 1A and 1C (the earlier-window repurchases and deals) rest on them.

## Hosts tried

- `corporate.ferguson.com` and `www.corporate.ferguson.com` (annual-reports pages; the 2017 report URL redirects there): HTTP 403, a Cloudflare "Just a moment…" bot challenge. `robots.txt` was not readable either.
- `s201.q4cdn.com/465729859/files/doc_news/`: the "Annual Financial Report" files of 2017, 2018, 2019 and 2020 are the RNS publication notices (DTR 6.3.5 extracts), not the reports; the 2016 file name guessed from the 19 Oct 2016 notice returned 404.
- `investegate.co.uk`: the FY2018 results announcement retrieved (primary statements, no lease commitment schedule).
- 2 exploratory searches (P14), both looking for the annual-report PDFs.

**Fix for the next run:** an attended session obtains the Annual Reports and Accounts 2016–2020 (FCA National Storage Mechanism, or the IR site from a browser) and the Form 20-F FY2021 PDF (`s201.q4cdn.com/465729859/files/doc_news/2021-Annual-Report-on-Form-20-F-09-29-2021-2021.pdf`, found but not opened this run). Or Jakub decides whether pre-FY2020 years on the IFRS basis and an older perimeter count as history-limited for this name. Then reset the queue line.

## Sourced figures: consolidated US GAAP (USD million; SEC XBRL, 10-K/10-KT facts)

| Line | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | TP2025 (5 months to 31 Dec 2025) |
|---|---|---|---|---|---|---|---|
| Net sales | 19,940 | 22,792 | 28,566 | 29,734 | 29,635 | 30,762 | 12,833 |
| Gross profit | 5,983 | 6,980 | 8,756 | 9,025 | 9,053 | 9,435 | 3,930 |
| Operating income (as reported) | 1,372 | 1,950 | 2,820 | 2,659 | 2,652 | 2,606 | 1,099 |
| Net income | 961 | 1,472 | 2,122 | 1,889 | 1,735 | 1,856 | 786 |
| CFO | 1,545 | 1,382 | 1,149 | 2,723 | 1,873 | 1,908 | 859 |
| Capital expenditures | 283 | 241 | 290 | 441 | 372 | 305 | 185 |
| CFO − all capex `[derived]` | 1,262 | 1,141 | 859 | 2,282 | 1,501 | 1,603 | 674 |
| Depreciation (PP&E) | 139 | 130 | 140 | 148 | 162 | 187 | 89 |
| Amortisation of acquired intangibles | 143 | 168 | 161 | 173 | 173 | 186 | 68 |
| Share-based compensation | 29 | 77 | 57 | 51 | 49 | 28 | 70 |
| Diluted weighted-average shares (m) | 226.8 | 224.8 | 218.9 | 207.2 | 203.5 | 199.2 | 196.2 |
| Repurchases (cash) | 451 | 400 | 1,545 | 908 | 634 | 948 | 407 |
| Dividends paid | 327 | 1,036 | 538 | 711 | 784 | 489 | 326 |
| Acquisitions, net of cash acquired | 271 | 286 | 650 | 616 | 260 | 301 | 21 |
| Interest paid | 114 | 104 | 94 | 182 | 188 | 189 | 89 |

| Balance sheet | 31 Jul 2021 | 31 Jul 2022 | 31 Jul 2023 | 31 Jul 2024 | 31 Jul 2025 | 31 Dec 2025 | 30 Jun 2026 (10-Q) |
|---|---|---|---|---|---|---|---|
| Total assets | 13,709 | 15,661 | 15,994 | 16,572 | 17,729 | 17,152 | 19,303 |
| Total liabilities | 8,706 | 10,996 | 10,957 | 10,956 | 11,897 | 11,295 | n/a, not extracted |
| Shareholders' equity | 5,003 | 4,665 | 5,037 | 5,616 | 5,832 | 5,857 | 6,201 |
| Cash and cash equivalents | 1,335 | 771 | 601 | 571 | 674 | 557 | 437 |
| Accounts payable | 3,030 | 3,607 | 3,408 | 3,410 | 3,577 | 3,117 | n/a, not extracted |
| Other current liabilities | 1,445 | 1,297 | 1,516 | 1,261 | 1,578 | 1,392 | n/a, not extracted |
| Long-term debt, current | 0 | 250 | 55 | 150 | 400 | 148 | 448 |
| Long-term debt, non-current | 2,512 | 3,679 | 3,711 | 3,774 | 3,752 | 3,978 | 4,456 |
| Operating lease liabilities (total) | 1,090 | 1,199 | 1,492 | 1,593 | 1,814 | 1,891 | n/a, not extracted |
| Goodwill | 1,828 | 2,048 | 2,241 | 2,357 | 2,464 | 2,470 | n/a, not extracted |
| Other intangible assets | 546 | 782 | 783 | 753 | 726 | 685 | n/a, not extracted |
| Net PP&E | 1,305 | 1,376 | 1,595 | 1,752 | 1,846 | 1,911 | n/a, not extracted |

- US GAAP equity at 31 Jul 2019 and 31 Jul 2020: 4,407 and 4,609 (10-K FY2022 equity statement).
- **IFRS (Form 20-F FY2021, continuing operations, USD million):** operating profit FY2019 1,379, FY2020 1,449, FY2021 2,034; CFO 1,290, 1,868, 1,541; equity 4,057 (31 Jul 2018), 4,350 (2019), 4,371 (2020), 4,810 (2021); cash 833, 1,133, 2,115, 1,335; total assets 13,456 (2020) and 13,485 (2021); total liabilities 9,085 and 8,675. **Extraction note (§4):** the IFRS and US GAAP figures for the same years differ (FY2020 operating profit 1,449 IFRS against 1,372 US GAAP; FY2020 CFO 1,868 against 1,545, IFRS 16 putting lease principal in financing), so the two bases cannot be spliced without a reconciliation.
- **Interim 2026 (10-Qs):** Q1 2026 net sales 7,472, operating income 612; Q2 2026 net sales 8,751, operating income 893; H1 2026 diluted weighted shares 194.4m (Q2 194.0m). Shares outstanding 193,452,717 at 3 Aug 2026 (10-Q cover).
- **Price (endpoint `FERG`, retrieved 2026-10-24):** USD, exchange NYQ (NYSE), "Ferguson Enterprises Inc.", close 226.86 on 2026-10-23, no split events in the last five days' query. MCap at 194.0m diluted shares ≈ 44,011 `[derived]`.

## Sources retrieved

- SEC: submissions indexes (CIKs 2011641, 1832433, 1139313, 1714179, 1773261); XBRL companyfacts (CIKs 2011641 and 1832433); company tickers file. All with the configured user agent.
- investegate.co.uk: Ferguson plc results for the year ended 31 July 2018 (RNS 5427008).
- s201.q4cdn.com: RNS publication notices of 25 Oct 2017, 12 Oct 2018, 18 Oct 2019 and 30 Oct 2020.
- query1.finance.yahoo.com: `FERG` chart.

*Framework output, not investment advice.*
