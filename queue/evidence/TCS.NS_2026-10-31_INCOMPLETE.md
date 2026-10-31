# TCS.NS — Tata Consultancy Services Limited — INCOMPLETE evidence (ANALYSE 2026-10-31)

Resumable record (README §5, v4.8.0). No grade, no verdict.

## 1. Header

- Key TCS.NS · job ANALYSE · D 2026-10-31 · T 0627 · base sha 03ee15de2b97fac63ca73a3291478831b2a2f23b · model_version v4.8.0 · produced_by ROUTINE
- Prior memo: none (name and ISIN grep over `memos/`, `archive/memos/`, `register.csv` and `_REGISTER.md`: no match). Prior memo `model_version`: none.
- ISIN: INE467B01029 (AR26, shareholder information section).
- Named gap: **group build exceeds budget** (first overrun). TCS reports six reportable segments (industry verticals), every one material under P22 (revenue or Σ positive segment results ≥ 10% at FY2026), so the run is a group build: B4 with weights and S, six Appendix D blocks, and the allocation-across-the-parts table, on top of an eleven-balance-sheet P1 record. The ten annual reports were retrieved (below), but the full build could not be finished inside the routine time budget.
- Resumes: none (first record of this key).

## 2. Documents (primary, retrieved 2026-10-31; tcs.com returns HTTP 403 to the sandbox, so the BSE copies were used)

| id | document | URL |
|---|---|---|
| PX | price endpoint | query1.finance.yahoo.com/v8/finance/chart/TCS.NS (exchangeName NSI, currency INR, longName "Tata Consultancy Services Limited", instrumentType EQUITY; no split events in range) |
| AR26 | Integrated Annual Report 2025-26 (FY2026; statements approved 9 Apr 2026) | bseindia.com/xml-data/corpfiling/AttachHis/ad42e748-d73c-4c79-8c52-bcf1b1399bc1.pdf |
| AR25 | Integrated Annual Report 2024-25 | bseindia.com/xml-data/corpfiling/AttachHis/bb9f9e0a-e4ce-4a4e-997e-0b5de8c2bec0.pdf |
| AR24 | Integrated Annual Report 2023-24 (retrieved, not yet read) | bseindia.com/xml-data/corpfiling/AttachHis/d57e49b6-fd89-4fa8-b591-4f590100db1e.pdf |
| AR23 | Integrated Annual Report 2022-23 (filing letter 9 Jun 2023) | bseindia.com/xml-data/corpfiling/AttachHis/085896fa-2e3b-4ecc-b9f1-31a31b7204b5.pdf |
| AR22 | Integrated Annual Report 2021-22 (filing letter 18 May 2022; retrieved, not yet read) | bseindia.com/xml-data/corpfiling/AttachHis/33b4133d-7690-410b-b0ab-2c3994c8eeb3.pdf |
| AR21 | Annual Report 2020-21 | bseindia.com/bseplus/AnnualReport/532540/68468532540_25_05_21.pdf |
| AR20 | Annual Report 2019-20 (retrieved, not yet read) | bseindia.com/bseplus/AnnualReport/532540/5325400320.pdf |
| AR19 | Annual Report 2018-19 | bseindia.com/bseplus/AnnualReport/532540/5325400319.pdf |
| AR18 | Annual Report 2017-18 (retrieved, not yet read) | bseindia.com/bseplus/AnnualReport/532540/5325400318.pdf |
| AR17 | Annual Report 2016-17 (first Ind AS year; FY2016 comparatives; consolidated statements did not extract with pdftotext -layout) | bseindia.com/bseplus/AnnualReport/532540/5325400317.pdf |
| AR16 | Annual Report 2015-16 (not retrieved) | bseindia.com/bseplus/AnnualReport/532540/5325400316.pdf |

Aggregator: screener.in/company/TCS/consolidated/ (one exploratory fetch). **Rejected on the tier-2 test:** its FY2026 total assets 181,167 cr against the primary 182,372 cr (AR26, consolidated balance sheet); its FY2024 total assets 145,472 cr against 146,449 cr (AR25 comparative). Not used for any figure below.

## 3. Item table (INR crore unless stated; FY ends 31 March; consolidated, Ind AS)

