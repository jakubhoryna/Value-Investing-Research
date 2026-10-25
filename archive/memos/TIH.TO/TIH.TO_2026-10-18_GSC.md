---
ticker: TIH.TO
company: Toromont Industries Ltd.
exchange: Toronto Stock Exchange (TIH)
isin: CA8911021050
currency: CAD
memo_date: 2026-10-18
memo_version: v1
model_version: v4.5.3
price_at_memo: 210.16 CAD (TSX close 16 Oct 2026; Yahoo Finance chart endpoint TIH.TO, exchangeName TOR, currency CAD, instrument "Toromont Industries Ltd.")
mcap_at_memo: ≈ C$17,327m (context only; 82.447m Q2 2026 diluted weighted average shares, Q2 2026 report, × C$210.16)
verdict: DNAF
quality_past: n.m.
quality_future: n.m.
sf: n.m.
cheapness: n.m.
window: n.m.
trigger_band: "n.m. — Gate 0 FAIL (§6.4): no gate below Gate 0 ran"
aliases: n.m.
px: 210.16
px_unit: CAD
px_date: 2026-10-16
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
next_review: "Gate 0 re-test when (a) CIMCO falls below 10% of revenue, segment assets and Σ positive segment results at a fiscal year-end (FY2024: 9.2% of revenue), (b) the filer prints CIMCO's industrial and recreational revenue with shares that clear the test, or (c) a MODEL ruling reads one engineered product sold to different end markets as one sub-business; then a full ANALYSE"
position: —
produced_by: ROUTINE
run_base: d23dea429d3093141d85d71b888bff9b8965505f
---

# TIH.TO — Toromont Industries Ltd.: GSC Memo

## 1. Verdict
Understanding **FAIL** (one-level decomposition: the CIMCO unit, 10.1% of FY2025 revenue, combines industrial and recreational refrigeration lines that differ in paying customer, reported by the filer without their shares) → **DO NOT ANALYSE FURTHER**. Past, Future, shareholder-friendliness and cheapness were not run.

Toromont is simple to describe at the top. It is the exclusive Caterpillar dealer for Eastern and Central Canada, selling, renting and servicing heavy equipment, plus a refrigeration contractor, CIMCO. The problem sits in the smaller unit. CIMCO crossed the 10% materiality line in FY2025 (10.1%, against 9.2% in FY2024). Its package revenue comes from two markets the filer reports separately: food-and-beverage processors and cold-storage operators, and ice-rink owners. Those are different paying customers, and the filer prints no shares for them. MODEL v4.5.x fails Gate 0 for such a unit. This is a parameter-driven result, not a finding of incomprehension or obfuscation. It flips if CIMCO drops back below 10% of revenue, the filer prints a split that clears the test, or a MODEL ruling treats one engineered product sold to two end markets as one sub-business.

## 2. Understanding
**Group sentence.** Toromont Industries Ltd., a TSX-listed company headquartered in Concord, Ontario, sells, rents and services Caterpillar and other makers' mobile equipment, engines, lift trucks and power enclosures as the exclusive Caterpillar dealer for Manitoba to the Atlantic provinces and most of Nunavut. Its customers are contractors, miners, utilities, municipalities, manufacturers and data-centre suppliers. Through CIMCO it also designs, builds, installs and services natural-refrigerant refrigeration systems for food processors, cold-storage operators and ice rinks in Canada and the US. Canada was 92% of FY2025 revenue.

**Units (P22; FY2025 financial statements, note 28; FY2025 MD&A).** Intersegment revenue is not reported; corporate is not a segment.

| Unit | FY2025 revenue (C$m) | Revenue share | Segment OI share | Identifiable-assets share | Material |
|---|---|---|---|---|---|
| Equipment Group | 4,678.7 | 89.9% | 90.6% | 94.4% | yes |
| CIMCO | 524.2 | **10.1%** | 9.4% | 5.6% | **yes** (revenue) |

**CIMCO's market lines (filer-reported).** CIMCO's package revenue is reported every year by market, and product support is a second revenue line. The MD&A prints changes, not shares: FY2025 recreational +51% and industrial −3%; FY2024 recreational +43% and industrial +19%.

