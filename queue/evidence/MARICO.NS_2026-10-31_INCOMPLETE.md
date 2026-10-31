# MARICO.NS — Marico Limited — INCOMPLETE evidence (ANALYSE 2026-10-31)

Resumable record (README §5, v4.8.0). No grade, no verdict. Every figure in the item table carries its primary document and its place in it, so the next run can carry it under README §5 Resume (re-opening the source for every governing figure).

## 1. Header

- Key MARICO.NS · job ANALYSE · D 2026-10-31 · T 0827 · base sha 0fca109f81a12f390ca048454e351c5eb257e231 · model_version v4.8.0 · produced_by ROUTINE
- Prior memo: none. Name ("Marico") and ISIN INE196A01026 (AR26) grep over `memos/`, `archive/memos/`, `register.csv` and `_REGISTER.md`: no match. Prior memo `model_version`: none.
- **Named gap: group build exceeds budget** (first overrun; the `[ ]` DRAFT_QUEUE line carries no ` — partial …` note at the base). Marico is a group: two material reportable segments (India, International) and one material controlled listed subsidiary, Marico Bangladesh Limited (90%, Dhaka and Chittagong stock exchanges; FY2026 turnover INR 1,502 crore = 11.0% of group revenue). The P1 record was being assembled from eight annual reports when the time budget ran out; B1–B4, the P20 build, the G6/P31 test, Appendices D–F and the allocation-across-the-parts table are not built.
- Resumes: none (first record of this key).

## 2. Documents (primary, retrieved 2026-10-31)

All Marico annual reports are served by `marico.com/investorspdf/{file}.pdf` (index: POST `marico.com/api/getData` with `{"country":"global","link":"/investors/documentation/annual-reports"}`; Bangladesh: `"country":"bangladesh"`). BSE copies `bseindia.com/bseplus/AnnualReport/531642/53164203{YY}.pdf` exist for FY2016–FY2020 only (FY2021+: 404) and the FY2020 BSE copy has broken font encoding (numbers missing), so use the marico.com copies.

| id | document | URL |
|---|---|---|
| AR26 | Integrated Annual Report 2025-26 (auditor B S R & Co. LLP, statements dated 5 May 2026) | marico.com/investorspdf/Marico_Annual_Report_FY26.pdf |
| AR25 | Annual Report 2024-25 | marico.com/investorspdf/Marico_Annual_Report_FY25.pdf |
| AR24 | Annual Report 2023-24 | marico.com/investorspdf/Marico_Annual_Report_FY24.pdf |
| AR23 | Annual Report 2022-23 (not yet read) | marico.com/investorspdf/Marico_Annual_Report_FY23.pdf |
| AR22 | Annual Report 2021-22 | marico.com/investorspdf/Marico_Annual_Report_FY22.pdf |
| AR21 | Annual Report 2020-21 | marico.com/investorspdf/annual-report-fy-2020-21.pdf |
| AR19 | Integrated Report 2018-19 (P&L and cash-flow figures do not extract with pdftotext; read the PDF pages) | marico.com/investorspdf/Marico_IR_2018-19_for_web_upload.pdf |
| AR17 | Annual Report 2016-17 (first Ind AS year; FY2016 and 1 Apr 2015 comparatives) | marico.com/investorspdf/Annual_Report_2017.pdf |
| AR20, AR18 | Annual Reports 2019-20 and 2017-18 (BSE copies; AR20 text layer broken) | bseindia.com/bseplus/AnnualReport/531642/5316420320.pdf, …0318.pdf |
| MBL26 | Marico Bangladesh Limited Annual Report 2025-26 | marico.com/investorspdf/Annual_Report_2025-26.pdf |
| PX | Price endpoint `query1.finance.yahoo.com/v8/finance/chart/MARICO.NS`: currency INR, exchangeName NSI, instrument "Marico Limited"; closes 2026-10-27 776.15, 2026-10-28 769.65, 2026-10-29 802.90; regularMarketPrice 800.0 (2026-10-30 session; the 10-30 daily bar was null at fetch) | — |
| FX | Endpoint closes 2026-10-30: USDINR=X 95.1524, USDBDT=X 120.2915 → INR 0.7910 per BDT (endpoint FX; ECB has no BDT rate) | — |

## 3. Item table (INR crore unless stated; FY ends 31 March; consolidated, Ind AS)

