# QUEUE-SEED routine — evidence-only queue upkeep (under MODEL §8.7)

**Schedule:** Monday and Thursday at 06:20 Europe/Prague.
Weekdays 09:00–18:00 are routine-free and 02:00–06:00 is quiet outside the weekend sprint. These times must equal the live routine crons (MODEL §8.7 item 12).
**Branch:** `claude/gsc-seed-{D}-{T}`. **PR title:** `GSC SEED {D} [running]`. The job token is `seed` in the branch and `SEED` in the title and run note (`queue/runs/{D}_{T}_SEED.md`); only the proposal file keeps the full name, `queue/proposals/{D}_{T}_QUEUE-SEED.md`.

Output is **proposals only**. Merging the PR approves section 6 (the restock), which INTAKE then appends to `queue/DRAFT_QUEUE.md`. To change the restock, edit or delete lines in the PR before merging. A SEED PR is never auto-merged; Jakub's merge approves the proposal (MODEL §8.7 item 10).

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

   A closed take-private or merger, a registered squeeze-out or an effective delisting that this run finds for a name with a register row (matched on company name or ISIN) is never retired here: it goes into section 5 as an open item, `ADD: KEY — delisting awaiting retirement (§7.1 RETIRED) — {event}, {date}, {source}`, which INTAKE applies to `▶ Open items (register)` once the PR is merged; retirement is attended only (MODEL §7.1 RETIRED) [v4.6.0; G5]. The same finding for a queue name, which has no register row, is a decay finding in section 5; the routine edits no queue line, and ANALYSE marks it `[x] no listed security` when it reaches it (ANALYSE.md step 5).
5. **Build the exclusion set.** A name in any of these places isn't new; at most you can propose re-ranking it:
   - every register row (RETIRED rows included, MODEL §7.1 RETIRED), matched on company name, and every ISIN in the `isin` column of `register.csv` and in every memo's `isin:` — every file in `memos/` and `archive/memos/` — where the candidate's ISIN is known
   - every `key` and every `aliases` entry in `register.csv`
   - every key and company in TODO, including block C3's recorded exclusions (never re-seed those; C3 records listing and perimeter facts, never a size exclusion [v4.7.0])
   - every line of `DRAFT_QUEUE.md`, whatever its marker
   - every held name
   - every open or recently rejected claim
6. **Verify each candidate,** one issuer per query:
   - the listed line, its §7.1a suffix, and one GET to the price endpoint for that key (record `exchangeName`, `currency` and the last bar's date, never the price)
   - no pending take-private, merger, delisting, squeeze-out or separation. If one is pending, the name goes under "Excluded", with the fact and its source.
   - the reporting currency and fiscal year-end
   - a primary-filing route actually reachable from the sandbox; record what you fetched

   A venue the price endpoint does not serve (MODEL §7.1a, "Not served"), or a dead feed on a served venue (no bar in the last 30 days; e.g. `MASTERPLAST.BD`, last bar 2024-07), goes under "Blocked — data access" with a one-line retrieval note, not into the queue. A thinly traded line whose last bar is newer is queued like any other, with that date in its note [v4.7.0]. No market and no company size is blocked by the framework: market cap, liquidity, free float and venue tier never exclude, hold back or block a candidate (MODEL v4.5.0; §8.7 item 6, v4.7.0).
7. **Write `queue/proposals/{D}_{T}_QUEUE-SEED.md`** with exactly these sections:
   1. Header: the TODO, register and queue state read, and the searches used.
   2. New names: `| Key | Company | Sector | Why queued | Status | Source |`. Propose at most 10, and only names that would rank in the top half of the current queue.
   3. Excluded at verification: one line each, with the fact and its source; company size is never such a fact [v4.7.0].
   4. Blocked — data access (venue not served, or a dead feed).
   5. Decay findings and re-ranking proposals, each with its criterion and source; then the open items for register names, one `ADD: KEY — delisting awaiting retirement (§7.1 RETIRED) — …` line each (step 4), or "none".
   6. **DRAFT_QUEUE restock:** paste-ready lines `- [ ] KEY — Company — market/route — note`. Draw from existing supply first. Retrieval route comes first in the ordering. A note carries facts to check first, never a lens or gate call and never a size threshold or size check [v4.7.0]. Where they apply, it names the facts the Gate 0 lens test will need: a banking or insurance licence, a captive finance arm, or a material listed subsidiary or holding (MODEL §2 Gate 0, round 2).
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
