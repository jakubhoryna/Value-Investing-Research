# TVK.TO — TerraVest Industries Inc. — INCOMPLETE evidence (ANALYSE 2026-10-31)

## 1. Header

- Key TVK.TO · job ANALYSE · D 2026-10-31 · T 0042 · base sha fdd5fd526216992bf7d623e5e6ac3c5a3e77bb80 · model_version v4.8.0 · produced_by ROUTINE
- Prior memo: none. No register row, memo or archived memo names TerraVest (name check over `_REGISTER.md`, `register.csv`, `memos/` and `archive/memos/`). ISIN: n/a — not established (no primary document carrying it was retrievable).
- Named gap: **data access — SEDAR+ bot-blocked.** TerraVest is not an SEC registrant (EDGAR full-text search finds no TerraVest filing). Its audited annual consolidated financial statements, MD&A, annual information form and management information circular are filed only on SEDAR+, and the company's IR site links there rather than hosting them. `www.sedarplus.ca` returned a Radware bot-manager CAPTCHA page ("your activity and behavior on this site made us think that you are a bot") to both a plain request and a headless browser, 2026-10-30 23:43 UTC; not circumvented. Without those documents, nothing a gate grades can be built: the P1 record (B1–B3), the segment note (Gate 0 units, B4 weights, the allocation test), the P20 build, the pay table (P17), the ownership table (P23), RPTs, the repurchase record, and the EV build.
- Not a budget gap: no resumable-record obligation, but the figures retrieved are tabled below for the retry.

## 2. Item table (CAD thousands unless stated; FY ends 30 September)

Sources: PX = query1.finance.yahoo.com/v8/finance/chart/TVK.TO (exchangeName TOR, currency CAD, longName "TerraVest Industries Inc.", instrumentType EQUITY; no split events in the 1-month range); PR-Q3-26 = issuer press release "TerraVest announces third quarter results for fiscal 2026 and dividend declaration", 13 Aug 2026, terravestindustries.com/terravest-announces-third-quarter-results-for-fiscal-2026-and-dividend-declaration/ (body text; its tables are images not read).

| item | FY | value | unit | source |
|---|---|---|---|---|
| Close | 2026-10-30 | 107.59 | CAD | PX |
| Sales, Q3 FY2026 / Q3 FY2025 | Q3 | 460,894 / 405,707 | CAD k | PR-Q3-26, Business Performance |
| Sales, 9M FY2026 / 9M FY2025 | 9M | 1,311,809 / 951,742 | CAD k | PR-Q3-26 |
| Sales ex-acquisitions (base portfolio), Q3 / 9M FY2026 vs prior | Q3, 9M | 404,904 vs 387,183 · 807,382 vs 750,566 | CAD k | PR-Q3-26 |
| Net income, Q3 / 9M FY2026 vs prior | Q3, 9M | 35,604 vs 13,306 · 83,559 vs 77,086 | CAD k | PR-Q3-26 |
| Adjusted EBITDA (non-IFRS; never OI, J1), Q3 / 9M FY2026 vs prior | Q3, 9M | 86,964 vs 68,098 · 230,253 vs 182,685 | CAD k | PR-Q3-26 |
| CFO, Q3 / 9M FY2026 vs prior | Q3, 9M | 30,956 vs 27,957 · 186,044 vs 98,785 | CAD k | PR-Q3-26 |
| Maintenance capex (company figure, P20 tier-1 candidate), Q3 FY2026 vs Q3 FY2025 | Q3 | 14,432 vs 4,571 | CAD k | PR-Q3-26 |
| PP&E paid, Q3 FY2026, of which growth | Q3 | 23,861; growth 9,429 | CAD k | PR-Q3-26 |

## 3. Readings settled

- Key: TVK.TO verified at the endpoint; `px_unit` CAD; px 107.59 at 2026-10-30.
- Deals in the trailing three fiscal years and the live year (names and dates only; consideration not retrieved): Aureus assets (Jan 2025, via the partially owned subsidiary GES — ownership share not retrieved), EnTrans Holding (Mar 2025), Simplex and LBT (Apr 2025), Tankcon FRP (May 2025), New Wave Energy Services assets (Sep 2025), KBK Industries (Jan 2026), Colter Energy Canadian assets (May 2026, via Colter Energy Inc., a partially owned company formed by GES) — PR-Q3-26, Business Combinations. Each above 1% of EV is an acquisition-stop input owed.
- The filer prints a maintenance / growth capex split each quarter (PR-Q3-26): P20 tier 1 (`disclosed`) is likely available once the MD&A series is retrieved.
- Gate 0: products and end markets are visible on the IR site (heating products, LPG/NGL, NH3 and industrial gas storage and transport, energy processing, refined-fuel and water/chemical tanks, tank trailers, well servicing, filtration, back-up power), but the segment note (units, P22 materiality) was not read. No grade, no verdict.

## 4. Scope still owed

- [ ] Audited consolidated financial statements FY2015 (opening balance sheet) through FY2025, and the Q3 FY2026 interim statements — SEDAR+ (issuer no. 00033827 on legacy SEDAR), or any issuer-hosted copy.
- [ ] MD&A FY2016–FY2025 (maintenance capex series for P20 tier 1; segment discussion).
- [ ] 2026 management information circular (pay table, director fees, ownership, RPTs) and the AIF (customers, suppliers, segments).
- [ ] Share-repurchase (NCIB) record by fiscal year; acquisition notes (consideration, acquiree revenue and profit, B64(q)).
- [ ] ISIN from a primary document.
- [ ] Then the full ANALYSE: Gate 0 group sentence and unit sentences, lens STD, B1–B4, Appendix D per material unit, SF, Gate 2.
