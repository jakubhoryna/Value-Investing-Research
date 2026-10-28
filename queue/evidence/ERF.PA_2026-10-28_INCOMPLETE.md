# INCOMPLETE evidence: ERF.PA, Eurofins Scientific SE, 2026-10-28

- run: ANALYSE routine, D 2026-10-28, T 2332, base 564bac3bbd49d6414bd96400893c845fb19650cd, MODEL v4.7.0
- identity: Eurofins Scientific SE (Luxembourg-registered European company; listed on Euronext Paris, ticker ERF). Price endpoint `ERF.PA`: instrument "Eurofins Scientific SE", `exchangeName` PAR, `currency` EUR; close 86.24 on 2026-10-28 (endpoint, no split events in the 5-day range). ISIN: n/a — not established this run (no primary document read so far prints it). Prior check: no `company:` line in `memos/` or `archive/memos/` names Eurofins, and `register.csv` has no such row.
- **No verdict.** The data-completeness gate (README §5, D3) stopped the run before any gate was called.

## Why INCOMPLETE: named gap (record-limited FY2016)

Fiscal year = calendar year. The P1 window is FY2016–FY2025, with 11 balance sheets from 31 Dec 2015. These years exist and were audited: Eurofins published full annual reports for 2015 (notice of 18 Mar 2016) and 2017 (notice of 6 Mar 2018), and a 2016 Annual Report is listed in its financial-reports archive. They are not history-limited.

