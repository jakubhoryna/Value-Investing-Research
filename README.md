# Value-Investing-Model

**A personal equity-research system: Kenneth Jeffrey Marshall's *Good Stocks Cheap* value-investing model, run by AI agents (Claude Code) under rules I write, version and audit.** Built and run by Jakub Horyna since July 2026. Not affiliated with or endorsed by Kenneth Jeffrey Marshall. Nothing here is investment advice.

## Start here (about 15 minutes)

| # | Read | Why |
|---|---|---|
| 1 | [Guided tour](docs/2026-11-08_guided-tour_v1.md) | What the system does, how a company moves through it, and why the output can be trusted |
| 2 | [CROX: holding-period review](docs/2026-11-08_CROX_holding-period-review_v1.md) | My largest position from 2023 to today: what worked, what didn't, and where the framework stands |
| 3 | [HelloFresh: post-mortem](docs/2026-11-08_HFG_post-mortem_v1.md) | My worst position, the rules I bent, and the framework changes that now prevent it |
| 4 | [A full memo: CROX](memos/CROX/) | What one research run produces: a body of up to 800 words, then the evidence appendix |
| 5 | [The register](_REGISTER.md) | 498 companies, one line each: the watchlist and the portfolio |
| 6 | [The framework](model/MODEL.md) | The rules: §2 the model, §3 the parameters, and the change log at the end |

**At a glance (8 Nov 2026):**

- 498 companies analysed: 69 WATCH, 426 AVOID, 0 BUY.
- 4 held positions. The framework currently flags all four for sale, and I hold them by logged decisions (see items 2 and 3).
- 1,865 commits and 29 framework versions since July 2026.

---

## Operator reference

Good Stocks Cheap (GSC) research vault — Kenneth Jeffrey Marshall's Value Investing Model, run in Claude Code sessions and scheduled routines with this repository attached. Governance is split: `CLAUDE.md` at the root is the committed bootstrap (BOOTSTRAP-CC), and `model/MODEL.md` is the live operative framework, read from the checkout at every session start. The claude.ai project holds a read-only mirror for discussion; its project-settings text is copied at `model/BOOTSTRAP.md`. The register is state, the model is rules, the queue is work; nothing else is authoritative.

### Layout contract

Every folder has one job and one retention rule. "Versioned archive" means: the outgoing version is written verbatim under the root `archive/` tree, at the path mirroring the live file (framework files: `model/archive/`), in the same commit that supersedes it (MODEL §7.5). "Transient" means: deleted in the commit that consumes it.

