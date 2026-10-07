# queue/rows/ — intake inbox (MODEL §8.7)

**What goes here:** one file per finished routine result that affects the register or the queue. ANALYSE, REVIEW and SWEEP write one each, including the INCOMPLETE and PRIOR outcomes. The format is in `routines/README.md` §4.

**Names** (`D` = run date, `T` = run time `HHMM`, both Europe/Prague):
- `{D}_{T}_ANALYSE_{KEY}.md` and `{D}_{T}_REVIEW_{KEY}.md`
- `{D}_{T}_SWEEP.md`
- `{D}_{T}_ANALYSE.md` — a queue-exhausted ANALYSE run that still has prior markers to record (`row_type: QUEUE`)

**Lifecycle.**
1. A routine PR adds the file.
2. The PR is merged — by gsc-automerge for a merge class about a minute after its guard check succeeds, by Jakub otherwise (MODEL §8.7 item 10). That merge is the confirm.
3. The next INTAKE builds the rows from the current memos — the one file in each `memos/{KEY}/` (memo wins) — writes at most one register version, updates `queue/DRAFT_QUEUE.md` and `queue/TODO.md`, and deletes the file.

A file here on `main` is by definition merged and not yet taken in.

**INTAKE may hold a row back.** If the memo a row points to is neither the current memo nor in `archive/memos/{KEY}/` (not on `main` yet), or the key's `memos/{KEY}/` holds more than one file, INTAKE leaves the file in place and lists it under "Held back" in its PR body. It stays pending until the memo lands or the folder is cleaned up, or until Jakub deletes it in an attended session. A row whose memo has since moved to `archive/memos/{KEY}/` (a newer REVIEW replaced it) is consumed as superseded: only its queue update is applied.

**Why a folder instead of direct register edits.** Every routine PR only *adds* files, so PRs never conflict and can be merged in any order. Register version numbers stay sequential because only INTAKE writes `_REGISTER.md`, and only one INTAKE PR is open at a time.

Never edit a file here by hand. To stop a result from landing, close its PR before it is merged (a held PR waits for Jakub; a merge-class PR merges within minutes of finishing). If it has already landed, revert its PR (GitHub Revert, merged with its `(#n)` title) or delete the row file in an attended session, before the next INTAKE. An attended session that writes a key with a pending row here takes the row in first: it applies every section of the file as INTAKE would (the register row from the current memo with `routines/tools/gsc_register.py apply --row`, queue marker, TODO additions, Open items to the `queue/TODO.md` head block `▶ Open items (register)`, IDEAS candidates), then deletes the file in the same commit.

This README is framework-owned.
