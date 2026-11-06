# BMW.DE — Bayerische Motoren Werke AG — INCOMPLETE evidence, resumable record (ANALYSE 2026-11-06)

## 1. Header

- Key: BMW.DE · job: ANALYSE · D 2026-11-06 · T 1941 · base sha f74f58bb9fde66c133aef0997b71136de9a79cb0
- Live `model_version`: v4.8.0
- Prior memo: none. No `memos/BMW.DE/` or `archive/memos/BMW.DE/` folder exists at base. No register row (`_REGISTER.md`, `register.csv`) and no memo `company:` line matches "Bayerische Motoren Werke" or "BMW". The ISIN is not printed in the documents read, so the ISIN half of the identity check is owed (below).
- Named gap: **group build exceeds budget** (README §5; MODEL §8.7 item 6). This is the **first overrun**: the queue line carries no ` — partial …` note at base.
- Also unretrievable this run: the price endpoint `query1.finance.yahoo.com/v8/finance/chart/BMW.DE` answered `Edge: Too Many Requests` (HTTP 429) on three tries (19:5x, 20:0x, 20:2x Prague). No px, `currency` or `exchangeName` was recorded, and no split check was run.
- No verdict, grade or band is stated here. Each "derived" figure below is arithmetic on the cited figures. It is not a grade.

## 2. Per gate or leg — work done and figures

### Document route

The issuer IR page `https://www.bmwgroup.com/en/investor-relations/company-reports.html` (HTTP 200) lists every report. All PDFs below returned HTTP 200 from `https://www.bmwgroup.com/content/dam/grpw/websites/bmwgroup_com/ir/downloads/en/` + path:

| doc | path |
|---|---|
| AR2025 (BMW Group Report 2025) | `2026/bericht/BMW-Group-Report-2025-en.pdf` |
| AR2024 | `2025/bericht/BMW-Group-Report-2024-en.pdf` |
| AR2023 | `2024/bericht/BMW-Group-Report-2023-en.pdf` |
| AR2022 | `2023/bericht/BMW-Group-Report-2022-en.pdf` |
| AR2021 | `2022/bericht/BMW-Group-Report-2021-en.pdf` |
| AR2020 | `2021/bericht/BMW-Group-Bericht-2020-EN.pdf` |
| AR2019 (financial report) | `2020/gb/BMW-GB19_en_Finanzbericht.pdf` |
| AR2018 (financial report) | `2019/gb/BMW-GB18_en_Finanzbericht_190315_ONLINE.pdf` |
| AR2017 (financial report) | `2018/gb/BMW-GB17_en_Finanzbericht_ONLINE.pdf` |
| AR2016 | `2017/GB/2016-BMW-Group-Annual-Report.pdf` |
| Q3 2026 quarterly statement | `2026/q3/BMW_Q3-2026-EN.pdf` |

"p." below is the PDF page index (pdftotext page number), not the printed folio. The statements are BMW's "Income Statement / Balance Sheet / Cash Flow Statement for Group and Segments"; the values below are the **Group** column. Statement pages: AR2016 IS p. 112, BS p. 114–115, CF p. 116–117 · AR2017 IS p. 120, BS p. 122–123, CF p. 124–125 · AR2018 IS p. 112, BS p. 114–115, CF p. 116–117 · AR2019 IS p. 110, BS p. 112–113, CF p. 114–115 · AR2020 IS p. 186, BS p. 188–189, CF p. 190–191 · AR2021 IS p. 149, BS p. 151–152, CF p. 153–154 · AR2022 IS p. 153, BS p. 155–156, CF p. 157–158 · AR2023 IS p. 152, BS p. 154–155, CF p. 156–157 · AR2024 IS p. 269, BS p. 271–272, CF p. 273–274 · AR2025 IS p. 271, BS p. 273–274, CF p. 275–276.

Each FY is taken from its own year's report (first reported), except where a row says "restated". FY2015 balance-sheet figures are AR2016's prior-year column (the opening balance sheet of the FY2016–FY2025 window).

