# EVIDENCE NOTE — CHAPTERS Group AG (`CHG.DE`)

**Status at extraction (2026-09-09):** no live row.
**Provenance:** extracted verbatim from the 2026-09-05 → 09-08 scheduled-run drafts listed below, which were written against a framework **reconstructed from the book, not from the live `MODEL.md`** (TRACK/PASS verdicts, "ROIC"/"invested capital" on the drafts' own basis, EV/EBIT trigger lines). **Every verdict, gate call, multiple and trigger in those drafts is void and has been dropped by construction here; only sections carrying sourced figures, tables, business description, open data gaps and sources are carried.** Figures labelled `[computed]` are the drafts' own arithmetic on their own basis — re-derive under §2·1A/§5, never adopt. Tier-2 figures still require the §4 acceptance test; anything below is a starting point for retrieval, not an accepted series.
**Key:** `CHG.DE` per §7.1a suffix convention (the drafts used exchange-prefix keys, e.g. `OM:`, `SWX:`, `XTRA:`). Run the §7.1a prior-check on company name + ISIN before any ANALYSE. Serial acquirer of software; the draft could not compute returns — expect Gate 0/1 work to dominate.
**Delete this file once the proper memo is committed** (routing per `queue/TODO.md` v26).

**Source drafts:** `claude_2026-09-05_memo_CHG_chapters-group_v1.md`

---


## ⟪ from `claude_2026-09-05_memo_CHG_chapters-group_v1.md` ⟫

### Verdict — *sourced lines and tables only; verdict prose dropped*
**First, the company reports its own performance on a basis that does not reconcile to its accounts, and the primary basis is not IFRS.** The FY2025 headline is **"total output €195.0m, adjusted operating EBITDA €49.1m"** `[sourced, Annual Report 2025]` — a pro-forma aggregation of 60 operating companies. The consolidated IFRS position for the most recent period obtainable was **H1 2025 revenue €70.96m and a net loss of €16.08m, against H1 2024 revenue €50.02m and a €4.48m loss** `[sourced]`. These are different universes with different numerators, and the annual report leads with the pro-forma one.
| FY2025 EPS measure | Value |
|---|---|
| Reported | **−€0.03** |
| Excluding the securities portfolio | **−€0.48** |
| Excluding securities portfolio *and* share-based compensation | **−€0.05** |

### Gate 1 — Do I understand it?
**Fail.**

#### What the business is
CHAPTERS Group AG is a Hamburg-listed permanent-capital acquirer of small vertical-market software and services businesses — the Constellation Software model, transplanted to German-speaking Europe. As at June 2026 it holds **60 operating companies across 10 countries**, employing more than 1,300 people `[sourced]`, in three segments `[all sourced, FY2025]`:

| Segment | Companies | Total output | EBITDA | EBITDA margin `[computed]` | Organic output growth | Recurring share |
|---|---|---|---|---|---|---|
| Public Sector | 29 | €92.0m | €14.7m | 16.0% | 1.2% | 59.7% |
| Enterprise | 27 | €53.0m | €15.3m | 28.9% | 5.2% | 65.3% |
| Financial Technologies | 3 | €46.8m | €19.1m | **40.8%** | 9.0% | 13.9% |
| Other | 1 | €3.3m | €0.1m | 3.0% | — | — |

The strategy is stated clearly and is coherent on its own terms: buy mission-critical niche software at low multiples, decentralise operating authority, hold permanently, redeploy the cash `[sourced, company presentation 2026-06-30]`. Nothing about the *concept* is hard to grasp.

#### Why it fails anyway — *sourced lines and tables only; verdict prose dropped*
**1. There is no reconciliation between the reporting basis and the accounts.** "Total output" of €195.0m for 60 companies is a pro-forma figure; consolidated IFRS revenue for H1 2025 was €70.96m `[sourced]`. Annualising that and allowing for the sixteen acquisitions made during the year leaves a gap of tens of millions between the two measures that the disclosure obtained does not bridge. **The consolidated IFRS statements sit at roughly pages 88–131 of the annual report and could not be retrieved in this run** `[stated as a limitation, not a criticism]` — but the front half of that report, which is what most readers will use, is pro-forma throughout.
**2. The company's own key-figures table is not internally usable.** As rendered from the June 2026 company presentation, the historic series places a "Revenue" line (€5.0m, €9.6m, €11.5m, €20.8m, €27.8m, €26.4m for 2020–2025) alongside an "EBITDA" line (€5.6m, €11.2m, €14.9m, €24.5m, €30.3m, €49.1m) — **EBITDA exceeding revenue in every year shown, and revenue falling in 2025 while sixteen companies were acquired** `[sourced as extracted; the two lines are evidently on different bases]`. There is presumably an explanation — the revenue line may be holding-company or a subset — but **the presentation does not supply one, and a table whose two headline rows cannot both be true of the same entity is not something to build a valuation on.** This should be verified directly against the PDF before the memo is committed, and it is the first question for IR.
**4. Sixty businesses in ten countries is beyond what segment disclosure at this granularity can convey.** Three segments and a company count do not let an outsider judge which of the sixty are good. The FY2025 disclosure that **three underperforming Public Sector acquisitions contributed negative €10.07m of EBITDA** `[sourced]` demonstrates the point: individually material outcomes are invisible until the company chooses to name them.

#### Returns on capital: not computable
The single most important number for a serial acquirer — the return on the capital it deploys — cannot be calculated, because the denominator appears twice in the company's own documents with a threefold difference (above). For scale only, and **explicitly not as a return figure**: attributable adjusted EBITDA of roughly **€36.8m** `[computed: €49.1m × the disclosed 74.9% CHAPTERS share of consolidated EBITDA]` against the annual report's **€563.4m** invested capital is about **6.5%** — *before* depreciation, amortisation, interest, tax and holding-company cost. On the presentation's €195.1m denominator the same numerator gives 18.9%. **The two answers sit either side of every threshold that matters. That is why the figure is not used.**

#### Organic growth — the number that decides whether a roll-up is compounding or just consolidating
`[all sourced]`:

| | FY2024 | FY2025 |
|---|---|---|
| Organic growth, total output | 11.4% | **1.5%** (4.7% adjusted for one-offs) |
| Organic growth, EBITDA | 1.0% | 12.0% |
| Operating companies | 48 | 60 |

**Organic output growth of 1.5% is the honest reading and 4.7% is the company's, after removing a ~€4m post-merger integration revenue write-off and a ~€1.2m accounting change** `[sourced]`. Either way, growth in FY2025 came overwhelmingly from buying twelve to sixteen more companies. The two-year pattern is also unstable in a way worth noting: output growth was strong and EBITDA growth flat in 2024, then the reverse in 2025.

Management raised FY2026 guidance on 13 July 2026 to **organic adjusted operating EBITDA growth "above 22%"** from "mid-teens", attributing it to AI and automation efficiency gains, value-based pricing, and cluster synergies, with organic revenue growth held at "high single digit" `[sourced, ad-hoc announcement]`. **Note the shape of that raise: margin, not volume.** EBITDA growth of 22% on high-single-digit revenue growth is a cost and pricing story. It may be real; it is also the kind of guidance that is easiest to produce and hardest to audit in a group of sixty companies reporting on a pro-forma basis.

#### Financial strength
Net debt at subsidiary level **€138.5m** (FY2025; €20.2m in FY2024) against equity of **€286m** and holding-company net cash and investments of **€36m** `[all sourced]`. Debt rose almost sevenfold in a year. This is not yet a stretched balance sheet, but the direction is the one that matters for a roll-up: **acquisitions are increasingly debt-funded, and the group is loss-making at the consolidated bottom line.**

### Gate 3 — Is it cheap? — *sourced lines and tables only; verdict prose dropped*
Inputs `[sourced]`: price **€46.85 (2026-09-04, MarketScreener)**; corroborated in magnitude by Google Finance at **€47.20 (2026-09-03 close, Xetra)**. **Note the two sources carry different dates, so the two-source/same-date standard proposed in the price sweep is not fully met here.** Market capitalisation **€1.12bn**; enterprise value **€1.25bn**; approximately **23.9m shares** `[computed]`; 52-week range €25.10 – €47.80.
| Measure | Value |
|---|---|
| Market capitalisation | €1,120m `[sourced]` |
| Enterprise value | €1,250m `[sourced]` |
| Implied net debt | €130m `[computed]` |
| **EV / FY2025 adjusted operating EBITDA (€49.1m, pro-forma)** | **25.5x** `[computed]` |
| **EV / attributable adjusted EBITDA (€36.8m, at the disclosed 74.9% share)** | **34.0x** `[computed]` |
| EV / Sales, 2026 estimate | 5.35x `[sourced, consensus]` |
| P/E, 2026 estimate | **negative** — consensus net loss of €13.85m `[sourced]` |
| Consolidated result, H1 2025 | **net loss €16.08m** on €70.96m revenue `[sourced]` |
The share price has compounded from **€4.96 in January 2021 to €40.15 at June 2026, roughly +709%** `[sourced, company presentation]`, and the market capitalisation has risen every calendar year since 2021 `[sourced]`. **The multiple, not the earnings, has done most of that work** — reported EPS was €0.38 in 2021 and −€0.03 in 2025 `[sourced]`.

### Evidence that would change the verdict — *sourced lines and tables only; verdict prose dropped*
- **One consistent invested-capital definition**, and a stated return-on-invested-capital or acquisition-hurdle disclosure. The company currently discloses **no return target or hurdle rate at all** `[sourced absence, company presentation]` — unusual for an acquirer whose entire pitch is capital allocation.

### Open items and data gaps
- **Consolidated IFRS statements for FY2025 were not obtained.** The annual report PDF truncated at the management report; pages ~88–131 contain the statements. **Every consolidated figure in this memo therefore comes from H1 2025 or from third parties.** This is the largest gap in the file and the reason gate 2 is marked "cannot assess" rather than failed.
- **FY2025 full-year consolidated revenue, EBIT, goodwill, total assets, operating cash flow and cash paid for acquisitions: all not sourced.** For an acquirer, goodwill and cash-paid-for-acquisitions are the two most important missing lines.
- **The presentation key-figures table showing EBITDA above revenue in all six years requires direct verification against the PDF.** It is reported here as extracted and flagged, not asserted as a company error.
- **The €563.4m vs €195.1m invested-capital conflict is unresolved** and no return on capital is computed anywhere in this memo as a result.
- **Share count is computed from market capitalisation divided by price (~23.9m), not sourced from a filing.** All per-share arithmetic inherits that.
- **The two price sources carry different dates** (MarketScreener 04-09, Google 03-09), so this name does not meet the sourcing standard proposed in the price sweep.
- The **74.9% CHAPTERS share of consolidated EBITDA** is taken from the annual report front section; the minority-interest structure behind it is not disclosed at segment or company level.
- **No named third-party bear thesis was obtained**; the bear case is built from the company's own disclosures and their inconsistencies.
- Morningstar's consolidated financials page returned a 403 and could not be used as a cross-check.

### Sources
- [CHAPTERS Group AG — Annual Report 2025](https://www.chaptersgroup.de/wp-content/uploads/2026/05/CHAPTERS-Group-Annual-Report-2025.pdf)
- [CHAPTERS Group AG — Company Presentation, 30 June 2026](https://www.chaptersgroup.com/wp-content/uploads/2026/07/20260630_Company-Presentation_eng-1.pdf)
- [EQS — Reporting of Preliminary Results 2025 and 2026 Outlook (2026-03-12)](https://www.eqs-news.com/news/corporate/reporting-of-preliminary-results-2025-and-2026-outlook/f0de6bed-1eed-49e8-8642-b0a79657c6d8_en)
- [CHAPTERS Group AG — raises 2026 outlook for organic adjusted operating EBITDA growth (2026-07-13)](https://www.chaptersgroup.com/2026/07/13/chapters-group-ag-raises-2026-outlook-for-organic-growth-of-adjusted-operating-ebitda/)
- [CHAPTERS Group AG — Investor Relations](https://www.chaptersgroup.com/investors-relations/)
- [Simply Wall St — H1 2025 consolidated revenue and net loss (2025-10-19)](https://simplywall.st/stocks/de/diversified-financials/etr-chg/chapters-group-shares/news/should-chapters-groups-surging-sales-and-deeper-losses-resha)
- [MarketScreener — CHG quote and consensus, 2026-09-04](https://www.marketscreener.com/quote/stock/CHAPTERS-GROUP-AG-452958/)
- [Google Finance — CHG:ETR, 2026-09-03 close](https://www.google.com/finance/beta/quote/CHG:ETR)
- [stockanalysis.com — CHG market cap history (data as of 2026-06-09)](https://stockanalysis.com/quote/etr/CHG/market-cap/)

*Framework output, not investment advice.*


---
*Evidence note — not a memo, not investment advice.*
