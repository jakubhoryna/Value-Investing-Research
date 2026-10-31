# APTV — Aptiv PLC — REVIEW resumable record (INCOMPLETE) — 2026-10-31

## 1. Header

- Key: APTV · job: REVIEW · D 2026-10-31 · T 1021 · base 5792f9a0191a83f1d3d0e87fe45983f63700e7c6 · live MODEL v4.8.0
- Prior memo: `memos/APTV/APTV_2026-08-18_GSC.md` (memo v1, MODEL v4.2.0; no §6.1 machine fields; AVOID, three gates: Past WEAK, Future WEAK, SF FAIL flag pair).
- Named gap: **method re-test exceeds budget** (second overrun).
- resumes: `queue/evidence/APTV_2026-10-26_INCOMPLETE.md` (REVIEW 2026-10-26, MODEL v4.6.1). That record is a scope note, not a full v4.8.0 resumable record. This file carries its figures into a cited item table and adds the post-spin continuing-operations figures.
- Also blocking this run: the price endpoint `query1.finance.yahoo.com/v8/finance/chart/APTV` returned HTTP 429 ("Edge: Too Many Requests") on all three GETs (09:22–09:40 UTC). There is no px, so no multiple can be computed. The 2026-10-26 run hit the same 429.
- ISIN: JE00B783TY65 per the prior memo and `register.csv`, still unverified after the Dec-2024 new-parent reorganisation. Not re-verified this run. SEC CIK 0001521332.
- EDGAR state at this run (data.sec.gov submissions): the latest periodic filing is the Q2-2026 10-Q (acc. 0001521332-26-000061, filed 2026-08-04). No Q3-2026 10-Q or Q3 earnings 8-K yet. The latest DEF 14A is acc. 0001193125-26-108328 (filed 2026-03-16).

Every figure below is either sourced (filing accession plus XBRL tag or page location) or labelled `derived`. Nothing is assumed. No grade, verdict, trigger or zone is stated.

## 2. Per gate or leg — work done and figures

**Source key.** XBRL facts come from SEC companyfacts (data.sec.gov/api/xbrl/companyfacts/CIK0001521332.json). Each figure is the value as filed in the named filing (the latest 10-K that prints that fiscal year), in USD m:
- K16 = FY2016 10-K, acc. 0001521332-17-000013
- K17 = 0001521332-18-000013
- K18 = 0001521332-19-000007
- K19 = 0001521332-20-000012
- K20 = 0001521332-21-000009
- K21 = 0001521332-22-000010
- K22 = 0001521332-23-000013
- K23 = 0001521332-24-000011
- K24 = 0001521332-25-000010
- K25 = 0001521332-26-000009
- Q2-26 = Q2-2026 10-Q, 0001521332-26-000061
- Q1-26 = 0001521332-26-000048
- Q3-25 = 0001521332-25-000051
- PF = 8-K/A of 2026-04-06, acc. 0001521332-26-000037, Exhibit 99.1 (aptv-ex991xunaditedproform.htm), unaudited pro forma statements, pp. 3–6

Tie-out to the printed statements is still owed for every XBRL figure (scope item 1).

### Past (Gate 1A) — whole-company record, as filed

