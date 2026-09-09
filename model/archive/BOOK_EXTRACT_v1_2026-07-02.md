# Good Stocks Cheap — First-Principles Extraction & Instruction Audit

**Date:** 2026-07-02 · **Source:** Marshall, *Good Stocks Cheap* (McGraw-Hill, 2017), full text (Preface–Ch. 21 + case studies) · **Purpose:** MODEL-mode re-derivation of the project instructions from the book itself. Companion to `2026-07-02_GSC-project-instructions_v2.md`.

---

## 1. The architecture of the model

Marshall's model is three layers. Top (permanent): **know what to do, do it, don't do anything else** — finance and strategy answer the first; the last two are pure psychology. Middle: **do I understand it? is it good? is it cheap?** — in strict order. Bottom (the part "most likely to change," Ch. 21): the specific parameters — six understanding elements, seven historic metrics, four forces, six moats, four SF indicators, four price metrics, 18 biases + 2 akrasia. The project's §3 tunable-parameter design is therefore book-sanctioned: Marshall expects the bottom layer to be edited.

Core definitions worth preserving verbatim in spirit: value investing is "acting on the observation of a clear difference between price and worth." Risk is "the chance of losing money," never volatility. Margin of safety: "we don't wait for a stock to get a little inexpensive. We wait for it to get undeniably inexpensive." Capital preservation comes first because the mathematics of realised losses is punitive (−50% needs +100%).

## 2. Understanding (Ch. 5)

One unambiguous sentence in plain language, built from six parameters: **products** (goods/services; commodity↔differentiated spectrum; hunt for hidden products — Vivint's tax credits), **customers** (who *pays*, not who uses; as specific as the filings allow), **industry** (incl. non-obvious ones — Avon is also multilevel marketing), **form** (legal *and* operational — REIT status explains Equity Residential's payout; franchisor/franchisee; vertical integration), **geography** (customers, operations, HQ — emphasise whichever is most enlightening; exposes tax/moral issues), **status** (prominence, age, transformation, size — size cuts both ways).

Four traps: product familiarity, marketing messages, mission statements, aspirations ("what the business is about and not what it could be"). Multi-unit companies: define six parameters for the dominant unit, or for each unit if equally weighted. Circle of competence evolves; a stretch is an invitation to learn, genuine incomprehension (or deliberate obfuscation) is a hard stop — the danger of investing in what you don't understand "isn't so much that we'll lose money. It's that we'll make money" and mislearn from it.

## 3. The key numbers (Ch. 6–10) — reasoning behind each

**Capital employed** = total assets − excess cash − non-interest-bearing current liabilities (possibly − goodwill). The philosophy is subtractive conservatism: *"all assets in the business need to be in the business unless proven otherwise... Only those items that certainly aren't required get subtracted."* Hence in the Gap case Marshall subtracts accounts payable, accrued compensation, and income taxes payable — but leaves gift-card deferred revenue, deferred rent, and "other" in CE, because "the burden of proof rests with the item to warrant subtraction." Excess cash is unknowable, so compute two CE versions (all cash out / no cash out) rather than a fake percent-of-revenue rule. Goodwill: the more recurring the acquisitions, the less deducting makes sense — "I often leave it in."

**Operating leases** are debt in disguise (the bicycle-lease parable): capitalise when accounting sees operating but the investor smells finance. Six-step mechanics; liability = PV of scheduled lease payments discounted at the company's own recent cost of debt (from the 10-K; precision here is "precision masquerading as accuracy" — great buys shine through assumption ranges). *Adjustments shaping one number must shape the others*: OI gets + old lease expense − imputed depreciation (where depreciation = lease expense − imputed interest); FCF gets + lease payments − imputed interest. Post-ASC 842/IFRS 16 balance sheets do this natively, so the procedure now matters only for pre-adoption years in the history window.

**Operating income** is the primary income measure because it strips capital structure and tax regime — enabling comparison of the same firm through time and different firms at a point in time. Marshall's stipple-drawing metaphor: the core operation is the art; tax and capital structure are a replaceable frame.

**Free cash flow** = CFO − *maintenance* capex ideally. Depreciation is rejected as a maintenance proxy (inflation makes it a fraction of replacement cost; replacement equipment differs in kind). Hunt for a disclosed maintenance figure in the 10-K or Q&A of earnings calls; failing both, subtract all capex, "knowing that I'm painting an overly dark picture... I prefer to assume the worst with the prospect of delight." Levered FCF (interest and tax in) is the preferred variant because it pairs with OI as the opposite lens — cash-basis, post-interest-and-tax vs. accrual, pre-both. **IFRS trap:** filers that book interest paid in financing must have it moved into CFO before deriving levered FCF.

