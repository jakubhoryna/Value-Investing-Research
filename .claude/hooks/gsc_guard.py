#!/usr/bin/env python3
"""GSC routine guard: PreToolUse hook (MODEL §8.7, spec v2 §5).

Runs only when GSC_SESSION=routine. Any other value: exit 0 at once, nothing
is read or checked. settings.json gates in the shell as well, so attended
sessions never even start Python.

In routine sessions it blocks (exit 2, one stderr line):
  * Edit/Write/NotebookEdit into framework-locked paths;
  * Bash/Monitor commands that push anything but the run's own claude/gsc-*
    branch, merge or rewrite history, call gh outside the REST allowlist,
    handle tokens, or visibly write into locked paths.
Any unexpected error also exits 2 (fail closed).

Python 3.11 stdlib only, no network. At most one subprocess per call
(`git symbolic-ref`, only for `git push`). This is a guard rail, not a
sandbox: gsc_guard_post.py self-heals locked files after each tool call and
the gsc-guard PR check is the visible second layer.
"""
import glob
import json
import os
import re
import shlex
import subprocess
import sys

# ---------------------------------------------------------------- constants

REPO = "jakubhoryna/Value-Investing-Model"
# Preflight self-test (routines/README §0): always refused, harmless when the guard is off.
CANARY = ": gsc-guard-canary"
LOCKED_DIRS = ("model", "routines", ".claude", ".github")
LOCKED_NAMES = ("CLAUDE.md", "CLAUDE.local.md", "AGENTS.md")

# Strict run-branch name (spec §1).
BRANCH_RE = re.compile(
    r"^claude/gsc-(analyse|review|seed|sweep|intake)-(?:(?P<key>[A-Za-z0-9._-]+)-)?"
    r"(?P<date>\d{4}-\d{2}-\d{2})-(?P<time>\d{4})$")

