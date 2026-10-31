# BABA — Alibaba Group Holding Limited — INCOMPLETE evidence, resumable record (REVIEW 2026-10-31)

## 1. Header

- Key: BABA · job: REVIEW · D 2026-10-31 · T 1121 · base sha 4bad5c07b7757d2b2ec19f602df2bc642fd9730a
- Live `model_version`: v4.8.0
- Prior memo: `memos/BABA/BABA_2026-10-06_GSC.md` (memo v2, `model_version` v4.4.1; no §6.1 machine fields, no `lens`, no group build)
- Named gap: **method re-test exceeds budget** (README §5; MODEL §8.7 item 6). This is the **second overrun**: the run resumed the partial of 2026-10-27.
- resumes: `queue/evidence/BABA_2026-10-27_INCOMPLETE.md` (kept beside this record; the memo that lands deletes both)
- No verdict, grade or band is stated here. No price GET was made (no memo is written).

## 2. Per gate or leg — work done and figures

Work this run: re-read the 2026-10-27 record; pulled the SEC companyfacts and submissions JSON again; fetched and read the FY2026 and FY2023 20-F face statements and Note 11. That closes the 2026-10-27 record's open item "20-F equity-method result FY2021–FY2026" and adds the FYE2022–FYE2026 investment-class carrying values, the FY2024–FY2026 cash-flow lines and the FYE2025–FYE2026 balance sheet. Figures from the 2026-10-27 record cite companyfacts by concept only, with no accession. A resuming run carries them as orientation and re-derives them from the 20-F face statements (README §5 Resume).

All figures are RMB m, fiscal years end 31 March. Source keys:
- `20-F FY2026` = accession 0001193125-26-231755, `baba-20260331.htm`, filed 2026-05-20
- `20-F FY2023` = accession 0000950170-23-033752, `baba-20230331.htm`, filed 2023-07-21
- `20-F FY2020` = accession 0001104659-20-082409 (XBRL fact, companyfacts `IncomeLossFromEquityMethodInvestments`)
- `20-F FY2019` = accession 0001047469-19-003492 (XBRL fact, same concept)

### Gate 1A — the equity-method class (G6 / P31)

| item | FY | value | unit | source |
|---|---|---|---|---|
| Share of results of equity method investees | FY2017 | -5,027 | RMB m | 20-F FY2019 XBRL `IncomeLossFromEquityMethodInvestments` |
| Share of results of equity method investees | FY2018 | -20,792 | RMB m | 20-F FY2020 XBRL, same concept |
| Share of results of equity method investees | FY2019 | 566 | RMB m | 20-F FY2020 XBRL, same concept |
| Share of results of equity method investees | FY2020 | -5,733 | RMB m | 20-F FY2020 XBRL, same concept |
| Share of results of equity method investees | FY2021 | 6,984 | RMB m | 20-F FY2023, Item 5 results-of-operations table (p. 129) |
| Share of results of equity method investees | FY2022 | 14,344 | RMB m | 20-F FY2023, Item 5 results table (p. 129) |
| Share of results of equity method investees | FY2023 | -8,063 | RMB m | 20-F FY2023, Item 5 results table (p. 129) |
| Share of results of equity method investees | FY2024 | -7,735 | RMB m | 20-F FY2026, consolidated income statements (F-5) |
| Share of results of equity method investees | FY2025 | 5,966 | RMB m | 20-F FY2026, F-5 |
| Share of results of equity method investees | FY2026 | 2,785 | RMB m | 20-F FY2026, F-5 |
| Investments in equity method investees | FYE2022 | 219,642 | RMB m | 20-F FY2023, consolidated balance sheets (F-6) |
| Investments in equity method investees | FYE2023 | 207,380 | RMB m | 20-F FY2023, F-6 |
| Investments in equity method investees | FYE2025 | 210,169 | RMB m | 20-F FY2026, consolidated balance sheets (F-7) |
| Investments in equity method investees | FYE2026 | 206,803 | RMB m | 20-F FY2026, F-7 |
| Disposals of and distributions from equity method investees (investing; dividends not split out) | FY2024 · FY2025 · FY2026 | 1,265 · 1,520 · 5,627 | RMB m | 20-F FY2026, consolidated statements of cash flows (F-12) |

### Gate 1A — the S3 / securities class (Note 11, carrying values)

