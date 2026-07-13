# Value-Investing-Model

Good Stocks Cheap (GSC) research vault — Kenneth Jeffrey Marshall's Value Investing Model,
run as a Claude project. Governance is split: a static bootstrap in project settings
(mirrored token-redacted at `instructions/BOOTSTRAP.md`) plus the live operative framework
at `instructions/MODEL.md`, fetched at every session start.

## Layout
- `_REGISTER.md` — master watchlist + portfolio layer. **Source of truth.** One row per company,
  latest memo version only; current version, date, and counts live in its front matter.
- `memos/` — one Markdown memo per company-version (`TICKER_YYYY-MM-DD_GSC.md`). Full history
  kept; memo files never overwrite.
- `instructions/` — `MODEL.md` (live framework, semver + change log), `BOOTSTRAP.md`
  (token-redacted mirror of the project instructions), `BOOK_EXTRACT.md`, and `archive/`
  (frozen superseded versions).
- `registers/archive/` — one verbatim snapshot per outgoing register version (MODEL §7.5),
  plus migration notes.
- `reference/` — book extraction and doctrine reference.
- `archive/` — early stubs and superseded pre-v3 files, kept for provenance.

## Access
Private repo — there is no tokenless raw URL. Reads and writes go through the GitHub
contents API with a fine-grained PAT (Contents R/W, single repo), loaded from the
bootstrap config at session start.

## Discipline
- Register updates are versioned commits (front matter version + change log, newest 5
  entries); outgoing versions snapshot to `registers/archive/`; every register PUT is
  preceded by base verification against the live head (MODEL §7.4a).
- Framework changes require the exact phrase "commit model"; superseded MODEL versions
  freeze to `instructions/archive/`.
- No secrets in this repo — the PAT lives only in the project-settings bootstrap; the
  committed `instructions/BOOTSTRAP.md` mirror is token-redacted.
- Plain Markdown only.

*Framework output, not investment advice.*
