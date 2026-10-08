# TXN — Texas Instruments Incorporated — REVIEW 2026-10-08 — INCOMPLETE (method re-test exceeds budget)

Run: REVIEW 2026-10-08 0106 · base d5e4c9a023e2f6ea03aedca4cfbf71ac4fe333c3 · MODEL v4.5.2 · prior memo v1 (2026-10-04, MODEL v4.4.1). No verdict. These are sourced figures for the attended re-test, not findings.

## Why INCOMPLETE

The v4.5.0 method re-test of a v4.4.1 prior could not finish within one run's time budget (MODEL §8.7 item 6). The session stalled after the evidence below had been collected, and it was past the ~90-minute budget before any memo was drafted. The re-test needs work that did not fit:
- **P20 rebuild for FY2016–FY2025.** The prior's pre-cycle capex/sales anchor (5.28%) is not a P20 tier. No company maintenance or growth-capex figure was found in the documents read (tier 1 not established; earnings-call Q&A was not searched). Tier 2 (constructed) needs k from the net-fixed-capital and revenue series below, a named US CPI source per year (π = max(3%, CPI)), and the depreciation floor. FY2023–FY2024 revenue fell, so the constructed tier finds no growth capex in those years.
- **J3 financial-income removal from CFO.** Interest income sits inside OI&E (below operating profit), so OI is clean. But CFO (indirect method) carries interest received, and from FY2017 onward it is not tagged separately in XBRL. It has to be read year by year from the OI&E notes of the FY2016, FY2019, FY2022 and FY2025 10-Ks and removed from CFO as `derived`.
- **R9 pay worksheet.** Every per-person total on every basis is needed, including the FY2023–FY2025 pay-versus-performance "compensation actually paid", from DEF 14A 2026 (0000097476-26-000078). So is the director cap under V3, the lower of 2× the home seat norm and ≈ US$666k. The prior used a lead-seat stop of ≈ $1.02m, which no longer applies.
- **Worth test re-read** on maintenance-capex FCF, including the sterilisation limb (V13). Purchases did not exceed shares issued for stock compensation in several recent years (table below).

## Sourced figures (delta)

- **Price:** USD 288.98, NasdaqGS close 2026-10-07 (query1.finance.yahoo.com chart, `currency` USD, `exchangeName` NMS, "Texas Instruments Incorporated"). No split events.
- **10-Q Q2 2026** (0000097476-26-000152, filed 2026-07-24), USD m:
  - Balance sheet at 30 Jun 2026: cash 3,660; STI 3,341; current portion of LTD 1,149; LTD 12,903; total assets 35,882; total liabilities 17,875; equity 18,007; goodwill 4,330; capitalised software licences 314; PP&E net 11,911; AP 680; accrued compensation 536; income taxes payable 70; accrued expenses and other 809; underfunded retirement plans 123; overfunded 316. No lease-liability figure is printed (FY2025 10-K: 731).
  - H1 2026 vs H1 2025: revenue 10,288 / 8,517; operating profit 4,118 / 2,887 (incl. acquisition charges 34 / 0); OI&E 116 / 128; NI 3,525 / 2,474; CFO 4,223 / 2,709; capex 1,190 / 2,428; CHIPS Act proceeds 1,104 / 260; depreciation 1,088 / 884; capitalised-software amortisation 42 / 41; dividends paid 2,586 / 2,473; repurchases 185 / 955 (0.9m / 5.4m shares).
  - Diluted average shares: Q2 2026 920m, H1 2026 917m. Treasury shares: 834m → 828m in H1 2026 (1m repurchased, 7m issued for stock compensation).
  - Silicon Labs: agreed 4 Feb 2026, $231/share cash, EV ≈ $7.5bn, close expected H1 2027, not completed. A $5bn 364-day delayed-draw term loan was entered in June 2026, conditional on the closing and undrawn at 30 Jun.
- **8-K 2026-06-02 (Item 5.02):** Julie Knecht CFO from 1 Aug 2026, succeeding Rafael Lizardi (retiring). Salary $700k, RSUs $2m.
- **8-K 2026-09-17 (Item 7.01, Ex. 99):** quarterly dividend +7% to $1.52 ($6.08 annualised), payable 10 Nov 2026. The release restates the objective "to return all free cash flow to its owners over time".

## XBRL series (SEC companyfacts CIK 97476; 10-K values, USD m)

| FY | Revenue | PP&E net | Cap. software net | Depreciation | Sw. amort. | Capex | CFO | Treasury sh. acquired (m) | Sh. issued for stock comp (m) | Repurchase $ | OI&E |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2015 | 13,000 | 2,596 | 46 | 766 | 48 | 551 | — | 51.4 | 16.0 | 2,741 | −16 |
| 2016 | 13,370 | 2,512 | 52 | 605 | 31 | 531 | 4,614 | 35.5 | 20.2 | 2,132 | 155 |
| 2017 | 14,961 | 2,664 | 110 | 539 | 47 | 695 | 5,363 | 30.6 | 17.7 | 2,556 | 75 |
| 2018 | 15,784 | 3,183 | 89 | 590 | 46 | 1,131 | 7,189 | 49.5 | 11.5 | 5,100 | 98 |
| 2019 | 14,383 | 3,303 | 69 | 708 | 54 | 847 | 6,649 | 27 | 14 | 2,960 | 175 |
| 2020 | 14,461 | 3,269 | 122 | 733 | 61 | 649 | 6,139 | 23 | 11 | 2,553 | 313 |
| 2021 | 18,344 | 5,141 | 85 | 755 | 57 | 2,462 | 8,756 | 3 | 7 | 527 | 143 |
| 2022 | 20,028 | 6,876 | 152 | 925 | 54 | 2,797 | 8,720 | 22 | 4 | 3,615 | 106 |
| 2023 | 17,519 | 9,999 | 223 | 1,175 | 63 | 5,071 | 6,420 | 2 | 5 | 293 | 440 |
| 2024 | 15,641 | 11,347 | 257 | 1,508 | 72 | 4,820 | 6,318 | 5 (4.7 per MD&A) | 7 | 929 | 496 |
| 2025 | 17,682 | 12,320 | 238 | 1,918 | 81 | 4,550 | 7,153 | 8.5 per MD&A (untagged) | n/a — not tagged | 1,477 | 230 |

FY2015 revenue (13,000) comes from the `SalesRevenueNet` tag, which fills the FY2016 growth-rate gap the prior noted. The FY2019–FY2024 share tags are in whole millions.

## Hosts tried

sec.gov and data.sec.gov (UA as configured): all retrieved. query1.finance.yahoo.com: one 429, then retrieved on retry. Nothing unretrievable. P14: 0 exploratory operations; due-check 0 (priority 1b needs none).
