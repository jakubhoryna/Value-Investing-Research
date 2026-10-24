# LAGR-B.ST — Lagercrantz Group AB (publ) — INCOMPLETE evidence (ANALYSE 2026-10-24 1026)

- Run: routine ANALYSE, MODEL v4.6.1, base b996c82a305bac92d3ee2b9f296556e5b31e6fa9, PR #224.
- **Named gap: price endpoint HTTP 429.** The README §5 price endpoint `query1.finance.yahoo.com/v8/finance/chart/LAGR-B.ST` answered "Edge: Too Many Requests" (HTTP 429) on every one of 37 GETs between 08:27 and 09:17 UTC (plain requests, 60–90 s apart; the session proxy reported healthy, no relay failures). Without it the key, `px_unit`, `px`, `px_date` and the split check cannot be recorded (MODEL §7.1a), and the cheapness leg cannot be computed. The price exists; it could not be retrieved (D3). No other quote source was substituted, because `px_unit` must be the endpoint's own `currency`.
- **No verdict.** Every figure below is sourced from primary documents and reusable by the re-run; only the price-dependent lines (MCap, multiples, trigger legs, the alignment value) are owed. Nothing here is a grade.

## Identity and documents

- Company: Lagercrantz Group AB (publ), Nasdaq Stockholm, B share `LAGR B`, **ISIN SE0014990966** (AR 2025/26, share data), listed since 3 September 2001. Class A shares (9,775,386, 10 votes) are unlisted. 3:1 share split in autumn 2020. Fiscal year ends 31 March.
- Prior-check: no `memos/LAGR-B.ST/` or `archive/memos/LAGR-B.ST/`, no register row and no memo front matter matching "Lagercrantz" or the ISIN (the name appears only as a peer in the LIFCO-B.ST and INDT.ST memos).
- Documents (all retrieved 2026-10-24; Lagercrantz via MFN `storage.mfn.se` and Cision `mb.cision.com`, located through the MFN news feed `feed.mfn.se/v1/feed/b6f366be-c350-48f3-959f-ed07a2047191.json`): Annual Reports 2016/17 (part 2), 2017/18, 2018/19, 2019/20, 2020/21, 2021/22, 2022/23, 2023/24, 2024/25, 2025/26; Interim Reports Q2 2025/26, Q1 2026/27 (2026-07-17), Q2 2026/27 (1 April–30 September 2026, published 2026-10-23). Exploratory searches: 1 (annual-report locator).
- SCB CPI fiscal-year (April–March) averages FY2017–26 as tabulated in the ADDT-B.ST memo v1 (same fiscal years): 1.2, 1.9, 2.0, 1.6, 0.6, 2.9, 10.06, 6.88, 1.9, 0.5%.

## B1 record (SEK m; FY = year ending 31 March)

| FY | Revenue | Reported EBIT | Contingent-consideration reversal (net, J3) | J1 OI | Reported CFO | Financial income | CFO less fin. income | Capex (intangibles + PP&E) | Maint. capex (P20) | Basis | FCF (maint.) | Dil. sh (m, split-adjusted) | Total assets | NIBCL | Cash | Equity | GW+intang | Owned PP&E |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 3,057 | 315 | 6 (+ disposal gain 11) | 298 | 257 | 7 | 250 | 73 | 73 | = all capex | 177 | 204.363 | 2,582 | 444 | 67 | 1,032 | 1,143 | 206 |
| 2017 | 3,096 | 361 | 5 | 356 | 375 | 7 | 368 | 55 | 55.0 | = all capex | 313.0 | 204.291 | 2,891 | 487 | 122 | 1,197 | 1,296 | 224 |
| 2018 | 3,410 | 378 | 38 | 340 | 282 | 7 | 275 | 60 | 60.0 | = all capex (tier 3) | 215.0 | 203.772 | 3,632 | 540 | 134 | 1,303 | 1,703 | 251 |
| 2019 | 3,932 | 451 | 4 | 447 | 462 | 11 | 451 | 80 | 69.2 | constructed | 381.8 | 203.046 | 3,854 | 638 | 139 | 1,508 | 1,798 | 266 |
| 2020 | 4,180 | 483 | 16 | 467 | 507 | 14 | 493 | 96 | 96.0 | = all capex | 397.0 | 203.616 | 4,349 | 705 | 117 | 1,684 | 1,995 | 301 |
| 2021 | 4,091 | 529 | 5 | 524 | 782 | 18 | 764 | 87 | 87.0 | = all capex | 677.0 | 203.673 | 4,610 | 745 | 151 | 1,855 | 2,097 | 340 |
| 2022 | 5,482 | 781 | 12 | 769 | 594 | 12 | 582 | 123 | 81.0 | constructed | 501.0 | 204.102 | 6,207 | 1,006 | 210 | 2,228 | 2,732 | 415 |
| 2023 | 7,246 | 1,062 | 3 | 1,059 | 1,070 | 47 | 1,023 | 178 | 178.0 | = all capex | 845.0 | 204.718 | 8,033 | 1,254 | 360 | 3,009 | 3,964 | 608 |
| 2024 | 8,129 | 1,256 | 24 | 1,232 | 1,327 | 32 | 1,295 | 125 | 125.0 | = all capex | 1,170.0 | 206.227 | 9,842 | 1,486 | 355 | 3,468 | 5,152 | 695 |
| 2025 | 9,389 | 1,439 | 41 | 1,398 | 1,322 | 45 | 1,277 | 169 | 169.0 | = all capex | 1,108.0 | 206.553 | 11,222 | 1,491 | 456 | 3,837 | 6,106 | 753 |
| 2026 | 10,609 | 1,694 | 30 | 1,664 | 1,502 | 22 | 1,480 | 214 | 214.0 | = all capex | 1,266.0 | 206.537 | 12,771 | 1,714 | 331 | 4,436 | 7,075 | 849 |

