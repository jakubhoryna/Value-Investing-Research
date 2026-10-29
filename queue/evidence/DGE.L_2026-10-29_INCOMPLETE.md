# DGE.L — Diageo plc: REVIEW evidence (INCOMPLETE, 2026-10-29)

- Run: REVIEW 2026-10-29 21:13 (Europe/Prague) · base ffaa52c04a767e38ec1b22c6300da1a5294a48fb · MODEL v4.7.0
- **Named gap: data access — the price endpoint returned HTTP 429 for the whole run**, so `px` and every multiple at px (MCap/FCF, EV/OI, the averaged readings, MCap/BV) are missing (README §5, D3). **No verdict.** The current memo (v1, 2026-10-04) stands.
- What follows are the worksheets the v4.5.0 and v4.6.0 re-test built at FY2026 figures: sourced figures, computations and the gate findings they point to. They are orientation only for the next run (REVIEW.md step 4), never findings to copy. The next run needs only the DGE.L close (GBp), and ideally the United Spirits (UNITDSPR.NS) and Shuijingfang (600779.SS) market values for the NCI debt-equivalent, to finish the memo.
- Provisional readings, not a verdict:
  - Past WEAK (leverage; growth).
  - Future WEAK (four material units, each with a customer-concentration flag by silence; S = 1.0).
  - SF three flags (big grant, chair fee above the $666k cap, FY2024 buybacks clearly above worth) → flag pair.
  - Trigger n.m. on debt-equivalents ≥ $26,580m (restoring J1 OI $3,797m). The FCF leg is 8 × 2,787 ÷ 2,231 = $9.99 ≈ 750p at GBP/USD 1.3317.


## A. Sources & data gaps (hosts tried)

- **Primary (SEC EDGAR, Diageo plc CIK 835403), retrieved 2026-10-29 unless stated:**
  - Form 20-F FY2026 (filed 18 Aug 2026): statements, segment note, notes 3, 6, 9, 10, 12, 14–18, 21, remuneration report, NCI note, supply-chain finance disclosure.
  - Form 20-F FY2025, FY2024, FY2023, FY2021, FY2019 and FY2017: PP&E, right-of-use and intangible-asset notes (P20), associate carrying values, organic net-sales and volume KPIs, contingent-consideration remeasurements, remuneration tables.
  - XBRL companyfacts API (share of associates, dividends received, interest received, PP&E, other investments; cross-checked against the 20-F text for FY2024–FY2026).
  - Carried from v1 (2026-10-04): the FY2016–FY2026 B1 record (net sales, reported OI, CFO, capex, diluted shares, total assets, NIBCL, cash, total liabilities, equity, intangibles) from the FY2017–FY2026 20-Fs; Diageo's disclosed GBP/USD translation rates; the FY2018–FY2024 repurchase record; the KPMG *Guide to Directors' Remuneration* (Feb 2026) chair-fee median of £525k.
- **Price:** not retrieved: query1.finance.yahoo.com and query2.finance.yahoo.com returned HTTP 429 "Too Many Requests" on every call from 20:23 to 21:03 UTC (about 50 calls, spaced 60–90 s); stooq.com connection reset; api.nasdaq.com (DEO ADR) empty reply; markets.ft.com and Google Finance not fetchable. **FX:** GBP/USD 1.3317, USD/GBP 0.75093 (ECB ref, 2026-10-29, api.frankfurter.dev).
- **Documents:** 8 primary filings plus the XBRL API, the price endpoint and the FX endpoint. More than ten documents across the two runs, because the decade spans two presentation currencies.
- **Gaps:**
  - **NCI of listed subsidiaries at market (R5):** United Spirits (42.79% NCI, NSE) and Shuijingfang (36.35%, Shanghai) need their market value at px_date. Their prices could not be retrieved (HTTP 429), and no primary share count was found within the search budget. The debt-equivalents carry total NCI at book ($2,083m), a lower bound. The trigger (n.m.) and EXPENSIVE cannot move, because more debt only lowers the EV/OI leg. The printed EV/OI multiples are floors.
  - **Supply-chain finance** is disclosed for FY2025–FY2026 only ($1,006m, $1,092m). It is taken out of NIBCL in those years and stays in NIBCL earlier, which flatters CE before FY2025.
  - **Contingent-consideration fair-value gains** are disclosed from FY2020. FY2017–FY2019 removals are nil (not shown).
  - **FY2023 and FY2024 contingent-consideration gains:** two extractions disagree, $153m against $157m for FY2023 (both in the FY2024 20-F) and $155m against $156m for FY2024 (FY2024 against FY2025 20-F). The larger removal is used (J13).
  - **FY2016 maintenance-capex FCF** is not built (FY2016 organic data not retrieved), so the ΔFCF/sh geometric mean runs over nine rates (FY2018–FY2026). The endpoint read is unaffected.
  - **Executive Committee holdings** below Board level are not disclosed.
  - **Segment assets** are not printed in any year, so the allocation test is INDETERMINATE (b).
