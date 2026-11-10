# BMW.DE — Bayerische Motoren Werke AG — INCOMPLETE evidence, resumable record (ANALYSE 2026-11-10)

## 1. Header

- Key: BMW.DE · job: ANALYSE · D 2026-11-10 · T 2135 · base sha 271b3886cdf165629ed8e0fe1859bc005b19d7d0
- Live `model_version`: v4.8.0
- Prior memo: none. No `memos/BMW.DE/` or `archive/memos/BMW.DE/` folder at base. ISIN **DE0005190003** (ordinary share; BMW IR page `https://www.bmwgroup.com/en/investor-relations/bmw-shares.html`, "Share Details", retrieved 2026-11-10). One grep of `memos/`, `archive/memos/` and `register.csv` for `DE0005190003` and "Bayerische Motoren Werke" found nothing: no prior.
- resumes: `queue/evidence/BMW.DE_2026-11-06_INCOMPLETE.md` (first overrun, partial 2026-11-06). That record's statement figures were carried after their sources were re-opened: every AR2016–AR2025 and Q3 2026 PDF was re-downloaded this run from the URLs in its document-route table (all HTTP 200), and every governing figure below was re-read in the primary.
- Named gap: **data access: price endpoint HTTP 429**. `query1.finance.yahoo.com/v8/finance/chart/BMW.DE` answered HTTP 429 on every try of this run, fourteen tries between 21:36 and 21:54 Prague (and three times on 2026-11-06). No `px`, `currency`, `exchangeName` or split check exists, so no memo can carry its machine fields (README §5, D3; ANALYSE.md step 5). Apart from the price, the work items the 2026-11-06 record listed are done below, except the point-in-time worth reads of the buybacks, which need the interim balance sheets (scope still owed).
- Corporate action found: **the preferred shares were converted into ordinary shares.** The AGM and a special meeting of preferred holders resolved this on 13 May 2026. It was registered on 30 June 2026, and trading in the preferred line (BMW3.DE) was suspended on 30 June 2026. Share capital stays €615,810,431, now all ordinary bearer shares of €1 (Q3 2026 statement p. 12, "Share buyback programme"; IR share page). From 30 Jun 2026 the key prices one line, BMW.DE.
- No verdict, grade or band is stated here. "Derived" figures are arithmetic on the cited figures.

## 2. Per gate or leg — work done and figures

### Document route

The PDFs are at `https://www.bmwgroup.com/content/dam/grpw/websites/bmwgroup_com/ir/downloads/en/` + path, as in the 2026-11-06 record: AR2025 `2026/bericht/BMW-Group-Report-2025-en.pdf` · AR2024 `2025/bericht/BMW-Group-Report-2024-en.pdf` · AR2023 `2024/bericht/BMW-Group-Report-2023-en.pdf` · AR2022 `2023/bericht/BMW-Group-Report-2022-en.pdf` · AR2021 `2022/bericht/BMW-Group-Report-2021-en.pdf` · AR2020 `2021/bericht/BMW-Group-Bericht-2020-EN.pdf` · AR2019 `2020/gb/BMW-GB19_en_Finanzbericht.pdf` · AR2018 `2019/gb/BMW-GB18_en_Finanzbericht_190315_ONLINE.pdf` · AR2017 `2018/gb/BMW-GB17_en_Finanzbericht_ONLINE.pdf` · AR2016 `2017/GB/2016-BMW-Group-Annual-Report.pdf` · Q3 2026 `2026/q3/BMW_Q3-2026-EN.pdf`. Statement page indices are in the 2026-11-06 record. Note references below use each AR's own note title. The Group column of the "… for Group and Segments" statements is used throughout.

### Figures carried from the 2026-11-06 record (sources re-opened this run)

These were carried: revenue, EBIT ("profit before financial result"), result from equity-accounted investments, interest and similar income, other financial result, average ordinary and preferred shares, total assets, equity attributable, NCI, intangible assets, PP&E, leased products, sales-financing receivables, equity-method investments, other investments, cash, trade payables, current tax liabilities, financial liabilities, pension provisions, CFO, the two book lines in CFO, capex, treasury shares acquired and dividends paid. Each is cited by year and page there, and each was re-checked in the primary this run. Added: **FY2015 revenue 92,175** (AR2016, income statement, prior-year column).

### New figures this run (EUR m)