| item | FY | value | unit | source |
|---|---|---|---|---|
| Listed equity securities | FYE2022 · FYE2023 | 103,260 · 107,751 | RMB m | 20-F FY2023, Note 11 (F-52) |
| Investments in privately held companies | FYE2022 · FYE2023 | 109,237 · 87,037 | RMB m | 20-F FY2023, Note 11 (F-52) |
| Debt securities and loan investments | FYE2022 · FYE2023 | 19,787 · 15,105 | RMB m | 20-F FY2023, Note 11 (F-52) |
| Other treasury investments | FYE2023 | 40,736 | RMB m | 20-F FY2023, Note 11 (F-52) |
| Note 11 total | FYE2022 · FYE2023 | 232,284 · 250,629 | RMB m | 20-F FY2023, Note 11 (F-52) |
| Listed equity securities | FYE2025 · FYE2026 | 77,630 · 100,594 | RMB m | 20-F FY2026, Note 11 (F-54) |
| Investments in privately held companies | FYE2025 · FYE2026 | 96,167 · 130,447 | RMB m | 20-F FY2026, Note 11 (F-54) |
| Debt securities and loan investments | FYE2025 · FYE2026 | 8,785 · 10,880 | RMB m | 20-F FY2026, Note 11 (F-54) |
| Other treasury investments | FYE2025 · FYE2026 | 228,016 · 238,075 | RMB m | 20-F FY2026, Note 11 (F-54) |
| Note 11 total | FYE2025 · FYE2026 | 410,598 · 479,996 | RMB m | 20-F FY2026, Note 11 (F-54) |
| Net unrealised gains (losses) incl. impairment, equity securities still held, in interest and investment income | FY2021 · FY2022 · FY2023 | 45,139 · -25,587 · -29,481 | RMB m | 20-F FY2023, Note 11 (F-52) |
| Same | FY2024 · FY2025 · FY2026 | -28,790 · 16,746 · 56,295 | RMB m | 20-F FY2026, Note 11 (F-54) |
| Measurement-alternative carrying value (privately held) | FYE2025 · FYE2026 | 88,728 · 124,979 | RMB m | 20-F FY2026, Note 11 (F-54) |

### Income statement, OI line and financial items

| item | FY | value | unit | source |
|---|---|---|---|---|
| Revenue | FY2021 · FY2022 · FY2023 | 717,289 · 853,062 · 868,687 | RMB m | 20-F FY2023, Item 5 results table (p. 129) |
| Income from operations | FY2021 · FY2022 · FY2023 | 89,678 · 69,638 · 100,351 | RMB m | 20-F FY2023, Item 5 results table (p. 129) |
| Interest and investment income, net | FY2021 · FY2022 · FY2023 | 72,794 · -15,702 · -11,071 | RMB m | 20-F FY2023, Item 5 results table (p. 129) |
| Interest expense | FY2021 · FY2022 · FY2023 | -4,476 · -4,909 · -5,918 | RMB m | same |
| Other income, net | FY2021 · FY2022 · FY2023 | 7,582 · 10,523 · 5,823 | RMB m | same |
| Revenue | FY2024 · FY2025 · FY2026 | 941,168 · 996,347 · 1,023,670 | RMB m | 20-F FY2026, F-5 |
| Other gains, net (inside income from operations) | FY2024 · FY2025 · FY2026 | — · 761 · 1,848 | RMB m | 20-F FY2026, F-5 |
| Income from operations | FY2024 · FY2025 · FY2026 | 113,350 · 140,905 · 50,150 | RMB m | 20-F FY2026, F-5 |
| Interest and investment income, net | FY2024 · FY2025 · FY2026 | -9,964 · 20,759 · 87,512 | RMB m | 20-F FY2026, F-5 |
| Interest expense | FY2024 · FY2025 · FY2026 | -7,947 · -9,596 · -9,793 | RMB m | 20-F FY2026, F-5 |
| Other income, net | FY2024 · FY2025 · FY2026 | 6,157 · 3,387 · 1,518 | RMB m | 20-F FY2026, F-5 |
| Diluted weighted-average shares | FY2024 · FY2025 · FY2026 | 20,359 · 19,318 · 19,235 | m shares | 20-F FY2026, F-5 |
| Gain on disposals of property and equipment (CFO adjustment; matches "Other gains, net" in FY2026) | FY2024 · FY2025 · FY2026 | -107 · -784 · -1,848 | RMB m | 20-F FY2026, F-12 |

