#!/usr/bin/env python3
"""gsc-notify: the morning digest, the standing 'GSC - needs Jakub' issue and
the daily maintenance run (MODEL v4.5.0 §8.7 items 10-11). Run by
.github/workflows/gsc-notify.yml.

Inputs (environment): GH_TOKEN (the per-run GITHUB_TOKEN), REPO, GSC_AUTOMERGE,
EVENT_SCHEDULE (the cron that fired, if any) and TASK (digest | maintenance,
manual dispatch).

Task: the '30 4,5 * * *' schedule is maintenance; any other schedule is the
digest; a manual dispatch runs TASK.

Digest (weekdays 08:30, Saturday/Sunday 09:45 Europe/Prague). Three UTC crons
fire per day (a dropped scheduled run still leaves a later tick inside the
window, in CET and in CEST); the Prague clock decides: post only when target
<= now < target + 3 h and no digest exists yet for the Prague date (a manual
dispatch skips the window, never the dedupe). Title 'GSC digest {Ddd d Mon}
- {m} merged, {h} needs you', prefixed 'STALL - ' when more than 15 finished
routine PRs wait > 24 h, or when no GSC INTAKE PR merged in 30 h while a row
file merged more than 6 h ago still waits on main. Assigned to and
@mentioning jakubhoryna. Sections: Needs you; Merged since; Held zone changes
(SWEEP) - J11: a SWEEP merges with its held-zone changes, so the digest is
where they reach Jakub (each merged SWEEP's portfolio table against
register.csv at the commit's first parent; never counted as needs-you); WATCH
nearest the buy zone (with the register tool's status_hint, so a key is IN
RANGE only when both primaries pass at Px, MODEL §8.3, R10); INCOMPLETE and
stopped runs; Health (with the register page link, MODEL §7.4: a private
claude.ai artifact that INTAKE refreshes). The new digest is created
first, then the previous open digest is closed. No PR is linked or written
'#n' (V4: a cross-reference may wake the routine session watching it): open
and closed PRs are written 'PR n' with a search link, merged ones link their
commit on main or the memo itself, and the whole body passes no_hash_ref.

Maintenance (06:30 Europe/Prague: after INTAKE's 06:00 start, inside the
usage window it opens, never in the 02:00-06:00 quiet window; MODEL §8.7
item 12). Two UTC crons; the Prague clock decides: run only when 06:30 <= now
< 08:30 and gsc-automerge has not been dispatched since 06:30 today (a manual
dispatch skips both). It ensures the needs-Jakub issue; re-runs guard runs
that GitHub cancelled, timed out or failed to start (attempt 1 only, at most
20 per run, never a 'failure') on open finished routine PRs, then polls them
together for at most 6 minutes; flags a finished routine PR whose head sha
has no non-skipped guard run after 1 h ('guard-missing') or whose guard run
has been queued or running for more than 1 h ('guard-stuck'); then
dispatches gsc-automerge for a full merge sweep (a re-run started with
GITHUB_TOKEN fires no workflow_run). Each merge wakes the routine session
watching that PR, so the daily sweep runs here and nowhere earlier.

Python 3.11+ standard library only. Tests: test_gsc_notify.py.
"""
import datetime
import math
import os
import re
import sys
import time

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import gsc_automerge as am  # noqa: E402
import gsc_gh  # noqa: E402

PRAGUE = gsc_gh.prague_tz()
UTC = datetime.timezone.utc
MAINTENANCE_CRON = "30 4,5 * * *"
MAINTENANCE_AT = (6, 30)
MAINTENANCE_WINDOW = datetime.timedelta(hours=2)
DAYS = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
WINDOW = datetime.timedelta(hours=3)
STALL_PRS = 15
STALL_AGE = datetime.timedelta(hours=24)
STALL_INTAKE = datetime.timedelta(hours=30)
GUARD_MISSING_AGE = datetime.timedelta(hours=1)
GUARD_STUCK_AGE = datetime.timedelta(hours=1)
ROWS_WAITING_AGE = datetime.timedelta(hours=6)
MAX_RERUNS = 20
POLL_EVERY = 20
POLL_TOTAL = 360
MINUTES_FREE = 2000
MINUTES_WARN = 1500
SUMMARY_CAP = 160
# The register page (MODEL v4.5.0 §7.4): a private claude.ai artifact INTAKE refreshes best-effort.
REGISTER_PAGE = "https://claude.ai/artifact/FnU69xTYSTMEjqHB21rVPs"
MEMO_ADD_RE = re.compile(r"^memos/(?P<key>[A-Za-z0-9._-]+)/(?P=key)_\d{4}-\d{2}-\d{2}_GSC\.md$")
PR_NUM_RE = re.compile(r"\(#(\d+)\)$")
SUBJECT_JOB_RE = re.compile(r"^(?:HELD · )?GSC (ANALYSE|REVIEW|SEED|SWEEP|INTAKE)\b")
SWEEP_ROW_RE = re.compile(r"^queue/rows/\d{4}-\d{2}-\d{2}_\d{4}_SWEEP\.md$")
SWEEP_DATE_RE = re.compile(r"^GSC SWEEP (\d{4}-\d{2}-\d{2})\b")


