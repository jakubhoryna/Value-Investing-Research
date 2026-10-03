# queue/proposals/ — QUEUE-SEED output (MODEL §8.7)

**What goes here:** `{D}_{T}_QUEUE-SEED.md` files (`D` = run date, `T` = run time `HHMM`, both Europe/Prague): new-name proposals, decay findings, re-ranking proposals and a paste-ready `DRAFT_QUEUE restock` section. The format is in `routines/QUEUE-SEED.md`. The run that writes one uses `seed` in its branch name (`claude/gsc-seed-{D}-{T}`) and `SEED` in its PR title and run note.

**Merge = approval.** Merging a QUEUE-SEED PR approves its section 6 restock lines as they stand in the PR. The next INTAKE appends them to `queue/DRAFT_QUEUE.md`, skipping keys already in the queue (it lists the skipped lines in its PR body), and moves the file unchanged to `queue/archive/proposals/` under the same name. To change the restock, edit the file in the PR before merging, or close the PR.

Sections 2–5 (new names, exclusions, decay findings, re-ranking) are **information**. They change nothing until an attended session acts on them.

Never edit a file here after it has merged. If an approved restock must not land, delete the file in an attended session before the next INTAKE.

This README is framework-owned.
