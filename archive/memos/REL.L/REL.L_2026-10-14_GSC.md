---
ticker: REL.L
company: RELX PLC
exchange: London Stock Exchange (REL)
isin: GB00B2B0DG97
currency: GBP
memo_date: 2026-10-14
memo_version: v1
model_version: v4.5.3
price_at_memo: 2775 GBp (LSE close 14 Oct 2026; Yahoo Finance chart endpoint REL.L, exchangeName LSE, currency GBp, instrument "RELX PLC")
mcap_at_memo: ≈ £50,479m (context only; 1,819.06m shares in issue net of treasury at 31 Dec 2025, Annual Report 2025 share capital note, × 2775p)
verdict: DNAF
quality_past: n.m.
quality_future: n.m.
sf: n.m.
cheapness: n.m.
window: n.m.
trigger_band: "n.m. — Gate 0 FAIL (§6.4): no gate below Gate 0 ran"
aliases: n.m.
px: 2775
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
next_review: "Gate 0 re-test when the Risk segment no longer combines market-facing verticals above 10% of the unit that differ in paying customer (a re-segmentation that reports Insurance and Business Services as units of their own, each describable in one sentence, or a disposal), or when a MODEL ruling sets how an information-services unit organised in customer-industry verticals is tested; then a full ANALYSE"
position: —
produced_by: ROUTINE
run_base: b8dc34c444a5426550d7f6b0a8a8e5e60681f887
---

# REL.L — RELX PLC: GSC Memo

## 1. Verdict
Understanding **FAIL** (one-level decomposition: the material Risk unit is irreducible) → **DO NOT ANALYSE FURTHER**. Past, Future, shareholder-friendliness and cheapness were not run.

RELX is easy to describe at the top: a provider of databases, analytics and decision tools to professional and business customers, plus trade exhibitions. The difficulty sits one level down. Risk, 36.3% of 2025 revenue and 39.0% of segment profit, is run as "market-facing industry/sector verticals" that the filer defines by the customer's industry and sizes itself: Business Services (over 40% of the unit), sold to banks, lenders and corporates for fraud, identity and financial-crime compliance; Insurance (around 40%), sold to auto, home, commercial and life insurance carriers; and Specialised Industry Data Services (just over 10%), selling commodity, chemical, energy, aviation, HR and tax data to professionals in those industries. Three sub-businesses above 10% of a material unit with different paying customers make the unit irreducible under MODEL v4.5.x, so Gate 0 fails. Legal shows the same pattern. The DNAF is a parameter-driven result, not a finding of incomprehension or obfuscation. It flips back to a full analysis if a re-segmentation clears the test or a MODEL ruling reads customer-industry verticals of one data platform as one paying customer.

## 2. Understanding
**Group sentence.** RELX PLC, a London-listed, UK-headquartered information group, sells mostly electronic subscriptions and per-use transactions of data, analytics and decision tools to insurers, banks, corporates and government agencies (LexisNexis Risk Solutions), to universities, research institutions, corporate R&D and healthcare providers (Elsevier), and to law firms, corporate legal departments, governments and businesses (LexisNexis Legal & Professional), and runs trade exhibitions paid for by exhibitors and attendees (RX), with North America 58% of 2025 revenue; it is a long-established FTSE 100 incumbent.