# ---------------------------------------------------------------- time

def iso(dt):
    return dt.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_iso(value):
    if not value:
        return None
    try:
        return datetime.datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(UTC)
    except ValueError:
        return None


def pick_task(env):
    schedule = (env.get("EVENT_SCHEDULE") or "").strip()
    if schedule:
        return "maintenance" if schedule == MAINTENANCE_CRON else "digest"
    task = (env.get("TASK") or "digest").strip()
    return task if task in ("digest", "maintenance") else "digest"


def target_time(prague_now):
    hour, minute = (8, 30) if prague_now.weekday() < 5 else (9, 45)
    return prague_now.replace(hour=hour, minute=minute, second=0, microsecond=0)


def in_window(now):
    p = now.astimezone(PRAGUE)
    target = target_time(p)
    return target <= p < target + WINDOW


def maintenance_start(now):
    """Today's 06:30 Europe/Prague as an aware datetime."""
    p = now.astimezone(PRAGUE)
    return p.replace(hour=MAINTENANCE_AT[0], minute=MAINTENANCE_AT[1], second=0, microsecond=0)


def maintenance_in_window(now):
    start = maintenance_start(now)
    return start <= now.astimezone(PRAGUE) < start + MAINTENANCE_WINDOW


def day_label(p):
    return "%s %d %s" % (DAYS[p.weekday()], p.day, MONTHS[p.month - 1])


def digest_title(prague_now, merged, needs, stall):
    return "%sGSC digest %s - %d merged, %d needs you" % ("STALL - " if stall else "", day_label(prague_now),
                                                           merged, needs)


def age_text(delta):
    hours = delta.total_seconds() / 3600
    return "%.0f h" % hours if hours < 48 else "%.1f d" % (hours / 24)


def cell(text):
    return str(text).replace("|", "/").replace("\n", " ").strip() or "-"


# ---------------------------------------------------------------- data

def list_digests(gh):
    """Digest issues by github-actions[bot], newest first."""
    issues = gh.get_all("issues?state=all&creator=github-actions%5Bbot%5D&sort=created&direction=desc&per_page=100",
                        limit=2)
    out = [i for i in issues if gsc_gh.is_issue(i) and (i.get("user") or {}).get("login") == gsc_gh.BOT
           and gsc_gh.DIGEST_TITLE_RE.match(i.get("title") or "")]
    out.sort(key=lambda i: i.get("created_at") or "", reverse=True)
    return out


def merged_since(ctx, since):
    """First-parent commits on main since `since`: [{sha, date, subject, pr, adds}]."""
    raw = am.git_ok(ctx, ["-c", "core.quotePath=false", "log", "--first-parent", "--no-renames", "--name-status",
                          "--format=%x1e%H%x1f%cI%x1f%s", "--since=" + iso(since), am.MAIN], "reading main's log")
    commits = []
    for record in raw.decode("utf-8", "replace").split("\x1e")[1:]:
        head, _, rest = record.partition("\n")
        parts = head.split("\x1f")
        if len(parts) != 3:
            continue
        sha, date, subject = parts
        adds = [line.split("\t", 1)[1] for line in rest.splitlines() if line.startswith("A\t")]
        m = PR_NUM_RE.search(subject)
        commits.append({"sha": sha, "date": date, "subject": subject, "pr": int(m.group(1)) if m else None,
                        "adds": adds})
    return commits


