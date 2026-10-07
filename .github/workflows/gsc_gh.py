#!/usr/bin/env python3
"""GitHub REST helper for gsc-automerge and gsc-notify (MODEL v4.5.0 §8.7
items 10-11), with an endpoint allowlist checked before any I/O.

The token is the per-run GITHUB_TOKEN that the workflow passes as env
GH_TOKEN (`GH_TOKEN: ${{ github.token }}`). GitHub mints it for the run and
expires it afterwards; it is never printed, logged or written: errors name
only the HTTP status, method and path.

Allowlist (paths relative to repos/{REPO}/; anything else raises NotAllowed):
  GET    pulls?…, pulls/{n}, issues?…, issues/{n}, issues/{n}/comments?…,
         actions/workflows/{gsc-guard|gsc-automerge|gsc-notify}.yml/runs?…,
         actions/runs?…, actions/runs/{id}, actions/runs/{id}/jobs?…
  POST   issues                      fields ⊆ {title, body, assignees}; title is
                                     'GSC - needs Jakub' or a digest title
         issues/{n}/comments         only the verified 'GSC - needs Jakub' issue
         actions/runs/{id}/rerun     only with allow_actions (gsc-notify maintenance)
         actions/workflows/gsc-automerge.yml/dispatches   {ref: main}, allow_actions
  PATCH  issues/{n}                  exactly {state: closed, state_reason: completed},
                                     only a verified digest issue
  PUT    pulls/{n}/merge             exactly {merge_method: squash, sha, commit_title},
                                     only with allow_merge (gsc-automerge)
Never: labels, assignees endpoints, requested_reviewers, reviews, any PATCH of a
pull request, git/, contents/, graphql, or a comment on a pull request.

Python 3.11+ standard library only. Tests: test_gsc_automerge.py and
test_gsc_notify.py use a fake transport (no network).
"""
import datetime
import json
import re
import urllib.error
import urllib.request

API = "https://api.github.com/"
OWNER = "jakubhoryna"
BOT = "github-actions[bot]"
NEEDS_TITLE = "GSC - needs Jakub"
DIGEST_TITLE_RE = re.compile(r"^(STALL - )?GSC digest ")
NEEDS_BODY = ("@jakubhoryna Standing issue. gsc-automerge posts one comment here for each routine PR "
              "it holds for you, with the reason and a link; gsc-notify posts here when a guard run "
              "never ran or a workflow failed. Pin this issue (once, by hand). Do not close it.")

# Query strings: no '/', '#' or whitespace, so a query can never smuggle a path.
_Q = r"(?:\?[^/#\s]*)?"
_GET_RULES = [re.compile(p) for p in (
    r"pulls" + _Q,
    r"pulls/\d+",
    r"issues" + _Q,
    r"issues/\d+",
    r"issues/\d+/comments" + _Q,
    r"actions/workflows/gsc-(?:guard|automerge|notify)\.yml/runs" + _Q,
    r"actions/runs" + _Q,
    r"actions/runs/\d+",
    r"actions/runs/\d+/jobs" + _Q,
)]
_FORBIDDEN_RE = re.compile(r"labels|assignees|requested_reviewers|reviews|(^|/)git/|(^|/)contents/|graphql",
                           re.I)


class NotAllowed(Exception):
    """A request outside the allowlist; raised before any I/O."""


class GhError(Exception):
    """An HTTP error from GitHub (status >= 400). Carries no token."""

    def __init__(self, status, method, path, message=""):
        super().__init__("GitHub %s %s -> HTTP %s %s" % (method, path, status, message))
        self.status = status
        self.method = method
        self.path = path
        self.message = message


