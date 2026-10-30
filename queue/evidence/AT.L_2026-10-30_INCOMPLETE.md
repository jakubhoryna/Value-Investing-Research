# AT.L — Ashtead Technology Holdings plc — INCOMPLETE evidence (ANALYSE 2026-10-30)

- Run: ANALYSE · D 2026-10-30 · T 2141 · base sha df90d8bacf21ea8205ac432deabfcf436645e028 · MODEL v4.7.0 · produced_by ROUTINE
- Named gap: **data access — price endpoint HTTP 429.** The cheapness leg needs a current price in the endpoint's unit (`px`, `px_unit`; ANALYSE.md step 5, MODEL §7.1a). query1 and query2.finance.yahoo.com returned HTTP 429 "Too Many Requests" on every call from 20:42 to about 21:35 UTC (one call per minute, about 50 calls, default client). The MODEL §4 tier-3 quote sources tried also failed: Google Finance ("not supported on this device"), Hargreaves Lansdown (HTTP 404), uk.finance.yahoo.com (HTTP 503), lse.co.uk (HTTP 403). No verdict is recorded. Every figure below is sourced from primary documents and is reusable at the retry.
- Identity: ISIN GB00BLH42507 (2025 simplified prospectus). LSE Main Market since 6 October 2025 (AIM from the November 2021 IPO). Registered number 13424040. No register row or memo matches the name or ISIN (prior-check clean).

## Sources (retrieved 2026-10-30)

- Annual reports FY2021–FY2025 (ashtead-technology.com/investors/documents); HY 2026 results presentation; simplified prospectus 1 October 2025; Project Tarifa analyst presentation (December 2024).
- Half-year report to 30 June 2026 (RNS 1 September 2026), FCA National Storage Mechanism: data.fca.org.uk/artefacts/NSM/RNS/5cc18c29-9f0a-4bd2-802a-c55f19a6c785.html.
- P14: 5 exploratory operations (one web search for the interim RNS; four quote pages).

## Window and record (£m; history-limited: November 2021 IPO; FY2020 is the unaudited comparative of AR2021, note 1.4)

| FY | Revenue | OI (J1) | CFO | Capex | Maint. capex (P20) | FCF (maint.) | FCF (all-capex) | Diluted shares (m) | Total assets | NIBCL | Cash | Total liab | Equity | GW+intang |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2020 | 42.401 | 2.717 | 14.982 | 5.073 | 5.073 (= all capex) | 9.909 | 9.909 | 69.998 | 99.896 | 7.758 | 10.958 | 55.111 | 44.785 | 51.044 |
| FY2021 | 55.805 | 7.608 | 7.236 | 7.889 | 7.878 (constructed, floor) | −0.642 | −0.653 | 70.996 | 99.035 | 10.236 | 4.857 | 37.903 | 61.132 | 50.411 |
| FY2022 | 73.120 | 17.718 | 32.854 | 14.453 | 10.325 (constructed) | 22.529 | 18.401 | 80.679 | 135.754 | 20.918 | 9.037 | 60.818 | 74.936 | 70.625 |
| FY2023 | 110.466 | 31.210 | 39.048 | 19.459 | 10.939 (constructed, floor) | 28.109 | 19.589 | 80.969 | 213.694 | 34.228 | 10.824 | 116.108 | 97.586 | 95.448 |
| FY2024 | 168.044 | 42.793 | 30.117 | 29.388 | 23.231 (constructed) | 6.886 | 0.729 | 81.246 | 313.603 | 34.953 | 12.168 | 186.275 | 127.328 | 147.137 |
| FY2025 | 203.195 | 51.555 | 57.621 | 37.198 | 37.198 (constructed, no real growth) | 20.423 | 20.423 | 81.331 | 323.273 | 32.989 | 14.073 | 166.185 | 157.088 | 140.652 |

