# NKR.OL — Nekkar ASA — INCOMPLETE evidence, resumable record (ANALYSE 2026-11-06)

## 1. Header

- Key: NKR.OL · job: ANALYSE · D 2026-11-06 · T 2203 · base sha 157ee8bb6706493ec46627549961dfebdd826e3a
- Live `model_version`: v4.8.0
- Prior memo: none (`model_version`: none). No `memos/NKR.OL/` or `archive/memos/NKR.OL/` at base; no register row, memo front matter or `register.csv` line matches "Nekkar", "TTS Group" or ISIN NO0003049405.
- ISIN: NO0003049405 from the DRAFT_QUEUE line; not yet confirmed in a primary document (the AR 2025 text layer prints no ISIN). Confirm at resume (Euronext/Oslo Børs page or the AR share note).
- Named gap: **group build exceeds budget** (README §5; MODEL §8.7 item 6). **First overrun**: the DRAFT_QUEUE line carries no ` — partial …` note at base.
- No verdict, grade or band is stated here. Every "derived" figure is arithmetic on cited figures, never a grade.

## 2. Per gate or leg — work done and figures

### Key and price (uncounted endpoint)

- `query1.finance.yahoo.com/v8/finance/chart/NKR.OL`: `currency` NOK, `exchangeName` OSL (Oslo), longName "Nekkar ASA", `instrumentType` EQUITY. Close 2026-11-06 = 18.60 NOK (prior closes 2026-11-05 18.40, 2026-11-04 16.60). No split event in the 1-month range. The resume re-takes px.

### Document route (all retrieved with HTTP 200; IR index `https://www.nekkar.com/report-archive` and `https://www.nekkar.com/financials`)

Abbreviation `CDN` = `https://cdn.prod.website-files.com/68baecea19bd19bfaef8953e/`.

| doc | URL |
|---|---|
| AR2025 (approved 30 Apr 2026) | `https://kommunikasjon.ntb.no/ir-files/17847326/18882153/8516/Nekkar%20Annual%20Integrated%20Report%202025.pdf` |
| AR2024 | `CDN` + `68c8e7cb37c1e1c51e239ffc_Nekkar-Annual-integrated-report-2024.pdf` |
| AR2023 | `CDN` + `68c8e7ef85a172034d735629_Nekkar-Annual-integrated-report-2023_2024-06-24-074946_qtoj.pdf` |
| AR2022 | `https://nekkar.s3.eu-north-1.amazonaws.com/Nekkar-Annual-report-2022_2023-04-26-224338_xwcj.pdf` |
| AR2021 | `CDN` + `68c3dcdb7626e123d0326f21_Nekkar-ASA_Annual-Report-2021.pdf` |
| AR2020 | `CDN` + `68c3dcf2a413b7cc641b2328_2020_Annual-Report-1.pdf` |
| AR2019 | `CDN` + `68c3dd0819f41136693bbc4e_2019_Annual-Report.pdf` |
| AR2018 (TTS Group ASA) | `CDN` + `68c3dd281670b95752eb230e_2018_Annual-Report_2022-05-16-130245_jcao.pdf` |
| AR2017 (TTS Group ASA) | `CDN` + `68c3dd3befff37e88802ac22_2017_Annual-Report.pdf` |
| AR2016 (TTS Group ASA) | `CDN` + `68c3dd53efff37e88802b151_2016_Annual-Report.pdf` |
| AR2015 (TTS Group ASA) | `CDN` + `68c3dd6b8622520d638784bd_2015_Annual-Report.pdf` |
| Q3 2026 report (presentation-format, incl. condensed statements) | `https://kommunikasjon.ntb.no/ir-files/17847326/19131083/20462/Nekkar%20ASA%20Q3%202026.pdf` |
| H1 2026 financial statement | `https://kommunikasjon.ntb.no/ir-files/17847326/19030496/15478/Nekkar%20ASA%20Financial%20Statement%20Q2%20and%20half-year%20results%202026.pdf` |
| Quarterly figures (xlsx, read as data only) | `https://nekkar.s3.eu-north-1.amazonaws.com/Nekkar-quarterly-figures-attachement-Q3-26.xlsx` (not yet opened) |

