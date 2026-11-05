# PYPL — INCOMPLETE evidence — REVIEW 2026-11-05 2111

- Key: PYPL · Job: REVIEW · D 2026-11-05 · T 2111 · base sha c5544b8585588e22083fe5c237bad53c4a0bac63 · live model_version v4.8.0
- Prior memo: memos/PYPL/PYPL_2026-10-21_GSC.md (memo v6, model_version v4.6.1)
- Named gap: **data access: price endpoint HTTP 429** — `query1.finance.yahoo.com/v8/finance/chart/PYPL` returned HTTP 429 ("Edge: Too Many Requests") on every attempt from 20:14 to 21:03 UTC (41 attempts). The current price is a Gate 2 input (`px`, every multiple, the cheapness verdict). No verdict is recorded here.
- Selection: priority 1b, `▶ Method re-tests v4.8.0` (Turned — Past, customer funds).

## Work done (every gate except the price)

The v4.8.0 re-test was carried through Gate 0, Past, Future and SF from primary filings; only `px` is missing. Findings below are figures and readings, never a grade or a verdict.

### Segregated customer funds (§2·1A v4.8.0)

Segregation evidence: 10-K FY2025 (acc. 0001633917-26-000024), Note 1, "Funds receivable and customer accounts" policy paragraph — PayPal holds customer balances as direct claims against it (amounts due to customers), must hold eligible liquid assets ≥ 100% of balances in certain jurisdictions, "restrict[s] the use of the assets underlying the customer balances" and identifies them "separately from corporate funds"; same wording in 10-K FY2016 (acc. 0001633917-17-000027) and FY2017 (acc. 0001633917-18-000029). Interest on the assets is booked in revenue. Customer-fund flows sit outside CFO.

Netted (held safely): customer-account cash and cash equivalents less the footnoted AFS within them, plus customer-account time deposits. Not netted: corporate, MBS/ABS, municipal and commercial-paper AFS; government and agency AFS (no within-12-months split for customer accounts — the maturity table pools every AFS line; J13); funds receivable. Judgment noted: "customer balances deposited with our partners on a short-term basis" sit inside the cash line and were netted as reported.

| item | FY | value | unit | source |
|---|---|---|---|---|
| customer-account cash & cash equivalents | FY2015 | 5,245 | $m | 10-K FY2016 (acc. 0001633917-17-000027), Note "Funds receivable and customer accounts" composition table |
| customer-account time deposits | FY2015 | 830 | $m | same table |
| customer-account cash & cash equivalents | FY2016 | 4,319 | $m | 10-K FY2017 (acc. 0001633917-18-000029), customer-account composition table |
| customer-account time deposits | FY2016 | 522 | $m | same |
| customer-account cash & cash equivalents | FY2017 | 5,192 | $m | same |
| customer-account time deposits | FY2017 | 739 | $m | same |
| customer-account cash & cash equivalents | FY2018 | 5,642 | $m | 10-K FY2019 (acc. 0001633917-20-000028), customer-account composition table |
| customer-account time deposits | FY2018 | 389 | $m | same |
| customer-account cash & cash equivalents | FY2019 | 8,387 | $m | same |
| customer-account time deposits | FY2019 | 514 | $m | same |
| customer-account cash & cash equivalents | FY2020 | 13,222 | $m | 10-K FY2021 (acc. 0001633917-22-000027), composition table |
| customer-account time deposits | FY2020 | 233 | $m | same |
| customer-account cash & cash equivalents | FY2021 | 12,723 | $m | same |
| customer-account time deposits | FY2021 | 334 | $m | same |
| customer-account cash & cash equivalents (of which AFS ≤ 3m: 192) | FY2022 | 11,363 | $m | 10-K FY2023 (acc. 0001633917-24-000024), Note 8 table and footnote (2) |
| customer-account time deposits | FY2022 | 95 | $m | same |
| customer-account cash & cash equivalents (of which AFS ≤ 3m: 399) | FY2023 | 12,750 | $m | same |
| customer-account time deposits | FY2023 | 82 | $m | same |
| customer-account cash & cash equivalents (of which AFS ≤ 3m: 149) | FY2024 | 15,827 | $m | 10-K FY2025, Note 8 table and footnote (1) |
| customer-account time deposits | FY2024 | 15 | $m | same |
| customer-account cash & cash equivalents (of which AFS ≤ 3m: 374) | FY2025 | 15,969 | $m | same |
| customer-account time deposits | FY2025 | 94 | $m | same |
| customer-account AFS (US gov 3,530; foreign gov 81; corporate 2,441; MBS/ABS 3,831; muni 98; CP 4,230) | FY2025 | 14,457 | $m | same, AFS fair-value table |
| funds receivable | FY2025 | 7,678 | $m | same |
| N netted | FY2015–FY2025 | 6,075; 4,841; 5,931; 6,031; 8,901; 13,455; 13,057; 11,266; 12,433; 15,693; 15,689 | $m | derived: cash & equivalents − footnoted AFS + time deposits |
| customer-account cash & equivalents (AFS 12) / time deposits | 30 Sep 2026 | 12,929 / 137 | $m | 10-Q Q3 2026 (acc. 0001633917-26-000088), Note 8 |
| N netted | 30 Sep 2026 | 13,054 | $m | derived |

### Past readings (B1 rows carried from memo v6, which cites its primary sources; CE re-derived)

