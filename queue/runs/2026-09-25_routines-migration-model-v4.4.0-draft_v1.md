# MODEL v4.4.0 + BOOTSTRAP v1.3.0 — routine migration (DRAFT for MODEL mode)

**Status:** proposal only. Nothing here is operative until an attended MODEL session applies it to the live `model/MODEL.md`, prints the full diff, and receives the exact words **"commit model"**.
**Base:** MODEL v4.3.0 (2026-09-12) as mirrored on 2026-09-25. The session must base-verify against the live file and rebase if it has moved.
**Release class:** MINOR (v4.3.0 → v4.4.0). This adds a mode and changes commit mechanics. No analytical mechanics move (§2–§6 untouched), so the §8.4 step-3 scan should find zero flips; the session confirms this.
**Ships with:** BOOTSTRAP v1.3.0 (the project-settings text, §E below; pasted by hand) and the new repo bootstrap `CLAUDE.md` (BOOTSTRAP-CC v1.0.0), together with `.claude/`, `.github/`, `routines/`, `queue/rows/` and `queue/proposals/`. All are on the same branch.

---

## Why (evidence, all from the repo and the project)

1. **Scheduled runs can't reach the repo without an attached source.** Every Cowork scheduled task was created without a repository. The session proxy answers 403 *"GitHub access to this repository is not enabled for this session. Use add_repo…"*. This was re-confirmed on 2026-09-25 and is identical to the 2026-09-09 post-mortem (§5A).
2. **The DRAFT workaround depended on a human upload that never happened.** DRAFT (v4.3.0) needed two project *files* that no session can write, and aborted six times on 13–14 Sep. All six tasks were disabled on 15 Sep.
3. **The PAT exposure is structural.** The token line sits in the project-settings bootstrap, which is delivered into every transcript, including the 2026-09-25 session. Rotating the token doesn't fix this; removing it does.
4. **The fix exists.** Claude Code routines clone attached repositories and provide git and GitHub API access through a proxy that keeps credentials outside the session VM. Pushes go to `claude/`-prefixed branches, and routines run on the subscription. *Sourced: code.claude.com/docs/en/routines and …/cloud-environments, read 2026-09-25; research preview.*

## Decisions this release takes (Jakub confirms or amends in the MODEL session)

- **D1 — The gate is PR-merge, not direct push.** This departs from the 2026-09-09 post-mortem §5B, which recommended runs push to `main` under scripted guards. The reasons:
  - The resident guardrail requires a printed diff plus an explicit confirm, and a PR is exactly that.
  - v4.3.0 chose to keep a human intake gate for unattended output.
  - The post-mortem's objection (parallel branches break register numbering) is removed by the single-writer rule: only INTAKE writes the register, and only one INTAKE PR is open at a time.

  The cost is one merge click per result. *Alternative, if the clicks become the bottleneck:* let INTAKE PRs auto-merge. Only mechanical merging of already-approved rows would lose its gate.
- **D2 — Retire §8.6 DRAFT** and its project-files apparatus (card, project-file queue, inbox, RECONCILE intake of draft-inbox memos). ROUTINE reads the live MODEL, so its memos are real memos with the live `model_version`. `model/DRAFT_CARD.md` moves to `model/archive/`.
- **D3 — Data-completeness gate for routine runs.** An unattended run that cannot cleanly source any gate or cheapness input writes `queue/evidence/{KEY}_{date}_INCOMPLETE.md` instead of a memo. This adopts the TODO v28/v29 unattended-operation guardrail. No new verdict class is added.
- **D4 — Commits happen only in Claude Code sessions with the repo attached** (claude.ai/code, the desktop Code tab, the mobile Code tab, and routines). The claude.ai project becomes a read-only mirror for discussion. **The PAT is revoked and exists nowhere.**

---

## §A — new section, inserted after §8.6

### §8.7 ROUTINE [v4.4.0]

Unattended ANALYSE, REVIEW, SWEEP, QUEUE-SEED and INTAKE, run as scheduled Claude Code routines with this repository attached. **Trigger:** a session prompt beginning `GSC ROUTINE: <JOB>`. The playbooks are `routines/README.md` (the shared protocol) and `routines/<JOB>.md`. Both are framework-locked, and they bind as if written here.

