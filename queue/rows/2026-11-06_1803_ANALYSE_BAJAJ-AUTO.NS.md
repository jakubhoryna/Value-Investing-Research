---
row_type: ANALYSE
key: BAJAJ-AUTO.NS
company: Bajaj Auto Limited
isin: INE917I01010
memo_path: memos/BAJAJ-AUTO.NS/BAJAJ-AUTO.NS_2026-11-06_GSC.md
run_date: 2026-11-06
run_time: 1803
run_base: 4b78cfe4733f1f9f4aebe5956654c96be6615427
model_version: v4.8.0
held: false
pr_title: GSC ANALYSE BAJAJ-AUTO.NS 2026-11-06 — AVOID (Future + SF)
---
## Register row (new)
| Ticker | Company | Memo date | Ver | Verdict | Past | Future | SF | Px | Trigger | MCap/FCF | EV/OI | MCap/FCF 3y · 5y | EV/OI 3y · 5y | Next review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BAJAJ-AUTO.NS | Bajaj Auto Limited | 2026-11-06 | v1 | AVOID | STRONG · 19.9% ROCE | WEAK · unit customer conc. | FAIL · acquisitions | 10900.00 | 2174.18 | 28.6 | 26.7 | 38.8 · 48.7 | 32.2 · 38.7 | May 2027 |
## Replaces
new name
## Queue update
DRAFT_QUEUE: BAJAJ-AUTO.NS → [x]
Group dependency: ABBN.SW → memo exists
Group dependency: ATCO-B.ST → memo exists
## Group dependency
`BMAG.SW` — subsidiary of BAJAJ-AUTO.NS, memo missing
## TODO additions
none
## Open items
none
## IDEAS candidates
- Captive finance arm's funding pairing in the core fields: this memo carries pairing A (the arm's funding in `core_debt_eq`, OI before its funding cost in `core_oi`) because it governs the trigger and `lint-memo` needs the binding leg at its threshold; `core_oi_basis` still reads `J1`. A basis tag for "J1 before captive funding cost" would make the pairing visible in the register (cf. the JUN3.DE candidate of 2026-11-05).
- Acquisition stop on a step-acquisition through an unlisted holding company of a listed target (PBAG → BMAG): this memo read the listed target's P3 record through the holding company under J13 (ADVERSE); the alternative private-target reading gives CAUTION. A rule naming which reading applies would fix it.