def default_transport(method, url, headers, body):
    """(status, headers, body bytes) for one HTTPS request."""
    req = urllib.request.Request(url, data=body, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, dict(resp.headers.items()), resp.read()
    except urllib.error.HTTPError as exc:
        return exc.code, dict((exc.headers or {}).items()), exc.read() or b""


def _next_link(headers):
    """The rel="next" URL of a Link header, or None."""
    link = ""
    for name, value in (headers or {}).items():
        if name.lower() == "link":
            link = value
    for part in link.split(","):
        m = re.match(r'\s*<([^>]+)>\s*;\s*rel="next"', part)
        if m:
            return m.group(1)
    return None


class Gh:
    """REST client restricted to the allowlist above."""

    def __init__(self, token, repo, transport=None, allow_merge=False, allow_actions=False):
        if not repo or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
            raise NotAllowed("repository %r is not owner/name" % (repo,))
        self.token = token or ""
        self.repo = repo
        self.prefix = "repos/%s/" % repo
        self.transport = transport or default_transport
        self.allow_merge = allow_merge
        self.allow_actions = allow_actions
        self.needs_issue = None      # set only by verify_needs_issue()
        self.closable = set()        # digest issues verified by verify_digest()

    # ---- allowlist

    def check(self, method, rel, fields):
        """Raise NotAllowed unless (method, rel, fields) is on the allowlist."""
        fields = fields or {}
        if not isinstance(rel, str) or rel.startswith("/") or ".." in rel or _FORBIDDEN_RE.search(rel):
            raise NotAllowed("%s %s is never allowed" % (method, rel))
        path = rel.split("?", 1)[0]
        if method == "GET":
            if fields or not any(r.fullmatch(rel) for r in _GET_RULES):
                raise NotAllowed("GET %s is not on the allowlist" % rel)
            return
        if "?" in rel:
            raise NotAllowed("%s %s: no query string on a write" % (method, rel))
        if method == "POST" and path == "issues":
            if not set(fields) <= {"title", "body", "assignees"} or "title" not in fields:
                raise NotAllowed("POST issues with fields %s" % sorted(fields))
            if fields["title"] != NEEDS_TITLE and not DIGEST_TITLE_RE.match(str(fields["title"])):
                raise NotAllowed("POST issues: only the needs-Jakub issue or a digest")
            if fields.get("assignees") not in (None, [OWNER]):
                raise NotAllowed("POST issues: assignee may only be %s" % OWNER)
            return
        m = re.fullmatch(r"issues/(\d+)/comments", path)
        if method == "POST" and m:
            if self.needs_issue is None or int(m.group(1)) != self.needs_issue:
                raise NotAllowed("comments go only to the verified 'GSC - needs Jakub' issue")
            if set(fields) != {"body"}:
                raise NotAllowed("comment fields %s" % sorted(fields))
            return
        if method == "POST" and re.fullmatch(r"actions/runs/\d+/rerun", path):
            if not self.allow_actions or fields:
                raise NotAllowed("re-runs are gsc-notify maintenance only")
            return
        if method == "POST" and path == "actions/workflows/gsc-automerge.yml/dispatches":
            if not self.allow_actions or fields != {"ref": "main"}:
                raise NotAllowed("dispatch of gsc-automerge on main only, maintenance only")
            return
        m = re.fullmatch(r"issues/(\d+)", path)
        if method == "PATCH" and m:
            if int(m.group(1)) not in self.closable:
                raise NotAllowed("PATCH issues/%s: not a verified digest issue" % m.group(1))
            if fields != {"state": "closed", "state_reason": "completed"}:
                raise NotAllowed("PATCH issues: only state=closed, state_reason=completed")
            return
        m = re.fullmatch(r"pulls/(\d+)/merge", path)
        if method == "PUT" and m:
            if not self.allow_merge:
                raise NotAllowed("only gsc-automerge merges")
            if set(fields) != {"merge_method", "sha", "commit_title"} or fields["merge_method"] != "squash" \
                    or not re.fullmatch(r"[0-9a-f]{40}", str(fields["sha"])):
                raise NotAllowed("merge fields must be exactly squash, a 40-hex sha and a commit title")
            return
        raise NotAllowed("%s %s is not on the allowlist" % (method, rel))

    # ---- I/O

    def request(self, method, rel, fields=None):
        """(json or None, headers) for one call; raises NotAllowed or GhError."""
        method = method.upper()
        self.check(method, rel, fields)
        body = json.dumps(fields).encode("utf-8") if fields is not None and method != "GET" else None
        return self._send(method, API + self.prefix + rel, rel, body)

    def _send(self, method, url, rel, body):
        headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28",
                   "User-Agent": "gsc-automation"}
        if self.token:
            headers["Authorization"] = "Bearer " + self.token
        if body is not None:
            headers["Content-Type"] = "application/json"
        status, resp_headers, data = self.transport(method, url, headers, body)
        payload = None
        if data:
            try:
                payload = json.loads(data.decode("utf-8"))
            except (ValueError, UnicodeDecodeError):
                payload = None
        if status >= 400:
            message = payload.get("message", "") if isinstance(payload, dict) else ""
            raise GhError(status, method, rel.split("?", 1)[0], str(message)[:200])
        return payload, resp_headers

    def get(self, rel):
        return self.request("GET", rel)[0]

    def get_all(self, rel, key=None, limit=40):
        """Every page of a list endpoint (Link rel="next"); `key` names the
        list inside an object payload (e.g. 'workflow_runs')."""
        items = []
        payload, headers = self.request("GET", rel)
        pages = 1
        while True:
            chunk = payload.get(key, []) if key and isinstance(payload, dict) else payload
            items.extend(chunk or [])
            url = _next_link(headers)
            if not url or pages >= limit:
                return items
            if not url.startswith(API + self.prefix):
                raise NotAllowed("pagination left the repository")
            nxt = url[len(API + self.prefix):]
            self.check("GET", nxt, None)
            payload, headers = self._send("GET", url, nxt, None)
            pages += 1

    # ---- verified targets

    def verify_needs_issue(self, number):
        """True and remember `number` when it is the open 'GSC - needs Jakub'
        issue created by github-actions[bot] (not a pull request)."""
        issue = self.get("issues/%d" % int(number))
        ok = (isinstance(issue, dict) and "pull_request" not in issue and issue.get("state") == "open"
              and (issue.get("user") or {}).get("login") == BOT and issue.get("title") == NEEDS_TITLE)
        self.needs_issue = int(number) if ok else None
        return ok

    def verify_digest(self, number):
        issue = self.get("issues/%d" % int(number))
        ok = (isinstance(issue, dict) and "pull_request" not in issue
              and (issue.get("user") or {}).get("login") == BOT
              and bool(DIGEST_TITLE_RE.match(issue.get("title") or "")))
        if ok:
            self.closable.add(int(number))
        return ok

    def close_digest(self, number):
        if not self.verify_digest(number):
            raise NotAllowed("issue %s is not a digest" % number)
        return self.request("PATCH", "issues/%d" % int(number),
                            {"state": "closed", "state_reason": "completed"})[0]

    def merge(self, number, sha, title):
        return self.request("PUT", "pulls/%d/merge" % int(number),
                            {"merge_method": "squash", "sha": sha, "commit_title": title})[0]


