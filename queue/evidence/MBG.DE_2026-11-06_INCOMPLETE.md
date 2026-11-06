# MBG.DE — Mercedes-Benz Group AG — INCOMPLETE evidence, resumable record (ANALYSE 2026-11-06)

## 1. Header

- Key: MBG.DE · job: ANALYSE · D 2026-11-06 · T 1903 · base sha 610ee90d44a57f8582d4fd00b30fcf062383f8c1
- Live `model_version`: v4.8.0
- Prior memo: none. No `memos/MBG.DE/` or `archive/memos/MBG.DE/` folder exists, and no register row matches "Mercedes-Benz" or "Daimler" (name check on `register.csv` at base). ISIN DE0007100000 matches no memo front matter in `memos/` or `archive/memos/`. LEI 529900R27DL06UVNT076 (GLEIF API, legal name "Mercedes-Benz Group AG").
- Named gap: **group build exceeds budget** (README §5; MODEL §8.7 item 6). This is the **first overrun**: the queue line carries no ` — partial …` note at base.
- No verdict, grade or band is stated here. Each "derived" figure below is arithmetic on the cited figures. It is not a grade.

## 2. Per gate or leg — work done and figures

### Key and price (uncounted endpoint)

- `query1.finance.yahoo.com/v8/finance/chart/MBG.DE`: `currency` EUR, `exchangeName` GER (Xetra), instrument "Mercedes-Benz Group AG". Close 2026-11-06 = 41.555 EUR. No split events were returned for the 10-day range. A resume must re-take px and check splits since FY2016 (the register needs only the current px).

### Document route

The issuer host `group.mercedes-benz.com` returns HTTP 403 to every request (IR pages, report PDFs, robots.txt). WebFetch also gets 403. The bot block was not worked around. The issuer's EQS IR document store serves the reports. It redirects to `ir-api.eqs.com/media/document/…`:

- `https://irpages2.eqs.com/download/companies/daimlerchrysler/Annual%20Reports/DE0007100000-JA-{YYYY}-EQ-E-{nn}.pdf`
  - `nn` = 00 for 2018, 2020, 2021, 2023, 2024 and 2025
  - `nn` = 01 for 2016 and 2017
  - `nn` = 03 for 2019
  - 2022 returned 404 for 00–03; FY2022 is read from AR2023's comparatives
- `…/Quarterly%20Reports/DE0007100000-Q{n}-2026-EQ-E-00.pdf`: Q1 and Q2 2026 retrieved. Q3 2026 returned 404 for 00–03 (owed).

"p." below is the PDF page index (pdftotext page number), not the printed folio.

