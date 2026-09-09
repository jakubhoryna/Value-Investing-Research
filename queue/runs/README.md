# queue/runs/ — run notes and post-mortems

**What goes here.** One short note per scheduled or unattended run, and any post-mortem of the run architecture. This is the only place a run may write prose that is not a memo, a register version or a queue update — never project knowledge.

**Naming.** `YYYY-MM-DD_<task>.md` for run notes (e.g. `2026-09-10_daily.md`); `YYYY-MM-DD_<topic>_v1.md` for post-mortems and design notes.

**Run-note content (≤ 300 words).** Preflight result (live `MODEL.md` version read, base sha); what committed (register version, memo files, queue version); what failed and why (host, robots, data gap); what needs the user (one line each). No verdicts, no figures that are not already in a committed file.

**Retention.** Dated log; prune run notes older than a quarter in a RECONCILE session (post-mortems stay). Nothing here is authoritative state — the register wins on state, `model/MODEL.md` on rules.

**Seed.** `2026-09-09_scheduled-runs-postmortem-and-workflow-fix_v1.md` — why the 5–9 Sep scheduled runs could not push, and the workflow fix (repo attachment, one bounded daily run, evidence-only hard stop). Moved here from `reference/` on 2026-09-09 when that folder was retired.
