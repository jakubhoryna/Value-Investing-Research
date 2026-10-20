---
ticker:             INVE-B.ST
company:            Investor AB
exchange:           Nasdaq Stockholm (XSTO), B share
isin:               SE0015811963
currency:           SEK
memo_date:          2026-10-21
memo_version:       v3
supersedes:         archive/memos/INVE-B.ST/INVE-B.ST_2026-10-05_GSC.md
model_version:      v4.6.1
price_at_memo:      "SEK 413.70 (INVE B, Nasdaq Stockholm close 20 Oct 2026)"
mcap_at_memo:       "≈ SEK 1,268.2bn (413.70 × 3,065.6m diluted shares, both share classes at the B price)"
verdict:            AVOID
quality_past:       WEAK
quality_future:     WEAK
sf:                 FAIL
cheapness:          EXPENSIVE
window:             "FY2016–FY2025 (10y; 11 balance sheets FY2015–FY2025) + Q3 2026 interim"
trigger_band:       "CHEAP n.m. — no positive price (EV/OI no-cash leg −SEK 29.3/sh: debt-equivalents SEK 141.0bn exceed 7 × OI SEK 51.2bn; restoring OI ≈ SEK 20.1bn; all-cash leg −SEK 17.0/sh; MCap/FCF leg SEK 3.42); holding credits owed (no current holding memo); no P12"
# --- machine fields
aliases:            "INVE-A.ST A share"
px:                 413.70
px_unit:            SEK
px_date:            2026-10-20
trigger:            n.m.
mcap_fcf:           966.6
ev_oi:              192.8
ev_oi_all_cash:     187.6
trigger_basis:      no-cash
mcap_fcf_3y:        517.0
mcap_fcf_5y:        955.6
ev_oi_3y:           185.3
ev_oi_5y:           220.9
lens:               STD
holding_keys:       n.m.
core_credit:        0
core_period:        "FY2025; BS 2026-09-30"
core_currency:      SEK
core_unit:          m
core_shares_diluted: 3065.6
core_debt_eq:       140981
core_cash:          37775
core_oi:            7311
core_oi_basis:      FY2025 J1 · fin. income out
core_fcf:           1312
core_fcf_basis:     FY2025 CFO − maint. capex (constructed) · fin. income out
core_oi_3y:         7603.3
core_oi_5y:         6378.4
core_fcf_3y:        2453
core_fcf_5y:        1327.2
core_fcf_all:       1312
core_fx:            1
core_fx_date:       2026-10-20
core_ratio:         1
past_reason:        0.4% ROCE
future_reason:      sub dependency
sf_reason:          compensation
next_review_short:  2027-01-22
# --- end of machine fields
next_review:        "Earlier of: a current memo landing for ABB, ATCO-B.ST, SAAB-B.ST, AZN.L or SEB-A.ST (parent re-run owed); a MODEL decision on queue/IDEAS.md §I (holding companies); Year-end report 2026 (22 Jan 2027: window roll, Nova Biomedical's first full year)"
position:           —
extraction_conflicts: "AR 2025 note 5 prints net cash for subsidiary acquisitions of 23,572 against 23,532 in the cash-flow statement (40 unexplained); note 11's 2025 D&A total (6,612) is 77 below the asset-note sum; the five-year summary prints 2024 net debt −21,194 against −12,194 everywhere else (typo). FY2023 and FY2024 repurchases differ between the cash-flow statement (226; 356) and the equity note (199; 229). None moves a gate; the statement figures are used."
---

# INVE-B.ST — Investor AB: GSC Memo

## 1. Verdict

Understanding PASS · Past WEAK (0.4% ROCE) · Future WEAK (sub dependency) · Shareholder-friendliness FAIL (compensation) · Cheapness EXPENSIVE → **AVOID** on three gates (was WATCH).

Investor is a conservatively financed owner of Nordic industrial champions. v2's WATCH priced it on net asset value, which the framework no longer allows for any holding company. Read as one company, three gates fail. Two fails come from how the rules read a holding company: the five largest stakes have no current memo, so they count as unread parts, and once dividends and value changes are stripped out almost no net income is left, so ordinary pay trips the proportionality strike. One fail is the business itself: Patricia Industries earns 3.6–5% on capital that is 60% acquisition goodwill and intangibles. Price is far from any line. Even with every stake credited at market, the rest of the price pays about 50 times Patricia's operating income. A flip needs current memos for the five holdings and a framework decision on holding companies.

## 2. Understanding

Investor AB is a Stockholm industrial holding company, founded in 1916 and controlled by the Wallenberg foundations (the largest holds 20.1% of capital and 43.0% of votes). Its value lies in stakes in thirteen listed companies (72% of adjusted assets at end-2025) and in EQT and its funds (9%). All of its revenue, SEK 64.8bn in 2025 (60% from US customers), comes from Patricia Industries' majority-owned companies (19%). They sell wound-care, surgical, diagnostic and urology products, emergency-medical supplies, wheelchairs, accessible vehicles and vacuum-automation components to hospitals, health systems, distributors, payers and manufacturers. **PASS.**

Parts:
- **Patricia Industries**: nine companies led by Mölnlycke, plus 40% of Tre Skandinavien.
- **Investments in EQT**: 14.4% of EQT AB plus EQT fund commitments.
- **ABB**: electrification and automation equipment.
- **Atlas Copco**: compressors, vacuum pumps and industrial tools.
- **Saab**: defence systems, sold mainly to governments.
- **AstraZeneca**: prescription medicines.
- **SEB**: a Nordic universal bank.

| Part | Kind | Weight | Future · reason | Past (holdings, information) | Source memo |
|---|---|---|---|---|---|
| Patricia Industries | unit | 32.3% | ADEQUATE | consolidated | this memo |
| Investments in EQT | unit | 0.0% | WEAK · ungradeable | consolidated | this memo |
| ABB | holding (14.4%) | 24.4% | WEAK · sub dependency | n.m. | `ABB` v4 (MODEL v4.3.0: stale) |
| Atlas Copco | holding (17.1%) | 15.2% | WEAK · sub dependency | n.m. | `ATCO-B.ST` v2 (MODEL v4.0.0: stale) |
| Saab | holding (30.2%) | 10.1% | WEAK · sub dependency | n.m. | none |
| AstraZeneca | holding (3.3%) | 9.1% | WEAK · sub dependency | n.m. | none |
| SEB | holding (21.8%) | 8.9% | WEAK · sub dependency | n.m. | none |

## 3. Quality — past record

Lens STD. No holding has a current memo, so every stake is read both ways. Without the stakes, the record is Patricia plus the parent's costs: worst-of-four ROCE 3.6% over ten years and 3.8% over five, FCFROCE 0.7% on maintenance-capex FCF (constructed, mostly equal to all capex). With the stakes, dividends come in, but so do up to SEK 1.1trn of market-value capital and the 2018 and 2022 value losses: the worst of eight is 0.4% (five-year window). Operating income per share grew 6.7% a year; FCF per share is n.m. Book value per share compounded at 13.4%. Liabilities are 16% of book. **WEAK** on the ROCE level under both readings, and on growth.

## 4. Quality — future

Patricia is graded on Mölnlycke, its largest company. No customer exceeds 10% of group sales (filer statement). One force is STRONG, hospital and purchasing-group buying power, contained: the EBITA margin held near 25% in 2024–25. The clinician-preference brand moat is stable, and wound care is growing. Patricia: ADEQUATE. Investments in EQT cannot be graded: the filings describe neither EQT's paying clients nor the funds' companies. The five material holdings carry 68% of the weight base, and none has a current memo (ABB's and Atlas Copco's predate MODEL v4.5.0), so each counts WEAK. S = 1.32. **WEAK** (sub dependency).

## 5. Shareholder-friendliness

The hairiest printed total is CEO Christian Cederholm's SEK 38.2m (2025, grant basis); the former CEO reached about SEK 72.6m in 2024 on a vested basis. Net income stripped of every dividend and value change was SEK 118m in 2023 and negative in 2024–25. Against it, pay is a proportionality strike in 2023 and a loss-year strike in 2025. Management holds SEK 240m of stock, 6.3 times the hairiest number: WEAKLY ALIGNED; votes are separated. Nova Biomedical, bought at about 21 times pre-deal profit, is a CAUTION. **FAIL** at step 1 (compensation strike).

## 6. Price

