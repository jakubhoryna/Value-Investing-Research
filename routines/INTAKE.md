# INTAKE routine — the single register writer (MODEL §8.7; §7.4a and §7.5 in git form)

**Schedule:** daily at 06:50 Europe/Prague.
**Branch:** `claude/gsc-intake-{D}-{T}`. **PR title:** `GSC INTAKE {D} [running]`.

INTAKE folds everything Jakub has **merged** since the last intake into one register version. On `main`, the files in `queue/rows/` and `queue/proposals/` (other than `README.md`) are by definition merged and pending. INTAKE does no web work. It also runs the daily abandoned-claim sweep and the free-plan audit.

Work in the working tree and stage nothing until step 9; that keeps the restart in step 8 clean.

0. **Preflight** per `routines/README.md` §0. Then:
   - **Open INTAKE PR.** If an open `GSC INTAKE` PR exists: when its title ends `[running]` and it is more than 6 hours stale, close it as `[abandoned]` (README §2) and continue; otherwise stop with **no PR**.
   - **Abandoned-claim sweep** for all jobs (README §2): close every stale `[running]` PR. Then re-run the ledger command (README §1), so the PRs just closed count, and find stalled keys from it.
   - **Nothing to do** means all of these hold:
     - no pending row file, other than rows that would be held back again (their `memo_path` is still missing on `main`, step 3);
     - no pending proposal;
     - no unrecorded closed-unmerged ANALYSE PR, meaning none that step 5 would record (its key has a `[ ]` line and its number appears nowhere in `queue/DRAFT_QUEUE.md`);
     - no stalled key still to record, meaning none that step 5 or step 6 would record (README §2).

     Then stop with no PR and end with a session summary. Name any held-back rows and any abandoned PRs closed in this step in that summary; the closing comment on each PR is their record.
1. **Base.** Record the HEAD sha; the outgoing register's `register_version` N and `register_date`; the TODO version n and date; the DRAFT_QUEUE version n and date. A version is the number after `v` in the file's version line. The next version is the next whole number: v36 → v37, and a dotted v1.1 → v2. Claim the branch and PR (README §2).
2. **Audit** (free-plan compensating control). Re-run the ledger command (README §1) first, so it includes this run's own PR. For the PR body, under `## Audit`:
   - commits on `origin/main` since the previous `GSC INTAKE` PR's `merged_at` (on the first run, the last 7 days) that didn't arrive through a PR merge: `git log --first-parent --since="<merged_at>" --format='%h %s' origin/main`. A subject that ends with `(#<n>)` (squash merge) or starts with `Merge pull request #<n> from ` (merge commit) is a PR merge; anything else is a direct commit. A rebase merge also shows up here as direct commits, so routine PRs are merged with "Squash and merge" or "Create a merge commit", never "Rebase and merge".
   - `claude/gsc-*` branches with no PR in the ledger: `git ls-remote origin 'refs/heads/claude/gsc-*'`. Leave out this run's own branch.

   If any direct commit exists, add a TODO item naming it.
