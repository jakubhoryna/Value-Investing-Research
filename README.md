# Value-Investing-Model

Good Stocks Cheap (GSC) research vault — Kenneth Jeffrey Marshall's Value Investing Model, run in Claude Code sessions and scheduled routines with this repository attached. Governance is split: `CLAUDE.md` at the root is the committed bootstrap (BOOTSTRAP-CC), and `model/MODEL.md` is the live operative framework, read from the checkout at every session start. The claude.ai project holds a read-only mirror for discussion; its project-settings text is copied at `model/BOOTSTRAP.md`. The register is state, the model is rules, the queue is work; nothing else is authoritative.

## Layout contract

Every folder has one job and one retention rule. "Versioned archive" means: the outgoing version is written verbatim to the sibling `archive/` folder in the same commit that supersedes it (MODEL §7.5). "Transient" means: deleted in the commit that consumes it.

| Path | What lives here | Retention | Governed by |
|---|---|---|---|
| `CLAUDE.md` | Repository bootstrap (BOOTSTRAP-CC) that Claude Code loads in every session on this repo: session start, mode detection, resident guardrails, config. Framework-locked. | Live; changes only under "commit model" | MODEL §0, §7.4a |
| `.claude/` | Committed hook configuration: `settings.json` and `hooks/` (the routine guard `gsc_guard.py`, its post-check and tests). The hooks are active only in routine sessions (`GSC_SESSION=routine`); the deny rules (no force-push, no reading `.git-credentials`) apply in every session. Framework-locked. `settings.local.json` and `worktrees/` are ignored. | Live; changes only under "commit model" | MODEL §8.7 |
| `.github/workflows/` | The `gsc-guard` check (`gsc-guard.yml`, `gsc_guard_check.py` and tests): checks every routine PR against the write contract. Advisory on GitHub Free. Framework-locked; cloud sessions cannot push it. | Live; changes only under "commit model", from an attended local push | MODEL §8.7 |
| `routines/` | Playbooks for scheduled runs: `README.md` (shared protocol) and one file per job (ANALYSE, REVIEW, SWEEP, INTAKE, QUEUE-SEED). Framework-locked; they bind as if written in MODEL. | Live; changes only under "commit model" | MODEL §0, §8.7 |
| `_REGISTER.md` | Master watchlist + portfolio layer — one row per company, latest memo version only. **Source of truth on state.** Version, date and counts in the front matter. | Live; every change is a versioned commit | MODEL §7.1–§7.5 |
| `registers/{YYYY}/` | One verbatim snapshot per outgoing register version (`REGISTER_v{N}_{YYYY-MM-DD}.md`), sharded by the year of the outgoing `register_date`, plus migration/run notes. The live register is `_REGISTER.md` at the root, so this folder is its archive. `registers/README.md` lists known gaps. | Versioned archive, append-only | MODEL §7.4a, §7.5 |
| `memos/<KEY>/` | One folder per §7.1a key; one Markdown memo per company-version inside it (`<KEY>_YYYY-MM-DD_GSC.md`). The folder is the memo history: a REVIEW adds a file, never overwrites; a same-day supersession renames the outgoing file `…_GSC_superseded-v{n}.md` in place. A re-key renames the folder. | Live history, append-only | MODEL §6, §7.1a, §7.4a |
| `model/` | `MODEL.md` (live framework, semver + change log), `BOOTSTRAP.md` (copy of the claude.ai project-settings text; no secret exists, so nothing is redacted), `BOOK_EXTRACT.md` (doctrine reference, read on demand). | Live | MODEL §0 |
| `model/archive/` | Frozen superseded framework files: `MODEL_v*` and `BOOTSTRAP_v*` copies, earlier book extractions and project instructions, relocation notes, and the retired `DRAFT_CARD_v4.3.0_2026-09-12.md` (DRAFT mode retired in MODEL v4.4.0). Framework history lives here and nowhere else. | Versioned archive | MODEL §0, §8.4 |
| `queue/TODO.md` | The single work sink — re-tests, backfills, corporate actions, ANALYSE candidate supply. Not state; the register wins. In routine runs only INTAKE writes it. | Live, versioned | MODEL §7.1, §7.5, §8.7 |
| `queue/IDEAS.md` | Framework parking lot — one entry per idea with status, instances, recommendation, consequence scan. Nothing here is operative until its own "commit model". Attended sessions only. | Live, versioned | MODEL §7.5, §8.4 |
| `queue/DRAFT_QUEUE.md` | The ANALYSE queue — one line per candidate key with a status marker (see its header). Operative in the repo; in routine runs only INTAKE writes it. Runs claim keys by PR title, never by editing lines. | Live, versioned | MODEL §7.5, §8.7 |
| `queue/archive/` | Outgoing `TODO_v*`, `IDEAS_v*` and `DRAFT_QUEUE_v*` versions. | Versioned archive | MODEL §7.5 |
| `queue/archive/proposals/` | Applied QUEUE-SEED proposals, moved here unchanged by INTAKE. | Archive, append-only | MODEL §7.5, §8.7 |
| `queue/rows/` | One row file per routine result (ANALYSE, REVIEW, SWEEP): the register row to apply, queue and TODO updates, open items, IDEAS candidates. INTAKE's inbox. | **Transient** — INTAKE deletes each file when it applies it; a held-back row stays until its memo is on `main` | MODEL §8.7, `queue/rows/README.md` |
| `queue/proposals/` | QUEUE-SEED restock and decay proposals. A merged proposal is approved. | **Transient** — INTAKE moves each applied file to `queue/archive/proposals/` | MODEL §8.7, `queue/proposals/README.md` |
| `queue/evidence/` | Per-name evidence notes harvested ahead of a memo (sourced figures, corporate actions, data gaps — never verdicts), and routine `{KEY}_{date}_INCOMPLETE.md` files (data-completeness gate). | **Transient** — delete the name's files in the commit that writes its memo (an INCOMPLETE run keeps them) | MODEL §8.7, TODO v26 block C |
| `queue/runs/` | Run notes from scheduled runs (`{D}_{T}_{JOB}[_{KEY}].md`, ≤ 300 words) and post-mortems (`YYYY-MM-DD_<topic>_v1.md`). Scheduled runs write here via their PR, never to project knowledge. | Dated log; prune quarterly | `queue/runs/README.md` |