| item | FY | value | unit | source |
|---|---|---|---|---|
| Revenue | FY2025 | 132,214 | EUR m | AR2025 p. 252, consolidated statement of income |
| Revenue | FY2024 | 145,594 | EUR m | AR2025 p. 252, consolidated statement of income |
| Gains/losses on equity-method investments, net | FY2025 | 1,118 | EUR m | AR2025 p. 252 |
| Gains/losses on equity-method investments, net | FY2024 | 1,138 | EUR m | AR2025 p. 252 |
| Other financial income/expense, net | FY2025 | 93 | EUR m | AR2025 p. 252 |
| Other financial income/expense, net | FY2024 | -37 | EUR m | AR2025 p. 252 |
| EBIT (reported, includes the two lines above) | FY2025 | 5,820 | EUR m | AR2025 p. 252 |
| EBIT (reported) | FY2024 | 13,599 | EUR m | AR2025 p. 252 |
| Net profit attributable to shareholders | FY2025 | 5,141 | EUR m | AR2025 p. 252 |
| Net profit attributable to shareholders | FY2024 | 10,207 | EUR m | AR2025 p. 252 |
| Weighted average shares, basic = diluted | FY2025 | 962.4 | m | AR2025 p. 369, Note 35 |
| Weighted average shares, basic = diluted | FY2024 | 1,002.0 | m | AR2025 p. 369, Note 35 |
| Total assets | FY2025 | 255,466 | EUR m | AR2025 p. 254, consolidated statement of financial position |
| Total assets | FY2024 | 265,010 | EUR m | AR2025 p. 254 |
| Equity-method investments | FY2025 | 10,037 | EUR m | AR2025 p. 254 |
| Equity-method investments | FY2024 | 12,786 | EUR m | AR2025 p. 254 |
| Equipment on operating leases | FY2025 | 39,472 | EUR m | AR2025 p. 254 |
| Equipment on operating leases | FY2024 | 45,220 | EUR m | AR2025 p. 254 |
| Receivables from financial services, non-current + current | FY2025 | 41,902 + 34,387 | EUR m | AR2025 p. 254 |
| Receivables from financial services, non-current + current | FY2024 | 48,547 + 39,320 | EUR m | AR2025 p. 254 |
| Cash and cash equivalents | FY2025 | 12,254 | EUR m | AR2025 p. 254 |
| Cash and cash equivalents | FY2024 | 14,511 | EUR m | AR2025 p. 254 |
| Marketable debt securities, current + non-current | FY2025 | 6,940 + 626 | EUR m | AR2025 p. 254 |
| Marketable debt securities, current + non-current | FY2024 | 7,086 + 644 | EUR m | AR2025 p. 254 |
| Assets held for sale | FY2025 | 11,013 | EUR m | AR2025 p. 254 (Athlon companies and Daimler Truck shares: AR2025 combined management report, financial position text; Note 3) |
| Equity attributable to shareholders | FY2025 | 93,257 | EUR m | AR2025 p. 255 |
| Equity attributable to shareholders | FY2024 | 92,625 | EUR m | AR2025 p. 255 |
| Total equity (incl. NCI 983 / 1,005) | FY2025 / FY2024 | 94,240 / 93,630 | EUR m | AR2025 p. 255 |
| Provisions for pensions and similar obligations | FY2025 / FY2024 | 807 / 952 | EUR m | AR2025 p. 255 |
| Financing liabilities, non-current | FY2025 / FY2024 | 62,410 / 73,487 | EUR m | AR2025 p. 255 |
| Financing liabilities, current | FY2025 / FY2024 | 37,596 / 39,311 | EUR m | AR2025 p. 255 |
| Trade payables | FY2025 / FY2024 | 10,665 / 11,312 | EUR m | AR2025 p. 255 |
| Contract and refund liabilities, non-current + current | FY2025 | 2,942 + 7,955 | EUR m | AR2025 p. 255 |
| Contract and refund liabilities, non-current + current | FY2024 | 3,100 + 8,146 | EUR m | AR2025 p. 255 |
| Income tax liabilities, non-current + current | FY2025 | 1,020 + 646 | EUR m | AR2025 p. 255 |
| Liabilities held for sale | FY2025 / FY2024 | 1,340 / 46 | EUR m | AR2025 p. 255 |
| Cash flow from operating activities | FY2025 / FY2024 | 18,006 / 17,735 | EUR m | AR2025 p. 256, consolidated statement of cash flows |
| of which: change in receivables from financial services | FY2025 / FY2024 | +5,828 / +3,280 | EUR m | AR2025 p. 256 |
| of which: vehicles on operating leases | FY2025 / FY2024 | -4,060 / -3,110 | EUR m | AR2025 p. 256 |
| of which: dividends received from equity-method investments | FY2025 / FY2024 | 1,330 / 1,918 | EUR m | AR2025 p. 256 |
| Depreciation and amortisation/impairments | FY2025 / FY2024 | 7,223 / 6,772 | EUR m | AR2025 p. 256 |
| Acquisitions of property, plant and equipment | FY2025 / FY2024 | -5,482 / -4,039 | EUR m | AR2025 p. 256 |
| Acquisitions of intangible assets | FY2025 / FY2024 | -4,260 / -4,626 | EUR m | AR2025 p. 256 |
| Acquisition of treasury shares | FY2025 / FY2024 | -360 / -4,921 | EUR m | AR2025 p. 257 |
| Dividend paid to shareholders | FY2025 / FY2024 | -4,140 / -5,486 | EUR m | AR2025 p. 257 |
| Revenue / EBIT / equity-method result / other financial income | FY2023 | 153,218 / 19,660 / 2,129 / 108 | EUR m | AR2023 p. 195, consolidated statement of income |
| Revenue / EBIT / equity-method result / other financial income | FY2022 | 150,017 / 20,458 / 1,732 / 340 | EUR m | AR2023 p. 195 (2022 column) |
| Total assets | FY2023 / FY2022 | 263,022 / 260,015 | EUR m | AR2023 p. 197 |
| Cash flow from operating activities | FY2023 / FY2022 | 14,470 / 16,894 | EUR m | AR2023 p. 199 |
| Additions to PP&E / to intangible assets | FY2023 | -3,745 / -4,468 | EUR m | AR2023 p. 199 |
| Additions to PP&E / to intangible assets | FY2022 | -3,481 / -3,418 | EUR m | AR2023 p. 199 |
| Revenue / EBIT / other financial income | FY2021 | 133,893 / 16,028 / 317 | EUR m | AR2021 p. 187 (continuing operations; Daimler Truck spun off Dec 2021, discontinued) |
| Revenue / EBIT / other financial income | FY2020 restated | 121,778 / 6,091 / -323 | EUR m | AR2021 p. 187 (2020 column restated for discontinued operations) |
| Total assets | FY2021 / FY2020 | 259,831 / 285,737 | EUR m | AR2021 balance sheet (equity line on p. 190) |
| Equity attributable to shareholders | FY2021 / FY2020 | 71,951 / 60,691 | EUR m | AR2021 p. 190 |
| Revenue / total assets | FY2020 (as first reported, incl. trucks) | 154,309 / 285,737 | EUR m | AR2020 statements |
| Revenue / total assets | FY2019 | 172,745 / 302,438 | EUR m | AR2020 and AR2019 statements |
| Revenue / total assets | FY2018 | 167,362 / 281,619 | EUR m | AR2019 and AR2018 statements |
| Revenue (IFRS 15 restated) / total assets | FY2017 | 164,154 / 255,345 (AR2018); first reported 164,330 / 255,605 (AR2017) | EUR m | AR2018 and AR2017 statements |
| Revenue / total assets | FY2016 | 153,261 / 242,988 | EUR m | AR2017 and AR2016 statements |
| Revenue / total assets | FY2015 | 149,467 / 217,166 | EUR m | AR2016 statements |
| Total assets | 30 Jun 2026 | 259,716 | EUR m | Q2 2026 interim report p. 41, condensed statement of financial position |
| Cash and cash equivalents | 30 Jun 2026 | 10,142 | EUR m | Q2 2026 p. 41 |
| Equity-method investments | 30 Jun 2026 | 9,516 | EUR m | Q2 2026 p. 41 |
| Assets held for sale | 30 Jun 2026 | 11,163 | EUR m | Q2 2026 p. 41 |
| Financing liabilities (total) | 30 Jun 2026 / 31 Dec 2025 | 102,231 / 100,006 | EUR m | Q2 2026 p. 31, segment balance sheet table (Group column) |
| Daimler Truck Holding AG shares held for sale (fair value less costs to sell) | 30 Jun 2026 / 31 Dec 2025 | 1,242 / 1,784 | EUR m | Q2 2026 p. 47, notes (assets held for sale table) |
| Partial sale of Daimler Truck shares, cash inflow / gain | H1 2026 | 417 / 77 | EUR m | Q2 2026 p. 47, notes ("Sale of shares in the Daimler Truck Holding AG") |

