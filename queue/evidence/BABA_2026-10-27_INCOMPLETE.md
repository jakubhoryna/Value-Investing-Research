# BABA — Alibaba Group Holding Limited — INCOMPLETE evidence (REVIEW 2026-10-27)

- Run: REVIEW · D 2026-10-27 · T 2117 · base 95098344287c1902754997efae23efe8a2f082b1 · MODEL v4.7.0
- Prior: `memos/BABA/BABA_2026-10-06_GSC.md` (memo v2, MODEL v4.4.1, AVOID on three gates; no §6.1 machine fields, no `lens`, no group build)
- Named gap: **method re-test exceeds budget** (README §5, MODEL §8.7 item 6). No verdict is stated here.

## Why the re-test does not fit one run

The prior predates v4.5.0 and v4.6.0, so the REVIEW must apply every rule it predates (REVIEW.md step 4), and as a legacy memo without machine fields the new memo must establish all of them. The scope:

1. **G6 / P31 above the line, both readings, every window year.** Equity-method investees alone exceed 5% of total assets at every balance-sheet date FYE2016–FYE2026 (table below), so both readings are owed: per-year equity-method results (post-FY2020 not in XBRL; the 20-F income-statement line, Ant Group on a one-quarter lag), per-year long-term equity-security carrying values (FYE2026 RMB 449,942m per the TODO pointer, not re-sourced this run) and their income inside "interest and investment income, net", the include-reading loss rule and the dividends-received placement.
2. **J1/J3** on "income from operations" in every window year, the B1 rebuild from primary 20-Fs (the prior's FY2022–26 series is tier-2), and an 11th balance sheet.
3. **P20 constructed** (k over the window, PRC CPI deflators with the 3% floor, deal-year tier-3 checks against §2·1C·3).
4. **The group build (G3/G4, P22, P29):** FY2026 segments (Alibaba China E-commerce Group, Cloud Intelligence Group, All others — a mixed unit to be described by its parts), the materiality of controlled listed subsidiaries, the unit-level Future blocks with R7 customer-silence reads, B4 and the §2·1C·3 allocation table.
5. **Gate 1C on the R9/V3/J14 rules** (pay worksheets, the worth test on maintenance-capex FCF, the 2025–26 deals) and **Gate 2** on the no-cash bound (R10), P28, and the 3-year and 5-year readings.

## Sourced figures gathered (SEC XBRL companyfacts, CIK 0001577552, pulled 2026-10-27; RMB m, FYE 31 Mar)

| FYE | Equity-method investments | Total assets | Share (derived) |
|---|---|---|---|
| 2016 | 58,197 | 364,245 | 16.0% |
| 2017 | 84,964 | 506,812 | 16.8% |
| 2018 | 79,758 | 717,124 | 11.1% |
| 2019 | 84,454 | 965,076 | 8.8% |
| 2020 | 189,632 | 1,312,985 | 14.4% |
| 2021 | 200,189 | 1,690,218 | 11.8% |
| 2022 | 219,642 | 1,695,553 | 13.0% |
| 2023 | 207,380 | 1,753,044 | 11.8% |
| 2024 | 203,131 | 1,764,829 | 11.5% |
| 2025 | 210,169 | 1,804,227 | 11.6% |
| 2026 | 206,803 | 1,909,570 | 10.8% |

- P31 asset limb: fails at all eleven dates on the equity-method class alone (sourced carrying values; shares derived). Both readings are owed.
- Equity-method result (XBRL `IncomeLossFromEquityMethodInvestments`): FY2017 −5,027 · FY2018 −20,792 · FY2019 566 · FY2020 −5,733; FY2021–26 not tagged (20-F face statement owed).
- Dividends from equity-method investees (`EquityMethodInvestmentDividendsOrDistributions`): FY2021 1,976 · FY2022 5,329 · FY2023 11,645 · FY2024 1,258 · FY2025 3,906 · FY2026 4,684.
- Equity securities without readily determinable fair value: FYE2019 81,514 · 2020 80,939 · 2021 96,946 · 2022 99,270 · 2023 79,545 · 2024 89,660 · 2025 88,728 · 2026 124,979.
- Unrealised gains/losses on marketable securities in earnings: FY2020 −15,264 · FY2021 45,139 · FY2022 −25,587 · FY2023 −29,481 · FY2024 −28,790 · FY2025 16,746 · FY2026 56,295.
- Interest income (`InterestIncomeInterestEarningAsset`): FY2022 13,602 · FY2023 16,339 · FY2024 24,868 · FY2025 20,449 · FY2026 18,806.
- Operating income (`OperatingIncomeLoss`): FY2016 29,102 · FY2017 48,055 · FY2018 69,314 · FY2019 57,084 · FY2020 91,430 · FY2021 89,678 · FY2022 69,638 · FY2023 100,351 · FY2024 113,350 · FY2025 140,905 · FY2026 50,150.
- CFO: FY2016 56,836 · FY2017 82,854 · FY2018 125,805 · FY2019 150,975 · FY2020 180,607 · FY2021 231,786 · FY2022 142,759 · FY2023 199,752 · FY2024 182,593 · FY2025 163,509 · FY2026 76,213.
- Revenue: FY2016 101,143 · FY2017 158,273 · FY2018 250,266 · FY2019 376,844 · FY2020 509,711 · FY2021 717,289 · FY2022 853,062 · FY2023 868,687 · FY2024 941,168 · FY2025 996,347 · FY2026 1,023,670.

## Hosts tried

- data.sec.gov (companyfacts JSON): retrieved.
- No other host was called; no price GET was made (no memo is written).

## Still to establish (beyond the scope above)

- ISIN (backfill owed since v2).
- The 20-F equity-method result and investment-income split FY2021–FY2026; the long-term investment-securities carrying values FYE2016–FYE2026.

*Framework output, not investment advice.*
