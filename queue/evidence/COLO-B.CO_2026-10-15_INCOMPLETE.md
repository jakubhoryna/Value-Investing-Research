# COLO-B.CO — Coloplast A/S — REVIEW evidence (INCOMPLETE) — 2026-10-15

- Run: REVIEW · D 2026-10-15 · T 2111 · base b774bd9d05c516c06307c67c1e39ab207f51e8f5 · MODEL v4.5.3
- ISIN DK0060448595 · prior memo v1 (2026-08-08, MODEL v4.1.0) · priority 1b (`▶ Method re-tests v4.5.0`)
- **Named gap: method re-test exceeds budget.** The primary record below was retrieved and tabulated, but the v4.5.0 memo (body, Appendices C–G, machine fields, lint) was not finished within the run's time budget. The session then stalled, and INTAKE closed claim PR 140 as `[abandoned]` on 2026-10-19. **No verdict, no grade.** Every figure below is either sourced (document named) or labelled `derived` (arithmetic on sourced figures). This file is orientation for the attended re-test, not a finding.

## Sources retrieved (all coloplast.com, uncounted primary documents)

Annual Reports 2014/15–2024/25 (11), Remuneration Reports 2022/23, 2023/24, 2024/25, 9M 2025/26 earnings release (Announcement 07/2026, 18 Aug 2026, BS 30 Jun 2026), FY 2024/25 earnings release, pre-close brief FY 2025/26, "Number of shares and votes" (11 Nov 2025). Danish CPI: Statistics Denmark Statbank table PRIS111 (api.statbank.dk). FX: ECB reference via api.frankfurter.dev (USD/DKK 6.6693 on 2026-10-15; 6.358 on 2025-09-30). Price: query1.finance.yahoo.com chart, COLO-B.CO, currency DKK, CPH, close **468.50 on 2026-10-15**, no split events. P14: 2 exploratory operations of ~2 (Statbank CPI; one coloplast.com-scoped search to locate the 2024/25 remuneration report). Nothing unretrievable.

## Record — DKK m, fiscal years ending 30 Sep (FY2016 = 2015/16)

OI = operating profit (EBIT) after special items, the lowest operating subtotal (J1); financial items and associates sit below it. CFO is after interest paid and tax paid; "interest received / ingoing interest payments" is the J3 removal. Capex = investments in intangible assets + land and buildings + plant and machinery + PP&E under construction (FY2019: land and buildings net of the 54 shown as "of which finance leases"). FY2021's intangible investment of 1,047 includes the Nine Continents Medical asset purchase (the AR 2020/21 note gives DKK 1,218m). Sep-2022 balance sheet as restated in AR 2022/23 (goodwill and deferred tax liability each +2,490; equity unchanged). NIBCL = trade payables + current income tax payable. Other payables, and the non-current income tax payable from FY2025, stay in CE (burden of proof, as in v1). Cash+STI = cash + 0.9 × marketable securities (S1 longer-bond reading; nature not verified). Amounts held in escrow (mesh litigation) are excluded from cash.

| FY | Revenue | OI | Special items | CFO | Int. received | Capex | Dil. sh (m) | NI | Dividends paid | Total assets | NIBCL | Cash+STI | Equity | GW+Intang |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2015 (BS) | 13,909 | 1,535 | −3,000 | 3,337 | 13 | — | 212.9 | 899 | 2,535 | 10,817 | 656 | 1,348 | 4,706 | 1,511 |
| FY2016 | 14,681 | 4,096 | −750 | 3,028 | 29 | 649 | 212.5 | 3,143 | 2,650 | 11,007 | 808 | 986 | 5,068 | 1,397 |
| FY2017 | 15,528 | 5,024 | 0 | 3,251 | 73 | 685 | 212.5 | 3,797 | 2,864 | 12,050 | 1,301 | 598 | 5,952 | 2,295 |
| FY2018 | 16,449 | 5,091 | 0 | 4,361 | 101 | 669 | 212.4 | 3,845 | 3,288 | 11,769 | 1,574 | 576 | 6,418 | 2,518 |
| FY2019 | 17,939 | 5,156 | −400 | 4,357 | 20 | 636 | 213.1 | 3,873 | 3,398 | 12,732 | 1,927 | 638 | 6,913 | 2,502 |
| FY2020 | 18,544 | 5,854 | 0 | 4,759 | 9 | 931 | 213.3 | 4,197 | 3,612 | 13,499 | 1,817 | 559 | 7,406 | 2,364 |
| FY2021 | 19,426 | 6,155 | −200 | 5,290 | 31 | 1,966 | 213.2 | 4,825 | 3,830 | 15,841 | 1,964 | 651 | 8,168 | 3,651 |
| FY2022 | 22,579 | 6,439 | −471 | 5,099 | 16 | 1,135 | 212.8 | 4,706 | 4,041 | 37,446 | 2,584 | 611 | 8,292 | 22,767 |
| FY2023 | 24,500 | 6,771 | −74 | 4,226 | 40 | 1,241 | 215.5 | 4,783 | 4,247 | 48,159 | 5,523 | 911 | 17,299 | 31,255 |
| FY2024 | 27,030 | 7,320 | +34 | 2,766 | 82 | 1,346 | 224.9 | 5,052 | 4,720 | 48,073 | 2,385 | 788 | 17,942 | 30,332 |
| FY2025 | 27,874 | 7,201 | −469 | 6,645 | 30 | 1,427 | 225.4 | 3,636 | 4,958 | 48,367 | 1,473 | 947 | 16,122 | 29,811 |

