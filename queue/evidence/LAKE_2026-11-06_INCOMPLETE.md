# LAKE — Lakeland Industries, Inc. — INCOMPLETE evidence, resumable record (ANALYSE 2026-11-06)

## 1. Header

- Key: LAKE · job: ANALYSE · D 2026-11-06 · T 2103 · base sha 009642ca45ca568574971c5dc037cf49bb4dec24
- Live `model_version`: v4.8.0
- Prior memo: none (`model_version`: none). No `memos/LAKE/` or `archive/memos/LAKE/` folder exists at base; no register row matches "Lakeland" (`_REGISTER.md`, `register.csv`); ISIN US5117951062 and the name match no memo front matter in `memos/` or `archive/memos/`. The ISIN is the issuer's ordinary share as known to the analyst; the resume confirms it from a primary document (10-K cover or a Schedule 13D/G CUSIP 511795106).
- Named gap: **group build exceeds budget** (README §5; MODEL §8.7 item 6). **First overrun**: the DRAFT_QUEUE line carries no ` — partial …` note at base.
- No verdict, grade or band is stated here. Every "derived" figure below is arithmetic on cited figures, never a grade.

## 2. Per gate or leg — work done and figures

### Key and price (uncounted endpoint)

- `query1.finance.yahoo.com/v8/finance/chart/LAKE`: `currency` USD, `exchangeName` NGM (NasdaqGM), instrument "Lakeland Industries, Inc.", `instrumentType` EQUITY. Close 2026-11-06 = 8.98 USD. No split events in the 5-day range; a resume re-takes px and checks splits over the window (`&events=split`, `range=10y`).

### Document route (all SEC EDGAR, CIK 798081; `sec_user_agent` sent)

- FY2026 10-K (FYE 2026-01-31): accn 0001193125-26-159176, `lake-20260131.htm`, filed 2026-04-16; 10-K/A accn 0001193125-26-167279 filed 2026-04-21 (cover share-count correction per the queue note; not yet opened).
- Q1 FY2027 10-Q accn 0001193125-26-264001 (period 2026-04-30); Q2 FY2027 10-Q accn 0001193125-26-386590 (period 2026-07-31, filed 2026-09-09; opened: material weakness in ICFR re foreign reporting packages, repeated in Item 4).
- DEF 14A 2026 accn 0000798081-26-000008 (meeting 2026-06-16), fetched, not yet read.
- Multi-year series: SEC XBRL companyfacts `data.sec.gov/api/xbrl/companyfacts/CIK0000798081.json` (values as filed in each 10-K; each row below names the 10-K accession). Tier-2 acceptance (MODEL §4) is not yet run: the resume ties FY2026 and one earlier year out against the face statements on revenue, OI, equity and one composite (net cash = cash − debt − lease liability).

### Gate 0 and the lens (work done)