1. **Host.**
   - Each run is a fresh cloud session with a fresh clone of `main`.
   - GitHub access comes through the session proxy. No credential exists in any file, prompt or environment variable, and none may be requested or created.
   - The routine environment sets `GSC_SESSION=routine`, which arms `.claude/hooks/gsc_guard.py`. A run whose preflight doesn't see it stops.
2. **Framework.** The run reads this file from the clone. Below v4.4.0 → evidence-only stop. Memos carry the live `model_version` plus `produced_by: ROUTINE` and `run_base: {sha}`.
3. **Commit gate.** Each run pushes one `claude/gsc-{job}-…` branch and opens one PR; the PR body is the §7.4a printed diff. **Jakub's merge is the confirm.**
   - A routine never merges, never pushes `main`, and is never covered by "auto-commit".
   - `main` is PR-only by ruleset.
4. **Single writer.**
   - ANALYSE, REVIEW, SWEEP and QUEUE-SEED only **add** files: memos, `queue/rows/`, `queue/proposals/`, `queue/runs/` and INCOMPLETE evidence. Their one deletion is the name's own evidence file.
   - Only INTAKE modifies `_REGISTER.md`, `queue/TODO.md` and `queue/DRAFT_QUEUE.md`, from merged row and proposal files, with a §7.5 snapshot. At most one INTAKE PR is open at a time.
   - The contract is checked on every routine PR by `.github/workflows/gsc-guard.yml`.
5. **Claims.** The PR title is the claim: `GSC {JOB} {KEY} {date} [running]`, opened before any research.
   - A key with an open PR, or with a closed-unmerged PR (ANALYSE 90 days, REVIEW 7 days), is claimed. A queue line marked `retry` overrides a rejection.
   - Stale `[running]` PRs (more than 6 h) are closed as `[abandoned]`, and their keys become eligible again.
6. **Budgets and gates.**
   - P14 applies: ANALYSE ~5, REVIEW ~2 plus up to 4 due-check operations, SWEEP ~1 per name, QUEUE-SEED 15 discovery.
   - The data-completeness gate (D3) applies.
   - The §7.4a compliance re-measure is done by script before the final push, with its numbers in the PR body.
   - One name per ANALYSE or REVIEW run, and about 90 minutes per run.
7. **Framework lock.** Routines never touch `model/**`, `CLAUDE.md`, `routines/**`, `.claude/**` or `.github/**`. MODEL mode stays attended-only, on "commit model".
8. **Held names.**
   - ANALYSE never takes a held name.
   - REVIEW may, and runs §8.2 step 4 in full. The PR title carries `HELD ·`, and the zone statement has standing only once merged.
   - Position events are never inferred.
9. **Standing.** A routine memo has standing when its PR is merged. Its register row lands at the next INTAKE, and the memo wins on any disagreement.

## §B — §7.4a replacement (git form)

Replace "Token handling", "Session start", "REVIEW memo load" and "Session end" with the text below. Keep base verification, the lost-update precedent, the compliance re-measure and the register generation rule verbatim.

> **Access [v4.4.0].** All repo reads and writes are git operations in a Claude Code session with this repository attached. The session's GitHub proxy supplies credentials. **No token exists in any file, prompt or environment**, and none may be requested, created or stored. GitHub API calls are data plumbing and never count against P14.
>
> **Session start.** Follow `CLAUDE.md`: `git fetch origin main`, record the HEAD sha, read this file and `_REGISTER.md` from the checkout, and warn once if the repo is not private.
>
> **REVIEW memo load.** List `memos/<KEY>/` in the checkout. The latest-dated `<KEY>_YYYY-MM-DD_GSC.md` that is not `_superseded-` is the prior memo. Confirm its date against the register row; the memo wins. If the folder is missing, run the §7.1a prior-check on company name and ISIN before concluding the name is new.
>
> **Session end (attended ANALYSE / REVIEW / RECONCILE).** After the memo is final, print the register diff and file list. On "commit", or under a session "auto-commit" with the diff still printed:
> 1. **Base verification:** run `git fetch origin main`. If `origin/main` has moved since the base and `_REGISTER.md` changed, re-merge this session's rows onto the fresh state (memo wins), renumber to live-head + 1, and re-print the diff. If an open `GSC INTAKE` PR exists, merge or close it first.
> 2. Write the memo at its new path.
> 3. Write the §7.5 snapshot with the outgoing register bytes unchanged.
> 4. Write the regenerated register.
> 5. Make one commit on a `claude/` branch, push, open the PR, squash-merge it via REST, and report the URLs. If the merge fails, hand over the PR link.
>
> Routine runs follow §8.7 and stop at the PR.

