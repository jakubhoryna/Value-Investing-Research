# QUEUE-SEED routine — evidence-only queue upkeep (under MODEL §8.7)

**Schedule:** weekdays at 06:20 Europe/Prague.
**Branch:** `claude/gsc-seed-{D}-{T}`. **PR title:** `GSC SEED {D} [running]`. The job token is `seed` in the branch and `SEED` in the title and run note (`queue/runs/{D}_{T}_SEED.md`); only the proposal file keeps the full name, `queue/proposals/{D}_{T}_QUEUE-SEED.md`.

Output is **proposals only**. Merging the PR approves section 6 (the restock), which INTAKE then appends to `queue/DRAFT_QUEUE.md`. To change the restock, edit or delete lines in the PR before merging.

1. **Preflight** per `routines/README.md` §0. If an open `GSC SEED` PR exists, stop with no PR.
2. **Claim** before any web work (README §2): branch, run-note stub, push, PR.
3. **Load from the checkout:**
   - `queue/TODO.md` (record its version line)
   - `_REGISTER.md` (record `register_version`)
   - `queue/DRAFT_QUEUE.md` (count the `[ ]` lines that aren't claimed per the ledger)
   - `model/MODEL.md` §7.1a (the suffix table)
4. **Choose the mode.**
   - If **10 or more** unclaimed lines remain, skip discovery and run the **decay pass** on the next 8 unclaimed lines. For each issuer, check its corporate actions: take-private, merger, delisting, squeeze-out, split or share-count change, buyback with cancellation, and reporting-segment change. Use one issuer per query, at most 8 queries.
   - Otherwise, run **discovery (≤ 15 searches) + the decay pass**. Search by sector + exchange or by issuer, never generically. The discovery targets are:
     - direct listed peers of live WATCH rows
     - the register's named coverage gaps (UK, Canada, Australia, pure automation platforms, manufacturing software)
     - event-driven names: a first buyback, a control change, or a first annual report in the last ~90 days, in markets on the §7.1a table
5. **Build the exclusion set.** A name in any of these places isn't new; at most you can propose re-ranking it:
   - every register row, matched on company name (the register has no ISIN column), and every memo's `isin:` where the candidate's ISIN is known
   - every key and company in TODO, including block C3's recorded exclusions (never re-seed those)
   - every line of `DRAFT_QUEUE.md`, whatever its marker
   - every held name
   - every open or recently rejected claim
6. **Verify each candidate,** one issuer per query:
   - the listed line and a suffix on the §7.1a table
   - no pending take-private, merger, delisting, squeeze-out or separation. If one is pending, the name goes under "Excluded", with the fact and its source.
   - the reporting currency and fiscal year-end
   - a primary-filing route actually reachable from the sandbox; record what you fetched

   Suffix-gap markets (`.NS .BO .IR .LS .SR .AE .BD`) go under "Blocked — framework", not into the queue.
7. **Write `queue/proposals/{D}_{T}_QUEUE-SEED.md`** with exactly these sections:
   1. Header: the TODO, register and queue state read, and the searches used.
   2. New names: `| Key | Company | Sector | Why queued | Status | Source |`. Propose at most 10, and only names that would rank in the top half of the current queue.
   3. Excluded at verification: one line each, with the fact and its source.
   4. Blocked — framework.
   5. Decay findings and re-ranking proposals, each with its criterion and source.
   6. **DRAFT_QUEUE restock:** paste-ready lines `- [ ] KEY — Company — market/route — note`. Draw from existing supply first. Retrieval route comes first in the ordering.
   7. Method notes: routes that worked or failed, for TODO block D.

   Close the file with: "Proposal only — approved by merge; INTAKE applies section 6."
8. **Write the run note** (≤ 300 words), push, and finish the PR (README §1) as `GSC SEED {D} — {n} new · {d} decay findings · restock {r}`.

**Forbidden:**
- any verdict, gate call, multiple, band, price or "cheap"/"expensive" reasoning
- any memo
- any edit to an existing file
- more than 10 new names

Label every carried fact as sourced (document + date) or unverified.

*Framework output, not investment advice.*
