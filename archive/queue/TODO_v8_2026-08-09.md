# GSC Analysis Queue — TODO.md (v8 · 2026-08-09)

**Purpose.** Backlog of names to run through the GSC pipeline — ANALYSE for names with no memo, REVIEW for existing ones. This file is *not* authoritative state: `_REGISTER.md` remains the single source of truth. Nothing here is a verdict or a recommendation; it is a work queue.

**Ticker discipline.** Tickers below are *suggested* primary listings for convenience only. They are **resolved and verified at analysis time** against the data-source hierarchy (SEC EDGAR / primary annual report / Yahoo), never trusted from this file. A wrong suggestion here costs nothing; a wrong verdict from bad data costs everything — so resolution + a data-completeness check happen per name at run time.

---

## ⛳ QUEUE STATUS — CLOSED (2026-08-09)

**Zero runnable ANALYSE names. Zero open flags requiring analysis.** All 94 names carried in the v7 backlog now hold register rows and committed memos; every market block is closed (see "Backlog — closure record"). The only work this file schedules is **REVIEW work**: the dated re-tests below and the P19 judgment queue.

**One residual token:** ⚑ the "Cartara" line was resolved **by assumption** to Certara (CERT) and analysed. If a different company was intended, the CERT memo stands as a valid extra row and the flag reopens — user confirmation owed.

---

## P19 judgment re-test queue — MODEL v4.0.0 §2·1C·3

**Why it exists.** MODEL v4.0.0 (2026-07-31) replaced the mechanical P19 buyback/dividend tests with a single capital-allocation judgment — **SOUND / CAUTION (= one flag) / ADVERSE (= SF FAIL)**. Every name whose SF FAIL rested on a mechanical P19 strike must be re-read under the judgment protocol at its next touch. The authoritative status list is the register's `## Open items` entry "MODEL v4.0.0 judgment re-test queue"; this block is the work queue.

**Tier 1 — quality gates pass, so the P19 re-read alone decides the verdict: CLOSED 2026-08-06 (8/8).**

| Name | Prior | Run | Judgment | Outcome |
|---|---|---|---|---|
| SONY → 6758.T | AVOID (P19) | 2026-08-06 v2 | CAUTION | **→ WATCH** |
| ASICS → 7936.T | AVOID (P19) | 2026-08-06 v2 | CAUTION | **→ WATCH** |
| SOON → SOON.SW | AVOID (P19) | 2026-08-06 v2 | CAUTION | **→ WATCH** |
| STMN → STMN.SW | AVOID (P19 + DTC pair) | 2026-08-06 v2 | CAUTION | **→ WATCH** (STRONG/STRONG) |
| TRI | AVOID (P19) | 2026-08-06 v2 | CAUTION | **→ WATCH** |
| SU → SU.PA | AVOID (P19 + AVEVA) | 2026-08-06 v2 | ADVERSE | AVOID holds |
| TER | AVOID (P19) | 2026-08-06 v3 | ADVERSE | AVOID holds |
| WMT | AVOID (P19) | 2026-08-06 v2 | ADVERSE | AVOID holds |

**Tier 2 — mixed pairs, where the P19 leg is only one of two flags. A P19 re-read alone cannot flip these; the second leg has to be tested too.**

| Name | Second leg | Status |
|---|---|---|
| NOLA-B.ST | P17 fiscal-year read flag | **Run 2026-08-06 v3 — CAUTION, pair holds, AVOID.** Flip is now one dated event: FY2026 FCF > ≈ SEK 295m clears the P17 year read → WATCH. FY2026 AR ~Apr 2027 |
| WISE.L | Class B entrenchment (9:1, 64.7% of votes on 20.4% of capital) | **Run 2026-08-06 v3 — CAUTION, pair holds, AVOID.** KNEBV governs, not MC.PA. Re-test H1 FY2027 ~Nov 2026 |
| AAPL | P17 comp strike | **Open** — flip requires comp reform; FY2026 10-K ~Oct/Nov 2026, then Jan 2027 proxy |
| MA | P17 comp strike ($35.4m > $30m stop) | **Open** — 2027 proxy (~Apr 2027) |
| DLG.MI | La Marzocco RPT pair | **Open** — FY2026 AR (~Mar 2027); hard dates Feb 2028 IPO right / Feb 2029 demerger right |
| PSH.L | Fee extraction | **Open** — FY2026 AR (~Feb 2027) or any fee change |