Derived, indicative only, never a grade:
- J1 OI = EBIT − equity-method result − positive other financial income (J3; a net loss stays in): FY2025 5,820 − 1,118 − 93 = **4,609**; FY2024 13,599 − 1,138 = **12,461**; FY2023 19,660 − 2,129 − 108 = **17,423**; FY2022 20,458 − 1,732 − 340 = **18,386**. The interest income in EBIT on the Mobility book is operating-book revenue. Still to check: other financial income components and the pension net-interest placement (AR Note 7).
- L/E FY2025 = (255,466 − 94,240) ÷ 93,257 = 172.9%. The P31 G6 classes (BBAC and other associates, Daimler Truck while equity-accounted) and the leasing and FS books' treatment can still move this reading.
- Daimler Truck materiality (P22): €1,784m at 31 Dec 2025 ÷ MCap at px (41.555 × ≈962m shares ≈ €40.0bn, derived) ≈ 4.5% < 10%. So it is **not a material listed holding**. It is an equity-accounted associate, a G6 class in Gate 1A, with no credit at Gate 2. The resume must confirm the stake percentage and the share count at the latest balance-sheet date.

## 3. Readings settled (as far as the run got)

- **Gate 0 (provisional):** the business is describable in one sentence. Premium passenger cars (Mercedes-Benz Cars) and vans (Mercedes-Benz Vans) are sold to private and fleet buyers through own and independent retail. Mercedes-Benz Mobility is the captive finance, leasing and fleet arm. Group HQ is Stuttgart, with sales worldwide (China, the US and Germany largest). No P30 ground was found.
- **Lens:** STD. Not a bank or insurer group: the Mobility arm is a captive finance arm (R2) consolidated on STD. The captive test (> half of the book unrelated to group products) has not been run; it is owed.
- **Group:** three reportable segments (Cars, Vans, Mobility), each material on revenue or assets (AR2025 segment table: Cars revenue 96,407 / Vans 17,148 / Mobility 24,625 EUR m FY2025; segment total assets Industrial 117,085 / Mobility 138,381 EUR m — AR2025 combined management report, Group/Industrial/Mobility tables). No material listed holding at 31 Dec 2025 (Daimler Truck ≈ 4.5% of MCap, above). BAIC Motor (HK-listed, ~10% stake) has its materiality owed. The Beijing Benz (BBAC) JV is unlisted, equity-method, a G6 class.
- **P31:** above the line by inspection. The equity-method carrying value of €10–13bn is ≈ 4–5% of total assets, and the equity-method result of €1.1–2.3bn is ≥ 5% of J1 OI in FY2022–FY2025. So two G6 readings over the window are owed.
- **Perimeter:** FY2016–FY2020 are Daimler AG including trucks and buses. AR2021 restates FY2020 for discontinued operations. The window record therefore mixes perimeters, and B1 must use each year as reported in the latest available restatement (J13 on any choice).

