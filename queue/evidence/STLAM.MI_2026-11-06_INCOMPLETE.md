# STLAM.MI — Stellantis N.V. — INCOMPLETE evidence, resumable record (ANALYSE 2026-11-06)

## 1. Header

- Key: STLAM.MI · job: ANALYSE · D 2026-11-06 · T 2042 · base sha 1e92ecba1da7593ea6834af7a5aac627046c0833
- Live `model_version`: v4.8.0
- Prior memo: none. There is no `memos/STLAM.MI/` or `archive/memos/STLAM.MI/` folder at base. No register row and no memo `company:` or `isin:` line matches "Stellantis", "Fiat Chrysler", "Peugeot" or the ISIN NL00150001Q9 (one grep over `memos/*/*.md` and `archive/memos/*/*.md`; `_REGISTER.md`).
- Identity: Stellantis N.V. (Dutch N.V., legal successor of Fiat Chrysler Automobiles N.V. renamed at the 16 Jan 2021 merger with Peugeot S.A.); ISIN **NL00150001Q9**; lines Euronext Milan `STLAM`, Euronext Paris `STLAP`, NYSE `STLA` (20-F FY2025, Item 4 front section). SEC CIK 1605484. The ISIN is from the listing record, not yet quoted from a primary page in this run: confirm it from the 20-F cover or the AFM register at resume.
- Named gap: **group build exceeds budget** (README §5; MODEL §8.7 item 6). This is the **first overrun**: the queue line carries no ` — partial …` note at base.
- Price endpoint (one GET, uncounted): `query1.finance.yahoo.com/v8/finance/chart/STLAM.MI` → HTTP 200, `currency` **EUR**, `exchangeName` MIL (Milan), instrument "Stellantis N.V.", `instrumentType` EQUITY. Close **4.02 EUR on 2026-11-06** (4.0200 regular-session; prior closes 3.9685 on 11-05, 4.155 on 11-04). The 1-month `events=split` check returned no events. `px_unit` = EUR.
- Fiscal year-end close for the P22 holding test: **9.461 EUR on 2025-12-30** (last Milan session of 2025; same endpoint, daily series 2025-12-24 → 2026-01-02).
- No grade, verdict or band is stated here. A "derived" figure is arithmetic on the cited figures, not a grade.

## 2. Per gate or leg — work done and figures

### Document route (all primary; SEC requests sent with the `sec_user_agent`; all HTTP 200)

| doc | accession / URL | notes |
|---|---|---|
| 20-F FY2025 | `https://www.sec.gov/Archives/edgar/data/1605484/000160548426000021/stellantis-20251231.htm` (acc. 0001605484-26-000021, filed 2026-02-26) | IS printed p. 198; BS p. 200; CF p. 201; Note 12 equity method pp. 261–263; Note 16 receivables from financing; Note 22 debt (maturity table); Note 29 EPS; Note 30 segments pp. 315–318; Remuneration report pp. 170–173; Major shareholders p. 11; Board table and share ownership (Item 6) |
| 20-F FY2024 | acc. 0001605484-25-000013, `…/000160548425000013/stellantis-20241231.htm` | IS (2024, 2023, 2022); remuneration table (Tavares 2024/2023); equity note: GM warrant buyback and 2024 programme |
| 20-F FY2023 | acc. 0001605484-24-000022, `…/000160548424000022/stellantis-20231231.htm` | IS (2023, 2022 and 2021 restated: equity-method share moved into OI); BS 2023/2022; CF 2023/2022/2021 (pre-reclassification); remuneration table (Tavares 2023/2022) |
| 20-F FY2022 | acc. 0001605484-23-000020, `…/000160548423000020/stellantis-20221231.htm` | IS 2022/2021/2020 (old presentation, equity share below OI) |
| 20-F FY2021 | acc. 0001605484-22-000023, `…/000160548422000023/stellantis-20211231.htm` | IS 2021/2020/2019 and CF 2021/2020/2019 (2020 and 2019 = PSA, the accounting acquirer, restated with Faurecia as discontinued); BS 2021/2020 |
| Merger prospectus (424B3) | acc. 0001605484-20-000174, `…/000160548420000174/fcanvprospectus.htm` (filed 2020-11-23) | PSA audited consolidated financial statements 2019, 2018, 2017 restated (auditors Mazars, EY et Autres): IS, BS, CF **with Faurecia consolidated**; PSA selected data 2015–2019 (summary BS lines only) |
| Q3 2026 interim report (6-K) | acc. 0001605484-26-000092, `…/000160548426000092/stellantisnvq32026interimr.htm` (filed 2026-10-28) | interim condensed IS (Q3 and 9M), BS 30 Sep 2026, CF 9M |
| H1 2026 semi-annual report (6-K) | acc. 0001605484-26-000064, `…/000160548426000064/stellantisnv20260630semi-a.htm` | located, not read |
| Stellantis IR site | `https://www.stellantis.com/en/investors/reporting/financial-reports` | HTTP 403 from the sandbox |