# ---------------------------------------------------------------- shared helpers

def is_issue(item):
    return isinstance(item, dict) and "pull_request" not in item


def find_needs_issue(gh):
    """Number of the open 'GSC - needs Jakub' issue, or None."""
    issues = gh.get_all("issues?state=open&creator=github-actions%5Bbot%5D&per_page=100")
    for issue in sorted(issues, key=lambda i: i.get("number", 0)):
        if is_issue(issue) and issue.get("title") == NEEDS_TITLE and (issue.get("user") or {}).get("login") == BOT:
            return issue["number"]
    return None


def ensure_needs_issue(gh, create=True):
    """The verified needs-Jakub issue number, created once when absent."""
    number = find_needs_issue(gh)
    if number is None and create:
        created = gh.request("POST", "issues", {"title": NEEDS_TITLE, "body": NEEDS_BODY,
                                                "assignees": [OWNER]})[0]
        number = created["number"]
    if number is None or not gh.verify_needs_issue(number):
        raise NotAllowed("no verifiable 'GSC - needs Jakub' issue")
    return number


def post_needs_comment(gh, body, marker, since):
    """Post `body` on the needs-Jakub issue unless a comment carrying `marker`
    exists among those updated since `since` (ISO time). Returns True when
    posted. The body never names an open PR as '#n' (callers write 'PR n')."""
    number = ensure_needs_issue(gh)
    query = "issues/%d/comments?per_page=100" % number
    if since:
        query += "&since=" + since
    for comment in gh.get_all(query):
        if marker in (comment.get("body") or ""):
            return False
    gh.request("POST", "issues/%d/comments" % number, {"body": body})
    return True


