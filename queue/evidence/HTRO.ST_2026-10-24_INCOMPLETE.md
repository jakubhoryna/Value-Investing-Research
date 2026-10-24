# HTRO.ST — Hexatronic Group AB (publ) — INCOMPLETE evidence (ANALYSE 2026-10-24 2126)

- Run: routine ANALYSE, MODEL v4.6.1, base 52571cb100f859da70ebe808b7904980cd3982a6, PR #257.
- **Named gap: price endpoint HTTP 429.** The README §5 price endpoint `query1.finance.yahoo.com/v8/finance/chart/HTRO.ST` answered "Edge: Too Many Requests" (HTTP 429) on every one of 41 GETs between 19:27 and 20:21 UTC (plain requests, about 75 s apart; the session proxy reported healthy). Without it the key, `px_unit`, `px`, `px_date` and the split check cannot be recorded (ANALYSE.md step 5; MODEL §7.1a), so no memo is written (README §5, D3).
- **No verdict.** Every figure below is sourced from primary documents and reusable by the re-run; only the price-dependent lines (MCap, multiples, the alignment value) are owed. Nothing here is a grade.

## Identity and documents

- Company: Hexatronic Group AB (publ), Nasdaq Stockholm `HTRO`, **ISIN SE0018040677** (issuer's MFN entity record; split notice of 30 May 2022: 5:1, new ISIN from 2 June 2022). One ordinary share class; 4,730,366 C shares (1/10 vote, no dividend) held by the company for LTIPs.
- Prior-check: no `memos/HTRO.ST/` or `archive/memos/HTRO.ST/`, no register row and no memo front matter matching "Hexatronic" or the ISIN.
- Documents (all retrieved 2026-10-24 via the MFN feed `feed.mfn.se/v1/feed/abde977a-bd49-4bf1-960f-09e990fbca71.json`, attachments on hugin.info, ml-eu.globenewswire.com and storage.mfn.se): Årsredovisning 2015/2016 and 2016/17 (16 months to 31 Dec 2017); Annual Reports 2018–2020; Annual and Sustainability Reports 2021–2025; Year-End Report 2016-17; Interim report Jan–Sep 2025; Year-end report 2025; Interim report Q3 2026; press releases on the split, the 2023 repurchase and the 2025/2026 C-share issues. ECB USD/SEK 9.2098 (2025-12-31).

## Record (SEK m; FY2016/17 is 16 months; leases capitalised in the three pre-IFRS 16 years)

| FY | Revenue | OI (J1) | CFO | Capex | Maint. capex | Basis | FCF (maint.) | FCF (all-capex) | Dil. sh (m) | Total assets | NIBCL | Cash+STI | Total liab | Equity | GW+intang |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2015/16 | 890.9 | 63.6 | 76.9 | 28.5 | 28.5 | = all capex | 48.4 | 48.4 | 176.366 | 734.6 | 139.4 | 51.1 | 433.7 | 300.8 | 93.1 |
| 2016/17 | 1,717.8 | 155.6 | 145.6 | 37.7 | 37.7 | = all capex | 108.0 | 108.0 | 189.243 | 904.1 | 203.2 | 108.2 | 488.8 | 415.3 | 118.6 |
| 2018 | 1,597.8 | 86.2 | 52.6 | 41.0 | 41.0 | = all capex | 11.5 | 11.5 | 183.381 | 1,503.3 | 232.2 | 84.6 | 1,008.9 | 494.4 | 454.5 |
| 2019 | 1,842.3 | 97.8 | 173.6 | 81.8 | 75.6 | constructed | 98.1 | 91.8 | 186.087 | 1,497.9 | 233.2 | 103.8 | 923.5 | 574.4 | 434.3 |
| 2020 | 2,080.8 | 176.4 | 249.6 | 65.0 | 36.4 | constructed | 213.2 | 184.6 | 187.817 | 1,953.3 | 376.4 | 212.3 | 1,303.7 | 649.5 | 548.4 |
| 2021 | 3,491.6 | 355.1 | 104.6 | 202.3 | 56.8 | constructed | 47.8 | −97.7 | 195.491 | 4,715.2 | 750.7 | 675.1 | 3,067.7 | 1,642.1 | 1,385.2 |
| 2022 | 6,574.0 | 1,027.6 | 667.5 | 479.0 | 176.2 | constructed | 491.3 | 188.5 | 203.997 | 7,388.4 | 1,246.8 | 552.0 | 4,583.2 | 2,768.2 | 2,490.8 |
| 2023 | 8,150 | 1,122 | 936 | 519 | 436.6 | constructed | 499.4 | 417 | 203.454 | 8,733 | 945 | 813 | 5,296 | 3,402 | 2,978 |
| 2024 | 7,581 | 680 | 909 | 325 | 325 | = all capex | 584 | 584 | 204.454 | 8,962 | 1,081 | 633 | 4,904 | 4,022 | 3,041 |
| 2025 | 7,519 | 226 | 571 | 98 | 98 | = all capex | 473 | 473 | 205.555 | 8,057 | 1,118 | 661 | 4,589 | 3,437 | 2,835 |

OI (J1) = reported operating profit, the lowest operating subtotal (EBITA is struck before acquired-intangible amortisation; adjusted EBITA also excludes the 2025 non-recurring items), less, under J3, positive remeasurements of additional purchase prices in other operating income (FY2016/17 9.2; FY2018 9.2; FY2019 8.6; FY2020 0.9) and FY2015/16 negative goodwill (1.6); plus, in the three pre-IFRS 16 years, the imputed interest on capitalised operating leases (2.2, 3.2, 2.8; Appendix C). Reported operating profit: 62.9, 161.6, 92.5, 106.4, 177.3, 355.1, 1,027.6, 1,122, 680, 226. Patent-dispute cost recoveries (FY2016/17 6.9, FY2018 1.5), grants, exchange differences and gains on equipment stay operating. FY2025 OI carries SEK 298m of items the filer calls non-recurring (impairment of tangible and right-of-use assets SEK 163m, restructuring in the performance-improvement programme). CFO = reported CFO less interest received (0.1, 0.2, 0.2, 0.3, 0.2, 0.1, 2.0, 8, 12, 13; interest paid is already in CFO), plus, in the pre-IFRS 16 years, operating-lease payments less imputed interest (20.3, 43.1, 37.2). Capex = acquisitions of tangible plus intangible assets. Diluted shares: weighted average after dilution, pre-split counts × 5 (5:1 split, June 2022). Equity attributable to the parent (NCI 5.4–37). Total assets and total liabilities in FY2015/16, FY2016/17 and FY2018 include the capitalised leases (129.4, 127.0, 200.2). Opening balance sheet 31 Aug 2015 (AR2015/2016): total assets 482.0 (593.5 with leases of 111.5), NIBCL 108.5, cash 45.9, total liabilities 233.1, equity 249.0, goodwill and intangibles 82.4. Averages (latest FY included): OI 3-year 676.0, 5-year 682.1; maintenance FCF 3-year 518.8, 5-year 419.1 (all-capex 491.3 and 313.0).

## Worked figures (price-independent)

### Returns (FY2016/17 flows × 12/16 for the return tests; beginning-of-period CE; FCFROCE on maintenance-capex FCF)

| FY | CE_wc (end) | CE_xc (end) | ROCE_wc | ROCE_xc | FCFROCE_wc | FCFROCE_xc |
|---|---|---|---|---|---|---|
| 2015/16 | 595.1 | 544.1 | 13.1% | 14.5% | 10.0% | 11.0% |
| 2016/17 | 700.9 | 592.6 | 19.6% | 21.4% | 13.6% | 14.9% |
| 2018 | 1,271.1 | 1,186.5 | 12.3% | 14.5% | 1.6% | 1.9% |
| 2019 | 1,264.7 | 1,160.9 | 7.7% | 8.2% | 7.7% | 8.3% |
| 2020 | 1,576.9 | 1,364.6 | 13.9% | 15.2% | 16.9% | 18.4% |
| 2021 | 3,964.5 | 3,289.4 | 22.5% | 26.0% | 3.0% | 3.5% |
| 2022 | 6,141.6 | 5,589.6 | 25.9% | 31.2% | 12.4% | 14.9% |
| 2023 | 7,788 | 6,975 | 18.3% | 20.1% | 8.1% | 8.9% |
| 2024 | 7,881 | 7,248 | 8.7% | 9.7% | 7.5% | 8.4% |
| 2025 | 6,939 | 6,278 | 2.9% | 3.1% | 6.0% | 6.5% |

- Opening CE (31 Aug 2015, leases capitalised): CE_wc 485.0, CE_xc 439.1.
- Worst-of-four ROCE (beg_wc · end_wc · beg_xc · end_xc): ten-year 12.5 · 10.4 · 13.9 · 11.5%; five-year 12.5 · 10.4 · 13.9 · 11.6%; latest three 9.3 · 9.0 · 10.2 · 9.9%.
- Worst-of-four FCFROCE (maintenance): ten-year 8.0 · 6.7 · 9.0 · 7.4%; five-year 7.7 · 6.4 · 8.6 · 7.1%; latest three 7.1 · 6.9 · 7.9 · 7.6%. All-capex: ten-year 6.3 · 5.2 · 7.0 · 5.8%; five-year 5.7 · 4.8 · 6.4 · 5.3%.
- Beginning-of-period ROCE_wc fell in 2023, 2024 and 2025 (25.9 → 18.3 → 8.7 → 2.9%): three consecutive declines ending in the latest year (J6 limb (a) series). The latest-three averages are 13% below the window's (limb (b) threshold one third).
- G6: shares in associates 13–14 (end-2024, end-2025), 0.2% of total assets; no S3, non-operating loans or insurance activity: below the P31 line.

### Growth and leverage (per diluted share; flows as reported)

| FY | ΔOI/sh | ΔFCF/sh (maint.) | ΔBV/sh | ΔTBV/sh | L/E |
|---|---|---|---|---|---|
| 2015/16 | n/a | n/a | n/a | n/a | 144.2% |
| 2016/17 | +128.0% | +107.9% | +28.6% | +33.1% | 117.7% |
| 2018 | −42.8% | −89.0% | +22.9% | −86.1% | 204.1% |
| 2019 | +11.9% | +738.6% | +14.5% | +246.2% | 160.8% |
| 2020 | +78.6% | +115.5% | +12.0% | −28.5% | 200.7% |
| 2021 | +93.4% | −78.4% | +142.9% | +144.0% | 186.8% |
| 2022 | +177.3% | +884.2% | +61.5% | +3.5% | 165.6% |
| 2023 | +9.5% | +1.9% | +23.2% | +53.3% | 155.7% |
| 2024 | −39.7% | +16.4% | +17.6% | +130.2% | 121.9% |
| 2025 | −66.9% | −19.4% | −15.0% | −39.0% | 133.5% |

- ΔOI/sh geometric +13.2%, endpoint +29.2%; ΔFCF/sh (maintenance) geometric +26.6%, endpoint +35.5%; ΔBV/sh geometric +28.9%; ΔTBV/sh +10.6%. L/E FY2025 133.5% (4,589 ÷ 3,437).
- Averages (latest FY included): OI 3-year 676.0, 5-year 682.1; maintenance FCF 3-year 518.8, 5-year 419.1 (all-capex 491.3, 313.0).
- P28 inputs for FY2025: OI 226 below both averages; SEK 298m of non-recurring items (impairment of tangible and right-of-use assets 163, restructuring) = 65% of the shortfall against the 5-year average; FY2024 (680) not down (5-year 672.2); no such items in 2021–24 (adjusted EBITA = EBITA); OI before the named charges 524, below the lower average 676.0. FCF 473 is above its lower average.

### P20 maintenance capex (k = 0.1943; π = max(3%, Swedish CPI); organic growth as printed)

| FY | Organic growth | π | Real growth (prior revenue × (organic − π)) | Growth capex | Capex | Maint. capex | Floor | Bound |
|---|---|---|---|---|---|---|---|---|
| 2015/16 | n/p | — | — | — | 28.5 | 28.5 | — | tier 3 |
| 2016/17 | n/p | — | — | — | 37.7 | 37.7 | — | tier 3 |
| 2018 | n/p | — | — | — | 41.0 | 41.0 | — | tier 3 |
| 2019 | 5% | 3.00% | 32.0 | 6.2 | 81.8 | 75.6 | 25.2 | — |
| 2020 | 11% | 3.00% | 147.4 | 28.6 | 65.0 | 36.4 | 29.8 | — |
| 2021 | 39% | 3.00% | 749.1 | 145.5 | 202.3 | 56.8 | 42.2 | — |
| 2022 | 53% | 8.37% | 1,558.3 | 302.8 | 479.0 | 176.2 | 74.1 | — |
| 2023 | 15% | 8.55% | 424.0 | 82.4 | 519 | 436.6 | 142 | — |
| 2024 | −13% | 3.00% | negative | 0 | 325 | 325 | 179 | = capex |
| 2025 | 3% | 3.00% | 0 | 0 | 98 | 98 | 192 | = capex (floor above capex) |

### Units (AR2025 Note 5; segments from 2025, 2024 restated; no segment assets)

| Part | Kind | Net sales (2024 / 25) | Segment EBITA (2024 / 25) | Adjusted EBITA (2024 / 25) | Weight base (2-yr avg revenue) | Revenue weight |
|---|---|---|---|---|---|---|
| Fiber Solutions | unit | 5,441 / 4,870 | 587 / 26 | 587 / 310 | 5,155.5 | 0.682 |
| Harsh Environment | unit | 1,178 / 1,241 | 121 / 137 | 121 / 139 | 1,209.5 | 0.160 |
| Data Center | unit | 972 / 1,409 | 154 / 252 | 154 / 252 | 1,190.5 | 0.158 |
| Corporate/Elimination | — | −11 / −1 | −60 / −80 | −60 / −70 | — | — |

- Three biggest customers 2025: SEK 259m, 252m, 217m; "no single customer accounts for more than 10 percent of the Group's sales". 2025 sales by region: Europe 4,243, North America 2,591, APAC 685.
- Fiber Solutions: industry overcapacity and price pressure (AR2024, AR2025); segment EBITA 587 → 26 (adjusted 310).

### EV inputs at 30 Sep 2026 (Interim report Q3 2026)

- Liabilities to credit institutions 1,984; lease liabilities 473 (346 + 127); additional purchase prices and acquisition options (incl. redeemable minorities) 379; NCI at book 31 → debt-equivalents 2,867. Cash 678. Equity attributable 4,865; intangible assets 3,462.
- Shares: 221,448,661 ordinary (after a SEK 584m new issue in 2026) + 0.080m dilutive = 221.529m; 4,730,366 C shares held by the company.
- FY2025 J1 OI 226 and maintenance FCF 473 (both above-TTM checks: LTM EBIT 663, LTM FCF ≥ 657, so the fiscal year governs). EV/OI legs: 7 × 226 − 2,867 = −1,285 (no positive no-cash or all-cash price); FCF leg 8 × 473 ÷ 221.529 = SEK 17.08.

### Shareholder-friendliness inputs (AR2023–AR2025 Note 10; Notes 9; MFN press releases)

| Executive | 2023 | 2024 | 2025 |
|---|---|---|---|
| CEO Henrik Larsson Lyon (to Feb 2025): salary + variable + share-based + benefits + pension | 5.8 + 0.6 + 1.7 + 0.1 + 1.7 = 9.8 | 5.8 + 0.7 + 1.1 + 0.1 + 1.7 = 9.3 | 2.8 |
| CEO Rikard Fröberg (from 1 Mar 2025) | — | — | 4.6 + 4.2 + 0.4 + 0.1 + 0.1 = 9.4; with the LTIP 2025 grant (189,000 rights × SEK 32.2, the filer's maximum programme cost of SEK 24m ÷ 745,824 rights; labelled estimate) **≈ 15.5 (hairiest)** |
| Deputy CEO Martin Åberg | 6.2 | 6.2 | 7.3 |
| Other senior executives (aggregate; members) | 21.8 (7) | 23.4 (8) | 22.3 (7) |

- FY2025 NI attributable −14 (loss year); outside-director cap ≈ US$666k × 9.2098 = SEK 6.13m; chair fee SEK 1.1m.
- Management holdings (7 March 2026): Fröberg 200,000; Lindén 63,737; Åberg 83,784 privately plus 3,658,449 via part ownership of Chirp AB (share undisclosed); Angermund 215,547; Lundstedt 8,602; Schönbeck 34,096; Skov 23,569. Largest holder Handelsbanken Fonder 9.3%; no pool ≥ 20% of votes.
- Repurchases: 1,200,000 shares for SEK 80.4m at SEK 67.0 (May–June 2023); C-share issues and repurchases at quota value for LTIP 2025 and 2026. RPT: premises from Fastighets AB Balder (SEK 6m, 2024), arm's length.

| FY | Deal | EV (price + assumed financial liabilities − acquired cash) | Full-year pro forma EBITDA | EV ÷ EBITDA (lower bound on EV/OI) |
|---|---|---|---|---|
| 2023 | Rochester Cable, Fibron, ATG, USNet (aggregate) | 988 + 132 − 75 = 1,045 | 158 | 6.6× |
| 2024 | MConnect, Endor (asset deal) | not material (filer: no material impact) | — | — |
| 2025 | Communication Zone (Nov) | 285 − 44 = 241 | 39 | 6.2× |
| 2026 (live) | JOWO Systemtechnik (Apr), Superior Fiber & Data Services (Jun) | 551 − 51 = 500 | 93 (70 for nine months, annualised) | 5.4× |