3. **Apply the row files, oldest `run_date` then `run_time` first.** Step 3 only collects the changes (in `/tmp` notes); do not edit `_REGISTER.md`, `queue/TODO.md` or `queue/DRAFT_QUEUE.md` until its archive copy is taken (steps 4–6).
   - **ANALYSE / REVIEW.**
     - If `memo_path` doesn't exist on `main`, **hold back** the row: leave the file in place, list it under `## Held back` in the PR body with the reason, and apply nothing from it.
     - Find the latest non-superseded memo in `memos/{KEY}/` (the latest `{KEY}_YYYY-MM-DD_GSC.md`; never a `_superseded-` file). If `memo_path` is not that memo, the row is **superseded**: apply only its `## Queue update`, consume the file, and log "superseded by {latest memo}".
     - Otherwise build the row from that memo (README §4, memo wins): verdict, Past, Future, SF, memo date, version, Px and band from the front matter; annotation tokens from the row file, within 160 characters. Px @ memo prints as `{price} ({close date as D Mon YYYY})`. Log any front-matter disagreement in the PR body.
     - Merge the row into its verdict section per §7.1 ordering. A REVIEW row replaces the key's old row, moving section if the verdict changed. An ANALYSE row adds a new name.
     - Held name: update its portfolio row from the row file's `## Portfolio row`; the memo's front matter wins on zone, ADD band and sell-flag line. Never add or remove a portfolio row.
   - **INCOMPLETE / PRIOR / QUEUE.** No register change.
   - **SWEEP.** For each key in `## Price/ordering refresh`, take only Px and its close date. Skip the key if its register row changed in this INTAKE from an ANALYSE or REVIEW memo dated after the sweep's close date, or if the close date isn't later than the date in the current Px cell. Otherwise:
     - set Px @ memo to `{Px} ({close date as D Mon YYYY})`, and recompute Dist % from that Px and the row's **current** band per §7.1. For an AVOID or DNAF row, update only Px @ memo (and `Last zone check` for a held name); its Dist % stays `—`;
     - for a held name, set `Last zone check` to `{sweep run_date} @ {Px} ({close date as D Mon} close)`. Zone, bands and the distance text inside band cells don't change from a sweep.

     → step 6: replace the TODO block `▶ Review requests (SWEEP)` with this sweep's `## Review requests`, one line each: `` - `KEY` — reason — sweep {run_date} ``. Leave out a key whose latest memo date is on or after the sweep's run_date.
   - **Every row type**, unless held back (a superseded row: `## Queue update` only):
     - `## Queue update` → step 5.
     - `## TODO additions` → step 6.
     - `## Open items` → apply under §7.1: two classes only (pending user decisions, register-integrity holds), one line each, at most 7 entries. Never remove a pending user decision; you may update its text. An entry that doesn't fit the classes or the cap goes to TODO instead (→ step 6), and the PR body says so.
     - `## IDEAS candidates` → step 6: copy verbatim into the TODO head block `▶ IDEAS candidates (attended triage)`, each line prefixed `{run_date} · {KEY} {JOB} —`.
   - **REVIEW applied** → step 6: remove its key from `▶ Review requests (SWEEP)` when the REVIEW's run_date is on or after that line's sweep date.
4. **Regenerate the register (§7.4a generation rule)** — only if at least one register row or the `## Open items` section changed. Otherwise write no snapshot and no new version; queue and TODO changes still go ahead.
   - **Snapshot first.** `cp _REGISTER.md registers/{YYYY}/REGISTER_v{N}_{register_date}.md`, where YYYY is the year of the outgoing `register_date`. It is a byte copy: never write it with the Write tool. If that path already exists on `main`, something else wrote the register: treat it as an unfixable breach (step 7).
   - Write the complete file:
     - Front matter: `register_version` v{N+1}, `register_date` {D}, and `names_total`, `verdict_split` and `portfolio_names` recomputed. Update the H1 line's version and date.
     - Sections: PORTFOLIO → BUY → WATCH → AVOID → DNAF, with the counts in the section headings updated. BUY and WATCH ascending by Dist % (no computable trigger: `n.m.`, at the section bottom). AVOID and DNAF alphabetical, Dist % `—`.
     - Carry the legend, the table preambles and `## Open items` verbatim, except the entries this INTAKE changes. Rows this INTAKE didn't touch stay byte-identical.
     - Dist % is recomputed for every row this INTAKE changed, as a signed whole percent (`+11%`, `−4%`).
     - Prepend one change-log line, ≤ 200 characters: `- **v{N+1} — {D}** — INTAKE: KEY ANALYSE VERDICT (gate); KEY REVIEW …; SWEEP refresh ({k} Px)`. If it doesn't fit, list the keys only; the PR body carries the detail. Trim the log to the newest 5 entries and keep the pointer line below it.
5. **Update `queue/DRAFT_QUEUE.md`** — only if something changes. First `cp queue/DRAFT_QUEUE.md queue/archive/DRAFT_QUEUE_v{n}_{date}.md` (the outgoing version and its date). Markers replace only the leading token and keep `KEY — Company — …`. A marker is set only on a line whose marker is `[ ]` at that moment, counting changes made earlier in this INTAKE. It never overwrites another marker, so a later prior marker can't replace `[x] {D}`. List any skipped update in the PR body.
   - `[ ]` open · `[x] {D}` analysed (merged ANALYSE row) · `[x] prior — REVIEW` (PRIOR row or queue marker)
   - `[-] rejected {D} (PR #n)` — for each closed-unmerged PR titled `GSC ANALYSE {KEY} {date} …` whose key has a `[ ]` line and whose number appears nowhere in the file. Skip titles ending `[abandoned]` or `[running]`, `— prior found (REVIEW)` and keyless `queue exhausted` PRs.
   - `[!] incomplete {D} — {evidence_path}` (INCOMPLETE row)
   - `[!] stalled {D} (PR #a, #b)` (README §2) — only if the later number, `#b`, appears nowhere in the file.

   "Appears" means as a whole number: `#44` doesn't match `#445`.

   Append the section 6 `DRAFT_QUEUE restock` lines of each pending `*_QUEUE-SEED.md` below the last queue line (above the footer note), skipping any key already present with any marker; list skipped lines in the PR body. Never reorder lines. Bump the version line to `(v{next} · {D})`, `{next}` per step 1.
