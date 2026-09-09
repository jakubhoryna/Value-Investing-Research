# Value-Investing-Model

Good Stocks Cheap (GSC) research vault — Kenneth Jeffrey Marshall's Value Investing Model, run as a Claude project. Governance is split: a static bootstrap in the Claude project settings (mirrored token-redacted at `model/BOOTSTRAP.md`) plus the live operative framework at `model/MODEL.md`, fetched at every session start. The register is state, the model is rules, the queue is work; nothing else is authoritative.

## Layout contract

Every folder has one job and one retention rule. "Versioned archive" means: the outgoing version is written verbatim to the sibling `archive/` folder in the same commit that supersedes it (MODEL §7.5). "Transient" means: deleted in the commit that consumes it.

| Path | What lives here | Retention | Governed by |
|---|---|---|---|
| `_REGISTER.md` | Master watchlist + portfolio layer — one row per company, latest memo version only. **Source of truth on state.** Version, date and counts in the front matter. | Live; every change is a versioned commit | MODEL §7.1–§7.5 |
| `registers/archive/{YYYY}/` | One verbatim snapshot per outgoing register version (`REGISTER_v{N}_{YYYY-MM-DD}.md`), sharded by the year of the outgoing `register_date`, plus migration/run notes. `registers/archive/README.md` lists known gaps. | Versioned archive, append-only | MODEL §7.4a, §7.5 |
| `memos/<KEY>/` | One folder per §7.1a key; one Markdown memo per company-version inside it (`<KEY>_YYYY-MM-DD_GSC.md`). The folder is the memo history: a REVIEW adds a file, never overwrites; a same-day supersession renames the outgoing file `…_GSC_superseded-v{n}.md` in place. A re-key renames the folder. | Live history, append-only | MODEL §6, §7.1a, §7.4a |
| `model/` | `MODEL.md` (live framework, semver + change log), `BOOTSTRAP.md` (token-redacted mirror of the project instructions), `BOOK_EXTRACT.md` (doctrine reference, fetch on demand). | Live | MODEL §0 |
| `model/archive/` | Frozen superseded framework files: every `MODEL_v*` and `BOOTSTRAP_v*`, earlier book extractions and project instructions, relocation notes. Framework history lives here and nowhere else. | Versioned archive | MODEL §0, §8.4 |
| `queue/TODO.md` | The single work sink — re-tests, backfills, corporate actions, ANALYSE candidate supply. Not state; the register wins. | Live, versioned | MODEL §7.1, §7.5 |
| `queue/IDEAS.md` | Framework parking lot — one entry per idea with status, instances, recommendation, consequence scan. Nothing here is operative until its own "commit model". | Live, versioned | MODEL §7.5, §8.4 |
| `queue/archive/` | Outgoing `TODO_v*` and `IDEAS_v*` versions. | Versioned archive | MODEL §7.5 |
| `queue/evidence/` | Per-name evidence notes harvested ahead of a memo (sourced figures, corporate actions, data gaps — never verdicts). | **Transient** — delete each file in the commit that writes its memo | TODO v26 block C |
| `queue/runs/` | Dated notes from scheduled/unattended runs (`YYYY-MM-DD_<task>.md`, ≤ 300 words: what committed, what failed, what needs the user) and run post-mortems. Runs write here, never to project knowledge. | Dated log; prune quarterly | `queue/runs/README.md` |

Not in the repo, by design: secrets (the PAT lives only in the project-settings bootstrap; the committed mirror is redacted), editor/vault configuration (`.obsidian/` is ignored), binaries. Plain Markdown only.

## Access

Private repo — there is no tokenless raw URL. Attended sessions read and write through the GitHub Contents API with a fine-grained PAT (Contents R/W, single repo), loaded from the bootstrap config at session start. Scheduled (cloud) sessions cannot use the PAT for writes — the sandbox proxy gates GitHub per session and requires the repository to be attached as a source; see `queue/runs/2026-09-09_scheduled-runs-postmortem-and-workflow-fix_v1.md`.

## Discipline

- **Register commits** are versioned: front-matter version + counts derived from the rows, change log capped at the newest 5 entries of ≤ 200 characters, outgoing version snapshotted to `registers/archive/` before the live PUT, every PUT preceded by base verification against the live head (MODEL §7.4a). A sweep may commit a price/ordering refresh only.
- **Memo commits** never overwrite; the register row is regenerated from the memo's front matter (memo wins on conflict).
- **Framework commits** require the exact phrase "commit model"; the outgoing `MODEL.md` freezes to `model/archive/` in the same commit. The bootstrap changes only by manual re-paste and a version bump.
- **Queue commits** follow the same versioned-archive pattern; work routes to `TODO.md`, framework ideas to `IDEAS.md`, never to the register's `## Open items`.
- **No live `MODEL.md` read → no verdict, no memo, no register version.** Evidence-only work is allowed and lands in `queue/evidence/` or `queue/runs/`.

## Directory sizes

The GitHub Contents API lists at most 1,000 entries per directory. Memos are sharded per key (`memos/<KEY>/`, ~3 files per folder; 322 folders at the top level) and register snapshots per year (`registers/archive/<YYYY>/`, ~250 per year at the 2026 pace), so no directory approaches the limit; the top-level `memos/` listing itself will need a second shard level only past ~1,000 names. `instructions/MODEL.md` is a `status: moved` stub for one transition window (MODEL v4.2.1) and is deleted at the next PATCH.

*Framework output, not investment advice.*