### Cash flow (P20, FCF)

| item | FY | value | unit | source |
|---|---|---|---|---|
| Net cash provided by operating activities | FY2024 · FY2025 · FY2026 | 182,593 · 163,509 · 76,213 | RMB m | 20-F FY2026, F-12 |
| Acquisitions of land use rights, property and equipment | FY2024 · FY2025 · FY2026 | -32,087 · -85,972 · -126,063 | RMB m | 20-F FY2026, F-12 |
| Acquisitions of intangible assets | FY2024 · FY2025 · FY2026 | -842 · — · -874 | RMB m | 20-F FY2026, F-12 |
| Depreciation and impairment of PP&E, and operating lease cost relating to land use rights | FY2024 · FY2025 · FY2026 | 26,640 · 29,260 · 37,067 | RMB m | 20-F FY2026, F-12 (P20 floor needs the depreciation alone, from Note 15) |
| Repurchase of ordinary shares (cash) | FY2024 · FY2025 · FY2026 | -88,745 · -86,662 · -7,638 | RMB m | 20-F FY2026, F-12 |
| Dividend distribution | FY2024 · FY2025 · FY2026 | -17,946 · -29,077 · -33,732 | RMB m | 20-F FY2026, F-12 |
| Repurchase and retirement of ordinary shares (shares) | FY2024 · FY2026 | 1,249,196,660 · 72,733,488 | shares | 20-F FY2026, statements of changes in equity (F-9, F-11) |

### Balance sheet FYE2025 · FYE2026 (CE, Gate 2)

| item | FY | value | unit | source |
|---|---|---|---|---|
| Cash and cash equivalents | FYE2025 · FYE2026 | 145,487 · 131,530 | RMB m | 20-F FY2026, F-7 |
| Short-term investments | FYE2025 · FYE2026 | 228,826 · 155,310 | RMB m | 20-F FY2026, F-7 |
| Restricted cash and escrow receivables | FYE2025 · FYE2026 | 43,781 · 42,038 | RMB m | 20-F FY2026, F-7 |
| Equity securities and other investments, current | FYE2025 · FYE2026 | 53,780 · 30,054 | RMB m | 20-F FY2026, F-7 |
| Equity securities and other investments, non-current | FYE2025 · FYE2026 | 356,818 · 449,942 | RMB m | 20-F FY2026, F-7 |
| Property and equipment, net | FYE2025 · FYE2026 | 203,348 · 282,699 | RMB m | 20-F FY2026, F-7 |
| Intangible assets, net | FYE2025 · FYE2026 | 20,911 · 16,983 | RMB m | 20-F FY2026, F-7 |
| Goodwill | FYE2025 · FYE2026 | 255,501 · 247,378 | RMB m | 20-F FY2026, F-7 |
| Total assets | FYE2025 · FYE2026 | 1,804,227 · 1,909,570 | RMB m | 20-F FY2026, F-7 |
| Current bank borrowings | FYE2025 · FYE2026 | 22,562 · 28,224 | RMB m | 20-F FY2026, F-7 |
| Income tax payable | FYE2025 · FYE2026 | 11,638 · 10,630 | RMB m | 20-F FY2026, F-7 |
| Accrued expenses, accounts payable and other liabilities | FYE2025 · FYE2026 | 332,537 · 359,893 | RMB m | 20-F FY2026, F-7 (Note 19 split owed: it may carry debt-like items) |
| Merchant deposits | FYE2025 · FYE2026 | 274 · 236 | RMB m | 20-F FY2026, F-7 |
| Deferred revenue and customer advances (current) · deferred revenue (non-current) | FYE2026 | 77,415 · 4,885 | RMB m | 20-F FY2026, F-7 |
| Non-current bank borrowings · unsecured senior notes · convertible notes · exchangeable bonds | FYE2026 | 47,450 · 117,485 · 55,861 · 10,976 | RMB m | 20-F FY2026, F-7 |
| Total liabilities | FYE2025 · FYE2026 | 714,121 · 783,300 | RMB m | 20-F FY2026, F-7 |
| Mezzanine equity | FYE2025 · FYE2026 | 11,713 · 7,845 | RMB m | 20-F FY2026, F-8 |
| Total shareholders' equity (excl. NCI) | FYE2025 · FYE2026 | 1,009,858 · 1,060,886 | RMB m | 20-F FY2026, F-8 |
| Noncontrolling interests | FYE2025 · FYE2026 | 68,535 · 57,539 | RMB m | 20-F FY2026, F-8 |
| Shares issued and outstanding | FYE2026 | 18,580,374,278 | shares | 20-F FY2026, F-8 |
| Total assets · total liabilities | FYE2022 · FYE2023 | 1,695,553 · 1,753,044 · 613,360 · 630,123 | RMB m | 20-F FY2023, F-6 |

