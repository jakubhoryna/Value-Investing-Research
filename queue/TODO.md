# GSC Analysis Queue — TODO.md (v6 · 2026-08-07)

**Purpose.** Backlog of names to run through the GSC pipeline — ANALYSE for names with no memo, REVIEW for existing ones. This file is *not* authoritative state: `_REGISTER.md` remains the single source of truth. Nothing here is a verdict or a recommendation; it is a work queue.

**Ticker discipline.** Tickers below are *suggested* primary listings for convenience only. They are **resolved and verified at analysis time** against the data-source hierarchy (SEC EDGAR / primary annual report / Yahoo), never trusted from this file. A wrong suggestion here costs nothing; a wrong verdict from bad data costs everything — so resolution + a data-completeness check happen per name at run time.

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

**Near-dated re-tests created by the 2026-08-06 batch** — the earliest points at which any of the five flips could revert: **7936.T Q2 tanshin 14 Aug 2026** (art. 459 board authority means a new programme can appear with no notice), **TRI NCIB expiry 18 Aug 2026** (renewal price decides), **STMN.SW H1-2026 19 Aug 2026** (treasury-share movement), **SOON.SW H1 FY26/27 ~Nov 2026** (successor programme), **6758.T H1 FY3/27 10 Nov 2026** (first completed half of the ¥500bn facility).

---

## Priority — next up

**France block, in list order** (user-set 2026-07-29) — **16 of 16 done — France block CLOSED**: OR.PA, RMS.PA, CDI.PA, EL.PA, DG.PA, BN.PA, SGO.PA, EDEN.PA, DEC.PA, LR.PA, ML.PA, SW.PA, BVI.PA, FR.PA, MMB.PA and TRI.PA all carry register rows. **Japan majors is the ACTIVE BLOCK** (assumption stated to the user, not user-set — redirectable at any point). In TODO list order: Hitachi ✅, Mitsubishi Heavy ✅, Panasonic ✅, then Nintendo (7974.T), Marubeni (8002.T), Daikin (6367.T), Fanuc (6954.T), Fujitsu (6702.T), Komatsu (6301.T), Seven & i (3382.T), Bridgestone (5108.T), Canon (7751.T). Other coherent blocks: US backlog (78), Poland (6), Finland (4), Denmark (3). The P19 re-test queue above is REVIEW work and runs alongside this ANALYSE block, not instead of it. Largest coherent blocks after France: US backlog (78), Japan majors (12), Poland (6).

*France note.* Six French names already carry register rows from earlier runs — SAF, SAN, MC.PA (LVMH), KER, DSY, SU — and are REVIEW territory, not part of this ANALYSE block. CDI.PA is a ~42% holding company over LVMH (MC.PA, analysed): expect the §2·1A securities-heavy-holdco substitution question at Gate 1A and a MCap/NAV anchor at Gate 2, not a re-underwrite of LVMH.

---

## Scheduled reviews — near-term calendar

*Refreshed 2026-07-29 against register v173 row cells and Open items — non-authoritative, the register wins; refresh at RECONCILE/SWEEP touches. Dated triggers only; price-alert triggers live in the rows.*

