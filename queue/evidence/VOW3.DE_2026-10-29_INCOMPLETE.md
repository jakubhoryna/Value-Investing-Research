# VOW3.DE — Volkswagen AG (preferred) — INCOMPLETE evidence (REVIEW 2026-10-29)

- Run: REVIEW · D 2026-10-29 · T 0612 · base cb9dd7bf4e7685caf64894f98b385339e553f7b1 · MODEL v4.7.0
- Prior: `memos/VOW3.DE/VOW3.DE_2026-07-09_GSC.md` (memo v1, no `model_version` (pre-v3 format), no §6.1 machine fields, no `lens`, no group build; AVOID on three gates)
- Named gap: **method re-test exceeds budget** (README §5, MODEL §8.7 item 6). No verdict is stated here.

## Why the re-test does not fit one run

The prior predates v4.5.0 and v4.6.0. The REVIEW must apply every rule it predates (REVIEW.md step 4). Because the prior has no machine fields, the new memo must also establish all of them. The scope:

1. **B1–B3 primary rebuild, FY2016–FY2025 plus the FY2015 balance sheet.** The prior carries only FY2021–25, from a tier-2 aggregator that was never tie-out tested (§4), so the window is record-limited. The full ten-year record has to be built from the annual reports: ten fiscal years plus an eleventh balance sheet. The J1 line is the "Operating result". J-charges (diesel special items, restructuring, impairments) stay in OI.
2. **G6 / P31 above the line, both readings, every window year.** The income limb fails in several years (table below), so both readings are owed. The classes are equity-accounted investments (the China JVs) and other equity investments (S3). Each needs its income per year (share of result; dividends inside other financial result) and its carrying value per year.
3. **Captive finance with deposits (R2, STD).** Volkswagen Financial Services is a captive arm with Volkswagen Bank deposits. It needs:
   - OI after funding cost;
   - the ±3% book-change rule on lease assets and financial-services receivables (P20, lending and leasing books);
   - funding principal kept out of FCF;
   - the funding concentration test (P15, strict), with the parent's treasury looked through;
   - both funding pairings at Gate 2, on the P9 and P19 reads too.
4. **P20 maintenance capex**, built per year: the disclosed tier or the constructed tier, with k over the window, euro-area HICP deflators floored at 3%, deal-year tier-3 checks, and the depreciation floor.
5. **Group build (G3, G4, P22, P29).**
   - Three material reportable segments at FY2025 (sourced below): Passenger Cars and Light Commercial Vehicles, Commercial Vehicles, Financial Services.
   - Two material controlled listed subsidiaries:
     - Porsche AG (`P911.DE`): no memo in `memos/`, so it is ungradeable and missing;
     - TRATON (`8TRA.ST`): memo v1 dated 2026-07-22 has no `model_version` (below v4.5.0), so it is stale and ungradeable.
   - Listed-subsidiary NCI at the higher of market and book (R5).
   - B4 with weights and S.
   - The §2·1C·3 allocation-across-the-parts table.
6. **Gate 1C on the R9/V3/R8/J14 rules.** This needs:
   - the hairiest-number pay worksheet over three years from the remuneration reports;
   - the director cap;
   - the P23 alignment call and the votes-versus-economics table: Porsche SE holds 53.3% of the votes per the prior, the ordinary and preferred share classes split votes from economics, and Lower Saxony holds its VW-Law blocking minority;
   - the RPT read of the Porsche SE relationship;
   - the worth test: no repurchases per the prior, to be re-verified;
   - the acquisition stop over FY2023–25 plus the live year.
7. **Gate 2 on the R10 no-cash bound**, including:
   - hybrid capital (€12,379m at 30 Jun 2026) as a debt-equivalent;
   - the P28 test, since FY2025 OI of €8,868m is well below FY2024's €19,060m;
   - the 3-year and 5-year readings;
   - every §6.1 machine field.

## Sourced figures gathered (EUR m)

Sources:
- Volkswagen Group Annual Report 2025 (`2026-03-10-volkswagen-group-annual-report-2025-en.pdf`): consolidated income statement p. 461 and balance sheet p. 464;
- Annual Report 2020 (`Y_2020_e.pdf`): consolidated income statement and balance sheet;
- H1 2026 interim report (`2026-07-24-volkswagen-group-h1-2026-intrim-report-en.pdf`).

