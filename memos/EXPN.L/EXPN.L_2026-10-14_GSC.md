---
ticker: EXPN.L
company: Experian plc
exchange: London Stock Exchange (EXPN)
isin: GB00B19NLV48
currency: USD
memo_date: 2026-10-14
memo_version: v1
model_version: v4.5.3
price_at_memo: 2696 GBp (LSE close 14 Oct 2026; Yahoo Finance chart endpoint EXPN.L, exchangeName LSE, currency GBp, instrument "Experian plc" / "EXPERIAN PLC ORD USD0.10")
mcap_at_memo: ≈ £24.6bn (context only; 913m weighted-average ordinary shares net of own shares held, FY2026, Annual Report 2026 note 18(d), × 2696p)
verdict: DNAF
quality_past: n.m.
quality_future: n.m.
sf: n.m.
cheapness: n.m.
window: n.m.
trigger_band: "n.m. — Gate 0 FAIL (§6.4): no gate below Gate 0 ran"
aliases: n.m.
px: 2696
px_unit: GBp
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
next_review: "Gate 0 re-test when North America no longer combines two or more filer-reported business lines above 10% of the unit that differ in paying customer or industry (a re-segmentation that reports Financial Services, Verticals and Consumer Services as units of their own, each describable in one sentence, or a disposal), or when a MODEL ruling sets how an information-services unit organised in customer business lines is tested (the REL.L question); then a full ANALYSE"
position: —
produced_by: ROUTINE
run_base: c82793a618b7a4a17a9a85021541e24166e5d854
---

# EXPN.L — Experian plc: GSC Memo

## 1. Verdict
Understanding **FAIL** (one-level decomposition: the material North America unit is irreducible) → **DO NOT ANALYSE FURTHER**. Past, Future, shareholder-friendliness and cheapness were not run.

At the top Experian is easy to describe: a consumer and business credit bureau that sells data, analytics and decisioning software to lenders and other businesses, and credit-monitoring and marketplace services to consumers. The difficulty is one level down. The filer reports its four operating segments as regions. North America, 66.3% of FY2026 revenue and 74.4% of segment Benchmark EBIT, is broken down by the filer itself into three business lines, each well above 10% of the unit. Financial Services (42.3%) is sold to lenders and FinTechs. Verticals (27.0%) is sold to US hospitals and physician groups (healthcare revenue-cycle software), car makers, dealers and auto insurers, and advertisers. Consumer Services (30.7%) is paid for by consumers' memberships and by the lenders and partners on its marketplace. Business lines above 10% of a material unit that differ in paying customer, and in Health's case in industry, make the unit irreducible under MODEL v4.5.x, so Gate 0 fails. Latin America and UK and Ireland show the same pattern. This DNAF follows from the framework's parameters. It is not a finding of incomprehension or obfuscation. The verdict flips back to a full analysis if a re-segmentation clears the test, or if a MODEL ruling reads customer business lines of one data platform as a single paying customer.

## 2. Understanding
**Group sentence.** Experian plc, a Jersey-incorporated, Dublin-headquartered, London-listed (FTSE 100) global information-services group reporting in US dollars, sells credit, identity, fraud and other data with analytics and decisioning software, mainly on subscription and per-use terms. It sells to lenders and FinTechs (Financial Services), to car makers, dealers and insurers, US healthcare providers and advertisers (Verticals), and to consumers through free and paid credit-monitoring memberships and a lending marketplace (Consumer Services). It operates in four regions, North America providing 67% of FY2026 revenue; it is a long-established incumbent that describes itself as "the largest credit bureau operator in the world" (p. 13), with Serasa in Brazil.