**Jul 2026 (imminent):** HEXA-B Q2 interim 29 Jul — first clean post-Octave basis, re-base Past + Cheapness · AMZN Q2 30 Jul (AWS growth/capex) · NKE FY2026 10-K re-anchor · INPST offer closed 27 Jul (settlement H2 → delist, archive row).
**Aug 2026:** ROK Q3 4 Aug opt. · NOVO-B H1 5 Aug (band only; held) · CROX Q2 6 Aug opt. (held) · CSG H1 7 Aug (FCF/leverage/Ammo+) · TEAM FY2026 10-K (OI inflection + P19) · BABA FY27 Q1 · ADYEN H1 · PAH3 H1 · BNR H1 opt. · BYD H1 opt. · GAP Q2 ~26 Aug.
**Sep 2026:** CRM Q2 FY27 ~2 Sep opt. · LULU Q2 (O'Neill's first quarter) · COST FY2026 P19 re-test (FY21–25 all >20×) · NKE proxy (Hill + Denton comp) · SAF H1 · ORCL Q1 FY27 · EA deal outside date 28 Sep (close → delist; lapse → REVIEW).
**Oct–Nov 2026:** MU 10-K ~Oct · AAPL 10-K ~Oct/Nov (SF comp flip check) · QCOM 10-K ~Nov (FY26 buyback re-test) · ROK 10-K ~Nov (buyback discipline) · V 10-K ~Nov (P15 11%-client + comp) · SONY H1 ~Nov (¥500bn facility, P19) · EKTA-B H1 ~Nov · SCHN repurchase-cessation watch (programme to Nov 2026).
**Dec 2026 / Q4 events:** ENR FY2026 AR (first clean-cycle year + P19 €2bn/€6bn) · SIE FY2026 (buyback re-test; Feb 2027 AGM spin vote → full re-base) · SKF-B Automotive Lex Asea separation ~Q4 (resets basis, both entities re-underwritten) · TKA / TUI1 FY2026 ARs informational.
**Q1–Q2 2027 — FY2026 annual season:** bulk of the WATCH list re-anchors (all four held names incl. HFG/NOVO-B decisions if still open) plus the named re-test queue — P19 dual-read (SCHN, GEBN, SAF, TER, MORN, GRMN, SU), acquisition-audit INDETERMINATEs (FIE Shopko, ASSA-B HHI, ESSITY-B BSN, GETI-B Paragonix, EPI-A Stanley, MYCR cohort, KRN Netstal), P4 third-decline tests (INDT, SKF-B), ONON arithmetic flip check, CON tyre re-basis, SHA0/BAYN P17 columns, MA comp (Apr 2027 proxy), worth-check flag-clears (CROX, BKNG, AD), PIRC control determination (Camfin–MPI agreement lapsed 28 Feb 2026), MONC FY2016–20 record rebuild (CDN-blocked, cap liftable) — **detail: register `## Open items`.**

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

## Backlog by market — 109 names remaining

Recent IPOs / spin-offs (thin public history) are marked ⚠ — the Past gate needs several years of data; these may auto-flag `INCOMPLETE` or Past = WEAK on insufficient history. *Completed markets removed: Switzerland (13/13), Germany (30/30), Netherlands (3/3) at v2; Sweden (25/25) at v3; Italy (6/6) at v4.*

### Finland — 4 remaining (Kone completed)
- Nokia — NOKIA.HE
- Neste — NESTE.HE
- Fortum — FORTUM.HE
- Amer Sports — AS (US)  ⚠ (2024 IPO)

### Japan — 9 remaining ◄ ACTIVE BLOCK (Sony, Hitachi, Mitsubishi Heavy and Panasonic completed; ASICS, Asahi, TOTO and Mitsubishi Electric also carry register rows)
- Nintendo — 7974.T
- Marubeni — 8002.T
- Daikin — 6367.T
- Fanuc — 6954.T
- Fujitsu — 6702.T
- Komatsu — 6301.T
- Seven & i Holdings (7-Eleven) — 3382.T
- Bridgestone — 5108.T
- Canon — 7751.T

### France — COMPLETE 16/16 as at v6 (Safran, Sanofi + LVMH, Kering, Dassault Systèmes, Schneider were already in the register). Block removed.

### Brazil
- Nu Holdings — NU (US)
- Ambev — ABEV (US ADR) / ABEV3.SA

### Poland
- Orlen — PKN.WA
- Allegro — ALE.WA
- Żabka — ZAB.WA  ⚠ (2024 IPO)
- Dino Polska — DNP.WA
- CD Projekt — CDR.WA
- Asseco Poland — ACP.WA

### United Kingdom — 2 remaining (Wise completed)
- BAE Systems — BA.L
- Haleon — HLN.L  (2022 GSK spin-off)

