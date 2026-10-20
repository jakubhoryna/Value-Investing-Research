#!/usr/bin/env python3
"""GSC routine guard: PreToolUse hook (MODEL §8.7, spec v2 §5).

Runs only when GSC_SESSION=routine. Any other value: exit 0 at once, nothing
is read or checked. settings.json gates in the shell as well, so attended
sessions never even start Python.

In routine sessions it blocks (exit 2, one stderr line):
  * any job-gated call from a session acting as another job. A routine session's job is the one its
    prompt names: the first user prompt in the hook's transcript_path begins 'GSC ROUTINE: <JOB>'
    (CLAUDE.md mode table). git push, a gh api call other than GET, a push notification, the artifact
    tools and the allowed MCP tool need the current run branch's job to equal it (a gh api write off
    a run branch, as in INTAKE's step-0 sweep before its branch exists, needs a readable prompt that
    is not WEEKLY). A readable first prompt naming no routine job is refused; a transcript that cannot
    be read falls back to the branch alone (the pre-v4.6.1 rule). A run never leaves
    its run branch: once HEAD is on
    a claude/gsc-* branch, git switch, git checkout of a branch and git branch <new> are refused;
  * Edit/Write/NotebookEdit into framework-locked paths, .git anywhere below the root, and the
    session transcripts (~/.claude/projects);
  * Bash/Monitor commands that push anything but the run's own claude/gsc-*
    branch (from the root's own repository: a nested or copied .git is refused), merge or rewrite
    history, call gh outside the REST allowlist, handle tokens, fetch anything but origin main, read
    curl or wget options from a file, or visibly write into locked paths. WEEKLY (its prompt or its
    claude/gsc-weekly-* branch, local only: a guard identity, never pushed) is refused every git
    push, every gh api call other than GET, git add, commit, mv and rm, and editor writes inside the
    repo (MODEL v4.6.1 section 8.7, routines/WEEKLY.md: WEEKLY never writes to the repo or to GitHub);
  * any edit of the append-only archive/ tree (MODEL v4.5.0 section 7.5):
    Edit/Write/NotebookEdit, redirections, tee, touch, truncate, in-place
    sed/perl/awk into archive/, mv or git mv out of archive/, and rm, git rm
    or cp/mv onto an archive/ file that git tracks. New archive files are made
    with cp or git mv; untracked ones (INTAKE's restart) stay removable;
  * Edit/Write/NotebookEdit of a memo that exists on origin/main (MODEL v4.5.0
    section 6.6): a memo is never edited in place; a REVIEW writes a new file
    and moves the prior to archive/memos/ with git mv;
  * any hand write of the register (MODEL v4.5.0 section 7.1): editor tools,
    redirections, tee, touch, truncate, dd, in-place sed/perl/awk, cp/mv onto,
    mv away and rm of _REGISTER.md or register.csv at the repo root. Only
    routines/tools/gsc_register.py writes them (run with python3; reading and
    copying them elsewhere, and git checkout of them, stay allowed). Its
    `rebuild` subcommand (the one-time attended lean rebuild), `retrigger`
    subcommand (the one-time attended trigger re-read of round 2, R10) and
    `retire` subcommand (the attended RETIRED state and its --undo, MODEL
    v4.6.0 section 7.1, G5) are refused, whether the tool runs as a script
    or as a module (python3 -m routines.tools.gsc_register, or a runner
    module such as runpy or pdb in front of it);
  * PushNotification outside the routine push rule (MODEL v4.6.1 §8.7 item
    11, routines/README.md §5): two classes only, each in its exact form. 'GSC BUY · {JOB} {KEY}
    {D} · PR {n} · {reason}' comes from that ANALYSE or REVIEW run (JOB, KEY and D are its branch's);
    'GSC WEEKLY · {period} · {d} to decide · {f} to fix · {m} memos · {weekly page url}' or 'GSC
    WEEKLY · not published · {reason}' only from the WEEKLY run. The HELD, VERDICT CHANGE, STOPPED,
    BLOCKED and STALL pushes are retired: their content reaches Jakub in the weekly report. A push is
    one line of at most 200 characters without '#', control, format or separator characters, or any
    link but the weekly page's, and each class is sent at most once per run (an O_EXCL marker per
    session and class in the repo's git dir, which no routine command may touch);
  * any comment on a PR or issue: routines never comment (a comment wakes the
    session watching it; the needs-Jakub issue belongs to the gsc-automerge
    and gsc-notify workflows);
  * the claude.ai artifact tools outside two steps. INTAKE's register page
    (MODEL v4.5.0 section 7.4, routines/INTAKE.md step 9): Artifact passes for INTAKE only,
    as action read or publish on the one
    register page url (REGISTER_PAGE_URL), a publish only of the rendered file
    REGISTER_PAGE_FILE from outside the repo, with no other field (no new
    artifact, delete, list, open, pin, capabilities, assets, type, force or
    sharing). WEEKLY's report page (MODEL v4.6.1 section 7.4,
    routines/WEEKLY.md): for WEEKLY only and on the one
    url WEEKLY_PAGE_URL, Artifact read, and Artifact publish with exactly
    action, url, file_path and asset: true (an upload to the page's asset
    store, never the page itself) of one dataset file {id}.json from a
    gsc-weekly folder outside the repo, read first: a JSON array of flat rows whose keys are that
    dataset's own fields (DATASET_FIELDS), never a private field; ArtifactData get of one
    datasets/{id} document, list of the datasets collection (query limit/cursor only), and one batch
    of exactly one pinned (if_version) update per datasets/{id} document, meta last, each changing
    exactly source (kind 'file', a /_blob/ asset url, name {id}.json, format json) and updated (one
    at for the whole batch, within 6 h of the hook's clock, by 'GSC WEEKLY routine'). Never set,
    delete, str_replace, query, profiles, as_level, out_dir, file_path, the page's files/ or dash/
    documents, or another url. An artifact file_path with '$' or a leading '~' is refused (the tool
    takes it literally). ArtifactComments and any other artifact tool are refused;
  * every MCP tool (mcp__*; settings.json routes them here with a second
    PreToolUse matcher): MCP servers attached to the account (GitHub,
    remote sessions and routines, document stores) would bypass the gh api
    REST allowlist. Only the read-only schedule listing MCP_ALLOWED names
    passes, and only for WEEKLY (its optional schedule health);
  * the built-in worktree, cron and design-sync tools (BUILTIN_REFUSED): no routine uses them.
Any unexpected error also exits 2 (fail closed).

Python 3.11 stdlib only, no network. Files read: the hook's transcript (its first
lines, up to the first user prompt) for job-gated calls, and a weekly dataset file before its
upload. Subprocesses: `git symbolic-ref`, for the job-gated calls, a branch move and the WEEKLY
write rules; `git rev-parse` (the git dir, and the directory a push runs in), only for `git push`
and PushNotification; `git ls-files`, only when a command would remove or
overwrite a path under archive/; `git ls-tree origin/main`, only when an
editor tool targets a path under memos/. The trusted tools under routines/tools/ never spell a
locked path fragment in their source (the interpreter-code scan cannot tell a read from a write).
This is a guard rail, not a sandbox:
gsc_guard_post.py self-heals locked files after each tool call and the
gsc-guard PR check is the visible second layer (it also rejects any M or D
under archive/).
"""
import datetime
import glob
import json
import os
import re
import shlex
import subprocess
import sys
import unicodedata

# ---------------------------------------------------------------- constants

REPO = "jakubhoryna/Value-Investing-Model"
# Preflight self-test (routines/README §0): always refused, harmless when the guard is off.
CANARY = ": gsc-guard-canary"
LOCKED_DIRS = ("model", "routines", ".claude", ".github")
LOCKED_NAMES = ("CLAUDE.md", "CLAUDE.local.md", "AGENTS.md")
# Append-only history (MODEL v4.5.0 §7.5). Not locked: routines add files here
# (INTAKE snapshots and archives by cp / git mv). Not in the post hook's
# pathspecs either, which would unstage those adds.
APPEND_ONLY_DIRS = ("archive",)
APPEND_ONLY_HINT = "archive/ is append-only: copy with cp or move with git mv (MODEL §7.5)"
# Memos on main are never edited in place (MODEL v4.5.0 §6.6). The run's own
# new memo is not on main yet, so writing and fixing it stays allowed.
MEMO_DIR = "memos"
MAIN_REF = "refs/remotes/origin/main"
MEMO_HINT = ("a memo on main is never edited in place: a REVIEW writes a new memo and moves "
             "the prior to archive/memos/ with git mv (MODEL §6.6)")

# The register and its machine twin (MODEL v4.5.0 §7.1): written only by the register
# tool, never by a hand edit. Repo-root files, compared without case.
REGISTER_FILES = ("_register.md", "register.csv")
REGISTER_HINT = ("the register is written only by routines/tools/gsc_register.py (MODEL §7.1): "
                 "run its apply/render commands; never edit _REGISTER.md or register.csv by hand")

# Routine phone pushes (MODEL v4.6.1 §8.7 item 11, routines/README.md §5): two classes only,
# one per class per run, one line of at most PUSH_MAX characters, no '#'.
#   BUY     'GSC BUY · {JOB} {KEY} {D} · PR {n} · {reason}': an ANALYSE or REVIEW memo with verdict
#           BUY; JOB must be the job of the current run branch;
#   WEEKLY  'GSC WEEKLY · {period} · …' or 'GSC WEEKLY · not published · {reason}': the WEEKLY run
#           only (its local claude/gsc-weekly-* branch).
# HELD, VERDICT CHANGE, STOPPED, BLOCKED and STALL are retired (v4.6.1): their content reaches
# Jakub in the weekly report, J11 (SWEEP held-zone changes) included.
PUSH_RE = re.compile(r"^GSC (BUY|WEEKLY) · (\S+)")
PUSH_RETIRED_RE = re.compile(r"^GSC (HELD|VERDICT CHANGE|STOPPED|BLOCKED|STALL) · ")
PUSH_MAX = 200
PUSH_HINT = ("only 'GSC BUY · {ANALYSE|REVIEW} {KEY} {D} · PR {n} · {reason}' from that ANALYSE or REVIEW run, "
             "or 'GSC WEEKLY · {period} · {d} to decide · {f} to fix · {m} memos · {weekly page}' or "
             "'GSC WEEKLY · not published · {reason}' from the WEEKLY run (routines/README.md §5)")
# The exact forms (MODEL v4.6.1 review): the BUY key and date are the run branch's; the published WEEKLY
# line is the one gsc_weekly.py writes, ending with the weekly page url; no other url in any push.
PUSH_BUY_RE = re.compile(r"^GSC BUY · (?P<job>ANALYSE|REVIEW) (?P<key>[A-Za-z0-9._-]+) (?P<date>\d{4}-\d{2}-\d{2}) · "
                         r"PR \d+ · \S.*$")
PUSH_WEEKLY_RE = re.compile(r"^GSC WEEKLY · (?:[A-Z][a-z]{2} \d{1,2} [A-Z][a-z]{2}(?: \d{4})? – [A-Z][a-z]{2} \d{1,2} "
                            r"[A-Z][a-z]{2} \d{4} · \d{1,4} to decide · \d{1,4} to fix · \d{1,4} memos · "
                            r"(?P<url>https://claude\.ai/artifact/6L264JT8pg5vuia9dUrcuj)|not published · \S.*)$")
URL_TEXT_RE = re.compile(r"(?i)://|\bwww\.|\bhttps?:")
# Characters a push never carries: controls, format characters (zero-width, bidi) and the line and
# paragraph separators that would break the one-line rule.
PUSH_BAD_CATEGORIES = ("Cc", "Cf", "Zl", "Zp")
# The run-branch jobs (BRANCH_RE group 1) that may send each class.
PUSH_FROM = {"BUY": ("analyse", "review"), "WEEKLY": ("weekly",)}

# The register page (MODEL v4.5.0 §7.4, routines/INTAKE.md step 9): INTAKE refreshes one
# private claude.ai artifact in place, best-effort. read is the Artifact tool's own
# precondition for an update; publish sends the page rendered outside the repo by
# routines/tools/gsc_site.py. Only these fields pass: never a new artifact, a delete, a
# listing, open/pin, capabilities, assets, a type, force or sharing.
REGISTER_PAGE_URL = "https://claude.ai/artifact/FnU69xTYSTMEjqHB21rVPs"
REGISTER_PAGE_FILE = "gsc-register-page.html"
REGISTER_PAGE_FIELDS = {"read": {"action", "url"}, "publish": {"action", "url", "file_path", "label"}}
REGISTER_PAGE_HINT = ("only INTAKE's register page step may use the Artifact tool on the register page: action "
                      "read or publish on " + REGISTER_PAGE_URL + ", publishing /tmp/" + REGISTER_PAGE_FILE
                      + " (routines/INTAKE.md step 9)")

# The weekly report page (MODEL v4.6.1 §7.4, routines/WEEKLY.md): one private claude.ai Dashboard
# artifact. WEEKLY reads it (the Artifact tool's precondition for an upload), uploads each dataset
# file rendered outside the repo by routines/tools/gsc_weekly.py to the page's asset store
# (publish with asset: true; the page itself is never republished), reads the datasets/{id}
# documents for their versions, and repoints them at the new uploads with one ArtifactData batch
# of pinned updates of source and updated. Never the page's files/ or dash/ documents, never a
# set, delete or str_replace, never another url.
WEEKLY_PAGE_URL = "https://claude.ai/artifact/6L264JT8pg5vuia9dUrcuj"
WEEKLY_DIR = "gsc-weekly"                    # the render folder: /tmp/gsc-weekly/{id}.json
DATASET_IDS = ("summary", "meta", "kpis", "attention", "shortlist", "changes", "weekly", "pipeline",
               "coverage", "backlog", "held")
