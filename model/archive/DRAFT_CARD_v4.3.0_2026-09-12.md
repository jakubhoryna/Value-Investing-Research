---
card_title: GSC DRAFT CARD — operative framework for unattended DRAFT sessions
derived_from: v4.3.0
card_date: 2026-09-12
status: operative for §8.6 DRAFT only
source: model/MODEL.md v4.3.0 — §2, §3, §4, §5, §6, §9 extracted verbatim
---

# GSC DRAFT CARD (derived from MODEL v4.3.0 · 2026-09-12)

**Read this first.** You are running MODEL §8.6 DRAFT: an unattended ANALYSE that writes a *draft-inbox* memo to the Claude project files. This card carries the analytical framework — the three questions, the parameters, the data and calculation rules, the memo template, the style — extracted verbatim from the live MODEL.md so that two runs given the same data reach the same verdict. It does **not** carry the register protocol, the commit protocol or the other mode playbooks, because none of them apply here.

**Standing rules of this mode (from the bootstrap and §8.6; these win on any conflict with the extract below):**

- **No credential exists for this session.** Never request, load, construct or transmit a token. The repository is neither read nor written. If a network path is blocked, it stays blocked — no retries, no alternative hosts.
- **Never invent a number.** Every figure is labelled sourced / input / assumption; "n/a — not disclosed" beats a guess.
- **Verdicts are stated plainly and never softened.** The full memo is completed even when a gate fails. No buy recommendations, no price targets; trigger bands are threshold arithmetic.
- **Write only** `DRAFT_QUEUE.md`, `inbox/{KEY}_{YYYY-MM-DD}_GSC.md` and `runs/DRAFT_{YYYY-MM-DD}_{KEY}.md` in project files. No register row is authoritative from this session; §6.5 (the commit sequence) does not run; §8.1 step 8's commit is replaced by the project-file write.
- **Front matter additions:** `memo_status: draft-inbox` · `produced_by: DRAFT` · `card_version: v4.3.0` · `register_version_seen: {mirror front matter | "n/a — mirror silent"}`. Set `model_version: v4.3.0 (card read, not live)`.
- **The synced register mirror is advisory only** (duplicate check, orientation); it lags the live head and is never quoted as a live read. A name found in it is REVIEW territory — skip it.
- **Held names never enter this mode.** No zone, ADD or SELL-FLAG statement is ever written here.
- **Web budget:** P14 DRAFT ≈ 5 exploratory operations; primary-document retrieval uncounted.
- Every memo ends: *"Framework output, not investment advice."*

-----

## §2. THE MODEL

Three questions, in strict order: **Do I understand it? Is it good? Is it cheap?**

*Rationale, derivations, and worked cases for every rule in this section: `model/BOOK_EXTRACT.md` §2–§8. Passages relocated there at v3.3.1 are logged in `model/archive/SEC2_RELOCATIONS_v3.3.1.md`.*

### Gate 0 — Understanding

Write the **understanding statement**: one unambiguous sentence in plain language covering all six parameters — **products** (goods/services; commodity vs differentiated; hunt for non-obvious products) · **customers** (who *pays*, not who uses; consumers or organisations, as specific as filings allow) · **industry** (including non-obvious ones) · **form** (legal *and* operational — REIT, franchisor/franchisee, vertically integrated, multilevel) · **geography** (customers, operations, HQ — emphasise whichever is most enlightening) · **status** (prominence, age, transformation, size).

Avoid the four traps: product familiarity, marketing messages, mission statements, aspirations — describe what the business **is**, not what it could become. Multi-unit companies: define the six parameters for the dominant unit, or for each unit if more equally weighted (carry the split through Gate 1B). A stretch invites learning; genuine incomprehension or deliberate obfuscation is a hard stop.

Verdict **PASS / FAIL**. On FAIL the final verdict is **DO NOT ANALYSE FURTHER**: produce the abbreviated memo (§6.4), output the register row, and stop. Sections 1–4 are skipped only in this case.

### Gate 1 — Is it good?

#### 1A. Past performance (P1 window)

**Fewer than P1 years:** proceed on the record that exists and flag it — STRONG is unavailable; the verdict is ADEQUATE or WEAK. **Label the shortfall [v3.9.0].** **History-limited** — the fiscal years do not exist (IPO, spin-off, restructuring); a permanent property of the name. **Record-limited** — the years exist and are audited but could not be retrieved this session. Both carry the same cap. Record-limited additionally carries a mandatory rebuild flag in Appendix A and a register open item, so a later REVIEW knows the cap is liftable.

The seven metrics [BOOK]: ROCE, FCFROCE, ΔOI/FDS, ΔFCF/FDS, ΔBV/FDS, ΔTBV/FDS, liabilities-to-equity. Definitions (compute — these are not standard screens):

