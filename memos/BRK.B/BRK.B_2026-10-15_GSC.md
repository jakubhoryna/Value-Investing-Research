---
ticker: BRK.B
company: Berkshire Hathaway Inc.
exchange: "NYSE (BRK.B; class A line BRK.A)"
isin: "n/a — not found: the FY2025 10-K and Q2 2026 10-Q consulted print no CUSIP or ISIN (backfill owed)"
currency: USD
memo_date: 2026-10-15
memo_version: v2
supersedes: archive/memos/BRK.B/BRK.B_2026-06-24_GSC.md
model_version: v4.5.3
price_at_memo: "$526.35 (Class B, NYSE close 14 Oct 2026; price endpoint BRK-B, exchangeName NYQ, currency USD)"
mcap_at_memo: "≈ $1,134bn (2,154,664,073 average equivalent Class B shares, Q2 2026 10-Q; context only)"
verdict: DNAF
quality_past: n.m.
quality_future: n.m.
sf: n.m.
cheapness: n.m.
window: n.m.
trigger_band: "n.m. — Gate 0 FAIL (§6.4): no gate below Gate 0 ran"
aliases: BRK.A class A line 1:1500
px: 526.35
px_unit: USD
px_date: 2026-10-14
trigger: n.m.
mcap_fcf: n.m.
ev_oi: n.m.
ev_oi_all_cash: n.m.
trigger_basis: n.m.
mcap_fcf_3y: n.m.
mcap_fcf_5y: n.m.
ev_oi_3y: n.m.
ev_oi_5y: n.m.
lens: n.m.
holding_keys: n.m.
core_credit: 0
core_period: n.m.
core_currency: n.m.
core_unit: n.m.
core_shares_diluted: n.m.
core_debt_eq: n.m.
core_cash: n.m.
core_oi: n.m.
core_oi_basis: n.m.
core_fcf: n.m.
core_fcf_basis: n.m.
core_oi_3y: n.m.
core_oi_5y: n.m.
core_fcf_3y: n.m.
core_fcf_5y: n.m.
core_fcf_all: n.m.
core_fx: n.m.
core_fx_date: n.m.
core_ratio: n.m.
past_reason: n.m.
future_reason: n.m.
sf_reason: n.m.
next_review_short: n.m.
next_review: "Gate 0 re-test only if Berkshire disposes of or deconsolidates its licensed insurers (GEICO, BH Primary, BHRG) so that no non-captive insurer is a material part, and the Manufacturing segment is re-segmented so that no unit mixes industries above 10% of its revenue; or if a MODEL ruling changes R4(b) or the one-level decomposition. Then a full v4.5.x REVIEW."
position: —
produced_by: ROUTINE
run_base: b774bd9d05c516c06307c67c1e39ab207f51e8f5
---

# BRK.B — Berkshire Hathaway Inc.: GSC Memo

## 1. Verdict
Understanding **FAIL** (too hard, R4(b): material non-captive licensed insurers; the Manufacturing unit is also irreducible) → **DO NOT ANALYSE FURTHER**. Past, Future, shareholder-friendliness and cheapness were not graded.

Berkshire is not hard to describe in words; it is outside what either of the framework's two lenses can read. Its Insurance segment (GEICO, Berkshire Hathaway Primary Group and Berkshire Hathaway Reinsurance Group) is a set of state-licensed insurers that sell auto, commercial property and casualty, and reinsurance cover to unrelated policyholders and cedants. It is 28.3% of FY2025 segment revenue, 47.8% of segment pre-tax earnings and 58.4% of segment identifiable assets. A group with a material licensed insurer that is not a captive arm is too hard under MODEL v4.5.0 (R4(b)). Berkshire also cannot take the FI lens: it has large non-financial parts (BNSF, BHE, Manufacturing, Service and retailing, McLane, Pilot) and publishes no capital ratio covering 90% of its assets. Separately, the Manufacturing segment (21.3% of revenue) combines industrial products, building products and consumer products, each more than 10% of the unit, in different industries, so it fails the one-level decomposition too. The v1 verdict (WATCH, under MODEL v4.1.0 with documented ROCE and cheapness overrides) predates these rules. The move to DNAF is parameter-driven, not a change in the business.

## 2. Understanding
**Group sentence.** Berkshire Hathaway Inc., an Omaha-based US holding company led since 1 January 2026 by CEO Greg Abel, owns state-licensed property-casualty insurers and reinsurers whose float funds a large securities portfolio, and wholly owns a freight railroad (BNSF), regulated utilities and pipelines (BHE), and dozens of manufacturing, service, retail and distribution businesses (McLane, Pilot), selling mainly in the United States.

**Gate 0: FAIL — too hard: (b).** The test order is FI, then too hard, then STD (MODEL §2 Gate 0, Lens).
- **FI does not fit.** The listed entity is the parent of a supervised insurance group: Nebraska's insurance department is lead supervisor of "Berkshire's insurance group" and receives an annual group capital calculation. But the group has material non-financial parts, and the filings print no regulatory capital ratio covering at least 90% of consolidated total assets. On the harsher reading this is limb (a) as well (J13); the verdict is the same.
- **Limb (b) applies.** GEICO's subsidiaries "sell private passenger automobile insurance to individuals in all 50 states". BH Primary writes commercial property and casualty. BHRG writes excess-of-loss, quota-share and facultative reinsurance. All are "subject to regulation by their states of domicile and by those states in which they are licensed". They insure third parties, not the group's own products, so none is a captive finance arm (R2).
- **Materiality (P22)** on the filer's FY2025 segment note (USD m; corporate, eliminations, investment gains and equity-method lines are not units):