| item | FY | value | unit | source |
|---|---|---|---|---|
| Revenue | 2016 · 2017 · 2018 · 2019 · 2020 · 2021 · 2022 · 2023 · 2024 · 2025 | 12,274 · 12,884 · 14,435 · 14,357 · 13,066 · 15,618 · 17,489 · 20,051 · 19,713 · 20,398 | USD m | XBRL `Revenues`: K18, K19, K20, K21, K22, K23, K24, K25, K25, K25 |
| Operating income (as filed) | 2015 · 2016 · 2017 · 2018 · 2019 · 2020 · 2021 · 2022 · 2023 · 2024 · 2025 | 1,235 · 1,539 · 1,416 · 1,473 · 1,276 · 2,118 · 1,189 · 1,263 · 1,559 · 1,842 · 1,184 | USD m | XBRL `OperatingIncomeLoss`: K17, K18, K19, K20, K21, K22, K23, K24, K25, K25, K25 |
| Motional JV gain inside FY2020 OI | 2020 | 1,434 | USD m | prior memo v1 App. C (FY2020 Q4 release, 8-K ex-99.1, 3 Feb 2021); to be re-opened in K21/K22 |
| CFO total (incl. discontinued) | 2016 · 2017 | 1,941 · 1,468 | USD m | XBRL `NetCashProvidedByUsedInOperatingActivities`: K18, K19 |
| CFO continuing operations | 2015 · 2016 · 2017 · 2018 · 2019 · 2020 | 1,140 · 1,494 · 1,106 · 1,640 · 1,624 · 1,413 | USD m | XBRL `NetCashProvidedByUsedInOperatingActivitiesContinuingOperations`: K17, K18, K19, K20, K20, K20 |
| CFO (total = continuing, no discontinued ops) | 2021 · 2022 · 2023 · 2024 · 2025 | 1,222 · 1,263 · 1,896 · 2,446 · 2,185 | USD m | XBRL `NetCashProvidedByUsedInOperatingActivities`: K23, K24, K25, K25, K25 |
| Capex (`PaymentsToAcquireProductiveAssets`) | 2015 · 2016 · 2017 · 2018 · 2019 · 2020 · 2021 · 2022 · 2023 · 2024 · 2025 | 503 · 657 · 698 · 846 · 781 · 584 · 611 · 844 · 906 · 830 · 656 | USD m | XBRL: K17, K18, K19, K20, K21, K22, K23, K24, K25, K25, K25 |
| Depreciation | 2016 · 2017 · 2018 · 2019 · 2020 · 2021 · 2022 · 2023 · 2024 · 2025 | 372 · 429 · 522 · 571 · 620 · 625 · 613 · 679 · 753 · 783 | USD m | XBRL `Depreciation`: K18, K19, K20, K21, K22, K23, K24, K25, K25, K25 |
| D&A | 2016 · 2017 · 2018 · 2019 · 2020 · 2021 · 2022 · 2023 · 2024 · 2025 | 489 · 546 · 676 · 717 · 764 · 773 · 762 · 912 · 964 · 991 | USD m | XBRL `DepreciationAndAmortization`: same filings |
| Diluted shares (weighted) | 2015 · 2016 · 2017 · 2018 · 2019 · 2020 · 2021 · 2022 · 2023 · 2024 · 2025 | 286.64 · 273.70 · 268.03 · 265.22 · 257.39 · 270.70 · 271.22 · 271.18 · 282.88 · 256.66 · 220.75 | m | XBRL `WeightedAverageNumberOfDilutedSharesOutstanding`: K17, K18, K19, K20, K21, K22, K23, K24, K25, K25, K25 |
| Total assets | Dec-15 · 16 · 17 · 18 · 19 · 20 · 21 · 22 · 23 · 24 · 25 | 11,973 · 12,292 · 12,169 · 12,480 · 13,459 · 17,522 · 18,007 · 21,884 · 24,427 · 23,458 · 23,413 | USD m | XBRL `Assets`: K16, K17, K18, K19, K20, K21, K22, K23, K24, K25; Dec-25 PF p. 3 historical column |
| Accounts payable | Dec-15 … Dec-25 | 2,541 · 1,820 · 2,227 · 2,334 · 2,463 · 2,571 · 2,953 · 3,150 · 3,151 · 2,870 · 3,157 | USD m | XBRL `AccountsPayableCurrent` (same filings); Dec-25 PF p. 3 |
| Accrued liabilities | Dec-15 … Dec-25 | 1,204 · 1,242 · 1,296 · 1,054 · 1,155 · 1,385 · 1,246 · 1,684 · 1,648 · 1,752 · 1,799 | USD m | XBRL `AccruedLiabilitiesCurrent`; Dec-25 PF p. 3 |
| Operating lease liability, current | Dec-19 … Dec-24 | 94 · 100 · 92 · 109 · 121 · 124 | USD m | XBRL `OperatingLeaseLiabilityCurrent`: K20 … K25 (sits inside accrued liabilities, so it is not NIBCL: add it back to CE) |
| Cash and equivalents | Dec-15 … Dec-25 | 427 · 737 · 1,596 · 567 · 412 · 2,821 · 3,139 · 1,531 · 1,640 · 1,573 · 1,851 | USD m | XBRL `CashAndCashEquivalentsAtCarryingValue`; Dec-25 PF p. 3 (restricted 3) |
| Short-term borrowings | Dec-15 … Dec-25 | 52 · 10 · 17 · 306 · 393 · 90 · 8 · 31 · 9 · 509 · 81 | USD m | XBRL `ShortTermBorrowings`; Dec-25 PF p. 3 |
| Long-term debt | Dec-15 … Dec-25 | 3,956 · 3,953 · 4,132 · 4,038 · 3,971 · 4,011 · 4,059 · 6,460 · 6,204 · 7,843 · 7,470 | USD m | XBRL `LongTermDebtNoncurrent`; Dec-25 PF p. 3 |
| Operating lease liability, long-term | Dec-19 … Dec-25 | 329 · 300 · 304 · 361 · 453 · 412 · 401 | USD m | XBRL `OperatingLeaseLiabilityNoncurrent`; Dec-25 PF p. 3 |
| Aptiv shareholders' equity | Dec-15 … Dec-25 | 2,250 · 2,401 · 3,299 · 3,459 · 3,819 · 7,905 · 8,347 · 8,809 · 11,548 · 8,796 · 9,207 | USD m | XBRL `StockholdersEquity`; Dec-25 PF p. 3 |
| Noncontrolling interest | Dec-15 … Dec-25 | 483 · 362 · 218 · 211 · 192 · 195 · 214 · 189 · 197 · 197 · 190 | USD m | XBRL `MinorityInterest`; Dec-25 PF p. 3 (plus redeemable NCI 102) |
| Goodwill | Dec-15 … Dec-25 | 1,531 · 1,502 · 1,944 · 2,524 · 2,407 · 2,580 · 2,511 · 5,106 · 5,151 · 5,024 · 4,596 | USD m | XBRL `Goodwill` (latest filing per date); Dec-25 PF p. 3 |
| Intangibles, net | Dec-15 … Dec-25 | 1,383 · 1,148 · 1,219 · 1,380 · 1,186 · 1,091 · 964 · 2,585 · 2,399 · 2,140 · 2,004 | USD m | XBRL `IntangibleAssetsNetExcludingGoodwill`; Dec-25 PF p. 3 |
| PP&E, net | Dec-15 … Dec-25 | 2,126 · 2,325 · 2,804 · 3,179 · 3,309 · 3,301 · 3,294 · 3,495 · 3,785 · 3,698 · 3,774 | USD m | XBRL `PropertyPlantAndEquipmentNet`; Dec-25 PF p. 3 |
| Other income, net (below OI; holds interest income) | 2015 · 2016 · 2017 · 2018 · 2019 · 2020 · 2021 · 2022 · 2023 · 2024 · 2025 | −2 · 9 · 8 · 36 · 20 · 6 · 1 · −12 · 63 · 41 · 50 | USD m | XBRL `OtherNonoperatingIncomeExpense`: K17 … K25 |
| Interest expense | 2016 · 2017 · 2018 · 2019 · 2020 · 2021 · 2022 · 2023 · 2024 · 2025 | 155 · 140 · 141 · 164 · 164 · 150 · 219 · 285 · 337 · 361 | USD m | XBRL `InterestExpense` |
| Net income attributable to Aptiv | 2016 · 2017 · 2018 · 2019 · 2020 · 2021 · 2022 · 2023 · 2024 · 2025 | 1,257 · 1,355 · 1,067 · 990 · 1,804 · 590 · 594 · 2,938 · 1,787 · 165 | USD m | XBRL `NetIncomeLoss` (incl. discontinued ops in FY2016–17) |