### Income statement (EUR m)

| item | FY | value | unit | source |
|---|---|---|---|---|
| Revenues | FY2016 / FY2017 / FY2018 / FY2019 / FY2020 | 94,163 / 98,678 / 97,480 / 104,210 / 98,990 | EUR m | each year's AR, IS page above |
| Revenues | FY2021 / FY2022 / FY2023 / FY2024 / FY2025 | 111,239 / 142,610 / 155,498 / 142,380 / 133,453 | EUR m | each year's AR, IS page above |
| Revenues, restated (IFRS 15/16 comparatives) | FY2017 / FY2018 | 98,282 (AR2018 p. 112) / 96,855 (AR2019 p. 110) | EUR m | as cited |
| Profit before financial result (EBIT) | FY2016 / FY2017 / FY2018 / FY2019 / FY2020 | 9,386 / 9,880 / 9,121 / 7,411 / 4,830 | EUR m | each year's AR, IS page |
| Profit before financial result (EBIT) | FY2021 / FY2022 / FY2023 / FY2024 / FY2025 | 13,400 / 13,999 / 18,482 / 11,509 / 10,186 | EUR m | each year's AR, IS page |
| EBIT, restated | FY2017 / FY2018 | 9,899 (AR2018 p. 112) / 8,933 (AR2019 p. 110) | EUR m | as cited |
| Result from equity accounted investments (in financial result, below EBIT) | FY2015 / FY2016 / FY2017 / FY2018 / FY2019 / FY2020 / FY2021 | 518 / 441 / 738 / 632 / 136 / 920 / 1,520 | EUR m | AR2016 p. 112 (FY2015, FY2016); then each year's AR IS page |
| Result from equity accounted investments | FY2022 / FY2023 / FY2024 / FY2025 | -100 / -159 / -14 / 38 | EUR m | each year's AR IS page |
| Interest and similar income (group, financial result) | FY2016 … FY2025 | 196 / 201 / 397 / 179 / 116 / 135 / 422 / 701 / 655 / 502 | EUR m | each year's AR IS page |
| Other financial result | FY2016 … FY2025 | 131 / 248 / 51 / -109 / -186 / 1,170 / 8,937 / -1,272 / -606 / 72 | EUR m | each year's AR IS page (FY2022 includes the BMW Brilliance revaluation on full consolidation: AR2022 Note 13, owed) |
| Profit before tax | FY2021 / FY2022 / FY2023 / FY2024 / FY2025 | 16,060 / 23,509 / 17,096 / 10,971 / 10,236 | EUR m | AR2021 p. 149; AR2023 p. 152 (FY2022 col.); AR2024 p. 269; AR2025 p. 271 |
| Net profit attributable to shareholders of BMW AG | FY2020 / FY2021 / FY2024 / FY2025 | 3,775 / 12,382 / 7,290 / 7,294 | EUR m | AR2021 p. 149; AR2025 p. 271 |
| EPS basic = diluted (ordinary) | FY2024 / FY2025 | 11.62 / 11.89 | EUR | AR2025 p. 271 ("Dilutive effects –") |

### Shares (EPS note; basic = diluted in every year read)