All three were retrieved 2026-10-29 from uploads.vw-mms.de, linked from volkswagen-group.com/en/financial-reports-18134.

**P31 inputs (shares derived):**

| FY | Operating result | Share of result of equity-accounted inv. | Share ÷ OI | Equity-accounted inv. (YE) | Total assets (YE) | EAI ÷ TA |
|---|---|---|---|---|---|---|
| 2019 | 16,960 | 3,349 | 19.7% | 8,169 (as printed in AR2020) | n/a this run | n/a |
| 2020 | 9,675 | 2,756 | 28.5% | 10,080 | 497,114 | 2.0% |
| 2024 | 19,060 | 375 | 2.0% | 10,269 | 632,905 | 1.6% |
| 2025 | 8,868 | 930 | 10.5% | 9,996 | 644,467 | 1.6% |

- Other equity investments (S3 class) at YE2025: 7,366; at YE2024: 5,731.
- **P31 result:** the income limb fails in FY2019, FY2020 and FY2025 (each above 5% of OI, on the share of result alone). The classes are therefore above the line, and both readings are owed over the whole window. The asset limb (EAI plus other equity investments ≈ 2.7% of total assets at YE2025, derived) still needs every one of the eleven balance-sheet dates.
- H1 2026: operating result 5,931 (H1 2025: 6,707); share of result of equity-accounted investments 446 (H1 2025: 317).

**FY2025 segments (AR2025, "Key figures for 2025 by segment"; P22 materiality to be completed on assets):**

| Segment | Sales revenue | Segment operating result | Capex incl. capitalised development |
|---|---|---|---|
| Passenger Cars and Light Commercial Vehicles | 244,484 | 4,966 | 20,953 |
| Commercial Vehicles | 42,540 | 2,417 | 2,784 |
| Financial Services | 62,136 | 3,708 | 270 |
| Other Operating Companies | 6,487 | 198 | 335 |
| Reconciliation | −33,733 | −2,420 | 3 |
| Group | 321,913 | 8,868 | 24,346 |

**Balance sheet at 30 Jun 2026 (H1 2026, primary interim; group, with the Automotive and Financial Services divisions):**

| Line | Group | Automotive | Financial Services |
|---|---|---|---|
| Total assets | 669,347 | 426,054 | 336,840 |
| Financial liabilities, non-current | 138,898 | 51,025 | 115,568 |
| Financial liabilities, current | 142,006 | 21,756 | 145,966 |
| Provisions for pensions | 22,325 | 21,976 | 348 |
| Cash and cash equivalents | 40,538 | 28,398 | 15,960 |
| Marketable securities and time deposits | 32,084 | 26,236 | 5,848 |
| Equity attributable to VW AG hybrid capital investors | 12,379 | 12,379 | – |
| Equity attributable to VW AG shareholders | 175,342 | 152,866 | 46,174 |
| Non-controlling interests | 14,738 | 14,393 | 480 |
| Assets held for sale / associated liabilities | 6,246 / 3,594 | 6,220 / 3,594 | 32 / – |

- Division columns do not add to the group; consolidation column not shown here.

**Identity and price:**
- ISIN of the preferred line: DE0007664039; ordinary line: DE0007664005 (AR2025, Volkswagen share data).
- Price endpoint (one GET each): VOW3.DE, EUR, exchangeName GER, last close €68.80 (2026-10-27); VOW.DE €68.35 (2026-10-27).
- No 2026-10-28 bar was returned.

## Hosts tried

- volkswagen-group.com (IR index) and uploads.vw-mms.de (PDFs): retrieved.
- query1.finance.yahoo.com: retrieved.
- data.sec.gov: one due-check on CROX before the claim, which is not this key.

## Still to establish (beyond the scope above)

- FY2015–FY2018 and FY2021–FY2023 primary statements: annual reports 2016–2018 and 2021–2023 are linked on the same IR page.
- Per-year dividends from other equity investments and where the cash received sits in the cash-flow statement.
- Porsche AG and TRATON memos: queue Porsche AG for ANALYSE and TRATON for REVIEW. The parent completes regardless (G4).

*Framework output, not investment advice.*
