# WISE.L — Wise Group plc — REVIEW resumable record (INCOMPLETE) — 2026-11-06

## 1. Header

- Key: WISE.L · ISIN JE00BQKY0816 (prior memo v3, from the UK Prospectus of 13 Apr 2026) · job REVIEW · D 2026-11-06 · T 2111 · base sha f7bee9b67a6abb4630e2a06998adb7cbb50739ec · live `model_version` v4.8.0
- Prior memo: `memos/WISE.L/WISE.L_2026-08-06_GSC.md` (memo v3, `model_version` v4.1.0, no §6.1 machine fields). Earlier: `archive/memos/WISE.L/WISE.L_2026-07-28_GSC.md` (v2) and `archive/memos/WISE.L/WISE.L_2026-07-14_GSC.md` (v1).
- Selected at REVIEW priority 1b: `queue/TODO.md` `▶ Method re-tests v4.8.0`, "Turned — Past" (customer funds). It was the first key in block order that was not claimed, pending, held under an incomplete marker or owed to an attended run. The prior is below v4.5.0, so every v4.5.0, v4.6.0 and v4.8.0 method rule applies in one run (`routines/REVIEW.md` step 4).
- **Named gap: method re-test exceeds budget.** This is a first overrun: at the base, no open ` — partial …` line or item exists for the key. No verdict and no grade are recorded here. Every figure is sourced to a primary document and a place in it, or labelled `derived` with its inputs.
- resumes: none (first record).

**Why one run cannot finish.** The prior's window is "FY2022–FY2026 (5y, listing-limited)", with FY2022–23 rows from an aggregator. Audited group accounts exist for every year FY2017–FY2026 at Companies House (§2, sources CH17–CH26), so the window is FY2017–FY2026 with the 31 Mar 2016 opening balance sheet. Under MODEL §2·1A that is a record-limited shortfall, not history-limited, and README §5 (D3) treats it as a gap. Every Companies House PDF is an **image-only scan**: `pdftotext` returns no text, and the routine sandbox has no OCR tool. Each year's statements and safeguarding note must therefore be read page by page. Each year also needs its own segregated-funds netting (v4.8.0), its own P20 build, and both cash variants. That is more than one run.

## 2. Per gate or leg — work done and the item table