- J1 OI = EBIT (the lowest operating subtotal, after acquired-intangible amortisation) less net positive reversals of contingent considerations (other operating income less other operating expenses lines, latest presentation). NIBCL = trade payables + tax liabilities + accrued expenses and deferred income + contract liabilities + advance payments from customers. Other liabilities (contingent considerations, minority put/call options, other) stay in CE. Equity is attributable to the parent; the group recognises no NCI (minority shares sit as put/call-option liabilities).
- P20: k = Σ owned PP&E ÷ Σ revenue FY2017–26 = 4,702 ÷ 59,564 = 0.0789. Organic growth printed: FY2019 7%, FY2020 0%, FY2021 −4%, FY2022 16%, FY2023 10%, FY2024 −1%, FY2025 2%, FY2026 3%; FY2017 not printed (reported +1.3%, below π); FY2018 not printed and deals above 1% of EV → tier 3. Growth capex FY2019 10.8 (real growth 136.4), FY2022 42.0 (531.8); floors (PP&E depreciation) 42 and 66 not binding. Pre-IFRS 16 operating-lease commitments 124 / 210 / 156 / 148 (FY2016–19), 3.8–7.3% of total assets: not capitalised.
- Averages (latest FY included): OI 3y 1,431.3, 5y 1,224.4; maintenance FCF 3y 1,181.3, 5y 978.0 (all-capex 1,181.3 and 969.6).
- No equity-accounted associates, no S3 securities, no insurance activity: G6 below the P31 line. Lens test: no bank, insurer, lending book or captive finance arm.

## Returns and growth (worked; price-independent)

- Worst-of-four ROCE (beg_wc · end_wc · beg_xc · end_xc): ten-year 17.0 · 14.4 · 17.8 · 15.0%; five-year 18.0 · 14.9 · 18.9 · 15.5%; latest three 17.3 · 14.7 · 18.1 · 15.3%.
- Worst-of-four FCFROCE (maintenance): ten-year 14.2 · 12.0 · 14.8 · 12.5%; five-year 14.4 · 11.9 · 15.1 · 12.4%; latest three 14.3 · 12.2 · 15.0 · 12.7%.
- Per-year beginning-CE ROCE_wc: 16.7, 14.1, 14.5, 14.5, 14.4, 19.9, 20.4, 18.2, 16.7, 17.1%; FCFROCE_wc: 14.6, 8.9, 12.3, 12.3, 18.6, 13.0, 16.2, 17.3, 13.3, 13.0%. End-of-period FCFROCE_xc: 13.7, 7.3, 12.4, 11.3, 18.2, 10.0, 13.2, 14.6, 11.9, 11.8%. No series shows three consecutive declines ending in the latest two years; the latest-three averages sit above the window's.
- ΔOI/sh: geometric +18.6%, endpoint +20.6%. ΔFCF/sh (maintenance): geometric +21.6%, endpoint +21.2%. L/E FY2026 187.9% (8,335 ÷ 4,436). TBV negative at every year-end (−2,639 at FY2026; −3,280 at 30 Sep 2026).
- TTM to 30 Sep 2026: EBIT 1,838 less contingent reversals 44 ≈ J1 OI 1,794 (above FY2026); CFO 1,498, gross capex ≈ 202 (approximate), interim financial income not disclosed: TTM FCF ≈ SEK 1.27–1.30bn, at or above FY2026's 1,266. FY2026 governs both.

## Units (AR 2024/25 and 2025/26 Note 3; FY2024 restated onto the current segmentation)

