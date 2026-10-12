---
ticker: DPLM.L
company: Diploma PLC
exchange: London Stock Exchange (DPLM)
isin: GB0001826634
currency: GBP
memo_date: 2026-10-12
memo_version: v1
model_version: v4.5.3
price_at_memo: 7870 GBp (LSE close 12 Oct 2026; Yahoo Finance chart endpoint DPLM.L, exchangeName LSE, currency GBp, instrument "Diploma PLC")
mcap_at_memo: ≈ £10,598m (context only; 134.66m FY2025 weighted average diluted shares, Annual Report 2025 note 9, × 7870p)
verdict: DNAF
quality_past: n.m.
quality_future: n.m.
sf: n.m.
cheapness: n.m.
window: n.m.
trigger_band: "n.m. — Gate 0 FAIL (§6.4): no gate below Gate 0 ran"
aliases: n.m.
px: 7870
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
next_review: "Gate 0 re-test when (a) a re-segmentation or disposal leaves no material unit mixing paying customers or industries (for Controls: Windy City Wire reported apart from the aerospace and defence fastener businesses, or one side below 10% of its unit), or (b) a MODEL ruling sets how a value-added distributor's unit spanning distinct product industries is tested; then a full ANALYSE"
position: —
produced_by: ROUTINE
run_base: 33c71476872184a20df4dbe82024e803f02f6407
---

# DPLM.L — Diploma PLC: GSC Memo

## 1. Verdict
Understanding **FAIL** (one-level decomposition: the Controls unit combines sub-businesses above 10% of the unit that differ in industry and paying customer) → **DO NOT ANALYSE FURTHER**. Past, Future, shareholder-friendliness and cheapness were not run.

Diploma is simple to describe at the top: a decentralised group of value-added distributors of specialised technical consumables and components. The problem sits one level down. Controls, 54.9% of FY2025 revenue, is run as separately managed businesses whose shares of the Sector the filer prints. Windy City Wire (36%) sells low-voltage wire and cable-management kits to the integrators who wire buildings and datacentres in the US. Peerless (23%) and Clarendon (13%) sell certified specialty fasteners to aerospace, space, defence and motorsport manufacturers. The filer's own product split confirms it: wire & cable 41%, specialty fasteners 37%. No single six-parameter sentence covers building low-voltage cabling bought by systems integrators and flight-critical fasteners bought by aircraft makers. MODEL v4.5.x fails Gate 0 for such a unit. The DNAF is a parameter-driven result, not a finding of incomprehension or obfuscation. It flips back to a full analysis if a re-segmentation or disposal removes the mix, or if a MODEL ruling reads a distributor's industry as distribution itself.

## 2. Understanding
**Group sentence.** Diploma PLC, a London-listed group headquartered in London, UK, owns a portfolio of value-added distribution businesses that stock, kit and technically support specialised products — wire and cable, aerospace fasteners, interconnect components, seals, gaskets, hoses and fittings, and medical and diagnostic devices — for manufacturers, contractors, repair shops, hospitals and laboratories, with the USA 53% of FY2025 revenue by origin and the UK and Rest of Europe 35%.

**Units (P22; Annual Report 2025, note 3).** Sector revenue is external revenue; the filer states there is no material inter-Sector revenue.

| Unit | Filer's description (abridged) | FY2025 revenue (£m) | Revenue share | Adjusted OP share (of Σ Sectors) | Material |
|---|---|---|---|---|---|
| Controls | "precision products for highly-technical applications across a wide range of markets, including aerospace, defence, datacentres, energy, infrastructure and medical" | 836.4 | **54.9%** | 65.3% | **yes** |
| Seals | "reliable, high performance" seals, gaskets, hoses, fittings, pumps and valves, OEM to aftermarket | 456.0 | 29.9% | 22.9% | yes |
| Life Sciences | "value-add solutions in the medtech, in vitro diagnostics (IVD) and scientific segments of the global healthcare market" | 232.1 | 15.2% | 11.8% | yes |

**Sub-businesses of Controls (pro forma FY2025 share of Sector revenue, as the filer prints it).**