**Book value** = shareholders' equity *excluding* noncontrolling interests (the smaller number). **TBV** flags acquisition overpayers: when BV ≫ TBV from a recent deal, analyse the target's last standalone filings — *"Would I have paid that price? If not, I stop my analysis. I don't care what the purported synergies were."* **Shares**: fully diluted, weighted average — "in a successful company, anything that can become a share will become a share."

## 4. Past performance (Ch. 11)

Seven metrics: ROCE, FCFROCE, ΔOI/FDS, ΔFCF/FDS, ΔBV/FDS, ΔTBV/FDS, L/E. Only ~a dozen inputs per year are needed.

**Denominators as ranges.** CE is measured four ways (beginning/end of period × with/without cash) → four ROCE and four FCFROCE readings, and — decisively — Marshall tests the *worst* against the benchmark ("the worst average ROCE figure is 18 percent. That's still well above my benchmark of 15 percent. So I'm still interested"). Worst-of-four is the operative test.

**Normalisation** = multiyear averages only (ΣOI ÷ ΣCE across the window; geometric mean for growth rates). Never tweak individual years, for three stated reasons: only the future reveals what was truly one-off; spotting real irregularities requires management-level knowledge outsiders don't have; every year has irregularities, so tweaking never ends. "I prefer to regard historic operating performance as just that: historic." L/E is never normalised — only the most recent reading matters — and the numerator may be fluffed with capitalised-lease PV.

**Benchmarks and their derivation:** ROCE ≥ **15%** (his estimate of the S&P 500's ~10.2% long-run total return grossed up as if constituents paid no interest or tax — the delisted-company thought experiment). FCFROCE ≥ **8%** (market return haircut for the normal cash cycle — FCF is structurally held to a lower standard than OI). Per-share growth ≥ **~3%** nominal (US inflation; below it the business shrinks in real terms; "higher benchmarks are appropriate" but unspecified). L/E ≤ **2** as a rule; up to **7** only when all other metrics are great and a creditworthy company is using cheap borrowed money to repurchase clearly under-priced stock (or equity has shrunk through distributions). ΔBV/ΔTBV are of limited standalone use (dividends and buybacks distort them) but still worth computing — recognising a metric as unhelpful in a case is itself information (Gap). And the discipline: "Avoid making excuses for unremarkable companies... If a business looks bad, consider it no further."

## 5. Future performance (Ch. 12)

**Breadth analysis** — two questions; the business isn't good unless both answers are yes. Broad customer base: *no single customer over a tenth of revenue* (the annual-report disclosure sentence is the test; its absence "suggests the absence of this happy condition"). Broad supplier base: *no single supplier over a tenth of COGS or operating expenses* — with one exception: deliberate concentration for bulk terms is fine **if several potential vendors stand ready to serve** (alternatives keep the favourite honest). Look through nominal counts to the effective supplier (Delta Financial's real supplier was the RMBS market itself — its seizure bankrupted the company); "sources from over 100 suppliers" proves nothing.

**Forces analysis** — Marshall's four-force company-level rendition of Porter (rivalry is dropped; its substance lives inside direct substitutes). Each force is called **strong or weak, binary — "Medium isn't useful. After all, they're all kind of medium."** Reducers of customer power: many customers; improbable backward integration; high switching costs (West Marine vs. IFF). Reducers of supplier power: many suppliers; improbable forward integration; low switching costs (Kraft Heinz). Substitutes take three forms: direct, doing-without, wholly-different-function (Axis cameras); kept low by lower substitute value or high adoption switching costs. New entrants = barriers to entry **plus barriers to success**; any one of scale, switching costs, or hard-to-get permits can dull the threat.

**Decision rule:** all four weak → warranted; **two or more strong → stop** (GameStop: strong supplier power + strong substitutes → "I considered it no further"); exactly one strong → the judgment zone (Kone had exactly one strong force on each side — substitutes in goods, local new entrants in services — and "continues to look good"). "When in doubt, quit." Multi-unit businesses get segment-level force calls (Kone goods vs. services).

