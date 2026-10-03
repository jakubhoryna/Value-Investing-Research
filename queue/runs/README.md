# queue/runs/ — run notes and post-mortems

**What goes here.** One short note per scheduled run, and any post-mortem of the run architecture. Scheduled runs write here via their PR, never to project knowledge. Besides memos, `queue/rows/`, `queue/proposals/` and INCOMPLETE evidence, this is the only place a run may write prose.

**Naming.**
- Run notes: `{D}_{T}_{JOB}[_{KEY}].md` — `D` = run date `YYYY-MM-DD` and `T` = time `HHMM`, both Europe/Prague and fixed once at preflight; `JOB` = `ANALYSE` · `REVIEW` · `SWEEP` · `INTAKE` · `SEED` (QUEUE-SEED writes `SEED`); `_{KEY}` only for keyed runs. Examples: `2026-10-04_2250_ANALYSE_7309.T.md`, `2026-10-05_0650_INTAKE.md`. The claim stub (status *in progress*) and the final note share this path (MODEL §8.7, `routines/README.md`).
- Post-mortems and design notes: `YYYY-MM-DD_<topic>_v1.md`.
- Notes written before MODEL v4.4.0 keep their old names (e.g. `2026-09-10_daily.md`).

**Run-note content (≤ 300 words).** Preflight result (live `MODEL.md` version read, base sha); what the run's PR carries (memo, row file, proposal, INCOMPLETE evidence, register version); what failed and why (host, robots, data gap); what needs Jakub (one line each). No verdicts, no figures that are not already in a committed file.

**Retention.** Dated log; prune run notes older than a quarter in a RECONCILE session (post-mortems stay). Nothing here is authoritative state — the register wins on state, `model/MODEL.md` on rules.

**Seed.** `2026-09-09_scheduled-runs-postmortem-and-workflow-fix_v1.md` — why the 5–9 Sep scheduled runs could not push, and the workflow fix (repo attachment, one bounded daily run, evidence-only hard stop). Moved here from `reference/` on 2026-09-09 when that folder was retired.