### Income statement (EUR m; J1 candidate = the face "Operating income/(loss)", the lowest operating subtotal; from FY2023 the face OI **includes** the share of equity-method results)

| item | FY | value | unit | source |
|---|---|---|---|---|
| Net revenues | 2025 / 2024 / 2023 | 153,508 / 156,878 / 189,544 | EUR m | 20-F FY2025 p. 198 |
| Net revenues | 2022 / 2021 | 179,592 / 149,419 | EUR m | 20-F FY2023 IS |
| Net revenues (PSA, Faurecia discontinued) | 2020 / 2019 | 47,656 / 58,993 | EUR m | 20-F FY2021 IS |
| Revenue (PSA incl. Faurecia) | 2019 / 2018 / 2017 | 74,731 / 74,027 / 62,256 | EUR m | 424B3, PSA consolidated income statement |
| Revenue (PSA incl. Faurecia, selected data) | 2016 / 2015 | 54,030 / 54,676 | EUR m | 424B3, "PSA Consolidated Income Statement Data" table |
| Operating income/(loss) (face, equity share inside) | 2025 / 2024 / 2023 | −26,254 / 3,687 / 22,376 | EUR m | 20-F FY2025 p. 198 |
| Operating income (face, restated, equity share inside) | 2022 / 2021 | 20,276 / 15,863 | EUR m | 20-F FY2023 IS |
| Operating income (old presentation, equity share below OI) | 2022 / 2021 / 2020 / 2019 | 20,012 / 15,126 / 3,010 / 3,655 | EUR m | 20-F FY2022 IS; 20-F FY2021 IS (2020, 2019 = PSA ex-Faurecia) |
| Operating income (PSA incl. Faurecia) | 2019 / 2018 / 2017 | 4,668 / 4,400 / 3,074 | EUR m | 424B3 PSA IS (charges inside: restructuring −1,531 / −1,051 / −951; impairment of CGUs −283 / −299 / −96) |
| Share of profit/(loss) of equity method investees | 2025 / 2024 / 2023 / 2022 / 2021 | −1,271 / −33 / 491 / 264 / 737 | EUR m | 20-F FY2025 p. 198; 20-F FY2023 IS |
| Share of profit/(loss) of equity method investees (below OI) | 2020 / 2019 | −74 / −62 | EUR m | 20-F FY2021 IS |
| Share in net earnings of equity method investments (PSA incl. Faurecia) | 2019 / 2018 / 2017 | −24 / −44 / 217 | EUR m | 424B3 PSA IS |
| Gains/(losses) on disposal of investments (inside OI) | 2025 / 2024 / 2023 / 2022 / 2021 | −1,839 / −98 / 20 / 72 / −35 | EUR m | 20-F FY2025 p. 198; 20-F FY2023 IS |
| Restructuring costs (inside OI) | 2025 / 2024 / 2023 / 2022 / 2021 | 913 / 1,617 / 1,119 / 1,144 / 698 | EUR m | same |
| Net financial expenses/(income) | 2025 / 2024 / 2023 / 2022 / 2021 | 351 / −345 / −42 / 768 / 734 | EUR m | same |
| Net profit/(loss) | 2025 / 2024 / 2023 / 2022 / 2021 (cont. ops) | −22,332 / 5,520 / 18,625 / 16,779 / 13,218 | EUR m | same |
| Net profit attributable to owners of the parent | 2025 / 2024 / 2023 / 2022 / 2021 | −22,368 / 5,473 / 18,596 / 16,799 / 14,200 (incl. 990 discontinued) | EUR m | same |
| Net profit attributable to owners (PSA) | 2020 / 2019 | 2,173 / 3,201 | EUR m | 20-F FY2021 IS |
| 9M operating income/(loss) | 9M-2026 / 9M-2025 | 1,059 / −8,411 | EUR m | Q3 2026 interim IS |
| 9M share of equity-method results | 9M-2026 / 9M-2025 | 86 / −498 | EUR m | same |
| 9M net revenues | 9M-2026 / 9M-2025 | 119,225 / 111,467 | EUR m | same |
| TTM OI to Q3-2026 | TTM | −16,784 (derived: −26,254 + 1,059 − (−8,411)) | EUR m | derived: items above |

