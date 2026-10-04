# INCOMPLETE evidence — KARN.SW — Kardex Holding AG — 2026-10-04

- run: ANALYSE routine, D 2026-10-04, T 0226, base 446eb1417a1d060e054910b2abe1fb918478ed10, MODEL v4.4.1
- identity: Kardex Holding AG, SIX Swiss Exchange, symbol KARN, ISIN **CH0100837282** (AR2025 p.6, sourced). Prior check: no `memos/*/` front matter carries this ISIN or the name "Kardex"; no register row matches the name.
- **No verdict.** The data-completeness gate (README §5, D3) stopped the run before any gate was called.

## Why INCOMPLETE — named gaps

The P1 window (FY2016–FY2025, 11 balance sheets FY2015–FY2025) is published, audited and exists in primary annual reports, but only part of it was retrieved this run:

| Needed | Status | Where it exists |
|---|---|---|
| FY2025, FY2024 statements | **retrieved** (AR2025) | investors.kardex.com |
| FY2023 statements | **not retrieved** | AR2023 / AR2024 (comparatives) |
| FY2022, FY2021 | URL located, not downloaded | kardex.com/hubfs/…/Annual_Reports/Kardex%20Annual%20Report%202022.pdf |
| FY2020 statements | **not retrieved** | AR2020 / AR2021 (comparatives) |
| FY2019, FY2018 | URL located, not downloaded | …/Annual_Reports/Kardex_Annual_Report_2019.pdf |
| FY2017 | URL located, not downloaded | …/Annual_Reports/Kardex_Annual_Report_2018_final.pdf |
| FY2016, FY2015 | URL located, not downloaded | …/Annual_Reports/Kardex_Annual_Report_2016.pdf |
| Remuneration report, RPT note (Gate 1C) | in AR2025, not yet worked | AR2025 |
| Current price (Gate 2) | not retrieved | SIX / any quote endpoint |

Record-limited shortfall where more years are published = INCOMPLETE (D3). Never filled with an assumption.

## Hosts tried

- `investors.kardex.com/investor-center/reporting` — a SvelteKit SPA; curl returns the shell only. WebFetch rendered the 2025–2026 entries (AR2025, Interim Report 2026, both downloaded). The year tabs for 2020–2024 load from the EQS content API (`tools.cms-eqs.com/6d5169/content/documents`), which returns 401 without a browser-issued token.
- `www.kardex.com/hubfs/Financial_reports_and_presentations/Annual_Reports/` — filename probes found the 2016, 2018 (`_final`), 2019 and 2022 reports. The 2020, 2021, 2023 and 2024 reports were not found under the tried name patterns.
- Rendering the IR page in headless Chromium failed (proxy CA not trusted by the browser). The session's permission classifier then refused further retrieval commands (third-party release pages and the located hubfs report downloads). The run stopped retrieval there.
- `sustainabilityreports.com` — 403.

**Fix for the next run:** the four located hubfs URLs plus AR2021 (gives FY2021/FY2020) and AR2024 (gives FY2024/FY2023) cover the window. Try `Kardex%20Annual%20Report%202024.pdf`-style names or the EQS archive from an attended session, then re-queue.

## Sourced figures (AR2025, Swiss GAAP FER, EUR m; and Interim Report 2026)

Reporting currency EUR; shares trade in CHF. **Goodwill is offset against equity** (Swiss GAAP FER option): goodwill offset −44.9 (FY25) / −45.0 (FY24) sits inside equity; theoretical capitalised net goodwill 0.7 / 1.3 (AR2025 note 3.3). This bears on TBV and CE and must be logged in Appendix C.

| Line | FY2025 | FY2024 | H1 2026 (30 Jun) |
|---|---|---|---|
| Net revenues | 850.4 | 791.2 | 440.5 (H1 2025: 415.7) |
| Operating result (EBIT) | 101.2 | 98.4 | 30.1 (H1 2025: 48.9) |
| Financial result, net | −34.9 | 5.1 | — |
| Result for the period | 41.8 | 80.8 | 22.3 |
| NI attributable to shareholders | 41.6 | 80.7 | — |
| CFO | 62.8 | 114.2 | 16.7 |
| Purchase of PP&E | −23.8 | −11.9 | −10.6 |
| Purchase of intangibles | −12.3 | −3.4 | −4.3 |
| FCF (derived = CFO − PP&E − intangibles capex) | 26.7 | 98.9 | 1.8 |
| Cash and cash equivalents | 118.1 | 136.0 | 91.8 |
| Current fixed-term deposits | 18.2 | 37.3 | 0.0 |
| Total assets | 503.0 | 493.5 | 514.9 |
| Trade accounts payable | 48.6 | 41.5 | 69.1 |
| Accruals | 86.1 | 84.9 | 93.1 |
| Other current liabilities | 59.3 | 41.1 | — |
| Non-current financial liabilities | 0.0 | 0.1 | — |
| Total liabilities | 233.3 | 208.6 | 269.8 |
| Equity before NCI (BV) | 268.3 | 283.9 | 244.0 |
| Intangible assets | 22.2 | 6.9 | — |
| Dividend paid | −48.5 | −39.4 | — |
| Acquisition of treasury shares | −1.7 | 0.0 | — |

Share data (AR2025 p.6): 7,730,000 registered shares (CHF 0.45 par), unchanged 2021–2025. Treasury shares 15,552 (2025) / 8,728 / 14,210 / 16,832 / 17,984 (2021). EPS basic = diluted ("no dilutive effect", AR2025). Dividend per share CHF 6.00 (2025 proposed), 6.00, 5.00, 3.50, 4.30 (2021).

FY2025 note (AR2025 income statement and cash flow): depreciation, amortisation and impairment 49.3 vs 13.7, consistent with the ~EUR 39m Rocket Solution loan write-off booked in the financial result (orientation note; verify in note 1.4 at the next run).

Derived FY2025 L/E = 233.3 ÷ 268.3 = 87.0% (derived; no lease capitalisation tested yet).

*Evidence note, no verdict. Framework output, not investment advice.*