| item | FY | value | unit | source |
|---|---|---|---|---|
| Average ordinary (common) shares in circulation | FY2015–FY2021 | 601,995,196 each year | shares | AR2016 p. 137; AR2017 p. 145; AR2018 p. 145; AR2019 p. 140; AR2020 p. 214; AR2021 p. 174 |
| Average preferred shares in circulation | FY2015 / FY2016 / FY2017 / FY2018 / FY2019 / FY2020 / FY2021 | 54,499,460 / 54,809,375 / 55,114,290 / 55,605,380 / 56,122,857 / 56,867,180 / 57,686,234 | shares | same notes as above |
| Average ordinary / preferred shares | FY2022 | 597,924,318 / 59,035,325 | shares | AR2022 p. 179 |
| Average ordinary / preferred shares | FY2023 | 579,941,360 / 58,776,197 | shares | AR2023 p. 178 |
| Average ordinary / preferred shares | FY2024 | 570,599,065 / 56,741,178 | shares | AR2024 p. 294 |
| Average ordinary / preferred shares | FY2025 | 559,313,364 / 54,225,635 | shares | AR2025 p. 296 |
| Shares issued at 31 Dec 2025, ordinary / preferred | FY2025 | 561,134,926 / 54,675,505 | shares | AR2025 p. 308, Note 31 ("Number of shares issued at 31 December") |
| Treasury shares held at 30 Sep 2026 | Q3 2026 | 24,676,720 (4.01% of share capital) | shares | Q3 2026 p. 12, "Share buyback programme" |
| Third buyback (≤ €2bn, approved 20 May 2025): tranche 1 7,498,153 ord. + 1,773,313 pref., ≈ €750m (21 May–8 Dec 2025); tranche 2 8,252,475 ord., ≈ €625m (2 Jan–26 Jun 2026); tranche 3 €625m from 1 Jul 2026, to end by 30 Nov 2026 | 2025–2026 | as stated | shares, EUR m | Q3 2026 p. 12 |

### Balance sheet (EUR m, 31 Dec)

