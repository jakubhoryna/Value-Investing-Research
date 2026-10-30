# HEIA.AS — Heineken N.V. — INCOMPLETE evidence (REVIEW 2026-10-30)

- Run: REVIEW · D 2026-10-30 · T 2112 · base df90d8bacf21ea8205ac432deabfcf436645e028 · MODEL v4.7.0
- Prior: `memos/HEIA.AS/HEIA.AS_2026-10-04_GSC.md` (memo v1, MODEL v4.4.1, AVOID on Past alone; no §6.1 machine fields, no `lens`, no group build)
- Pick: priority 1b, `▶ Method re-tests v4.6.0` (G6 line); also a SWEEP review request (move +11.3%, sweep 2026-10-24)
- Named gap: **method re-test exceeds budget** (README §5, MODEL §8.7 item 6). No verdict is stated here.

## Why the re-test does not fit one run

The prior predates v4.5.0 and v4.6.0 and carries no machine fields, so the new memo must apply every rule it predates and establish every §6.1 field (REVIEW.md step 4). The scope:

1. **G6 / P31 above the line, both readings, every window year.** Associates and JVs are above 5% of total assets at every sourced date from FY2019, and their share of profit is above 5% of OI in most sourced years (table below). Both readings are owed across FY2016–FY2025 (eleven balance sheets FY2015–FY2025). FY2015–FY2017 associate carrying values, FY2016–FY2017 share of profit and dividends received, and the FY2016–FY2017 and FY2020 other-income splits were not retrieved: the company's report archive is behind an age gate, and ESEF filings start at FY2021 (FY2020 comparatives).
2. **J1/J3 OI.** Reported operating profit carries gains on previously held equity interests and on the sale of subsidiaries, JVs and associates inside "Other income". J3 takes them out (table below); the prior kept them in. FY2021 alone carries €1,270m. Every window year's B1 OI must be rebuilt.
3. **P20 constructed** maintenance capex for each year: k over the window, euro-area HICP deflators with the 3% floor, organic volume caps and the deal-year tier-3 checks (Brasil Kirin 2017, CR Beer 2019, Distell 2023, FIFCO 2026).
4. **The group build (G3/G4, P22, P29).** There are four material units at FY2025 on net revenue: Europe €11,457m, Americas €9,549m, Africa & Middle East €4,283m and Asia Pacific €3,976m, against €28,753m consolidated. Each needs a Gate-0 sentence and a Future block. Also owed: P29 weights on segment results after the J1 charges (segment profit is beia; the note allocates impairment and amortisation by segment), B4, and the §2·1C·3 allocation table on segment assets. The listed controlled subsidiaries are Nigerian Breweries Plc (72.9%) and United Breweries Limited (61.5%), per AR2025 note 13.4. Their P22 materiality, at 10% of group revenue or assets, is not tested on sourced figures. CR Beer is held through the 40% associate CRH (Beer); its look-through P22 test (10% of MCap at market) is not run.
5. **Gate 1C on R9/V3/J14.** Owed: the hairiest number from the remuneration reports FY2023–FY2025 and P17 on maintenance-capex FCF; the director cap; the P23 alignment call with votes versus economics (Heineken Holding 50.005%); the worth table for the 2023, 2025 and 2026 tranches on maintenance-capex FCF; and the acquisition stop on Distell (2023) and FIFCO (live year, €2,838m).
6. **Gate 2 on R10.** Owed: the no-cash trigger; NCI of the listed subsidiaries at the higher of market and book; post-retirement obligations; P28; and the 3-year and 5-year readings.

## Sourced figures gathered (€m)

Associates and JVs. Carrying value is from the balance sheet. Share of profit is from the income statement. Dividends received is the CFO line, which also carries dividends on FVOCI equity instruments.

| FY-end | Carrying value | Total assets | Share (derived) | Share of profit | Reported OI | Share / OI (derived) | Dividends received |
|---|---|---|---|---|---|---|---|
| 2018 | 2,021 | 42,151 | 4.8% | 210 | 3,121 | 6.7% | 109 |
| 2019 | 4,868 | 46,504 | 10.5% | 164 | 3,633 | 4.5% | 181 |
| 2020 | 4,437 | 42,632 | 10.4% | (31) | 778 | 4.0% | 89 |
| 2021 | 4,148 | 48,850 | 8.5% | 250 | 4,483 | 5.6% | 184 |
| 2022 | 4,296 | 52,406 | 8.2% | 223 | 4,283 | 5.2% | 177 |
| 2023 | 4,130 | 55,153 | 7.5% | 218 | 3,229 | 6.8% | 147 |
| 2024 | 3,500 | 53,773 | 6.5% | (705) | 3,517 | 20.0% | 199 |
| 2025 | 3,238 | 53,753 | 6.0% | 255 | 3,406 | 7.5% | 192 |
| 30 Jun 2026 | 3,679 | 58,044 | 6.3% | 36 (H1) | — | — | — |

