# ATS.TO — ATS Corporation — INCOMPLETE evidence (ANALYSE 2026-10-30)

## 1. Header

- Key ATS.TO · job ANALYSE · D 2026-10-30 · T 2303 · base sha f56ec25020bb4787ecba0015429efff9d4a65a26 · model_version v4.8.0 · produced_by ROUTINE
- Prior memo: none. ISIN CA0019401052; no register row or memo matches the name or ISIN.
- Named gap: **data access — price endpoint HTTP 429.** query1.finance.yahoo.com/v8/finance/chart/ATS.TO returned "Edge: Too Many Requests" on every call, one per minute, from 22:05 UTC to 23:14 UTC (70 calls, default client). The cheapness leg needs `px` in the endpoint's unit (MODEL §7.1a; ANALYSE.md step 5). No verdict is recorded. Every gate input below is sourced and reusable at the retry; a retry needs one TSX close (CAD) and the cheapness leg.
- Other hosts: investors.atsautomation.com (Cloudflare challenge on every path); www.sedarplus.ca (bot-manager page); s201.q4cdn.com FY2017 and FY2024 statement paths 404 (FY2024 taken from SEC instead). The FY2016 balance sheet and FY2016 revenue were therefore not retrieved.

## 2. Item table (CAD thousands unless stated; FY ends 31 March)

Sources: FS{yy} = audited annual consolidated financial statements, s201.q4cdn.com/979379719/files/doc_financials/20{yy}/q4/Q4-FY{yy}-Financial-Statements-vFinal.pdf (FY26: doc_earnings/2026/q4/supplemental-info/Q4-26-Financial-Statements.pdf); 40-F24 = SEC 0001628280-24-023696 ats-20240331.htm; Q1-27 = SEC 6-K 0001394832-26-000023 ats-financialstatementsxfy.htm; MIC26 = SEC 6-K 0001394832-26-000020 exhibit a991noticeofmeetingandmicf.pdf.