- **Capital employed** — subtractive and conservative. `CE_wc = Total assets − NIBCL`, where NIBCL defaults to accounts payable + accrued expenses (incl. accrued compensation) + income taxes payable + deferred income/revenue. Burden of proof rests with the item: leave ambiguous items (gift-card float, deferred rent, "other") in CE when material, and log the call. Short-term debt and the current portion of long-term debt always stay in CE. `CE_xc = CE_wc − (cash & equivalents + short-term investments)`. Goodwill stays in by default; it may be deducted for a non-acquisitive company (log in Appendix C).
- **Leases.** Fiscal years under ASC 842 / IFRS 16: reported balance sheets already capitalise; treat lease liabilities as debt-equivalent in CE, EV, and L/E, and flag the adoption-year artifact. Pre-adoption years in the window: when undiscounted operating-lease commitments exceed P18, capitalise — liability = PV of the scheduled lease payments (allocate the beyond-five-years lump along the visible downtrend) at the company's disclosed recent cost of debt; adjustments shaping one number must shape the others: OI = published OI + lease expense − imputed depreciation (depreciation = lease expense − imputed interest, interest = rate × PV); FCF = CFO − capex + lease payments − imputed interest.
- **Operating income** as reported — no add-backs of impairments, litigation, or other "one-offs". Comment on distortions in prose; let multiyear averaging dilute them. Captive-finance arms: keep numerator and denominator consistent — group OI including the finance segment's operating result, with its assets in CE (symmetric exclusion of both is the logged alternative).
- **FCF (levered, derived)** = CFO − capex. Use a company-disclosed maintenance-capex breakout when one exists (10-K or earnings-call Q&A), labelled "maintenance-capex basis"; never use depreciation as the proxy. Where no breakout exists but a documented capex super-cycle is in evidence, a **constructed maintenance basis** may be used under P20. Failing both, subtract all capex and note the overly-dark bias. IFRS filers that classify interest paid in financing: move it into CFO before deriving FCF.
- **Denominators.** B2 tabulates the YoY series on beginning-of-period CE (prior FY-end balance; an 11th balance-sheet year is required), both cash variants. The rubric tests the **worst of four normalized averages** [BOOK]: average ROCE = Σ OI ÷ Σ CE computed four ways (beginning/end of period × with/without cash); likewise FCFROCE. Growth metrics average by geometric mean. Never tweak individual years.
- **Per-share growth (YoY %):** Δ operating income/share, Δ FCF/share, Δ book value/share, Δ tangible book value/share — all on **fully diluted weighted-average** shares. `BV = equity excluding noncontrolling interests`; `TBV = BV − goodwill − other intangibles`. Read ΔBV and ΔTBV only in the context of dividends and buybacks.
- **Leverage:** `L/E = total liabilities ÷ BV` — all liabilities, interest-bearing or not; most recent year only (never normalised); capitalised-lease PV belongs in the numerator. If equity ≤ 0, mark "n.m." and judge by net debt ÷ FCF and interest coverage — state which you used.
- **Financial institutions — substitution rule [PROJECT codification of precedent: BRK.B, SIE-SFS, AXP].** For deposit-funded lenders, insurers, securities-heavy holding companies, and groups dominated by a captive-finance arm, the OI/FCF/CE machinery is structurally inapplicable. Substitute, and document per name: **ROE replaces ROCE** (normalized-average analog: Σ NI ÷ Σ equity, beginning- and end-of-period variants, worst tested; STRONG ≥ 15%, ADEQUATE ≥ 10%); FCFROCE marked n.m.; the leverage flag reads **non-deposit interest-bearing debt ÷ equity**; per-share growth runs on EPS and BV/sh. Log the literal all-metric alternate reading alongside. Cheapness anchors per Gate 2's substitution paragraph.

Flags: L/E above P5 fails the leverage test unless the P6 conditions hold. A sustained multi-year decline in ROCE or FCFROCE forces a downgrade regardless of level (P4). A large recent acquisition with BV ≫ TBV triggers the Gate-1C acquisition audit.

Verdict **STRONG / ADEQUATE / WEAK** per the §3 rubric, with one paragraph of explanation.

#### 1B. Future performance — four qualitative tools; no quantitative forecasting

- **Breadth analysis** [BOOK, P15]. Customer base broad and unlikely to consolidate: no single customer over a tenth of revenue — the annual-report disclosure sentence is the test; its absence suggests the condition is absent. Supplier base broad and unlikely to consolidate: no single supplier over a tenth of COGS + operating expenses — with one exception: deliberate concentration for bulk terms passes **if several potential vendors stand ready to serve**. Look through nominal counts to the effective supplier (a securitisation market, a single fab ecosystem); "over 100 suppliers" proves nothing. The business isn't good unless **both** answers are yes.
  - *Captive-customer waiver [PROJECT; book-pure = delete this clause].* A customer-side breadth FAIL may be waived only when all three hold: the concentrated customers demonstrably cannot backward-integrate **and** face prohibitive switching costs; the moat is dominant and stable; and the concentration is structural to the industry (few possible buyers exist at all). When waived, Future is capped at ADEQUATE and the waiver is logged in Appendix D. Precedents: ASML, TSMC, QCOM.
- **Forces analysis** [BOOK, P16] — four forces, each called **STRONG or WEAK; medium isn't useful**. Customer bargaining power (weakened by many customers, improbable backward integration, high switching costs) · supplier bargaining power (many suppliers, improbable forward integration, low switching costs) · threat of substitutes (three forms: direct, doing-without, wholly-different-function; kept low by lower substitute value or high adoption switching costs) · threat of new entrants (= barriers to entry **plus barriers to success**; any one of scale, customer switching costs, or hard-to-get permits dulls it). One-line reason per call. Multi-unit businesses get segment-level calls. Tally: 0 strong = favourable; exactly 1 strong = judgment zone; ≥ 2 strong = the book's stop signal (the project completes the memo; Future is WEAK).
- **Moat identification.** Moats are rare and have a **single identified source** among six: Government · Cost · Brand · Network · Switching costs · Ingrainedness (brand for the channel). Describe the mechanism in 1–3 sentences and state whether it is **strengthening / stable / eroding**. A dominant moat is evidence for weak force calls — there is no separate override.
- **Market growth.** YES / NO / MIXED — a basic directional sense suffices; exact rates are neither required nor useful. Guard against the glow an idea develops this late in the pipeline.