| Unit | Revenue | Share | Pre-tax earnings | Share of Σ positive | Identifiable assets | Share | Material |
|---|---|---|---|---|---|---|---|
| Insurance (GEICO, BH Primary, BHRG; underwriting + investment income) | 104,212 | **28.3%** | 24,721 | **47.8%** | 571,145 | **58.4%** | yes, non-captive insurer → too hard |
| Manufacturing | 78,487 | 21.3% | 12,571 | 24.3% | 122,132 | 12.5% | yes, irreducible (below) |
| Service and retailing | 42,647 | 11.6% | 4,039 | 7.8% | 39,124 | 4.0% | yes (not tested) |
| McLane | 50,998 | 13.8% | 676 | 1.3% | 7,135 | 0.7% | yes (revenue) |
| Pilot | 42,198 | 11.5% | 190 | 0.4% | 18,828 | 1.9% | yes (revenue) |
| BHE | 26,297 | 7.1% | 2,342 | 4.5% | 136,515 | 14.0% | yes (assets) |
| BNSF | 23,533 | 6.4% | 7,175 | 13.9% | 82,532 | 8.4% | yes (results) |
| Total segments | 368,372 | | 51,714 | | 977,411 | | |

GEICO alone is 12.1% of segment revenue. The Insurance share holds in FY2024 (28.3%), FY2023 (26.1%) and H1 2026 (26.6% of revenue, 42.8% of pre-tax earnings).

**One-level decomposition, a second ground.** The filer describes Manufacturing as "manufacturers and distributors of numerous industrial, consumer and building products, as well as home building and related financial services", and reports it in three groups: industrial products (aerospace castings and fasteners, specialty chemicals, cutting tools, Marmon) $37,301m, 47.5% of the unit; building products $26,764m, 34.1%; consumer products $14,422m, 18.4%. These differ in industry and paying customer, each is at least 10% of the unit, and the unit is material, so it is irreducible. Service and retailing (aviation services, electronic-components distribution, leasing, auto dealerships, furniture retail) was not tested; the verdict does not depend on it.

**Limb (c)** is not met: on the FY2025 balance sheet, equities, fixed maturities and equity-method stakes were about 27.5% of total assets. The group dependency check on material listed holdings was not needed for the verdict. **FAIL → DNAF.**

*Framework output, not investment advice.*

---

# APPENDIX

## A. Sources consulted
All primary, retrieved 2026-10-15 from sec.gov (CIK 0001067983, uncounted; user agent per CLAUDE.md). P14 exploratory: 0 of ~2. Due-check operations: 0 (priority 1b pick). Documents: 3 primary (plus the EDGAR submissions index), and one quote GET.
- **Form 10-K FY2025** (filed 2026-03-02, accession 0001193125-26-083899): Item 1 Insurance regulation (state licensing; Nebraska DOI lead supervisor of the insurance group; GCC) and GEICO, BH Primary and BHRG descriptions; Note 26 Business segment data (segment list and descriptions; FY2023–25 revenue and pre-tax earnings by segment; FY2025 and FY2024 identifiable assets and goodwill); MD&A Manufacturing (revenue and pre-tax earnings by industrial, building and consumer products, FY2023–25).
- **Form 10-Q Q2 2026** (filed 2026-08-10, accession 0001193125-26-341032): Note 24 Business segment data (insurance earnings Q2 and H1 2026; total operating businesses revenue and pre-tax earnings); average equivalent Class B shares; cover page (BRK.A, BRK.B on NYSE).
- **Balance-sheet securities for limb (c):** equities 297,778, fixed maturities 17,816 and equity-method investments 19,978 against total assets 1,222,176 (USD m, FY2025 10-K; carried from v1, 2026-06-24).
- **Price:** endpoint BRK-B — close $526.35 on 14 Oct 2026, exchangeName NYQ, currency USD, instrument "Berkshire Hathaway Inc. New"; no split event in the range.
- **Unretrievable:** none needed for the verdict. ISIN not printed in the documents consulted (register `isin` stays owed).

## G. Change log
- v1 — 2026-06-24 — ANALYSE — WATCH (Cheapness) — archive/memos/BRK.B/BRK.B_2026-06-24_GSC.md
- **v2 — 2026-10-15 — REVIEW (routine; MODEL v4.5.3 method re-test, TODO `▶ Method re-tests v4.5.0`) — DNAF (Gate 0).** What changed: Gate 0 now applies the v4.5.0 lens test and too-hard pile (R4) and the one-level decomposition, which v1 (MODEL v4.1.0) predates. The Insurance segment (licensed, non-captive insurers; 28.3% of FY2025 segment revenue, 47.8% of segment pre-tax earnings, 58.4% of segment assets) makes the group too hard under R4(b); FI cannot apply because of the material non-financial parts and no group capital ratio covering 90% of assets. The Manufacturing segment (21.3% of revenue) is irreducible on its three product groups (47.5%, 34.1% and 18.4% of the unit). The verdict moves WATCH → DNAF. This is a parameter-driven movement (R4, one-level decomposition, J13), not a change in the business.

  What did not run: Past, Future, SF and Gate 2. v1's findings (Past STRONG by a documented override of the ~12% ROCE; Future ADEQUATE; SF PASS; cheapness FAIR on a P/B gauge with a ≈ $400 reference level) were not re-graded and carry no standing: the v4.5.0 framework has no P/B substitution and no metric override of that kind.

  Observations (not grades): average equivalent Class B shares fell from 2,157,335,139 (Q2 2025) to 2,154,664,073 (Q2 2026), consistent with repurchases; not examined. On 2 January 2026 Berkshire acquired OxyChem from Occidental Petroleum, consolidated in industrial products. Zone: not held. Price $526.35 (register Px $502.65 at 2 Oct 2026; memo price at v1 $488.70).

*Framework output, not investment advice.*
