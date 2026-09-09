# EVIDENCE NOTE — Kalmar Corporation (`KALMAR.HE`)

**Status at extraction (2026-09-09):** no live row.
**Provenance:** extracted verbatim from the 2026-09-05 → 09-08 scheduled-run drafts listed below, which were written against a framework **reconstructed from the book, not from the live `MODEL.md`** (TRACK/PASS verdicts, "ROIC"/"invested capital" on the drafts' own basis, EV/EBIT trigger lines). **Every verdict, gate call, multiple and trigger in those drafts is void and has been dropped by construction here; only sections carrying sourced figures, tables, business description, open data gaps and sources are carried.** Figures labelled `[computed]` are the drafts' own arithmetic on their own basis — re-derive under §2·1A/§5, never adopt. Tier-2 figures still require the §4 acceptance test; anything below is a starting point for retrieval, not an accepted series.
**Key:** `KALMAR.HE` per §7.1a suffix convention (the drafts used exchange-prefix keys, e.g. `OM:`, `SWX:`, `XTRA:`). Run the §7.1a prior-check on company name + ISIN before any ANALYSE. Demerged from Cargotec mid-2024 — history-limited (two standalone years); class A/B structure, votes-per-share unverified in the draft.
**Delete this file once the proper memo is committed** (routing per `queue/TODO.md` v26).

**Source drafts:** `claude_2026-09-07_memo_KALMAR_kalmar_v1.md`

---


## ⟪ from `claude_2026-09-07_memo_KALMAR_kalmar_v1.md` ⟫

### Verdict: **TRACK** — *sourced lines and tables only; verdict prose dropped*
**One correction to the queue's framing, in Kalmar's favour.** The restock cautioned that all six priority names were being measured "at or near a record order book." **That is not true of Kalmar.** The order book is **EUR 986m against EUR 977m at 31 December 2025, up 0.9%**, and Q2 book-to-bill was **0.94** `[sourced/computed]`. **Kalmar's returns are being earned on flat orders, not on a surge** — which is a better fact than the one the queue assumed, and it shifts the cycle question from "is the peak about to break" to "has the peak already been and gone without the returns falling."

### Gate 1 — Do I understand it?
**Pass, with one incomplete item.**

Kalmar makes and services the machines that move containers and heavy loads around ports, intermodal terminals and industrial sites: reachstackers, empty-container handlers, terminal tractors, straddle carriers, forklifts at the heavy end of the range, plus automation software and the spare parts and service contracts behind the fleet. The customer is a terminal operator or a heavy industrial site trying to move more boxes per hour through the yard it already has. **This is the same brownfield-productivity mechanism the file exists to underwrite, expressed in a yard rather than a warehouse** — and it is the outdoor complement to Kardex and Interroll indoors.

**Two reported segments** `[sourced — H1 2026 report]`:

| H1 2026 | Sales | Operating profit | Margin `[computed]` |
|---|---|---|---|
| **Equipment** | EUR 593m `[computed: 899 − 306]` | EUR 73.5m | **12.4%** |
| **Services** | EUR 306m | EUR 50.4m | **16.5%** |
| Group (after corporate and eliminations) | EUR 899m | EUR 109.8m reported | 12.2% |

**Services is 34.0% of sales and, before corporate costs, 40.7% of segment profit** `[computed]`. Full-year 2025 services sales were **EUR 602m** `[sourced]`. **The eco portfolio — electrified and lower-emission equipment — was EUR 419m, 47% of consolidated H1 sales, and 39% of orders** `[sourced]`, so the electrification transition is roughly half done in revenue and slightly behind in the book.

**Corporate history, and it is the gate-1 caution rather than a footnote.** Kalmar was demerged from **Cargotec** and began trading as a standalone company in 2024. **There are two years of standalone accounts.** Every ratio in this memo is computed on them.

**Capital structure — two classes, and the listed class is the smaller one** `[sourced — H1 2026 report]`:

| | Shares | Listed? |
|---|---|---|
| Class A | **9,526,089** | **No** |
| Class B | **54,798,029** | Yes (Nasdaq Helsinki) |
| **Total issued** | **64,324,118** | |
| Treasury (class B) | (432,610) — 0.67% | |
| **Net of treasury** | **63,891,508** | |

**Class A shares are 14.8% of the capital and are held outside the market** `[computed]`. The Shareholders' Nomination Board is composed so that *"the two largest shareholders of class A shares are entitled to appoint one (1) member each, and the two largest shareholders of class B shares who do not own any class A shares, are entitled to appoint one (1) member each"* `[sourced, verbatim]`; the class A appointees for 2025 were nominated by **Wipunen varainhallinta oy** and **Mariatorp Oy** — Herlin family holding companies — and the class B appointees by **Varma** and **Ilmarinen** `[sourced]`.

**What is missing, and it is the same gap Campari's row carries: the votes-per-share ratio between the classes is not verified.** Kalmar's own investor pages return **HTTP 403** to this session, and no primary document reached this run states the ratio. **If class A carries multiple votes — the convention in the Finnish family-controlled industrials and in Cargotec before the demerger — then a 14.8% capital holding is a controlling vote block, and a class B holder is a minority in a company controlled elsewhere.** **No figure is asserted. Gate 1 is incomplete on this point and it is one page of the articles of association.**

### Gate 2 — Is it good? — *sourced lines and tables only; verdict prose dropped*
| EUR m | 30-06-2026 | 31-12-2025 |
|---|---|---|
| Total assets | 1,749.2 | 1,748.5 |
| **Total equity** | **723.2** | **717.8** |
| **Goodwill** | **257.7** | **256.3** |
| Other intangible assets | 6.6 | 5.8 |
| Interest-bearing liabilities | 291.2 | 280.7 |
| Cash and cash equivalents | 280.2 | 278.4 |
| **Interest-bearing net debt** | **13.1** | **5.3** |
| Gearing | 1.1% (H1 2025: 9.0%) | — |
| EUR m | Reported operating profit | Items affecting comparability | Comparable |
|---|---|---|---|
| Q2 2026 | 58.3 | (1.3) | 59.6 |
| H1 2026 | 109.8 | (1.5) | **111.3** |
| Q2 2025 | 53.9 | (1.0) | 54.9 |
| H1 2025 | 99.6 | (3.2) | **102.9** |
| **FY2025** | **220.4** | (2.9) | **223.3** |

#### Return on invested capital — the register's common basis
NOPAT over equity plus interest-bearing net debt, goodwill included by construction — the method that reproduces Heineken's disclosed figure exactly and Krones' within 0.7 points `[all computed]`:

| | LTM to 30-06-2026 | FY2025 |
|---|---|---|
| Comparable operating profit | EUR 231.7m | EUR 223.3m |
| Invested capital (equity + net debt) | EUR 736.3m | EUR 723.1m |
| Effective tax rate `[sourced: H1 2026 21.1%, H1 2025 23.0%]` | 21.1% | ~22% |
| **ROIC including goodwill** | **24.8%** | **24.1%** |
| on average invested capital (EUR 729.7m) | 25.1% | — |
| at an 18% tax rate | 25.8% | — |
| at a 24% tax rate | 23.9% | — |
| **on the REPORTED numerator** | **24.7%** | — |
| **ROIC excluding goodwill** (capital EUR 478.6m) | **38.2%** | — |

**The verdict is invariant to every basis question the framework has open.** Post-tax or pre-tax, reported or comparable, period-end or average, 18% tax or 24% tax, goodwill in or goodwill out: **the answer is between 23.9% and 38.2%, and the register's bar has been applied at 7.7%.**

**The company's own figure, and it is not on a stated basis.** Kalmar discloses **"ROCE, last 12 months, %" of 24.1% at Q2 2026, 20.7% at Q2 2025, and 23.0% for full-year 2025** `[sourced]`. **No formula is given in the report's key-figures or definitions section** `[sourced absence — the section names the metric and does not define it]`. **So the coincidence between the disclosed 24.1% LTM and this memo's computed 24.1% for FY2025 is a coincidence and must not be read as a replication.** Two candidate reconstructions were tested `[both computed]`: post-tax comparable operating profit over equity plus net debt gives **24.1%** for FY2025 against a disclosed **23.0%**; pre-tax comparable operating profit over equity plus gross interest-bearing debt — that is, **without netting the EUR 278m cash pile** — gives **22.4%**, which on average capital is close to the disclosed 23.0%. **The second is the better fit, which would make the disclosed figure pre-tax on un-netted capital.** `[inference — not asserted, and it does not matter, because the register computes its own]`

#### A counterexample to note (cc), and it should be recorded
**Note (cc) generalises that "goodwill wedges are small in capital goods and large in consumer" — Krones ~0, Interroll 1.2 points, Nabtesco 1.2 points, Kardex immaterial, against 13 points across the brewers.**

**Kalmar is a capital-goods business with a brewer-sized wedge.** Goodwill of **EUR 257.7m is 35.0% of invested capital**, and the wedge between the inclusive and exclusive returns is **13.4 percentage points** `[both computed]` — **larger than any brewer's.**

**So the generalisation is wrong as stated, and the corrected version is more useful: the wedge tracks acquisition history, not sector.** Krones grew organically and has no wedge; Kalmar inherited two decades of Cargotec's purchases and has a large one. **Note (cc)'s second-order claim should be amended, and MODEL question 8 should stop describing the denominator question as "a consumer-sector question."** It is an acquirer question, and acquirers exist in every sector — which is exactly what question 8's own serial-acquirer paragraph already says about the numerator.

### Gate 3 — Is it cheap? — *sourced lines and tables only; verdict prose dropped*
**Price: EUR 40.04, the close of Friday 2026-09-04, Nasdaq Helsinki** `[sourced — Google Finance previous-close field, page read 2026-09-07 with a live intraday stamp of **"Sep 7, 2:43:58 PM GMT+3 · EUR"**, company name returned as *"Kalmar Oyj"*]`.
**The company's own convention settles which count to use, exactly as note (z) settled Jungheinrich.** Kalmar reports **FY2025 EPS of EUR 2.55 on net profit of EUR 163.3m**, implying **64.04m shares** `[sourced/computed]` — **all shares, both classes, net of treasury.** **So value per share is struck on 63,891,508 shares** (issued 64,324,118 net of 432,610 treasury), per verification item 22's rule: reconcile on the issued count, value on the net count.
| At EUR 40.04 | Value `[all computed]` |
|---|---|
| Market capitalisation (net count 63.89m) | **EUR 2,558.2m** |
| Market capitalisation (issued count 64.32m) | EUR 2,575.5m |
| Plus interest-bearing net debt (30-06-2026) | 13.1 |
| **Enterprise value** | **EUR 2,571.3m** |
| **EV / LTM comparable operating profit (231.7)** | **11.10x** |
| EV / LTM reported operating profit (230.6) | 11.15x |
| EV / FY2025 comparable operating profit (223.3) | 11.51x |
| **P/E on LTM net profit (173.4)** | **14.75x** |
| Dividend yield | ~2.75% `[provider-derived — see open items]` |
| vs 52-week low EUR 33.16 | **+20.7%** |
| vs 52-week high EUR 51.15 | −21.7% |
**On fiscal 2026 as the company guides it** — *"comparable operating profit margin to be above 12.5 percent in 2026"* `[sourced, verbatim]`. On H1 sales annualised at EUR 1,798m `[computed]`, a 12.5% margin is **EUR 225m** and 13.0% is **EUR 234m** → **EV/FY2026E of 11.4x to 11.0x.** **The forward multiple is the trailing multiple. There is no growth discount and no growth penalty in the price.**

#### Mechanical trigger arithmetic — not a price target — *sourced lines and tables only; verdict prose dropped*
| Multiple | Threshold `[computed]` | vs EUR 40.04 | vs 52-week low EUR 33.16 |
|---|---|---|---|
| 12x | EUR 43.31 | **+8.2%** | +30.6% |
| 11x | EUR 39.69 | −0.9% | +19.7% |
| **10x** | **EUR 36.06** | **−9.9%** | **+8.7%** |
| 9x | EUR 32.43 | −19.0% | **−2.2%** `< L` |
| 8x | EUR 28.81 | −28.1% | −13.1% |

### What would need to be true — *sourced lines and tables only; verdict prose dropped*
2. **That the 16.5%-margin service book is an annuity on an installed fleet rather than project aftermarket that moves with equipment deliveries.** Services sales were flat half-on-half in profit terms (EUR 50.4m in both H1 2026 and H1 2025) while equipment profit rose from EUR 66.4m to EUR 73.5m `[sourced]` — **the durable half did not grow and the cyclical half did**, which is the opposite of the pattern the thesis wants.

### Open items and data gaps
- **The ROCE formula is not disclosed** `[sourced absence — the key-figures section names the metric without defining it]`. The register computes its own, so this is a comparability gap rather than a blocker.
- **The class A / class B voting ratio is unverified.** **Gate 1 is incomplete on this point.** `kalmarglobal.com` returns **HTTP 403** to this session on both the shares-and-shareholders and major-shareholders paths — the same organisation egress denial recorded against `krones.com`.
- **The dividend per share is provider-derived, not company-sourced.** The displayed yield of 2.77% at EUR 39.74 implies **DPS ~EUR 1.10** `[computed]`, which is a 43% payout on FY2025 EPS of EUR 2.55 and sits inside the stated **30–50%** policy `[sourced]` — coherent, but not read from a company document. The H1 report's profit-distribution figure of **EUR 64.0m** was recovered but its per-share basis and whether it is one instalment of two were not. **Do not carry the yield as sourced.**
- **H1 2025 net sales were not obtained**, so the LTM sales figure and the margin series are incomplete. Only the profit series is complete.
- **No full-cycle history.** Cargotec's pre-demerger Kalmar segment disclosure was not retrieved.
- **The demerger date was not confirmed from a primary document** — 2024 is sourced, the month is not.
- **Provider market capitalisation reconciliation fails by 14.8%** with the cause identified (class B only). **Not a price defect; a count defect. The price itself is corroborated by the day range and the 52-week range.**
- **Host caveat on the primary source.** Kalmar's own domain 403s, so the H1 2026 report was read from the **GlobeNewswire-hosted PDF of the company's own release** — primary content on a distribution host. **Verification rule 16(2) is satisfied: the document states its own company name and period before any figure was taken.** Re-read from `kalmarglobal.com` at a PC before merge.

---

### Verification — one new finding
**27. NEW — a provider can use two different share counts on the same page, and a two-class capital structure is the cause.** Google Finance's Kalmar page displays a market capitalisation reconciling to **54.80m shares** (class B alone, to 0.02%) beside a P/E reconciling to **64.0m shares** (both classes, to 0.1%) `[both computed]`. **Each figure is internally correct and they are 14.8% apart.** **This is the identified cause of the Fanuc defect's family** — a market capitalisation and an earnings figure struck on different counts — **and it means the mandatory reconciliation of item 21/22 must state WHICH count the provider used, not merely whether the multiplication works.** A reconciliation that "passes" against a single-class count on a two-class company has confirmed nothing about the company. **Rule to add: on any multi-class issuer, reconcile against every disclosed class count and record which one the provider matched.** **Three names now sit in this family: Jungheinrich (provider 53% low), Carlsberg (`V·c`, count owed), Kalmar (provider 14.8% low, cause identified).**

**A proposed new price mark, and it answers MODEL question 5b in practice.** **`V·p` = the last completed session's close for the venue, taken from the previous-close field of a provider page carrying a live intraday stamp for the session in progress.** The live stamp proves the page is current; the previous-close field supplies the completed session. **This is strictly stronger evidence than a page whose own stamp equals the last completed session, because it also proves the page is not stale** — the failure mode of items 20, 24 and 25. **Kalmar is `V·p`.**

---


---
*Evidence note — not a memo, not investment advice.*
