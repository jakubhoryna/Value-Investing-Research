# BAJAJ-AUTO.NS — INCOMPLETE evidence (resumable record, first overrun)

## 1. Header

| Field | Value |
|---|---|
| Key | BAJAJ-AUTO.NS (Bajaj Auto Limited; NSE `BAJAJ-AUTO`, BSE 532977) |
| ISIN | INE917I01010 (AR26 PDF p. 135, shareholder information, "ISIN for depositories (NSDL and CDSL)") |
| Job | ANALYSE (routine) |
| D · T | 2026-11-03 · 2332 (Europe/Prague) |
| Base sha | 5152758b24e0006f02d019bcd78713f2939ebe5d |
| Live model_version | v4.8.0 |
| Prior memo | none. No `memos/BAJAJ-AUTO.NS/` or `archive/memos/BAJAJ-AUTO.NS/`; no register row, memo `company:` or `isin:` matches "Bajaj", "Pierer", "KTM", INE917I01010 or AT0000KTMI02 (one grep over `memos/`, `archive/memos/`, `register.csv`) |
| Named gap | `INCOMPLETE (group build exceeds budget)` — **first overrun** (the DRAFT_QUEUE line carried no ` — partial …`) |
| Resumes | none |

**Why it overran.** Bajaj Auto is a group under MODEL §2 Group Gate 0 with three material parts at FYE 31 Mar 2026: the Automotive segment ex-KTM, the Financing segment (Bajaj Auto Credit Ltd, a captive arm under R2 pending the captive test), and the controlled listed subsidiary Bajaj Mobility AG (formerly PIERER Mobility AG; KTM group), consolidated from 18 Nov 2025. Bajaj Mobility has no memo, so it is ungradeable (G4). On top of that, G6 sits above the P31 line: the PBAG associate's carrying value is 9–12% of total assets FY2016–FY2024 and its income is above 5% of exclude-reading OI in most years. So B1–B3 need both readings over the ten-year window. They also need the P20 constructed build for ten years, the R6 book rule for the Financing unit (FY2024–FY2026), three Appendix D blocks with the R7 worksheet, B4 weights, the allocation-across-the-parts table, two point-in-time buyback worth tables (FY2023 open market, FY2024 tender) and the KTM acquisition stop, plus Gate 2 with Bajaj Mobility's NCI at market. That does not fit one routine run. This run retrieved all eleven annual reports and settled the figures and readings below.

Units: ₹ crore (₹10m), consolidated Ind AS, fiscal years ending 31 March (FY2026 = year to 31 Mar 2026), unless stated. PDF page = the file's page index. Figures were read from `pdftotext -layout` extractions of the PDFs; the resuming run re-opens each governing figure at the cited page (README §5 Resume).

## 2. Sources retrieved this run (primary; P14 exploratory operations: 2 web searches)

| Ref | Document | URL |
|---|---|---|
| AR26 | 19th Annual Report 2025-26 (FY2026 and FY2025; auditor S R B C & CO LLP, signed 6 May 2026) | investors.bajajauto.com/ar26/wp-content/uploads/2026/06/Bajaj-Auto-Annual-Report-2025-26-1.pdf |
| AR25 | Annual Report 2024-25 | investors.bajajauto.com/ar25/wp-content/uploads/2025/07/BAL_Annual_Report_2025.pdf |
| AR24 | Annual Report 2023-24 | investors.bajajauto.com/ar24/wp-content/uploads/2024/06/BAL_Annual_Report_2024.pdf |
| AR23 | Annual Report 2022-23 | investors.bajajauto.com/ar23/wp-content/uploads/2023/06/BAL2023_Annual_Report_for_WEB.pdf |
| AR22 | Annual Report 2021-22 | investors.bajajauto.com/ar22/wp-content/uploads/2022/07/BAL_AR_2022_for-Web_IndiDesign.pdf |
| AR21 | Annual Report 2020-21 | investors.bajajauto.com/ar21/wp-content/uploads/2021/06/Bajaj-Auto-2021-for-web_Dummy.pdf |
| AR20 | Annual Report 2019-20 | bseindia.com/bseplus/AnnualReport/532977/5329770320.pdf |
| AR19 | Annual Report 2018-19 | bseindia.com/bseplus/AnnualReport/532977/5329770319.pdf |
| AR18 | Annual Report 2017-18 | bseindia.com/bseplus/AnnualReport/532977/5329770318.pdf |
| AR17 | Annual Report 2016-17 (first Ind AS year; FY2016 comparatives and the 1 Apr 2015 opening balance sheet) | bseindia.com/bseplus/AnnualReport/532977/5329770317.pdf |
| AR16 | Annual Report 2015-16 (Indian GAAP) | bseindia.com/bseplus/AnnualReport/532977/5329770316.pdf |
| PX | query1.finance.yahoo.com/v8/finance/chart/BAJAJ-AUTO.NS — currency INR, exchangeName NSI (NSE), longName "Bajaj Auto Limited", instrumentType EQUITY; regularMarketPrice 10,540.00 at 2026-11-03 09:59:38 UTC; daily closes 10,485.00 (2026-10-28), 10,383.00 (2026-10-29), 10,350.00 (2026-10-30), 10,339.00 (2026-11-02); no split in the 5-day range (`&events=split` returned none) |
| PX-BMAG | query1.finance.yahoo.com/v8/finance/chart/BMAG.SW — currency CHF, exchangeName EBS, longName "Bajaj Mobility AG", regularMarketPrice 29.75; BMAG.VI — currency EUR, exchangeName VIE, regularMarketPrice 32.60 (both at the 2026-11-03 session). PKTM.SW and PKTM.VI return HTTP 404 ("symbol may be delisted") |

Unretrievable: `api.bseindia.com` annual-report index (HTTP 403, Akamai); bajajauto.com `/investors/annual-reports` (HTTP 404; the IR pages are JS-rendered). The investors.bajajauto.com `ar21`–`ar26` index pages list the PDFs directly.

## 3. Figures (per gate or leg)

### 3a. Item table