- **Unretrievable:** query1/query2.finance.yahoo.com returned HTTP 429 on the first calls (about 50 retries over 40 minutes, all HTTP 429).
- **P14:** 1 exploratory search (United Spirits share count, not found); 0 due-check operations. Everything else was primary documents, the XBRL API, the quote endpoint and the FX endpoint.

## B. Financial record (P1 window FY2017–FY2026; balance sheets FY2016–FY2026; native currency, m)

B1 Raw inputs (FY2017–FY2022 GBP; FY2022 also USD re-presented; FY2023–FY2026 USD). OI = J1 (reported operating profit less contingent-consideration fair-value gains). FCF (maint.) = CFO − dividends received − interest received − maintenance capex (the exclude reading and Gate 2); FCF (all-capex) = CFO − dividends received − interest received − capex.

| FY | Ccy | Net sales | Reported OI | J1 OI | CFO | Div. rec. | Int. rec. | Capex | Maint. capex | Basis | FCF (maint.) | FCF (all-capex) | Diluted sh | Total assets | NIBCL | Cash | Total liab | Equity | GW+intang |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2016 | GBP | 10,485 | 2,841 | 2,841 | 2,548 | 173 | 174 | 506 | — | not built | — | 2,201 | 2,518 | 28,491 | 3,631 | 1,089 | 18,311 | 8,530 | 12,370 |
| FY2017 | GBP | 12,050 | 3,559 | 3,559 | 3,132 | 223 | 180 | 518 | 474.1 | constructed | 2,254.9 | 2,211 | 2,523 | 28,848 | 3,782 | 1,191 | 16,820 | 10,313 | 12,566 |
| FY2018 | GBP | 12,163 | 3,691 | 3,691 | 3,084 | 159 | 167 | 584 | 492.2 | constructed | 2,265.8 | 2,174 | 2,495 | 29,715 | 4,089 | 874 | 18,002 | 9,948 | 12,572 |
| FY2019 | GBP | 12,867 | 4,042 | 4,042 | 3,248 | 168 | 216 | 671 | 564.5 | constructed | 2,299.5 | 2,193 | 2,428 | 31,296 | 4,453 | 932 | 21,140 | 8,361 | 12,557 |
| FY2020 | GBP | 11,752 | 2,137 | 2,137 | 2,320 | 4 | 185 | 700 | 700.0 | = all capex | 1,431.0 | 1,431 | 2,354 | 33,308 | 3,777 | 3,323 | 24,868 | 6,772 | 11,300 |
| FY2021 | GBP | 12,733 | 3,731 | 3,731 | 3,654 | 290 | 89 | 626 | 350.0 | constructed (floor) | 2,925.0 | 2,649 | 2,345 | 31,953 | 4,670 | 2,749 | 23,522 | 6,897 | 10,764 |
| FY2022 | GBP | 15,452 | 4,409 | 4,344 | 3,935 | 190 | 110 | 1,097 | 597.7 | constructed | 3,037.3 | 2,538 | 2,325 | 36,516 | 5,996 | 2,285 | 27,002 | 7,798 | 11,902 |
| FY2022 | USD | 20,516 | 5,897 | 5,810 | 5,213 | 238 | 146 | 1,457 | 793.8 | constructed | 4,035.2 | 3,372 | 2,325 | 44,183 | 7,255 | 2,765 | 32,672 | 9,435 | 14,401 |
| FY2023 | USD | 20,555 | 5,547 | 5,390 | 3,636 | 271 | 157 | 1,417 | 1,417.0 | = all capex | 1,791.0 | 1,791 | 2,271 | 44,883 | 6,549 | 1,813 | 33,174 | 9,856 | 14,506 |
| FY2024 | USD | 20,269 | 6,001 | 5,845 | 4,105 | 269 | 156 | 1,510 | 1,510.0 | = all capex | 2,170.0 | 2,170 | 2,239 | 45,474 | 6,132 | 1,130 | 33,404 | 10,032 | 14,814 |
| FY2025 | USD | 20,245 | 4,335 | 4,196 | 4,297 | 175 | 181 | 1,612 | 1,612.0 | = all capex | 2,329.0 | 2,329 | 2,228 | 49,322 | 5,669 | 2,200 | 36,144 | 11,090 | 14,776 |
| FY2026 | USD | 19,643 | 3,156 | 3,067 | 4,392 | 116 | 292 | 1,197 | 1,197.0 | = all capex | 2,787.0 | 2,787 | 2,231 | 46,845 | 5,106 | 1,520 | 33,891 | 10,871 | 13,375 |

Averages (USD, Gate 2): J1 OI 3-year (FY2024–26) **4,369.3**, 5-year (FY2022–26) **4,861.6**; maintenance-capex FCF 3-year **2,428.7**, 5-year **2,622.4** (all-capex 3-year 2,428.7).