# Command wrappers skipped before the real program. Value = options taking an argument.
WRAPPERS = {
    "sudo": {"-u", "-g", "-C", "-h", "-p"}, "env": {"-u", "-C", "-S"},
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
    "clone": "routines work in their own checkout", "daemon": "not needed",
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
LOCKED_FRAG_RE = re.compile(r"model/|routines/|\.claude|\.github|CLAUDE\.md|CLAUDE\.local\.md|"
                            r"AGENTS\.md|settings\.local\.json|disableAllHooks")
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

    # ---- entry point

    def run(self):
        tool = self.event.get("tool_name", "")
        ti = self.event.get("tool_input") or {}
        if not isinstance(ti, dict):
            block("tool input is not an object")
        if tool in ("Edit", "Write", "NotebookEdit", "MultiEdit"):
            target = ti.get("file_path") or ti.get("notebook_path") or ""
            if not isinstance(target, str):
                block("file path is not a string")
            hit = self.locked(target, self.cwd)
            if hit:
                block(f"'{hit}' is framework-locked")
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
            if re.search(r"/\.claude/settings[^/]*\.json$|/\.claude\.json$|"
                         r"/etc/claude-code/|/Library/Application Support/ClaudeCode/", fwd, re.I):
                return full
            return None
        if rel == ".":
            return "the repo root" if whole else None
        parts = rel.split("/")
        # .git/ too: a file written there (hooks, config) makes git run arbitrary code.
        if parts[0].lower() in {d.lower() for d in LOCKED_DIRS} | {".git"}:
            return rel
        if parts[-1].lower() in {n.lower() for n in LOCKED_NAMES}:
            return rel
        return None

    def need_unlocked(self, paths, base, what, whole=False):
        for p in paths:
            hit = self.locked(p, base, whole)
            if hit:
                block(f"{what} on '{hit}' (framework-locked)")

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
            if target:
                self.check_dest(target, pos, base, prog)
            elif len(pos) >= 2:
                self.check_dest(pos[-1], pos[:-1], base, prog)
        elif prog == "mv":
            sources = pos if target else pos[:-1]
            self.need_unlocked(sources, base, "mv", whole=True)
            dest = target or (pos[-1] if len(pos) >= 2 else None)
            if dest:
                self.check_dest(dest, sources, base, "mv")
        elif prog in ("rm", "rmdir", "unlink", "shred", "chmod", "chown", "chgrp"):
            self.need_unlocked(pos, base, prog, whole=True)
        elif prog in ("touch", "mkdir", "truncate", "ln", "tee"):
            self.need_unlocked(pos + ([target] if target else []), base, prog)
        elif prog == "dd":
            self.need_unlocked([a[3:] for a in args if a.startswith("of=")], base, "dd")
        elif prog == "sed":
            if any(re.match(r"^-[A-Za-z]*i", a) or a.startswith("--in-place") for a in args):
                # Without -e/-f the first positional is the sed script, not a file.
                scripted = any(a in ("-e", "-f") or a.startswith(("--expression", "--file"))
                               for a in args)
                self.need_unlocked(pos if scripted else pos[1:], base, "sed -i")
        elif prog == "perl":
            if any(re.match(r"^-[A-Za-z]*i", a) for a in args):
                self.need_unlocked(pos, base, "perl -i")
        elif prog in ("awk", "gawk"):
            joined = " ".join(args)
            if re.search(r"(^|\s)(-i\s*inplace|--include[= ]inplace)", joined):
                self.need_unlocked(pos, base, f"{prog} -i inplace")
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

    # ---- interpreters

    def check_code(self, code, net=True):
        """Interpreter code. net=False for shell code, which check_command parses properly."""
        if LOCKED_FRAG_RE.search(code) and WRITE_IND_RE.search(code):
            frag = LOCKED_FRAG_RE.search(code).group(0)
            block(f"script code writes and names a locked path ('{frag}'); routines never change locked files")
        if net and (CODE_PUSH_RE.search(code) or CODE_GHAPI_RE.search(code)):
            block("script code mentions git push / gh api; routine scripts never talk to GitHub "
                  "(run git and gh commands directly)")

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
        codes, script, stdin, module, i = [], None, False, False, 0
        while i < len(args):
            a = args[i]
            nxt = args[i + 1] if i + 1 < len(args) else ""
            if a == "-":
                stdin = True
                break
            if prog.startswith("python"):
                if a == "-c":
                    codes.append(nxt)
                    break
                if a == "-m":
                    module = True
                    break
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
            self.check_script(script, base, shell, depth)
        if not codes and not script and not module:
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
            "remote": self.git_remote, "lfs": self.git_lfs,
        }.get(sub)
        if handler:
            handler(sub, rest, gitcwd)

    def git_push(self, sub, rest, gitcwd):
        if rel_to(gitcwd, self.root) is None:
            block("git push is allowed only inside the repo checkout")
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
        cur = self.current_branch()
        if not BRANCH_RE.match(cur):
            block(f"current branch is '{cur or 'detached HEAD'}', not a claude/gsc-… run branch; never push main")
        if dest != "HEAD" and dest != cur:
            block(f"push destination '{dest}' is not the current branch '{cur}'")

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

    def git_switch(self, sub, rest, gitcwd):
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
        if len(pos) == 1 and (BRANCH_RE.match(pos[0]) or pos[0] in ("main", "origin/main")):
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

    def git_rm_mv(self, sub, rest, gitcwd):
        if any(a.startswith("--pathspec-from-file") for a in rest):
            block(f"git {sub} --pathspec-from-file is not allowed")
        k = rest.index("--") if "--" in rest else len(rest)
        paths = [a for a in rest[:k] if not a.startswith("-")] + rest[k + 1:]
        self.git_paths(paths, gitcwd, f"git {sub}")

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
            return
        if method == "PATCH" and re.fullmatch(repo + r"/pulls/" + num, ep, re.I):
            extra = set(kv) - {"title", "body", "state"}
            if extra:
                block(f"PR PATCH of {sorted(extra)} is not allowed (title, body, state=closed only)")
            if "state" in kv and kv["state"] != "closed":
                block("PR PATCH may only set state=closed")
            return
        if method == "POST" and re.fullmatch(repo + r"/issues/" + num + r"/comments", ep, re.I):
            extra = set(kv) - {"body"}
            if extra:
                block(f"comment with fields {sorted(extra)} is not allowed")
            return
        block(f"gh api {method} {short(ep, 70)} is not on the routine allowlist "
              f"(never merge, contents, git refs, graphql or other repos)")

    # ---- curl / wget

    def check_http(self, prog, args):
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