- Business (10-K FY2026 Item 1, p. 1): global maker of protective apparel — firefighter turnout gear and accessories, high-end chemical protective suits, limited-use/disposable protective clothing, durable woven garments; the high-performance FR/AR and high-visibility lines were sold to National Safety Apparel on 2026-03-27 (Note 14 / subsequent events). Customers named in Item 1 to be read at resume (distributors vs fire departments vs industrial end users).
- Lens: no bank or insurer licence appears anywhere read; STD expected. The FI test is still to be logged in Appendix C.
- **Group status (P22; MODEL §2 Group Gate 0).** The 10-K (Item 1 p. 3; Note 14 "Segment Information", p. 70) reports **seven reportable geographic segments**: U.S. Operations (incl. Corporate), Europe, Mexico, Asia, Canada, Latin America, Other foreign. At least U.S. and Europe are ≥ 10% of external revenue, so LAKE is a group with two or more material units and the full group build is owed (B4 weights and S, one Appendix D block per material unit, the allocation-across-the-parts table). This is why the run overran.
- **Sister-unit merge (P22).** Asia FY2026 total segment sales 50.2 USD m of which intersegment 35.7 (71%) — above 50%, so Asia merges with its main internal customer (to be identified from the note or MD&A; not yet established). Other units' intersegment shares FY2026: U.S. 7.5/89.1, Europe 2.2/56.5, Mexico 2.8/7.5, Canada 0.2/9.1, Latin America 0.5/16.8, Other foreign 6.0/18.3 (all below 50%).
- **Materiality caution for the resume.** Σ positive segment results is tiny in FY2026 (Mexico 0.2, Asia 3.5, Canada 0.3), so the profit limb may make small units material, especially once Asia merges into a loss-making unit. Run all three P22 limbs on the latest FY (revenue, segment assets as share of Σ reportable segments' assets, Σ positive segment results) and log each.

### Segment note (10-K FY2026, Note 14, p. 70; USD m, as printed; "amounts may not foot due to rounding")

| Segment | Net sales FY26 | FY25 | External FY26 | FY25 | Intersegment FY26 | FY25 | Gross profit FY26 | FY25 | Opex FY26 | FY25 | Operating (loss) profit FY26 | FY25 | Total assets FY26 | FY25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| U.S. Operations | 89.1 | 66.7 | 81.6 | 60.4 | 7.5 | 6.3 | (not captured) | | 45.2 | 33.4 | (17.0) | (8.0) | 170.4 | 167.4 |
| Europe | 56.5 | 42.9 | 54.2 | 42.1 | 2.2 | 0.8 | 14.0 | 10.4 | 15.1 | 19.5 | (1.1) | (9.6) | 61.1 | 60.3 |
| Mexico | 7.5 | 7.6 | 4.7 | 5.0 | 2.8 | 2.6 | (0.5) | 0.6 | (0.7) | 2.1 | 0.2 | (1.5) | 11.7 | 13.7 |
| Asia | 50.2 | 53.8 | 14.5 | 13.9 | 35.7 | 39.9 | 9.8 | 12.1 | 6.3 | 5.6 | 3.5 | 6.5 | owed | owed |
| Canada | 9.1 | 10.3 | 8.9 | 10.3 | 0.2 | — | 2.8 | 4.1 | 2.5 | 4.2 | 0.3 | (0.2) | owed | owed |
| Latin America | 16.8 | 21.3 | 16.4 | 21.2 | 0.5 | 0.1 | 5.3 | 9.8 | 5.7 | 5.4 | (0.4) | 4.5 | owed | owed |
| Other foreign | 18.3 | 18.3 | 12.3 | 14.3 | 6.0 | 4.0 | 5.8 | 7.4 | 6.1 | 9.1 | (0.3) | (1.7) | owed | owed |
| Intersegment elim. | (54.9) | (53.7) | | | | | (2.1) | (0.7) | (1.4) | (1.4) | (0.7) | (0.7) | | |
| Consolidated | 192.6 | 167.2 | 192.6 | 167.2 | | | 63.3 | 68.7 | 78.8 | 77.9 | (15.5) | (9.3) | | |

Footnote (1) to opex: includes the goodwill impairment, the gain on the sale-leaseback transaction and lease impairments (so segment operating profit is after those J1 charges). FY2024 segment figures (from the FY2025 10-K, accn 0001654954-25-004352) are owed for the latest-3-FY P29 weights and the allocation window.

### Past (B1 inputs; figures as filed, XBRL companyfacts)

Window: FY2017–FY2026 (10 fiscal years; 11 balance sheets FY2016–FY2026 — full P1 record, no history or record limit on the face of it). Fiscal year ends 31 January (FY2026 = year to 2026-01-31).

| item | FY | value | unit | source |
|---|---|---|---|---|
| Revenue | FY2016 (FYE 2016-01-31) | 99646 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:SalesRevenueGoodsNet, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Revenue | FY2017 (FYE 2017-01-31) | 86183 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:SalesRevenueGoodsNet, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Revenue | FY2018 (FYE 2018-01-31) | 95987 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:SalesRevenueGoodsNet, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Revenue | FY2019 (FYE 2019-01-31) | 99011 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Revenues, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| Revenue | FY2020 (FYE 2020-01-31) | 107809 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Revenues, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| Revenue | FY2021 (FYE 2021-01-31) | 159000 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Revenues, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| Revenue | FY2022 (FYE 2022-01-31) | 118386 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Revenues, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| Revenue | FY2023 (FYE 2023-01-31) | 112846 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Revenues, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Revenue | FY2024 (FYE 2024-01-31) | 124688 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Revenues, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Revenue | FY2025 (FYE 2025-01-31) | 167211 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Revenues, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Revenue | FY2026 (FYE 2026-01-31) | 192648 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Revenues, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| OI (operating income/loss, face) | FY2016 (FYE 2016-01-31) | 11812 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OperatingIncomeLoss, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| OI (operating income/loss, face) | FY2017 (FYE 2017-01-31) | 6847 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OperatingIncomeLoss, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| OI (operating income/loss, face) | FY2018 (FYE 2018-01-31) | 8477 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OperatingIncomeLoss, as filed in 10-K accn 0001654954-19-004479 (filed 2019-04-16) |
| OI (operating income/loss, face) | FY2019 (FYE 2019-01-31) | 3565 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OperatingIncomeLoss, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| OI (operating income/loss, face) | FY2020 (FYE 2020-01-31) | 5876 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OperatingIncomeLoss, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| OI (operating income/loss, face) | FY2021 (FYE 2021-01-31) | 43886 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OperatingIncomeLoss, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| OI (operating income/loss, face) | FY2022 (FYE 2022-01-31) | 16047 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OperatingIncomeLoss, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| OI (operating income/loss, face) | FY2023 (FYE 2023-01-31) | 5541 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OperatingIncomeLoss, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| OI (operating income/loss, face) | FY2024 (FYE 2024-01-31) | 5993 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OperatingIncomeLoss, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| OI (operating income/loss, face) | FY2025 (FYE 2025-01-31) | -9265 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OperatingIncomeLoss, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| OI (operating income/loss, face) | FY2026 (FYE 2026-01-31) | -15512 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OperatingIncomeLoss, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| CFO | FY2016 (FYE 2016-01-31) | -518 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetCashProvidedByUsedInOperatingActivities, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| CFO | FY2017 (FYE 2017-01-31) | 11493 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetCashProvidedByUsedInOperatingActivities, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| CFO | FY2018 (FYE 2018-01-31) | 648 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetCashProvidedByUsedInOperatingActivities, as filed in 10-K accn 0001654954-19-004479 (filed 2019-04-16) |
| CFO | FY2019 (FYE 2019-01-31) | 1785 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetCashProvidedByUsedInOperatingActivities, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| CFO | FY2020 (FYE 2020-01-31) | 3590 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetCashProvidedByUsedInOperatingActivities, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| CFO | FY2021 (FYE 2021-01-31) | 40666 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetCashProvidedByUsedInOperatingActivities, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| CFO | FY2022 (FYE 2022-01-31) | 12785 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetCashProvidedByUsedInOperatingActivities, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| CFO | FY2023 (FYE 2023-01-31) | -5451 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetCashProvidedByUsedInOperatingActivities, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| CFO | FY2024 (FYE 2024-01-31) | 10912 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetCashProvidedByUsedInOperatingActivities, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| CFO | FY2025 (FYE 2025-01-31) | -15881 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetCashProvidedByUsedInOperatingActivities, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| CFO | FY2026 (FYE 2026-01-31) | -15750 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetCashProvidedByUsedInOperatingActivities, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Capex (PP&E purchases) | FY2016 (FYE 2016-01-31) | 840 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsToAcquirePropertyPlantAndEquipment, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Capex (PP&E purchases) | FY2017 (FYE 2017-01-31) | 413 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsToAcquirePropertyPlantAndEquipment, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Capex (PP&E purchases) | FY2018 (FYE 2018-01-31) | 905 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsToAcquirePropertyPlantAndEquipment, as filed in 10-K accn 0001654954-19-004479 (filed 2019-04-16) |
| Capex (PP&E purchases) | FY2019 (FYE 2019-01-31) | 3103 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsToAcquirePropertyPlantAndEquipment, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| Capex (PP&E purchases) | FY2020 (FYE 2020-01-31) | 1033 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsToAcquirePropertyPlantAndEquipment, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| Capex (PP&E purchases) | FY2021 (FYE 2021-01-31) | 1662 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsToAcquirePropertyPlantAndEquipment, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| Capex (PP&E purchases) | FY2022 (FYE 2022-01-31) | 801 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsToAcquirePropertyPlantAndEquipment, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| Capex (PP&E purchases) | FY2023 (FYE 2023-01-31) | 1985 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsToAcquirePropertyPlantAndEquipment, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Capex (PP&E purchases) | FY2024 (FYE 2024-01-31) | 2069 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsToAcquirePropertyPlantAndEquipment, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Capex (PP&E purchases) | FY2025 (FYE 2025-01-31) | 1540 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsToAcquirePropertyPlantAndEquipment, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Capex (PP&E purchases) | FY2026 (FYE 2026-01-31) | 671 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsToAcquirePropertyPlantAndEquipment, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| D&A | FY2016 (FYE 2016-01-31) | 986 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:DepreciationDepletionAndAmortization, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| D&A | FY2017 (FYE 2017-01-31) | 1194 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:DepreciationDepletionAndAmortization, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| D&A | FY2018 (FYE 2018-01-31) | 775 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:DepreciationDepletionAndAmortization, as filed in 10-K accn 0001654954-19-004479 (filed 2019-04-16) |
| D&A | FY2019 (FYE 2019-01-31) | 965 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:DepreciationDepletionAndAmortization, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| D&A | FY2020 (FYE 2020-01-31) | 1645 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:DepreciationDepletionAndAmortization, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| D&A | FY2021 (FYE 2021-01-31) | 1965 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:DepreciationDepletionAndAmortization, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| D&A | FY2022 (FYE 2022-01-31) | 1868 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:DepreciationDepletionAndAmortization, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| D&A | FY2023 (FYE 2023-01-31) | 1505 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:DepreciationDepletionAndAmortization, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| D&A | FY2024 (FYE 2024-01-31) | 1900 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:DepreciationDepletionAndAmortization, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| D&A | FY2025 (FYE 2025-01-31) | 2600 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:DepreciationDepletionAndAmortization, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| D&A | FY2026 (FYE 2026-01-31) | 2800 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:DepreciationDepletionAndAmortization, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Acquired-intangible amortisation | FY2016 (FYE 2016-01-31) | 101 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AmortizationOfIntangibleAssets, as filed in 10-K accn 0001144204-16-095568 (filed 2016-04-21) |
| Acquired-intangible amortisation | FY2023 (FYE 2023-01-31) | 67 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AmortizationOfIntangibleAssets, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Acquired-intangible amortisation | FY2024 (FYE 2024-01-31) | 423 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AmortizationOfIntangibleAssets, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Acquired-intangible amortisation | FY2025 (FYE 2025-01-31) | 997 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AmortizationOfIntangibleAssets, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Acquired-intangible amortisation | FY2026 (FYE 2026-01-31) | 2200 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AmortizationOfIntangibleAssets, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Diluted wtd avg shares | FY2016 (FYE 2016-01-31) | 7254 | k shares | SEC XBRL companyfacts CIK0000798081, us-gaap:WeightedAverageNumberOfDilutedSharesOutstanding, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Diluted wtd avg shares | FY2017 (FYE 2017-01-31) | 7327 | k shares | SEC XBRL companyfacts CIK0000798081, us-gaap:WeightedAverageNumberOfDilutedSharesOutstanding, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Diluted wtd avg shares | FY2018 (FYE 2018-01-31) | 7692 | k shares | SEC XBRL companyfacts CIK0000798081, us-gaap:WeightedAverageNumberOfDilutedSharesOutstanding, as filed in 10-K accn 0001654954-19-004479 (filed 2019-04-16) |
| Diluted wtd avg shares | FY2019 (FYE 2019-01-31) | 8170 | k shares | SEC XBRL companyfacts CIK0000798081, us-gaap:WeightedAverageNumberOfDilutedSharesOutstanding, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| Diluted wtd avg shares | FY2020 (FYE 2020-01-31) | 8037 | k shares | SEC XBRL companyfacts CIK0000798081, us-gaap:WeightedAverageNumberOfDilutedSharesOutstanding, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| Diluted wtd avg shares | FY2021 (FYE 2021-01-31) | 8141 | k shares | SEC XBRL companyfacts CIK0000798081, us-gaap:WeightedAverageNumberOfDilutedSharesOutstanding, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| Diluted wtd avg shares | FY2022 (FYE 2022-01-31) | 8054 | k shares | SEC XBRL companyfacts CIK0000798081, us-gaap:WeightedAverageNumberOfDilutedSharesOutstanding, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| Diluted wtd avg shares | FY2023 (FYE 2023-01-31) | 7738 | k shares | SEC XBRL companyfacts CIK0000798081, us-gaap:WeightedAverageNumberOfDilutedSharesOutstanding, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Diluted wtd avg shares | FY2024 (FYE 2024-01-31) | 7540 | k shares | SEC XBRL companyfacts CIK0000798081, us-gaap:WeightedAverageNumberOfDilutedSharesOutstanding, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Diluted wtd avg shares | FY2025 (FYE 2025-01-31) | 7426 | k shares | SEC XBRL companyfacts CIK0000798081, us-gaap:WeightedAverageNumberOfDilutedSharesOutstanding, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Diluted wtd avg shares | FY2026 (FYE 2026-01-31) | 9626 | k shares | SEC XBRL companyfacts CIK0000798081, us-gaap:WeightedAverageNumberOfDilutedSharesOutstanding, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Net income | FY2016 (FYE 2016-01-31) | 3854 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetIncomeLoss, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Net income | FY2017 (FYE 2017-01-31) | 3893 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetIncomeLoss, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Net income | FY2018 (FYE 2018-01-31) | 440 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetIncomeLoss, as filed in 10-K accn 0001654954-19-004479 (filed 2019-04-16) |
| Net income | FY2019 (FYE 2019-01-31) | 1459 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetIncomeLoss, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| Net income | FY2020 (FYE 2020-01-31) | 3281 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetIncomeLoss, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| Net income | FY2021 (FYE 2021-01-31) | 35330 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetIncomeLoss, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| Net income | FY2022 (FYE 2022-01-31) | 11372 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetIncomeLoss, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| Net income | FY2023 (FYE 2023-01-31) | 1873 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetIncomeLoss, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Net income | FY2024 (FYE 2024-01-31) | 5425 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetIncomeLoss, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Net income | FY2025 (FYE 2025-01-31) | -18075 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetIncomeLoss, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Net income | FY2026 (FYE 2026-01-31) | -25311 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:NetIncomeLoss, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Share-based pay | FY2016 (FYE 2016-01-31) | 586 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ShareBasedCompensation, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Share-based pay | FY2017 (FYE 2017-01-31) | 276 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ShareBasedCompensation, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Share-based pay | FY2018 (FYE 2018-01-31) | 424 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ShareBasedCompensation, as filed in 10-K accn 0001654954-19-004479 (filed 2019-04-16) |
| Share-based pay | FY2019 (FYE 2019-01-31) | 744 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ShareBasedCompensation, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| Share-based pay | FY2020 (FYE 2020-01-31) | -403 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ShareBasedCompensation, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| Share-based pay | FY2021 (FYE 2021-01-31) | 1727 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ShareBasedCompensation, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| Share-based pay | FY2022 (FYE 2022-01-31) | 1667 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ShareBasedCompensation, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| Share-based pay | FY2023 (FYE 2023-01-31) | 1491 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ShareBasedCompensation, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Share-based pay | FY2024 (FYE 2024-01-31) | 1365 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ShareBasedCompensation, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Share-based pay | FY2025 (FYE 2025-01-31) | 1558 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ShareBasedCompensation, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Share-based pay | FY2026 (FYE 2026-01-31) | 3391 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ShareBasedCompensation, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Goodwill impairment | FY2016 (FYE 2016-01-31) | 0 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:GoodwillImpairmentLoss, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Goodwill impairment | FY2017 (FYE 2017-01-31) | 0 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:GoodwillImpairmentLoss, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Goodwill impairment | FY2018 (FYE 2018-01-31) | 0 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:GoodwillImpairmentLoss, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Goodwill impairment | FY2024 (FYE 2024-01-31) | 0 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:GoodwillImpairmentLoss, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Goodwill impairment | FY2025 (FYE 2025-01-31) | 10538 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:GoodwillImpairmentLoss, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Goodwill impairment | FY2026 (FYE 2026-01-31) | 2604 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:GoodwillImpairmentLoss, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Equity-method investment impairment | FY2024 (FYE 2024-01-31) | 0 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ImpairmentOfInvestments, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Equity-method investment impairment | FY2025 (FYE 2025-01-31) | 7639 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ImpairmentOfInvestments, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Repurchases (cash) | FY2018 (FYE 2018-01-31) | 0 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsForRepurchaseOfEquity, as filed in 10-K accn 0001654954-19-004479 (filed 2019-04-16) |
| Repurchases (cash) | FY2019 (FYE 2019-01-31) | 1165 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsForRepurchaseOfEquity, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| Repurchases (cash) | FY2020 (FYE 2020-01-31) | 506 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsForRepurchaseOfEquity, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| Repurchases (cash) | FY2021 (FYE 2021-01-31) | 0 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsForRepurchaseOfEquity, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| Repurchases (cash) | FY2022 (FYE 2022-01-31) | 9183 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsForRepurchaseOfEquity, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| Repurchases (cash) | FY2023 (FYE 2023-01-31) | 5439 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsForRepurchaseOfEquity, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Repurchases (cash) | FY2024 (FYE 2024-01-31) | 333 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsForRepurchaseOfEquity, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Dividends paid | FY2024 (FYE 2024-01-31) | 908 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsOfDividends, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Dividends paid | FY2025 (FYE 2025-01-31) | 887 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsOfDividends, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Dividends paid | FY2026 (FYE 2026-01-31) | 1152 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsOfDividends, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Acquisitions, net of cash | FY2024 (FYE 2024-01-31) | 5452 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsToAcquireBusinessesNetOfCashAcquired, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Acquisitions, net of cash | FY2025 (FYE 2025-01-31) | 45084 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsToAcquireBusinessesNetOfCashAcquired, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Acquisitions, net of cash | FY2026 (FYE 2026-01-31) | 6165 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PaymentsToAcquireBusinessesNetOfCashAcquired, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Total assets | FY2016 (FYE 2016-01-31) | 88260 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Assets, as filed in 10-K accn 0001144204-17-022256 (filed 2017-04-26) |
| Total assets | FY2017 (FYE 2017-01-31) | 84554 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Assets, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Total assets | FY2018 (FYE 2018-01-31) | 94531 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Assets, as filed in 10-K accn 0001654954-19-004479 (filed 2019-04-16) |
| Total assets | FY2019 (FYE 2019-01-31) | 94723 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Assets, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| Total assets | FY2020 (FYE 2020-01-31) | 99405 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Assets, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| Total assets | FY2021 (FYE 2021-01-31) | 139550 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Assets, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| Total assets | FY2022 (FYE 2022-01-31) | 140793 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Assets, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| Total assets | FY2023 (FYE 2023-01-31) | 142936 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Assets, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Total assets | FY2024 (FYE 2024-01-31) | 153745 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Assets, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Total assets | FY2025 (FYE 2025-01-31) | 212531 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Assets, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Total assets | FY2026 (FYE 2026-01-31) | 209933 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Assets, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Accounts payable | FY2016 (FYE 2016-01-31) | 4254 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AccountsPayableCurrent, as filed in 10-K accn 0001144204-17-022256 (filed 2017-04-26) |
| Accounts payable | FY2017 (FYE 2017-01-31) | 4928 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AccountsPayableCurrent, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Accounts payable | FY2018 (FYE 2018-01-31) | 6855 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AccountsPayableCurrent, as filed in 10-K accn 0001654954-19-004479 (filed 2019-04-16) |
| Accounts payable | FY2019 (FYE 2019-01-31) | 6214 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AccountsPayableCurrent, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| Accounts payable | FY2020 (FYE 2020-01-31) | 7204 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AccountsPayableCurrent, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| Accounts payable | FY2021 (FYE 2021-01-31) | 7397 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AccountsPayableCurrent, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| Accounts payable | FY2022 (FYE 2022-01-31) | 5855 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AccountsPayableCurrent, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| Accounts payable | FY2023 (FYE 2023-01-31) | 6558 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AccountsPayableCurrent, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Accounts payable | FY2024 (FYE 2024-01-31) | 7378 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AccountsPayableCurrent, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Accounts payable | FY2025 (FYE 2025-01-31) | 15742 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AccountsPayableCurrent, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Accounts payable | FY2026 (FYE 2026-01-31) | 15565 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AccountsPayableCurrent, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Accrued expenses (pre-FY2023 tag) | FY2016 (FYE 2016-01-31) | 1813 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AccruedLiabilitiesCurrent, as filed in 10-K accn 0001144204-17-022256 (filed 2017-04-26) |
| Accrued expenses (pre-FY2023 tag) | FY2017 (FYE 2017-01-31) | 1024 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AccruedLiabilitiesCurrent, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Accrued expenses (pre-FY2023 tag) | FY2018 (FYE 2018-01-31) | 1384 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AccruedLiabilitiesCurrent, as filed in 10-K accn 0001654954-19-004479 (filed 2019-04-16) |
| Accrued expenses (pre-FY2023 tag) | FY2019 (FYE 2019-01-31) | 2825 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AccruedLiabilitiesCurrent, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| Accrued expenses (pre-FY2023 tag) | FY2020 (FYE 2020-01-31) | 2445 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AccruedLiabilitiesCurrent, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| Accrued expenses (pre-FY2023 tag) | FY2021 (FYE 2021-01-31) | 1793 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AccruedLiabilitiesCurrent, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| Accrued expenses (pre-FY2023 tag) | FY2022 (FYE 2022-01-31) | 1372 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:AccruedLiabilitiesCurrent, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| Other accrued liabilities | FY2022 (FYE 2022-01-31) | 1372 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OtherAccruedLiabilitiesCurrent, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| Other accrued liabilities | FY2023 (FYE 2023-01-31) | 4068 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OtherAccruedLiabilitiesCurrent, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Other accrued liabilities | FY2024 (FYE 2024-01-31) | 2487 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OtherAccruedLiabilitiesCurrent, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Other accrued liabilities | FY2025 (FYE 2025-01-31) | 8130 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OtherAccruedLiabilitiesCurrent, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Other accrued liabilities | FY2026 (FYE 2026-01-31) | 8964 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OtherAccruedLiabilitiesCurrent, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Accrued compensation | FY2016 (FYE 2016-01-31) | 1157 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:EmployeeRelatedLiabilitiesCurrent, as filed in 10-K accn 0001144204-17-022256 (filed 2017-04-26) |
| Accrued compensation | FY2017 (FYE 2017-01-31) | 1311 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:EmployeeRelatedLiabilitiesCurrent, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Accrued compensation | FY2018 (FYE 2018-01-31) | 1771 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:EmployeeRelatedLiabilitiesCurrent, as filed in 10-K accn 0001654954-19-004479 (filed 2019-04-16) |
| Accrued compensation | FY2019 (FYE 2019-01-31) | 1137 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:EmployeeRelatedLiabilitiesCurrent, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| Accrued compensation | FY2020 (FYE 2020-01-31) | 1300 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:EmployeeRelatedLiabilitiesCurrent, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| Accrued compensation | FY2021 (FYE 2021-01-31) | 4694 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:EmployeeRelatedLiabilitiesCurrent, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| Accrued compensation | FY2022 (FYE 2022-01-31) | 3225 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:EmployeeRelatedLiabilitiesCurrent, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| Accrued compensation | FY2023 (FYE 2023-01-31) | 2522 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:EmployeeRelatedLiabilitiesCurrent, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Accrued compensation | FY2024 (FYE 2024-01-31) | 3922 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:EmployeeRelatedLiabilitiesCurrent, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Accrued compensation | FY2025 (FYE 2025-01-31) | 4501 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:EmployeeRelatedLiabilitiesCurrent, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Accrued compensation | FY2026 (FYE 2026-01-31) | 4984 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:EmployeeRelatedLiabilitiesCurrent, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Income taxes payable | FY2020 (FYE 2020-01-31) | 0 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:TaxesPayableCurrent, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| Income taxes payable | FY2021 (FYE 2021-01-31) | 1534 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:TaxesPayableCurrent, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| Income taxes payable | FY2022 (FYE 2022-01-31) | 321 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:TaxesPayableCurrent, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| Income taxes payable | FY2023 (FYE 2023-01-31) | 609 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:TaxesPayableCurrent, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Income taxes payable | FY2024 (FYE 2024-01-31) | 1454 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:TaxesPayableCurrent, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Income taxes payable | FY2025 (FYE 2025-01-31) | 1993 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:TaxesPayableCurrent, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Income taxes payable | FY2026 (FYE 2026-01-31) | 1802 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:TaxesPayableCurrent, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Cash & equivalents (incl. restricted where tagged) | FY2021 (FYE 2021-01-31) | 52596 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| Cash & equivalents (incl. restricted where tagged) | FY2022 (FYE 2022-01-31) | 52719 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Cash & equivalents (incl. restricted where tagged) | FY2023 (FYE 2023-01-31) | 24639 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Cash & equivalents (incl. restricted where tagged) | FY2024 (FYE 2024-01-31) | 25222 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Cash & equivalents (incl. restricted where tagged) | FY2025 (FYE 2025-01-31) | 17476 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Cash & equivalents (incl. restricted where tagged) | FY2026 (FYE 2026-01-31) | 12515 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Cash & equivalents | FY2016 (FYE 2016-01-31) | 7022 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:CashAndCashEquivalentsAtCarryingValue, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Cash & equivalents | FY2017 (FYE 2017-01-31) | 10365 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:CashAndCashEquivalentsAtCarryingValue, as filed in 10-K accn 0001654954-19-004479 (filed 2019-04-16) |
| Cash & equivalents | FY2018 (FYE 2018-01-31) | 15788 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:CashAndCashEquivalentsAtCarryingValue, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| Cash & equivalents | FY2019 (FYE 2019-01-31) | 12831 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:CashAndCashEquivalentsAtCarryingValue, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| Cash & equivalents | FY2020 (FYE 2020-01-31) | 14606 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:CashAndCashEquivalentsAtCarryingValue, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| Cash & equivalents | FY2021 (FYE 2021-01-31) | 52596 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:CashAndCashEquivalentsAtCarryingValue, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| Cash & equivalents | FY2022 (FYE 2022-01-31) | 52719 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:CashAndCashEquivalentsAtCarryingValue, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| Cash & equivalents | FY2023 (FYE 2023-01-31) | 24639 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:CashAndCashEquivalentsAtCarryingValue, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Cash & equivalents | FY2024 (FYE 2024-01-31) | 25222 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:CashAndCashEquivalentsAtCarryingValue, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Total liabilities | FY2016 (FYE 2016-01-31) | 20744 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Liabilities, as filed in 10-K accn 0001144204-17-022256 (filed 2017-04-26) |
| Total liabilities | FY2017 (FYE 2017-01-31) | 13047 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Liabilities, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Total liabilities | FY2018 (FYE 2018-01-31) | 11691 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Liabilities, as filed in 10-K accn 0001654954-19-004479 (filed 2019-04-16) |
| Total liabilities | FY2019 (FYE 2019-01-31) | 11495 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Liabilities, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| Total liabilities | FY2020 (FYE 2020-01-31) | 14353 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Liabilities, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| Total liabilities | FY2021 (FYE 2021-01-31) | 17799 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Liabilities, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| Total liabilities | FY2022 (FYE 2022-01-31) | 15693 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Liabilities, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| Total liabilities | FY2023 (FYE 2023-01-31) | 22946 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Liabilities, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Total liabilities | FY2024 (FYE 2024-01-31) | 30294 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Liabilities, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Total liabilities | FY2025 (FYE 2025-01-31) | 65905 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Liabilities, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Total liabilities | FY2026 (FYE 2026-01-31) | 80806 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Liabilities, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Stockholders equity | FY2016 (FYE 2016-01-31) | 67516 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:StockholdersEquity, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Stockholders equity | FY2017 (FYE 2017-01-31) | 71507 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:StockholdersEquity, as filed in 10-K accn 0001654954-19-004479 (filed 2019-04-16) |
| Stockholders equity | FY2018 (FYE 2018-01-31) | 82840 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:StockholdersEquity, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| Stockholders equity | FY2019 (FYE 2019-01-31) | 83228 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:StockholdersEquity, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| Stockholders equity | FY2020 (FYE 2020-01-31) | 85052 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:StockholdersEquity, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| Stockholders equity | FY2021 (FYE 2021-01-31) | 121751 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:StockholdersEquity, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| Stockholders equity | FY2022 (FYE 2022-01-31) | 125100 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:StockholdersEquity, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Stockholders equity | FY2023 (FYE 2023-01-31) | 119990 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:StockholdersEquity, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Stockholders equity | FY2024 (FYE 2024-01-31) | 123450 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:StockholdersEquity, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Stockholders equity | FY2025 (FYE 2025-01-31) | 146626 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:StockholdersEquity, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Stockholders equity | FY2026 (FYE 2026-01-31) | 129127 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:StockholdersEquity, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Goodwill | FY2016 (FYE 2016-01-31) | 871 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Goodwill, as filed in 10-K accn 0001144204-17-022256 (filed 2017-04-26) |
| Goodwill | FY2017 (FYE 2017-01-31) | 871 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Goodwill, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Goodwill | FY2018 (FYE 2018-01-31) | 871 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Goodwill, as filed in 10-K accn 0001654954-19-004479 (filed 2019-04-16) |
| Goodwill | FY2019 (FYE 2019-01-31) | 871 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Goodwill, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| Goodwill | FY2020 (FYE 2020-01-31) | 871 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Goodwill, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| Goodwill | FY2021 (FYE 2021-01-31) | 871 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Goodwill, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| Goodwill | FY2022 (FYE 2022-01-31) | 871 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Goodwill, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Goodwill | FY2023 (FYE 2023-01-31) | 8473 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Goodwill, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Goodwill | FY2024 (FYE 2024-01-31) | 13669 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Goodwill, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Goodwill | FY2025 (FYE 2025-01-31) | 16240 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Goodwill, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Goodwill | FY2026 (FYE 2026-01-31) | 15287 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:Goodwill, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Intangibles net | FY2016 (FYE 2016-01-31) | 95 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:IntangibleAssetsNetExcludingGoodwill, as filed in 10-K accn 0001144204-16-095568 (filed 2016-04-21) |
| Intangibles net | FY2022 (FYE 2022-01-31) | 0 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:IntangibleAssetsNetExcludingGoodwill, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Intangibles net | FY2023 (FYE 2023-01-31) | 6042 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:IntangibleAssetsNetExcludingGoodwill, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Intangibles net | FY2024 (FYE 2024-01-31) | 6830 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:IntangibleAssetsNetExcludingGoodwill, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Intangibles net | FY2025 (FYE 2025-01-31) | 25503 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:IntangibleAssetsNetExcludingGoodwill, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Intangibles net | FY2026 (FYE 2026-01-31) | 31724 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:IntangibleAssetsNetExcludingGoodwill, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Net PP&E | FY2016 (FYE 2016-01-31) | 9268 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PropertyPlantAndEquipmentNet, as filed in 10-K accn 0001144204-17-022256 (filed 2017-04-26) |
| Net PP&E | FY2017 (FYE 2017-01-31) | 8527 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PropertyPlantAndEquipmentNet, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Net PP&E | FY2018 (FYE 2018-01-31) | 8789 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PropertyPlantAndEquipmentNet, as filed in 10-K accn 0001654954-19-004479 (filed 2019-04-16) |
| Net PP&E | FY2019 (FYE 2019-01-31) | 10781 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PropertyPlantAndEquipmentNet, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| Net PP&E | FY2020 (FYE 2020-01-31) | 10113 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PropertyPlantAndEquipmentNet, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| Net PP&E | FY2021 (FYE 2021-01-31) | 9819 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PropertyPlantAndEquipmentNet, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| Net PP&E | FY2022 (FYE 2022-01-31) | 8714 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PropertyPlantAndEquipmentNet, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| Net PP&E | FY2023 (FYE 2023-01-31) | 9140 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PropertyPlantAndEquipmentNet, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Net PP&E | FY2024 (FYE 2024-01-31) | 10685 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PropertyPlantAndEquipmentNet, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Net PP&E | FY2025 (FYE 2025-01-31) | 13948 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PropertyPlantAndEquipmentNet, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Net PP&E | FY2026 (FYE 2026-01-31) | 11640 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:PropertyPlantAndEquipmentNet, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Operating lease liability | FY2020 (FYE 2020-01-31) | 2249 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OperatingLeaseLiability, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| Operating lease liability | FY2021 (FYE 2021-01-31) | 2381 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OperatingLeaseLiability, as filed in 10-K accn 0001654954-21-004289 (filed 2021-04-16) |
| Operating lease liability | FY2022 (FYE 2022-01-31) | 4920 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OperatingLeaseLiability, as filed in 10-K accn 0001654954-22-005270 (filed 2022-04-21) |
| Operating lease liability | FY2023 (FYE 2023-01-31) | 4906 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OperatingLeaseLiability, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| Operating lease liability | FY2024 (FYE 2024-01-31) | 11285 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OperatingLeaseLiability, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Operating lease liability | FY2025 (FYE 2025-01-24) | 14283 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OperatingLeaseLiability, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Operating lease liability | FY2026 (FYE 2026-01-31) | 15020 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:OperatingLeaseLiability, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Debt (LongTermDebt tag, incl. current) | FY2016 (FYE 2016-01-31) | 13425 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:LongTermDebt, as filed in 10-K accn 0001144204-16-095568 (filed 2016-04-21) |
| Debt (LongTermDebt tag, incl. current) | FY2017 (FYE 2017-01-31) | 5784 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:LongTermDebt, as filed in 10-K accn 0001144204-17-022256 (filed 2017-04-26) |
| Debt (LongTermDebt tag, incl. current) | FY2018 (FYE 2018-01-31) | 1681 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:LongTermDebt, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Debt (LongTermDebt tag, incl. current) | FY2019 (FYE 2019-01-31) | 1319 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:LongTermDebt, as filed in 10-K accn 0001654954-19-004479 (filed 2019-04-16) |
| Debt (LongTermDebt tag, incl. current) | FY2020 (FYE 2020-01-31) | 1155 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:LongTermDebt, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| Debt (LongTermDebt tag, incl. current) | FY2025 (FYE 2025-01-31) | 16426 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:LongTermDebt, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Debt (LongTermDebt tag, incl. current) | FY2026 (FYE 2026-01-31) | 30382 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:LongTermDebt, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Short-term borrowings | FY2016 (FYE 2016-01-31) | 3226 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ShortTermBorrowings, as filed in 10-K accn 0001144204-17-022256 (filed 2017-04-26) |
| Short-term borrowings | FY2017 (FYE 2017-01-31) | 153 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ShortTermBorrowings, as filed in 10-K accn 0001144204-18-020717 (filed 2018-04-16) |
| Short-term borrowings | FY2018 (FYE 2018-01-31) | 211 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ShortTermBorrowings, as filed in 10-K accn 0001654954-19-004479 (filed 2019-04-16) |
| Short-term borrowings | FY2019 (FYE 2019-01-31) | 0 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ShortTermBorrowings, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| Short-term borrowings | FY2020 (FYE 2020-01-31) | 0 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ShortTermBorrowings, as filed in 10-K accn 0001654954-20-004107 (filed 2020-04-15) |
| Short-term borrowings | FY2022 (FYE 2022-01-31) | 0 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ShortTermBorrowings, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| Short-term borrowings | FY2023 (FYE 2023-01-31) | 405 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ShortTermBorrowings, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Short-term borrowings | FY2024 (FYE 2024-01-31) | 298 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ShortTermBorrowings, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Short-term borrowings | FY2025 (FYE 2025-01-31) | 939 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:ShortTermBorrowings, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Equity-method investment (Bodytrak) | FY2024 (FYE 2024-01-31) | 4719 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:EquityMethodInvestments, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Equity-method investment (Bodytrak) | FY2025 (FYE 2025-01-31) | 0 | USD k | SEC XBRL companyfacts CIK0000798081, us-gaap:EquityMethodInvestments, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Treasury shares | FY2022 (FYE 2022-01-31) | 940 | k shares | SEC XBRL companyfacts CIK0000798081, us-gaap:TreasuryStockCommonShares, as filed in 10-K accn 0001654954-23-004860 (filed 2023-04-18) |
| Treasury shares | FY2023 (FYE 2023-01-31) | 1331 | k shares | SEC XBRL companyfacts CIK0000798081, us-gaap:TreasuryStockCommonShares, as filed in 10-K accn 0001654954-24-004465 (filed 2024-04-11) |
| Treasury shares | FY2024 (FYE 2024-01-31) | 1358 | k shares | SEC XBRL companyfacts CIK0000798081, us-gaap:TreasuryStockCommonShares, as filed in 10-K accn 0001654954-25-004352 (filed 2025-04-17) |
| Treasury shares | FY2025 (FYE 2025-01-31) | 1358 | k shares | SEC XBRL companyfacts CIK0000798081, us-gaap:TreasuryStockCommonShares, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |
| Treasury shares | FY2026 (FYE 2026-01-31) | 1358 | k shares | SEC XBRL companyfacts CIK0000798081, us-gaap:TreasuryStockCommonShares, as filed in 10-K accn 0001193125-26-159176 (filed 2026-04-16) |

Notes on the table:
- `Cash & equivalents (incl. restricted where tagged)`: FY2025 17,476 and FY2026 12,515 USD k are tagged cash + restricted cash; the restricted part (if any) must be split out from the balance sheet / Note 1 at resume (restricted cash is never cash, Gate 2).
- Accrued-expense tags change in FY2023 (`AccruedLiabilitiesCurrent` to FY2022, `OtherAccruedLiabilitiesCurrent` from FY2022): the NIBCL build is re-read from each face balance sheet at resume.
- Debt: `LongTermDebt` FY2026 30,382 and FY2025 16,426 USD k (incl. current 1,891 / 939); FY2025 `LineOfCredit` 46,200 is a facility amount, not a drawing — confirm from Note (Long-term debt / credit facility).
- Revenue FY2023 also shows a 6,000 / FY2024 6,300 Revenues fact ending April (quarter or segment fact) — ignore; the annual figures are those ending 31 January.

### Past readings already visible (arithmetic on the cited figures, not a grade)

- OI (face, as filed): FY2025 −9,265 and FY2026 −15,512 USD k, operating losses in both latest years; window Σ OI FY2017–FY2026 = 71,410 USD k (derived), of which FY2021 (COVID demand) 43,853.
- CFO negative in FY2023 (−5,451), FY2025 (−15,881) and FY2026 (−15,750) USD k.
- Diluted shares rose from 7,426k (FY2025) to 9,626k (FY2026): equity issued in FY2026 (financing, to be read from the equity statement).
- J1 OI candidates still to be logged: face OI (above) includes the goodwill impairments (FY2025 10,538; FY2026 2,604 USD k) per the segment footnote; the FY2025 Bodytrak impairment 7,639 USD k sits below OI (to confirm from the face statement).

### G6 / P31 (work done)

- Class: equity-method investment and convertible notes in Inova Design Solutions Ltd (Bodytrak), unlisted (10-K FY2026 Note 4 "Investments"; MD&A p. 34). Carrying value 4,719 USD k at FY2024 (3.1% of total assets 153,745); impaired in full at FY2025 (7,639 USD k, equity method plus convertible debt) after Bodytrak entered UK insolvency in February 2025; cumulative equity losses 1.5 USD m to 2025-01-31.
- P31 income limb: FY2025 exclude-reading OI is ≤ 0 and the class's loss is non-nil, so the limb **fails** and both G6 readings are owed for Gate 1A (include reading keeps the equity-method loss and the impairment loss in OI where booked below the line). Per-year carrying values and equity results FY2017–FY2026 (investment start year) are owed.

### Gate 1C (work done)

- Repurchases (cash, `PaymentsForRepurchaseOfEquity`): FY2019 1,165; FY2020 506; FY2022 9,183; FY2023 5,439; FY2024 333 USD k; none tagged FY2025–FY2026. Treasury shares 1,358k from FY2024. Worth table owed (point-in-time reads per tranche-year, per-year 1% floor).
- Dividends paid: FY2024 908; FY2025 887; FY2026 1,152 USD k.
- Acquisitions (cash net of cash acquired): FY2024 5,452 (Eagle Technical Products, Australia/NZ — to confirm); FY2025 45,084 (Jolly Scarpe, Italy; LHD Group, Germany, 16.3 USD m on 2024-07-01; Veridian Ltd, US, 26.3 USD m on 2024-12-16 — per auditor CAM, 10-K FY2026 p. 61); FY2026 6,165 (California PPE Recon 5.8 USD m on 2025-09-15; Arizona PPE). Goodwill impairment FY2025 10,538 USD k; FY2026 2,604 USD k (≈45% of LHD reporting-unit goodwill, Europe segment, 10-K FY2026 Critical accounting estimates). Acquisition-related costs 3.2 / 2.0 USD m FY2026 / FY2025 (Note 6). Pro forma table (Note 6) exists for the acquisition-stop proxy.
- Acquisition stop and write-down limb are live for the trailing three FYs (deals above 1% of EV; LHD write-down ≈45% of its goodwill within the window, CEO/CFO in office to check).
- Pay table, director fees, alignment: DEF 14A 2026 fetched (accn 0000798081-26-000008), not yet read.

### Gate 2 (work done)

- px 8.98 USD (2026-11-06). Latest-FY OI and maintenance FCF are both ≤ 0 on the figures above, so the primaries are expected n.m. and the band n.m. with a restoring OI level; the Q2 FY2027 balance sheet (accn 0001193125-26-386590) is the EV source and has not been extracted.

## 3. Readings settled

- Key LAKE, `px_unit` USD, exchange NasdaqGM.
- B1 record years: FY2017–FY2026 window, FY2016 opening balance sheet; full 10-year record expected (XBRL facts exist for every year).
- Group: seven reportable geographic segments; Asia merges into its main internal customer (71% intersegment). Material units and the merge target not yet fixed.
- G6: the Bodytrak class fails the P31 income limb in FY2025 (exclude-reading OI ≤ 0), so both readings are owed.
- Nothing else is settled: no P20 build, no P17 table, no worth table, no weights or S.

## 4. Scope still owed

- [ ] Re-take px and splits; confirm ISIN from a primary document.
- [ ] Tier-2 tie-out of the XBRL series (FY2026 and one earlier year: revenue, OI, equity, net cash composite) against the 10-K face statements; rebuild any year that breaks.
- [ ] B1: NIBCL per year from the face balance sheets (AP, accrued expenses, accrued compensation, income taxes payable, deferred revenue), restricted cash split, debt and lease liabilities per year; pre-ASC 842 years FY2017–FY2019 P18 test (lease commitments vs 10% of total assets).
- [ ] P20 per year: k from net PP&E (ROU excluded) / revenue; π_t = max(3%, US CPI-U for the calendar year matching the fiscal year, BLS); organic or acquired revenue for the deal years FY2024–FY2026 (Note 6 acquiree revenue since acquisition) — else all capex for those years.
- [ ] J1 OI log and financial-income removals (interest income, FX, Bodytrak equity results and impairment placement) from each face statement.
- [ ] G6: per-year Bodytrak carrying value and equity results; both readings in B2/B3.
- [ ] Group build: FY2024–FY2026 segment table (FY2025 10-K accn 0001654954-25-004352 for FY2024); segment assets for Asia, Canada, Latin America, Other foreign (Note 14 p. 70, the page break cut the extraction); P22 materiality on all three limbs; Asia's merge target; P29 weights (revenue weights if any material base ≤ 0) and S; one Appendix D block per material unit, with the group customer statement read for each unit; allocation-across-the-parts table on segment result ÷ segment assets.
- [ ] Gate 1B breadth: 10-K Item 1 customer statement (any customer > 10%; distributor channel), supplier statement (fabric suppliers, e.g. DuPont Tyvek/Nomex as specified inputs).
- [ ] Gate 1C: DEF 14A 2026 and 2025 (accn 0001654954-25-005043) Summary Compensation Tables and PvP tables (three years), director fees, ownership table (GVIC 13D 8.38%); RPTs; worth table for FY2019, FY2020, FY2022–FY2024 tranches (point-in-time trailing-3 reads); acquisition stop for Eagle, Jolly, LHD, Veridian, Arizona, California (pre-deal OI or Note 6 proxy grossed up per v4.8.0); LHD write-down limb.
- [ ] Gate 2: Q2 FY2027 balance sheet (debt, leases, cash, restricted cash); TTM OI and FCF; averaged readings; P28 test (latest FY below both averages; expect the impairment/restructuring path, needing operating evidence); restoring OI level for an n.m. band.
- [ ] Memo, row (`row-from-memo --table`), `lint-memo`, `lint-row`; delete this record when the memo lands.
