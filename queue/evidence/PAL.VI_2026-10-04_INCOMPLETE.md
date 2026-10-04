# INCOMPLETE evidence — PAL.VI — Palfinger AG — 2026-10-04

- run: ANALYSE routine, D 2026-10-04, T 0356, base 446eb1417a1d060e054910b2abe1fb918478ed10, MODEL v4.4.1
- identity: Palfinger AG, Wiener Börse (prime market), symbol PAL, ISIN **AT0000758305** (sourced: palfinger.com investors page, 2026-10-04), LEI 529900IFAV83BX8O1O91 (sourced: ESEF filings index). Prior check: no `memos/*/` file carries this ISIN or the name "Palfinger"; no register row matches the name.
- **No verdict.** The data-completeness gate (README §5, D3) stopped the run before any gate was called.

## Why INCOMPLETE — named gaps

The P1 window (FY2016–FY2025; 11 balance sheets FY2015–FY2025) is published and audited in Palfinger's annual reports. This run could retrieve only FY2019–FY2025 (seven balance sheets, six YoY return years). That is a record-limited shortfall where more years are published, so the run stops (D3) instead of writing a capped memo.

| Needed | Status | Where it exists |
|---|---|---|
| FY2020–FY2025 statements (FY2019 as comparatives) | **retrieved**: ESEF xBRL-JSON | filings.xbrl.org, LEI 529900IFAV83BX8O1O91 |
| FY2015–FY2018 statements | **not retrieved** | Integrated Annual Reports 2016, 2017 and 2018 (PDF), www.palfinger.com `/content/dam/…/reports/2016/PALFINGER_Integrated-Annual-Report_2016_EN.pdf`, `…/2017/PALFINGER_Integrated-Annual-Report_2017_EN.pdf`; 2018: assets.palfinger.com `…/en/reports/2018/PALFINGER_iGB_2018_EN.pdf` |
| Notes: NIBCL composition, debt and lease split, diluted share counts, treasury movements, segment/customer sentences | **not worked** | the ESEF reports (text blocks) and annual reports; diluted counts are not tagged as numbers in the JSON |
| Remuneration report 2025, RPT note (Gate 1C) | **not retrieved** | palfinger.com corporate-governance / remuneration pages (PDF) |
| H1 2026 interim balance sheet (EV inputs) | **not retrieved** | `PALFINGER Halfyear Report 2026.pdf` on www.palfinger.com |
| Current price (Gate 2) | not retrieved (stopped before Gate 2) | Wiener Börse / any quote endpoint |

## Hosts tried

- `www.palfinger.com`: the IR index pages load (200). Its `robots.txt` disallows `/*.pdf$` for all user agents, and every annual, half-year and remuneration report is a PDF there. Not fetched: this unattended run honours robots exclusions.
- `assets.palfinger.com`: `robots.txt` is `Disallow: /` for all user agents. This host carries the 2018 report and the ESEF zips (2020–2025). Not fetched.
- `i-report.palfinger.ag` (the online report for 2016–2019): retired; it 301-redirects to palfinger.com pages.
- `issuerinfo.at` / `www.issuerinfo.at` (OeKB OAM): the proxy refused CONNECT (502). `issuerinfo.oekb.at` redirects to `my.oekb.at`, an SPA gated by a captcha. Not pursued.
- `sustainabilityreports.com` (a 2018 report mirror): 403.
- `filings.xbrl.org`: no robots exclusion; xBRL-JSON for FY2020–FY2025 retrieved (2021: filing version 1; 2024: filing version 2).

**Fix for the next run:** an attended session (or one where Jakub approves the palfinger.com PDFs) needs the Integrated Annual Reports 2016 and 2018 (FY2015–FY2018 with comparatives; 2017 as a cross-check), the Remuneration Report 2025, and the H1 2026 report. With those, the window is complete.

## Sourced figures — ESEF consolidated statements (IFRS, EUR m; latest filing per period wins)

