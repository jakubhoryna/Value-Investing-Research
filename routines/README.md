# routines/ — shared protocol for scheduled GSC runs (MODEL §8.7)

Every routine's saved prompt is one line:

```
GSC ROUTINE: <JOB> — follow routines/README.md and routines/<JOB>.md exactly.
```

`<JOB>` is one of `ANALYSE · REVIEW · SWEEP · INTAKE · QUEUE-SEED`. Everything a run needs is in this repo. This folder is framework-locked: it changes only under "commit model".

---

## 0. Preflight — in this order; stop at the first failure

1. **Session start.** Complete the `CLAUDE.md` session start: HEAD sha, `model_version` ≥ v4.4.0, register read, private check.
2. **Environment.** `echo "$GSC_SESSION"` must print `routine`. If it doesn't, the run is in the wrong environment and the guard is inactive.
3. **Guard live.** Both must hold:
   - `git ls-files --error-unmatch .claude/settings.json .claude/hooks/gsc_guard.py` succeeds;
   - the canary `: git push origin main`, run as its own Bash command, is **refused** with a message containing `GSC guard`. (`:` is a no-op, so the canary is harmless when the guard is off.)

   If the canary runs (exit 0) or the files are untracked, the guard is off.
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
# ledger (all pages) — §0 step 4
gh api --paginate "repos/jakubhoryna/Value-Investing-Model/pulls?state=all&per_page=100&sort=created&direction=desc" --jq '.[] | [.number, .state, (.merged_at // "-"), .updated_at, .head.ref, .title] | @tsv'
# claim: create the PR, keep the number it prints
gh api "repos/jakubhoryna/Value-Investing-Model/pulls" -f head="{BR}" -f base=main -f title="GSC … [running]" -f body="Claim — run in progress. Do not merge." --jq .number
# state check before finishing
gh api "repos/jakubhoryna/Value-Investing-Model/pulls/{n}" --jq '[.state, .merged] | @tsv'
# finish: one PATCH, title + body from the file
gh api -X PATCH "repos/jakubhoryna/Value-Investing-Model/pulls/{n}" -f title="GSC … — …" -F body=@/tmp/pr_body.md
# comment
gh api "repos/jakubhoryna/Value-Investing-Model/issues/{n}/comments" -f body="…"
# close an abandoned claim (INTAKE only, §2)
gh api -X PATCH "repos/jakubhoryna/Value-Investing-Model/pulls/{n}" -f state=closed -f title="… [abandoned]"
```

Never merge. Never `gh pr …`. Never `gh api graphql`. Never PUT or DELETE. Never PATCH a PR's `base`.

**Git commands — exact forms.**

```
git fetch origin main
git switch --no-track -c "{BR}" origin/main
git add <explicit paths>          # never -A on a run branch
git commit -m "…"
git push -u origin "{BR}"         # the ONLY push form; repeat it for later pushes
git merge --no-edit origin/main   # the only way to absorb a moved main (INTAKE restart)
```

Never rebase, reset, amend, cherry-pick onto or force-push a pushed run branch. Never push any other ref. Never touch another run's branch or PR, except INTAKE under the abandoned-claim rule (§2).

**Finishing a run.**
1. Final commit and `git push -u origin "{BR}"`.
2. State check. If the PR is still open, send the one finishing PATCH.
3. If it is no longer open (merged early or closed), open a **new** PR from the same branch with the final title, and start its body with "Replaces #{n}, which was {merged | closed} before the run finished."
4. If PR creation fails after a successful push, retry once. If it fails again, name the branch in the run note, push the note, and stop. INTAKE's audit lists branches that have no PR.

## 2. Claim ledger

A key is **claimed** for a job family (ANALYSE or REVIEW) if the ledger shows either of these for it. Match titles with `^(HELD · )?GSC (ANALYSE|REVIEW) {KEY} ` — note the trailing space, so `ABC` never matches `ABCD`.

- an open PR with that title, whatever its state (`[running]`, finished, `[fixing]`);
- a closed, unmerged PR with that title updated in the last **90 days for ANALYSE** or the last **7 days for REVIEW**. This means Jakub rejected it. Closed PRs whose title ends `[abandoned]` or still ends `[running]` don't count; they were abandoned, not rejected.

**Override:** a queue line for the key that carries the word `retry` (added by Jakub) makes the key eligible despite a rejection. To retry, Jakub rewrites the line as `- [ ] KEY — Company — route — notes — retry (PR #n)`: he drops `rejected {D}`, keeps the KEY right after the marker, and moves `(PR #n)` into the trailing note. INTAKE's marker replacement never touches that note, and the number in it stops INTAKE recording the old rejection again.

Compare `updated_at` (UTC) with `date -u +%s`, never with Prague time.

**Abandoned claim — executed only by INTAKE (daily).** An open PR whose title ends `[running]` and whose `updated_at` is more than 6 hours old:
1. Comment one line: "No update for > 6 h — closed as abandoned by INTAKE {D}."
2. Close it with the single PATCH in §1, the title ending `[abandoned]` in place of `[running]`.

Its key becomes eligible again. Until INTAKE closes it, every other job treats it as a claim and skips the key. To keep a stalled run for repair, Jakub retitles its PR to end `[fixing]`; the rule never touches that.

**Stalled key.** A key with two abandoned PRs (title ending `[abandoned]`, or closed while still `[running]`) of the same job within 14 days, `#a` the earlier and `#b` the later:
- **ANALYSE key.** INTAKE marks its `[ ]` queue line `[!] stalled {D} (PR #a, #b)`, and ANALYSE skips it until Jakub edits the line. To release it, Jakub rewrites the line as `- [ ] KEY — Company — route — notes — reset (PR #a, #b)`, keeping the numbers in the trailing note.
- **REVIEW key.** It has no queue line: INTAKE adds a TODO item `` `KEY` — REVIEW stalled {D} (PR #a, #b) ``. REVIEW skips the key until 14 days have passed since `#b` was closed (its `updated_at`).

INTAKE records a stalled key only once: only if `#b` appears nowhere in `queue/DRAFT_QUEUE.md` (ANALYSE key) or `queue/TODO.md` (REVIEW key), as a whole number. A third abandonment brings a new `#b`, so it is recorded again.

**Claim before any research:**
1. `git fetch origin main`, then `git switch --no-track -c "{BR}" origin/main`.
2. Commit the run-note stub `queue/runs/{D}_{T}_{JOB}[_{KEY}].md`: job, key, D, T, base sha, status *in progress*.
3. `git push -u origin "{BR}"`.
4. Open the PR (§1) and keep its number.

Only then fetch anything from the web. The one exception is REVIEW's due-check operations (REVIEW.md step 2), which happen before the claim.

## 3. Write contract — single writer

Checked on every routine PR by the `gsc-guard` check (`.github/workflows/gsc-guard.yml`). On GitHub Free that check is advisory, so the guard hook and this contract are what hold.

| Job | May add | May delete | May modify |
|---|---|---|---|
| ANALYSE | `memos/{K}/{K}_{D}_GSC.md` (at most one memo) · `queue/rows/{D}_{T}_ANALYSE_{K}.md` · `queue/rows/{D}_{T}_ANALYSE.md` · `queue/runs/{D}_{T}_ANALYSE[_{K}].md` · `queue/evidence/{K}_{D}_INCOMPLETE.md` | `queue/evidence/{K}_*.md` | nothing |
| REVIEW | the same with `REVIEW`, except the keyless row file; the memo key must equal the branch key | `queue/evidence/{K}_*.md` | nothing |
| SWEEP | `queue/rows/{D}_{T}_SWEEP.md` · `queue/runs/{D}_{T}_SWEEP.md` | — | nothing |
| QUEUE-SEED | `queue/proposals/{D}_{T}_QUEUE-SEED.md` · `queue/runs/{D}_{T}_SEED.md` | — | nothing |
| INTAKE | `registers/{YYYY}/REGISTER_v{N}_{date}.md` · `queue/archive/TODO_v{n}_{date}.md` · `queue/archive/DRAFT_QUEUE_v{n}_{date}.md` · `queue/archive/proposals/{name}.md` · `queue/runs/{D}_{T}_INTAKE.md` | `queue/rows/{name}.md` · `queue/proposals/{name}.md` | `_REGISTER.md` · `queue/TODO.md` · `queue/DRAFT_QUEUE.md` |

- `K` is the branch key or, after a §7.1a re-key, the key of the memo added. `D` and `T` in every added name equal the branch's D and T.
- No job touches `model/`, `routines/`, `.claude/` or `.github/`, any path with a segment starting with `.`, or any file named `CLAUDE.md`, `CLAUDE.local.md`, `AGENTS.md` or `README.md`. Only `.md` files. Only adds, deletes and modifications — no renames (INTAKE's proposal move shows as a delete plus an add of the same bytes).
- INTAKE's archives are byte copies: each register snapshot equals the outgoing `_REGISTER.md`, each TODO and DRAFT_QUEUE archive the outgoing file, and each archived proposal the deleted `queue/proposals/` file.

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
| … the complete §7.1 row, generated from the memo front matter … |
## Replaces
| … the current row, verbatim … |   or   new name
## Portfolio row                    (held names only)
## Queue update                     one line per key, e.g. DRAFT_QUEUE: KEY → [x]  or  DRAFT_QUEUE: KEY → [x] prior — REVIEW
## TODO additions                   one bullet each, dated trigger, or "none"
## Open items                       ADD: <one-line entry> · UPDATE <KEY>: <one-line entry> · CLEAR <KEY>: <reason> · or "none"
## IDEAS candidates                 one bullet each, or "none"
## Price/ordering refresh           (SWEEP only) | Key | Px | Close date | Source |
## Review requests                  (SWEEP only) KEY — reason, one per line
## Held names — info only           (SWEEP only) KEY — zone — decision recorded
```

- `row_type: QUEUE` is the keyless ANALYSE row: only `## Queue update` (prior markers found while walking the queue).
- `## Open items` follows MODEL §7.1: only pending user decisions and register-integrity holds, one line each. A run never clears a pending user decision; only Jakub decides.
- In the SWEEP refresh, `Px` is written in the currency and instrument form of the row's current Px cell, and `Close date` as `YYYY-MM-DD`.

**Memo wins.** INTAKE builds each ANALYSE or REVIEW row from the latest non-superseded memo in `memos/{KEY}/`. Front-matter fields win for verdict, gates, memo date, version, Px and band. Annotation tokens (the SF flag note, the notes cell) come from the row file, within the 160-character cap. INTAKE logs a disagreement only on front-matter fields.

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

  Never fill a gap with an assumption to finish a memo or a row.
- **Compliance re-measure before the final push (MODEL §7.4a).** A run's own compliance claim is not evidence.
  - What to check: the P13 body word count, the §7.1 160-character cell cap, the four-gates-only check, and no register-wide superlatives.
  - How: write a short script to `/tmp`, run it with `python3`, count characters (not bytes), and paste the numbers into the PR body.
  - On a breach: fix it and re-measure. If it can't be fixed, the run is INCOMPLETE.
- **Time budget.** After about 90 minutes of work, or under context pressure, stop. Push what is complete (INCOMPLETE if the memo isn't), finish the run note, and finish the PR (§1).
- **Long commands.** A Bash command is cut off after 10 minutes. Run long downloads or extractions in the background, or in chunks.
- **One name per ANALYSE or REVIEW run.** Never start a second.
- **Run note** at the §1 path, ≤ 300 words, per `queue/runs/README.md`:
  - `model_version` read and the base sha
  - what was written
  - what failed, with host and reason
  - what needs Jakub, one line each
- **SEC.** Every request to a `sec.gov` host sends the `sec_user_agent` value from the `CLAUDE.md` Config block: `curl -sS -A "<sec_user_agent>" "<url>" -o /tmp/<file>`. WebFetch can't set the header, so use curl for SEC. If the value still holds a `{{…}}` placeholder, don't call SEC at all: log "SEC user agent not configured" and treat SEC documents as unretrievable.
- **Retrieval hints.** These are subordinate to MODEL §4: hints, not rules.
  - **SEC filers:** a 10-Q's Item 1 and the earnings-release 8-K exhibits carry full statements early in the document. A 10-K truncates before Item 8. `FilingSummary.xml` → `R1.htm` is the cheapest primary share count.
  - **Japan:** use the kabupro.jp EDINET mirror for yūhō PDFs, and company tanshin stores.
  - **FX:** `api.frankfurter.dev/v1/{YYYY-MM-DD}?from={BASE}&to={CCY}` (ECB reference). Record the returned date and label it "ECB ref, {date}".
  - **Prices:**
    - Record the instrument, venue, close and close date with every price.
    - Run one price × shares = market cap check.
    - Provider market caps use the issued count; value per share uses the net count.
  - **Corporate actions:** one issuer per query.
  - **Primary PDFs:** save them to `/tmp` only and read them with the Read tool or `pdftotext`. Never commit a PDF.