| item | FY | value | unit | source |
|---|---|---|---|---|
| Revenue | 2017–2026 | 1,010,904 · 1,114,930 · 1,253,616 · 1,429,734 · 1,430,052 · 2,182,717 · 2,577,384 · 3,032,883 · 2,533,288 · 2,972,932 | CAD k | FS18, FS20, FS22, FS23, 40-F24, FS26, income statements |
| Earnings from operations (J1) | 2017–2026 | 71,935 · 85,462 · 114,795 · 95,613 · 119,609 · 186,611 · 222,489 · 315,391 · 9,256 · 198,780 | CAD k | same, income statements |
| Net income | 2017–2026 | 35,027 · 47,209 · 70,762 · 52,951 · 64,103 · 121,392 · 127,701 · 194,181 · −27,978 · 71,733 | CAD k | same, income statements |
| CFO | 2017–2026 | 127,900 · 59,686 · 127,598 · 20,347 · 185,159 · 216,163 · 127,800 · 20,780 · 25,771 · 448,383 | CAD k | same, cash-flow statements |
| Interest income | 2017–2026 | 656 · 1,923 · 5,108 · 2,065 · 1,621 · 508 · 1,961 · 1,979 · 6,049 · 956 | CAD k | net finance costs notes (FS18 n.20, FS20 n.23, FS22/FS23/FS26 n.24, 40-F24 n.24) |
| PP&E additions | 2017–2026 | 9,892 · 19,851 · 21,096 · 45,448 · 21,541 · 36,309 · 56,104 · 58,830 · 33,952 · 33,642 | CAD k | cash-flow statements |
| Intangible additions | 2017–2026 | 8,006 · 6,124 · 19,824 · 11,119 · 10,031 · 16,957 · 24,192 · 29,628 · 44,078 · 43,134 | CAD k | cash-flow statements |
| PP&E depreciation | 2017–2026 | 10,492 · 10,352 · 12,137 · 14,675 · 14,820 · 20,917 · 25,590 · 28,455 · 33,674 · 34,470 | CAD k | cash-flow statements |
| Amortisation, development + software/licences | 2017–2026 | 4,103 · 5,749 · 7,615 · 11,581 · 6,500 · 23,147 · 18,334 · 18,857 · 20,566 · 27,558 | CAD k | intangible-assets notes (FS18 n.10; FS20, FS22, FS23, 40-F24, FS26 n.12) |
| Net PP&E | 2017–2026 | 69,233 · 85,102 · 97,669 · 136,284 · 180,296 · 222,123 · 263,119 · 296,977 · 325,048 · 259,791 | CAD k | balance sheets |
| Net development + software/licences | 2017–2026 | 21,591 · 23,202 · 29,011 · 28,893 · 37,942 · 46,297 · 61,278 · 77,893 · 110,843 · 128,513 | CAD k | intangible-assets notes |
| Acquired revenue (in-year, IFRS 3 B64(q)) | 2019–2025 | FY19 Comecer 8,669 (KMW undisclosed) · FY20 iXLOG 4,023 + IAP 2,061 + MARCO 5,492 · FY21 Inimco 1,150 (CFT undisclosed) · FY22 SP 75,153 + NCC 21,997 + BioDot 51,661 (BLSG, CIM, DF, HSG undisclosed) · FY24 Avidity 38,615 (others undisclosed); FY23 and FY25 deals undisclosed; FY18 and FY26 no deals | CAD k | acquisitions notes (n.5) |
| Business acquisitions, net cash | 2019–2025 | 156,351 · 53,367 · 68,523 · 745,018 · 51,679 · 276,538 · 179,389 | CAD k | cash-flow statements |
| Diluted weighted shares | 2017–2026 | 92.807109 · 94.035200 · 94.050845 · 92.461236 · 92.367244 · 92.627450 · 92.241973 · 98.575316 · 97.975703 · 98.140188 | m | EPS notes |
| Total assets | 2017–2026 | 1,374,570 · 1,542,219 · 1,688,843 · 2,097,973 · 2,201,752 · 3,069,397 · 3,543,793 · 4,088,799 · 4,621,872 · 4,340,030 | CAD k | balance sheets (FY2021 re-presented, FS22) |
| AP & accrued | 2017–2026 | 183,839 · 246,384 · 254,227 · 289,313 · 368,901 · 501,465 · 647,629 · 604,488 · 665,109 · 622,436 | CAD k | balance sheets |
| Income tax payable | 2017–2026 | — · — · 7,721 · 3,084 · 30,998 · 48,617 · 38,904 · 44,732 · 40,073 · 34,123 | CAD k | balance sheets |
| Contract liabilities (FY17–18 billings in excess) | 2017–2026 | 96,490 · 95,912 · 161,139 · 117,757 · 218,290 · 248,329 · 296,555 · 312,204 · 330,134 · 307,306 | CAD k | balance sheets |
| Cash | 2017–2026 | 286,697 · 330,148 · 224,540 · 358,645 · 187,467 · 135,282 · 159,867 · 170,177 · 225,947 · 284,957 | CAD k | balance sheets |
| Total liabilities | 2017–2026 | 688,561 · 783,446 · 899,212 · 1,228,960 · 1,291,392 · 2,083,714 · 2,413,210 · 2,404,852 · 2,912,515 · 2,560,572 | CAD k | balance sheets |
| Equity attributable | 2017–2026 | 685,761 · 758,481 · 789,320 · 868,225 · 895,264 · 981,596 · 1,126,848 · 1,680,666 · 1,705,777 · 1,777,757 | CAD k | balance sheets |
| Goodwill + intangibles | 2017–2026 | 579,319 · 608,028 · 765,588 · 828,412 · 949,240 · 1,592,970 · 1,711,472 · 1,908,147 · 2,153,107 · 2,103,463 | CAD k | balance sheets |
| Lease commitments (pre-IFRS 16) | 2018, 2019 | 33,604 (five-year table) · 42,878 | CAD k | FS18 commitments note; FS20 n.3 transition |
| Q1 FY2027 (to 28 Jun 2026) / Q1 FY2026 | Q1 | revenue 693,721 / 736,720; OI 24,214 / 57,783; CFO −10,348 / 155,782; capex 15,611 / 16,334; interest income 497 / 136 | CAD k | Q1-27 |
| BS 28 Jun 2026 | Q1 | cash 198,933; bank 850; current debt 175; LTD 1,234,465; leases 36,891 + 118,391; employee benefits 26,023; other LT liabilities 21,990 (hedging derivatives); NCI 1,764; equity attributable 1,801,022; goodwill 1,414,437; intangibles 692,257; assets held for sale 61,415; diluted weighted shares 98.429582m | CAD k | Q1-27 |
| Note fees deferred (bound on principal − carrying) | Q1 | 8,100 (US$350m notes) + 9,604 (CAD 600m notes) | CAD k | Q1-27, long-term debt note |
| CPI Canada, fiscal-year average | 2017–2026 | 1.52 · 1.63 · 2.15 · 2.00 · 0.63 · 4.50 · 6.61 · 3.31 · 2.24 · 2.04 | % | Statistics Canada vector v41690973 (WDS) |
| Segments | 2026 | one operating segment, Automation Systems | text | FS26 n.21 |
| Customer statement | 2026 | no single customer ≥ 10% of revenue (FY2026, FY2025) | text | FS26 n.21 |
| Revenue by market | 2026 | Life Sciences 1,521,973; Consumer Products 553,002; Food & Beverage 498,749; Energy 226,658; Transportation 172,550 | CAD k | FS26 n.22 |
| Revenue by type / geography | 2026 | construction contracts 1,602,013; services 723,879; goods 647,040 · US 1,273,047; Canada 196,407; Germany 283,385; Italy 108,318; Other Europe 628,691; Other 483,084 | CAD k | FS26 n.21–22 |
| EV-customer settlement | 2025 | 171,090 before tax (revenue −146,900; SG&A 24,190) | CAD k | FS26 n.22 |
| Summary Compensation Table | 2024–2026 | Wright FY26 19,140,500 (700,000 PSOs 9,815,800; share awards 8,639,800); Hider 10,787,000 / 11,370,400 / 9,734,300; McLeod 2,467,600 / 2,394,400 / 3,369,000; Kafedzhiev — / 1,959,900 / 2,546,600 | CAD | MIC26 p. 50 |
| Mason Capital advisory agreement | 2014–2026 | US$500,000 a year for strategic and capital-markets advisory services; principal M. Martino is a director and chair; terminated 31 Mar 2026 | USD | MIC26 pp. 23, 60 |
| Holdings | 2026 | Wright 25,700 shares; Mason Capital (funds) 16,404,170 = 16.72%; 98,125,081 shares outstanding at 22 Jun 2026 | shares | MIC26 pp. 7, director table |
| Highest outside director | 2026 | McAusland 472,550 | CAD | MIC26 director compensation table |
| Repurchases | 2019–2026 | FY19 2,509,120 / 39,279; FY20 301,386 / 4,785; FY21 511,528 / 8,662; FY23 619,695 / 21,071; FY25 1,020,887 / 44,986 (1 Apr–3 May 2024); FY26 308,758 / 10,000; NCIB to 21 Dec 2026, up to 8,225,621 shares at prevalent market prices | shares / CAD k | share-capital notes (FS20, FS22, FS23, 40-F24 n.17; FS26 n.17) |