WEEKLY_PAGE_FIELDS = {"read": {"action", "url"}, "publish": {"action", "url", "file_path", "asset"}}
WEEKLY_DATA_FIELDS = {"get": {"action", "url", "collection", "doc_id"},
                      "list": {"action", "url", "collection", "query"},
                      "batch": {"action", "url", "writes"}}
WEEKLY_WRITE_FIELDS = {"op", "collection", "doc_id", "data", "if_version"}
WEEKLY_SOURCE_FIELDS = {"kind", "url", "name", "format"}
WEEKLY_UPDATED_FIELDS = {"at", "by"}
WEEKLY_BY = "GSC WEEKLY routine"
BLOB_URL_RE = re.compile(r"/_blob/[0-9a-f]{32}")                      # used with fullmatch
ISO_TS_RE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2}(?:\.\d{1,6})?)?(?:Z|[+-]\d{2}:\d{2})")
WEEKLY_PAGE_HINT = ("only the WEEKLY run (a claude/gsc-weekly-* branch) uses the weekly page " + WEEKLY_PAGE_URL
                    + ": Artifact read; Artifact publish of one /tmp/" + WEEKLY_DIR + "/{id}.json dataset with "
                    "asset: true; ArtifactData get or list on 'datasets'; one ArtifactData batch of pinned "
                    "updates of datasets/{id} source and updated (routines/WEEKLY.md)")

# Strict run-branch name (spec §1). WEEKLY's branch is local only: it never reaches origin.
BRANCH_RE = re.compile(
    r"^claude/gsc-(analyse|review|seed|sweep|intake|weekly)-(?:(?P<key>[A-Za-z0-9._-]+)-)?"
    r"(?P<date>\d{4}-\d{2}-\d{2})-(?P<time>\d{4})$")
# MCP tools a routine may call, with the run-branch jobs allowed to call each. Every other MCP tool is
# refused: no routine playbook uses one, and they would bypass the gh api REST allowlist.
MCP_ALLOWED = {"mcp__claude-code-remote__list_triggers": ("weekly",)}
# Built-in tools no routine uses that would give the session a second checkout or a schedule of its own;
# settings.json routes them here and they are refused (MODEL v4.6.1 review).
BUILTIN_REFUSED = {
    "EnterWorktree": "worktrees are not used: a second checkout escapes the run-branch checks",
    "ExitWorktree": "worktrees are not used", "CronCreate": "a routine schedules nothing",
    "CronDelete": "a routine schedules nothing", "DesignSync": "a routine touches no design system",
}
# The job a routine session runs is the one its prompt names (CLAUDE.md mode table: the first prompt
# begins 'GSC ROUTINE: <JOB>'), read from the hook's transcript_path. Every job-gated check (git push,
# a GitHub write, a push notification, the artifact and MCP tools) needs the current run branch's job
# to equal it, so a session cannot act as another job by changing branch; unreadable = refused.
PROMPT_RE = re.compile(r"^\s*GSC ROUTINE:\s*(ANALYSE|REVIEW|SWEEP|INTAKE|QUEUE-SEED|WEEKLY)\b")
PROMPT_JOBS = {"ANALYSE": "analyse", "REVIEW": "review", "SWEEP": "sweep", "INTAKE": "intake",
               "QUEUE-SEED": "seed", "WEEKLY": "weekly"}
TRANSCRIPT_MAX_LINES = 5000
# The weekly page's dataset files (MODEL §7.4): each a JSON array of flat rows with these fields only
# (gsc_weekly.py DATASET_SCHEMA; its test checks the two agree). An upload is read before it leaves.
DATASET_FIELDS = {
    "summary": {"order", "kind", "text"},
    "meta": {"period_label", "since", "until", "report_date", "ref_sha", "ref_time", "register_from",
             "register_to", "model_live", "decide", "fix", "know", "generated_at", "tool_version"},
    "kpis": {"order", "metric", "value", "prior", "unit", "basis"},
    "attention": {"rank", "list", "severity", "item", "detail", "action", "since"},
    "shortlist": {"key", "company", "region", "px", "px_unit", "px_date", "px_age_d", "trigger", "trigger_basis",
                  "distance_pct", "needs_fall_pct", "mcap_fcf", "ev_oi", "status", "memo_date", "model_version",
                  "retest_owed", "all_cash_trigger", "pending", "reliable", "next_review"},
    "changes": {"key", "company", "job", "from_verdict", "to_verdict", "deciding", "ground_retired", "model_version",
                "merged_at", "merged_by", "pr"},
    "weekly": {"week", "week_start", "analyse", "review", "incomplete", "model_releases", "watch_end", "keys_end",
               "note"},
    "pipeline": {"job", "scheduled_base", "scheduled_sprint", "prs_opened", "merged_auto", "merged_jakub",
                 "closed_unmerged", "last_run_failed_usage_limit", "triggers"},
    "coverage": {"region", "keys", "watch", "avoid", "dnaf", "share_pct"},
    "backlog": {"item", "start", "end", "unit", "note"},
    "held": {"key", "company", "verdict", "zone", "last_zone_check", "memo_date", "open_since", "status"},
}
DATASET_MAX_BYTES = 1024 * 1024
PRIVATE_KEY_RE = re.compile(r"(?i)avg_?cost|cost|position|shares|qty|quantity|^core_")
# How far a batch's updated.at may sit from the hook's clock: a future stamp would make every later
# WEEKLY run read its week as published and stop silently.
STAMP_SKEW = datetime.timedelta(hours=6)
WEEKLY_READ_ONLY = ("WEEKLY never writes to the repo or to GitHub: its claude/gsc-weekly-… branch is a local "
                    "guard identity, never pushed, and it opens, edits, closes and comments on nothing "
                    "(routines/WEEKLY.md)")

# Command wrappers skipped before the real program. Value = options taking an argument.
WRAPPERS = {
    "sudo": {"-u", "-g", "-C", "-h", "-p"}, "env": {"-u", "-C"},
    "command": set(), "nice": {"-n"}, "time": {"-f", "-o"}, "nohup": set(),
    "stdbuf": {"-i", "-o", "-e"}, "exec": {"-a"}, "builtin": set(),
    "timeout": {"-s", "-k", "--signal", "--kill-after"},
}
KEYWORDS = {"if", "then", "else", "elif", "do", "while", "until", "!", "{", "}", "(", ")"}
# Redirection token: optional fd, operator, optional attached target.
REDIR_RE = re.compile(r"^(\d+|&)?(>>|>\||>&|<>|<<<|<<|<&|>|<)(.*)$", re.S)
ASSIGN_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)=(.*)$", re.S)
VAR_RE = re.compile(r"\$\{(\w+)\}|\$(\w+)")

# git -c keys a routine may set (everything else is blocked).
GIT_C_OK = re.compile(r"^(core\.quotepath|core\.autocrlf|core\.safecrlf|color\..*|user\.name|"
                      r"user\.email|advice\..*|log\..*|merge\.conflictstyle|pager\..*|"
                      r"init\.defaultbranch|safe\.directory|gc\.auto|commit\.gpgsign)$")
GIT_GLOBAL_OK = {"--no-pager", "-p", "-P", "--paginate", "--no-replace-objects",
                 "--literal-pathspecs", "--glob-pathspecs", "--noglob-pathspecs",
                 "--icase-pathspecs", "--no-optional-locks", "--no-advice"}
# git config keys a routine may never write.
GIT_CONFIG_LOCKED = re.compile(r"^(remote\.|push\.|branch\.|credential|url\.|http\.|include\.|"
                               r"includeif\.|alias\.|core\.(hookspath|sshcommand|askpass|"
                               r"fsmonitor|gitproxy|pager|editor))")
# git subcommands never needed by a routine.
GIT_DENY = {
    "rebase": "rebase rewrites history", "cherry-pick": "cherry-pick is not part of the run",
    "filter-branch": "history rewrite", "filter-repo": "history rewrite",
    "update-ref": "direct ref writes", "apply": "patches are not part of the run",
    "am": "patches are not part of the run", "stash": "stash is not needed",
    "pull": "use git fetch origin main + git merge --no-edit origin/main",
    "send-pack": "alternate push path", "http-push": "alternate push path",
    "submodule": "submodules are not used", "bisect": "bisect is not needed",
    "replace": "replace refs", "worktree": "worktrees are not used",
    "credential": "routines never handle credentials",
    "credential-store": "routines never handle credentials",
    "credential-cache": "routines never handle credentials",
    "difftool": "runs an external program", "mergetool": "runs an external program",
    "clone": "routines work in their own checkout", "init": "routines work in their own checkout",
    "daemon": "not needed",
    "instaweb": "not needed", "web--browse": "not needed",
}
# GIT_* variables that redirect git to another repo, config or transport.
GIT_ENV_LOCKED = re.compile(r"^GIT_(DIR|WORK_TREE|COMMON_DIR|SSH.*|ASKPASS|CONFIG.*|EXEC_PATH|"
                            r"NAMESPACE|PROXY_COMMAND|OBJECT_DIRECTORY|ALTERNATE_OBJECT_DIRECTORIES|"
                            r"EDITOR|SEQUENCE_EDITOR|EXTERNAL_DIFF)$")
# Variables naming a program that git (or another tool) would run.
PROGRAM_VARS = {"EDITOR", "VISUAL", "PAGER", "GIT_PAGER"}
# git options that make git run another program, for any subcommand.
GIT_EXEC_OPTS = ("--upload-pack", "--receive-pack", "--exec", "--open-files-in-pager",
                 "--extcmd", "--ext-diff", "--tool")
TOKEN_VARS = {"GH_TOKEN", "GITHUB_TOKEN", "GH_ENTERPRISE_TOKEN"}
TOKEN_LITERAL_RE = re.compile(r"(?<![A-Za-z0-9])(github_pat_|gh[pousr]_)[A-Za-z0-9_]{4,}")

INTERPRETERS = re.compile(r"^(python[0-9.]*|node|nodejs|perl|ruby|bash|sh|zsh|dash|ksh)$")
SHELLS = {"bash", "sh", "zsh", "dash", "ksh"}
# Python's short options that take an argument: the rest of their cluster ('-mpkg', '-Wignore',
# '-Bc code') or the next word. -c and -m end the interpreter's own options.
PY_ARG_OPTS = "cmWX"
# The register tool's attended-only subcommands (MODEL v4.5.0 §7.1b; round 2, R10; v4.6.0 §7.1, G5).
REGISTER_ATTENDED = (
    ("rebuild", "gsc_register.py rebuild is the one-time attended lean rebuild (MODEL v4.5.0 §7.1b); "
                "routines never run it"),
    ("retrigger", "gsc_register.py retrigger is the one-time attended trigger re-read (MODEL v4.5.0 "
                  "round 2, R10); routines never run it"),
    ("retire", "gsc_register.py retire sets or undoes the RETIRED register state, attended only (MODEL "
               "v4.6.0 §7.1, G5); a routine raises a delisting awaiting retirement as an open item"),
)
# The trusted tools under routines/tools/ (framework-locked, healed by the post hook) never spell these
# fragments in their source: this scan cannot tell a read from a write, so gsc_weekly.py builds its
# MODEL path from parts. The scan is a tripwire for ad-hoc /tmp scripts, not a boundary for those tools.
LOCKED_FRAG_RE = re.compile(r"model/|routines/|\.claude|\.github|CLAUDE\.md|CLAUDE\.local\.md|"
                            r"AGENTS\.md|settings\.local\.json|disableAllHooks|\.git[/\\]")
# Interpreter code that names GitHub beside a request body or a write method (routine scripts never
# talk to GitHub; README §5).
CODE_GITHUB_RE = re.compile(r"(?i)github\.com")
CODE_HTTP_WRITE_RE = re.compile(r"\bdata\s*=|\bmethod\s*=|['\"](?:POST|PUT|PATCH|DELETE)['\"]|"
                                r"\.(?:post|put|patch|delete)\s*\(")
WRITE_IND_RE = re.compile(
    r"""open\s*\([^)]*['"][rwxabt+]*[wax+][rwxabt+]*['"]|mode\s*=\s*['"][^'"]*[wax+]|write|"""
    r"""unlink|remove|rename|replace\(|shutil|os\.system|subprocess|rmtree|truncate|symlink|"""
    r"""chmod|FileUtils|appendFile|\brm(Sync)?\s*\(|['"]\s*\+?>|os\.popen|copyfile""", re.I)
# Unparseable push / gh api text (spec §5): `git … push` / `gh … api` as words, so that
# paths such as .git/hooks/pre-push or /git push/ inside a sed address don't count.
PUSH_TEXT_RE = re.compile(r"(?<![\w./-])git\b.*?(?<![\w./-])push(?![\w-])", re.S)
GHAPI_TEXT_RE = re.compile(r"(?<![\w./-])gh\b.*?(?<![\w./-])api(?![\w-])", re.S)
# In interpreter code (python/node/perl/ruby) any mention of both words counts:
# routine scripts never talk to GitHub (routines/README §5).
CODE_PUSH_RE = re.compile(r"\bgit\b.*\bpush\b", re.S)
CODE_GHAPI_RE = re.compile(r"\bgh\b.*\bapi\b", re.S)
# Read-only text tools may mention git push / gh api in their arguments (searching playbooks).
READ_ONLY_TOOLS = {"grep", "egrep", "fgrep", "rg", "cat", "head", "tail", "less", "more", "jq",
                   "wc", "sort", "uniq", "cut", "nl", "column", "ls", "stat", "file", "echo",
                   "printf", "diff", "cmp", "sed", "awk", "gawk"}