FY2025 operating-loss charges named by the filer (Note 30 AOI reconciliation, total 25,412): restructuring 913; Takata recall 622; platform impairments 6,583; product-plan realignments and programme cancellations 9,072; other impairments 243; battery JVs 2,054; hydrogen programme discontinuation 1,094; CAFE penalty rate 269; Stellantis Türkiye disposal 246; change in estimate for contractual warranties 4,130; other 186. FY2024 (total 4,961): restructuring 1,617; impairment expense and supplier obligations 1,807; Takata 768; lifetime onerous contracts 637; other 132. FY2023 (total 1,967): restructuring 1,161; collective agreements 428; Argentina devaluation 302; impairments 201; other items as printed. None is added back (J1); they matter only for the P28 test (§3 below).

### Balance sheet (EUR m, 31 Dec; 2020 = PSA restated, Faurecia out)

| item | 2025 | 2024 | 2023 | 2022 | 2021 | 2020 | source |
|---|---|---|---|---|---|---|---|
| Goodwill and indefinite-life intangibles | 29,176 | 31,986 | 30,994 | 31,738 | 29,921 | 6,327 | 20-F FY2025 p. 200; FY2023 BS; FY2021 BS |
| Other intangible assets | 15,709 | 22,379 | 20,625 | 19,006 | 16,635 | 8,694 | same |
| Property, plant and equipment | 42,958 | 45,011 | 37,687 | 36,205 | 35,488 | 15,983 | same |
| Equity method investments | 7,276 | 9,100 | 8,070 | 4,834 | 6,022 | 3,152 | same |
| Non-current financial assets | 1,794 | 3,294 | 3,269 | 710 | 607 | 412 | same |
| Inventories | 22,153 | 20,861 | 21,414 | 17,360 | 11,361 | 5,366 | same |
| Assets sold with a buy-back commitment | 3,616 | 1,938 | 1,328 | 1,594 | 2,134 | 793 | same |
| Trade receivables | 5,662 | 5,506 | 6,426 | 4,928 | 2,998 | 4,923 | same |
| Other current assets and prepaid expenses | 15,770 | 12,973 | 10,288 | 7,549 | 6,362 | 2,393 | same |
| Current financial assets | 1,987 | 3,872 | 6,830 | 4,323 | 1,903 | 935 | same |
| Cash and cash equivalents | 30,146 | 34,100 | 43,669 | 46,433 | 49,629 | 22,893 | same |
| Total assets | 195,153 | 207,607 | 202,128 | 186,156 | 171,766 | 75,285 | same |
| Equity attributable to owners of the parent | 53,551 | 81,692 | 81,693 | 71,999 | 55,907 | 21,293 | same |
| Non-controlling interests | 450 | 423 | 427 | 383 | 400 | 2,580 | same |
| Long-term debt | 31,826 | 25,028 | 20,001 | 19,469 | 22,624 | 11,068 | same |
| Short-term debt and current portion of LT debt | 14,121 | 12,199 | 9,462 | 7,684 | 10,958 | 2,635 | same |
| Trade payables | 29,999 | 29,684 | 33,008 | 31,726 | 28,181 | 15,955 | same |
| Current tax liabilities | 491 | 475 | 1,264 | 900 | 546 | 128 | same |
| Other liabilities (current) | 19,265 | 17,558 | 15,570 | 14,528 | 14,439 | 8,569 | same |
| Other non-current liabilities | 5,475 | 5,980 | 8,065 | 8,129 | 7,696 | 4,681 | same |
| Provisions, non-current / current | 18,596 / 14,317 | 8,860 / 14,220 | 7,744 / 13,724 | 8,460 / 11,311 | 7,270 / 9,909 | 1,610 / 4,114 | same |
| Employee benefits liabilities, non-current / current | 4,795 / 517 | 5,441 / 583 | 4,911 / 562 | 5,891 / 545 | 8,065 / 684 | 1,463 / 50 | same |
| Deferred tax liabilities | 1,294 | 4,507 | 4,784 | 4,332 | 4,374 | 801 | same |