**Tier 3 — WATCH-name P19 flags: judgment context only, no queue action.** INVE-B.ST, FIE.DE, ROG.SW, ULVR.L, KNIN.SW, AXFO.ST, LIFCO-B.ST — each already carries one unpaired capital-allocation flag; they matter as calibration for the names above, and as pair-risk if a second negative ever appears.

**Near-dated re-tests created by the 2026-08-06 batch** — the earliest points at which any of the five flips could revert: **7936.T Q2 tanshin 14 Aug 2026** (art. 459 board authority means a new programme can appear with no notice), **TRI NCIB expiry 18 Aug 2026** (renewal price decides), **STMN.SW H1-2026 19 Aug 2026** (treasury-share movement), **SOON.SW H1 FY26/27 ~Nov 2026** (successor programme), **6758.T H1 FY3/27 10 Nov 2026** (first completed half of the ¥500bn facility). **New at v7: DLB FY2026 10-K ~Nov 2026** — window-roll re-test of a bound-proof Past WEAK (w-o-4 ROCE 9.1–9.9% against the 10% floor), plus the customer-concentration disclosure. ⚠ The first three (14/18/19 Aug 2026) fall within days of this commit.

---

---

## Priority — next up

**REVIEW work only, in date order.** These are the near-dated re-tests where a live event can move a verdict, three of them within nine days of this commit:

1. **7936.T (ASICS) — Q2 FY2026 tanshin, 14 Aug 2026.** Article 459 board authority means a new buyback programme can appear with no advance notice; the P19 judgment that flipped this name to WATCH is the thing being re-tested.
2. **TRI (Thomson Reuters) — NCIB expiry, 18 Aug 2026.** The renewal price is the re-test; a renewal at current multiples is the CAUTION→ADVERSE risk.
3. **STMN.SW (Straumann) — H1-2026, 19 Aug 2026.** Treasury-share movement against a name with no live programme.
4. **INTU (Intuit) — FY2026 results, ~21 Aug 2026.** New WATCH row; the FY2026 tranche prices decide whether P19 CAUTION holds at 35–46× or turns.
5. **SOON.SW ~Nov 2026 · 6758.T H1 10 Nov 2026** — the remaining two Tier-1 flip-reversion watches.

**Re-seeding the ANALYSE queue is a user decision.** Three candidate directions, in the order they would add most:

- **(a) Run the named re-test backlog as REVIEW work.** The register's Open items now carry a large named queue — P19 dual-reads, acquisition-audit INDETERMINATEs, P4 third-decline tests, window-roll Past re-tests (DLB ~Nov 2026, WDAY and DBX ~FY2028), and the SF re-test tiers. This is the highest-value work per hour because every name already has a memo, so each run is a delta, not a build.
- **(b) A corporate-actions sweep of the full register** — owed at the next RECONCILE regardless: delistings, renames, re-keys (BBBY→NXH is already pending), spin-offs and closed deals across 304 names. Cheap, mechanical, and it prevents the register from quietly rotting.
- **(c) A new ANALYSE market block.** Coherent untouched universes: Canada, Australia, Korea/Taiwan beyond the two names held, India, the US mid-cap industrial tail (the automation-thesis adjacency), or the European small-cap compounders. **Note the standing screen-at-queue-stage rule from this batch: regulated utilities should not be seeded** — NEE, IBE.MC, SRE, FORTUM.HE and ORSTED.CO all fail Past structurally, by design of their capital base, and cost full ANALYSE budget to reach a foregone conclusion.

---

## Scheduled reviews — near-term calendar

*Refreshed 2026-08-09 against register **v248** row cells — this clears the staleness carried since v5 (which read against v173). Non-authoritative: the register wins. Dated triggers only; price-alert triggers live in the rows.*