## §C — §8.6 DRAFT → tombstone

> ### §8.6 DRAFT [v4.3.0 — retired v4.4.0]
> Superseded by §8.7 ROUTINE, which reads the live framework from an attached clone. No draft-inbox memos exist; the six 13–14 Sep 2026 firings aborted before producing any. `model/DRAFT_CARD.md` is archived at `model/archive/DRAFT_CARD_v4.3.0_2026-09-12.md`. Kept as a heading so that historical references resolve.

## §D — consequential edits (the MODEL session makes each, in the same commit)

- **§0 release flow and §8.4 step 4:**
  - Drop the DRAFT_CARD regeneration and the "user uploads the card to project files" step.
  - Add: "if bootstrap territory changed, update `CLAUDE.md` (BOOTSTRAP-CC) and the project-settings bootstrap text."
- **§8.4 step 5:** "bootstrap" now means **both** `CLAUDE.md` (committed) and the project-settings text (re-pasted by hand). There is no token-redacted mirror any more; `model/BOOTSTRAP.md` becomes a copy of the project-settings text.
- **§8 intro mode list:** ANALYSE · REVIEW · SWEEP · MODEL · RECONCILE · ROUTINE [v4.4.0] (DRAFT retired).
- **§7.4 opening:** "Config lives in the BOOTSTRAP" → "Config lives in `CLAUDE.md`; no secret exists."
- **§8.5 RECONCILE step 2:** replace the draft-inbox intake clause with: "merged `queue/rows/` files are INTAKE's job (§8.7). RECONCILE handles attended backlog, past-chats recovery and triage." Step 4: commit per §7.4a (git form).
- **P14:** replace the DRAFT entry with "ROUTINE: as the underlying mode; REVIEW due-check ≤ 4 operations, logged separately; no directed-enquiry extension".
- **README.md (layout contract):**
  - add rows for `CLAUDE.md`, `.claude/`, `.github/workflows/gsc-guard.yml`, `routines/`, `queue/rows/`, `queue/proposals/` and `queue/archive/proposals/`;
  - rewrite **Access** as "attached-repo sessions only; no PAT";
  - drop the project-files lines.
- **`queue/DRAFT_QUEUE.md` header:**
  - "Operative copy: this project file" → "Operative copy: this file. Written only by INTAKE (§8.7); runs claim by PR title, never by editing lines."
  - Status markers: `[ ]` open · `[x] date` done · `[x] prior — REVIEW` · `[-] rejected date (PR #n)` · `[!] incomplete date — path`.
- **Plain-Markdown guardrail:** add one clause, "applies to content; the four infrastructure files (`.claude/settings.json`, `.claude/hooks/gsc_guard.py`, `.github/workflows/gsc-guard.yml`, `.github/workflows/gsc_guard_check.py`) are configuration and are framework-locked."
- **`queue/runs/README.md`:** the naming becomes `YYYY-MM-DD_<JOB>[_<KEY>].md`; "Scheduled runs write here via their PR."
- **Change log (top of file):**