### Past — G6 class (equity-method investees; Motional JV from FY2020)

| item | FY | value | unit | source |
|---|---|---|---|---|
| Equity-method investments | Dec-15 … Dec-25 | 94 · 67 · 91 · 99 · 106 · 2,011 · 1,797 · 1,723 · 1,443 · 1,433 · 1,431 | USD m | XBRL `EquityMethodInvestments`; Dec-25 PF p. 3 ("Investments in affiliates") |
| Equity income (loss), net of tax | 2015 · 2016 · 2017 · 2018 · 2019 · 2020 · 2021 · 2022 · 2023 · 2024 · 2025 | 16 · 35 · 31 · 23 · 15 · −83 · −200 · −279 · −299 · −118 · −38 | USD m | XBRL `IncomeLossFromEquityMethodInvestments` |
| Net gain on equity method transactions (below OI) | 2024 · 2025 | 605 · 46 | USD m | PF pp. 4 and 3 historical columns |
| P31 shares (derived: investments ÷ total assets; equity income ÷ as-filed OI, FY2020 OI ex Motional gain 684) | Dec-20 … Dec-25 | assets 11.5% · 10.0% · 7.9% · 5.9% · 6.1% · 6.1%; income 12.1% · 16.8% · 22.1% · 19.2% · 6.4% · 3.2% | % | derived from the rows above |