SUBST = "__GSC_SUBST__"          # placeholder for $( ), ` `, <( ), >( )
HEREDOC = "__GSC_HEREDOC_%d__"   # placeholder for a heredoc operator
HEREDOC_OP_RE = re.compile(r"<<(-?)[ \t]*(\\?)(['\"]?)(\w+)\3")
MAX_DEPTH = 6


def python_short_option(word):
    """(option, attached value) for the first argument-taking option of a python short-option
    cluster ('-m' -> ('m', ''), '-Bmpkg' -> ('m', 'pkg'), '-Wignore' -> ('W', 'ignore')), or
    (None, None) for a cluster of plain flags ('-B', '-OO')."""
    for k, ch in enumerate(word[1:], 1):
        if ch in PY_ARG_OPTS:
            return ch, word[k + 1:]
    return None, None


def register_tool_word(word):
    """True when a word names the register tool: its script (any path to gsc_register.py) or
    its module (routines.tools.gsc_register, or gsc_register run from routines/tools)."""
    w = word.replace("\\", "/")
    if os.path.basename(w).lower() == "gsc_register.py":
        return True
    return "/" not in w and w.rsplit(".", 1)[-1].lower() == "gsc_register"


def check_register_tool(rest):
    """The words after the register tool: refuse its attended-only subcommands."""
    for sub, reason in REGISTER_ATTENDED:
        if sub in rest:
            block(reason)


def prompt_job_of(path):
    """The job token ('analyse', …, 'seed', 'weekly') that the session's first prompt names
    ('GSC ROUTINE: <JOB> — …'), read from the hook's transcript (JSON lines: the first entry of type
    user that is neither meta, a side chain nor a tool result); '' when that prompt names no routine
    job; None when the transcript cannot be read or holds no such prompt within TRANSCRIPT_MAX_LINES."""
    if not isinstance(path, str) or not path.strip():
        return None
    try:
        with open(os.path.expanduser(path), encoding="utf-8", errors="replace") as fh:
            for n, line in enumerate(fh):
                if n >= TRANSCRIPT_MAX_LINES:
                    return None
                try:
                    entry = json.loads(line)
                except ValueError:
                    continue
                if not isinstance(entry, dict) or entry.get("type") != "user" or entry.get("isMeta") \
                        or entry.get("isSidechain"):
                    continue
                msg = entry.get("message")
                content = msg.get("content") if isinstance(msg, dict) else None
                if isinstance(content, list):
                    if any(isinstance(b, dict) and b.get("type") == "tool_result" for b in content):
                        continue
                    content = "".join(b.get("text") or "" for b in content
                                      if isinstance(b, dict) and b.get("type") == "text")
                if not isinstance(content, str):
                    continue
                m = PROMPT_RE.match(content)
                return PROMPT_JOBS[m.group(1)] if m else ""
    except OSError:
        return None
    return None


def parse_iso(text):
    """An aware datetime from ISO text with an offset or 'Z' (None when it is not one)."""
    if not isinstance(text, str) or not ISO_TS_RE.fullmatch(text):
        return None
    try:
        return datetime.datetime.fromisoformat(text[:-1] + "+00:00" if text.endswith("Z") else text)
    except ValueError:
        return None


def literal_path(path, hint):
    """An artifact file_path is taken literally by the tool: refuse one the shell would expand ($VAR, ~),
    since the guard would check a different file from the one sent."""
    if "$" in path or path.lstrip().startswith("~"):
        block(f"Artifact file_path '{short(path, 60)}' with '$' or '~': write the path out in full; " + hint)


def check_dataset_file(full, doc):
    """Read a weekly dataset file before it leaves (MODEL §7.4 privacy): at most DATASET_MAX_BYTES, a JSON
    array of flat objects whose keys are the dataset's own fields (DATASET_FIELDS) and never a private
    field (average cost, position size, core numbers)."""
    try:
        if os.path.getsize(full) > DATASET_MAX_BYTES:
            block(f"dataset file {doc}.json is larger than {DATASET_MAX_BYTES // 1024} KB; " + WEEKLY_PAGE_HINT)
        with open(full, encoding="utf-8") as fh:
            rows = json.load(fh)
    except (OSError, ValueError) as exc:
        block(f"dataset file {doc}.json cannot be read as JSON ({type(exc).__name__}); " + WEEKLY_PAGE_HINT)
    if not isinstance(rows, list):
        block(f"dataset file {doc}.json is not a JSON array of rows; " + WEEKLY_PAGE_HINT)
    allowed = DATASET_FIELDS[doc]
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            block(f"dataset file {doc}.json row {i + 1} is not an object; " + WEEKLY_PAGE_HINT)
        private = sorted(k for k in row if PRIVATE_KEY_RE.search(str(k)))
        if private:
            block(f"dataset file {doc}.json carries the private field(s) {private[:3]} (never average cost, "
                  "position size or core numbers, MODEL §7.4); " + WEEKLY_PAGE_HINT)
        extra = sorted(set(row) - allowed)
        if extra:
            block(f"dataset file {doc}.json row {i + 1} has field(s) {extra[:3]} that {doc} does not carry; "
                  + WEEKLY_PAGE_HINT)
        if any(isinstance(v, (dict, list)) for v in row.values()):
            block(f"dataset file {doc}.json row {i + 1} is not flat; " + WEEKLY_PAGE_HINT)


def push_text_problem(msg):
    """Why a push text breaks the one-line rule (a control, format or separator character), or None."""
    for ch in msg:
        if unicodedata.category(ch) in PUSH_BAD_CATEGORIES:
            return "routine push contains the character U+%04X (one plain line only)" % ord(ch)
    return None


class Blocked(Exception):
    """Raised to refuse the tool call; the message is the reason."""


def block(reason):
    raise Blocked(reason)


def emit(reason):
    """Write the one stderr line in the spec's format."""
    reason = " ".join(str(reason).split())[:400]
    msg = f"GSC guard (routine session): {reason} — see MODEL §8.7 / routines/README.md §3.\n"
    sys.stderr.buffer.write(msg.encode("utf-8", "replace"))
    sys.stderr.buffer.flush()


def short(text, n=80):
    text = " ".join(str(text).split())
    return text if len(text) <= n else text[: n - 1] + "…"


# ---------------------------------------------------------------- paths

def norm(path):
    return os.path.normcase(os.path.realpath(path))


def rel_to(full, root):
    """Path of `full` relative to `root` with '/' separators, or None if outside."""
    try:
        rel = os.path.relpath(full, root)
    except ValueError:            # other drive (Windows)
        return None
    rel = rel.replace(os.sep, "/")
    if rel == ".." or rel.startswith("../"):
        return None
    return rel


def expand_braces(word):
    """a{b,c}d -> [abd, acd] (simple, non-nested)."""
    m = re.match(r"^(.*?)\{([^{}]*,[^{}]*)\}(.*)$", word)
    if not m:
        return [word]
    out = []
    for part in m.group(2).split(","):
        out.extend(expand_braces(m.group(1) + part + m.group(3)))
    return out


# ---------------------------------------------------------------- command scanner

def ansi_c_end(s, i):
    """Index just past the closing quote of a $'…' string starting at s[i] ('$')."""
    j, n = i + 2, len(s)
    while j < n and s[j] != "'":
        j += 2 if s[j] == "\\" else 1
    return min(j + 1, n)


def match_paren(s, k):
    """Index of the ')' closing the '(' at s[k], or len(s).

    Quote aware, including $'…', and skips heredoc bodies (an apostrophe in a
    heredoc commit message must not open a quote)."""
    depth, i, sq, dq, pending, n = 0, k, False, False, [], len(s)
    while i < n:
        c = s[i]
        if c == "\\" and not sq:
            i += 2
            continue
        if not sq and not dq:
            if c == "$" and s.startswith("$'", i):
                i = ansi_c_end(s, i)
                continue
            if s.startswith("<<", i) and not s.startswith("<<<", i):
                m = HEREDOC_OP_RE.match(s, i)
                if m:
                    pending.append((m.group(4), m.group(1) == "-"))
                    i = m.end()
                    continue
            if c == "\n" and pending:
                i += 1
                for delim, dash in pending:     # skip each body up to its terminator line
                    while i < n:
                        j = s.find("\n", i)
                        j = n if j < 0 else j
                        line = s[i:j]
                        i = j + 1
                        if (line.lstrip("\t") if dash else line).rstrip("\r") == delim:
                            break
                pending.clear()
                continue
        if c == "'" and not dq:
            sq = not sq
        elif c == '"' and not sq:
            dq = not dq
        elif not sq and not dq:
            if c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0:
                    return i
        i += 1
    return len(s)


def body_substitutions(body):
    """Commands bash runs inside an unquoted heredoc body: $( ) and ` `."""
    subs, i = [], 0
    while i < len(body):
        if body[i] == "\\":
            i += 2
            continue
        if body.startswith("$(", i):
            j = match_paren(body, i + 1)
            subs.append(body[i + 2:j])
            i = j + 1
            continue
        if body[i] == "`":
            j = body.find("`", i + 1)
            j = len(body) if j < 0 else j
            subs.append(body[i + 1:j])
            i = j + 1
            continue
        i += 1
    return subs


def scan(cmd):
    """Split a shell command into simple-command segments, quote aware.

    Returns (segments, heredocs, subs):
      segments  raw text of each simple command (operators removed);
      heredocs  list of (quoted, body); the operator becomes <<__GSC_HEREDOC_n__;
      subs      inner text of $( ), ` `, <( ), >( ) (each replaced by __GSC_SUBST__).
    Separators: ; & && || | |& ( ) and newline. Comments are dropped.
    """
    segs, heredocs, subs, pending, cur = [], [], [], [], []
    i, n, dq = 0, len(cmd), False

    def flush():
        s = "".join(cur).strip()
        if s:
            segs.append(s)
        cur.clear()

    while i < n:
        c = cmd[i]
        if c == "\\":
            if i + 1 < n and cmd[i + 1] == "\n":
                i += 2                          # line continuation
                continue
            cur.append(cmd[i:i + 2])
            i += 2
            continue
        if c == "$" and not dq and cmd.startswith("$'", i):     # ANSI-C quoting: \' does not end it
            j = ansi_c_end(cmd, i)
            cur.append(cmd[i:j])
            i = j
            continue
        if c == "'" and not dq:
            j = cmd.find("'", i + 1)
            j = n - 1 if j < 0 else j
            cur.append(cmd[i:j + 1])
            i = j + 1
            continue
        if c == '"':
            dq = not dq
            cur.append(c)
            i += 1
            continue
        if cmd.startswith("$(", i) or (not dq and cmd.startswith(("<(", ">("), i)):
            j = match_paren(cmd, i + 1)
            subs.append(cmd[i + 2:j])
            cur.append(cmd[i] + SUBST if cmd[i] in "<>" else SUBST)
            i = j + 1
            continue
        if c == "`":
            j = cmd.find("`", i + 1)
            j = n if j < 0 else j
            subs.append(cmd[i + 1:j])
            cur.append(SUBST)
            i = j + 1
            continue
        if c == "$" and i + 1 < n and cmd[i + 1] == "{":
            j = cmd.find("}", i)
            j = n - 1 if j < 0 else j
            cur.append(cmd[i:j + 1])
            i = j + 1
            continue
        if dq:
            cur.append(c)
            i += 1
            continue
        # ---- unquoted context
        if c == "#" and (i == 0 or cmd[i - 1] in " \t\n;&|()"):
            j = cmd.find("\n", i)
            i = n if j < 0 else j               # comment: skip to end of line
            continue
        if c == "\n":
            flush()
            i += 1
            for idx, delim, dash in pending:    # read heredoc bodies
                body = []
                while i < n:
                    j = cmd.find("\n", i)
                    j = n if j < 0 else j
                    line = cmd[i:j]
                    i = j + 1
                    if (line.lstrip("\t") if dash else line).rstrip("\r") == delim:
                        break
                    body.append(line)
                heredocs[idx] = (heredocs[idx][0], "\n".join(body))
            pending.clear()
            continue
        if cmd.startswith("<<", i) and not cmd.startswith("<<<", i):
            m = HEREDOC_OP_RE.match(cmd, i)
            if m:
                quoted = bool(m.group(2) or m.group(3))
                heredocs.append((quoted, ""))
                pending.append((len(heredocs) - 1, m.group(4), m.group(1) == "-"))
                cur.append(" <<" + HEREDOC % (len(heredocs) - 1) + " ")
                i = m.end()
                continue
        if c == "&" and (cmd.startswith("&>", i) or (cur and cur[-1] in "<>")):
            cur.append(c)                       # &> file, >&2, <&0 are redirections
            i += 1
            continue
        if c == "|" and cur and cur[-1] == ">":
            cur.append(c)                       # >| file
            i += 1
            continue
        if c in ";&|()":
            flush()
            i += 1
            continue
        if c in "<>" and cur:
            # `echo x>file`: bash splits the word at the operator, so must we. A bare
            # fd number (2>file) and multi-char operators (>>, 2>&1, &>) stay joined.
            prev = "".join(cur)
            if prev and not prev[-1].isspace() and prev[-1] not in "<>&|" and \
                    not re.fullmatch(r"\d+", re.split(r"\s", prev)[-1]):
                cur.append(" ")
        cur.append(c)
        i += 1
    flush()
    return segs, heredocs, subs


