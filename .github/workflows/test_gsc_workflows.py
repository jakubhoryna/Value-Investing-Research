#!/usr/bin/env python3
"""Structure tests for the three GSC workflow files (no YAML library, no network).

Checks: the guard's once-per-PR job condition, its triggers, runner and
permissions; the exact permissions of gsc-automerge and gsc-notify; the
digest and maintenance crons; no secrets; every checkout pinned to a commit
sha, on the default branch (no ref:) and keeping its credentials (the merger
and notifier fetch PR refs of this private repo); untrusted event values
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
    record("notify: the digest job reads actions, never writes them", sorted(job_permissions(notify, "digest")) ==
           sorted(["contents: read", "pull-requests: read", "actions: read", "issues: write"]),
           job_permissions(notify, "digest"))
    record("notify: only the maintenance job holds actions: write", sorted(job_permissions(notify, "maintenance"))
           == sorted(["contents: read", "pull-requests: read", "actions: write", "issues: write"]),
           job_permissions(notify, "maintenance"))
    crons = re.findall(r"cron: '([^']+)'", notify)
    record("notify: the three crons (two digest triples and maintenance at 06:30 Prague)",
           crons == ["30 6,7,8 * * 1-5", "45 7,8,9 * * 0,6", "30 4,5 * * *"], crons)
    record("notify: maintenance cron matches the script's constant and both job conditions",
           "MAINTENANCE_CRON = \"30 4,5 * * *\"" in read("gsc_notify.py")
           and "github.event.schedule != '30 4,5 * * *'" in job_if(notify, "digest")
           and "github.event.schedule == '30 4,5 * * *'" in job_if(notify, "maintenance"),
           (job_if(notify, "digest"), job_if(notify, "maintenance")))
    record("notify: a manual dispatch runs only from main",
           all("github.event_name == 'workflow_dispatch' && github.ref == 'refs/heads/main'" in job_if(notify, j)
               for j in ("digest", "maintenance")))
    # No scheduled tick acts in the 02:00-06:00 Prague quiet window (MODEL §8.7
    # item 12), in CET or in CEST: a tick there must be one the script's
    # Prague-clock window turns into a no-op.
    sys.path.insert(0, HERE)
    sys.dont_write_bytecode = True
    import datetime
    import gsc_notify as nt
    acting, quiet = [], []
    for day in ("2026-01-14", "2026-01-17", "2026-07-15", "2026-07-18"):     # Wed/Sat in CET and in CEST
        for cron in re.findall(r"cron: '([^']+)'", notify):
            minute, hours, _dom, _mon, dows = cron.split()
            for hour in (int(h) for h in hours.split(",")):
                when = datetime.datetime.fromisoformat("%sT%02d:%s:00+00:00" % (day, hour, minute))
                if str(when.isoweekday() % 7) not in dows.replace("1-5", "1,2,3,4,5").split(",") and dows != "*":
                    continue
                task = nt.pick_task({"EVENT_SCHEDULE": cron})
                acts = nt.maintenance_in_window(when) if task == "maintenance" else nt.in_window(when)
                local = when.astimezone(nt.PRAGUE)
                if acts:
                    acting.append("%s %s" % (task, local.strftime("%a %H:%M")))
                    if 2 <= local.hour < 6:
                        quiet.append("%s %s -> %s Prague" % (cron, day, local.strftime("%H:%M")))
    record("no scheduled gsc-notify tick acts in the 02:00-06:00 Prague quiet window", not quiet, quiet)
    record("maintenance acts at 06:30 Prague in CET and in CEST",
           all(("maintenance %s 06:30" % d) in acting for d in ("Wed", "Sat")), acting)
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