| item | FY | value | unit | source |
|---|---|---|---|---|
| Capitalised development costs, carrying amount | FY2015 … FY2025 | 6,351 / 7,221 / 8,409 / 9,976 / 10,443 / 11,007 / 11,573 / 12,127 / 12,344 / 13,780 / 15,251 | EUR m | each AR, note "Analysis of changes in Group tangible, intangible and investment assets" (AR2016 note 18; AR2017–AR2021, AR2023–AR2025 note 20; AR2022 note 21); FY2015 = AR2016 prior-year table |
| Goodwill, carrying amount | FY2015 … FY2025 | 364 / 364 / 380 / 380 / 380 / 379 / 380 / 1,562 / 1,487 / 1,529 / 1,440 | EUR m | same note |
| Other intangible assets, carrying amount | FY2015 … FY2025 | 657 / 572 / 675 / 615 / 906 / 956 / 1,027 / 8,087 / 6,191 / 4,911 / 3,224 | EUR m | same note |
| Right-of-use assets within PP&E (sum of the three "thereof right-of-use" lines) | FY2019 … FY2025 | 2,830 / 2,422 / 2,422 / 3,958 / 4,152 / 4,301 / 3,865 | EUR m | same note (derived sums of printed lines) |
| Development-cost amortisation, current year | FY2015 … FY2025 | 1,166 / 1,222 / 1,236 / 1,414 / 1,667 / 1,710 / 1,935 / 2,265 / 2,387 / 2,089 / 1,956 | EUR m | same note |
| PP&E depreciation, current year | FY2015 … FY2025 | 3,318 / 3,403 / 3,395 / 3,504 / 4,202 / 4,250 / 4,358 / 4,827 / 5,117 / 5,130 / 5,388 | EUR m | same note |
| Right-of-use depreciation (sum of thereof lines) | FY2019 … FY2025 | 467 / 504 / 484 / 659 / 823 / 898 / 909 | EUR m | same note |
| BBA business-combination column, FY2022 | FY2022 | goodwill 1,197; other intangibles 8,349; PP&E 7,072; right-of-use 633 | EUR m | AR2022 note 21 |
| Deferred income (other liabilities, total) | FY2015 … FY2025 | 6,254 / 7,256 / 7,174 / 7,484 / 3,635 / 3,546 / 3,820 / 3,633 / 3,359 / 3,568 / 3,448 | EUR m | each AR, note "Other liabilities" (AR2016–AR2017 note 34; AR2018–AR2021 note 36; AR2022 note 38); first-reported values, restatements below |
| Contract liabilities | FY2018 … FY2025 | 4,985 / 5,038 / 5,485 / 5,955 / 7,651 / 7,998 / 8,644 / 8,506 | EUR m | same note (FY2018 in the note text) |
| Advance payments received (other liabilities) | FY2015 … FY2025 | 802 / 977 / 1,056 / 911 / 585 / 139 / 160 / 237 / 237 / 115 / 172 | EUR m | same note |
| Restated: FY2017 (IFRS 15) deferred income 6,666, contract liabilities 4,820 | FY2017 | as stated | EUR m | AR2018 note 36 |
| Restated: FY2018 deferred income 3,112, contract liabilities 4,976, advance payments 297 | FY2018 | as stated | EUR m | AR2019 note 36 |
| Marketable securities and investment funds (financial assets note) | FY2015 … FY2025 | 5,261 / 5,287 / 5,447 / 5,316 / 5,391 / 4,226 / 4,243 / 3,438 / 2,170 / 1,470 / 696 | EUR m | each AR, note "Financial assets" |
| Lease liabilities | FY2019 … FY2025 | 2,895 / 2,511 / 2,420 / 2,764 / 2,539 / 2,553 / 2,492 | EUR m | each AR, note "Financial liabilities" |
| Interest received (in CFO) | FY2016 … FY2025 | 142 / 125 / 170 / 91 / 163 / 130 / 453 / 683 / 644 / 518 | EUR m | each AR, Group cash flow statement |
| Interest paid (in financing) | FY2016 … FY2025 | −118 / −165 / −136 / −199 / −275 / −217 / −222 / −186 / −196 / −245 | EUR m | each AR, Group cash flow statement (footnote: FS interest is in revenues and cost of sales) |
| Dividends received from investment assets (footnote to investing proceeds; mainly BBA) | FY2016 … FY2021 | 134 / 258 / 384 / 643 / 1,020 / nil | EUR m | AR2017–AR2021 cash flow footnote; FY2016 from AR2016 equity-method note (BBA "Dividends received by the Group"); not printed FY2022–FY2025 |
| Other financial result: result on investments (income from subsidiaries and participations less expenses) | FY2016 … FY2025 | −179 / 14 / 156 / 80 / 48 / 584 / 7,770 / −57 / −149 / −29 | EUR m | each AR, note "Other financial result"; FY2022 includes the 7,649 BBA remeasurement gain |
| Interest expense relating to the financial services business (in cost of sales) | FY2019 … FY2025 | 2,288 / 1,960 / 1,643 / 2,114 / 3,554 / 4,902 / 5,196 | EUR m | each AR, combined management report, condensed income statement ("thereof interest expense relating to financial services business") |
| Net profit / attributable to BMW AG shareholders | FY2023 / FY2024 / FY2025 | 12,165 / 11,290 · 7,678 / 7,290 · 7,451 / 7,294 | EUR m | AR2024 and AR2025 Group income statement |
| BBA step acquisition: 25% bought for €3,735m (CNY 27,941m) in cash on 11 Feb 2022; prior 50% remeasured at 12,341 (gain 7,649); goodwill 1,197; NCI 4,960; BBA revenue 28,031 and profit after tax 2,211 since acquisition; pro-forma group revenue 145,521 | FY2022 | as stated | EUR m | AR2022 note 3 |
| BBA (100%) revenue / profit after tax | FY2016 … FY2021 | 12,991 / 1,031 · 14,628 / 1,337 · 17,766 / 1,561 · 21,910 / 1,947 · 23,913 / 2,560 · 28,001 / 3,596 | EUR m | each AR, equity-method note (FY2016 PAT from AR2017 prior-year column) |
| Euro-area HICP, annual average rate of change | 2016 … 2025 | 0.2 / 1.5 / 1.8 / 1.2 / 0.3 / 2.6 / 8.4 / 5.4 / 2.4 / 2.1 | % | Eurostat `prc_hicp_aind`, geo EA, coicop CP00, unit RCH_A_AVG (API JSON, retrieved 2026-11-10) |
| 9M 2026 / 9M 2025: revenue 92,718 / 99,999; EBIT 5,224 / 8,064; PBT 6,128 / 8,056; CFO 4,060 / 7,592; capex −5,436 / −7,626; leased products and sales-financing receivables (one line) −4,469 / −4,674 | 9M | as stated | EUR m | Q3 2026 statement, Group income statement and condensed cash flow statement |
| 30 Sep 2026: cash 19,278; financial liabilities non-current 72,437, current 46,210; pension provisions 195; equity attributable 96,173; NCI 2,106; total equity 98,279; treasury shares 24,676,720 | 30 Sep 2026 | as stated | EUR m / shares | Q3 2026 statement, Group balance sheet and p. 12 |
| Group refinancing mix, 31 Dec 2025 (derived from the financial liabilities note): bonds 49.9%, ABS 21.0%, customer deposits 17.3%, banks 8.5%, commercial paper 3.3% | FY2025 | as stated | % | AR2025 note 36 (derived shares) |
| Segment figures FY2016–FY2025 (Automotive and Motorcycles: EBIT and capital employed; FS: profit before tax and net assets) | FY2016 … FY2025 | B4 below | EUR m | each AR, note "Segment information"; capital-employed definition changed from FY2022, Automotive 31.12.2021 restated 17,466 → 41,617 (AR2022) |
| Board of Management pay, largest per-person total (Zipse, §162 AktG "granted and owed" + service cost) | FY2023 / FY2024 / FY2025 | 8,158,904 + 712,729 = 8,871,633 · 4,976,840 + 711,077 = 5,687,917 · 5,784,538 + 750,000 = 6,534,538 | EUR | AR2023–AR2025 Remuneration Report, tables of remuneration granted and owed |
| Supervisory Board, highest fee | FY2023 / FY2024 / FY2025 | Reithofer (chair) 610,000 / 610,000; FY2025 Bock 460,000 | EUR | AR2023–AR2025 Remuneration Report, Supervisory Board tables |
| Board of Management shareholdings | 31 Dec 2025 | 144,806 shares in total (Zipse 56,308; Goller 3,803; Horstmeier 30,271; Martin 0; Mertl 7,238; Nedeljković 30,369; Post 16,817) | shares | AR2025 Remuneration Report, share-ownership guideline table |
| Voting rights: Stefan Quandt 0.2% direct + 27.52% indirect; Susanne Klatten 0.2% + 22.35% (ordinary voting shares, before the conversion) | 31 Dec 2025 | as stated | % | AR2025, notifications of voting rights |
| Buybacks: Programme 1 (Jul 2022–Jun 2023) 22,199,529 ord + 1,923,871 pref, €2.0bn (H2 2022: 15,312,007 + 1,448,950 for €1,278m); Programme 2 (Jul 2023–Apr 2025) 18,660,741 ord at avg €88.42 + 4,244,903 pref at €82.45, €2.0bn; Programme 3 tranche 1 (21 May–8 Dec 2025) 7,498,153 ord at €82.02 + 1,773,313 pref at €76.13, ≈ €750m; tranche 2 (2 Jan–26 Jun 2026) 8,252,475 ord, ≈ €625m; tranche 3 €625m from 1 Jul 2026 | 2022–2026 | as stated | shares, EUR | AR2022–AR2025 (equity / treasury-share sections, note on equity); Q3 2026 p. 12. No buyback programme FY2016–FY2021 |
| No filer statement ruling out a customer at ≥ 10% of revenue was found in AR2024 or AR2025 (segment information note, risk report searched) | FY2024–FY2025 | none | — | AR2024, AR2025 |
| Deliveries: China −12.5% in 2025, 25.4% of group deliveries (2024: 29.2%); Q3 2026 China sales −24.8%; Automotive EBIT margin 9.8% (2023), 6.3% (2024), 5.3% (2025) | 2023–2026 | as stated | % | AR2025 combined management report (deliveries by region; Automotive segment); Q3 2026 p. 8–9 |