P31 is above the line on both limbs from FY2020. Every Gate 1A test needs the exclude-both and include-both readings at each balance-sheet date. Not yet built.

### Gate 2 and the post-spin perimeter (Versigent distributed 1 Apr 2026)

| item | FY | value | unit | source |
|---|---|---|---|---|
| Continuing-ops net sales | 2023 · 2024 · 2025 | 11,995 · 12,088 · 12,397 | USD m | PF pp. 5, 4 and 3, "Pro Forma Aptiv PLC Continuing Operations" column (FY2025 has no TSA adjustment to sales) |
| Historical OI less Versigent discontinued OI | 2023 · 2024 · 2025 | 616 · 1,080 · 488 | USD m | derived: PF pp. 5, 4 and 3, historical column minus the "Versigent Discontinued Operations" column (1,559 − 943; 1,842 − 762; 1,184 − 696). This is before the FY2025 TSA adjustment (+100 SG&A, PF note G), which is a pro forma item, not J1. FY2025 includes the 648 goodwill impairment. |
| Continuing-ops OI, H1 | H1-2025 · H1-2026 | 614 · 641 | USD m | XBRL `OperatingIncomeLoss`, Q2-26 (2025-01-01–06-30 recast; 2026-01-01–06-30) |
| TTM Q2-2026 continuing OI | TTM Q2-2026 | 515 | USD m | derived: 488 + 641 − 614. **Caveat:** PF (preliminary, ASC 205 estimates) and Q2-26 recast bases may differ. Tie out against the Q2-26 10-Q discontinued-ops note or the Q3-2026 10-Q. |
| Continuing CFO, H1 | H1-2025 · H1-2026 | 531 · 82 | USD m | XBRL `NetCashProvidedByUsedInOperatingActivitiesContinuingOperations`, Q2-26 |
| Capex, H1 | H1-2025 · H1-2026 | 267 · 278 | USD m | XBRL `PaymentsToAcquireProductiveAssets`, Q2-26 (H1-2025 is whole-company or recast: check) |
| FY2025 continuing CFO | 2025 | n/a — not in the PF or XBRL | — | owed: Q2-26 10-Q discontinued-ops cash-flow note, or the FY2026 10-K |
| Balance sheet 30 Jun 2026 | Jun-26 | total assets 17,996 · AP 1,910 · accrued 1,042 · cash 761 · ST debt 23 · LT debt 5,331 · LT op. lease 241 · current op. lease 89 · equity 8,753 · NCI 0 · goodwill 3,937 · intangibles 1,875 · PP&E 2,756 · equity-method inv. 1,255 | USD m | XBRL Q2-26 (tags as above) |
| Diluted shares | Q2-2026 · H1-2026 | 212.10 · 212.53 | m | XBRL Q2-26 |
| Equity income (loss) | H1-2025 · H1-2026 | −29 · −34 | USD m | XBRL Q2-26 |

The current operating-lease liability ($89m at 30 Jun 2026) is now disclosed in XBRL. Prior memo App. A gap 5 is closed for the EV build.

### SF (Gate 1C) — repurchase cash per fiscal year

| item | FY | value | unit | source |
|---|---|---|---|---|
| Repurchase payments | 2015 · 2016 · 2017 · 2018 · 2019 · 2020 · 2021 · 2022 · 2023 · 2024 · 2025 · H1-2026 | 1,159 · 634 · 383 · 499 · 420 · 57 · 0 · 0 · 398 · 4,104 · 397 · 322 | USD m | XBRL `PaymentsForRepurchaseOfCommonStock`: K17, K18, K19, K20, K21, K22, K23, K24, K25, K25, K25, Q2-26 |
| Top SCT total (Kevin P. Clark) | 2023 · 2024 · 2025 | 18.00 · 18.76 · 19.25 | USD m | prior memo v1 App. E (DEF 14A of 2026). Re-open DEF 14A acc. 0001193125-26-108328, SCT, to cite the page. |

