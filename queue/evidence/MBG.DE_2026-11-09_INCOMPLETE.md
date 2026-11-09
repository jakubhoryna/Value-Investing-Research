# MBG.DE — Mercedes-Benz Group AG — INCOMPLETE evidence, resumable record (ANALYSE 2026-11-09)

## 1. Header

- Key: MBG.DE · job: ANALYSE · D 2026-11-09 · T 2332 · base sha 75950dfb6679cd5c7a745710ad3db6af194630fb
- Live `model_version`: v4.8.0
- Prior memo: none (no `memos/MBG.DE/` or `archive/memos/MBG.DE/` at base; no register row matches "Mercedes-Benz" or "Daimler"; ISIN DE0007100000 matches no memo front matter — re-checked at this base).
- Named gap: **group build exceeds budget** (README §5; MODEL §8.7 item 6). This is the **second overrun**: this run took the DRAFT_QUEUE line carrying ` — partial 2026-11-06 (queue/evidence/MBG.DE_2026-11-06_INCOMPLETE.md)`.
- resumes: queue/evidence/MBG.DE_2026-11-06_INCOMPLETE.md (every figure in that record's item table stands as cited there and is not repeated below; both records stay until the key's memo lands).
- No verdict, grade or band is stated here. Each "derived" figure is arithmetic on the cited figures, labelled; it is not a grade.

## 2. Per gate or leg — work done and figures added this run

### Key and price (uncounted endpoint)

- `query1.finance.yahoo.com/v8/finance/chart/MBG.DE` (range 1mo, `events=split`): `currency` EUR, `exchangeName` GER, `longName` "Mercedes-Benz Group AG". Close 2026-11-09 = 41.86 EUR (2026-11-06 = 41.555). No split events in the range.

### Document route (re-tested)

- EQS store as in the first record. `…/Quarterly%20Reports/DE0007100000-Q3-2026-EQ-E-{00..03}.pdf` still 404 at 2026-11-09 (Q3 2026 interim owed; another file name or the issuer host, which 403s, holds it).
- AR2025, AR2024, AR2023 and AR2021 re-retrieved (`…/Annual%20Reports/DE0007100000-JA-{YYYY}-EQ-E-00.pdf`). "p." is the PDF page index (pdftotext), not the printed folio.

### Group, segments and weights (B4 inputs)

AR2025 Note 33 (pp. 363–367) names three reportable segments: Mercedes-Benz Cars, Mercedes-Benz Vans and Mercedes-Benz Financial Services (called Mercedes-Benz Mobility in AR2023–AR2024). Segment EBIT includes each segment's equity-method result and other financial income; segment assets include equity-method carrying values. Intra-group refinancing of the financial-services business is shown under Cars (earnings €445m FY2025, €398m FY2024; AR2025 p. 365).

| item | FY | value | unit | source |
|---|---|---|---|---|
| Cars total revenue / EBIT / segment assets | FY2025 | 96,407 / 3,564 / 89,641 | EUR m | AR2025 p. 366, segment information |
| Vans total revenue / EBIT / segment assets | FY2025 | 17,148 / 1,309 / 12,532 | EUR m | AR2025 p. 366 |
| Financial Services total revenue / EBIT / segment assets | FY2025 | 24,625 / 690 / 138,381 | EUR m | AR2025 p. 366 |
| Cars / Vans / FS equity-method result in segment EBIT | FY2025 | 715 / 52 / 25 | EUR m | AR2025 p. 366 |
| Reconciliation equity-method result (Daimler Truck €353m incl.) | FY2025 / FY2024 | 326 / 686 | EUR m | AR2025 p. 367 |
| Equity-method carrying value: Daimler Truck (incl. held-for-sale shares) / BAIC Motor | FY2025 | 8,221 / 173 | EUR m | AR2025 p. 367, reconciliation of segment assets (fn 1, 2) |
| Equity-method carrying value: Daimler Truck / BAIC Motor | FY2024 | 8,655 / 227 | EUR m | AR2025 p. 367 |
| Cars total revenue / EBIT / segment assets | FY2024 | 107,761 / 8,460 / 92,365 | EUR m | AR2025 p. 366 (= AR2024 p. 407) |
| Vans total revenue / EBIT / segment assets | FY2024 | 19,320 / 2,932 / 11,410 | EUR m | AR2025 p. 366 |
| FS (Mobility) total revenue / EBIT / segment assets | FY2024 | 25,083 / 1,134 / 149,251 | EUR m | AR2025 p. 366 |
| Cars total revenue / EBIT / segment assets | FY2023 (adjusted) | 112,756 / 14,224 / 93,435 | EUR m | AR2024 p. 407, segment information |
| Vans total revenue / EBIT / segment assets | FY2023 (adjusted) | 20,288 / 3,138 / 10,486 | EUR m | AR2024 p. 407 |
| Mobility total revenue / EBIT / segment assets | FY2023 (adjusted, IAS 8 correction) | 25,571 / 1,302 / 145,057 | EUR m | AR2024 p. 407 (AR2023 p. 312 printed Mobility revenue 26,718) |
| Cars / Vans / Mobility EBIT | FY2022 | 16,340 / 1,897 / 2,428 | EUR m | AR2023 p. 312, segment information |
| Cars / Vans / Mobility segment assets | FY2022 | 91,908 / 10,036 / 142,524 | EUR m | AR2023 p. 312 |
| Segment assets: Cars & Vans (combined segment) / Mobility | FY2021 | 95,758 / 146,196 | EUR m | AR2021 p. 307 (old segmentation: Cars and Vans one segment) |
| Revenue by region: Europe / N. America / Asia (China) / other | FY2025 | 57,908 / 34,552 / 31,571 (16,519) / 8,183 | EUR m | AR2025 p. 368 |
| Net assets: Cars / Vans / FS (equity) | FY2025 avg | 39,404 / 1,454 / 13,002 | EUR m | AR2025 p. 369, Note 34 |

