# archive/ — append-only history (MODEL §7.5)

Every standing artifact keeps its live file lean and its history here, at the path that mirrors the live file. The outgoing version is written verbatim, in the same commit that supersedes it. Framework history (MODEL, BOOTSTRAP) stays in `model/archive/` (MODEL §0).

| Path | Content | Written by |
|---|---|---|
| `archive/memos/{KEY}/` | Every earlier memo version, byte-identical, under its own filename `{KEY}_{YYYY-MM-DD}_GSC.md` (a same-day supersession: `…_GSC_superseded-v{n}.md`). `memos/{KEY}/` holds only the current memo. | the commit that writes the successor memo (a REVIEW), attended or routine |
| `archive/registers/{YYYY}/` | One verbatim snapshot per outgoing register version, `REGISTER_v{N}_{YYYY-MM-DD}.md`, with its twin `REGISTER_v{N}_{YYYY-MM-DD}.csv` (the outgoing `register.csv`) from MODEL v4.5.0, in the year folder of the outgoing `register_date`, plus legacy migration and run notes. `archive/registers/README.md` lists known gaps. | INTAKE, and attended register commits |
| `archive/queue/` | Outgoing `TODO_v{n}_{date}.md`, `IDEAS_v{n}_{date}.md` and `DRAFT_QUEUE_v{n}_{date}.md` versions. | INTAKE (TODO, DRAFT_QUEUE), attended sessions (IDEAS) |
| `archive/queue/proposals/` | Applied QUEUE-SEED proposals, moved here unchanged under their own filename. | INTAKE |

**Rules.**
- **Append-only.** A file here is never edited or deleted. Its path changes only at a §7.1a re-key (the RECONCILE renames `archive/memos/<old-key>/` with `memos/<old-key>/`; the bytes stay unchanged) or by a GitHub Revert of the PR that added it. Routines only add files here; the gsc-guard check and the guard hook enforce that, and INTAKE's audit lists any other change on `main`.
- **Byte copies.** Every snapshot, archived memo and archived proposal here equals the live file it replaced, byte for byte (the READMEs and the one-time rebuild and retrigger reports are the exceptions). Copy with `cp` or move with `git mv`; never write an archive file with an editor.
- **Retired paths.** `registers/` and `queue/archive/` no longer exist; nothing is written there.
- The READMEs in this tree are framework-owned and change only in an attended session.

*Created at MODEL v4.5.0 (2026-10) by an index-only migration — pure renames, no content change — from `registers/` (262 files), `queue/archive/` (50 files) and the 122 non-current files of 69 `memos/` folders, counted at origin/main a89ef2f and recomputed at landing. The earlier root `archive/` retired on 2026-09-09 held different content; that layout is not revived.*