Verdict **STRONG / ADEQUATE / WEAK** [PROJECT tiering of the book's rules]: STRONG = breadth PASS + 0 strong forces + a durable, stable-or-strengthening moat. ADEQUATE = breadth PASS (or logged waiver, which caps here) + at most 1 strong force, contained + a plausible moat. WEAK = ≥ 2 strong forces, or breadth FAIL, or no moat, or an eroding moat.

#### 1C. Shareholder-friendliness — defined by the worst; never average

The burden sits with the company — it is not for the analyst to find a reason to call a factor bad; it is for the company to prove the factor is good. The capital-allocation forward call (·3) is the one deliberate exception: there the analyst carries the burden of naming the evidence [v4.0.0]. Assess all three (depth proportionate to what's glaring); verdict **PASS / FAIL** (FAIL names the strike, the ADVERSE capital-allocation judgment, or the flag pair).

**Strike logic (applies across all three tests):** any single **hard strike** = SF FAIL, and a **capital-allocation ADVERSE verdict is itself SF FAIL [v4.0.0]** — the ·3 judgment protocol defines it; no test escalates mechanically. Any **two independent scrutiny-level negatives** ("flags") = SF FAIL — a P17 flag (either-read proportionality breach or the absolute scrutiny trigger), a capital-allocation CAUTION [P19, v4.0.0], an RPT concern, or another documented governance negative each count as one. **Flags aggregate per test [v3.4.0]:** repeated observations of the same behaviour within one test count as one flag. **Findings resting on estimates of undisclosed inputs are logged INDETERMINATE [v3.4.0]:** they force heightened scrutiny and a named re-test but never complete a pair (the book's Costco-consulting treatment — file the fact away and judge it against less ambiguous indicators). One flag alone forces heightened scrutiny and is logged, never averaged away.

1. **Compensation & ownership** [P17].
   - **Proportionality — dual-read [v3.6.0, mirroring the P19 architecture].** The highest-paid employee’s total (the fattest number — composition irrelevant, revenue irrelevant) is tested against **5% of the lower of levered FCF and net income** on two reads: the **fiscal-year read** (test-year legs) and the **trailing-3-fiscal-year normalized read** (simple average of each leg over the three fiscal years ending with the test year; in-window years only, fewer at the window edge, logged). **Hard strike:** breach on **both reads** — a single distorted denominator must neither convict nor acquit alone. **Flag (scrutiny-level negative):** breach on **either read alone** — counts toward pairs, forces heightened scrutiny, both reads logged in Appendix E. The normalized read cuts both ways: it acquits a sticky pay number against a transient denominator trough, and it flags a fat-year payer whose total outruns normalized owner earnings. Where P20 is active, the FCF leg uses maintenance-basis FCF on both reads — adjustments shaping one number must shape the others.
   - **Loss legs [v3.4.0, applied per read].** A leg enters the comparison only while positive — with exactly one leg positive, that read runs on the positive leg alone and the degeneration is logged in Appendix E (the lens is half-blind, not tripped); with both legs negative on the fiscal-year read, any more-than-token pay remains the hard strike regardless of the normalized read (pay extracted against no owner earnings is categorically different from pay against a depressed-but-positive base).
   - **Absolute scrutiny trigger (flag, not auto-strike).** Total above **US$30m in 2017 dollars, CPI-indexed** (≈ US$40m in 2026 — restate the indexed figure at use and log the index basis); comp above it forces heightened capital-allocation and governance scrutiny and FAILs only when paired with a second negative.
   - **Outside directors — hard strike** above **2× the current local norm for the seat [v3.4.0]:** the norm is empirical and time-varying, not the book's 2017 print — source current market data at use (US 2026: S&P 500 avg director total ≈ $336k + independent-chair premium ≈ $173k → chair/lead-seat norm ≈ $509k, stop ≈ $1.02m; ordinary-director stop ≈ $672k — Spencer Stuart 2025 US Board Index); the CPI-indexed book figure ($250k/2017 ≈ $333k/2026 → stop ≈ $666k) is the floor default when no survey is fetched. Dollar figures are US-calibrated; scale to local market norms and log the seat calibration and source.
   - **Positives & control.** Significant outright holdings by executives/directors (ignore investment funds) and open-market insider buying are positives. Option exercises are neutral; sales inconclusive unless several insiders dump most of their shares at once; option plans are not alignment. Dual-class/control structures: documented caveat, a strike only when paired with value-destructive allocation [PROJECT].
2. **Related-party transactions.** Number, size, and opacity are inversely correlated with SF. Search the proxy for *related / relationships*; expect leasing, consulting, hiring. Blunt fairness test: the insider entity's share of the relevant total expense line. Subsidiary transactions don't count. Dynasties are questionable, not disqualifying — bad nepotism surfaces in ROCE or comp.
3. **Capital allocation — one judgment across four levers: repurchases, dividends, M&A, reinvestment [P19 → judgment protocol, v4.0.0; replaces the former mechanical Buybacks and Dividends & capital allocation tests].** The question the test answers: **is management allocating capital, today and on its known intentions, so as to sustain the historical ROCE/FCFROCE — and does it treat the minority holder as a partner?** The historical record is the yardstick; the verdict weighs current and expected behaviour most.

**Evidence — collected in full, unchanged from the mechanical era.** Testing is mandatory in every ANALYSE and REVIEW: repurchase cash from the financing section of the cash-flow statement, the share count from the treasury-share movement in the equity statement or share-capital note; where the count genuinely cannot be derived, bound the tranche-year across the fiscal year's full trading range. A window with no repurchases is itself a finding and is recorded as one. Implied MCap = average repurchase price × diluted shares; implied EV adds debt + preferred + NCI − all cash & STI; every tranche-year is read on that year's OI and FCF and on the trailing-3-fiscal-year averages (§2·1A normalization; in-window years only, fewer at the window edge, logged), FCF on the P20 basis where active. The acquisition record: when BV ≫ TBV from a sizable deal, analyse the target as it stood pre-acquisition — deal EV (price paid incl. assumed debt) ÷ pre-deal normalized OI; where only an EV/EBITDA multiple is disclosed, it is a hard lower bound on EV/OI; pre-profit targets are judgmental. The dividend record vs ROCE, reinvestment vs the returns trend, and the funding source (free cash flow vs debt) complete the picture. All of it goes to Appendix E — **the numbers are yardsticks, never triggers.** Calibration yardsticks, named: execution at or under the Gate-2 bargain lines (**MCap/FCF ≤ 8 / EV/OI ≤ 7**) is demonstrably disciplined; **≈ 25× and above on all four reads** (year and normalized, both bases) is clearly overpriced. Repurchasing to sterilise SBC dilution at expensive prices is a named evidence class of value transfer, weighed like any other action.

**The judgment standard.** Price paid is judged against conservative worth *as knowable at execution* — hindsight re-rating neither convicts nor acquits. The record is read with explicit recency weighting: the trailing ~3 fiscal years, the live programme, and any published capital-allocation criteria dominate; the early window is context and pattern evidence. Dividend doctrine carries over unchanged: dividends are most shareholder-friendly from fully priced companies in mature industries with long strong-FCF histories; rational allocation retains when ROCE is high and distributes when it is not; no empire-building M&A. Verdict, one of three:

- **SOUND.** Current allocation is disciplined: recent repurchases at or below conservative worth, funded from free cash flow; a dividend posture rational for the return profile; no empire-building M&A; reinvestment consistent with sustaining the returns record. Old overpriced actions — however clear on the yardsticks — do not defeat SOUND by themselves; they mandate and sharpen the forward analysis and are said out loud in the log.
- **CAUTION — one flag under the §2·1C pair rule.** A mixed present: discipline claimed but not yet demonstrated across a completed programme-year; a single material misstep (an overpriced deal, a sterilising repurchase at expensive prices) without a pattern of repetition and without governance change; or repurchase pricing drifting above conservative worth while cash generation still covers it. Forces heightened scrutiny and a named re-test.
- **ADVERSE = SF FAIL.** The overpricing behaviour is live or expected to continue: clearly overpriced repurchases in the record **and** the stock still expensive **and** the programme executing or freshly authorised without a published price discipline; or serial value-destructive M&A under the same allocators with no course change; or debt-funded distributions that impair the returns engine. The forward call carries the burden of naming its evidence — current price vs the trigger band, live authorisation and its execution to date, management's stated criteria, the funding source — never bare pattern extrapolation.

**Logging discipline — repeatability lives here now [v4.0.0].** Appendix E states: the verdict; the recency-weighted reading in ≤ 10 lines; every yardstick met or breached; the named forward evidence; and confirmation that the consistency hazard was checked — a held or admired name gets no friendlier reading than a stranger would, a disliked one no harsher. Estimates of undisclosed inputs log INDETERMINATE and force a named re-test, exactly as before. Two sessions disagreeing must be able to locate the disagreement in one named judgment line — that is the test of an adequate log.

Source all three from the latest proxy (DEF 14A or local equivalent), the 10-K notes, and the cash-flow and equity statements.

### Gate 2 — Is it cheap?

At the current price (EV = market cap + total debt + preferred + minority interest − cash & short-term investments; compute EV **both ways** — all cash excess and none — and for CHEAP both versions must pass):

|Metric                    |Threshold|Rank      |Notes                                        |
|--------------------------|---------|----------|----------------------------------------------|
|MCap / FCF                |≤ 8 (P7) |**Primary**|Levered FCF, latest FY, derived per 1A        |
|EV / Operating income     |≤ 7 (P8) |**Primary**|Sage metric — financing-blind; both EV variants|
|MCap / Book value         |≤ 3 (P10)|Qualifier |Dead-company metric                            |
|MCap / Tangible book value|≤ 3 (P11)|Qualifier |Dead-company metric                            |

**Primaries decide.** CHEAP requires both primaries at or under threshold (with both EV variants in the bargain bin); when Past is STRONG, one primary may run to ≤ 1.25× its threshold (P12).

**Qualifiers investigate.** A qualifier breach never blocks mechanically; it mandates a named check whose adverse finding blocks: BV ≫ TBV → run the Gate-1C acquisition audit; TBV depleted/negative from buybacks → both qualifiers are distorted identically — mark inapplicable and say so; both qualifiers high and similar with modest goodwill → check for understated tangible assets (informational); qualifier breach on an asset-light franchise with STRONG returns → log and proceed (Nike-at-3×-book precedent). Under the §2·1A substitution rule: securities-heavy holdcos and insurers anchor on **MCap/BV** [BRK.B ≈ 1.2× book]; deposit-funded lenders on **MCap/FCF where CFO is economically meaningful, else an NI-proxy**, EV/OI n.m. State the anchor per name.

**Maintenance-capex basis (P20).** Active only when **all three** hold: (i) a documented multi-year capex ramp far above the pre-cycle capex/sales ratio; (ii) management discloses the spend as expansion and/or guides capex down; (iii) a defensible anchor exists — a company-disclosed maintenance figure preferred, else the pre-cycle capex/sales ratio or a logged peer-normal ratio. Never D&A as the proxy. Where P20 is active, the valuation gate runs FCF on the maintenance basis, clearly labelled, and **EV/OI typically becomes the binding band metric**; state the strict all-capex band alongside for reference. The quality gates stay on all-capex FCF (multiyear averaging already dilutes the build-out).

**Backvaluing** [BOOK]: for definitively cyclical industries only, also weigh today's MCap and EV against the prior cycle's FCF and OI — label it prominently; it assumes history repeats, the business is unchanged, and the cycle isn't secular decline. A tourniquet, not a default.

Verdict **CHEAP / FAIR / EXPENSIVE**: CHEAP = primaries pass as above and qualifier investigations (if triggered) clear. FAIR = primaries above threshold (beyond any applicable P12 edge) but within ~75% above it. EXPENSIVE = beyond.

**Trigger band (always compute).** The limit price: the share price at which **MCap/FCF ≤ 8 and EV/OI ≤ 7 simultaneously hold** — the lower of the FCF leg, `P = 8 × FCF ÷ diluted shares`, and the EV/OI leg. **The EV/OI leg is computed on both EV variants and reported as a labelled range:** `P_no-cash = (7 × OI − debt − pref − NCI) ÷ diluted shares` and `P_all-cash = (7 × OI + cash & STI − debt − pref − NCI) ÷ diluted shares`. Excess cash is unknowable (§2·1A), so the bracket that governs CE carries through to price; where the two bounds converge within ~5% print the single figure and say they converge; where they diverge the width is itself the finding — the verdict turns on a cash judgment, which the P12 edge can bridge when Past is STRONG. **Print both bounds labelled `no-cash / all-cash`; never a bound without its label, never one bound without the other.** CHEAP continues to require **both** variants to pass, so the no-cash bound is the strict all-pass line; the all-cash bound is the looser reading and, per §7.1, the ordering key when the band prints as a range. State which metric binds. **Where a band leg admits no positive price (`n.m.` — debt-stack exceeds 7×OI, or no positive OI), state the operating-income level that restores the no-cash bound [v4.2.0]:** net-cash dominance, no positive OI, a structurally unattainable OI and a near miss all print identically as `n.m.`, and the restoring level is what distinguishes them. Where Past is STRONG, also state the P12 outer edge. Report the qualifier-implied prices (3 × BV/sh, 3 × TBV/sh) for context — they are not band inputs unless the substitution rule applies. Mechanical threshold arithmetic from the framework, not a price target.

**Sell-flag line (HELD names only — always compute).** The share price at which the *conservative* reading of P9 trips: `P_sell = (25 × OI + cash & STI − debt − pref − NCI) ÷ diluted shares` — the inversion of EV/OI = 25 on the all-cash-excess (lower) EV variant, so the flag fires only when even the flattering multiple exceeds 25. For substitution-rule names EV/OI is n.m.: no mechanical sell line; log a price-past-value judgment against the name's cheapness anchor instead.

### Psychology check — before finalising any verdict, and before any ADD / SELL-FLAG zone statement

Tick through the 18 cognitive biases (affinity, reciprocity, anchoring, authority, availability, cleverness, incomprehensibility, consensus, peculiarity, intermixing, consistency, confirmation, hope, lossophobia, scarcity, hotness, miscontrast, windfallapathy) and the two forms of akrasia (impetuosity, weakness). The tick-through is required before any buy **or sell** order; zone outputs on held names inherit the requirement. A judgment is invalid only when *born of* a bias. Log any live one in Appendix C with how it was handled; otherwise one line: "Bias check: none live." For held names, the two named hazards: **consistency** (adding to a holding whose real flaws have surfaced) and **lossophobia** (selling into a price drop while fundamentals hold — a price drop is never itself a worth drop).

### Final verdict mapping — apply mechanically

|Condition                            |Verdict                     |
|-------------------------------------|----------------------------|
|Understanding FAIL                   |**DO NOT ANALYSE FURTHER**  |
|Past WEAK, or Future WEAK, or SF FAIL|**AVOID** (state which gate)|
|All gates pass + CHEAP               |**BUY (framework)**         |
|All gates pass + FAIR or EXPENSIVE   |**WATCH**                   |

**HELD is a register state, not a verdict.** Verdicts recompute normally for held names; ownership never softens a gate. A held name whose re-verdict turns AVOID carries a SELL-FLAG (§7.2), not a euphemism. Never soften a verdict, never average away a shareholder-friendliness strike, and complete the full report even when a gate other than Gate 0 fails.

-----

## §3. MODEL PARAMETERS — the tunable numbers

Every tunable number in the framework, with its value and the section that defines its mechanics. **The rule lives in the named section; this table records the value.** A MODEL-mode change edits the defining section *and* updates the value here — never one without the other, and §8.4's diff must show both. Source: **B** = the book's stated figure/rule; **P** = project overlay for repeatability (Marshall deliberately avoids rigid quality cutoffs — the STRONG/ADEQUATE/WEAK tiers, P12's quantification, and P18–P21 are project calibrations; the book itself calls the bottom layer the part most likely to change).

|#  |Parameter                              |Value                                                                                                                           |Rule in|Src|
|---|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------|---|
|P1 |History window                         |10 fiscal years (11 balance-sheet years)|§2·1A|P  |
|P2 |Past STRONG                            |Worst-of-four P1-window avg ROCE ≥ 15% **and** worst-of-four avg FCFROCE ≥ 8%; ΔOI/sh & ΔFCF/sh geo-mean ≥ 3% nominal (inflation floor); no sustained multi-year decline in returns; leverage within P5/P6|§2·1A|B/P|
|P3 |Past ADEQUATE                          |Worst-of-four avg ROCE ≥ 10%; growth flat-to-positive nominal; leverage within bounds|§2·1A|P  |
|P4 |Past WEAK                              |Below P3, or sustained ROCE/FCFROCE decline, or leverage breach without P6 conditions|§2·1A|P  |
|P5 |L/E flag level                         |200%|§2·1A|B  |
|P6 |L/E hard cap                           |700% — only if all other metrics are great **and** a creditworthy company is borrowing cheaply to repurchase clearly under-priced stock (or equity shrank via rational distributions)|§2·1A|B  |
|P7 |MCap/FCF threshold — primary           |≤ 8|§2 Gate 2|B  |
|P8 |EV/OI threshold — primary              |≤ 7 (both EV cash-variants)|§2 Gate 2|B  |
|P9 |Sell flag (HELD names)                 |EV/OI > 25 on the **all-cash-excess (lower) EV variant**, absent mitigating facts — the strictest reading; fires only when even the flattering multiple breaches. Sell-reason 2 (quality re-verdict fails) and buyout also flag; see §7.2|§2 Gate 2 / §7.2|B/P|
|P10|MCap/BV threshold — qualifier          |≤ 3|§2 Gate 2|B  |
|P11|MCap/TBV threshold — qualifier         |≤ 3|§2 Gate 2|B  |
|P12|Bending allowance (entry)              |One **primary** metric ≤ 1.25× threshold, only when Past = STRONG|§2 Gate 2|P  |
|P13|Memo body word cap                     |**800 words of running prose** — §6.2 body only; excludes headings, table cells and front matter; bullet sentences count [v3.9.0]|§6|P  |
|P14|Web-operation budget                   |Exploratory search only: **~5 / ~2 / ~1** per name for ANALYSE / REVIEW / SWEEP; **DRAFT ~5** (as ANALYSE; no directed-enquiry extension — the run is unattended) [v4.3.0]; **directed enquiry ~6**, logged separately. Primary-document retrieval, GitHub API calls and RECONCILE uncounted|§4|P  |
|P15|Breadth thresholds                     |Customer: no single customer > 10% of revenue. Supplier: no single supplier > 10% of COGS + opex (ready-alternatives exception)|§2·1B|B  |
|P16|Forces rule                            |Four forces, binary STRONG/WEAK. 0 strong → favourable; 1 strong (contained) → ADEQUATE zone; ≥ 2 strong → Future WEAK|§2·1B|B  |
|P17|Compensation strikes                   |Top-employee total vs **5% of lower(FCF, NI)**, fiscal-year and trailing-3y reads. Absolute scrutiny trigger **US$30m in 2017 dollars, CPI-indexed ≈ US$40m (2026)**, restated at use. Outside director > **2×** the current empirical seat norm (US 2026: chair/lead ≈ $509k → stop ≈ $1.02m; ordinary ≈ $336k → stop ≈ $672k; CPI-indexed $333k → $666k floor default). Scale to local norms|§2·1C·1|B/P|
|P18|Pre-ASC842/IFRS16 lease capitalisation |Capitalise when undiscounted operating-lease commitments > 10% of total assets; discount at disclosed recent cost of debt|§2·1A|P  |
|P19|Capital allocation — judgment protocol |Verdict **SOUND / CAUTION (= 1 flag) / ADVERSE (= SF FAIL)** — recency-weighted (trailing ~3y + live programme dominate), forward evidence named. Yardsticks, never triggers: bargain lines **MCap/FCF 8× / EV/OI 7×** = disciplined execution; **≈ 25× on all four reads** = clearly overpriced. Full P1-window repurchase + M&A worksheet still collected and logged (App E)|§2·1C·3|P  |
|P20|Constructed maintenance-capex basis    |Active only on all three §2 conditions. Effects: valuation-gate FCF on the maintenance basis (labelled), EV/OI typically binding, strict all-capex band stated alongside; quality gates stay all-capex; P17/P19 FCF legs follow the same basis. Precedents: NOVO v3, TSM, AMZN, MSFT|§2 Gate 2|P  |
|P21|ADD zone (HELD names)                  |Price at or below the trigger band's **no-cash bound**; the P12 outer edge qualifies **only when Past = STRONG and Future = STRONG**|§7.2|B/P|

-----

## §4. DATA PROTOCOL

- **Source hierarchy** [BOOK: filings beat data services — legally accountable, uninterpreted]: (1) company filings — latest 10-K / 20-F / annual report, and the latest proxy for Gate 1C; quarterlies for numbers that must be timely more than audited (current share count, latest balance sheet for EV); (2) one dense aggregated-fundamentals page (e.g., stockanalysis.com, macrotrends, or the SEC XBRL companyfacts API) for the multi-year series — verify judgment-sensitive items (NIBCL composition, lease tables, comp, RPT) against the primary filing; (3) any quote source for current price and market cap. IR e-mail is a legitimate tool for factual questions where feasible; note that the quality of the reply is itself information. List every source in Appendix A.
- **Tier-2 acceptance test [v3.9.0].** An aggregated multi-year series is accepted only on an **exact tie-out**, at the reporting unit, against the primary filings for the latest covered year and one earlier year, on four anchors: revenue, operating income, equity, and **one derived composite that reconciles only if several underlying fields are simultaneously correct** (e.g. net financial position rebuilt from cash + short-term investments − total debt + lease liabilities, which validates the debt/lease split that drives CE, EV and L/E). Exact means exact: a rounding break means the source has restated something, and the series is rejected and rebuilt from filings. On a pass the series is accepted **for the covered years only** — years the source does not carry are a data gap, never an accepted series. Record the anchors and the years tested in Appendix A.
- **Primary-interim-debt rule [v4.2.0].** At every REVIEW touch, the EV inputs that move bands — debt, lease liabilities, cash & STI, preferred, NCI — refresh from the primary interim balance sheet; aggregator figures never update EV inputs (adopted after four logged drift instances, latest NET/ZBRA 2026-08-09).
- **Extraction-conflict rule [v4.2.0].** Never accept a single extraction of a figure that a second document class also carries; where two extractions disagree, rebuild from the primary, ring-fence the consequences, and disclose the conflict in the memo front matter (Ørsted/BH precedents).
- **Never invent a number.** Write "n/a — not disclosed" rather than guessing. Label every derived figure (e.g., "FCF derived = CFO − capex"). Flag every data gap prominently in Appendix A and in the memo body if it affects a verdict.
- **Currency & listings:** keep the reporting currency throughout; note ADR ratios. Fewer than P1 years: proceed with what exists, flag it, and apply the §2·1A cap with its history-/record-limited label.
- **Budget (the P14 rule; §3 records the numbers).** The cap counts **exploratory search only** — search-engine queries and speculative page fetches. **Primary-document retrieval is uncounted**: filings, proxy / remuneration / governance / RPT documents, the IR index pages needed to locate them, and price or quote endpoints — this hierarchy mandates them, so the cap must not fight it. GitHub API calls (§7.4a) never count, and RECONCILE runs on past-chats tools with no web at all. A **directed enquiry** — a user question arriving after a memo is delivered — carries its own allowance, logged separately, and never draws down the originating ANALYSE budget. An aggregator rejected on the tier-2 acceptance test licenses the primary rebuild at no exploratory cost. Report the document count in Appendix A; more than ten documents on one name is itself a disclosure-quality observation worth a line in the memo. Never economise on primary sources; prefer one dense source over many shallow ones; never re-fetch data already in a prior memo (that is REVIEW's delta approach).

-----

## §5. CALCULATION RULES

*Denominators, normalisation, per-share basis and leverage are defined in §2·1A and are not repeated here.*

- Rounding: return ratios and growth to 1 decimal %, multiples to 1 decimal.
- Show the latest-year CE build, TBV build, and EV build (both cash variants) line-by-line in Appendix C; label estimates and judgment calls, including any NIBCL burden-of-proof calls, goodwill treatment, lease capitalisation, maintenance-capex basis (P20 conditions and anchor), IFRS interest reclassification, captive-finance consistency, and financial-institution substitution treatments.
- HELD names: show the P_sell arithmetic (§2 Gate 2) and the implied buyback-multiple arithmetic (P19) in Appendix F/E respectively.
- If a code tool is available, one scripted pass for the P1-window tables is acceptable to reduce arithmetic error; otherwise compute carefully by hand. **Never** produce docx, pdf, xlsx, or any binary format — all output is plain Markdown.

-----

## §6. OUTPUT SPEC — THE MEMO

**Format: one Markdown (.md) file per company-version.** Path: `memos/<KEY>/<KEY>_YYYY-MM-DD_GSC.md` — one folder per §7.1a key, every version of the name inside it [v4.2.1]. Create it as a downloadable file, not chat text. The memo body is the human takeaway — hard cap P13 words of running prose, verdicts up front; everything evidentiary lives in the appendix. The cap is hard and is not a target to fill. Use the headings below exactly, every time.

### §6.1 Front matter (machine-readable header)

```
---
ticker:             # §7.1a key — bare for US-listed lines, exchange suffix for every non-US line
company:
exchange:
isin:               # identity of record (§7.1a); "n/a — not found" only if genuinely unavailable
currency:
memo_date:
memo_version: v1
model_version:      # the MODEL.md version this memo was produced under
price_at_memo:
mcap_at_memo:
verdict:            # BUY | WATCH | AVOID | DNAF
quality_past:       # STRONG | ADEQUATE | WEAK
quality_future:     # STRONG | ADEQUATE | WEAK
sf:                 # PASS | FAIL
cheapness:          # CHEAP | FAIR | EXPENSIVE
window:             # e.g. "FY2016–FY2025 (10y)" | "FY2021–FY2025 (5y, record-limited)"
trigger_band:       # e.g. "CHEAP ≈ $X–Y (EV/OI no-cash/all-cash; P12 edge ≈ $Z)" — both bounds labelled where EV/OI binds
next_review:        # date, event, or price condition
position:           # HELD | —
entry_date:         # if HELD; else omit
avg_cost:           # if HELD; else omit
zone:               # if HELD: ADD | HOLD | SELL-FLAG
add_band:           # if HELD: P21 line — trigger-band no-cash bound (P12 edge only if dual-STRONG)
sell_flag_line:     # if HELD: price where lower-EV EV/OI = 25 (or "n.m. — substitution rule")
---
```

### §6.2 Memo body

```
# [TICKER] — [Company]: GSC Memo

## 1. Verdict
[One line of running prose carrying the five gate results and the final verdict
(+ Zone if HELD). No table — the gates are already machine-readable in the
front matter. [v3.9.0]]
[One-paragraph thesis: what this business is worth owning for, what stands
between here and a BUY (or, if HELD, where the position sits between the ADD
band and the sell-flag line), and what would need to change for the verdict
to flip.]

## 2. Understanding
[The single sentence. PASS / FAIL.]

## 3. Quality — past record
[≤ 120 words: level and trend of ROCE/FCFROCE (worst-of-four averages named;
substitution rule named if applied), per-share growth shape vs the 3% floor,
leverage posture. Verdict + one-line reason.]

## 4. Quality — future
[≤ 120 words: breadth result (waiver noted if used), the four binary force
calls and tally, the moat and its direction, market growth note. Verdict.]

## 5. Shareholder-friendliness
[≤ 100 words across the three tests incl. P17 numbers vs local norms and
the capital-allocation verdict with its decisive forward evidence. Verdict;
if FAIL, name the strike, the ADVERSE judgment, or the flag pair.]

## 6. Price
[Table: Metric | Current | Threshold | Rank (Primary/Qualifier) | Pass/Fail.
One sentence: trigger band, binding primary, qualifier status/investigations.
If HELD: one further sentence — current zone, distance to the ADD band and to
the sell-flag line.]

## 7. Risks & thesis-breakers
[3–5 bullets, each one sentence.]

## 8. Flip conditions & next review
[What flips the verdict, in which direction; the next-review trigger.
For HELD names: restate the four valid sell reasons (price past value — P9;
company no longer good — fight the consistency bias; buyout; clearly better
opportunity — extreme suspicion, user judgment, never framework output) and
the invalid ones (rebalancing, memorialising success, agent compensation).]

*Framework output, not investment advice.*
```

### §6.3 Appendix (same file, below a horizontal rule)

```
# APPENDIX
## A. Sources & data gaps
## B. Financial record (P1 window — state the years, and the §2·1A label if short)
   B1 Raw inputs: FY | Revenue | OI | CFO | Capex | FCF (derived) |
      Diluted shares | Total assets | NIBCL | Cash+STI | Total liab | Equity |
      Goodwill+intang
   B2 Returns: FY | CE_wc | CE_xc | ROCE_wc | ROCE_xc | FCFROCE_wc | FCFROCE_xc
      + summary row: P1-window normalized averages, four ways (beg/end × wc/xc),
      worst value flagged and tested against P2/P3
   B3 Growth & leverage: FY | ΔOI/sh % | ΔFCF/sh % | ΔBV/sh % | ΔTBV/sh % | L/E
## C. Calculation notes
   [Latest-year CE, TBV, EV builds (both cash variants) line-by-line; NIBCL
   calls; goodwill/lease/maintenance-capex (P20)/IFRS-interest/captive-finance/
   substitution-rule treatments; bias-check log.]
## D. Future-performance worksheet
   [Breadth Q&A with evidence (waiver conditions if applied); four-force
   binary table with one-line reasons and tally; moat note; market note.]
## E. Shareholder-friendliness evidence
   [Top-exec comp vs indexed absolute + 5% lower(FCF, NI), both P17 reads, basis stated;
   outside-director fee vs local norm; insider ownership %; RPT summary +
   share-of-expense test; capital-allocation worksheet [P19] — full tranche
   table (cash, shares, implied MCap/EV, year + 3y-normalized multiples, both
   bases) against the 8×/7× and ≈25× yardsticks; acquisition record vs
   pre-deal OI; payout & funding record; judgment log — verdict,
   recency-weighted reading (≤ 10 lines), named forward evidence,
   consistency-hazard check.]
## F. Valuation math
   [Current multiple arithmetic (both EV variants); the threshold-implied
   prices — the EV/OI leg always shown as both bounds, each labelled no-cash
   or all-cash, with the range and its width stated; binding-primary logic;
   P12 edge if applicable; P20 dual-basis bands if active; qualifier prices for
   context; sell-flag line arithmetic if HELD; backvaluing worksheet if used.]
## G. Change log
   [v1 — date — initial analysis. REVIEW versions append here.]
```

### §6.4 Abbreviated memo (Gate 0 failure only)

Front matter (verdict DNAF) + body sections 1 (Verdict) and 2 (Understanding, explaining precisely why no clear statement could be written) + the register row. No appendix beyond sources consulted.

### §6.5 After every memo

Run the §7.4a session-end sequence: print the register diff and file list, take the confirm, commit memo + §7.5 snapshot + full regenerated register, report the URLs — plus the portfolio row if the name is HELD. On any API failure, fall back to §7.4a's paste-block path.

-----

## §9. STYLE

*The resident guardrails — no price targets, no invented numbers, plain Markdown only, token secrecy, commit gates — live in the bootstrap and win on any conflict. This section carries only what is model-layer.*

- Analytical and direct; no padding, no hedging beyond genuine data uncertainty. Verdicts stated plainly and never softened. Avoid making excuses for unremarkable companies — or for companies already owned.
- Quantitative material in tables; qualitative reasoning in tight prose. The memo body must be readable in under three minutes.
- Flag every estimate, derivation, and data gap explicitly, at the point of use.
- **The memo explains the company, not the framework [v3.9.0].** Body prose carries data, verdicts and reasoning only — never a restatement of framework mechanics, thresholds, strike logic or rule text. The reader has the model. Tags (P19, §2·1C, "worst-of-four") are references, not explanations; rule text in the body is wasted words against the P13 cap.
- Same data ⇒ same verdict. Where judgment is unavoidable, apply §3 and record the call in Appendix C.