### Gate 0 and the lens

- **Group sentence (best the filings allow).** BMW AG is a Munich-headquartered group, founded in 1916 and controlled in votes by the Quandt and Klatten families. It designs, makes and sells premium passenger cars under the BMW, MINI and Rolls-Royce brands, plus BMW Motorrad motorcycles. The vehicles are sold mainly to independent and own dealers, with MINI on an agency model and the BMW brand moving to direct sales from 2027; the final buyers are private and fleet customers worldwide (2025 deliveries: Europe 41%, China 25%, Americas 21%). Its captive Financial Services arm leases and finances those vehicles for retail customers, finances dealers, and takes deposits through BMW Bank (AR2025 combined management report, "BMW Group business model", Automotive and Financial Services segment descriptions).
- **Units (P22).** Automotive: material. Financial Services: material; FY2025 revenue 39,806 ÷ group 133,453 = 29.8%. It is a captive finance arm (R2): the filer describes it as financing BMW Group vehicles, it financed or leased 46.6% of new BMW Group vehicles in 2025, and no non-group-brand share of its book is printed. Motorcycles: immaterial (2.4% of revenue, 0.7% of assets, 1.8% of Σ positive segment results, FY2025), named in one line. Other Entities: the holding and group-financing companies (segment note), not a unit; it stays in the consolidated record.
- **Listed parts.** No controlled listed subsidiary. No material listed holding: equity-method investments were 526 and other investments 891 at FY2025 (YOUR NOW, IONITY, IONNA, Solid Power, THERE; AR2025 note 24), each far below 10% of MCap. `holding_keys` n.m., `core_credit` 0, no `## Group dependency` line.
- **P30.** The filings show what the company sells and who pays for it for all of revenue. There is no Gate-0 ground.
- **Lens.** BMW AG is not a bank or insurer, nor the parent of a group supervised on a consolidated basis as one, so the lens is not FI. It is STD. Financial Services is a captive finance arm, consolidated (R2), and it is not lens case (b): customer deposits are 17,952 of 110,469 financial liabilities (16.3%), so the bank is not funded mainly by deposits. The bank's liquidity is not split from group cash in the filings. J13: the cash variants carry group cash, logged.

### P31 test (G6) and the two readings

- **Classes:** equity-accounted investments (BBA until 10 Feb 2022, then YOUR NOW, IONITY, IONNA, Solid Power, THERE and others), plus other investments (participations and non-consolidated subsidiaries, S3).
- **Asset limb:** at most 5,112 + 1,241 = 6,353, which is 2.8% of total assets (FY2021). It holds.
- **Income limb:** fails. FY2020: (920 + 48) ÷ 4,830 = 20.0%; FY2021: (1,520 + 584) ÷ 13,400 = 15.7%; FY2017: (738 + 14) ÷ 9,880 = 7.6%. The classes are therefore **above the P31 line**, and two readings were built.
- **Exclude reading:** OI = EBIT. FCF = the build below, with no dividends added. CE excludes the equity-method and other investments.
- **Include reading:** OI = EBIT + equity-method result + result on investments. The FY2022 result on investments is taken as 7,770 − 7,649 (the BBA remeasurement gain stays out) = 121. A negative result on investments is a net loss on class assets and stays in. FCF = exclude FCF + dividends received from investment assets (booked in investing; moved into CFO). CE keeps the classes.
- Interest income is on the company's own cash and securities and is not attributed to a class, so it is out on both readings.

### J1 OI line

The Group income statement runs revenues → cost of sales → gross profit → selling and administrative expenses → other operating income and expenses → **profit before financial result (EBIT)** → financial result → profit before tax. EBIT is the lowest operating subtotal; no adjusted subtotal is used. FS interest income and expense sit in revenues and cost of sales, so EBIT is after the captive arm's funding cost (R2). Net interest on the defined-benefit liability is booked in the financial result (AR2025 note "Financial result") and, being a net cost, stays out of OI. The equity-method result, interest income and other financial result sit below EBIT, so the exclude reading needs no removal from OI.

### NIBCL, cash and the CE build

- **NIBCL** = trade payables + current tax liabilities + deferred income + contract liabilities + advance payments received. These are the first-reported values; the default burden-of-proof list is used.
- Left in CE (logged): other taxes, social security, other provisions (warranty, personnel) and the other "other liabilities".
- **Cash + STI** = cash and cash equivalents + 0.9 × marketable securities and investment funds. The securities are taken at market × 0.9 because their composition (money-market funds and bonds) is not split (J13).
- **FY2025 latest-year build:**
  - CE_wc (include) = 265,967 − 25,478 = 240,489.
  - CE_wc (exclude) = 240,489 − 526 − 891 = 239,072.
  - CE_xc (exclude) = 239,072 − 18,854 − 626.4 = 219,591.6.
- **TBV FY2025** = 95,697 − 19,915 = 75,782. All intangible assets are deducted, capitalised development included.
- **L/E FY2025** = (265,967 − 95,697 − 2,209) ÷ 95,697 = 175.6%. This counts all liabilities, customer deposits and FS funding included; there are no segregated customer funds to net.

### P20 and R2 build (per year)

k = Σ net fixed capital ÷ Σ revenue, FY2016–FY2025:
- Net fixed capital = PP&E − right-of-use + capitalised development = 358,774.
- Σ revenue = 1,178,701.
- k = 0.3044.

Rules applied:
- **Software:** not split out of other intangibles, so it is excluded from both k and the floor (logged).
- **Leased products:** they are vehicles on lease, a book (R2), and stay out of net fixed capital.
- **FY2022 deal year:** BBA's revenue since acquisition (28,031) is printed, so organic revenue = 142,610 − 28,031 = 114,579. Real growth against 111,239 × 1.084 is nil, so the constructed tier is available.
- **Restated comparatives:** FY2018 is read against the restated FY2017 revenue (98,282, AR2018) and FY2019 against the restated FY2018 revenue (96,855, AR2019).
- **R2 book rule:** applied to the change the cash-flow statement carries in CFO, i.e. the change in leased products plus the change in receivables from sales financing, against ±3% of the prior year-end book (leased products + both receivables lines). The part beyond 3% leaves FCF.
- **Judgment logged:** the cash-flow book lines differ from the balance-sheet book change through FX, depreciation and disposals. The balance-sheet reading was not used; attended review may test it.
- **Customer deposits** and other funding principal sit in financing, so nothing leaves CFO for them.
- **J3:** interest received leaves CFO. Interest paid (non-FS, in financing) moves into CFO.