Locations "AR26 BS/PL/CF" = the consolidated balance sheet, statement of profit and loss and statement of cash flows (AR26 pp. 377–382); comparatives taken from the later report as printed there.

| item | FY | value | unit | source |
|---|---|---|---|---|
| Revenue from operations | FY2026 / FY2025 | 13,611 / 10,831 | INR crore | AR26 PL |
| Other income | FY2026 / FY2025 | 204 / 208 | INR crore | AR26 PL, note 20 |
| Finance costs | FY2026 / FY2025 | 53 / 53 | INR crore | AR26 PL, note 25 |
| Depreciation and amortisation | FY2026 / FY2025 | 202 / 178 | INR crore | AR26 PL, note 23 |
| Profit before tax (no exceptional items) | FY2026 / FY2025 | 2,277 / 2,116 | INR crore | AR26 PL |
| Profit attributable to owners / to NCI | FY2026 / FY2025 | 1,762 / 51 ; 1,629 / 29 | INR crore | AR26 PL |
| Diluted EPS | FY2026 / FY2025 | 13.59 / 12.56 | INR | AR26 PL, note 36 |
| CFO (after tax) | FY2026 / FY2025 | 2,084 / 1,363 | INR crore | AR26 CF |
| Capex (payment for PP&E and intangibles) | FY2026 / FY2025 | 319 / 161 | INR crore | AR26 CF |
| Acquisition of subsidiary net of cash (Plix, note 41) / acquisition of NCI | FY2026 | 452 / 221 | INR crore | AR26 CF |
| Interest paid on borrowings / on leases (financing) | FY2026 / FY2025 | 37 / 16 ; 51 / 14 | INR crore | AR26 CF |
| Dividends paid to owners / to NCI | FY2026 / FY2025 | 908 / 81 ; 453 / 47 | INR crore | AR26 CF |
| Interest received (investing) | FY2026 / FY2025 | 24 / 70 | INR crore | AR26 CF |
| Total assets | FY2026 / FY2025 | 10,075 / 8,332 | INR crore | AR26 BS |
| Goodwill / other intangibles | FY2026 / FY2025 | 1,036 / 1,498 ; 857 / 946 | INR crore | AR26 BS, note 5 |
| Current investments / non-current investments | FY2026 / FY2025 | 1,948 / 135 ; 1,375 / 215 | INR crore | AR26 BS, note 6(a) |
| Cash and equivalents / other bank balances | FY2026 / FY2025 | 404 / 89 ; 321 / 456 | INR crore | AR26 BS, notes 6(d), 6(e) |
| Borrowings current / non-current | FY2026 / FY2025 | 355 / 0 ; 379 / – | INR crore | AR26 BS, note 13(a) |
| Lease liabilities current / non-current | FY2026 / FY2025 | 75 / 127 ; 51 / 124 | INR crore | AR26 BS |
| Other financial liabilities current / non-current (acquisition put and deferred-consideration liabilities among them: composition owed, note 13(b)) | FY2026 / FY2025 | 1,585 / 947 ; 288 / 1,211 | INR crore | AR26 BS, note 13(b) |
| Trade payables (MSE + other) | FY2026 / FY2025 | 146 + 1,488 ; 89 + 1,217 | INR crore | AR26 BS, note 13(c) |
| Other current liabilities / current tax liabilities | FY2026 / FY2025 | 221 / 76 ; 232 / 92 | INR crore | AR26 BS, notes 18, 17 |
| Employee benefit obligations current / non-current | FY2026 / FY2025 | 146 / 31 ; 92 / 27 | INR crore | AR26 BS, note 15 |
| Deferred tax liabilities | FY2026 / FY2025 | 374 / 248 | INR crore | AR26 BS, note 16 |
| Total liabilities | FY2026 / FY2025 | 5,581 / 4,066 | INR crore | AR26 BS |
| Equity attributable to owners / NCI | FY2026 / FY2025 | 4,210 / 284 ; 3,975 / 291 | INR crore | AR26 BS |
| Segment revenue India / International | FY2026 / FY2025 | 10,348 / 3,263 ; 8,110 / 2,721 | INR crore | AR26 note 30(ii) |
| Revenue by customer location: India / Bangladesh / Vietnam / Others | FY2026 / FY2025 | 10,348 / 1,474 / 653 / 1,136 ; 8,110 / 1,065 / 441 / 1,215 | INR crore | AR26 note 30 |
| Revenue by product: edible oils / hair oils / personal care / others | FY2026 / FY2025 | 7,049 / 2,624 / 2,020 / 1,918 ; 5,494 / 2,115 / 1,886 / 1,336 | INR crore | AR26 note 30 |
| Customer statement | FY2026 | "The Group does not have revenue more than 10% of total revenue from single customer." | text | AR26 note 30 |
| Marico Bangladesh Ltd: turnover / PBT / PAT / total assets (INR at 0.770) | FY2026 | 1,502 / 551 / 471 / 643 | INR crore | AR26 Form AOC-1, Part A, row 1 |
| Revenue from operations; PBT; owners' NI | FY2024 / FY2023 | 9,653 / 9,764 ; 1,937 / 1,743 ; 1,481 / 1,302 | INR crore | AR24 PL |
| Other income; finance costs; D&A | FY2024 / FY2023 | 142 / 144 ; 73 / 56 ; 158 / 155 | INR crore | AR24 PL |
| Diluted EPS | FY2024 / FY2023 | 11.43 / 10.05 | INR | AR24 PL |
| CFO; capex; acquisitions net of cash; acquisition of NCI | FY2024 / FY2023 | 1,436 / 1,419 ; 153 / 182 ; 103 / 277 ; 141 / – | INR crore | AR24 CF |
| Interest paid / lease interest; dividends to owners | FY2024 / FY2023 | 54 / 11 ; 42 / 11 ; 1,229 / 582 | INR crore | AR24 CF |
| Total assets; total liabilities; owners' equity; NCI | FY2024 / FY2023 | 7,421 / 6,946 ; 3,252 / 2,990 ; 3,832 / 3,799 ; 337 / 157 | INR crore | AR24 BS |
| Goodwill / other intangibles | FY2024 / FY2023 | 863 / 937 ; 862 / 560 | INR crore | AR24 BS |
| Investments current / non-current; cash; other bank balances | FY2024 / FY2023 | 259 / 343 ; 578 / 518 ; 228 / 207 ; 715 / 549 | INR crore | AR24 BS |
| Borrowings current / non-current; leases current / non-current | FY2024 / FY2023 | 383 / – ; 473 / 2 ; 41 / 104 ; 42 / 91 | INR crore | AR24 BS |
| Other financial liabilities non-current / current | FY2024 / FY2023 | 405 / 59 ; 266 / 40 | INR crore | AR24 BS |
| Trade payables (MSE + other); other current liab.; current tax liab. | FY2024 / FY2023 | 71 + 1,510 ; 68 + 1,384 ; 211 / 217 ; 83 / 87 | INR crore | AR24 BS |
| Revenue; other income; finance costs; D&A; PBT; owners' NI; diluted EPS | FY2022 / FY2021 | 9,512 / 8,048 ; 98 / 94 ; 39 / 34 ; 139 / 139 ; 1,601 / 1,523 ; 1,225 / 1,172 ; 9.49 / 9.08 | INR crore (EPS INR) | AR22 PL |
| Exceptional items; share of equity-method JV result | FY2022 / FY2021 | – / +13 ; – / −2 | INR crore | AR22 PL (note 39) |
| Total assets; total liabilities; owners' equity; NCI | FY2022 / FY2021 | 5,786 / 5,510 ; 2,381 / 2,252 ; 3,348 / 3,240 ; 57 / 18 | INR crore | AR22 BS |
| Goodwill / other intangibles; investments NC / current; cash; other bank | FY2022 / FY2021 | 654 / 306 ; 613 / 230 ; 187 / 641 ; 226 / 628 ; 276 / 109 ; 303 / 835 | INR crore | AR22 BS |
| Borrowings current; leases NC / current; other fin. liab. current | FY2022 / FY2021 | 345 / 340 ; 91 / 43 ; 122 / 38 ; 45 / 44 | INR crore | AR22 BS |
| Trade payables (MSE + other); other current liab.; current tax liab. | FY2022 / FY2021 | 76 + 1,268 ; 50 + 1,084 ; 224 / 287 ; 67 / 72 | INR crore | AR22 BS |
| Capex; acquisitions; interest paid / lease interest; dividends to owners | FY2022 / FY2021 | 132 / 142 ; 55 / 132 ; 28 / 11 ; 21 / 13 ; 1,195 / 968 | INR crore | AR22 CF |
| CFO | FY2021 / FY2020 | 2,068 / 1,214 | INR crore | AR21 CF |
| Capex; interest paid / lease interest | FY2021 / FY2020 | 142 / 188 ; 21 / 13 ; 34 / 16 | INR crore | AR21 CF |
| Revenue; PBT; diluted EPS | FY2021 / FY2020 | 8,048 / 7,315 ; 1,523 / 1,374 ; 9.08 / 7.91 | INR crore (EPS INR) | AR21 PL |
| Total assets; total liabilities; owners' equity; NCI; goodwill / intangibles | FY2021 / FY2020 | 5,510 / 4,970 ; 2,252 / 1,934 ; 3,240 / 3,023 ; 18 / 13 ; 613 / 538 ; 230 / 41 | INR crore | AR21 BS |
| Finance costs | FY2021 / FY2020 | 34 / 50 | INR crore | AR21 CF |
| CFO; payment for PP&E | FY2019 / FY2018 | 1,018 / 516 ; 162 / 127 | INR crore | AR19 CF |
| Total assets; total liabilities; owners' equity | FY2019 / FY2018 | 4,742 / 4,081 ; 1,732 / 1,526 ; 2,999 / 2,543 | INR crore | AR19 BS |
| Revenue; other income; finance costs; PBT; NCI share; diluted EPS | FY2017 / FY2016 | 5,935.92 / 6,024.45 ; 97.31 / 93.33 ; 16.58 / 20.62 ; 1,148.70 / 1,028.70 ; 12.38 / 11.85 ; 6.20 / 5.53 | INR crore (EPS INR) | AR17 PL |
| CFO; payment for PP&E | FY2017 / FY2016 | 611.57 / 817.62 ; 87.09 / 100.74 | INR crore | AR17 CF |
| Total assets; total liabilities; owners' equity; NCI | FY2017 / FY2016 / 1 Apr 2015 | 3,599.52 / 3,381.17 / 3,126.50 ; 1,260.50 / 1,349.49 / 1,312.39 ; 2,325.68 / 2,017.37 / 1,800.46 ; 13.34 / 14.31 / 13.65 | INR crore | AR17 BS |
| Goodwill / other intangibles | FY2017 / FY2016 / 1 Apr 2015 | 479.45 / 497.36 / 489.15 ; 28.08 / 28.73 / 30.10 | INR crore | AR17 BS |
| MBL shares outstanding; free float | FY2026 | 31,500,000; 10% | shares | MBL26, "MBL Share: Brief Overview" |
| MBL year-end price / year high / year low (DSE) | FY2026 | 2,731.80 / 3,000.00 / 2,230.90 | BDT | MBL26, share-performance table |
| MBL year-end market capitalisation (DSE) | FY2022–FY2026 | 7,419 / 7,628 / 7,701 / 7,673 / 8,605 | BDT crore | MBL26, share-performance table |
| MBL EPS / dividend per share | FY2026 | 206.09 / 207.50 | BDT | MBL26, share-performance table |