**Moat identification** — a moat is a barrier that *lasts*, from a **single identified source** among six: government (Weyerhaeuser licences), network (Facebook), cost (POSCO's gifted deep-water land), brand (Maggi — verified by unaided-recall questions in the target market), switching costs (Oracle), ingrainedness (Geberit — brand for the channel; verified by open-ended questions to channel participants). Moats are rare; most businesses have none.

**Market growth** — a basic directional sense suffices; exact rates are neither required nor useful; the tool doubles as a checkpoint against the "glow" an idea develops late in the pipeline. Overlap among the four tools is deliberate redundancy.

**Quantitative forecasting is rejected**: dummied-up future financials are guesswork cloaked in mathematics and mistake precision for accuracy.

## 6. Shareholder-friendliness (Ch. 13)

Qualitative, four indicators, **defined by the worst — one dicey indicator is enough**; the operative question is "Do I want to be in business with these people?" And the burden sits with the company: *"It's not for the investor to find a reason to consider a factor bad. It's for the company to prove that a factor is good"* (the Swatch verdict).

1. **Compensation & ownership.** The test is the fattest number for the highest-paid employee: strike at **> $30,000,000 or > 5% of the lower of free cash flow and net income** — revenue is irrelevant. Highest-paid *outside* director: norm ≈ **$250,000; stop above twice that**. Both figures are "very American... absurdly high in most other countries" (Norway < $100k) — scale to local context. Why care when comp is an EPS rounding error? Because comp is a window into top-level decision-making: boards that tolerate outsized pay tolerate overpriced acquisitions, and "paying too much for acquisitions can kill companies." Outright open-market insider ownership is the positive (ignore investment funds); option exercises are neutral; sales inconclusive unless several insiders dump most of their shares at once; option plans as "alignment" are laughable.
2. **Related-party transactions.** Number, size, and opacity are inversely correlated with SF. Search the proxy for *related/relationships*; expect leasing, consulting, hiring. Blunt fairness test: insider entity's share of the relevant expense line (H&M's chairman got 2% of total rent — tolerable). Subsidiary transactions don't count. Dynasties are questionable, not disqualifying — bad nepotism surfaces in ROCE or comp.
3. **Buybacks.** Positive **only at a discount to worth**; at other prices they *are* overpriced acquisitions. EPS-linked bonuses and option plans create the perverse incentive; accounting can't flag the overpayment and buybacks mechanically turbocharge ROCE. The option-sterilisation rationale is "one of the worst rationales in the history of finance. Using company cash to transfer shares from outsiders to insiders has a name. Theft."
4. **Dividends.** Most shareholder-friendly from **fully priced companies in mature industries with long strong-FCF histories**; a dividend can signal exhausted reinvestment opportunities; weigh against local custom and law (Germany: only profitable firms may pay). Dividends are a capital-allocation choice, not a yield statistic.

Not every indicator needs equal depth in every case — "look at those factors that jump out" — but all four get assessed.

## 7. Inexpensiveness (Ch. 14) — the part that changes the project most

Four price metrics, but **not of equal rank**. *"I prefer both MCAP/BV and MCAP/TBV to be no higher than 3. But these are just qualifiers for me. They're not what I look for. What I look for is MCAP/FCF and EV/OI."*

- **MCap/FCF ≤ 8** (levered FCF; consistent numerator/denominator — equity price over equity cash) and **EV/OI ≤ 7** (the "particularly sage" metric — financing-blind, prices everything) are the primary tests. Their pairing is deliberate: accrual-pre-interest-and-tax vs. cash-post-both — "using both makes it harder to get bamboozled." Multiples are shorthand for a DCF; a low multiple = a high implied discount rate on the income stream.
- **MCap/BV ≤ 3 and MCap/TBV ≤ 3** are qualifiers — "dead company" metrics. Their diagnostic value is in the *gap*: BV reasonable but TBV stratospheric → goodwill is enormous → audit the acquisition history; both high and similar → hunt for understated tangible assets (old land). Both are distorted identically by buybacks and dividends. Marshall's own worst error (Preface) was selling Nike because P/B crossed 3 while the swoosh sat on the books at zero — a standing warning against letting book-value metrics drive decisions on asset-light franchises.
- **EV in two versions** (all cash excess / none): *"Don't buy before both versions put the company squarely in the bargain bin."*
- **The limit price** — the direct ancestor of the register's trigger band: *"What would the stock price have to sink to such that MCAP/FCF is no more than 8 and EV/OI is no more than 7? That becomes our limit price. We wait for it."* In the Flowserve case the $17 limit is computed on the two flow metrics alone, with MCap/TBV at 23 treated as an investigation trigger (acquisition audit), not a band input.
- **Benchmark flexibility**: metrics fall into return / growth / price categories, and "strength in two... can compensate for averageness in the third" — a higher EV/OI is acceptable when ROCE and growth are high. No formula (metrics are historic; category weights depend on holding period), just "slight, constructive benchmark bending."
- **Backvaluing** for definitively cyclical industries only: today's MCap and EV against the prior cycle's FCF/OI. "A tourniquet" — assumes history repeats, the business is unchanged, and the cycle isn't secular decline.
- Valuation comes **last** so ignorance of price keeps the earlier gates objective, and because understanding + quality findings are durable — "they can be called into service whenever a stock price takes a sharp turn" (the Kone/Toshiba episode). When a good company isn't cheap: wait, for years if necessary — action ≠ progress, and cash has option value.