def deciding_gate(ctx, fm):
    """'AVOID · Past WEAK · ROCE decline', 'WATCH · Cheapness · Px …', … ('-' for a missing reason)."""
    verdict = am.verdict_word(ctx, fm.get("verdict"))

    def reason(name):
        value = (fm.get(name) or "").strip()
        return "-" if value in ("", "-", "n.m.") else value
    if verdict == "BUY":
        return "BUY · all gates pass"
    if verdict == "DNAF":
        return "DNAF · Gate 0"
    if verdict == "WATCH":
        return "WATCH · Cheapness · Px %s vs trigger %s %s" % (fm.get("px") or "-", fm.get("trigger") or "-",
                                                               fm.get("px_unit") or "")
    if verdict == "AVOID":
        for field, failing, why, label in (("quality_past", "WEAK", "past_reason", "Past"),
                                           ("quality_future", "WEAK", "future_reason", "Future"),
                                           ("sf", "FAIL", "sf_reason", "SF")):
            grade = ctx.tool.first_token(fm.get(field) or "")
            if grade == failing:
                return "AVOID · %s %s · %s" % (label, grade, reason(why))
        return "AVOID · -"
    return verdict or "-"


def first_sentence(ctx, text):
    """First sentence of the memo's '## 1. Verdict' section, at most 160 characters."""
    body = None
    for heading, lines in ctx.tool.sections_of(text or "").items():
        if re.match(r"1\.\s*Verdict", heading):
            body = lines
            break
    if body is None:
        return "-"
    words = []
    for line in body:
        s = line.strip()
        if not s:
            if words:
                break
            continue
        if s.startswith(("|", "#", ">", "---")):
            if words:
                break
            continue
        words.append(re.sub(r"^[-*]\s+", "", s))
    flat = re.sub(r"[*_`]", "", " ".join(words)).strip()
    m = re.match(r"^(.+?[.!?])(?:\s|$)", flat)
    sentence = m.group(1) if m else flat
    return sentence if len(sentence) <= SUMMARY_CAP else sentence[:SUMMARY_CAP - 1].rstrip() + "…"


def memo_rows(ctx, commits):
    rows, others = [], []
    for c in commits:
        if c["subject"].startswith('Revert "'):
            continue
        link = gsc_gh.commit_link(ctx.repo, c["sha"])     # never /pull/{n} (V4)
        job_m = SUBJECT_JOB_RE.match(c["subject"])
        memos = [p for p in c["adds"] if MEMO_ADD_RE.match(p)]
        for path in memos:
            key = MEMO_ADD_RE.match(path).group("key")
            text = am.show(ctx, c["sha"], path)
            fm = am.front_matter(ctx, text)
            if job_m and job_m.group(1) in ("ANALYSE", "REVIEW"):
                job = job_m.group(1)
            elif c["subject"].startswith("GSC: "):
                job = "attended"
            else:
                job = "REVIEW" if ("archive/memos/%s/" % key) in " ".join(c["adds"]) else "ANALYSE"
            rows.append({"key": key, "company": fm.get("company") or "-", "job": job,
                         "gate": deciding_gate(ctx, fm), "summary": first_sentence(ctx, text),
                         "link": gsc_gh.blob_link(ctx.repo, c["sha"], path)})
        if not memos and job_m and job_m.group(1) in ("SWEEP", "INTAKE", "SEED"):
            subject = cell(PR_NUM_RE.sub("", c["subject"]).strip())
            others.append("- %s · PR %d · [commit](%s)" % (subject, c["pr"], link) if c["pr"]
                          else "- %s · [commit](%s)" % (subject, link))
    return rows, others


