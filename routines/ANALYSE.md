# ANALYSE routine — one new name per run (MODEL §8.1 under §8.7)

**Schedule:** Sunday–Thursday at 21:30 and 23:30 Europe/Prague; weekend sprint Friday 18:00–23:40 at :00 and :40, Saturday hourly at :26 and :40, Sunday 00:00–07:40 at :00 and :40.
Weekdays 09:00–18:00 are routine-free and 02:00–06:00 is quiet outside the weekend sprint. These times must equal the live routine crons (MODEL §8.7 item 12).
**Branch:** `claude/gsc-analyse-{KEY}-{D}-{T}`. **PR title:** `GSC ANALYSE {KEY} {D} [running]`.

1. **Preflight** per `routines/README.md` §0.
2. **Pick.** No web work. A key qualifies when it passes all of these checks:
   - a. There is no `memos/{KEY}/` folder and no `archive/memos/{KEY}/` folder on `origin/main`.
   - b. No register row matches the **company name**. A queue line carries no ISIN, so this check is name-only; the ISIN check against memo front matter (and the `isin` column of `register.csv`) happens at §8.1 step 1 (step 5 below). Never match on the key alone.
   - c. The key isn't claimed (README §2).
   - d. No row for it is pending: there is no `queue/rows/*_{KEY}.md`, and no file in `queue/rows/` has a `DRAFT_QUEUE: {KEY} →` or `Group dependency: {KEY} →` line (exact key, then a space). This catches a merged run that re-keyed under §7.1a.
   - e. It isn't a held name, and it isn't in the queue header's excluded set.
   - f. `queue/TODO.md` has no item `` `{KEY}` — attended group build owed …`` (README §5: the build overran a routine run; Jakub deletes the item after the attended build).

   Check (c), (d), (e) and (f) first. A key that fails any of them is in flight or excluded: skip it silently and move on. Only a key that passes (c)–(f) but fails (a) or (b) is REVIEW territory: record it under `## Queue update` in this run's row file, note it in the run note, and move on. Never reorder or edit the queue or TODO; INTAKE owns both files.

   **Group dependencies first** (MODEL §2 Group dependencies; §8.7 item 6). Read the `queue/TODO.md` head block `▶ Group dependencies` top-down and take the first **unmarked** line — one without `[!]` (`[!] incomplete …`, `[!] stalled …`), and not a `parent re-run owed` line — whose key qualifies. A listed subsidiary or listed holding is analysed as a company in its own right: the run is an ordinary ANALYSE of that key, and its row carries no `DRAFT_QUEUE:` line. A dependency key that fails (a) records `Group dependency: {KEY} → memo exists`; one that fails (b) records `Group dependency: {KEY} → prior {KEY2}`, KEY2 being the matching register row's key. INTAKE then clears the line or rewrites it to KEY2 (INTAKE.md step 3); a stale memo is REVIEW's (priority 1c).

   **Then the queue.** Walk `queue/DRAFT_QUEUE.md` from the top and take the first `[ ]` line whose key qualifies. A queue key that fails (a) or (b) records `DRAFT_QUEUE: {that KEY} → [x] prior — REVIEW`.

   **Queue exhausted.** If no dependency line and no queue line qualifies, claim keyless: branch `claude/gsc-analyse-{D}-{T}`, title `GSC ANALYSE {D} [running]`. Write `queue/rows/{D}_{T}_ANALYSE.md` (`row_type: QUEUE`) only if there are prior markers to record, plus the run note. Finish the PR as `GSC ANALYSE {D} — queue exhausted` and stop.