| Line | Share of unit FY2025 | Paying customer (filer's text) |
|---|---|---|
| Industrial packages | n/a — not disclosed (FY2019 derived: 32.2%) | "companies engaged in all aspects of the food and beverage industry, including processors, producers and cold storage"; food distribution; mining (ground freezing) |
| Recreational packages | n/a — not disclosed (FY2019 derived: 21.0%) | "recreational facilities": ice-rink owners and operators |
| Product support | 46.2% (filer key ratio) | the installed base, both markets |

**Gate 0 test.**
- **CIMCO.** The industrial and recreational markets are revenue lines the filer reports for the unit, so each is a sub-business. Both lines are well above 10% of the unit in the last year the MD&A printed dollar amounts (FY2019: C$107.8m and C$70.4m of C$334.8m, derived from the reported changes). Recreational revenue has grown faster since then. The filer's segment description is one industry ("thermal management solutions"), but the paying customers differ: food and beverage processors and cold-storage operators on one side, owners of ice rinks on the other. The filer names these lines without their FY2025 shares, so under J13 the unit is irreducible. → **FAIL.**
- **Equipment Group (judgment line, not decisive).** Toromont Cat, Battlefield rentals, Tri-City rentals, Material Handling and SITECH are all described in the same terms: supply, rental and support of mobile equipment. The filer aggregates them as having a similar class of customers and markets and lists a single customer base for the unit. AVL, the enclosure maker, differs in industry but was C$254.7m, 5.4% of the unit, in FY2025. Read as reducible.

CIMCO alone fails Gate 0. **FAIL → DNAF.**

**Lens (note).** STD: Toromont is not a licensed bank or insurer. It has no finance, leasing or insurance part (customer financing is provided by Caterpillar Financial Services). Nothing makes it too hard under (a)–(c). It holds no listed subsidiary or listed holding, so no group dependency arises.

*Framework output, not investment advice.*

---

# APPENDIX

## A. Sources consulted
P14 exploratory searches: 1 of ~5 (ISIN). Documents: 25 retrieved from investor.toromont.com (robots.txt allows all), 6 used for the verdict.
- **FY2025 audited consolidated financial statements** (investor.toromont.com/download/Financial+Statements+-+2025+Q4+(FINAL)+v2.pdf), retrieved 2026-10-18. Used: note 28, segmented information (the two segments and their business units; revenue, operating income and identifiable assets by segment; the aggregation statement on "class of customers and markets served"; "No reportable segment is reliant on any single external customer").
- **FY2025 MD&A** (MD&A - 2025 Q4 (FINAL).pdf), retrieved 2026-10-18. Used: corporate profile; CIMCO key ratios ("Group total revenue as a % of consolidated revenue 10.1%", 2024 9.2%; product support 46.2%); CIMCO market commentary (recreational +51%, industrial −3%); AVL revenue C$254.7m.
- **FY2024 MD&A**, retrieved 2026-10-18. Used: CIMCO market commentary (recreational +43%, industrial +19%).
- **FY2019 MD&A**, retrieved 2026-10-18. Used: CIMCO package revenue C$177,974k and total revenue C$334,755k. The market dollar changes give derived FY2019 lines: Canada industrial −C$20.3m (−17%) → C$99.1m; US industrial −C$19.4m (−69%) → C$8.7m; Canada recreational +C$11.1m (+27%) → C$52.2m; US recreational +C$4.2m (+30%) → C$18.2m. The four lines sum to C$178.2m against reported packages of C$178.0m (rounding).
- **Annual Information Form dated 2026** (Toromont-2026-Annual-Information-Form.pdf), retrieved 2026-10-18. Used: Equipment Group businesses and their customers; CIMCO customer base and markets; Caterpillar dealer agreements (terminable on 90 days' notice); 81,449,458 shares outstanding at 31 Dec 2025.
- **Q2 2026 reporting package**, retrieved 2026-10-18. Used: diluted weighted average shares 82,447,005 (Q2 2026), the context share count only.
- **Price:** Yahoo Finance chart endpoint TIH.TO, close C$210.16 on 16 Oct 2026 (exchangeName TOR, currency CAD, instrument "Toromont Industries Ltd."; no split events in the period).
- **ISIN** CA8911021050 (CUSIP 891102105): onvista.de and MarketVector security profiles, via one search.
- Also retrieved but not needed for the verdict: the FY2016–FY2024 financial statements and MD&As, the Q2 2025 package, and the 2025 and 2026 management information circulars.
- **Unretrievable:** none. Prior-check: no memo in `memos/` or `archive/memos/`, no register row and no `register.csv` line matches "Toromont" or CA8911021050; no `queue/evidence/TIH.TO_*` file.
