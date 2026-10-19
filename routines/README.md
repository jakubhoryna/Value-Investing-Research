# routines/ — shared protocol for scheduled GSC runs (MODEL §8.7)

Every routine's saved prompt is one line:

```
GSC ROUTINE: <JOB> — follow routines/README.md and routines/<JOB>.md exactly.
```

`<JOB>` is one of `ANALYSE · REVIEW · SWEEP · INTAKE · QUEUE-SEED`. Everything a run needs is in this repo. This folder is framework-locked: it changes only under "commit model".

---

## 0. Preflight — in this order; stop at the first failure

1. **Session start.** Complete the `CLAUDE.md` session start: HEAD sha, `model_version` ≥ v4.5.0, register read, private check.
2. **Environment.** `echo "$GSC_SESSION"` must print `routine`. If it doesn't, the run is in the wrong environment and the guard is inactive.
3. **Guard live.** Both must hold:
   - `git ls-files --error-unmatch .claude/settings.json .claude/hooks/gsc_guard.py` succeeds;
   - the self-test `: gsc-guard-canary`, run as its own Bash command, is **refused** with a message containing `GSC guard canary`. (`:` is a no-op, so the self-test is harmless when the guard is off. Never use a push or a locked-path write as a self-test: the permission classifier reads those as real attempts and then blocks the run's next GitHub calls.)

   If the self-test runs (exit 0) or the files are untracked, the guard is off.
4. **Ledger.** Run the paginated ledger command (§1). Its output is this run's **claim ledger** (§2). If the call fails, stop: without the ledger a run can collide with another.
5. **Fix the run date and time, once.** `D=$(TZ=Europe/Prague date +%F)` and `T=$(TZ=Europe/Prague date +%H%M)`. Write both down and reuse them literally (§5: never re-read the clock).
6. **Exactly one repository.** `git rev-parse --show-toplevel` must print the session's starting directory (`pwd -P`), and so must `$CLAUDE_PROJECT_DIR` if it is set; `ls -d ../*/.git` must list no other clone. With a second repository attached, hooks and deny rules don't load.

**On failure.**
- Steps 1, 2 and 4: write nothing. End with a session summary that names the failed step.
- Steps 3 and 6 (guard off): if you can, fix D and T, cut the keyless branch `claude/gsc-{job}-{D}-{T}`, commit only the run note `queue/runs/{D}_{T}_{JOB}.md` saying "guard off: {reason}", push it and open a PR titled `GSC {JOB} {D} — stopped: guard off`. REVIEW has no key at this point and its branches must carry one, so REVIEW only ends with a summary. Then stop.

## 1. Names, commands and the PR contract

**One run → one branch → one PR.** Ignore any branch name the harness suggests; use the name below.

| Prompt job | Branch token | Title word | Branch | Run note | Output file |
|---|---|---|---|---|---|
| ANALYSE | `analyse` | ANALYSE | `claude/gsc-analyse-{KEY}-{D}-{T}`; queue exhausted: `claude/gsc-analyse-{D}-{T}` | `queue/runs/{D}_{T}_ANALYSE_{KEY}.md` (keyless: `…_ANALYSE.md`) | `queue/rows/{D}_{T}_ANALYSE_{KEY}.md` (keyless with prior markers: `queue/rows/{D}_{T}_ANALYSE.md`) |
| REVIEW | `review` | REVIEW | `claude/gsc-review-{KEY}-{D}-{T}` | `queue/runs/{D}_{T}_REVIEW_{KEY}.md` | `queue/rows/{D}_{T}_REVIEW_{KEY}.md` |
| SWEEP | `sweep` | SWEEP | `claude/gsc-sweep-{D}-{T}` | `queue/runs/{D}_{T}_SWEEP.md` | `queue/rows/{D}_{T}_SWEEP.md` |
| INTAKE | `intake` | INTAKE | `claude/gsc-intake-{D}-{T}` | `queue/runs/{D}_{T}_INTAKE.md` | register, TODO and queue versions (§3) |
| QUEUE-SEED | `seed` | SEED | `claude/gsc-seed-{D}-{T}` | `queue/runs/{D}_{T}_SEED.md` | `queue/proposals/{D}_{T}_QUEUE-SEED.md` |

- `D` = `YYYY-MM-DD`, `T` = `HHMM`, both from §0 step 5. KEY uses only `[A-Za-z0-9._-]` (e.g. `7309.T`, `ATCO-B.ST`).
- In file names and titles, `{JOB}` is the title word (so `SEED` for QUEUE-SEED); in branch names, `{job}` is the branch token.
- Every branch must match `^claude/gsc-(analyse|review|seed|sweep|intake)-(?:(?P<key>[A-Za-z0-9._-]+)-)?(?P<date>\d{4}-\d{2}-\d{2})-(?P<time>\d{4})$`. A key is required for review, optional for analyse (queue exhausted only), and forbidden for seed, sweep and intake.
- INCOMPLETE evidence: `queue/evidence/{KEY}_{D}_INCOMPLETE.md`. The claim stub and the final run note share one path.

**PR title — the claim.** Open as `GSC {JOB} {KEY} {D} [running]` (keyless jobs omit KEY). Finish as `GSC {JOB} {KEY} {D} — {outcome}`. A REVIEW of a name in the portfolio table carries the prefix `HELD · ` on both titles. Every routine title matches `^(HELD · )?GSC (ANALYSE|REVIEW|SEED|SWEEP|INTAKE)\b`.

**Finished-title grammar — machine-read by gsc-automerge (MODEL §8.7 item 10).** After ` — ` the outcome is exactly one of:
- ANALYSE: `{VERDICT} ({deciding gate})`, `INCOMPLETE ({named gap})`, `prior found (REVIEW)`; keyless: `queue exhausted`
- REVIEW: `{VERDICT}; {what moved}` or `{VERDICT} ({gates}); {what moved}` — when the verdict changed, `{what moved}` begins `was {OLD}`, and only then; `INCOMPLETE ({named gap})`
- SWEEP: `{n}/{N} priced · …`
- SEED: free text
- INTAKE: `register v{N} ({k} rows)`, `no register change ({k} rows)`
- any job: `stopped: {reason}`, `blocked: {reason}` (ANALYSE's `stopped: no listed security`, ANALYSE.md step 5, among them [v4.6.0])

`{VERDICT}` is one of BUY, WATCH, AVOID, DNAF. The title's key and date equal the branch's. The row file's `pr_title:` equals the final title byte for byte, so a title never contains ` #` (the front-matter reader drops a ` # …` tail). A title outside this grammar is held for Jakub.

**PR body — the printed diff (MODEL §7.4a).** Write it to `/tmp/pr_body.md` with the Write tool. It contains:
- the verdict line or outcome
- the register diff: old row → new row, or "new name"
- the file list
- the compliance re-measure numbers
- the source and document count
- the P14 operations used
- anything unretrievable, with host and reason
- what needs Jakub, in at most 3 lines

End the body with *"Framework output, not investment advice."*

**GitHub commands — REST through `gh api` only.** Write the repo path, branch name and PR number literally: shell variables don't survive between tool calls, and the guard checks the literal text. `{BR}` is this run's branch and `{n}` its PR number.

```
# ledger (all pages, lean output) — §0 step 4; page by page, never --paginate (see below)
p=1; while :; do n=$(gh api "repos/jakubhoryna/Value-Investing-Model/pulls?state=all&per_page=100&sort=updated&direction=desc&page=$p" --jq length) || exit 1; [ "$n" -gt 0 ] || break; gh api "repos/jakubhoryna/Value-Investing-Model/pulls?state=all&per_page=100&sort=updated&direction=desc&page=$p" --jq '(now - 90*86400 | todate) as $c90 | (now - 14*86400 | todate) as $c14 | .[] | select(.state == "open" or (.merged_at == null and .updated_at >= $c90) or .updated_at >= $c14 or ((.title | startswith("GSC INTAKE ")) and .updated_at >= $c90)) | [.number, .state, (.merged_at // "-"), .updated_at, .head.ref, .title] | @tsv' || exit 1; [ "$n" -lt 100 ] && break; p=$((p+1)); done
# claim: create the PR, keep the number it prints
gh api "repos/jakubhoryna/Value-Investing-Model/pulls" -f head="{BR}" -f base=main -f title="GSC … [running]" -f body="Claim — run in progress. Do not merge." --jq .number
# state check before finishing (repeat until head.sha is the pushed sha)
gh api "repos/jakubhoryna/Value-Investing-Model/pulls/{n}" --jq '[.state, .merged, .head.sha] | @tsv'
# finish: one PATCH, title + body from the file
gh api -X PATCH "repos/jakubhoryna/Value-Investing-Model/pulls/{n}" -f title="GSC … — …" -F body=@/tmp/pr_body.md
# close an abandoned claim (INTAKE only, §2)
gh api -X PATCH "repos/jakubhoryna/Value-Investing-Model/pulls/{n}" -f state=closed -f title="… [abandoned]"
# supersede a stale INTAKE PR (INTAKE only, INTAKE.md step 0)
gh api -X PATCH "repos/jakubhoryna/Value-Investing-Model/pulls/{n}" -f state=closed -f title="{old title} [superseded]"
```

The ledger lists open PRs, closed-unmerged PRs updated in the last 90 days, everything updated in the last 14 days, and `GSC INTAKE` PRs of the last 90 days. It reads the pages one by one (`&page=1`, `2`, … up to the first page with fewer than 100 PRs): `--paginate` follows GitHub's `Link` header, whose `repositories/{id}` URL the cloud proxy refuses with HTTP 403 from page 2 on (v4.5.3). That covers every claim, stall, rejection and audit window in §2 and INTAKE. Older merged PRs are left out on purpose. The closing PATCHes keep the PR body (the printed diff): the reason goes in the title suffix and in the run note.

Never merge. Never comment on any PR or issue: a comment wakes the session watching it, and the `GSC - needs Jakub` and `GSC digest` issues belong to the gsc-automerge and gsc-notify workflows (the guard hook refuses every comment). Never `gh pr …`. Never `gh api graphql`. Never PUT or DELETE. Never PATCH a PR's `base`.

**Git commands — exact forms.**

```
git fetch origin main
git switch --no-track -c "{BR}" origin/main
git add <explicit paths>          # never -A on a run branch
git commit -m "…"
git push -u origin "{BR}"         # the ONLY push form; repeat it for later pushes
git merge --no-edit origin/main   # the only way to absorb a moved main (INTAKE restart)
mkdir -p <archive dir>            # REVIEW: archive/memos/{K} · INTAKE: archive/registers/{YYYY} · archive/queue/proposals
git mv <src> <dst>                # REVIEW: memos/{K}/{f} → archive/memos/{K}/{f} · INTAKE: queue/proposals/{f} → archive/queue/proposals/{f}
```

Never rebase, reset, amend, cherry-pick onto or force-push a pushed run branch. Never push any other ref. Never touch another run's branch or PR, except INTAKE under the abandoned-claim rule (§2).

**Finishing a run.**
1. Final commit and `git push -u origin "{BR}"`.
2. State check: `gh api "repos/jakubhoryna/Value-Investing-Model/pulls/{n}" --jq '[.state, .merged, .head.sha] | @tsv'`. Until `.head.sha` equals your pushed `git rev-parse HEAD`, repeat the state check (at most 5 times): GitHub updates the PR head a moment after the push, and a finishing PATCH sent before that runs the guard on the old sha and leaves the final head unchecked. If the PR is still open, send the one finishing PATCH.
3. If it is no longer open (merged early or closed), open a **new** PR from the same branch with the final title, and start its body with "Replaces #{n}, which was {merged | closed} before the run finished."
4. If PR creation fails after a successful push, retry once. If it fails again, name the branch in the run note, push the note, and stop. INTAKE's audit lists branches that have no PR.

## 2. Claim ledger

A key is **claimed** for a job family (ANALYSE or REVIEW) if the ledger shows either of these for it. Match titles with `^(HELD · )?GSC (ANALYSE|REVIEW) {KEY} ` — note the trailing space, so `ABC` never matches `ABCD`.

- an open PR with that title, whatever its state (`[running]`, finished, `[fixing]`);
- a closed, unmerged PR with that title updated in the last **90 days for ANALYSE** or the last **7 days for REVIEW**. This means Jakub rejected it. Closed PRs whose title ends `[abandoned]`, `[superseded]` or still ends `[running]` don't count; they were abandoned, not rejected.
- a merged PR with that title that has been reverted on `main`: a first-parent subject starting `Revert "{that PR's title}` within the same window (90 days for ANALYSE, 7 days for REVIEW), checked with `git log --first-parent --since="90 days ago" --format=%s origin/main`. A revert is Jakub's undo of an auto-merge (MODEL §8.7 item 10), so it counts as a rejection; once INTAKE has recorded it on the queue line (INTAKE.md step 5), the marker carries it.

**Override:** a queue line for the key that carries the word `retry` (added by Jakub) makes the key eligible despite a rejection. To retry, Jakub rewrites the line as `- [ ] KEY — Company — route — notes — retry (PR #n)`: he drops `rejected {D}`, keeps the KEY right after the marker, and moves `(PR #n)` into the trailing note. INTAKE's marker replacement never touches that note, and the number in it stops INTAKE recording the old rejection again.

Compare `updated_at` (UTC) with `date -u +%s`, never with Prague time.

**Abandoned claim — executed only by INTAKE (daily).** An open PR whose title ends `[running]` and whose `updated_at` is more than 6 hours old: close it with the single abandoned-close PATCH in §1, the title ending `[abandoned]` in place of `[running]`. No comment; INTAKE names it in its run note and PR body.

Its key becomes eligible again. Until INTAKE closes it, every other job treats it as a claim and skips the key. To keep a stalled run for repair, Jakub retitles its PR to end `[fixing]`; the rule never touches that.

**Stalled key.** A key with two abandoned PRs (title ending `[abandoned]`, or closed while still `[running]`) of the same job within 14 days, `#a` the earlier and `#b` the later:
- **ANALYSE key.** INTAKE marks its `[ ]` queue line `[!] stalled {D} (PR #a, #b)`, and ANALYSE skips it until Jakub edits the line. To release it, Jakub rewrites the line as `- [ ] KEY — Company — route — notes — reset (PR #a, #b)`, keeping the numbers in the trailing note. A key picked from the `queue/TODO.md` block `▶ Group dependencies` gets the same marker on its dependency line (INTAKE.md step 3); its parent then counts the subsidiary or holding as ungradeable.
- **REVIEW key.** It has no queue line: INTAKE adds a TODO item `` `KEY` — REVIEW stalled {D} (PR #a, #b) ``. REVIEW skips the key until 14 days have passed since `#b` was closed (its `updated_at`).

INTAKE records a stalled key only once: only if `#b` appears nowhere in `queue/DRAFT_QUEUE.md` (ANALYSE queue key) or `queue/TODO.md` (REVIEW key, or an ANALYSE dependency key), as a whole number. A third abandonment brings a new `#b`, so it is recorded again.

**Claim before any research:**
1. `git fetch origin main`, then `git switch --no-track -c "{BR}" origin/main`.
2. Commit the run-note stub `queue/runs/{D}_{T}_{JOB}[_{KEY}].md`: job, key, D, T, base sha, status *in progress*.
3. `git push -u origin "{BR}"`.
4. Open the PR (§1) and keep its number.

Only then fetch anything from the web. The one exception is REVIEW's due-check operations (REVIEW.md step 2), which happen before the claim.

## 3. Write contract — single writer

Checked once per routine PR, on its final title, by the `gsc-guard` check (`.github/workflows/gsc-guard.yml`), and again by gsc-automerge before it merges (MODEL §8.7 item 10). On GitHub Free nothing server-side enforces the check, so the guard hook and this contract are what hold.

| Job | May add | May delete | May modify |
|---|---|---|---|
| ANALYSE | `memos/{K}/{K}_{D}_GSC.md` (at most one memo; only for a key with neither `memos/{K}/` nor `archive/memos/{K}/`) · `queue/rows/{D}_{T}_ANALYSE_{K}.md` · `queue/rows/{D}_{T}_ANALYSE.md` · `queue/runs/{D}_{T}_ANALYSE[_{K}].md` · `queue/evidence/{K}_{D}_INCOMPLETE.md` | `queue/evidence/{K}_*.md` | nothing |
| REVIEW | `memos/{K}/{K}_{D}_GSC.md` (at most one memo; K = the branch key) · `archive/memos/{K}/{K}_{P}_GSC.md` (exactly one with a memo, none without: the byte copy of the deleted prior, P before D) · `queue/rows/{D}_{T}_REVIEW_{K}.md` · `queue/runs/{D}_{T}_REVIEW_{K}.md` · `queue/evidence/{K}_{D}_INCOMPLETE.md` | `queue/evidence/{K}_*.md` · `memos/{K}/{K}_{P}_GSC.md` (only as that move) | nothing |
| SWEEP | `queue/rows/{D}_{T}_SWEEP.md` · `queue/runs/{D}_{T}_SWEEP.md` | — | nothing |
| QUEUE-SEED | `queue/proposals/{D}_{T}_QUEUE-SEED.md` · `queue/runs/{D}_{T}_SEED.md` | — | nothing |
| INTAKE | `archive/registers/{YYYY}/REGISTER_v{N}_{date}.md` · `archive/registers/{YYYY}/REGISTER_v{N}_{date}.csv` · `archive/queue/TODO_v{n}_{date}.md` · `archive/queue/DRAFT_QUEUE_v{n}_{date}.md` · `archive/queue/proposals/{name}.md` · `queue/runs/{D}_{T}_INTAKE.md` | `queue/rows/{name}.md` · `queue/proposals/{name}.md` | `_REGISTER.md` · `register.csv` · `queue/TODO.md` · `queue/DRAFT_QUEUE.md` |

- `K` is the branch key or, after a §7.1a re-key, the key of the memo added. `D` and `T` in every added name equal the branch's D and T.
- No job touches `model/`, `routines/`, `.claude/` or `.github/`, any path with a segment starting with `.`, or any file named `CLAUDE.md`, `CLAUDE.local.md`, `AGENTS.md` or `README.md`. Only `.md` files, plus INTAKE's `register.csv` and its `.csv` snapshot. Only adds, deletes and modifications — no renames (a move shows as a delete plus an add of the same bytes: REVIEW's prior memo, INTAKE's proposal).
- **The register changes only through `routines/tools/gsc_register.py`** (MODEL §7.1): `_REGISTER.md` and `register.csv` are modified together or not at all, and their snapshots share N and date.
- Archives are byte copies: each register snapshot equals the outgoing `_REGISTER.md` (and its `.csv` twin the outgoing `register.csv`), each TODO and DRAFT_QUEUE archive the outgoing file, each archived proposal the deleted `queue/proposals/` file, and REVIEW's archived memo the deleted `memos/{K}/` file.
- **One file per memo folder (MODEL §6, §6.6).** The check lists `memos/{K}/` in git: for a REVIEW it holds exactly the prior at the merge base and on the current `main`, and exactly the new memo at the PR head; an ANALYSE memo needs `memos/{K}/` and `archive/memos/{K}/` to be absent at the merge base and on `main`. A listing that fails fails the check.
- **`archive/` is append-only (MODEL §7.5):** a routine only adds files there, never modifies or deletes one. `registers/` and `queue/archive/` are retired paths: nothing is written there.

A run that wants anything else changed puts it in its row file (queue updates, TODO additions, Open items, IDEAS candidates) or in its run note. INTAKE applies row-file content. Nothing reaches `queue/IDEAS.md` without an attended session.

## 4. Row file — `queue/rows/{D}_{T}_{JOB}_{KEY}.md` (`{D}_{T}_SWEEP.md`; keyless ANALYSE `{D}_{T}_ANALYSE.md`)

```
---
row_type: ANALYSE | REVIEW | INCOMPLETE | PRIOR | SWEEP | QUEUE
key: KEY                         # omitted for SWEEP and QUEUE
company: Company name            # omitted for SWEEP and QUEUE
isin: XX0000000000               # "n/a — not established" if unknown
memo_path: memos/KEY/KEY_YYYY-MM-DD_GSC.md                   # ANALYSE/REVIEW only
evidence_path: queue/evidence/KEY_YYYY-MM-DD_INCOMPLETE.md   # INCOMPLETE only
run_date: YYYY-MM-DD             # = D
run_time: HHMM                   # = T
run_base: <HEAD sha at preflight>
model_version: vX.Y.Z            # as read from the live file
held: true | false
pr_title: GSC … (as final)
---
## Register row (new)
| Ticker | Company | … |   all three table lines row-from-memo --table prints: header, separator, row |
## Replaces
| … the key's current row in _REGISTER.md, verbatim … |   or   new name
## Portfolio row                    (held names only) the 7-column §7.2 table row-from-memo --table prints: header, separator, row
## Queue update                     one line per key, e.g. DRAFT_QUEUE: KEY → [x]  or  DRAFT_QUEUE: KEY → [x] prior — REVIEW
                                    or  DRAFT_QUEUE: KEY → [x] retired  or  DRAFT_QUEUE: KEY → [x] no listed security (ANALYSE.md steps 2 and 5)
                                    (a dependency pick, ANALYSE.md step 2: Group dependency: KEY → prior KEY2  or  Group dependency: KEY → memo exists
                                    or  Group dependency: KEY → retired  or  Group dependency: KEY → no listed security)
## Group dependency                 (ANALYSE or REVIEW of a group) one line per material controlled listed subsidiary or listed holding read as ungradeable for want of a current memo:
                                    `HKEY` — subsidiary of PARENT, memo missing  or  `HKEY` — holding of PARENT, memo stale {memo date}
## TODO additions                   one bullet each, dated trigger, or "none"
## Open items                       ADD: <one-line entry> · UPDATE <KEY>: <one-line entry> · CLEAR <KEY>: <reason> · or "none"
## IDEAS candidates                 one bullet each, or "none"
## Portfolio table                  (SWEEP only) | Ticker | Avg cost | Current | Zone (ADD / HOLD / SELL-FLAG) | Distance to ADD band | Distance to sell-flag line | — every held name; the Zone cell starts with the zone word (gsc-automerge holds the PR only when a held name is missing or its Zone cell has no zone word; zone changes merge and appear in the digest, J11)
## Price/ordering refresh           (SWEEP only) | Key | Px | Px unit | Close date | Source |
## FX                               (SWEEP only) | Pair | Rate | Date |
## Unit or instrument mismatches    (SWEEP only) KEY — unit | instrument | session | split — detail, one per line, or "none"
## Review requests                  (SWEEP only) KEY — reason, one per line; the reason starts with its class: held {zone} · held zone {Portfolio} → {sweep} · IN RANGE · move · split
## Held names — info only           (SWEEP only) KEY — zone — decision recorded
```

- `row_type: QUEUE` is the keyless ANALYSE row: only `## Queue update` (prior and retired markers found while walking the queue and the `▶ Group dependencies` block).
- `row_type: PRIOR` is a keyed ANALYSE run that stopped before a memo: a prior found under another key (`prior found (REVIEW)`), or a name with no listed security (`stopped: no listed security`, ANALYSE.md step 5) [v4.6.0]. It carries `## Queue update` and no register row.
- `## Group dependency` (MODEL §2 Group dependencies) [v4.6.0; G4] appears in a group parent's ANALYSE or REVIEW row whose memo read a material listed subsidiary or holding as ungradeable because its memo is missing or stale (ANALYSE.md step 5; a part on a venue the price endpoint does not serve is not listed): the parent completes, and the line queues the part. Each line names a controlled listed subsidiary (`subsidiary of`) or a non-controlled listed holding (`holding of`). INTAKE adds each line to the `queue/TODO.md` head block `▶ Group dependencies` (INTAKE.md step 3), where ANALYSE (no memo) or REVIEW (stale memo) takes the subsidiary or holding first; when its memo lands, INTAKE lists the parent `parent re-run owed` for REVIEW priority 1c. Before v4.6.0 the same lines rode on an `INCOMPLETE (dependency: KEY)` row; INTAKE applies a pending one once (INTAKE.md step 3, Legacy rows).
- `## Register row (new)` and `## Portfolio row` are pasted from `python3 routines/tools/gsc_register.py row-from-memo memos/{KEY}/{KEY}_{D}_GSC.md --table`; never typed by hand. Paste every line of each table it prints: the header line, the `|---|` separator and the row. gsc-automerge finds the Verdict cell by the header line, so a row without its header reads as no verdict and the PR is held (PR 87, 2026-10-07). `lint-row` (§5) checks the paste [v4.5.2].
- `## Open items` follows MODEL §7.1: only pending user decisions and register-integrity holds, one line each. INTAKE applies them to the `queue/TODO.md` head block `▶ Open items (register)`. A run never clears a pending user decision; only Jakub decides. A closed take-private or merger, a registered squeeze-out or an effective delisting that a run finds for a register name is raised here as `ADD: KEY — delisting awaiting retirement (§7.1 RETIRED) — {event}, {date}, {source}` (QUEUE-SEED carries the same line in its proposal's section 5). No routine retires a key: `gsc_register.py retire` is attended only, and the guard hook refuses it in routines (MODEL §7.1 RETIRED) [v4.6.0; G5].
- In the SWEEP refresh, `Px` is a plain number (no symbol, no separator) in the endpoint's `currency`, written verbatim in `Px unit` (it must equal the row's `px_unit`); `Close date` is `YYYY-MM-DD`. `## FX` rates are major-unit rates written `{core_currency}/{px currency}` (px currency per 1 core_currency, e.g. `USD/GBP` for a GBp line reporting in USD), ECB reference via frankfurter, else the endpoint's `{CCY1}{CCY2}=X` close.

**Memo wins.** INTAKE builds each ANALYSE or REVIEW row from the current memo — the one file in `memos/{KEY}/` — with `gsc_register.py apply`, from the memo's front matter alone. Row files carry no register annotations (MODEL v4.5.0). The held flag is never taken from a memo: a `position` that disagrees with the register is an open item for Jakub. Nor is the RETIRED state, which only an attended `retire` sets: INTAKE holds back a row for a RETIRED key with a TODO item, because `apply` refuses it (MODEL §7.1 RETIRED; INTAKE.md step 3) [v4.6.0].

## 5. Standing rules for every job

- **Never ask a question.** If something is ambiguous, write a run note naming it and stop.
- **Never re-read the clock for a date.** D is the memo's `memo_date`, the row's `run_date` and every date the run writes, even after midnight.
- **REST only.** Every GitHub call is a §1 `gh api` form. No curl, no Python and no other client talks to GitHub. Read repo files from the clone.
- **Exactly one repository** stays attached (§0 step 6).
- **Run every command from the repository root.** Never `cd` into a subfolder; use paths.
- **Write files with the Write tool**, not shell heredocs: repo files, `/tmp/pr_body.md` and `/tmp` scripts.
- **Budgets (P14):** ANALYSE ~5 · REVIEW ~2, plus at most 4 due-check operations logged separately · SWEEP ~1 per name · QUEUE-SEED at most 15 discovery searches plus at most 8 decay-pass queries (one issuer each) · INTAKE none. These count exploratory search only. Primary-document retrieval, IR index pages, quote endpoints and GitHub calls are uncounted. Log the counts.
- **Data-completeness gate (D3).** INCOMPLETE means an input required by a gate or the cheapness leg exists in a primary document but could not be retrieved this run. That includes a record-limited shortfall where more years are published. History-limited records, "n/a — not disclosed" and §2·1C INDETERMINATE findings proceed to a memo exactly as in attended runs. On INCOMPLETE, don't write a memo. Write:
  - `queue/evidence/{KEY}_{D}_INCOMPLETE.md`: sourced figures, the named gaps, and the hosts tried; no verdict;
  - a row file with `row_type: INCOMPLETE`.

  Never fill a gap with an assumption to finish a memo or a row. Two named gaps belong to the MODEL method set (MODEL §8.1 step 3, §8.2 step 3, §8.7 item 6), for ANALYSE and REVIEW alike:
  - `INCOMPLETE (group build exceeds budget)`: a group build that cannot finish within the time budget. The build covers B4 with its weights and S, one Appendix D block per material unit, the holding credits at the three yardsticks, the listed-subsidiary NCI and the allocation-across-the-parts table (MODEL §2·1C·3, v4.6.0). `## TODO additions` carries `` `KEY` — attended group build owed ({JOB} {D}) ``.
  - `INCOMPLETE (method re-test exceeds budget)`: a REVIEW of a memo below v4.5.0 or v4.6.0 whose re-test on the method rules it predates (every v4.5.0 rule; the v4.6.0 Gate-0, lens and group rules and the G6 pairing; MODEL §8.2 step 3) cannot finish within the time budget. `## TODO additions` carries `` `KEY` — attended re-test owed (REVIEW {D}) ``.

  ANALYSE and REVIEW skip a key while either `attended … owed` item is open in `queue/TODO.md`; Jakub deletes it after the attended run.

  **A group dependency is never a gap [v4.6.0; G4].** `INCOMPLETE (dependency: KEY)` and verdict invariance are retired (MODEL §2 Group dependencies). A material controlled listed subsidiary or material listed holding (P22) without a current memo of its own (no more than 15 months old and written under MODEL v4.5.0 or later; a DNAF memo written below v4.6.0 is stale), or with a DNAF memo, a `[!]`-marked `▶ Group dependencies` line or an unserved venue, is ungradeable: it counts WEAK with its weight in the weighted Future (`sub dependency`), adds nothing to the look-through Past and earns no credit (the band prints `credit owed`, and `holding_keys` lists only the memos read). A non-controlled holding is read as a G6 class throughout (an equity-accounted one as an associate, any other as S3; on the G6 readings in Gate 1A, P31; no credit at Gate 2), and the part's SF is INDETERMINATE (b) for the parent; while ungradeable parts carry more than a third of the P29 weight base, the group Future is WEAK (ANALYSE.md step 5). The run completes, and its row lists each part whose memo is missing or stale under `## Group dependency` (§4), a part on an unserved venue excepted. A legacy row with that gap still pending is applied once (INTAKE.md step 3, Legacy rows).
- **Compliance re-measure before the final push (MODEL §7.4a).** A run's own compliance claim is not evidence.
  - What to check: the P13 body word count, the §7.1 160-character cell cap (the `row-from-memo --table` cells), the four-gates-only check, and no register-wide superlatives.
  - **Machine fields (MODEL §6.1, §7.1b)**, for an ANALYSE or REVIEW memo: `python3 routines/tools/gsc_register.py lint-memo memos/{KEY}/{KEY}_{D}_GSC.md` exits 0. It checks:
    - **Presence.** Every v4.5.0 field is present and none is `-`: `aliases px px_unit px_date trigger mcap_fcf ev_oi ev_oi_all_cash trigger_basis mcap_fcf_3y mcap_fcf_5y ev_oi_3y ev_oi_5y lens holding_keys core_credit core_period core_currency core_unit core_shares_diluted core_debt_eq core_cash core_oi core_oi_basis core_fcf core_fcf_basis core_oi_3y core_oi_5y core_fcf_3y core_fcf_5y core_fcf_all core_fx core_fx_date core_ratio past_reason future_reason sf_reason next_review_short`. No retired field (`sotp_keys`, `core_credit_fix`, `core_credit_mkt`, `core_credit_px`) appears.
    - **Forms.** The enumerations are one bare word. `px` and `trigger` are numbers in `px_unit`, the price endpoint's `currency` as recorded in Appendix F (`trigger` may be `n.m.`). `next_review_short` has its form. `core_fx` is a major-unit rate.
    - **Reasons** (the §7.1 vocabulary):
      - A `unit` or `sub` prefix appears only in a group memo, one with a line starting `B4 Division table`.
      - `{x}% ROE` appears only under FI (which never writes ROCE), or on a prefixed group part.
      - A Future ADEQUATE prints `n.m.` or its concentration caveat (`customer conc.`, `supplier conc.`).
      - A PASS never carries `alignment`, `flag pair` or `inherited`.
      - Where several reasons decide one grade, the cell takes the first failing one in the vocabulary's order (a failing `{x}% ROCE` level first), and the memo body names the others (MODEL §7.1 Precedence).
    - **Recomputation.** `mcap_fcf`, `ev_oi` and `ev_oi_all_cash`, and the four averaged multiples, are recomputed from the core numbers and `core_credit` at `px` (MODEL §7.1b), with the 3-year and 5-year averages in place of `core_oi` and `core_fcf` for the averaged ones. They must match the printed values within ±0.1, or be `n.m.` exactly when the base is ≤ 0 (and EV/OI under FI).
    - **The trigger is the no-cash bound (R10).** `trigger_basis` is `no-cash`. At `trigger`, MCap/FCF ≤ 8.0 and EV/OI no-cash ≤ 7.0 (to 0.1), with the binding one at its threshold (FI: the MCap/NI leg only). A held name's `add_band` equals `trigger`.
    - **The lens (MODEL §6.1).**
      - `lens` is STD or FI (`n.m.` only in a Gate-0 DNAF memo).
      - Under FI, `core_oi`, `core_debt_eq`, `core_cash`, `core_oi_3y`, `core_oi_5y` and `core_fcf_all` are `n.m.`.
      - `core_credit` is a number ≥ 0, non-zero only under STD with `holding_keys` set, and then `## F.` carries the `Holding credits` table.
      - `holding_keys` is `n.m.` or `;`-separated §7.1a keys; any value other than `n.m.` needs a line starting `B4 Division table`.
    - **The bases.**
      - `core_oi_basis` follows `{FY####|TTM Qn-YYYY|LTM Qn-YYYY|FY####–FY#### avg} {J1|NI basis}[ · lease-capitalised][ · down-year avg][ · fin. income out]`. Its line fits the lens (STD `J1`, FI `NI basis`), and it never names an adjusted, underlying, before-special or ex-{charge} line (J1).
      - `core_fcf_basis` follows `{period} CFO − maint. capex ({disclosed|constructed|= all capex})[ · down-year avg][ · fin. income out]`, or `{period} NI basis[ · down-year avg]` under FI.
      - An average period appears only with ` · down-year avg` (P28; an FI P1-average NI basis aside). `core_oi` (or `core_fcf`) then equals the lower of its 3-year and 5-year averages exactly.
      - Off the down-year path, `core_fcf_all` ≤ `core_fcf`, and the two are equal under `= all capex` (P20, R6).

    Paste its output. Its `WARN` lines (px vs `price_at_memo`, trigger vs the no-cash bound `trigger_band` states first, an unusual `px_unit`) are checked by eye and explained in the PR body. A `FAIL` is a breach.
  - How: write a short script to `/tmp`, run it with `python3`, count characters (not bytes), and paste the numbers into the PR body.
  - **Row file [v4.5.2]**, for every ANALYSE, REVIEW and SWEEP row file: `python3 routines/tools/gsc_register.py lint-row queue/rows/{file}` exits 0, and its output goes into the PR body. It reads the file the way gsc-automerge does and checks:
    - the file name against `row_type`, `key`, `run_date` and `run_time`, and that `pr_title` starts with the job's title word;
    - for a verdict row (ANALYSE or REVIEW): `memo_path` is the run's memo, `## Register row (new)` (and `## Portfolio row` for a held memo) is exactly what `row-from-memo --table` prints for it, header and separator included, and the row table's verdict equals the memo's and the one in `pr_title`;
    - for a SWEEP: `## Portfolio table` is present, with its header line naming the Ticker and Zone columns.
    The gsc-guard check runs the same lint on the PR head, so a row that fails it shows a red guard check.
  - **Self-containment (MODEL §6.6)**, for a full ANALYSE or REVIEW memo, in the same script:
    1. the body headings `## 1.`–`## 8.` and the appendix headings `## A.`–`## G.` each appear exactly once;
    2. under `## B.`, the B1 block (a heading or line starting `B1`) holds a Markdown table with a row for each fiscal year in `window:` (N years; a row's first cell names its fiscal year, e.g. `2025`, `FY2025`, `3/26`), and the B2 and B3 blocks each hold one with at least N − 1 such rows (a growth or beginning-of-period series may start a year later);
    3. the body and Appendices A–F match neither `(?i)\b(unchanged from|see|as in|incorporated by reference (from|to|in)) v\d+\b(?!\.\d)` nor `(?i)\b(delta only|not repeated)\b[^.\n]{0,80}\bv\d+\b(?!\.\d)` — pointers to an earlier memo version; a dotted model version such as v4.5.0 never matches, and "incorporated by reference in the 10-K" is not a pointer;
    4. no memo file name — `_GSC.md`, `_GSC_superseded-v{n}.md`, or this key's `{KEY}_YYYY-MM-DD_GSC` — appears outside the `supersedes:` line and Appendix G;
    5. REVIEW only: `memo_version` matches `^v\d+$` and is one more than the prior's (REVIEW.md step 5), and `supersedes:` equals `archive/memos/{KEY}/{P_FILE}`.

    A §6.4 Gate-0 memo skips checks 1–4; a REVIEW Gate-0 memo still runs check 5 and carries `## G.`. Paste the five results into the PR body.
  - On a breach: fix it and re-measure. If it can't be fixed, the run is INCOMPLETE.
- **Register computations run only through `routines/tools/gsc_register.py`** (MODEL §7.1, §7.1b): a register row, a multiple (credits included), a trigger distance or status, a sort order or a register check is never computed by a `/tmp` script. Run it from the repository root as `python3 routines/tools/gsc_register.py <command>`; never edit it (framework-locked).
- **Register page (MODEL §7.4).** `routines/tools/gsc_site.py` renders the register as one plain-language page for third parties: `python3 routines/tools/gsc_site.py render --out /tmp/gsc-register-page.html` (`stats` prints extraction coverage). It only reads the repo and writes the `--out` file; never edit it (framework-locked). Only INTAKE publishes the page, best-effort, in place to the one private artifact (`register_page` in `CLAUDE.md`; `routines/INTAKE.md` step 9). No other job uses the Artifact tools (the guard hook refuses them), and the page is never committed.
- **Time budget.** After about 90 minutes of work, or under context pressure, stop. Push what is complete (INCOMPLETE if the memo isn't), finish the run note, and finish the PR (§1).
- **Long commands.** A Bash command is cut off after 10 minutes. Run long downloads or extractions in the background, or in chunks.
- **One name per ANALYSE or REVIEW run.** Never start a second.
- **Phone pushes (PushNotification) — MODEL §8.7 item 11.** Send at most one push per class per run, after the PR is finished (INTAKE's `STALL` push is the one exception: it goes at step 0, before any PR, and says `PR -`), and only for:
  - `BUY`: an ANALYSE or REVIEW memo with verdict BUY;
  - `HELD`: any REVIEW of a held name;
  - `VERDICT CHANGE`: a REVIEW whose verdict differs from the prior memo's;
  - `STOPPED` / `BLOCKED`: a run whose final title outcome starts `stopped:` / `blocked:`;
  - `STALL`: INTAKE's watchdog (INTAKE.md step 0).

  Format: `GSC {CLASS} · {JOB} {KEY} {D} · PR {n} · {one-line reason}` (keyless jobs omit KEY; `PR -` when no PR exists), one line, at most 200 characters, no `#`. Never push for any other outcome: WATCH, AVOID, DNAF, INCOMPLETE, prior found, every SWEEP, SEED and a routine INTAKE reach Jakub through the morning digest (gsc-notify). A SWEEP zone change reaches Jakub through the digest (MODEL §8.7 items 10–11, J11): the SWEEP merges and the digest lists it under `## Held zone changes (SWEEP)`. The guard hook refuses any other push, including a class sent from a job other than the one named above (`HELD` from a SWEEP included). A push that the app reports as not sent is not retried.
- **Run note** at the §1 path, ≤ 300 words, per `queue/runs/README.md`:
  - `model_version` read and the base sha
  - what was written
  - what failed, with host and reason
  - what needs Jakub, one line each
- **SEC.** Every request to a `sec.gov` host sends the `sec_user_agent` value from the `CLAUDE.md` Config block: `curl -sS -A "<sec_user_agent>" "<url>" -o /tmp/<file>`. WebFetch can't set the header, so use curl for SEC. If the value still holds a `{{…}}` placeholder, don't call SEC at all: log "SEC user agent not configured" and treat SEC documents as unretrievable.
- **Retrieval hints.** These are subordinate to MODEL §4: hints, not rules.
  - **SEC filers:** a 10-Q's Item 1 and the earnings-release 8-K exhibits carry full statements early in the document. A 10-K truncates before Item 8. `FilingSummary.xml` → `R1.htm` is the cheapest primary share count.
  - **Japan:** use the kabupro.jp EDINET mirror for yūhō PDFs, and company tanshin stores.
  - **FX:** `api.frankfurter.dev/v1/{YYYY-MM-DD}?from={BASE}&to={CCY}` (ECB reference). Record the returned date and label it "ECB ref, {date}". The ECB has no rate for some currencies (TWD, SAR, AED, QAR, KWD, ARS, CLP, COP, VND, among others): use the price endpoint's `{CCY1}{CCY2}=X` daily close and label it "endpoint FX, {date}". Rates are major units (GBP, ZAR, ILS, KWD), never minor.
  - **Prices:**
    - The price endpoint is `query1.finance.yahoo.com/v8/finance/chart/{symbol}` (MODEL §7.1a; a US class share's dot becomes a hyphen: `BRK.B` → `BRK-B`). Record `currency` (that is `px_unit`), `exchangeName`, the instrument name, the close and its date with every price.
    - `&events=split` lists splits and consolidations; a split since the register's `px_date` means the core numbers are pre-split.
    - Provider market caps use the issued count; value per share uses the net count.
  - **Corporate actions:** one issuer per query.
  - **Primary PDFs:** save them to `/tmp` only and read them with the Read tool or `pdftotext`. Never commit a PDF.