| item | FY | value | unit | source |
|---|---|---|---|---|
| Total assets | FY2015 / FY2016 / FY2017 / FY2018 / FY2019 / FY2020 | 172,174 / 188,535 / 193,483 / 208,980 / 228,034 / 216,658 | EUR m | AR2016 p. 114 (FY2015, FY2016); then each year's AR BS page |
| Total assets | FY2021 / FY2022 / FY2023 / FY2024 / FY2025 / 30 Sep 2026 | 229,527 / 246,926 / 250,890 / 267,732 / 265,967 / 274,668 | EUR m | each year's AR BS page; Q3 2026 p. 30 |
| Total assets, restated | FY2017 (IFRS 15) / FY2018 | 195,586 (AR2018 p. 114) / 208,938 (AR2019 p. 112; 1 Jan 2019 after IFRS 16: 211,304) | EUR m | as cited |
| Equity attributable to shareholders of BMW AG | FY2015 / FY2016 / FY2017 / FY2018 / FY2019 / FY2020 | 42,530 / 47,108 / 54,112 / 57,559 / 59,324 / 60,891 | EUR m | AR2016 p. 114; then each year's AR |
| Equity attributable to shareholders of BMW AG | FY2021 / FY2022 / FY2023 / FY2024 / FY2025 / 30 Sep 2026 | 74,366 / 87,125 / 89,596 / 92,315 / 95,697 / 96,173 | EUR m | each year's AR; Q3 2026 p. 32 |
| Minority / non-controlling interests | FY2015 … FY2025 | 234 / 255 / 436 / 529 / 583 / 629 / 766 / 4,163 / 3,327 / 2,688 / 2,209 | EUR m | each year's AR BS equity page |
| Intangible assets | FY2015 … FY2025 | 7,372 / 8,157 / 9,464 / 10,971 / 11,729 / 12,342 / 12,980 / 21,776 / 20,022 / 20,220 / 19,915 | EUR m | each year's AR BS (goodwill inside: Note 21/22, owed) |
| Property, plant and equipment | FY2015 … FY2025 | 17,759 / 17,960 / 18,471 / 19,801 / 23,245 / 21,850 / 22,390 / 32,126 / 35,266 / 39,581 / 39,903 | EUR m | each year's AR BS (FY2019 on includes right-of-use assets: split owed, Note 22) |
| Leased products | FY2015 … FY2025 | 34,965 / 37,789 / 36,257 / 38,572 / 42,609 / 41,995 / 44,700 / 42,820 / 43,118 / 48,838 / 53,024 | EUR m | each year's AR BS |
| Receivables from sales financing, non-current | FY2015 … FY2025 | 41,865 / 48,032 / 48,321 / 48,109 / 51,030 / 48,025 / 51,712 / 50,368 / 50,517 / 55,149 / 53,599 | EUR m | each year's AR BS |
| Receivables from sales financing, current | FY2015 … FY2025 | 28,178 / 30,228 / 32,113 / 38,674 / 41,407 / 36,252 / 35,705 / 35,340 / 36,838 / 38,569 / 36,440 | EUR m | each year's AR BS |
| Investments accounted for using the equity method | FY2015 … FY2025 | 2,233 / 2,546 / 2,767 / 2,624 / 3,199 / 3,585 / 5,112 / 420 / 443 / 553 / 526 | EUR m | each year's AR BS |
| Other investments | FY2015 … FY2025 | 428 / 560 / 690 / 739 / 703 / 735 / 1,241 / 1,351 / 1,197 / 1,099 / 891 | EUR m | each year's AR BS |
| Financial assets, non-current + current | FY2015 | 2,208 + 6,635 | EUR m | AR2016 p. 114 |
| Financial assets, non-current + current | FY2016 / FY2017 / FY2018 / FY2019 / FY2020 | 2,705 + 7,065 / 2,369 + 7,965 / 1,010 + 6,675 / 1,370 + 5,955 / 2,644 + 5,108 | EUR m | each year's AR BS |
| Financial assets, non-current + current | FY2021 / FY2022 / FY2023 / FY2024 / FY2025 | 1,715 + 5,800 / 3,073 + 5,164 / 1,387 + 4,131 / 834 + 2,565 / 2,568 + 2,460 | EUR m | each year's AR BS (split into marketable securities, derivatives, loans: Note 26, owed) |
| Cash and cash equivalents | FY2015 … FY2025 / 30 Sep 2026 | 6,122 / 7,880 / 9,039 / 10,979 / 12,036 / 13,537 / 16,009 / 16,870 / 17,327 / 19,287 / 18,854 / 19,278 | EUR m | each year's AR BS; Q3 2026 p. 30 |
| Trade payables | FY2015 … FY2025 | 7,773 / 8,512 / 9,731 / 9,669 / 10,182 / 8,644 / 10,932 / 14,120 / 15,547 / 14,126 / 12,488 | EUR m | each year's AR BS |
| Current tax liabilities | FY2015 … FY2025 | 1,441 / 1,074 / 1,124 / 1,158 / 963 / 747 / 921 / 1,224 / 1,401 / 1,131 / 864 | EUR m | each year's AR BS |
| Financial liabilities, non-current | FY2015 … FY2025 / 30 Sep 2026 | 49,523 / 55,405 / 53,548 / 64,772 / 70,647 / 67,390 / 62,342 / 53,469 / 52,880 / 66,770 / 68,159 / 72,437 | EUR m | each year's AR BS; Q3 2026 p. 32 |
| Financial liabilities, current | FY2015 … FY2025 / 30 Sep 2026 | 42,160 / 42,326 / 41,100 / 38,825 / 46,093 / 38,986 / 41,121 / 40,727 / 42,130 / 44,491 / 42,310 / 46,210 | EUR m | each year's AR BS; Q3 2026 p. 32 |
| Pension provisions | FY2015 … FY2025 | 3,000 / 4,587 / 3,252 / 2,330 / 3,335 / 3,693 / 1,247 / 339 / 427 / 222 / 203 | EUR m | each year's AR BS |
| Other provisions, non-current + current | FY2025 / FY2024 | 6,524 + 7,670 / 7,830 + 8,543 | EUR m | AR2025 p. 274 |
| Other liabilities, non-current + current | FY2025 / FY2024 | 7,341 + 18,392 / 7,597 + 19,398 | EUR m | AR2025 p. 274 (contract liabilities and deferred income inside: Note 37, owed for NIBCL) |
| Liabilities from customer deposits (banking) | FY2025 / FY2024 | 17,952 / 19,439 | EUR m | AR2025 p. 325, Note 36 financial liabilities |

