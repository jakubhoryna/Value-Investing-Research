# BSL.DE — INCOMPLETE evidence record (ANALYSE 2026-11-06 2303)

## 1. Header

- **Key:** BSL.DE — Basler AG (Aktiengesellschaft), Ahrensburg, Germany. ISIN DE0005102008 (from the EQS document names `DE0005102008-JA-{year}` and the newswire pages found; the annual report body was not searched for it).
- **Job:** ANALYSE · D 2026-11-06 · T 2303 (Europe/Prague) · base sha 25fdced2566a8f7a9ae94b8fd7a759087c2755b4 · live `model_version` v4.8.0.
- **Prior memo:** none (no `memos/BSL.DE/` or `archive/memos/BSL.DE/`; no memo, register row or pending row matches "Basler" or DE0005102008).
- **Named gap:** `INCOMPLETE (data access: FY2016–FY2017 and FY2023 statements)`. This is a data-access gap, not a budget gap. The full IFRS statements for FY2016 and FY2017, the FY2015 closing balance sheet (the window's opening balance sheet) and the FY2023 income and cash-flow statements exist in Basler's annual reports 2016, 2017 (or 2018) and 2023 (or 2024). None of them was retrievable this run (section 4). Without them the P1 window (FY2016–FY2025, 11 balance sheets) cannot be built, and the D3 gate (routines/README.md §5) forbids a record-limited memo where more years are published.
- **No verdict.** Nothing below is a grade, a trigger or a verdict.

## 2. Figures sourced this run

Price endpoint: `query1.finance.yahoo.com/v8/finance/chart/BSL.DE` — currency EUR, exchangeName GER (Xetra), "Basler Aktiengesellschaft", close 23.70 on 2026-11-06. Splits: 3:1 on 2019-06-25 and 3:1 on 2022-07-19 (`events=split`). Per-share series before each split need restating (×3 per split); the AR2022 share counts are already post-split.

Documents (all primary, retrieved 2026-11-06; uncounted under P14):
- **AR2025** — "Annual Report 2025" (English), assets-ctf.baslerweb.com `…/0AnfMesaOHzNvPM9qnxCv/…/Geschäftsbericht_2025_Basler-AG_final_EN.pdf` (filename with a decomposed "ä"; curl got HTTP 403 on every spelling tried, WebFetch on the search-result URL returned the 139-page PDF). FY2025, FY2024 restated (IAS 8: building leases, treasury-share accounting) and the 1 Jan 2024 balance sheet.
- **AR2022 (DE)** — "Geschäftsbericht 2022", hauptversammlung.de `/fileadmin/public/user_upload/Basler_AG_HV_2023_Geschaeftsbericht.pdf`. FY2022 and FY2021 (FY2021 restated under IAS 8.42, note 3.12.2).
- **AR2020** — "Basler Annual Report 2020", irpages2.eqs.com `/Download/Companies/basler/Annual%20Reports/DE0005102008-JA-2020-EQ-E-01.pdf` (redirects to ir-api.eqs.com). FY2020 and FY2019.
- **AR2019** — "Annual Report 2019", assets-ctf.baslerweb.com `…/5xLU0YlYWNr1AUMATahqWj/…/IR_Financial_Reports_2019_annual_report_open.pdf`. FY2019 and FY2018; key-figure table carries FY2017.
- **Pres2025** — "Annual Report 2025" results presentation of 31 Mar 2026, assets-ctf.baslerweb.com `…/2XPjHAr01mrY20FNWI05yg/…/20260331_Annual_Report_2025_final.pdf` (31 slides; context only).

| item | FY | value | unit | source |
|---|---|---|---|---|
| Sales revenues | FY2025 | 224,537 | EUR k | AR2025, consolidated income statement |
| Sales revenues | FY2024 | 183,715 | EUR k | AR2025, consolidated income statement (adjusted) |
| Operating result | FY2025 | 17,691 | EUR k | AR2025, consolidated income statement |
| Operating result | FY2024 | -10,079 | EUR k | AR2025, consolidated income statement (adjusted) |
| Currency earnings (inside gross profit) | FY2025 / FY2024 | -2,767 / 1,211 | EUR k | AR2025, consolidated income statement |
| Equity-method profit share | FY2025 / FY2024 | 45 / -345 | EUR k | AR2025, consolidated income statement (below the operating result) |
| Impairment on equity-method investments | FY2025 / FY2024 | -381 / -724 | EUR k | AR2025, consolidated income statement (below the operating result) |
| Financial income / expenses | FY2025 | 370 / -1,494 | EUR k | AR2025, consolidated income statement |
| Consolidated net income | FY2025 / FY2024 | 11,632 / -14,200 | EUR k | AR2025, consolidated income statement |
| Average shares (diluted = basic) | FY2025 / FY2024 | 30,746,474 / 30,740,144 | shares | AR2025, consolidated income statement |
| Total assets | 31 Dec 2025 / 31 Dec 2024 / 1 Jan 2024 | 238,055 / 230,334 / 253,162 | EUR k | AR2025, consolidated balance sheet |
| Cash in bank and cash in hand | 31 Dec 2025 / 31 Dec 2024 / 1 Jan 2024 | 28,994 / 21,323 / 32,228 | EUR k | AR2025, consolidated balance sheet |
| Goodwill | 31 Dec 2025 / 31 Dec 2024 / 1 Jan 2024 | 46,075 / 49,431 / 45,790 | EUR k | AR2025, consolidated balance sheet |
| Intangible assets | 31 Dec 2025 / 31 Dec 2024 / 1 Jan 2024 | 39,286 / 41,152 / 44,304 | EUR k | AR2025, consolidated balance sheet |
| Equity-method investments | 31 Dec 2025 / 31 Dec 2024 / 1 Jan 2024 | 0 / 336 / 1,786 | EUR k | AR2025, consolidated balance sheet (note 31) |
| Equity (no NCI) | 31 Dec 2025 / 31 Dec 2024 / 1 Jan 2024 | 132,854 / 123,886 / 139,083 | EUR k | AR2025, consolidated balance sheet |
| Liabilities to banks, non-current + current | 31 Dec 2025 | 34,672 + 11,821 | EUR k | AR2025, consolidated balance sheet |
| Liabilities to banks, non-current + current | 31 Dec 2024 | 44,244 + 8,256 | EUR k | AR2025, consolidated balance sheet |
| Lease liabilities, non-current + current | 31 Dec 2025 / 31 Dec 2024 | 16,164 + 2,814 / 14,462 + 2,630 | EUR k | AR2025, consolidated balance sheet |
| Trade payables | 31 Dec 2025 / 31 Dec 2024 / 1 Jan 2024 | 19,507 / 13,869 / 14,672 | EUR k | AR2025, consolidated balance sheet |
| Current income tax liabilities | 31 Dec 2025 / 31 Dec 2024 | 2,763 / 5,028 | EUR k | AR2025, consolidated balance sheet |
| Other non-financial liabilities (current) | 31 Dec 2025 / 31 Dec 2024 | 5,795 / 8,469 | EUR k | AR2025, consolidated balance sheet (note 28; composition not yet read) |
| Net cash flow from operating activities (after tax paid) | FY2025 / FY2024 | 30,129 / 16,333 | EUR k | AR2025, consolidated cash-flow statement |
| Capex: tangible + intangible payments | FY2025 | 1,540 + 8,726 | EUR k | AR2025, consolidated cash-flow statement |
| Capex: tangible + intangible payments | FY2024 | 1,401 + 9,321 | EUR k | AR2025, consolidated cash-flow statement |
| Interest paid in financing (loans + lease interest) | FY2025 | 738 + 835 | EUR k | AR2025, consolidated cash-flow statement (to move into CFO, §2·1A) |
| Interest paid in financing (loans + lease interest) | FY2024 | 1,067 + 754 | EUR k | AR2025, consolidated cash-flow statement |
| Acquisition of subsidiaries / associates | FY2024 | 2,996 / 1,177 | EUR k | AR2025, consolidated cash-flow statement |
| Treasury-share purchases / dividends paid | FY2025 | 0 / 0 | EUR k | AR2025, IAS 7 reconciliation |
| Sales revenues | FY2022 / FY2021 | 272,203 / 214,728 | EUR k | AR2022 (DE), Konzern-Gewinn- und Verlustrechnung |
| Operatives Ergebnis | FY2022 / FY2021 (restated) | 28,930 / 28,563 | EUR k | AR2022 (DE), Konzern-GuV (FY2021 as reported: 28,361) |
| Equity-method profit share | FY2022 | 156 | EUR k | AR2022 (DE), Konzern-GuV |
| Konzernjahresüberschuss | FY2022 / FY2021 (restated) | 21,362 / 21,001 | EUR k | AR2022 (DE), Konzern-GuV |
| Average shares (diluted = basic, post-2022 split) | FY2022 / FY2021 | 29,878,360 / 29,913,693 | shares | AR2022 (DE), Konzern-GuV |
| Mittelzufluss aus betrieblicher Tätigkeit | FY2022 / FY2021 | 12,402 / 25,333 | EUR k | AR2022 (DE), Kapitalflussrechnung |
| Investitionen in das Anlagevermögen | FY2022 / FY2021 | 29,974 / 15,726 | EUR k | AR2022 (DE), Kapitalflussrechnung |
| Akquisitionen abzüglich übernommener Zahlungsmittel | FY2022 | 14,497 | EUR k | AR2022 (DE), Kapitalflussrechnung |
| Bilanzsumme | 31 Dec 2022 / 31 Dec 2021 (restated) | 265.5 / 227.3 | EUR m | AR2022 (DE), Unternehmenskennzahlen (statement figures owed) |
| Eigenkapital | 31 Dec 2022 / 31 Dec 2021 | 141.5 / 128.7 | EUR m | AR2022 (DE), Unternehmenskennzahlen |
| Sales revenues | FY2020 / FY2019 | 170,459 / 161,961 | EUR k | AR2020, consolidated profit and loss statement |
| Operating result | FY2020 / FY2019 | 20,063 / 17,020 | EUR k | AR2020, consolidated profit and loss statement |
| Average shares (pre-2022 split) | FY2020 / FY2019 | 10,005,420 / 9,942,657 | shares | AR2020, consolidated profit and loss statement |
| Net cash provided by operating activities | FY2020 / FY2019 | 37,318 / 24,745 | EUR k | AR2020, cash-flow statement |
| Payout for investments in fixed assets | FY2020 / FY2019 | 14,993 / 19,982 | EUR k | AR2020, cash-flow statement |
| Acquisitions less cash acquired | FY2020 / FY2019 | 8,492 / 14,503 | EUR k | AR2020, cash-flow statement |
| Total assets | 31 Dec 2020 / 31 Dec 2019 | 190,132 / 181,211 | EUR k | AR2020, group balance sheet |
| Equity | 31 Dec 2020 / 31 Dec 2019 | 114,908 / 102,981 | EUR k | AR2020, group balance sheet |
| Cash in bank and cash in hand | 31 Dec 2020 / 31 Dec 2019 | 47,860 / 35,177 | EUR k | AR2020, group balance sheet |
| Goodwill | 31 Dec 2020 / 31 Dec 2019 | 27,474 / 27,474 | EUR k | AR2020, group balance sheet |
| Sales revenues | FY2018 | 150,003 | EUR k | AR2019, consolidated income statement |
| Operating result | FY2018 | 24,827 | EUR k | AR2019, consolidated income statement |
| Average shares (pre-2019 and pre-2022 splits as printed) | FY2018 | 9,642,198 | shares | AR2019, consolidated income statement |
| Net cash provided by operating activities | FY2018 | 26,998 | EUR k | AR2019, cash-flow statement |
| Payout for investments in fixed assets | FY2018 | 18,026 | EUR k | AR2019, cash-flow statement |
| Cash in bank and cash in hand | 31 Dec 2018 | 31,830 | EUR k | AR2019, consolidated balance sheet |
| Sales / EBIT / total assets / equity | FY2017 | 150.2 / 30.5 / 117.7 / 65.6 | EUR m | AR2019, key-figures table (orientation; statements owed) |
| Total assets / equity | 31 Dec 2016 | 90.4 / 50.0 | EUR m | Annual Report 2017 results presentation (search snippet only; not retrieved; statements owed) |

Derived (labelled, never carried as governing): FY2025 MCap at px ≈ 23.70 × 30.75m ≈ EUR 729m (derived; the diluted count at the latest balance sheet is owed from the Q3 2026 report).

## 3. Readings settled

None. Gate 0, the lens and the G6 test were not started on the record. Orientation only, for the next run:
- Basler makes industrial machine-vision cameras, lenses, lighting, frame grabbers and software, sold to machine builders and OEMs (factory automation, logistics, medical, retail). It reports as one business; whether there is more than one reportable segment is owed (AR2025 segment note).
- Roboception GmbH was equity-accounted (25.1%), carried at EUR 0.3m at end-2024 and written to zero in 2025. Its income is below the operating result. FY2024 operating result is negative (-10.1m), so the P31 income limb fails in FY2024 unless the difference is nil. The G6 two readings will probably apply; carrying values stay far under 5% of total assets.
- Controller: Norbert Basler Holding GmbH holds about 52.7% of votes (queue note; to confirm from AR2025).

## 4. Scope still owed

- [ ] **FY2016 and FY2017 IFRS statements** and the **31 Dec 2015 balance sheet**: Annual Report 2017 (FY2017 + FY2016) and Annual Report 2016 (31 Dec 2015 comparatives). Hosts tried: www.baslerweb.com (HTTP 403 to the sandbox, per the queue note); assets-ctf.baslerweb.com (asset ids unknown; only the 2017 results presentation surfaced in search); irpages2.eqs.com `DE0005102008-JA-{2015…2019}-EQ-E-01.pdf` (HTTP 404, only 2020 exists); more-ir.de `DE0005102008-JA-{year}-EQ-E-00/01.pdf` (a JavaScript app page, no PDF to curl or WebFetch); hauptversammlung.de `Basler_AG_HV_{2017,2018,2019}_Geschaeftsbericht.pdf` (HTTP 404).
- [ ] **FY2023 income statement and cash-flow statement**: Annual Report 2023 (published 28 Mar 2024) or Annual Report 2024 comparatives. Hosts tried: more-ir.de `DE0005102008-JA-2023-EQ-E-00.pdf` (surfaced in search; JavaScript page), hauptversammlung.de `Basler_AG_HV_2024_Geschaeftsbericht.pdf` (404), the EQS pattern (404).
- [ ] FY2021 and FY2022 full balance sheets from AR2022 (DE): retrieved, not yet extracted.
- [ ] **Q3 2026 report** (expected early November 2026): the latest balance sheet for EV and the diluted share count.
- [ ] Remuneration report 2025 (§162 AktG) and 2024, 2023, for the P17 pay table; AR2025 notes on the treasury-share buyback (2023 programme ended early; 894k treasury shares resold), the Alpha TechSys 76% acquisition (closed 17 Jan 2026: live-year acquisition stop), the non-recourse factoring with Commerzfactoring (debt-equivalent test), and note 28 (other non-financial liabilities, NIBCL calls).
- [ ] Then the full §8.1 build on FY2016–FY2025.

A later run may try: the German company register (unternehmensregister.de), Basler's EQS newsroom links to each annual report, or a copy Jakub supplies in an attended session.