Notes:
- NIBCL FY2025 and FY2026 exclude the supply-finance payables ($1,006m and $1,092m; v1 had 6,675 and 6,198).
- G6 class records (associates and joint ventures plus other investments; share of after-tax results; impairment of associates booked in OI): FY2016 2,528 + 31; FY2017 2,824 + 31, 309; FY2018 3,009 + 46, 309; FY2019 3,173 + 49, 312; FY2020 3,557 + 41, 282; FY2021 3,308 + 40, 334; FY2022 3,652 + 37 (GBP) / 4,418 + 45 (USD), 417 / 555; FY2023 4,825 + 71, 443; FY2024 5,032 + 94, 414; FY2025 5,334 + 39, 193, impairment 380; FY2026 5,284 + 21, 218, impairment 69 (65 exceptional + 4 underlying).

B2 Returns (YoY on beginning-of-period CE, native currency; both G6 readings; FCFROCE on maintenance-capex FCF)

| FY | Ccy | Exclude: CE_wc | CE_xc | ROCE_wc | ROCE_xc | FCFROCE_wc | FCFROCE_xc | Include: CE_wc | CE_xc | ROCE_wc | ROCE_xc | FCFROCE_wc | FCFROCE_xc |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2017 | GBP | 22,301 | 21,212 | 16.0% | 16.8% | 10.1% | 10.6% | 24,860 | 23,771 | 15.6% | 16.3% | 10.0% | 10.4% |
| FY2018 | GBP | 22,211 | 21,020 | 16.6% | 17.6% | 10.2% | 10.8% | 25,066 | 23,875 | 16.0% | 16.8% | 9.7% | 10.2% |
| FY2019 | GBP | 22,571 | 21,697 | 17.9% | 18.6% | 10.2% | 10.6% | 25,626 | 24,752 | 17.0% | 17.6% | 9.6% | 10.0% |
| FY2020 | GBP | 23,621 | 22,689 | 9.0% | 9.4% | 6.1% | 6.3% | 26,843 | 25,911 | 9.0% | 9.3% | 5.3% | 5.5% |
| FY2021 | GBP | 25,933 | 22,610 | 14.4% | 16.5% | 11.3% | 12.9% | 29,531 | 26,208 | 13.8% | 15.5% | 10.9% | 12.3% |
| FY2022 | GBP | 23,935 | 21,186 | 18.1% | 20.5% | 12.7% | 14.3% | 27,283 | 24,534 | 17.5% | 19.4% | 11.8% | 13.2% |
| FY2023 | USD | 32,465 | 29,700 | 16.6% | 18.1% | 5.5% | 6.0% | 36,928 | 34,163 | 15.8% | 17.1% | 5.6% | 6.0% |
| FY2024 | USD | 33,438 | 31,625 | 17.5% | 18.5% | 6.5% | 6.9% | 38,334 | 36,521 | 16.3% | 17.1% | 6.4% | 6.7% |
| FY2025 | USD | 34,216 | 33,086 | 13.4% | 13.8% | 6.8% | 7.0% | 39,342 | 38,212 | 11.2% | 11.5% | 6.4% | 6.6% |
| FY2026 | USD | 38,280 | 36,080 | 8.2% | 8.7% | 7.3% | 7.7% | 43,653 | 41,453 | 7.5% | 7.9% | 6.7% | 7.0% |

