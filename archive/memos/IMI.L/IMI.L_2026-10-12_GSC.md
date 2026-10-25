---
ticker: IMI.L
company: IMI plc
exchange: London Stock Exchange (IMI)
isin: GB00BGLP8L22
currency: GBP
memo_date: 2026-10-12
memo_version: v1
model_version: v4.5.3
price_at_memo: 3110 GBp (LSE close 12 Oct 2026; Yahoo Finance chart endpoint IMI.L, exchangeName LSE, currency GBp, instrument "IMI plc")
mcap_at_memo: ≈ £7,784m (context only; 250.3m FY2025 weighted diluted shares, derived as profit £309.9m ÷ diluted EPS 123.8p, × 3110p)
verdict: DNAF
quality_past: n.m.
quality_future: n.m.
sf: n.m.
cheapness: n.m.
window: n.m.
trigger_band: "n.m. — Gate 0 FAIL (§6.4): no gate below Gate 0 ran"
aliases: n.m.
px: 3110
px_unit: GBp
px_date: 2026-10-12
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
next_review: "Gate 0 re-test when (a) a re-segmentation or disposal leaves no material unit mixing paying customers or industries (for Life Technology: Climate Control, Life Science & Fluid Control and Transport reported as separate units, or two of them below 10% of their unit), or (b) a MODEL ruling changes how a unit whose filer-reported sectors serve different industries is tested; then a full ANALYSE"
position: —
produced_by: ROUTINE
run_base: bea519cf62eca9211e8a1798c78b766bc6a61567
---

# IMI.L — IMI plc: GSC Memo

## 1. Verdict
Understanding **FAIL** (one-level decomposition: the Life Technology unit combines three filer-reported sectors that differ in industry and paying customer, each above 10% of the unit) → **DO NOT ANALYSE FURTHER**. Past, Future, shareholder-friendliness and cheapness were not run.

IMI is easy to describe at the top: it makes valves, actuators and other fluid- and motion-control components for industrial customers worldwide. The problem sits one level down. It reports two segments (FY2024 and FY2025 annual reports). Life Technology, 34.7% of FY2025 revenue, is run as three sectors with their own presidents and reported revenue: Climate Control (£410m, 51% of the unit) sells heating and cooling balancing valves into buildings through HVAC installers and contractors; Life Science & Fluid Control (£232m, 29%) sells precision valves, pumps and detection components to analytical, diagnostic and critical-care instrument makers; Transport (£158m, 20%) sells engine, chassis and thermal-management components to commercial-vehicle makers. No single six-parameter sentence covers buildings, medical instruments and trucks. MODEL v4.5.x fails Gate 0 for such a unit. The DNAF is a parameter-driven result, not a finding of incomprehension or obfuscation. It flips back to a full analysis if a re-segmentation or disposal removes the mix.

## 2. Understanding
**Group sentence.** IMI plc, a London-listed engineering group headquartered in Birmingham, UK, designs and makes fluid- and motion-control products: severe-service valves and actuators for power, oil and gas and process plants (Process Automation); pneumatic and electric motion components for factory and warehouse machinery (Industrial Automation); hydronic balancing and control valves for buildings (Climate Control); precision fluid-handling components for life-science instruments and medical devices (Life Science & Fluid Control); and commercial-vehicle components (Transport). It sells to organisations worldwide, Europe 44% and the Americas 29% of FY2025 revenue.

**Units (P22; FY2025 Annual Report, Note 4 and the operating review).**

| Unit | Filer's description (abridged) | FY2025 revenue (£m) | Revenue share | Adjusted OP share | Material |
|---|---|---|---|---|---|
| Automation | "deep automation technology and applications expertise … in the Process Automation and Industrial Automation sectors" | 1,504 | 65.3% | 68.3% | yes |
| Life Technology | "technologies that enhance and improve everyday life, particularly in the areas of health, sustainability and comfort across the Climate Control, Transport and Life Science & Fluid Control sectors" | 800 | **34.7%** | 31.7% | **yes** |

**Sectors inside each unit (filer-reported revenue, FY2025 / FY2024, £m).**

