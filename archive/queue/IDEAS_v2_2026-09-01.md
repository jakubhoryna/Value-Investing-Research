# GSC MODEL Ideas — IDEAS.md (v2 · 2026-09-01)

**Purpose.** Parking lot for framework questions — everything MODEL-mode-shaped that a session surfaces goes here, never into the register's `## Open items` (routing per MODEL §7.1, v4.2.0). Each entry carries: status, the instances that raised it, the question in one line, a book-grounded recommendation with confidence, and the consequence scan. **Nothing here is operative** until a MODEL session adopts it under its own explicit "commit model"; recommendations below are pre-work, not doctrine. MODEL sessions open from this file and close by updating entry statuses.

**Statuses:** OPEN (undecided) · SCHEDULED (user has queued a MODEL session) · CODIFIED vX.Y.Z (adopted — entry retained one cycle, then archived) · REJECTED (with reason).

---

## A. Verdict-affecting — each needs a dedicated MODEL decision

### A1. Operating-income line convention — THE blocking item
- **Status:** **SCHEDULED** (user, 2026-08-18) — next MODEL session decides A1 alone; A2–A7 stay parked. The register's own instruction stands: codify or reject before a third name is decided on it.
- **Instances (10):** SGO.PA (decisive → WATCH), ML.PA (decisive → AVOID), SW.PA, BVI.PA, FR.PA, MMB.PA, TRI.PA, 6501.T, 7011.T, 6752.T. Two decided in **opposite directions**: SGO.PA survived Past on the line *labelled* "Operating income" (10.07% vs 7.70–9.26% on Business income); ML.PA died on the same label rule (8.39% vs 10.09% on segment OI). MMB.PA/7011.T: no labelled line exists at all. 6501.T: the clean definitional object is itself a prohibited add-back ("Adjusted OI" excludes impairments/restructuring). 6752.T: all three candidate rules coincide, wedge 28.9%, still non-determinative.
- **Question:** which reported subtotal is "operating income" when a filer presents several candidates — the label, the definition (revenue − COGS − SG&A), or something substantive?
- **Book grounding:** Ch. 8 defines OI substantively to strip *only* capital structure and tax — never operating misfortune. §2·1A / D8: as-reported OI, **no add-backs** of impairments, litigation or "one-offs"; multiyear averaging dilutes them; never tweak. Ch. 7: subtractive conservatism — the dimmest defensible light. A subtotal that excludes recurring restructuring or acquisition amortisation is an add-back wearing a label.
- **Recommendation (~85%):** the substantive-conservative rule — **"the reported operating subtotal that includes the most operating charges"** (7011.T's restatement), scoped by materiality (TRI.PA's proposal): where candidate lines differ by < ~50bp of worst-of-four ROCE, take the labelled line and log one sentence. Never accept a subtotal that excludes recurring operating charges. This dissolves the label-vs-definition conflict, works on filers with no labelled line, and is nationality-blind (the 8th–10th instances proved it is not a French question).
- **Counter-case:** a pure label rule maximises repeatability — but MMB.PA and 7011.T show the label can be absent, so the label rule is incomplete by construction; and 6501.T shows the pure definitional rule selects a prohibited add-back.
- **Consequence scan:** ML.PA AVOID unchanged (its labelled line is already the conservative one). **SGO.PA re-verdicts at next REVIEW — likely WATCH → AVOID** (Business income 7.70–9.26% → Past WEAK). SW.PA unchanged (verdict carried by Future). BVI.PA, FR.PA, MMB.PA, TRI.PA, 6501.T, 7011.T, 6752.T all non-determinative. One flip, downward — conservative.
- **Class:** MINOR (verdict-affecting through the SGO.PA re-test).

