# GSC Analysis Queue — TODO.md

**Purpose.** Backlog of names to run through the GSC pipeline — ANALYSE for names with no memo, REVIEW for existing ones. This file is *not* authoritative state: `_REGISTER.md` remains the single source of truth. Nothing here is a verdict or a recommendation; it is a work queue.

**Ticker discipline.** Tickers below are *suggested* primary listings for convenience only. They are **resolved and verified at analysis time** against the data-source hierarchy (SEC EDGAR / primary annual report / Yahoo), never trusted from this file. A wrong suggestion here costs nothing; a wrong verdict from bad data costs everything — so resolution + a data-completeness check happen per name at run time.

---

## Priority — next up

- Gen Digital — GEN (US)
- Teradyne — TER (US)

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

## Backlog by market

Recent IPOs / spin-offs (thin public history) are marked ⚠ — the Past gate needs several years of data; these may auto-flag `INCOMPLETE` or Past = WEAK on insufficient history.

### Switzerland
- Roche — ROG.SW
- Lindt & Sprüngli — LISN.SW
- Garmin — GRMN (US-listed, CH-domiciled)
- Schindler — SCHP.SW
- Sika — SIKA.SW
- Kühne + Nagel — KNIN.SW
- Geberit — GEBN.SW
- Straumann — STMN.SW
- Sonova — SOON.SW
- Logitech — LOGN.SW / LOGI (US)
- On Holding — ONON (US)
- Inficon — IFCN.SW
- HUBER+SUHNER — HUBN.SW

### Germany
- Thyssenkrupp — TKA.DE
- Schaeffler — SHA.DE
- Siemens Energy — ENR.DE
- Bayer — BAYN.DE
- BASF — BAS.DE
- Hochtief — HOT.DE
- Henkel — HEN3.DE
- Talanx — TLX.DE
- Fresenius — FRE.DE
- Hapag-Lloyd — HLAG.DE
- INNIO — ⚑ listing status uncertain (PE-owned; confirm public)
- Uniper — UN01.DE  ⚑ (listed as "Unipet" — read as Uniper; confirm)
- Traton — 8TRA.DE
- Beiersdorf — BEI.DE  (listed as "Baiersdorf")
- Knorr-Bremse — KBX.DE
- Continental — CON.DE
- Sartorius — SRT3.DE
- Covestro — 1COV.DE  ⚑ (Adnoc/XRG takeover in progress; confirm still analysable)
- Symrise — SY1.DE
- Brenntag — BNR.DE
- Hella (Forvia Hella) — HLE.DE
- Evonik Industries — EVK.DE
- flatexDEGIRO — FTK.DE
- Bechtle — BC8.DE
- Aumovio — AUV.DE  ⚠ (2025 Continental spin-off; thin history)
- TUI — TUI1.DE
- Krones — KRN.DE
- Fielmann — FIE.DE
- Bilfinger — GBF.DE
- Synlab — ⚑ likely delisted (Cinven take-private, 2024) — confirm before queueing

### Netherlands
- Philips — PHIA.AS
- Akzo Nobel — AKZA.AS
- Signify — LIGHT.AS

### Sweden
- Atlas Copco — ATCO-A.ST
- Sandvik — SAND.ST
- Ericsson — ERIC-B.ST
- Assa Abloy — ASSA-B.ST
- Epiroc — EPI-A.ST
- Alfa Laval — ALFA.ST
- Hexagon — HEXA-B.ST
- Essity — ESSITY-B.ST
- Lifco — LIFCO-B.ST
- Boliden — BOL.ST
- Evolution — EVO.ST
- SKF — SKF-B.ST
- Nordnet — SAVE.ST
- Indutrade — INDT.ST
- Klarna — KLAR (US)  ⚠ (2025 IPO)
- Avanza — AZA.ST
- Mycronic — MYCR.ST
- Getinge — GETI-B.ST
- Thule — THULE.ST
- Husqvarna — HUSQ-B.ST
- Electrolux — ELUX-B.ST
- Elekta — EKTA-B.ST
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

### Finland
- Nokia — NOKIA.HE
- Kone — KNEBV.HE
- Neste — NESTE.HE
- Fortum — FORTUM.HE
- Amer Sports — AS (US)  ⚠ (2024 IPO)

### Japan
- Hitachi — 6501.T
- Sony — 6758.T
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

### France
- L'Oréal — OR.PA
- Hermès — RMS.PA
- Safran — SAF.PA
- Sanofi — SAN.PA
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
- Trigano — TRI.PA

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

### United Kingdom
- BAE Systems — BA.L
- Haleon — HLN.L  (2022 GSK spin-off)
- Wise — WISE.L

### United States
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
- Gen Digital — GEN  (dup — see Priority)
- Unity Software — U
- Zebra Technologies — ZBRA
- Figma — FIG  ⚠ (2025 IPO)
- DocuSign — DOCU
- FactSet — FDS
- Compass — COMP
- Mobileye — MBLY  ⚠ (2022 IPO)
- Dropbox — DBX
- SentinelOne — S
- UiPath — PATH
- Upstart — UPST  (dup — appears twice in source list)

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

- **Uniper** (listed "Unipet") — read as UN01.DE; confirm.
- **INNIO** — confirm public listing (PE-owned).
- **Synlab** — likely delisted (Cinven take-private 2024); confirm before queueing.
- **Covestro** — XRG/Adnoc takeover in progress; confirm still analysable as a going independent name.
- **"Cartara"** — no known US listing under this spelling; confirm intended name/ticker.
- **Bed Bath & Beyond** — original bankrupt; brand now under Beyond Inc (BYON). Confirm entity.
- **Thin-history names** (⚠ throughout) — recent IPOs/spin-offs may not clear the Past gate; expect `INCOMPLETE` or Past = WEAK on insufficient data.

---

## Change log
- 2026-07-15 — File created. Seeded with priority names (Gen Digital, Teradyne) + long backlog by market. Overnight-runner design sketch recorded for later build.