Not in the repo, by design: secrets (none is held in the repo — GitHub access comes from the Claude Code session's proxy in the cloud, or Jakub's own git/gh login on his machine), local Claude Code files (`.claude/settings.local.json`, `.claude/worktrees/`), editor/vault configuration (`.obsidian/` is ignored), binaries. Content is plain Markdown; the guard configuration under `.claude/` and `.github/` is the only exception.

## Access

Private repo. Every read and write happens in a Claude Code session with this repository attached: attended (claude.ai/code, the desktop or mobile app's Code tab, or a local clone on Jakub's machine) or a scheduled routine. Cloud sessions and routines: the session's GitHub proxy supplies access (`GH_TOKEN` holds only the proxy placeholder). Local attended sessions: Jakub's own git/gh login on his machine. **There is no PAT.** In no case does a credential appear in a repo file, prompt or chat, and a session never requests, prints, sets or stores one. GitHub calls use `git` and `gh api` (REST) only. The claude.ai project is a read-only mirror: it discusses and prepares, and anything durable leaves it as a paste-block for a Claude Code session. Background: `queue/runs/2026-09-09_scheduled-runs-postmortem-and-workflow-fix_v1.md` and `queue/runs/2026-09-25_routines-migration-model-v4.4.0-draft_v1.md`.

## Discipline

- **Nothing reaches `main` except through a PR merge.** This is a rule, not a server setting: the repo is on GitHub Free, so it is enforced by the routine guard hook, the `gsc-guard` check and attended discipline (MODEL §7.4).
- **Register commits** are versioned: front-matter version + counts derived from the rows, change log capped at the newest 5 entries of ≤ 200 characters, outgoing version snapshotted to `registers/{YYYY}/` in the same commit, base verification against `origin/main` before the commit and again before the merge (MODEL §7.4a). A sweep may commit a price/ordering refresh only.
- **Memo commits** never overwrite; the register row is regenerated from the memo's front matter (memo wins on conflict).
- **Routine commits** go through one PR per run; Jakub's merge is the confirm. Only INTAKE writes `_REGISTER.md`, `queue/TODO.md` and `queue/DRAFT_QUEUE.md` (MODEL §8.7).
- **Framework commits** require the exact phrase "commit model"; the outgoing `MODEL.md` freezes to `model/archive/` in the same commit. `CLAUDE.md`, `routines/`, `.claude/` and `.github/` change under the same confirm and bump `MODEL.md` (workflow files only from a local attended session). The project-settings bootstrap changes only by manual re-paste and a version bump, with a copy at `model/BOOTSTRAP.md`.
- **Queue commits** follow the same versioned-archive pattern; work routes to `TODO.md`, framework ideas to `IDEAS.md`, never to the register's `## Open items`.
- **No live `MODEL.md` read → no verdict, no memo, no register version.** Evidence-only work is allowed and lands in `queue/evidence/` or `queue/runs/`.

## Directory sizes

GitHub directory listings (web and API) stop at 1,000 entries per directory. Memos are sharded per key (`memos/<KEY>/`, ~3 files per folder; 322 folders at the top level) and register snapshots per year (`registers/<YYYY>/`, ~250 per year at the 2026 pace), so no directory approaches the limit; the top-level `memos/` listing itself will need a second shard level only past ~1,000 names.

*Framework output, not investment advice.*