def watch_nearest(ctx, limit=5):
    """[(key, company, px, trigger, distance, status)] for WATCH rows, nearest
    first. status is the register tool's status_hint (MODEL §8.3 step 3, R10): a
    key whose core numbers establish the primaries is IN RANGE only when MCap/FCF
    <= 8 and EV/OI no-cash <= 7 both hold at Px (holding credits are a constant,
    V14: no holding price check)."""
    out, by_key = [], {}
    today = ctx.now().astimezone(PRAGUE).strftime("%Y-%m-%d")
    text = am.show(ctx, am.MAIN, "register.csv")
    if text is not None:
        rows, _ = ctx.tool.read_csv_text(text, legacy_ok=True)
        by_key = {r["key"]: r for r in rows}
        cand = [r for r in rows if r["verdict"] == "WATCH"]
    else:
        md = am.show(ctx, am.MAIN, "_REGISTER.md") or ""
        cand = []
        for heading, lines in ctx.tool.sections_of(md).items():
            if re.match(r"WATCH\b", heading):
                for r in ctx.tool.table_rows(lines):
                    key = re.split(r"[\s(]", (r.get("ticker") or "").strip(), 1)[0]
                    cand.append({"key": key, "company": r.get("company", "-"), "px": r.get("px", ""),
                                 "trigger": r.get("trigger", "")})
    for row in cand:
        try:
            p, t = float(row["px"]), float(row["trigger"])
        except (TypeError, ValueError):
            continue
        if t > 0 and p > 0:
            status, _dist = ctx.tool.status_hint(row, row["px"], rows_by_key=by_key, as_of=today)
            out.append((row["key"], row["company"], row["px"], row["trigger"], p / t - 1, status))
    out.sort(key=lambda r: (r[4], r[0]))
    return out[:limit]


def held_zone_changes(ctx, commits):
    """[{key, portfolio, sweep, px, date, link}] for the SWEEPs merged since the
    last digest (J11, MODEL §8.7 item 11): each SWEEP row file, read at its merge
    commit (INTAKE deletes it from main later), against the held rows of
    register.csv at the commit's first parent. A held name the table does not
    list is no zone change (gsc-automerge holds such a SWEEP for Jakub)."""
    out = []
    for c in commits:
        m = SWEEP_DATE_RE.match(c["subject"])
        if not m:
            continue
        held = {k: v for k, v in am.register_rows(ctx, c["sha"] + "^").items() if v["held"]}
        for path in [p for p in c["adds"] if SWEEP_ROW_RE.match(p)]:
            sections = ctx.tool.sections_of(am.show(ctx, c["sha"], path) or "")
            heading = next((h for h in sections if h.lower().startswith("portfolio table")), None)
            table = {}
            for row in ctx.tool.table_rows(sections.get(heading, [])) if heading else []:
                key = re.split(r"[\s(]", (row.get("ticker") or "").strip().strip("`"), 1)[0]
                zone = next((row[col] for col in row if col.startswith("zone")), "")
                table[key] = (zone, row.get("current") or row.get("px") or "-")
            for key, entry in sorted(held.items()):
                if key not in table:
                    continue
                swept = am.ZONE_WORD_RE.match(table[key][0] or "")
                reg = am.ZONE_WORD_RE.match(entry["zone"] or "")
                if swept and (not reg or reg.group(1) != swept.group(1)):
                    out.append({"key": key, "portfolio": entry["zone"] or "-", "sweep": swept.group(1),
                                "px": table[key][1], "date": m.group(1),
                                "link": gsc_gh.commit_link(ctx.repo, c["sha"])})
    return out


def open_items_count(ctx):
    text = am.show(ctx, am.MAIN, "queue/TODO.md") or ""
    count, inside = 0, False
    for line in text.replace("\r\n", "\n").split("\n"):
        if line.startswith("## "):
            inside = line.startswith("## ▶ Open items (register)")
            continue
        if inside and line.startswith("- "):
            count += 1
    return count


def last_intake(ctx):
    """(commit time, subject, sha) of the newest GSC INTAKE merge on main, or Nones."""
    raw = am.git_ok(ctx, ["log", "--first-parent", "-1", "--format=%cI%x1f%s%x1f%H", "--grep=^GSC INTAKE ",
                          am.MAIN], "finding the last INTAKE").decode("utf-8", "replace").strip()
    if not raw:
        return None, None, None
    date, subject, sha = (raw.split("\x1f") + ["", ""])[:3]
    return parse_iso(date), subject, sha or None


def rows_waiting(ctx, since_sha, cutoff):
    """Row files still on main that were added after `since_sha` (all of
    main's history when None) by a commit older than `cutoff`: work that an
    INTAKE should already have taken in."""
    present = set(am.git_ok(ctx, ["-c", "core.quotePath=false", "ls-tree", "--name-only", am.MAIN, "queue/rows/"],
                            "listing queue/rows").decode("utf-8", "replace").splitlines())
    rng = "%s..%s" % (since_sha, am.MAIN) if since_sha else am.MAIN
    raw = am.git_ok(ctx, ["-c", "core.quotePath=false", "log", "--first-parent", "--no-renames", "--diff-filter=A",
                          "--name-only", "--format=%x1e%cI", rng, "--", "queue/rows/"],
                    "listing rows added on main").decode("utf-8", "replace")
    waiting = set()
    for record in raw.split("\x1e")[1:]:
        head, _, rest = record.partition("\n")
        when = parse_iso(head.strip())
        if when is None or when >= cutoff:
            continue
        for path in rest.splitlines():
            path = path.strip()
            if path in present and not path.endswith("/README.md"):
                waiting.add(path)
    return len(waiting)