| Line | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|---|
| Revenue | 1,753.8 | 1,533.9 | 1,841.5 | 2,226.2 | 2,445.9 | 2,359.8 | 2,339.3 |
| EBIT (operating result, as reported) | 149.0 | 100.3 | 155.0 | 150.4 | 210.2 | 185.6 | 174.3 |
| Net result, owners of parent | 80.0 | 49.8 | 86.6 | 71.4 | 107.7 | 100.0 | 96.7 |
| CFO | 156.0 | 224.7 | 87.4 | 46.1 | 186.7 | 228.0 | 255.5 |
| Payments for intangibles and PP&E | 95.6 | 65.1 | 128.8 | 116.1 | 155.5 | 151.8 | 107.8 |
| **FCF derived = CFO − capex** `[derived]` | 60.4 | 159.6 | −41.4 | −70.0 | 31.2 | 76.2 | 147.7 |
| Company "free cash flow" (own definition, not used) | 112.4 | 173.3 | −42.1 | −29.4 | 46.5 | 119.5 | 181.5 |
| Interest paid (classified in CFO) | 11.8 | 10.2 | 8.5 | 10.6 | 28.8 | 37.7 | 32.1 |
| Dividends paid to owners (financing) | 19.2 | 13.2 | 16.9 | 28.9 | 26.8 | 36.5 | 31.3 |
| Total assets | 1,641.6 | 1,556.9 | 1,692.6 | 1,958.2 | 2,061.1 | 2,134.5 | 2,142.6 |
| Cash and cash equivalents | 42.0 | 104.2 | 39.8 | 61.1 | 76.5 | 131.8 | 157.5 |
| Other current financial assets | 5.1 | 8.9 | 6.4 | 3.2 | 5.8 | 1.1 | 1.4 |
| Trade and other current payables | 273.2 | 259.2 | 355.4 | 430.1 | 405.9 | 387.9 | 403.8 |
| Current contract liabilities | 29.9 | 34.4 | 44.6 | 50.7 | 66.1 | 69.1 | 72.3 |
| Current tax liabilities | 9.0 | 6.8 | 15.4 | 12.8 | 18.9 | 14.2 | 14.6 |
| Current provisions | 21.2 | 23.2 | 30.9 | 34.6 | 44.4 | 46.0 | 43.5 |
| Other current financial liabilities | 69.7 | 68.7 | 189.4 | 121.4 | 148.2 | 108.0 | 115.5 |
| Current liabilities | 403.5 | 404.4 | 636.0 | 662.7 | 684.3 | 628.5 | 649.7 |
| Non-current liabilities | 609.0 | 536.1 | 442.8 | 620.6 | 661.3 | 752.9 | 573.7 |
| Total equity | 629.1 | 616.4 | 613.9 | 674.9 | 715.5 | 753.1 | 919.2 |
| Equity, owners of parent (BV) | 580.2 | 568.7 | 558.2 | 613.6 | 655.4 | 698.8 | 861.3 |
| Non-controlling interests | 48.9 | 47.8 | 55.6 | 61.2 | 60.1 | 54.3 | 57.9 |
| Intangible assets incl. goodwill | 280.4 | 248.7 | 256.7 | 257.8 | 249.6 | 253.4 | 260.5 |

Notes:
- Cash at 31 Dec 2018 was 34.7 (FY2019 cash-flow opening balance). It is the only FY2018 figure in the retrieved filings.
- Check: FY2025 total assets 2,142.6 = equity 919.2 + current liabilities 649.7 + non-current liabilities 573.7. It ties.
- Treasury-share transactions in the equity statement: −99.5 in FY2021 (shares acquired) and +99.0 in FY2025 (shares disposed). Counterparties and share counts were not worked; they are P19 evidence for the next run.
- The tagged lease-payment line reads 12.0 / 12.6 / 16.4 / 17.7 for FY2020, FY2021, FY2024 and FY2025, but 110.2 / 130.0 for FY2022 / FY2023, which looks like a tagging inconsistency. Unverified and not used; read the cash-flow statement in the report itself.
- The company's "free cash flow" is its own definition (it differs from CFO − capex by 0.7–52.0 a year). Only the derived line is a framework input.
- The company-disclosed ROCE (9.5% FY2025, basis undisclosed) in `queue/evidence/PAL.VI_draft-evidence_2026-09.md` is not a framework figure. The four CE variants need the NIBCL notes.

---
*Evidence note — not a memo, no verdict, not investment advice.*
