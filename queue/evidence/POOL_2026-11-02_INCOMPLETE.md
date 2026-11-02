# POOL — INCOMPLETE evidence — 2026-11-02 0611

- Key: POOL · Job: REVIEW · D 2026-11-02 · T 0611 · base sha 3668514b6b17b0d2caa8dbe5ddcc6256b20835ac · live model_version v4.8.0
- Prior memo: memos/POOL/POOL_2026-10-23_GSC.md (memo_version v1, MODEL v4.6.1)
- Named gap: **data access — price endpoint HTTP 429.** `query1.finance.yahoo.com` and `query2.finance.yahoo.com` (`/v8/finance/chart/POOL`) returned HTTP 429 ("Edge: Too Many Requests") on every call of the run, 05:14–05:46 UTC; `stooq.com` reset the connection. Without px no multiple, no cheapness reading and no current-price-against-worth reading can be written; the last of these decides the SF result (below). No verdict.

## What the run established (v4.8.0 buyback-timing re-test)

Every tranche-year is read at the point of purchase: MCap/FCF (maintenance capex) and EV/OI (J1) on the averages of the trailing three fiscal years whose 10-Ks were published before the purchase, EV from the latest balance sheet published before it. January purchases take the earlier set, February both (the 10-K date falls inside the month), March onward the later set.

| item | FY | value | unit | source |
|---|---|---|---|---|
| Point-in-time sets OI · FCF (maint.) | FY2019–21 / FY2020–22 / FY2021–23 / FY2022–24 / FY2023–25 | 546.0 · 309.8 / 774.2 · 369.8 / 868.4 · 520.5 / 796.5 · 625.3 / 648.0 · 579.1 | $m | derived: B1 of memos/POOL/POOL_2026-10-23_GSC.md (10-Ks FY2016–25, SEC EDGAR CIK 945841) |
| 10-K filing dates | FY2021–FY2025 | 2022-02-25, 2023-02-24, 2024-02-27, 2025-02-27, 2026-02-26 | date | SEC submissions index CIK0000945841 |
| Jan / Feb purchases | 2023 | 0 / 34,851 @ $356.99 | shares | 10-Q Q1 2023, acc. 0000945841-23-000078, Part II Item 2 |
| Jan / Feb purchases | 2024 | 0 / 15,967 @ $390.32 | shares | 10-Q Q1 2024, acc. 0000945841-24-000089, Part II Item 2 |
| Jan / Feb purchases | 2025 | 68,320 @ $337.88 / 20,920 @ $346.53 | shares | 10-Q Q1 2025, acc. 0000945841-25-000072, Part II Item 2 |
| Monthly purchases | Q1 2026 | Jan 0; Feb 20,536 @ $218.60 (withholding); Mar 295,185 @ $203.04 | shares | 10-Q Q1 2026, acc. 0001193125-26-185263, Part II Item 2 |
| Q3 purchases | Q3 2026 | 630,978 @ $176.90; $468.4m left under the plan | shares | 10-Q Q3 2026, acc. 0001193125-26-435644, Part II Item 2 |
| Repurchases net of retirements | Q1–Q3 2026 | 316 / 120 / 631 (64.889 / 22.195 / 112.722) | k shares ($m) | 10-Q Q3 2026, equity statements |
| Debt-equivalents | 30 Sep 2026 | 1,521.4 (debt 1,166.882 + financing costs 2.695 + leases 120.756 + 231.098) | $m | 10-Q Q3 2026, balance sheet and Note 5 debt table |
| Cash | 30 Sep 2026 | 105.657 | $m | 10-Q Q3 2026, balance sheet |
| Diluted shares | Q3 2026 / 9M 2026 | 35.923 / 36.163 | m | 10-Q Q3 2026, Note 2 |
| OI | 9M 2026 / 9M 2025 | 522.486 / 528.195 | $m | 10-Q Q3 2026, income statement (TTM OI 574.5, derived) |
| Point-in-time MCap/FCF | 2023 tranche (862k sh, 2.21%) | 37.6–44.9 | × | derived: avg price × FY2023 diluted shares ÷ sets above |
| Point-in-time EV/OI nc | 2023 tranche | 19.8–28.7 | × | derived; EV from 30 Sep 2022 – 30 Sep 2023 balance sheets (XBRL companyfacts quarter-ends) |
| Point-in-time MCap/FCF · EV/OI | 2024 tranche (843k, 2.21%) | Feb 40.4 / 28.7 · 21.0 / 18.8; Mar–Dec 26.6 · 17.4–17.6 | × | derived |
| Point-in-time MCap/FCF · EV/OI | 2025 tranche (1,271k, 3.41%) | 16.1–24.8 · 14.2–17.8 | × | derived |
| Point-in-time MCap/FCF · EV/OI | 2026 to 30 Sep (1,067k, 2.95%) | 11.0–13.7 · 12.5–14.6 | × | derived |
| Per-year floor | 2019 / 2020 / 2021 | 0.38% / 0.98% / 0.89% | of avg diluted | derived: equity-statement shares ÷ diluted WA (below the floor) |

## Readings settled
- 2023: clearly above worth (MCap/FCF governs the straddle with EV/OI, the less flattering). 2024, 2025: above worth. 2026: at or below worth. 2018 and 2022: clearly above under chairman Stokely (earlier window, CAUTION, same behaviour).
- v1's ADVERSE rested on the 2025 year read (33.1×), which no longer governs.
- The SF result turns on the stock against worth on the reads a purchase today takes (FY2023–25 averages, 30 Sep 2026 balance sheet): EV/OI no-cash reaches 14 at px ≈ $210.19 (MCap/FCF reaches 16 at ≈ $257.9). At or below $210.19: ADVERSE fails → CAUTION, SF PASS (`buybacks`), verdict AVOID (Past). Above it: ADVERSE stands, SF FAIL, AVOID (Past + SF).
- Other v4.8.0 rules do not bind (one segment; read (i) defined for both growth metrics; no customer funds; no deal > 1% of EV in the trailing years).

## Scope still owed
- [ ] One GET to `query1.finance.yahoo.com/v8/finance/chart/POOL` (currency, exchangeName, close and date).
- [ ] Write memo v2 at that price (all other figures above and in the prior chain).