def finished(title):
    t = (title or "").rstrip()
    return not t.endswith("[running]") and not t.endswith("[fixing]")


def minutes_estimate(gh, now):
    """Month-to-date billable minutes, estimated: each completed, non-skipped
    run rounded up to a whole minute (every GSC workflow has one job)."""
    start = now.astimezone(UTC).replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    runs = gh.get_all("actions/runs?created=%%3E%%3D%s&exclude_pull_requests=true&per_page=100"
                      % iso(start), key="workflow_runs", limit=40)
    total = 0
    for run in runs:
        if run.get("status") != "completed" or run.get("conclusion") == "skipped":
            continue
        begin, end = parse_iso(run.get("run_started_at")), parse_iso(run.get("updated_at"))
        if begin and end:
            total += max(1, math.ceil((end - begin).total_seconds() / 60))
    return total


def workflow_runs(gh, workflow, since):
    return gh.get_all("actions/workflows/%s/runs?created=%%3E%%3D%s&per_page=100" % (workflow, iso(since)),
                      key="workflow_runs", limit=20)


# ---------------------------------------------------------------- digest

def build_digest(ctx, now, since):
    """(title, body, needs_count, merged_count)."""
    p = now.astimezone(PRAGUE)
    am.fetch_main(ctx)
    needs, info, waiting = [], [], []
    running = held = 0
    oldest = None
    open_prs = [pr for pr in ctx.gh.get_all("pulls?state=open&base=main&per_page=100")
                if gsc_gh.routine_kind(pr) is not None]
    stalled = 0
    for pr in open_prs:
        n = int(pr["number"])
        updated = parse_iso(pr.get("updated_at"))
        if finished(pr.get("title")) and updated is not None:
            oldest = updated if oldest is None or updated < oldest else oldest
            if now - updated > STALL_AGE:
                stalled += 1
        try:
            o = am.decide(ctx, pr)
        except Exception as exc:
            o = am.Outcome(am.HOLD_NOTIFY, "automerge-exception", "gsc-automerge could not evaluate it (%s)"
                           % type(exc).__name__, title=pr.get("title") or "")
        label = cell(" ".join(x for x in (o.job, o.key) if x) or (pr.get("title") or "")[:60])
        link = gsc_gh.search_link(ctx.repo, n)
        if o.kind == am.WAIT and o.code == "running":
            running += 1
            continue
        if o.kind in (am.HOLD, am.HOLD_NOTIFY):
            held += 1
            if o.code == "intake-base":
                info.append("- PR %d · %s — %s · [open](%s)" % (n, label, cell(o.text), link))
                continue
            text = "yours, marked [fixing]" if o.code == "fixing" else o.text
            needs.append("- PR %d · %s — %s · [open](%s)" % (n, label, cell(gsc_gh.no_hash_ref(text)), link))
        elif o.kind == am.MERGE and ctx.mode != "on":
            needs.append("- PR %d · %s — auto-merge %s: ready for your merge · [open](%s)"
                         % (n, label, ctx.mode, link))
        elif o.kind == am.MERGE:
            waiting.append("- PR %d · %s — eligible; gsc-automerge merges it on its next run" % (n, label))
        else:
            waiting.append("- PR %d · %s — waiting: %s" % (n, label, cell(o.text)))

    commits = merged_since(ctx, since)
    merged = [c for c in commits if c["pr"]]
    memos, others = memo_rows(ctx, commits)
    last_dt, _last_subject, last_sha = last_intake(ctx)
    waiting_rows = rows_waiting(ctx, last_sha, now - ROWS_WAITING_AGE)
    no_intake = (last_dt is None or now - last_dt > STALL_INTAKE) and waiting_rows > 0
    stall = stalled > STALL_PRS or no_intake

    lines = ["@jakubhoryna GSC morning digest, %s %d (Europe/Prague)." % (day_label(p), p.year), ""]
    lines.append("## Needs you (%d)" % len(needs))
    lines += needs or ["- nothing is held for you"]
    lines.append("- Register open items: %d — [queue/TODO.md ▶ Open items (register)]"
                 "(https://github.com/%s/blob/main/queue/TODO.md#-open-items-register)"
                 % (open_items_count(ctx), ctx.repo))
    lines += info
    lines += ["", "## Merged since %s (%d)" % (day_label(since.astimezone(PRAGUE)) + " "
                                              + since.astimezone(PRAGUE).strftime("%H:%M"), len(merged))]
    if memos:
        lines += ["| Key | Company | Job | Verdict · deciding gate | Summary | Link |", "|---|---|---|---|---|---|"]
        for r in memos:
            lines.append("| %s | %s | %s | %s | %s | [memo](%s) |" % (cell(r["key"]), cell(r["company"]), r["job"],
                                                                     cell(r["gate"]), cell(r["summary"]), r["link"]))
    lines += others
    if not memos and not others:
        lines.append("- nothing merged")
    lines += ["", "## Held zone changes (SWEEP)"]
    zones = held_zone_changes(ctx, merged)
    if zones:
        lines += ["| Key | Portfolio zone | Sweep zone | Px | Sweep |", "|---|---|---|---|---|"]
        for z in zones:
            lines.append("| %s | %s | %s | %s | %s · [commit](%s) |" % (cell(z["key"]), cell(z["portfolio"]),
                                                                    z["sweep"], cell(z["px"]), z["date"], z["link"]))
    else:
        lines.append("- none")
    lines += ["", "## WATCH nearest the buy zone"]
    nearest = watch_nearest(ctx)
    if nearest:
        lines += ["| Key | Company | Px | Trigger | Distance | Status |", "|---|---|---|---|---|---|"]
        for key, company, px, trigger, dist, status in nearest:
            lines.append("| %s | %s | %s | %s | %+.1f%% | %s |" % (cell(key), cell(company), px, trigger,
                                                                   dist * 100, status))
    else:
        lines.append("- no WATCH row with a numeric Px and trigger")
    lines += ["", "## INCOMPLETE and stopped runs"]
    flagged = []
    for c in merged:
        if " — INCOMPLETE (" in c["subject"]:
            flagged.append("- %s · PR %d · [commit](%s)" % (cell(PR_NUM_RE.sub("", c["subject"]).strip()), c["pr"],
                                                             gsc_gh.commit_link(ctx.repo, c["sha"])))
    recent = ctx.gh.get("pulls?state=all&sort=updated&direction=desc&per_page=100") or []
    for pr in recent:
        updated = parse_iso(pr.get("updated_at"))
        title = (pr.get("title") or "").rstrip()
        if updated is None or updated < since or not SUBJECT_JOB_RE.match(title):
            continue
        if am.STOP_RE.search(title) or title.endswith("[abandoned]") or title.endswith("[superseded]"):
            n = int(pr["number"])
            where = ("[open](%s)" % gsc_gh.search_link(ctx.repo, n) if pr.get("state") == "open"
                     else "[closed](%s)" % gsc_gh.search_link(ctx.repo, n, state="closed"))
            flagged.append("- PR %d · %s · %s" % (n, cell(gsc_gh.no_hash_ref(title)), where))
    lines += flagged or ["- none"]

    lines += ["", "## Health"]
    raw = getattr(ctx, "mode_raw", None)
    lines.append("- GSC_AUTOMERGE: %s%s" % (ctx.mode, "" if raw in (None, "", ctx.mode) else
                                            " (value %r is not one of off, dry-run, on, so auto-merge is off)" % raw))
    guard = workflow_runs(ctx.gh, "gsc-guard.yml", since)
    counts = {}
    for run in guard:
        counts[run.get("conclusion") or run.get("status") or "?"] = counts.get(run.get("conclusion")
                                                                              or run.get("status") or "?", 0) + 1
    lines.append("- Guard runs since the last digest: %s; re-runs (attempt ≥ 2): %d" % (
        " · ".join("%s %d" % (k, counts.get(k, 0)) for k in ("success", "failure", "cancelled", "skipped")),
        sum(1 for r in guard if int(r.get("run_attempt") or 1) > 1)))
    failed = [r for r in workflow_runs(ctx.gh, "gsc-automerge.yml", since) if r.get("conclusion") == "failure"]
    lines.append("- gsc-automerge runs failed: %d ([Actions](https://github.com/%s/actions/workflows/gsc-automerge.yml))"
                 % (len(failed), ctx.repo))
    lines.append("- Open routine PRs: %d running · %d held · oldest finished %s" % (
        running, held, age_text(now - oldest) if oldest else "-"))
    lines += waiting
    lines.append("- Stall test: %d finished routine PRs waiting > 24 h (limit %d) · last INTAKE merge %s (limit 30 h "
                 "while row files merged > 6 h ago wait on main: %d)%s"
                 % (stalled, STALL_PRS, (age_text(now - last_dt) + " ago") if last_dt else "never", waiting_rows,
                    " — STALL" if stall else ""))
    reg = am.front_matter(ctx, am.show(ctx, am.MAIN, "_REGISTER.md"))
    model = am.front_matter(ctx, am.show(ctx, am.MAIN, "model/MODEL.md"))
    lines.append("- Register %s · %s on main · MODEL %s" % (reg.get("register_version", "?"),
                                                              reg.get("register_date", "?"),
                                                              model.get("model_version", "?")))
    lines.append("- Register page: %s (private; refreshed by INTAKE)" % REGISTER_PAGE)
    minutes = minutes_estimate(ctx.gh, now)
    lines.append("- Actions minutes this month (estimate): %d of %d%s" % (
        minutes, MINUTES_FREE, " — WARNING: above %d" % MINUTES_WARN if minutes >= MINUTES_WARN else ""))
    lines += ["", "*Framework output, not investment advice.*"]
    title = digest_title(p, len(merged), len(needs), stall)
    # No '#<digit>' anywhere (V4): memo summaries, company names and labels included.
    return title, gsc_gh.no_hash_ref("\n".join(lines) + "\n"), len(needs), len(merged)