## 4. Scope still owed (in order)

- [ ] Re-take px; collect the share count at the latest balance-sheet date (Q3 2026 interim if published: find its EQS path; else Q2 2026).
- [ ] B1 for FY2016–FY2025 plus the 31 Dec 2015 balance sheet (AR2016): revenue, J1 OI, CFO, PP&E + intangible additions, D&A, diluted shares, total assets, NIBCL, cash + marketable debt securities, total liabilities, equity attributable, goodwill + intangibles. Statement pages: AR2025 pp. 252–257; AR2024 pp. 292–295; AR2023 pp. 195–199; AR2021 pp. 187–192; AR2016–AR2020: locate the "Consolidated Statement of Income/Financial Position/Cash Flows" pages.
- [ ] R2/P20 book adjustments per year: the change in receivables from financial services and vehicles on operating leases in CFO (±3% rule); equipment-on-operating-lease additions out of net fixed capital; P20 constructed maintenance capex (k, π_t from Destatis or HICP, the floor at D&A of PP&E plus capitalised development).
- [ ] G6 classes per year (equity-method carrying value and result, dividends received in CFO); two readings in B2/B3; P31 log.
- [ ] Funding pairing for the Mobility financing liabilities (Gate 2 and P19).
- [ ] B4: segment revenue, EBIT and assets for Cars, Vans and Mobility, latest 3 FYs; weights; Appendix D per unit (breadth: group customer statement; forces; moat; market).
- [ ] Captive test for Mobility; BAIC Motor materiality; Daimler Truck stake %.
- [ ] Appendix E: remuneration reports 2023–2025 (§162 AktG; CEO Källenius), Supervisory Board fees, management holdings; worth table at the point of purchase for the 2022–2025 buyback tranches (€4.9bn in FY2024, €0.36bn in FY2025; FY2022/FY2023 from AR2023), each against trailing-3-FY published reads; acquisition stop (Athlon sale is a disposal); allocation across the parts (segment assets FY2021–FY2025 on the post-spin segmentation).
- [ ] Gate 2: core numbers, P28 test (FY2025 is below the 3y/5y averages: test the named causes), averaged readings, trigger band.