| Unit | FY2026 share of external revenue | Segment EBITA FY2024 / 25 / 26 | Segment EBIT FY2024 / 25 / 26 | Segment assets Mar 2024 / 25 / 26 | EBITA margin FY2024 / 25 / 26 (H1 FY2027 vs H1 FY2026) |
|---|---|---|---|---|---|
| Electrify | 24.8% | 312 / 387 / 543 | 290 / 353 / 504 | 2,080 / 2,788 / 2,853 | 17.1 / 16.8 / 20.5% (20.4 vs 19.7%) |
| Control | 12.6% | 144 / 175 / 228 | 121 / 150 / 204 | 1,002 / 1,355 / 1,446 | 14.2 / 14.6 / 17.0% (13.6 vs 15.6%) |
| TecSec | 21.8% | 367 / 359 / 339 | 312 / 300 / 276 | 2,124 / 2,139 / 2,767 | 17.8 / 16.5 / 14.6% (14.2 vs 14.9%) |
| Niche Products | 22.5% | 399 / 479 / 492 | 358 / 427 / 432 | 2,353 / 2,660 / 2,953 | 22.6 / 22.0 / 20.6% (22.2 vs 19.9%) |
| International | 18.2% | 252 / 273 / 358 | 218 / 237 / 316 | 1,654 / 1,528 / 2,124 | 16.8 / 17.4 / 18.5% (16.1 vs 18.8%) |

- P29 weight bases (3-year average segment EBIT): 382.3 / 158.3 / 296.0 / 405.7 / 257.0 → weights 0.255 / 0.106 / 0.197 / 0.271 / 0.171.
- Pooled FY2024–26 segment EBIT ÷ assets: 14.9 / 12.5 / 12.6 / 15.3 / 14.5%; segment-asset growth Mar 2024 → Mar 2026: +773 / +444 / +643 / +600 / +470.
- Customer disclosure: the risk section says "The Group has a broad customer and supplier base where no single party accounts for more than 5% of revenue. Meanwhile, dependence on individual relationships is a significant risk at subsidiary level, especially where the operations are based on a few key customers or suppliers." No division-level customer statement or table. "Credit risk is generally spread over a large number of customers" (credit statement).

## Shareholder-friendliness inputs

- CEO Jörgen Wigh total remuneration (Note 5, home statutory table): FY2024 11,792; FY2025 13,288; FY2026 15,279 (SEK '000). EVP/Head of Acquisitions 5,761 / 7,226 / 8,230. NI 877 / 1,019 / 1,200. Chair Fredrik Börjesson SEK 1.565m (FY2026).
- Holdings at 31 Mar 2026: Jörgen Wigh 698,998 A + 1,760,350 B = 2,459,348 (1.19% of 206.191m outstanding; 3.0% of votes). Anders Börjesson & Tisenhult group 8,190,630 A + 3,445,650 B: 5.6% of capital, 29.0% of votes. Directors and close family control about 32% of votes (Note 38). No related-party transactions beyond intra-group (Note 38; Q2 interim).
- Repurchases: none of own shares FY2019–26 and the live year; FY2018 SEK 32m, FY2016 SEK 10m. Employee call-option buy-backs SEK 80m (FY2025), 32m (FY2026), 45m (H1 FY2027). Treasury 3,026,886 B shares (30 Sep 2026).
- Acquisitions (Note 35, filer pro forma): FY2024 consideration 1,542, IB debt assumed 17, cash acquired 140, full-year OP before acquisition costs 204, surplus amortisation 33; FY2025 1,447 / 67 / 152 / 143 / 38; FY2026 1,276 / 137 / 153 / 164 / 28. Live year (allocations since 1 Oct 2025): 1,447, IB debt 115, cash 140, acquiree profit not yet disclosed. No goodwill impairment in FY2025–26 (Note 16).
- Dividends to parent shareholders FY2017–26: 119, 136, 135, 169, 135, 204, 265, 329, 392, 453 (SEK 2,337m); 515 paid in Q2 FY2027.

## EV inputs at 30 Sep 2026 (SEK m; price-independent)

- Interest-bearing liabilities excl. pensions 5,554 (incl. lease liabilities 476) + pensions 55 + contingent considerations 393 (fair value; maximum 483) + minority put/call-option liabilities 649 = **debt-equivalents 6,651**. Cash 419. Equity 4,630; goodwill 4,669; other intangibles 3,241.
- Shares: 206,191,347 outstanding after repurchases; call options 757,000 at SEK 144.50 (2023/27), 788,000 at 233.90 (2024/28), 759,300 at 276.60 (2025/29) — treasury method at px, owed with the price.
- Price-dependent arithmetic, owed: with N ≈ 206.4m the EV/OI no-cash leg is (7 × 1,664 − 6,651) ÷ N ≈ SEK 24.2, the all-cash leg ≈ SEK 26.2, the FCF leg 8 × 1,266 ÷ N ≈ SEK 49.1 (context, not a trigger: N moves with px). The interim's "latest price paid" on 30 Sep 2026 was SEK 212.80 (filer KPI table; not the endpoint).

## Hosts tried

- `query1.finance.yahoo.com` — HTTP 429 "Edge: Too Many Requests", 37 attempts 08:27–09:17 UTC.
- `www.lagercrantz.com` (IR page; reports load through a Modular Finance widget) — 200, no PDF links; `mfn.se` and `feed.mfn.se` — 200; `storage.mfn.se`, `mb.cision.com` — 200 for every document listed.