Total liabilities = total assets − equity (no NCI): Sep-2025 32,245, so L/E is 200.006% (`derived`). At 30 Jun 2026 (9M release): total assets 46,938, equity 13,367, total liabilities 33,571, so L/E is 251.1% (`derived`).

**P20 inputs.**
- Net fixed capital (net PP&E excl. right-of-use + software + intangibles in progress), Sep-2016…Sep-2025: 3,010 / 3,163 / 3,277 / 3,397 / 3,503 / 4,026 / 4,881 / 5,668 / 6,245 / 6,663.
- Floor (PP&E depreciation + software amortisation): 416 / 478 / 502 / 533 / 526 / 505 / 505 / 563 / 673 / 831.
- Organic growth % (ARs): 7 / 7 / 8 / 8 / 4 / 7 / 6 / 8 / 8 / 7.
- DK CPI by fiscal year (Statbank PRIS111, Oct–Sep average, `derived`): 0.23 / 0.93 / 0.93 / 0.78 / 0.48 / 1.18 / 6.18 / 5.48 / 1.06 / 1.81, so π is 3% except FY2022 (6.18%) and FY2023 (5.48%).
- No tier-1 split: the Portugal factory is disclosed only as a cumulative DKK 450m to Sep-2025.
- Constructed tier (`derived`), k = 0.2143: maintenance capex 530 / 559 / 503 / 533 (floor) / 893 / 1,807 / 1,135 (= capex) / 1,119 / 1,083 / 1,195.
- Maintenance FCF (CFO − interest received − maintenance capex, `derived`): 2,469 / 2,619 / 3,757 / 3,804 / 3,857 / 3,452 / 3,948 / 3,067 / 1,601 / 5,420. The all-capex reading is 2,350 … 5,188.

**Returns (`derived`, on the rows above).**
- Worst-of-four ROCE: P1 window 24.9%, latest 5 FYs 18.4%, latest 3 FYs 15.7%.
- Worst-of-four FCFROCE on maintenance FCF: P1 window 14.3%, latest 5 FYs 9.5%, latest 3 FYs 7.5%.
- ROCE_wc on end-of-period CE by year: 40.2 / 46.7 / 49.9 / 47.7 / 50.1 / 44.4 / 18.5 / 15.9 / 16.0 / 15.4%.
- ROCE_wc on beginning-of-period CE declines in each of FY2022–FY2025 (46.4 → 19.4 → 17.2 → 15.8%).
- Harsher-of growth reads: ΔOI/sh 5.77% / 5.28%; ΔFCF/sh 8.42% / 1.24%.
- TBV is negative from Sep-2022.

## Interim, price and EV inputs (9M 2025/26, BS 30 Jun 2026)

- 9M EBIT 2,521 (5,477 a year earlier), after the DKK 3,000m Kerecis goodwill impairment (special items). TTM OI is 7,201 − 5,477 + 2,521 = **4,245** (`derived`).
- 9M CFO 5,409 (4,380); interest received 138 (27); 9M capex 1,159 (1,036).
- Debt-equivalents 23,928: bonds 11,585, other credit institutions 8,622 + 2,627, leases 717 + 252, pensions 118 + 7. Non-current income tax payable of 2,422 is excluded (not on the Gate 2 list; logged). Cash 817.
- Shares: 228.2m issued (A 18.0m at 10 votes each, B 210.2m) less 2,831,862 treasury, so 225.17m outstanding; dilution nil (EPS note).
- Next results: FY 2025/26 annual report on **5 Nov 2026** (AR 2024/25 financial calendar).