### United States — 78 remaining (Gen Digital, Unity, DocuSign completed; dup lines removed)
- Lyft — LYFT
- Lemonade — LMND
- Klaviyo — KVYO  ⚠ (2023 IPO)
- Opendoor — OPEN
- Dolby — DLB
- Tenable — TENB
- Waystar — WAY  ⚠ (2024 IPO)
- Bath & Body Works — BBWI
- Box — BOX
- Abercrombie & Fitch — ANF
- Warby Parker — WRBY  ⚠ (2021 direct listing)
- Fastly — FSLY
- Upstart — UPST
- Magnite — MGNI
- Sunrun — RUN
- Steve Madden — SHOO
- SoundHound AI — SOUN  ⚠ (thin history)
- Freshworks — FRSH
- Visteon — VC
- Grindr — GRND  ⚠ (2022 SPAC)
- Under Armour — UAA
- Chemours — CC
- Harley-Davidson — HOG
- Cohu — COHU
- Ducommun — DCO
- Peloton — PTON
- Calix — CALX
- Ingevity — NGVT
- Whirlpool — WHR
- Payoneer — PAYO
- Atkore — ATKR
- Coty — COTY
- Sonos — SONO
- Fortrea — FTRE  ⚠ (2023 Labcorp spin-off)
- Arteris — AIP  ⚠ (2021 IPO)
- Teladoc Health — TDOC
- Revolve Group — RVLV
- Coursera — COUR
- Tripadvisor — TRIP
- TriMas — TRS
- Enovis — ENOV
- Wendy's — WEN
- Carter's — CRI
- Olaplex — OLPX  ⚠ (2021 IPO)
- Winmark — WINA
- Ameresco — AMRC
- XPEL — XPEL
- Biglari Holdings — BH
- Arhaus — ARHS  ⚠ (2021 IPO)
- Azenta — AZTA
- "Cartara" — ⚑ unresolved (no known US listing under this spelling; confirm name/ticker)
- Cricut — CRCT
- Transcat — TRNS
- Hyliion — HYLN
- Ceribell — CBLL  ⚠ (2024 IPO)
- Udemy — UDMY
- Bed Bath & Beyond — ⚑ original bankrupt; brand now under Beyond Inc (BYON). Confirm which entity
- Unifi — UFI
- Arq — ARQ
- Palo Alto Networks — PANW
- CrowdStrike — CRWD
- Cloudflare — NET
- Snowflake — SNOW
- Datadog — DDOG
- Adobe — ADBE
- Intuit — INTU
- Workday — WDAY
- Twilio — TWLO
- Zoom — ZM
- Okta — OKTA
- Zebra Technologies — ZBRA
- Figma — FIG  ⚠ (2025 IPO)
- FactSet — FDS
- Compass — COMP
- Mobileye — MBLY  ⚠ (2022 IPO)
- Dropbox — DBX
- SentinelOne — S
- UiPath — PATH

### Energy
- CATL — 300750.SZ (Shenzhen); 2025 HK dual-listing
- NextEra Energy — NEE
- Iberdrola — IBE.MC
- Equinor — EQNR
- Sempra — SRE

### Denmark
- Ørsted — ORSTED.CO
- Coloplast — COLO-B.CO
- Rockwool — ROCK-B.CO

---

## Flags — confirm before analysis

- **"Cartara"** — no known US listing under this spelling; confirm intended name/ticker.
- **Bed Bath & Beyond** — original bankrupt; brand now under Beyond Inc (BYON). Confirm entity.
- **Trigano** — RESOLVED at register v233 under MODEL §7.1a (suffix-always for non-US lines): Trigano keys `TRI.PA`, Thomson Reuters keeps the bare US key `TRI`. No action needed at analysis time.
- **Thin-history names** (⚠ throughout) — recent IPOs/spin-offs may not clear the Past gate; expect `INCOMPLETE` or Past = WEAK on insufficient data.

---

