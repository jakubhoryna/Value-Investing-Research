# SWEEP routine — weekly price screen (MODEL §8.3 under §8.7)

**Schedule:** Saturdays at 09:10 Europe/Prague, after every Friday close.
**Branch:** `claude/gsc-sweep-{D}-{T}`. **PR title:** `GSC SWEEP {D} [running]`.

SWEEP never writes the register. It writes one row file. INTAKE applies that file as the §8.3 step-5 price/ordering refresh after Jakub merges it: it takes each Px and its close date and recomputes Dist % itself.

1. **Preflight** per `routines/README.md` §0. If an open `GSC SWEEP` PR exists, the previous sweep hasn't been merged: stop with no PR.
2. **Claim:** open the branch and the PR (README §2).
3. **Held names first, always, regardless of verdict** (§8.3 step 1). For each name:
   - Get the current price.
   - Compute both primaries.
   - Build the portfolio table: `Ticker | Avg cost | Current | Zone (ADD / HOLD / SELL-FLAG) | Distance to ADD band | Distance to sell-flag line`.
4. **BUY and WATCH rows** (§8.3 steps 2–3). Current price only, one lookup per name. Build the watchlist table: `Ticker | Trigger band | Current price | Distance % | Status (IN RANGE / NEAR within ~10% / FAR)`. Compute Dist % exactly as §7.1 defines it: the price ÷ the operative trigger − 1, with dual-line and slash bands on the leg the price cell carries. These figures are for the PR body; INTAKE recomputes the register's Dist %.
5. **Price discipline.**
   - **One key, one instrument.** The §7.1a key is the price lookup. Record the instrument, venue, currency, close and close date for every price.
   - A close more than 5 trading days old counts as **stale**: mark it and don't use it.
   - **Two-source rule:** if a price moves more than 10% against the carried price, confirm it on a second venue before using it. If it can't be confirmed, mark it *unconfirmed* and leave it out of the refresh.
   - **FX:** use the ECB reference via frankfurter, dated.
   - **If a price host blocks the sandbox:** log the host and HTTP status once, then move on. Never retry a blocked host through an alternative.
6. **Review requests** (§8.3 step 4). One line each, with the reason:
   - every IN RANGE BUY or WATCH name;
   - every held name at ADD;
   - every name whose move beyond 10% was confirmed;
   - a held name at SELL-FLAG **only if** its zone changed since the register's `Last zone check`, or `## Open items` has no entry for its SELL-FLAG. An entry that records a decision, a deferral or "decision pending" means the flag is already with Jakub: list the name under `## Held names — info only` as "info only — decision recorded", not as a request.

   The sweep never substitutes for a REVIEW.
7. **Write** `queue/rows/{D}_{T}_SWEEP.md` (README §4, `row_type: SWEEP`). It contains:
   - the full price table: key, instrument, venue, currency, close, close date, source
   - the portfolio table
   - the watchlist table
   - `## Price/ordering refresh`: `| Key | Px | Close date | Source |` for every priced, fresh and confirmed name. Px is in the currency and instrument form of the row's current Px cell; the close date is `YYYY-MM-DD`.
   - `## Review requests`
   - `## Held names — info only`

   Verdicts, bands and memo references don't change. Write the run note too.
8. **Push** and finish the PR (README §1) as `GSC SWEEP {D} — {n}/{N} priced · {k} in range · {s} stale`. The PR body carries the two tables and the review requests.

**Forbidden:**
- any edit to an existing file
- any verdict, band or memo change
- any REVIEW work
- any buy or sell language

*Framework output, not investment advice.*
