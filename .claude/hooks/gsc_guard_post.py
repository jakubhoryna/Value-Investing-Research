#!/usr/bin/env python3
"""GSC routine guard: PostToolUse self-heal (MODEL §8.7, spec v2 §5).

Runs only when GSC_SESSION=routine; any other value exits 0 at once.
After every Bash/Monitor/Edit/Write/NotebookEdit call it checks the locked
paths and repairs what the PreToolUse guard could not see:

  * tracked locked files that changed or were deleted -> restored from HEAD
    (from MERGE_HEAD while `git merge origin/main` is in progress, so main's
    own framework changes are kept);
  * locked files staged as new -> unstaged; then handled as untracked;
  * untracked CLAUDE.md / CLAUDE.local.md / AGENTS.md anywhere, and
    .claude/settings*.json other than the tracked settings.json -> deleted;
  * other untracked files under model/ routines/ .claude/ .github/ ->
    reported once (the run cannot delete them, so they are not re-reported).

Exit 2 with one stderr line when it acted or has something new to report
(PostToolUse exit 2 only feeds the message back to Claude; the tool call has
already run). Exit 0 otherwise. Internal errors: one stderr line, exit 1
(reported in the transcript, never a loop).
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

PATHSPECS = ["model", "routines", ".claude", ".github", "CLAUDE.md",
             ":(glob)**/CLAUDE.md", ":(glob)**/CLAUDE.local.md", ":(glob)**/AGENTS.md"]
LOCKED_DIRS = ("model/", "routines/", ".claude/", ".github/")
DELETE_NAMES = {"claude.md", "claude.local.md", "agents.md"}
SETTINGS_RE = re.compile(r"^\.claude/settings[^/]*\.json$", re.I)
GUARD_SETTINGS = ".claude/settings.json"   # never deleted: it is the guard's own config


def say(text):
    line = " ".join(text.split())[:600]
    msg = f"GSC guard (routine session): {line} — see MODEL §8.7 / routines/README.md §3.\n"
    sys.stderr.buffer.write(msg.encode("utf-8", "replace"))
    sys.stderr.buffer.flush()


def git(root, *args):
    r = subprocess.run(["git", "-C", root, *args], capture_output=True, timeout=30)
    if r.returncode != 0:
        err = r.stderr.decode("utf-8", "replace").strip()[:200]
        raise RuntimeError(f"git {args[0]} failed: {err}")
    return r.stdout


def zsplit(raw):
    return [p for p in raw.decode("utf-8", "surrogateescape").split("\0") if p]


def deletable(rel):
    if rel == GUARD_SETTINGS:
        return False
    return os.path.basename(rel).lower() in DELETE_NAMES or bool(SETTINGS_RE.match(rel))


def remove(root, rel):
    full = os.path.join(root, rel)
    if os.path.isfile(full) or os.path.islink(full):
        os.remove(full)
        return True
    return False


def heal(root):
    restored, removed, report = [], [], []
    git_dir = git(root, "rev-parse", "--git-dir").decode().strip()
    ref = "MERGE_HEAD" if os.path.exists(os.path.join(root, git_dir, "MERGE_HEAD")) else "HEAD"

    # 1. Tracked locked files that differ from ref (worktree or index).
    changed = set(zsplit(git(root, "diff", "--name-only", "-z", "--no-renames", ref, "--", *PATHSPECS)))
    changed |= set(zsplit(git(root, "diff", "--cached", "--name-only", "-z", "--no-renames",
                              ref, "--", *PATHSPECS)))
    if changed:
        in_ref = set(zsplit(git(root, "ls-tree", "-r", "-z", "--name-only", ref, "--", *sorted(changed))))
        back = sorted(changed & in_ref)
        if back:
            git(root, "checkout", ref, "--", *back)
            restored += back
        for rel in sorted(changed - in_ref):     # staged as new: unstage, then treat as untracked
            git(root, "rm", "-q", "-f", "--cached", "--ignore-unmatch", "--", rel)
            if deletable(rel) and remove(root, rel):
                removed.append(rel)
            elif os.path.exists(os.path.join(root, rel)):
                report.append(rel)

    # 2. Untracked files in the locked set.
    for entry in zsplit(git(root, "status", "--porcelain=v1", "-z", "--untracked-files=all",
                            "--no-renames", "--", *PATHSPECS)):
        if not entry.startswith("?? "):
            continue
        rel = entry[3:]
        if deletable(rel) and remove(root, rel):
            removed.append(rel)
        elif rel.startswith(LOCKED_DIRS) and rel not in report:
            report.append(rel)

    # 3. Ignored settings files (.gitignore hides .claude/settings.local.json from status).
    cdir = os.path.join(root, ".claude")
    if os.path.isdir(cdir):
        for name in sorted(os.listdir(cdir)):
            rel = ".claude/" + name
            if deletable(rel) and rel not in removed and \
                    not zsplit(git(root, "ls-files", "-z", "--", rel)) and remove(root, rel):
                removed.append(rel)
    return restored, removed, report


def new_reports(root, report):
    """Paths not reported before in this checkout (state kept in the temp dir)."""
    if not report:
        return []
    key = hashlib.sha1(root.encode("utf-8", "replace")).hexdigest()[:12]
    state = os.path.join(tempfile.gettempdir(), f"gsc_guard_post_{key}.json")
    try:
        with open(state, "r", encoding="utf-8") as fh:
            seen = set(json.load(fh))
    except (OSError, ValueError):
        seen = set()
    fresh = [p for p in report if p not in seen]
    if fresh:
        try:
            with open(state, "w", encoding="utf-8") as fh:
                json.dump(sorted(seen | set(report)), fh)
        except OSError:
            pass
    return fresh


def main():
    if os.environ.get("GSC_SESSION", "") != "routine":
        return 0
    try:
        try:
            event = json.loads(sys.stdin.buffer.read().decode("utf-8", "replace") or "{}")
        except ValueError:
            event = {}
        cwd = event.get("cwd") if isinstance(event, dict) else None
        root = os.environ.get("CLAUDE_PROJECT_DIR") or cwd or os.getcwd()
        restored, removed, report = heal(root)
        fresh = new_reports(root, report)
        if not (restored or removed or fresh):
            return 0
        parts = []
        if restored:
            parts.append("restored locked files " + ", ".join(restored[:12]))
        if removed:
            parts.append("removed " + ", ".join(removed[:12]))
        if fresh:
            parts.append("untracked files under locked folders (left in place, never commit them): "
                         + ", ".join(fresh[:12]))
        say("post-check: " + "; ".join(parts) + ". Routines never change locked paths")
        return 2
    except Exception as e:  # never raise; report and let the session go on
        sys.stderr.write(f"GSC guard post-check: internal error ({type(e).__name__}: {e})\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