Derived (labelled): all-capex FCF = CFO − interest paid (borrowings and leases, moved from financing) − capex: FY2026 2,084 − 37 − 16 − 319 = 1,712; FY2025 1,363 − 51 − 14 − 161 = 1,137; FY2024 1,436 − 54 − 11 − 153 = 1,218; FY2023 1,419 − 42 − 11 − 182 = 1,184 (derived: items above). P22: Bangladesh 1,474 ÷ 13,611 = 10.8% of FY2026 revenue (customer location); MBL turnover 1,502 ÷ 13,611 = 11.0% (AOC-1); International 3,263 ÷ 13,611 = 24.0%. MBL minority at the harsh market bound: 10% × 31.5m × BDT 3,000 (FY2026 high) × 0.7910 = INR 747 crore against book NCI 284 crore (group NCI, all subsidiaries).

## 4. Readings settled (as far as the run got; no grade, no verdict)

- **Group.** Two material reportable segments (India 76% and International 24% of FY2026 revenue; AR26 note 30) and one material controlled listed subsidiary, Marico Bangladesh Limited (90%; 11.0% of group revenue, AOC-1). Other listed parts: none found (all other subsidiaries unlisted, AR26 note 31).
- **MBL is ungradeable.** Its venue (Dhaka/Chittagong) is not served by the price endpoint (`MARICO.DS`, `MARICO.DH`: no data), so it counts WEAK with its weight in the Future, its SF is INDETERMINATE (b) for the parent, and no `## Group dependency` line is written (an unserved venue is not listed for queuing). Its NCI enters EV at the higher of market and book; the px_date DSE close was not retrievable (dsebd.org old pages retired, HTTP 410; cse.com.bd TLS chain failure / HTTP 503), so the run took the harsh bound at the FY2026 high of BDT 3,000 (re-read at the next run if a dated close can be fetched). P29 weight base needs MBL's own J1 OI from MBL26 (its statement of profit or loss), with the International segment reduced by it.
- **Lens.** STD: a branded consumer-goods maker; no banking or insurance licence; no finance arm.
- **Gate 0 (draft, not settled):** Marico, a Mumbai-based company founded in 1990 and controlled by the Mariwala family, makes and sells branded coconut and value-added hair oils (Parachute, Nihar), refined edible oils (Saffola), foods, and skin, hair and male-grooming products (Livon, Set Wet, Beardo, Plix and other digital brands), mainly to Indian consumers through distributors, wholesalers, retailers, modern trade and e-commerce, and abroad in Bangladesh, Vietnam, the Middle East and Africa, chiefly through its listed Bangladeshi subsidiary.
- **J1 OI.** No operating subtotal on the face; segment results (note 30, not yet read) are the other candidate. With no subtotal, OI = PBT − other income + finance costs only where other income is wholly financial (note 20 to read; FY2026 fair-value gains 153 and interest 14 in the CF adjustments). FY2021 exceptional item +13 is a gain (leaves); FY2021 equity-method share −2 (JV; G6 class, below the line on its size).
- **Acquisition stop live.** BV ≫ TBV (FY2026 goodwill + intangibles 2,534 against owners' equity 4,210); deals in window: FY2023 acquisitions 277 (True Elements; Beardo step-up), FY2024 103 + NCI 141, FY2026 Plix 452 + NCI 221, with put/deferred-consideration liabilities in other financial liabilities (FY2026 non-current 947, current 1,585). Each year's aggregate against 1% of EV (MCap ≈ INR 1.03 lakh crore at INR 800) is owed.

## 5. Scope still owed (next run, in this order)

- [ ] Re-open the governing figures above (AR26, AR24, AR22, AR21, AR19, AR17) and complete B1 for FY2016–FY2026: revenue, J1 OI (read note 20 other income and the note 30 segment results for the J1 candidates), CFO, capex, interest paid, D&A of PP&E and capitalised software, diluted shares, NIBCL, cash + STI, total liabilities, BV, goodwill + intangibles. Missing so far: FY2018–FY2020 P&L lines (AR19 and AR21; AR19's P&L does not extract with pdftotext, read the PDF pages 12389–12460 region or the AR20 marico.com copy `Annual-Report-FY-2019-20.pdf`), FY2022 CFO (AR22 CF), FY2018 and FY2020 balance-sheet detail, AR23 (FY2023 as first printed), AR18 (FY2017–FY2018).
- [ ] Note 13(b) composition (AR24–AR26): acquisition put/call and deferred-consideration liabilities (debt-equivalents at carrying fair value, maximum payable logged); MBL NCI market value at px_date (DSE or CSE close).
- [ ] P20 build (home CPI for India; organic growth disclosures in the MD&A: Marico prints India volume growth each year), G6/P31 test (JV/associate carrying values; Zed Lifestyle before control), lease P18 test for FY2016–FY2019.
- [ ] B4: India and International segment revenue, results and assets for FY2024–FY2026 (AR26 note 30(iii)–(iv)); MBL J1 OI from MBL26 for the P29 weight; Appendix D blocks for India, International ex-MBL, and MBL as ungradeable.
- [ ] Appendix E: managerial remuneration tables (Saugata Gupta, MD & CEO; Harsh Mariwala, Chairman) FY2024–FY2026 on every basis (paid incl. ESOP/STAR perquisites; Board's report Annexure on remuneration and Form MGT-7), director commissions, promoter holdings (alignment; Mariwala family trusts — disclaimed or not), WEOMA trust purchases (sterilisation), acquisition worksheet (Beardo, Just Herbs, True Elements, Plix: pre-deal figures and put liabilities), allocation-across-the-parts table on note 30 segment assets.
- [ ] Appendix F at px INR 800.0 (or the run's own close) with N = diluted shares (AR26 EPS note 36), both EV variants, averaged readings.

*Framework output, not investment advice.*