**Sources retrieved this run (primary, uncounted under P14):**
- 20F = Wise plc / Wise Group plc Form 20-F for FY2026 (year to 31 Mar 2026), SEC accession 0001193125-26-282911, `https://www.sec.gov/Archives/edgar/data/2099039/000119312526282911/d17323d20f.htm`. US GAAP, USD millions. It contains the consolidated statement of comprehensive income (p. F-4), the statement of financial position (p. F-5), the statement of cash flows (p. F-7), Note 2 (cash and cash equivalents: safeguarding), Note 11 (AFS debt securities), Note 16 (funds payable and amounts due to customers), Note 17 (debt) and Item 6.B (compensation, p. 84).
- XBRL = SEC companyfacts for CIK 0002099039, `https://data.sec.gov/api/xbrl/companyfacts/CIK0002099039.json` (the 20-F's tagged facts; same figures as 20F).
- Companies House PDFs (`https://find-and-update.company-information.service.gov.uk` + path + `&download=0`). All are image-only scans; page counts as listed:
  - CH26 = Wise plc (13211214), group accounts to 31 Mar 2026, filed 10 Jul 2026, 147 pp: `/company/13211214/filing-history/MzUzMDM1ODkxM2FkaXF6a2N4/document?format=pdf`
  - CH25 = Wise plc, to 31 Mar 2025, filed 4 Jul 2025, 172 pp: `/company/13211214/filing-history/MzQ3MjU3ODE1NWFkaXF6a2N4/document?format=pdf`
  - CH24 = Wise plc, to 31 Mar 2024, filed 18 Jul 2024, 172 pp: `/company/13211214/filing-history/MzQyODY2ODYyNmFkaXF6a2N4/document?format=pdf`
  - CH23 = Wise plc, to 31 Mar 2023, filed 11 Sep 2023, 195 pp: `/company/13211214/filing-history/MzM5MjA5MjgwN2FkaXF6a2N4/document?format=pdf`
  - CH22 = Wise plc, to 31 Mar 2022, filed 9 Aug 2022, 167 pp: `/company/13211214/filing-history/MzM0ODAzMTExNWFkaXF6a2N4/document?format=pdf`
  - CH21 = TransferWise Ltd (07209813, now Wise Payments Ltd), group accounts to 31 Mar 2021, filed 27 Jul 2021, 92 pp: `/company/07209813/filing-history/MzMwNzkyNjE1NGFkaXF6a2N4/document?format=pdf`
  - CH20 = TransferWise Ltd, to 31 Mar 2020, filed 1 Oct 2020, 69 pp: `/company/07209813/filing-history/MzI3OTI1NDg5NWFkaXF6a2N4/document?format=pdf`
  - CH19 = TransferWise Ltd, to 31 Mar 2019, filed 24 Sep 2019, 76 pp: `/company/07209813/filing-history/MzI0NDg4MjkyN2FkaXF6a2N4/document?format=pdf`
  - CH18 = TransferWise Ltd, to 31 Mar 2018, filed 25 Oct 2018, 47 pp: `/company/07209813/filing-history/MzIxNzg5MjA0NGFkaXF6a2N4/document?format=pdf`
  - CH17 = TransferWise Ltd, to 31 Mar 2017 (with the 31 Mar 2016 comparatives), filed 17 Nov 2017, 50 pp: `/company/07209813/filing-history/MzE5MDI3NzIyNWFkaXF6a2N4/document?format=pdf`
  - Not needed for the window: Wise plc's initial accounts to 30 Jun 2021 (18 pp), and Wise Payments Ltd's solo accounts FY2022–FY2026.
- Price: `query1.finance.yahoo.com/v8/finance/chart/WISE.L` — `currency` GBp, `exchangeName` LSE, longName "Wise Group plc", instrument "WISE GROUP PLC CLS A ORD", regularMarketPrice 838.6 at 2026-11-06 16:48 UTC. Daily closes: 2026-10-30 807.4, 11-02 810.4, 11-03 806.0, 11-04 850.6, 11-05 825.2, 11-06 838.6. No split event in the 1-month range.
- FX: GBP/USD 1.3385 (ECB ref, 2026-11-06) and 1.3459 (ECB ref, 2026-11-05), from `api.frankfurter.dev`.
- Not retrievable: `owners.wise.com`, the IR host that would serve text-layer annual reports, returns HTTP 403 to the sandbox (wise.com/owners/ redirects there).

### Gate 0 and the lens

- Gate 0: the prior's sentence (PASS, unchanged from v1) is a pointer only. The v4.6.0 form is owed: the best sentence the filings allow, on all six parameters.
- Segments: one operating segment (XBRL `NumberOfOperatingSegments` = 1, FY2026). No units, so no group build is expected (to confirm on CH26's segment note).
- Lens: Wise is an e-money and payment institution group. It does not publish a consolidated bank or insurance capital ratio covering ≥ 90% of assets; to confirm on CH26. → STD by the Lens rule ("payment and e-money institutions … STD"). Settled reading, §3.

### Past — item table (USD m unless stated; FY ends 31 Mar)

| item | FY | value | unit | source |
|---|---|---|---|---|
| Revenue (from contracts with customers, ex assessed tax) | 2026 | 1,893.6 | $m | 20F p. F-4; XBRL RevenueFromContractWithCustomerExcludingAssessedTax |
| Revenue | 2025 | 1,546.3 | $m | same |
| Revenue | 2024 | 1,323.1 | $m | same |
| Interest income (operating, in revenue) | 2026 | 806.1 | $m | 20F p. F-4; XBRL InterestIncomeOperating |
| Interest income (operating) | 2025 | 758.3 | $m | same |
| Interest income (operating) | 2024 | 610.0 | $m | same |
| of which interest on corporate debt securities (operating) | 2026 / 2025 / 2024 | 63.0 / 42.5 / 24.8 | $m | XBRL InterestIncomeSecuritiesCorporateDebtOperating |
| Interest expense on customer deposits (operating) | 2026 / 2025 / 2024 | 196.9 / 205.7 / 157.0 | $m | XBRL InterestExpenseCustomerDeposits |
| Revenue net of interest expense | 2026 / 2025 / 2024 | 2,502.8 / 2,098.9 / 1,776.1 | $m | XBRL RevenuesNetOfInterestExpense |
| Total operating expenses | 2026 / 2025 / 2024 | 1,912.1 / 1,370.7 / 1,126.0 | $m | 20F p. F-4 |
| Operating income (J1 candidate: the only operating subtotal on the face) | 2026 / 2025 / 2024 | 590.7 / 728.2 / 650.1 | $m | 20F p. F-4 |
| Other income/(loss), net (below OI; Note 4) | 2026 / 2025 / 2024 | 69.7 / −10.7 / 6.6 | $m | 20F p. F-4 |
| Income before tax | 2026 / 2025 / 2024 | 660.4 / 717.5 / 656.7 | $m | 20F p. F-4 |
| Net income | 2026 / 2025 / 2024 | 498.7 / 550.3 / 501.5 | $m | 20F p. F-4 |
| Diluted weighted-average shares | 2026 / 2025 / 2024 | 1,029.7 / 1,045.7 / 1,048.9 | m | 20F p. F-4 |
| Basic weighted-average shares | 2026 / 2025 / 2024 | 1,019.5 / 1,032.3 / 1,032.6 | m | 20F p. F-4 |
| Share-based compensation | 2026 / 2025 / 2024 | 95.5 / 74.6 / 91.1 | $m | 20F p. F-7 |
| Depreciation and amortization | 2026 / 2025 / 2024 | 14.4 / 9.7 / 14.3 | $m | 20F p. F-7 |
| Depreciation (PP&E) | 2026 / 2025 / 2024 | 11.5 / 5.4 / 5.7 | $m | XBRL Depreciation |
| Impairment of assets | 2026 / 2025 / 2024 | 1.8 / 14.6 / — | $m | 20F p. F-7 |
| Net cash from operating activities | 2026 / 2025 / 2024 | 7,553.9 / 5,719.5 / 4,075.1 | $m | 20F p. F-7 |
| of which change in funds payable and amounts due to customers | 2026 / 2025 / 2024 | 6,999.7 / 5,138.4 / 3,571.5 | $m | 20F p. F-7 |
| Purchase of PP&E | 2026 / 2025 / 2024 | 19.6 / 44.1 / 13.4 | $m | 20F p. F-7 |
| Purchase of intangible assets | 2026 / 2025 / 2024 | 1.8 / 1.2 / 3.0 | $m | 20F p. F-7 |
| Purchase of AFS debt securities | 2026 / 2025 / 2024 | 9,047.4 / 8,227.9 / 11,988.5 | $m | 20F p. F-7 |
| Proceeds from sale and maturity of AFS securities | 2026 / 2025 / 2024 | 10,807.3 / 7,514.7 / 11,823.7 | $m | 20F p. F-7 |
| Repurchases of shares (cash) | 2026 / 2025 / 2024 | 473.4 / 92.5 / 86.2 | $m | 20F p. F-7 |
| Cash paid for interest | 2026 / 2025 / 2024 | 15.9 / 19.0 / 21.0 | $m | 20F p. F-7 (supplemental) |
| Cash paid for income taxes, net | 2026 / 2025 / 2024 | 162.5 / 184.4 / 93.1 | $m | 20F p. F-7 (supplemental) |
| Shares repurchased | 2026 / 2025 / 2024 | 35,913,201 / 8,704,883 / 9,071,706 | shares | XBRL StockRepurchasedDuringPeriodShares |
| Shares held in employee trust (year-end) | 2026 / 2025 / 2024 | 37.7 / 14.6 / 22.9 | m | XBRL CommonStockSharesHeldInEmployeeTrustShares |
| Total assets | 31 Mar 2026 / 2025 | 33,259.8 / 24,781.1 | $m | 20F p. F-5 |
| Cash and cash equivalents (incl. customer funds) | 31 Mar 2026 / 2025 | 27,802.2 / 18,066.3 | $m | 20F p. F-5 |
| Cash and cash equivalents | 31 Mar 2024 / 2023 | 13,245.7 / 9,474.6 | $m | 20F p. F-7 |
| AFS debt securities (current) | 31 Mar 2026 / 2025 | 4,582.7 / 6,013.6 | $m | 20F p. F-5; Note 11 |
| Accounts receivable, net | 31 Mar 2026 / 2025 | 391.3 / 347.8 | $m | 20F p. F-5 |
| Prepaid expenses and other current assets | 31 Mar 2026 / 2025 | 185.4 / 103.6 | $m | 20F p. F-5 |
| Current tax assets | 31 Mar 2026 / 2025 | 19.0 / 19.4 | $m | 20F p. F-5 |
| PP&E, net (incl. operating-lease ROU assets — split owed, Note 9/10) | 31 Mar 2026 / 2025 | 189.9 / 150.8 | $m | 20F p. F-5 |
| Intangible assets, net (no goodwill line on the face) | 31 Mar 2026 / 2025 | 4.5 / 5.1 | $m | 20F p. F-5 |
| Other assets, noncurrent / deferred tax assets | 31 Mar 2026 | 27.4 / 57.4 | $m | 20F p. F-5 |
| Accounts payable and other current liabilities (Note 15) | 31 Mar 2026 / 2025 | 522.3 / 468.9 | $m | 20F p. F-5 |
| of which accounts payable trade / other accrued liabilities | 31 Mar 2026 / 2025 | 15.8 / 79.5 ; 21.7 / 86.3 | $m | XBRL AccountsPayableTradeCurrent; OtherAccruedLiabilitiesCurrent |
| Contract liabilities current / noncurrent | 31 Mar 2026 / 2025 | 22.5 / 21.9 ; 14.7 / 18.1 | $m | XBRL ContractWithCustomerLiabilityCurrent/Noncurrent |
| Funds payable and amounts due to customers (Note 16) | 31 Mar 2026 / 2025 | 30,254.2 / 22,279.9 | $m | 20F p. F-5; Note 16 |
| of which customer balances | 31 Mar 2026 / 2025 | 29,958.7 / 22,036.0 | $m | 20F Note 16 |
| of which outstanding money transmission liabilities | 31 Mar 2026 / 2025 | 295.5 / 243.9 | $m | 20F Note 16 |
| Current tax liabilities | 31 Mar 2026 / 2025 | 6.7 / 5.7 | $m | 20F p. F-5 |
| Short-term debt (RCF) | 31 Mar 2026 / 2025 | 6.0 / 128.4 | $m | 20F p. F-5; Note 17 |
| Long-term debt | 31 Mar 2026 / 2025 | 328.7 / 0.0 | $m | 20F p. F-5; Note 17 |
| Operating lease liabilities current / noncurrent | 31 Mar 2026 | 16.4 / 132.6 | $m | 20F p. F-5 |
| Operating lease liabilities current / noncurrent | 31 Mar 2025 | 13.4 / 97.1 | $m | 20F p. F-5 |
| Deferred tax liabilities / other long-term liabilities | 31 Mar 2026 / 2025 | 8.2 / 59.5 ; 5.4 / 44.9 | $m | 20F p. F-5 |
| Total liabilities | 31 Mar 2026 / 2025 | 31,334.6 / 23,043.7 | $m | 20F p. F-5 |
| Total shareholders' equity (no NCI) | 31 Mar 2026 / 2025 | 1,925.2 / 1,737.4 | $m | 20F p. F-5 |
| Total shareholders' equity | 31 Mar 2024 / 2023 | 1,165.1 / 673.0 | $m | XBRL StockholdersEquity |
| Treasury stock | 31 Mar 2026 / 2025 | 422.8 / 85.0 | $m | 20F p. F-5 |
| Class A shares issued and outstanding | 31 Mar 2026 / 2025 | 1,025,672,252 / 1,025,000,252 | shares | 20F p. F-5 |
| Class B shares issued and outstanding | 31 Mar 2026 / 2025 | 208,883,268 / 243,584,255 | shares | 20F p. F-5 |

**FY2016–FY2017 (CH17, TransferWise Ltd group, IFRS, £000; read from the scanned page images; PDF page = printed page):**

| item | FY | value | unit | source |
|---|---|---|---|---|
| Revenue | 2017 / 2016 | 67,010 / 27,852 | £000 | CH17 p. 12, consolidated statement of comprehensive income |
| Cost of sales | 2017 / 2016 | −20,947 / −12,441 | £000 | CH17 p. 12 |
| Administrative expenses | 2017 / 2016 | −46,119 / −32,784 | £000 | CH17 p. 12 |
| Operating loss (J1 candidate; the filer's "adjusted operating profit (EBITDA, non-GAAP)" 2,068 / −16,722 is never OI) | 2017 / 2016 | −56 / −17,373 | £000 | CH17 p. 12 |
| Amortisation and depreciation | 2017 / 2016 | 2,124 / 651 | £000 | CH17 p. 12 |
| Finance income / finance costs | 2017 | 5 / −287 | £000 | CH17 p. 12 |
| Finance costs | 2016 | −33 | £000 | CH17 p. 12 |
| Loss before tax | 2017 / 2016 | −338 / −17,406 | £000 | CH17 p. 12 |
| Income tax credit/(expense) | 2017 / 2016 | 6,993 / −168 | £000 | CH17 p. 12 |
| Profit/(loss) for the year | 2017 / 2016 | 6,655 / −17,574 | £000 | CH17 p. 12 |
| PP&E | 31 Mar 2017 / 2016 | 2,561 / 1,683 | £000 | CH17 p. 13, consolidated statement of financial position |
| Intangible assets | 31 Mar 2017 / 2016 | 8,102 / 3,788 | £000 | CH17 p. 13 |
| Long-term receivables / deferred tax asset | 31 Mar 2017 | 285 / 5,944 | £000 | CH17 p. 13 |
| Trade and other receivables | 31 Mar 2017 / 2016 | 40,208 / 7,612 | £000 | CH17 p. 13 |
| Cash and cash equivalents | 31 Mar 2017 / 2016 | 60,295 / 47,793 | £000 | CH17 p. 13 |
| Total assets | 31 Mar 2017 / 2016 | 117,395 / 60,876 | £000 | CH17 p. 13 |
| Trade and other payables (= total current liabilities = total liabilities) | 31 Mar 2017 / 2016 | 68,193 / 25,793 | £000 | CH17 p. 13 |
| Total equity (share premium 70,645 / 66,042; SBP reserve 2,096 / –; accumulated losses −24,564 / −31,219; CTD 1,025 / 260) | 31 Mar 2017 / 2016 | 49,202 / 35,083 | £000 | CH17 p. 13 |
| Cash generated from/(used in) operating activities | 2017 / 2016 | 16,745 / −9,381 | £000 | CH17 p. 17, consolidated statement of cash flows |
| Interest paid / income tax paid | 2017 | −287 / −148 | £000 | CH17 p. 17 |
| Interest paid / income tax paid | 2016 | −33 / −27 | £000 | CH17 p. 17 |
| Net cash from operating activities | 2017 / 2016 | 16,311 / −9,441 | £000 | CH17 p. 17 |
| Purchases of PP&E | 2017 / 2016 | −1,857 / −1,439 | £000 | CH17 p. 17 |
| Purchases of intangible assets | 2017 / 2016 | −5,604 / −3,028 | £000 | CH17 p. 17 |
| Interest received (investing) | 2017 | 5 | £000 | CH17 p. 17 |
| Proceeds from issue of shares | 2017 / 2016 | 4,603 / 14,688 | £000 | CH17 p. 17 |
| Cash at beginning of FY2016 (31 Mar 2015) | 2016 | 46,491 | £000 | CH17 p. 17 |
| CH17 page map | — | IS p. 12; group BS p. 13; parent BS p. 14; group SoCE p. 15; group CF p. 17; notes pp. 19–50 (financial-instrument and cash tables pp. 28–29; revenue and expense notes p. 31) | — | CH17 contact sheet, pp. 8–31 |

**Basis observation (CH17; to settle):** total assets of £117.4m at 31 Mar 2017 against cash of £60.3m, with no customer-funds line. In FY2016–FY2017, customer money held in safeguarding accounts was evidently **outside** the group balance sheet. By FY2025–FY2026 the 20-F carries it inside: cash of $27.8bn and funds payable of $30.3bn. The year the customer funds came onto the balance sheet, and whether Note 12 / Note 13 of the early years show safeguarded balances off balance sheet, decides the CE build per year. Without those balances there is nothing to net, and the early years' CE is the filer's own capital. Read CH17 note 12 (p. 28–29 area) and each later year's cash note.

**Segregated customer funds — the v4.8.0 inputs (20F Note 2, Note 11, Note 16):**

| item | FY | value | unit | source |
|---|---|---|---|---|
| Customer funds in segregated safeguarding bank accounts and term deposits (inside cash and cash equivalents) | 31 Mar 2026 / 2025 | 14,824.1 / 7,503.0 | $m | 20F Note 2, "Cash and Cash Equivalents" |
| Safeguarded customer deposits held in money-market funds | 31 Mar 2026 / 2025 | 7,592.1 / 7,034.4 | $m | 20F Note 2 |
| Safeguarded funds in "liquid, investment-grade fixed income securities, comprising government treasury bonds and highly-rated corporate paper" | 31 Mar 2026 / 2025 | 4,582.7 / 6,013.6 | $m | 20F Note 2 |
| AFS: U.S. government bonds (FV) | 31 Mar 2026 / 2025 | 1,272.8 / 1,689.0 | $m | 20F Note 11 |
| AFS: UK government bonds (FV) | 31 Mar 2026 / 2025 | 1,063.4 / 1,081.8 | $m | 20F Note 11 |
| AFS: other foreign bonds ("include foreign government and state bonds") (FV) | 31 Mar 2026 / 2025 | 1,695.5 / 2,526.8 | $m | 20F Note 11 |
| AFS: corporate debt securities (FV) | 31 Mar 2026 / 2025 | 551.0 / 716.0 | $m | 20F Note 11 |
| AFS by maturity: within one year / one to five years (FV; all types together) | 31 Mar 2026 | 3,630.4 / 952.3 | $m | 20F Note 11 |
| UK safeguarding via comparable guarantees (nine investment-grade sureties) | 31 Mar 2026 | 1,119.1 (£845.0) | $m | 20F Note 2 |
| AFS net realized gains/(losses) | 2026 / 2025 / 2024 | 7.6 / −42.5 / −3.7 | $m | 20F Note 11 |

**Gate 1C inputs found (partial):**

| item | FY | value | unit | source |
|---|---|---|---|---|
| Total compensation to NEDs, executive directors and executive officers as a group (salary, equity awards granted in the year, benefits; no bonuses) | 2026 | 18,178,159.51 | $ | 20F Item 6.B, p. 84 (translated at £1 = $1.32, the FY2026 average) |
| Chair fee (David Wells) | 2026 | 517 | $000 | 20F Item 6.B, NED table |
| NED fees (highest non-chair: Clare Gilmartin 245; Elizabeth Chambers 238; Terri Duhon 235; Hooi Ling Tan 225; Alastair Rampell 177) | 2026 | as listed | $000 | 20F Item 6.B, NED table |
| Buyback authorisation (amount) | 25 Jun 2026 | 500,000,000 | $ | XBRL srt StockRepurchaseProgramAuthorizedAmount1 |

The 20-F prints no per-person executive totals. The UK single total figure tables are in the directors' remuneration reports of CH24–CH26 (scanned). Those reports are the P17 source for FY2024–FY2026.

### Future, SF and Gate 2

Nothing beyond the inputs above was gathered. The prior's Appendix D and E are pointers only.

## 3. Readings settled (as far as the run got; figures in §2, no grade, no verdict)

1. **Lens: STD.** Wise is an e-money and payment institution group, the explicit STD case in MODEL §2 Lens; to confirm on CH26 that no consolidated bank capital ratio covers ≥ 90% of assets.
2. **Window: FY2017–FY2026, ten years.** The opening balance sheet is 31 Mar 2016, from CH17's comparatives. The audited group accounts exist and are published (CH17–CH26), so the prior's "listing-limited" 5-year window is a record-limited shortfall (MODEL §2·1A, label rule). It is not history-limited. FY2017–FY2021 are TransferWise Ltd's group accounts, the predecessor parent; Wise plc was inserted in 2021 and Wise Group plc on 8 May 2026 (20F Note 1). The basis question is owed: CH22–CH26 are UK IFRS (presentation currency to be read: GBP in the earlier years), while the 20-F is US GAAP in USD for FY2024–FY2026. The next run picks one basis for the whole window. One consistent IFRS series from CH17–CH26 is the likely route, with the 20-F as cross-check, and the currency translation is logged.
3. **Segregated customer funds (MODEL §2·1A, v4.8.0) — FY2025 and FY2026.**
   - Held safely and shown apart: the bank accounts and term deposits plus the MMFs. They total 22,416.2 (31 Mar 2026; 14,824.1 + 7,592.1) and 14,537.4 (31 Mar 2025; 7,503.0 + 7,034.4) (`derived`).
   - The securities net nothing. The note pools "government treasury bonds and highly-rated corporate paper". Note 11 gives the type split, but its maturity split (3,630.4 within a year) is for all types together, and "other foreign bonds" mixes government and state bonds. The rule needs government securities maturing within 12 months, so where the split is not shown nothing is netted (J13). The 4,582.7 / 6,013.6 stay in CE and are never cash.
   - Printed obligation: funds payable and amounts due to customers, 30,254.2 / 22,279.9.
   - N = the smaller of the two: 22,416.2 (FY2026) and 14,537.4 (FY2025) (`derived`). The excess obligation, 7,838.0 and 7,742.5 (`derived`), is not NIBCL and stays in L/E.
   - Float income: interest income is in revenue (InterestIncomeOperating), so it stays in OI and FCF. Interest on the non-netted securities is also booked in revenue, and it stays too: the securities are kept in CE, so it is not interest on the company's own cash.
   - CFO's line "funds payable and amount due to customers" (6,999.7 / 5,138.4 / 3,571.5) carries the movement of the netted pair, which leaves FCF in both directions. The part of the movement that relates to the non-netted excess also needs a reading; a per-year split is owed. The prior chain's own-cash ceiling (equity + own debt) is not a v4.8.0 reading.
4. **Indicative pointers (derived; not grades):**
   - CE_wc at 31 Mar 2026 ≈ 33,259.8 − 22,416.2 − (522.3 + 6.7) = 10,314.6, with an indicative NIBCL taken as the whole "accounts payable and other current liabilities" line plus current tax. The Note 15 split is owed and burden of proof applies.
   - OI ÷ that CE ≈ 5.7%.
   - L/E at 31 Mar 2026 ≈ (31,334.6 − 22,416.2) ÷ 1,925.2 = 463.2%; at 31 Mar 2025 ≈ (23,043.7 − 14,537.4) ÷ 1,737.4 = 489.6%.
   - These point to a Past reading far below the prior's ADEQUATE on 36% ROE: the ROE substitution is retired, ROCE is read on STD and L/E sits above P5. Only the rebuilt ten-year record decides.
5. **One segment.** No group build is expected.
6. **P17 basis.** The hairiest number must come from the UK single total figure tables (CH24–CH26 DRR). The 20-F prints only the group aggregate ($18.18m FY2026, NEDs included).

## 4. Scope still owed (in order)

- [ ] Read the scanned statements, rendering page images (`pdftoppm -r 110 -f N -l N`) and reading them, or with an attended OCR. For each year, read the income statement, the balance sheet, the cash-flow statement, the safeguarding/customer-funds note, and the PP&E and intangibles notes. FY2016 comes from CH17's comparatives. Record the PDF page of each figure.
- [ ] For each year FY2016–FY2026, take the safeguarding split: bank/term deposits, MMFs, government securities ≤ 12 months, other securities. Take the customer-balances obligation. Compute N per year, then CE_wc, CE_xc (own cash only: cash not segregated, never the funds) and L/E per year.
- [ ] Settle the J1 OI line per year: the IFRS operating profit in CH17–CH26 against the US GAAP operating income in the 20-F. Note the FY2024 restatement differences, and decide on the basis and currency.
- [ ] Settle the J3 items per year: other income/(loss) (20F Note 4: FY2026 69.7), AFS gains and losses, and interest on own cash, if the filer shows it apart.
- [ ] Build P20 for FY2017–FY2026 (constructed: k from net PP&E ex ROU plus capitalised software over revenue; UK CPI or US CPI deflators per the presentation currency; floor at PP&E depreciation). Then FCF = CFO − movement of the netted pair − maintenance capex, with the all-capex reading beside it.
- [ ] B1–B3 for ten years. Run the P31 test (no associates are expected; corporate debt securities in the safeguarded pool are not an S3 class while they back the customer obligation — settle and log). Run per-share growth on both reads, the J6 decline series, the L/E and P6 test, and both level-bar windows.
- [ ] Gate 0 sentence (v4.6.0 form) from CH26's strategic report.
- [ ] Gate 1B on v4.8.0: the paying customers (consumers and businesses; whether a customer statement exists), the forces, the moat (cost) and its direction from the take-rate cuts, and market growth.
- [ ] Gate 1C:
  - the P17 table for FY2024–FY2026 from the CH24–CH26 DRR single total figures (CEO Kristo Käärmann; CFO);
  - NED fees against the line;
  - RPT note;
  - P23 alignment, and votes versus economics: Class B 208,883,268 shares at 9 votes each against 1,025,672,252 Class A (20F p. F-5);
  - the July-2025 bundled resolution (prior's second flag);
  - point-of-purchase worth reads per tranche-year: FY2024 86.2, FY2025 92.5, FY2026 473.4 cash, plus the live £405m programme from 21 Jul 2026. The weekly 6-K "transaction in own shares" notices on EDGAR (CIK 2099039) give prices and volumes. Read each on the trailing-3-FY figures published before the tranche, and test the ≈ 1% floor per year;
  - the acquisition stop (no deals expected).
- [ ] Gate 2:
  - price in GBp on the LSE line (838.6 GBp on 2026-11-06; refresh);
  - the net share count at the latest balance sheet (Class A less treasury and trust shares);
  - EV no-cash with own debt 334.7 and the leases;
  - own cash for the all-cash variant: cash not in the segregated pool. Owed, because the 27,802.2 of cash holds the 22,416.2 netted funds and unsegregated balances; funds are never cash;
  - the P28 test on FY2026 (OI fell 728.2 → 590.7), the 3-year and 5-year readings, and the trigger at the no-cash bound in GBp at the ECB GBP/USD rate;
  - the H1 FY2027 interim (30 Sep 2026; expected mid-November 2026) if it is out by then.
- [ ] Every §6.1 machine field; Appendix G with a history line for v1–v3.

*Framework output, not investment advice.*