### A2. Captive-finance basis / substitution boundary is verdict-bearing (SIE.DE, KSPI)
- **Status:** OPEN.
- **Instances:** SIE.DE (strict/include-both basis → Past WEAK; SFS-excluded basis → ADEQUATE; band moves materially — the treatment decides a gate and the zone). 6501.T ran the symmetric test on Hitachi Capital: 2bp, decides nothing — evidence this is a *live-captive* question, not a conglomerate question. **KSPI (2026-09-01) — the decisive instance, and the first to move a *final verdict* rather than a gate.** Kaspi.kz run under §2·1A substitution (v2) = **WATCH**, worst-of-two normalized ROE 60.5%, MCap/NI anchor, band ≈$98, first in the WATCH section. The same balance sheet run on the industrial machinery (v3, user-directed) = **AVOID**: L/E 340% breaches P5 with P6 unmet, which no deposit-taker can avoid. The two readings are each internally consistent and they disagree on the verdict, not the level. Kaspi also splits the two candidate boundary tests: the deposit-funded segment is **33% of net income** (below a profit-share boundary → industrial lens) but the loan book alone is **62% of assets** (above the ~1/3 asset boundary proposed below → substitution). The parameter choice therefore *is* the verdict here.
- **Question:** when the §2·1A default (include the finance segment's OI and assets — "include-both") and the logged alternative (symmetric exclusion) straddle a gate, which reading bears the verdict?
- **Book grounding:** three-statement consistency (adjustments shaping one number shape the others); burden of proof sits with the flattering treatment; dimmest light; the Introduction's blind-spot concession licenses *substitution* only where finance dominates the group.
- **Recommendation (~80%):** the default (include-both) is verdict-bearing; the symmetric exclusion is logged context. A gate that passes only on the alternative reading has not passed. Where the captive dominates, the §2·1A financial-institution substitution rule applies instead — that boundary (say, finance segment > ~1/3 of group assets) is the parameter to set. **Sharpened by KSPI (~85%): set the boundary on assets, not profit, and state it as a bright line.** Substitution exists because the CE/EV/L-E machinery is structurally inapplicable to a deposit-funded balance sheet — a balance-sheet defect, so a balance-sheet test. An earnings-share boundary would put a licensed bank with ₸7.4tn of customer loans through a leverage test it cannot pass, purely because its non-bank siblings out-earned it that year. Two further KSPI findings belong in whatever is codified: (a) where OI is reported after funding cost (no operating subtotal), EV/OI must be paired **financing-blind** or marked n.m. — the mixed pairing produced a spurious 6.0× 'uncertainty' spread in KSPI v2; (b) where CFO embeds loan-book and deposit movements, FCF must be carried on **two labelled bases** (as-reported and pre-balance-sheet), because the two disagree by a factor of 2.5 in a single year and by sign on per-share growth.
- **Consequence scan:** SIE.DE Past re-tests at next REVIEW under the codified basis — possible WATCH → AVOID. **KSPI re-verdicts immediately on either codification** — AVOID stands under a profit-share boundary, reverts to WATCH under the ~1/3-of-assets boundary. Sweep the other substitution-rule names for the same boundary sensitivity at next touch: BRK.B, INVE-B.ST, AZA.ST, NU, IBKR, KLAR, 8002.T, TROW.
- **Class:** MINOR (verdict-affecting through SIE.DE and KSPI; KSPI is live and mis-stated under whichever reading is not codified).

### A3. Gate-0 per-unit stopping rule (conglomerates)
- **Status:** OPEN — raised formally by 6752.T (Gate-0 confidence ~60%, the register's lowest).
- **Instances (drift chain):** BRK.B → SIE.DE → 005930.KS → 6503.T → 6501.T (4 units / 31% cap; CI itself a portfolio) → 7011.T (per-unit applied to a 16% six-limb segment) → 6752.T (7 units, none above 17.6%, **two irreducible portfolio units ≈35% of revenue**, largest block literally named "Other").
- **Question:** does the per-unit understanding route have a stopping rule? MODEL currently does not say.
- **Book grounding:** Ch. 5 multi-unit rule defines the six parameters *per unit* — one level of decomposition, never per sub-unit; each statement must pass the "author cannot fail to understand it" test; genuine incomprehension or obfuscation is a hard stop; and the famous inversion — the danger of the ununderstood is *making* money on it.
- **Recommendation (~75%):** codify **one-level decomposition**: the per-unit route passes only if every material unit (≥10% of revenue) is itself describable in one six-parameter sentence; an irreducible portfolio unit above that line, or a material "Other", fails Gate 0 → DNAF. BRK.B survives (its units individually pass, insurance under the D20 substitution context).
- **Consequence scan:** 6752.T likely AVOID → DNAF (verdict word only — it is AVOID on two quality gates regardless); 6501.T PASS survives at ~75% (CI is the contestable unit); 7011.T ~70%. No band or zone moves.
- **Class:** MINOR (doctrinal cleanliness; minimal row movement).

### A4. Substitution-rule scope bundle (financial-adjacent forms)
- **Status:** OPEN — three logged extensions await codification; none was verdict-deciding where applied, which is exactly when to codify.
- **Instances:** ZIP.AX (non-deposit-funded lender — warehouse/ABS-funded, no licence — admitted on the rule's rationale; P19 yardsticks restated on the NI anchor: bargain 8×, overpriced ≈ 8 × 25/7 ≈ 28.6×). WISE.L (licensed e-money institution: ROE for ROCE; EV/OI + MCap/FCF anchors; all-cash EV a *bound* because own cash is inseparable from safeguarded customer funds). SAVE.ST (deposit-funded lender NI-proxy — already inside the Gate-2 substitution paragraph; listed for completeness). BH (circular structure: consolidated fund holds parent stock → gross and look-through readings of share count and equity — second §2·1A substitution run, wrinkle unhandled).
- **Book grounding:** the Introduction concedes the model yields weird verdicts on financial institutions — substitutions there are repairs, not deviations (D20).
- **Recommendation (~85%):** codify the two scope extensions verbatim from the memos' App C/E statements, plus one general rule: **under any substitution, the P19 yardsticks restate on the name's cheapness anchor** — disciplined at ≤ the anchor threshold, clearly overpriced at ≈ anchor × (25/7). Handle the BH circular structure inside the same paragraph: where the consolidated entity holds parent stock, state both gross and look-through readings and let the more conservative bear the verdict.
- **Consequence scan:** none retroactive — no current verdict rests on the calls.
- **Class:** MINOR.

### A5. Holdco / large-NCI substitution (CDI.PA)
- **Status:** OPEN.
- **Instances:** CDI.PA (full consolidation of a 42%-owned listed subsidiary breaks two rules in opposite directions: L/E 296% ex-NCI vs 109% incl.; MCap/FCF 5.5× consolidated vs 13.5× look-through; NCI at book understates the minority claim by ≈€95bn vs market). MMB.PA logged as a **non-instance** (NCI unlisted — no quotation to substitute).
- **Book grounding:** Ch. 14 — the income statement "dreams full ownership", so EV must carry the minority's claim; the book uses book NCI because that is what a balance sheet offers, but where a market quotation exists, book NCI is not the conservative reading. BV excludes NCI by definition.
- **Recommendation (~80%):** for groups consolidating a **listed** subsidiary whose NCI is material: EV carries NCI at market value; cheapness runs look-through (parent's share of the sub at market + stub); L/E on ex-NCI equity, flagged. Unlisted NCI stays at book (MMB.PA treatment).
- **Consequence scan:** CDI.PA re-screens at next touch; no other current name.
- **Class:** MINOR.

### A6. P4 on definitively cyclical industries
- **Status:** OPEN — genuinely two-sided; the register's `P4-driven` class is the evidence base.
- **Instances (6):** EQNR (sharpest: worst-of-four ROCE 21.9–23.6%, EV/OI 4–5×, failed by the 2023–25 declines alone), ATKR (29.4%), XPEL (25.1%), CRI (14.8–19.0%), HOG (ROE substitution), ML.PA.
- **Question:** should a multi-year returns decline force Past WEAK regardless of level on a definitively cyclical name, or cap it at ADEQUATE when worst-of-four still clears the P2 level bars?
- **Book grounding — both sides:** P4's regardless-of-level rule is a **project overlay (Src P)**, not book text. The book judges the past on worst-of-four multiyear averages, never tweaks, and reads trend as *where to look next* (the Gap case: declining growth sent the question to Gate 1B, it did not kill Gate 1A). Backvaluing (Ch. 14) is the book's only cyclicality instrument — price-side, three strict conditions, "a tourniquet". Against relaxing: Ch. 11's discipline — *avoid making excuses for unremarkable companies* — is precisely an anti-rationalisation rule, and P4 is its teeth.
- **Recommendation (~65%):** scope P4 with a carve-out mirroring backvaluing's own conditions: on a definitively cyclical industry (the backvaluing test), a decline that still leaves worst-of-four ≥ P2 levels caps Past at ADEQUATE rather than forcing WEAK; everywhere else P4 stands unchanged. If instead kept as-is: that is also defensible — the model simply waits for the cycle to restore the record (patience, not error).
- **Consequence scan:** EQNR, ATKR, XPEL, CRI, HOG, ML.PA all queue for re-test if adopted — the largest verdict surface of any A-item. Requires the full §8.4 step-3 scan at drafting.
- **Class:** MINOR, verdict-affecting.

### A7. Channel-structure breadth — distributor and OEM concentration (P15)
- **Status:** OPEN — register flagged "MODEL calibration blocking-relevant".
- **Instances:** fulfilment-distributor: ZBRA (3 distributors = 59% of revenue — the register's most extreme; its MODEL-recalibration flip path was removed by the live ADVERSE path), PANW. OEM-concentration: MBLY, CATL (provisional; waiver denied 3×). Platform-payer cluster (EA, TTWO, CDR.WA — all Future WEAK on the same finding) is the adjacent precedent line.
- **Question:** is distributor concentration customer concentration when end-demand is demonstrably broad?
- **Book grounding:** Ch. 12 — the customer is whoever *pays* (Yahoo's advertisers), and the disclosure sentence is the test; Delta Financial teaches look-through, but that lesson cut toward *finding hidden concentration*, never toward waving disclosed concentration away. The supplier side carries a ready-alternatives exception; the customer side deliberately does not.
- **Recommendation (~70%):** keep the paying-customer reading as the test (book-faithful, conservative). Add at most a narrow, logged mitigation mirroring the supplier exception: concentration through **demonstrably replaceable pass-through distributors** (several stand ready, no credit/stocking dependence) may be downgraded from breadth FAIL to a flag — never for OEMs or platform payers, where the payer bears real bargaining power. Until decided, the precedent binds (EA/TTWO/CDR.WA line).
- **Consequence scan:** ZBRA (moot — ADVERSE path), PANW, MBLY, CATL re-test if adopted.
- **Class:** MINOR, verdict-affecting.

---

## B. Codified at MODEL v4.2.0 (2026-08-18) — traceability list

- **B1. Open-items routing** — register carries state only; two admissible open-item classes (user decisions, integrity holds), cap 7; work → TODO, ideas → here; RECONCILE triage step; MODEL sessions open from this file. (§7.1, §7.5, §8.4, §8.5)
- **B2. Primary-interim-debt rule** — EV inputs refresh from primary interim balance sheets at every REVIEW; aggregator figures never move bands. Four logged drift instances (latest NET $3,530→$3,270.3m, ZBRA $2,960→$2,776m). (§4)
- **B3. Extraction-conflict rule** — never accept a single extraction of a figure a second document class also carries; on disagreement rebuild primary, ring-fence, disclose in front matter. (Ørsted AR2025 table; BH double-fetch divergence.) (§4)
- **B4. `n.m.`-band restoring-OI statement** — whenever a band leg has no positive solution, state the OI level that restores the no-cash bound; four structurally distinct causes print identically as `n.m.` (TRS ≈$62.5m net-cash case · ENOV ≈$183.5m no-positive-OI · WEN ≈$487m unattainable · CRI ≈$153.7m near miss). (§2 Gate 2)
- **B5. Commit-time compliance re-measure** — P13 body count, §7.1 cell caps, §7.5 log caps, the four-gates-only check (ROCK-B.CO defect class), and register-wide superlatives (computable only against the full live register) are re-measured at commit; a run's own compliance assertion is not evidence. (§7.4a)
- **B6. Same-day memo archive symmetry** — a same-day supersession archives the outgoing memo to `memos/archive/` before the overwrite, closing the §7.4a asymmetry (cross-day versions keep both files; same-day previously did not). (§7.4a/§7.5)
- **B7. (No MODEL change)** Utilities screen-at-queue-stage stays a queue rule in `queue/TODO.md` — regulated-return capital bases fail Past by construction (NEE, IBE.MC, SRE, FORTUM.HE, ORSTED.CO); screen candidates out before ANALYSE budget is spent.

---

## C. Register / process feature ideas

- **C1. `P4-driven` notes tag.** Four-to-six AVOID names failed by the trend rule over adequate-to-strong levels (ATKR, XPEL, CRI, HOG; EQNR, ML.PA adjacent) are structurally different from the loss-making cohort around them. A one-token tag in the `Next review / notes` cell at the next regeneration is contract-compatible (one flag token allowed); adopt with A6 or standalone.
- **C2. Captive-customer waiver precedent table (calibration — keep current here).** GRANTED: ASML, 2330.TW/TSMC, QCOM, BA.L. DENIED: 7011.T (moat limb — group-level returns don't evidence dominance), CDR.WA (platform payers), FR.PA (limbs 1–2 — OEMs demonstrably backward-integrate), 6752.T (0 of 3 — first zero, customer both integrated and second-sourced). Calibration line: sovereign/fab-class fewness + prohibitive switching + dominant moat grants; platform payers and in-sourcing OEMs deny. 6752.T also answered 7011.T's open question — the moat limb reads at **group** level (the unit-level reading was worse there, so unit-level is no shelter).

---

## D. Calibration observations — evidence on file, no rule proposed

- **D1. SBC-wedge cluster (9 names, 2026-08-09 run).** Stock comp consumes the GAAP operating line while FCF compounds; every member fails Past bound-proof. Control cases with real net retirement: ADBE, INTU, FDS. Evidence for a possible future note on SBC-heavy filers; no change proposed — the wedge is real economics, not noise.
- **D2. P17 denominator collapse is the register's dominant SF failure mode** (33 SF FAILs in the 62-name batch; 7 of 9 in the 09-Aug run). Mechanism: the 5%-of-owner-earnings ceiling falls with earnings, so ordinary packages strike in bad years. Exceptions worth keeping: XPEL (1.04×/1.20×) and ARHS (1.58×/1.60×) — healthy positive denominators; WINA the narrowest strike (1.2%/3.9%). Read: **the rule working as designed** — pay against no owner earnings is the book's own categorical case; no change proposed.
- **D3. MCap/FCF-passes / EV-OI-fails cluster (6: PTON, COTY, TDOC, TRIP, CC, WEN).** The two-primaries pairing catching leverage exactly as Ch. 14 intends (WEN: equity 5.9× while the enterprise fails at 13–16× on $3.41bn of debt/leases over a $1.43bn MCap). No change.
- **D4. P19 ADVERSE tally 7** (PANW #5, SNOW #6, WDAY #7; TWLO named risk on 2026 tranches; INTU the liveness-calibration case; DBX the debt-funded acquittal at ~9–11× FCF). Calibration context for §2·1C·3 judgments; no change.

---

*Framework output, not investment advice.*