**Normalized averages (Σ OI ÷ Σ CE, USD; GBP years at Diageo's disclosed average and closing rates), ROCE / FCFROCE:**

| Window · reading | beg wc | beg xc | end wc | end xc | worst |
|---|---|---|---|---|---|
| P1 FY2017–26 · exclude | 14.7% / 8.6% | 15.7% / 9.2% | 14.4% / 8.4% | 15.4% / 9.0% | 14.4% / 8.4% |
| P1 FY2017–26 · include | 13.8% / 8.2% | 14.7% / 8.7% | 13.5% / 8.0% | 14.3% / 8.5% | **13.5% / 8.0%** |
| 5y FY2022–26 · exclude | 14.4% / 7.6% | 15.5% / 8.2% | 14.2% / 7.5% | 15.0% / 7.9% | 14.2% / 7.5% |
| 5y FY2022–26 · include | 13.3% / 7.2% | 14.2% / 7.7% | 13.1% / 7.1% | 13.7% / 7.4% | **13.1% / 7.1%** (governing) |

The harsher (include) reading governs. Level bars: ROCE 13.1% and FCFROCE 7.1% (worst of eight, lower window). They meet P3(b)'s 10% / 5.3% and miss P2's 15% / 8%. All-capex FCFROCE context (exclude reading): 8.0% on ten years, 7.1% on five. Latest three years pooled (J6 limb (b)): exclude 12.4% / 6.7% against the window's 14.4% / 8.4%; include 11.2% / 6.3% against 13.5% / 8.0%. That is 14–21% below, not more than a third.

B3 Growth & leverage (YoY per diluted share; GBP years chain-linked to USD at each metric's FY2022 USD/GBP re-presentation ratio)

| FY | ΔOI/sh exclude | ΔOI/sh include | ΔFCF/sh exclude | ΔFCF/sh include | ΔBV/sh | ΔTBV/sh | L/E |
|---|---|---|---|---|---|---|---|
| FY2017 | +25.0% | +26.1% | n.m. (FY2016 not built) | n.m. | +20.7% | n.m. | 163% |
| FY2018 | +4.9% | +4.6% | +1.6% | −1.0% | −2.5% | n.m. | 181% |
| FY2019 | +12.5% | +11.9% | +4.3% | +4.6% | −13.6% | n.m. | 253% |
| FY2020 | −45.5% | −42.7% | −35.8% | −40.0% | −16.5% | n.m. | 367% |
| FY2021 | +75.3% | +68.7% | +105.2% | +124.9% | +2.2% | n.m. | 341% |
| FY2022 | +17.4% | +18.1% | +4.7% | +1.2% | +14.0% | n.m. | 346% |
| FY2023 | −5.0% | −6.2% | −54.6% | −50.6% | +6.9% | n.m. | 337% |
| FY2024 | +10.0% | +8.8% | +22.9% | +20.0% | +3.2% | n.m. | 333% |
| FY2025 | −21.3% | −29.5% | +7.9% | +3.2% | +11.1% | n.m. | 326% |
| FY2026 | −31.6% | −25.3% | +19.5% | +15.8% | −2.1% | n.m. | 312% |

Reads (geometric mean / 3-year endpoint averages over 7 years):
- ΔOI/sh: exclude −0.7% / −0.1%; include −1.0% / −0.8%. **Harsher −1.0%.**
- ΔFCF/sh: exclude +0.6% / −1.6%; include 0.0% / −1.6%. **Harsher −1.6%.**
- ΔBV/sh: +1.7% / +0.4%. TBV is negative throughout (n.m.).

B4 Division table (filer segment note; $m; segment result = operating profit before exceptional items less the exceptional impairments and accelerated depreciation the note allocates to each segment)

| Part | Kind | Net sales FY24 / FY25 / FY26 | Segment result FY24 / FY25 / FY26 | Weight base (3y avg) | Weight | Future |
|---|---|---|---|---|---|---|
| North America | unit | 7,908 / 7,973 / 7,249 | 3,149 / 2,407 / 2,278 | 2,611.3 | 51.8% | WEAK |
| Europe | unit | 4,804 / 4,821 / 5,097 | 1,278 / 1,013 / 407 | 899.3 | 17.8% | WEAK |
| Asia Pacific | unit | 3,817 / 3,635 / 3,333 | 1,434 / 898 / 803 | 1,045.0 | 20.7% | WEAK |
| Latin America and Caribbean | unit | 1,839 / 1,847 / 2,160 | 502 / 525 / 427 | 484.7 | 9.6% | WEAK |
| Africa (immaterial) | — | 1,778 / 1,834 / 1,642 | 131 / 283 / 356 | — | — | — |

Allocated charges: FY2024 NA −87, Europe −101, APAC +371 (a brand-impairment reversal), LAC 0. FY2025 NA −646, Europe −289, APAC −32, LAC −3. FY2026 NA −323, Europe −1,205 (Türkiye), APAC −43, LAC −160. Restructuring is not allocated by segment (logged). Segment assets: not disclosed. **S = 0.518 × 1 + 0.178 × 1 + 0.207 × 1 + 0.096 × 1 = 1.0 → WEAK.** No material controlled listed subsidiary or listed holding, so no look-through additions.

## C. Calculation notes

- **Lens test.** No regulatory capital ratio, no licensed bank or insurer, no finance unit: **STD**.
- **J1 OI build.** The candidate subtotals are operating profit (face statement, after exceptional operating items) and operating profit before exceptional items (segment note, an APM). The lowest is reported operating profit: FY2026 $3,156m, after $2,527m of exceptional items (impairment $1,489m, restructuring $908m, distribution-model changes $75m, Irish pension increase $38m, litigation $17m). J3 removes the positive fair-value remeasurements of contingent consideration, earn-outs and equity options booked in marketing and other operating items: FY2022 £65m / $87m, FY2023 $157m, FY2024 $156m, FY2025 $139m, FY2026 $89m. The FY2020 (£7m) and FY2021 (£36m) losses stay in. Agave fair-value changes are an operating (IAS 41) item and stay in. Non-operating items (disposal gains and losses) and net finance charges, pension finance income included, sit below the line.
- **Financial income in CFO.** Diageo books dividends received (mainly associates) and interest received inside CFO. Interest received leaves FCF on every reading. Dividends received leave FCF on the exclude reading and at Gate 2, and stay on the include reading (cash the class brought in). Interest paid stays in CFO.
- **G6 classes and the P31 test.** The class is associates and joint ventures (Moët Hennessy 34%, Distill Ventures investees and others, with loans to associates inside "other investments and loans") plus other investments (S3).
  - The capital limb fails at every balance-sheet date: 9.0% (FY2016), 9.9%, 10.3%, 10.3%, 10.8%, 10.5%, 10.1% (FY2022), 10.9%, 11.3%, 10.9%, 11.3% (FY2026) of total assets.
  - The income limb (|include OI − exclude OI| ÷ exclude OI) is 8.7%, 8.4%, 7.7%, 13.2%, 9.0%, 9.6%, 8.2%, 7.1%, 4.1% and 4.8% (FY2017–FY2026).
  - Above the line, so both readings run.
  - **Exclude:** the class carrying value leaves CE (both cash variants). The FY2025 ($380m) and FY2026 ($69m) impairments of associates, booked in operating items, leave OI (exclude-reading OI FY2025 $4,576m, FY2026 $3,136m).
  - **Include:** the share of after-tax results is added to OI (FY2026 $3,285m) and dividends received stay in FCF. The impairments stay in OI. Capital stays in CE.
  - Loans to associates are a few tens of millions (FY2026 "other investments and loans" $53m, of which other investments $21m) and are not split by year: logged.
  - At Gate 2 the class earns no credit and its income stays out (J3).
- **CE build (FY2026, $m).** Total assets 46,845 − NIBCL 5,106 = **CE_wc 41,739**; − cash 1,520 = **CE_xc 40,219**. NIBCL = trade and other payables 6,425 − interest payable 434 − supply-chain-finance payables 1,092 + corporate tax payables 207. Interest payable stays in CE as financing. Provisions, excise and social-security payables, deferred income and dividends payable stay as booked. Goodwill and acquired brands stay in CE. Exclude reading: − class 5,305 → 36,434 / 34,914.
- **Leases.** IFRS 16 from FY2020 (lease liabilities $685m FY2026). Pre-adoption commitments were about 2% of assets (FY2019), below P18, so no capitalisation.
- **P20 maintenance capex (constructed tier; Diageo calls "a portion" of capex non-discretionary without a figure, so tier 1 is unavailable).**
  - k = Σ net fixed capital ÷ Σ net sales, FY2017–FY2026 in USD: 69,121 ÷ 181,547 = **0.3807**.
  - Net fixed capital = PP&E − right-of-use + computer software. In native currency: FY2017 4,194; FY2018 4,246; FY2019 4,594; FY2020 4,473; FY2021 4,511; FY2022 5,418 (GBP); FY2023 7,387; FY2024 8,226; FY2025 9,428; FY2026 8,861 (USD). GBP years are translated at closing rates, revenue at average rates.
  - Real growth = min(organic net-sales growth − π, organic volume growth) × prior-year net sales. π = 3% (the floor). UK CPI was below 3% in FY2017–FY2021 on ONS annual rates (a published series, not re-fetched). In FY2022 organic volume (10.3%) binds for any π below 11.1%.
  - FY2017: min(4.3−3, 1.1) = 1.1% → £115.3m → growth capex £43.9m → maint. £474.1m (floor £358m).
  - FY2018: min(2.0, 2.5) = 2.0% → £241.0m → £91.8m → £492.2m (floor £365m).
  - FY2019: min(3.1, 2.3) = 2.3% → £279.7m → £106.5m → £564.5m (floor £371m).
  - FY2021: min(13.0, 11.2) = 11.2% → £1,316.2m → £501.1m → £124.9m, below the floor → **£350m (floor bound:** owned depreciation £306m + software amortisation £44m).
  - FY2022: min(18.4, 10.3) = 10.3% → £1,311.5m → £499.3m → £597.7m (floor £387m). In USD: $1,457m × 597.7/1,097 = $793.8m.
  - FY2020 (organic −8.4%), FY2023 (volume −0.8%), FY2024 (organic −0.6%), FY2025 (organic +1.7%, below π) and FY2026 (organic −2.0%): no growth, maintenance = all capex.
  - Floors (owned PP&E depreciation + software amortisation) for the no-growth years: FY2020 £387m, FY2023 £385m, FY2024 $537m, FY2025 $602m, FY2026 $589m. All are below capex.
  - No year's deals exceed 1% of EV without organic disclosure.
- **TBV.** 10,871 − 13,375 = **−$2,504m**: MCap/TBV n.m. The deficit comes from acquired brands, so both qualifiers are distorted.
- **EV build ($m, 30 June 2026; no interim balance sheet since).**
  - MCap: n/a (px not retrieved); at a px of P pence it is P ÷ 100 × 2,231m × 1.3317.
  - Debt-equivalents **26,580**:
    - borrowings at principal 21,922 (long-term debt principal 21,771 + overdrafts 26 + short-term bank loans 125, above the 21,511 carrying amount);
    - leases 685;
    - loans and leases inside liabilities held for sale 272;
    - Ketel One put option 112;
    - contingent consideration 27;
    - post-employment deficits 387 (the $1,006m surpluses are never deducted);
    - supply-chain-finance payables 1,092;
    - NCI 2,083 at book: USL 755, other 1,328 (Shuijingfang, Ketel One, EABL; the market reading is owed, see Appendix A).
  - Cash 1,520. The $268m mutual fund is of undisclosed type, so it is not cash.
  - **EV no-cash n/a (px not retrieved); all-cash n/a (px not retrieved).**
  - Derivatives are not netted (conservative).
- **Leverage.** L/E = 33,891 ÷ 10,871 = **312%**, above 200% since FY2019 (peak 367% FY2020). P6 fails on both limbs: no other metric is at the P2 level, and the equity shrank through repurchases at 17–55× (Appendix E), not through buying clearly under-priced stock. Net debt ÷ maintenance-capex FCF is 7.0× (context).
- **Returns trend.** ROCE fell two years running (FY2024 → FY2026) on impairments and restructuring. FCFROCE rose from FY2023. No J6 limb fires.
- **Bias check.** Affinity and authority (famous brands, a celebrated new CEO): checked. The verdict rests on leverage, the customer-statement rule and two pay and repurchase facts. Consistency (v1 was PASS on SF): the SF move comes from the V3 cap and the maintenance-capex FCF reads, not from a changed view of management. Bias check: no other live bias.

## D. Future-performance worksheet

**Breadth (all units).**
- *Customers:* Diageo sells to wholesalers, distributors, control boards, retailers and on-trade operators, so organisations pay all of revenue. No filing statement or customer table rules out a customer above 10% of revenue (the segment note is silent, and silence is not a statement). Each unit carries a **customer-concentration flag** (`customer conc.`). The risk factors name "significant customers" and "increasingly powerful retailers".
- *Suppliers:* grain, agave, molasses, cream and glass from many named vendors, with own distilleries and maturing stocks: no supplier flag.

**Concentration worksheet (each unit).** For the strong-moat carry, condition (1), dominance by evidenced share with no competitor of comparable share, is not evidenced in any unit: Pernod Ricard, Bacardi, Suntory Global Spirits and local leaders hold comparable shares. Condition (2) fails in North America (an eroding franchise). Condition (3), pricing power over the unnamed customers, is not shown. So each flag is a **STRONG customer-power force** (P16). Distributor pass-through containment cannot be named without knowing who the customer is.

| Unit | Customer power | Supplier power | Substitutes | Entrants | Moat | Market | Grade |
|---|---|---|---|---|---|---|---|
| North America | STRONG (conc. flag; three-tier distributor consolidation) | WEAK | STRONG (moderation, GLP-1, RTDs, downtrading; US spirits price/mix −2.5%) | WEAK (aged stock, brand spend; celebrity tequila entrants logged) | brand, **eroding** (organic −8.4%, volume −6.7% FY2026; tequila −16%) | MIXED | WEAK · customer conc. |
| Europe | STRONG (conc. flag; retailer power named) | WEAK | STRONG (moderation, low/no alcohol) | WEAK (Guinness, Scotch scale) | brand, stable (organic +3.4% FY2026, positive price/mix) | MIXED | WEAK · customer conc. |
| Asia Pacific | STRONG (conc. flag; Indian state distribution corporations) | WEAK | STRONG (downtrading; Chinese white spirits policy hit, organic −6.3%) | WEAK | brand, eroding in Chinese white spirits, stable in India | MIXED | WEAK · customer conc. |
| Latin America and Caribbean | STRONG (conc. flag) | WEAK | WEAK (organic +7.7%, volume +3.1% FY2026) | WEAK | brand, stable | YES | WEAK · customer conc. |

Tally: three units at 2 STRONG (WEAK). LAC has one STRONG force with no nameable containment, because the concentrated customer is unknown (WEAK; "when in doubt, quit", Ch12). Every material part is WEAK, S = 1.0. **Group Future WEAK.** The heaviest WEAK part's reason is `customer conc.` (vocabulary order; North America's `moat eroding` and `2+ forces` are named here). Market: guidance of low-single-digit organic growth for FY2027–29 → MIXED.

## E. Shareholder-friendliness evidence

**Pay worksheet (three-year table FY2024–FY2026; UK single total figure, the printed per-person totals).**

| Person | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Debra Crew (CEO to Jul 2025) | $3,804k | $4,859k | £79k |
| Lavanya Chandrashekar (CFO to Sep 2024) | $3,296k | $546k | — |
| Nik Jhangiani (CFO from Sep 2024; interim CEO Jul–Dec 2025) | — | $12,285k (= £9,484k ≈ $12.7m at the FY2026 rate) incl. joining awards $10,224k (£7,893k: shares of £7.3m face plus £593k cash) | £2,615k ≈ $3.5m |
| Sir Dave Lewis (CEO from Jan 2026) | — | — | £1,429k ≈ $1.9m |

- **Hairiest number:** Jhangiani FY2025, **≈ $12.7m**. Pension is inside the single figure.
- Grant face values are printed per award, not as a total: Lewis FY2026 regular DLTIP, options £5,625k and performance shares £5,625k at joining; Jhangiani FY2026 £3,240k + £3,240k. They are logged. A derived grant-basis total for Lewis (≈ £12.7m ≈ $17m) is also below every line. The 20-F states no buy-out or one-off awards to Lewis.
- **Proportionality** (group P17 denominator, the lower of NI attributable and maintenance-capex FCF × parent share):
  - FY2024: lower(3,870, 2,170 × 0.929 = 2,016) → line $100.8m.
  - FY2025: lower(2,354, 2,329 × 0.927 = 2,160) → $108.0m.
  - FY2026: lower(1,737, 2,787 × 0.887 = 2,472) → $86.9m.
  - Trailing: lower(2,654, 2,216) → $110.8m.
  - The hairiest number is 0.15× the tightest line: pass. Taking associates' results out of NI lowers the FY2026 line to about $76m: still pass.
- **Absolute:** ≈ $40m: pass. **Home average:** home benchmark not set.
- **Big grant — FLAG.** Jhangiani's FY2025 joining arrangements (£7,893k, a make-whole for forfeited awards and bonus) are at least his regular annual total, the average of his other year in the table (FY2026 £2,615k). Strike test: 2× the trailing proportionality line ≈ $222m and 2× absolute ≈ $80m, so not a strike.
- **Executive findings: one behaviour, one flag (`compensation`).**

**Director worksheet.** Cap = lower(2 × UK chair median £525k = £1,050k ≈ $1.41m, ≈ $666k) = **$666k**. 2× cap = $1.33m.
- Chair: Sir John Manzoni FY2026 £704k ≈ **$944k** → **FLAG** (1.4× the cap). The predecessor Javier Ferrán FY2024 was £696k ≈ $0.88m, also above.
- SID Susan Kilsby £212k ≈ $284k and the other NEDs £118–158k: pass.
- The chair has no executive role.
- **Director pay: a second behaviour, one flag (`director pay`).**

**Alignment worksheet.**
- Executive directors at 10 Aug 2026: Jhangiani 127,588 shares (value at px n/a); Lewis 0. Executive Committee holdings are not disclosed.
- Management's holding is about 0.006% of shares and below 3× the hairiest number ($38.1m) at any price under about 22,400p (3 × $12.7m ÷ 1.3317 ÷ 127,588 shares). Holdings are partly undisclosed → **NOT ALIGNED**.
- No open-market purchases recorded in the 20-F.
- Votes versus economics: one share class and no holder above 20% of votes → not separated. This is an input only.

**RPT.** Sales to associates $13m and purchases $72m (0.9% of cost of sales), at arm's length; key-management pay $39m (carried from v1, 2026-10-04, same 20-F). P27: far below 0.5% of the denominator. No RPT concern.

**Worth table — repurchases.** Implied MCap = average price × diluted shares. FCF is maintenance-capex FCF ex financial income (exclude reading). EV/OI reads are carried from v1: reported OI, net borrowings + NCI at book, a lower bound on the v4.5.0 debt list. Yardsticks: worth MCap/FCF 16 · EV/OI 14; clearly above worth 28.6 · 25.

| FY | Shares (m, gross) | Cash | Avg price | MCap/FCF yr / trailing-3 | EV/OI yr / trailing-3 (all-cash–no-cash) | Reading |
|---|---|---|---|---|---|---|
| FY2018 | 58.9 | £1,507m | £25.59 (der.) | 28.2× / 28.2× (2y) | 20.2–20.5× / 20.6–20.8× | above worth, at the clearly-above line |
| FY2019 | 94.7 | £2,775m | £29.24 | 30.9× / 31.2× | 20.8–21.0× / 22.3–22.6× | clearly above worth (FCF) |
| FY2020 | 39.0 | £1,282m | £32.87 (der.) | 54.1× / 38.7× | 43.2–44.7× / 28.1–29.1× | clearly above worth |
| FY2021 | 3.2 | £109m | £34.07 | 27.3× / 36.0× | 25.1–25.8× / 28.3–29.1× | clearly above worth |
| FY2022 | 61.2 | £2,284m | £37.32 (der.) | 28.6× / 35.2× | 23.3–23.8× / 30.0–30.6× | clearly above worth |
| FY2023 | 37.8 | £1,381m | 3,616p | 55.1× / 30.3× (USD) | 21.4–21.7× / 23.3–23.6× | clearly above worth (FCF) |
| FY2024 | 27.4 | $987m | 3,644¢ | 37.6× / 30.6× | 17.9–18.1× / 18.4–18.6× (J1) | clearly above worth (FCF governs, the less flattering) |
| FY2025–26 | — | none | — | — | — | — |

- **Materiality:** 27.4m shares ÷ ≈ 2,233m average diluted shares (FY2024–26 + live) = 1.2%, which is material. The readings straddle the yardsticks (EV/OI above worth, MCap/FCF clearly above). When in doubt, the less flattering governs: **clearly above worth**.
- **Allocators then:** CEO Crew, CFO Chandrashekar, chair Ferrán. None is in office.
- **Live programme:** none executing. The routine AGM authority (10%) is not exercised. Stated criteria: deleveraging to 2.5–3.0× first, "significantly increased financial flexibility from fiscal 28", no worth reference. Live year FY2027: no purchases.
- → **CAUTION (`buybacks`)**: material repurchases clearly above worth in the recent record, behaviour not live. Not ADVERSE: nothing is executing or freshly authorised beyond the routine authority, and the pause is evidenced by the cash-flow statement and the leverage target. IDEAS A8 hazard noted: a fresh programme while the stock is above worth makes this ADVERSE.

**Sterilisation.** Net sale of own shares for schemes is a $15m inflow (FY2026): no purchases on this limb.

**Acquisition worksheet.**
- 1% of EV ≈ $750m. Deals in FY2024–FY2026 + live: acquisitions of subsidiaries $6m, $35m, $23m; associate investments $133m, $84m, $47m. None is above 1% singly or per year: no finding.
- Earlier window: Casamigos (FY2018, up to $1bn) and Aviation (FY2021), with pre-deal OI not re-derived, and Don Papa (FY2023). Impairments of acquired brands followed (US brands, Aviation, Don Papa: FY2025–26 $1,489m and $416m). The CEOs and CFOs who made those deals (Menezes, Mahony, Chandrashekar, Crew) are not in office, so the earlier-window and write-down limbs do not apply. Logged as pattern evidence.

**Distributions and funding.** Dividends paid: $2,243m (FY2024), $2,298m (FY2025), $1,846m (FY2026), against maintenance-capex FCF of $2,170m, $2,329m and $2,787m.
- FY2024's dividends plus the $987m buyback were debt-funded.
- FY2026 is covered.
- The FY2026 dividend was cut to 50¢ (−52%). Debt-funded distributions are not live, so they are context and inside the buybacks behaviour.

**Allocation across the parts (§2·1C·3).** No segment assets are printed in any year → **INDETERMINATE (b)**. Re-test if Diageo starts reporting segment assets. Context: segment capex FY2026 NA $250m, Europe $429m, APAC $95m, LAC $2m, Africa $50m, corporate/SC&P $371m.

**SF ladder.**
1. Strikes: none (pay 0.15× the line; chair 1.4× the cap; no ADVERSE).
2. Flags on distinct behaviours: (i) executive pay — big grant (Jhangiani joining award, FY2025); (ii) director pay — chair $944k against $666k; (iii) capital allocation — FY2024 repurchases clearly above worth (CAUTION). **Three flags → step 2: FAIL (`flag pair`).**
3. Inputs: NOT ALIGNED (undisclosed Executive Committee holdings); votes not separated; dividend cut and deleveraging (favourable, never netted).

**Recency-weighted reading.** The trailing three years hold one material tranche (FY2024), clearly above worth on maintenance-capex FCF, then nothing. A new chair, CEO and CFO are in place. The stated priority is deleveraging, with distributions to "grow over time" from fiscal 28. The forward evidence is the absence of a live programme and the leverage target. The re-test is the first resumed repurchase against worth. INDETERMINATE: allocation test (b), segment assets. Consistency hazard checked: the admired brand gets no friendlier reading. The v1 PASS rested on the £1.05m UK stop, which V3 caps at $666k.

## F. Valuation math

- **Inputs ($m):** MCap n/a (px not retrieved); FCF (FY2026 maintenance-capex, = all capex, ex financial income) 2,787; J1 OI 3,067; debt-equivalents 26,580; cash 1,520; BV 10,871; diluted shares 2,231; GBP/USD 1.3317.
- **Multiples:**
  - MCap/FCF = MCap ÷ 2,787: n/a (px not retrieved).
  - EV/OI = (MCap + 26,580) ÷ 3,067 (no-cash); (MCap + 25,060) ÷ 3,067 (all-cash): n/a (px not retrieved).
  - MCap/BV n/a (px not retrieved); MCap/TBV n.m.
  - Both primaries are more than 75% above threshold: **EXPENSIVE**.
- **Band:**
  - FCF leg: 8 × 2,787 ÷ 2,231 = $9.99 ≈ **750p**.
  - EV/OI legs: no-cash (21,469 − 26,580) ÷ 2,231 = −$2.29 → **n.m.**; all-cash (21,469 + 1,520 − 26,580) ÷ 2,231 = −$1.61 → **n.m.** The bounds do not converge.
  - Restoring OI: **$3,797m** no-cash, $3,580m all-cash, against FY2026 J1 OI of $3,067m (a 24% shortfall).
  - EV/OI binds: **trigger n.m.** No P12 (Past WEAK).
  - With the listed subsidiaries' NCI at market, the debt-equivalents only rise, so the band stays n.m.
- **All-capex band (context):** the same, since FY2026 maintenance = all capex.
- **Averaged readings (at px):**

| Reading | MCap/FCF | EV/OI no-cash | EV/OI all-cash |
|---|---|---|---|
| 3-year (OI 4,369.3; FCF 2,428.7) | n/a (px not retrieved) | n/a (px not retrieved) | n/a (px not retrieved) |
| 5-year (OI 4,861.6; FCF 2,622.4) | n/a (px not retrieved) | n/a (px not retrieved) | n/a (px not retrieved) |

  Context only.
- **P28 test (FY2026).**
  1. Down: met ($3,067m < $4,369m).
  2. Named cause: met (exceptional items $2,527m against a $1,795m shortfall to the 5-year average).
  3. One year: unmet. FY2025 was itself down under tests 1–2 ($4,196m below both its averages, with $1,369m of exceptional items against a shortfall of about $1,060m), and same-kind charges exceeded 10% of OI in FY2025.
  4. Recovery and nothing structural: unmet. There is no interim after FY2026, the moat is eroding in North America, the doing-without substitute is STRONG and Future is WEAK.
  - → not a one-off down year. **The latest year governs.**
- **Backvaluing:** not a definitively cyclical industry: no.
- **Qualifier context:** 3 × BV/sh = $14.62 ≈ 1,098p; 3 × TBV n.m.
- No sell-flag line (not held). No holding credits.