def run_digest(ctx, manual=False):
    now = ctx.now()
    p = now.astimezone(PRAGUE)
    if not manual and not in_window(now):
        ctx.log("digest: outside the %s window (Prague %s) - nothing to do" % (
            target_time(p).strftime("%H:%M"), p.strftime("%a %H:%M")))
        return 0
    digests = list_digests(ctx.gh)
    for d in digests:
        created = parse_iso(d.get("created_at"))
        if created and created.astimezone(PRAGUE).date() == p.date():
            ctx.log("digest: already posted for %s (issue %s)" % (p.date(), d.get("number")))
            return 0
    since = parse_iso(digests[0].get("created_at")) if digests else None
    since = since or now - datetime.timedelta(hours=24)
    title, body, _needs, _merged = build_digest(ctx, now, since)
    created = ctx.gh.request("POST", "issues", {"title": title, "body": body,
                                                "assignees": [gsc_gh.OWNER]})[0]
    ctx.log("digest: created issue %s" % created.get("number"))
    for d in digests:
        if d.get("state") == "open" and d.get("number") != created.get("number"):
            ctx.gh.close_digest(d["number"])
            ctx.log("digest: closed the previous digest %s" % d["number"])
    return 0


# ---------------------------------------------------------------- maintenance

def flag(ctx, pr, sha, code, text):
    """One needs-Jakub comment per (PR, head sha, code)."""
    n = int(pr["number"])
    marker = "<!-- gsc-hold pr=%d sha=%s code=%s -->" % (n, sha[:7], code)
    body = "@jakubhoryna PR %d held - %s\n%s\nOpen: %s\n%s" % (
        n, text, gsc_gh.no_hash_ref(pr.get("title") or ""), gsc_gh.search_link(ctx.repo, n), marker)
    gsc_gh.post_needs_comment(ctx.gh, body, marker, pr.get("created_at"))


