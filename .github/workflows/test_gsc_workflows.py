#!/usr/bin/env python3
"""Structure tests for the three GSC workflow files (no YAML library, no network).

Checks: the guard's once-per-PR job condition, its triggers, runner and
permissions; the exact permissions of gsc-automerge and gsc-notify; gsc-notify
has only its maintenance job and cron (the digest is retired, MODEL v4.8.0),
and no tick acts outside 06:30-21:00 Prague; no secrets; every checkout pinned
to a commit sha, on the default branch (no ref:) and keeping its credentials
(the merger fetches PR refs of this private repo); untrusted event values
(PR title, head ref, display title, head branch) only inside env: or if:,
never inside run:; the token only as env GH_TOKEN from github.token.

Run:  python3 .github/workflows/test_gsc_workflows.py   (exit code = failures)
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = []


def record(name, ok, detail=""):
    RESULTS.append(ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("" if ok or not detail else "  -- " + str(detail)[:300]))


def read(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as fh:
        return fh.read()


def block(text, key, indent=0):
    """Lines of the mapping under `key:` at `indent` spaces (comments dropped)."""
    lines = text.splitlines()
    out, inside = [], False
    for line in lines:
        bare = line.split(" #", 1)[0].rstrip() if not line.lstrip().startswith("#") else ""
        if not bare:
            continue
        lead = len(bare) - len(bare.lstrip())
        if inside:
            if lead <= indent:
                break
            out.append(bare.strip())
        elif lead == indent and bare.strip() == key + ":":
            inside = True
    return out


def job_lines(text, job):
    """The lines of job `job` (two-space indent under jobs:), comments dropped."""
    m = re.search(r"\n  %s:\n((?:(?:    .*)?\n)+)" % re.escape(job), text + "\n")
    if not m:
        return []
    return [line.split(" #", 1)[0].rstrip() for line in m.group(1).splitlines()
            if line.strip() and not line.lstrip().startswith("#")]


def job_permissions(text, job):
    out, inside = [], False
    for line in job_lines(text, job):
        if line == "    permissions:":
            inside = True
            continue
        if inside:
            if not line.startswith("      "):
                break
            out.append(line.strip())
    return out


def job_if(text, job):
    lines = job_lines(text, job)
    out, inside = [], False
    for line in lines:
        if line.startswith("    if: >-"):
            inside = True
            continue
        if inside:
            if not line.startswith("      "):
                break
            out.append(line.strip())
    return " ".join(out)


def run_bodies(text):
    """The text of every run: step (inline or block scalar)."""
    bodies, lines = [], text.splitlines()
    i = 0
    while i < len(lines):
        m = re.match(r"^(\s*)(?:- )?run:\s*(.*)$", lines[i])
        if not m:
            i += 1
            continue
        indent, rest = len(m.group(1)), m.group(2)
        body = [] if rest in ("|", ">", "|-", ">-") else [rest]
        i += 1
        while i < len(lines) and (not lines[i].strip() or len(lines[i]) - len(lines[i].lstrip()) > indent + 2):
            body.append(lines[i])
            i += 1
        bodies.append("\n".join(body))
    return bodies


def main():
    guard, merger, notify = read("gsc-guard.yml"), read("gsc-automerge.yml"), read("gsc-notify.yml")
    files = {"gsc-guard.yml": guard, "gsc-automerge.yml": merger, "gsc-notify.yml": notify}

    # gsc-guard: once per PR on the final title.
    cond = " ".join(block(guard, "if: >-", 4))
    if not cond:
        m = re.search(r"\n    if: >-\n((?:      .*\n)+)", guard)
        cond = " ".join(line.strip() for line in m.group(1).splitlines()) if m else ""
    record("guard: job if: skips a '[running]' routine title",
           "endsWith(github.event.pull_request.title, '[running]')" in cond
           and "startsWith(github.event.pull_request.head.ref, 'claude/gsc')" in cond, cond)
    record("guard: job if: runs 'edited' only for a title or base change",
           "github.event.action != 'edited' || github.event.changes.title || github.event.changes.base" in cond, cond)
    record("guard: job if: open PRs only", "github.event.pull_request.state == 'open'" in cond, cond)
    record("guard: keeps the four pull_request_target types",
           "types: [opened, synchronize, reopened, edited]" in guard and "pull_request_target:" in guard)
    record("guard: permissions contents: read only", block(guard, "permissions") == ["contents: read"],
           block(guard, "permissions"))
    # gsc_automerge.guard_state() finds the job by its name 'guard'; a job with
    # its own name: would make every guard run read as 'failed' (held).
    jobs = block(guard, "jobs")
    record("guard: the job id is 'guard' and it has no name: (its name stays 'guard')",
           jobs[:1] == ["guard:"] and not any(line.startswith("name:") for line in block(guard, "guard", 2)),
           jobs[:3])
    for name, text in files.items():
        code = "\n".join(line for line in text.splitlines() if not line.lstrip().startswith("#"))
        record("%s: runs on ubuntu-24.04" % name, "runs-on: ubuntu-24.04" in code and "ubuntu-latest" not in code)

    # Permissions, triggers, concurrency.
    record("automerge: exactly the four permissions", sorted(block(merger, "permissions")) == sorted([
        "contents: write", "pull-requests: write", "actions: read", "issues: write"]),
        block(merger, "permissions"))
    record("automerge: a manual dispatch runs only from main",
           "(github.event_name == 'workflow_dispatch' && github.ref == 'refs/heads/main')" in job_if(merger, "merge"),
           job_if(merger, "merge"))
    record("automerge: on guard completion and by dispatch",
           "workflows: [gsc-guard]" in merger and "types: [completed]" in merger and "workflow_dispatch:" in merger)
    record("automerge: skipped guard runs never start the merger",
           "github.event.workflow_run.conclusion != 'skipped'" in merger)
    record("automerge: one run at a time, never cancelled",
           "group: gsc-automerge" in merger and "cancel-in-progress: false" in merger)
    record("notify: workflow permissions contents: read only", block(notify, "permissions") == ["contents: read"],
           block(notify, "permissions"))
    jobs = re.findall(r"(?m)^  ([A-Za-z0-9_-]+):\s*$", notify.split("\njobs:\n", 1)[-1])
    record("notify: one job, maintenance (the digest job is retired, v4.8.0)", jobs == ["maintenance"], jobs)
    record("notify: no digest left in the workflow (no task input, no digest step or env)",
           not re.search(r"digest|TASK:|inputs:", "\n".join(line for line in notify.splitlines()
                                                             if not line.lstrip().startswith("#"))))
    record("notify: the maintenance job holds exactly its four permissions",
           sorted(job_permissions(notify, "maintenance"))
           == sorted(["contents: read", "pull-requests: read", "actions: write", "issues: write"]),
           job_permissions(notify, "maintenance"))
    sys.path.insert(0, HERE)
    sys.dont_write_bytecode = True
    import datetime
    import gsc_notify as nt
    crons = re.findall(r"cron: '([^']+)'", notify)
    record("notify: five cron lines, one tick each: 06:30 Prague in CEST and in CET, three spares",
           crons == ["30 4 * * *", "30 5 * * *", "30 8 * * *", "30 11 * * *", "30 14 * * *"], crons)
    record("notify: the cron lines match the script's MAINTENANCE_CRONS", crons == list(nt.MAINTENANCE_CRONS),
           (crons, nt.MAINTENANCE_CRONS))
    record("notify: one hour per cron line (GitHub has started at most one run per line per day)",
           all(len(c.split()) == 5 and c.split()[1].isdigit() for c in crons), crons)
    record("notify: a scheduled run or a manual dispatch from main only",
           job_if(notify, "maintenance") == "github.event_name == 'schedule' || "
           "(github.event_name == 'workflow_dispatch' && github.ref == 'refs/heads/main')",
           job_if(notify, "maintenance"))
    record("notify: one run at a time, never cancelled",
           "group: gsc-notify" in notify and "cancel-in-progress: false" in notify)
    # No scheduled tick acts in the 02:00-06:00 Prague quiet window (MODEL §8.7
    # item 12) or after 21:00, in CET, in CEST or on a DST change day: a tick
    # there must be one the script's Prague-clock window turns into a no-op.
    # Every day has a tick that acts at 06:30, and spares later in the window.
    acting, outside = {}, []
    for day in ("2026-01-14", "2026-01-17", "2026-07-15", "2026-07-18", "2026-10-25", "2027-03-28"):
        for cron in crons:
            minute, hours, _dom, _mon, dows = cron.split()
            for hour in (int(h) for h in hours.split(",")):
                when = datetime.datetime.fromisoformat("%sT%02d:%s:00+00:00" % (day, hour, minute))
                if dows != "*" and str(when.isoweekday() % 7) not in dows.split(","):
                    continue
                local = when.astimezone(nt.PRAGUE)
                if nt.maintenance_in_window(when):
                    acting.setdefault(day, []).append(local.strftime("%H:%M"))
                    if not ((6, 30) <= (local.hour, local.minute) < (21, 0)):
                        outside.append("%s %s -> %s Prague" % (cron, day, local.strftime("%H:%M")))
                for late in range(0, 12 * 60 + 1, 30):  # GitHub starts the tick up to 12 h late
                    started = (when + datetime.timedelta(minutes=late)).astimezone(nt.PRAGUE)
                    if nt.maintenance_in_window(started) and 2 <= started.hour < 6:
                        outside.append("%s %s +%d min -> %s" % (cron, day, late, started.strftime("%H:%M")))
    record("no scheduled gsc-notify tick acts in the 02:00-06:00 quiet window or after 21:00, even started late",
           not outside, outside)
    record("maintenance acts at 06:30 Prague every day (CET, CEST, both DST change days) with >= 3 later spares",
           all(acting.get(d, [""])[0] == "06:30" and len(acting[d]) >= 4 for d in
               ("2026-01-14", "2026-01-17", "2026-07-15", "2026-07-18", "2026-10-25", "2027-03-28")), acting)
    # The observed delay (2026-10-08 to 2026-10-20: 4-8 h): some line still lands in the window.
    for season, day in (("CET", "2026-01-14"), ("CEST", "2026-07-15")):
        missed = []
        for late_h in range(4, 9):
            starts = [datetime.datetime.fromisoformat("%sT%02d:%s:00+00:00" % (day, int(h), c.split()[0]))
                      + datetime.timedelta(hours=late_h) for c in crons for h in c.split()[1].split(",")]
            if not any(nt.maintenance_in_window(s) for s in starts):
                missed.append(late_h)
        record("maintenance: with every tick started 4-8 h late, one still acts (%s)" % season, not missed, missed)
    for name, text in (("gsc-guard.yml", guard), ("gsc-automerge.yml", merger)):
        record("%s: no schedule (it acts only on events)" % name, "schedule:" not in text)

    for name, text in files.items():
        record("%s: no secrets" % name, "secrets." not in text)
        uses = re.findall(r"uses:\s*(\S+)", text)
        record("%s: every action pinned to a commit sha" % name,
               uses and all(re.fullmatch(r"[\w.-]+/[\w.-]+@[0-9a-f]{40}", u) for u in uses), uses)
        checkout_with = re.findall(r"uses: actions/checkout@\S+.*\n((?:\s+.*\n)*?)\s+- ", text + "\n      - ")
        record("%s: checkout has no ref: and keeps its credentials" % name,
               all("ref:" not in w and "persist-credentials: false" not in w for w in checkout_with), checkout_with)
        bodies = run_bodies(text)
        record("%s: no ${{ }} expression inside run:" % name, bodies and all("${{" not in b for b in bodies), bodies)
        for value in ("github.event.pull_request.title", "github.event.pull_request.head.ref",
                      "github.event.workflow_run.display_title", "github.event.workflow_run.head_branch"):
            hits = [line.strip() for line in text.splitlines() if value in line and not line.lstrip().startswith("#")]
            ok = all(re.match(r"^[A-Z_]+: \$\{\{ " + re.escape(value) + r" \}\}$", h) or h.startswith(("if:", "!", "(", "github.", "startsWith", "endsWith"))
                     for h in hits)
            record("%s: %s only in env: or if:" % (name, value.split(".")[-1]), ok, hits)
        tokens = [line.strip() for line in text.splitlines() if "github.token" in line and not line.lstrip().startswith("#")]
        record("%s: the token only as env GH_TOKEN" % name,
               all(t == "GH_TOKEN: ${{ github.token }}" for t in tokens) and "GITHUB_TOKEN" not in
               "\n".join(line for line in text.splitlines() if not line.lstrip().startswith("#")), tokens)

    failed = RESULTS.count(False)
    print("\n%d case(s), %d failed" % (len(RESULTS), failed))
    return failed


if __name__ == "__main__":
    sys.exit(main())