## 3. Readings settled (inputs only, never grades)

- **P31.** The equity-method class alone is above 5% of total assets at every date the two records cite (10.8%–16.8%). With the Note 11 equity securities, the summed classes are about 22.9% of FYE2026 total assets (206,803 + 100,594 + 130,447 = 437,844 of 1,909,570, derived; the S2/H/S3 split of the listed securities is still owed). The income limb fails too: the FY2022 equity-method result of 14,344 is 20.6% of that year's OI of 69,638 (derived). Both G6 readings are owed over the whole window.
- **Include-reading cash.** The FY2024–FY2026 cash-flow statement carries equity-method distributions only inside an investing line that mixes them with disposals. Under J13 nothing is moved into CFO unless the 20-F splits them, and the 2026-10-27 record's XBRL dividend figures need a location in the 20-F before they are used.
- **J1 / J3 pointer.** From FY2025 "income from operations" includes "Other gains, net" (761; 1,848). In FY2026 that equals the CFO add-back for gains on PP&E disposals. Whether it is operating (it stays in) or a disposal gain on a business or stake (J3: it leaves) is open.
- **Shares.** The FY2026 cash buyback is 7,638 against 88,745 in FY2024 and 86,662 in FY2025. Each tranche-year needs its point-of-purchase reads (v4.8.0), on the trailing 3-FY averages published before it.

## 4. Scope still owed (attended run, in order)

- [ ] The FY2025 20-F (0000950170-25-090161) and FY2022 20-F (0001104659-22-082622) face statements and Note 11, for FYE2021 and FYE2024; FY2017–FY2021 20-Fs for FYE2016–FYE2021 balance sheets and Note 11 carrying values (B1 from primary documents; the prior's FY2022–26 series is tier-2).
- [ ] The interest-and-investment-income note, per year: interest income on own cash and securities, dividends, fair-value changes, disposal gains. Then the G6 include and exclude readings: B2 per-year series and summary rows on both readings, the harsher governing; ΔOI/sh and ΔFCF/sh on both readings, with read (ii) where read (i) is n.m.
- [ ] Classify Note 11: listed equity securities into S2, H (material listed holdings, P22) or S3; privately held companies are S3; other treasury investments into S1 or S2 if cash-like. Gate 2 cash variants.
- [ ] P20 constructed: Note 15 depreciation alone; k over the window; PRC CPI deflators with the 3% floor; tier 3 in deal years above 1% of EV without an organic split.
- [ ] Group build on the FY2026 segments (Alibaba China E-commerce Group; Cloud Intelligence Group; All others, described by its parts). Unit Future blocks, the R7 breadth reads and the v4.8.0 unit statement. B4 weights (P29). Materiality of the controlled listed subsidiaries (P22). The §2·1C·3 allocation table.
- [ ] Gate 1C on the live rules: Item 6 director and executive pay (R9, V3, the director cap); P23 and the Alibaba Partnership under votes versus economics; RPT (Ant Group); the worth test with v4.8.0 point-of-purchase reads and the per-year floor for FY2022–FY2026; the acquisition stop for FY2025–FY2026 deals with the v4.8.0 deal proxy.
- [ ] Gate 2: the latest interim balance sheet (6-K, Sep-quarter 2026 if published), debt-equivalents (NCI at the higher of market and book for listed subsidiaries), no-cash trigger (R10), P28, 3-year and 5-year readings; one GET to the price endpoint `BABA` (USD) and the ECB CNY/USD rate.
- [ ] ISIN from a primary source (backfill owed since memo v2); machine fields per MODEL §6.1.

*Framework output, not investment advice.*