- J1: statutory operating profit; FY2020 less the US PPP loan forgiveness 0.391 (J3, ambiguous positive). FY2022 as restated in AR2023 (note 2.2). Other operating income (gain on customer-compensated rental-asset losses) and the FY2025 receivable-impairment reversal stay in.
- P20: k = Σ PP&E ÷ Σ revenue FY2020–FY2025 = 0.5067; organic growth as printed FY2021 31.6%, FY2022 23.7%, FY2023 35%, FY2024 14%, FY2025 3%; π = max(3%, UK CPI) 3.0, 9.1, 7.3, 3.0, 3.4%; floor = PP&E depreciation 9.92, 7.88, 7.50, 10.94, 17.85, 21.25. Capitalised software not split out (logged).
- TTM Q2-2026: OI 51.555 − 23.157 + 21.793 = 50.191; CFO 57.621 − 21.092 + 20.377 = 56.906; capex 37.198 − 20.484 + 25.857 = 42.571; FCF 14.335 (= all capex: FY2025 organic 3%, H1 2026 constant-currency 1.7%, both ≤ π). Both below FY2025, so TTM governs.
- Averages: OI 3y 41.853, 5y 30.177; maintenance FCF 3y 18.473, 5y 15.461.
- Returns (worst-of-four): ROCE 14.7% (window FY2020–FY2025), 15.8% (5y); FCFROCE 8.4%, 8.1% (all-capex 6.6%, 6.1%). G6 classes nil.
- Growth: ΔOI/sh 74.8% (geometric) · 61.7% (endpoint); ΔFCF/sh geometric n.m. (FY2021 negative) · 18.4% endpoint; ΔBV/sh 24.7% · 24.6%. L/E FY2025 106%. No J6 decline.
- Balance sheet 30 June 2026: RCF principal 122.016 (carrying 121.442), leases 4.137, provisions 0.516 (warranty and end-of-service benefits, not split) → debt-equivalents 126.669; cash 8.861; equity 170.350; goodwill 112.242; intangibles 26.510; H1 2026 weighted diluted shares 81.364380m.
- Band legs (price-independent): FCF leg 8 × 14.335 ÷ 81.36438 = 140.9p; EV/OI no-cash (7 × 50.191 − 126.669) ÷ 81.36438 = 276.1p; all-cash 287.0p.

## Group and Future inputs

- Four material geographic reportable segments (Europe, Americas, Asia Pacific, Middle East). Segment operating profit FY2023/FY2024/FY2025: Europe 30.283/35.200/42.659; Americas 5.241/6.501/4.781; APAC 4.052/6.912/8.277; Middle East 2.705/5.352/8.541. Segment assets: Europe 167.063/245.525/243.400; Americas 17.293/24.799/31.134; APAC 9.991/16.452/17.763; ME 7.012/13.154/15.918 (FY2022: 93.522/15.335/11.025/5.429). Weights 0.674/0.103/0.120/0.103; pooled segment returns 16.5%/22.6%/43.5%/46.0%.
- Customer statement: "No single customer or group of customers under common control account for 10% or more of Group revenue" (group only; no per-segment statement).

## Shareholder-friendliness inputs

- A Pirie single figure: FY2023 1,194 and FY2024 1,853 (AR2024, LTIP at 771p); FY2024 1,578 and FY2025 1,056 (AR2025). LTIP grants at 150% of salary: 154,417 (May 2023), 79,001 (April 2024), 117,782 (September 2025). Salary 353/406/426 (FY2023–FY2025).
- P17 legs (lower of maintenance FCF, NI): FY2023 21.579 (NI), FY2024 6.886 (FCF), FY2025 20.423 (FCF); trailing three-year legs 12.161, 19.175, 18.473. FY2024 hairiest 1,853 = 26.9% fiscal, 9.7% trailing.
- Directors' total interests 31 December 2025 (incl. vested unexercised options): Pirie 1,477,063; Stewart 400,229. No entity with significant influence; one share class; no buybacks.
- Deals: ACE Winches (Nov 2023) consideration 63.657 incl. loan repaid 11.004, cash acquired 10.065, pro forma OI proxy 10.871; Seatronics and J2 Subsea (Nov 2024) consideration 66.548, cash acquired 2.156, pro forma OI proxy 12.925, ≈ 7.0× TTM adjusted EBITA per the filer.

## Retry

One GET to the price endpoint for AT.L (GBp, LSE). With a close in hand, the memo can be completed from the figures above with no further exploratory work.
