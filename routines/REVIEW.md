# REVIEW routine — one due name per run (MODEL §8.2 under §8.7)

**Schedule:** weekdays at 07:20 and 15:20 Europe/Prague. During the burn-in week it runs only at 07:20.
**Branch:** `claude/gsc-review-{KEY}-{D}-{T}`. **PR title:** `GSC REVIEW {KEY} {D} [running]`, with the `HELD · ` prefix for portfolio names.

1. **Preflight** per `routines/README.md` §0.
2. **Find what's due.** Build the candidate list in this priority order:
   1. **Held names** (portfolio table) whose `Next review` trigger has fired.
   2. **Review requests** in the `queue/TODO.md` block `▶ Review requests (SWEEP)`. Skip a request whose key's latest memo date is on or after the request's sweep date: that name has already been reviewed since.
   3. **WATCH rows** whose dated trigger (a results date, a filing or an event) is past.
   4. **AVOID rows** whose dated trigger is past. These are low priority by construction.

   Drop any key that:
   - is claimed (README §2);
   - has a pending `queue/rows/*_{KEY}.md`;
   - already has a memo dated D (`memos/{KEY}/{KEY}_{D}_GSC.md`);
   - is a stalled REVIEW key (README §2): it has two abandoned REVIEW PRs closed within 14 days of each other, and the later one was closed less than 14 days ago.

   Check at most 4 candidates, in order, to see whether the cited document or event has actually been published. Use one search or IR-page lookup per candidate and log these as "due-check operations". They are the one web work allowed before the claim. The first confirmed candidate is the run's name.

   If nothing is confirmed, open no PR. End with a session summary listing each candidate checked and why it isn't due. A due-but-unpublished trigger (for example "10-K not yet filed") is worth one line under `## TODO additions` only if a row file is being written anyway.
3. **Claim** before any further research (README §2).
4. **Review.** Follow MODEL §8.2 steps 1–6 exactly, within the P14 REVIEW budget.
   - Load the prior memo per §7.4a: the latest-dated file in `memos/{KEY}/`, never a `_superseded-` file. Confirm its date matches the register row.
   - Fetch only the delta.
   - Re-test the sections the new information touches, plus any section whose mechanics changed between the prior memo's `model_version` and the live version.
   - **Held names** also get step 4: the sell-reason audit, the current zone with distances to the ADD band and the sell-flag line, and the bias tick-through before the zone statement. Jakub decides at merge; the PR title carries `HELD · `. A SELL-FLAG decision for Jakub goes under `## Open items` in the row file.
   - Any `queue/evidence/{KEY}_*` file is orientation only.
   - If a gate or cheapness input is missing, apply the data-completeness gate (README §5, D3).
5. **Write:**
   - **Memo:**
     - the new memo `memos/{KEY}/{KEY}_{D}_GSC.md`, with the version bumped and an Appendix G entry. Front matter: `memo_date: {D}`, the live `model_version`, `produced_by: ROUTINE` and `run_base: {sha}`. Never overwrite a memo.
     - `queue/rows/{D}_{T}_REVIEW_{KEY}.md` (README §4) with the replacement row, plus the portfolio row if the name is held
     - a deletion of this name's `queue/evidence/{KEY}_*.md` orientation files, if any exist
     - the final run note
   - **INCOMPLETE:** `queue/evidence/{KEY}_{D}_INCOMPLETE.md`, the row file with `row_type: INCOMPLETE`, and the final run note. Delete no evidence file.
6. **Re-measure compliance** (README §5), commit (`GSC: {KEY} v{n} {VERDICT}`, or `GSC: {KEY} INCOMPLETE`), push, and finish the PR (README §1) as `GSC REVIEW {KEY} {D} — {VERDICT}; {what moved}`, or `— INCOMPLETE ({named gap})`.
7. **Stop.** One name per run.

**Forbidden:**
- a second name
- any edit to the register, TODO, the queue or IDEAS
- position events: a "bought" or "sold" line in any source never becomes a portfolio change here
- any change to a locked path

*Framework output, not investment advice.*