PSA incl. Faurecia (424B3, PSA consolidated statement of financial position): total assets 2019 / 2018 / 2017 = 69,766 / 61,952 / 57,915; equity excl. NCI (share capital + treasury + retained) 19,074 / 17,085 / 14,564 (derived: 905 − 240 + 18,409; 905 − 270 + 16,450; 905 − 270 + 13,929); NCI 2,727 / 2,509 / 2,142; trade payables 14,505 / 13,551 / 13,362; other payables 8,869 / 8,293 / 8,139; current provisions 4,941 / 5,065 / 4,782; non-current financial liabilities 8,917 / 5,257 / 4,778; current financial liabilities 2,520 / 2,182 / 2,531; equity-method investments (manufacturing + finance companies) 3,323 / 3,444 / 3,472; cash (manufacturing + finance companies) 17,833 / 15,426 / 11,894. PSA selected data (424B3): total assets 2016 / 2015 = 45,153 / 49,110; total equity 14,618 / 12,219; cash 12,098 / 10,896. The FY2015 and FY2016 full balance sheets are not in any document read.

**30 Sep 2026** (Q3 2026 interim BS): total assets 214,407; equity attributable 61,291 (includes the hybrid perpetual notes issued in 2026); NCI 472; long-term debt 39,778; short-term debt 16,221; cash 29,046; current financial assets 1,749; non-current financial assets 4,451; equity method investments 7,507; trade payables 30,973; employee benefits liabilities 4,441 + 562; provisions 15,498 + 15,291; assets held for sale 323, liabilities held for sale 178. **Hybrid perpetual notes issued 9M-2026: 4,927** (CF financing line; coupons paid 77) — a Gate-2 debt-equivalent at 100% whatever its equity classification.

### Debt detail, 31 Dec 2025 (Note 22 maturity table, EUR m; 2024 in brackets)

Notes 23,201 (19,117); borrowings from banks 1,960 (3,572); asset-backed financing 15,479 (10,016); lease liabilities 2,454 (2,556); other debt 2,853 (1,966); **total debt 45,947 (37,227)**. Asset-backed financing is mainly SFS U.S. securitisation: 14,759 (9,866) (Note 22, "Asset-backed financing"). Debt excluding lease liabilities 43,493 carrying, fair value 42,852.

### Consolidated financial services (the captive arm)

Receivables from financing activities (Note 16), 31 Dec 2025 / 2024: dealer financing 3,087 / 2,330; retail financing 10,703 / 8,494; finance leases 540 / 299; other 1,401 / 1,408; **total 15,731 / 12,531** ("mainly … financial services companies fully consolidated"; the €3.2bn increase in 2025 mainly South America and North America). The consolidated arm sits in "Other activities" (Note 30). The European captive finance is equity-accounted (JVs with Santander Consumer Finance and BNP Paribas PF; Leasys SAS 50%), outside the consolidated record.

### Cash flow (EUR m)

| item | 2025 | 2024 | 2023 | 2022 | 2021 | source |
|---|---|---|---|---|---|---|
| CFO (current presentation) | −4,650 | 1,535 | 17,954 | n/a | n/a | 20-F FY2025 p. 201 (2024 and 2023 reclassified: financing-receivables change moved into CFO) |
| CFO (old presentation) | — | — | 22,485 | 19,959 | 18,646 | 20-F FY2023 CF |
| of which net change in receivables related to financial services | −4,867 | −3,455 | −3,586 | (−1,413 in investing, old presentation) | (−306 in investing) | same |
| of which change in carrying amount of leased vehicles | −5,379 | −3,885 | −1,747 | −483 | 358 | same |
| Dividends received (in CFO) | 276 | 335 | 312 | n/a | n/a | 20-F FY2025 p. 201 |
| Investments in PP&E and intangible assets | −7,987 | −11,060 | −10,193 | −8,615 | −8,687 | same; 20-F FY2023 CF |
| Change in amounts payable on PP&E and intangibles | −1,155 | 223 | 1,068 | −399 | −1,426 | same |
| Depreciation and amortisation | 6,981 | 7,226 | 7,549 | 6,797 | 5,871 | same |
| Acquisitions of subsidiaries, equity-method and other investments | −425 | −1,652 | −3,885 | −666 | −726 | same |
| Changes in loans to JVs and associates | 91 | −696 | −248 | n/a | n/a | 20-F FY2025 p. 201 |
| Distributions to Stellantis shareholders | −1,959 | −4,651 | −4,208 | −3,353 | −4,204 | same |
| (Purchases)/sales of treasury shares | — | −3,000 | −2,434 | −923 | — | same |