3. **Claim** before any research (README §2).
4. **Orientation.** If `queue/evidence/{KEY}_draft-evidence_*.md` exists, read it for orientation only. Its verdicts are void, and every figure is re-derived from primaries under MODEL §4.
5. **Analyse.** Follow MODEL §8.1 steps 1–8 exactly, within the P14 ANALYSE budget, and produce the full §6 memo: front matter, a body within P13, and Appendices A–G.
   - **Key and unit, first.** One GET to the price endpoint for the §7.1a key's endpoint symbol (README §5 retrieval hints; a US class share's dot becomes a hyphen). Record `exchangeName`, `currency` and the instrument name: `currency` is the memo's `px_unit`, verbatim. A venue the endpoint does not serve (MODEL §7.1a, "Not served") → INCOMPLETE (data access: no price endpoint). A quote endpoint is uncounted under P14.
   - **Machine fields (MODEL §6.1, v4.5.0 with round 2).** The front matter carries every machine field, in the §6.1 order: `aliases`, `px`, `px_unit`, `px_date`, `trigger`, the three multiples, `trigger_basis`, the four averaged multiples (`mcap_fcf_3y`, `mcap_fcf_5y`, `ev_oi_3y`, `ev_oi_5y`), `lens`, `holding_keys`, `core_credit`, the core numbers (with `core_oi_3y`, `core_oi_5y`, `core_fcf_3y`, `core_fcf_5y` and `core_fcf_all`), the three reasons and `next_review_short`, with one-word enumerations.
     - `trigger` is the operative trigger, the no-cash bound: the lower of the FCF leg and the EV/OI no-cash leg (R10), on the credited legs where holdings are credited. `trigger_basis` is `no-cash`. At `trigger`, MCap/FCF ≤ 8.0 and EV/OI no-cash ≤ 7.0 hold and the binding one sits at its threshold (FI: the MCap/NI leg of the P25 band). `trigger_band` prints the trigger first and the all-cash bound beside it, labelled, as context.
     - `core_fcf` is CFO − maintenance capex (P20), and `core_fcf_basis` names the tier: `{period} CFO − maint. capex (disclosed|constructed|= all capex)`. `core_fcf_all` is the all-capex reading of the same period: never above `core_fcf`, and equal to it under `= all capex`.
     - `core_oi_basis` names the J1 line (MODEL §6.1 grammar), never an adjusted one. Only where the P28 test qualifies the latest fiscal year as a one-off down year (OI and FCF are tested separately) does a basis read an `FY####–FY#### avg` period tagged ` · down-year avg`; `core_oi` (or `core_fcf`) is then exactly the lower of its 3-year and 5-year averages.
     - Under FI, `core_oi`, `core_debt_eq`, `core_cash`, `core_oi_3y`, `core_oi_5y` and `core_fcf_all` are `n.m.`; `core_fcf` is the NI basis (`{period} NI basis`; the P1 average needs no tag, a P28 average carries ` · down-year avg`), and `core_fcf_3y` and `core_fcf_5y` are average NI.
     - A group's core numbers are its consolidated figures, captive finance arms and controlled listed subsidiaries inside, with the non-controlled holdings' income out. `core_credit` is Σ H at the buy line, taken from each holding's own current memo (never a market price), and `0` without holdings. `holding_keys` lists the subsidiaries' and holdings' memos actually read (`n.m.` if none).
     - The three reasons use the MODEL §7.1 vocabulary.
       - A group reason may carry one prefix, `unit` or `sub`. A weighted WEAK prints the reason of the heaviest-weighted WEAK part; a weighted ADEQUATE prints the caveat of the heaviest-weighted part carrying one. An ungradeable subsidiary or holding is `sub dependency`. A consolidated Past reason carries no prefix.
       - A Future ADEQUATE carried with a concentration flag prints its caveat (`customer conc.` or `supplier conc.`, R7). Every other ADEQUATE, and every STRONG, is `n.m.`.
       - `alignment`, `flag pair` and `inherited` appear only on an SF FAIL.
       - Where several reasons decide one grade, take the first failing one in the vocabulary's order (a failing `{x}% ROCE` level first); the memo body names the others.
     - The multiples and the averaged multiples must recompute from the core numbers and `core_credit` at `px` (§7.1b). `lint-memo` checks every rule here in step 7.
   - Front matter: `memo_date: {D}`, `model_version` as read at preflight, plus `produced_by: ROUTINE` and `run_base: {sha}`.
   - Step 1's identity check compares the company name and the resolved ISIN with the `company:` and `isin:` front matter of every memo file in `memos/*/` and `archive/memos/*/` (one grep over both trees). A match under a key with a current memo is a prior for that key. A match only in `archive/memos/{K}/`, with no `memos/{K}/`, is an integrity finding: treat {K} as the prior key and add `` `{K}` — archived memos without a current memo (ANALYSE {D}) `` under `## TODO additions`. Legacy memos without `isin:` are a gap to note, never a match. If a prior memo turns up under another key, stop the analysis: write a row file with `row_type: PRIOR` naming the prior key and `DRAFT_QUEUE: {KEY} → [x] prior — REVIEW` (a dependency pick: `Group dependency: {KEY} → prior {KEY2}`), and finish the PR as `GSC ANALYSE {KEY} {D} — prior found (REVIEW)`.
   - If §7.1a resolves a different key, name the memo and row file by the resolved key, and keep the queue update on the queue line's key.
   - **Gate 0 states the lens (MODEL §2 Gate 0, R4).** `lens:` is STD or FI; the test and its evidence are logged in Appendix C. The tests run in the order FI, too hard, STD.
     - **FI** only for a licensed bank or insurer, or the parent of a banking or insurance group supervised on a consolidated basis. It must publish a capital ratio covering ≥ 90% of consolidated total assets and have no material non-financial part.
     - **Too hard: Gate 0 FAIL, verdict DNAF, reason logged.** This covers:
       - (a) a bank or insurer that does not fit FI;
       - (b) a group with a material unit or controlled subsidiary that is a licensed insurer, or a licensed bank funded mainly by customer deposits, and is not a captive finance arm;
       - (c) total assets more than half unlisted non-controlled stakes, or securities that are neither cash-like (S1/S2) nor material listed holdings.

       The §6.4 memo states `Gate 0: FAIL — too hard: (a)`, `(b)` or `(c)` with its evidence.
     - **STD** for every other company, however financial the product.
     - A **captive finance arm** (R2) is a unit like any other: consolidated on STD, with its OI, assets and debt in, and no lens or capital-ratio test of its own. Appendix C logs the captive test (more than half of the book unrelated to the group's products means not captive).
     - No holding company is valued on NAV.
   - **Groups (MODEL §2 Group Gate 0, Group grades, Group dependencies; R3, R5, V14).** A group is a listed entity with two or more material units (P22), or with any material controlled listed subsidiary or material listed holding.
     - **Gate 0.** Write one group sentence, plus one six-parameter sentence for each material unit (a captive finance arm included), each material controlled listed subsidiary and each material listed holding. The last two come from their own current memos. The group is DNAF if a material unit fails, if a subsidiary's or holding's own memo is DNAF, or if material holdings form a cycle (A holds B, B holds A). A cycle never waits on a dependency.
     - **Grades.**
       - Past is graded once, never weighted: on the consolidated record (B1–B3), or, with material non-controlled listed holdings, on the look-through record (each STD holding's OI, maintenance-capex FCF, CE, liabilities, BV and TBV added per window year at the parent's share, from its own memo's B record; an FI, ungradeable or owed holding adds nothing). The consolidated record's own L/E (P5/P6), equity ≤ 0 and J6 findings bind: no holding lifts them (MODEL §2·1A Groups).
       - Each material unit's Future is graded in Appendix D. A listed subsidiary's or holding's Future comes from its own memo.
       - The group Future is the P29 weighted score: STRONG 3, ADEQUATE 2, WEAK 1. Weights are the latest-3-FY average OI (a unit's segment result after the J1 charges where the note allocates them; a non-controlled holding × the parent's economic share), or revenue for all parts if any base is ≤ 0 or undisclosed. STRONG is above 2.5 with no material part WEAK, and ADEQUATE above 1.5; a score on a cut-off takes the lower grade.
       - B4 prints every weight and S (`B4 Division table`). Parts carry grades, never verdicts.
     - **Dependency check, at Gate 0.** List the material controlled listed subsidiaries and listed holdings, and fix each one's key: the register row matching its company name or ISIN, else the §7.1a key of its primary line (one GET to the price endpoint, uncounted). Each needs a current memo: the one file in `memos/{HKEY}/`, dated on or after D minus 15 months and written under MODEL v4.5.0 or later (its `model_version`). An older-version memo is stale.
       - **Ungradeable.** A dependency whose `▶ Group dependencies` line is marked `[!]` (incomplete or stalled), or whose venue the price endpoint does not serve, counts WEAK with its weight in the weighted Future, adds nothing to the look-through Past and earns no credit (S3); its Future reason is `sub dependency`. The run goes on. A dependency whose own memo is DNAF is never ungradeable: the group is DNAF.
       - **Missing memo.** For any other dependency without a current memo, first grade what can be graded without it: Gate 0 for the units, the consolidated Past, the units' Futures and SF. Then apply verdict invariance. If a material unit fails Gate 0 or holdings form a cycle (DNAF), SF is FAIL, the Past is WEAK where no missing memo can move it (the consolidated Past when only controlled listed subsidiaries' memos are missing; otherwise the consolidated record's own L/E, equity or J6 finding, a guard no holding lifts), or the Future is WEAK even with every missing part at STRONG, the verdict cannot depend on the missing memo, so finish without it. (A controlled listed subsidiary sits inside the consolidated Past, which never waits for its memo; a missing holding adds nothing to the look-through record; the printed Future counts each missing part WEAK with its weight until its memo lands.) A missing holding then earns no credit, the band prints `credit owed`, and `holding_keys` lists only the memos read.
       - Otherwise stop: `INCOMPLETE (dependency: {HKEY})`. The row's `## Group dependency` names every such subsidiary or holding as `memo missing` or `memo stale {date}` (README §4, §5).
     - **Gate 2.**
       - A listed subsidiary stays consolidated. Its minority's claim enters EV at the higher of market value at `px_date` and book; Appendix F prints both.
       - A material non-controlled listed holding is credited at intrinsic value from its own memo, after tax, never at market price or NAV: its buy line inside the trigger legs (`core_credit`), its worth inside the worth reads, and its sell-line value inside the sell line. Appendix F prints the `Holding credits:` table.
     - **Budget.** A group build that cannot finish within the time budget is `INCOMPLETE (group build exceeds budget)`, with `` `{KEY}` — attended group build owed (ANALYSE {D}) `` under `## TODO additions`. The build covers B4 with its weights and S, one Appendix D block per material unit, the holding credits at the three yardsticks, and the NCI.
   - **Round-2 method steps (MODEL §8.1 steps 4–7; R1, R6, R7, R8, R9, R10).** The memo shows each of these (MODEL §6.2, §6.3); `lint-memo` checks the machine fields they feed:
     - **B1 and the P20 maintenance-capex build** for each fiscal year: the disclosed figure (a netted growth figure floored like the constructed one); else the constructed real-growth estimate, growth deflated by the higher of 3% and the year's home consumer-price inflation, floored at the D&A of the capex base, unavailable in a deal year without acquired-revenue disclosure (Appendix C shows k, each year's deflator and real growth, the growth capex and whether the floor bound); else all capex. B1 also carries the all-capex FCF beside it, and the 3-year and 5-year average OI and FCF. Every FCF test runs on maintenance-capex FCF; the all-capex reading is printed and never governs.
     - **The P28 one-off down-year test**, in Appendix F, whenever the latest fiscal year is below the lower of its 3-year and 5-year averages. For an impairment, write-down or restructuring, recovery needs operating evidence (OI before the named charges at or above the lower average, and interims at or above the last pre-down year's same periods); "the cause ended" serves a disruption only. In doubt, the latest year governs.
     - **The R7 concentration worksheet**, in Appendix D. A customer concentration (any payer above 10% of revenue, or silence for a business selling to organisations) or a supplier concentration is flagged. It is then either carried by a strong moat (all three conditions evidenced; Future capped at ADEQUATE, with the flag as its caveat) or called a STRONG force under P16. Funding concentration stays strict.
     - **Appendix E's worksheets.** The pay worksheet reads the hairiest number: every per-person total on every disclosed basis. Then the director worksheet, and the alignment worksheet: the P23 call from management's economic holding (disclaimed holdings excluded; ≥ 1% of shares, or worth ≥ 10× the hairiest number, ALIGNED; ≥ 3× WEAKLY), with pledges and sales recorded as facts, never flags. The SF ladder names the step that decided.
     - **The averaged readings** in §6 and Appendix F: MCap/FCF and EV/OI on the 3-year and 5-year averages, both EV variants.
     - **The trigger band**, with the no-cash bound first.
   - If Gate 0 fails, write the abbreviated memo (§6.4) with `lens:` as tested, or `n.m.`. That is a complete run, not INCOMPLETE.
   - If a gate or cheapness input is missing, apply the data-completeness gate (README §5, D3).
6. **Write:**
   - **Full or Gate-0 memo:**
     - the memo `memos/{KEY}/{KEY}_{D}_GSC.md`
     - the row file `queue/rows/{D}_{T}_ANALYSE_{KEY}.md` (README §4), including `DRAFT_QUEUE: {KEY} → [x]` (a dependency pick has no queue line: INTAKE clears its `▶ Group dependencies` line when the memo lands); its `## Register row (new)` is pasted from `python3 routines/tools/gsc_register.py row-from-memo memos/{KEY}/{KEY}_{D}_GSC.md --table`
     - a deletion of this name's `queue/evidence/{KEY}_*.md` files (draft evidence and any earlier INCOMPLETE note), if any exist
     - the final run note
   - **INCOMPLETE:**
     - `queue/evidence/{KEY}_{D}_INCOMPLETE.md`
     - the row file with `row_type: INCOMPLETE` (with `## Group dependency` for a dependency gap, and the `attended group build owed` TODO addition for a budget overrun)
     - the final run note

     Keep `queue/evidence/{KEY}_draft-evidence_*.md`. Only a full or Gate-0 memo deletes it.
7. **Re-measure compliance** (README §5, including `python3 routines/tools/gsc_register.py lint-memo memos/{KEY}/{KEY}_{D}_GSC.md` for a memo), commit (`GSC: {KEY} v1 {VERDICT}`, or `GSC: {KEY} INCOMPLETE`), push, and finish the PR (README §1) as `GSC ANALYSE {KEY} {D} — {VERDICT} ({deciding gate})`, or `— INCOMPLETE ({named gap})`. A BUY sends one `BUY` push (README §5); every other ANALYSE outcome reaches Jakub through the morning digest, and gsc-automerge merges WATCH, AVOID, DNAF, INCOMPLETE, prior found and queue exhausted (MODEL §8.7 item 10).
8. **Stop.** One name per run.

**Forbidden:**
- a second name
- any edit to `_REGISTER.md`, `queue/TODO.md`, `queue/DRAFT_QUEUE.md` or `queue/IDEAS.md`
- any zone, ADD or SELL-FLAG statement (held names never enter this job)
- any path under `archive/` (ANALYSE never moves or archives a memo)
- any change to a locked path

*Framework output, not investment advice.*
