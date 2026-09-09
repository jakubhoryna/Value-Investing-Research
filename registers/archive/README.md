# registers/archive/ — verbatim register snapshots

One file per outgoing register version, `{YYYY}/REGISTER_v{N}_{YYYY-MM-DD}.md` (year folder = year of the outgoing `register_date`; MODEL v4.2.1), written unchanged in the same commit that supersedes it (MODEL §7.4a step 3, §7.5). Append-only. Git history of `_REGISTER.md` is the secondary net; these files exist so that any session — including API-only or mobile ones — can retrieve a past state without git.

## Coverage and known gaps (audited 2026-09-09 against the git history of `_REGISTER.md`)

- **v0 (header-only stub), v1, v2** — the pre-GitHub registers from the project-knowledge era, moved here from the retired root `archive/` folder on 2026-09-09 (`REGISTER_v0-stub_2026-07-05.md`, `REGISTER_v1_2026-07-03.md`, `REGISTER_v2_2026-07-03.md`).
- **v3 – v42** — no snapshots: the register lived in project knowledge and then in git before the snapshot rule (MODEL v3.3.0, 2026-07-12). The vault seed commit of 2026-07-05 carried v3; intermediate versions survive only where git history of `_REGISTER.md` has them. `MIGRATION_v43-to-v44_2026-07-12.md` records the switch to the versioned-archive discipline.
- **v43 – v286** — complete except the entries below.
- **v234** — never committed. Git history shows v233 (6 Aug 2026 09:47 UTC) followed directly by v235 (6 Aug 2026 20:50 UTC, the P19 v4.0.0 judgment batch); the number was consumed by a session that re-merged before pushing. No register state is lost — every committed state is either v233 or v235.
- **v237 – v244** — never committed as separate files: nine ANALYSE memos went into one register PUT (v236 → v245) on 7 Aug 2026. The full chain and the run's findings are preserved in `RUNLOG_v237-v245_2026-08-07.md`.
- **v287 onward** — one snapshot per version, no gaps expected; a gap in future indicates a batched PUT and must carry its own RUNLOG note.

Other files here: `MIGRATION_v43-to-v44_2026-07-12.md` (backend migration note), `RECONCILE_open-items_2026-08-18.md` (disposition map of the 108 open items cleared at v257), `RUNLOG_v237-v245_2026-08-07.md`.

*Sharded by year since MODEL v4.2.1 (2026-09-10) to stay clear of the GitHub Contents API's 1,000-entries-per-directory listing limit; this README stays at the folder root.*