def maintenance_due(ctx, now):
    """(True, '') when a scheduled maintenance should run now, else (False, why)."""
    if not maintenance_in_window(now):
        return False, "outside the 06:30 window (Prague %s)" % now.astimezone(PRAGUE).strftime("%a %H:%M")
    start = iso(maintenance_start(now))
    runs = ctx.gh.get_all("actions/workflows/gsc-automerge.yml/runs?event=workflow_dispatch&created=%%3E%%3D%s"
                          "&per_page=100" % start, key="workflow_runs", limit=2)
    if runs:
        return False, "gsc-automerge already dispatched since 06:30 (run %s)" % runs[0].get("id")
    return True, ""


def run_maintenance(ctx, clock=time.monotonic, scheduled=True):
    now = ctx.now()
    if scheduled:
        due, why = maintenance_due(ctx, now)
        if not due:
            ctx.log("maintenance: %s - nothing to do" % why)
            return 0
    gsc_gh.ensure_needs_issue(ctx.gh)
    reruns = []
    for pr in ctx.gh.get_all("pulls?state=open&base=main&per_page=100"):
        if gsc_gh.routine_kind(pr) is None or not finished(pr.get("title")):
            continue
        sha = (pr.get("head") or {}).get("sha") or ""
        state, run = am.guard_state(ctx.gh, sha)
        if state == "retry" and len(reruns) < MAX_RERUNS:
            ctx.gh.request("POST", "actions/runs/%d/rerun" % int(run["id"]))
            reruns.append(int(run["id"]))
            ctx.log("maintenance: re-ran guard run %s (PR %s, %s)" % (run["id"], pr["number"], run.get("conclusion")))
        elif state == "none":
            updated = parse_iso(pr.get("updated_at"))
            if updated is not None and now - updated > GUARD_MISSING_AGE:
                flag(ctx, pr, sha, "guard-missing", "the guard never ran on its head sha %s" % sha[:7])
        elif state == "pending" and run is not None:
            created = parse_iso(run.get("created_at"))
            if created is not None and now - created > GUARD_STUCK_AGE:
                flag(ctx, pr, sha, "guard-stuck", "its guard run %s on head sha %s has been %s for %s"
                     % (run.get("id"), sha[:7], run.get("status") or "unfinished", age_text(now - created)))
    # A re-run started with GITHUB_TOKEN fires no workflow_run: poll them together.
    start = clock()
    pending = list(reruns)
    while pending and clock() - start < POLL_TOTAL:
        ctx.sleep(POLL_EVERY)
        pending = [rid for rid in pending if (ctx.gh.get("actions/runs/%d" % rid) or {}).get("status") != "completed"]
    if pending:
        ctx.log("maintenance: %d re-run(s) still running after %d s" % (len(pending), POLL_TOTAL))
    ctx.gh.request("POST", "actions/workflows/gsc-automerge.yml/dispatches", {"ref": "main"})
    ctx.log("maintenance: %d re-run(s); gsc-automerge dispatched" % len(reruns))
    return 0