### Cash flow (EUR m)

| item | FY | value | unit | source |
|---|---|---|---|---|
| Cash inflow from operating activities (group) | FY2015 / FY2016 / FY2017 / FY2018 / FY2019 / FY2020 | 960 / 3,173 / 5,909 / 5,051 / 3,662 / 13,251 | EUR m | AR2016 p. 116 (FY2015, FY2016); then each year's AR CF page |
| Cash inflow from operating activities (group) | FY2021 / FY2022 / FY2023 / FY2024 / FY2025 / 9M 2026 | 15,903 (restated 15,914 in AR2022) / 23,523 / 17,542 / 7,566 / 8,228 / 4,060 | EUR m | each year's AR CF page; Q3 2026 p. 34 |
| of which change in leased products | FY2016 … FY2025 | -2,526 / -1,134 / -1,693 / -3,825 / -1,016 / -1,282 / 2,794 / -999 / -5,231 / -6,773 | EUR m | each year's AR CF page (R2 book: ±3% rule owed) |
| of which change in receivables from sales financing | FY2016 … FY2025 | -8,368 / -7,440 / -5,670 / -3,560 / 4,192 / 965 / 1,888 / -3,622 / -4,144 / -1,746 | EUR m | each year's AR CF page (R2 book: ±3% rule owed) |
| Depreciation and amortisation of tangible and intangible assets (CF line) | FY2016 … FY2025 | 4,998 / 4,822 / 5,113 / 6,017 / 6,139 / 6,495 / 8,566 / 8,974 / 8,650 / 8,692 | EUR m | each year's AR CF page (P20 floor needs RoU depreciation out: Notes 21/22, owed) |
| Total investment in intangible assets and PP&E | FY2015 / FY2016 / FY2017 / FY2018 / FY2019 / FY2020 | -5,889 / -5,823 / -7,112 / -7,777 / -6,902 / -6,150 | EUR m | AR2016 p. 116 (FY2015, FY2016); AR2018 p. 116 (FY2017, FY2018); AR2019 p. 114; AR2020 p. 190 |
| Total investment in intangible assets and PP&E | FY2021 / FY2022 / FY2023 / FY2024 / FY2025 / 9M 2026 | -6,619 / -9,050 / -10,881 / -12,205 / -10,963 / -5,436 | EUR m | each year's AR CF page; Q3 2026 p. 34 |
| Result from equity accounted investments reversed in CFO | FY2016 … FY2025 | -441 / -738 / -632 / -136 / -920 / -1,520 / 100 / 159 / 14 / -38 | EUR m | each year's AR CF page (dividends received from equity investees: where booked, owed) |
| Treasury shares acquired | FY2022 / FY2023 / FY2024 / FY2025 | -1,278 / -1,222 / -1,002 / -1,250 | EUR m | AR2023 p. 157; AR2024 p. 274; AR2025 p. 276 |
| Dividends paid to shareholders of BMW AG | FY2019 / FY2020 / FY2021 / FY2022 / FY2023 / FY2024 / FY2025 | -2,366 / -1,671 / -1,277 / -3,827 / -5,430 / -3,781 / -2,649 | EUR m | AR2020 p. 191; AR2021 p. 154; AR2023 p. 157; AR2025 p. 276 |
| Dividends paid to non-controlling interests | FY2024 / FY2025 | -1,013 / -510 | EUR m | AR2025 p. 276 |
| Interest paid (group, financing) | FY2024 / FY2025 | -196 / -245 | EUR m | AR2025 p. 276 (FS interest is in revenues/cost of sales: footnote, same page) |

### Segments (EUR m; unaudited supplementary columns of the same statements)