## 3. Readings settled (figures above; no grade or verdict)

- Not a group (one operating segment). Lens STD (no bank, insurer or finance arm). No G6 classes. P18: no capitalisation (FY2018–FY2019 commitments 2.2–2.5% of total assets).
- NIBCL = AP & accrued + income tax payable + contract liabilities; provisions stay in CE.
- P20: k = 0.128 (Σ net PP&E + net development/software ÷ Σ revenue, FY2017–FY2026); π = 3% in every constructed year. Constructed FY2018 (maintenance 16,541), FY2020 (40,318), FY2026 (62,028, floor binds); all capex FY2017 (FY2016 revenue not retrieved) and FY2019, FY2021–FY2025 (deals above 1% of EV with acquired revenue undisclosed); TTM all capex (no amortisation split in the interim).
- Maintenance FCF (CFO − interest income − maintenance capex) FY2017–FY2026: 109,346 · 41,222 · 81,570 · −22,036 · 151,966 · 162,389 · 45,543 · −69,657 · −58,308 · 385,399; 3y avg 85,811, 5y 93,073. OI 3y 174,476, 5y 186,505.
- Worst-of-four ROCE: latest 5 FYs 6.2%, P1 window 6.5% (beginning-of-period variants FY2018–FY2026). FCFROCE (maintenance) 3.1% / 3.8%; all-capex 3.0% / 3.6%. ΔOI/sh endpoint 9.0% (geometric 11.3%); ΔFCF/sh (i) n.m., (ii) 0.8%; ΔBV/sh 10.5% / 12.0%; TBV negative from FY2021. L/E FY2026 144%. J6: no limb fires (FCFROCE limb (b) 2.55% vs threshold 2.53%).
- TTM Q1-2027: OI 165,211 (below FY2026, governs); FCF 204,883 (= all capex; below FY2026, governs). Debt-equivalents 1,436,263 (incl. the 17,704 fee bound); EV/OI no-cash and all-cash legs negative at any price; FCF leg CAD 16.65; OI restoring the no-cash bound 205,180.
- P17: FY2026 Wright 19.14m vs NI 71,733 (26.7%) and trailing NI 79,312 (24.1%); FY2025 loss-year limb (trailing maintenance FCF −27,470; total up on FY2024). P27: Mason fee ≈ CAD 696k at the circular's FY2026 rate 1.391 vs 0.5% × 71,733 = 359. FY2025 repurchase (1.04% of diluted shares) at point-in-time MCap/FCF 36.2 on FY2021–FY2023 averages; FY2019 (2.67%) 19.6.
- Acquisition stop: FY2024 (276,538) and FY2025 (179,389) deals above 1% of EV with contributions largely not printed; Avidity's printed post-acquisition result a net loss.

## 4. Scope still owed

- [ ] One price-endpoint GET for ATS.TO (close, currency, exchangeName, instrument name).
- [ ] Gate 2 at px: MCap/FCF, EV/OI both variants, the 3-year and 5-year readings, MCap/BV (MCap/TBV n.m.); the live-repurchase test (current price against worth).
- [ ] Re-open FS26 and Q1-27 for the governing figures, then write the memo from the record above.