## 8. Psychology (Ch. 16), portfolio (Ch. 17), ideas (Ch. 19)

**18 cognitive biases** (affinity, reciprocity, anchoring, authority, availability, cleverness, incomprehensibility, consensus, peculiarity, intermixing, consistency, confirmation, hope, lossophobia, scarcity, hotness, miscontrast, windfallapathy) **+ 2 akrasia** (impetuosity, weakness). A bias only invalidates a judgment *born of* it. Marshall's operational rule: before any buy or sell order, tick through the list of 20 — brief, but "just enough introspection." Modern frictionless trading removed natural circuit breakers, so reflection must be baked into the process.

**Portfolio**: 10% of the portfolio or nothing (conviction test; also caps single-name exposure); expect the price to drop right after buying. **Four valid sell reasons**: price flies past value (EV/OI > 25 absent mitigants); the company turns out not to be good (analysis wrong or context changed — fight the consistency bias); buyout; a clearly better opportunity (treat with extreme suspicion — the hope bias's prime hunting ground; Marshall has never actually done it). Invalid: rebalancing (anchoring in disguise), memorialising success, agent compensation. Selling's structural costs: taxes (annual churn halves 30-year outcomes) and the scarcity of replacements. Concentration outperforms because index-resembling portfolios index-perform; sequestered multi-year expense cash (outside the portfolio, insured, home currency) is what makes concentration psychologically survivable.

**Idea sources**: bad news, spin-offs, regulatory filings (13Fs, with seven listed limitations), reorganisations, small caps, screeners (his least favourite — valuation-first is backwards), serendipity. Then **forget the provenance** — it keeps "a whole raft of cognitive biases at bay."

**Ethics (Ch. 18)**: pick a moral posture early (amorality / failure abstention / success affirmation / failure activism) purely so principles never force an uneconomic sale later.

---

## 9. Deviation register — v1 instructions vs. the book, and the v2 resolution

| # | Topic | Book | v1 instructions | v2 resolution |
|---|-------|------|-----------------|---------------|
| D1 | MCap/BV threshold | ≤ 3 | < 5 | **≤ 3** (P10 corrected) |
| D2 | Rank of price metrics | FCF & EV/OI primary; BV/TBV qualifiers; limit price from the two flow metrics | Four co-equal tests; TBV/BV frequently the binding band metric | **Primaries vs. qualifiers codified; trigger band = joint P7∧P8 limit price; qualifier breaches trigger named investigations, not mechanical blocks.** Bands previously bound by TBV/BV must be recomputed |
| D3 | Cheapness allowance | Unquantified "slight, constructive benchmark bending" when return+growth are strong | One metric ≤ 1.25× threshold, unconditional | **P12 retained but restricted: one *primary* metric, only when Past = STRONG** |
| D4 | Forces | Four forces, binary strong/weak; 0 strong proceed, ≥2 stop, 1 = judgment | Five forces, LOW/MED/HIGH, FAVOURABLE/MIXED/UNFAVOURABLE tilt | **Four forces, binary, with the 0/1/≥2 rule mapped to STRONG/ADEQUATE/WEAK eligibility** |
| D5 | Breadth | Hard 10% definitions; both sides must pass; supplier ready-alternatives exception only | Qualitative "broad and unlikely to consolidate" | **10% thresholds codified (P15).** Customer-concentration FAIL is now explicit for ASML/TSM/QCOM-type names — see D6 |
| D6 | Moat-decides rule | No such override; breadth is a gate ("the business isn't good unless both are yes") | Dominant stable moat floors Future at ADEQUATE regardless of forces | **Retired in its old form.** A dominant moat is now *evidence for weak force calls* (the book's own reducers). Sole surviving override: a narrow, logged **captive-customer breadth waiver** [PROJECT] for structurally concentrated customer bases that cannot integrate or switch; Future capped at ADEQUATE. Marshall would likely not waive — delete the clause to go book-pure (flips ASML/TSM/QCOM to AVOID) |
| D7 | ROCE denominators | Four measures (beg/end × cash), **worst-of-four** tested vs. benchmark | Beginning-of-period only, both cash variants | **B2 keeps the beginning YoY series; a normalized-average summary row now computes all four ways and the rubric tests the worst** |
| D8 | Normalisation | Multiyear averages; never tweak one-offs | OI used partly to "neutralize" impairments etc. | **As-reported OI, no add-backs; one-offs commented in prose, diluted only by averaging.** (Tax charges below OI were always fine to ignore — OI never saw them) |
| D9 | Maintenance capex | Disclosed breakout > all-capex fallback; depreciation proxy banned | FCF always = CFO − total capex; separate "MCap/FCF suspension" rule invented for capex super-cycles | **Disclosed maintenance capex used when available (labelled); else all capex with the "overly dark" caveat and EV/OI anchoring the band — the suspension rule re-grounded in the book's own logic** |
| D10 | IFRS interest classification | Move interest paid from financing into CFO before deriving levered FCF | Silent | **Codified** — affects SIE, ABB, ADYEN, NVO, SDZ, KSPI, BABA series marginally |
| D11 | NIBCL scope | Burden of proof on the item; Gap's gift-card float and deferred rent stayed in CE | Subtract all non-debt current liabilities incl. deferred revenue | **Default list = AP + accrued expenses + taxes payable + deferred income, with the burden-of-proof scrutiny option logged when material** |
| D12 | Comp test | $30M / 5% of lower(FCF, NI); director $250k, stop > 2×; context-scaled | "Proportionate to operating income," unquantified | **P17 quantified, context-scaled** |
| D13 | Overpriced-acquisition stop | BV≫TBV → analyse the target pre-deal; overpayment → stop | Absent | **Codified as a capital-allocation strike under SF test 4** |
| D14 | Psychology layer | 20-item tick-through before orders | Absent | **Bias check before verdict finalisation; live biases logged in Appendix C** |
| D15 | Leases pre-2019 | Full capitalisation procedure | IFRS 16/ASC 842 liabilities treated as debt (post-adoption only) | **Pre-adoption years capitalised when commitments > 10% of total assets (P18), full three-statement consistency** |
| D16 | ΔBV/FDS | One of the seven metrics | Not computed | **Added to B3** |
| D17 | Growth benchmark | ≥ ~3% nominal (inflation floor) | "Up over the decade" | **3% floor codified in P2** |
| D18 | Thin history (spin-offs) | Proceed with what exists | Open MODEL question (SDZ) | **Resolved: STRONG unavailable below the P1 window; ADEQUATE/WEAK judged on the available record, flagged** |
| D19 | Captive finance (SFS) | "Adjustments shaping one must shape the other" | Open MODEL question (SIE) | **Resolved: numerator/denominator consistency — group OI including the finance segment's operating result, with its assets in CE (or exclude both symmetrically; include-both is the default)** |
| D20 | Securities-heavy holdcos | BV metrics are the "dead-company" lens — for such firms the balance sheet *is* the business | BRK.B P/B ~1.2× ad-hoc substitution | **Codified standing rule: where OI/FCF screens are structurally inapplicable, MCap/BV anchors cheapness and the trigger band; logged per name** |

## 10. Names to queue for REVIEW under v2 (from session memory — register file is currently empty)

- **ASML, TSM, QCOM** — customer breadth now an explicit FAIL absent the captive-customer waiver. With the waiver: WATCH stands, Future capped ADEQUATE. Waiver struck: AVOID. Decision required.
- **All WATCH rows** — trigger bands re-anchor to the joint MCap/FCF ≤ 8 ∧ EV/OI ≤ 7 limit price. Bands where MCap/TBV or MCap/BV was binding (ASML ≈ €140, PYPL ≈ $38, ABB ≈ $10–12; QCOM/BKNG TBV bands already flagged as distorted) shift; the P12 restriction and P10 5→3 also move edges. Recompute at next REVIEW/SWEEP touch — no mass re-memo.
- **AMZN, META, TSMC, BABA** — FCF-suspension logic restated as the maintenance-capex rule; hunt for disclosed maintenance figures first; verdicts unlikely to move.
- **CROX** — re-test Past on strictly as-reported OI (D8) at next REVIEW; multiyear averaging should absorb the impairment year.
- **IFRS names (SIE, ABB, ADYEN, NVO, SDZ, KSPI, BABA)** — levered-FCF interest reclass (D10) may shave FCF series; check at next REVIEW.
- **SIE** — SFS question resolved by D19; restate Past on the consistent basis at next REVIEW.
- **TROW** — re-derives as one-strong-force ADEQUATE without any special rule; verdict unchanged.
- **BRK.B** — D20 codifies the existing treatment; unchanged.
- **AVOID rows** (PYPL, CRM, HFG, BTI, KER, TSLA) — unchanged; rules only tightened.

*Framework output, not investment advice.*