def tokens(seg):
    try:
        return shlex.split(seg)
    except ValueError:
        return seg.split()


# Programs that write the files named in their arguments.
WRITE_PROGS = {"tee", "cp", "mv", "rm", "rmdir", "touch", "mkdir", "truncate", "chmod", "chown",
               "chgrp", "ln", "install", "unlink", "dd", "sed", "perl", "rsync", "shred", "awk",
               "gawk", "tar", "unzip"}
# Options that take a value, per program (the value is not a file to write).
OPT_VALUE = {"touch": {"-d", "-t", "-r"}, "truncate": {"-s", "-r"}, "mkdir": {"-m"},
             "install": {"-m", "-o", "-g", "-S"}, "cp": {"-S"}, "mv": {"-S"}, "ln": {"-S"},
             "sed": {"-e", "-f", "-l"}, "perl": {"-e", "-E", "-I", "-M", "-m"},
             "awk": {"-f", "-v", "-F"}, "gawk": {"-f", "-v", "-F"}, "rsync": {"-e"},
             "tar": {"-f", "-C", "--directory"}, "unzip": {"-d", "-x"}}


# ---------------------------------------------------------------- the guard

class Guard:
    def __init__(self, event):
        self.event = event if isinstance(event, dict) else {}
        cwd = self.event.get("cwd") if isinstance(self.event.get("cwd"), str) else ""
        self.root = norm(os.environ.get("CLAUDE_PROJECT_DIR") or cwd or os.getcwd())
        self.cwd = norm(cwd) if cwd else self.root
        self.vars = {}          # NAME -> value (None = unknown) for this command
        self._branch = None
        self._prompt_job = False  # not read yet; prompt_job_of gives None, '' or a job word

    # ---- entry point

    def run(self):
        tool = self.event.get("tool_name", "")
        ti = self.event.get("tool_input") or {}
        if not isinstance(ti, dict):
            block("tool input is not an object")
        if tool == "PushNotification":
            self.check_push(ti)
            return
        if tool == "Artifact":
            self.check_artifact(ti)
            return
        if tool == "ArtifactData":
            self.check_artifact_data(ti)
            return
        if tool.startswith("mcp__"):
            jobs = MCP_ALLOWED.get(tool)
            if not jobs:
                block(f"{tool} is not allowed in routines: MCP tools bypass the gh api REST allowlist "
                      f"(only {', '.join(sorted(MCP_ALLOWED))} passes, for WEEKLY)")
            if self.pinned_job(tool) not in jobs:
                block(f"{tool} outside {' or '.join(j.upper() for j in jobs)} (current branch "
                      f"'{self.current_branch() or 'detached HEAD'}')")
            return
        if tool in BUILTIN_REFUSED:
            block(f"{tool} is not allowed in routines: {BUILTIN_REFUSED[tool]}")
        if "artifact" in tool.lower():
            block(f"{tool} is not allowed in routines: only Artifact (the register and weekly pages) and "
                  "ArtifactData (the weekly page's datasets) pass")
        if tool in ("Edit", "Write", "NotebookEdit", "MultiEdit"):
            target = ti.get("file_path") or ti.get("notebook_path") or ""
            if not isinstance(target, str):
                block("file path is not a string")
            hit = self.locked(target, self.cwd)
            if hit:
                block(f"'{hit}' is framework-locked")
            arch = self.archive_rels(target, self.cwd)
            if arch:
                block(f"{tool} of '{arch[0]}': {APPEND_ONLY_HINT}")
            self.need_not_register([target], self.cwd, tool)
            if target.strip() and rel_to(self.resolve(target, self.cwd), self.root) is not None \
                    and self.weekly_session():
                block(f"{tool} of '{short(target, 60)}' inside the repo: " + WEEKLY_READ_ONLY)
            memo = self.memo_rel(target, self.cwd)
            if memo:
                found = self.on_main(memo)
                if found is None:
                    block(f"{tool} of '{memo}': cannot list memos/ on origin/main to rule out an "
                          "in-place memo edit (fail closed; run git fetch origin main)")
                if found:
                    block(f"{tool} of '{memo}': {MEMO_HINT}")
            return
        if tool in ("Bash", "Monitor"):
            cmd = ti.get("command")
            if not isinstance(cmd, str):
                # Monitor's field name is not documented: check every string field.
                cmd = "\n".join(v for v in ti.values() if isinstance(v, str))
            if cmd.strip() == CANARY:
                block("GSC guard canary — the guard is live; this refusal is the expected preflight self-test")
            if TOKEN_LITERAL_RE.search(cmd):
                block("a GitHub token literal appeared in the command")
            self.check_command(cmd, 0, self.cwd)

    # ---- phone pushes

    def check_push(self, ti):
        """A routine push must follow routines/README.md §5: class BUY from that ANALYSE or
        REVIEW run, or class WEEKLY from the WEEKLY run (both checked against the current run
        branch and the session's prompt), in its exact form, one plain line, at most PUSH_MAX
        characters, no '#', no url but the weekly page's, once per class per run."""
        msg = ti.get("message")
        if not isinstance(msg, str) or not msg.strip():
            block("routine push without a message; " + PUSH_HINT)
        msg = msg.strip()
        retired = PUSH_RETIRED_RE.match(msg)
        if retired:
            block(f"routine push not allowed: the {retired.group(1)} push is retired (MODEL v4.6.1 §8.7 item 11); "
                  "its content reaches Jakub in the weekly report")
        m = PUSH_RE.match(msg)
        if not m:
            block("routine push not allowed: " + PUSH_HINT)
        cls = m.group(1)
        if cls == "BUY" and m.group(2) not in ("ANALYSE", "REVIEW"):
            block("routine push not allowed: a BUY push comes only from an ANALYSE or REVIEW memo "
                  "(routines/README.md §5)")
        if "\n" in msg or "\r" in msg:
            block("routine push must be one line")
        bad = push_text_problem(msg)
        if bad:
            block(bad)
        if len(msg) > PUSH_MAX:
            block(f"routine push longer than {PUSH_MAX} characters")
        if "#" in msg:
            block("routine push contains '#': write 'PR n' (a '#n' may wake the session watching that PR)")
        exact = (PUSH_BUY_RE if cls == "BUY" else PUSH_WEEKLY_RE).match(msg)
        if not exact:
            block("routine push not in its exact form: " + PUSH_HINT)
        rest = msg.replace(exact.group("url"), "") if cls == "WEEKLY" and exact.group("url") else msg
        if URL_TEXT_RE.search(rest):
            block("routine push carries a link: the only link a push may carry is the weekly page's, at the end "
                  "of the WEEKLY report push")
        cur = self.current_branch()
        b = BRANCH_RE.match(cur)
        job = self.pinned_job(f"a {cls} push")
        if job not in PUSH_FROM[cls] or (cls == "BUY" and m.group(2) != job.upper()):
            block(f"routine push not allowed: a {cls} push comes only from "
                  + (f"the {m.group(2)} run itself" if cls == "BUY" else "the WEEKLY run")
                  + f" (current branch '{cur or 'detached HEAD'}'; routines/README.md §5)")
        if cls == "BUY" and (exact.group("key") != b.group("key") or exact.group("date") != b.group("date")):
            block(f"routine push not allowed: a BUY push names this run's own key and date "
                  f"({b.group('key') or 'no key'} {b.group('date')}, branch '{cur}')")
        # One push per class per run: an O_EXCL marker in the git dir, which no routine command may write
        # or remove (.git is locked), so deleting a temp file cannot buy a second push.
        session = re.sub(r"[^A-Za-z0-9_-]", "", str(self.event.get("session_id") or ""))[:80] or "nosession"
        folder = os.path.join(self.git_dir(), "gsc-guard")
        os.makedirs(folder, exist_ok=True)
        try:
            fd = os.open(os.path.join(folder, "push_%s_%s" % (session, cls)), os.O_CREAT | os.O_EXCL | os.O_WRONLY,
                         0o644)
        except FileExistsError:
            block(f"one push per class per run: a {cls} push was already sent (routines/README.md §5)")
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(msg[:PUSH_MAX] + "\n")

    # ---- the session's job: the prompt pins it, the run branch must match

    def prompt_job(self):
        """The job the session's routine prompt names (prompt_job_of on transcript_path), read once."""
        if self._prompt_job is False:
            self._prompt_job = prompt_job_of(self.event.get("transcript_path"))
        return self._prompt_job

    def pinned_job(self, what):
        """The current run branch's job, checked against the job the session's prompt names: a session
        acts only as the job it was started for, whatever branch it moves to. A transcript that cannot
        be read falls back to the branch alone (the pre-v4.6.1 rule), so an unexpected transcript
        format never stops every routine; a readable first prompt that names no routine job, or
        another job, is refused."""
        want, job = self.prompt_job(), self.run_job()
        if want is None:
            return job
        if not want:
            block(f"{what}: the session's first prompt names no routine job ('GSC ROUTINE: <JOB> — …')")
        if job != want:
            block(f"{what}: this session runs {want.upper()} (its prompt), but the current branch "
                  f"'{self.current_branch() or 'detached HEAD'}' is not a claude/gsc-{want}-… run branch; a session "
                  "acts only as its own job")
        return job

    def weekly_session(self):
        """True when the session is WEEKLY by its branch or by its prompt (the read-only job)."""
        return self.run_job() == "weekly" or self.prompt_job() == "weekly"

    def git_dir(self):
        """The repo root's absolute git dir (one subprocess); refused when git cannot name it."""
        try:
            r = subprocess.run(["git", "-C", self.root, "rev-parse", "--absolute-git-dir"], capture_output=True,
                               text=True, timeout=10)
        except (OSError, subprocess.SubprocessError):
            r = None
        if r is None or r.returncode != 0 or not r.stdout.strip():
            block("cannot locate the repo's git dir (fail closed)")
        return norm(r.stdout.strip())

    # ---- the claude.ai artifact tools (MODEL §7.4): the register page and the weekly page

    def check_artifact(self, ti):
        """Artifact passes only on the two pages a routine maintains: the weekly page
        (WEEKLY_PAGE_URL, the WEEKLY run) or else the register page (INTAKE)."""
        if ti.get("url") == WEEKLY_PAGE_URL:
            self.check_weekly_artifact(ti)
        else:
            self.check_register_artifact(ti)

    def run_job(self):
        """The current run branch's job token ('intake', 'weekly', …), or '' off a run branch."""
        m = BRANCH_RE.match(self.current_branch())
        return m.group(1) if m else ""

    def check_register_artifact(self, ti):
        """INTAKE's register page step (routines/INTAKE.md step 9): read or publish, in place,
        on REGISTER_PAGE_URL; a publish sends only the rendered REGISTER_PAGE_FILE from
        outside the repo. Every other action and every other field is refused."""
        action = ti.get("action", "publish")
        if not isinstance(action, str) or action not in REGISTER_PAGE_FIELDS:
            block(f"Artifact action '{short(action, 30)}' is not allowed in routines (never a new artifact, "
                  "delete, list, open, pin or quickstart); " + REGISTER_PAGE_HINT)
        extra = sorted(set(ti) - REGISTER_PAGE_FIELDS[action])
        if extra:
            block(f"Artifact {action} with {extra} is not allowed (no capabilities, assets, files, type, "
                  "force, pin or sharing); " + REGISTER_PAGE_HINT)
        if ti.get("url") != REGISTER_PAGE_URL:
            block(f"Artifact {action} of '{short(ti.get('url') or 'no url (a new artifact)', 60)}' is not "
                  "allowed: routines update only the register page and the weekly page, in place; "
                  + REGISTER_PAGE_HINT)
        if self.pinned_job(f"Artifact {action} of the register page") != "intake":
            block(f"Artifact {action} outside INTAKE (current branch '{self.current_branch() or 'detached HEAD'}'): "
                  + REGISTER_PAGE_HINT)
        if action == "read":
            return
        path = ti.get("file_path")
        if not isinstance(path, str) or not path.strip():
            block("Artifact publish without a file_path; " + REGISTER_PAGE_HINT)
        literal_path(path, REGISTER_PAGE_HINT)
        if os.path.basename(path.replace("\\", "/")) != REGISTER_PAGE_FILE:
            block(f"Artifact publish of '{short(path, 60)}': only the rendered {REGISTER_PAGE_FILE} is "
                  "published; " + REGISTER_PAGE_HINT)
        full = self.resolve(path, self.cwd)
        if rel_to(full, self.root) is not None:
            block(f"Artifact publish of '{short(path, 60)}' inside the repo: the page is rendered outside it "
                  "and never committed; " + REGISTER_PAGE_HINT)
        if os.path.isdir(full):
            block(f"Artifact publish of the folder '{short(path, 60)}'; " + REGISTER_PAGE_HINT)

    # ---- the weekly report page (MODEL v4.6.1 §7.4, routines/WEEKLY.md)

    def need_weekly_run(self, what):
        if self.pinned_job(what) != "weekly":
            block(f"{what} outside WEEKLY (current branch '{self.current_branch() or 'detached HEAD'}'): "
                  + WEEKLY_PAGE_HINT)

    def check_weekly_artifact(self, ti):
        """WEEKLY's Artifact calls on WEEKLY_PAGE_URL: read, or an upload of one dataset file
        to the page's asset store (publish with exactly action, url, file_path and asset: true).
        A publish without asset: true would replace the page itself and is refused."""
        action = ti.get("action", "publish")
        if not isinstance(action, str) or action not in WEEKLY_PAGE_FIELDS:
            block(f"Artifact action '{short(action, 30)}' on the weekly page is not allowed (never delete, list, "
                  "open, pin or quickstart); " + WEEKLY_PAGE_HINT)
        extra = sorted(set(ti) - WEEKLY_PAGE_FIELDS[action])
        if extra:
            block(f"Artifact {action} of the weekly page with {extra} is not allowed (no label, files, "
                  "file_paths, asset copies, capabilities, type, force or pin); " + WEEKLY_PAGE_HINT)
        self.need_weekly_run(f"Artifact {action} of the weekly page")
        if action == "read":
            return
        if ti.get("asset") is not True:
            block("Artifact publish to the weekly page without asset: true would replace the page itself; "
                  "WEEKLY only uploads dataset files to its asset store; " + WEEKLY_PAGE_HINT)
        path = ti.get("file_path")
        if not isinstance(path, str) or not path.strip():
            block("Artifact upload without a file_path; " + WEEKLY_PAGE_HINT)
        literal_path(path, WEEKLY_PAGE_HINT)
        name = os.path.basename(path.replace("\\", "/"))
        full = self.resolve(path, self.cwd)
        if not (name.endswith(".json") and name[:-5] in DATASET_IDS and os.path.basename(full) == name
                and os.path.basename(os.path.dirname(full)) == WEEKLY_DIR):
            block(f"Artifact upload of '{short(path, 60)}': only a rendered dataset file "
                  f"{WEEKLY_DIR}/{{id}}.json is uploaded ({', '.join(DATASET_IDS)}); " + WEEKLY_PAGE_HINT)
        if rel_to(full, self.root) is not None:
            block(f"Artifact upload of '{short(path, 60)}' inside the repo: the datasets are rendered outside "
                  "it and never committed; " + WEEKLY_PAGE_HINT)
        if os.path.isdir(full):
            block(f"Artifact upload of the folder '{short(path, 60)}'; " + WEEKLY_PAGE_HINT)
        check_dataset_file(full, name[:-5])

    def check_artifact_data(self, ti):
        """ArtifactData passes only for WEEKLY on WEEKLY_PAGE_URL: get of one datasets/{id}
        document, list of the datasets collection, and one batch of pinned updates of
        datasets/{id} source and updated. Every other action, field, collection and url is
        refused (never set, delete, str_replace, query, profiles, as_level or out_dir)."""
        action = ti.get("action")
        if not isinstance(action, str) or action not in WEEKLY_DATA_FIELDS:
            block(f"ArtifactData action '{short(action, 30)}' is not allowed in routines (only get, list and "
                  "batch; never set, update outside a batch, delete, str_replace, query or profiles); "
                  + WEEKLY_PAGE_HINT)
        extra = sorted(set(ti) - WEEKLY_DATA_FIELDS[action])
        if extra:
            block(f"ArtifactData {action} with {extra} is not allowed (no as_level, out_dir, file_path, or "
                  "collection/doc_id beside a batch); " + WEEKLY_PAGE_HINT)
        if ti.get("url") != WEEKLY_PAGE_URL:
            block(f"ArtifactData {action} on '{short(ti.get('url') or 'no url', 60)}' is not allowed: routines "
                  "touch only the weekly page's datasets; " + WEEKLY_PAGE_HINT)
        self.need_weekly_run(f"ArtifactData {action}")
        if action == "batch":
            self.check_dataset_writes(ti.get("writes"))
            return
        if ti.get("collection") != "datasets":
            block(f"ArtifactData {action} of collection '{short(ti.get('collection'), 40)}': only 'datasets' "
                  "(never the page's files/ or dash/ documents); " + WEEKLY_PAGE_HINT)
        if action == "get":
            if ti.get("doc_id") not in DATASET_IDS:
                block(f"ArtifactData get of datasets/{short(ti.get('doc_id'), 40)}: only the dataset documents "
                      f"({', '.join(DATASET_IDS)}); " + WEEKLY_PAGE_HINT)
            return
        query = ti.get("query")
        if query is not None and (not isinstance(query, dict) or set(query) - {"limit", "cursor"}):
            block("ArtifactData list with a query other than limit and cursor; " + WEEKLY_PAGE_HINT)

    def check_dataset_writes(self, writes, now=None):
        """One batch: exactly one update of each datasets/{id} document (DATASET_IDS), meta last, each
        pinned with if_version and changing exactly source (a /_blob/ asset url, name {id}.json) and
        updated (one at for the whole batch, within STAMP_SKEW of the hook's clock, by WEEKLY_BY)."""
        n = len(DATASET_IDS)
        if not isinstance(writes, list) or len(writes) != n:
            block(f"ArtifactData batch needs exactly {n} writes, one per dataset, meta last; " + WEEKLY_PAGE_HINT)
        seen, stamps = set(), set()
        for k, w in enumerate(writes, 1):
            if not isinstance(w, dict):
                block(f"ArtifactData batch write {k} is not an object; " + WEEKLY_PAGE_HINT)
            extra = sorted(set(w) - WEEKLY_WRITE_FIELDS)
            if extra:
                block(f"ArtifactData batch write {k} with {extra} is not allowed (inline data only, no "
                      "file_path); " + WEEKLY_PAGE_HINT)
            if w.get("op") != "update":
                block(f"ArtifactData batch write {k} with op '{short(w.get('op'), 20)}': only update (never set "
                      "or delete); " + WEEKLY_PAGE_HINT)
            if w.get("collection") != "datasets":
                block(f"ArtifactData batch write {k} to collection '{short(w.get('collection'), 40)}': only "
                      "'datasets' (never the page's files/ or dash/ documents); " + WEEKLY_PAGE_HINT)
            doc = w.get("doc_id")
            if doc not in DATASET_IDS:
                block(f"ArtifactData batch write {k} to datasets/{short(doc, 40)}: only the dataset documents "
                      f"({', '.join(DATASET_IDS)}); " + WEEKLY_PAGE_HINT)
            if doc in seen:
                block(f"ArtifactData batch writes datasets/{doc} twice; " + WEEKLY_PAGE_HINT)
            seen.add(doc)
            if (doc == "meta") != (k == n):
                block("ArtifactData batch: datasets/meta is written last (the published mark follows the data); "
                      + WEEKLY_PAGE_HINT)
            ver = w.get("if_version")
            if not isinstance(ver, int) or isinstance(ver, bool) or ver < 1:
                block(f"ArtifactData batch write of datasets/{doc} without an if_version: every write is pinned "
                      "to the version WEEKLY read; " + WEEKLY_PAGE_HINT)
            data = w.get("data")
            if not isinstance(data, dict) or set(data) != {"source", "updated"}:
                block(f"ArtifactData batch write of datasets/{doc} changes exactly source and updated (never "
                      "title, description or fixed, never one without the other); " + WEEKLY_PAGE_HINT)
            # A {"__delete__": true} anywhere fails these exact shapes, so no field is ever removed.
            src = data.get("source")
            if not (isinstance(src, dict) and set(src) == WEEKLY_SOURCE_FIELDS and src.get("kind") == "file"
                    and isinstance(src.get("url"), str) and BLOB_URL_RE.fullmatch(src["url"])
                    and src.get("name") == doc + ".json" and src.get("format") == "json"):
                block(f"datasets/{doc} source must be exactly {{kind: 'file', url: '/_blob/<32 hex>', name: "
                      f"'{doc}.json', format: 'json'}}, an asset url of the page; " + WEEKLY_PAGE_HINT)
            upd = data.get("updated")
            if not (isinstance(upd, dict) and set(upd) == WEEKLY_UPDATED_FIELDS and upd.get("by") == WEEKLY_BY
                    and isinstance(upd.get("at"), str) and ISO_TS_RE.fullmatch(upd["at"])):
                block(f"datasets/{doc} updated must be exactly {{at: <ISO time with offset>, by: '{WEEKLY_BY}'}}; "
                      + WEEKLY_PAGE_HINT)
            stamps.add(upd["at"])
        if len(stamps) != 1:
            block("ArtifactData batch: every dataset carries the same updated.at (the run start); " + WEEKLY_PAGE_HINT)
        at = parse_iso(stamps.pop())
        now = now or datetime.datetime.now(datetime.timezone.utc)
        if at is None or abs(at - now) > STAMP_SKEW:
            block(f"ArtifactData batch: updated.at is more than {int(STAMP_SKEW.total_seconds() // 3600)} h from the "
                  "clock; a future stamp would make every later WEEKLY run read its week as published; "
                  + WEEKLY_PAGE_HINT)

    # ---- paths

    def resolve(self, path, base):
        p = os.path.expandvars(os.path.expanduser(path))
        if not os.path.isabs(p):
            p = os.path.join(base, p)
        return norm(p)

    def locked(self, path, base, whole=False):
        """Locked path hit by writing `path`, or None.

        whole=True also counts the repo root and its parents (recursive ops)."""
        if not path or SUBST in path or "__GSC_HEREDOC_" in path:
            return None
        for word in expand_braces(path):
            full = self.resolve(word, base)
            cands = [full]
            if any(ch in word for ch in "*?["):
                cands += [norm(g) for g in glob.glob(full)]
            for c in cands:
                hit = self.locked_full(c, whole)
                if hit:
                    return hit
        return None

    def locked_full(self, full, whole):
        rel = rel_to(full, self.root)
        if rel is None:
            if whole and (self.root + os.sep).startswith(full.rstrip(os.sep) + os.sep):
                return full
            fwd = full.replace(os.sep, "/")
            # Claude Code settings outside the repo: user, managed (policy) and ~/.claude.json.
            # The session transcripts too: the guard reads the routine prompt there (prompt_job_of).
            if re.search(r"/\.claude/settings[^/]*\.json$|/\.claude\.json$|/\.claude/projects(/|$)|"
                         r"/etc/claude-code/|/Library/Application Support/ClaudeCode/", fwd, re.I):
                return full
            return None
        if rel == ".":
            return "the repo root" if whole else None
        parts = rel.split("/")
        # .git/ too: a file written there (hooks, config, HEAD) makes git run arbitrary code or moves the
        # branch the guard reads; and any .git below the root, which would be a second repository.
        if parts[0].lower() in {d.lower() for d in LOCKED_DIRS} or any(p.lower() == ".git" for p in parts):
            return rel
        if parts[-1].lower() in {n.lower() for n in LOCKED_NAMES}:
            return rel
        return None

    def need_unlocked(self, paths, base, what, whole=False):
        for p in paths:
            hit = self.locked(p, base, whole)
            if hit:
                block(f"{what} on '{hit}' (framework-locked)")

    # ---- append-only archive/ (MODEL v4.5.0 §7.5)

    def archive_rels(self, path, base):
        """Repo-relative paths under archive/ that `path` names (globs expanded), or []."""
        if not path or SUBST in path or "__GSC_HEREDOC_" in path:
            return []
        out = []
        for word in expand_braces(path):
            full = self.resolve(word, base)
            cands = [full]
            if any(ch in word for ch in "*?["):
                cands += [norm(g) for g in glob.glob(full)]
            for c in cands:
                rel = rel_to(c, self.root)
                if rel and rel != "." and rel.split("/")[0].lower() in APPEND_ONLY_DIRS:
                    out.append(rel)
        return out

    def tracked(self, rels):
        """True if any of these repo-relative paths (files, folders or globs) is in the
        git index. One `git ls-files`; an error counts as tracked (fail closed)."""
        if not rels:
            return False
        try:
            r = subprocess.run(["git", "-C", self.root, "ls-files", "-z", "--"] +
                               [":(icase)" + p for p in rels], capture_output=True, timeout=10)
        except (OSError, subprocess.SubprocessError):
            return True
        return r.returncode != 0 or bool(r.stdout.strip(b"\0"))

    # ---- memos on main are never edited in place (MODEL v4.5.0 §6.6)

    def memo_rel(self, path, base):
        """Repo-relative path of `path` when it lies under memos/, else None."""
        if not path or SUBST in path or "__GSC_HEREDOC_" in path:
            return None
        rel = rel_to(self.resolve(path, base), self.root)
        if rel and rel != "." and "/" in rel and rel.split("/")[0].lower() == MEMO_DIR:
            return rel
        return None

    def on_main(self, rel):
        """True if the file `rel` exists under memos/ on origin/main, compared without
        case (paths here may be case-folded); None when git cannot list it (the caller
        fails closed). One `git ls-tree -r`."""
        try:
            r = subprocess.run(["git", "-C", self.root, "ls-tree", "-r", "-z", "--name-only", MAIN_REF,
                                "--", MEMO_DIR], capture_output=True, timeout=10)
        except (OSError, subprocess.SubprocessError):
            return None
        if r.returncode != 0:
            return None
        names = {n.lower() for n in r.stdout.decode("utf-8", "replace").split("\0") if n}
        return rel.lower() in names

    def register_rel(self, path, base):
        """'_REGISTER.md' or 'register.csv' when `path` names one of them at the repo
        root (globs expanded), else None."""
        if not path or SUBST in path or "__GSC_HEREDOC_" in path:
            return None
        for word in expand_braces(path):
            full = self.resolve(word, base)
            cands = [full]
            if any(ch in word for ch in "*?["):
                cands += [norm(g) for g in glob.glob(full)]
            for c in cands:
                rel = rel_to(c, self.root)
                if rel and rel.lower() in REGISTER_FILES:
                    return rel
        return None

    def need_not_register(self, paths, base, what):
        """No hand write of the register files (MODEL v4.5.0 §7.1)."""
        for p in paths:
            rel = self.register_rel(p, base)
            if rel:
                block(f"{what} on '{rel}': {REGISTER_HINT}")

    def need_not_archive(self, paths, base, what):
        """Any write at all into archive/ (editors, redirections, touch …)."""
        for p in paths:
            rels = self.archive_rels(p, base)
            if rels:
                block(f"{what} on '{rels[0]}': {APPEND_ONLY_HINT}")

    def need_untracked_archive(self, paths, base, what):
        """Removing or overwriting an archive/ path is allowed only while git does not
        track it (INTAKE's restart removes its own uncommitted snapshot copies)."""
        rels = [r for p in paths for r in self.archive_rels(p, base)]
        if rels and self.tracked(rels):
            block(f"{what} on tracked '{rels[0]}': {APPEND_ONLY_HINT}")

    def dest_paths(self, dest, sources, base):
        """The files a copy or move writes: dest/<basename of each source> when dest is a
        folder, else dest itself."""
        full = self.resolve(dest, base)
        if dest.endswith("/") or os.path.isdir(full):
            return [os.path.join(full, os.path.basename(s.rstrip("/"))) for s in sources
                    if os.path.basename(s.rstrip("/"))]
        return [dest]

    # ---- variables

    def expand(self, word):
        def sub(m):
            name = m.group(1) or m.group(2)
            if name in self.vars:
                val = self.vars[name]
                return m.group(0) if val is None else val
            return os.environ.get(name, m.group(0))
        return VAR_RE.sub(sub, word)

    def check_assign(self, name, value=None):
        if name in TOKEN_VARS:
            block(f"setting {name} is not allowed (routines never handle tokens)")
        if GIT_ENV_LOCKED.match(name):
            block(f"setting {name} is not allowed (it redirects git)")
        if name in PROGRAM_VARS and value not in (None, "", "cat"):
            block(f"setting {name} to a program is not allowed (only {name}=cat)")

    def set_var(self, name, value):
        value = self.expand(value)
        if SUBST in value or "$" in value:
            value = None                       # unknown at check time
        if name in self.vars and self.vars[name] != value:
            value = None                       # assigned twice: ambiguous
        self.vars[name] = value

    # ---- shell commands

    def check_command(self, cmd, depth, base):
        if depth > MAX_DEPTH:
            block("command nesting is too deep to check")
        segs, heredocs, subs = scan(cmd)
        lvl = {"texts": [body for _, body in heredocs], "stdin_code": False, "stdin_shell": False}
        queue = list(subs)
        for seg in segs:
            # $( ) and ` ` inside this segment run first, with the variables set so far.
            for _ in range(min(seg.count(SUBST), len(queue))):
                self.check_command(queue.pop(0), depth + 1, base)
            base = self.check_segment(seg, base, depth, lvl)
        for inner in queue:                    # anything left over (defensive)
            self.check_command(inner, depth + 1, base)
        for quoted, body in heredocs:          # unquoted bodies expand $( ) and ` `
            if not quoted:
                for inner in body_substitutions(body):
                    self.check_command(inner, depth + 1, base)
        # A shell fed from a pipe runs text the guard never sees.
        if lvl["stdin_shell"] and not lvl["texts"]:
            block("piping commands into a shell is not allowed; run them directly")
        # An interpreter reading stdin gets the heredoc / here-string text as code.
        for text in lvl["texts"]:
            if lvl["stdin_code"]:
                self.check_code(text)
            if lvl["stdin_shell"]:
                self.check_command(text, depth + 1, base)

    def skip_wrappers(self, words):
        while words:
            w = os.path.basename(words[0])
            if w in KEYWORDS:
                words = words[1:]
                continue
            m = ASSIGN_RE.match(words[0])
            if m:
                self.check_assign(m.group(1), m.group(2))
                words = words[1:]
                continue
            if w not in WRAPPERS:
                break
            if w == "command" and len(words) > 1 and words[1] in ("-v", "-V"):
                return []                      # lookup only, runs nothing
            opts, j = WRAPPERS[w], 1
            while j < len(words):
                a = words[j]
                if w == "env":
                    # GNU env takes any unambiguous prefix of a long option (getopt_long).
                    name = a.split("=", 1)[0]
                    long_opt = a.startswith("--") and len(name) >= 3
                    if re.match(r"^-[A-Za-z0-9]*S", a) or (long_opt and "--split-string".startswith(name)):
                        # env -S splits one string into the command and its arguments, which the guard
                        # cannot read word by word (MODEL v4.6.0 review): run the command directly.
                        block("env -S (split string) runs a command the guard cannot check; run the command directly")
                    if ((long_opt and "=" not in a and ("--unset".startswith(name) or "--chdir".startswith(name)))
                            or re.match(r"^-[A-Za-z0-9]*[uC]$", a)):
                        j += 2                     # --unset NAME, --chdir DIR, a cluster ending in -u or -C
                        continue
                if a in opts:
                    j += 2
                elif a.startswith("-") and a != "-":
                    j += 1
                elif w == "env" and ASSIGN_RE.match(a):
                    self.check_assign(*ASSIGN_RE.match(a).groups())
                    j += 1
                else:
                    break
            if w == "timeout" and j < len(words):
                j += 1                         # the duration
            words = words[j:]
        return words

    def redirections(self, words, base, lvl):
        """Check write redirections; return the words without them."""
        out, i = [], 0
        while i < len(words):
            m = REDIR_RE.match(words[i])
            if not m:
                out.append(words[i])
                i += 1
                continue
            op, target = m.group(2), m.group(3)
            if not target and i + 1 < len(words):
                target = words[i + 1]
                i += 1
            i += 1
            if op == "<<<":
                lvl["texts"].append(target)
            elif op in (">", ">>", ">|", "<>") or (op == ">&" and not re.fullmatch(r"\d*-?", target)):
                hit = self.locked(target, base)
                if hit:
                    block(f"redirection into '{hit}' (framework-locked)")
                self.need_not_archive([target], base, "redirection")
                self.need_not_register([target], base, "redirection")
        return out

    def check_segment(self, seg, base, depth, lvl):
        words = [self.expand(w) for w in tokens(seg)]
        # Leading keywords and plain assignments (NAME=value).
        assigns, i = [], 0
        while i < len(words):
            if words[i] in KEYWORDS:
                i += 1
                continue
            m = ASSIGN_RE.match(words[i])
            if not m:
                break
            self.check_assign(m.group(1), m.group(2))
            assigns.append((m.group(1), m.group(2)))
            i += 1
        words = words[i:]
        if not words:
            for name, value in assigns:        # NAME=value alone persists in the shell
                self.set_var(name, value)
            return base
        words = self.redirections(self.skip_wrappers(words), base, lvl)
        if not words:
            return base
        prog, args = os.path.basename(words[0]), words[1:]

        # git push / gh api text that is not a direct git/gh call cannot be checked.
        # Read-only text tools may mention it (searching the playbooks), but sed/awk only
        # without in-place editing, and echo/printf only when their output isn't run.
        read_only = prog in READ_ONLY_TOOLS and not (
            prog == "sed" and any(re.match(r"^-[A-Za-z]*i", a) or a.startswith("--in-place") for a in args)
        ) and not (prog in ("awk", "gawk") and re.search(r"inplace", " ".join(args)))
        if prog not in ("git", "gh") and not read_only and \
                (PUSH_TEXT_RE.search(seg) or GHAPI_TEXT_RE.search(seg)):
            block(f"'{short(seg)}' hides git push / gh api where the guard cannot check it; run it directly")

        if prog in ("cd", "pushd"):
            dest = [a for a in args if not a.startswith("-")]
            if not dest:
                return norm(os.path.expanduser("~"))
            if SUBST in dest[0] or "$" in dest[0]:
                # The guard would lose track of where relative paths point.
                block(f"cd to a computed path ('{short(dest[0], 40)}') is not allowed; "
                      "use paths from the repo root")
            return self.resolve(dest[0], base)
        if prog in ("export", "declare", "typeset", "local", "readonly"):
            for a in args:
                m = ASSIGN_RE.match(a)
                name = m.group(1) if m else a
                self.check_assign(name, m.group(2) if m else None)
                if m:
                    self.set_var(name, m.group(2))
            return base
        if prog == "printenv" and any(a in TOKEN_VARS for a in args):
            block("printing GitHub tokens is not allowed")
        if prog == "git":
            self.check_git(args, base)
        elif prog == "gh":
            self.check_gh(args)
        elif prog in ("curl", "wget"):
            self.check_http(prog, args)
        elif prog == "eval":
            self.check_command(" ".join(args), depth + 1, base)
        elif prog in ("source", "."):
            if args:
                self.check_script(args[0], base, True, depth)
        elif prog == "find":
            self.check_find(args, base)
        if prog in WRITE_PROGS:
            self.check_writes(prog, args, base)
        if INTERPRETERS.match(prog):
            self.check_interpreter(prog, args, base, depth, lvl)
        elif "/" in words[0]:
            self.check_path_program(words[0], base, depth)
        return base

    def check_path_program(self, path, base, depth):
        """A program run by path (./x.sh, /tmp/p.py): look inside it if it is a script."""
        full = self.resolve(path, base)
        try:
            if not os.path.isfile(full) or os.path.getsize(full) > 512 * 1024:
                return
            with open(full, "rb") as fh:
                head = fh.read(256)
        except OSError:
            return
        first = head.split(b"\n", 1)[0].decode("utf-8", "replace")
        if first.startswith("#!"):
            parts = first[2:].split()
            interp = os.path.basename(parts[0]) if parts else "sh"
            if interp == "env":                # #!/usr/bin/env [-S] python3
                rest = [p for p in parts[1:] if not p.startswith("-") and "=" not in p]
                interp = os.path.basename(rest[0]) if rest else "sh"
            self.check_script(path, base, interp in SHELLS, depth)
        elif full.endswith((".sh", ".bash")):
            self.check_script(path, base, True, depth)
        elif full.endswith((".py", ".js", ".pl", ".rb")):
            self.check_script(path, base, False, depth)

    # ---- file-writing programs

    def positionals(self, prog, args):
        """(positional args, target directory from -t/--target-directory or None)."""
        pos, target, i, opts = [], None, 0, OPT_VALUE.get(prog, set())
        while i < len(args):
            a = args[i]
            if a == "--":
                pos += args[i + 1:]
                break
            if prog in ("cp", "mv", "ln", "install") and a in ("-t", "--target-directory"):
                target = args[i + 1] if i + 1 < len(args) else None
                i += 2
                continue
            m = re.match(r"^-([A-Za-z]*)t(.*)$", a) if prog in ("cp", "mv", "ln", "install") \
                and not a.startswith("--") else None
            if m:                                # combined short flags: -rt DIR or -tDIR
                if m.group(2):
                    target = m.group(2)
                    i += 1
                else:
                    target = args[i + 1] if i + 1 < len(args) else None
                    i += 2
                continue
            if prog in ("cp", "mv", "ln", "install") and a.startswith("--target-directory="):
                target = a.split("=", 1)[1]
            elif a in opts:
                i += 2
                continue
            elif not a.startswith("-") or a == "-":
                pos.append(a)
            i += 1
        return pos, target

    def check_dest(self, dest, sources, base, what):
        """Destination of cp/mv/install/rsync, including dest/<basename of source>."""
        self.need_unlocked([dest], base, what)
        full = self.resolve(dest, base)
        if dest.endswith("/") or os.path.isdir(full):
            for s in sources:
                name = os.path.basename(s.rstrip("/"))
                if name:
                    self.need_unlocked([os.path.join(full, name)], base, what)

    def check_writes(self, prog, args, base):
        pos, target = self.positionals(prog, args)
        if prog in ("cp", "install", "rsync"):
            sources, dest = (pos, target) if target else (pos[:-1], pos[-1] if len(pos) >= 2 else None)
            if dest:
                self.check_dest(dest, sources, base, prog)
                self.need_untracked_archive(self.dest_paths(dest, sources, base), base, prog)
                self.need_not_register(self.dest_paths(dest, sources, base), base, prog)
        elif prog == "mv":
            sources = pos if target else pos[:-1]
            self.need_unlocked(sources, base, "mv", whole=True)
            self.need_not_archive(sources, base, "mv out of archive/")
            self.need_not_register(sources, base, "mv")
            dest = target or (pos[-1] if len(pos) >= 2 else None)
            if dest:
                self.check_dest(dest, sources, base, "mv")
                self.need_untracked_archive(self.dest_paths(dest, sources, base), base, "mv")
                self.need_not_register(self.dest_paths(dest, sources, base), base, "mv")
        elif prog in ("rm", "rmdir", "unlink", "shred", "chmod", "chown", "chgrp"):
            self.need_unlocked(pos, base, prog, whole=True)
            self.need_not_register(pos, base, prog)
            if prog in ("chmod", "chown", "chgrp"):
                self.need_not_archive(pos, base, prog)
            else:
                self.need_untracked_archive(pos, base, prog)
        elif prog in ("touch", "mkdir", "truncate", "ln", "tee"):
            self.need_unlocked(pos + ([target] if target else []), base, prog)
            if prog != "mkdir":
                self.need_not_archive(pos + ([target] if target else []), base, prog)
                self.need_not_register(pos + ([target] if target else []), base, prog)
        elif prog == "dd":
            outs = [a[3:] for a in args if a.startswith("of=")]
            self.need_unlocked(outs, base, "dd")
            self.need_not_archive(outs, base, "dd")
            self.need_not_register(outs, base, "dd")
        elif prog == "sed":
            if any(re.match(r"^-[A-Za-z]*i", a) or a.startswith("--in-place") for a in args):
                # Without -e/-f the first positional is the sed script, not a file.
                scripted = any(a in ("-e", "-f") or a.startswith(("--expression", "--file"))
                               for a in args)
                self.need_unlocked(pos if scripted else pos[1:], base, "sed -i")
                self.need_not_archive(pos if scripted else pos[1:], base, "sed -i")
                self.need_not_register(pos if scripted else pos[1:], base, "sed -i")
        elif prog == "perl":
            if any(re.match(r"^-[A-Za-z]*i", a) for a in args):
                self.need_unlocked(pos, base, "perl -i")
                self.need_not_archive(pos, base, "perl -i")
                self.need_not_register(pos, base, "perl -i")
        elif prog in ("awk", "gawk"):
            joined = " ".join(args)
            if re.search(r"(^|\s)(-i\s*inplace|--include[= ]inplace)", joined):
                self.need_unlocked(pos, base, f"{prog} -i inplace")
                self.need_not_archive(pos, base, f"{prog} -i inplace")
                self.need_not_register(pos, base, f"{prog} -i inplace")
        elif prog in ("tar", "unzip"):
            if prog == "unzip":
                # -l/-v list, -p prints to stdout, -t tests, -Z/-z show info: nothing is written.
                extract = not any(re.match(r"^-[A-Za-z]*[lpvtZz]", a) for a in args
                                  if a.startswith("-") and not a.startswith("--"))
            else:
                extract = any(
                    a in ("-x", "--extract", "--get") or re.match(r"^-?[A-Za-wyz]*x[A-Za-z]*$", a)
                    for a in args[:1] + [a for a in args if a.startswith("-")])
            if extract:
                flag = ("-d",) if prog == "unzip" else ("-C", "--directory")
                dest = base
                for k, a in enumerate(args):
                    if a in flag and k + 1 < len(args):
                        dest = self.resolve(args[k + 1], base)
                    elif a.startswith("--directory="):
                        dest = self.resolve(a.split("=", 1)[1], base)
                # The repo root counts as locked here: extract archives under /tmp.
                self.need_unlocked([dest], base, f"{prog} extraction", whole=True)
                self.need_not_archive([dest], base, f"{prog} extraction")

    def check_find(self, args, base):
        """find … -delete / -exec <writer>: the start paths must not hold locked files."""
        writes = "-delete" in args
        for k, a in enumerate(args):
            if a in ("-exec", "-execdir", "-ok", "-okdir") and k + 1 < len(args):
                if os.path.basename(args[k + 1]) in WRITE_PROGS | {"git"}:
                    writes = True
        if not writes:
            return
        starts = []
        for a in args:
            if a.startswith("-") or a in ("(", "!", ")"):
                break
            starts.append(a)
        self.need_unlocked(starts or ["."], base, "find with -delete/-exec", whole=True)
        self.need_untracked_archive(starts or ["."], base, "find with -delete/-exec")

    # ---- interpreters

    def check_code(self, code, net=True):
        """Interpreter code. net=False for shell code, which check_command parses properly."""
        if LOCKED_FRAG_RE.search(code) and WRITE_IND_RE.search(code):
            frag = LOCKED_FRAG_RE.search(code).group(0)
            block(f"script code writes and names a locked path ('{frag}'); routines never change locked files")
        if net and (CODE_PUSH_RE.search(code) or CODE_GHAPI_RE.search(code)):
            block("script code mentions git push / gh api; routine scripts never talk to GitHub "
                  "(run git and gh commands directly)")
        if net and CODE_GITHUB_RE.search(code) and CODE_HTTP_WRITE_RE.search(code):
            block("script code names github.com beside a request body or write method; routine scripts never "
                  "write to GitHub (only the gh api REST forms of routines/README.md §1)")

    def check_script(self, path, base, shell, depth):
        """Look inside a script file the command runs (small files only)."""
        full = self.resolve(path, base)
        try:
            if not os.path.isfile(full) or os.path.getsize(full) > 512 * 1024:
                return
            with open(full, "r", encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError:
            return
        if shell:
            self.check_command(text, depth + 1, base)
        else:
            self.check_code(text)

    def check_interpreter(self, prog, args, base, depth, lvl):
        shell = prog in SHELLS
        if args[:1] and args[0] in ("--version", "-V", "--help", "-h"):
            return
        codes, script, stdin, i = [], None, False, 0
        module_words = []
        while i < len(args):
            a = args[i]
            nxt = args[i + 1] if i + 1 < len(args) else ""
            if a == "-":
                stdin = True
                break
            if prog.startswith("python"):
                if a == "--check-hash-based-pycs":
                    i += 2
                    continue
                opt, value = python_short_option(a) if re.match(r"^-[A-Za-z]", a) else (None, None)
                taken = 1 if value else 2           # the attached value, or the next word
                if opt == "c":
                    codes.append(value or nxt)
                    break
                if opt == "m":
                    # The module and its arguments: python3 -m routines.tools.gsc_register retire …,
                    # or a runner module (runpy, pdb, cProfile, trace) in front of the tool.
                    module_words = ([value] if value else []) + args[i + 1:]
                    break
                if opt in ("W", "X"):
                    i += taken
                    continue
            elif prog in ("node", "nodejs"):
                if a in ("-e", "--eval", "-p", "--print"):
                    codes.append(nxt)
                    break
            elif prog in ("perl", "ruby"):
                if re.match(r"^-[A-Za-z]*[eE]$", a):
                    codes.append(nxt)          # perl allows several -e
                    i += 2
                    continue
            elif shell:
                if re.match(r"^-[A-Za-z]*c$", a):
                    codes.append(nxt)
                    break
                if a == "-s":
                    stdin = True
                    break
            if a.startswith("-"):
                i += 1
                continue
            if not codes:
                script = a
            break
        for code in codes:
            self.check_code(code, net=not shell)
            if shell:
                self.check_command(code, depth + 1, base)
        if script:
            if os.path.basename(script.replace("\\", "/")).lower() == "gsc_register.py":
                check_register_tool(args[i + 1:])
            self.check_script(script, base, shell, depth)
        for k, word in enumerate(module_words):
            if register_tool_word(word):
                check_register_tool(module_words[k + 1:])
                break
        # A module may read its stdin as code (code, pdb), so a heredoc fed to it is checked as code too.
        if not codes and not script:
            stdin = True
        if stdin:
            lvl["stdin_shell" if shell else "stdin_code"] = True

    # ---- git

    def current_branch(self):
        """Current branch of the repo root ('' when detached or unknown). One subprocess at most."""
        if self._branch is None:
            try:
                r = subprocess.run(["git", "-C", self.root, "symbolic-ref", "--short", "-q", "HEAD"],
                                   capture_output=True, text=True, timeout=10)
                self._branch = r.stdout.strip() if r.returncode == 0 else ""
            except (OSError, subprocess.SubprocessError):
                self._branch = ""
        return self._branch

    def check_git(self, args, base):
        gitcwd, i = base, 0
        while i < len(args) and args[i].startswith("-"):
            a = args[i]
            nxt = args[i + 1] if i + 1 < len(args) else ""
            if a == "-C":
                gitcwd = self.resolve(nxt, gitcwd)
                i += 2
            elif a == "-c":
                key = nxt.split("=", 1)[0].lower()
                if not GIT_C_OK.match(key):
                    block(f"git -c {key or '?'} is not allowed in routines")
                i += 2
            elif a in GIT_GLOBAL_OK:
                i += 1
            elif a in ("--version", "--help", "-h", "-v"):
                return
            else:
                block(f"git option '{a}' is not allowed in routines")
        if i >= len(args):
            return
        sub, rest = args[i], args[i + 1:]
        if sub in GIT_DENY:
            block(f"git {sub} is blocked: {GIT_DENY[sub]}")
        for a in rest:
            if a.startswith(GIT_EXEC_OPTS) or (sub == "grep" and a.startswith("-O")):
                block(f"git {sub} {a.split('=', 1)[0]} makes git run another program; not allowed in routines")
        handler = {
            "push": self.git_push, "config": self.git_config, "switch": self.git_switch,
            "checkout": self.git_checkout, "restore": self.git_restore, "reset": self.git_reset,
            "rm": self.git_rm_mv, "mv": self.git_rm_mv, "add": self.git_add,
            "clean": self.git_clean, "commit": self.git_commit, "branch": self.git_branch,
            "merge": self.git_merge, "symbolic-ref": self.git_symbolic_ref,
            "remote": self.git_remote, "lfs": self.git_lfs, "fetch": self.git_fetch,
        }.get(sub)
        if handler:
            handler(sub, rest, gitcwd)

    def git_push(self, sub, rest, gitcwd):
        if rel_to(gitcwd, self.root) is None:
            block("git push is allowed only inside the repo checkout")
        # The directory git runs in must be the root's own repository: a nested copy of .git (or a
        # worktree) would push another HEAD while the root still sits on the run branch.
        try:
            r = subprocess.run(["git", "-C", gitcwd, "rev-parse", "--show-toplevel", "--absolute-git-dir"],
                               capture_output=True, text=True, timeout=10)
            lines = r.stdout.splitlines() if r.returncode == 0 else []
        except (OSError, subprocess.SubprocessError):
            lines = []
        if len(lines) != 2 or norm(lines[0]) != self.root or norm(lines[1]) != self.git_dir():
            block("git push from a directory that is not the repo checkout's own repository (a nested or copied "
                  ".git, or a worktree); push only from the repo root")
        pos = []
        for a in rest:
            if a in ("-u", "--set-upstream", "-q", "--quiet"):
                continue
            if a.startswith("-"):
                block(f"git push option '{a}' is not allowed (only -u)")
            pos.append(a)
        if len(pos) != 2 or pos[0] != "origin":
            block('the only push form is: git push -u origin "$BR" (remote origin, one branch)')
        dest = pos[1]
        if "$" in dest:
            block(f"push destination '{dest}' is not set in this command; "
                  "set BR=… in the same command, or use the literal branch name or HEAD")
        if dest != "HEAD" and not BRANCH_RE.match(dest):
            block(f"push destination '{short(dest, 60)}' is not this run's claude/gsc-… branch")
        if dest != "HEAD" and BRANCH_RE.match(dest).group(1) == "weekly":
            block(f"git push of '{short(dest, 60)}': " + WEEKLY_READ_ONLY)
        cur = self.current_branch()
        if not BRANCH_RE.match(cur):
            block(f"current branch is '{cur or 'detached HEAD'}', not a claude/gsc-… run branch; never push main")
        if BRANCH_RE.match(cur).group(1) == "weekly" or self.prompt_job() == "weekly":
            block("git push on a WEEKLY branch: " + WEEKLY_READ_ONLY)
        if dest != "HEAD" and dest != cur:
            block(f"push destination '{dest}' is not the current branch '{cur}'")
        self.pinned_job("git push")

    def git_config(self, sub, rest, gitcwd):
        if any(a in ("--edit", "-e") for a in rest) or rest[:1] == ["edit"]:
            block("git config --edit is not allowed in routines")
        write = read = False
        if rest[:1] and rest[0] in ("set", "unset", "rename-section", "remove-section"):
            write, rest = True, rest[1:]
        elif rest[:1] and rest[0] in ("get", "list"):
            read, rest = True, rest[1:]
        pos, i = [], 0
        while i < len(rest):
            a = rest[i]
            if a in ("--file", "-f", "--blob", "--type", "--default", "--comment", "--value"):
                if a in ("--file", "-f") and i + 1 < len(rest):
                    self.need_unlocked([rest[i + 1]], gitcwd, "git config --file")
                i += 2
                continue
            if a in ("--add", "--unset", "--unset-all", "--replace-all", "--rename-section",
                     "--remove-section"):
                write = True
            elif a.startswith("--get") or a in ("--list", "-l"):
                read = True
            elif not a.startswith("-"):
                pos.append(a)
            i += 1
        if not read and len(pos) >= 2:
            write = True
        if write and pos and GIT_CONFIG_LOCKED.match(pos[0].lower()):
            block(f"git config write to '{pos[0]}' is not allowed in routines")

    def leave_run_branch(self, what):
        """A run never leaves its run branch (one run, one branch): refuse branch moves once HEAD is on one."""
        cur = self.current_branch()
        if BRANCH_RE.match(cur):
            block(f"{what} on the run branch '{cur}': a run never leaves or adds a branch once its run branch is "
                  "cut (routines/README.md §1)")

    def git_switch(self, sub, rest, gitcwd):
        self.leave_run_branch(f"git {sub}")
        create_flags = ("-b",) if sub == "checkout" else ("-c", "--create")
        create, pos, i = None, [], 0
        while i < len(rest):
            a = rest[i]
            if a in create_flags:
                create = rest[i + 1] if i + 1 < len(rest) else ""
                i += 2
                continue
            if a in ("--no-track", "-q", "--quiet"):
                i += 1
                continue
            if a.startswith("-"):
                block(f"git {sub} option '{a}' is not allowed (use git switch --no-track -c <run branch> origin/main)")
            pos.append(a)
            i += 1
        if create is not None:
            if not BRANCH_RE.match(create):
                block(f"new branch '{short(create, 60)}' does not match claude/gsc-{{job}}-[KEY-]D-T")
            if pos not in ([], ["origin/main"]):
                block("new run branches start from origin/main")
            return
        # origin/main alone would detach HEAD (no branch, no job): never needed
        if len(pos) == 1 and (BRANCH_RE.match(pos[0]) or pos[0] == "main"):
            return
        block(f"git {sub} form not allowed (use git switch --no-track -c <run branch> origin/main)")

    def git_checkout(self, sub, rest, gitcwd):
        if "--" in rest:
            k = rest.index("--")
            if [a for a in rest[:k] if a not in ("-q", "--quiet", "HEAD")]:
                block("only git checkout -- <paths> is allowed for restoring files")
            self.git_paths(rest[k + 1:], gitcwd, "git checkout")
            return
        self.git_switch(sub, rest, gitcwd)

    def git_paths(self, paths, gitcwd, what):
        if not paths:
            block(f"{what} needs explicit paths")
        for p in paths:
            if p.startswith(":"):
                block(f"{what}: pathspec magic is not allowed")
        self.need_unlocked(paths, gitcwd, what, whole=True)

    def git_restore(self, sub, rest, gitcwd):
        paths, i = [], 0
        while i < len(rest):
            a = rest[i]
            if a in ("-s", "--source"):
                i += 2
                continue
            if not a.startswith("-"):
                paths.append(a)
            i += 1
        self.git_paths(paths, gitcwd, "git restore")

    def git_reset(self, sub, rest, gitcwd):
        if any(a in ("--hard", "--merge", "--keep", "--soft") for a in rest):
            block("git reset --hard/--merge/--keep/--soft is not allowed")
        k = rest.index("--") if "--" in rest else len(rest)
        paths = rest[k + 1:]
        for a in rest[:k]:
            if a.startswith("-"):
                continue
            if not os.path.exists(self.resolve(a, gitcwd)):
                block(f"git reset to a ref ('{short(a, 40)}') is not allowed")
            paths.append(a)
        if paths:
            self.git_paths(paths, gitcwd, "git reset")

    def no_weekly_write(self, what):
        if self.weekly_session():
            block(f"{what} on a WEEKLY run: " + WEEKLY_READ_ONLY)

    def git_rm_mv(self, sub, rest, gitcwd):
        self.no_weekly_write(f"git {sub}")
        if any(a.startswith("--pathspec-from-file") for a in rest):
            block(f"git {sub} --pathspec-from-file is not allowed")
        k = rest.index("--") if "--" in rest else len(rest)
        paths = [a for a in rest[:k] if not a.startswith("-")] + rest[k + 1:]
        self.git_paths(paths, gitcwd, f"git {sub}")
        if sub == "rm":
            self.need_untracked_archive(paths, gitcwd, "git rm")
        elif sub == "mv" and len(paths) >= 2:
            self.need_not_archive(paths[:-1], gitcwd, "git mv out of archive/")
            self.need_untracked_archive(self.dest_paths(paths[-1], paths[:-1], gitcwd), gitcwd, "git mv")

    def git_add(self, sub, rest, gitcwd):
        if any(a in ("-A", "--all", "-u", "--update", "--no-ignore-removal") or
               a.startswith("--pathspec-from-file") for a in rest):
            block("git add needs explicit paths (never -A/-u on a run branch)")
        self.git_rm_mv("add", rest, gitcwd)

    def git_clean(self, sub, rest, gitcwd):
        if "-n" in rest or "--dry-run" in rest:
            return
        paths, i = [], 0
        while i < len(rest):
            if rest[i] in ("-e", "--exclude"):
                i += 2
                continue
            if not rest[i].startswith("-"):
                paths.append(rest[i])
            i += 1
        self.git_paths(paths, gitcwd, "git clean")

    def git_commit(self, sub, rest, gitcwd):
        self.no_weekly_write("git commit")
        if "--amend" in rest:
            block("git commit --amend is not allowed (never rewrite a pushed run branch)")

    def git_branch(self, sub, rest, gitcwd):
        bad = {"-D", "-M", "-C", "-f", "--force", "-m", "--move", "-c", "--copy",
               "-u", "--set-upstream-to", "--unset-upstream", "--edit-description"}
        for a in rest:
            if a in bad or a.startswith("--set-upstream-to="):
                block(f"git branch {a} is not allowed in routines")
        listing = ("--list", "-l", "-a", "--all", "-r", "--remotes", "--contains", "--no-contains",
                   "--merged", "--no-merged", "--points-at", "-v", "-vv", "--verbose",
                   "--show-current", "--format", "--sort", "--column", "-d", "--delete")
        if any(a in listing or a.split("=", 1)[0] in listing for a in rest):
            return
        pos = [a for a in rest if not a.startswith("-")]
        if pos and not BRANCH_RE.match(pos[0]):
            block(f"new branch '{short(pos[0], 60)}' does not match claude/gsc-{{job}}-[KEY-]D-T")
        if pos:
            self.leave_run_branch("git branch (a new branch)")

    def git_merge(self, sub, rest, gitcwd):
        if rest in (["--abort"], ["--continue"]):
            return
        opts = [a for a in rest if a.startswith("-")]
        pos = [a for a in rest if not a.startswith("-")]
        if pos == ["origin/main"] and set(opts) <= {"--no-edit", "--ff-only", "-q", "--quiet"}:
            return
        block("the only merge is: git merge --no-edit origin/main")

    def git_symbolic_ref(self, sub, rest, gitcwd):
        pos, i = [], 0
        while i < len(rest):
            if rest[i] in ("-d", "--delete"):
                block("git symbolic-ref --delete is not allowed")
            if rest[i] == "-m":
                i += 2
                continue
            if not rest[i].startswith("-"):
                pos.append(rest[i])
            i += 1
        if len(pos) >= 2:
            block("git symbolic-ref writes are not allowed")

    def git_remote(self, sub, rest, gitcwd):
        if rest[:1] and rest[0] in ("add", "set-url", "rename", "remove", "rm", "set-head",
                                    "set-branches"):
            block(f"git remote {rest[0]} is not allowed in routines")

    def git_fetch(self, sub, rest, gitcwd):
        """Only git fetch origin main (CLAUDE.md, README §1): a refspec could rewrite refs/remotes/origin/main,
        which the memo-on-main rule trusts."""
        pos = []
        for a in rest:
            if a in ("-q", "--quiet", "--no-tags", "--prune", "-p"):
                continue
            if a.startswith("-"):
                block(f"git fetch option '{a}' is not allowed (only git fetch origin main)")
            pos.append(a)
        if pos not in ([], ["origin"], ["origin", "main"]):
            block(f"git fetch {' '.join(short(x, 40) for x in pos)}: only git fetch origin main (no refspec)")

    def git_lfs(self, sub, rest, gitcwd):
        if "push" in rest:
            block("git lfs push is not allowed")

    # ---- gh

    def check_gh(self, args):
        if args in (["--version"], ["version"]):
            return
        if not args or args[0] != "api":
            block(f"gh {args[0] if args else ''} is not allowed; use gh api REST per routines/README §1")
        method, fields, has_input, pos, i = None, [], False, [], 1
        while i < len(args):
            a = args[i]
            nxt = args[i + 1] if i + 1 < len(args) else ""
            if a in ("-X", "--method"):
                method, i = nxt, i + 2
            elif a.startswith("--method="):
                method, i = a.split("=", 1)[1], i + 1
            elif a.startswith("-X"):
                method, i = a[2:], i + 1
            elif a in ("-f", "-F", "--field", "--raw-field"):
                fields.append(nxt)
                i += 2
            elif a.startswith(("--field=", "--raw-field=")):
                fields.append(a.split("=", 1)[1])
                i += 1
            elif a.startswith(("-f", "-F")) and not a.startswith("--"):
                fields.append(a[2:])
                i += 1
            elif a == "--input" or a.startswith("--input="):
                has_input = True
                i += 1 if "=" in a else 2
            elif a in ("-H", "--header") or a.startswith("--header="):
                header = a.split("=", 1)[1] if "=" in a else nxt
                if re.search(r"authorization", header, re.I):
                    block("gh api with an Authorization header (routines never handle tokens)")
                i += 1 if "=" in a else 2
            elif a == "--hostname" or a.startswith("--hostname="):
                host = a.split("=", 1)[1] if "=" in a else nxt
                if host.lower() != "github.com":
                    block(f"gh api --hostname {host} is not allowed")
                i += 1 if "=" in a else 2
            elif a in ("--jq", "-q", "--template", "-t", "--cache", "-p", "--preview"):
                i += 2
            elif a.startswith(("--jq=", "--template=", "--cache=", "--preview=")) or \
                    a in ("--paginate", "--slurp", "-i", "--include", "--silent", "--verbose"):
                i += 1
            elif a.startswith("-"):
                block(f"gh api option '{a}' is not allowed in routines")
            else:
                pos.append(a)
                i += 1
        if len(pos) != 1:
            block("gh api takes exactly one endpoint")
        ep = pos[0].lstrip("/").split("?", 1)[0]
        method = (method or ("POST" if fields or has_input else "GET")).upper()
        if re.match(r"^graphql\b", ep, re.I):
            block("gh api graphql is not allowed; use REST per routines/README §1")
        if method == "GET":
            return
        if self.weekly_session():
            block(f"gh api {method} on a WEEKLY run: " + WEEKLY_READ_ONLY)
        # Off a run branch (INTAKE's step-0 sweep runs before its branch) the prompt must still name a
        # job; on one, the branch's job must be the prompt's.
        if not self.prompt_job() or self.run_job():
            self.pinned_job(f"gh api {method}")
        if has_input:
            block("gh api --input is not allowed for writes; use -f/-F fields")
        if ep.startswith("$"):
            block(f"gh api endpoint '{short(ep, 40)}' is not set in this command; "
                  "set R=… in the same command or write the repos/… path out")
        kv = {}
        for f in fields:
            key, _, value = f.partition("=")
            kv[key] = value
        repo = r"repos/(?:jakubhoryna/value-investing-model|\{owner\}/\{repo\})"
        num = r"(?:\d+|\$\{?\w+\}?|" + SUBST + r")"
        if method == "POST" and re.fullmatch(repo + r"/pulls", ep, re.I):
            extra = set(kv) - {"head", "base", "title", "body", "draft"}
            if extra:
                block(f"PR create with fields {sorted(extra)} is not allowed")
            if kv.get("base") != "main":
                block("a routine PR must have base=main")
            head = kv.get("head", "")
            if head and "$" not in head and SUBST not in head and not BRANCH_RE.match(head):
                block(f"PR head '{short(head, 60)}' is not a claude/gsc-… run branch")
            if head and BRANCH_RE.match(head) and BRANCH_RE.match(head).group(1) == "weekly":
                block(f"PR from '{short(head, 60)}': " + WEEKLY_READ_ONLY)
            return
        if method == "PATCH" and re.fullmatch(repo + r"/pulls/" + num, ep, re.I):
            extra = set(kv) - {"title", "body", "state"}
            if extra:
                block(f"PR PATCH of {sorted(extra)} is not allowed (title, body, state=closed only)")
            if "state" in kv and kv["state"] != "closed":
                block("PR PATCH may only set state=closed")
            return
        if re.search(r"/comments$", ep, re.I):
            block("routines never comment on a PR or issue (MODEL v4.5.0 §8.7 item 1): a comment wakes the "
                  "session watching it; put the text in the run note or the PR body")
        block(f"gh api {method} {short(ep, 70)} is not on the routine allowlist "
              f"(never merge, comment, contents, git refs, graphql or other repos)")

    # ---- curl / wget

    def check_http(self, prog, args):
        # Options that read the url, method or body from a file the guard does not see.
        for a in args:
            if prog == "curl" and (a == "-K" or a.startswith("--config") or re.match(r"^-[A-Za-z]*K", a)):
                block("curl -K/--config reads options from a file the guard cannot check; write them out")
            if prog == "wget" and (a in ("-i", "-e") or re.match(r"^-[ie]\S", a)
                                   or a.startswith(("--input-file", "--execute", "--config"))):
                block(f"wget {a.split('=', 1)[0]} reads urls or commands from elsewhere; write the url out")
        if not re.search(r"github\.com", " ".join(args), re.I):
            return
        write = False
        for k, a in enumerate(args):
            nxt = args[k + 1] if k + 1 < len(args) else ""
            if re.search(r"authorization", a, re.I) or \
                    (a in ("-H", "--header") and re.search(r"authorization", nxt, re.I)):
                block(f"{prog} with an Authorization header to GitHub (routines never handle tokens)")
            if prog == "curl":
                m = re.match(r"^(?:--request=?|-[A-Za-z]*X)(.*)$", a)
                if m:
                    verb = (m.group(1) or nxt).upper()
                    write = write or verb not in ("GET", "HEAD")
                elif a.startswith(("--data", "--json", "--form", "--upload-file")) or \
                        re.match(r"^-[A-Za-z]*[dFT]", a):
                    write = True
            elif a.startswith(("--method", "--post-data", "--post-file", "--body-data", "--body-file")):
                write = True
        if write:
            block(f"{prog} write to GitHub; use gh api REST per routines/README §1")


# ---------------------------------------------------------------- main

def main():
    # Defence in depth: outside routine sessions never block anything.
    if os.environ.get("GSC_SESSION", "") != "routine":
        return 0
    try:
        event = json.loads(sys.stdin.buffer.read().decode("utf-8", "replace"))
        if not isinstance(event, dict) or not isinstance(event.get("tool_name"), str):
            emit("malformed hook input; failing closed")
            return 2
        Guard(event).run()
        return 0
    except Blocked as b:
        emit(b)
        return 2
    except Exception as e:  # fail closed in routine sessions
        emit(f"internal error ({type(e).__name__}: {e}); failing closed")
        return 2


if __name__ == "__main__":
    sys.exit(main())