**Units (P22; Annual Report 2026, note 10(a), pp. 174–176).** The reportable segments are the four regions; Central Activities is a reconciling column, not a unit. Shares use ongoing-activities revenue (US$8,425m), Σ positive segment Benchmark EBIT (US$2,571m; the filer's segment measure) and segment total assets (US$13,233m).

| Unit | FY2026 revenue (US$m) | Revenue share | Segment EBIT share | Segment assets share | Material |
|---|---|---|---|---|---|
| North America | 5,587 | **66.3%** | **74.4%** | **55.3%** | **yes** |
| Latin America | 1,297 | 15.4% | 15.5% | 21.5% | yes |
| UK and Ireland | 942 | 11.2% | 8.6% | 12.2% | yes |
| EMEA and Asia Pacific | 599 | 7.1% | 1.6% | 11.0% | yes (assets) |

**Sub-businesses of North America (note 9(a), p. 172: revenue from external customers by business line and region; business-line descriptions, Strategic report pp. 10–14).**

| Business line | FY2026 revenue (US$m) | Share of unit | What it sells and who pays (filer's text) |
|---|---|---|---|
| Financial Services | 2,363 | **42.3%** | credit, identity and fraud data, analytics and decisioning to "Lenders" and "FinTechs" |
| Verticals | 1,510 | **27.0%** | Automotive (vehicle history and valuation data for "automotive manufacturers, dealer networks, auto finance providers, and insurers"); Health (patient identity, eligibility, claims and revenue-cycle software for "Hospitals, physician practices, and revenue cycle management providers in the USA"); Marketing Services (identity graphs and audiences for "Advertisers, media agencies, publishers and digital platforms") |
| Consumer Services | 1,714 | **30.7%** | credit reports and scores, identity protection and personalised credit offers to individuals (memberships; marketplace fees from lenders; Partner Solutions data-breach support) |

**Gate 0 test.**
- **North America.** Each business line is a revenue line the filer reports for this unit, with its amount, so each is a sub-business. All three are at least 10% of the unit. Financial Services is paid for by lenders buying credit and fraud decisioning. Verticals is paid for by hospitals and physician groups buying claims and revenue-cycle software, by car makers, dealers and insurers buying vehicle data, and by advertisers buying audiences. Consumer Services is paid for by consumers' subscriptions, and by lenders and partners on its marketplace and breach-support contracts. Financial Services and Verticals differ in paying customer, and Health also differs in industry (healthcare revenue-cycle management against credit reporting). Consumer Services differs from Financial Services in what is sold and to whom: subscriptions and a lead marketplace, against bureau data and decisioning. No exception applies. Lead fees paid by lenders on Experian's own marketplace and lenders' purchases of credit files are different products, not two sides of one transaction. The same goes for Verticals and Financial Services: different products for different payers, not one product sold through different channels. → **FAIL.**
- **Latin America (corroborating, not needed).** Financial Services 73.2% and Consumer Services 24.9% of the unit: banks and FinTechs against consumers (and the banks paying for Limpa Nome debt renegotiation). Irreducible on the same reading (J13).
- **UK and Ireland (corroborating, not needed).** Financial Services 63.2%, Consumer Services 23.4%, Verticals 13.5%. Irreducible on the same reading.
- **EMEA and Asia Pacific.** Financial Services 100% of ongoing revenue; not tested further, since the verdict does not depend on it.

North America alone fails Gate 0. **FAIL → DNAF.** Where a reading was open, the harsher one governs (J13). Here the filer's own business-line amounts by region decide it.

**Lens (note).** STD. Experian is not a licensed bank or insurer, nor the parent of a supervised banking or insurance group, and has no material finance or insurance part. Nothing is too hard under (a)–(c). The group dependency check was not needed for the verdict (no material listed subsidiary or listed holding was identified; investments in associates US$18m).

*Framework output, not investment advice.*

---

# APPENDIX

## A. Sources consulted
P14 exploratory searches: 3 of ~5 (one to locate the annual report, two for the ISIN). Documents: 2 retrieved and used, plus one quote GET.
- **Experian Annual Report 2026** (year to 31 March 2026), FCA National Storage Mechanism filing mirrored at reports.ticker.app/635400RXXHHYT1JTSZ26/2026-06-11/NI-000146608.pdf (LEI 635400RXXHHYT1JTSZ26), retrieved 2026-10-14. Pages used: pp. 6–7 (at a glance: business lines Financial Services 53%, Verticals 20%, Consumer Services 27% of Group revenue; regions); pp. 10–14 (business model and Verticals descriptions, key clients quoted in §2); pp. 33–35 (Chief Executive's review, regional highlights); p. 65 (Financial review, revenue and Benchmark EBIT by business line; Business-to-Business split into Financial Services and Verticals from 1 April 2025, FY2025 re-presented); note 9(a) p. 172 (revenue by business line and region, FY2026 and FY2025); note 10(a) pp. 174–176 (IFRS 8 segment income statement, Benchmark EBIT reconciliation, segment balance sheet); note 18(d) p. 185 (913m weighted-average shares, 919m diluted, FY2026); note 38 (959.2m shares in issue at 31 March 2026). "Corporate headquarters in Dublin, Ireland" (Board activities, governance report); "Experian plc is a Jersey-incorporated company" (p. 62); "the largest credit bureau operator in the world" (p. 13).
- **Experian plc transaction-in-own-shares RNS, 25 September 2023** (investegate.co.uk, announcement 7776685), retrieved 2026-10-14: issuer Experian plc; ordinary shares; treasury shares and shares in issue at that date. It confirms identity, not the ISIN.
- **ISIN GB00B19NLV48:** tier-2 identity from justETF, boerse.de and Fidelity UK factsheets (search results, 2026-10-14), each naming Experian plc. The annual report does not print the ISIN. Logged as a secondary-sourced identity.
- **Price:** Yahoo Finance chart endpoint, EXPN.L, close 2696 GBp on 14 Oct 2026 (exchangeName LSE, currency GBp, instrument "Experian plc"); no split events in the period queried.
- **Unretrievable:** none.
- **Prior-check:** no memo in `memos/` or `archive/memos/` and no register row matches "Experian" or GB00B19NLV48; no `queue/evidence/EXPN.L_*` file.
