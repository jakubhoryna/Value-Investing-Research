# WEEKLY routine — the weekly report (MODEL §7.4 and §8.7 item 11)

**Schedule:** Sunday at 09:10 Europe/Prague, after the weekly usage reset at 09:00 and the weekend sprint (its last fires are at 07:40); catch-ups Sunday at 21:40 and Monday at 06:40.
Weekdays 09:00–18:00 are routine-free and 02:00–06:00 is quiet outside the weekend sprint. These times must equal the live routine crons (MODEL §8.7 item 12): `CRON_TZ=Europe/Prague 10 9 * * 0`, `CRON_TZ=Europe/Prague 40 21 * * 0` and `CRON_TZ=Europe/Prague 40 6 * * 1`. A run that cannot start (a usage limit, a failed fire) sends nothing: no WEEKLY push by Monday 07:00 means the report did not run.
**Branch:** `claude/gsc-weekly-{D}-{T}`, local only, never pushed. **PR title:** none — WEEKLY opens no PR.

WEEKLY tells Jakub once a week what the system did and what waits for him. It replaces the morning digest and every per-event push except BUY (MODEL §8.7 item 11). It renders the weekly report with `routines/tools/gsc_weekly.py`, publishes it to the one private weekly page (`weekly_page` in `CLAUDE.md`, MODEL §7.4) and sends one push. **It writes nothing to the repository:** no commit, no push, no PR, no comment, no run note. The local branch only tells the guard hook which job is running. A run that finds its week already published stops at once without a push, so a catch-up after a good Sunday run costs two reads.