## Change log
- **v6 — 2026-08-07** — France block continues: **ML.PA (Michelin) completed — AVOID, Past WEAK** (w-o-4 ROCE 8.39%, P4 fires on three straight declines; 5y record-limited because FY2017–20 statements are unretrievable). and **SW.PA (Sodexo) — AVOID on two gates** (w-o-4 ROCE 9.34% *and* three strong forces; 3y history-limited after the Pluxee spin; ⚠ FY2026 guidance removes the trigger band entirely). and **BVI.PA (Bureau Veritas) — WATCH**, the block's first (w-o-4 ROCE 15.15% but capped ADEQUATE by a 5y record-limited window; Future STRONG on a Government moat; capital allocation SOUND). and **FR.PA (Valeo) — AVOID on two gates** (w-o-4 ROCE 4.13%, the lowest of the register's seven automotive names; breadth FAILs on an arithmetic floor and the captive-customer waiver was tested and denied; no positive price clears EV/OI ≤7). and **MMB.PA (Lagardère) — AVOID on two gates** (w-o-4 ROCE 5.11% *and* L/E 980% past the P6 hard cap; three strong forces on segment-level calls; the first register name with **both** EV/OI bounds negative). and **TRI.PA (Trigano) — AVOID on Future alone** (Past ADEQUATE on w-o-4 ROCE 18.24%, cheapness **FAIR**, and **only +7.7% from its band** — the closest name in the whole register, WATCH or AVOID — but a 2-strong-force tally kills Future). **France is CLOSED 16/16 and the block is removed.** 118 → 112 names. **Japan majors opened**: 6501.T (Hitachi) — AVOID, Past WEAK at w-o-4 ROCE 8.42% on a *full* ten-year window (the divestment programme turned out not to restate the record), Gate 0 a near-fail carried only by the per-unit route. 7011.T (Mitsubishi Heavy) — AVOID on two gates, w-o-4 ROCE 5.11% and a P15 breadth FAIL on ≈22.9% MoD revenue, with the captive-customer waiver tested limb-by-limb and denied on the moat limb alone. 6752.T (Panasonic) — AVOID on two gates, w-o-4 ROCE 4.56% and three strong forces, with SF surviving **only because P20 is active** — the first name where the maintenance-capex basis decides shareholder-friendliness rather than the band. 118 → 109 names. ⚠ ML.PA raises a **MODEL item that blocks clean French analysis**: the as-reported-OI-line convention decided this verdict in the *opposite* direction from SGO.PA, so a label-based and a definition-based rule now give opposite economics on two French filers — see the register Open items. The near-term calendar section is still stale (register v173) and still needs a RECONCILE refresh. v5 to be archived → `queue/archive/TODO_v5_2026-08-06.md`.
- **v5 — 2026-08-06** — **P19 judgment re-test queue added** as a first-class work queue. Tier 1 closed 8/8 on 2026-08-06 — five flips to WATCH (6758.T, 7936.T, SOON.SW, STMN.SW, TRI), three ADVERSE holds (SU.PA, TER, WMT); Tier 2 reduced to AAPL, MA, DLG.MI, PSH.L after NOLA-B.ST and WISE.L ran the same day. France block pruned of 10 completed names (16 → 6). Trigano key collision recorded as resolved at register v233. 128 → 118 names. **The "Scheduled reviews — near-term calendar" section was NOT refreshed** — it still reads against register v173 and is stale; refresh at the next RECONCILE. v4 to be archived → `queue/archive/TODO_v4_2026-07-29.md`.
- **v4 — 2026-07-29** — Italy block completed 6/6 (MONC, 1913.HK, PIRC, BC, DLG all carry register rows at v173) → block removed. Priority switched to **France, in list order** (user-set). Calendar refreshed against register v173. 133 → 128 names. v3 archived → `queue/archive/TODO_v3_2026-07-28.md`.
- **v3 — 2026-07-28** — Prune after the Sweden run: PDX, NOLA-B, RUSTA, BILI-A completed → Sweden block removed (25/25 done). Ferrari (RACE) completed → Italy down to 5. Priority set to the Italy block in list order. 138 → 133 names. v2 archived → `queue/archive/TODO_v2_2026-07-25.md`.
- **v2 — 2026-07-25** — RECONCILE prune: 75 completed names removed (all of CH 13, DE 30, NL 3; SE 21; FI Kone; JP Sony; FR SAF+SAN; UK Wise; US GEN/U/DOCU + priority GEN/TER; dup lines dropped). 4 flags resolved (Uniper→UN0, INNIO→INIO, Synlab→SYAB DNAF, Covestro→1COV — all analysed). Trigano/TRI collision flagged. Added near-term review calendar (derived from register v149). 138 names remain. v1 archived → `queue/archive/TODO_v1_2026-07-15.md`.
- **v1 — 2026-07-15** — File created. Seeded with priority names (Gen Digital, Teradyne) + long backlog by market. Overnight-runner design sketch recorded for later build.
