# GSC DRAFT QUEUE — DRAFT_QUEUE.md (v4 · 2026-10-04)

**Operative copy: this file (MODEL §8.7).** It is written only by INTAKE, from merged row and proposal files, and versioned: each outgoing version is archived to `queue/archive/DRAFT_QUEUE_v{n}_{date}.md` (MODEL §7.5). Runs claim a key by PR title (`GSC ANALYSE {KEY} {D} [running]`), never by editing lines. Jakub edits by hand, in an attended commit, only to reset a line, strike it, or add `retry`. The claude.ai project copy, if any, is a read-only mirror.

**Rules (MODEL §8.7; `routines/ANALYSE.md` holds the pick logic).** One name per ANALYSE run: the first eligible `[ ]` line, top-down. Held names never enter. Never reorder; restock lines are appended below the last line. A marker replaces only the line's leading token; the rest of the line (`KEY — Company — route — notes`) stays. Dates are Europe/Prague run dates. Markers:
- `[ ]` open
- `[x] {D}` done — memo merged and applied
- `[x] prior — REVIEW` — a prior memo exists; REVIEW territory
- `[-] rejected {D} (PR #n)` — Jakub closed the ANALYSE PR unmerged
- `[!] incomplete {D} — {path}` — the data-completeness gate stopped the run; `{path}` is the INCOMPLETE evidence file
- `[!] stalled {D} (PR #a, #b)` — abandoned twice within 14 days; skipped until Jakub edits the line

A trailing `retry` (added by Jakub) makes a reset `[ ]` line eligible despite an earlier rejection.

**Seeding basis (2026-09-13).** §7.1a prior-check on key against live register v296 (322 rows): none of the keys below has a row. Sources: `queue/TODO.md` v34 block C1 (evidence file `queue/evidence/<KEY>_draft-evidence_2026-09.md` — **orientation only; its verdicts are void and every figure re-derives from primaries under §4**) and block C2 (no research). Keys are suggested §7.1a keys, resolved with company name + ISIN at run time. **Excluded from routine ANALYSE by design:** `.KS` names (primaries bot-blocked from the sandbox); suffix-gap markets `.NS` `.IR` `.LS` `.SR` `.AE` `.BD` (framework change pending); §2·1A / captive-finance names — `KGX.DE`, `JUN3.DE`, `BG.VI`, `AVARDA.ST`, the automakers (IDEAS A2 open — attended sessions only); `VALMT.HE` (segment-separation review to FY2026 results); `CHG.DE` (Gate 0 form question); `.SZ` mainland names (governance check first); sub-€200m micro-caps.

**Ordering.** Retrieval reliability in the cloud sandbox first (SEC filers → Japan via the kabupro EDINET mirror → issuers with verified IR stores), thesis fit second, consumer/media last. Notes are carry-over facts to check first, not findings.

## Queue

