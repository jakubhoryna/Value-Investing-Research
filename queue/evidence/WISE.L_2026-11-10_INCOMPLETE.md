# WISE.L — Wise Group plc — REVIEW resumable record (INCOMPLETE, second overrun) — 2026-11-10

## 1. Header

- Key: WISE.L · ISIN JE00BQKY0816 · job REVIEW · D 2026-11-10 · T 2112 · base sha 21c42fc144a1e484a13de0aefde720a0fe455239 · live `model_version` v4.8.0
- Prior memo: `memos/WISE.L/WISE.L_2026-08-06_GSC.md` (memo v3, `model_version` v4.1.0, no §6.1 machine fields). It is not moved.
- **Named gap: method re-test exceeds budget.** This is a **second overrun**: the run resumed the partial of 2026-11-06 (`queue/TODO.md` `▶ Method re-tests v4.8.0` line marked ` — partial 2026-11-06 (…)`), so the row carries `attended re-test owed`.
- resumes: `queue/evidence/WISE.L_2026-11-06_INCOMPLETE.md`. That record stays. Its item table (20-F FY2024–FY2026, US GAAP, USD; CH17 FY2016–FY2017) and its readings are not repeated here. **Read both records**, the earlier one first for the 20-F figures, then this one.
- No verdict, grade or trigger is recorded. Every figure is sourced to a primary document and a place in it, or labelled `derived`.

**What this run added.** The first run found only image-only Companies House scans for the pre-20-F years. This run found **text-layer copies of the audited IFRS group statements** in the London Stock Exchange RNS results announcements (served by Investegate). Those cover FY2021–FY2025, with the filer's own customer/corporate cash split. It also read the scanned FY2018–FY2020 statements (CH18, CH20) from the page images. With CH17 from the first record, the IFRS GBP series now covers **FY2017–FY2025**, plus the 31 Mar 2016 opening balance. FY2026 exists only in US GAAP USD (20-F; the FY2026 RNS is also US GAAP, line 1002 of the announcement), so the series has a basis break at FY2026. What is still owed (§4) did not fit this run's context budget.

**Why not finished.** The run ended under context pressure (README §5 time budget). Still owed: the FY2026 basis bridge, the P20 build, ten-year B1–B3, Gate 0 and Future on v4.6.0/v4.8.0, the P17 table from the scanned DRRs, point-of-purchase buyback reads and Gate 2. That is more than one more run held after a resume.

## 2. Item table — new figures (IFRS, £m unless stated; FY ends 31 Mar)

