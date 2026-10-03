# ANALYSE routine — one new name per run (MODEL §8.1 under §8.7)

**Schedule:** daily at 12:50, 17:50 and 22:50 Europe/Prague. During the burn-in week it runs only at 22:50.
**Branch:** `claude/gsc-analyse-{KEY}-{D}-{T}`. **PR title:** `GSC ANALYSE {KEY} {D} [running]`.

1. **Preflight** per `routines/README.md` §0.
2. **Pick.** No web work. Walk `queue/DRAFT_QUEUE.md` from the top. Take the first `[ ]` line whose key passes all of these checks:
   - a. There is no `memos/{KEY}/` folder on `origin/main`.
   - b. No register row matches the **company name**. The register has no ISIN column, so this check is name-only; the ISIN check against memo front matter happens at §8.1 step 1 (step 5 below). Never match on the key alone.
   - c. The key isn't claimed (README §2).
   - d. No row for it is pending: there is no `queue/rows/*_{KEY}.md`, and no file in `queue/rows/` has a `DRAFT_QUEUE: {KEY} →` line (exact key, then a space). This catches a merged run that re-keyed under §7.1a.
   - e. It isn't a held name, and it isn't in the queue header's excluded set.

   Check (c), (d) and (e) first. A key that fails any of them is in flight or excluded: skip it silently and move to the next line. Only a key that passes (c), (d) and (e) but fails (a) or (b) is REVIEW territory: record `DRAFT_QUEUE: {that KEY} → [x] prior — REVIEW` under `## Queue update` in this run's row file, note it in the run note, and move to the next line. Never reorder the queue and never edit it; INTAKE owns the file.

   **Queue exhausted.** If no line qualifies, claim keyless: branch `claude/gsc-analyse-{D}-{T}`, title `GSC ANALYSE {D} [running]`. Write `queue/rows/{D}_{T}_ANALYSE.md` (`row_type: QUEUE`) only if there are prior markers to record, plus the run note. Finish the PR as `GSC ANALYSE {D} — queue exhausted` and stop.
3. **Claim** before any research (README §2).
4. **Orientation.** If `queue/evidence/{KEY}_draft-evidence_*.md` exists, read it for orientation only. Its verdicts are void, and every figure is re-derived from primaries under MODEL §4.
5. **Analyse.** Follow MODEL §8.1 steps 1–8 exactly, within the P14 ANALYSE budget, and produce the full §6 memo: front matter, a body within P13, and Appendices A–G.
   - Front matter: `memo_date: {D}`, `model_version` as read at preflight, plus `produced_by: ROUTINE` and `run_base: {sha}`.
   - Step 1's identity check compares the company name and the resolved ISIN with the `company:` and `isin:` of the latest memo in every `memos/*/` folder. Legacy memos without `isin:` are a gap to note, never a match. If a prior memo turns up under another key, stop the analysis: write a row file with `row_type: PRIOR` naming the prior key and `DRAFT_QUEUE: {KEY} → [x] prior — REVIEW`, and finish the PR as `GSC ANALYSE {KEY} {D} — prior found (REVIEW)`.
   - If §7.1a resolves a different key, name the memo and row file by the resolved key, and keep the queue update on the queue line's key.
   - If Gate 0 fails, write the abbreviated memo (§6.4). That is a complete run, not INCOMPLETE.
   - If a gate or cheapness input is missing, apply the data-completeness gate (README §5, D3).
6. **Write:**
   - **Full or Gate-0 memo:**
     - the memo `memos/{KEY}/{KEY}_{D}_GSC.md`
     - the row file `queue/rows/{D}_{T}_ANALYSE_{KEY}.md` (README §4), including `DRAFT_QUEUE: {KEY} → [x]`
     - a deletion of this name's `queue/evidence/{KEY}_*.md` files (draft evidence and any earlier INCOMPLETE note), if any exist
     - the final run note
   - **INCOMPLETE:**
     - `queue/evidence/{KEY}_{D}_INCOMPLETE.md`
     - the row file with `row_type: INCOMPLETE`
     - the final run note

     Keep `queue/evidence/{KEY}_draft-evidence_*.md`. Only a full or Gate-0 memo deletes it.
7. **Re-measure compliance** (README §5), commit (`GSC: {KEY} v1 {VERDICT}`, or `GSC: {KEY} INCOMPLETE`), push, and finish the PR (README §1) as `GSC ANALYSE {KEY} {D} — {VERDICT} ({deciding gate})`, or `— INCOMPLETE ({named gap})`.
8. **Stop.** One name per run.

**Forbidden:**
- a second name
- any edit to `_REGISTER.md`, `queue/TODO.md`, `queue/DRAFT_QUEUE.md` or `queue/IDEAS.md`
- any zone, ADD or SELL-FLAG statement (held names never enter this job)
- any change to a locked path

*Framework output, not investment advice.*