- [x] 2026-10-04 CGNX — Cognex Corporation — US SEC filer (10-Q / 8-K-exhibit route) — evidence file; machine vision
- [x] 2026-10-04 SYM — Symbotic Inc. — US SEC filer — evidence file; Walmart ≈85% of FY2025 revenue (primary) → customer-breadth test decisive; GreenBox JV related-party backlog → RPT/consolidation read
- [x] 2026-10-04 PTC — PTC Inc. — US SEC filer — no evidence; verify listing/corporate actions first; PLM/IIoT — the register has no manufacturing-software benchmark
- [x] 2026-10-04 6383.T — Daifuku Co., Ltd. — Japan (kabupro EDINET) — evidence file; intralogistics
- [x] 2026-10-04 6268.T — Nabtesco Corporation — Japan — evidence file; H1 PBT-vs-OI gap unexplained in the draft — resolve from the tanshin/yūhō
- [x] 2026-10-04 6324.T — Harmonic Drive Systems — Japan — evidence file; impairment year in the record (no add-backs, §2·1A); Nabtesco is the paired name
- [x] 2026-10-04 3064.T — MonotaRO Co., Ltd. — Japan — evidence file; W.W. Grainger anchor stake not sourced in the drafts — source it, carry as control caveat
- [x] 2026-10-04 7309.T — Shimano Inc. — Japan — evidence file incl. ERRATA section; reform-theme buyback record = P19 evidence
- [x] 2026-10-04 6841.T — Yokogawa Electric Corp. — Japan — no evidence; tanshin on the company store (verified 9 Sep 2026); pure process-automation platform
- [x] 2026-10-04 6845.T — Azbil Corp. — Japan — no evidence; verify listing; three-segment Gate 0 split
- [x] 2026-10-04 KCR.HE — Konecranes Plc — Finland — evidence file; AGM 26 Mar 2026 bonus issue (two new per one existing; count ×3) — check every per-share series for basis; read with KALMAR.HE
- [x] 2026-10-04 METSO.HE — Metso Oyj — Finland — no evidence; H1 2026 report 24 Jul 2026 (verified); direct peer to SAND.ST / EPI-A.ST (both WATCH)
- [x] 2026-10-04 KALMAR.HE — Kalmar Corporation — Finland — evidence file; demerged from Cargotec 2024 → history-limited label; class A/B votes unverified
- [x] 2026-10-04 INRN.SW — Interroll Holding AG — Switzerland — evidence file; Royal Apollo consideration undisclosed at announcement (Gate 1C)
- [!] incomplete 2026-10-04 — queue/evidence/KARN.SW_2026-10-04_INCOMPLETE.md KARN.SW — Kardex Holding AG — Switzerland — evidence file; check the 2025 write-off line; H1 2026 segment EBIT split owed
- [x] 2026-10-04 G1A.DE — GEA Group AG — Germany — evidence file; process equipment
- [x] 2026-10-04 ANDR.VI — ANDRITZ AG — Austria — evidence file; plant engineering, service
- [x] 2026-10-04 SUN.SW — Sulzer AG — Switzerland — evidence file (**read its last section first** — an 8 Sep re-read reversed an errata on the FY series)
- [x] 2026-10-04 RSW.L — Renishaw plc — UK — evidence file; metrology; quote in pence, reports GBP
- [x] 2026-10-04 RHIM.L — RHI Magnesita N.V. — UK line, Dutch N.V. — evidence file; refractories
- [x] 2026-10-04 WEIR.L — Weir Group plc — UK — no evidence; H1 to 30 Jun 2026 (verified); Metso peer
- [x] 2026-10-04 HMS.ST — HMS Networks AB — Sweden — no evidence; listing verified; acquisition intensity is the Gate 1C question
- [x] 2026-10-04 NMAN.ST — Nederman Holding AB — Sweden — no evidence; listing verified; filtration + connected aftermarket
- [x] 2026-10-04 ALIG.ST — Alimak Group AB — Sweden — evidence file; aftermarket share unauditable from disclosure per draft
- [x] 2026-10-04 MIPS.ST — Mips AB — Sweden — evidence file; licensee concentration = P15 breadth test; royalty model
- [!] incomplete 2026-10-04 — queue/evidence/PAL.VI_2026-10-04_INCOMPLETE.md PAL.VI — Palfinger AG — Austria — evidence file; company-disclosed ROCE is not the framework's — rebuild
- [x] 2026-10-04 FQT.VI — Frequentis AG — Austria — evidence file (primary-sourced dossier sections)
- [x] 2026-10-04 IP.MI — Interpump Group S.p.A. — Italy — evidence file; serial acquirer (FY25 organic −0.7% vs +2.3% acquired) → Gate 1C audit
- [x] 2026-10-04 AUTO.OL — AutoStore Holdings — Norway — evidence file; IPO Oct 2021 → history-limited; goodwill+intangibles ≈95% of equity, TBV negative
- [x] 2026-10-04 BRG.OL — Borregaard ASA — Norway — evidence file; wood-based biochemicals
- [x] 2026-10-04 CRL.MI — CAREL Industries S.p.A. — Italy — evidence file is `[secondary]` only; IR file server returns unparseable binary — expect §4 gaps, label them; Cotes consideration undisclosed
- [x] 2026-10-04 DGE.L — Diageo plc — UK — evidence file; quote in pence, reports USD (state FX rate + date); FY26 dividend cut
- [x] 2026-10-04 HEIA.AS — Heineken N.V. — Netherlands — evidence file; key the operating company, not the HEIO.AS holding vehicle
- [x] 2026-10-04 CARL-B.CO — Carlsberg A/S — Denmark — evidence file; Britvic (2025) → Gate 1C audit; hybrid capital in L/E; Foundation control
- [x] 2026-10-04 RBREW.CO — Royal Unibrew A/S — Denmark — evidence file; issued 49,300,000 / treasury 1,236,387 (Ann. 32/2026); PepsiCo-licence EBIT share undisclosed
- [x] 2026-10-04 RI.PA — Pernod Ricard SA — France (FY June) — evidence file; Brown-Forman approach 26 Mar 2026, terminated 28 Apr 2026 — the draft omits it; carry as a corporate action
- [x] 2026-10-04 RCO.PA — Rémy Cointreau SA — France (FY March) — evidence file; Orpar/Andromède family control; US duty + China minimum-price agreement
- [x] 2026-10-04 CPR.MI — Davide Campari-Milano N.V. — Italy — evidence file; Lagfin loyalty-share control claimed but unverified — read the articles
- [x] 2026-10-04 RRTL.DE — RTL Group S.A. — Germany line — evidence file; Bertelsmann ~75%; Sky Deutschland contingent consideration belongs in EV
- [x] 2026-10-04 VSURE.ST — Verisure plc — Sweden — evidence file; IPO Oct 2025 → history-limited; PE-era leverage; capitalised subscriber-acquisition cost is the CE/FCF question
- [!] incomplete 2026-10-04 — queue/evidence/ACAST.ST_2026-10-04_INCOMPLETE.md ACAST.ST — Acast AB — Sweden — evidence file; short listed history; loss-making years → P17 loss-leg logic
- [x] 2026-10-04 KEYS — Keysight Technologies, Inc. — US SEC filer — re-seed universe; electronic test & measurement, RF/comms test standard, software + calibration pull (TODO v36 L554)
- [x] 2026-10-04 MTD — Mettler-Toledo International Inc. — US SEC filer — re-seed universe; precision weighing & lab instruments, installed base + service annuity, very long record (TODO v36 L555)
- [x] 2026-10-04 AME — AMETEK, Inc. — US SEC filer — re-seed universe; electronic instruments & electromechanical; bolt-ons funded from internal cash → acquisition audit (TODO v36 L583)
- [x] 2026-10-04 NDSN — Nordson Corporation — US SEC filer — re-seed universe; precision dispensing, parts-and-consumables pull-through on installed base (TODO v36 L566)
- [x] 2026-10-04 GGG — Graco Inc. — US SEC filer — re-seed universe; fluid handling equipment, distributor lock-in, long record (TODO v36 L565)
- [x] 2026-10-04 IEX — IDEX Corporation — US SEC filer — re-seed universe; fluidics & health/science niches; decentralised acquirer → acquisition audit (TODO v36 L584)
- [x] 2026-10-04 DOV — Dover Corporation — US SEC filer — re-seed universe; diversified decentralised industrial, consumables-weighted mix; multi-segment Gate 0 (TODO v36 L582)
- [x] 2026-10-04 TDY — Teledyne Technologies Incorporated — US SEC filer — re-seed universe; instrumentation & digital sensing; acquirer that deleverages after deals (TODO v36 L586)
- [x] 2026-10-04 DCI — Donaldson Company, Inc. — US SEC filer — re-seed universe; filtration & replacement filters, aftermarket annuity, multi-decade statements (TODO v36 L567)
- [x] 2026-10-04 BMI — Badger Meter, Inc. — US SEC filer — re-seed universe; flow measurement & water metering, replacement-cycle demand (TODO v36 L556)
- [x] 2026-10-04 NOVT — Novanta Inc. — US SEC filer — re-seed universe; photonics & precision motion, designed-in OEM components (TODO v36 L551)
- [x] 2026-10-04 WWD — Woodward, Inc. — US SEC filer — re-seed universe; energy control & motion, sole-source positions, aftermarket pull (TODO v36 L562)
- [x] 2026-10-04 LECO — Lincoln Electric Holdings, Inc. — US SEC filer — re-seed universe; welding equipment & consumables, consumables attach rate (TODO v36 L572)
- [x] 2026-10-04 FAST — Fastenal Company — US SEC filer — re-seed universe; fastener & MRO distribution, onsite/vending model (TODO v36 L575)
- [x] 2026-10-04 SNA — Snap-on Incorporated — US SEC filer — re-seed universe; professional tools & diagnostics, franchised van channel (TODO v36 L573)
- [x] 2026-10-04 HEI — HEICO Corporation — US SEC filer — re-seed universe; aerospace aftermarket parts; family-controlled dual-class acquirer → acquisition audit, key the class priced (TODO v36 L585)
- [x] 2026-10-04 WTS — Watts Water Technologies, Inc. — US SEC filer — re-seed universe; flow control valves, replacement demand; dual-class family voting control (TODO v36 L569)
- [x] 2026-10-04 CAT — Caterpillar Inc. — US SEC filer — coverage audit Tier A (rank #39); construction & mining equipment; verify listing/corporate actions first (TODO v36 L405)
- [x] 2026-10-04 APH — Amphenol Corporation — US SEC filer — coverage audit Tier A (rank #97); connectors & interconnect; verify listing/corporate actions first (TODO v36 L428)
- [x] 2026-10-04 TXN — Texas Instruments Incorporated — US SEC filer — coverage audit Tier A (rank #73); analog semiconductors; verify listing/corporate actions first (TODO v36 L419)
- [x] 2026-10-04 6861.T — Keyence — Japan (kabupro EDINET) — C2; factory automation, core-thesis name; runs' "expensive on sight" drop is not a queue exclusion; verify listing/corporate actions first (TODO v36 L194)
- [x] 2026-10-04 6273.T — SMC — Japan (kabupro EDINET) — C2; pneumatics, core-thesis name; verify listing/corporate actions first (TODO v36 L194)
- [x] 2026-10-04 6645.T — Omron — Japan (kabupro EDINET) — C2; automation, core-thesis name; multi-segment Gate 0; verify listing/corporate actions first (TODO v36 L194)
- [x] 2026-10-04 6506.T — Yaskawa — Japan (kabupro EDINET) — C2; robotics/drives, core-thesis name; peer to 6954.T FANUC row; verify listing/corporate actions first (TODO v36 L194)
- [ ] LSS.PA — Lectra SA — France — C2; Industry-4.0 cutting rooms + SaaS, installed base + recurring; listed, H1 report 30 Jul 2026 (verified) (TODO v36 L171)
- [ ] SPX.L — Spirax Group plc — UK — re-seed universe; thermal energy / niche pumps, installed steam base drives aftermarket (TODO v36 L479)
- [ ] HLMA.L — Halma plc — UK — re-seed universe; safety & environmental tech, decentralised regulation-driven niches (TODO v36 L480)
- [ ] IMI.L — IMI plc — UK — re-seed universe; flow control & automation, engineered components, aftermarket pull-through (TODO v36 L481)
- [ ] DPLM.L — Diploma PLC — UK — re-seed universe; value-added industrial distribution, sticky specification, bolt-ons → acquisition audit (TODO v36 L484)
- [ ] OXIG.L — Oxford Instruments plc — UK — re-seed universe; scientific instruments, research niches with service annuity (TODO v36 L496)
- [ ] BNZL.L — Bunzl plc — UK — re-seed universe; outsourced business supplies, consolidator of a fragmented category (TODO v36 L485)
- [ ] REL.L — RELX PLC — UK — re-seed universe; professional information & analytics, subscription embedded in workflow (TODO v36 L489)
- [ ] EXPN.L — Experian plc — UK — re-seed universe; credit data & analytics, reciprocal-data bureau network effects (TODO v36 L488)
- [ ] CNR.TO — Canadian National Railway Company — Canada — re-seed universe; rail freight duopoly network, decades of statements (TODO v36 L510)
- [ ] TIH.TO — Toromont Industries Ltd. — Canada — re-seed universe; equipment distribution & services, protected CAT dealer territory, parts-and-service (TODO v36 L512)
- [ ] CCL.B.TO — CCL Industries Inc. — Canada — re-seed universe; specialty packaging & labels; Lang-family controlled serial acquirer → acquisition audit, control caveat (TODO v36 L519)
- [ ] COH.AX — Cochlear Limited — Australia — re-seed universe; implantable medical devices, installed base + processor upgrades (TODO v36 L537)
- [ ] BXB.AX — Brambles Limited — Australia — re-seed universe; pallet pooling, scale network, understandable unit economics (TODO v36 L538)
- [ ] TNE.AX — TechnologyOne Limited — Australia — re-seed universe; public-sector enterprise software, founder-anchored, net cash (TODO v36 L540)
- [ ] REH.AX — Reece Limited — Australia — re-seed universe; plumbing & HVAC distribution, Wilson-family control (TODO v36 L533)

*QUEUE-SEED restocks when fewer than 10 unclaimed lines remain; INTAKE appends merged restock lines above this note. Never restock from the named re-test backlog — those are REVIEWs.*