| FY | Revenue (organic basis) | π_t (max 3%, EA HICP) | Real growth | Growth capex (k × real growth) | Floor (PP&E dep. ex RoU + dev. amort.) | Capex | Maint. capex | Book change in CFO (leased products + sales-financing receivables) | ±3% of prior book | R2 add-back / (removal) | Interest received out | Interest paid in | CFO adj. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2016 | 94,163 | 3.0% (HICP 0.2%) | 0 | 0 | 4,625 | 5,823 | 5,823 | -10,894 | 3,150 | 7,744 | −142 | -118 | 10,657 |
| FY2017 | 98,678 | 3.0% (HICP 1.5%) | 1,690 | 514 | 4,631 | 7,112 | 6,598 | -8,574 | 3,481 | 5,093 | −125 | -165 | 10,712 |
| FY2018 | 97,480 | 3.0% (HICP 1.8%) | 0 | 0 | 4,918 | 7,777 | 7,777 | -7,363 | 3,501 | 3,862 | −170 | -136 | 8,607 |
| FY2019 | 104,210 | 3.0% (HICP 1.2%) | 4,449 | 1,354 | 5,402 | 6,902 | 5,548 | -7,385 | 3,761 | 3,624 | −91 | -199 | 6,996 |
| FY2020 | 98,990 | 3.0% (HICP 0.3%) | 0 | 0 | 5,456 | 6,150 | 6,150 | 3,176 | 4,051 | 0 | −163 | -275 | 12,813 |
| FY2021 | 111,239 | 3.0% (HICP 2.6%) | 9,279 | 2,824 | 5,809 | 6,619 | 5,809 | -317 | 3,788 | 0 | −130 | -217 | 15,556 |
| FY2022 | 114,579 (142,610 − BBA 28,031) | 8.4% (HICP 8.4%) | 0 | 0 | 6,433 | 9,050 | 9,050 | 4,682 | 3,964 | -718 | −453 | -222 | 22,130 |
| FY2023 | 155,498 | 5.4% (HICP 5.4%) | 5,187 | 1,579 | 6,681 | 10,881 | 9,302 | -4,621 | 3,856 | 765 | −683 | -186 | 17,438 |
| FY2024 | 142,380 | 3.0% (HICP 2.4%) | 0 | 0 | 6,321 | 12,205 | 12,205 | -9,375 | 3,914 | 5,461 | −644 | -196 | 12,187 |
| FY2025 | 133,453 | 3.0% (HICP 2.1%) | 0 | 0 | 6,435 | 10,963 | 10,963 | -8,519 | 4,277 | 4,242 | −518 | -245 | 11,707 |

Maintenance capex equals all capex in every year except FY2017, FY2019, FY2021 and FY2023. In FY2021 the floor bound (5,809).

### B1 raw inputs (exclude reading; EUR m)

Cash+STI = cash + 0.9 × marketable securities. Total liab. = total assets − total equity (NCI included).

| FY | Revenue | OI (J1, exclude) | CFO as reported | CFO adj. | Capex | Maint. capex | Basis | FCF (maint.) | FCF (all-capex) | Diluted sh. (m) | Total assets | NIBCL | Cash+STI | Total liab. | Equity (owners) | Goodwill+intang. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2015 | 92,175.0 | — | 960.0 | — | 5,889.0 | — | — | — | — | 656.49 | 172,174.0 | 16,270.0 | 10,856.9 | 129,410.0 | 42,530.0 | 7,372.0 |
| FY2016 | 94,163.0 | 9,386.0 | 3,173.0 | 10,656.8 | 5,823.0 | 5,823.0 | constructed | 4,833.8 | 4,833.8 | 656.80 | 188,535.0 | 17,819.0 | 12,638.3 | 141,172.0 | 47,108.0 | 8,157.0 |
| FY2017 | 98,678.0 | 9,880.0 | 5,909.0 | 10,711.5 | 7,112.0 | 6,597.6 | constructed | 4,114.0 | 3,599.5 | 657.11 | 193,483.0 | 19,085.0 | 13,941.3 | 138,935.0 | 54,112.0 | 9,464.0 |
| FY2018 | 97,480.0 | 9,121.0 | 5,051.0 | 8,607.3 | 7,777.0 | 7,777.0 | constructed | 830.3 | 830.3 | 657.60 | 208,980.0 | 24,207.0 | 15,763.4 | 150,892.0 | 57,559.0 | 10,971.0 |
| FY2019 | 104,210.0 | 7,411.0 | 3,662.0 | 6,996.4 | 6,902.0 | 5,547.7 | constructed | 1,448.6 | 94.4 | 658.12 | 228,034.0 | 20,403.0 | 16,887.9 | 168,127.0 | 59,324.0 | 11,729.0 |
| FY2020 | 98,990.0 | 4,830.0 | 13,251.0 | 12,813.0 | 6,150.0 | 6,150.0 | constructed | 6,663.0 | 6,663.0 | 658.86 | 216,658.0 | 18,561.0 | 17,340.4 | 155,138.0 | 60,891.0 | 12,342.0 |
| FY2021 | 111,239.0 | 13,400.0 | 15,903.0 | 15,556.0 | 6,619.0 | 5,809.0 | constructed | 9,747.0 | 8,937.0 | 659.68 | 229,527.0 | 21,788.0 | 19,827.7 | 154,395.0 | 74,366.0 | 12,980.0 |
| FY2022 | 142,610.0 | 13,999.0 | 23,523.0 | 22,129.5 | 9,050.0 | 9,050.0 | constructed | 13,079.5 | 13,079.5 | 656.96 | 246,926.0 | 26,865.0 | 19,964.2 | 155,638.0 | 87,125.0 | 21,776.0 |
| FY2023 | 155,498.0 | 18,482.0 | 17,542.0 | 17,438.2 | 10,881.0 | 9,302.2 | constructed | 8,136.0 | 6,557.2 | 638.72 | 250,890.0 | 28,542.0 | 19,280.0 | 157,967.0 | 89,596.0 | 20,022.0 |
| FY2024 | 142,380.0 | 11,509.0 | 7,566.0 | 12,186.8 | 12,205.0 | 12,205.0 | constructed | -18.2 | -18.2 | 627.34 | 267,732.0 | 27,584.0 | 20,610.0 | 172,729.0 | 92,315.0 | 20,220.0 |
| FY2025 | 133,453.0 | 10,186.0 | 8,228.0 | 11,707.3 | 10,963.0 | 10,963.0 | constructed | 744.3 | 744.3 | 613.54 | 265,967.0 | 25,478.0 | 19,480.4 | 168,061.0 | 95,697.0 | 19,915.0 |