| item | FY | value | unit | source |
|---|---|---|---|---|
| Revenue from operations | FY2017 | 23,088.03 | ₹ crore | AR17, consolidated statement of profit and loss, PDF p. 186 |
| Other income | FY2017 | 1,222.23 | ₹ crore | AR17, consolidated statement of profit and loss, PDF p. 186 |
| Finance costs | FY2017 | 1.40 | ₹ crore | AR17, consolidated statement of profit and loss, PDF p. 186 |
| Depreciation and amortisation | FY2017 | 307.29 | ₹ crore | AR17, consolidated statement of profit and loss, PDF p. 186 |
| Share of profit/(loss) of associate | FY2017 | 254.62 | ₹ crore | AR17, consolidated statement of profit and loss, PDF p. 186 |
| Profit before tax (after associate share and exceptional items) | FY2017 | 5,587.55 | ₹ crore | AR17, consolidated statement of profit and loss, PDF p. 186 |
| Net cash flow from operating activities | FY2017 | 3,267.36 | ₹ crore | AR17, consolidated cash flow statement, PDF pp. 189–191 |
| Capital expenditure (cash flow line vi) | FY2017 | 199.44 | ₹ crore | AR17, consolidated cash flow statement, PDF pp. 189–191 (also AR18 comparative) |
| Capital expenditure on development of technical know-how (line viii) | FY2017 | 6.18 | ₹ crore | AR17, consolidated cash flow statement, PDF pp. 189–191 |
| Total assets | FY2017 | 21,637.62 | ₹ crore | AR17, consolidated balance sheet, PDF pp. 184–185 |
| Trade payables (MSME + other creditors) | FY2017 | 2,235.98 | ₹ crore | AR17, consolidated balance sheet, PDF pp. 184–185 |
| Other current liabilities | FY2017 | 557.62 | ₹ crore | AR17, consolidated balance sheet, PDF pp. 184–185 |
| Cash and cash equivalents | FY2017 | 287.50 | ₹ crore | AR17, consolidated balance sheet, PDF pp. 184–185 |
| Other bank balances | FY2017 | 13.86 | ₹ crore | AR17, consolidated balance sheet, PDF pp. 184–185 |
| Non-current investments (note 5B) | FY2017 | 7,458.67 | ₹ crore | AR17, consolidated balance sheet, PDF pp. 184–185 |
| Current investments (note 5B) | FY2017 | 6,050.08 | ₹ crore | AR17, consolidated balance sheet, PDF pp. 184–185 |
| Investments in associate (equity method) | FY2017 | 1,968.29 | ₹ crore | AR17, consolidated balance sheet, PDF pp. 184–185 |
| Equity attributable to owners (share capital + other equity) | FY2017 | 17,856.57 | ₹ crore | AR17, consolidated balance sheet, PDF pp. 184–185 |
| Revenue from operations | FY2018 | 25,563.26 | ₹ crore | AR18, consolidated statement of profit and loss, PDF p. 179 |
| Other income | FY2018 | 1,212.27 | ₹ crore | AR18, consolidated statement of profit and loss, PDF p. 179 |
| Finance costs | FY2018 | 1.31 | ₹ crore | AR18, consolidated statement of profit and loss, PDF p. 179 |
| Depreciation and amortisation | FY2018 | 314.80 | ₹ crore | AR18, consolidated statement of profit and loss, PDF p. 179 |
| Share of profit/(loss) of associate | FY2018 | 287.61 | ₹ crore | AR18, consolidated statement of profit and loss, PDF p. 179 |
| Profit before tax (after associate share and exceptional items) | FY2018 | 5,933.41 | ₹ crore | AR18, consolidated statement of profit and loss, PDF p. 179 |
| Net cash flow from operating activities | FY2018 | 4,327.84 | ₹ crore | AR18, consolidated cash flow statement, PDF pp. 182–184 |
| Purchase of PP&E incl. advances | FY2018 | 182.63 | ₹ crore | AR18, consolidated cash flow statement, PDF pp. 182–184 |
| Total assets | FY2018 | 25,141.00 | ₹ crore | AR18, consolidated balance sheet, PDF pp. 177–178 |
| Trade payables (MSME + other creditors) | FY2018 | 3,244.42 | ₹ crore | AR18, consolidated balance sheet, PDF pp. 177–178 |
| Other current liabilities | FY2018 | 393.73 | ₹ crore | AR18, consolidated balance sheet, PDF pp. 177–178 |
| Cash and cash equivalents | FY2018 | 775.60 | ₹ crore | AR18, consolidated balance sheet, PDF pp. 177–178 |
| Other bank balances | FY2018 | 17.06 | ₹ crore | AR18, consolidated balance sheet, PDF pp. 177–178 |
| Non-current investments (note 5B) | FY2018 | 10,600.17 | ₹ crore | AR18, consolidated balance sheet, PDF pp. 177–178 |
| Current investments (note 5B) | FY2018 | 5,765.41 | ₹ crore | AR18, consolidated balance sheet, PDF pp. 177–178 |
| Investments in associate (equity method) | FY2018 | 2,528.99 | ₹ crore | AR18, consolidated balance sheet, PDF pp. 177–178 |
| Equity attributable to owners (share capital + other equity) | FY2018 | 20,425.24 | ₹ crore | AR18, consolidated balance sheet, PDF pp. 177–178 |
| Revenue from operations | FY2019 | 30,249.96 | ₹ crore | AR19, consolidated statement of profit and loss, PDF p. 219 |
| Other income | FY2019 | 1,555.01 | ₹ crore | AR19, consolidated statement of profit and loss, PDF p. 219 |
| Finance costs | FY2019 | 4.48 | ₹ crore | AR19, consolidated statement of profit and loss, PDF p. 219 |
| Depreciation and amortisation | FY2019 | 265.69 | ₹ crore | AR19, consolidated statement of profit and loss, PDF p. 219 |
| Share of profit/(loss) of associate | FY2019 | 349.75 | ₹ crore | AR19, consolidated statement of profit and loss, PDF p. 219 |
| Profit before tax (after associate share and exceptional items) | FY2019 | 6,955.58 | ₹ crore | AR19, consolidated statement of profit and loss, PDF p. 219 |
| Net cash flow from operating activities | FY2019 | 2,486.86 | ₹ crore | AR19, consolidated cash flow statement, PDF pp. 222–224 |
| Purchase of PP&E incl. advances | FY2019 | 163.53 | ₹ crore | AR19, consolidated cash flow statement, PDF pp. 222–224 |
| Total assets | FY2019 | 28,834.41 | ₹ crore | AR19, consolidated balance sheet, PDF pp. 217–218 |
| Trade payables (MSME + other creditors) | FY2019 | 3,786.83 | ₹ crore | AR19, consolidated balance sheet, PDF pp. 217–218 |
| Other current liabilities | FY2019 | 556.97 | ₹ crore | AR19, consolidated balance sheet, PDF pp. 217–218 |
| Cash and cash equivalents | FY2019 | 915.64 | ₹ crore | AR19, consolidated balance sheet, PDF pp. 217–218 |
| Other bank balances | FY2019 | 17.43 | ₹ crore | AR19, consolidated balance sheet, PDF pp. 217–218 |
| Non-current investments (note 5B) | FY2019 | 16,360.16 | ₹ crore | AR19, consolidated balance sheet, PDF pp. 217–218 |
| Current investments (note 5B) | FY2019 | 1,576.48 | ₹ crore | AR19, consolidated balance sheet, PDF pp. 217–218 |
| Investments in associate (equity method) | FY2019 | 2,666.21 | ₹ crore | AR19, consolidated balance sheet, PDF pp. 217–218 |
| Equity attributable to owners (share capital + other equity) | FY2019 | 23,233.81 | ₹ crore | AR19, consolidated balance sheet, PDF pp. 217–218 |
| Revenue from operations | FY2020 | 29,918.65 | ₹ crore | AR20, consolidated statement of profit and loss, PDF p. 220 |
| Other income | FY2020 | 1,524.57 | ₹ crore | AR20, consolidated statement of profit and loss, PDF p. 220 |
| Finance costs | FY2020 | 3.16 | ₹ crore | AR20, consolidated statement of profit and loss, PDF p. 220 |
| Depreciation and amortisation | FY2020 | 246.43 | ₹ crore | AR20, consolidated statement of profit and loss, PDF p. 220 |
| Share of profit/(loss) of associate | FY2020 | 321.51 | ₹ crore | AR20, consolidated statement of profit and loss, PDF p. 220 |
| Profit before tax (after associate share and exceptional items) | FY2020 | 6,692.13 | ₹ crore | AR20, consolidated statement of profit and loss, PDF p. 220 |
| Net cash flow from operating activities | FY2020 | 3,850.44 | ₹ crore | AR20, consolidated cash flow statement, PDF pp. 224–226 |
| Purchase of PP&E incl. advances | FY2020 | 282.81 | ₹ crore | AR20, consolidated cash flow statement, PDF pp. 224–226 |
| Total assets | FY2020 | 26,510.02 | ₹ crore | AR20, consolidated balance sheet, PDF pp. 218–219 |
| Trade payables (MSME + other creditors) | FY2020 | 3,199.82 | ₹ crore | AR20, consolidated balance sheet, PDF pp. 218–219 |
| Other current liabilities | FY2020 | 328.88 | ₹ crore | AR20, consolidated balance sheet, PDF pp. 218–219 |
| Cash and cash equivalents | FY2020 | 285.40 | ₹ crore | AR20, consolidated balance sheet, PDF pp. 218–219 |
| Other bank balances | FY2020 | 30.94 | ₹ crore | AR20, consolidated balance sheet, PDF pp. 218–219 |
| Non-current investments (note 5B) | FY2020 | 14,182.94 | ₹ crore | AR20, consolidated balance sheet, PDF pp. 218–219 |
| Current investments (note 5B) | FY2020 | 2,779.75 | ₹ crore | AR20, consolidated balance sheet, PDF pp. 218–219 |
| Investments in associate (equity method) | FY2020 | 2,950.89 | ₹ crore | AR20, consolidated balance sheet, PDF pp. 218–219 |
| Equity attributable to owners (share capital + other equity) | FY2020 | 21,662.08 | ₹ crore | AR20, consolidated balance sheet, PDF pp. 218–219 |
| Revenue from operations | FY2021 | 27,741.08 | ₹ crore | AR21, consolidated statement of profit and loss, PDF p. 188 |
| Other income | FY2021 | 1,276.46 | ₹ crore | AR21, consolidated statement of profit and loss, PDF p. 188 |
| Finance costs | FY2021 | 6.66 | ₹ crore | AR21, consolidated statement of profit and loss, PDF p. 188 |
| Depreciation and amortisation | FY2021 | 259.37 | ₹ crore | AR21, consolidated statement of profit and loss, PDF p. 188 |
| Share of profit/(loss) of associate | FY2021 | 306.32 | ₹ crore | AR21, consolidated statement of profit and loss, PDF p. 188 |
| Profit before tax (after associate share and exceptional items) | FY2021 | 6,241.43 | ₹ crore | AR21, consolidated statement of profit and loss, PDF p. 188 |
| Net cash flow from operating activities | FY2021 | 3,119.88 | ₹ crore | AR21, consolidated cash flow statement, PDF pp. 192–194 |
| Purchase of PP&E incl. advances | FY2021 | 244.06 | ₹ crore | AR21, consolidated cash flow statement, PDF pp. 192–194 |
| Total assets | FY2021 | 33,601.71 | ₹ crore | AR21, consolidated balance sheet, PDF pp. 186–187 |
| Trade payables (MSME + other creditors) | FY2021 | 4,574.11 | ₹ crore | AR21, consolidated balance sheet, PDF pp. 186–187 |
| Other current liabilities | FY2021 | 482.82 | ₹ crore | AR21, consolidated balance sheet, PDF pp. 186–187 |
| Cash and cash equivalents | FY2021 | 516.61 | ₹ crore | AR21, consolidated balance sheet, PDF pp. 186–187 |
| Other bank balances | FY2021 | 22.23 | ₹ crore | AR21, consolidated balance sheet, PDF pp. 186–187 |
| Non-current investments (note 5B) | FY2021 | 13,369.58 | ₹ crore | AR21, consolidated balance sheet, PDF pp. 186–187 |
| Current investments (note 5B) | FY2021 | 8,028.11 | ₹ crore | AR21, consolidated balance sheet, PDF pp. 186–187 |
| Investments in associate (equity method) | FY2021 | 3,288.96 | ₹ crore | AR21, consolidated balance sheet, PDF pp. 186–187 |
| Equity attributable to owners (share capital + other equity) | FY2021 | 27,273.43 | ₹ crore | AR21, consolidated balance sheet, PDF pp. 186–187 |
| Revenue from operations | FY2022 | 33,144.71 | ₹ crore | AR22, consolidated statement of profit and loss, PDF p. 202 |
| Other income | FY2022 | 1,284.14 | ₹ crore | AR22, consolidated statement of profit and loss, PDF p. 202 |
| Finance costs | FY2022 | 8.66 | ₹ crore | AR22, consolidated statement of profit and loss, PDF p. 202 |
| Depreciation and amortisation | FY2022 | 269.76 | ₹ crore | AR22, consolidated statement of profit and loss, PDF p. 202 |
| Share of profit/(loss) of associate | FY2022 | 579.53 | ₹ crore | AR22, consolidated statement of profit and loss, PDF p. 202 |
| Profit before tax (after associate share and exceptional items) | FY2022 | 7,651.68 | ₹ crore | AR22, consolidated statement of profit and loss, PDF p. 202 |
| Net cash flow from operating activities | FY2022 | 4,197.21 | ₹ crore | AR22, consolidated cash flow statement, PDF pp. 206–208 |
| Purchase of PP&E incl. advances | FY2022 | 550.75 | ₹ crore | AR22, consolidated cash flow statement, PDF pp. 206–208 |
| Total assets | FY2022 | 35,111.21 | ₹ crore | AR22, consolidated balance sheet, PDF pp. 200–201 |
| Trade payables (MSME + other creditors) | FY2022 | 3,632.15 | ₹ crore | AR22, consolidated balance sheet, PDF pp. 200–201 |
| Other current liabilities | FY2022 | 478.80 | ₹ crore | AR22, consolidated balance sheet, PDF pp. 200–201 |
| Cash and cash equivalents | FY2022 | 933.69 | ₹ crore | AR22, consolidated balance sheet, PDF pp. 200–201 |
| Other bank balances | FY2022 | 24.37 | ₹ crore | AR22, consolidated balance sheet, PDF pp. 200–201 |
| Non-current investments (note 5B) | FY2022 | 17,601.20 | ₹ crore | AR22, consolidated balance sheet, PDF pp. 200–201 |
| Current investments (note 5B) | FY2022 | 4,969.13 | ₹ crore | AR22, consolidated balance sheet, PDF pp. 200–201 |
| Investments in associate (equity method) | FY2022 | 4,063.79 | ₹ crore | AR22, consolidated balance sheet, PDF pp. 200–201 |
| Equity attributable to owners (share capital + other equity) | FY2022 | 29,859.65 | ₹ crore | AR22, consolidated balance sheet, PDF pp. 200–201 |
| Revenue from operations | FY2023 | 36,455.38 | ₹ crore | AR23, consolidated statement of profit and loss, PDF p. 200 |
| Other income | FY2023 | 1,187.52 | ₹ crore | AR23, consolidated statement of profit and loss, PDF p. 200 |
| Finance costs | FY2023 | 39.51 | ₹ crore | AR23, consolidated statement of profit and loss, PDF p. 200 |
| Depreciation and amortisation | FY2023 | 285.85 | ₹ crore | AR23, consolidated statement of profit and loss, PDF p. 200 |
| Share of profit/(loss) of associate | FY2023 | 529.29 | ₹ crore | AR23, consolidated statement of profit and loss, PDF p. 200 |
| Profit before tax (after associate share and exceptional items) | FY2023 | 7,841.98 | ₹ crore | AR23, consolidated statement of profit and loss, PDF p. 200 |
| Net cash flow from operating activities | FY2023 | 5,277.42 | ₹ crore | AR23, consolidated cash flow statement, PDF pp. 204–206 |
| Purchase of PP&E incl. advances | FY2023 | 1,074.47 | ₹ crore | AR23, consolidated cash flow statement, PDF pp. 204–206 |
| Total assets | FY2023 | 35,136.45 | ₹ crore | AR23, consolidated balance sheet, PDF pp. 198–199 |
| Trade payables (MSME + other creditors) | FY2023 | 4,121.18 | ₹ crore | AR23, consolidated balance sheet, PDF pp. 198–199 |
| Other current liabilities | FY2023 | 492.61 | ₹ crore | AR23, consolidated balance sheet, PDF pp. 198–199 |
| Current tax liabilities (net) | FY2023 | 23.74 | ₹ crore | AR23, consolidated balance sheet, PDF pp. 198–199 |
| Cash and cash equivalents | FY2023 | 241.62 | ₹ crore | AR23, consolidated balance sheet, PDF pp. 198–199 |
| Other bank balances | FY2023 | 448.86 | ₹ crore | AR23, consolidated balance sheet, PDF pp. 198–199 |
| Non-current investments (note 5B) | FY2023 | 16,717.53 | ₹ crore | AR23, consolidated balance sheet, PDF pp. 198–199 |
| Current investments (note 5B) | FY2023 | 4,581.35 | ₹ crore | AR23, consolidated balance sheet, PDF pp. 198–199 |
| Investments in associate (equity method) | FY2023 | 4,884.03 | ₹ crore | AR23, consolidated balance sheet, PDF pp. 198–199 |
| Equity attributable to owners (share capital + other equity) | FY2023 | 29,361.54 | ₹ crore | AR23, consolidated balance sheet, PDF pp. 198–199 |
| Revenue from operations | FY2024 | 44,870.43 | ₹ crore | AR24, consolidated statement of profit and loss, PDF p. 220 |
| Other income | FY2024 | 1,436.02 | ₹ crore | AR24, consolidated statement of profit and loss, PDF p. 220 |
| Finance costs | FY2024 | 60.36 | ₹ crore | AR24, consolidated statement of profit and loss, PDF p. 220 |
| Depreciation and amortisation | FY2024 | 364.77 | ₹ crore | AR24, consolidated statement of profit and loss, PDF p. 220 |
| Share of profit/(loss) of associate | FY2024 | 267.59 | ₹ crore | AR24, consolidated statement of profit and loss, PDF p. 220 |
| Profit before tax (after associate share and exceptional items) | FY2024 | 10,040.04 | ₹ crore | AR24, consolidated statement of profit and loss, PDF p. 220 |
| Net cash flow from operating activities | FY2024 | 6,558.16 | ₹ crore | AR24, consolidated cash flow statement, PDF pp. 224–226 |
| Purchase of PP&E incl. advances | FY2024 | 706.45 | ₹ crore | AR24, consolidated cash flow statement, PDF pp. 224–226 |
| Expenditure on intangible assets incl. under development | FY2024 | 16.39 | ₹ crore | AR24, consolidated cash flow statement, PDF pp. 224–226 |
| Total assets | FY2024 | 39,343.69 | ₹ crore | AR24, consolidated balance sheet, PDF pp. 218–219 |
| Trade payables (MSME + other creditors) | FY2024 | 5,597.39 | ₹ crore | AR24, consolidated balance sheet, PDF pp. 218–219 |
| Other current liabilities | FY2024 | 1,530.90 | ₹ crore | AR24, consolidated balance sheet, PDF pp. 218–219 |
| Current tax liabilities (net) | FY2024 | 20.08 | ₹ crore | AR24, consolidated balance sheet, PDF pp. 218–219 |
| Cash and cash equivalents | FY2024 | 560.45 | ₹ crore | AR24, consolidated balance sheet, PDF pp. 218–219 |
| Other bank balances | FY2024 | 394.87 | ₹ crore | AR24, consolidated balance sheet, PDF pp. 218–219 |
| Non-current investments (note 5B) | FY2024 | 17,834.69 | ₹ crore | AR24, consolidated balance sheet, PDF pp. 218–219 |
| Current investments (note 5B) | FY2024 | 5,431.59 | ₹ crore | AR24, consolidated balance sheet, PDF pp. 218–219 |
| Investments in associate (equity method) | FY2024 | 4,820.40 | ₹ crore | AR24, consolidated balance sheet, PDF pp. 218–219 |
| Borrowings (non-current + current) | FY2024 | 1,785.90 | ₹ crore | AR24, consolidated balance sheet, PDF pp. 218–219 |
| Equity attributable to owners (share capital + other equity) | FY2024 | 28,962.41 | ₹ crore | AR24, consolidated balance sheet, PDF pp. 218–219 |
| Revenue from operations | FY2025 | 50,994.55 | ₹ crore | AR25, consolidated statement of profit and loss, PDF p. 234 |
| Other income | FY2025 | 1,474.41 | ₹ crore | AR25, consolidated statement of profit and loss, PDF p. 234 |
| Finance costs | FY2025 | 388.90 | ₹ crore | AR25, consolidated statement of profit and loss, PDF p. 234 |
| Depreciation and amortisation | FY2025 | 414.23 | ₹ crore | AR25, consolidated statement of profit and loss, PDF p. 234 |
| Share of profit/(loss) of associate | FY2025 | -915.48 | ₹ crore | AR25, consolidated statement of profit and loss, PDF p. 234 |
| Profit before tax (after associate share and exceptional items) | FY2025 | 10,223.53 | ₹ crore | AR25, consolidated statement of profit and loss, PDF p. 234 |
| Net cash flow from operating activities | FY2025 | -1,405.57 | ₹ crore | AR25, consolidated cash flow statement, PDF pp. 238–240 |
| Purchase of PP&E incl. advances | FY2025 | 813.54 | ₹ crore | AR25, consolidated cash flow statement, PDF pp. 238–240 |
| Expenditure on intangible assets incl. under development | FY2025 | 60.30 | ₹ crore | AR25, consolidated cash flow statement, PDF pp. 238–240 |
| Total assets | FY2025 | 54,198.61 | ₹ crore | AR25, consolidated balance sheet, PDF pp. 232–233 |
| Trade payables (MSME + other creditors) | FY2025 | 6,372.71 | ₹ crore | AR25, consolidated balance sheet, PDF pp. 232–233 |
| Other current liabilities | FY2025 | 813.61 | ₹ crore | AR25, consolidated balance sheet, PDF pp. 232–233 |
| Current tax liabilities (net) | FY2025 | 235.77 | ₹ crore | AR25, consolidated balance sheet, PDF pp. 232–233 |
| Cash and cash equivalents | FY2025 | 2,331.53 | ₹ crore | AR25, consolidated balance sheet, PDF pp. 232–233 |
| Other bank balances | FY2025 | 516.07 | ₹ crore | AR25, consolidated balance sheet, PDF pp. 232–233 |
| Non-current investments (note 5B) | FY2025 | 19,323.58 | ₹ crore | AR25, consolidated balance sheet, PDF pp. 232–233 |
| Current investments (note 5B) | FY2025 | 5,902.02 | ₹ crore | AR25, consolidated balance sheet, PDF pp. 232–233 |
| Investments in associate (equity method) | FY2025 | 3,688.27 | ₹ crore | AR25, consolidated balance sheet, PDF pp. 232–233 |
| Borrowings (non-current + current) | FY2025 | 9,236.52 | ₹ crore | AR26, consolidated balance sheet, PDF pp. 248–249, comparative column (non-current 6,082.74 + current 3,153.78) |
| Equity attributable to owners (share capital + other equity) | FY2025 | 35,188.74 | ₹ crore | AR25, consolidated balance sheet, PDF pp. 232–233 |
| Revenue from operations | FY2026 | 62,905.00 | ₹ crore | AR26, consolidated statement of profit and loss, PDF p. 250 |
| Other income | FY2026 | 2,182.22 | ₹ crore | AR26, consolidated statement of profit and loss, PDF p. 250 |
| Finance costs | FY2026 | 1,168.59 | ₹ crore | AR26, consolidated statement of profit and loss, PDF p. 250 |
| Depreciation and amortisation | FY2026 | 644.69 | ₹ crore | AR26, consolidated statement of profit and loss, PDF p. 250 |
| Share of profit/(loss) of associate | FY2026 | 560.74 | ₹ crore | AR26, consolidated statement of profit and loss, PDF p. 250 |
| Exceptional items (net), loss | FY2026 | 39.21 | ₹ crore | AR26, consolidated statement of profit and loss, PDF p. 250 (note 32) |
| Profit before tax (after associate share and exceptional items) | FY2026 | 13,951.54 | ₹ crore | AR26, consolidated statement of profit and loss, PDF p. 250 |
| Profit attributable to owners / to NCI | FY2026 | 10,744.21 / -169.71 | ₹ crore | AR26, consolidated statement of profit and loss, PDF p. 250 |
| Net cash flow from operating activities | FY2026 | 2,596.60 | ₹ crore | AR26, consolidated cash flow statement, PDF pp. 254–256 |
| (Increase) in loans and other assets inside CFO (financing book) | FY2026 / FY2025 | -10,370.85 / -9,848.16 | ₹ crore | AR26, consolidated cash flow statement, PDF p. 254, item I(iii) |
| Purchase of PP&E incl. advances | FY2026 | 560.39 | ₹ crore | AR26, consolidated cash flow statement, PDF pp. 254–256 |
| Expenditure on intangible assets incl. under development | FY2026 | 161.93 | ₹ crore | AR26, consolidated cash flow statement, PDF pp. 254–256 |
| Total assets | FY2026 | 77,222.99 | ₹ crore | AR26, consolidated balance sheet, PDF pp. 248–249 |
| Trade payables (MSME + other creditors) | FY2026 | 8,804.01 | ₹ crore | AR26, consolidated balance sheet, PDF pp. 248–249 |
| Other current liabilities | FY2026 | 1,243.82 | ₹ crore | AR26, consolidated balance sheet, PDF pp. 248–249 |
| Current tax liabilities (net) | FY2026 | 412.70 | ₹ crore | AR26, consolidated balance sheet, PDF pp. 248–249 |
| Cash and cash equivalents | FY2026 | 2,989.97 | ₹ crore | AR26, consolidated balance sheet, PDF pp. 248–249 |
| Other bank balances | FY2026 | 81.92 | ₹ crore | AR26, consolidated balance sheet, PDF pp. 248–249 |
| Non-current investments (note 5B) | FY2026 | 16,661.34 | ₹ crore | AR26, consolidated balance sheet, PDF pp. 248–249 |
| Current investments (note 5B) | FY2026 | 7,811.66 | ₹ crore | AR26, consolidated balance sheet, PDF pp. 248–249 |
| Loans, non-current / current (mainly the Financing segment's book) | FY2026 | 10,887.85 / 7,936.17 | ₹ crore | AR26, consolidated balance sheet, PDF p. 248 (FY2025: 6,450.97 / 3,465.19) |
| Investments in associate (equity method) | FY2026 | 169.18 | ₹ crore | AR26, consolidated balance sheet, PDF pp. 248–249 |
| Borrowings (non-current + current) | FY2026 | 21,980.59 | ₹ crore | AR26, consolidated balance sheet, PDF pp. 248–249 |
| Lease liabilities (non-current + current) | FY2026 | 659.26 | ₹ crore | AR26, consolidated balance sheet, PDF p. 249 (469.07 + 190.19; nil at FY2025) |
| Non-controlling interest | FY2026 | 1,388.43 | ₹ crore | AR26, consolidated balance sheet, PDF p. 249 |
| Equity attributable to owners (share capital + other equity) | FY2026 | 38,831.99 | ₹ crore | AR26, consolidated balance sheet, PDF pp. 248–249 |
| Total assets | FY2016 (opening BS, Ind AS comparative) | 17,240.37 | ₹ crore | AR17, consolidated balance sheet, PDF pp. 184–185, comparative column |
| Trade payables (MSME + other creditors) | FY2016 (opening BS, Ind AS comparative) | 2,027.11 | ₹ crore | AR17, consolidated balance sheet, PDF pp. 184–185, comparative column |
| Cash and cash equivalents | FY2016 (opening BS, Ind AS comparative) | 819.91 | ₹ crore | AR17, consolidated balance sheet, PDF pp. 184–185, comparative column |
| Other bank balances | FY2016 (opening BS, Ind AS comparative) | 47.12 | ₹ crore | AR17, consolidated balance sheet, PDF pp. 184–185, comparative column |
| Non-current investments | FY2016 (opening BS, Ind AS comparative) | 7,717.93 | ₹ crore | AR17, consolidated balance sheet, PDF pp. 184–185, comparative column |
| Current investments | FY2016 (opening BS, Ind AS comparative) | 1,319.94 | ₹ crore | AR17, consolidated balance sheet, PDF pp. 184–185, comparative column |
| Investments in associate (equity method) | FY2016 (opening BS, Ind AS comparative) | 1,968.93 | ₹ crore | AR17, consolidated balance sheet, PDF pp. 184–185, comparative column |
| Other current liabilities | FY2016 (opening BS, Ind AS comparative) | 299.11 | ₹ crore | AR17, consolidated balance sheet, PDF pp. 184–185, comparative column |
| Current tax liabilities (net) | FY2016 (opening BS, Ind AS comparative) | 34.37 | ₹ crore | AR17, consolidated balance sheet, PDF pp. 184–185, comparative column |
| Equity attributable to owners | FY2016 (opening BS, Ind AS comparative) | 14,020.31 | ₹ crore | AR17, consolidated balance sheet, PDF pp. 184–185, comparative column |
| Revenue from operations (Ind AS comparative, gross of excise) | FY2016 | 23,883.20 | ₹ crore | AR17, consolidated P&L, PDF p. 186, comparative column |
| Other income | FY2016 | 984.58 | ₹ crore | AR17, consolidated P&L, PDF p. 186, comparative column |
| Share of profit of associate | FY2016 | 221.44 | ₹ crore | AR17, consolidated P&L, PDF p. 186, comparative column |
| Profit before tax | FY2016 | 5,678.89 | ₹ crore | AR17, consolidated P&L, PDF p. 186, comparative column |
| Net cash flow from operating activities | FY2016 | 3,689.85 | ₹ crore | AR17, consolidated cash flow, PDF p. 189, comparative column |
| Capital expenditure (line vi) / technical know-how (line viii) | FY2016 | 265.14 / 6.06 | ₹ crore | AR17, consolidated cash flow, PDF p. 189, comparative column |
| Segment revenue: Automotive / Investments / Financing | FY2026 | 60,530.43 / 1,309.18 / 3,247.61 | ₹ crore | AR26 note 44(a), PDF p. 350 |
| Segment result: Automotive / Investments / Financing | FY2026 | 12,016.19 / 1,306.98 / 888.58 | ₹ crore | AR26 note 44(a), PDF p. 350 (Automotive carries the 260.21 finance costs below its result; the Financing result is after its own funding cost) |
| Segment assets: Automotive / Investments / Financing (+ associate 169.18, unallocated 1,539.17) | FY2026 | 30,161.47 / 25,579.02 / 19,774.15 | ₹ crore | AR26 note 44(a), PDF p. 350 |
| Segment liabilities: Automotive / Financing | FY2026 | 13,216.26 / 16,003.17 | ₹ crore | AR26 note 44(a), PDF p. 350 |
| Capex / depreciation: Automotive, Investments, Financing | FY2026 | 678.95, 1.66, 13.55 / 634.82, –, 9.87 | ₹ crore | AR26 note 44(a), PDF p. 350 |
| Segment revenue: Automotive / Investments / Financing | FY2025 | 49,982.13 / 1,445.98 / 1,040.85 | ₹ crore | AR26 note 44, PDF p. 351 (comparative) |
| Segment result: Automotive / Investments / Financing | FY2025 | 8,769.75 / 1,443.72 / 78.15 | ₹ crore | AR26 note 44, PDF p. 351 (Automotive finance costs 68.09) |
| Segment assets: Automotive / Investments / Financing (+ associate 3,688.27) | FY2025 | 12,061.70 / 26,135.15 / 10,972.90 | ₹ crore | AR26 note 44, PDF p. 351 |
| Geographic revenue: India / rest of world | FY2026 | 42,920.23 / 22,166.99 | ₹ crore | AR26 note 44(b), PDF p. 350 |
| BAIH AG (ex-Pierer Bajaj AG) control acquired; group effective interest in Bajaj Mobility AG and KTM AG | 18 Nov 2025 | 74.94% | % | AR26 note 46, PDF p. 354 |
| Purchase consideration: call option on existing loan 524.09 + fair value of the 49.9% held 3,931.95 | FY2026 | 4,456.04 | ₹ crore | AR26 note 46, PDF pp. 354–355 |
| Remeasurement gain on the previously held interest / FCTR recycled to P&L | FY2026 | 953.10 / 645.71 | ₹ crore | AR26 note 46, PDF p. 354 (where booked: inside "Share of profits of associate (net)" or elsewhere is owed; note 49) |
| KTM group identifiable assets / liabilities / net assets at fair value / NCI | 18 Nov 2025 | 19,638.90 / 13,627.73 / 6,011.17 / 1,533.30 | ₹ crore | AR26 note 46, PDF p. 355 (incl. borrowings 9,562.82, intangibles 3,924.92, inventories 4,764.29) |
| Bargain purchase gain (capital reserve, via OCI) | FY2026 | 21.83 | ₹ crore | AR26 note 46, PDF p. 355 |
| BAIH AG contribution after acquisition: revenue / loss before tax | FY2026 | 1,296.23 / 871.86 | ₹ crore | AR26 note 46, PDF p. 355 (consolidated "from date of acquisition till 31 December 2025": one-quarter lag) |
| Pro forma full year as if acquired 1 Apr 2025: revenue / PBT (as printed) | FY2026 | 10,236.98 / 6,063.52 | ₹ crore | AR26 note 46, PDF p. 355 (the printed pro forma basis is unclear; re-read) |
| Bajaj Mobility AG CY2025 consolidated revenue | CY2025 | 1,009 | € million | AR26 Board's report, line ≈1653 of the text (PDF page owed) |
| Bajaj Holdings & Investment Ltd shares held (FVTOCI, quoted): 3,500,000 shares | FY2026 / FY2025 | 3,061.10 / 4,365.57 | ₹ crore | AR26 note 5B, PDF p. 285 |
| Yulu Bikes Pvt Ltd CCPS and equity (FVTOCI, unquoted) | FY2026 / FY2025 | 98.30 / 261.18 | ₹ crore | AR26 note 5B, PDF p. 285 |
| Associates after control: CFMOTO-KTMR2R 49% 168.85; LX Media 20% 0.33; KISKA 20% 13.74 (held for sale) | FY2026 | 169.18 | ₹ crore | AR26 note 5B(A), PDF p. 285 |
| Investment income inside other income: interest on fixed income securities 147.24, fixed deposits 102.47, loans 568.39, ETFs 432.53, FMPs 52.77; MF fair-value gains 486.49; profit on sale 12.79; dividends on strategic investments 32.55 | FY2026 | 1,829.07 | ₹ crore | AR26 consolidated cash flow, PDF p. 254, item I "Less: (i)" (FY2025: 1,453.79, of which loans 8.38, dividends 30.10) |
| Dividend income on other strategic investments | FY2024 / FY2023 | 43.05 / 47.25 | ₹ crore | AR24 consolidated cash flow, PDF p. 224 |
| Bajaj Holdings & Investment Ltd holding in Bajaj Auto | 31 Mar 2026 | 95,547,251 shares, 34.19% | shares, % | AR26 shareholding of promoter group, PDF p. 198 |
| Rajiv Bajaj (MD and CEO) shares held | 31 Mar 2026 | 878,001 | shares | AR26 corporate governance report, director table, PDF page owed (text line ≈4515) |
| Rajiv Bajaj total remuneration (salary and perquisites 236,588,385 + commission 352,148,400) | FY2026 | 588,736,785 | ₹ | AR26 corporate governance report, Table 11, PDF p. 117 |
| Pradeep Shrivastava / Rakesh Sharma (executive directors) total remuneration | FY2026 | 210,969,553 / 152,982,188 | ₹ | AR26 Table 11, PDF p. 117 |
| Non-executive director totals: Niraj Bajaj 4,565,000; Sanjiv Bajaj 2,490,000; Naushad Forbes 7,470,000; Anami N. Roy 6,225,000 | FY2026 | as listed | ₹ | AR26 Table 11, PDF p. 117 |
| Weighted average shares, net (basic) | FY2017–FY2019 | 289,367,020 | shares | AR17 p. 156, AR18 p. 147, AR19 p. 186 (EPS note) |
| Weighted average shares, net (basic) | FY2020 / FY2021 / FY2022 | 289,267,270 / 289,244,778 / 289,145,562 | shares | AR20 p. 187, AR21 p. 156, AR22 p. 166 (EPS note) |
| Weighted average shares, net (basic) | FY2023 / FY2024 | 285,206,634 / 282,695,661 | shares | AR23 p. 164; AR24 EPS note (PDF page owed) |
| Weighted average shares basic / diluted | FY2025 | 279,103,387 / 279,614,941 | shares | AR25 EPS note, PDF p. 196 |
| Weighted average shares basic / diluted | FY2026 | 279,096,661 / 279,515,161 | shares | AR26 EPS note, PDF p. 211 |
| Weighted average diluted shares | FY2024 | 282,975,118 | shares | AR25 EPS note, PDF p. 196 (comparative) |
| Buyback 1: 6,409,662 shares, open market, commenced 4 Jul 2022 (board 27 Jun 2022); outlay incl. tax | FY2023 | 3,094 | ₹ crore | AR23 Board's report / MD&A (text; PDF page owed) |
| Buyback 2: 40,00,000 shares by tender at ₹10,000 (board 8 Jan 2024; tendering from 6 Mar 2024); outlay incl. tax | FY2024 | 4,932 | ₹ crore | AR24 Board's report (text; PDF page owed); FY2025 cash flow carries 931.84 (AR26 PDF p. 256, item III(viii)) |
| Equity share capital | FY2022 / FY2023 / FY2024 / FY2025 / FY2026 | 289.37 / 282.96 / 279.18 / 279.26 / 279.50 | ₹ crore | AR24 and AR26 consolidated balance sheets (face value ₹10) |
| Price (px) | 2026-11-03 | 10,540.00 | INR | PX (endpoint `currency` INR = px_unit) |

**Derived (labelled; not carried as governing).** Exclude-reading OI on the J1 build in §4 = PBT − other income − share of associate + finance costs other than the Financing segment's funding cost: FY2017 4,112.10 · FY2018 4,434.84 · FY2019 5,055.30 · FY2020 4,849.21 · FY2021 4,665.31 · FY2022 5,796.67 · FY2023 6,164.68 · FY2024 8,396.79 · FY2025 9,732.69 · FY2026 11,468.79 (derived: items above; Financing funding cost FY2025 320.81 = 388.90 − 68.09, FY2026 908.38 = 1,168.59 − 260.21, from note 44; FY2024 assumes all finance costs non-Financing, to be confirmed in AR24 note 44). The FY2026 figure includes the J-tested exceptional loss of 39.21 and KTM's post-acquisition result. Include-reading OI adds the associate result and the S3 dividends, with fair-value and disposal gains out (the FY2026 associate line may carry the 953.10 remeasurement and 645.71 FCTR gains; they come out on both readings), so the derived include figures are owed.

## 4. Readings settled (as far as the run got)

- **Key and unit.** `BAJAJ-AUTO.NS`, NSE, `px_unit` INR. ISIN INE917I01010. No split in the endpoint's range.
- **Gate 0 materials.** FY2026 note 44 names three reportable segments: Automotive (two-, three- and four-wheelers incl. the KTM group from 18 Nov 2025, the Chetak EV and exports; external revenue 60,530.43), Investments (the treasury book; 1,309.18) and Financing (Bajaj Auto Credit Ltd's vehicle loans; 3,247.61). India 66% / rest of world 34% of FY2026 segment revenue (derived). The group and unit sentences and the customer statement (R7, P15) are owed.
- **Units (P22, at FYE 31 Mar 2026).** On segment assets: Automotive 39.9%, Investments 33.9%, Financing 26.2% of 75,514.64 (derived). Investments is a treasury book of state development loans, PSU bonds, bond ETFs, FMPs, mutual funds and deposits (note 5B; S1/S2 cash-like per P26, longer bonds and bond funds at market × 0.9). Read as cash-like securities, it is **not a unit**. Its income is financial income (J3), and the S3 items in it (Bajaj Holdings shares, Yulu) are G6 classes. The resuming run confirms the S1/S2/S3 split line by line. Material units: **Automotive ex-KTM**, **Financing** (captive test owed: the book is vehicle loans to Bajaj buyers per the segment description; show the split if the filer gives one), and the **controlled listed subsidiary Bajaj Mobility AG**: KTM's acquired gross assets are 19,638.90 against group total assets of 77,222.99, so 25.4% (derived), at or above 10%.
- **Lens.** STD. Bajaj Auto Credit Ltd is an NBFC subsidiary (licence class to confirm); the group publishes no capital ratio covering ≥ 90% of consolidated assets and has a material non-financial part, so FI fails. Financing is read as a captive arm (R2), unless the captive test fails, in which case it is a non-captive lending unit on STD. Either way it is graded on OI after funding cost; its borrowings are debt-equivalents with the funding pairing; and the R6 book rule applies (book change beyond ±3% leaves FCF; funding principal in CFO leaves FCF).
- **Dependency (G4).** Bajaj Mobility AG (ISIN AT0000KTMI02 per secondary sources; confirm from AR26 note or BMAG's AR2025), primary line SIX Swiss Exchange, so §7.1a key `BMAG.SW` (endpoint serves it: CHF, EBS; Vienna `BMAG.VI` EUR also served). No register row or memo, so it is **ungradeable**: WEAK with its weight in the P29 Future, nothing added to the Past, SF INDETERMINATE (b) for the parent, NCI at the higher of market (74.94% held; BMAG share count owed) and book (1,388.43) in Gate 2. The row lists it under `## Group dependency` as `memo missing`.
- **G6 / P31.** The classes are the equity-accounted PBAG/BAIH AG associate (FY2016–FY2025; carrying value 1,968.93 → 4,884.03, which is 11.4% of total assets at FY2016, 13.9% at FY2023 and 6.8% at FY2025, all derived); loans to PBAG/KTM before control (IAS 28.38, if they formed part of the net investment; FY2026 interest on loans 568.39, FY2025 8.38); the S3 stakes (Bajaj Holdings & Investment shares, which are the parent's stock and so S3 by rule, 4,365.57 at FY2025; Yulu); and post-control associates (CFMOTO-KTMR2R 49%). Both limbs fail at most B2 dates and years, so the classes sit **above the line** and B1–B3 need both readings, the harsher governing.
- **Cross-holding.** Bajaj Holdings & Investment Ltd owns 34.19% of Bajaj Auto, and Bajaj Auto owns 3,500,000 BHIL shares: a cycle, read under votes versus economics (P23, V4), never a Gate-0 ground.
- **Pointers, not grades.** (i) The P19 acquisition stop on the KTM control deal (FY2026; consideration 4,456.04, above 1% of EV): the target is listed (Bajaj Mobility / PIERER Mobility), and its pre-deal OI was negative in CY2024 (KTM AG insolvency proceedings; restructuring gain 2025). "No positive pre-deal OI = at least CAUTION", and "a listed target below P3 = ADVERSE" needs BMAG's own Past read. This may decide SF, so read it first. (ii) MD pay ₹58.87 crore FY2026 against 5% of NI (≈ ₹537 crore, derived) sits far below the P17 proportionality line. Rajiv Bajaj's 878,001 shares × px ≈ ₹925 crore (derived) is about 15.7× the FY2026 total, so ALIGNED on the 10× route, subject to the three-year hairiest number. (iii) The two buybacks are material (FY2023: 2.2% of shares; FY2024: 1.4%, derived) and need point-of-purchase worth reads.

## 5. Scope still owed (in order)

- [ ] Re-open the governing figures above at their cited pages; confirm current tax liabilities FY2017–FY2022 (extraction unreliable this run) and the NIBCL composition (other current liabilities: advances from customers, statutory dues) for each year.
- [ ] J1 build per year from note 26 (other income) and the segment notes: confirm the Financing funding cost by year (AR24 and AR25 note 44); P28 not triggered on FY2026 (latest year highest).
- [ ] P20 per year: no disclosed maintenance figure seen. Constructed build with k (Σ net fixed capital ÷ Σ revenue), India CPI deflators (MoSPI CPI-Combined, FY2017–FY2026), real growth from organic revenue (FY2026 organic = revenue less KTM's 1,296.23), floor at depreciation of PP&E + amortisation; FY2017–FY2023 intangible spend lines (cash-flow "technical know-how" / "intangible assets").
- [ ] R6 Financing book: the BACL loan book at each year-end FY2024–FY2026 and its funding in CFO (AR24–AR26 Financing segment, BACL subsidiary financials if published); FCF ex-book change.
- [ ] G6 classes per year: associate result split (AR17–AR25 note "Investment in associates"), FY2026 note 49 (where the 953.10 and 645.71 gains sit), BHIL shares and other S3 carrying values per year (note 5B of each AR), loans to PBAG/KTM per year; P31 table; B2/B3 on both readings.
- [ ] Bajaj Mobility AG: confirm ISIN, share count and the SIX primary line (AR2025 at bajajmobility.com, EQS release 26 Mar 2026); market value of the 25.06% NCI at px_date; segment / P22 figures for B4 and P29 weights (KTM revenue CY2023–CY2025, OI sign).
- [ ] Gate 0 sentences (group; Automotive ex-KTM; Financing; Bajaj Mobility from its filings) and the customer statement (R7; dealer network, export distributors in Africa / LatAm; the Financing unit's funding concentration, P15 strict).
- [ ] Appendix D blocks: Automotive ex-KTM, Financing (funding test), Bajaj Mobility as ungradeable (`sub dependency`).
- [ ] Gate 1C: three-year pay table (AR24–AR26 Table 11 / remuneration annexure), director fees, P23 holdings (promoter group, pledges), RPT with Bajaj group entities and KTM pre-control (AR26 Board's report lines ≈3493, ≈5842), worth tables for the FY2023 open-market buyback (point-in-time reads on FY2020–FY2022 averages, the 31 Mar 2022 balance sheet, prices from the AR23 disclosure) and the FY2024 tender at ₹10,000 (FY2021–FY2023 averages, the 30 Sep 2023 or 31 Dec 2023 interim balance sheet); acquisition stop on KTM (pre-deal BMAG OI and price, its P3 status); allocation-across-the-parts table (segment window FY2025–FY2026 only on the three-segment basis, so fewer than three FYs, INDETERMINATE (b) unless AR24 reports Financing).
- [ ] Gate 2 at the latest interim (Q2 FY2027 results to 30 Sep 2026, NSE/BSE filings Oct 2026): debt, leases, cash and S1/S2 at the cash rule, the Financing funding as debt-equivalents with the funding pairing, NCI at market, TTM test; then the machine fields and the memo.

*Framework output, not investment advice.*