Not gathered this run:
- shares bought per tranche-year
- the point-in-time trailing-3-FY reads
- compensation actually paid
- director fees
- insider holdings
- the RPT note
- acquisition data (Wind River, Intercable, earlier-window deals)

## 3. Readings settled (figures only; no grade)

- **Window.** OI and capex exist as filed back to FY2015, and continuing-operations CFO to FY2015. But the Dec-2015 balance sheet is on the pre-Delphi-Technologies perimeter (K16), and so is Dec-2016 (K17 presents it before the Dec-2017 spin). Whether FY2016–FY2017 enter the window, and with what label (history-limited or record-limited), is undecided.
- **J1 OI.** FY2020 as filed (2,118) holds the 1,434 Motional gain. The company's later presentation moves equity-method transaction gains below OI (FY2024 605, FY2025 46 below the line, PF). The J1 line for FY2020 still needs the K21/K22 income-statement check. Interest income is inside "other income, net", below OI. It needs the per-year other-income note to take it out of CFO (J3).
- **NIBCL.** From Dec-2019 the current operating-lease liability (94–124) is inside accrued liabilities. Deducting it with accrued liabilities understates CE. The XBRL split now allows the add-back.
- **Post-spin base.** Continuing OI is about 488 (FY2025, with the 648 impairment) and about 515 TTM Q2-2026, both derived. Annualised H1-2026 is 1,282 (the prior memo's band base). Whether P28 applies (a one-off down year carrying the impairment) is unsettled.
- **P20, G6 both readings, the group build, the pay and worth tables:** not started.

## 4. Scope still owed (in order)

- [ ] **Price.** One APTV close from `query1.finance.yahoo.com/v8/finance/chart/APTV` (HTTP 429 on 2026-10-26 and 2026-10-31). Record `currency`, `exchangeName` and the close date.
- [ ] **Q3-2026 10-Q** (due early Nov 2026, EDGAR CIK 0001521332). It replaces the 30 Jun 2026 balance sheet and gives TTM Q3-2026 continuing OI and CFO. It may also print the FY2025 continuing-ops recast in the discontinued-ops note.
- [ ] **Tie out the XBRL rows above** to the printed statements in K18–K25 and Q2-26: income statement, balance sheet, cash flow.
- [ ] **Window decision.** Set FY2016–FY2025 or FY2017–FY2025 and its label. Get the Dec-2016 continuing-perimeter balance sheet: the K17 discontinued-ops note (assets of Delphi Technologies), or use K18's Dec-2017 as the opening.
- [ ] **J1/J3.** Read the other-income note per year (K18–K25: interest income, the FY2020 Motional gain line, other items) and take interest out of OI and CFO.
- [ ] **G6.** Build the exclude-both and include-both ROCE/FCFROCE readings FY2020–FY2025, using the equity-method rows above and dividends from affiliates in CFO (K21–K25 cash-flow statement or the investments note). Log both readings in App. C.
- [ ] **P20 constructed.** Use the PP&E, depreciation and capex rows above, plus Aptiv's printed organic ("adjusted") growth per year (K18–K25 MD&A) and US CPI. Apply the FY2022 deal-year rule (Wind River, Intercable).
- [ ] **Gate 0 and the group build on the Q1-2026 realignment** (Q2-26 10-Q segment note):
  - one sentence and one Future block per material unit;
  - the P22 tests and P29 weights;
  - the allocation-across-the-parts table;
  - the v4.8.0 unit statement against the Q2-26 customer note (one Global OEM at about 11% of H1-2026 sales, prior memo App. D: a named concentration, so it does not cover the units).
- [ ] **Gate 1C.**
  - DEF 14A 2026 (acc. 0001193125-26-108328): SCT, compensation actually paid, director compensation, holdings, related-party section.
  - Repurchase shares per year: the K18–K25 equity notes.
  - The point-in-time worth table per tranche-year (v4.8.0), with the per-year ≈ 1% floor.
  - The acquisition stop: Wind River FY2022 (pre-profit) and Intercable.
- [ ] **Gate 2.** EV at the latest primary balance sheet, including:
  - current and long-term operating leases;
  - pension (212 continuing, PF p. 3);
  - redeemable NCI (nil at 30 Jun 2026).

  Then compute the trigger at the no-cash bound and the §6.1 machine fields.
- [ ] **Memo v2** per MODEL §6.6, then `lint-memo`.

*Framework output, not investment advice.*