### B2 returns, both G6 readings (beginning-of-period CE per year), and the summary rows (Σ numerator ÷ Σ CE)

| FY | CE_wc excl. | CE_xc excl. | ROCE_wc excl. | ROCE_xc excl. | FCFROCE_wc excl. | FCFROCE_xc excl. | OI incl. | FCF incl. | CE_wc incl. | CE_xc incl. | ROCE_wc incl. | ROCE_xc incl. | FCFROCE_wc incl. | FCFROCE_xc incl. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2016 | 153,243.0 | 142,386.1 | 6.1% | 6.6% | 3.2% | 3.4% | 9,648.0 | 4,967.8 | 155,904.0 | 145,047.1 | 6.2% | 6.7% | 3.2% | 3.4% |
| FY2017 | 167,610.0 | 154,971.7 | 5.9% | 6.4% | 2.5% | 2.7% | 10,632.0 | 4,372.0 | 170,716.0 | 158,077.7 | 6.2% | 6.7% | 2.6% | 2.8% |
| FY2018 | 170,941.0 | 156,999.7 | 5.3% | 5.8% | 0.5% | 0.5% | 9,909.0 | 1,214.3 | 174,398.0 | 160,456.7 | 5.7% | 6.2% | 0.7% | 0.8% |
| FY2019 | 181,410.0 | 165,646.6 | 4.1% | 4.5% | 0.8% | 0.9% | 7,627.0 | 2,091.6 | 184,773.0 | 169,009.6 | 4.1% | 4.5% | 1.1% | 1.2% |
| FY2020 | 203,729.0 | 186,841.1 | 2.4% | 2.6% | 3.3% | 3.6% | 5,798.0 | 7,683.0 | 207,631.0 | 190,743.1 | 2.8% | 3.0% | 3.7% | 4.0% |
| FY2021 | 193,777.0 | 176,436.6 | 6.9% | 7.6% | 5.0% | 5.5% | 15,504.0 | 9,747.0 | 198,097.0 | 180,756.6 | 7.8% | 8.6% | 4.9% | 5.4% |
| FY2022 | 201,386.0 | 181,558.3 | 7.0% | 7.7% | 6.5% | 7.2% | 14,020.0 | 13,079.5 | 207,739.0 | 187,911.3 | 6.7% | 7.5% | 6.3% | 7.0% |
| FY2023 | 218,290.0 | 198,325.8 | 8.5% | 9.3% | 3.7% | 4.1% | 18,266.0 | 8,136.0 | 220,061.0 | 200,096.8 | 8.3% | 9.1% | 3.7% | 4.1% |
| FY2024 | 220,708.0 | 201,428.0 | 5.2% | 5.7% | -0.0% | -0.0% | 11,346.0 | -18.2 | 222,348.0 | 203,068.0 | 5.1% | 5.6% | -0.0% | -0.0% |
| FY2025 | 238,496.0 | 217,886.0 | 4.3% | 4.7% | 0.3% | 0.3% | 10,195.0 | 744.3 | 240,148.0 | 219,538.0 | 4.2% | 4.6% | 0.3% | 0.3% |

| Reading · metric · window | beg wc | end wc | beg xc | end xc | worst of four |
|---|---|---|---|---|---|
| Exclude · ROCE · FY2016–25 | 5.6% | 5.3% | 6.1% | 5.8% | 5.3% |
| Exclude · ROCE · FY2021–25 | 6.3% | 6.0% | 6.9% | 6.6% | 6.0% |
| Exclude · FCFROCE · FY2016–25 | 2.5% | 2.4% | 2.8% | 2.7% | 2.4% |
| Exclude · FCFROCE · FY2021–25 | 3.0% | 2.8% | 3.2% | 3.1% | 2.8% |
| Include · ROCE · FY2016–25 | 5.7% | 5.5% | 6.2% | 6.0% | 5.5% |
| Include · ROCE · FY2021–25 | 6.4% | 6.1% | 7.0% | 6.7% | 6.1% |
| Include · FCFROCE · FY2016–25 | 2.6% | 2.5% | 2.9% | 2.8% | 2.5% |
| Include · FCFROCE · FY2021–25 | 2.9% | 2.8% | 3.2% | 3.1% | 2.8% |
| Exclude · FCFROCE all-capex (context) · FY2016–25 | 2.3% | 2.2% | 2.5% | 2.4% | 2.2% |

### B3 growth and leverage (per average diluted share: ordinary + preferred, basic = diluted in every year)

| FY | ΔOI/sh % excl. | ΔFCF/sh % excl. | ΔOI/sh % incl. | ΔFCF/sh % incl. | ΔBV/sh % | ΔTBV/sh % | L/E |
|---|---|---|---|---|---|---|---|
| FY2016 | — | — | — | — | 10.7 | 10.7 | 299.7% |
| FY2017 | 5.2 | -14.9 | 10.1 | -12.0 | 14.8 | 14.6 | 256.8% |
| FY2018 | -7.8 | -79.8 | -6.9 | -72.2 | 6.3 | 4.3 | 262.2% |
| FY2019 | -18.8 | 74.3 | -23.1 | 72.1 | 3.0 | 2.1 | 283.4% |
| FY2020 | -34.9 | 359.4 | -24.1 | 266.9 | 2.5 | 1.9 | 254.8% |
| FY2021 | 177.1 | 46.1 | 167.1 | 26.7 | 22.0 | 26.3 | 207.6% |
| FY2022 | 4.9 | 34.7 | -9.2 | 34.7 | 17.6 | 6.9 | 178.6% |
| FY2023 | 35.8 | -36.0 | 34.0 | -36.0 | 5.8 | 9.5 | 176.3% |
| FY2024 | -36.6 | n.m. | -36.8 | n.m. | 4.9 | 5.5 | 187.1% |
| FY2025 | -9.5 | n.m. | -8.1 | n.m. | 6.0 | 7.5 | 175.6% |


### B4 division table (segment figures; EUR m)

| Part | Kind | Revenue FY2023 / FY2024 / FY2025 | Segment result FY2023 / FY2024 / FY2025 | Segment assets FY2023 / FY2024 / FY2025 | Weight base (3-yr avg EBIT) | Weight |
|---|---|---|---|---|---|---|
| Automotive | unit | 132,277 / 124,917 / 117,557 | EBIT 12,981 / 7,893 / 6,259 | capital employed 66,168 / 70,804 / 69,481 | 9,044.3 | 77.3% |
| Financial Services | captive finance unit | 36,227 / 38,562 / 39,806 | EBIT 3,055 / 2,511 / 2,411 (PBT 2,962 / 2,538 / 2,401) | net assets 16,573 / 16,954 / 16,444 | 2,659.0 | 22.7% |
| Motorcycles | immaterial unit | 3,214 / 3,220 / 3,143 | EBIT 259 / 198 / 178 | 1,190 / 1,298 / 1,331 | — | — |
| Other Entities | holding and group financing, not a unit | 11 / 14 / 12 | PBT −100 / 837 / 1,087 | — | — | — |