| Needed | Status | Where it exists |
|---|---|---|
| FY2024–FY2025 statements | **retrieved**: Annual Report 2025 (consolidated statements pp. 133–136) | cdnmediaassets.eurofins.com |
| FY2022–FY2024 statements | **retrieved**: Annual Reports 2023 and 2024 | cdnmediaassets.eurofins.com |
| FY2017–FY2021 statements (each report carries the prior year) | **retrieved**: Annual Reports 2018, 2019, 2021 (bnains.org mirror), 2020 (zelenaslovenija.si mirror) | as listed |
| FY2016 income statement and cash flow; balance sheets 31 Dec 2015 and 31 Dec 2016 at the line level (NIBCL build) | **not retrieved** | Annual Report 2016 (and the 2017 report's comparatives) |
| Undiscounted operating-lease commitments for 31 Dec 2015 and 2016 (P18: IFRS 16 adopted 1 Jan 2019, so FY2016–FY2018 are pre-adoption years) | **not retrieved** for 2015–2016 | leases note of the 2016 and 2017 reports |
| H1 2026 interim (balance sheet for the EV inputs) | **retrieved**: First Half Year 2026 Report | cdnmediaassets.eurofins.com |

B1–B3 need eleven balance sheets and ten years of OI and maintenance-capex FCF; with FY2016 and the 2015/2016 balance sheets missing, the record is nine fiscal years (FY2017–FY2025) and ten balance sheets at best. The years are published, so this is a record-limited shortfall: INCOMPLETE, not a memo on the short record (README §5, D3).

## Hosts tried

- `www.eurofins.com/en/investors/reports-and-presentations/` and `…/previous-financial-years/`: the current page links only the 2023–2025 annual reports; the previous-years page loads its list by script and returned no document links to curl. `…/financial-reports-archive/` redirects to the current page.
- `cdnmediaassets.eurofins.com`: 2023, 2024 and 2025 annual reports and the H1 2026 report retrieved.
- `eurofins.com/media/12154549/…2020-annual-report_final.pdf`: not retrieved (empty response); the same report came from the `zelenaslovenija.si` mirror.
- `www.bnains.org/archives/communiques/Eurofins/`: 2018, 2019 and 2021 annual reports retrieved. File names `{date}_Annual_report_{2016|2017}_Eurofins_EN.pdf` and `{date}_Communique_resultats_annuels_{2016|2017}_Eurofins_EN.pdf` tried for every date 15 Feb–20 Apr of the following year (several naming variants): all 404.
- `echanges.dila.gouv.fr/OPENDATA/AMF/BWR/`: the 2015 and 2017 annual-report notices only (no statements); the 24 Feb–9 Mar 2017 Business Wire files carry no Eurofins release.
- `web.archive.org`: blocked by the egress policy.
- 4 exploratory searches (P14), all looking for the older annual-report PDFs.

**Fix for the next run:** an attended session obtains the Annual Report 2016 (and 2017, for the restated comparatives and lease note) from the Eurofins previous-financial-years page in a browser, or from the Luxembourg Stock Exchange OAM, and runs the analysis; or Jakub resets the queue line with `retry`. Or Jakub decides how a run should treat the missing years.

## Sourced figures: consolidated IFRS (EUR million; Annual Report 2025, pp. 133–136)

| Line | FY2024 | FY2025 |
|---|---|---|
| Revenues (reported) | 6,951.0 | 7,296.1 |
| EBITAS (reported) | 842.5 | 931.5 |
| Share-based payment charge and acquisition-related expenses, net | -138.3 | -138.1 |
| Gain and loss on disposal of subsidiaries, net | -23.6 | -8.9 |
| EBIT (reported; the lowest operating subtotal on the face) | 680.5 | 784.5 |
| EBIT "adjusted" (filer APM, before separately disclosed items; never OI under J1) | 1,016.9 | 1,079.0 |
| Finance income / finance costs | 24.2 / -151.2 | 35.2 / -165.8 |
| Net profit for the year | 405.5 | 473.0 |
| Diluted average shares (m) | 194.5 | 186.5 |
| Net cash provided by operating activities | 1,318.9 | 1,398.9 |
| Purchase of PP&E / of intangible assets | -453.6 / -74.8 | -461.7 / -74.9 |
| Acquisition of subsidiaries, net | -343.4 | -261.4 |
| Purchase of PP&E from related parties (note 2.37) | 0 | -298.2 |
| Purchase of treasury shares, net | -271.9 | -541.3 |
| Repayment of lease liabilities | -192.4 | -194.0 |
| Earnings paid to hybrid capital investors | -53.5 | -49.7 |
| Interest and premium paid (financing) | -114.2 | -115.5 |
| Dividends paid | -98.0 | -109.8 |

| Balance sheet (31 Dec) | 2024 | 2025 |
|---|---|---|
| Total assets | 10,888.4 | 10,985.4 |
| Goodwill | 4,840.7 | 4,657.2 |
| Other intangible assets | 787.8 | 689.9 |
| Cash and cash equivalents | 613.9 | 791.2 |
| Borrowings, non-current + current | 3,610.3 | 4,432.0 |
| Hybrid capital (inside equity; a debt-equivalent at 100% under Gate 2) | 1,000.0 | 1,000.0 |
| Trade accounts payable | 645.9 | 678.1 |
| Contract liabilities | 195.9 | 217.4 |
| Other current liabilities | 621.0 | 644.6 |
| Total attributable to owners (hybrid included) | 5,339.0 | 4,543.3 |
| Non-controlling interests | 45.8 | 33.4 |
| Total equity | 5,384.7 | 4,576.7 |

Observations for the next run (facts, no grades):
- The reported EBIT and the filer's "adjusted" EBIT differ by EUR 294.5m in FY2025 (separately disclosed items: SBP, acquisition-related charges, network-reorganisation and start-up costs); J1 takes the reported EBIT.
- FY2025 carries a EUR 298.2m purchase of property from related parties (note 2.37): a controller-as-counterparty asset dealing for §2·1C·2 and the ·3 worth reading.
- Hybrid capital (EUR 1,000m) sits inside equity; BV for L/E and per-share series excludes NCI, and Gate 2 adds the hybrid at 100%.
- Lease liabilities' location inside borrowings (note 2.18) still to be confirmed.

Framework output, not investment advice.