- P31: the asset limb fails at FY2019–FY2025 and at 30 Jun 2026. The income limb fails in FY2018, FY2021–FY2025. Both readings are owed. FY2024's (705) includes the €874m CR Beer impairment; the prior memo cites it, and it was not re-sourced this run.
- Equity instruments (FVOCI; S3 class, joining the associates in the test): FY2023 562 · FY2024 465 · FY2025 476 · 30 Jun 2026 432. FY2022 145 is tagged as "investments other than equity-method"; reconcile it at the attended run.
- Interest received (CFO; J3 removal from FCF): FY2020 45 · FY2021 43 · FY2022 46 · FY2023 118 · FY2024 120 · FY2025 107.

Other income inside operating profit (notes 6.2). The J3 items are business, JV and associate disposal gains and gains on previously held equity interests.

| FY | PP&E gains | Intangible gains | Subs/JV/assoc. disposal gains | Previously held interests | Tax credits / other | Total | J3 removal | Reported OI | OI after J3 removal (derived) |
|---|---|---|---|---|---|---|---|---|---|
| 2018 | 31 | 2 | 42 | — | — | 75 | 42 | 3,121 | 3,079 |
| 2019 | 20 | — | 75 | — | — | 95 | 75 | 3,633 | 3,558 |
| 2020 | n/a | n/a | n/a | n/a | n/a | 56 | n/a — split not retrieved | 778 | n/a |
| 2021 | 41 | 9 | 5 | 1,270 | 196 | 1,521 | 1,275 | 4,483 | 3,208 |
| 2022 | 46 | 10 | 15 | 76 | — | 147 | 91 | 4,283 | 4,192 |
| 2023 | 47 | 86 | 196 | 23 | 41 | 393 | 219 | 3,229 | 3,010 |
| 2024 | 37 | — | — | — | 43 | 80 | 0 | 3,517 | 3,517 |
| 2025 | 72 | 2 | — | — | 94 + 37 other operational | 205 | 0 | 3,406 | 3,406 |

- H1 2026 other income was €573m (2025 H1: €96m), mostly the remeasurement gain on the previously held FIFCO interest (HY2026 release). It is a J3 removal for any TTM read.

Latest balance sheet, 30 Jun 2026 (HY2026 interim, primary):
- borrowings 16,290 non-current + 4,354 current = 20,644 (leases included);
- NCI 2,584 at book;
- post-retirement obligations 556;
- cash 2,831;
- shareholders' equity 19,122;
- intangible assets 23,531.

H1 2026 diluted weighted shares: 548,673,541.

Price: HEIA.AS close **79.56 EUR** on 2026-10-30 (Yahoo chart endpoint; currency EUR; exchange AMS; Heineken N.V.).

Q3 2026 trading update (28 Oct 2026; the delta since the prior):
- organic net revenue (beia) +4.6% (YTD +3.4%);
- consolidated volume +3.9% (YTD +1.6%);
- Heineken® volume +9.7% (YTD +6.8%);
- all four regions grew volume;
- FIFCO consolidation added €182m of net revenue in Q3 (YTD €507m);
- 2026 guidance of 2–6% organic operating profit (beia) growth reiterated;
- agreed to acquire a majority stake in Stëlz;
- new CEO Rafa Oliveira.

## Sources and hosts

- theheinekencompany.com:
  - Annual Report 2025 (PDF);
  - HY2026 press release;
  - Q3 2026 trading update;
  - Annual Report 2019 (PDF), located by one exploratory search.
- filings.xbrl.org: Heineken N.V. ESEF filings (LEI 724500K5PTPSST86UQ23), xBRL-JSON FY2021–FY2025 and reports FY2022 and FY2024. One exploratory entity lookup.
- query1.finance.yahoo.com: the price.

The theheinekencompany.com report archive (2015–2018 annual reports) is behind an age gate, so it was not retrieved.

P14: 2 exploratory operations (the ESEF entity lookup and the AR2019 search) and 0 due-check operations.