Source: AR2024 and AR2025 note "Segment information" and the segment columns of the Group income statement; FY2021 Automotive capital employed restated 41,617 (AR2022), FS net assets FY2021 17,324.

Growth reads (derived):

| Reading · metric | (i) geometric | (ii) three-year endpoint |
|---|---|---|
| Exclude · ΔOI/sh | 1.7% | 5.7% |
| Exclude · ΔFCF/sh | n.m. (FY2024 FCF ≤ 0) | −0.9% |
| Include · ΔOI/sh | 1.4% | 4.7% |
| Include · ΔFCF/sh | n.m. | −2.0% |

- **ΔFCF/sh:** read (ii) governs because read (i) is n.m.; the lower reading is −2.0%.
- **ΔOI/sh:** the harsher read on the lower reading is 1.4%.

J6 sustained decline, limb (b) (latest-three-year pooled worst-of-four ÷ the window's):

| Reading | ROCE | FCFROCE |
|---|---|---|
| Exclude | 5.8% vs 5.3% | 1.3% vs 2.4% (ratio 0.52) |
| Include | 5.7% vs 5.5% | 1.3% vs 2.5% (ratio 0.50) |

- **FCFROCE:** more than one third below the window on both readings. FY2025 is not a P28 year (below), so no re-read applies.
- **Limb (a)** was not tabulated.

### P28 (latest FY down?)

- **OI:** FY2025 EBIT 10,186 is below the 3-year average (13,392.3) and the 5-year average (13,515.2).
- **Causes the filer names:** US and EU tariffs (about 1.5 pp of the Automotive EBIT margin), China price competition and dealer support, and currency.
- None of these is an impairment, write-down, restructuring or disruption under P28 test 2, so P28 does not qualify and the latest year governs.
- **FCF:** FY2025 FCF 744.3 is below both averages (3y 2,954.0; 5y 6,337.8), with no named one-off cause, so it does not qualify either.

### Gate 1B (Appendix D inputs)

- **Weights (P29), latest-3-FY average segment result:**
  - Automotive EBIT (12,981 + 7,893 + 6,259) ÷ 3 = 9,044.3.
  - FS EBIT (3,055 + 2,511 + 2,411) ÷ 3 = 2,659.0. This is the FS profit before financial result, after its funding cost, printed in the segment columns of the Group income statement (AR2024, AR2025).
  - Weights: Automotive 77.3%, FS 22.7%.
- **Breadth, group:** no customer statement was found.
  - Automotive sells mainly wholesale to dealers, i.e. to organisations, so silence is concentration (P15).
  - FS lends to retail customers and finances dealers; dealers that borrow are customers (R7), so silence there too.
- **Automotive, readings:**
  - Dominance is not evidenced: there are several premium rivals, and the filer names its premium-segment share as 21.7% (AR2024 CEO letter). The strong-moat carry therefore fails condition (1), and the silence reads as a STRONG customer-power call.
  - New entrants: local Chinese makers drive the China market and price war (AR2024 and AR2025 market sections). BMW's China deliveries fell 12.5% in 2025 and its Q3-2026 China sales fell 24.8%. The Automotive EBIT margin went 9.8% → 6.3% → 5.3% (2023–2025), with 4–6% guided for 2026. No containment mechanism is named.
  - Moat: brand. Stable outside China, eroding in China on the figures above.
  - Market growth: global car market +3.3% in 2024 and 2025; China contracting in 2026. MIXED.
- **FS, readings:** looking the group treasury through to the group's external funding, the capital-market channel (bonds 49.9% + ABS 21.0% + bank loans 8.5% + CP 3.3% = 82.7%) is above 50%. That is `funding conc.` under P15 (strict).

### Gate 1C (Appendix E inputs)

- **Pay (P17):**
  - Hairiest number: Zipse FY2023, 8,871,633 (§162 total + service cost).
  - Group P17 denominator: the lower of NI attributable and maintenance-capex FCF × parent share. FY2024: NI 7,290; FCF −18.2 × (7,290 ÷ 7,678) = −17.3, which is ≤ 0. The loss-year limb applies: Zipse's FY2024 year total of 5,687,917 is above the outside-director cap (≈ US$666k), so the reading is a **flag**.
  - It is not a strike: the trailing FY2022–FY2024 leg is positive.
  - FY2023: the line is 5% × min(11,290, 8,136.0 × 0.928 = 7,550) = 377.5m. FY2025: 5% × 744.3 × 0.979 = 36.4m. Both are far above pay.
  - Absolute line: below US$40m. No big grant was printed.
- **Directors:**
  - Highest fee: Reithofer FY2023 and FY2024, €610,000.
  - Home benchmark not set. Cap ≈ US$666k (2026 CPI-indexed).
  - At the ECB rate of 2026-11-10 (1.1214, frankfurter) the fee is US$684k, above the cap. At the 2024 average ECB rate (1.0825) it is US$660k, under it.
  - J13: the harsher reading governs, so **flag** (director pay; a second behaviour). Logged for attended confirmation.
- **Alignment:** management holds 144,806 shares, 0.02% of 615.8m; its value at px is owed. It is below 1%, and ≥ 10× the hairiest number would need about €88.7m, so the call is NOT ALIGNED at any plausible px.
  - Votes vs economics: the Quandt and Klatten pools together held 50.27% of ordinary votes against roughly 45.9% economic (ordinary 561.1m of 615.8m shares), a ratio of 1.10 < 1.25. Since 30 Jun 2026 there is one class. Not separated.
- **RPT:** dealings with Quandt/Klatten entities (DELTON, SOLARWATT, UnternehmerTUM, ALTANA) are each under about €33m a year (AR2023–AR2025 related-party note). This is below P27 materiality against the expense line, but against the group P17 denominator in FY2024 (≤ 0) P27 is not met by the FCF leg. Logged for attended review.
- **Acquisition stop:** no deal above 1% of EV in FY2023–FY2026. Earlier in the window, BBA 2022: €3,735m for 25%, against BBA FY2021 profit after tax 3,596 × 25% = 899, i.e. 4.2× after-tax profit. That is below worth on any reading, under CEO Zipse (in office until 13 May 2026).
- **Allocation across the parts:** the window runs FY2021 (restated) to FY2025 on the FY2022 capital-employed definition.
  - Pooled FY2023–FY2025 return: Automotive 27,133 ÷ 206,453 = 13.1%; FS profit before tax 7,901 ÷ net assets 49,971 = 15.8%. Both are above 10%.
  - Growth: Automotive 41,617 → 69,481 (+27,864); FS 17,324 → 16,444 (shrank). All growth went to a unit above the line, so no `reinvestment` finding.
- **Buybacks:** material in every year from FY2022 (each above 1% of average diluted shares).
  - Derived average prices: H2 2022 €76.25; programme 2 €88.42 ord / €82.45 pref; programme 3 tranche 1 €82.02 / €76.13; tranche 2 ≈ €75.7.
  - Indicative trailing-3-FY reads at the year-end balance sheets (not the governing point-in-time reads):
    - MCap/FCF is below 16 in each year (FY2026 purchases ≈ 75.7 × ≈ 600m ÷ 2,954 ≈ 15.4, close to worth).
    - EV/OI on the funding-in pairing reaches ≈ 15–16 for early-2023 purchases read on FY2019–FY2021 figures, above the 14 worth line.
  - The governing reads need the interim balance sheets: scope still owed.

### Gate 2 inputs (px owed)

- **N:** 615,810,431 issued − 24,676,720 treasury (30 Sep 2026) = 591,133,711; basic = diluted.
- **Funding pairing** (FS funding is a debt-equivalent):
  - Pairing B, funding in EV with OI before funding cost: D = financial liabilities 118,647 (non-current 72,437 + current 46,210; leases, deposits and any derivative liabilities inside, not split at Q3: J13 includes them) + pensions 195 + NCI at book 2,106 (BBA's minority, unlisted) = 120,948. OI = FY2025 EBIT 10,186 + FS interest expense 5,196 = 15,382. The FS interest is not printed for 9M 2026, so no TTM for this pairing; FY2025 stands.
  - No-cash leg: (7 × 15,382 − 120,948) ÷ N = −22.46, i.e. **n.m.** The OI level that restores the bound is 120,948 ÷ 7 = 17,278.3.
  - All-cash leg: (107,674 − 120,948 + 19,278) ÷ N = 10.16, context.
  - Pairing A (funding out of EV, OI after funding cost, TTM EBIT 7,346): its band is higher. The lower band governs, so pairing B governs.
- **FCF leg:**
  - TTM Q3-2026 FCF (derived): CFO 8,228 − 7,592 + 4,060 = 4,696.
  - R2 book change (−8,519 + 4,674 − 4,469 = −8,314) less 3% of the 31 Dec 2025 book (143,063 × 3% = 4,291.9) gives an add-back of 4,022.1.
  - Capex 10,963 − 7,626 + 5,436 = 8,773, all maintenance (TTM revenue 126,172 is below FY2025's).
  - TTM FCF = −54.9. The 9M interest received and paid are not printed; the J3 removals would lower it further.
  - TTM is lower than FY2025 (744.3), so TTM governs. FCF ≤ 0, so MCap/FCF is n.m. and the FCF leg is n.m.
- **Averages on pairing B:** OI 3y 17,943.0, 5y 16,997.0. FCF 3y 2,954.0, 5y 6,337.8.
- **Context:** BV/sh (30 Sep 2026) = 96,173 ÷ N = 162.69; TBV/sh using FY2025 intangibles = 129.00.


### Interim balance sheets for the point-in-time worth reads (EUR m; Group balance sheet of each quarterly statement)

Source files: `https://www.bmwgroup.com/content/dam/grpw/websites/bmwgroup_com/ir/downloads/en/{year}/q{n}/…` as listed on the IR "company reports" page (2022 Q1 `BMW-Group-Q1-2022-en.pdf`; 2022 Q2–2025 Q3 `BMW_Q{n}-{year}_EN.pdf`; 2026 Q1/Q2 `BMW_Q{n}-2026-EN.pdf`), all HTTP 200 on 2026-11-10. The "File" column names the PDF; "l." is the text line of its pdftotext layout and serves only as a locator. The filer prints no marketable-securities line on the balance sheet, so financial assets (derivatives and loans inside) are shown and are not cash (J13). No report prints its publication date, so the next run takes each date from the IR financial calendar or the filer's results press release. Buyback purchases are printed cumulatively per programme or tranche, never by month, so a tranche-year that spans a publication date is read on both sets of figures (§2·1C·3).

| Quarter-end | File | Fin. liab. NC | Fin. liab. C | Pension prov. | Minority / NCI | Equity attrib. to BMW AG shareholders | Total equity | Cash & cash equiv. | Financial assets NC | Financial assets C | Total assets |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 31.3.2022 | BMW-Group-Q1-2022-en.txt | 61,856 (l.1180) | 42,768 (l.1186) | 969 (l.1177) | 5,132 "Minority interest" (l.1174) | 85,133 (l.1172) | 90,265 (l.1175) | 20,644 (l.1115) | 2,735 (l.1104) | 6,407 (l.1112) | 252,483 (l.1118) |
| 30.6.2022 | BMW_Q2-2022_EN.txt | 61,892 (l.1566) | 44,076 (l.1572) | 310 (l.1563) | 5,263 "Minority interest" (l.1560) | 84,069 (l.1558) | 89,332 (l.1561) | 22,241 (l.1489) | 2,190 (l.1478) | 6,033 (l.1486) | 255,334 (l.1492) |
| 30.9.2022 | BMW_Q3-2022_EN.txt | 59,552 (l.1588) | 46,043 (l.1594) | 286 (l.1585) | 5,620 "Minority interest" (l.1582) | 86,499 (l.1580) | 92,119 (l.1583) | 24,447 (l.1522) | 3,172 (l.1511) | 5,455 (l.1519) | 260,920 (l.1525) |
| 31.3.2023 | BMW_Q1-2023_EN.txt | 52,009 (l.1049) | 37,664 (l.1055) | 327 (l.1046) | 4,369 NCI (l.1043) | 89,487 (l.1041) | 93,856 (l.1044) | 17,178 (l.985) | 2,492 (l.974) | 5,193 (l.982) | 247,576 (l.988) |
| 30.6.2023 | BMW_Q2-2023_EN.txt | 52,603 (l.1424) | 43,438 (l.1430) | 229 (l.1421) | 4,303 NCI (l.1418) | 85,685 (l.1416) | 89,988 (l.1419) | 18,560 (l.1348) | 2,721 (l.1337) | 5,617 (l.1345) | 249,958 (l.1351) |
| 30.9.2023 | BMW_Q3-2023_EN.txt | 52,389 (l.1413) | 45,122 (l.1419) | 220 (l.1410) | 4,567 NCI (l.1407) | 88,402 (l.1405) | 92,969 (l.1408) | 23,115 (l.1347) | 1,935 (l.1336) | 4,021 (l.1344) | 255,233 (l.1350) |
| 31.3.2024 | BMW_Q1-2024_EN.txt | 54,386 (l.1204) | 40,752 (l.1214) | 228 (l.1198) | 3,477 NCI (l.1190) | 92,161 (l.1188) | 95,638 (l.1192) | 16,773 (l.1106) | 1,182 (l.1086) | 4,323 (l.1100) | 254,325 (l.1110) |
| 30.6.2024 | BMW_Q2-2024_EN.txt | 57,726 (l.1607) | 44,534 (l.1617) | 226 (l.1601) | 2,559 NCI (l.1593) | 90,915 (l.1591) | 93,474 (l.1595) | 17,856 (l.1499) | 1,045 (l.1479) | 3,339 (l.1493) | 259,096 (l.1503) |
| 30.9.2024 | BMW_Q3-2024_EN.txt | 60,457 (l.1502) | 46,376 (l.1512) | 235 (l.1496) | 2,637 NCI (l.1492) | 90,724 (l.1490) | 93,361 (l.1494) | 17,788 (l.1408) | 1,203 (l.1388) | 2,972 (l.1402) | 261,926 (l.1412) |
| 31.3.2025 | BMW_Q1-2025_EN.txt | 69,715 (l.1290) | 38,780 (l.1300) | 214 (l.1284) | 2,723 NCI (l.1280) | 93,771 (l.1278) | 96,494 (l.1282) | 19,682 (l.1196) | 1,239 (l.1176) | 2,205 (l.1190) | 265,393 (l.1200) |
| 30.6.2025 | BMW_Q2-2025_EN.txt | 66,447 (l.1628) | 39,897 (l.1638) | 242 (l.1622) | 2,160 NCI (l.1618) | 91,790 (l.1616) | 93,950 (l.1620) | 18,085 (l.1526) | 2,179 (l.1506) | 3,022 (l.1520) | 259,708 (l.1530) |
| 30.9.2025 | BMW_Q3-2025_EN.txt | 67,013 (l.1597) | 40,735 (l.1607) | 219 (l.1591) | 2,201 NCI (l.1587) | 93,359 (l.1585) | 95,560 (l.1589) | 19,257 (l.1503) | 2,359 (l.1483) | 2,133 (l.1497) | 261,970 (l.1507) |
| 31.3.2026 | BMW_Q1-2026-EN.txt | 71,478 (l.1266) | 40,705 (l.1276) | 207 (l.1260) | 2,288 NCI (l.1256) | 97,267 (l.1254) | 99,555 (l.1258) | 19,011 (l.1172) | 2,440 (l.1152) | 2,673 (l.1166) | 270,624 (l.1176) |
| 30.6.2026 | BMW_Q2-2026-EN.txt | 73,953 (l.1575) | 42,836 (l.1585) | 203 (l.1569) | 2,092 NCI (l.1565) | 95,350 (l.1563) | 97,442 (l.1567) | 18,495 (l.1473) | 1,898 (l.1453) | 2,137 (l.1467) | 272,992 (l.1477) |

Year-end comparatives, as printed in the following Q1 statement:

| Year-end | Fin. liab. NC | Fin. liab. C | Pension prov. | NCI | Equity attrib. | Cash | Fin. assets NC | Fin. assets C | Source |
|---|---|---|---|---|---|---|---|---|---|
| 31.12.2021 | 62,342 | 41,121 | 1,247 | 766 | 74,366 | 16,009 | 1,715 | 5,800 | BMW-Group-Q1-2022-en.txt, the same lines as above |
| 31.12.2022 | 53,469 | 40,727 | 339 | 4,163 | 87,125 | 16,870 | 3,073 | 5,164 | BMW_Q1-2023_EN.txt, the same lines |
| 31.12.2023 | 52,880 | 42,130 | 427 | 3,327 | 89,596 | 17,327 | 1,387 | 4,131 | BMW_Q1-2024_EN.txt, the same lines |
| 31.12.2024 | 66,770 | 44,491 | 222 | 2,688 | 92,315 | 19,287 | 834 | 2,565 | BMW_Q1-2025_EN.txt, the same lines |
| 31.12.2025 | 68,159 | 42,310 | 203 | 2,209 | 95,697 | 18,854 | 2,568 | 2,460 | BMW_Q1-2026-EN.txt, the same lines |

### Corporate event after FY2025 (for the P28 test at the next fiscal year)

The press release "BMW Group accelerates realignment" (4 Nov 2026; IR Q3 2026 downloads, `2026/q3/Press_release_BMW_Group_accelerates_realignment.pdf`) announces portfolio and structural measures: an earlier phase-out of some Gen5 models and a faster cut in management functions. It prints no euro charge, job count or impairment. The only size given is a hit of about 2.5 pp to the Automotive EBIT margin in Q4 2026. Reported Automotive EBIT margin guidance for FY2026 is now −0.5% to +0.5% (previously 1–3%). This bears on the FY2026 P28 test (a restructuring needs operating evidence of recovery) and on the Automotive Future readings.

## 3. Readings settled (figures above; no grade or verdict stated)

- **Window:** FY2016–FY2025 (10 fiscal years, 11 balance sheets). STD lens. Group of two material units (Automotive 77.3%, FS 22.7%); no listed parts.
- **Past:** worst of eight ROCE 5.3% (exclude, ten-year, end-of-period wc); worst of eight FCFROCE 2.4%, on maintenance-capex FCF (all-capex context 2.2%). ΔOI/sh 1.4%, ΔFCF/sh −2.0% ((ii) governs). J6 limb (b) fires on FCFROCE. L/E 175.6%.
- **Future inputs:** Automotive has customer silence with no dominant moat, so a STRONG customer-power call, plus the new-entrant evidence in China. FS has funding concentration at 82.7% capital market.
- **SF inputs:** two flags on distinct behaviours, executive pay (FY2024 loss-year leg) and director pay (FY2024 chair fee, J13 FX reading). Alignment NOT ALIGNED; votes not separated. Acquisitions clear. No reinvestment finding. Buyback worth reads pending.
- **Gate 2:** EV/OI trigger leg n.m. (pairing B). TTM FCF ≤ 0.

## 4. Scope still owed (in order)

- [ ] Price endpoint: GET `BMW.DE` (record `currency`, `exchangeName`, instrument, close and date; `&events=split` since FY2016). It answered HTTP 429 on all fourteen tries on 2026-11-10 and three on 2026-11-06.
- [ ] Buyback worth table at the point of purchase. The interim balance sheets are tabled above. Still owed: each report's publication date (IR financial calendar or results press releases), then the trailing-3-FY reads on both EV variants and both funding pairings for each tranche-year (FY2022–FY2026), with the higher multiple governing each P19 read. A tranche-year that spans an annual-report publication date (programme 1 in early 2023, and every January–March tranche) is read on both sets of figures. Also run the sterilisation limb on the Employee Share Programme counts (AR notes on equity).
- [ ] Confirm the director-fee FX reading (Reithofer FY2024 €610k against ≈ US$666k) and the loss-year pay limb on the FY2024 FCF build. Both decide the SF ladder.
- [ ] J6 limb (a) table on each per-year series (B2 above).
- [ ] Write the memo (§6) from this record: Appendix D blocks for Automotive and FS, the B4 table, F with both funding pairings, the trigger `n.m.` with restoring OI, and `lint-memo` / `lint-row`.
