# EVIDENCE NOTE — Kardex Holding AG (`KARN.SW`)

**Status at extraction (2026-09-09):** no live row.
**Provenance:** extracted verbatim from the 2026-09-05 → 09-08 scheduled-run drafts listed below, which were written against a framework **reconstructed from the book, not from the live `MODEL.md`** (TRACK/PASS verdicts, "ROIC"/"invested capital" on the drafts' own basis, EV/EBIT trigger lines). **Every verdict, gate call, multiple and trigger in those drafts is void and has been dropped by construction here; only sections carrying sourced figures, tables, business description, open data gaps and sources are carried.** Figures labelled `[computed]` are the drafts' own arithmetic on their own basis — re-derive under §2·1A/§5, never adopt. Tier-2 figures still require the §4 acceptance test; anything below is a starting point for retrieval, not an accepted series.
**Key:** `KARN.SW` per §7.1a suffix convention (the drafts used exchange-prefix keys, e.g. `OM:`, `SWX:`, `XTRA:`). Run the §7.1a prior-check on company name + ISIN before any ANALYSE. 
**Delete this file once the proper memo is committed** (routing per `queue/TODO.md` v26).

**Source drafts:** `claude_2026-09-06_memo_KARN_kardex_v1.md`

---


## ⟪ from `claude_2026-09-06_memo_KARN_kardex_v1.md` ⟫

### Verdict: **TRACK** — *sourced lines and tables only; verdict prose dropped*
**The reason it is TRACK and not a purchase is a mix problem hiding inside a growth number.** Bookings rose **25.8% in H1 2026** and the backlog **41.8%** `[sourced]` — but the growth is in the **5.0%-margin** segment, not the **16.1%-margin** one. **Standardized Systems bookings grew 52.9% in fiscal 2025; Automated Products grew 8.7%** `[sourced]`. A company growing fastest where it earns least is not straightforwardly compounding, and the H1 2026 EBIT margin of **6.8% against 11.8%** is what that looks like in the accounts.

### Gate 1 — Do I understand it?
**Pass.**

Kardex sells automated storage and retrieval: vertical lift modules and carousels that bring the goods to the picker instead of the picker to the goods, plus the software that directs them, and increasingly the larger automated systems around them. The customer is a manufacturer, distributor or retailer trying to get more throughput out of the floor space it already has. **This is brownfield productivity in its purest form** — the machine goes into an existing building and replaces racking and walking.

Two segments `[sourced, FY2025]`:

| | Bookings | Net revenues | EBIT | EBIT margin |
|---|---|---|---|---|
| **Automated Products** (Kardex Remstar) | EUR 560.6m (+8.7%) | EUR 572.8m (+2.8%) | EUR 92.1m | **16.1%** |
| **Standardized Systems** (Kardex Mlog, AS Solutions, Rocket Solution) | EUR 422.1m (**+52.9%**) | EUR 278.1m (+18.6%) | EUR 13.8m (−4.2%) | **5.0%** |

**Automated Products is 67% of revenue and 87% of EBIT** `[computed]`. **Standardized Systems is where all the growth is.**

**Ownership:** BURU Holding AG and Philipp Buhofer hold **22.1%**; UBS Fund Management 5.1%; free float **72.8%** `[sourced, as at 31-12-2025]`. An anchor holder without control — a different structure from Krones' 51.9% family block, and on balance a better one for a minority holder.

**Dividend policy, stated:** *"distribute normally up to 75% of Kardex's consolidated net profit"* `[sourced, claim]`. **Note what happened to that policy in 2025 — see gate 3.**

### Gate 2 — Is it good? — *sourced lines and tables only; verdict prose dropped*
**Balance sheet** `[sourced]`: equity **EUR 269.7m** at 31-12-2025 (2024: 284.9m), **net cash EUR 136.5m** (2024: 173.3m), equity ratio 53.6%. At 30-06-2026: equity **EUR 245.1m**, net cash **EUR 89.5m**, equity ratio 47.6%.
| | FY2024 | FY2025 |
|---|---|---|
| EBIT `[sourced]` | EUR 98.4m | EUR 101.2m |
| Invested capital = equity − net cash `[computed]` | EUR 111.6m | EUR 133.2m |
| **ROIC (18–22% tax)** `[computed]` | **~71%** | **~59–62%** |
- **The margin is falling.** Group EBIT margin **12.4% (FY2024) → 11.9% (FY2025) → 6.8% (H1 2026)**, guided **8–10% for the full year 2026** `[sourced]`. **The return will follow the margin down.** At an 8% margin on FY2026E revenue the ROIC roughly halves — still exceptional, and still falling.
**Why the margin fell, in the company's own words:** *"The underperformance of Automated Products, combined with significant growth investments in R&D, IT, and Sales & Marketing"*, with *"the comparatively weak order backlog at the start of the year, longer lead times for increasingly complex projects, and customer-driven delays"* leading to *"underutilization of production capacity"* `[sourced, verbatim]`.

#### The 2025 earnings figure is misleading in the company's favour, and it should be stated plainly — *sourced lines and tables only; verdict prose dropped*
**Reported net profit fell 48.3% to EUR 41.8m while EBIT rose 2.8%** `[sourced]`. The cause, from the company's own ad-hoc release, verbatim:
> *"The financial result was impacted by the acquisition of the majority stake in Rocket Solution. As a consequence of the accounting treatment of the acquisition, the loans that Kardex had granted to fund the startup since 2021, were written off in full. Due to this one-time non-cash effect of roughly EUR 39 million, the net profit for the period decreased to EUR 41.8 million (EUR 80.8 million)."* `[sourced, verbatim]`

### Gate 3 — Is it cheap? — *sourced lines and tables only; verdict prose dropped*
**Price: CHF 251.00, stamped "Sep 4, 5:31:48 PM GMT+2", SIX Swiss Exchange** `[sourced — Google Finance, and see the reconciliation below]`. Day range CHF 248.50–254.00; 52-week range **CHF 202.00–333.50**.
**Reconciliation, per verification rule 17b** `[computed]`: **7,730,000 registered shares** of CHF 0.45 nominal `[sourced — Kardex investor relations]` × CHF 251.00 = **CHF 1,940.2m**, against the provider's displayed market capitalisation of **CHF 1.93bn** — **0.5% apart, reconciled.** Dividend yield check: CHF 6.00 ÷ CHF 251.00 = **2.39%**, exactly the displayed yield `[computed]`. **Two independent internal checks pass. This price is usable.**
**FX convention, and the row must carry it.** Kardex **reports in EUR and trades in CHF** — the same defect note (v) logs for Diageo. **EUR/CHF 0.9405, ECB euro reference rate, 4 September 2026** `[sourced — European Central Bank]`. This is the first row in the register to carry a central-bank FX rate dated to the pricing session.
| | Value `[computed]` |
|---|---|
| Market capitalisation | CHF 1,940.2m = **EUR 2,063.0m** |
| Less net cash (30-06-2026) | (EUR 89.5m) |
| **Enterprise value** | **EUR 1,973.5m** |
| EV / FY2025 EBIT (EUR 101.2m) | **19.5x** |
| EV / FY2025 EBITDA (EUR 111.8m) | 17.7x |
| P/E on **reported** FY2025 net profit (EUR 41.8m) | 49.4x — **do not use** |
| **P/E on underlying FY2025 net profit (EUR 80.8m)** | **25.5x** |
| Dividend yield (CHF 6.00) | 2.39% |
**On fiscal 2026 as the company guides it** — revenue growth 15–20% on EUR 850.4m, EBIT margin 8–10% `[sourced]`:
| FY2026E revenue | @8% margin | @9% | @10% |
|---|---|---|---|
| EUR 978m–1,020m | **25.2x** | 21.9x | 19.3x |

#### Mechanical trigger arithmetic — not a price target — *sourced lines and tables only; verdict prose dropped*
| Multiple | Threshold `[computed]` | vs CHF 251.00 | vs 52-week low CHF 202.00 |
|---|---|---|---|
| 18x | CHF 233 | −7.4% | +15% |
| **15x** | **CHF 196** | **−22.1%** | **−3.0%** |
| 12x | CHF 159 | −36.8% | −21% |

### What would need to be true — *sourced lines and tables only; verdict prose dropped*
2. **That Standardized Systems' 5.0% margin rises materially as it scales.** It is now 33% of revenue and growing at 3–6x the rate of the good business. The mid-term target — **EUR 1.5bn revenue for 2029–31 at a 10–14% group EBIT margin** `[sourced, claim]` — is arithmetically impossible unless it does. **Treat as ambition, not evidence.**

### Evidence that would change the verdict — *sourced lines and tables only; verdict prose dropped*
- **The Rocket Solution option.** Founders hold 13% with an option `[sourced, secondary — verify against the annual report]`. The terms are not in hand and they are a claim on the equity.

### Open items and data gaps
- **No segment split for H1 2026** was obtained. The single most decisive gap.
- **Total assets, goodwill and the tax charge were not separately disclosed** in the ad-hoc release; the effective tax rate is inferred from the EBIT-to-net-profit gap and stated as a range.
- **The Rocket Solution consideration and the founders' 13% option terms** come from an earnings-call transcript, a secondary source, and are **not verified against a primary document.**
- **Net cash at 30-06-2026 (EUR 89.5m) is used in the enterprise value while FY2025 EBIT is used in the numerator** — a half-year mismatch, conservative in direction (it raises EV), flagged not corrected.
- **No free-cash-flow figure for FY2025 beyond EUR 20.5m** and no capital expenditure figure was obtained.

---

*Framework output, not investment advice.*

**Sources.** [Kardex Holding AG — Financial Results 2025, ad-hoc release, 12 March 2026 (EQS)](https://www.eqs-news.com/news/ad-hoc/kardex-holding-ag-financial-results-2025/4cf92263-b51e-48de-87fc-3ebaabfdde7c_en) · [Kardex Holding AG — Half-Year Results 2026, 30 July 2026](https://www.tradingview.com/news/eqs:f62237b1a094b:0-kardex-holding-ag-half-year-results-2026/) · [Kardex Holding AG — Financial Results 2025 (full release)](https://www.tradingview.com/news/eqs:65f54a54f094b:0-kardex-holding-ag-financial-results-2025/) · [Kardex — Share information (share count, shareholders, dividend policy)](https://investors.kardex.com/investor-center/share-information) · [Google Finance — Kardex KARN:SWX, close 2026-09-04](https://www.google.com/finance/quote/KARN:SWX) · [European Central Bank — euro foreign exchange reference rates, 4 September 2026](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html) · FY2025 earnings call transcript (secondary, used only to flag the currency error): [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-kardex-reports-record-2025-performance-in-h2-2025-93CH-4557394)


---
*Evidence note — not a memo, not investment advice.*
