# APTV — Aptiv PLC — REVIEW evidence (INCOMPLETE) — 2026-10-26

- Run: REVIEW · D 2026-10-26 · T 0611 · base b149f7f55610685b90d16fea68b03c4bbb9376a7 · MODEL v4.6.1
- ISIN: JE00B783TY65 per the prior memo and `register.csv`, still marked unverified there (the Dec-2024 new-parent reorganisation, EIN 98-1824200); not re-verified this run. SEC CIK 0001521332.
- Prior memo: v1 (2026-08-18, MODEL v4.2.0; no §6.1 machine fields; AVOID on three gates: Past WEAK, Future WEAK, SF FAIL flag pair; EXPENSIVE). Picked at priority 1b (`▶ Method re-tests v4.6.0`, G6 sub-block, first eligible line).
- **Named gap: method re-test exceeds budget.** The prior predates every v4.5.0 rule and every v4.6.0 rule and carries none of the §6.1 machine fields, so the REVIEW is a full rebuild. It did not fit in this routine run (scope below). **No verdict, no grade.** Every figure below is sourced (document named) or labelled `derived`. Nothing is assumed.

## Why the re-test exceeds one run

1. **G6 sits above the P31 line on both limbs from FY2020 (Motional JV).** Equity-method investments, as filed in each year's 10-K (SEC XBRL `EquityMethodInvestments`), against total assets (`Assets`) give these shares (`derived`):

   | Dec | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
   |---|---|---|---|---|---|---|---|---|---|---|
   | Equity-method investments $m | 67 | 91 | 99 | 106 | 2,011 | 1,797 | 1,723 | 1,443 | 1,433 | 1,431 |
   | Total assets $m | 12,292 | 12,169 | 12,480 | 13,459 | 17,522 | 18,007 | 21,884 | 24,427 | 23,458 | 23,413 |
   | Share of total assets | 0.5% | 0.7% | 0.8% | 0.8% | 11.5% | 10.0% | 7.9% | 5.9% | 6.1% | 6.1% |
   | Equity income (loss) $m (`IncomeLossFromEquityMethodInvestments`) | 35 | 31 | 23 | 15 | −83 | −200 | −279 | −299 | −118 | −38 |
   | As % of the prior's OI | 2.3% | 2.2% | 1.6% | 1.2% | 12.1% | 16.8% | 22.1% | 19.2% | 6.4% | 3.2% |

   The prior OI column is the prior memo's B1 (FY2020 $684m, the Motional $1,434m gain taken out; XBRL as filed in the FY2022 10-K prints $2,118m). Both P31 limbs fail from FY2020, so every Gate 1A test needs exclude-both and include-both at each balance-sheet date. Also owed: dividends from investees inside CFO, the 2024 Motional ownership change (the "net gain on equity method transactions" the prior notes sits below OI), and any S3 securities beside the JVs.
2. **The ten-year window.** The prior ran FY2019–FY2025 (7 years, record-limited). Restated continuing-operations figures for the post-Delphi-Technologies perimeter exist in later 10-Ks (XBRL as filed, $m): revenue FY2016 12,274, FY2017 12,884; OI FY2015 1,235, FY2016 1,539, FY2017 1,416; CFO FY2016 1,941, FY2017 1,468; capex FY2016 657, FY2017 698; total assets Dec-2016 12,292, Dec-2017 12,169; diluted shares FY2016 273.70m, FY2017 268.03m. The Dec-2015 balance sheet appears only on the old perimeter (total assets $11,973m, FY2016 10-K as filed). The attended run decides the window (FY2017–FY2025 with Dec-2016 opening, history- or record-limited) and the label.
3. **P20 for every year.** The prior ran all-capex FCF ("P20 not activated", a pre-R6 reading). The constructed tier needs net PP&E (XBRL `PropertyPlantAndEquipmentNet`: Dec-2016 2,325 · 2017 2,804 · 2018 3,179 · 2019 3,309 · 2020 3,301 · 2021 3,294 · 2022 3,495 · 2023 3,785 · 2024 3,698 · 2025 3,774), capitalised software, depreciation, Aptiv's printed organic ("adjusted") growth, US CPI per year, and the FY2022 deal-year rule (Wind River and Intercable above 1% of EV).
4. **J3 interest income.** Interest income sits in other income; it leaves OI and, as `derived`, CFO (US GAAP indirect method). No XBRL `InvestmentIncomeInterest` fact was found; the other-income note is owed per year.
5. **The group build (G3, G4).** After the 1 Apr 2026 Versigent (EDS) distribution and the Q1-2026 segment realignment, the remaining reportable segments need P22 tests, one Gate-0 sentence and Future block per material unit, P29 weights, and the allocation-across-the-parts test (likely INDETERMINATE (b): the new segmentation has fewer than three fiscal years).
6. **Gate 2 on a post-spin TTM base.** The prior's band rests on annualised H1-2026 continuing-operations OI, which is not a §6.1 `core_oi_basis` period. A TTM Q2-2026 continuing-operations OI and maintenance-capex FCF need the FY2025 continuing-operations figures (the 8-K/A of 6 Apr 2026, item 9.01 pro forma, or the Q2-2026 10-Q discontinued-operations note) and the Q2-2026 10-Q's H1 figures. The 30 Jun 2026 balance sheet is the latest primary interim one (no Q3-2026 10-Q in EDGAR at this run).
7. **Gate 1C on R9, V3, V13 and J14.** The hairiest number on every printed basis over FY2023–FY2025 (DEF 14A filed 16 Mar 2026: the SCT totals $18.00m, $18.76m and $19.25m for Kevin P. Clark, per the prior, plus compensation actually paid); outside-director fees, insider holdings and the RPT note (all INDETERMINATE in the prior, not retrieved); the worth table on maintenance-capex FCF (repurchase cash per XBRL: FY2023 398, FY2024 4,104, FY2025 397; H1-2026 $325m per the prior); the acquisition stop and the earlier-window Wind River read.

Projection for the attended run (never a finding): Past likely stays WEAK (the prior's best four-way ROCE reading was 10.0%, and the include reading lowers OI by the Motional losses), so AVOID is unlikely to move. The trigger needs the TTM rebuild.

## Sources retrieved this run (uncounted)

- SEC EDGAR submissions index, CIK 0001521332 (data.sec.gov): latest filings are the Q2-2026 10-Q (filed 4 Aug 2026), the 8-K of 4 Aug 2026 (item 2.02), the DEF 14A of 16 Mar 2026 and the 8-K/A of 6 Apr 2026 (item 9.01). No Q3-2026 filing yet.
- SEC XBRL companyfacts, CIK 0001521332 (data.sec.gov/api/xbrl/companyfacts): the series above, from each 10-K as filed (latest filing per fiscal year-end). No tier-2 acceptance test was run on it this run; each figure is to be tied out to the primary filings in the attended rebuild.
- Not retrieved: the price. query1.finance.yahoo.com returned "Too Many Requests" on the one GET. The register carries $49.19 (18 Aug 2026).
- P14: **0** of ~2 exploratory searches. Due-check operations: 0 (priority 1b needs none).
