# EVIDENCE NOTE — Borregaard ASA (`BRG.OL`)

**Status at extraction (2026-09-09):** no live row — already queued in TODO (Norway block).
**Provenance:** extracted verbatim from the 2026-09-05 → 09-08 scheduled-run drafts listed below, which were written against a framework **reconstructed from the book, not from the live `MODEL.md`** (TRACK/PASS verdicts, "ROIC"/"invested capital" on the drafts' own basis, EV/EBIT trigger lines). **Every verdict, gate call, multiple and trigger in those drafts is void and has been dropped by construction here; only sections carrying sourced figures, tables, business description, open data gaps and sources are carried.** Figures labelled `[computed]` are the drafts' own arithmetic on their own basis — re-derive under §2·1A/§5, never adopt. Tier-2 figures still require the §4 acceptance test; anything below is a starting point for retrieval, not an accepted series.
**Key:** `BRG.OL` per §7.1a suffix convention (the drafts used exchange-prefix keys, e.g. `OM:`, `SWX:`, `XTRA:`). Run the §7.1a prior-check on company name + ISIN before any ANALYSE. 
**Delete this file once the proper memo is committed** (routing per `queue/TODO.md` v26).

**Source drafts:** `claude_2026-09-05_memo_BRG_borregaard_v1.md`

---


## ⟪ from `claude_2026-09-05_memo_BRG_borregaard_v1.md` ⟫

### Gate 1 — Do I understand it?
**Pass.**

Borregaard runs one integrated biorefinery at Sarpsborg, Norway. Spruce goes in; lignin-based binding and dispersing agents (BioSolutions), speciality cellulose (BioMaterials) and fine chemicals — principally intermediates for X-ray contrast media — come out. Revenue is essentially price × volume of a handful of product families sold into four unrelated end-markets, and the economics turn on whether the speciality grades command a price premium over commodity substitutes. That is testable from disclosure, and the segment reporting is granular enough to test it.

FY2025 mix `[sourced]`: BioSolutions revenue NOK 4,396m / EBITDA 1,209m; BioMaterials 2,691m / 495m; Fine Chemicals 670m / 174m. Segment EBITDA sums exactly to group EBITDA in every year 2022–H1 2026, and segment revenue reconciles to group within a consistent NOK 40–50m elimination `[computed]` — a clean cross-check that raises confidence in the segment series.

End-market split FY2025 `[sourced]`: construction 38%, agriculture 28%, chemicals/other 21%, food and pharma 13%. Geography: Europe 45%, Americas 29%, Asia 25%.

One structural feature must be carried into every other section: **costs are largely NOK, revenues largely USD and EUR.** Net exposure 2025 was USD 63% (~USD 268m) and EUR 38% (~EUR 146m), with a disclosed sensitivity of ±NOK 40m per 1% FX move before hedging and ±NOK 8.7m after `[sourced]`. Reported price declines therefore do not automatically mean lost pricing power, and reported price increases do not automatically mean gained pricing power. This cuts both ways and is the main reason the goodness gate is scored "moderate confidence".

---

#### Returns
| Period | ROCE `[sourced]` |
|---|---|
| 2022 | 18.1% |
| 2023 | 18.3% |
| 2024 | 17.1% |
| 2025 | 15.7% |
| LTM to 30.06.2026 | **14.4%** |

Company definition `[sourced]`: capital contribution (operating profit before amortisation and other income and expenses) over average capital employed on the last five quarters' closing balances. Stated financial objective: **ROCE above 15% pre-tax over the business cycle** — currently below it, for the first time in the visible series.

Average capital employed rose from 7,700 (2024) to 8,256 (LTM Q2 2026) `[sourced]`. Returns are compressing as the asset base grows. That is the opposite signature of a widening moat, and it is the central finding of this memo.

EBITDA margin has moved the same way: 25.0% (2023) → 24.6% → 24.3% → 23.1% LTM `[computed from sourced revenue and EBITDA]`.

#### Pricing power — the specific test
BioSolutions average gross sales price fell to NOK 10,770/mtds from NOK 12,193/mtds `[sourced]`; BioMaterials to NOK 15,682/mt from NOK 17,588/mt `[sourced]`. Management attributes BioSolutions to weaker USD/EUR, which is consistent with the FX structure above and is a fair defence `[claim]`.

BioMaterials is not so easily defended. On the Q2 2026 call management confirmed **selective price adjustments made specifically to counter Chinese cellulose-ether competition**, and attributed 9% volume growth to them `[sourced]`. Volume bought with price is the observable signature of commoditisation, and it is happening in the segment that is supposed to be protected. The company's claim that 87% of BioMaterials sits in highly specialised grades `[claim]` is not audited and is in tension with this behaviour.

#### Capital allocation — two different companies
The operating discipline is orthodox and adhered to: replacement capex pegged to depreciation, a stated >15% pre-tax IRR hurdle on expansion, leverage at 1.20x against a 1.0–2.25x target and a 3.50x covenant, equity ratio 59%, and a dividend raised every year since the 2012 IPO — 1.00 → 4.75 proposed for 2025, a 12.8% CAGR `[sourced, computed]`, maintained through 2020.

The venture portfolio is where capital has gone. **NOK 245m impaired in Q4 2025** across Alginor, Kaffe Bueno and Lignovations, then **NOK 337m on Alginor alone in Q2 2026** — roughly **NOK 582m in three quarters** `[sourced]`, close to a full year of expansion capex (349m in 2025) and near the entire FY2025 net profit of 600m.

The Alginor sequence is the part that speaks to judgement rather than conditions: carrying value was NOK 292m at 31 March 2026, and rather than stop, Borregaard **made a further NOK 100m of subordinated liquidity available** alongside other shareholders before writing the position down by 337m `[sourced]`. Adding capital to a position already disclosed as facing raw-material supply problems, delayed commercialisation and cost overruns — after a first write-down — is textbook escalation of commitment.

#### Financial strength
**Pass, and this is the strongest part of the file.** Total equity NOK 5,610m on assets of 9,506m (equity ratio 59.0%), net interest-bearing debt 2,141m, leverage 1.20x reported against a 3.50x covenant `[sourced, 30.06.2026]`. There is no solvency question here and no forced-seller risk.

---

### Gate 3 — Is it cheap? — *sourced lines and tables only; verdict prose dropped*
Inputs `[sourced]`: price NOK 156.00 (2026-09-04, MarketScreener); 100,000,000 shares issued less 355,404 treasury = 99.64m outstanding (30.06.2026); net interest-bearing debt NOK 2,141m.
| Measure | Value | Basis |
|---|---|---|
| Market capitalisation | NOK 15,544m | `[computed]` |
| Enterprise value | NOK 17,685m | `[computed]` |
| EV / LTM EBITDA (1,788) | **9.9x** | `[computed]` |
| EV / FY2025 EBIT (1,287) | **13.7x** | `[computed]` |
| P/E on FY2025 reported EPS 6.22 | 25.1x | `[computed]` |
| P/E on FY2025 EPS excluding impairments ≈ 8.64 | **18.1x** | `[computed]` — see note |
| FY2025 FCF after all capex (1,356 − 925 = 431) | 2.8% yield | `[computed]` |
| FY2025 owner earnings after replacement capex only (1,356 − 576 = 780) | **5.0% yield** | `[computed]` |
*Note on the ex-impairment EPS:* the company describes the 4.75 dividend as 55% of net profit excluding impairments `[sourced]`; 4.75 ÷ 0.55 = 8.64 `[computed]`. This is a derived figure, not a reported one, and it is the fairest available normalised earnings number.
**A 5.0% owner-earnings yield on a business earning 14.4% on capital, with returns falling, is not a value-investing entry.** And the yield is about to get worse before it gets better: 2027 guidance is replacement capex 600 plus expansion capex **1,000 (±150)** `[sourced]`, versus 349m of expansion capex actually spent in 2025 — roughly a tripling. On flat operating cash flow, 2027 free cash flow after all capex is negative `[computed]`, against a dividend the company has never cut. Something gives in 2027: the dividend record, the balance sheet, or the capex plan.
The capex itself deserves scepticism. The Sarpsborg debottlenecking is budgeted at **~NOK 800m for 5–10% additional capacity**, with output rising gradually only **from Q2 2027** `[sourced]`. Whether that clears the company's own >15% pre-tax IRR hurdle is not obvious from the arithmetic, and the company has not shown the bridge.

### Open items and data gaps
- Clean financial history spans **2022–H1 2026 only**. FY2022 and FY2023 operating profit are single-source from a partially unreliable extraction and are flagged as indicative.
- EBITA is not a line Borregaard reports; only EBITDA and operating profit. Net income is **not disclosed by segment** — segment reporting stops at EBITDA.
- Fully diluted share count is not separately disclosed.
- No published third-party bear thesis was obtained; Nordic broker research is paywalled and screener-model output is excluded by policy. The bear case above is built from primary filings and from analyst questions on the Q2 2026 call.
- Dividend policy percentage is **contradictory between two company sources** (30–50% on the dividend-policy webpage vs 40–60% in the July 2026 presentation). The webpage appears stale.

### Sources
- [Borregaard Q2 2026 report (2026-07-16)](https://www.borregaard.com/hubfs/Media/InvestorFiles/Q22026/2nd%20quarter%202026%20report.pdf)
- [Borregaard Q2 2026 quarterly and accounting figures](https://www.borregaard.com/hubfs/Media/InvestorFiles/Q22026/Quarterly%20and%20accounting%20figures%202nd%20quarter%202026.pdf)
- [Borregaard Q4 2025 report](https://www.borregaard.com/hubfs/Media/InvestorFiles/Q42025/4th%20quarter%202025%20report.pdf)
- [Borregaard general presentation, July 2026](https://www.borregaard.com/hubfs/Media/InvestorFiles/Q22026/Borregaard%20general%20presentation%20-%20July%202026.pdf)
- [Borregaard dividend policy](https://www.borregaard.com/investors/the-share/dividend-policy/)
- [Q2 2026 earnings call transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-borregaard-posts-solid-q2-2026-results-as-shares-rise-57-93CH-4794832)
- [E24, 2026-02-04 — Q4 2025 impairments](https://e24.no/bors/nyheter/a/303376)
- [E24, 2026-07-16 — Q2 2026 and guidance](https://e24.no/bors/nyheter/a/305032)
- [MarketScreener — BRG quote, 2026-09-04](https://www.marketscreener.com/quote/stock/BORREGAARD-ASA-11751909/)

*Framework output, not investment advice.*


---
*Evidence note — not a memo, not investment advice.*
