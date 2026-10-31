# TITAN.NS — Titan Company Limited — INCOMPLETE evidence (ANALYSE 2026-10-31)

Evidence record (README §5, D3). No grade, no verdict. Figures in the item table carry their primary document and location, so a later run can carry them under README §5 Resume.

## 1. Header

- Key TITAN.NS · job ANALYSE · D 2026-10-31 · T 0727 · base sha daa5f4baee102011a732a7c89777a4e5414e5149 · model_version v4.8.0 · produced_by ROUTINE
- Prior memo: none. Name ("Titan Company") and ISIN grep over `memos/`, `archive/memos/`, `register.csv` and `_REGISTER.md`: no match. Prior memo `model_version`: none.
- ISIN: INE280A01028 (AR20, shareholder information).
- **Named gap: data access: FY2021–FY2026 annual reports.** The annual reports for FY2020-21 through FY2025-26 exist (the FY2025-26 report is the 42nd Annual Report, filed with the exchanges in July 2026) but could not be retrieved this run:
  - `www.titancompany.in` (company IR site, every path including `/robots.txt` and `/sites/default/files/2026-07/Titan%20AR%202026.pdf`): HTTP 406 "Request was blocked due to suspicious behavior" (AppTrana WAF). Not circumvented.
  - `nsearchives.nseindia.com` (NSE archive, e.g. `annual_reports/AR_24142_TITAN_2023_2024_18062024113823.pdf` and the Q4 FY2026 iXBRL integrated filing `corporate/ixbrl/INTEGRATED_FILING_INDAS_156398_08052026194742_iXBRL_WEB.html`): connection closed by the server (HTTP/2 INTERNAL_ERROR; HTTP/1.1 empty reply). The proxy recorded no relay failure, so the host refused the client. Not circumvented.
  - `www.bseindia.com/bseplus/AnnualReport/500114/50011403{YY}.pdf` serves FY2016–FY2020 only (FY2021 path: 404). Later BSE copies sit under `xml-data/corpfiling/AttachHis/{uuid}.pdf`, whose ids for the annual reports were not found in two searches. The ids found were a 4 May 2024 results letter (scanned, no text layer), the 18 Jun 2024 BRSR (53 pages, not the annual report) and two other letters.
  - Price endpoint `query1.finance.yahoo.com/v8/finance/chart/TITAN.NS`: HTTP 429 (Too Many Requests) on four tries between 06:28 and 06:40 UTC. Not retried with altered headers.
- Consequence: the FY2021–FY2026 statements (B1–B3 for six of the ten window years and five of the eleven balance sheets), the FY2024–FY2026 pay tables (P17), the repurchase and acquisition record (P19), the current segment note (group weights, allocation test) and the price all sit in documents not retrieved. Every gate except Gate 0 needs them.
- Resumes: none (first record of this key).

## 2. Documents retrieved (primary, 2026-10-31)

| id | document | URL |
|---|---|---|
| AR16 | Annual Report 2015-16 (184 pp.) | bseindia.com/bseplus/AnnualReport/500114/5001140316.pdf |
| AR17 | Annual Report 2016-17 (first Ind AS year, FY2016 comparatives) | bseindia.com/bseplus/AnnualReport/500114/5001140317.pdf |
| AR18 | Annual Report 2017-18 | bseindia.com/bseplus/AnnualReport/500114/5001140318.pdf |
| AR19 | Annual Report 2018-19 | bseindia.com/bseplus/AnnualReport/500114/5001140319.pdf |
| AR20 | Annual Report 2019-20 | bseindia.com/bseplus/AnnualReport/500114/5001140320.pdf |
| BRSR24 | BRSR FY2023-24, filed 18 Jun 2024 (not the annual report) | bseindia.com/xml-data/corpfiling/AttachHis/51c89546-c90c-45c2-8ff3-e5b034e00832.pdf |
| R24 | Results filing, 4 May 2024 (scanned; no text extracted) | bseindia.com/xml-data/corpfiling/AttachHis/95468b87-4b59-461d-861a-9f3b30dbd80e.pdf |

AR16–AR20 were extracted with `pdftotext -layout` and are text-searchable. AR18 and AR19 were not yet read.

## 3. Gate 0 and the group reading (work done)

- **Group.** Titan reports four segments: Watches & Wearables, Jewellery, Eyewear and Others (Accessories, Fragrances, Indian dress wear), plus Corporate (unallocated) (AR20, standalone note 27(a)). At FY2020 two units are material under P22: Jewellery and Watches (Watches 15.1% of Σ positive segment results and 19.3% of reportable segment assets, consolidated and standalone respectively, derived below). Eyewear and Others are under 10% on all three measures at FY2020. A group build (B4 weights and S, an Appendix D block per material unit, the allocation-across-the-parts table) is therefore owed, on the latest segmentation (FY2026 segment note, not retrieved; the filer has since added units such as CaratLane and international businesses, to be checked).
- **Listed parts.** No controlled listed subsidiary or listed holding found in AR20; to re-check in AR21–AR26 (CaratLane and any later acquisitions: listing status not yet verified from a primary).
- **Lens.** STD expected: a jewellery, watch and eyewear retailer and maker with no banking or insurance licence. The gold-on-loan liability (below) is a debt-equivalent, not a funding book.
- **Draft Gate-0 sentence (not settled):** Titan, a Tata-group company founded in 1984 in Bengaluru, makes and retails branded gold and diamond jewellery (Tanishq and other brands), watches and wearables, eyewear and smaller lines, selling mainly to Indian consumers through its own and franchised stores, multi-brand dealers and online.

