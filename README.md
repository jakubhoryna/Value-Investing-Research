# Value-Investing-Model

Good Stocks Cheap (GSC) research vault — Kenneth Jeffrey Marshall's Value Investing Model,
implemented under Project Instructions v3 (2026-07-05).

## Layout
- `_REGISTER.md` — master watchlist + portfolio layer. **Source of truth.** One row per company,
  latest memo version only. This is the file Claude reads at session start (raw URL below).
- `memos/` — one Markdown memo per company-version (`TICKER_YYYY-MM-DD_GSC.md`). Full history kept.
- `reference/` — book extraction (doctrine reference).
- `archive/` — superseded register versions and the earlier stub, kept for provenance.

## Register read URL (tokenless, public)
https://raw.githubusercontent.com/jakubhoryna/Value-Investing-Model/main/_REGISTER.md

## Discipline
- Register updates are commits; git history is the change log.
- Memo files never overwrite — new versions are new dated files.
- No secrets in this repo. Auth tokens live only in the local git credential store.

*Framework output, not investment advice.*

<!-- Obsidian Git sync test — 2026-07-05 -->
