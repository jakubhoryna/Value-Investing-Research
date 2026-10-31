# TUI1.DE — TUI AG — REVIEW evidence (INCOMPLETE, resumable record) — 2026-10-31

## 1. Header

- key: TUI1.DE · company: TUI AG · ISIN DE000TUAG505 (sourced in the first record from the filer's EQS document name `DE000TUAG505-Q2-2025-EQ-E-00.pdf`; the prior memo and `register.csv` carry none)
- job: REVIEW · D 2026-10-31 · T 0921 (Europe/Prague) · base 244eecdb96602d7b3440ca2736ff82d4ab4e829d · live `model_version` v4.8.0
- prior memo: `memos/TUI1.DE/TUI1.DE_2026-07-24_GSC.md`, memo_version v1, **no `model_version`** (pre-v3 format, no §6.1 machine fields; AVOID on Past WEAK and Future WEAK, SF PASS with one flag, CHEAP; trigger €7.48 on an all-cash-era reading)
- named gap: **method re-test exceeds budget**. This is the **second overrun**.
- resumes: `queue/evidence/TUI1.DE_2026-10-25_INCOMPLETE.md` (first overrun, REVIEW 2026-10-25, PR #271). That record predates the v4.8.0 record format: it holds no item table and cites its figures by report and note, not by page. Every figure below is re-cited to a page in the primary report; nothing from the first record is carried without a page.
- re-tests owed in one run: every v4.5.0 rule (the prior predates them all), Gate 0 / lens / group rules / G6 pairing (v4.6.0), and the v4.8.0 rules.
- **No verdict, no grade.** Every figure below is sourced (report and page) or labelled `derived`. Nothing is assumed.

**Documents (primary, uncounted under P14), all text-extracted with `pdftotext -layout`. Page = PDF page index.**

| tag | document | URL |
|---|---|---|
| AR16 | TUI Group Annual Report 2015/16 | annualreports.com/HostedData/AnnualReportArchive/t/LSE_TUI_2016.pdf |
| AR17 | TUI Group Annual Report 2016/17 | …/LSE_TUI_2017.pdf |
| AR18 | TUI Group Annual Report 2017/18 | …/LSE_TUI_2018.pdf |
| AR19 | TUI Group Annual Report 2018/19 | …/LSE_TUI_2019.pdf |
| AR20 | TUI Group Annual Report 2019/20 | …/LSE_TUI_2020.pdf |
| AR21 | TUI Group Annual Report 2020/21 | …/LSE_TUI_2021.pdf |
| AR22 | TUI Group Annual Report 2021/22 | …/LSE_TUI_2022.pdf |
| AR23 | TUI Group Annual Report 2022/23 | …/LSE_TUI_2023.pdf |
| AR24 | TUI Group Annual Report 2023/24 | …/LSE_TUI_2024.pdf |
| AR25 | TUI Annual Report 2025 | annualreport.tuigroup.com/2025/download-center/TUI_AR25_Gesamt_EN.pdf |

Statement pages: income statement AR16 p238, AR17 p138, AR18 p154, AR19 p156, AR20 p143, AR21 p148, AR22 p156, AR23 p182, AR24 p175, AR25 p232. Balance sheet AR16 p240–241, AR17 p140–141, AR18 p156–157, AR19 p158–159, AR20 p144, AR21 p149, AR22 p157, AR23 p183, AR24 p176, AR25 p234–235. Cash flow statement AR16 p244, AR17 p144, AR18 p160, AR19 p162, AR20 p147, AR21 p152, AR22 p160, AR23 p186, AR24 p179, AR25 p238. AR20–AR24 print the income statement, balance sheet and comprehensive income side by side in two columns: read each value against its row label on the page.

## 2. Per gate or leg

### 2.1 Gate 0 and the lens

Work done: the segment note read (AR25 p260–261). Seven reportable segments in two divisions: Holiday Experiences (Hotels & Resorts, Cruises, TUI Musement) and Markets + Airline (Northern, Central, Western Region), plus All other segments. The filer states: "Assets and liabilities by segment are not included in the reporting to the Executive Board and are therefore not shown in segment reporting" (AR25 p260). It also states: "No single external customer accounts for 10% or more of revenue" (AR25 p260). No licensed bank or insurer part is visible in the segment note, so the lens is STD on the face of the record (FI is not open: TUI is a tourism group). The captive-finance test, the unit sentences and the P22 sister-unit test are still owed.

| item | FY | value | unit | source |
|---|---|---|---|---|
| Revenue, Hotels & Resorts (external / group / total) | FY2025 | 1,243.8 / 999.7 / 2,243.5 | €m | AR25 p261, Revenue by segment |
| Revenue, Cruises (total; group −0.0) | FY2025 | 883.4 | €m | AR25 p261, Revenue by segment |
| Revenue, TUI Musement (external / group / total) | FY2025 | 1,044.8 / 457.8 / 1,502.6 | €m | AR25 p261, Revenue by segment |
| Revenue, Northern Region (external / group / total) | FY2025 | 8,856.8 / 315.2 / 9,172.0 | €m | AR25 p261, Revenue by segment |
| Revenue, Central Region (external / group / total) | FY2025 | 8,854.0 / 86.4 / 8,940.4 | €m | AR25 p261, Revenue by segment |
| Revenue, Western Region (external / group / total) | FY2025 | 3,282.8 / 121.7 / 3,404.5 | €m | AR25 p261, Revenue by segment |
| Revenue, All other segments (external / group / total) | FY2025 | 13.2 / 5.6 / 18.8 | €m | AR25 p261, Revenue by segment |
| Revenue by segment, same seven lines | FY2024 | 2,089.5 · 840.1 · 1,362.0 · 8,862.3 · 8,419.2 · 3,470.3 · 17.7 | €m | AR25 p261, Revenue by segment |
| Underlying EBIT: H&R · Cruises · Musement · Northern · Central · Western · All other | FY2025 | 735.0 · 481.1 · 67.2 · 123.2 · 98.3 · −21.6 · −70.0 | €m | AR25 p261, Underlying EBIT by segment |
| Underlying EBIT, same seven lines | FY2024 | 668.4 · 374.3 · 49.2 · 165.4 · 128.1 · 10.3 · −99.6 | €m | AR25 p261, Underlying EBIT by segment |
| Separately disclosed items by segment (net expense): H&R 0.8; Musement −15.4 (net income, incl. ARP Group disposal gain 11.7); Northern 6.5; Central 10.5; Western 9.1; All other 12.1 | FY2025 | 23.6 total | €m | AR25 p260, Notes to the segment data |
| PPA expense (amortisation of acquired intangibles), group | FY2025 / FY2024 | 20.6 / 20.9 | €m | AR25 p261, reconciliation; p260 |

The segment measure is underlying EBIT, which excludes separately disclosed items and PPA (AR25 p260). P29 weights need the segment result after the J1 charges: deduct each segment's separately disclosed restructuring and its PPA where the note allocates them; the PPA split by segment is still owed. Underlying EBIT includes each segment's share of JV and associate results (AR25 p260: "the share of result of joint ventures and associates are likewise shown for each segment").

### 2.2 Past — the G6 classes and the P31 test

The class is the equity-accounted joint ventures and associates (TUI Cruises 50%, the Riu hotel vehicles and others; the material-JV notes are AR21 p192, AR22 p202, AR23 p228, AR24 p221–223, AR25 p279). Their result is booked inside EBT on its own line, above financial items. Dividends received from them sit inside cash inflow from operating activities, so the include reading keeps them in FCF and the exclude reading removes them.

| item | FY | value | unit | source |
|---|---|---|---|---|
| Investments in JVs and associates (carrying value) | FY2015 | 1,077.8 | €m | AR16 p240, balance sheet, prior-year column |
| Investments in JVs and associates | FY2016 | 1,180.8 | €m | AR16 p240; AR17 p140 |
| Investments in JVs and associates | FY2017 | 1,306.2 (restated 1,273.9 at 1 Oct 2017) | €m | AR17 p140; restated AR19 p158, third column |
| Investments in JVs and associates | FY2018 | 1,436.6 (restated 1,398.1) | €m | AR18 p156; restated AR19 p158 |
| Investments in JVs and associates | FY2019 | 1,507.6 | €m | AR19 p158; AR20 p144 |
| Investments in JVs and associates | FY2020 | 1,186.7 | €m | AR20 p144 |
| Investments in JVs and associates | FY2021 | 640.5 | €m | AR21 p149 |
| Investments in JVs and associates | FY2022 | 785.4 | €m | AR22 p157 |
| Investments in JVs and associates | FY2023 | 1,198.2 | €m | AR23 p183 |
| Investments in JVs and associates | FY2024 | 1,507.5 | €m | AR24 p176; AR25 p234 |
| Investments in JVs and associates | FY2025 | 1,716.5 | €m | AR25 p234 |
| Total assets | FY2015 / FY2016 | 14,086.5 / 14,457.9 | €m | AR16 p240 (and p176, balance-sheet summary) |
| Total assets | FY2017 | 14,185.5 (restated 14,166.0) | €m | AR17 p140; restated AR19 p158 |
| Total assets | FY2018 | 15,611.8 (restated 15,590.8) | €m | AR18 p156; restated AR19 p158 |
| Total assets | FY2019 | 16,270.9 (restated 16,218.1) | €m | AR19 p158; restated AR20 p144 |
| Total assets | FY2020 · FY2021 · FY2022 · FY2023 · FY2024 · FY2025 | 15,341.1 · 14,155.7 · 15,255.5 · 16,152.4 · 17,416.7 · 18,148.9 | €m | AR20 p144; AR21 p149; AR22 p157; AR23 p183; AR24 p176; AR25 p234 |
| Share of result of JVs and associates | FY2015 · FY2016 | 143.9 · 187.2 | €m | AR16 p238 |
| Share of result of JVs and associates | FY2017 | 252.3 | €m | AR17 p138 |
| Share of result of JVs and associates | FY2018 | 297.7 (restated 292.1) | €m | AR18 p154; restated AR19 p156 |
| Share of result of JVs and associates | FY2019 · FY2020 | 297.5 · −193.3 | €m | AR20 p143 (2019 also AR19 p156) |
| Impairment of net investments in JVs and associates | FY2020 | 34.5 (charge) | €m | AR20 p143 |
| Share of result of JVs and associates | FY2021 | −232.7 | €m | AR21 p148 |
| Impairment (+)/reversal (−) of net investments in JVs | FY2021 · FY2022 · FY2023 | owed: the line wraps on AR21 p148, AR22 p156, AR23 p182; read its value against the label | €m | AR21 p148; AR22 p156; AR23 p182 |
| Share of result of JVs and associates | FY2022 · FY2023 | 100.7 · 407.2 | €m | AR22 p156; AR23 p182 |
| Share of result of JVs and associates | FY2024 · FY2025 | 371.7 · 463.9 | €m | AR25 p232 |
| Impairment (+)/reversal (−) of net investments in JVs | FY2024 · FY2025 | 0.2 · −0.7 | €m | AR25 p232 |
| Dividends from JVs and associates (inside CFO) | FY2015 · FY2016 | 81.3 · 82.2 | €m | AR16 p244 |
| Dividends from JVs and associates (inside CFO) | FY2017 · FY2018 · FY2019 | 118.2 · 222.7 · 244.6 | €m | AR17 p144; AR18 p160; AR19 p162 |
| Dividends from JVs and associates (inside CFO) | FY2020 · FY2021 · FY2022 | 7.1 · 14.2 · 0.2 | €m | AR21 p152; AR22 p160 |
| Dividends from JVs and associates (inside CFO) | FY2023 · FY2024 · FY2025 | 24.1 · 67.2 · 268.1 | €m | AR24 p179; AR25 p238 |
| Carrying value ÷ total assets | FY2015 → FY2025 | 7.7 · 8.2 · 9.2 · 9.2 · 9.3 · 7.7 · 4.5 · 5.1 · 7.4 · 8.7 · 9.5 | % | derived: the two rows above (as-reported values; restated values change FY2017–FY2019 by < 0.3 pp) |
| \|include OI − exclude OI\| ÷ exclude OI | FY2015 → FY2025 | 22.1 · 26.1 · 33.4 · 39.4 · 66.7 · fail (OI_x ≤ 0) · fail (OI_x ≤ 0) · 44.4 · 69.0 · 41.3 · 51.8 | % | derived: §2.3 OI candidates less the JV result, plus the JV impairment; FY2021–FY2023 before the owed impairment line |

**P31: above the line on both limbs.** The carrying value is ≥ 5% of total assets at every balance-sheet date but FY2021, and the income limb fails in every window year. Every Gate 1A test reads exclude-both and include-both, and the harsher governs.

### 2.3 Past — J1 OI

TUI prints no operating subtotal on the face of the income statement. Candidates: (a) EBT plus financial expenses less financial income, which is the build the prior used; (b) the segment-note EBIT (EBT plus net interest expense, less interest-hedge measurement income), FY2025 1,368.9 and FY2024 1,275.3 (AR25 p261). Candidate (a) is lower in FY2025 and carries more charges. Underlying EBIT (1,413.1) excludes separately disclosed items and PPA, so it is never OI. The J3 removals inside (a) are still owed per year. These include disposal gains on stakes or businesses booked in other income (the ARP Group gain of 11.7 in FY2025, AR25 p260) and any fair-value results.

| item | FY | value | unit | source |
|---|---|---|---|---|
| Revenue (turnover) | FY2015 · FY2016 | 17,515.5 · 17,184.6 | €m | AR16 p238 |
| Revenue | FY2017 · FY2018 | 18,535.0 · 19,523.9 | €m | AR17 p138; AR18 p154 (FY2018 restated 18,468.7 in AR19 p156, IFRS 15) |
| Revenue | FY2019 · FY2020 · FY2021 | 18,928.1 · 7,943.7 · 4,731.6 | €m | AR19 p156; AR21 p148 |
| Revenue | FY2022 · FY2023 · FY2024 · FY2025 | 16,544.9 · 20,665.9 · 23,167.3 · 24,178.7 | €m | AR22 p156; AR23 p182; AR25 p232 |
| Earnings before income taxes | FY2015 · FY2016 | 465.8 · 618.3 | €m | AR16 p238 |
| EBT | FY2017 · FY2018 | 1,079.7 · 971.5 (restated 965.8) | €m | AR17 p138; AR18 p154; restated AR19 p156 |
| EBT | FY2019 · FY2020 | 691.6 · −3,203.3 | €m | AR20 p143 (AR19 p156 printed 691.4) |
| EBT | FY2021 · FY2022 · FY2023 | −2,461.7 · −145.9 · 551.2 | €m | AR21 p148; AR22 p156; AR23 p182 |
| EBT | FY2024 · FY2025 | 861.4 · 1,034.2 | €m | AR25 p232 |
| Financial income | FY2015 → FY2025 | 35.8 · 58.5 · 229.3 · 83.8 · 119.7 · 35.3 · 27.3 · 35.9 · 87.6 · 109.7 · 101.0 | €m | AR16 p238; AR17 p138; AR18 p154; AR20 p143; AR21 p148; AR22 p156; AR23 p182; AR25 p232 |
| Financial expenses | FY2015 → FY2025 | 364.5 · 345.9 · 156.2 · 165.5 · 171.4 · 321.7 · 464.1 · 509.5 · 533.6 · 518.3 · 429.0 | €m | same pages |
| OI candidate (a) = EBT + fin. expenses − fin. income | FY2015 → FY2025 | 794.5 · 905.7 · 1,006.6 · 1,053.2 · 743.3 · −2,916.9 · −2,024.9 · 327.7 · 997.2 · 1,270.0 · 1,362.2 | €m | derived: the three rows above (FY2018 on the as-reported AR18 figures; the restated year is owed) |
| OI exclude reading = (a) − JV result + JV impairment | FY2015 → FY2025 | 650.6 · 718.5 · 754.3 · 755.5 · 445.8 · −2,689.1 · −1,792.2* · 227.0* · 590.0* · 898.5 · 897.6 | €m | derived (*before the owed FY2021–FY2023 impairment line) |
| Segment-note EBIT | FY2025 · FY2024 | 1,368.9 · 1,275.3 | €m | AR25 p261, reconciliation to underlying EBIT |
| Net interest expense (excl. interest-hedge measurement) | FY2025 · FY2024 | 337.5 · 414.9 | €m | AR25 p261 |

### 2.4 Past — cash flow, P20 inputs, balance sheet and leverage

TUI classifies interest paid in financing, so it is moved into CFO (§2·1A). CFO below is as printed, before that move.

| item | FY | value | unit | source |
|---|---|---|---|---|
| Cash inflow from operating activities (as printed) | FY2015 · FY2016 | 790.5 · 1,034.7 | €m | AR16 p244 |
| CFO (as printed) | FY2017 · FY2018 · FY2019 | 1,583.1 · 1,150.9 · 1,114.9 | €m | AR17 p144; AR18 p160; AR19 p162 |
| CFO (as printed) | FY2020 · FY2021 · FY2022 | −2,771.9 · −151.3 · 2,077.8 | €m | AR20 p147; AR21 p152; AR22 p160 |
| CFO (as printed) | FY2023 · FY2024 · FY2025 | 1,637.3 · 1,910.8 · 2,058.2 | €m | AR23 p186; AR24 p179; AR25 p238 |
| Interest paid (financing) | FY2015 · FY2016 · FY2017 · FY2018 · FY2019 | 92.0 · 92.3 · 74.8 · 110.8 · 117.9 | €m | AR16 p244; AR17 p144; AR18 p160; AR19 p162 |
| Interest paid | FY2020 · FY2021 · FY2023 · FY2024 · FY2025 | 251.9 · 404.8 · 435.6 · 384.7 · 329.7 | €m | AR20 p147; AR21 p152; AR24 p179; AR25 p238 |
| Interest paid | FY2022 | owed (the prior memo's 385.6 is uncited; re-read AR22 p160 or AR23 p186) | €m | AR22 p160 |
| Payments for PP&E and intangible assets (capex) | FY2019 · FY2020 · FY2021 | 987.0 · 587.0 · 299.7 | €m | AR20 p147; AR21 p152 |
| Capex | FY2022 · FY2023 · FY2024 · FY2025 | 515.7 · 666.2 · 712.5 · 738.9 | €m | AR22 p160; AR23 p186; AR24 p179; AR25 p238 |
| Capex | FY2015 · FY2016 · FY2017 · FY2018 | owed: the line wraps on AR16 p244, AR17 p144, AR18 p160 (the prior memo's 697.4 · 1,049.0 · 956.2 for FY2016–FY2018 are uncited) | €m | AR16 p244; AR17 p144; AR18 p160 |
| Depreciation, amortisation and impairment (CF statement, all assets) | FY2015 · FY2016 · FY2017 · FY2018 · FY2019 | 700.5 · 578.5 · 517.8 · 438.9 (restated 440.4) · 509.6 | €m | AR16 p244; AR17 p144; AR18 p160; AR19 p162 |
| Property, plant and equipment (net) | FY2015 · FY2016 · FY2017 · FY2018 | 3,636.8 · 3,714.5 · 4,253.7 · 4,899.2 (restated 4,876.3) | €m | AR16 p240; AR17 p140; AR18 p156; AR19 p158 |
| PP&E (net) | FY2019 · FY2020 | 5,840.4 (restated 5,810.7) · 3,462.5 | €m | AR19 p158; AR20 p144 (IFRS 16 moved leased aircraft to right-of-use assets) |
| PP&E (net) | FY2022 · FY2023 · FY2024 · FY2025 | 3,400.9 · 3,480.3 · 3,697.4 · 4,133.3 | €m | AR23 p183; AR24 p176; AR25 p234 |
| Goodwill · other intangible assets | FY2015 | 3,220.4 · 911.5 | €m | AR16 p240 |
| Goodwill · other intangible assets | FY2016 · FY2017 · FY2018 | 2,853.5 · 545.8; 2,889.5 · 548.1; 2,958.6 · 569.9 | €m | AR17 p140; AR18 p156 |
| Goodwill · other intangible assets | FY2019 · FY2020 | 2,985.8 · 710.6; 2,914.5 · 553.5 | €m | AR19 p158; AR20 p144 |
| Other intangible assets | FY2021 · FY2022 · FY2023 | 498.6 · 507.6 · 538.0 | €m | AR22 p157; AR23 p183 |
| Goodwill · other intangible assets | FY2024 · FY2025 | 2,998.7 · 589.6; 2,933.6 · 596.8 | €m | AR25 p234 |
| Right-of-use assets | FY2021 · FY2022 · FY2023 · FY2024 · FY2025 | 3,009.2 · 2,971.5 · 2,763.4 · 2,538.7 · 2,356.3 | €m | AR22 p157; AR23 p183; AR25 p234 |
| Cash and cash equivalents | FY2015 · FY2016 · FY2017 · FY2018 · FY2019 | 1,672.7 · 2,072.9 · 2,516.1 · 2,548.0 · 1,741.5 | €m | AR16 p240; AR17 p140; AR18 p156; AR19 p158 |
| Cash and cash equivalents | FY2022 · FY2023 · FY2024 · FY2025 | 1,736.9 · 2,060.3 · 2,848.2 · 3,120.2 | €m | AR23 p183; AR25 p234 |
| Other financial assets, current | FY2024 · FY2025 | 53.4 · 12.1 | €m | AR25 p234 |
| Trade payables · touristic advance payments received · current income tax liabilities | FY2025 | 3,355.4 · 4,094.3 · 147.8 | €m | AR25 p235 |
| Trade payables · touristic advance payments · current income tax liabilities | FY2024 | 3,393.2 · 4,017.1 · 100.5 | €m | AR25 p235 |
| Touristic advance payments received | FY2017 · FY2018 · FY2019 · FY2020 · FY2021 · FY2022 · FY2023 | 2,446.4 · 2,551.0 · 2,911.2 · 1,770.1 · 2,379.4 · 2,998.9 · 3,530.2 | €m | AR17 p141; AR18 p157; AR19 p159; AR20 p144; AR21 p149; AR22 p157; AR23 p183 |
| Trade payables | FY2015 · FY2016 · FY2017 · FY2018 · FY2019 | 3,224.2 · 2,476.9 · 2,653.3 · 2,937.3 · 2,873.9 | €m | AR16 p241; AR17 p141; AR18 p157; AR19 p159 |
| Trade payables | FY2020 · FY2021 · FY2023 | 1,611.5 · 2,052.4 · 3,373.7 | €m | AR21 p149; AR24 p176 |
| Equity before NCI | FY2015 · FY2016 · FY2017 · FY2018 | 1,913.4 · 2,675.1 · 2,939.7 · 3,698.1 | €m | AR16 p241; AR17 p141; AR18 p157 |
| Equity before NCI | FY2019 | 3,453.9 | €m | AR19 p159 |
| Equity before NCI | FY2023 · FY2024 · FY2025 | 1,122.9 · 956.4 · 1,762.5 | €m | AR25 p236–237, statement of changes in equity |
| NCI · total equity | FY2025 | 924.2 · 2,686.7 | €m | AR25 p237 |
| Total liabilities | FY2025 | 15,462.2 | €m | derived: total assets 18,148.9 (AR25 p234) − total equity 2,686.7 (AR25 p237) |
| L/E | FY2025 | 877.3 | % | derived: 15,462.2 ÷ 1,762.5 |
| Financial liabilities (non-current · current) | FY2025 | 1,562.2 · 420.6 | €m | AR25 p235 |
| Lease liabilities (non-current · current) | FY2025 | 1,768.7 · 685.8 | €m | AR25 p235 |
| Pension provisions (non-current · current) | FY2025 | 583.0 · 35.6 | €m | AR25 p235 (net of plan assets as presented; the surplus side is owed, AR25 note 29) |
| Group profit attributable to TUI AG shareholders · NCI | FY2025 | 635.9 · 205.8 | €m | AR25 p232 |
| Diluted EPS · basic EPS | FY2025 | 1.17 · 1.25 | € | AR25 p232 |
| Dividends paid to NCI | FY2025 · FY2024 | 99.5 · 144.8 | €m | AR25 p237; p236 |

### 2.5 Future

Work done: the group customer statement (AR25 p260, quoted in §2.1) rules out any external customer at 10% of revenue. Under v4.8.0 it covers every material unit, unless the filer names a concentrated customer or unit. None was found in the segment note; the unit-level read is owed. Each unit's forces, moat and market are owed.

### 2.6 SF

Work done: none beyond locating the documents. The remuneration report is AR25 from p205 (contents, AR25 p3); §162 AktG "granted and owed" basis (AR25 p94). There are no repurchases of shares in FY2024–FY2025: the statement of changes in equity carries no treasury-share line (AR25 p236–237). The full window is owed. Capital-allocation events in the window that are visible on the record: the 2021–2023 capital increases and the silent participation (AR21 p149: 1,091.0; AR22 p157: 420.0; nil at FY2023, AR23 p183), the capital reserve withdrawal of 1,178.5 in FY2024 (AR25 p236), and dividends to NCI.

### 2.7 Gate 2

Not built. Price endpoint `query1.finance.yahoo.com/v8/finance/chart/TUI1.DE`: HTTP 429 "Too Many Requests" on both calls made (from 08:23 UTC, about 15 minutes apart). The first record's close was €6.576 on 2026-10-23. The 30 Jun 2026 interim (Q3 FY2026 statement) is still owed: its balance sheet is required for EV (MODEL §4).

## 3. Readings settled (inputs, never grades)

- **Window:** FY2016–FY2025 (10y), 11 balance sheets FY2015–FY2025. FY2026 ends 30 Sep 2026; its annual report (~Dec 2026) is not yet published. The record is complete on the primary reports listed above. No history-limited or record-limited label applies once the owed lines are read.
- **G6:** the class is the equity-accounted JVs and associates. Above the P31 line on both limbs (§2.2), so both readings are built, with dividends from JVs (inside CFO) out of exclude-reading FCF.
- **J1:** candidate (a), EBT + financial expenses − financial income, is the lowest subtotal in FY2025 (1,362.2 against the segment-note EBIT of 1,368.9). The other years and the J3 removals inside it are owed.
- **Leverage, FY2025:** L/E 877.3% (derived, §2.4). That is above P5's 200% and above P6's 700% cap on the printed figures, before the v4.5.0 debt-equivalent and lease rules, which only add to liabilities if anything. **Pointer (never a finding):** Past WEAK on `leverage` looks determinate on the consolidated record, whatever the G6 and P20 builds give. A resumed run should confirm total liabilities from the face of AR25 p235 before relying on it.
- **Group:** seven reportable segments (§2.1), so this is a group. No segment assets are reported (AR25 p260), so the §2·1C·3 allocation-across-the-parts test is INDETERMINATE (b), with its re-test named. The group customer statement exists (AR25 p260).
- **P20, P17, worth table:** not settled.

## 4. Scope still owed (in order)

- [ ] Price: one GET to `query1.finance.yahoo.com/v8/finance/chart/TUI1.DE` (currency, exchangeName, close and date, split events).
- [ ] Q3 FY2026 quarterly statement (30 Jun 2026 balance sheet: financial liabilities at principal, leases, cash, pensions, NCI, diluted shares). tuigroup.com/en-en/investors loads its reports by script, so find a direct PDF (EQS `ir-api.eqs.com` document store, as in the first record's ISIN source).
- [ ] J3 per year inside OI candidate (a): other income and other expenses notes (AR25 note 3 and each year's equivalent) for disposal gains on stakes or businesses (Hotelbeds FY2016–17, the Specialist Group, Sunwing FY2023, ARP FY2025), fair-value results, and the pension net-interest rule (net cost stays below the line; net income leaves).
- [ ] The wrapped lines: JV impairment FY2021–FY2023 (AR21 p148, AR22 p156, AR23 p182); capex FY2015–FY2018 (AR16 p244, AR17 p144, AR18 p160); interest paid FY2022 (AR22 p160); equity before NCI FY2020–FY2022 (AR20 p144, AR21 p149, AR22 p157).
- [ ] NIBCL per year (trade payables, touristic advance payments, current income tax, accrued expenses where printed) and the FY2015–FY2016 advance-payment line (AR16 p241 prints it as part of other liabilities: note 37). Read the IFRS 9/15 restatements of FY2017–FY2018 (AR19 p158–159).
- [ ] P18 for FY2015–FY2019 (pre-IFRS 16): operating-lease commitment tables (AR16 operating-lease note; AR18; AR19), the discount rate (the IFRS 16 transition rate of 4.99%, AR20, as used by the prior), and the PV per year.
- [ ] P20 constructed per year: net PP&E (right-of-use excluded) plus capitalised software (other-intangibles note: software vs acquired intangibles); depreciation of PP&E plus amortisation of software (fixed-asset notes); organic revenue (acquisitions and disposals per year); euro-area HICP FY2016–FY2025 (Eurostat); k over the window. TUI's reporting currency is EUR, so the deflator is euro-area HICP.
- [ ] B1–B3 on both G6 readings, with the four-way averages on the P1 and 5-year windows, both growth reads (read (ii) where (i) is n.m., v4.8.0), J6 on each reading, and the 10:1 share consolidation of 2023 applied to the per-share series.
- [ ] Gate 0: the group sentence and one sentence per material unit. P22: Hotels & Resorts sells 999.7 of 2,243.5 to group (44.6%, derived), below the 50% merge line. All other segments (18.8 revenue, −70.0 underlying EBIT) are immaterial on revenue; test them on Σ positive results and assets.
- [ ] Future per unit (H&R, Cruises, Musement, Northern, Central, Western): breadth under the group statement, four forces, moat, market; P29 weights on the latest three FYs' segment results after J1 charges (FY2023 from AR24, FY2024–FY2025 from AR25 p261); S.
- [ ] SF: the §162 AktG table FY2023–FY2025 (AR23, AR24, AR25 remuneration reports), the hairiest number on every basis, the director cap (Supervisory Board fees), alignment (Executive Board holdings at px; Riu family holding and seat under votes versus economics), RPTs with the JVs (AR25 note 48: services received 469.6), the worth table (no repurchases expected: confirm per year from the CF statements), the acquisition stop for deals > 1% of EV in FY2023–FY2026, dilution (2021–2023 capital increases) under distributions and funding, and the allocation test, INDETERMINATE (b).
- [ ] Gate 2: EV both ways at the interim balance sheet, the debt-equivalents in full (borrowings at principal, leases, pensions net unfunded, NCI at book for unlisted subsidiaries, earn-outs, supplier finance if any), core numbers, the P28 test, the 3-year and 5-year readings, and the trigger at the no-cash bound.

*Framework output, not investment advice.*