PSA (20-F FY2021 CF, Faurecia discontinued): CFO 2020 / 2019 = 6,241 / 8,667 including discontinued-operations CFO 1,136 / 1,837, so continuing CFO 5,105 / 6,830 (derived); investments in PP&E and intangibles −2,733 / −3,544; D&A 2,376 / 2,191. PSA incl. Faurecia (424B3 PSA CF): CFO 8,705 / 8,395 / 5,459 (2019 / 2018 / 2017); investments in PP&E −2,765 / −2,510 / −2,351 and intangibles −2,146 / −2,061 / −1,947; depreciation, amortisation and impairment 3,717 / 2,995 / 2,754; change in leased vehicles 50 / 226 / −90.

9M-2026 (Q3 2026 interim CF): CFO −6,817 (9M-2025 −6,838), incl. change in leased vehicles −2,591 and financing receivables −4,281; investments in PP&E and intangibles −4,551 (−6,187).

### Shares and holders

| item | FY | value | unit | source |
|---|---|---|---|---|
| Weighted average shares, diluted | 2025 / 2024 / 2023 / 2022 / 2021 | 2,886,684 / 2,975,820 / 3,132,458 / 3,163,959 / 3,151,432 | thousand | 20-F FY2025 Note 29; 20-F FY2023 EPS note (2021 = 17 Jan–31 Dec 2021) |
| Weighted average shares, basic | 2025 / 2024 / 2023 | 2,886,684 / 2,949,652 / 3,107,725 | thousand | 20-F FY2025 Note 29 |
| Issued common shares | 2026-02-25 | 2,903,716,295 (plus 866,522,224 class A special voting shares) | shares | 20-F FY2025 p. 11 |
| Exor N.V. | 2026-02-25 | 449,410,092 common = 15.48% of common; 23.84% of voting power (loyalty voting) | — | 20-F FY2025 p. 11 |
| Établissements Peugeot Frères (Peugeot Invest / Peugeot 1810) | 2026-02-25 | 224,228,121 common = 7.72%; 11.89% of votes | — | same |
| Bpifrance Participations | 2026-02-25 | 192,703,907 common = 6.64%; 10.22% of votes | — | same |
| Executive directors' holdings | 2026-02-26 | John Elkann (Chairman, Executive Director) 1,227,009; Antonio Filosa (CEO, Executive Director) 414,737 | shares | 20-F FY2025 Item 6, Directors' share ownership; board table ("Chairman and Executive Director") |
| PSA→Stellantis exchange ratio | 2021-01-16 | 1.742 FCA (Stellantis) shares per PSA share | — | 20-F FY2022 Item 10 share capital |

### Listed holdings and equity-method classes (Note 12, 20-F FY2025 pp. 261–263)

Equity-method investments 31 Dec 2025 / 2024: joint ventures 5,229 / 7,037 (SCF finance JVs 2,098 / 2,016; BNPP PF finance JVs 1,084 / 1,086; Tofaş 37.9%, 1,042 / 1,101; NextStar 0 / 897; StarPlus 703 / 763; ACC 0 / 429; Leasys 207 / 424; Symbio 0 / 197; others 95 / 124); associates 2,026 / 2,015 (Leapmotor 20.0% / 21.3%, 1,274 / 1,349; Archer 8.0% / 16.0%, 218 / 206; Nordex 137 / 148; 360 Energy 103 / 113; Comau 49.9% 109 / 124; STM Financial 86 / —; others 99 / 75); other 21 / 48. Market value of the interests at 31 Dec 2025 (2024): **Leapmotor 1,511 (1,147); Tofaş 929 (1,056); Archer 382 (533)**. SCF JVs' share of net profit 2025 / 2024 / 2023: 228 / 229 / 314.

### Segments (Note 30, 20-F FY2025; EUR m; segment measure = Adjusted operating income, AOI; filer adjustments = the J1 charges allocated by segment)