Locations: "BS" = consolidated balance sheet, "PL" = consolidated statement of profit and loss, "CF" = consolidated statement of cash flows, "SoCE" = consolidated statement of changes in equity, "N19" = note 19 segment information. AR26 pages: BS p. 196, PL p. 197, CF pp. 202–203, N19 pp. 254–255. For an earlier AR the comparative column of the later AR is used where both exist.

| item | FY | value | unit | source |
|---|---|---|---|---|
| Close | 2026-10-30 | 2502.60 | INR | PX |
| Weighted average shares (basic = diluted) | FY2026 | 3,618,087,518 | shares | AR26 PL |
| Weighted average shares | FY2025 | 3,618,087,518 | shares | AR25 PL |
| Weighted average shares | FY2024 | 3,646,851,755 | shares | AR25 PL (comparative) |
| Weighted average shares | FY2023 | 3,659,051,373 | shares | AR23 PL |
| Weighted average shares | FY2022 | 3,698,832,195 | shares | AR23 PL (comparative) |
| Weighted average shares | FY2021 | 3,740,110,733 | shares | AR21 PL |
| Weighted average shares | FY2020 | 3,752,384,706 | shares | AR21 PL (comparative) |
| Weighted average shares | FY2019 | 3,789,749,350 | shares | AR19 PL |
| Weighted average shares (post-2018 1:1 bonus basis) | FY2018 | 3,849,185,612 | shares | AR19 PL (comparative) |
| Revenue from operations | FY2026 / FY2025 | 267,021 / 255,324 | cr | AR26 PL |
| Revenue from operations | FY2024 | 240,893 | cr | AR25 PL |
| Revenue from operations | FY2023 / FY2022 | 225,458 / 191,754 | cr | AR23 PL |
| Revenue from operations | FY2021 / FY2020 | 164,177 / 156,949 | cr | AR21 PL |
| Other income | FY2026 / FY2025 / FY2024 | 4,402 / 3,962 / 4,422 | cr | AR26 PL; AR25 PL |
| Other income | FY2023 / FY2022 | 3,449 / 4,018 | cr | AR23 PL |
| Other income | FY2021 / FY2020 | 3,134 / 4,592 | cr | AR21 PL |
| Other income | FY2019 / FY2018 | 4,311 / 3,642 | cr | AR19 PL |
| Employee benefit expenses | FY2026 / FY2025 | 154,994 / 145,788 | cr | AR26 PL |
| Cost of equipment and software licences | FY2026 / FY2025 | 4,399 / 11,648 | cr | AR26 PL |
| Other expenses | FY2026 / FY2025 | 35,230 / 30,481 | cr | AR26 PL |
| Finance costs | FY2026 / FY2025 / FY2024 | 1,227 / 796 / 778 | cr | AR26 PL; AR25 PL |
| Finance costs | FY2023 / FY2022 | 779 / 784 | cr | AR23 PL |
| Depreciation and amortisation | FY2026 / FY2025 / FY2024 | 5,560 / 5,242 / 4,985 | cr | AR26 PL; AR25 PL |
| Depreciation and amortisation | FY2023 / FY2022 | 5,022 / 4,604 | cr | AR23 PL |
| Profit before exceptional items and tax | FY2026 / FY2025 | 70,013 / 65,331 | cr | AR26 PL |
| Exceptional: restructuring expenses (note 25) | FY2026 | 1,388 | cr | AR26 PL |
| Exceptional: statutory impact of new Labour Codes (note 26) | FY2026 | 2,128 | cr | AR26 PL |
| Exceptional: provision towards legal claim (note 20) | FY2026 | 1,010 | cr | AR26 PL |
| Profit before tax | FY2026 / FY2025 / FY2024 | 65,487 / 65,331 / 61,997 | cr | AR26 PL; AR25 PL |
| Profit before tax | FY2023 / FY2022 | 56,907 / 51,687 | cr | AR23 PL |
| Profit before tax | FY2021 / FY2020 | 43,760 / 42,248 | cr | AR21 PL |
| Profit before tax | FY2019 / FY2018 | 41,563 / 34,092 | cr | AR19 PL |
| Profit attributable to shareholders | FY2026 / FY2025 / FY2024 | 49,210 / 48,553 / 45,908 | cr | AR26 PL; AR25 PL |
| Profit attributable to shareholders | FY2023 / FY2022 | 42,147 / 38,327 | cr | AR23 PL |
| Profit attributable to shareholders | FY2021 / FY2020 | 32,430 / 32,340 | cr | AR21 PL |
| Profit attributable to shareholders | FY2019 / FY2018 | 31,472 / 25,826 | cr | AR19 PL |
| Segment "Operating income" (after unallocable expenses, incl. D&A, exceptional items and finance costs; before other income) | FY2026 / FY2025 | 61,085 / 61,369 | cr | AR26 N19 |
| Total unallocable expenses | FY2026 / FY2025 | 11,313 / 6,038 | cr | AR26 N19 |
| Segment revenue: BFSI / Manufacturing / Consumer Business / CMT / Life Sciences & Healthcare / Others | FY2026 | 103,363 / 26,614 / 42,432 / 39,474 / 27,745 / 27,393 | cr | AR26 N19 |
| Segment result, same order | FY2026 | 27,011 / 8,051 / 12,090 / 11,473 / 7,504 / 6,269 | cr | AR26 N19 |
| Segment revenue, same order | FY2025 | 94,597 / 25,170 / 40,197 / 45,893 / 26,456 / 23,011 | cr | AR26 N19 |
| Segment result, same order | FY2025 | 25,135 / 8,225 / 11,222 / 9,582 / 7,448 / 5,795 | cr | AR26 N19 |
| Geographic revenue: Americas / Europe / India / Others | FY2026 | 134,998 / 87,467 / 15,775 / 28,781 | cr | AR26 N19 |
| Total assets | FY2026 / FY2025 | 182,372 / 159,629 | cr | AR26 BS |
| Total assets | FY2024 | 146,449 | cr | AR25 BS (comparative) |
| Total assets | FY2023 / FY2022 | 143,651 / 141,514 | cr | AR23 BS |
| Total assets | FY2021 / FY2020 | 130,759 / 120,899 | cr | AR21 BS |
| Total assets | FY2019 / FY2018 | 114,943 / 106,296 | cr | AR19 BS |
| Equity attributable to shareholders | FY2026 / FY2025 | 107,240 / 94,756 | cr | AR26 BS |
| Equity attributable to shareholders | FY2024 | 90,489 | cr | AR25 BS (comparative) |
| Equity attributable to shareholders | FY2023 / FY2022 | 90,424 / 89,139 | cr | AR23 BS |
| Equity attributable to shareholders | FY2021 / FY2020 | 86,433 / 84,126 | cr | AR21 BS |
| Equity attributable to shareholders | FY2019 / FY2018 | 89,446 / 85,128 | cr | AR19 BS |
| Non-controlling interests | FY2026 / FY2025 / FY2024 | 1,238 / 1,015 / 830 | cr | AR26 BS; AR25 BS |
| Goodwill | FY2026 / FY2025 / FY2024 | 9,108 / 1,860 / 1,832 | cr | AR26 BS; AR25 BS |
| Goodwill | FY2023 / FY2022 | 1,858 / 1,787 | cr | AR23 BS |
| Goodwill | FY2021 / FY2020 | 1,798 / 1,710 | cr | AR21 BS |
| Goodwill | FY2019 / FY2018 | 1,700 / 1,745 | cr | AR19 BS |
| Other intangible assets | FY2026 / FY2025 / FY2024 | 176 / 940 / 510 | cr | AR26 BS; AR25 BS |
| Other intangible assets | FY2023 / FY2022 / FY2021 / FY2020 / FY2019 / FY2018 | 867 / 1,101 / 480 / 283 / 179 / 12 | cr | AR23 BS; AR21 BS; AR19 BS |
| Current investments | FY2026 / FY2025 / FY2024 | 33,770 / 30,689 / 31,481 | cr | AR26 BS; AR25 BS |
| Current investments | FY2023 / FY2022 | 36,897 / 30,262 | cr | AR23 BS |
| Non-current investments | FY2026 / FY2025 / FY2024 | 218 / 275 / 281 | cr | AR26 BS; AR25 BS |
| Cash and cash equivalents | FY2026 / FY2025 / FY2024 | 6,417 / 8,342 / 9,016 | cr | AR26 BS; AR25 BS |
| Cash and cash equivalents | FY2023 / FY2022 | 7,123 / 12,488 | cr | AR23 BS |
| Cash and cash equivalents | FY2021 / FY2020 | 6,858 / 8,646 | cr | AR21 BS |
| Cash and cash equivalents | FY2019 / FY2018 | 7,224 / 4,883 | cr | AR19 BS |
| Other balances with banks | FY2026 / FY2025 / FY2024 | 6,491 / 7,121 / 4,270 | cr | AR26 BS; AR25 BS |
| Other balances with banks | FY2023 / FY2022 / FY2021 / FY2020 / FY2019 / FY2018 | 3,909 / 5,733 / 2,471 / 1,020 / 5,624 / 2,278 | cr | AR23 BS; AR21 BS; AR19 BS |
| Lease liabilities non-current / current | FY2026 | 9,453 / 1,830 | cr | AR26 BS (non-current line prints "9 453"; ties to total non-current liabilities 12,980) |
| Lease liabilities non-current / current | FY2025 | 7,838 / 1,554 | cr | AR26 BS |
| Lease liabilities non-current / current | FY2024 | 6,516 / 1,505 | cr | AR25 BS |
| Lease liabilities non-current / current | FY2023 / FY2022 | 6,203 + 1,485 / 6,368 + 1,450 | cr | AR23 BS |
| Lease liabilities non-current / current | FY2021 / FY2020 | 6,503 + 1,292 / 6,906 + 1,268 | cr | AR21 BS |
| Borrowings non-current / current | FY2019 / FY2018 | 44 + 0 / 54 + 181 | cr | AR19 BS |
| Class B compulsorily convertible preference shares (liability) | FY2026 | 126 | cr | AR26 BS |
| Trade payables | FY2026 / FY2025 / FY2024 | 14,808 / 13,909 / 9,981 | cr | AR26 BS; AR25 BS |
| Trade payables | FY2023 / FY2022 / FY2021 / FY2020 / FY2019 / FY2018 | 10,515 / 8,045 / 7,860 / 6,740 / 6,292 / 5,094 | cr | AR23 BS; AR21 BS; AR19 BS |
| Unearned and deferred revenue (non-current + current) | FY2026 / FY2025 / FY2024 | 647 + 4,487 / 518 + 4,028 / 482 + 3,640 | cr | AR26 BS; AR25 BS |
| Unearned and deferred revenue (non-current + current) | FY2023 / FY2022 | 1,003 + 3,843 / 1,110 + 3,635 | cr | AR23 BS |
| Unearned and deferred revenue (non-current + current) | FY2021 / FY2020 / FY2019 / FY2018 | 1,197 + 3,650 / 697 + 2,915 / 844 + 2,392 / 503 + 2,032 | cr | AR21 BS; AR19 BS |
| Income tax liabilities (net) | FY2026 / FY2025 / FY2024 | 14,751 / 12,715 / 11,433 | cr | AR26 BS; AR25 BS |
| Income tax liabilities (net) | FY2023 / FY2022 / FY2021 / FY2020 / FY2019 / FY2018 | 9,345 / 7,921 / 6,243 / 3,712 / 2,667 / 1,421 | cr | AR23 BS; AR21 BS; AR19 BS |
| Employee benefit obligations (non-current + current) | FY2026 / FY2025 / FY2024 | 961 + 5,600 / 841 + 4,885 / 686 + 4,519 | cr | AR26 BS; AR25 BS |
| Employee benefit obligations (non-current + current) | FY2023 / FY2022 | 536 + 4,065 / 677 + 3,810 | cr | AR23 BS |
| Other current liabilities / current provisions | FY2026 / FY2025 / FY2024 | 6,866 + 1,378 / 7,188 + 180 / 6,524 + 140 | cr | AR26 BS; AR25 BS |
| Other current financial liabilities | FY2026 / FY2025 / FY2024 | 11,194 / 8,542 / 8,362 | cr | AR26 BS; AR25 BS |
| Total current liabilities | FY2026 / FY2025 / FY2024 | 60,914 / 53,001 / 46,104 | cr | AR26 BS; AR25 BS |
| Total non-current liabilities | FY2026 / FY2025 / FY2024 | 12,980 / 10,857 / 9,026 | cr | AR26 BS; AR25 BS |
| CFO | FY2026 / FY2025 / FY2024 | 52,094 / 48,908 / 44,338 | cr | AR26 CF; AR25 CF |
| CFO | FY2023 / FY2022 | 41,965 / 39,949 | cr | AR23 CF |
| CFO | FY2021 / FY2020 | 38,802 / 32,369 | cr | AR21 CF |
| CFO | FY2019 / FY2018 | 28,593 / 25,067 | cr | AR19 CF |
| Interest paid (financing; to move into CFO for FCF) | FY2026 / FY2025 / FY2024 | 901 / 840 / 699 | cr | AR26 CF; AR25 CF |
| Interest paid | FY2023 / FY2022 | 779 / 698 | cr | AR23 CF |
| Repayment of lease liabilities | FY2026 / FY2025 / FY2024 | 1,861 / 1,664 / 1,614 | cr | AR26 CF; AR25 CF |
| Repayment of lease liabilities | FY2023 / FY2022 / FY2021 / FY2020 | 1,515 / 1,417 / 1,336 / 1,062 | cr | AR23 CF; AR21 CF |
| Payment for PP&E / intangibles | FY2026 | 3,670 / 367 | cr | AR26 CF |
| Payment for PP&E / intangibles | FY2025 / FY2024 | 2,917 / 944 · 2,202 / 442 | cr | AR25 CF |
| Payment for PP&E / intangibles | FY2023 / FY2022 | 2,532 / 355 · 2,483 / 497 | cr | AR23 CF |
| Payment for PP&E / intangibles | FY2021 / FY2020 | 2,719 / 356 · 2,538 / 192 | cr | AR21 CF |
| Payment for PP&E / intangibles | FY2019 / FY2018 | 2,053 / 178 · 1,862 / 0 | cr | AR19 CF |
| Payment for right-of-use assets (advances) | FY2026 / FY2025 | 109 / 76 | cr | AR26 CF |
| Acquisition of assets (note 21) | FY2026 / FY2025 | 554 / 1,063 | cr | AR26 CF |
| Acquisition of subsidiaries, net of cash 130 (note 7) | FY2026 | 6,750 | cr | AR26 CF |
| Interest income (CF adjustment) | FY2026 / FY2025 / FY2024 | 3,854 / 3,296 / 3,781 | cr | AR26 CF; AR25 CF |
| Interest income (CF adjustment) | FY2023 / FY2022 / FY2021 / FY2020 | 3,248 / 2,663 / 2,504 / 3,562 | cr | AR23 CF; AR21 CF |
| Dividend paid (incl. tax on dividend before FY2021) | FY2026 / FY2025 / FY2024 | 39,437 / 44,864 / 25,137 | cr | AR26 CF; AR25 CF |
| Dividend paid | FY2023 / FY2022 / FY2021 / FY2020 / FY2019 / FY2018 | 41,347 / 13,317 / 10,850 / 37,634 / 11,424 / 10,726 | cr | AR23 CF; AR21 CF; AR19 CF |
| Buy-back of equity shares (cash) | FY2024 / FY2022 / FY2021 / FY2019 / FY2018 | 17,000 / 18,000 / 16,000 / 16,000 / 16,000 | cr | AR25 CF; AR23 CF; AR21 CF; AR19 CF |
| Tax on buy-back paid | FY2024 / FY2023 | 3,959 / 4,192 | cr | AR25 CF; AR23 CF |
| Buy-back expenses | FY2024 / FY2022 | 46 / 49 | cr | AR25 SoCE; AR23 SoCE |
| Trusts and TCS Foundation equity held for specified purposes | FY2025 / FY2024 / FY2023 / FY2022 | 1,570 / 1,612 / 1,601 / 1,759 | cr | AR25 SoCE footnote; AR23 SoCE footnote |