| item | FY | Automotive | Motorcycles | Financial Services | Other Entities | Eliminations | source |
|---|---|---|---|---|---|---|---|
| Revenues | FY2025 | 117,557 | 3,143 | 39,806 | 12 | -27,065 | AR2025 p. 271 |
| Revenues | FY2024 | 124,917 | 3,220 | 38,562 | 14 | -24,333 | AR2025 p. 271 |
| Revenues | FY2023 | 132,277 | 3,214 | 36,227 | 11 | -16,231 | AR2024 p. 269 |
| Revenues | FY2022 | 123,602 | 3,176 | 35,122 | 8 | -19,298 | AR2023 p. 152 |
| Profit before tax | FY2025 | 5,945 | 174 | 2,401 | 1,087 | 629 | AR2025 p. 271 |
| Profit before tax | FY2024 | 7,544 | 198 | 2,538 | 837 | -146 | AR2025 p. 271 |
| Profit before tax | FY2023 | 12,642 | 258 | 2,962 | -100 | 1,334 | AR2024 p. 269 |
| Profit before financial result | FY2025 / FY2024 / FY2023 | 6,259 / 7,893 / 12,981 | 178 / 198 / 259 | 2,411 / 2,511 / 3,055 | owed (column garbled in the text layer) | owed | AR2025 p. 271; AR2024 p. 269 |
| Total assets | FY2025 | 145,254 | 1,872 | 164,787 | 136,800 | -182,746 | AR2025 p. 273 |
| Total assets | FY2024 | 144,568 | 1,915 | 164,883 | 131,623 | -175,257 | AR2025 p. 273 |
| Total assets | FY2023 | 143,628 | 1,817 | 150,392 | 118,127 | -163,074 | AR2024 p. 271 |
| Total assets | FY2022 | 147,024 | 1,671 | 149,413 | 118,799 | -169,981 | AR2023 p. 154 |
| 9M revenues / EBIT | 9M 2026 (9M 2025) | 80,990 (87,164) / 2,875 (5,120) | owed | owed | — | — | Q3 2026 p. 28 (group 92,718 (99,999) / 5,224 (8,064)) |

Derived, indicative only, never a grade:
- Exclude-reading EBIT basis: BMW books the equity-method result, interest income and other financial result below EBIT, and Financial Services interest in revenues and cost of sales (AR2025 p. 276 footnote). So EBIT is the J1 OI candidate before the J1 line check (lowest operating subtotal; pension and other items: Notes 9–12, owed).
- P31 income limb, equity-method result ÷ EBIT: FY2017 738 ÷ 9,880 = 7.5%; FY2020 920 ÷ 4,830 = 19.0%; FY2021 1,520 ÷ 13,400 = 11.3%. Each is above 5%, so the classes are **above the P31 line** and both G6 readings are owed over the window.
- P31 asset limb, equity-method carrying value ÷ total assets: at most 5,112 ÷ 229,527 = 2.2% (FY2021).
- L/E FY2025 = (265,967 − 97,906) ÷ 95,697 = 175.6% (all liabilities, before any segregated-funds or G6 adjustment).
- Motorcycles materiality (P22), FY2025: revenue 3,143 ÷ 133,453 = 2.4%; assets 1,872 ÷ 265,967 = 0.7%; profit before tax 174 ÷ Σ positive segment PBT (5,945 + 174 + 2,401 + 1,087) = 1.8%. **Immaterial** on all three.
- Financial Services materiality, FY2025: revenue 39,806 ÷ 133,453 = 29.8%. **Material.**

## 3. Readings settled (as far as the run got)

