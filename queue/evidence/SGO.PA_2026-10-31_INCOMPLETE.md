# SGO.PA — Compagnie de Saint-Gobain S.A. — REVIEW resumable record (INCOMPLETE) — 2026-10-31

## 1. Header

- Key SGO.PA · job REVIEW · D 2026-10-31 · T 0322 · base c064a25d33c8fd6a8727169999243b7cf2b1f149 · live model_version v4.8.0
- Prior memo: memos/SGO.PA/SGO.PA_2026-08-03_GSC.md (memo v1, MODEL v4.0.0, WATCH; no machine fields, no ISIN)
- Named gap: **method re-test exceeds budget**, the second overrun. The prior is below v4.5.0, so one run owes every v4.5.0 rule, the v4.6.0 Gate-0, lens, group and G6 rules, and the v4.8.0 rules (MODEL §8.2 step 3).
- resumes: queue/evidence/SGO.PA_2026-10-08_INCOMPLETE.md (partial 2026-10-08, written under MODEL v4.5.2 before the v4.8.0 record format existed). Its FY2023–FY2025 release figures name the documents but no page or table, so they are listed in §2 as carried pointers to re-derive, never as carried figures.
- No verdict, no grade. Every figure is sourced (document and location) or labelled `derived`.

## 2. Per gate or leg — work done and figures