| Unit | Sector | FY2025 | FY2024 | Share of unit FY2025 | Paying customer (filer's text) |
|---|---|---|---|---|---|
| Automation | Process Automation | 1,006 | 906 | 66.9% | operators of gas, conventional and nuclear power and other severe-service process plants |
| Automation | Industrial Automation | 498 | 508 | 33.1% | manufacturers automating "precision manufacturing, product assembly, logistics and packaging" |
| Life Technology | Climate Control | 410 | 389 | 51.3% | "HVAC installers, control contractors and data centre specialists"; buildings ("Heating Ventilation and Air Conditioning industry") |
| Life Technology | Life Science & Fluid Control | 232 | 236 | 29.0% | "many of the world's leading OEMs" of analytical, diagnostic and critical-care platforms |
| Life Technology | Transport | 158 | 171 | 19.8% | commercial-vehicle makers ("cleaner, safer and more efficient commercial vehicles") |

**Gate 0 test.** Each sector is a separately managed operation (its own president) with revenue the filer reports for the unit, so each is a sub-business under §2 Gate 0.
- **Life Technology.** All three sectors are above 10% of the unit in both years. They differ in industry, on the filer's own words (building HVAC; life-science instruments and critical care; commercial vehicles), and in paying customer (building-services installers and contractors; instrument and device OEMs; truck makers). The segment description itself names three sectors rather than one industry. The unit is irreducible → **FAIL**.
- **Automation (judgment line, not decisive).** Process Automation and Industrial Automation are both above 10% of the unit, and their paying customers differ (process and power plant operators against machine builders and manufacturers). The filer's segment description reads "automation" as one industry, so this memo does not rest on it. Under the harsher reading [J13] it would fail as well.

Life Technology alone fails Gate 0. **FAIL → DNAF.**

**Lens (Appendix-level note).** STD on the evidence: IMI is not a licensed bank or insurer and has no finance, leasing, deposit-taking or insurance part; nothing makes it too hard under (a)–(c). The group dependency check (listed subsidiaries and listed holdings) was not needed for the verdict.

*Framework output, not investment advice.*

---

# APPENDIX

## A. Sources consulted
P14 exploratory searches: 3 of ~5 (two for the pre-2020 results announcements, one for the ISIN). Documents: 10 retrieved, 2 used for the verdict.
- **IMI plc Annual Report 2025** (ESEF xhtml and its xBRL-JSON facts), filings.xbrl.org, LEI 2138002W9Q21PF751R30, period 2025-12-31, retrieved 2026-10-12: Note 4 segmental information (the two segment descriptions quoted in §2; revenue, adjusted and statutory operating profit, assets by segment; geographical revenue); the operating review (sector revenue FY2025 / FY2024 and organic growth); the sector pages (Process Automation, Industrial Automation, Climate Control, Life Science & Fluid Control, Transport: descriptions and customers quoted in §2); Note 27 (Truflo Marine, Automation, held for sale at 31 Dec 2025; immaterial to the test); diluted EPS 123.8p and profit for the year £309.9m (the context share count).
- **Price:** Yahoo Finance chart endpoint, IMI.L, close 3110 GBp on 12 Oct 2026 (exchangeName LSE, currency GBp, instrument "IMI plc"; no split events).
- **ISIN** GB00BGLP8L22 (ordinary shares of 28 4/7p): Börse Frankfurt equity page and IMI's "Admission to trading" RNS announcements (investegate.co.uk), via one search.
- **Retrieved, not needed for the verdict:** IMI Annual Reports 2020–2024 (ESEF, filings.xbrl.org); FY2015, FY2017 and FY2018 preliminary-results RNS (data.fca.org.uk NSM archive). They would supply the FY2015–FY2025 record for a full analysis.
- **Unretrievable:** imiplc.com (every investor page, HTTP 403 "Sorry, you have been blocked", also from a headless browser); not needed, since the ESEF filings carry the annual reports.
- **Prior-check:** no memo in `memos/` or `archive/memos/` and no register row matches "IMI plc" or GB00BGLP8L22.