## Shareholder-friendliness inputs

- **Kerecis** (AR 2022/23 note 32), closed 31 Aug 2023 (FY2023, inside the trailing three fiscal years):
  - Consideration 8,868, including contingent consideration at fair value of 648 (maximum earn-out USD 100m) and deferred consideration of 103. Acquired cash 194; assumed leases 11.
  - Pro-forma FY2022/23 operating profit before special items, excluding PPA amortisation: **DKK 46m** on revenue 772.
  - Derived: deal EV 8,685 ÷ 46 ≈ 188.8×.
  - Goodwill 6,184 plus acquired intangibles 3,159. DKK 3,000m impairment in Apr 2026. The CFO who made the deal (Anders Lonning-Skovgaard, CFO throughout FY2016–FY2026) is still in office; the CEO (Villumsen) left on 5 May 2025.
- **Atos Medical** (AR 2021/22 note 32), closed 31 Jan 2022 (FY2022, earlier window): cash consideration 10,622. Combined pro-forma FY2021/22 OI before special items was 7,000, against Coloplast's 6,910 before special items incl. Atos's 231 from consolidation. Derived Atos annualised ≈ 321, giving EV/OI ≥ 33× on equity consideration alone.
- **Repurchases**: DKK 500m a year in FY2016–FY2022, none since.
  - B shares bought (thousands): 1,014 / 928 / 939 / 686 / 505 / 498 / 513. Derived average prices: 493 / 539 / 532 / 729 / 990 / 1,004 / 975.
  - Derived year EV/OI no-cash: 25.7 / 23.1 / 22.5 / 30.4 / 36.4 / 35.3 / 35.1×.
  - Treasury shares were sold for option exercises in most years (proceeds 282 / 374 / 454 / 380 / 407 / 306 / −119), so the sterilisation limb applies.
  - Allocators: CFO throughout; Lars Rasmussen CEO to FY2018, then chair to May 2025.
- **Pay** (Remuneration Reports; DKK m, total incl. share options at grant value):
  - Villumsen (CEO): 23.3 (FY2023), 22.0 (FY2024), 14.5 (FY2025) plus a severance of 50.5 printed for him in FY2025.
  - Lonning-Skovgaard (CFO): 11.9 / 11.3 / 12.5.
  - Lars Rasmussen (interim CEO from 5 May 2025): 6.2.
  - Chair fees: DKK 1.84m in FY2024; about 1.07m in FY2025 for each of the two chairs.
  - New CEO Gavin Wood (9M 2025/26 release): his package and holdings are not yet in a remuneration report.
- **Holdings** (Remuneration Report 2024/25, 30 Sep 2025): CFO 2,649 B shares; Lars Rasmussen 12,100. Coloplast Holding ApS (controlled by Deputy Chairman N.P. Louis-Hansen) holds 29.49% of capital and 51.36% of votes.
- **Distributions**: dividends paid exceeded CFO − capex in FY2023 (4,247 vs 2,985) and FY2024 (4,720 vs 1,420); credit facilities were drawn.
- **Segments FY2025** (revenue; segment result):
  - Chronic Care 18,881 (Ostomy 9,897 / Continence 8,984); 11,063.
  - Voice & Respiratory Care 2,280; 837.
  - Interventional Urology 2,784 (9.99% of revenue); 984.
  - Advanced Wound Dressings 2,675; 1,105.
  - Biologics 1,254; 159.
  - No segment assets. The AR states "No single customer accounts for more than 10% of revenue".

## Owed to finish (attended)

The v4.5.0 memo v2 itself:
- Gate 0 one-level decomposition and P22 materiality, with Interventional Urology at 9.99% of revenue;
- the Past grade on the record above;
- the Future worksheet;
- the SF ladder, with the acquisition-stop and earlier-window readings judged;
- Gate 2 on a fresh price, with the TTM OI rule and P28 (the FY2025/26 annual report on 5 Nov 2026 will make FY2026 the latest year);
- the machine fields and the compliance re-measure.