| segment | rev 2025 | rev 2024 | rev 2023 | AOI 2025 | AOI 2024 | AOI 2023 | adjustments 2025 / 2024 / 2023 | equity-method share 2025 / 2024 / 2023 |
|---|---|---|---|---|---|---|---|---|
| North America | 60,962 | 63,450 | 86,500 | −1,892 | 2,660 | 13,298 | 17,464 / 1,239 / 1,033 | 37 / −8 / −6 |
| Enlarged Europe | 57,773 | 59,010 | 66,598 | −651 | 2,419 | 6,519 | 6,491 / 1,939 / 497 | −1,282 / −310 / −139 |
| Middle East & Africa | 9,709 | 10,097 | 10,560 | 1,429 | 1,901 | 2,503 | 284 / 24 / 31 | 60 / 51 / 192 |
| South America | 16,197 | 15,863 | 16,058 | 1,963 | 2,272 | 2,369 | 308 / 88 / 272 | −3 / 1 / 16 |
| China and India & Asia Pacific | 1,868 | 1,993 | 3,528 | 74 | −58 | 502 | −8 / 18 / 84 | 3 / −72 / 18 |
| Maserati | 726 | 1,040 | 2,335 | −198 | −260 | 141 | 620 / 1,548 / 1 | — |
| Other activities | 6,870 | 6,151 | 5,211 | −726 | 144 | −322 | 262 / 63 / 42 | −86 / 305 / 410 |
| Unallocated & eliminations | −597 | −726 | −1,246 | −841 | −430 | −667 | −9 / 42 / 7 | — |
| Stellantis | 153,508 | 156,878 | 189,544 | −842 | 8,648 | 24,343 | 25,412 / 4,961 / 1,967 | −1,271 / −33 / 491 |

Note 30: "Operating assets are not included in the data reviewed by the chief operating decision maker … the related information is not provided." Other activities holds the financial services activities, pre-owned cars, mobility, software and data, Archer and other investments (and industrial automation until its December 2024 disposal). From 1 Jan 2026 the Maserati segment is folded into the regions.

### Remuneration (20-F remuneration reports; "Total Remuneration", LTI at IFRS accounting expense; EUR)

| person | FY | base | fringe | STI | LTI (expense) | post-retirement | other | total | source |
|---|---|---|---|---|---|---|---|---|---|
| Carlos Tavares (CEO to Dec 2024) | 2022 | 2,000,000 | 14,345 | 7,480,000 | 11,594,661 | 2,370,000 | — | 23,459,006 | 20-F FY2023 table |
| Carlos Tavares | 2023 | 2,000,000 | 634,697 | 5,786,800 | 26,125,828 | 1,946,700 | — | 36,494,025 | 20-F FY2023 / FY2024 tables |
| Carlos Tavares | 2024 | 2,000,000 | 71,224 | — | 20,514,494 (incl. 10,000,000 Transformation Incentive) | 500,000 | — | 23,085,718 | 20-F FY2024 table |
| Carlos Tavares (former CEO) | 2025 | — | 1,896 | — | 9,926,170 | — | 2,000,000 | 11,928,066 | 20-F FY2025 p. 172 |
| Antonio Filosa (CEO from 2025) | 2025 | 1,424,359 | 374,194 | — | 1,508,985 | 192,366 | 1,924,779 | 5,424,683 | 20-F FY2025 p. 172 |
| John Elkann (Chairman, Executive Director) | 2025 / 2024 / 2023 / 2022 | 960,293 / 922,386 / 924,404 / 951,519 | 396,849 / 721,830 / 684,230 / 1,124,290 | — | 1,093,796 / 1,153,062 / 3,214,886 / 3,774,242 | — | — | 2,450,938 / 2,797,278 / 4,823,520 / 5,850,051 | 20-F FY2025 p. 172; FY2023 table |
| Highest outside-director fee | 2025 | Henri de Castries 275,000 + 16,018 = 291,018 | | | | | | | 20-F FY2025 p. 172 |

Filosa's 2025 package (p. 170): base US$1.8m; STI target 200%; cash awards US$1.2m on 31 Dec 2025, 2026 and 2027; annual equity grant 500% of base target. Other bases (grant-date value, realised or vested pay, Dutch statutory table) are not yet read.

### Repurchases

| year | cash | shares | price | counterparty / programme | source |
|---|---|---|---|---|---|
| 2022 | 923 | 69,125,544 | 13.36 per share (5-day VWAP, Milan) | GM warrant shares issued on 15 Sep 2022 and immediately repurchased; cancelled April 2023 | 20-F FY2023 / FY2024 equity note |
| 2023 | 2,434 | n/a (owed) | n/a | Feb 2023 programme up to €1.5bn, plus other purchases (owed: split) | 20-F FY2023 CF; equity note |
| 2024 | 3,000 | n/a (owed) | n/a | Feb 2024 programme up to €3.0bn, open market, Feb–2024 (end date owed); cap 110% of market price; up to €0.5bn for equity plans | 20-F FY2024 equity note; CF |
| 2025 | — | — | — | none | 20-F FY2025 CF |

## 3. Readings settled (figures in the tables above; no grade or verdict)