Derived (not carried; re-derive on resume): MCap at px ≈ 2502.60 × 3,618.09m shares = INR 905,454 cr (derived: PX close × FY2026 weighted shares; the resume takes the share count at 30 Sep 2026 from the Q2 FY2027 interim).

## 4. Readings settled (as far as the run got; no grade, no verdict)

- **Key and unit.** TCS.NS verified at the endpoint: exchangeName NSI, currency INR, so `px_unit` INR; px 2502.60 at 2026-10-30. ISIN INE467B01029.
- **Gate 0 (draft sentence, not settled).** Mumbai-headquartered, Tata Sons-controlled IT services firm (promoter holding to be read from the AR26 shareholding pattern), selling application development and maintenance, consulting, cloud and infrastructure services, business-process services and software products to large enterprises (banks and insurers ≈ 39% of FY2026 revenue), billed mostly in the Americas (51%) and Europe (33%) and delivered from Indian centres. The filings plainly show product and paying customer: Gate 0 will pass; no P30 ground was seen.
- **Group.** Six reportable segments (N19): BFSI (38.7% of FY2026 revenue; 37.3% of Σ segment results), Consumer Business (15.9%; 16.7%), CMT (14.8%; 15.8%), Life Sciences & Healthcare (10.4%; 10.4%), Others — energy, resources and utilities, s-Governance and products, a unit that mixes businesses (10.3%; 8.7%), Manufacturing (9.97% of revenue; 11.1% of results). All six are material units (P22). No controlled listed subsidiary and no material listed holding found (no `holding_keys` expected; confirm on resume).
- **Segment assets: not reported.** N19 states assets and liabilities are used interchangeably and are not identified to segments, so the allocation-across-the-parts test is INDETERMINATE (b) (re-test: a filer segment-asset disclosure). Weight base: three-year average segment results (FY2024 segment figures owed from AR25 N19).
- **Customer breadth.** N19 (AR26 p. 255): "No single customer represents 10% or more of the Group's total revenue for the years ended March 31, 2026 and 2025" — a group statement that covers every unit (§2·1B v4.8.0) unless a unit discloses its own concentration.
- **Lens.** STD (not a bank or insurer; no finance activity).
- **J1 OI candidates (not settled).** (a) PL profit before exceptional items and tax less other income plus finance costs (FY2026: 70,013 − 4,402 + 1,227 = 66,838, derived) — excludes the exceptional items, so it is never OI; (b) the N19 "Operating income" (61,085), which carries every operating charge including the exceptional items but also finance costs (lease interest is a Gate 2 debt-equivalent's cost); (c) (a) less the exceptional items 4,526 = 62,312 (derived). The lowest subtotal carrying every operating charge, with finance costs read on the lease rule, is the resume's call; FY2026 exceptional items 4,526 make FY2026 a P28 candidate (test owed).
- **Securities.** Current investments (≈ 33,770 at FY2026) are mainly Indian government securities, treasury bills and mutual funds (S1 class test owed, AR26 note 8(a)); trusts' and TCS Foundation's investments held for specified purposes are never cash.
- **Buy-backs.** Tender-offer buy-backs: FY2018 16,000, FY2019 16,000, FY2021 16,000, FY2022 18,000, FY2024 17,000 cr (cash), plus buy-back tax. The price per share and shares bought in each, and the point-in-time worth reads, are owed (P19). The promoter (Tata Sons) tendered in these offers: an RPT and controller-as-counterparty reading is owed (§2·1C·2).
- **FY2026 deals.** Acquisition of subsidiaries 6,750 cr net of 130 cash (note 7); goodwill rose 1,860 → 9,108. Size against 1% of EV (≈ 8,900 cr at px, derived) and the acquisition stop are owed.

## 5. Scope still owed (next run, in this order)

- [ ] Extract FY2016 and FY2017 balance sheets, P&L and CF from AR17 (the consolidated statements did not extract with `pdftotext -layout`; try without `-layout` or by page range), and FY2017 from AR18 comparatives; FY2019–FY2020 P&L lines from AR19/AR20.
- [ ] Read AR24, AR22 and AR20 for the remaining statement lines (other financial liabilities, provisions, NCI, investments FY2018–FY2021) and the FY2024 segment note.
- [ ] NIBCL composition per year (trade payables, accrued employee costs in other financial liabilities, unearned revenue, income tax liabilities) — note 8(h) and 10(f) each year.
- [ ] Q2 FY2027 interim (quarter to 30 Sep 2026, results ~9 Oct 2026; NSE integrated filing iXBRL at nsearchives.nseindia.com/corporate/ixbrl/…): balance sheet for EV, TTM OI and FCF, share count.
- [ ] P20: k, deflators (India CPI, MOSPI), real growth, floors (D&A of PP&E and intangibles excl. ROU and acquired intangibles); acquired revenue for FY2026 deals (note 7).
- [ ] B1–B3 on eleven balance sheets; P31 test (associates negligible; check); J6; P28 on FY2026 exceptional items.
- [ ] B4 weights (three-year average segment results), six Appendix D blocks, S.
- [ ] Gate 1C: remuneration (AR26 Board's report / corporate governance: CEO K Krithivasan, COO Aarthi Subramanian, CFO; commission and perquisites), director fees, ownership; RPTs with Tata Sons (brand equity contribution) and Tata group companies; buy-back worth table (FY2018–FY2024 tenders, price per share from the letters of offer); FY2026 acquisitions.
- [ ] Gate 2: EV build both variants, trigger band, averaged readings.