| Business | Share | What it sells (filer's text) | Paying customer (filer's text) |
|---|---|---|---|
| Windy City Wire (US) | 36% | "low-voltage wire and cable management solutions into broad industrial and infrastructure markets and datacentres" | systems integrators on building projects ("save integrators time and money on projects", AR 2023) |
| Peerless (US) | 23% | "high performance fasteners to customers in the aerospace market" | aerospace manufacturers and their supply chain |
| IS Group (UK) | 17% | "electrical-mechanical interconnect solutions" | defence, energy, medical and industrial customers |
| Clarendon (UK) | 13% | "specialty fasteners into aerospace, space, motorsport and defence markets" | aerospace, space, motorsport and defence manufacturers |
| Shoal, T.I.E., Techsil | 6%, 3%, 2% | wire & cable (UK), automation repair, adhesives | various |

**Gate 0 test.** Each business is a separately managed operation with a revenue share the filer reports for the unit, so each is a sub-business under §2 Gate 0.
- **Controls.** Windy City Wire (36%) against Peerless (23%) and Clarendon (13%): all above 10% of the unit. They differ in industry (low-voltage building and datacentre wire and cable against certified aerospace and defence fasteners; the filer's own product split, wire & cable 41% and specialty fasteners 37%) and in paying customer (low-voltage systems integrators on building projects against aircraft, space and defence manufacturers). The segment description lists markets rather than one industry. The unit is irreducible → **FAIL**.
- **Seals (judgment line, not decisive).** Six businesses each above 7% of the Sector (R&G 23%, Hercules Aftermarket 18%, DICSA 16%, VSP 15%, Hercules OEM 13%, DAS 8%); all sell sealing and fluid-power components, OEM and aftermarket, which the filer describes as one product lifecycle. Read as one industry.
- **Life Sciences (judgment line, not decisive).** Three regional businesses (Europe 43%, North America 39%, Australasia 18%) each selling medtech and IVD products to hospitals, clinics and laboratories. One industry and one paying-customer type.

Controls alone fails Gate 0. **FAIL → DNAF.**

**Lens (Appendix-level note).** STD on the evidence: Diploma is not a licensed bank or insurer and has no finance, leasing, deposit-taking or insurance part; nothing makes it too hard under (a)–(c). It holds no material listed subsidiary or listed holding, so no group dependency arises.

*Framework output, not investment advice.*

---

# APPENDIX

## A. Sources consulted
P14 exploratory searches: 1 of ~5 (the ISIN). Documents: 14 retrieved, 3 used for the verdict.
- **Diploma PLC Annual Report and Accounts 2025** (year to 30 Sep 2025; authorised 18 Nov 2025), diplomaplc.com/media/5s3fi0yk, retrieved 2026-10-12: note 3 Business Sector analysis (three reportable Sectors; revenue, adjusted and statutory operating profit, Sector assets; no material inter-Sector revenue); note 4 geographic analysis by origin; note 9 (diluted weighted shares 134,658,354, the context share count); Sector reviews pp. 22–33 (the descriptions, business shares, product splits and customers quoted in §2).
- **Diploma PLC Annual Report 2023**, diplomaplc.com/media/rkej2axs, retrieved 2026-10-12: Controls page (Windy City Wire "save integrators time and money on projects").
- **Price:** Yahoo Finance chart endpoint, DPLM.L, close 7870 GBp on 12 Oct 2026 (exchangeName LSE, currency GBp, instrument "Diploma PLC"; no split events in the month).
- **ISIN** GB0001826634 (ordinary shares of 5p): Diploma PDMR notification of March 2025 (lse.co.uk RNS) and justETF stock profile, via one search.
- **Retrieved, not needed for the verdict:** Annual Reports FY2016–FY2022 and FY2024, FY2025 preliminary results, H1 FY2026 results (May 2026), the Q3 FY2026 trading-update transcript (16 Jul 2026) and the January 2026 handbook of businesses (diplomaplc.com). They would supply the FY2015–FY2025 record for a full analysis.
- **Unretrievable:** none.
- **Prior-check:** no memo in `memos/` or `archive/memos/` and no register row matches "Diploma" or GB0001826634.