**Sources (primary, uncounted under P14):**
- RNS22 = "Wise plc FY22 results for year ended 31 March 2022", RNS via `https://www.investegate.co.uk/announcement/rns/wise-class-a--wise/wise-plc-fy22-results-for-year-ended-31-march-2022/7115103`. It carries the consolidated statements (the balance sheet is marked "unaudited") with FY2021 comparatives, the Note 15 cash table, Note 16 payables, Note 21 cash generated and a corporate cash-flow table.
- RNS23 = "Wise plc Preliminary Results FY end 31 March 2023", `…/wise-plc-preliminary-results-fy-end-31-march-2023-/7596407`: statements, Note 17 cash, Note 18 payables, Note 24 cash generated.
- RNS24 = "Wise plc Preliminary Results FY end 31 March 2024", `…/wise-plc-preliminary-results-fy-end-31-march-2024/8256893`: statements, Note 15 cash, Note 16 payables, Note 22 cash generated.
- RNS25 = "Results for the financial year ended 31 March 2025", `…/results-for-the-financial-year-ended-31-march-2025/8913542`: statements (FY2024 "re-presented"), Note 15 cash, Note 16 payables, Note 24, and the APM "Corporate cash" tables.
- RNS26 = "Wise FY26 results", `…/wise-fy26-results/9637901`: US GAAP (basis statement at the text's line 1002); not read further.
- NOTICE = "Notice of Results", `…/notice-of-results/9752729`: **H1 FY2027 results due 12 Nov 2026**, after the US close.
- CH18 = TransferWise Ltd group accounts FY2018 (first record's URL), image scan, 47 pp: IS p. 15, BS p. 16, CF p. 20, Note 12 p. 42, Note 13 p. 42, Note 14–15 p. 43.
- CH20 = TransferWise Ltd group accounts FY2020 (first record's URL), image scan, 69 pp: IS p. 33, BS p. 35, CF p. 43, Note 13–15 p. 65, Note 16 p. 66.
- Not yet read: CH19 (FY2019 notes; its FY2019 figures come from CH20's comparatives here) and CH21–CH26 (the RNS text covers their statements; the DRRs are needed for P17).

### Income statement

| item | FY | value | unit | source |
|---|---|---|---|---|
| Revenue | 2018 / 2017 restated | 117,283 / 66,328 | £000 | CH18 p. 15 (CH17 printed 2017 revenue 67,010, op. loss −56; CH18 restates both) |
| Operating profit/(loss) | 2018 / 2017 restated | 9,502 / (519) | £000 | CH18 p. 15 |
| Finance income / interest expenses | 2018 | 49 / (1,696) | £000 | CH18 p. 15 |
| Net profit | 2018 / 2017 | 6,244 / 6,192 | £000 | CH18 p. 15 |
| Revenue | 2020 / 2019 | 302.6 / 177.9 | £m | CH20 p. 33 |
| Investment and other income (inside OP; FY2019 restated) | 2020 / 2019 | 2.5 / 1.2 | £m | CH20 p. 33 |
| Operating profit | 2020 / 2019 | 21.8 / 12.0 | £m | CH20 p. 33 |
| Interest income / interest expenses (below OP) | 2020 / 2019 | 3.1 / (4.5) ; 0.2 / (2.1) | £m | CH20 p. 33 |
| Profit for the year | 2020 / 2019 | 21.3 / 10.3 | £m | CH20 p. 33 |
| Revenue | 2022 / 2021 | 559.9 / n/a here | £m | RNS23 IS (2022 col.); RNS22 IS |
| Interest income from investments and operating assets / interest expense from operating assets (inside OP) | 2022 / 2021 | 3.9 / (6.7) ; 1.9 / (3.8) | £m | RNS22 IS |
| Operating profit | 2022 / 2021 | 48.7 / 44.9 | £m | RNS22 IS |
| Profit before tax / profit for the year | 2022 / 2021 | 43.9 / 41.1 ; 32.9 / 30.9 | £m | RNS22 IS |
| Revenue | 2023 / 2024 / 2025 | 846.1 / 1,052.0 / 1,211.9 | £m | RNS24 IS; RNS25 IS |
| Interest income on customer balances (inside OP) | 2022 / 2023 / 2024 / 2025 | 3.9 / 140.2 / 485.2 / 594.3 | £m | RNS23 IS; RNS25 IS |
| Interest expense on customer balances | 2022 / 2023 | (6.7) / (3.7) | £m | RNS23 IS |
| Benefits paid relating to customer balances | 2023 / 2024 / 2025 | (18.4) / (124.9) / (161.2) | £m | RNS24 IS; RNS25 IS |
| Interest income from corporate investments (inside OP) | 2023 / 2024 / 2025 | 2.8 / 19.7 / 33.3 | £m | RNS24 IS ("net interest income from corporate investments"); RNS25 IS |
| Other operating income, net (inside OP) | 2023 / 2024 / 2025 | 10.7 / 5.7 / 7.1 | £m | RNS24 IS; RNS25 IS |
| Operating profit | 2023 / 2024 / 2025 | 157.2 / 501.9 / 579.6 | £m | RNS24 IS; RNS25 IS |
| Finance expense | 2023 / 2024 / 2025 | (10.7) / (20.5) / (15.5) | £m | RNS24 IS; RNS25 IS |
| Profit before tax | 2023 / 2024 / 2025 | 146.5 / 481.4 / 564.8 | £m | RNS24 IS; RNS25 IS |
| Profit for the year | 2023 / 2024 / 2025 | 114.0 / 354.6 / 416.7 | £m | RNS24 IS; RNS25 IS |
| Diluted EPS | 2023 / 2024 | 10.94 / 33.73 | pence | RNS24 IS |
| Depreciation and amortisation | 2018 / 2017 | 3,884 / 2,124 | £000 | CH18 Note 15 p. 43 |
| Depreciation and amortisation | 2020 / 2019 | 20.6 / 6.3 | £m | CH20 Note 16 p. 66 |
| Depreciation and amortisation | 2022 / 2023 / 2024 | 22.9 / 23.2 / 18.3 | £m | RNS23 Note 24; RNS24 Note 22 |
| Share-based payments (non-cash) | 2018 / 2020 / 2019 | 3,074 £000 / 24.4 / 7.0 | £m unless stated | CH18 Note 15; CH20 Note 16 |
| Share-based payments (non-cash) | 2022 / 2023 / 2024 | 42.2 / 58.2 / 72.5 | £m | RNS23 Note 24; RNS24 Note 22 |

J3 pointer, not settled: from FY2023 the filer books interest on customer balances (float income) inside operating profit. It stays in OI under v4.8.0, because float income reported as operating stays. "Interest income from corporate investments" (19.7 / 33.3) is the corporate cash yield: under J3 it is financial income on the company's own cash, and it goes out of OI. FY2019–FY2020 "investment and other income" (1.2 / 2.5) and the FY2021–FY2022 "interest income from investments and operating assets" need the same split.

### Balance sheet and the customer-funds inputs

| item | 31 Mar | value | unit | source |
|---|---|---|---|---|
| Total assets / total liabilities | 2018 / 2017 restated | 378,412 / 270,965 ; 128,396 / 79,737 | £000 | CH18 p. 16 (CH17 printed 2017 TA 117,395) |
| Equity | 2018 / 2017 | 107,447 / 48,659 | £000 | derived: TA − TL, CH18 p. 16 |
| Cash and cash equivalents (bank 253,025; transit between group accounts 18,638; transit to customers 29,586) | 2018 | 301,249 | £000 | CH18 Note 12 p. 42 |
| Cash and cash equivalents (bank 34,890; 5,422; 31,042) | 2017 restated | 71,354 | £000 | CH18 Note 12 p. 42 |
| Borderless accounts (customer balances) / outstanding money transmission liabilities / deferred customer liability | 2018 | 147,328 / 66,860 / 26,278 | £000 | CH18 Note 13 p. 42 |
| Borderless / OMTL / deferred customer liability | 2017 | 542 / 44,844 / 18,448 | £000 | CH18 Note 13 p. 42 |
| Borrowings (overdraft) | 2018 / 2017 | 20,226 / 11,001 | £000 | CH18 Note 14 p. 43 |
| PP&E / intangibles | 2018 / 2017 | 3,477 / 14,029 ; 2,561 / 8,102 | £000 | CH18 p. 16 |
| Total assets / total liabilities / equity | 2020 | 2,352.5 / 2,178.0 / 174.5 | £m | CH20 p. 35 |
| Total assets / total liabilities / equity | 2019 | 1,108.8 / 982.4 / 126.4 | £m | CH20 p. 35 |
| Cash (bank 1,933.2; transit between accounts 20.5; transit to customers 66.8; MMF 57.1) | 2020 | 2,077.6 | £m | CH20 Note 13 p. 65 |
| Cash (794.8; 26.2; 35.1; MMF –) | 2019 | 856.1 | £m | CH20 Note 13 p. 65 |
| Cash on safeguarding accounts ("protected from the Group insolvency, as a collateral to secure customer deposits") | 2020 / 2019 | 1,433.9 / 688.4 | £m | CH20 Note 13 p. 65 |
| Short-term financial investments (FVOCI) | 2020 / 2019 | 114.1 / 109.7 | £m | CH20 p. 35 |
| Borderless accounts / OMTL | 2020 | 1,967.3 / 118.0 | £m | CH20 Note 14 p. 65 |
| Borderless accounts / OMTL | 2019 | 829.5 / 122.4 | £m | CH20 Note 14 p. 65 |
| Borrowings: RCF 49.2, leases 14.6 (IFRS 16 from FY2020) | 2020 | 63.8 | £m | CH20 Note 15 p. 65 |
| Borrowings (RCF) | 2019 | 13.9 | £m | CH20 Note 15 p. 65 |
| PP&E (incl. ROU from FY2020) / intangibles | 2020 / 2019 | 19.1 / 21.3 ; 4.5 / 20.4 | £m | CH20 p. 35 |
| Total assets / total liabilities | 2022 / 2021 | 7,564.4 / 7,155.2 ; 4,301.8 / 4,016.5 | £m | RNS22 BS |
| Equity | 2022 / 2021 | 409.2 / 285.3 | £m | derived: TA − TL, RNS22 BS |
| Cash: MMF / transit to customers / total | 2022 | 282.9 / 154.6 / 6,056.3 | £m | RNS22 Note 15 |
| Cash: MMF / transit to customers / total | 2021 | 232.0 / 108.6 / 3,358.6 | £m | RNS22 Note 15 |
| Corporate cash (filer: "not related to customer funds") | 2022 / 2021 | 357.8 / 286.1 | £m | RNS22 Note 15 |
| Cash at bank in segregated, safeguarded accounts | 2022 / 2021 | 4,930.2 / 2,472.9 | £m | RNS22 Note 15 |
| Short-term financial investments (FVOCI bonds) | 2022 / 2021 | 1,192.4 / 737.5 | £m | RNS22 BS |
| Wise Accounts / OMTL | 2022 | 6,783.2 / 170.6 | £m | RNS22 Note 16 |
| Wise Accounts / OMTL | 2021 | 3,712.7 / 141.2 | £m | RNS22 Note 16 |
| Borrowings non-current / current | 2022 / 2021 | 90.2 / 5.5 ; 95.2 / 3.5 | £m | RNS22 BS |
| Total assets / total liabilities / equity | 2023 | 11,904.2 / 11,327.3 / 576.9 | £m | RNS24 BS |
| Total assets / total liabilities / equity | 2024 | 15,137.4 / 14,157.5 / 979.9 | £m | RNS24 BS |
| Total assets / total liabilities / equity | 2025 | 19,246.2 / 17,860.0 / 1,386.2 | £m | RNS25 BS |
| Cash: bank and in transit between accounts / MMF / transit to customers / total | 2023 | 4,827.8 / 2,669.6 / 182.0 / 7,679.4 | £m | RNS23 Note 17 |
| Cash: same split | 2024 | 6,570.3 / 3,776.1 / 132.8 / 10,479.2 | £m | RNS24 Note 15 (term deposits 285.8 inside bank) |
| Cash: same split | 2025 | 7,845.9 / 5,992.2 / 144.7 / 13,982.8 | £m | RNS25 Note 15 (term deposits 204.2 inside bank) |
| Corporate cash | 2023 / 2024 / 2025 | 671.1 / 1,061.1 / 1,430.2 | £m | RNS23 Note 17; RNS24 Note 15; RNS25 Note 15 |
| Segregated safeguarding bank accounts and term deposits | 2023 / 2024 / 2025 | 3,832.9 / 5,290.5 / 5,807.5 | £m | RNS23 Note 17; RNS24 Note 15; RNS25 Note 15 |
| Short-term financial investments (FVOCI; "treasury bonds and investment grade corporate paper", no type or maturity split in the RNS) | 2023 / 2024 / 2025 | 3,804.5 / 4,033.9 / 4,654.9 | £m | RNS24 BS; RNS25 BS |
| Wise Accounts | 2023 / 2024 / 2025 | 10,676.4 / 13,261.0 / 17,056.4 | £m | RNS23 Note 18; RNS24 Note 16; RNS25 Note 16 |
| OMTL | 2023 / 2024 | 191.3 / 235.9 | £m | RNS23 Note 18; RNS24 Note 16 |
| Filer's corporate cash bridge: cash + STFI 18,637.5 (14,513.2) + customer/processor receivables 209.6 (287.7) − OMTL and other customer payables 361.2 (479.4) − Wise customer accounts 17,055.7 (13,260.4) = corporate cash 1,430.2 (1,061.1) | 2025 (2024) | as listed | £m | RNS25 APM "Breakdown of corporate and customer cash" |
| Borrowings non-current / current; leases non-current / current | 2025 | 98.1 / 1.3 ; 75.9 / 10.3 | £m | RNS25 BS |

### Cash flow

| item | FY | value | unit | source |
|---|---|---|---|---|
| CFO excl. change on customer accounts (filer subtotal) | 2018 / 2017 | 22,789 / 2,987 | £000 | CH18 Note 15 p. 43 |
| Net cash inflow from customer-related balances | 2018 / 2017 | 169,765 / 13,702 | £000 | CH18 Note 15 p. 43 |
| Net cash from operating activities | 2018 / 2017 | 190,760 / 16,309 | £000 | CH18 p. 20 |
| PP&E purchases / intangible development payments | 2018 / 2017 | (2,316) / (8,749) ; (1,857) / (5,604) | £000 | CH18 p. 20 |
| Proceeds from issue of shares | 2018 | 49,782 | £000 | CH18 p. 20 |
| CFO excl. change on customer accounts (filer subtotal) | 2020 / 2019 | 40.9 / 19.7 | £m | CH20 Note 16 p. 66 |
| Net cash inflow from customer-related balances | 2020 / 2019 | 1,146.9 / 667.3 | £m | CH20 Note 16 p. 66 |
| Net cash from operating activities | 2020 / 2019 | 1,182.0 / 682.7 | £m | CH20 p. 43 |
| PP&E / intangibles purchases | 2020 / 2019 | (3.1) / (15.0) ; (2.3) / (11.3) | £m | CH20 p. 43 |
| Lease principal | 2020 | (4.1) | £m | CH20 p. 43 |
| Net cash from operating activities (IFRS) | 2022 / 2021 | 3,138.0 / 2,073.9 | £m | RNS22 CF |
| Increase in Wise Accounts (inside CFO) | 2022 / 2021 | 2,983.9 / 1,881.6 | £m | RNS22 Note 21 |
| Corporate net cash from operating activities (filer's corporate cash-flow table) | 2022 / 2021 | 72.1 / 136.4 | £m | RNS22 corporate cash table |
| PP&E / intangibles payments | 2022 / 2021 | (4.6) / (7.3) ; (2.3) / (20.9) | £m | RNS22 CF |
| Net cash from operating activities | 2023 / 2024 / 2025 | 3,919.9 / 3,248.9 / 4,494.4 | £m | RNS24 CF; RNS25 CF |
| Increase in Wise Accounts (inside CFO) | 2023 / 2024 / 2025 | 3,801.8 / 2,788.7 / 4,073.8 | £m | RNS24 Note 22; RNS25 Note 24 |
| PP&E / intangibles payments | 2023 / 2024 / 2025 | (3.6) / (5.2) ; (10.6) / (2.4) ; (34.5) / (0.9) | £m | RNS24 CF; RNS25 CF |
| Funding relating to share purchases and employee share schemes | 2023 / 2024 / 2025 | (10.1) / (68.4) / (72.6) | £m | RNS24 CF; RNS25 APM |
| Filer's "Free cash flow" (non-IFRS; a pointer, never the P20 figure) | 2024 / 2025 | 486.6 / 615.4 | £m | RNS25 APM corporate cash table |

## 3. Readings settled (inputs, not grades)

1. **Window: FY2017–FY2026** stands (the first record's reading 2). Basis: the **IFRS GBP series from FY2017 to FY2025 is now complete in primary sources.** FY2026 is US GAAP USD only (20-F; RNS26). The resuming run must either bridge FY2026 to IFRS (CH26 is Wise plc's statutory IFRS account to 31 Mar 2026 if it is IFRS: read its basis-of-preparation note) or read the whole window on one basis and log the translation. Use the restated FY2017 (CH18: OP −519, TA 128,396) over CH17's original figures.
2. **Customer funds came onto the balance sheet in FY2018.** At 31 Mar 2017 (restated), Borderless balances were 542 £000 against OMTL 44,844. By 31 Mar 2018 Borderless reached 147,328 and cash 301,249. The filer's own subtotal "CFO excluding change on customer accounts" exists for FY2017–FY2020 (CH18, CH20). For FY2021–FY2022 the corporate cash-flow table gives the same, and for FY2023–FY2025 the CFO less the increase in Wise Accounts and the customer-balance lines (Note 22/24) do. That is the v4.8.0 FCF basis: the netted pair's movement out, both directions.
3. **N per year (pointer, `derived`; reading (b): segregated bank + MMF, capped at the Wise Accounts obligation):** FY2021 2,704.9; FY2022 5,213.1; FY2023 6,502.5; FY2024 9,066.6; FY2025 11,799.7 (£m), against customer-related cash (cash − corporate cash) of 3,072.5 / 5,698.5 / 7,008.3 / 9,418.1 / 12,552.6. Counting the MMFs as segregated assumes they hold no corporate cash; the RNS does not split them. Burden of proof applies: the resuming run reads the annual report notes (CH21–CH25) for the MMF split, or nets the segregated bank balance alone (reading (a)). FY2019–FY2020: segregated 688.4 / 1,433.9 (+ MMF 57.1 in FY2020). FY2018: no safeguarding figure was seen in Note 12; read CH18's financial-risk note (p. 31) and the strategic report.
4. **Crude pointers on reading (b) (`derived`, total assets − N, no NIBCL, OI untouched by J3):** OP ÷ (TA − N) ≈ 2.8% FY2021, 2.1% FY2022, 2.9% FY2023, 8.3% FY2024, 7.8% FY2025; (TL − N) ÷ equity ≈ 460%, 475%, 836%, 520%, 437%. The first record's FY2026 pointers were ≈ 5.7% and 463%. These do not decide anything, but every pointer sits well below the prior's ADEQUATE (36% ROE) and the P5 leverage line. The STFI bond pools stay in CE and are never cash, and they dominate the denominator.
5. **H1 FY2027 lands 12 Nov 2026** (NOTICE). The resuming run takes it into Gate 2 (latest balance sheet: net share count, own debt, own cash) and the TTM.

## 4. Scope still owed (in order) — attended re-test

- [ ] FY2026 basis: read CH26's basis-of-preparation note (IFRS or US GAAP), or bridge 20-F FY2026 to the IFRS series; decide the window's basis and currency (`core_currency`, `core_fx`).
- [ ] The MMF split per year (CH21–CH25 annual report notes on safeguarding), or settle on reading (a). FY2018 safeguarding (CH18 p. 31 or the strategic report). NIBCL per year from the payables notes (accrued expenses, accounts payable, deferred revenue, tax).
- [ ] J3 per year: take interest income from corporate investments out of OI (FY2023 2.8, FY2024 19.7, FY2025 33.3); split the earlier "investment and other income" lines (CH19 and RNS22 notes).
- [ ] P20: k from (PP&E ex ROU + capitalised software) ÷ revenue; CPI deflators; the depreciation floor. FCF = filer's CFO excl. customer accounts − maintenance capex, with the all-capex reading beside it; leases after IFRS 16 (FY2020+) as debt-equivalents.
- [ ] B1–B3, FY2017–FY2026, with the 2016 opening balance; both growth reads (per diluted share: CH17–CH20 share counts are preferred + ordinary, so read the share notes, e.g. CH20 Note 17: 35,661,560 shares pre-split); J6; L/E and P6; the P31 test (expected: no G6 class above the line; the bond pool backs customer obligations — log it).
- [ ] Gate 0 sentence (v4.6.0 form) and Gate 1B on v4.8.0 (paying customers, the customer statement, forces, moat and its direction after the take-rate cuts, market growth).
- [ ] Gate 1C: the P17 table from the CH24–CH26 DRR single-total figures (scans); NED fees; RPT; P23 and votes versus economics (Class B 208,883,268 at 9 votes against Class A 1,025,672,252, 20-F p. F-5); the bundled July-2025 resolution; point-of-purchase worth reads for the FY2024–FY2026 tranches and the £405m programme from 21 Jul 2026 (EDGAR 6-K "transaction in own shares", CIK 2099039); the ≈ 1% floor per year; the acquisition stop.
- [ ] Gate 2 on the H1 FY2027 balance sheet (12 Nov 2026): price GBp on the LSE line (endpoint WISE.L); net count; EV no-cash with own debt and leases; own cash = corporate cash (never customer funds); the P28 test (US GAAP OI 728.2 → 590.7 in FY2026); the 3-year and 5-year reads; the trigger at the no-cash bound.
- [ ] Every §6.1 machine field; Appendix G with history lines for v1–v3 and `resumed from partial 2026-11-06` plus this record.

*Framework output, not investment advice.*