| Metric | Current | Threshold | Rank | Pass/Fail |
|---|---|---|---|---|
| MCap / FCF (FY2025, maint. capex) | 966.6× | ≤ 8 | Primary | Fail |
| EV / OI no-cash / all-cash (FY2025 J1) | 192.8× / 187.6× | ≤ 7 | Primary | Fail |
| MCap / BV (30 Sep 2026) | 1.15× | ≤ 3 | Qualifier | Pass |
| MCap / TBV | 1.30× | ≤ 3 | Qualifier | Pass |
| MCap/FCF 3y · 5y | 517.0× · 955.6× | context | — | — |
| EV/OI 3y · 5y (no-cash / all-cash) | 185.3× / 180.4× · 220.9× / 215.0× | context | — | — |
| Holding credits (buy line · worth · sell line) | owed · owed · owed | — | — | — |

No positive price satisfies both primaries: debt-equivalents exceed seven times operating income, and the no-cash bound needs about SEK 20.1bn of operating income, 2.75 times FY2025's. The qualifiers pass and raise no investigation. **EXPENSIVE.**

## 7. Risks & thesis-breakers

- Patricia keeps buying at full prices (Nova Biomedical, SEK 21.7bn), so returns on acquired capital stay below 10%.
- Atlas Antibodies' goodwill write-downs show bought businesses can disappoint.
- About 40% of value sits in two cyclical industrials, ABB and Atlas Copco.
- The foundations hold 43% of the votes on 20% of the capital; outside owners cannot change the allocators.

## 8. Flip conditions & next review

Toward WATCH: current memos for the five holdings would bring the unread share below a third. Past would still need Patricia's own returns at 10% or more, and the compensation strike turns on a framework reading (`queue/IDEAS.md` §I2). Toward a lasting AVOID: more acquisitions above worth. Next review: the earlier of a holding memo landing, a MODEL decision on §I, or the year-end report on 22 January 2027. Not held.

*Framework output, not investment advice.*

---

# APPENDIX

## A. Sources & data gaps