### Gate 0, group status and the lens (work done)

- Business (AR2025 Note 1 "Operating segments", p. 82): Nekkar is a Kristiansand-based industrial holding of ocean-technology businesses. Reportable segments at FY2025: **Syncrolift** (shiplifts and ship transfer systems sold to commercial repair and newbuilding yards and navy bases worldwide, plus service), **Intellilift** (drilling-rig automation and software, project, perpetual-licence and SaaS models; also sells engineering inside the group), **Techano Oceanlift** (cranes, gangways and fish-transfer systems for aquaculture and offshore energy), **Globetech** (maritime ICT infrastructure, satellite connectivity and cybersecurity services; acquired Aug 2024), **Other** (parent functions, the equity-accounted FiiZK stake, eliminations).
- Since Q3 2026: FiiZK (closed-cage systems for fish farmers) consolidated from 1 Jul 2026, and Satco consolidated in Globetech from 1 Aug 2026 (Q3 2026 report, p. 7 note; p. 18). Q3 2026 reports FiiZK as its own segment (revenue 69.6, EBIT −2.0 NOK m).
- **Group (P22), derived from AR2025 Note 1, p. 83.** FY2025 external revenue: Syncrolift 313,653 (54.9%), Techano Oceanlift 114,894 (20.1%), Globetech 103,180 (18.1%), Intellilift 38,962 (6.8%) of 571,087 NOK k. Σ positive segment operating profit FY2025 = 38,670 + 15,616 + 19,509 = 73,795; Intellilift 15,616 = 21.2% → material on the profit limb. So **four material units** → group rules apply (B4, one Appendix D block per unit, allocation-across-the-parts table). Segment assets: not found yet in Note 1 (to check; without them the allocation test is INDETERMINATE (b)).
- Customer statement (AR2025 Note 1, p. 84): "During 2025 Syncrolift and Techano Oceanlift AS had one customer each that accounted for more than 10% of the consolidated revenue … MNOK 62.7 and MNOK 82.2." Named concentrated customers in two units → those units read on the disclosure (§2·1B); Intellilift and Globetech: no statement found yet.
- Lens: no bank or insurer licence in anything read → STD expected; FI test to be logged.
- Listed subsidiaries/holdings: none found (FiiZK unlisted; Skeie Teknologi AS is a holder, not a holding). NCI exists (Globetech, Techano Oceanlift; put liabilities booked against equity, AR2025 SoCE and Notes 21–22).

### Past (B1 inputs; NOK k; the latest primary that prints each year governs)

Window to build: FY2016–FY2025 (10 FYs; balance sheets FY2015–FY2025). FY2016–FY2018 are TTS Group ASA (same legal entity, renamed Nekkar after the 2019 sale of the TTS businesses to MacGregor, completed 31 Jul 2019 per AR2019). Those years exist and are audited, so the record is not history-limited on its face; how their discontinued operations enter CE is a reading still owed (§3).