**Units (P22; Annual Report 2025, note 2, pp. 146–148, 2023–2024 restated).** The filer reports no segment assets, so materiality reads on revenue and Σ positive segment results (adjusted operating profit, the filer's segment measure; central costs excluded).

| Unit | Filer's description | 2025 revenue (£m) | Revenue share | Segment result share | Material |
|---|---|---|---|---|---|
| Risk | information-based analytics and decision tools to evaluate and predict risk | 3,485 | **36.3%** | **39.0%** | **yes** |
| Scientific, Technical & Medical | scientific and medical information, data sets and tools | 2,714 | 28.3% | 30.9% | yes |
| Legal | legal, regulatory and business information with analytics | 1,806 | 18.8% | 12.4% | yes |
| Exhibitions | in-person and online events, digital tools and data | 1,186 | 12.4% | 12.2% | yes |
| Print & print-related | print revenue of the business areas (separate segment from 2025) | 399 | 4.2% | 5.5% | no |

**Sub-businesses of Risk (filer's business review, AR 2025 pp. 10–11).**

| Vertical | Share of unit (filer) | What it sells and who pays (filer's text) |
|---|---|---|
| Business Services | "over 40% of revenue" | fraud and identity, credit risk and financial crime compliance tools for "all risk and compliance segments": banking, lending, ecommerce, gaming, telecoms, corporations |
| Insurance | "around 40% of revenue" | data, analytics and decision tools "for personal auto and home, commercial and life insurance carriers" (underwriting, rating, claims) |
| Specialised Industry Data Services | "just over 10% of revenue" | business intelligence to "professionals in many of the world's largest industries": ICIS (commodities, chemicals, energy), Cirium (aviation), Brightmine (HR), Nextens (tax professionals) |
| Government | "just over 5% of revenue" | identity authentication and investigative tools for US federal, state and local agencies |
| Healthcare | n/a — not disclosed (residual, below 10% by subtraction) | provider, claims and identity data for payers, providers, pharmacies and life sciences |

**Gate 0 test.**
- **Risk.** Each vertical is a "market-facing" operation the filer reports for the unit, with its share, so each is a sub-business. Business Services, Insurance and Specialised Industry Data Services are each at least 10% of the unit. They differ in paying customer: banks, lenders and corporates buying compliance and fraud tools; insurance carriers buying underwriting and claims data; commodity traders, airlines and HR and tax professionals buying market data. The filer itself draws the verticals by customer industry. The unit's industry is read at the filer's segment description, so the paying-customer limb decides it. No exception applies: these are different products for different payers (claims histories for insurers, sanctions screening for banks), not two sides of one transaction or one product sold through different channels. → **FAIL.**
- **Legal (corroborating, not needed).** "Market-facing groups": Law Firms & Corporate Legal around 70%; Government & Academic and News & Business together around 30%, two groups named without separate shares (pp. 22, 24). Law firms and corporate legal departments against government agencies, law schools and businesses buying news and company information differ in paying customer. Irreducible on the same reading (J13).
- **STM and Exhibitions.** Not tested; the verdict does not depend on them.

Risk alone fails Gate 0. **FAIL → DNAF.** Where a reading was open, the harsher governs (J13); here the filer's own vertical definitions and shares decide it.

**Lens (note).** STD: not a licensed bank or insurer and no finance or insurance part; nothing too hard under (a)–(c). The group dependency check was not needed for the verdict.

*Framework output, not investment advice.*

---

# APPENDIX

## A. Sources consulted
P14 exploratory searches: 1 of ~5 (the ISIN). Documents: 3 retrieved, all used, plus one quote GET.
- **RELX Annual Report 2025** (year to 31 Dec 2025), relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2025-annual-report.pdf, retrieved 2026-10-14: pp. 10–11 Risk business overview (revenue £3,485m; the five market-facing verticals and their shares, quoted in §2); pp. 22–24 Legal business overview (market-facing groups and their shares); note 2 pp. 146–148 segment analysis (five reported segments with print separated from 2025, revenue and adjusted operating profit 2023–2025 restated, revenue by geography, format and type; no segment assets); share capital note (1,819,061,446 shares in issue net of treasury at 31 Dec 2025, the context share count).
- **RELX PLC transaction-in-own-shares announcement**, SEC Form 6-K exhibit 99.19 (accession 0000929869-25-000053, sec.gov), retrieved 2026-10-14: issuer RELX PLC, ordinary shares of 14 51/116p, ISIN GB00B2B0DG97; located with one search.
- **Price:** Yahoo Finance chart endpoint, REL.L, close 2775 GBp on 14 Oct 2026 (exchangeName LSE, currency GBp, instrument "RELX PLC"); no split events in the period.
- **Unretrievable:** none.
- **Prior-check:** no memo in `memos/` or `archive/memos/` and no register row matches "RELX", "Reed Elsevier" or GB00B2B0DG97; no `queue/evidence/REL.L_*` file.