# ---------------------------------------------------------------- main

def main(env=None, gh=None, git=None, sleep=None, now=None, clock=time.monotonic):
    env = os.environ if env is None else env
    repo = env.get("REPO", "")
    task = pick_task(env)
    # Only maintenance may re-run guard runs or dispatch the merger (its job alone has actions: write).
    gh = gh or gsc_gh.Gh(env.get("GH_TOKEN", ""), repo, allow_actions=(task == "maintenance"))
    ctx = am.Ctx(gh, git=git, repo=repo, mode=am.read_mode(env.get("GSC_AUTOMERGE")), now=now, sleep=sleep,
                 log=lambda line: print("gsc-notify: " + am.chk.printable(line)))
    ctx.mode_raw = env.get("GSC_AUTOMERGE")
    scheduled = bool((env.get("EVENT_SCHEDULE") or "").strip())
    try:
        if ctx.tool is None:
            raise am.AutomergeError("cannot load routines/tools/gsc_register.py")
        if task == "maintenance":
            return run_maintenance(ctx, clock, scheduled=scheduled)
        return run_digest(ctx, manual=not scheduled)
    except Exception as exc:  # tell Jakub once per Prague day
        ctx.log("%s failed: %s" % (task, type(exc).__name__))
        try:
            day = ctx.now().astimezone(PRAGUE)
            marker = "<!-- gsc-hold pr=0 sha=0000000 code=notify-error-%s -->" % day.strftime("%Y-%m-%d")
            start = day.replace(hour=0, minute=0, second=0, microsecond=0)
            gsc_gh.post_needs_comment(gh, "@jakubhoryna gsc-notify %s failed: %s\n%s"
                                      % (task, type(exc).__name__, marker), marker, iso(start))
        except Exception:
            pass
        return 1


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(errors="backslashreplace")
    except AttributeError:
        pass
    sys.exit(main())
