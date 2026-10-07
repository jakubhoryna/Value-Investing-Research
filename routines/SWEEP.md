# SWEEP routine — weekly price screen (MODEL §8.3 under §8.7)

**Schedule:** Saturday at 06:30 Europe/Prague, after the Friday close.
Weekdays 09:00–18:00 are routine-free and 02:00–06:00 is quiet outside the weekend sprint. These times must equal the live routine crons (MODEL §8.7 item 12).
**Branch:** `claude/gsc-sweep-{D}-{T}`. **PR title:** `GSC SWEEP {D} [running]`.

SWEEP never writes the register. It writes one row file. INTAKE applies that file as the §8.3 step-5 price refresh after the PR merges: it takes each Px and its close date and recomputes MCap/FCF and EV/OI, and their 3-year and 5-year readings, from the `register.csv` core numbers (MODEL §7.1b) with `routines/tools/gsc_register.py`.

1. **Preflight** per `routines/README.md` §0. If an open `GSC SWEEP` PR exists, the previous sweep hasn't been merged: stop with no PR.
2. **Claim:** open the branch and the PR (README §2).
3. **Held names first, always, regardless of verdict** (§8.3 step 1). For each name:
   - Get the current price (step 5 rules).
   - Compute both primaries and the distances: `python3 routines/tools/gsc_register.py metrics {KEY} {PX}` (add `--fx {RATE}` when step 5 fetched a fresher rate for the name's pair). `metrics` prints both primaries, the 3-year and 5-year readings, the distances, and, for a held name, `trigger = ADD band`. Never compute them by hand. Holding credits are a constant (MODEL §7.1b, V14): no holding's own price enters, and there is no holding price check.
   - **Held ADD (MODEL P21, R10).** A held name is ADD at or under its ADD band, which is its trigger: the no-cash bound, the strict line. SELL-FLAG is unaffected.
   - Build the portfolio table, one row per held name: `Ticker | Avg cost | Current | Zone (ADD / HOLD / SELL-FLAG) | Distance to ADD band | Distance to sell-flag line`. The Ticker cell is the bare key and the Zone cell starts with the zone word (`ADD`, `HOLD` or `SELL-FLAG`; a note may follow). gsc-automerge reads this table (MODEL §8.7 item 10): a held name missing from this table, or a Zone cell without a zone word, holds the PR. A zone change does not (J11); the morning digest reports it under `## Held zone changes (SWEEP)`, and step 6 raises a review request.
4. **BUY, WATCH and one-gate AVOID rows** (§8.3 steps 2–3). The list is `python3 routines/tools/gsc_register.py sweep-scope` (held names, BUY, WATCH and one-gate AVOID, with each key's endpoint symbol, `px_unit`, `px_date`, trigger, core currency and `holding_keys`); query each `endpoint_symbol`. Current price only, one lookup per name. **Never price a two-or-more-gate AVOID or DNAF row.** Build the watchlist table for BUY and WATCH (PR body only): `Ticker | Trigger | Px | Distance % (Px ÷ Trigger − 1) | EV/OI 3y · 5y | Status (IN RANGE / NEAR within ~10% / FAR)` (MODEL §8.3 step 3); a row with Trigger `n.m.` shows Status `n.m.`. Distance, Status and the 3-year and 5-year EV/OI readings are what `python3 routines/tools/gsc_register.py metrics {KEY} {PX}` prints. Status comes from `status_hint` (MODEL §8.3 step 3, R10): IN RANGE needs MCap/FCF ≤ 8 and EV/OI no-cash ≤ 7 at Px, wherever the core numbers establish them; this also covers a row still carrying an older all-cash trigger. The MCap/FCF leg counts only on a P20 maintenance-capex `core_fcf_basis` (or the FI NI basis): a pre-R6 all-capex or unrecorded FCF breach is not established (R6), and `metrics` notes it. One-gate AVOID names appear only in the price table.
5. **Price discipline.**
   - **One key, one instrument.** The §7.1a key is the price lookup (`endpoint_symbol`). Record the instrument name, venue (`exchangeName`), `currency`, close and close date for every price.
   - **Unit and instrument checks (IDEAS C5).** The endpoint's `currency` must equal the row's `px_unit`; the instrument name must match the company; the bar must be a regular-session close on the stated close date. A key failing any check is left out of the refresh and listed under `## Unit or instrument mismatches` with the reason (`unit`, `instrument`, `session`).
   - **Splits.** Query with `&events=split` (the same call). A split or consolidation dated after the row's `px_date` means the register's core numbers are per pre-split share: leave the key out of the refresh, list it under `## Unit or instrument mismatches` as `split — {ratio} on {date}`, and add it to `## Review requests`. INTAKE never applies a Px across a split.
   - A close more than 5 trading days old counts as **stale**: mark it and don't use it.
   - **Two-source rule:** if a price moves more than 10% against the register's Px, confirm it on a second venue before using it. If it can't be confirmed, mark it *unconfirmed* and leave it out of the refresh.
   - **FX:** for each in-scope key whose `core_currency` differs from its px currency (the major unit of `px_unit`: GBp → GBP, ZAc → ZAR, ILA → ILS, KWF → KWD), fetch the pair once: the ECB reference via frankfurter, dated; where the ECB has no rate (TWD, SAR, AED, QAR, KWD, ARS, CLP, COP, VND and others), the endpoint's `{CCY1}{CCY2}=X` close. Record it in `## FX` as `{core_currency}/{px currency}`, a major-unit rate (px currency per 1 core currency) — never ×100.
   - **If a price host blocks the sandbox:** log the host and HTTP status once, then move on. Never retry a blocked host through an alternative.
6. **Review requests** (§8.3 step 4). One line each, `KEY — reason`, the reason starting with its class (REVIEW takes held and IN RANGE requests at priority 1a, the rest at 2):
   - every held name whose zone differs from its Portfolio `Zone`: `held zone {Portfolio} → {sweep} — …` (J11: the SWEEP merges with it, so this request and the digest are how it reaches a REVIEW and Jakub; MODEL §7.2);
   - every other held name at ADD (zone unchanged): `held ADD — …`;
   - a held name at SELL-FLAG whose zone is unchanged **only if** the `queue/TODO.md` head block `▶ Open items (register)` has no entry for its SELL-FLAG: `held SELL-FLAG — …`. An entry that records a decision, a deferral or "decision pending" means the flag is already with Jakub: list the name under `## Held names — info only` as "info only — decision recorded", not as a request;
   - every IN RANGE BUY or WATCH name (its `status_hint`): `IN RANGE — …`;
   - every name whose move beyond 10% was confirmed: `move {±x}% — …`;
   - every key with a split since its `px_date` (step 5): `split — …`.

   The sweep never substitutes for a REVIEW.
7. **Write** `queue/rows/{D}_{T}_SWEEP.md` (README §4, `row_type: SWEEP`). It contains:
   - the full price table: key, instrument, venue, currency, close, close date, source
   - `## Portfolio table` (step 3): every held name, Zone cell starting with the zone word
   - the watchlist table
   - `## Price/ordering refresh`: `| Key | Px | Px unit | Close date | Source |` for every priced, fresh, confirmed, unit-checked name in scope. Px is a plain number (no symbol, no separator) in the endpoint's `currency`, written verbatim in `Px unit`; the close date is `YYYY-MM-DD`.
   - `## FX`: `| Pair | Rate | Date |`, one line per pair fetched (or "none")
   - `## Unit or instrument mismatches`: one line per key left out by the step-5 checks (or "none")
   - `## Review requests`
   - `## Held names — info only`

   Verdicts, bands and memo references don't change. Write the run note too.
8. **Lint the row file** (`python3 routines/tools/gsc_register.py lint-row queue/rows/{D}_{T}_SWEEP.md` exits 0, README §5 [v4.5.2]), **push** and finish the PR (README §1) as `GSC SWEEP {D} — {n}/{N} priced · {k} in range · {s} stale`, where N is the `sweep-scope` count. The PR body carries the two tables, the mismatches and the review requests. A SWEEP sends no push (README §5): a held zone change reaches Jakub through the morning digest (J11). gsc-automerge merges the PR unless a held name is missing from the portfolio table or its Zone cell has no zone word.

**Forbidden:**
- any edit to an existing file
- any verdict, band or memo change
- pricing a two-or-more-gate AVOID or DNAF row
- multiples (the 3-year and 5-year averaged readings included) or distances computed outside `routines/tools/gsc_register.py`
- the tool's one-time attended `rebuild` and `retrigger`
- any REVIEW work
- any buy or sell language

*Framework output, not investment advice.*