**Work done this run.** The 2026-10-08 record and the prior memo were read in full. The issuer IR host still refuses scripted access (`www.saint-gobain.com`, HTTP 403 "Verifying your browser"). The French ESEF annual financial reports on `filings.xbrl.org` (LEI NFONVGN05Z0FMN5PEC35) were read as xBRL-JSON: FY2021, FY2022, FY2023 and FY2025 (FY2024 is not listed there; its figures come from the FY2025 report's comparatives). That gives a primary per-year record for FY2020–FY2025. FY2016–FY2019 per-year J1 lines, the P20 split for FY2016–FY2022, the units, the pay table and the deal data were not reached.

**Source key.** `ESEF{Y}` = the Saint-Gobain ESEF annual financial report for FY{Y}, French, xBRL-JSON at `https://filings.xbrl.org/NFONVGN05Z0FMN5PEC35/{Y}-12-31/ESEF/FR/0/{file}.json` (FY2021 `NFONVGN05Z0FMN5PEC35-2021-12-31AR.json`; FY2022 `com-2022-12-31-fr.json`; FY2023 `com-2023-12-31-fr.json`; FY2025 `com-2025-12-31-fr.json`), consolidated statements, located by the tagged concept and period named in the row. Every value in €m. Where two filings tag one period, the values agree.

### Gate 1A — Past: income lines (J1, J3, G6)

| item | FY | value | unit | source |
|---|---|---|---|---|
| Operating income (Résultat d'exploitation, incl. operating equity-method share) | 2020 | 2,855 | €m | ESEF2021, `COM:ProfitLossFromOperatingActivitiesBeforeOtherOperatingIncomeAndExpenses`, 2020 |
| Operating income | 2021 | 4,507 | €m | ESEF2021 and ESEF2022, same concept, 2021 |
| Operating income | 2022 | 5,337 | €m | ESEF2022, same concept, 2022; ESEF2023 `com:ResultatDexploitationIncluantLaQuotePart…Operationnelles`, 2022 |
| Operating income | 2023 | 5,251 | €m | ESEF2023, `com:ResultatDexploitationIncluantLaQuotePartDuResultatDesSocietesMisesEnEquivalenceOperationnelles`, 2023 |
| Operating income | 2024 | 5,304 | €m | ESEF2025, `com:ResultatDexploitationIncluantLaQuotePartDuResultatDesSocietesMisesEnEquivalenceOperationnelles`, 2024 |
| Operating income | 2025 | 5,293 | €m | ESEF2025, same concept, 2025 |
| Business income (Résultat opérationnel, incl. operating equity-method share) — the lowest operating subtotal, J1 candidate | 2020 | 1,432 | €m | ESEF2021, `ifrs-full:ProfitLossFromOperatingActivities`, 2020 |
| Business income | 2021 | 3,936 | €m | ESEF2021 and ESEF2022, same concept, 2021 |
| Business income | 2022 | 4,582 | €m | ESEF2022, same concept, 2022; ESEF2023 `com:ResultatOperationnelIncluantLaQuotePart…Operationnelles`, 2022 |
| Business income | 2023 | 4,231 | €m | ESEF2023, `com:ResultatOperationnelIncluantLaQuotePart…Operationnelles`, 2023 |
| Business income | 2024 | 4,377 | €m | ESEF2025, `com:ResultatOperationnelIncluantLaQuotePartDuResultatDesSocietesMisesEnEquivalenceOperationnelles`, 2024 |
| Business income | 2025 | 4,551 | €m | ESEF2025, same concept, 2025 |
| Share of operating ("core business") equity-method results, inside both lines above | 2020 | 13 | €m | ESEF2021, `COM:ShareOfProfitLossOfAssociatesAndJointVenturesAccountedForUsingEquityMethodCoreBusiness`, 2020 |
| same | 2021 | 52 | €m | ESEF2021/ESEF2022, same concept, 2021 |
| same | 2022 | 61 | €m | ESEF2022, same concept, 2022 |
| same | 2023 | 80 | €m | ESEF2023, `com:QuotePartDansLesResultatsDesSocietesMisesEnEquivalenceOperationnelles`, 2023 |
| same | 2024 | 76 | €m | ESEF2025, same concept, 2024 |
| same | 2025 | 50 | €m | ESEF2025, same concept, 2025 |
| Share of non-operating equity-method results (below Business income) | 2020 / 2021 / 2022 / 2023 / 2024 / 2025 | 2 / 4 / 5 / 9 / 6 / 4 | €m | ESEF2021–ESEF2025, `…NonCoreBusiness` and `com:QuotePartDansLesResultatsDesSocietesMisesEnEquivalenceNonOperationnelles`, each year |
| Interest income on cash and equivalents (financial result) | 2020 / 2021 / 2022 / 2023 / 2024 / 2025 | 6 / 7 / 54 / 229 / 301 / 193 | €m | ESEF2021–ESEF2025, `ifrs-full:InterestIncomeOnCashAndCashEquivalents`, each year |
| Net income, group share | 2020 / 2021 / 2022 / 2023 / 2024 / 2025 | 456 / 2,521 / 3,003 / 2,669 / 2,844 / 2,883 | €m | ESEF2021–ESEF2025, `ifrs-full:ProfitLossAttributableToOwnersOfParent`, each year |
| Business income less operating equity-method share (G6 exclude reading, before any J3 disposal-gain removal) | 2020 / 2021 / 2022 / 2023 / 2024 / 2025 | 1,419 / 3,884 / 4,521 / 4,151 / 4,301 / 4,501 | €m | derived: Business income − core-business equity-method share, rows above |

Composition of the Business-income bridge (disposal results, write-downs, PPA amortisation, structure effects) is sourced only for FY2024–FY2025 in the 2026-10-08 record (results releases, no page cited): re-open it in the FY2024 and FY2025 consolidated statements, note on other business income and expense, for every year (J3: a net disposal gain leaves OI).

### Gate 1A — Past: cash flow and per share

| item | FY | value | unit | source |
|---|---|---|---|---|
| CFO | 2020 / 2021 / 2022 / 2023 / 2024 / 2025 | 4,711 / 4,439 / 5,711 / 6,035 / 5,569 / 5,638 | €m | ESEF2021–ESEF2025, `ifrs-full:CashFlowsFromUsedInOperatingActivities`, each year |
| Capex (PP&E and intangibles acquired, cash-flow statement) | 2020 / 2021 / 2022 / 2023 / 2024 / 2025 | 1,290 / 1,441 / 1,889 / 1,971 / 2,083 / 2,174 | €m | ESEF2021–ESEF2025, `ifrs-full:PurchaseOfPropertyPlantAndEquipmentIntangibleAssetsOtherThanGoodwillInvestmentPropertyAndOtherNoncurrentAssets`, each year |
| D&A and impairment add-back in CFO | 2020 / 2021 / 2022 / 2023 | 2,906 / 2,174 / 2,442 / 2,395 | €m | ESEF2021–ESEF2023, `ifrs-full:AdjustmentsForDepreciationAndAmortisationExpenseAndImpairmentLossReversalOfImpairmentLoss…`, each year (P20 floor needs operating D&A ex right-of-use: owed) |
| Lease principal paid (financing) | 2020 / 2021 / 2022 / 2023 / 2024 / 2025 | 766 / 762 / 725 / 693 / 722 / 756 | €m | ESEF2021–ESEF2025, `ifrs-full:PaymentsOfLeaseLiabilitiesClassifiedAsFinancingActivities`, each year |
| Treasury-share purchases net (statement of changes in equity / cash flow) | 2022 / 2023 / 2024 / 2025 | 781 / 828 / 811 / 778 | €m | ESEF2023 and ESEF2025, `com:AugmentationDiminutionDesActionsPropres` (2024–25 also `ifrs-full:IncreaseDecreaseThroughTreasuryShareTransactions`), each year |
| Diluted weighted average shares | 2020 / 2021 / 2022 / 2023 / 2024 / 2025 | 539.3 / 529.9 / 517.6 / 510.5 / 503.9 / 498.4 | m | ESEF2021–ESEF2025, `ifrs-full:AdjustedWeightedAverageShares`, each year |

Carried pointers to re-derive (2026-10-08 record, FY results releases, no location): capex per release 2,029 / 2,049 / 2,049 and "o/w additional capacity investments" 837 / 842 / 877 (FY2023 / 2024 / 2025); operating D&A 1,986 / 2,137 / 2,141 and right-of-use depreciation 692 / 727 / 747. The release capex differs from the cash-flow capex above (FY2024 2,049 vs 2,083; FY2025 2,049 vs 2,174): reconcile before any P20 build.

### Gate 1A — Past: balance sheet (year-end)

| item | FY | value | unit | source |
|---|---|---|---|---|
| Total assets | 2020 / 2021 / 2022 / 2023 / 2024 / 2025 | 48,626 / 51,584 / 55,377 / 57,299 / 61,718 / 60,836 | €m | ESEF2021–ESEF2025, `ifrs-full:Assets`, each year-end |
| Cash and cash equivalents | 2019 / 2020 / 2021 / 2022 / 2023 / 2024 / 2025 | 4,987 / 8,443 / 6,943 / 6,134 / 8,602 / 8,460 / 7,582 | €m | ESEF2021–ESEF2025, `ifrs-full:CashAndCashEquivalents`, each year-end |
| Short-term deposits not cash equivalents | 2025 | 150 | €m | ESEF2025, `ifrs-full:ShorttermDepositsNotClassifiedAsCashEquivalents`, 31 Dec 2025 |
| Trade payables | 2020 / 2021 / 2022 / 2023 / 2024 / 2025 | 5,897 / 6,903 / 7,266 / 6,806 / 6,773 / 6,809 | €m | ESEF2021–ESEF2025, `ifrs-full:TradeAndOtherCurrentPayablesToTradeSuppliers`, each year-end |
| Other payables and accrued expenses | 2020 / 2021 / 2022 / 2023 / 2024 / 2025 | 3,911 / 4,808 / 5,078 / 5,504 / 5,679 / 5,544 | €m | ESEF2021–ESEF2025, `ifrs-full:OtherCurrentPayables`, each year-end |
| Current tax liabilities | 2020 / 2021 / 2022 / 2023 / 2024 / 2025 | 175 / 236 / 263 / 249 / 240 / 172 | €m | ESEF2021–ESEF2025, `ifrs-full:CurrentTaxLiabilitiesCurrent`, each year-end |
| Total equity (incl. NCI) | 2019 / 2020 / 2021 / 2022 / 2023 / 2024 / 2025 | 19,780 / 18,203 / 21,126 / 23,154 / 23,758 / 25,648 / 25,109 | €m | ESEF2021–ESEF2025, `ifrs-full:Equity`, each year-end |
| Non-controlling interests | 2020 / 2021 / 2022 / 2023 / 2024 / 2025 | 311 / 411 / 443 / 485 / 513 / 568 | €m | ESEF2021–ESEF2025, `ifrs-full:NoncontrollingInterests`, each year-end |
| Goodwill | 2020 / 2021 / 2022 / 2023 / 2024 / 2025 | 10,028 / 11,181 / 12,858 / 13,111 / 14,236 / 14,401 | €m | ESEF2021–ESEF2025, `ifrs-full:Goodwill`, each year-end |
| Other intangible assets | 2020 / 2021 / 2022 / 2023 / 2024 / 2025 | 2,505 / 2,705 / 4,026 / 4,368 / 4,849 / 5,296 | €m | ESEF2021–ESEF2025, `ifrs-full:IntangibleAssetsOtherThanGoodwill`, each year-end |
| Equity-method investments (G6 class) | 2020 / 2021 / 2022 / 2023 / 2024 / 2025 | 462 / 536 / 639 / 705 / 1,005 / 898 | €m | ESEF2021–ESEF2025, `ifrs-full:InvestmentAccountedForUsingEquityMethod`, each year-end |
| Other non-current financial assets (content not split: S3 stakes, loans, deposits) | 2021 / 2022 / 2023 / 2024 / 2025 | 528 / 537 / 596 / 735 / 652 | €m | ESEF2022–ESEF2025, `ifrs-full:OtherNoncurrentFinancialAssets`, each year-end |

The prior memo's B1 (FY2015–FY2025, NIBCL, total liabilities, equity ex-NCI) names the annual consolidated statements but no page: the FY2020–FY2025 values above match its B1 total assets and cash where both exist; FY2015–FY2019 balance sheets are re-opened by the next run.

### Gate 2 — debt-equivalents at 31 Dec 2025 (latest annual; refresh to 30 Jun 2026 owed)

| item | FY | value | unit | source |
|---|---|---|---|---|
| Long-term borrowings, non-current | 2025 | 12,243 | €m | ESEF2025, `ifrs-full:LongtermBorrowings`, 31 Dec 2025 |
| Current portion of long-term borrowings | 2025 | 2,091 | €m | ESEF2025, `ifrs-full:CurrentPortionOfLongtermBorrowings` |
| Short-term borrowings | 2025 | 590 | €m | ESEF2025, `ifrs-full:ShorttermBorrowings` |
| Lease liabilities, non-current / current | 2025 | 2,495 / 669 | €m | ESEF2025, `ifrs-full:NoncurrentLeaseLiabilities` / `ifrs-full:CurrentLeaseLiabilities` |
| Employee-benefit provisions, non-current | 2025 | 1,444 | €m | ESEF2025, `ifrs-full:NoncurrentProvisionsForEmployeeBenefits` |
| Defined-benefit plan assets recognised | 2025 | 332 | €m | ESEF2025, `ifrs-full:NoncurrentRecognisedAssetsDefinedBenefitPlan` |
| Liabilities in disposal groups held for sale | 2025 | 140 | €m | ESEF2025, `ifrs-full:LiabilitiesIncludedInDisposalGroupsClassifiedAsHeldForSale` |

### Price

| item | FY | value | unit | source |
|---|---|---|---|---|
| px (close) | 2026-10-30 | 67.88 | EUR | query1.finance.yahoo.com/v8/finance/chart/SGO.PA, meta currency EUR, exchangeName PAR, "Compagnie de Saint-Gobain S.A."; regularMarketTime 2026-10-30 16:35 UTC; no split events in range=1mo |

## 3. Readings settled (as far as this run got; figures in §2, never a grade)

- **J1 line.** Business income (Résultat opérationnel) is the lowest operating subtotal on the face statement; Operating income (Résultat d'exploitation) excludes restructuring, impairment, PPA amortisation and litigation charges, so it is never OI. Both printed lines include the operating equity-method share (the FY2022–FY2025 concept names say so; FY2022 agrees across both concept sets).
- **G6 / P31, FY2020–FY2025 only.** Class carrying value (equity-method investments alone) 0.95% / 1.04% / 1.15% / 1.23% / 1.63% / 1.48% of total assets; class income (operating plus non-operating equity-method share) 1.1% / 1.4% / 1.5% / 2.1% / 1.9% / 1.2% of the exclude-reading OI (derived, §2). Both limbs hold for these six years on the equity-method class alone. Not settled: the S3 part of other non-current financial assets, and FY2015–FY2019.
- **Record.** P1 needs FY2016–FY2025; FY2016–FY2019 exist and are audited but were not retrieved per year, so the record is record-limited (D3), not history-limited.

## 4. Scope still owed

- [ ] FY2016–FY2019 per-year Business income, operating equity-method share and the other-business-income bridge (disposal gains for J3), and FY2015–FY2019 balance sheets: Saint-Gobain URDs 2016–2019 (www.saint-gobain.com/en/finance, browser-verified host; try an attended browser, or the AMF BDIF, bdif.amf-france.org, whose API answers but whose URD type filter returned nothing this run).
- [ ] P20 for every year: "o/w additional capacity investments" and operating D&A ex right-of-use, FY2016–FY2025, from the results releases or the URD management report; reconcile release capex with cash-flow capex.
- [ ] G6: split other non-current financial assets into S3 stakes, loans and deposits; P31 for FY2015–FY2019.
- [ ] Gate 0 and units: group sentence plus one sentence per material unit (FY2025 regional segments Northern Europe; Southern Europe, ME & Africa; Americas; Asia-Pacific), each with its Future block; the "Industrial solutions" line printed only at group level.
- [ ] v4.8.0 unit statement: the FY2025 group statement that no external customer reaches 10% of sales (prior memo Appendix D) — re-open in the FY2025 segment note.
- [ ] Gate 1C: FY2023–FY2025 pay table (URD chapter on remuneration, French), director fees, P23 alignment, RPT; the point-in-time buyback worth table FY2016–FY2025 and H1 2026 (purchased-share counts and prices; per-year 1% floor); the acquisition stop for CSR (2024, ASX-listed target: its last annual reports), Fosroc, Cemix, Bailey, Building Products of Canada/Kaycan, Xypex, QSI Peru and the North-American waterproofing deal, with the v4.8.0 OI-basis gross-up; GCP (2022) re-read.
- [ ] Gate 2: 30 Jun 2026 interim balance sheet (debt, leases, net pension, NCI at the higher of market and book where listed, held-for-sale), P28 test, 3-year and 5-year averages, the no-cash trigger, every §6.1 machine field and the ISIN from a primary source.