## 4. Item table (INR; consolidated unless stated; FY ends 31 March)

| item | FY | value | unit | source |
|---|---|---|---|---|
| Segment revenue — Watches / Jewellery / Eyewear / Others / Corporate | FY2020 | 2,615.49 / 16,738.22 / 544.01 / 171.11 / 87.22 | INR crore | AR20, consolidated segment results table ("Segment Revenue … Year Ended 31st March 2020 (Audited)", text line ~6301) |
| Segment revenue — same order | FY2019 | 2,440.93 / 16,029.58 / 511.41 / 133.43 / 133.12 | INR crore | AR20, same table, comparative |
| Segment results (before finance costs and taxes, after share of associate) — Watches / Jewellery / Eyewear / Others | FY2020 | 365.31 / 2,061.32 / (14.33) / (58.41) | INR crore | AR20, same table |
| Segment results — same order | FY2019 | 316.38 / 1,948.00 / (2.38) / (58.11) | INR crore | AR20, same table |
| Corporate (unallocated) result; finance costs; PBT | FY2020 | (99.44); 149.48; 2,104.97 | INR crore | AR20, same table |
| Segment assets (standalone) — Watches / Jewellery / Eyewear / Others / Corporate | FY2020 | 214,345 / 822,448 / 49,517 / 21,737 / 210,748 | INR lakh | AR20, standalone note 27(d), p. 188 |
| Segment assets (standalone) — same order | FY2019 | 150,204 / 674,225 / 39,447 / 10,656 / 272,450 | INR lakh | AR20, standalone note 27(d), p. 188 |
| Total assets | FY2020 / FY2019 | 1,354,979 / 1,171,525 | INR lakh | AR20, consolidated balance sheet |
| Gold on loan (current financial liability, note 16.2) | FY2020 / FY2019 | 158,455 / 235,290 | INR lakh | AR20, consolidated balance sheet |
| Borrowings, current (note 16.1) | FY2020 / FY2019 | 70,590 / 8 | INR lakh | AR20, consolidated balance sheet |
| Borrowings, non-current (note 14.1; FY2020 = lease liabilities era, to confirm) | FY2020 / FY2019 | 1,697 / 3,167 | INR lakh | AR20, consolidated balance sheet |

Derived (P22 test, FY2020): Watches share of Σ positive segment results = 365.31 ÷ (365.31 + 2,061.32) = 15.1% (consolidated); Watches share of reportable segment assets = 214,345 ÷ 1,108,047 = 19.3% (standalone; derived: AR20 note 27(d)). Revenue share 13.0%.

## 5. Readings settled

- Group: yes (two material units at FY2020; latest segmentation to confirm). Lens: STD (expected, not logged in Appendix C form).
- Gold on loan: a borrowing of gold to fund jewellery inventory; a Gate 2 debt-equivalent and in L/E. Its scale (INR 1,585–2,353 crore at FY2019–FY2020) makes L/E a live P5 question for the window.
- Nothing else settled: no B1 year, P20 build, P17 table or worth table.

## 6. Scope still owed

- [ ] Retrieve the annual reports FY2020-21 to FY2025-26: find the BSE `AttachHis` ids (BSE announcements for scrip 500114, "Integrated Annual Report under Regulation 34(1)", late June or July each year), or an attended session supplies them (titancompany.in and NSE refuse the routine client).
- [ ] Retrieve the H1 FY2027 results (BS at 30 Sep 2026) for Gate 2 EV inputs and TTM.
- [ ] Price: one GET to the price endpoint (exchangeName, currency, instrument name, close, splits).
- [ ] B1 FY2017–FY2026 and BS FY2016–FY2026 from AR17–AR26 (consolidated), with the P20 build (India CPI deflator, k), the J1 OI build (exceptional items, other income out), gold on loan and lease liabilities in CE, EV and L/E.
- [ ] G6 / P31: associates or JVs and S3 stakes (check AR20–AR26 notes).
- [ ] B4 and S on the latest segmentation; Appendix D blocks for each material unit (Jewellery, Watches & Wearables, and any other unit at 10%); group customer statement.
- [ ] Gate 1C: FY2024–FY2026 managerial remuneration (Annexure to the Board's report and the MGT-7 extract), outside-director commission, Tata Sons and TIDCO as controllers (alignment, RPTs incl. Tata brand royalty), repurchases (none known), acquisitions in FY2024–FY2027 on the acquisition stop (deals to be listed from the primaries); allocation across the parts.
- [ ] Gate 2: core numbers, trigger band, averaged readings.