- **Reporting entity and record.** Stellantis is the legal successor of FCA N.V., but PSA is the accounting acquirer (reverse acquisition, 16 Jan 2021): the 20-F comparatives for 2020 and 2019 are PSA's, restated with Faurecia as a discontinued operation. PSA's own audited statements for 2017–2019 (424B3) consolidate Faurecia. Unsettled: whether the P1 window FY2016–FY2025 runs on PSA's audited record before 2021 (perimeter break at the merger, and a Faurecia break between the 424B3 and the 20-F restatement), or whether the pre-2021 years are read history-limited. Decide at resume, logging the call; the FY2015 and FY2016 PSA full statements are needed only on the first reading.
- **J1 OI line.** The face "Operating income/(loss)" is the lowest operating subtotal and carries restructuring, impairments, disposal results and (from the FY2023 presentation, restated back to 2021) the share of equity-method results. Gate 2 under J3's one-way rule: the FY2025 equity-method loss (−1,271) and disposal loss (−1,839) stay in OI. FY2025 J1 OI = −26,254.
- **P31: above the line.** FY2025 exclude-reading OI = −24,983 (derived: −26,254 + 1,271) is ≤ 0, and the class income is not nil, so the income limb fails in FY2025; both G6 readings are owed for the whole window. Equity-method carrying value / total assets: 3.7% (2025), 4.4% (2024), 4.0% (2023), 2.6% (2022), 3.5% (2021), 4.2% (2020; derived from the BS table). S3 stakes, non-current financial assets and loans to JVs still have to be added to the class sum.
- **P22 listed holdings: none material.** MCap at FY2025 year-end ≈ 27,311 (derived: 9.461 × 2,886.684m diluted weighted shares; ≈ 27,472 on the 2,903.7m issued common shares). Leapmotor 1,511 = 5.5%, Tofaş 929 = 3.4%, Archer 382 = 1.4% of that MCap; their sum (2,822) is under ⅓ of MCap. All three stay equity-accounted G6 classes (associate or JV) in Gate 1A, with no credit at Gate 2; `holding_keys` n.m. and `core_credit` 0 unless the resume finds a different year-end share count that moves Leapmotor past 10% (it cannot: 1,511 ÷ 0.10 = 15,110 < any plausible MCap).
- **P22 units, FY2025.** Revenue shares: North America 39.7%, Enlarged Europe 37.6%, South America 10.6%, Middle East & Africa 6.3%, Other activities 4.5%, China/India/AP 1.2%, Maserati 0.5%. Σ positive AOI 3,466 (MEA 1,429, SA 1,963, CIAP 74): MEA 41.2%, SA 56.6%, CIAP 2.1%. On segment results after the filer's allocated adjustments (MEA 1,145, SA 1,655, CIAP 82; Σ 2,882) the set is the same. Material units: **North America, Enlarged Europe, South America, Middle East & Africa**. Immaterial: CIAP, Maserati, Other activities (which holds the consolidated captive finance arm). No segment assets (Note 30), so the asset leg of P22 is not available.
- **P29 weights.** North America's 3-year average segment result after the allocated J1 charges is ≤ 0 (derived: (−19,356 + 1,421 + 12,265) ÷ 3 = −1,890), so every weight uses the latest-3-FY average revenue: NA 70,304, EE 61,127, MEA 10,122, SA 16,039 (Σ 157,592) → **weights NA 44.6%, EE 38.8%, SA 10.2%, MEA 6.4%**. No ungradeable listed part.
- **Allocation across the parts (§2·1C·3).** No segment assets are published (Note 30): the test is INDETERMINATE (b), with its re-test named at the memo.
- **L/E, FY2025.** Total liabilities 141,152 (derived: 195,153 − 54,001) ÷ equity attributable 53,551 = **263.6%**, against the P5 line of 200%. The P6 route needs every other Past metric at the P2 level; ΔOI/sh read (i) is n.m. (FY2025 OI ≤ 0), and the include-reading 3-year endpoint average of OI 2023–2025 is ≤ 0 (derived: (22,376 + 3,687 − 26,254) ÷ 3 = −64).
- **P28, FY2025.** Test 3 fails on the record: FY2024 carried impairment expense and supplier obligations of 1,807 (49.0% of FY2024 OI 3,687) and restructuring of 1,617 (43.9%), charges of the kinds named for FY2025 above 10% of OI within the four prior years. The latest year governs Gate 2; P28 does not apply.
- **TTM.** TTM OI to Q3-2026 (−16,784) is above FY2025 (−26,254), so it does not replace the latest FY (TTM only when lower).
- **Gate-2 inputs owed but bounded.** FY2025 CFO −4,650. Adding back the whole financing-receivables change (−4,867) and the whole leased-vehicles change (−5,379), which overstates the R2 rule's ±3% removal, gives at most 5,596 (derived) against investments in PP&E and intangibles of 7,987.
- **Votes versus economics (V4).** Exor holds 23.84% of the votes on 15.48% of the common shares (1.54×): separated, as an input only.
- **Alignment inputs.** Executive directors hold 1,641,746 shares directly (derived: 1,227,009 + 414,737) = 0.06% of issued common shares, worth 6.6m at px (derived: × 4.02). Whether John Elkann's look-through economic interest in Exor's 449.4m shares (through Giovanni Agnelli B.V. and Dicembre, entities he controls) counts as his holding, and at what economic percentage, is unsettled: it can move the P23 call. The other executive officers' holdings are not yet read.
- **Pay year totals on the one basis read.** 2025: Tavares 11,928,066, Filosa 5,424,683; 2024: Tavares 23,085,718; 2023: Tavares 36,494,025 (the largest in a FY2023–FY2025 table on this basis). Other bases owed before the hairiest number is fixed.