| Path | What lives here | Retention | Governed by |
|---|---|---|---|
| `CLAUDE.md` | Repository bootstrap (BOOTSTRAP-CC) that Claude Code loads in every session on this repo: session start, mode detection, resident guardrails, config. Framework-locked. | Live; changes only under "commit model" | MODEL §0, §7.4a |
| `.claude/` | Committed hook configuration: `settings.json` and `hooks/` (the routine guard `gsc_guard.py`, its post-check and tests). The hooks are active only in routine sessions (`GSC_SESSION=routine`); the deny rules (no force-push, no reading `.git-credentials`) apply in every session. Framework-locked. `settings.local.json` and `worktrees/` are ignored. | Live; changes only under "commit model" | MODEL §8.7 |
| `.github/workflows/` | The `gsc-guard` check (`gsc-guard.yml`, `gsc_guard_check.py`: the write contract; runs once per routine PR on its final title), `gsc-automerge` (`gsc-automerge.yml`, `gsc_automerge.py`: squash-merges merge-class routine PRs with the per-run token, fail closed; kill switch `GSC_AUTOMERGE`) and `gsc-notify` (`gsc-notify.yml`, `gsc_notify.py`: the `GSC - needs Jakub` record issue and the daily maintenance, the re-run of incident-cancelled guard runs and the merge sweep; its morning digest, retired by MODEL v4.6.1, left the workflow at v4.8.0, which also made its maintenance late-tolerant and every record comment mention-free), the REST helper `gsc_gh.py`, and their tests. Framework-locked; GitHub accepts a push that changes it only with the workflow scope (v4.8.0 went from a cloud session). | Live; changes only under "commit model", from an attended push (local when a cloud push is refused) | MODEL §8.7 items 3, 10–12 |
| `routines/` | Playbooks for scheduled runs: `README.md` (shared protocol) and one file per job (ANALYSE, REVIEW, SWEEP, INTAKE, QUEUE-SEED, WEEKLY), plus `tools/gsc_register.py` — the register tool (render, row-from-memo, apply, position, rekey, metrics, sweep-scope, check, lint-memo, and the one-time attended rebuild and retrigger, which the guard hook refuses in routines) — and `tools/gsc_site.py` — the register page generator (render, stats; the page is generated, never committed, and published to a private claude.ai artifact: `register_page` in `CLAUDE.md`) — and `tools/gsc_weekly.py` — the weekly report tool (window, render, lint-summary, dash-writes; offline; the report is generated, never committed, and published by WEEKLY to a private claude.ai Dashboard artifact: `weekly_page` in `CLAUDE.md`) — with their tests. Framework-locked; they bind as if written in MODEL. | Live; changes only under "commit model" | MODEL §0, §7.1, §7.1b, §8.7 |
| `_REGISTER.md` | Master watchlist + portfolio layer — one lean row per company, from its current memo only, no prose (MODEL v4.5.0). **Source of truth on state.** Version, date and counts in the front matter. Rendered from `register.csv` by the register tool; never edited by hand. | Live; every change is a versioned commit | MODEL §7.1–§7.5 |
| `register.csv` | Machine twin of `_REGISTER.md`: every register column plus the core numbers (MODEL §7.1b) and the position record, one line per key. Written only through `routines/tools/gsc_register.py` (INTAKE, attended register writes). | Live; snapshotted beside the `.md` in `archive/registers/{YYYY}/` | MODEL §7.1, §7.1b, §7.5 |
| `memos/<KEY>/` | Exactly one file per §7.1a key: the current memo `<KEY>_YYYY-MM-DD_GSC.md`. A REVIEW writes a complete, self-contained successor (MODEL §6.6); the commit that adds it (or a same-day rerun) moves the outgoing file unchanged to `archive/memos/<KEY>/`. A re-key renames both folders. | Live, one file per key | MODEL §6, §6.6, §7.1a, §7.4a, §7.5 |
| `archive/` | Append-only history of the live files, mirroring their paths: `memos/`, `registers/`, `queue/` (below). A file here is never edited or deleted; its path changes only at a §7.1a re-key or by a GitHub Revert of the PR that added it. `archive/README.md` holds the rules. Created at MODEL v4.5.0 by an index-only migration from `registers/`, `queue/archive/` and the non-current files of `memos/`. | Versioned archive, append-only | MODEL §7.5, §8.7 |
| `archive/memos/<KEY>/` | Every earlier memo version, byte-identical, under its own filename (incl. `…_GSC_superseded-v{n}.md` same-day supersessions). | Versioned archive, append-only | MODEL §6, §7.5 |
| `archive/registers/{YYYY}/` | One verbatim snapshot per outgoing register version (`REGISTER_v{N}_{YYYY-MM-DD}.md`, with its `.csv` twin from MODEL v4.5.0), sharded by the year of the outgoing `register_date`, plus legacy migration/run notes. `archive/registers/README.md` lists known gaps. | Versioned archive, append-only | MODEL §7.4a, §7.5 |
| `archive/queue/` | Outgoing `TODO_v*`, `IDEAS_v*` and `DRAFT_QUEUE_v*` versions. | Versioned archive, append-only | MODEL §7.5 |
| `archive/queue/proposals/` | Applied QUEUE-SEED proposals, moved here unchanged by INTAKE. | Archive, append-only | MODEL §7.5, §8.7 |
| `model/` | `MODEL.md` (live framework, semver + change log), `BOOTSTRAP.md` (copy of the claude.ai project-settings text; no secret exists, so nothing is redacted), `BOOK_EXTRACT.md` (doctrine reference, read on demand). | Live | MODEL §0 |
| `model/archive/` | Frozen superseded framework files: `MODEL_v*` and `BOOTSTRAP_v*` copies, earlier book extractions and project instructions, relocation notes, and the retired `DRAFT_CARD_v4.3.0_2026-09-12.md` (DRAFT mode retired in MODEL v4.4.0). Framework history lives here and nowhere else. | Versioned archive | MODEL §0, §8.4 |
| `queue/TODO.md` | The single work sink — re-tests, backfills, corporate actions, ANALYSE candidate supply. Not state; the register wins. In routine runs only INTAKE writes it. | Live, versioned | MODEL §7.1, §7.5, §8.7 |
| `queue/IDEAS.md` | Framework parking lot — one entry per idea with status, instances, recommendation, consequence scan. Nothing here is operative until its own "commit model". Attended sessions only. | Live, versioned | MODEL §7.5, §8.4 |
| `queue/DRAFT_QUEUE.md` | The ANALYSE queue — one line per candidate key with a status marker (see its header). Operative in the repo; in routine runs only INTAKE writes it. Runs claim keys by PR title, never by editing lines. | Live, versioned | MODEL §7.5, §8.7 |
| `queue/rows/` | One row file per routine result (ANALYSE, REVIEW, SWEEP): the register row to apply, queue and TODO updates, open items, IDEAS candidates. INTAKE's inbox. | **Transient** — INTAKE deletes each file when it applies it; a held-back row stays until its memo is on `main` | MODEL §8.7, `queue/rows/README.md` |
| `queue/proposals/` | QUEUE-SEED restock and decay proposals. A merged proposal is approved. | **Transient** — INTAKE moves each applied file to `archive/queue/proposals/` | MODEL §8.7, `queue/proposals/README.md` |
| `queue/evidence/` | Per-name evidence notes harvested ahead of a memo (sourced figures, corporate actions, data gaps — never verdicts), and routine `{KEY}_{date}_INCOMPLETE.md` files (data-completeness gate; a budget overrun's file is the resumable record the next run starts from, MODEL v4.8.0). | **Transient** — delete the name's files in the commit that writes its memo, every INCOMPLETE record included (an INCOMPLETE run keeps them) | MODEL §8.7, TODO v26 block C |
| `queue/runs/` | Run notes from scheduled runs (`{D}_{T}_{JOB}[_{KEY}].md`, ≤ 300 words) and post-mortems (`YYYY-MM-DD_<topic>_v1.md`). Scheduled runs write here via their PR, never to project knowledge. | Dated log; prune quarterly | `queue/runs/README.md` |
| `docs/` | Write-ups for readers outside the project: the guided tour, position reviews and post-mortems, `YYYY-MM-DD_<topic>_v{n}.md`. Narrative only, never state or rules: the register wins on state, the memo on its verdict, MODEL on rules. Attended sessions only; routines never write here. | Live; a revision is a new `_v{n+1}` file beside the old one | — |

Not in the repo, by design: secrets (none is held in the repo — GitHub access comes from the Claude Code session's proxy in the cloud, or Jakub's own git/gh login on his machine), local Claude Code files (`.claude/settings.local.json`, `.claude/worktrees/`), editor/vault configuration (`.obsidian/` is ignored), binaries. Content is plain Markdown; the exceptions are `register.csv` (the register's machine twin), the Python tools under `routines/tools/` (the register tool, the register page generator and the weekly report tool; the page and the report are generated, never committed), the guard configuration under `.claude/` and `.github/`, and `.gitattributes` (LF line ends for `_REGISTER.md` and `register.csv`).

### Access

Private repo. Every read and write happens in a Claude Code session with this repository attached: attended (claude.ai/code, the desktop or mobile app's Code tab, or a local clone on Jakub's machine) or a scheduled routine. Cloud sessions and routines: the session's GitHub proxy supplies access (`GH_TOKEN` holds only the proxy placeholder). Local attended sessions: Jakub's own git/gh login on his machine. **There is no PAT.** In no case does a credential appear in a repo file, prompt or chat, and a session never requests, prints, sets or stores one. GitHub calls use `git` and `gh api` (REST) only. The claude.ai project is a read-only mirror: it discusses and prepares, and anything durable leaves it as a paste-block for a Claude Code session. Background: `queue/runs/2026-09-09_scheduled-runs-postmortem-and-workflow-fix_v1.md` and `queue/runs/2026-09-25_routines-migration-model-v4.4.0-draft_v1.md`.

### Discipline

- **Nothing reaches `main` except through a PR merge.** This is a rule, not a server setting: the repo is on GitHub Free, so it is enforced by the routine guard hook, the `gsc-guard` check and attended discipline (MODEL §7.4).
- **Register commits** are versioned and made only by the register tool: `register.csv` updated and `_REGISTER.md` rendered from it, front-matter version + counts derived from the rows, no in-file change log (the one-line entry goes in the commit and PR body), the outgoing `.md` and `.csv` snapshotted to `archive/registers/{YYYY}/` in the same commit, base verification against `origin/main` before the commit and again before the merge (MODEL §7.4a). A sweep may commit a price refresh only.
- **Memo commits** never overwrite or edit a memo; a superseding memo moves its prior unchanged to `archive/memos/<KEY>/` in the same commit; the register row is regenerated from the current memo's front matter (memo wins on conflict).
- **Routine commits** go through one PR per run (WEEKLY commits nothing); the merge is the confirm — gsc-automerge for merge classes, Jakub for held PRs (MODEL §8.7 items 3 and 10). Undo is a GitHub Revert before the next INTAKE. Only INTAKE writes `_REGISTER.md`, `register.csv`, `queue/TODO.md` and `queue/DRAFT_QUEUE.md` (MODEL §8.7).
- **Framework commits** require the exact phrase "commit model"; the outgoing `MODEL.md` freezes to `model/archive/` in the same commit. `CLAUDE.md`, `routines/`, `.claude/` and `.github/` change under the same confirm and bump `MODEL.md` (workflow files only from an attended push GitHub accepts: a cloud session's since v4.8.0, a local one when a cloud push is refused). The project-settings bootstrap changes only by manual re-paste and a version bump, with a copy at `model/BOOTSTRAP.md`.
- **Queue commits** follow the same versioned-archive pattern; work routes to `TODO.md`, framework ideas to `IDEAS.md`. Register open items (pending user decisions, register-integrity holds; cap 7) live in the TODO head block `▶ Open items (register)`.
- **No live `MODEL.md` read → no verdict, no memo, no register version.** Evidence-only work is allowed and lands in `queue/evidence/` or `queue/runs/`.

### Directory sizes

GitHub directory listings (web and API) stop at 1,000 entries per directory. Memos are sharded per key: one current file in each `memos/<KEY>/` (386 folders at MODEL v4.5.0) and the history in `archive/memos/<KEY>/` (a handful of files each); register snapshots are sharded per year (`archive/registers/<YYYY>/`: two files per version since MODEL v4.5.0, the `.md` and its `.csv` twin — roughly 600–900 a year at the 2026 pace, so a year folder can near the limit; shard by half-year if one passes ~900). No directory approaches the limit; the top-level `memos/` and `archive/memos/` listings will need a second shard level only past ~1,000 names.

*Framework output, not investment advice.*