Run every command from the repository root. Write every file you author under `/tmp/gsc-weekly/` with the Write tool. `{RUN}`, `{SINCE}`, `{UNTIL}`, `{PERIOD}` and `{DETAILS_SINCE}` are fixed in steps 1 and 2; write them out literally in later commands (shell variables don't survive between tool calls).

1. **Preflight** per `routines/README.md` §0, steps 1–3, 5 and 6. Step 4, the ledger, is replaced by step 4 below: WEEKLY claims nothing.
   - At §0 step 5 also fix the run start, once: `TZ=Europe/Prague date +%FT%T%:z` (e.g. `2026-10-25T08:41:07+01:00`). That is `{RUN}`.
   - Then `git fetch origin main && git switch --no-track -c "claude/gsc-weekly-{D}-{T}" origin/main`. The branch is never pushed. On it the guard hook refuses every push, every GitHub call but a GET, any edit inside the repository, `git add` and `git commit`, and any later branch switch.
   - Then `rm -rf /tmp/gsc-weekly && mkdir -p /tmp/gsc-weekly/fetch`.

   On any failure: publish nothing, send the not-published push (step 9) if the branch exists, and end with a session summary that names the failed step. Without the branch the guard refuses the push: end with the summary only.
2. **Window.** `python3 routines/tools/gsc_weekly.py window --at "{RUN}"` prints one JSON object:
   - `since` and `until`: the seven Prague days ending at the most recent Sunday 08:30 Europe/Prague at or before `{RUN}`. They are computed in Prague local time, so a week with a DST change lasts 167 or 169 hours. Every catch-up of the same week prints the same window. A sprint PR that merges after 08:30, or is still running when step 4 reads it, lands in the next week's report.
   - `period`: the window's label, e.g. `Sun 18 Oct – Sun 25 Oct 2026`.
   - `details_since`: `since` minus 14 days, in UTC (`2026-10-04T06:30:00Z`).

   Write the four values down as `{SINCE}`, `{UNTIL}`, `{PERIOD}` and `{DETAILS_SINCE}`.
3. **Already published?**
   - Read the page once: Artifact `action: "read"`, `url: "https://claude.ai/artifact/6L264JT8pg5vuia9dUrcuj"`, nothing else. The Artifact tool requires this read before the step-8 uploads.
   - ArtifactData `action: "get"`, the same `url`, `collection: "datasets"`, `doc_id: "meta"`, nothing else.
   - `python3 routines/tools/gsc_weekly.py window --at "{RUN}" --meta-at "{updated.at}" --meta-by "{updated.by}"`, with the two values from the `meta` document's `updated` field (`-` when a value is missing). It adds `published: true` when `updated.by` is `GSC WEEKLY routine` and `updated.at` lies between `{UNTIL}` and five minutes after `{RUN}`. A stamp after the run never counts, so a wrong stamp is overwritten by the next run instead of silencing every later week.
   - Published → stop now: no push, and a one-line session summary.
   - A missing Artifact or ArtifactData tool, or a failed read → stop with the not-published push (step 9).
4. **Fetch.** GitHub reads, every one a `gh api` GET, page by page, into `/tmp/gsc-weekly/fetch/`. Never use `--paginate`: it follows GitHub's `Link` URL, which the cloud proxy refuses from page 2 on (README §1). Run each command exactly as written, with `{DETAILS_SINCE}` filled in. Any failure → stop with the not-published push.

   ```
   # every PR, all pages
   p=1; while :; do gh api "repos/jakubhoryna/Value-Investing-Model/pulls?state=all&per_page=100&sort=updated&direction=desc&page=$p" > "/tmp/gsc-weekly/fetch/pulls_$p.json" || exit 1; n=$(jq length "/tmp/gsc-weekly/fetch/pulls_$p.json") || exit 1; [ "$n" -lt 100 ] && break; p=$((p+1)); done
   # merged_by (gsc-automerge or Jakub) for every PR merged and updated since DETAILS_SINCE
   ns=$(jq -r --arg c "{DETAILS_SINCE}" '.[] | select(.merged_at != null and .updated_at >= $c) | .number' /tmp/gsc-weekly/fetch/pulls_*.json) || exit 1; for n in $ns; do gh api "repos/jakubhoryna/Value-Investing-Model/pulls/$n" > "/tmp/gsc-weekly/fetch/pull_$n.json" || exit 1; done
   # the issues the workflows opened (GSC - needs Jakub; the retired digests), all pages
   p=1; while :; do gh api "repos/jakubhoryna/Value-Investing-Model/issues?state=all&creator=github-actions%5Bbot%5D&per_page=100&page=$p" > "/tmp/gsc-weekly/fetch/issues_$p.json" || exit 1; n=$(jq length "/tmp/gsc-weekly/fetch/issues_$p.json") || exit 1; [ "$n" -lt 100 ] && break; p=$((p+1)); done
   # the workflows' records on GSC - needs Jakub since DETAILS_SINCE: hold reasons and failures (read only; never post)
   i=$(jq -rs 'add | map(select(.pull_request == null and .title == "GSC - needs Jakub")) | .[0].number // empty' /tmp/gsc-weekly/fetch/issues_*.json) || exit 1; [ -n "$i" ] || exit 0; p=1; while :; do gh api "repos/jakubhoryna/Value-Investing-Model/issues/$i/comments?since={DETAILS_SINCE}&per_page=100&page=$p" > "/tmp/gsc-weekly/fetch/comments_$p.json" || exit 1; n=$(jq length "/tmp/gsc-weekly/fetch/comments_$p.json") || exit 1; [ "$n" -lt 100 ] && break; p=$((p+1)); done
   ```
5. **Schedule health (optional).** This step runs only if the session has the read-only `list_triggers` tool.
   - Call it until no `next_cursor` is left.
   - Write `/tmp/gsc-weekly/health.json` with the Write tool. It is a JSON array with one object per Routine whose prompt begins `GSC ROUTINE:`: `name`, `job` (the word after `GSC ROUTINE:`), `cron` (as listed, with its `CRON_TZ=` prefix), `enabled`, `sprint` (true when the name contains "sprint", in any case) and `last_run` (`{"status": …, "fired_at": …, "finished_at": …, "failure_reason": …}`, or `null`). Copy every value from the result and infer nothing.
   - Never call any other trigger or session tool.
   - No tool, or an error → write no file. The report then shows schedule health as n/a. A file the tool cannot read is reported under Fix and never stops the render.
6. **Render** (offline: git reads, the files at `origin/main`, the fetched pages):

   `python3 routines/tools/gsc_weekly.py render --repo-dir . --ref origin/main --since "{SINCE}" --until "{UNTIL}" --fetch-dir /tmp/gsc-weekly/fetch --health-json /tmp/gsc-weekly/health.json --out-dir /tmp/gsc-weekly`

   Leave out `--health-json …` when step 5 wrote no file. The tool writes:
   - one dataset file per dataset id: `/tmp/gsc-weekly/summary.json` (the tool's own six sentences), `meta.json`, `kpis.json`, `attention.json`, `shortlist.json`, `changes.json`, `weekly.json`, `pipeline.json`, `coverage.json`, `backlog.json` and `held.json`;
   - `/tmp/gsc-weekly/notification.txt`, the one-line push (step 9).

   Exit 0, or stop with the not-published push (reason: the first line of its error). It refuses an incomplete fetch: a PR merged in the last two weeks without its `pull_{n}.json`, or the `GSC - needs Jakub` issue without a comments page. Never edit a dataset file.
7. **Summary.**
   - Read `attention.json`, `kpis.json`, `held.json`, `changes.json` and `backlog.json`.
   - Write exactly six plain sentences, one per slot of the page, to `/tmp/gsc-weekly/summary_draft.json` with the Write tool, as a JSON array of `{"order": n, "kind": …, "text": "…"}`, `order` 1 to 6 and `kind` in the page's slot order: `takeaway`, `decide`, `fix`, `fix`, `know`, `know`. A slot with nothing to say says so in plain words.
   - Each text is one line of at most 300 characters with no `#`. Copy every number, date, key and PR number exactly as the datasets print it, and write a PR as `PR n`.
   - Say what happened and what waits for Jakub. Give no advice, no buy or sell language and no price target: a zone or a flag is framework output (`CLAUDE.md`).
   - Then run `python3 routines/tools/gsc_weekly.py lint-summary --datasets /tmp/gsc-weekly --in /tmp/gsc-weekly/summary_draft.json --apply`. It checks the rules above, that every number in a text appears in the other datasets, and that the takeaway's headline figures (memos merged, new WATCH, IN RANGE, NEAR, WATCH) equal the `kpis` values.
   - Exit 0 → it has replaced `summary.json` with your sentences. Any other exit → it leaves the tool's own `summary.json` in place. Keep that file, put the lint lines in the session summary and go on: a failed lint never stops the run.
8. **Publish.** Only the weekly page, and only its `datasets` collection (MODEL §7.4).
   1. **Upload** each of the eleven step-6 dataset files, in the order listed there, as an asset of the page: Artifact `action: "publish"`, `url: "https://claude.ai/artifact/6L264JT8pg5vuia9dUrcuj"`, `asset: true`, `file_path: "/tmp/gsc-weekly/{id}.json"`, nothing else. Each result gives that file's url, `/_blob/` plus 32 hex characters. Write the eleven urls, exactly as returned, to `/tmp/gsc-weekly/blobs.json` with the Write tool: `{"summary": "/_blob/…", "meta": "/_blob/…", …}`.
   2. **Versions.** ArtifactData `action: "list"`, the same `url`, `collection: "datasets"`, nothing else. Write each dataset document's `version` to `/tmp/gsc-weekly/versions.json` with the Write tool: `{"summary": 7, …}`.
   3. **Build the batch:** `python3 routines/tools/gsc_weekly.py dash-writes --datasets /tmp/gsc-weekly --blobs /tmp/gsc-weekly/blobs.json --versions /tmp/gsc-weekly/versions.json --at "{RUN}" --out /tmp/gsc-weekly/writes.json`.
      - It checks the eleven urls (their form, all distinct), the eleven versions and that `{RUN}` is not after the clock, and prints the batch.
      - It writes one `update` per dataset, pinned with `if_version`, with `meta` last. Each `data` is `{"source": {"kind": "file", "url": …, "name": "{id}.json", "format": "json"}, "updated": {"at": "{RUN}", "by": "GSC WEEKLY routine"}}`.
   4. **Apply:** one ArtifactData `action: "batch"` on the same `url`. Its `writes` is the array the tool printed, copied exactly, with each `data` inline and never as `file_path`. Every entry is pinned, so the batch applies all or nothing.
      - Refused because a document's version moved → redo sub-steps 2–4 once.
      - A second refusal, or any other failure in this step → stop with the not-published push. Uploaded assets left unreferenced are harmless.

   Never write the page's `files/` or `dash/` documents, or a dataset's `title`, `description` or `fixed`. Never use `set`, `delete` or `str_replace`. The guard hook refuses each of these.
9. **Push.** Send exactly one `PushNotification` (README §5):
   - Published → the line in `/tmp/gsc-weekly/notification.txt`, unedited: `GSC WEEKLY · {PERIOD} · {d} to decide · {f} to fix · {m} memos · https://claude.ai/artifact/6L264JT8pg5vuia9dUrcuj`.
   - Not published (a failure in preflight after the branch exists, or in steps 2, 3, 4, 6 or 8) → `GSC WEEKLY · not published · {step}: {first error line}`, shortened to fit.

   Either way: one line, at most 200 characters, no `#`. A push that the app reports as not sent is not retried. A run that stopped in step 3 because the week was already published sends no push.

   End with a session summary: the period, published or not, the lint result and the Decide, Fix and Know counts.

**Budget.** No research. The only network calls are the step-4 `gh api` GETs and the weekly page's Artifact and ArtifactData calls (P14: none). About 30 minutes; past that, stop with the not-published push.

**Forbidden:**
- any repository write: Edit or Write inside the repo, `git add`, `git commit`, `git push` (the branch stays local), a run note; any branch switch after step 1
- opening, editing or closing a PR or issue, and any comment
- any `gh api` method but GET, `--paginate`, and any other GitHub client
- any Artifact action other than step 3's `read` and step 8's asset uploads of the eleven dataset files; any other artifact url
- any ArtifactData action other than step 3's `get` and step 8's `list` on `datasets` and its one `batch`; `as_level`; `out_dir`
- any MCP tool other than the read-only `list_triggers` (the guard hook refuses every other one, and refuses `list_triggers` outside WEEKLY)
- editing a rendered dataset file (only `lint-summary --apply` replaces `summary.json`)
- advice, buy or sell language and price targets; cost basis, position size or core numbers in anything you write

*Framework output, not investment advice.*
