---
row_type: INCOMPLETE
key: MARICO.NS
company: Marico Limited
isin: INE196A01026
evidence_path: queue/evidence/MARICO.NS_2026-11-02_INCOMPLETE.md
run_date: 2026-11-02
run_time: 2353
run_base: ec9d2d4893fb8560bfc5e4e3ebf1dd3d7bceec50
model_version: v4.8.0
held: false
pr_title: GSC ANALYSE MARICO.NS 2026-11-02 — INCOMPLETE (data access: marico.com HTTP 406, price endpoint HTTP 429)
---
## Queue update
DRAFT_QUEUE: MARICO.NS → [!] incomplete 2026-11-02 — queue/evidence/MARICO.NS_2026-11-02_INCOMPLETE.md

## TODO additions
- `MARICO.NS` — ANALYSE 2026-11-02 INCOMPLETE (data access): the resume of the 2026-10-31 partial could not start. marico.com returned HTTP 406 ("blocked due to suspicious behavior") on every annual-report PDF, which the 2026-10-31 run fetched without a block; the BSE annual-report index (403), NSE archives (connection reset) and the price endpoint (429) were also unreachable. Retry when marico.com serves again; the 2026-10-31 record holds the scope. Records: queue/evidence/MARICO.NS_2026-10-31_INCOMPLETE.md, queue/evidence/MARICO.NS_2026-11-02_INCOMPLETE.md

## Open items
none

## IDEAS candidates
none