## 4. Scope still owed (in this order)

- [ ] Confirm the ISIN NL00150001Q9 from a primary page (20-F FY2025 cover or AFM register).
- [ ] Settle the record reading (§3 first bullet). If PSA's audited record governs before 2021: PSA FY2015 and FY2016 full statements (PSA Document de référence 2016 and 2015, AMF / info-financiere.fr; stellantis.com returns 403), and decide how the Faurecia perimeter in the 424B3 2017–2019 statements meets the 20-F 2019–2020 restatement.
- [ ] B1–B3 on both G6 readings (P31 above the line): per year the class carrying values (equity-method investments, S3 stakes in non-current financial assets, loans to JVs) and income (equity-method share; dividends received 276 / 335 / 312 in CFO for 2025 / 2024 / 2023; the 2021–2022 dividends from the old-presentation CF note 30); NIBCL per year (trade payables, current tax, the accrued-expense part of other liabilities; provisions stay in CE unless shown to be accruals; log each call).
- [ ] The R2 captive-arm build: financing-receivables book per year (Note 16) and the leased-vehicles / buy-back book; the ±3% rule on each; ABS funding as a debt-equivalent; both funding pairings at Gate 2 (OI before and after the arm's funding cost, from the SFS figures in Note 30 Other activities or the financial-services disclosures).
- [ ] P20 per year: capex is "investments in PP&E and intangible assets" (capitalised development inside); net fixed capital = PP&E (ROU and leased vehicles out) + capitalised development; k over the window; HICP (euro area) deflators; FY2021 is a deal year (FCA merger) with no organic disclosure → all capex that year unless organic figures are printed; floor = depreciation of PP&E + amortisation of capitalised development.
- [ ] Appendix D blocks for North America, Enlarged Europe, South America and Middle East & Africa (dealers and fleet customers as payers; search the 20-F for a group customer statement; supplier concentration on batteries and semiconductors; forces, moat, market).
- [ ] Appendix E: pay on every basis (grant-date values in the LTI tables; realised/vested; Dutch statutory table), the hairiest number against the P17 lines (loss years FY2025, and FY2024 if its maintenance-capex FCF ≤ 0); outside directors (de Castries 291,018 against the cap); executive officers' holdings and the Elkann look-through question; worth table for the 2022 (GM warrants, 69.1m shares at 13.36), 2023 (2,434) and 2024 (3,000) tranches at the point of purchase (trailing-3 reads published before each purchase; share counts and dates from the programme reports); acquisition stop for the trailing three FYs and the live year (Leapmotor 21% stake, Oct 2023; FY2023 aggregate acquisitions 3,885; later deals), and write-downs (FY2025 battery-JV and other impairments) against allocators in office.
- [ ] Gate 2 at px 4.02: MCap on the latest share count (H1/Q3 2026 interim); debt-equivalents at 30 Sep 2026 (total debt 55,999 incl. leases and ABS; hybrid perpetual 4,927; net unfunded pensions from the H1 2026 note; supplier finance; guarantees of the finance JVs' or battery JVs' debt; NCI at book 472); cash 29,046 plus S1 securities in current financial assets 1,749 (class split owed); FY2025 core OI −26,254 and the FY2025 maintenance-capex FCF; 3-year and 5-year averages.
- [ ] Then the memo (group: B4 Division table, P29 S, Appendix D × 4, the allocation table as INDETERMINATE (b)), the row file from `row-from-memo --table`, and deletion of this record.

*Framework output, not investment advice.*
