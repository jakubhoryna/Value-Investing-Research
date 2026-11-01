# CRISIL.NS — INCOMPLETE evidence (resumable record)

## 1. Header

| Field | Value |
|---|---|
| Key | CRISIL.NS (CRISIL Limited; NSE `CRISIL`, BSE 500092) |
| ISIN | INE007A01025 (AR23 PDF p. 102 and AR21 PDF p. 79, shareholder-information section "ISIN : INE007A01025"; not printed in AR25's text layer) |
| Job | ANALYSE (routine) |
| D · T | 2026-11-01 · 2132 (Europe/Prague) |
| Base sha | 131f28ea32208e317ac9a90739a94959ad3144fc |
| Live model_version | v4.8.0 |
| Prior memo | none (no `memos/CRISIL.NS/`, no `archive/memos/CRISIL.NS/`; no register row matches "CRISIL") |
| Named gap | `INCOMPLETE (group build exceeds budget)` — first overrun (the DRAFT_QUEUE line carries no ` — partial …` note at base) |
| Resumes | none (first record) |

**Why a group build.** AR25 note 39 (consolidated segment reporting) shows two reportable segments, both material under P22: Ratings services (revenue ₹107,663 lakh, 29.5% of ₹364,901 lakh) and Research, Analytics and Solutions (₹257,238 lakh, 70.5%). The group therefore needs B4 with P29 weights and S, one Appendix D block per unit, and the §2·1C·3 allocation-across-the-parts table. On top of it the run found a G6 class above the P31 line (quoted and unquoted equity stakes at 10.7% of total assets at FY2025, §3 below) and a pre-Ind AS 116 lease test (P18) owed for FY2016–FY2019. That build could not finish inside the run's time budget, so research stopped here and this record was written.

All figures below are ₹ lakh (1 lakh = 0.1 INR m) as printed, consolidated Ind AS, fiscal years ending 31 December, unless stated. PDF page numbers are the file's page index; the printed folio is PDF page − 3 in AR25.

## 2. Sources (primary, retrieved 2026-11-01)

| Ref | Document | URL |
|---|---|---|
| AR25 | Integrated Annual Report 2025 (FY2025; auditor Walker Chandiok & Co LLP; statements signed 13 Feb 2026) | bseindia.com/xml-data/corpfiling/AttachHis/5ca06d60-aff0-4016-981c-caf1990aecad.pdf |
| AR24 | Annual Report 2024 (FY2024, FY2023 restated comparatives) | bseindia.com/xml-data/corpfiling/AttachHis/3efc592d-0a2e-4b79-8158-6f0f50180319.pdf |
| AR23 | Annual Report 2023 (FY2023, FY2022) | bseindia.com/xml-data/corpfiling/AttachHis/9b8b42ca-53ea-43a2-9070-108e429872cf.pdf |
| AR21 | Annual Report 2021 (FY2021, FY2020) | bseindia.com/bseplus/AnnualReport/500092/72949500092.pdf |
| AR19 | Annual Report 2019 (FY2019, FY2018) | bseindia.com/bseplus/AnnualReport/500092/5000921219.pdf |
| AR17 | Annual Report 2017 (FY2017, FY2016 and the Ind AS transition balance sheet at 1 Jan 2016 = BS FY2015) | bseindia.com/bseplus/AnnualReport/500092/5000921217.pdf |
| AR16 | Annual Report 2016 (downloaded, not yet read) | bseindia.com/bseplus/AnnualReport/500092/5000921216.pdf |
| PX | query1.finance.yahoo.com/v8/finance/chart/CRISIL.NS: currency INR, exchangeName NSI, longName "CRISIL Limited", instrumentType EQUITY; daily close 4,516.60 on 2026-10-30 (meta regularMarketPrice 4,533.0 at 2026-10-30 09:59 UTC, the last trade); no split events over 10 years | — |

P14: 1 exploratory operation (one fetch of the screener.in consolidated company page to locate the BSE annual-report links). Everything else is primary retrieval or the quote endpoint, uncounted. AR22 and AR20 were not needed (each AR carries two years).

## 3. Figures by gate or leg

### 3a. Gate 0 and the lens (work done)

- **Segments (AR25 note 39, PDF p. 262–263).** Ratings services: "credit ratings for corporates, banks, bank loans, credit analysis services, grading services and global analytical services". Research, Analytics and Solutions: "global research and risk solutions, industry reports, customized research assignments, subscription to data services, training, advisory services and a comprehensive range of risk management tools, analytics and solutions to financial institutions, banks and corporates in India".
- **Geography (same page).** FY2025 revenue: India 112,668; Europe 74,323; North America 142,532; rest of world 35,378.
- **Controller.** S&P Global Inc. is the ultimate holding company (AR25 note 40, PDF p. 264); its holders of record in the dividend lines are S&P India, LLC, S&P Global Asian Holdings Pte. Limited and Standard & Poor's International LLC. Share capital outstanding with them: 312 + 115 + 60 = ₹487 lakh of ₹731 lakh (₹1 shares) = 66.6%, derived from AR25 note 40 (PDF p. 265–266). Re-confirm from the shareholding pattern.
- **Lens (orientation, not settled).** No banking or insurance licence found in the documents read; a credit rating and research business is not FI. STD expected. Log the test in Appendix C at resume.
- **Listed parts.** No controlled listed subsidiary found. Listed holdings: CARE Ratings Limited 2,622,431 shares (percentage of CARE's capital not yet sourced) carried at ₹41,956 lakh FY2025 (₹36,180 lakh FY2024) through OCI, and one ICRA share (nil). CARE at market is about 1.3% of CRISIL's market cap (derived), so it is not a material holding (P22: ≥ 10% of MCap); it is S2 or S3 at Gate 2 depending on whether the filer calls it strategic (note 9.1, owed).

### 3b. Item table

| item | FY | value | unit | source |
|---|---|---|---|---|
| Revenue from operations | 2025 | 364,901 | ₹ lakh | AR25 PDF p. 218, consolidated P&L |
| Other income | 2025 | 10,654 | ₹ lakh | AR25 PDF p. 218 |
| Employee benefits expense | 2025 | 194,332 | ₹ lakh | AR25 PDF p. 218 |
| Finance costs (lease interest) | 2025 | 2,222 | ₹ lakh | AR25 PDF p. 218; CF p. 220 "Finance cost paid towards lease liabilities" |
| Depreciation and amortisation | 2025 | 12,852 | ₹ lakh | AR25 PDF p. 218 |
| Other expenses | 2025 | 62,046 | ₹ lakh | AR25 PDF p. 218 |
| Profit before tax | 2025 | 104,103 | ₹ lakh | AR25 PDF p. 218 |
| Profit after tax (all to owners; NCI nil) | 2025 | 76,601 | ₹ lakh | AR25 PDF p. 218 |
| Diluted EPS | 2025 | 104.75 | ₹ | AR25 PDF p. 218 |
| OI candidate (revenue − employee − D&A − other expenses) | 2025 | 95,671 | ₹ lakh | derived: AR25 PDF p. 218 lines above |
| CFO | 2025 | 75,558 | ₹ lakh | AR25 PDF p. 219 |
| Purchase of PP&E and intangibles | 2025 | 7,340 | ₹ lakh | AR25 PDF p. 219 |
| Payment for PriceMetrix, net of cash | 2025 | 28,491 | ₹ lakh | AR25 PDF p. 219; note 45.3 PDF p. 273 |
| Fixed deposits > 3 months placed (net) | 2025 | 33,612 | ₹ lakh | AR25 PDF p. 219 |
| Dividend on investments received | 2025 | 498 | ₹ lakh | AR25 PDF p. 219 |
| Dividend paid | 2025 | 43,147 | ₹ lakh | AR25 PDF p. 220 |
| Lease principal paid | 2025 | 1,630 | ₹ lakh | AR25 PDF p. 220 |
| Total assets | 2025 | 463,194 | ₹ lakh | AR25 PDF p. 217, consolidated balance sheet |
| Total equity | 2025 | 303,344 | ₹ lakh | AR25 PDF p. 217 |
| Goodwill | 2025 | 68,065 | ₹ lakh | AR25 PDF p. 217 |
| Other intangible assets | 2025 | 30,775 | ₹ lakh | AR25 PDF p. 217 |
| Intangible assets under development | 2025 | 2,821 | ₹ lakh | AR25 PDF p. 217 |
| PP&E | 2025 | 15,109 | ₹ lakh | AR25 PDF p. 217 |
| Capital work-in-progress | 2025 | 157 | ₹ lakh | AR25 PDF p. 217 |
| Right-of-use assets | 2025 | 30,050 | ₹ lakh | AR25 PDF p. 217 |
| Non-current investments | 2025 | 49,403 | ₹ lakh | AR25 PDF p. 217; note 9A PDF p. 241 |
| — of which unquoted equity (NCDEX 3,700; CARICRA 116; Online PSB Loans 3,631) | 2025 | 7,447 | ₹ lakh | AR25 note 9A PDF p. 241 |
| — of which CARE Ratings (2,622,431 shares, quoted, FVOCI) | 2025 | 41,956 | ₹ lakh | AR25 note 9A PDF p. 241 |
| Current investments (mutual funds, FVTPL) | 2025 | 68,643 | ₹ lakh | AR25 PDF p. 217; note 9B PDF p. 241 |
| Cash and cash equivalents | 2025 | 32,013 | ₹ lakh | AR25 PDF p. 217 |
| Other bank balances | 2025 | 321 | ₹ lakh | AR25 PDF p. 217 |
| Other current financial assets | 2025 | 36,363 | ₹ lakh | AR25 PDF p. 217 (holds the term deposits placed in 2025; note 18 split owed) |
| Trade receivables | 2025 | 68,743 | ₹ lakh | AR25 PDF p. 217 |
| Trade payables (MSE 1,401; others 13,153) | 2025 | 14,554 | ₹ lakh | AR25 PDF p. 217 |
| Current tax liabilities | 2025 | 328 | ₹ lakh | AR25 PDF p. 217 |
| Lease liabilities (non-current 24,718; current 4,963) | 2025 | 29,681 | ₹ lakh | AR25 PDF p. 217; CF reconciliation p. 220 |
| Other current financial liabilities | 2025 | 44,252 | ₹ lakh | AR25 PDF p. 217 (note 26 split owed) |
| Other current liabilities | 2025 | 42,818 | ₹ lakh | AR25 PDF p. 217 (note 27 split owed: contract liabilities) |
| Current provisions | 2025 | 13,715 | ₹ lakh | AR25 PDF p. 217 |
| Equity share capital (₹1 shares) | 2025 | 731 | ₹ lakh | AR25 PDF p. 217 |
| Segment revenue Ratings / RAS | 2025 | 107,663 / 257,238 | ₹ lakh | AR25 note 39 PDF p. 262 |
| Segment results Ratings / RAS | 2025 | 47,822 / 56,655 | ₹ lakh | AR25 note 39 PDF p. 262 |
| Unallocable D&A | 2025 | 7,775 | ₹ lakh | AR25 note 39 PDF p. 263 |
| Unallocable expenditure | 2025 | 2,289 | ₹ lakh | AR25 note 39 PDF p. 263 |
| Segment assets Ratings / RAS / unallocable | 2025 | 48,748 / 167,428 / 247,018 | ₹ lakh | AR25 note 39 PDF p. 263 |
| Segment liabilities Ratings / RAS / unallocable | 2025 | 35,596 / 74,990 / 49,264 | ₹ lakh | AR25 note 39 PDF p. 263 |
| Revenue from operations | 2024 | 325,978 | ₹ lakh | AR25 PDF p. 218 (comparative) |
| Other income | 2024 | 8,964 | ₹ lakh | AR25 PDF p. 218 |
| Employee / D&A / other expenses / finance costs | 2024 | 176,509 / 6,995 / 58,388 / 403 | ₹ lakh | AR25 PDF p. 218 |
| PBT / PAT / diluted EPS | 2024 | 92,647 / 68,407 / 93.55 | ₹ lakh, ₹ | AR25 PDF p. 218 |
| OI candidate | 2024 | 84,086 | ₹ lakh | derived: AR25 PDF p. 218 |
| CFO / capex | 2024 | 76,506 / 17,316 | ₹ lakh | AR25 PDF p. 219 |
| Dividend on investments / dividend paid | 2024 | 472 / 42,412 | ₹ lakh | AR25 PDF p. 219–220 |
| Lease principal / lease interest paid | 2024 | 1,609 / 403 | ₹ lakh | AR25 PDF p. 220 |
| Total assets (restated in AR25; AR24 printed 394,178) | 2024 | 394,597 | ₹ lakh | AR25 PDF p. 217 |
| Total equity | 2024 | 256,482 | ₹ lakh | AR25 PDF p. 217 |
| Goodwill / other intangibles / IAUD / PP&E / CWIP / ROU | 2024 | 42,464 / 10,834 / 5,375 / 16,003 / 85 / 28,262 | ₹ lakh | AR25 PDF p. 217 |
| Non-current investments (unquoted equity 2,786; CARE 36,180) | 2024 | 38,966 | ₹ lakh | AR25 PDF p. 217; note 9A p. 241 |
| Current investments / cash / other bank balances | 2024 | 106,441 / 30,191 / 254 | ₹ lakh | AR25 PDF p. 217 |
| Trade payables (1,208 + 16,389) / tax liabilities | 2024 | 17,597 / 165 | ₹ lakh | AR25 PDF p. 217 |
| Lease liabilities (24,127 + 873) | 2024 | 25,000 | ₹ lakh | AR25 PDF p. 217, p. 220 |
| Segment revenue Ratings / RAS | 2024 | 90,915 / 235,063 | ₹ lakh | AR25 note 39 PDF p. 263 |
| Segment results Ratings / RAS | 2024 | 40,012 / 50,310 | ₹ lakh | AR25 note 39 PDF p. 263 |
| Unallocable D&A / unallocable expenditure | 2024 | 4,914 / 967 | ₹ lakh | AR25 note 39 PDF p. 263 |
| Segment assets Ratings / RAS / unallocable | 2024 | 46,878 / 134,523 / 212,777 | ₹ lakh | AR25 note 39 PDF p. 263 |
| Revenue / other income | 2023 | 313,952 / 9,364 | ₹ lakh | AR24 PDF p. 170 (= AR23 PDF p. 174) |
| Employee / finance / D&A / other expenses | 2023 | 174,777 / 366 / 10,378 / 51,025 | ₹ lakh | AR24 PDF p. 170 |
| PBT / PAT / diluted EPS | 2023 | 86,770 / 65,844 / 90.07 | ₹ lakh, ₹ | AR24 PDF p. 170 |
| OI candidate | 2023 | 77,772 | ₹ lakh | derived: AR24 PDF p. 170 |
| CFO / capex / dividend on investments | 2023 | 78,033 / 6,294 / 839 | ₹ lakh | AR24 PDF p. 171 (AR23 p. 175 prints capex 6,295) |
| Dividend paid / lease principal / lease interest | 2023 | 35,816 / 5,506 / 366 | ₹ lakh | AR24 PDF p. 171–172 |
| Total assets (AR24 restated; AR23 printed 331,452) | 2023 | 329,739 | ₹ lakh | AR24 PDF p. 169 |
| Total equity | 2023 | 218,926 | ₹ lakh | AR24 PDF p. 169 |
| Goodwill / other intangibles / IAUD / PP&E / ROU | 2023 | 42,080 / 11,409 / 3,086 / 4,446 / 5,529 | ₹ lakh | AR24 PDF p. 169 |
| Non-current investments / current investments | 2023 | 27,813 / 77,800 | ₹ lakh | AR24 PDF p. 169 |
| Cash / other bank balances / trade receivables (restated) | 2023 | 36,612 / 378 / 67,238 | ₹ lakh | AR24 PDF p. 169 (AR23 prints receivables 68,951) |
| Trade payables (1,064 + 13,192) / tax liabilities | 2023 | 14,256 / 389 | ₹ lakh | AR24 PDF p. 169 |
| Lease liabilities (3,076 + 1,656) | 2023 | 4,732 | ₹ lakh | AR24 PDF p. 169 |
| Revenue / other income | 2022 | 276,872 / 12,247 | ₹ lakh | AR23 PDF p. 174 |
| Employee / finance / D&A / other expenses | 2022 | 155,298 / 640 / 10,331 / 48,610 | ₹ lakh | AR23 PDF p. 174 |
| PBT / PAT / diluted EPS | 2022 | 74,240 / 56,439 / 77.26 | ₹ lakh, ₹ | AR23 PDF p. 174 |
| OI candidate | 2022 | 62,633 | ₹ lakh | derived: AR23 PDF p. 174 |
| CFO / capex / dividend on investments | 2022 | 45,634 / 4,114 / 272 | ₹ lakh | AR23 PDF p. 175 |
| Dividend paid / lease principal / lease interest | 2022 | 34,314 / 5,429 / 640 | ₹ lakh | AR23 PDF p. 176 |
| Total assets / total equity | 2022 | 283,100 / 179,198 | ₹ lakh | AR23 PDF p. 173 |
| Goodwill / other intangibles / IAUD / PP&E / ROU | 2022 | 37,983 / 10,518 / 1,359 / 4,737 / 8,660 | ₹ lakh | AR23 PDF p. 173 |
| Non-current investments / current investments | 2022 | 19,077 / 49,265 | ₹ lakh | AR23 PDF p. 173 |
| Cash / other bank balances | 2022 | 31,925 / 218 | ₹ lakh | AR23 PDF p. 173 |
| Trade payables (735 + 13,465) / tax liabilities | 2022 | 14,200 / 1,199 | ₹ lakh | AR23 PDF p. 173 |
| Lease liabilities (2,389 + 5,957) | 2022 | 8,346 | ₹ lakh | AR23 PDF p. 173 |
| Revenue / other income | 2021 | 230,069 / 7,702 | ₹ lakh | AR21 PDF p. 175 |
| Employee / finance / D&A / other expenses | 2021 | 128,691 / 893 / 10,598 / 40,327 | ₹ lakh | AR21 PDF p. 175 |
| Exceptional item (gain; profit on sale of property, note 19.1) | 2021 | 4,582 | ₹ lakh | AR21 PDF p. 175 |
| PBT / PAT / diluted shares | 2021 | 61,844 / 46,581 / 72,827,971 | ₹ lakh, shares | AR21 PDF p. 175 |
| OI candidate (exceptional gain out) | 2021 | 50,453 | ₹ lakh | derived: AR21 PDF p. 175 |
| CFO / capex / dividend paid / lease payment | 2021 | 40,312 / 2,279 / 27,649 / 5,823 | ₹ lakh | AR21 PDF p. 176–177 |
| Total assets / equity (729 + 157,113) | 2021 | 250,387 / 157,842 | ₹ lakh | AR21 PDF p. 174 |
| Goodwill / intangibles / IAUD / PP&E / ROU | 2021 | 37,267 / 12,081 / 549 / 4,034 / 12,700 | ₹ lakh | AR21 PDF p. 174 |
| Non-current investments / current investments | 2021 | 19,538 / 44,946 | ₹ lakh | AR21 PDF p. 174 |
| Cash / other bank balances | 2021 | 28,992 / 443 | ₹ lakh | AR21 PDF p. 174 |
| Trade payables (13 + 13,357) / tax liabilities | 2021 | 13,370 / 528 | ₹ lakh | AR21 PDF p. 174 |
| Revenue / other income | 2020 | 198,183 / 8,315 | ₹ lakh | AR21 PDF p. 175 |
| Employee / finance / D&A / other expenses | 2020 | 106,844 / 1,439 / 12,111 / 40,275 | ₹ lakh | AR21 PDF p. 175 |
| PBT / PAT / diluted shares | 2020 | 45,829 / 35,473 / 72,547,286 | ₹ lakh, shares | AR21 PDF p. 175 |
| OI candidate | 2020 | 38,953 | ₹ lakh | derived: AR21 PDF p. 175 |
| CFO / capex / Greenwich Associates payment / dividend paid / lease payment | 2020 | 50,047 / 3,492 / 25,117 / 23,203 / 6,791 | ₹ lakh | AR21 PDF p. 176–177 |
| Total assets / equity (726 + 130,455) | 2020 | 220,665 / 131,181 | ₹ lakh | AR21 PDF p. 174 |
| Goodwill / intangibles / IAUD / PP&E / ROU | 2020 | 37,586 / 13,656 / 1,357 / 4,102 / 20,908 | ₹ lakh | AR21 PDF p. 174 |
| Non-current investments / current investments | 2020 | 17,028 / 30,574 | ₹ lakh | AR21 PDF p. 174 |
| Cash / other bank balances | 2020 | 27,488 / 380 | ₹ lakh | AR21 PDF p. 174 |
| Trade payables (10 + 10,526) / tax liabilities | 2020 | 10,536 / 1,620 | ₹ lakh | AR21 PDF p. 174 |
| Revenue / other income | 2019 | 173,172 / 7,284 | ₹ lakh | AR19 PDF p. 142 |
| Employee / finance / D&A / other expenses | 2019 | 87,756 / 23 / 3,686 / 39,832 | ₹ lakh | AR19 PDF p. 142 |
| PBT / PAT / diluted shares | 2019 | 49,159 / 34,395 / 72,339,528 | ₹ lakh, shares | AR19 PDF p. 142 |
| OI candidate (pre-Ind AS 116: rent inside other expenses) | 2019 | 41,898 | ₹ lakh | derived: AR19 PDF p. 142 |
| CFO / capex / dividend on investments | 2019 | 44,586 / 2,906 / 777 | ₹ lakh | AR19 PDF p. 143 |
| Total assets / equity (723 + 116,469) | 2019 | 168,873 / 117,192 | ₹ lakh | AR19 PDF p. 141 |
| Goodwill / intangibles / IAUD / PP&E | 2019 | 28,861 / 2,515 / 1,180 / 3,512 | ₹ lakh | AR19 PDF p. 141 |
| Non-current investments / current investments | 2019 | 20,080 / 25,225 | ₹ lakh | AR19 PDF p. 141 |
| Cash / other bank balances / tax liabilities / borrowings (4 + 258) | 2019 | 34,169 / 389 / 1,530 / 262 | ₹ lakh | AR19 PDF p. 141 |
| Revenue / other income | 2018 | 174,849 / 7,341 | ₹ lakh | AR19 PDF p. 142 |
| Employee / finance / D&A / other expenses | 2018 | 88,736 / 223 / 4,282 / 38,990 | ₹ lakh | AR19 PDF p. 142 |
| PBT / PAT / diluted shares | 2018 | 49,959 / 36,310 / 72,148,415 | ₹ lakh, shares | AR19 PDF p. 142 |
| OI candidate | 2018 | 42,841 | ₹ lakh | derived: AR19 PDF p. 142 |
| CFO / capex / Pragmatix payment / dividend on investments | 2018 | 37,852 / 3,347 / 5,600 / 1,457 | ₹ lakh | AR19 PDF p. 143 |
| Total assets / equity (721 + 112,904) | 2018 | 163,376 / 113,625 | ₹ lakh | AR19 PDF p. 141 |
| Goodwill / intangibles / IAUD / PP&E | 2018 | 27,725 / 3,164 / 744 / 4,104 | ₹ lakh | AR19 PDF p. 141 |
| Non-current investments / current investments | 2018 | 29,359 / 18,303 | ₹ lakh | AR19 PDF p. 141 |
| Cash / other bank balances / tax liabilities / borrowings (8 + 246) | 2018 | 20,307 / 403 / 1,176 / 254 | ₹ lakh | AR19 PDF p. 141 |
| Revenue / other income | 2017 | 165,846 / 2,538 | ₹ lakh | AR17 PDF p. 152 |
| Employee / finance / D&A / other expenses | 2017 | 84,593 / 41 / 4,664 / 35,725 | ₹ lakh | AR17 PDF p. 152 |
| PBT / PAT / diluted shares | 2017 | 43,361 / 30,443 / 71,940,435 | ₹ lakh, shares | AR17 PDF p. 152 |
| OI candidate | 2017 | 40,864 | ₹ lakh | derived: AR17 PDF p. 152 |
| CFO / capex | 2017 | 28,671 / 3,387 | ₹ lakh | AR17 PDF p. 153 |
| Total assets / equity (717 + 104,140) | 2017 | 149,471 / 104,857 | ₹ lakh | AR17 PDF p. 151 |
| Goodwill / intangibles / IAUD / PP&E | 2017 | 23,203 / 708 / 1,321 / 5,435 | ₹ lakh | AR17 PDF p. 151 |
| Non-current investments / current investments | 2017 | 38,610 / 13,933 | ₹ lakh | AR17 PDF p. 151 |
| Cash / other bank balances / trade payables | 2017 | 8,469 / 4,709 / 5,671 | ₹ lakh | AR17 PDF p. 151 |
| Revenue / other income | 2016 | 154,751 / 4,967 | ₹ lakh | AR17 PDF p. 152 |
| Employee / finance / D&A / other expenses | 2016 | 78,774 / 0 / 5,452 / 31,644 | ₹ lakh | AR17 PDF p. 152 |
| PBT / PAT / diluted shares | 2016 | 43,848 / 29,433 / 72,026,251 | ₹ lakh, shares | AR17 PDF p. 152 |
| OI candidate | 2016 | 38,881 | ₹ lakh | derived: AR17 PDF p. 152 |
| CFO / capex | 2016 | 27,901 / 2,333 | ₹ lakh | AR17 PDF p. 153 |
| Total assets / equity (713 + 97,824) | 2016 | 138,524 / 98,537 | ₹ lakh | AR17 PDF p. 151 |
| Goodwill / intangibles / IAUD / PP&E | 2016 | 22,425 / 1,806 / 432 / 6,643 | ₹ lakh | AR17 PDF p. 151 |
| Non-current investments / current investments | 2016 | 3,557 / 42,952 | ₹ lakh | AR17 PDF p. 151 |
| Cash / other bank balances / trade payables | 2016 | 16,391 / 1,358 / 4,286 | ₹ lakh | AR17 PDF p. 151 |
| Total assets / equity (712 + 95,857) — Ind AS transition BS, 1 Jan 2016 | 2015 | 133,669 / 96,569 | ₹ lakh | AR17 PDF p. 151 (third column) |
| Goodwill / intangibles / IAUD / PP&E / CWIP | 2015 | 28,695 / 4,307 / 248 / 7,847 / 13 | ₹ lakh | AR17 PDF p. 151 |
| Non-current investments / current investments | 2015 | 3,039 / 39,091 | ₹ lakh | AR17 PDF p. 151 |
| Cash / other bank balances / trade payables | 2015 | 13,089 / 2,087 / 3,735 | ₹ lakh | AR17 PDF p. 151 |
| PriceMetrix total consideration (USD 32.9m), completed 7 Nov 2025 | 2025 | 29,397 | ₹ lakh | AR25 note 45.3 PDF p. 273 |
| PriceMetrix goodwill / customer relationships / information database / DTL / net liabilities | 2025 | 21,164 / 8,585 / 8,799 / 4,607 / 4,544 | ₹ lakh | AR25 note 45.3 PDF p. 273 |
| Group customer statement | 2025, 2024 | "None of the customers … constituted 10% or more of the total revenue of the Group" | text | AR25 note 39 (entity-wide disclosures) PDF p. 264 |
| Standalone customer statement | 2025, 2024 | "One customer … constituted 10% or more of the total revenue of the Company" | text | AR25 standalone note 39, ar25 text line ≈ 21,787 (PDF page to fix at resume) |
| Services rendered to S&P Global group entities (sum of note 40 "Professional services rendered" and "Subscription fees charged" lines) | 2025 | 47,593 | ₹ lakh | derived: AR25 note 40 PDF p. 264–266 (13.0% of revenue, derived) |
| Same | 2024 | 38,904 | ₹ lakh | derived: AR25 note 40 PDF p. 264–266 (11.9% of revenue, derived) |
| Of which Standard & Poor's Financial Services LLC | 2025 / 2024 | 25,347 / 19,370 | ₹ lakh | AR25 note 40 PDF p. 264 |
| Payments to S&P group: subscription fees to S&P Global Market Intelligence LLC; rent (Markit / Asia Index) | 2025 | 362; 288 | ₹ lakh | AR25 note 40 PDF p. 264–266 |
| Dividends paid to S&P India LLC / S&P Global Asian Holdings / S&P International LLC | 2025 | 18,414 / 6,799 / 3,540 | ₹ lakh | AR25 note 40 PDF p. 265 |
| KMP remuneration: short-term benefits / other long-term benefits | 2025 / 2024 | 1,283 / 578; 1,387 / 547 | ₹ lakh | AR25 note 40 PDF p. 267 (aggregate; per-person table owed) |
| Highest independent-director fee (Shyamala Gopinath, sitting fees and commission) | 2025 | 107 | ₹ lakh | AR25 note 40 PDF p. 267 |
| Contingent liabilities: disputed direct taxes / indirect taxes | 2025 | 77,979 / 1,295 | ₹ lakh | AR25 note 38 PDF p. 262 |
| ESOS outstanding at year-end | 2025 | 0 options | options | AR25 note 46 PDF p. 273–274 |

## 4. Readings settled (as far as the run got)

- **Record.** B1 record years FY2016–FY2025 (10y), balance sheets FY2015–FY2025 (11), all Ind AS consolidated; FY2015 is the Ind AS transition balance sheet at 1 Jan 2016. No shortfall label expected. Where a later AR restates (FY2024 in AR25; FY2023 in AR24), the restated figure is the one carried.
- **J1 OI.** The face statement has no operating subtotal. The OI candidate is revenue from operations − employee benefits − D&A − other expenses (= PBT − other income + finance costs, plus exceptional charges and less exceptional gains); all of other income leaves OI (J3; any foreign-exchange gain inside it is removed when positive, J13); FY2021's exceptional gain of 4,582 stays out. Finance costs are lease interest (IFRS 16 / Ind AS 116 from FY2020): they sit below OI, and in FCF the lease interest paid moves from financing into CFO. The segment note's "unallocable D&A" and "unallocable expenditure" are J1 charges to be allocated pro rata when the P29 weights are built, or the weights fall back to revenue (P29) if the resume cannot allocate them.
- **Lens.** STD expected (no banking or insurance licence; not tested in Appendix C form yet).
- **G6 / P31.** Classes found: CARE Ratings shares (quoted; S2 or S3 per note 9.1), and unquoted equity in NCDEX, CARICRA and Online PSB Loans (S3). FY2025 class carrying value 49,403 = 10.7% of total assets 463,194 (derived), FY2024 38,966 = 9.9% (derived): the carrying-value limb fails, so Gate 1A reads both G6 readings over the window. Income is dividends on investments (498 in FY2025; fair-value changes go through OCI). The pre-FY2024 composition of non-current investments (FY2017 38,610 jumps from FY2016 3,557) is not yet split between equity stakes (G6) and debt instruments or fixed-maturity funds (cash-like S1 at 0.9).
- **Leases.** Ind AS 116 from FY2020 (ROU first appears at 31 Dec 2020). FY2016–FY2019 are pre-adoption: the P18 test (undiscounted operating-lease commitments > 10% of total assets) is owed for each year.
- **P20 (orientation).** Total D&A exceeds capex in FY2016–FY2023 and FY2025 (e.g. FY2025 12,852 vs 7,340), so a constructed maintenance figure is likely capped at capex in most years (maintenance = all capex where the floor binds above capex). FY2024 capex 17,316 exceeds D&A 6,995 (office fit-out with the new leases): the constructed build decides that year. Deal years with acquired revenue: FY2018 (Pragmatix), FY2020 (Greenwich Associates), FY2025 (PriceMetrix, two months).
- **Acquisition stop (orientation).** PriceMetrix total consideration 29,397 against an EV near 3,30,000 at today's price (MCap 4,516.60 × ≈ 73.1m shares, derived) is about 0.9% of EV: below the 1% line on today's EV; the EV at the deal date is to be checked. No other deal above 1% of EV found in FY2023–FY2025. Greenwich Associates (FY2020, cash 25,117) is earlier-window: whether its CEO and CFO are still in office is to be checked against AR21's KMP list (AR25 note 40 lists Amish Mehta as MD & CEO and Dinesh Venkatasubramanian as CFO from 28 Oct 2024; Sanjay Chakravarti was CFO until then).
- **Repurchases.** Equity share capital rises every year FY2015–FY2025 (712 → 731, ESOS exercises); no buyback found in the window so far. To confirm by a text search of each AR for "buy-back".
- **Breadth (orientation, not a grade).** The group statement rules out a 10% customer by legal entity, but entities under common control count as one customer (§2·1B): services to S&P Global group entities sum to 13.0% of FY2025 revenue (11.9% FY2024), derived. S&P Global is the controller, so the concentration is in the Ratings unit (global analytical services), to be confirmed by the segment description and any unit split. R7 then requires either the three strong-moat conditions or a STRONG customer-power call for that unit.
- **SF (orientation).** S&P Global (≈ 66.6%) controls; the RPTs are mainly services sold to the controller's group (revenue), plus small subscription fees and rent paid to it. Management's own holdings and the per-person pay table are owed. Votes appear to equal economics (one share class).

## 5. Scope still owed (in the order the next run should take it)

- [ ] Re-open AR25 PDF p. 217–220 and note 39 (p. 262–264) for every governing figure before relying on it.
- [ ] Notes for NIBCL and cash in every year: AR25 notes 18, 26, 27 (other financial assets, other financial liabilities, other current liabilities: contract liabilities, employee payables); equivalents in AR24, AR23, AR21, AR19, AR17. Decide the NIBCL build (default vs narrow) and log it.
- [ ] Non-current and current investment notes for FY2015–FY2023 (AR17, AR19, AR21, AR23): split each year into G6 classes (CARE, NCDEX, CARICRA, Online PSB Loans, any other equity) and cash-like S1 (liquid and debt mutual funds, bonds, term deposits ≤ 12 months at 0.9 where not government/bank). Read AR25 note 9.1 (whether CARE is called strategic → S3, else S2 at Gate 2).
- [ ] FY2025 term deposits inside other current financial assets (note 18): amount and maturity (S1 cash if ≤ 12 months).
- [ ] P18 lease test FY2016–FY2019: operating-lease commitment notes in AR17 and AR19 (and AR16 for FY2016 if needed); capitalise if commitments > 10% of total assets.
- [ ] Lease liabilities FY2020–FY2021 (inside other financial liabilities in AR21: lease note).
- [ ] P20 build per year: k (net PP&E + CWIP + intangibles under development and capitalised software; acquired intangibles out), India CPI per calendar year (World Bank FP.CPI.TOTL.ZG), organic revenue in deal years (Pragmatix FY2018, Greenwich FY2020, PriceMetrix FY2025: acquired revenue disclosures), D&A split (PP&E, software, ROU, acquired intangibles) for the floor.
- [ ] B1–B3 on both G6 readings; P2–P6; J6 on each reading.
- [ ] B4: segment revenue, results and assets for FY2023–FY2025 (AR24 and AR23 note 39 for FY2023 and earlier on the same segmentation); P29 weights (segment results after allocating the unallocable D&A and expenditure where the note allows, else revenue weights).
- [ ] Allocation across the parts: earliest year the two-segment structure (Ratings; Research, Analytics and Solutions) is reported or restated (check AR21/AR23 segment notes), each unit's pooled latest-3-FY segment result ÷ segment assets against 10%, growth in segment assets.
- [ ] Appendix D, Ratings unit: share of revenue from S&P group entities (global analytical services) vs domestic ratings; R7 strong-moat test or STRONG customer-power call with containment; forces (regulatory registration, issuer-pay competition with the other domestic agencies, as the filings name them), moat, market.
- [ ] Appendix D, RAS unit: its parts as AR25's segment description and MD&A name them (global research and risk solutions, industry research, subscriptions to data, risk tools; Coalition Greenwich benchmarking, which PriceMetrix joins per AR25) with revenue sizes where printed; forces, moat, market; the J13 harsher-call rule where parts are unsized or within 10pp.
- [ ] Appendix E: per-person pay table FY2023–FY2025 (Board's report Annexure on managerial remuneration; MD & CEO Amish Mehta; CFOs), the P17 lines; directors' commission; management's shareholding (CG report) and the P23 call; shareholding pattern (S&P entities' %); RPT reading of the S&P services (pricing basis, shareholder approval of material RPTs in the AGM notice); dividends paid record; buy-back check.
- [ ] Gate 2: interim balance sheet at 30 Sep 2026 (Q3 2026 results, NSE/BSE filing, Oct 2026) for debt-equivalents (leases, gratuity), cash and STI; TTM OI test; diluted shares; MCap at px 4,516.60 (2026-10-30, NSI, INR); trigger band and averaged readings; P28 test if FY2025 is down (it is not on the OI candidate).

*Framework output, not investment advice.*
