---
ticker: BNZL.L
company: Bunzl plc
exchange: London Stock Exchange (BNZL)
isin: GB00B0744B38
currency: GBP
memo_date: 2026-10-13
memo_version: v1
model_version: v4.5.3
price_at_memo: 2776 GBp (LSE close 13 Oct 2026; Yahoo Finance chart endpoint BNZL.L, exchangeName LSE, currency GBp, instrument "Bunzl plc")
mcap_at_memo: ≈ £9,050m (context only; 326.0m FY2025 diluted weighted average shares, Annual Report 2025 note 8, × 2776p)
verdict: DNAF
quality_past: n.m.
quality_future: n.m.
sf: n.m.
cheapness: n.m.
window: n.m.
trigger_band: "n.m. — Gate 0 FAIL (§6.4): no gate below Gate 0 ran"
aliases: n.m.
px: 2776
px_unit: GBp
px_date: 2026-10-13
trigger: n.m.
mcap_fcf: n.m.
ev_oi: n.m.
ev_oi_all_cash: n.m.
trigger_basis: n.m.
mcap_fcf_3y: n.m.
mcap_fcf_5y: n.m.
ev_oi_3y: n.m.
ev_oi_5y: n.m.
lens: STD
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
next_review: "Gate 0 re-test when (a) the filer reports North America's businesses with their revenue shares and no two sub-businesses above 10% of the unit differ in paying customer or industry, or a re-segmentation leaves no such mixed unit, or (b) a MODEL ruling sets how a distributor's unit serving several customer sectors is tested (TODO IDEAS candidate DPLM.L 2026-10-12); then a full ANALYSE"
position: —
produced_by: ROUTINE
run_base: 654ca71e04721df9e57358cd29fa8002b38610df
---

# BNZL.L — Bunzl plc: GSC Memo

## 1. Verdict
Understanding **FAIL** (one-level decomposition: the North America unit combines sub-businesses that differ in paying customer, named by the filer without their shares) → **DO NOT ANALYSE FURTHER**. Past, Future, shareholder-friendliness and cheapness were not run.

Bunzl is easy to describe at the top: a distributor of goods-not-for-resale to businesses. The problem sits one level down. North America, 53.0% of FY2025 revenue, is one business area, but its largest business, Distribution (about 57% of the unit), has one division selling store supplies to US grocers and another selling goods for resale to foodservice redistributors, while other businesses sell protective equipment to industrial and construction firms. The filer prints none of their shares for the unit, and its sector table is Group-only. MODEL v4.5.x fails Gate 0 for such a unit: a parameter-driven result, not a finding of incomprehension or obfuscation. It flips if the filer prints a split that clears the test, or a MODEL ruling reads a distributor's unit as one industry.

## 2. Understanding
**Group sentence.** Bunzl plc, a London-listed distributor headquartered in London, UK, buys consumable goods-not-for-resale — food packaging, disposable tableware, films and labels, cleaning & hygiene supplies, personal protective equipment and healthcare consumables — from manufacturers and its own-brand sources and delivers them, through about 150 operating companies in 33 countries, to grocers, foodservice redistributors and operators, industrial and construction firms, retailers, cleaning contractors and hospitals and care homes, with North America 53% of FY2025 revenue.

**Units (P22; Annual Report 2025, note 4).** Revenue is external; sales between business areas are not material. Rest of the World is an "other" segment of operating businesses (Latin America and Asia Pacific), so it is a unit.

| Unit | FY2025 revenue (£m) | Revenue share | Adjusted OP share (Σ areas, before corporate) | Segment assets share | Material |
|---|---|---|---|---|---|
| North America | 6,276.7 | **53.0%** | 46.7% | 36.5% | **yes** |
| Continental Europe | 2,442.0 | 20.6% | 21.7% | 27.2% | yes |
| UK & Ireland | 1,883.6 | 15.9% | 16.2% | 20.8% | yes |
| Rest of the World | 1,243.1 | 10.5% | 15.4% | 15.6% | yes |