| item | FY | value | unit | source |
|---|---|---|---|---|
| Revenue | 2025 | 571087 | NOK k | AR2025, consolidated statement of comprehensive income, p. 63 |
| OI (operating profit/loss) | 2025 | -30711 | NOK k | AR2025, SoCI p. 63 (after impairment of intangibles 13,724) |
| Impairment of intangible assets | 2025 | 13724 | NOK k | AR2025, SoCI p. 63 |
| Depreciation and amortisation | 2025 | 18485 | NOK k | AR2025, SoCI p. 63 |
| Financial income / expense | 2025 | 36542 / 17884 | NOK k | AR2025, SoCI p. 63 |
| Share of equity-accounted result (FiiZK) | 2025 | -25351 | NOK k | AR2025, SoCI p. 63 |
| Profit for the period / attributable to parent | 2025 | -34563 / -40924 | NOK k | AR2025, SoCI p. 63 |
| CFO | 2025 | 35614 | NOK k | AR2025, consolidated statement of cash flow, p. 67 |
| Capex (fixed/intangible) | 2025 | -19234 | NOK k | AR2025, cash flow p. 67 |
| Repurchases / lease payments / NCI dividends | 2025 | -64266 / -6064 / -6382 | NOK k | AR2025, cash flow p. 67 |
| Total assets | 2025 | 744647 | NOK k | AR2025, statement of financial position, p. 64 |
| Goodwill / other intangibles | 2025 | 106132 / 85265 | NOK k | AR2025, SoFP p. 64 |
| PP&E / right-of-use | 2025 | 14243 / 23035 | NOK k | AR2025, SoFP p. 64 |
| Equity-accounted investees (FiiZK) | 2025 | 56812 | NOK k | AR2025, SoFP p. 64 |
| Cash and cash equivalents | 2025 | 149557 | NOK k | AR2025, SoFP p. 64 |
| Shareholders' equity / NCI | 2025 | 296020 / 71773 | NOK k | AR2025, SoFP p. 65 |
| Total liabilities | 2025 | 376854 | NOK k | AR2025, SoFP p. 65 |
| Lease liabilities non-current / current | 2025 | 16656 / 7042 | NOK k | AR2025, SoFP p. 65 |
| Non-current provision (NCI put liabilities, Notes 20–22) | 2025 | 55809 | NOK k | AR2025, SoFP p. 65 |
| Trade payables / income tax payable / social security | 2025 | 82763 / 18199 / 13020 | NOK k | AR2025, SoFP p. 65 |
| Prepayments from customers / other current liabilities | 2025 | 98445 / 71322 | NOK k | AR2025, SoFP p. 65 |
| Weighted average shares excl. own shares (no dilution) | 2025 | 100665 | thousand | AR2025, Note 14, p. 101 |
| Issued shares / treasury shares at 31.12 | 2025 | 107427112 / 9282931 | shares | AR2025, Note 12, p. 96; Note 14 |
| Revenue | 2024 | 623508 | NOK k | AR2025, SoCI p. 63 |
| OI | 2024 | 80615 | NOK k | AR2025, SoCI p. 63 |
| D&A | 2024 | 11616 | NOK k | AR2025, SoCI p. 63 |
| Financial income / expense / equity-accounted | 2024 | 27288 / 42563 / 34451 | NOK k | AR2025, SoCI p. 63 |
| Profit / attributable | 2024 | 85872 / 82670 | NOK k | AR2025, SoCI p. 63 |
| CFO / capex / investment in subsidiaries / repurchases | 2024 | 141550 / -25121 / -56299 / -48779 | NOK k | AR2025, cash flow p. 67 |
| Total assets / goodwill / other intangibles | 2024 | 818563 / 106132 / 96238 | NOK k | AR2025, SoFP p. 64 |
| PP&E / ROU / equity-accounted / cash | 2024 | 10113 / 14524 / 82163 / 204937 | NOK k | AR2025, SoFP p. 64 |
| Shareholders' equity / NCI / total liabilities | 2024 | 418574 / 70026 / 329964 | NOK k | AR2025, SoFP p. 65 |
| Lease liabilities nc / current; NC provision | 2024 | 9083 / 6039; 33767 | NOK k | AR2025, SoFP p. 65 |
| Trade payables / tax payable / social security / prepayments / derivatives / other current | 2024 | 45080 / 4944 / 11684 / 74629 / 11037 / 96720 | NOK k | AR2025, SoFP p. 65 |
| Weighted average shares | 2024 | 105182 | thousand | AR2025, Note 14, p. 101 |
| Revenue / OI / D&A | 2023 | 575086 / 101073 / 7685 | NOK k | AR2024, SoCI |
| Fin. income / fin. expense / equity-accounted | 2023 | 24099 / 8825 / -7083 | NOK k | AR2024, SoCI |
| Profit / attributable | 2023 | 83309 / 81243 | NOK k | AR2024, SoCI |
| CFO / capex / inv. in subsidiaries / repurchases / lease payments | 2023 | 75155 / -19240 / -2733 / -11009 / -3539 | NOK k | AR2024, cash flow statement |
| Total assets / goodwill / other intangibles / PP&E / ROU / equity-accounted / cash | 2023 | 600711 / 17050 / 50234 / 9188 / 13541 / 47712 / 194162 | NOK k | AR2024, SoFP |
| Shareholders' equity / NCI / total liabilities | 2023 | 404398 / 22548 / 173766 | NOK k | AR2024, SoFP |
| Lease nc / current; trade payables; tax payable; prepayments; other current; deferred tax | 2023 | 9087 / 4276; 57242; 1512; 39002; 36815; 17859 | NOK k | AR2024, SoFP |
| Revenue / OI (restated) / D&A | 2022 | 387503 / 56824 / 10475 | NOK k | AR2023, SoCI (AR2022 printed OI 51,766: restated, the later print governs; reconcile the 5,058 change at resume) |
| Fin. income / fin. expense (restated) | 2022 | 16921 / 31111 | NOK k | AR2023, SoCI (AR2022: 4,884 / 14,016) |
| Profit / attributable | 2022 | 32654 / 31839 | NOK k | AR2023, SoCI |
| CFO (restated) / capex / lease payments | 2022 | 28819 / -22401 / -1725 | NOK k | AR2023, cash flow (AR2022 printed CFO 37,950) |
| Total assets / goodwill / other intangibles / PP&E / ROU / cash | 2022 | 507143 / 16643 / 58035 / 9809 / 4409 / 181281 | NOK k | AR2023, SoFP |
| Shareholders' equity / NCI / total liabilities | 2022 | 330878 / 20090 / 156175 | NOK k | AR2023, SoFP |
| Lease nc / current; trade payables; tax payable; prepayments; other current | 2022 | 2716 / 1549; 45893; 1562; 42418; 46917 | NOK k | AR2023, SoFP |
| Revenue / OI / D&A | 2021 | 479983 / 134103 / 5665 | NOK k | AR2022, SoCI |
| Fin. income / fin. expense / profit / attributable | 2021 | 5696 / 7265 / 111621 / 110224 | NOK k | AR2022, SoCI |
| CFO / capex / lease payments | 2021 | -54595 / -26253 / -991 | NOK k | AR2022, cash flow |
| Total assets / goodwill / other intangibles / PP&E / cash | 2021 | 451241 / 16643 / 40084 / 14439 / 174501 | NOK k | AR2022, SoFP |
| Shareholders' equity / NCI / total liabilities | 2021 | 296952 / 19276 / 135013 | NOK k | AR2022, SoFP |
| Lease nc / current; trade payables; tax payable; prepayments; other current | 2021 | 4234 / 1566; 20682; 2618; 29456; 65439 | NOK k | AR2022, SoFP |
| Revenue / OI | 2020 | 359467 / 74626 | NOK k | AR2021, SoCI and segment note (continuing operations) |
| D&A | 2020 | 2746 | NOK k | AR2020, SoCI |
| CFO (restated) / capex | 2020 | 125421 / -12083 | NOK k | AR2021, cash flow (AR2020 capex line) |
| Total assets / goodwill / other intangibles / PP&E | 2020 | 558084 / 16643 / 26840 / 6224 | NOK k | AR2021 and AR2020, SoFP |
| Cash at 31.12 | 2020 | 355114 | NOK k | AR2021, cash flow opening balance 2021 (AR2020 printed 367,849: **extraction conflict**, rebuild from AR2021 SoFP at resume) |
| Equity: share capital / treasury / premium / other equity; NCI; total equity | 2020 | 11696 / -1 / 2751 / 171152; 17879; 203477 | NOK k | AR2021, SoFP (shareholders' equity 185,598 derived: sum of the four) |
| Total liabilities; trade payables; prepayments; current lease; other current | 2020 | 354607; 24616; 187469; 950; 127053 | NOK k | AR2021/AR2020, SoFP |
| Revenue / OI / D&A | 2019 | 266614 / 33074 / 3026 | NOK k | AR2019, SoCI (continuing) |
| CFO / capex / dividends paid | 2019 | 57658 / -13311 / -422450 | NOK k | AR2019 cash flow "A. Net cash flow from operating activities"; AR2020 cash flow (capex, dividends) |
| Total assets / intangibles (GW 16,643 + other 16,633) / PP&E / cash | 2019 | 416041 / 33276 / 7112 / 260948 | NOK k | AR2019, SoFP (AR2020 prints PP&E 6,528 for 2019: conflict, resolve at resume) |
| Shareholders' equity / NCI / total equity / total liabilities | 2019 | 217495 / 16050 / 233545 / 182496 | NOK k | AR2019, SoFP |
| Trade payables / income tax payable / prepayments / other current | 2019 | 14005 / 574 / 109293 / 37038 | NOK k | AR2019, SoFP |
| Revenue / OI / D&A (continuing, restated) | 2018 | 220310 / 15113 / 1887 | NOK k | AR2019, SoCI comparative |
| CFO | 2018 | 65239 | NOK k | AR2019 cash flow comparative (AR2018 printed 126,040: restated; reconcile basis — continuing vs total) |
| Total assets (incl. assets held for sale 1,916,148) / cash | 2018 | 2416036 / 349445 | NOK k | AR2019 and AR2018, SoFP |
| Intangibles+GW / PP&E | 2018 | 6081 / 13611 | NOK k | AR2018, SoFP |
| Shareholders' equity / NCI / total equity | 2018 | 357702 / 156528 / 514230 | NOK k | AR2019, SoFP |
| Total liabilities (incl. liabilities held for sale 1,356,637) | 2018 | 1901806 | NOK k | AR2019, SoFP |
| Trade payables / prepayments / other current | 2018 | 9715 / 130538 / 88523 | NOK k | AR2019, SoFP |
| Revenue / OI / D&A (continuing, restated) | 2017 | 211038 / 8835 / 1680 | NOK k | AR2018, SoCI comparative |
| CFO | 2017 | 25640 | NOK k | AR2018 cash flow comparative (AR2017 printed 84,399: restated) |
| Total assets (incl. HFS 1,941,413) / cash / intangibles+GW / PP&E | 2017 | 2328483 / 261843 / 6473 / 7322 | NOK k | AR2018, SoFP |
| Shareholders' equity / total equity / total liabilities (incl. LHFS 1,251,241) | 2017 | 456078 / 607460 / 1721023 | NOK k | AR2018, SoFP |
| Prepayments / other current | 2017 | 58469 / 32781 | NOK k | AR2018, SoFP |
| Revenue / OI (continuing, restated) | 2016 | 202339 / -15625 | NOK k | AR2017, SoCI comparative |
| Revenue / OI (as reported, whole TTS group, after 98,724 impairments) | 2016 | 3086706 / -71961 | NOK k | AR2016, SoCI |
| CFO (whole group) | 2016 | -94086 | NOK k | AR2016, cash flow |
| Total assets / goodwill / other intangibles / PP&E / cash | 2016 | 2175226 / 575799 / 89356 / 94338 / 175784 | NOK k | AR2016 SoFP (PP&E from AR2017 comparative) |
| Shareholders' equity / total equity / total liabilities | 2016 | 471937 / 616426 / 1558800 | NOK k | AR2016, SoFP |
| Prepayments / other current | 2016 | 249196 / 327589 | NOK k | AR2016, SoFP |
| Total assets / goodwill / other intangibles / cash | 2015 | 3025503 / 701807 / 122190 / 413210 | NOK k | AR2016, SoFP comparative |
| Shareholders' equity / total equity / total liabilities / prepayments / other current | 2015 | 634507 / 854566 / 2170938 / 633979 / 398430 | NOK k | AR2016, SoFP comparative |
| Revenue / OI (whole group) | 2015 | 3051243 / 32007 | NOK k | AR2016, SoCI comparative |

### Segment figures (B4 inputs, NOK k)

| item | FY | value | unit | source |
|---|---|---|---|---|
| Syncrolift ext. revenue / OI / capex | 2025 | 313653 / 38670 / 8688 | NOK k | AR2025 Note 1, p. 83 |
| Intellilift ext. revenue (total incl. internal 71,839) / OI / capex | 2025 | 38962 / 15616 / 404 | NOK k | AR2025 Note 1, p. 83 |
| Techano Oceanlift ext. revenue / OI / capex | 2025 | 114894 / -51981 / 6529 | NOK k | AR2025 Note 1, p. 83 |
| Globetech ext. revenue / OI / capex | 2025 | 103180 / 19509 / 3865 | NOK k | AR2025 Note 1, p. 83 |
| Other/elim. OI (incl. 13,724 impairment) | 2025 | -52525 | NOK k | AR2025 Note 1, p. 83 |
| Syncrolift / Intellilift / Techano / Globetech / Other OI | 2024 | 116745 / 3878 / -10503 / 8531 / -38035 | NOK k | AR2025 Note 1, p. 83 |
| Syncrolift / Intellilift / Techano / Other ext. revenue | 2024 | 491061 / 29241 / 63514 / 1799 (Globetech 37892) | NOK k | AR2025 Note 1, p. 83 |
| Syncrolift / Intellilift / Techano / Other total revenue; OI | 2023 | 515494 / 33854 / 30336 / 9816; 130049 / 4672 / 978 / -34626 | NOK k | AR2024 Note 1 |
| Syncrolift / Intellilift / Other total revenue; OI (restated) | 2022 | 383423 / 22384 / 11539; 91017 / 2662 / -36856 | NOK k | AR2023 Note 1 |
| Customers >10% of consolidated revenue (Syncrolift; Techano Oceanlift) | 2025 | 62700 / 82200 | NOK k | AR2025 Note 1, p. 84 (MNOK 62.7 and 82.2) |

### Gate 1C inputs found so far

| item | FY | value | unit | source |
|---|---|---|---|---|
| Treasury shares purchased (count / cash) | 2025 | 6026749 / 64266 | shares / NOK k | AR2025 Note 12, p. 96; cash flow p. 67 |
| Treasury shares purchased (count / cash) | 2024 | 4804327 / 48779 | shares / NOK k | AR2025 Note 12, p. 96; cash flow p. 67 |
| Treasury shares used for the Globetech acquisition | 2024 | 1482550 | shares | AR2025 Note 12, p. 96 |
| Treasury shares purchased (cash) | 2023 | 11009 | NOK k | AR2024 cash flow |
| Repurchases as a share of weighted average shares (derived) | 2025 / 2024 | 6.0% / 4.6% | % | derived: 6,026,749 ÷ 100,665k; 4,804,327 ÷ 105,182k — both above the ≈ 1% per-year floor |
| Largest holder: Skeie Teknologi AS (+ Skeie Consultants AS 1.4%, Skeie Kappa Invest AS 1.1%) | 31.12.2025 | 29.3% (votes 32.1%) | % | AR2025 Note 12, p. 96 |
| Board chair Håkon André Berg; CEO Ole Falk Hansen | 2026-04-30 | — | — | AR2025 signature page, p. 65 |

## 3. Readings settled (as far as the run got; no grade, no verdict)

- **Window and record:** P1 window FY2016–FY2025. The legal entity's audited statements exist for every year (TTS Group ASA to 2018, renamed Nekkar ASA 2019), so the run reads the record as full, not history-limited. **Owed reading:** FY2016 is printed both as the whole TTS group (AR2016) and restated to continuing operations (AR2017); FY2017–FY2018 balance sheets carry assets and liabilities held for sale (1.94bn and 1.92bn NOK) against continuing-only OI. The resume must fix one consistent J13 reading of CE for FY2016–FY2018 (latest restated print governs each figure; the harsher reading where two remain) and log it in Appendix C.
- **G6 (P31):** the equity-accounted FiiZK stake is 82,163 of 818,563 total assets at FY2024 (10.0%, derived) → the asset limb fails → both G6 readings are owed for every window year (associates' carrying values for FY2016–FY2022 still to collect; TTS-era 50/50 companies — AR2016 cites "consolidated 50/50 owned companies" — to check).
- **Group:** four material units at FY2025 (above). FiiZK becomes a consolidated unit only from Q3 2026 (after the latest FY): at FY2025 it is an associate, not a unit.
- **Concentration:** the filer names one >10% customer each in Syncrolift and Techano Oceanlift (FY2025).
- **SF:** repurchases above the per-year floor in FY2024 and FY2025 → the point-in-time worth table is owed; acquisition stop owed for Globetech (Aug 2024, cash 56,299 NOK k in "investment in subsidiaries" plus 1,482,550 treasury shares), the Techano Oceanlift purchase (first in the FY2023 segment note), FiiZK step-up and Satco (2026, live year).
- **Gate 2 pointer:** FY2025 J1 OI is negative (−30,711), so EV/OI is n.m. unless P28 qualifies FY2025 (impairment 13,724 and Techano losses; test owed with the Q1–Q3 2026 interims, whose EBIT reads −2 (Q2) and −3 (Q3) NOK m per the Q3 2026 report, "Profit & Loss" table; FY2025 EBIT −31).

## 4. Scope still owed (in order)

- [ ] Confirm ISIN NO0003049405 from a primary (Oslo Børs/Euronext or AR share note).
- [ ] Settle the FY2016–FY2018 TTS reading (CE with held-for-sale assets vs continuing OI) and build B1–B3 for FY2016–FY2025 from the table above; NIBCL per year (trade payables, tax payable, social security, accruals; prepayments from customers stay in CE unless the build rules otherwise — log the call).
- [ ] Collect, per year, equity-accounted carrying values and results (FY2016–FY2025) for the G6 readings; FY2023–FY2025 are in the table.
- [ ] P20 maintenance-capex build: k from net PP&E + capitalised development per year (AR notes 6–7), Norwegian CPI per year (SSB) as π_t, organic revenue (acquired revenue of Techano Oceanlift and Globetech per AR Note 21).
- [ ] Segment assets (AR2025 Note 1 or elsewhere) for B4 and the allocation-across-the-parts test; segment figures FY2023 Techano/Globetech context.
- [ ] Appendix D: one block per unit (Syncrolift, Intellilift, Techano Oceanlift, Globetech), each with the named-customer reading.
- [ ] Gate 1C: remuneration report 2025 (`https://www.nekkar.com/governance#documents`), pay table FY2023–FY2025, management holdings (AR2025 Note 12 / remuneration report), RPTs with Skeie entities (AR2025 Note 16), worth table for FY2023–FY2025 tranches at point of purchase, acquisition stop (AR2024/AR2025 Note 21; FiiZK and Satco 2026 announcements).
- [ ] Gate 2: Q3 2026 balance sheet (debt-equivalents: lease liabilities 55, interest-bearing 16 NOK m per Q3 report p. 18; NCI put liabilities; cash), TTM, P28 test, averaged readings, trigger band.

*Framework output, not investment advice.*