Derived, indicative only:
- P29 weight base (latest-3-FY average segment EBIT as filed, FY2023–FY2025; no J1 charge allocation found in the note, logged): Cars (14,224 + 8,460 + 3,564) ÷ 3 = 8,749; Vans (3,138 + 2,932 + 1,309) ÷ 3 = 2,460; FS (1,302 + 1,134 + 690) ÷ 3 = 1,042. Weights ≈ Cars 71.4%, Vans 20.1%, FS 8.5% (derived). All three bases positive.
- P22: each segment is material on revenue or segment assets (FS 57.5% of FY2025 segment assets).
- Allocation across the parts, pooled FY2023–FY2025 (Σ EBIT ÷ Σ year-end segment assets, filer's measures, equity-method in both): Cars 26,248 ÷ 275,441 = 9.5%; Vans 7,379 ÷ 34,428 = 21.4%; FS 3,126 ÷ 432,689 = 0.7% (derived). Line 10% (pre-tax segment EBIT).
- Segment-asset change FY2022 → FY2025: Cars −2,267; Vans +2,496; FS −4,143 (derived). The window's opening year on the current three-segment split is FY2022 at the earliest found (AR2021 reports Cars & Vans as one segment); whether AR2022 restates FY2021 on three segments is owed (AR2022 PDF 404 on the EQS store).

### Mobility funding (P15 funding test for the captive arm)

| item | FY | value | unit | source |
|---|---|---|---|---|
| Notes/bonds and liabilities from ABS transactions | FY2025 / FY2024 | 71,039 / 81,085 | EUR m | AR2025 p. 64, refinancing instruments table |
| Liabilities to financial institutions | FY2025 / FY2024 | 24,427 / 26,315 | EUR m | AR2025 p. 64 |
| Deposits in the direct banking business | FY2025 / FY2024 | 1,562 / 1,557 | EUR m | AR2025 p. 64 |
| Notes/bonds+ABS / financial institutions / deposits | FY2023 / FY2022 | 71,185 / 25,317 / 5,759 · 70,984 / 24,738 / 10,538 | EUR m | AR2023 p. 64 |
| Total financing liabilities | FY2025 / FY2024 | 100.0 / 112.8 | EUR bn | AR2025 p. 64 text |
| ABS issued / repaid in year | FY2025 | 10.2 / 10.7 | EUR bn | AR2025 p. 64 text |
| Syndicated credit line, undrawn | 31 Dec 2025 | 11.0 | EUR bn | AR2025 p. 64 text |

Derived, indicative only: the capital-market channel (bonds, notes, ABS, CP and bank loans are one channel under P15) holds (71,039 + 24,427) ÷ 97,028 = 98.4% of the refinancing instruments and 95,466 ÷ 161,226 (total liabilities, first record) = 59.2% of liabilities at FY2025. The resume must still read the deposit split (insured retail vs corporate or above-limit) and the largest single counterparty, then call `funding conc.` on P15 for the FS unit.

### Breadth (P15) — what was searched

- AR2025 full text searched for a major-customer statement ("major customer", "single customer", "individual customer", "no customer", "10% of revenue"): none found in the segment note (AR2025 pp. 363–368) or elsewhere; the only "10% of total revenue" hit (p. 173) is EU-Taxonomy sector materiality, not a customer statement. Silence for the vehicle units, whose payers include independent dealers and importers (organisations), stays to be read under P15 (silence = concentration for a business selling to organisations ≥ 10% of revenue). The share of revenue paid by dealers/importers vs own retail and fleet buyers is owed.

### Cash flow and SF items

| item | FY | value | unit | source |
|---|---|---|---|---|
| Cash provided by operating activities (group incl. Daimler Truck until spin) | FY2021 / FY2020 | 24,549 / 22,332 | EUR m | AR2021 p. 191, consolidated statement of cash flows |
| Additions to PP&E / to intangible assets | FY2021 | -4,579 / -2,741 | EUR m | AR2021 p. 191 |
| Additions to PP&E / to intangible assets | FY2020 | -5,741 / -2,819 | EUR m | AR2021 p. 191 |
| Dividend paid to shareholders | FY2021 / FY2020 | -1,444 / -963 | EUR m | AR2021 p. 191 |
| Acquisition of treasury shares | FY2021 / FY2020 | -48 / -30 | EUR m | AR2021 p. 191 |
| Acquisition of treasury shares | FY2023 / FY2022 | -1,941 / -48 | EUR m | AR2023 p. 58, condensed cash-flow table (group column) |
| Receivables from financial services, total | FY2021 / FY2020 | 80,625 / 96,185 | EUR m | AR2021 condensed balance sheet (pdftotext line 3755; page owed) |

Note: AR2021's cash-flow statement includes Daimler Truck (discontinued) for both years; the continuing-operations split (AR2021 p. ≈ 236, cash-flow line "Cash provided by operating activities 987 / 23,562 / 24,549" by segment) needs reading before B1 takes FY2020–FY2021.

## 3. Readings settled (as far as the run got)

- **Gate 0 (provisional, as in the first record):** describable in one sentence; three material units (Cars, Vans, Financial Services). No P30 ground.
- **Lens:** STD; FS is a captive finance arm by the filer's description ("supports the sales of the Mercedes-Benz Group's automotive brands worldwide", AR2025 p. 364; leasing and financing for end customers and dealers, insurance services, subscriptions, fleet management). The book split (> half unrelated to group products?) is not shown; on the description rule it is captive. The insurance-services activity (broker or underwriter, and any float) is owed: a captive insurance float would be a G6 class.
- **Listed parts:** Daimler Truck Holding AG (equity-accounted, ≈ 4.5% of MCap at 31 Dec 2025, first record) and BAIC Motor (equity-method carrying €173m) are below the P22 10%-of-MCap line → no material listed holding, no dependency, `holding_keys` n.m., `core_credit` 0 (to confirm on the stake counts). Both are G6 associates in Gate 1A.
- **G6 / P31:** above the line (first record). Classes: BBAC and other associates/JVs in the segments, Daimler Truck and BAIC in the reconciliation; the S3 strategic stakes owed.
- **Group weights and allocation:** above (derived; the window opening year is owed).

## 4. Scope still owed (in order) — for the attended group build

- [ ] Q3 2026 interim (EQS file name, or the issuer's press release mirror) for the latest balance sheet, share count and TTM.
- [ ] B1 FY2016–FY2025 + the 31 Dec 2015 balance sheet: CFO, capex, D&A, diluted shares, NIBCL, cash + marketable debt securities, total liabilities, equity attributable, goodwill + intangibles per year (AR2016–AR2025; AR2022 is 404 on the EQS store, read FY2022 from AR2023 and FY2021 restated from AR2022 if another route serves it). FY2016–FY2020 carry Daimler Trucks & Buses.
- [ ] R2/P20 per year: the FS receivables and operating-lease vehicle changes in CFO (±3% rule), operating-lease additions out of net fixed capital; constructed maintenance capex (k; euro-area HICP deflators; the D&A floor).
- [ ] G6 per year: equity-method carrying values, results and dividends received; both readings in B2/B3; the P31 log.
- [ ] Funding test for FS: deposit split, largest counterparty; funding pairing for Gate 2 and P19.
- [ ] Breadth: dealer/importer share of revenue; any customer statement in the AR2024/AR2023 notes or investor materials; Appendix D blocks for Cars, Vans, FS.
- [ ] Appendix E: remuneration reports 2023–2025 (§162 AktG; separate PDFs on the EQS store or group site), Supervisory Board fees, Board holdings; worth table for the FY2022–FY2025 tranches at the point of purchase (cash per year above; share counts from the treasury-share notes); acquisition stop (no deal > 1% of EV identified yet; Athlon is a disposal); allocation-across-the-parts window from the first year on the three-segment split.
- [ ] Gate 2: core numbers on the latest balance sheet, debt-equivalents incl. FS funding, P28 test (FY2025 below both averages: workforce-programme and tariff causes to quantify), averaged readings, trigger band.