**Sub-businesses of North America (filer's business review, AR 2025 pp. 22–24).**

| Business | Share of unit | What it sells and who pays (filer's text) |
|---|---|---|
| Distribution — grocery division | n/a — not disclosed | "goods not for resale", "contracted product categories" to "grocery end customers" ("the division of Distribution which supports US grocers"), incl. convenience stores |
| Distribution — foodservice redistribution division | n/a — not disclosed | "goods for resale", "partly uncontracted business" to "foodservice redistributors" |
| Safety businesses | n/a — not disclosed | personal protection and safety equipment to "industrial, construction and e-commerce sectors" |
| Retail supplies; food processor and agriculture; cleaning & hygiene; Canada; Mexico | n/a — not disclosed | store supplies to retailers; supplies to food processors and commercial growers; cleaning materials to cleaning and facilities-management firms |

North America Distribution as a whole is "c.30% of Group revenue" (FY2025 presentation p. 4; AR p. 23), about 57% of the unit (derived: 0.30 × 11,845.4 ÷ 6,276.7).

**Gate 0 test.**
- **North America.** Each row above is a separately managed operation or a division the filer reports for the unit, so each is a sub-business. The grocery and foodservice-redistribution divisions differ in paying customer (grocery chains buying store supplies they consume, against wholesale redistributors buying goods to resell), and the filer contrasts them itself ("goods not for resale" against "goods for resale"). The safety businesses differ from both in industry and paying customer (PPE for industrial and construction firms against food packaging for food retail and foodservice). The filer names these sub-businesses without their shares of the unit, so under J13 the unit is irreducible. The segment description lists sectors ("customers operating primarily in the grocery, foodservice, safety, cleaning & hygiene, retail and healthcare market sectors"), not one industry; the Group-only sector revenue table (note 4: Foodservice 31.2%, Grocery 24.2%, Safety 14.9%, Cleaning & Hygiene 10.7%, Retail 7.8%, Healthcare 7.0%, Other 4.4%) does not count for a unit ("results are not monitored on this basis"). → **FAIL.**
- **Other units (not decisive).** Each also mixes sectors named without shares (e.g. UK & Ireland: Nisbets catering equipment, cleaning & hygiene, grocery). Not tested further.

North America alone fails Gate 0. **FAIL → DNAF.**

**Lens (note).** STD: not a licensed bank or insurer, no finance or insurance part, nothing too hard under (a)–(c). No material listed subsidiary or holding (Nisbets, 80%, is unlisted), so no group dependency.

*Framework output, not investment advice.*

---

# APPENDIX

## A. Sources consulted
P14 exploratory searches: 2 of ~5 (locating the FY2025 report; the ISIN). Documents: 4 retrieved, 3 used for the verdict.
- **Bunzl plc Annual Report 2025** (year to 31 Dec 2025), bunzl.com/media/px0hi0zf/bunzl_ar25_interactive.pdf, retrieved 2026-10-13: p. 5 market sectors (customer descriptions quoted in §2); pp. 22–24 North America business area review and North America Distribution overview (the divisions, "c.30% of Group revenue", "goods not for resale" / "goods for resale"); note 4 segment analysis (four business areas, revenue, adjusted operating profit, segment assets, the Group-only revenue by market sector, no customer ≥ 10% of Group revenue); note 8 (diluted weighted average shares 326.0m, the context share count).
- **Bunzl FY2025 results presentation** (2 Mar 2026), bunzl.com/media/ptdltede/fy25-presentation-full-vfinal2.pdf, retrieved 2026-10-13: p. 4 ("North America Distribution business (c.30% Group revenue) … predominantly grocery and foodservice redistribution customers"); appendix 6 country-by-sector presence.
- **Bunzl FY2025 results announcement** (RNS, 2 Mar 2026), FCA NSM data.fca.org.uk/artefacts/NSM/RNS/a71c7bd1-d735-47ea-b519-ce6174c23ff3.html, retrieved 2026-10-13: business area reviews (same text as the annual report), note 3 segment analysis.
- **Price:** Yahoo Finance chart endpoint, BNZL.L, close 2776 GBp on 13 Oct 2026 (exchangeName LSE, currency GBp, instrument "Bunzl plc"; no split events in the period).
- **ISIN** GB00B0744B38 (ordinary shares of 32 1/7p): LSE admission-to-trading notice (lse.co.uk RNS) and justETF stock profile, via one search.
- **Unretrievable:** none.
- **Prior-check:** no memo in `memos/` or `archive/memos/` and no register row matches "Bunzl" or GB00B0744B38; no `queue/evidence/BNZL.L_*` file.
