# GSC Analysis Queue — TODO.md (v2 · 2026-07-25)

**Purpose.** Backlog of names to run through the GSC pipeline — ANALYSE for names with no memo, REVIEW for existing ones. This file is *not* authoritative state: `_REGISTER.md` remains the single source of truth. Nothing here is a verdict or a recommendation; it is a work queue.

**Ticker discipline.** Tickers below are *suggested* primary listings for convenience only. They are **resolved and verified at analysis time** against the data-source hierarchy (SEC EDGAR / primary annual report / Yahoo), never trusted from this file. A wrong suggestion here costs nothing; a wrong verdict from bad data costs everything — so resolution + a data-completeness check happen per name at run time.

---

## Priority — next up

*(empty — GEN and TER completed; user to set the next batch. Largest coherent remaining blocks: Japan majors (12), France (16), US backlog (~77).)*

---

## Scheduled reviews — near-term calendar

*Derived 2026-07-25 from register v149 row cells and Open items — non-authoritative, the register wins; refresh at RECONCILE/SWEEP touches. Dated triggers only; price-alert triggers live in the rows.*

**Jul 2026 (imminent):** NKE FY2026 10-K re-anchor · INPST offer closes 27 Jul (settlement H2 → delist, archive row) · AMZN Q2 30 Jul (AWS growth/capex).
**Aug 2026:** ROK Q3 4 Aug opt. · NOVO-B H1 5 Aug (band only; held) · CROX Q2 6 Aug opt. (held) · CSG H1 7 Aug (FCF/leverage/Ammo+) · TEAM FY2026 10-K (OI inflection + P19) · BABA FY27 Q1 · ADYEN H1 · PAH3 H1 · BNR H1 opt. · BYD H1 opt. · GAP Q2 ~26 Aug.
**Sep 2026:** CRM Q2 FY27 ~2 Sep opt. · LULU Q2 (O'Neill's first quarter) · COST FY2026 P19 re-test (FY21–25 all >20×) · NKE proxy (Hill + Denton comp) · SAF H1 · ORCL Q1 FY27 · EA deal outside date 28 Sep (close → delist; lapse → REVIEW).
**Oct–Nov 2026:** MU 10-K ~Oct · AAPL 10-K ~Oct/Nov (SF comp flip check) · QCOM 10-K ~Nov (FY26 buyback re-test) · ROK 10-K ~Nov (buyback discipline) · V 10-K ~Nov (P15 11%-client + comp) · SONY H1 ~Nov (¥500bn facility, P19) · EKTA-B H1 ~Nov · SCHN repurchase-cessation watch (programme to Nov 2026).
**Dec 2026 / Q4 events:** ENR FY2026 AR (first clean-cycle year + P19 €2bn/€6bn) · SIE FY2026 (buyback re-test; Feb 2027 AGM spin vote → full re-base) · SKF-B Automotive Lex Asea separation ~Q4 (resets basis, both entities re-underwritten) · TKA / TUI1 FY2026 ARs informational.
**Q1–Q2 2027 — FY2026 annual season:** bulk of the WATCH list re-anchors (all four held names incl. HFG/NOVO-B decisions if still open) plus the named re-test queue — P19 dual-read (SCHN, GEBN, SAF, TER, MORN, GRMN, SU), acquisition-audit INDETERMINATEs (FIE Shopko, ASSA-B HHI, ESSITY-B BSN, GETI-B Paragonix, EPI-A Stanley, MYCR cohort, KRN Netstal), P4 third-decline tests (INDT, SKF-B), ONON arithmetic flip check, CON tyre re-basis, SHA0/BAYN P17 columns, MA comp (Apr 2027 proxy), worth-check flag-clears (CROX, BKNG, AD) — **detail: register `## Open items`.**

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

## Backlog by market — 138 names remaining

Recent IPOs / spin-offs (thin public history) are marked ⚠ — the Past gate needs several years of data; these may auto-flag `INCOMPLETE` or Past = WEAK on insufficient history. *Completed markets removed at v2: Switzerland (13/13), Germany (30/30), Netherlands (3/3).*

### Sweden — 4 remaining (21 completed at v2)
- Paradox Interactive — PDX.ST
- Nolato — NOLA-B.ST
- Rusta — RUSTA.ST
- Bilia — BILI-A.ST

### Italy
- Ferrari — RACE (US) / RACE.MI
- Moncler — MONC.MI
- Prada — 1913.HK (Hong Kong-listed)
- Pirelli — PIRC.MI
- Brunello Cucinelli — BC.MI
- De'Longhi — DLG.MI

### Finland — 4 remaining (Kone completed)
- Nokia — NOKIA.HE
- Neste — NESTE.HE
- Fortum — FORTUM.HE
- Amer Sports — AS (US)  ⚠ (2024 IPO)

### Japan — 12 remaining (Sony completed)
- Hitachi — 6501.T
- Mitsubishi Heavy Industries — 7011.T
- Panasonic — 6752.T
- Nintendo — 7974.T
- Marubeni — 8002.T
- Daikin — 6367.T
- Fanuc — 6954.T
- Fujitsu — 6702.T
- Komatsu — 6301.T
- Seven & i Holdings (7-Eleven) — 3382.T
- Bridgestone — 5108.T
- Canon — 7751.T

### France — 16 remaining (Safran, Sanofi completed)
- L'Oréal — OR.PA
- Hermès — RMS.PA
- Christian Dior — CDI.PA
- EssilorLuxottica — EL.PA
- Vinci — DG.PA
- Danone — BN.PA
- Saint-Gobain — SGO.PA
- Legrand — LR.PA
- Michelin — ML.PA
- Sodexo — SW.PA
- Edenred — EDEN.PA
- JCDecaux — DEC.PA
- Bureau Veritas — BVI.PA
- Valeo — FR.PA
- Lagardère — MMB.PA
- Trigano — TRI.PA  ⚑ ticker collision: register key `TRI` = Thomson Reuters — use a distinct register key (e.g. `TRI.PA`) at analysis time

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
- **Trigano** — TRI.PA; register key `TRI` is taken by Thomson Reuters — assign a distinct key at analysis time.
- **Thin-history names** (⚠ throughout) — recent IPOs/spin-offs may not clear the Past gate; expect `INCOMPLETE` or Past = WEAK on insufficient data.

---

## Change log
- **v2 — 2026-07-25** — RECONCILE prune: 75 completed names removed (all of CH 13, DE 30, NL 3; SE 21; FI Kone; JP Sony; FR SAF+SAN; UK Wise; US GEN/U/DOCU + priority GEN/TER; dup lines dropped). 4 flags resolved (Uniper→UN0, INNIO→INIO, Synlab→SYAB DNAF, Covestro→1COV — all analysed). Trigano/TRI collision flagged. Added near-term review calendar (derived from register v149). 138 names remain. v1 archived → `queue/archive/TODO_v1_2026-07-15.md`.
- **v1 — 2026-07-15** — File created. Seeded with priority names (Gen Digital, Teradyne) + long backlog by market. Overnight-runner design sketch recorded for later build.