- **Gate 0 (provisional):** the business can be described in one sentence. BMW makes and sells premium passenger cars (BMW, MINI, Rolls-Royce) and BMW Motorrad motorcycles, mostly to private buyers and fleets through independent and own dealers worldwide. Its captive Financial Services arm finances and leases BMW Group vehicles to retail customers, finances dealers, takes customer deposits through BMW Bank, and runs the Alphabet multi-brand fleet business (AR2025 p. 39, "Financial Services segment"; p. 84). The group is headquartered in Munich. No P30 ground was found.
- **Lens:** STD. BMW AG is not a bank or insurer and not the parent of a group supervised on a consolidated basis as one. Financial Services (BMW Bank GmbH, a licensed bank, among others) is a finance part. It is funded mainly by financial liabilities, not deposits: customer deposits were 17,952 of group financial liabilities of 110,469 at 31 Dec 2025 (68,159 + 42,310). So lens case (b) does not apply, and FS reads as a captive finance arm (R2), consolidated on STD. The captive test is owed in figures: the share of the FS book that is non-group brands (Alphabet multi-brand). The filer describes FS as financing BMW Group vehicles, with 46.6% of new BMW Group vehicles financed or leased by FS in 2025 (AR2025 p. 84).
- **Group:** material units are **Automotive** and **Financial Services** (P22). **Motorcycles** is immaterial (above) and is named in one line. "Other Entities" (holding and group financing companies, assets 136,800) has not been confirmed as non-operating: AR segment note, owed. There is no listed subsidiary. Material listed holdings are not yet checked; none is seen on the balance sheet (equity-method 526 at FY2025).
- **Perimeter:** BMW Brilliance Automotive (BBA, China) was equity-accounted to FY2021 (carrying value 5,112 at FY2021) and is fully consolidated from 2022: FY2022 shows intangible assets up 8.8bn, PP&E up 9.7bn and NCI up to 4,163. The FY2022 other financial result of 8,937 contains the revaluation of the previously held stake; it is a J3 removal (gain on stakes). The two G6 readings must carry BBA as an associate for FY2016–FY2021.
- **P31:** above the line (income limb fails FY2017, FY2020 and FY2021, among others).

## 4. Scope still owed (in order)

- [ ] Price endpoint: GET `BMW.DE` (record `currency`, `exchangeName`, instrument, close and date; `&events=split` since FY2016). Also GET `BMW3.DE` (preferred line), because both lines count in MCap (queue note). Resolve the ISIN for the identity check (ordinary-share ISIN from the AR's share section or the Q3 2026 statement), then grep memos and `register.csv`.
- [ ] J1 line check, AR2016–AR2025 Notes 9–12 (other operating income and expenses, financial result, pension net interest placement); confirm that EBIT is the lowest operating subtotal.
- [ ] NIBCL per year (Notes "Other liabilities" and "Other provisions": contract liabilities, deferred income, accruals); goodwill split out of intangibles (TBV); right-of-use assets and their depreciation out of PP&E and D&A (P20 floor); capitalised development (Note 21).
- [ ] R2 book rule per year: FS book (leased products + receivables from sales financing), prior-year change vs ±3%, and the CFO lines above.
- [ ] P20: k over FY2016–FY2025, π_t from euro-area HICP, deal-year test (FY2022 BBA consolidation: organic revenue disclosure needed, else tier 3 for FY2022).
- [ ] G6: two readings FY2016–FY2025 (BBA and other associates; dividends received from equity investees, AR CF and Note 24); B2/B3 on both readings; Appendix C P31 log.
- [ ] Gate 1B: Appendix D for Automotive and Financial Services (R7 customer worksheet: group statement on customers ≥ 10%; FS funding conc.); P29 weights on latest-3-FY segment profit before financial result.
- [ ] Gate 1C: remuneration reports 2023–2025 (AR2025 Remuneration Report section); Quandt/Klatten holdings and voting (shareholder structure); worth table at the point of purchase for the 2022–2026 buybacks (2022 −1,278, 2023 −1,222, 2024 −1,002, 2025 −1,250, 2026 tranches above); acquisition stop (BBA step-up 2022, consideration in AR2022 Note 3); allocation across the parts (segment assets FY2022–FY2025 above, earlier years on the same segmentation).
- [ ] Gate 2: funding pairing for FS financial liabilities and deposits; core numbers on TTM Q3-2026 or FY2025; P28 test (FY2025 EBIT 10,186 is below the 3-year average of FY2023–FY2025: test named causes); averaged readings; trigger band.