| item | FY | value | unit | source |
|---|---|---|---|---|
| worst-of-eight ROCE, 10y (include reading, CE_wc end) | FY2016–25 | 7.3 (7.253) | % | derived: Σ OI include 35,843 ÷ Σ CE 494,158, CE = TA − N − NIBCL |
| worst-of-eight ROCE, 5y | FY2021–25 | 7.8 | % | derived |
| worst-of-eight FCFROCE, 5y (include, CE_wc end) | FY2021–25 | 9.2 (9.203) | % | derived: Σ FCF 28,136.84 ÷ Σ CE 305,749 |
| worst-of-eight FCFROCE, 10y | FY2016–25 | 9.3 | % | derived |
| L/E, funds netted | FY2025 | 218.3 | % | derived: (59,917 − 15,689) ÷ 20,256 |
| L/E, funds netted | 30 Sep 2026 | 251.9 | % | derived: (62,139 − 13,054) ÷ 19,483, 10-Q Q3 2026 balance sheet |
| J6 | — | no sustained decline (FCFROCE declines FY2021–23 end before the latest two years; latest-3 averages above the window's) | — | derived |
| ΔOI/sh, ΔFCF/sh harsher reads | FY2016–25 | 18.2 / 13.0 | % | memo v6 B3 (read (i) defined; growth (ii) rule does not act) |

Reading so far (not a grade): ROCE below P3's 10% on both windows and L/E above P5 without P6 — both Past grounds still fail after netting.

### Future, SF

| item | FY | value | unit | source |
|---|---|---|---|---|
| active accounts | Q3 2026 / Q3 2025 | 440 / 438 | m | 10-Q Q3 2026, key metrics table |
| TPV growth | Q3 2026 | 6 | % | same |
| unit-statement rule | — | not applicable (one segment) | — | memo v6 Gate 0 |
| 10-K publication dates | FY2022–FY2025 | 2023-02-10; 2024-02-08; 2025-02-04; 2026-02-03 | date | SEC submissions index CIK 1633917 |
| Jan / Feb 2023 repurchases | 2023 | 5.9m @ 78.31 / 6.7m @ 77.80 | m sh, $ | 10-Q Q1 2023 (acc. 0001633917-23-000072), Item 2 monthly table |
| Feb / Mar 2024 repurchases | 2024 | 16.3m @ 59.07 / 9.1m @ 59.39 | m sh, $ | 10-Q Q1 2024 (acc. 0001633917-24-000048) |
| Jan / Feb / Mar 2025 repurchases | 2025 | 5.9m @ 88.39 / 6.4m @ 76.86 / 7.1m @ 69.27 | m sh, $ | 10-Q Q1 2025 (acc. 0001633917-25-000064) |
| Feb 2026 repurchases | 2026 | 11.3m @ 43.03 | m sh, $ | 10-Q Q1 2026 (acc. 0001633917-26-000067) |
| 9M 2026 repurchases | 2026 | 94m, $4,553m, avg 47.78; Q3 27m, $1,515m | m sh, $m | 10-Q Q3 2026, cash-flow statement and stock repurchase program note |
| Jan 2023 tranche point-in-time reads (FY2019–21 averages, FY2022 YE stack) | 2023 | M/FCF 19.1; EV/OI nc 29.8; ac 25.9 | × | derived from memo v6 B1 and the rows above |
| 9M 2026 tranche reads (FY2023–25 averages, FY2025 YE stack) | 2026 | M/FCF 7.0; EV/OI nc 10.4; ac 8.1 | × | derived |

Reading so far: pay flag (FY2023 absolute) unchanged; buybacks clearly above worth in Jan–Feb 2023 at the point of purchase, above worth FY2023–25, below in 2026 — ADVERSE turns on whether the stock is above worth at the current price, which is the missing input.

### Gate 2 inputs (30 Sep 2026; price missing)

| item | FY | value | unit | source |
|---|---|---|---|---|
| TTM OI (J1) | TTM Q3-2026 | 5,828 | $m | derived: FY2025 6,065 − 9M'25 4,554 + 9M'26 4,317 (10-Q Q3 2026 income statement) |
| FCF (maint., governs; TTM higher) | FY2025 | 6,701.84 | $m | memo v6 B1/C.3–C.4 |
| debt-equivalents | 30 Sep 2026 | 16,832 | $m | derived: notes principal 12,735 + Paidy 572 + other 46 + CP 200 (10-Q Note 12) + leases 779 (lease note) + designated European balances 2,500 (10-Q liquidity section) |
| cash, STI, S1 | 30 Sep 2026 | 13,031.3 | $m | derived: 7,160 + 3,120 + 0.9 × (3,052 + 5), 10-Q balance sheet and Note 8 |
| diluted shares | 30 Sep 2026 | 846 | m | derived: 837 outstanding (balance sheet) + 9 (Q3 diluted 858 − basic 849) |
| trigger (no-cash) / all-cash / FCF leg | — | 28.33 / 43.73 / 63.37 | $ | derived; price-independent |

## Scope still owed

- [ ] One GET to `query1.finance.yahoo.com/v8/finance/chart/PYPL` for `px`, `px_date`, `currency`, splits.
- [ ] Re-open the governing figures above at their cited locations (README §5 Resume), then write memo v7 on the readings above.