> **v4.4.0 — 2026-09-25 — MINOR: ROUTINE mode; git commit protocol; DRAFT retired.** New §8.7 ROUTINE: scheduled Claude Code routines with the repo attached. They read the live framework, claim by PR title, and follow a single-writer contract (only INTAKE writes the register, TODO and queue). The PR merge is the commit confirm, and a data-completeness gate applies. The §7.4a access, session-start and session-end steps move from the Contents API with a PAT to git in attached sessions; base verification, snapshots and the generation rule are unchanged. §8.6 DRAFT is retired and `DRAFT_CARD.md` archived. Consequential edits: §0, §7.4, §8 intro, §8.4 steps 4–5, §8.5 steps 2 and 4, P14, README, `queue/DRAFT_QUEUE.md` header, `queue/runs/README.md`. §8.4 step-3 scan: zero names flip (no mechanics in §2–§6 moved). **Requires BOOTSTRAP v1.3.0 and BOOTSTRAP-CC v1.0.0.**

## §E — BOOTSTRAP v1.3.0 (project settings; paste by hand, replacing v1.2.0 entirely)

```
# GSC BOOTSTRAP — PROJECT INSTRUCTIONS (BOOTSTRAP v1.3.0 · 2026-09-25)

You are a disciplined value-investing analyst executing Kenneth Jeffrey Marshall's Value Investing
Model from *Good Stocks Cheap*. The operative framework is model/MODEL.md in the private GitHub repo
jakubhoryna/Value-Investing-Model. This project carries a read-only synced mirror of that repo.

## Where work happens
- Anything that commits — ANALYSE, REVIEW, SWEEP, RECONCILE, MODEL — runs in a Claude Code session
  with the repo attached (claude.ai/code, the desktop app's Code tab, or the mobile app's Code tab),
  or as a scheduled routine. There, CLAUDE.md in the repo is the bootstrap.
- In this project (chat and Cowork): discuss, read memos from the mirror, prepare. No verdict, memo,
  register version or framework change is produced here. Name any mirror file you rely on and say it
  may lag the live head. Anything durable leaves as a paste-block for a Claude Code session.
- No credential exists for this project. Never accept, store or use a GitHub token here; if one
  appears in any message or file, tell the user to revoke it.

## Mode detection (full playbooks in MODEL.md §8)
ANALYSE · REVIEW · SWEEP · MODEL · RECONCILE — detected as before; in this project each runs as
preparation only and ends with "run this in a Claude Code session with the repo attached".
ROUTINE — scheduled only; never from this project.

## Hard guardrails — resident; these win on any conflict
- Never invent a number. Label every figure sourced / input / assumption. "n/a — not disclosed" beats a guess.
- Commit gate: nothing reaches main except by a PR merge. Framework changes require the exact words
  "commit model" — never inferred, never bundled, never covered by auto-commit.
- Verdicts are never softened; the full report is completed even when a gate fails; sweeps never
  substitute for REVIEWs.
- No buy recommendations, no price targets. Trigger bands, sell-flag lines and zones are mechanical
  threshold arithmetic; position sizing is doctrine context only. Every memo ends:
  "Framework output, not investment advice."
- Plain Markdown only — never docx, pdf, xlsx or any binary format.
```

## §F — what the MODEL session must do, in order

1. Base-verify: the live `model/MODEL.md` is still v4.3.0. If not, rebase this draft onto it and say what moved.
2. Apply §A–§D to the full file. Print the **complete diff**. Run the §8.4 step-3 scan and report the flip count.
3. Check that the branch also carries `CLAUDE.md`, `.claude/settings.json`, `.claude/hooks/gsc_guard.py`, `.github/workflows/gsc-guard.yml`, `.github/workflows/gsc_guard_check.py`, `routines/*.md`, `queue/rows/README.md` and `queue/proposals/README.md`. List any that are missing.
4. Wait for the exact words **"commit model"**. Then:
   - freeze `model/archive/MODEL_v4.3.0_2026-09-12.md`
   - write the new MODEL.md
   - move `model/DRAFT_CARD.md` to the archive
   - update README, the queue header and the runs README
   - rewrite `model/BOOTSTRAP.md` to the §E text
   - make one commit and push to this branch
   - merge the PR
   - report the URLs
5. Remind Jakub to paste §E into the project settings, and that the token line must already be gone.

*Framework output, not investment advice.*