6. **Update `queue/TODO.md`** — only if something changes. First `cp queue/TODO.md queue/archive/TODO_v{n}_{date}.md` (the outgoing version and its date). Then:
   - The two standing head blocks sit first, below the purpose paragraphs: `## ▶ Review requests (SWEEP)`, then `## ▶ IDEAS candidates (attended triage)`. Create them if absent, then apply the head-block changes collected in step 3. INTAKE never clears IDEAS candidates; attended triage does.
   - Add one dated block below them, `## ▶ Routed by INTAKE {D}, register v{N+1}` (or "register unchanged"), with the `## TODO additions`, grouped by key, each item starting with the backticked key. Add the audit items here too, and a stalled-REVIEW item `` `KEY` — REVIEW stalled {D} (PR #a, #b) `` only if the later number, `#b`, appears nowhere in `queue/TODO.md` (README §2).
   - Bump the version line to `(v{next} · {D})`, `{next}` per step 1, and prepend one line to `## Change log` in the file's own style, naming the archive.
7. **Checks — by script, not by eye.** Write a script to `/tmp`, run it with `python3`, count characters (not bytes), and paste the numbers into the PR body:
   - every register cell ≤ 160 characters; every change-log line ≤ 200;
   - `names_total`(new) = `names_total`(old) + ANALYSE rows added as new names;
   - every key in the outgoing register is still present (the key is the first token of the Ticker cell);
   - `verdict_split` and `portfolio_names` match the section and table row counts;
   - no duplicate keys within the master table (BUY, WATCH, AVOID and DNAF together), and every Portfolio-table key appears exactly once in the master table and only once in the Portfolio table;
   - no duplicate ISIN across the `isin:` of the latest memo per key. Legacy memos without `isin:` are listed as gaps, never a failure. A duplicate that involves a row changed in this version is a breach; one among untouched rows goes into the PR body and a TODO item;
   - BUY and WATCH ascending by Dist %;
   - for rows changed in this version only, `memos/{KEY}/{KEY}_{memo date}_GSC.md` exists.

   Fix any breach and re-run. **Unfixable:** throw away the uncommitted changes, commit only the run note naming the breach, push, close your own PR titled `GSC INTAKE {D} — blocked: {reason}` (one PATCH with `state=closed`, title and body), and stop.
8. **Base check.** `git fetch origin main`. If `origin/main` has moved since step 1 and the move touched `_REGISTER.md`, `queue/TODO.md` or `queue/DRAFT_QUEUE.md`, **restart once** on the same branch and PR. Never re-claim.
   1. Throw away the uncommitted work: `git checkout -- _REGISTER.md queue`, and `rm` the snapshot and archive files you created.
   2. `git merge --no-edit origin/main`.
   3. Redo steps 1–7 (without the claim) from the merged tree.

   On a second collision, close the PR as blocked (step 7) with reason "main moved twice".
9. **Consume, commit, push.**
   - `git rm` each applied or superseded row file. Leave held-back rows.
   - For each applied proposal: `mkdir -p queue/archive/proposals`, then `git mv queue/proposals/{name}.md queue/archive/proposals/{name}.md`. Don't edit it first.
   - Write the run note `queue/runs/{D}_{T}_INTAKE.md`. `git add` the exact paths you changed, then commit: `GSC: register v{N+1} — INTAKE {D}`, or `GSC: INTAKE {D} — no register change` (this form also covers a run that only consumed files).
   - `git push -u origin "{BR}"` (a fast-forward, also after a restart merge) and finish the PR (README §1) as `GSC INTAKE {D} — register v{N+1} ({k} rows)`, or `GSC INTAKE {D} — no register change ({k} rows)`.

   The PR body contains every old row → new row, queue changes, TODO changes, the compliance numbers, memo-vs-row disagreements, superseded rows, `## Held back`, abandoned PRs closed, stalled keys and `## Audit`.

**Forbidden:**
- web work
- verdict judgment: rows come from memos, never from reasoning
- position events: never add or remove a portfolio row
- edits to memos, MODEL, IDEAS or locked paths
- merging any PR, including its own

*Framework output, not investment advice.*