- **Primary — Investor AB:**
  1. Annual Report 2025, retrieved 2026-10-20 ([PDF](https://www.investorab.com/media/mjzjnq4d/investor_ar25_eng.pdf)). Used for:
     - the group statements (pp.121–124) and notes 5, 7, 8, 10, 11, 14, 16, 17, 18, 20–23, 26–31, 33 and 34;
     - the net asset value table (p.119), the business-area pages (pp.33–53), the Executive Leadership Team and Board pages (pp.64–67), the five-year summary (p.189) and the share pages (pp.193–195).
  2. Interim Management Statement Jan–Sep 2026, 16 Oct 2026 ([report](https://www.investorab.com/media/lqmkx2d5/interim-management-statement-january-september-2026.pdf), [presentation](https://www.investorab.com/media/5cdapoae/interim-management-statement-january-september-2026.pdf)). Used for the condensed group statements, the segment tables, the holdings at 30 Sep 2026, and the Electrolux rights issue and Nasdaq and Atlas Copco purchases.
  3. Annual Reports used for the window record (statements, notes and segment notes):
     - 2024 ([PDF](https://www.investorab.com/media/uwdfk3lk/investor-annual-report-2024.pdf))
     - 2023 ([PDF](https://www.investorab.com/media/l5jddjxo/investor_ar2023_eng_linked.pdf))
     - 2022 ([PDF](https://www.investorab.com/media/uwlhndq1/investor_annual-report-2022.pdf))
     - 2021 ([PDF](https://www.investorab.com/media/rnenyv2r/ar.pdf))
     - 2020 ([PDF](https://www.investorab.com/media/civlxee5/ar2020.pdf))
     - 2019 ([PDF](https://www.investorab.com/media/o3ogwynf/investor-annual-report-2019.pdf)): FY2019, and the FY2018 comparative column
     - 2017 ([PDF](https://mb.cision.com/Main/1084/2483108/812436.pdf))
     - 2016: Investor's report, as hosted by ECGI ([PDF](https://www.ecgi.global/sites/default/files/Annual%20Report%202016%20%28AB%29.pdf)): FY2016 and the FY2015 balance sheet.
  4. Year-End Report 2018 presentation ([PDF](https://www.investorab.com/media/sl3dmzed/investor-year-end-report-january-december-2018.pdf)). A slide deck; Q4 2018 context only.
  5. Remuneration Reports (Table A and its notes):
     - 2025 ([PDF](https://www.investorab.com/media/lsxjiqzq/9-remuneration-report-2025.pdf))
     - 2024 ([PDF](https://www.investorab.com/media/grkal1ea/9-remuneration-report-2024.pdf))
     - 2023 ([PDF](https://www.investorab.com/media/yv4ndbid/9-remuneration-report-2023.pdf)): an image-only PDF, read from rendered pages 3–4.
  6. AGM 2026 papers:
     - the Nomination Committee's proposals, for 2026 Board fees ([PDF](https://www.investorab.com/media/3wkdj3bn/the-nomination-committees-proposals-for-decision-2026.pdf));
     - the Board's proposal on purchase and transfer of own shares ([PDF](https://www.investorab.com/media/5arlataw/18-purchase-and-transfer-of-own-shares-2026.pdf)).
- **Primary — holdings (P29 weight base only; FY2023–25 revenue as first published):**
  - ABB: Form 20-F 2023 ([SEC](https://www.sec.gov/Archives/edgar/data/1091587/000110465924026633/abb20231231.htm)) and the Q4 2024 and Q4 2025 releases ([2024](https://library.e.abb.com/public/91cea5d0b51b4f73ac22c0399107875a/ABB-Q4-2024-press-release-English.pdf), [2025](https://library.e.abb.com/public/17c5f84dedb946478c22ba1e00f5673e/ABB-Q4-2025-press-release-English.pdf)). FY2025 excludes Robotics (discontinued); FY2024 as first published.
  - Atlas Copco Q4 reports ([2023](https://www.atlascopcogroup.com/content/dam/corporate/cision/20240125_Atlas_Copco_Group_Interim_report_on_Q4_and_full-year_summary_2023.pdf), [2024](https://www.atlascopcogroup.com/content/dam/atlas-copco/group/documents/investors/financial-publications/english/20250128-en-q4-2024-lg.pdf), [2025](https://www.atlascopcogroup.com/content/dam/brands/atlas-copco-group/cision/20260127-en-Q4_2025.pdf.coredownload.pdf)).
  - Saab year-end reports ([2023](https://www.saab.com/globalassets/cision/documents/2024/20240209-saab-year-end-report-2023-taking-the-next-step-on-our-growth-journey-en-0-4746415.pdf), [2024](https://www.saab.com/globalassets/cision/documents/2025/20250207-saab-year-end-report-2024making-steady-progress-on-our-profitable-growth-journey-en-0-4984391.pdf), [2025](https://www.saab.com/globalassets/cision/documents/2026/20260205-saab-year-end-report-2025record-order-bookings-building-for-growth-en-0-5300016.pdf)).
  - AstraZeneca Form 20-F 2023–2025 (SEC EDGAR, e.g. [2025](https://www.sec.gov/Archives/edgar/data/901832/000110465926019130/azn-20251231x20f.htm)).
  - SEB Q4 reports ([2023](https://sebgroup.com/siteassets/documents/press/cision/documents/2024/20240125-sebs-annual-accounts-and-results-for-the-fourth-quarter-2023-en-gb-0-3392585-4732523.pdf), [2024](https://sebgroup.com/siteassets/documents/press/cision/documents/2025/20250129-sebs-annual-accounts-and-results-for-the-fourth-quarter-2024-en-gb-0-3543262-4977961.pdf), [2025](https://sebgroup.com/siteassets/documents/press/cision/documents/2026/20260129-sebs-annual-accounts-and-results-for-the-fourth-quarter-2025-en-gb-0-3711559-5295282.pdf)).
- **Price, FX and inflation:**
  - Price: query1.finance.yahoo.com chart endpoint, INVE-B.ST (currency SEK, exchange STO), close 20 Oct 2026 SEK 413.70.
  - FX, ECB reference rates via api.frankfurter.dev:
    - USD/SEK 9.918 (2026-10-20);
    - 2025 averages EUR/SEK 11.0678 and USD/SEK 9.8213 (computed from the daily series);
    - year-end USD/SEK 10.0416 (2023-12-29), 11.0299 (2024-12-31) and 9.2098 (2025-12-31).
  - Inflation: Swedish CPI from Statistics Sweden's API (table PR0101A/KPI2020M, shadow index). The annual averages and their changes are computed (Appendix C).
- **ISIN:** SE0015811963 (B share). The annual report does not print it; it was taken from three secondary listings (boerse.de, justETF, Börse Stuttgart), which agree.
- **Gaps:**
  1. The 2018 IFRS 3 note and the 2018 organic-growth figure were not retrieved (Annual Report 2018 is not in the source set). FY2018 maintenance capex therefore takes all capex (tier 3, harsher).
  2. The cash-flow statement prints no split of capex between intangible and tangible assets in any year. FY2016–17 print a PP&E line only, so the note-16 intangible additions are added (derived, harsher).
  3. ABB's and AstraZeneca's dividends to Investor are not printed per holding: the FY2025 total for ABB, AstraZeneca, Nasdaq and Wärtsilä is 5,466. The P17 FCF leg is therefore a lower bound; it is never the lower leg.
  4. The worth reads of Investor's purchases of listed holdings' shares (2023–26) were not built (no current memos; Appendix E). This is an attended gap, not decisive: SF fails at step 1.
- **Document count:** 21 primary documents (14 Investor, 7 holdings), plus the price, FX and SCB endpoints. More than ten documents on one name reflects a ten-year group rebuild, not opacity.
- **P14:** exploratory searches: AR 2016 locator (1), CPI (1, plus one failed SCB page fetch), ISIN (1), and 7 searches for the holdings' filings by a helper. That is 11 against the REVIEW guide of ~2: this is an attended full v4.5/v4.6 re-test of a group (TODO `▶ Method re-tests v4.6.0`), logged here.

## B. Financial record (P1 window FY2016–FY2025; 11 balance sheets FY2015–FY2025)

Consolidated Investor AB, SEK m. Pre-2021 diluted share counts are restated ×4 for the May 2021 4:1 split (AR 2021 restates FY2020 at 3,064.0m).

**B1 — Raw inputs** (FCF = CFO − dividends received − interest received − maintenance capex, J3)

| FY | Revenue | J1 OI | CFO | Div. rec'd (CF) | Int. rec'd | Capex | Maint. capex | Basis | FCF (maint.) | FCF (all-capex) | Diluted sh (m) | Total assets | NIBCL | Cash+STI+S1/S2 | G6 class assets | Total liab | Equity (parent) | GW+intang |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2015 (BS) | 25,365 | – | – | – | – | – | – | – | – | – | – | 336,590 | 4,122 | 21,074 | 256,526 | 64,613 | 271,801 | 41,448 |
| 2016 | 31,742 | 4,056 | 12,261 | 8,352 | 903 | 1,750 | 1,640 | constructed | 1,366 | 1,256 | 3,059.2 | 369,973 | 4,896 | 19,718 | 278,449 | 69,832 | 300,077 | 51,275 |
| 2017 | 34,381 | 2,584 | 10,863 | 8,411 | 599 | 1,667 | 1,667 | constructed | 186 | 186 | 3,061.6 | 408,567 | 4,856 | 25,507 | 311,876 | 72,240 | 336,262 | 49,825 |
| 2018 | 42,492 | 3,611 | 11,934 | 9,289 | 630 | 1,776 | 1,776 | = all capex | 239 | 239 | 3,062.0 | 416,028 | 6,457 | 16,845 | 303,186 | 88,338 | 327,508 | 68,109 |
| 2019 | 42,239 | 3,409 | 14,540 | 10,338 | 553 | 2,090 | 2,090 | constructed | 1,559 | 1,559 | 3,062.8 | 517,456 | 6,687 | 31,279 | 390,946 | 96,533 | 420,681 | 65,485 |
| 2020 | 39,323 | 4,469 | 10,970 | 7,994 | 526 | 2,786 | 2,786 | constructed | −336 | −336 | 3,064.0 | 571,047 | 7,314 | 30,875 | 432,130 | 108,271 | 461,837 | 75,081 |
| 2021 | 40,737 | 3,972 | 14,256 | 11,254 | 257 | 3,799 | 3,799 | constructed | −1,054 | −1,054 | 3,065.1 | 795,542 | 6,933 | 32,132 | 638,337 | 112,036 | 682,614 | 88,605 |
| 2022 | 51,812 | 5,110 | 16,610 | 11,507 | 460 | 4,368 | 4,312 | constructed | 331 | 275 | 3,064.7 | 724,365 | 8,837 | 35,732 | 550,556 | 118,711 | 604,865 | 97,688 |
| 2023 | 59,643 | 6,864 | 20,966 | 12,481 | 953 | 3,721 | 3,670 | constructed | 3,862 | 3,811 | 3,064.6 | 838,450 | 9,236 | 34,763 | 663,669 | 121,019 | 716,768 | 98,015 |
| 2024 | 63,196 | 8,635 | 23,582 | 15,637 | 1,566 | 4,420 | 4,194 | constructed | 2,185 | 1,959 | 3,065.1 | 952,090 | 10,351 | 37,044 | 765,252 | 132,339 | 819,364 | 104,959 |
| 2025 | 64,826 | 7,311 | 22,164 | 16,023 | 1,652 | 3,177 | 3,177 | constructed | 1,312 | 1,312 | 3,064.9 | 1,102,807 | 9,560 | 35,065 | 908,639 | 148,909 | 953,705 | 111,674 |

Averages (latest FY included): J1 OI 3y 7,603.3 · 5y 6,378.4; maintenance-capex FCF 3y 2,453.0 · 5y 1,327.2. The all-capex reading is the same in every year where growth capex is nil.

**G6 income lines** (the include reading adds them; the exclude reading removes them whatever their sign)

| FY | Dividends (IS) | Equity-accounted result | Net value change, class assets (Listed + EQT segments) | Include-reading OI | Include-reading FCF |
|---|---|---|---|---|---|
| 2016 | 8,351 | 516 | 24,093 (gain: out) | 12,923 | 9,718 |
| 2017 | 8,404 | 390 | 37,121 (gain: out) | 11,378 | 8,597 |
| 2018 | 9,342 | −139 | −11,428 (loss: in OI on include) | 1,386 | 9,528 |
| 2019 | 9,858 | 579 | 90,825 (gain: out) | 13,846 | 11,897 |
| 2020 | 7,664 | 1,825 | 39,171 (gain: out) | 13,958 | 7,658 |
| 2021 | 11,254 | 2,938 | 211,790 (gain: out) | 18,164 | 10,200 |
| 2022 | 11,427 | −1,176 | −81,944 (loss: in OI on include) | −66,583 | 11,838 |
| 2023 | 12,484 | 208 | 113,769 (gain: out) | 19,556 | 16,343 |
| 2024 | 15,637 | −124 | 97,362 (gain: out) | 24,148 | 17,822 |
| 2025 | 16,185 | 384 | 139,577 (gain: out) | 23,880 | 17,335 |

**B2 — Returns** (per-year ratios on beginning-of-period CE; the CE columns show each year's opening balance, the prior FY-end)

| FY | CE_wc excl. (beg.) | CE_xc excl. (beg.) | ROCE_wc excl. | ROCE_xc excl. | FCFROCE_wc excl. | FCFROCE_xc excl. | CE_wc incl. (beg.) | CE_xc incl. (beg.) | ROCE_wc incl. | ROCE_xc incl. | FCFROCE_wc incl. | FCFROCE_xc incl. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 75,942 | 54,868 | 5.3% | 7.4% | 1.8% | 2.5% | 332,468 | 311,394 | 3.9% | 4.2% | 2.9% | 3.1% |
| 2017 | 86,628 | 66,910 | 3.0% | 3.9% | 0.2% | 0.3% | 365,077 | 345,359 | 3.1% | 3.3% | 2.4% | 2.5% |
| 2018 | 91,835 | 66,328 | 3.9% | 5.4% | 0.3% | 0.4% | 403,711 | 378,204 | 0.3% | 0.4% | 2.4% | 2.5% |
| 2019 | 106,385 | 89,540 | 3.2% | 3.8% | 1.5% | 1.7% | 409,571 | 392,726 | 3.4% | 3.5% | 2.9% | 3.0% |
| 2020 | 119,823 | 88,544 | 3.7% | 5.0% | −0.3% | −0.4% | 510,769 | 479,490 | 2.7% | 2.9% | 1.5% | 1.6% |
| 2021 | 131,603 | 100,728 | 3.0% | 3.9% | −0.8% | −1.0% | 563,733 | 532,858 | 3.2% | 3.4% | 1.8% | 1.9% |
| 2022 | 150,272 | 118,140 | 3.4% | 4.3% | 0.2% | 0.3% | 788,609 | 756,477 | −8.4% | −8.8% | 1.5% | 1.6% |
| 2023 | 164,972 | 129,240 | 4.2% | 5.3% | 2.3% | 3.0% | 715,528 | 679,796 | 2.7% | 2.9% | 2.3% | 2.4% |
| 2024 | 165,545 | 130,782 | 5.2% | 6.6% | 1.3% | 1.7% | 829,214 | 794,451 | 2.9% | 3.0% | 2.1% | 2.2% |
| 2025 | 176,487 | 139,443 | 4.1% | 5.2% | 0.7% | 0.9% | 941,739 | 904,695 | 2.5% | 2.6% | 1.8% | 1.9% |
| FY2025 closing CE | 184,608 | 149,543 | | | | | 1,093,247 | 1,058,182 | | | | |

Summary — normalized averages (Σ numerator ÷ Σ CE), four ways on each reading:

| Window · reading · metric | beg·wc | beg·xc | end·wc | end·xc | worst of four |
|---|---|---|---|---|---|
| 10y FY2016–25 · exclude · ROCE | 3.9% | 5.1% | 3.6% | 4.6% | 3.6% |
| 10y FY2016–25 · exclude · FCFROCE | 0.8% | 1.0% | 0.7% | 0.9% | 0.7% |
| 10y FY2016–25 · include · ROCE | 1.2% | 1.3% | 1.1% | 1.1% | 1.1% |
| 10y FY2016–25 · include · FCFROCE | 2.1% | 2.2% | 1.8% | 1.9% | 1.8% |
| 5y FY2021–25 · exclude · ROCE | 4.0% | 5.2% | 3.8% | 4.8% | 3.8% |
| 5y FY2021–25 · exclude · FCFROCE | 0.8% | 1.1% | 0.8% | 1.0% | 0.8% |
| **5y FY2021–25 · include · ROCE** | 0.5% | 0.5% | **0.4%** | 0.5% | **0.4% ← governs (lower window's worst of eight)** |
| 5y FY2021–25 · include · FCFROCE | 1.9% | 2.0% | 1.7% | 1.8% | 1.7% |
| 3y FY2023–25 · exclude · ROCE (J6 limb b) | 4.5% | 5.7% | 4.3% | 5.4% | 4.3% |
| 3y FY2023–25 · include · ROCE (J6 limb b) | 2.7% | 2.8% | 2.4% | 2.5% | 2.4% |
| 10y · exclude · FCFROCE all-capex (context) | 0.7% | 0.9% | 0.7% | 0.9% | 0.7% |
| 5y · exclude · FCFROCE all-capex (context) | 0.8% | 1.0% | 0.7% | 0.9% | 0.7% |

The ROCE worst of eight is 1.1% (10y) and 0.4% (5y), so the level bar reads 0.4%. The FCFROCE worst of eight is 0.7% (10y) and 0.8% (5y), so it reads 0.7%. Both are far below P3(b)'s 10% and 5.3%. The exclude reading on its own (3.6% / 0.7%) fails too. **J6:** limb (b) does not fire on either reading, since the latest three years run above the window. Limb (a) finds no three consecutive declines on any series: the exclude FCFROCE fell in 2024 and 2025 only, after rising in 2023.

**B3 — Growth & leverage** (per diluted share)

| FY | ΔOI/sh excl. | ΔFCF/sh excl. | ΔOI/sh incl. | ΔFCF/sh incl. | ΔBV/sh | ΔTBV/sh | L/E |
|---|---|---|---|---|---|---|---|
| 2016 | – | – | – | – | 10.4% | 8.0% | 23.3% |
| 2017 | −36.3% | −86.4% | −12.0% | −11.6% | 12.0% | 15.0% | 21.5% |
| 2018 | 39.7% | 28.5% | −87.8% | 10.8% | −2.6% | −9.5% | 27.0% |
| 2019 | −5.6% | 552.1% | 898.7% | 24.8% | 28.4% | 36.9% | 22.9% |
| 2020 | 31.0% | −121.5% | 0.8% | −35.7% | 9.7% | 8.8% | 23.4% |
| 2021 | −11.2% | n.m. | 30.1% | 33.1% | 47.8% | 53.5% | 16.4% |
| 2022 | 28.7% | n.m. | −466.6% | 16.1% | −11.4% | −14.6% | 19.6% |
| 2023 | 34.3% | 1,067.3% | n.m. | 38.1% | 18.5% | 22.0% | 16.9% |
| 2024 | 25.8% | −43.4% | 23.5% | 9.0% | 14.3% | 15.4% | 16.2% |
| 2025 | −15.3% | −40.0% | −1.1% | −2.7% | 16.4% | 17.9% | 15.6% |

| Read | Geometric mean of YoY | 3-yr endpoint averages (7 yrs) | Harsher |
|---|---|---|---|
| ΔOI/sh exclude | 6.7% | 12.1% | 6.7% |
| ΔFCF/sh exclude | n.m. (FY2020–21 negative) | 22.3% | **n.m.** |
| ΔOI/sh include | n.m. (FY2022 negative) | 14.8% | **n.m.** |
| ΔFCF/sh include | 6.6% | 9.2% | 6.6% |

Over FY2015–25, BV/sh rose from SEK 88.85 to 311.17 (13.4% a year) and TBV/sh from 75.30 to 274.73 (13.8% a year). That reflects mark-to-market gains on the stakes, with dividends of SEK 2.75–5.20 a share paid each year. L/E at FY2025 is 15.6%, within P5. P3 fails on level and on growth (n.m.).

**B4 Division table (group parts; P29 weights on revenue, because the holdings without a memo have no disclosed base)**

| Part | Kind | Revenue FY2023 · FY2024 · FY2025 (filer source) | Segment result FY2023 · 24 · 25 | Segment assets FY2023 · 24 · 25 | Weight base (3y avg revenue, Investor's share, SEK m) | Weight | Future |
|---|---|---|---|---|---|---|---|
| Patricia Industries | unit | 59,643 · 63,196 · 64,826 | 6,846 · 9,518 · 7,415 (operating profit) | 153,305 · 162,870 · 170,253 | 62,555 | 32.3% | ADEQUATE (2) |
| Investments in EQT | unit | – (no net sales) | 11,777 · 6,713 · 13,551 | 82,088 · 88,710 · 104,390 | 0 | 0.0% | WEAK, ungradeable (1) |
| ABB | holding 14.1/14.3/14.4% | USD 32,235 · 32,850 · 33,220 | — | — | 47,170 | 24.4% | WEAK, sub dependency (1) |
| Atlas Copco | holding 17.0/17.0/17.1% | SEK 172,664 · 176,771 · 168,343 | — | — | 29,397 | 15.2% | WEAK, sub dependency (1) |
| Saab | holding 30.2% | SEK 51,609 · 63,751 · 79,146 | — | — | 19,580 | 10.1% | WEAK, sub dependency (1) |
| AstraZeneca | holding 3.3% | USD 45,811 · 54,073 · 58,739 | — | — | 17,572 | 9.1% | WEAK, sub dependency (1) |
| SEB | holding 21.3/21.7/21.8% | total operating income SEK 80,193 · 81,887 · 76,939 | — | — | 17,208 | 8.9% | WEAK, sub dependency (1) |
| **Total** | | | | | **193,482** | 100% | **S = 1.32 → WEAK** |

- USD revenue is translated at Investor's year-end reference rates (10.0416 / 11.0299 / 9.2098). Investor's capital share is from each year's NAV table.
- Ungradeable parts carry 67.7% of the base (more than a third) → group Future WEAK (`sub dependency`).
- Patricia's segment results include its value changes and associates; the allocation test removes the positive value change (Appendix E).
- No look-through additions are made: no material holding has a current memo, so none adds to the Past (§2 Group dependencies). The guard tests on the consolidated record alone are the B2/B3 exclude reading: L/E 15.6%, equity positive, no J6 decline.

## C. Calculation notes

- **Lens test.** Investor AB is neither a licensed bank or insurer nor the parent of a supervised banking or insurance group (SEB is a 21.8% associate at fair value, not consolidated). FI does not apply, so the lens is **STD**.
  - Test (c) of the retired R4, now an STD rule: at FY2025, unlisted stakes plus securities that are neither S1/S2 nor material listed holdings come to ≈ SEK 321bn. That is the eight immaterial listed stakes, EQT AB and the EQT funds, Tre Skandinavien and Patricia's financial investments, about 29% of total assets.
  - It is below half, so no STD special rule applies beyond S3.
- **Materiality (P22, at FY2025 year-end).**
  - Listed holdings, SEK 797.9bn (863.2bn with EQT AB), exceed a third of market cap (SEK 1,010.0bn). The material ones are therefore the largest that together reach two-thirds of their value. Cumulative: ABB 182,966, Atlas Copco 321,854, Saab 410,273, AstraZeneca 498,282, SEB 585,512. That reaches ≥ 531,933 (≥ 575,455 with EQT AB), so the same five qualify either way.
  - ABB and Atlas Copco are also ≥ 10% of market cap each.
  - Units: Patricia Industries is material (100% of net sales). Investments in EQT is 10.5% of segment net asset value (797,899 / 92,019 / 104,390) but 9.7% of gross segment assets (shares and participations plus other assets: 798,008 / 170,253 / 104,390). Treated as material on the net-asset-value measure, the harsher reading because it adds an ungradeable part. Its weight is 0 under revenue weights, so S does not move.
  - Listed Companies is a segment of non-controlled listed holdings, not a unit.
- **G6 classes and the P31 test.** The class is:
  - shares and participations at fair value: every listed stake (all S3 or ungradeable H), EQT AB, the EQT funds and Patricia's financial investments;
  - equity-accounted associates and JVs (Tre Skandinavien, Steptura, others);
  - loans to associates in long-term receivables (1,705 / 1 / 1 / 1 in 2016–19; 240 in 2023, as restated by AR 2024; 267 in 2025).

  Its carrying value is 76.2% of total assets at FY2015 and 82.4% at FY2025, far above 5% at every date, and its income is several times exclude-reading OI every year. **Above the P31 line:** both readings, the harsher governing.
  - Class income on the include reading: IS dividends, the equity-accounted result as reported, and the net value change of the class in loss years only (FY2018 −11,428; FY2022 −81,944). The class value change is the Listed plus EQT segment value changes.
  - Cash: dividends received in CFO (which include associates' dividends, e.g. Tre's 480 in 2019) stay on the include reading. Interest on loans to associates is not attributed and stays out on both readings (J13).
  - Tax and interest paid on the debt that funds the stakes stay in CFO on both readings.
- **J1 OI build (FY2025).**
  - The face statement's "Operating profit/loss" of 162,782 includes dividends (16,185), changes in value (138,902) and associates (384), all J3 financial income.
  - J1 OI = net sales 64,826 − COGS 33,819 − sales and marketing 9,277 − administrative, R&D and other 13,624 − management costs 795 = **7,311**.
  - It carries the Atlas Antibodies goodwill impairment (1,378) and acquisition amortisation (proprietary technology 1,611, customer relations 1,320, tradenames 268).
  - Patricia's EBITA (an APM) is not a candidate: it omits acquisition amortisation.
  - FY2016–18 "other operating income" (40 / 17 / 7) is Patricia's and stays in OI.
  - TTM to Q3 2026 (FY2025 − 9M 2025 + 9M 2026 = 7,311 − 6,412 + 8,114 = 9,013) is higher, so FY2025 governs.
- **FCF.** CFO as reported (interest paid sits in operating activities; lease principal in financing), less dividends received and interest received (J3), less maintenance capex.
  - TTM to Q3 2026 is not computable: the interim prints net interest only. It is bounded above FY2025: TTM CFO 26,453 − TTM dividends 17,436 − TTM capex 3,390 = 5,627 before interest received, which was at most SEK 1.7bn in any window year. FY2025 governs.
- **P20 build.** k = Σ net fixed capital ÷ Σ revenue, FY2016–25 = 102,320 ÷ 470,391 = 0.2175.
  - Net fixed capital is net PP&E excluding right-of-use assets, plus capitalised development and software. Investment property is excluded.
  - Organic revenue is the lower of revenue less acquired revenue (IFRS 3 B64(q)) and prior revenue × (1 + organic growth of the major subsidiaries in constant currency). FY2016 uses 5%, the lower bound of the CEO letter's "between 5 and 17 percent" (J13).
  - π = max(3%, Swedish CPI annual average).

| FY | CPI (SCB, %) | π | Revenue − acquired | Organic cap | Real growth | Growth capex | Floor | Capex | Maintenance | Tier |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 0.98 | 3.00% | 31,020 | 26,633 (g 5%) | 507 | 110 | 879 | 1,750 | 1,640 | constructed |
| 2017 | 1.80 | 3.00% | 33,353 | 32,377 (g 2%) | −317 | 0 | 950 | 1,667 | 1,667 | constructed |
| 2018 | 1.95 | 3.00% | n/a | – | – | 0 | 1,201 | 1,776 | 1,776 | = all capex |
| 2019 | 1.78 | 3.00% | 42,079 | 44,192 (g 4%) | −1,688 | 0 | 1,097 | 2,090 | 2,090 | constructed |
| 2020 | 0.50 | 3.00% | 38,078 | 43,084 (g 2%) | −5,428 | 0 | 987 | 2,786 | 2,786 | constructed |
| 2021 | 2.16 | 3.00% | 39,951 | 40,503 (g 3%) | −552 | 0 | 1,039 | 3,799 | 3,799 | constructed |
| 2022 | 8.37 | 8.37% | 51,394 | 44,403 (g 9%) | 257 | 56 | 1,462 | 4,368 | 4,312 | constructed |
| 2023 | 8.55 | 8.55% | 59,347 | 56,475 (g 9%) | 233 | 51 | 1,417 | 3,721 | 3,670 | constructed |
| 2024 | 2.84 | 3.00% | 62,473 | 63,222 (g 6%) | 1,041 | 226 | 1,331 | 4,420 | 4,194 | constructed |
| 2025 | 0.68 | 3.00% | 62,565 | 65,724 (g 4%) | −2,527 | 0 | 1,391 | 3,177 | 3,177 | constructed |

  The floor (depreciation of PP&E excluding right-of-use, plus amortisation of capitalised development and software) never binds. FY2016–17 capex is the cash-flow PP&E line plus the note-16 intangible additions (205; 290): derived, harsher.
- **Leases.** IFRS 16 applies from FY2019, and lease liabilities are inside interest-bearing liabilities. Pre-2019 undiscounted operating-lease commitments were 2,428 / 3,403 / 3,523 / 4,537 (FY2015–18), against 10% of total assets (≥ SEK 33.7bn). No capitalisation (P18).
- **NIBCL calls.** NIBCL = trade payables + tax liabilities (including FY2018–19's long-term tax liability of 372) + accrued expenses and prepaid income.
  - Left out of NIBCL, and so kept in CE: accrued interest (842–1,124 a year), acquisition-related accruals (359 in 2023; 331 in 2025) and the FY2021 licence accrual of 1,266. All are debt-like or ambiguous, so they stay in CE (burden of proof).
  - "Other liabilities" (customer prepayments, VAT, floorplan, NCI puts) stays in CE.
  - FY2025: 4,036 + 470 + (6,509 − 1,124 − 331) = **9,560**.
- **CE build, FY2025.**
  - Total assets 1,102,807 − NIBCL 9,560 = CE_wc include **1,093,247**.
  - Less the class 908,639 (904,799 + 3,573 + 267) = CE_wc exclude **184,608**.
  - Cash = cash 14,058 + short-term investments 8,135 + 0.9 × other financial investments (bonds of 13–24 months) 13,910 + trading-operation shares 445 × (1 − 20.6%) = **35,065**.
  - CE_xc: exclude 149,543; include 1,058,182.
  - Goodwill plus intangibles (111,674) are 60.5% of exclude CE_wc.
- **TBV build (30 Sep 2026).** Equity attributable 1,099,072 − goodwill 82,550 − other intangibles 38,672 = **977,850**.
- **EV build (30 Sep 2026, primary interim; YE2025 note values where the interim prints no split).**

| Debt-equivalent | SEK m | Source |
|---|---|---|
| Long-term interest-bearing liabilities (bonds, bank loans, leases, negative derivatives) | 125,825 | Q3 2026 BS |
| Current interest-bearing liabilities | 1,429 | Q3 2026 BS |
| Pensions (net unfunded) | 1,030 | Q3 2026 BS |
| NCI put options at fair value | 6,194 | AR 2025 note 30 |
| NCI (book) | 283 | Q3 2026 BS |
| Acquisition-related liabilities (earn-outs; LT 2,005 + ST 727 + accrued 331) | 3,063 | AR 2025 notes 30–31 |
| Guarantees of associates' debt (Tre Skandinavien) | 2,680 | AR 2025 note 33 |
| Vehicle floorplan liabilities (supplier finance) | 477 | AR 2025 note 30 |
| **Debt-equivalents D** | **140,981** | |
| Cash: cash, bank and STI 16,652 + 0.9 × other financial investments 23,255 + trading shares 243 × 0.794 | **37,775** | Q3 2026 BS |

  - Diluted shares: 3,065.6m, derived from 9M 2026 profit attributable of 159,316 ÷ diluted EPS of SEK 51.97 (3,063.7m outstanding at 30 Sep).
  - MCap 1,268,239; EV no-cash 1,409,220; EV all-cash 1,371,445.
- **Securities classes (30 Sep 2026, SEK m, market values per the interim).**

| Holding | Class | Value | Note |
|---|---|---|---|
| ABB, Atlas Copco, Saab, AstraZeneca, SEB | H, ungradeable → S3 / G6 class | 252,810 · 172,275 · 101,235 · 84,398 · 102,026 | no current memo; credit owed |
| Epiroc, Sobi, Nasdaq, Wärtsilä, Ericsson, Electrolux, Husqvarna, Electrolux Professional | S3 (immaterial, held as long-term "core" ownership by the filer) | 54,357 · 54,215 · 53,639 · 33,325 · 30,978 · 3,993 · 3,386 · 2,642 | no credit; G6 class |
| EQT AB (14.0%) and EQT fund investments | S3 | 94,970 in total | no credit; G6 class |
| Tre Skandinavien (40%), Steptura (50%) | equity-accounted | 2,560 · 972 (YE2025 book) | G6 class |
| Bonds 13–24 months | S1 at × 0.9 | 23,255 | cash |
| Trading-operation shares | S2 | 243 | cash at × (1 − 20.6%) |

  Investor states that capital gains and dividends on business-related holdings are tax-exempt. That would set t = 0 for an H credit; no credit is computed while the memos are owed.
- **Bias check.**
  - *Consistency:* the v2 WATCH and the name's prestige. Handled by running every rule as written and logging each holding-company artefact separately.
  - *Authority* (Wallenberg standing): noted.
  - *Incomprehensibility:* the rebuild is long, but every step is in these tables.
  - **Bias check: none live.**

## D. Future-performance worksheet

**Patricia Industries (unit).** Graded as one unit on its largest part, Mölnlycke, ≈ 36% of 2025 net sales (derived: EUR 2,104m × 11.0678 = SEK 23,287m of 64,826).
- Other parts by 2025 sales, at 2025 average rates (derived): Sarnova ≈ SEK 11.3bn (17%), BraunAbility ≈ 10.9bn (17%), Permobil 6.2bn (10%), Laborie ≈ 4.8bn (7%), Piab 3.6bn (6%), Nova Biomedical from 10 Jul 2025 (2.1bn since acquisition), Vectura 0.3bn, Atlas Antibodies 0.3bn.
- The largest part leads by ≈ 18pp, so the calls read Mölnlycke, and each line names any part where the call runs the other way.
- **Breadth.**
  - Customer: "No customer exceeds 10 percent of total net sales" (AR 2025 note 8, p.134). This is a filer statement covering all consolidated sales, and with them the distributors through which 52% of sales go (33,924 of 64,826). Clean.
  - Supplier: no single supplier above 10% of COGS + opex is disclosed or evidenced. No flag.
  - *Runs the other way:* BraunAbility converts minivans from a few automakers, a likely supplier concentration for about 17% of the unit that the filings do not size.
- **Forces (Mölnlycke).**

| Force | Call | One-line reason |
|---|---|---|
| Customer power | STRONG | Hospitals buy through purchasing groups, national tenders and integrated distributors with professional purchasing. Contained (below). |
| Supplier power | WEAK | Medical-grade materials (nonwovens, silicone, polymers) come from many vendors. |
| Substitutes | WEAK | Advanced dressings and single-use surgical products displace traditional ones; negative-pressure therapy competes in part of wound care only. |
| New entrants | WEAK | Clinical evidence, regulatory clearance, formulary listing and clinician preference (Mepilex/Safetac, Biogel) are barriers to entry and to success. |

  - Tally: 1 STRONG. **Containment:** the force does not reach the moat's source, since clinicians set the specification and the buyer negotiates price within it. The EBITA margin held at 24.8% (2025) against 25.3% (2024) (AR 2025 p.42). Earlier years' margins were not re-extracted.
  - *Runs the other way:* Sarnova, a US distributor of emergency-medical supplies, faces STRONG customer power and new-entrant threat and has no moat beyond scale. BraunAbility is cyclical.
- **Moat:** brand with clinicians (one source). **Stable.** In Q3 2026 Mölnlycke announced the intention to separate into two companies, Wound Care and Mölnlycke Surgical: a change of structure, not erosion.
- **Market growth: YES.** Ageing populations and chronic wounds. Mölnlycke grew organically +4% in 2025 and +5% in Q3 2026; the major subsidiaries +4% (2025) and +7% (Q3 2026), in constant currency.
- **Grade: ADEQUATE** (one STRONG force, contained).

**Investments in EQT (unit): ungradeable.** It holds 177.3m EQT AB shares (14.4%, SEK 65,284m at YE2025) and LP interests in EQT funds (SEK 39,106m; outstanding commitments SEK 26.8bn). The filer describes EQT AB as a private-markets manager and lists the funds by vintage and value (AR 2025 pp.52–53). It describes neither EQT AB's paying customers (the fund investors) nor the funds' portfolio companies, so breadth, forces and moat cannot be called from its filings. **WEAK** (§2 Units).

**Material listed holdings: all ungradeable → WEAK.**

| Holding | YE2025 value SEK m | Own memo | Status |
|---|---|---|---|
| ABB | 182,966 | `ABB` v4, 2026-09-25, MODEL v4.3.0 | stale (below v4.5.0) |
| Atlas Copco | 138,888 | `ATCO-B.ST` v2, 2026-07-31, MODEL v4.0.0 | stale (below v4.5.0) |
| Saab | 88,419 | none (key `SAAB-B.ST`) | missing |
| AstraZeneca | 88,009 | none (key `AZN.L`, the primary line) | missing |
| SEB | 87,230 | none (key `SEB-A.ST`; FI lens if it fits) | missing |

Each is queued in `queue/TODO.md` `▶ Group dependencies`. **Group Future: WEAK (`sub dependency`):** ungradeable parts carry 67.7% of the P29 base, and S = 1.32 ≤ 1.5 on its own.

## E. Shareholder-friendliness evidence

**SF ladder — decided at step 1 (hard strike).**

| # | Finding | Kind | Evidence |
|---|---|---|---|
| 1 | Executive pay against the group P17 denominator (one behaviour, all years) | **Strike** | FY2023 proportionality: 37.8m against a leg of SEK 118m (32%, more than twice the 10% strike line), with the trailing leg negative. FY2025 loss-year limb: leg ≤ 0, trailing ≤ 0, year total 38.2m above FY2024's 29.3m on the grant basis (on the vested basis the FY2024 test year strikes instead) |
| 2 | Nova Biomedical bought at 21.3× pre-deal profit, and all segment-asset growth into units below 10% | CAUTION (`reinvestment`/`acquisitions`, one behaviour) | Acquisition worksheet and allocation table below |
| — | Alignment WEAKLY ALIGNED; votes separated; CEO bought SEK 6.8m of participation shares; rising dividend from dividends received | inputs | below |
| — | The five holdings' own SF | INDETERMINATE (b) | re-test when their memos land |
| — | Worth reads of purchases of holdings' shares (≈ 1.1% of market cap, 2023 to Q3 2026) | INCOMPLETE (attended) | not decisive: step 1 decides |

**Pay worksheet** (Remuneration Reports, Table A; SEK).

| Person · FY | Grant basis (Table A total, as printed) | Vested basis (derived from printed components) | Note |
|---|---|---|---|
| Johan Forssell, CEO · 2022 | 34,454,558 | — | reference year |
| Forssell, CEO · 2023 | **37,804,176** (fixed 13.50m, benefits 0.38m, STVR 1.28m, LTVR grant 16.88m, extraordinary 0.16m, pension 5.60m) | ≈ 48.53m (LTVR vested net value SEK 27.6m in place of the grant) | board fees from holdings ≈ SEK 5m, outside Investor |
| Christian Cederholm, CEO from 8 May · 2024 | **29,296,424** | — | pre-May pay sits in the ELT aggregate |
| Forssell, CEO to 7 May · 2024 | 16,949,903 (incl. SEK 6.20m cash in lieu of the 2024 LTVR) | **≈ 72.65m** (vested net value SEK 55.7m added) | the largest per-person figure in the table |
| Cederholm, CEO · 2025 | **38,181,961** (fixed 13.53m, benefits 0.38m, LTVR grant 18.94m, extraordinary 0.62m, pension 4.71m) | — | plus SEK 0.95m expensed in a subsidiary (AR 2025 note 12) and ≈ SEK 1.3m of holdings' board fees, not added |
| Other 7 ELT members · 2025 | aggregate 106,569k expensed (AR 2025 note 12) | — | floor 15.2m per head, ceiling 106.6m |

- **Year totals (grant basis, as printed):** 2023 37.80m · 2024 29.30m · 2025 38.18m. The hairiest printed total is 38.18m. The hairiest on any basis is ≈ 72.65m (derived vested basis, Forssell 2024; read beside it).
- **Denominator (group P17; NI leg after the financial-income rule, every dividend, value change, associate result and financial income removed):**

| FY | NI attributable | − dividends | − value changes (if net +) | − associates (if +) | − financial income (if +) | **NI leg** | FCF (maint.) × parent share | + dividends from material holdings (printed: Atlas Copco + Saab + SEB) | **FCF leg (≥)** | Lower leg |
|---|---|---|---|---|---|---|---|---|---|---|
| 2021 | 228,065 | 11,254 | 213,505 | 2,938 | 83 | **285** | −1,054 × 1.0004 = −1,054 | 1,517+193+3,741 = 5,451 | **4,397** | 285 |
| 2022 | −74,681 | 11,427 | 0 (net loss stays) | 0 (loss stays) | 81 | **−86,189** | 331 × 0.9987 = 330 | 1,584+201+2,737 = 4,522 | **4,852** | −86,189 |
| 2023 | 127,045 | 12,484 | 113,187 | 208 | 1,048 | **118** | 3,862 × 1.0018 = 3,869 | 1,923+217+3,079 = 5,219 | **9,088** | 118 |
| 2024 | 113,338 | 15,637 | 97,942 | 0 (loss stays) | 945 | **−1,186** | 2,185 × 1.0015 = 2,189 | 2,340+262+5,246 = 7,848 | **10,037** | −1,186 |
| 2025 | 157,494 | 16,185 | 138,902 | 384 | 2,354 | **−331** | 1,312 × 1.0010 = 1,313 | 2,514+328+5,246 = 8,088 | **9,401** | −331 |

  Trailing legs (lower of the two): 2021–23 −28,595 · 2022–24 −29,086 · 2023–25 −466. FY2022's parent share is equity attributable ÷ total equity, because total NI ≤ 0.
- **Limbs.**
  - FY2023, proportionality: the fiscal-year read is 37.8m ÷ 118m = 32% (above 10%, egregious). The trailing leg is ≤ 0, so pay exceeds 5% of it. **Strike.**
  - FY2024, loss year: the leg is ≤ 0 and the year total of 29.3m is above the token cap. Flag. The year total fell from FY2023 (grant basis), so no strike. On the vested basis (72.65m against 48.53m) it rose: **strike**.
  - FY2025, loss year: the leg is ≤ 0, the trailing leg is ≤ 0, and the year total rose from 29.30m to 38.18m (grant basis). **Strike.** On the vested basis it fell, so a flag only.
  - The token cap is the outside-director cap in use: the lower of 2× the home seat norm (home benchmark not set) and US$666k = **SEK 6.61m** (USD/SEK 9.918).
  - Absolute line US$40m = SEK 396.7m: no flag (72.65m at most). Big grants: none; the SEK 6.20m cash paid to Forssell in lieu of his 2024 grant is below his regular annual total. Home average: home benchmark not set.
- **This reading is a framework artefact, logged rather than softened.** The NI leg strips a holding company's whole income, while the FCF leg (≥ SEK 9bn) is never the lower. With the dividends Investor actually received added back, the FY2025 leg would be ≈ SEK 15.9bn and the CEO's pay 0.24% of it, no flag. Parked as `queue/IDEAS.md` I2.
- **Directors.**
  - Chair Jacob Wallenberg, 2025: fee at grant SEK 4,033k; actual cost including the synthetic-share revaluation SEK 4,436k ≈ US$448k. Below the cap in use (US$666k; home norm not set), no flag.
  - The 2026 AGM set the Chair at SEK 3.75m plus committee fees. The Vice Chair received SEK 2.04m.
  - Mats Rahmström: SEK 1.025m plus SEK 1.63m expensed in a subsidiary = 2.66m, below the cap.
  - No full-time executive role is stated for the Chair.
- **Alignment (P23; holdings at 31 Dec 2025, valued at px SEK 413.70).**

| Executive | A shares | B shares | Total |
|---|---|---|---|
| Christian Cederholm (CEO) | 46,700 | 180,800 | 227,500 |
| Jenny Ashman Haquinius (CFO) | – | 15,416 | 15,416 |
| Petra Hedengran | 18,000 | 90,700 | 108,700 |
| Jessica Häggström | 5,600 | 5,236 | 10,836 |
| Thomas Kidane | 5,959 | 24,809 | 30,768 |
| Jacob Lund | 3,000 | 8,375 | 11,375 |
| Daniel Nodhäll | 7,500 | 72,500 | 80,000 |
| Yuriy Prilutskiy | – | 96,609 | 96,609 |
| **Management** | | | **581,204 ≈ SEK 240.4m; 0.019% of shares** |

  The holdings as disclosed include spouses' and minor children's holdings; no disclaimer is printed. The ratio to the hairiest number is 6.3× (38.18m), or 3.3× (72.65m). Both are ≥ 3× and < 10×, so the call is **WEAKLY ALIGNED** either way.
- **Votes against economics.** A shares carry one vote and B shares one-tenth. The Knut and Alice Wallenberg Foundation holds 20.1% of capital and 43.0% of votes; the Marianne and Marcus Wallenberg Foundation 1.9% and 4.1%. The pool holds ≥ 47.1% of votes on ≥ 22.0% of capital, a ratio of ≥ 2.1×: **separated.** That is an input only, and step 3 is never reached. The Nomination Committee is chaired by the foundations' representative.
- **Insider transactions.** The CEO's own investment in LTVR participation shares was SEK 6,782k in 2025 (50.1% of base salary): a positive input. No sales or pledges are recorded.
- **RPT.**
  - In Oct 2025 Vectura sold AB Näckström (Arsenalsgatan 8, Villa Täcka Udden) to FAM AB, the Wallenberg foundations' company, at a property value of SEK 1.4bn (net proceeds 1,342; loss of 3 in changes in value). Both sides retained independent appraisers, and conflicted directors did not participate (AR 2025 note 33/34). The controller dealt as counterparty at appraised value, which is at worth. P27 is material on the group denominator (≤ 0) but checkable. **Caveat, not a flag.**
  - Context from earlier in the window: the 2021 sale of Grand Group and the Grand Hôtel to FAM (SEK 3.7bn, gain of 290).
  - No management, advisory or licence payments to insiders were found. Patricia's carried-interest and parallel-investment plans (legacy Investor Growth Capital) are disclosed and immaterial.
- **Repurchases (worth table; LTI delivery hedges).** D is approximated as interest-bearing liabilities plus pensions; logged only.

| FY | Shares | SEK m (equity · CF) | Avg price | Implied MCap | EV/OI (year) | MCap/FCF (year) | vs worth |
|---|---|---|---|---|---|---|---|
| 2023 | 0.9m | 199 · 226 | ≈ 221 | ≈ 677.6bn | ≈ 112× (no-cash) / 107× (all-cash) | ≈ 175× | clearly above, below floor |
| 2024 | 0.8m | 229 · 356 | ≈ 286 | ≈ 876.6bn | ≈ 113× | ≈ 401× | clearly above, below floor |
| 2025 | 0.6m | 154 · 198 | ≈ 257 | ≈ 787.7bn | ≈ 124× | ≈ 600× | clearly above, below floor |
| 9M 2026 | n/a | 96 · 311 | — | — | — | — | below floor |

  The total of ≈ 2.6m shares is 0.08% of average diluted shares, under the 1% floor (sterilising: 0.8–0.9m shares a year were transferred to programmes), so the tranches are logged, never flagged. The live authorisation (AGM 2026) allows up to 10% of shares with no worth-referenced price discipline, but no value-capture programme is executing.
- **Purchases of listed holdings' shares** (cash ÷ average market cap):
  - 2023: SEK 2,188m, mainly the Sobi rights issue (2.2bn): 0.34%.
  - 2024: 2,842m (Ericsson 2.8bn): 0.35%.
  - 2025: 2,428m (Ericsson 1.7bn, Atlas Copco 0.6bn): 0.25%.
  - 9M 2026: ≈ 1,919m (Electrolux rights issue 1,701, Nasdaq 188, Atlas Copco 30): ≈ 0.17%.

  The sum is ≈ 1.1%, at the "about 1%" floor. The tranche-by-tranche worth reads need each holding's own figures, and no holding has a current memo: INCOMPLETE (attended gap). Not decisive, because step 1 decides.
- **Acquisition worksheet** (deals > 1% of EV, trailing three FYs plus the live year).
  - FY2023, FY2024 and FY2026 YTD deals sum to 3,301 (plus Urotronic's contingent consideration of up to USD 314m), 3,789 and ≈ 4.5bn (JADA, USD 440m plus up to 25m, and Mercury Medical, USD 43m). Each is below 1% of that year's EV (≈ 7.7bn / 9.6bn / 13bn).
  - **Nova Biomedical** (10 Jul 2025, 100%, via Advanced Instruments): consideration SEK 21,733m, ≈ 1.9% of EV.
    - Its pre-deal OI is undisclosed (a private target). The IFRS 3 B64(q) proxy is the pre-acquisition profit of 531 for 1 Jan–9 Jul (190 days), annualised to ≈ 1,020.
    - Deal EV/OI proxy = **21.3×**: above worth (≈ 14), below clearly above (≈ 25). **CAUTION.**
    - The post-acquisition loss (−193, after deal costs of 293 and purchase-price-allocation charges) and the full-year pro forma (338 → 64×) are post-deal readings, not the target as it stood. They are logged, not governing.
    - Price/FCF n/a (target FCF not disclosed); EV/OI governs.
  - **Write-downs:** Atlas Antibodies goodwill was impaired by SEK 0.8bn (2023) and 1.38bn (2025) on the evitria deal (2021, SEK 2.3bn). The CEO and CFO who made that deal are no longer in office: logged as context.
  - **Earlier in the window:** Sarnova (2018, EV USD 903m at ≈ 12% EBITDA margin), Laborie (2016, 2018), Advanced Instruments (2020) and others, under allocators no longer in office: context.
- **Allocation across the parts (G4)** — window FY2016–FY2025 (the segmentation reported since 2016); pooled FY2023–25.

| Unit | Σ result FY2023–25 (positive fair-value changes out) | Σ segment assets (shares & participations + other assets) | Pooled return | vs 10% | Δ segment assets FY2016→FY2025 | Share of growth |
|---|---|---|---|---|---|---|
| Patricia Industries | 6,846 + (9,518 − 571) + 7,415 = 23,208 | 153,305 + 162,870 + 170,253 = 486,428 | 4.8% | below | 87,532 → 170,253: +82,721 | 47.8% |
| Investments in EQT | (11,777 − 11,272) + (6,713 − 6,105) + (13,551 − 12,810) = 1,854 | 82,088 + 88,710 + 104,390 = 275,188 | 0.7% | below | 14,191 → 104,390: +90,199 | 52.2% |

  All of the growth went to units below the line → **CAUTION (`reinvestment`)**. It is one behaviour with the Nova acquisition-stop CAUTION, which is a deal into Patricia, a below-line unit. EQT's result without its value changes is mostly dividends, so this read also carries the holding-company artefact (IDEAS I1).
- **Dividends and funding.** The dividend per share rose from SEK 4.00 (2021) to 5.60 (2025; SEK 17.2bn), at 106–123% of dividends received from Listed Companies, and was funded from dividends received. Leverage was 1.8–2.1% of adjusted assets, with no debt-funded distribution. Rational for the profile.
- **Recency-weighted reading.**
  - Allocation 2023–26 is disciplined on the parent balance sheet: low leverage, a rising dividend, no value-capture buybacks.
  - Patricia's acquisitions are priced at 20×+ pre-deal profit and keep its returns in single digits. The 2026 add-ons (JADA, Mercury Medical) continue the pattern at a smaller scale.
  - Forward evidence: the Q3 2026 statement says Investor remains "ready to support our companies, and we have ample opportunity to fund attractive investments across the three business areas over time"; Mölnlycke is to be split.
- **INDETERMINATE.** (b): the SF findings of the five ungradeable holdings, re-tested at the parent re-run when their memos land. INCOMPLETE (attended): the worth reads of holding-share purchases.
- **Consistency hazard: checked.** The previous WATCH and the Wallenberg prestige get no softer reading: every limb is applied as written. A stranger whose net income, stripped of investment income, came to SEK 118m and whose CEO earned SEK 38m would draw the same strike. The artefacts are logged in IDEAS, never netted here.

## F. Valuation math

- **At px SEK 413.70:**
  - MCap = 413.70 × 3,065.6m = SEK 1,268,239m.
  - MCap/FCF = 1,268,239 ÷ 1,312 = **966.6×**.
  - EV/OI no-cash = (1,268,239 + 140,981) ÷ 7,311 = **192.8×**.
  - EV/OI all-cash = (1,409,220 − 37,775) ÷ 7,311 = **187.6×**.
- **Threshold-implied prices:**
  - FCF leg: 8 × 1,312 ÷ 3,065.6 = **SEK 3.42**.
  - EV/OI no-cash leg: (7 × 7,311 − 140,981) ÷ 3,065.6 = **−SEK 29.29 → n.m.**
  - EV/OI all-cash leg: (51,177 + 37,775 − 140,981) ÷ 3,065.6 = **−SEK 16.97 → n.m.**
  - Both EV/OI bounds are n.m. (a 12.3-SEK gap between them), so no price passes both primaries. **Trigger n.m.** The no-cash bound needs OI ≥ D ÷ 7 = **SEK 20,140m**, 2.75× FY2025's J1 OI.
  - P12: none (Past and Future not STRONG).
  - All-capex band: the same, since FCF equals the all-capex reading in FY2025.
- **Averaged readings (context):**

| Base | MCap/FCF | EV/OI no-cash | EV/OI all-cash |
|---|---|---|---|
| 3y (OI 7,603.3; FCF 2,453.0) | 517.0× | 185.3× | 180.4× |
| 5y (OI 6,378.4; FCF 1,327.2) | 955.6× | 220.9× | 215.0× |

- **P28: the latest year governs.**
  - OI: FY2025's 7,311 is above the lower average (6,378.4), so it is not down.
  - FCF: 1,312 is just below the 5y average of 1,327.2 (test 1 met). But no impairment, restructuring or disruption explains more than half of the SEK 15m shortfall: Nova's SEK 293m of deal costs and the higher interest on its financing are not named causes. Test 2 fails.
  - Backvaluing: not applicable (not definitively cyclical).
- **Qualifiers (context):** 3 × BV/sh = SEK 1,075.6; 3 × TBV/sh = SEK 956.9.
- **Holding credits: owed.** No material holding has a current memo, so C = 0 at every yardstick (buy line, worth, sell line) and `holding_keys` is n.m. The legs are uncredited.
- **Illustration outside the rules (V14 forbids market-value credits; printed only to show the verdict does not hinge on the credit):**
  - Crediting every listed and EQT stake at its 30 Sep 2026 market value (949,279 + 94,970 = SEK 1,044.2bn) leaves SEK 224.0bn of market cap for Patricia and the parent.
  - EV no-cash ≈ 365.0bn, which is ≈ 49.9× FY2025 J1 OI (40.5× TTM OI of 9,013) and ≈ 44.8× all-cash. That is still far beyond 7×.
  - On Investor's own estimate, Patricia is worth SEK 242bn (30 Sep 2026, excluding cash).
- **Sell-flag line:** n/a (not held).

## G. Change log

- **v1** — 2026-07-09 — ANALYSE — WATCH (all gates pass; substitution rule, price against NAV) — archive/memos/INVE-B.ST/INVE-B.ST_2026-07-09_GSC.md
- **v2** — 2026-10-05 — REVIEW (routine) — WATCH (unchanged; band ≈ SEK 318 on 0.80 × adjusted NAV) — archive/memos/INVE-B.ST/INVE-B.ST_2026-10-05_GSC.md
- **v3 — 2026-10-21 — REVIEW (attended; full v4.5.0/v4.6.0 method re-test under MODEL v4.6.1) — AVOID (Past WEAK, Future WEAK, SF FAIL).**
  - **What changed:** everything that rested on v2's holding-company substitution rule, which MODEL v4.5.0 retired (J4 and V14: no holding company is valued on NAV; R3–R5 and G4: groups are read as one company at the parent).
    - Gate 0 now writes the group sentence and part sentences. **PASS** (unchanged).
    - Lens **STD**.
    - Past is graded on the consolidated record, ten years rebuilt from nine annual reports (FY2015–25), with the stakes read on the G6 readings. **ADEQUATE (13.9% ROE) → WEAK (0.4% ROCE**; exclude reading alone 3.6%).
    - Future is the weighted grade of the parts. **ADEQUATE → WEAK** (`sub dependency`: five material holdings without a current memo, 67.7% of the base).
    - SF is re-tested on the group P17 denominator, the R9 hairiest number, the J14 worth test and acquisition stop, and the G4 allocation test. **PASS → FAIL** (`compensation` strike; plus an `acquisitions`/`reinvestment` CAUTION on Nova Biomedical).
    - Cheapness: **FAIR → EXPENSIVE**. The band ≈ SEK 318 (NAV) becomes trigger n.m. (no positive price; credits owed).
    - ISIN backfilled (SE0015811963). The register's `trigger_basis: all-cash` backfill line closes (the trigger is now n.m. on the no-cash basis).
  - **What didn't change:** the business description, the low leverage, the rising dividend, and Investor's own NAV arithmetic, which is context only and no longer a band.
  - **Verdict moved:** WATCH → AVOID, driven by parameters and method, not by new evidence about the business. The three fails are (1) the G6 include reading and Patricia's own low returns, (2) unread holdings, and (3) the group P17 denominator. Each is logged with its holding-company proposal in `queue/IDEAS.md` §I. Not held, so no zone.