def routine_kind(pr):
    """'routine' for a well-formed routine PR, 'mismatch' for a claude/gsc…
    branch whose name or title is off (held for Jakub), None to ignore
    (attended branches, forks, other bases)."""
    from gsc_guard_check import BRANCH_RE, TITLE_RE   # sibling module, trusted default branch
    head = pr.get("head") or {}
    base = pr.get("base") or {}
    ref = head.get("ref") or ""
    if base.get("ref") != "main" or not ref.startswith("claude/gsc"):
        return None
    head_repo = (head.get("repo") or {}).get("full_name")
    base_repo = (base.get("repo") or {}).get("full_name")
    if not head_repo or head_repo != base_repo:
        return None
    if BRANCH_RE.fullmatch(ref) and TITLE_RE.match(pr.get("title") or ""):
        return "routine"
    return "mismatch"


def search_link(repo, number, state="open"):
    """A search link that finds PR n (open, or closed with state='closed')
    without naming it as #n: a direct PR link or #n in an issue may wake the
    routine session watching it (V4, unchecked)."""
    return "https://github.com/%s/pulls?q=is%%3Apr+is%%3A%s+%d" % (
        repo, "closed" if state == "closed" else "open", int(number))


def commit_link(repo, sha):
    """A link to a commit on main (never to the PR it came from, V4)."""
    return "https://github.com/%s/commit/%s" % (repo, sha)


def blob_link(repo, sha, path):
    """A permalink to a file at a commit."""
    return "https://github.com/%s/blob/%s/%s" % (repo, sha, path)


def no_hash_ref(text):
    """'#12' -> '# 12', so GitHub never cross-references a PR from a comment
    or an issue body. URLs written by gsc-notify carry no '#<digit>'."""
    return re.sub(r"#(?=\d)", "# ", str(text))


# ---------------------------------------------------------------- Europe/Prague

def _last_sunday(year, month):
    day = datetime.date(year, month, 31)
    return day - datetime.timedelta(days=(day.weekday() + 1) % 7)


class EuropePrague(datetime.tzinfo):
    """CET/CEST under the EU rule (summer time from the last Sunday of March to
    the last Sunday of October, switching at 01:00 UTC). Used only where the
    system has no time-zone database (a Windows test run); the Ubuntu runner
    uses zoneinfo."""

    _HOUR = datetime.timedelta(hours=1)

    def _bounds(self, year):
        return (datetime.datetime.combine(_last_sunday(year, 3), datetime.time(1)),
                datetime.datetime.combine(_last_sunday(year, 10), datetime.time(1)))

    def dst(self, dt):
        if dt is None:
            return datetime.timedelta(0)
        start, end = self._bounds(dt.year)
        local = dt.replace(tzinfo=None)
        start_local, end_local = start + self._HOUR, end + 2 * self._HOUR   # 02:00 CET, 03:00 CEST
        if start_local <= local < end_local - self._HOUR:
            return self._HOUR
        if end_local - self._HOUR <= local < end_local:                   # the repeated hour
            return datetime.timedelta(0) if dt.fold else self._HOUR
        return datetime.timedelta(0)

    def utcoffset(self, dt):
        return self._HOUR + self.dst(dt)

    def tzname(self, dt):
        return "CEST" if self.dst(dt) else "CET"

    def fromutc(self, dt):
        utc = dt.replace(tzinfo=None)
        start, end = self._bounds(utc.year)
        summer = start <= utc < end
        local = utc + (2 if summer else 1) * self._HOUR
        fold = 1 if (not summer and end <= utc < end + self._HOUR) else 0
        return local.replace(tzinfo=self, fold=fold)


def prague_tz():
    """Europe/Prague from the system tz database, else the EU-rule fallback."""
    try:
        from zoneinfo import ZoneInfo
        return ZoneInfo("Europe/Prague")
    except Exception:
        return EuropePrague()