**Aug 2026 (imminent):** **7936.T Q2 tanshin 14 Aug** (P19 re-test, no advance notice) · **TRI NCIB expiry 18 Aug** (renewal price) · **STMN.SW H1 19 Aug** (treasury movement) · **ZIP.AX FY26 Appendix 4E 20 Aug** (P19 re-test on the live Feb-26 programme + P17 re-read) · **INTU FY2026 ~21 Aug** · GAP Q2 ~26 Aug · ABNB Q2 10-Q 12 Aug (cadence) · BABA FY2027 Q1 · ADYEN.AS H1 · PAH3.DE H1 mid-Aug · WMT Q2 FY27 10-Q · TEAM FY2026 10-K (OI inflection + P19 on the $1.5bn 2024 programme) · CELH Q2 10-Q · RUSTA.ST AR 25/26 · BNR.DE H1 (optional) · 1211.HK H1 (optional) · NET Q2 2026 (6 Aug, out — fold in at next touch) · ZBRA Q2 2026 (4 Aug record print, not folded in).
**Sep 2026:** **FDS FY2026 results ~Sep** (first Viswanathan-era print; the make-whole SCT is the named P17 strike risk) · **PANW FY2026 10-K ~Sep** (first CyberArk-consolidated statements) · **UFI FY2026 10-K ~Sep** · CRM Q2 FY27 ~2 Sep (optional) · LULU Q2 ~Sep (O'Neill's first quarter) · NKE Q1 FY2027 10-Q ~Sep/Oct + Sept proxy (dated second-flag risk) · RUSTA.ST AGM ~Sep (P19 authorisation watch) · **EA deal outside date 28 Sep** — close → row terminal/archive; lapse → full REVIEW at the de-pinned price.
**Oct 2026:** **COST FY2026 10-K ~early Oct** (completed programme year; Jan-2027 authorisation expiry is the natural re-test) · MU FY2026 10-K ~Oct (band re-anchor only — structural) · TER Q3 10-Q ~Oct · MSFT FY2026 proxy ~Oct (P17 absolute-trigger flag) · EL.PA Q3 20 Oct (informational) · **SW.PA FY2026 results 23 Oct** (guided 3.2–3.4% margin removes the band entirely; P4 + P19 re-test) · AAPL FY2026 10-K ~Oct/Nov (SF flip needs comp reform).
**Nov 2026:** **6758.T H1 FY3/27 10 Nov** (first completed half of the ¥500bn facility — the §2·1C·3 re-test) · SOON.SW H1 FY26/27 ~Nov (successor-programme watch) · **DLB FY2026 10-K ~Nov** (window-roll re-test of a bound-proof Past WEAK at 9.1–9.9% against the 10% floor — the most interesting near-dated flip in the file) · QCOM FY2026 10-K ~Nov (FY26 tranche; band re-anchors on a falling base) · ROK FY2026 10-K ~Nov (completed programme year) · V FY2026 10-K ~Nov (the 11%-client disclosure) · ATKR FY2026 10-K ~Nov · AZTA FY2026 ~Nov · SONO FY2026 10-K ~Nov · COLO-B.CO FY2025/26 ~Nov (L/E exactly at the P5 line) · 7974.T Q2 FY3/27 ~Nov · 8002.T H1 FY3/27 ~Nov · EKTA-B.ST H1 ~Nov · WISE.L H1 FY2027 ~Nov (the £405m tranche price) · **TRI.PA FY2026 results ~25 Nov** (first buyback year; the register's closest AVOID at +7.7% from band) · SCHN.SW repurchase-cessation watch (programme runs to Nov 2026) · PANW 2026 proxy ~Nov.
**Dec 2026 / Q4 events:** ENR.DE FY2026 AR ~Dec (first clean-cycle year + P19 re-test of the €2bn/€6bn programme) · SIE.DE FY2026 ~Dec (tranche + CAUTION re-test; the Feb-2027 AGM Healthineers spin vote forces a full quality re-base) · SKF-B.ST Automotive Lex Asea separation ~Q4 (resets the basis; both entities re-underwritten) · TKA.DE and TUI1.DE FY2026 ARs (informational) · INPST.AS settlement H2 2026 → delist, archive the row · BAYN.DE Roundup class-settlement approval + post-Durnell provisioning (H2 2026).
**Q1–Q2 2027 — FY2026 annual season:** the bulk of the 68-name WATCH list re-anchors, including all four held names (and the HFG / NOVO-B decisions if still open), plus the named re-test queue — P19 dual-reads (SCHN.SW, GEBN.SW, SAF.PA, TER, MORN, GRMN, SU.PA), acquisition-audit INDETERMINATEs (FIE.DE Shopko, ASSA-B.ST HHI, ESSITY-B.ST BSN, GETI-B.ST Paragonix, EPI-A.ST Stanley, MYCR.ST cohort, KRN.DE Netstal), P4 third-decline tests (INDT.ST, SKF-B.ST, CELH), **EQNR FY2026 ~Feb 2027 — the P4-break that would flip a name whose shadow P12 edge already sits at the print**, ABEV FY2026 + the band-moving FCF tie-out, NU FY2026, CATL FY2026 AR (the customer-concentration table is Future-deciding), ADBE FY2026 10-K ~Jan, and the FY2027 10-K cluster from this batch (CRWD, SNOW, OKTA, PATH, S, WDAY ~Mar 2027) — **detail: register `## Open items`.**

---

## Overnight / delayed-run design (draft — for later recycling)

Design sketch for an unattended runner that processes this queue on a schedule. Not built yet; finalise later.

**Substrate.** Claude Code in headless mode (`claude -p`) driven by a **scheduled GitHub Action** (`on: schedule: cron`). This reuses the existing repo-native pipeline — `MODEL.md` as the operative framework, `_REGISTER.md` as state, §7.4a as the commit protocol — rather than re-plumbing it into a bespoke script. Same agent loop (bash, web fetch, git), no human in the loop. Alternatives: plain `cron` on a local/cloud box running the same `claude -p` call, or Claude Code Routines for clock-triggered runs. Cost for a nightly list of a few dozen names is single-digit dollars.

**Flow.**
1. Runner reads this file's queue section (mode + name).
2. Session-start: load PAT from secret, fetch live `MODEL.md` + `_REGISTER.md`.
3. Process each name **strictly sequentially** through the five-gate pipeline.
4. Commit each memo, then merge the register — one runner, sequential writes only.
5. Clear processed names from the queue; emit a JSON run summary (`--output-format json`, per-name verdict + `total_cost_usd`).

**Non-negotiable guardrails for unattended operation.**
- **Data-completeness gate.** If the inputs for the four CE variants / cheapness legs are not cleanly sourced, emit an `INCOMPLETE` stub memo flagged for human review and skip the verdict. Never fill a gap with an assumption to finish a row. This is what keeps the runner from laundering bad data into confident verdicts overnight.
- **Sequential register I/O.** No fan-out. Parallel jobs PUT-ing `_REGISTER.md` manufacture exactly the collisions §7.4a exists to catch. One runner, in order.
- **MODEL-mode lockout.** Runner handles ANALYSE / REVIEW / SWEEP only. Framework changes stay a human-only, exact-phrase "commit model" gate; runner has no write access to `instructions/`.
- Secrets (`ANTHROPIC_API_KEY`, PAT) as repo secrets, never in workflow files; `--allowedTools` scoped to EDGAR / Yahoo / GitHub.

**The real bottleneck is data, not scheduling.** The SEC-filer path is deterministic and safe to automate. The European and Japanese non-SEC names depend on primary-report PDF extraction — the fragile, judgment-heavy path where an unattended run is most likely to silently produce a wrong verdict. Harden those fetchers (or route them to `INCOMPLETE`) before trusting overnight output on this universe.

---

---

## Backlog — closure record

*Kept as a record of what was worked, not as a queue. Every name below carries a register row and a committed memo.*

- **Switzerland 13/13** (v2) · **Germany 30/30** (v2) · **Netherlands 3/3** (v2) · **Sweden 25/25** (v3) · **Italy 6/6** (v4) · **France 16/16** (v6) · **Japan majors 9/9** (v7).
- **Finland 4/4** (v8): NOKIA.HE, NESTE.HE, FORTUM.HE, AS.
- **Poland 6/6** (v8): PKN.WA, ALE.WA, ZAB.WA, DNP.WA, CDR.WA, ACP.WA.
- **United Kingdom 2/2** (v8): BA.L, HLN.L.
- **Denmark 3/3** (v8): ORSTED.CO, COLO-B.CO, ROCK-B.CO.
- **Brazil 2/2** (v8): NU, ABEV — the backlog's only all-WATCH block.
- **Energy 5/5** (v8): 300750.SZ, NEE, IBE.MC, EQNR, SRE — 0 WATCH; EQNR the near-miss, failed by P4 alone.
- **United States 72/72** (v8), closed across seven runs on 07–09 Aug 2026. Struck rather than analysed: **UDMY** and **OLPX** (dead listings), **ZM** (duplicate — row and memo already existed at v247).

---

## Flags — all resolved

- **"Cartara"** — ⚑ **RESOLVED BY ASSUMPTION → Certara (CERT)**, analysed 2026-08-09 (AVOID, two gates). No listing exists under the queue's spelling anywhere; the only near-match in the world is Cartiere Carrara, a private Italian tissue maker. **User confirmation owed** — if a different company was meant, the flag reopens and the CERT memo simply stands as an extra row.
- **Bed Bath & Beyond** — **RESOLVED BY EVIDENCE**, analysed 2026-08-09 as **BBBY** (AVOID, three gates). The 2023 Ch. 11 estate is dead; the brand IP went to Overstock.com, which renamed to Beyond, Inc. and then in Aug 2025 to Bed Bath & Beyond, Inc., reclaiming NYSE: BBBY. ⚠ A further rename to **Neighborhood Intelligence (Nasdaq: NXH)** is announced — key frozen at BBBY per §7.1a until effective; the re-key is a RECONCILE act, logged in the register change log.
- **Trigano** — RESOLVED at register v233 under §7.1a: Trigano keys `TRI.PA`, Thomson Reuters keeps the bare US key `TRI`.
- **Thin-history names** — the ⚠ convention retires with the queue; recent IPOs and spin-offs produced Past WEAK or record-limited windows exactly as expected (FIG 4y, PATH 6y, S 7y, MBLY 4y in this batch).

---

## Change log
- **v8 — 2026-08-09** — **THE ANALYSIS QUEUE IS CLOSED.** The 94-name v7 backlog is fully worked: 62 names committed at register v247 (Poland 6, US 07-Aug evening 6 + night 6, Finland 4, US 08-Aug 10 + evening 10 + night 10, Denmark 3, UK 2, US 09-Aug morning 9), and the final 29 in this commit (US afternoon 20, Brazil 2 + Energy 5, flag-resolution 2). Every market block is closed: Finland 4/4, Poland 6/6, UK 2/2, Denmark 3/3, Brazil 2/2, Energy 5/5, United States 72/72. Three flags actioned: **ZM** was a duplicate (row and memo already existed) and is struck; **Bed Bath & Beyond** resolved by evidence — the 2023 Ch. 11 estate is dead, the brand IP sits with the former Overstock.com, renamed Beyond, Inc. and then in Aug 2025 renamed Bed Bath & Beyond, Inc. reclaiming NYSE: BBBY — one analysable entity, analysed, AVOID on three gates, with a further rename to Neighborhood Intelligence (Nasdaq: NXH) pending as a RECONCILE re-key; **"Cartara"** resolved by assumption to **Certara (CERT)** — no listing exists under the queue's spelling, CERT is edit-distance 2 and sector-adjacent to its queue neighbours, analysed, AVOID on two gates — **the one residual token in this file is the user's confirmation that CERT was the intended name.** UDMY and OLPX were struck earlier as dead listings. The near-term calendar is **refreshed against register v248** — the staleness carried since v5 (register v173) is cleared. Only REVIEW work is now runnable; three dated re-tests fall within nine days of this commit (7936.T 14 Aug, TRI 18 Aug, STMN.SW 19 Aug, then INTU 21 Aug). **Re-seeding the ANALYSE queue is a user decision** — see "Priority" for the three candidate directions. v7 archived → `queue/archive/TODO_v7_2026-08-07.md`.
- **v7 — 2026-08-07** — **Japan majors CLOSED 9/9** (2026-08-07 cloud session): 7974.T Nintendo and 8002.T Marubeni **WATCH** (Marubeni the register's first sōgō shōsha, run on the §2·1A substitution rule); 6367.T Daikin, 6954.T Fanuc, 6702.T Fujitsu, 6301.T Komatsu, 3382.T Seven & i, 5108.T Bridgestone and 7751.T Canon **AVOID** — every one of the seven on Past WEAK, and 3382.T additionally on an SF FAIL flag pair (¥2tn criterion-free programme + the 2024–25 control-contest governance negative). Canon was the closest of the run at +133%. Block removed. 109 → 100 names. **US backlog opened as the ACTIVE BLOCK by assumption** (not user-set — redirectable, exactly as Japan was; rationale is the block's size and the overnight-runner note naming US SEC filers as the deterministic unattended path), and the first six ran the same day, all **AVOID**: LYFT and OPEN and LMND on three or two gates each, KVYO and TENB on Past WEAK with SF FAIL flag pairs, and **DLB the near-miss** — a bound-proof w-o-4 ROCE of 9.1–9.9% against the 10% floor, on a real ingrainedness moat at 13× FCF, which makes its **FY2026 10-K (~Nov 2026) window-roll the most interesting near-dated re-test in the file**. Four SF FAILs in six names: LMND and OPEN on P17 hard strikes (OPEN's is a $741m CEO package), KVYO and TENB on P17-plus-buyback pairs. 100 → **94 names**; US 78 → 72. All fifteen memos and register v246 committed in one batch on 2026-08-07. The near-term calendar section is **still stale** (reads against register v173) — RECONCILE refresh still owed, carried from v5/v6. v6 archived → `queue/archive/TODO_v6_2026-08-07.md`.
- **v6 — 2026-08-07** — France block continues: **ML.PA (Michelin) completed — AVOID, Past WEAK** (w-o-4 ROCE 8.39%, P4 fires on three straight declines; 5y record-limited because FY2017–20 statements are unretrievable). and **SW.PA (Sodexo) — AVOID on two gates** (w-o-4 ROCE 9.34% *and* three strong forces; 3y history-limited after the Pluxee spin; ⚠ FY2026 guidance removes the trigger band entirely). and **BVI.PA (Bureau Veritas) — WATCH**, the block's first (w-o-4 ROCE 15.15% but capped ADEQUATE by a 5y record-limited window; Future STRONG on a Government moat; capital allocation SOUND). and **FR.PA (Valeo) — AVOID on two gates** (w-o-4 ROCE 4.13%, the lowest of the register's seven automotive names; breadth FAILs on an arithmetic floor and the captive-customer waiver was tested and denied; no positive price clears EV/OI ≤7). and **MMB.PA (Lagardère) — AVOID on two gates** (w-o-4 ROCE 5.11% *and* L/E 980% past the P6 hard cap; three strong forces on segment-level calls; the first register name with **both** EV/OI bounds negative). and **TRI.PA (Trigano) — AVOID on Future alone** (Past ADEQUATE on w-o-4 ROCE 18.24%, cheapness **FAIR**, and **only +7.7% from its band** — the closest name in the whole register, WATCH or AVOID — but a 2-strong-force tally kills Future). **France is CLOSED 16/16 and the block is removed.** 118 → 112 names. **Japan majors opened**: 6501.T (Hitachi) — AVOID, Past WEAK at w-o-4 ROCE 8.42% on a *full* ten-year window (the divestment programme turned out not to restate the record), Gate 0 a near-fail carried only by the per-unit route. 7011.T (Mitsubishi Heavy) — AVOID on two gates, w-o-4 ROCE 5.11% and a P15 breadth FAIL on ≈22.9% MoD revenue, with the captive-customer waiver tested limb-by-limb and denied on the moat limb alone. 6752.T (Panasonic) — AVOID on two gates, w-o-4 ROCE 4.56% and three strong forces, with SF surviving **only because P20 is active** — the first name where the maintenance-capex basis decides shareholder-friendliness rather than the band. 118 → 109 names. ⚠ ML.PA raises a **MODEL item that blocks clean French analysis**: the as-reported-OI-line convention decided this verdict in the *opposite* direction from SGO.PA, so a label-based and a definition-based rule now give opposite economics on two French filers — see the register Open items. The near-term calendar section is still stale (register v173) and still needs a RECONCILE refresh. v5 to be archived → `queue/archive/TODO_v5_2026-08-06.md`.
- **v5 — 2026-08-06** — **P19 judgment re-test queue added** as a first-class work queue. Tier 1 closed 8/8 on 2026-08-06 — five flips to WATCH (6758.T, 7936.T, SOON.SW, STMN.SW, TRI), three ADVERSE holds (SU.PA, TER, WMT); Tier 2 reduced to AAPL, MA, DLG.MI, PSH.L after NOLA-B.ST and WISE.L ran the same day. France block pruned of 10 completed names (16 → 6). Trigano key collision recorded as resolved at register v233. 128 → 118 names. **The "Scheduled reviews — near-term calendar" section was NOT refreshed** — it still reads against register v173 and is stale; refresh at the next RECONCILE. v4 to be archived → `queue/archive/TODO_v4_2026-07-29.md`.
- **v4 — 2026-07-29** — Italy block completed 6/6 (MONC, 1913.HK, PIRC, BC, DLG all carry register rows at v173) → block removed. Priority switched to **France, in list order** (user-set). Calendar refreshed against register v173. 133 → 128 names. v3 archived → `queue/archive/TODO_v3_2026-07-28.md`.
