# Lean register rebuild — v307 → v308 (2026-10-06)

One-time switch to the lean register (MODEL v4.5.0 §7.1, §7.1b), written by `gsc_register.py rebuild --base dd2260db749e30c37e3cf101e0b9a318cb4c619d`. The outgoing register is archived byte for byte as `REGISTER_v307_2026-10-06.md` beside this report.

## Rules

1. Never invent a number: a value no source establishes is '-' (backfill owed).
2. Keys, sections and the held flag come from the outgoing register; identity, grades, verdict and memo date from the memo each row cites (memo wins), enums normalised to their first token. A DNAF row the register made terminal after its memo (a delisting) keeps DNAF and is listed.
3. Px: held, BUY, WATCH and one-gate AVOID rows that the last applied SWEEP priced carry that close when the outgoing register shows it; every other row carries the memo's price. A price on another line or in another currency than the key's quote unit is '-' and listed.
4. Trigger: the memo's operative trigger (section 7.1, IDEAS C4 and C6) in the quote unit; an assisted value overrides the parser; a trigger in another currency is '-'.
5. Core numbers: only from the assisted file; each number must be a number of its verbatim memo quote, that number in another scale, a signed sum of the quote's numbers (a debt build) or a quotient or product of two of them (with the memo price and 1, 7, 8 as operands), at most six decimals; and only those whose multiples reproduce the memo's own printed multiples within 5% at the memo price (a memo that prints its current multiples on another share count or balance sheet than its band differs by a few per cent). Every row whose recomputed multiples differ from the print by more than 0.1 at the memo price is listed.
6. Multiples: recomputed from accepted core numbers at the Px shown; without them, the memo's printed multiples when Px is the memo price; otherwise '-'. DNAF rows print n.m.
7. Reasons: Past STRONG or ADEQUATE prints the worst-of-four level found in the memo; WEAK, FAIL and an SF caution only from the assisted file (section 7.1 vocabulary).

## Inputs

- Base: `dd2260db749e30c37e3cf101e0b9a318cb4c619d` — outgoing register v307 (2026-10-06), 384 names.
- Last applied SWEEP: `queue/rows/2026-10-05_1839_SWEEP.md` (added in 736fd154b678).
- Assisted file: 2608 rows (embedded below); 0 rejected.
- Assisted numbers traced to their memo quote: quoted 740 · scaled 25 · sum 96 · quotient 8 · product 0.

## Counts

| Measure | Value |
|---|---|
| Names | 384 |
| Split | BUY 0 · WATCH 88 · AVOID 294 (one gate 103 · two+ 191) · DNAF 2 |
| Held | 4 |
| In SWEEP scope (held, BUY, WATCH, one-gate AVOID) | 193 |
| In scope with core numbers (any) | 177 (92%) |
| In scope with every core number | 154 (80%) |
| WATCH rows with EV/OI shown (number or n.m.) | 86 of 88 |
| Rows with at least one owed field | 379 |

## Register-held DNAF rows (register-integrity hold) (1)

- EA: the register made the row DNAF after its memo (DNAF (delisted — take-private closed)); the memo says AVOID. DNAF kept; a Gate-0 memo is owed (register-integrity hold)

## Rows citing an archived memo (pending row at the base) (1)

- BABA: the register cites memos/BABA/BABA_2026-07-02_GSC.md; a pending row moves it to memos/BABA/BABA_2026-10-06_GSC.md at the next INTAKE

## Normalisations (42)

- CROX sf: 'PASS (1 flag — capital-allocation CAUTION; HEYDUDE + Malta-structure I' -> 'PASS'
- CROX memo_version: 'v7 (REVIEW — NYT Malta tax investigation; price delta; MODEL' -> 'v7'
- ABEV company: note 'ADR; B3: ABEV3' dropped from the cell (aliases from the assisted file)
- BKNG sf: 'PASS (1 flag — capital-allocation CAUTION)' -> 'PASS'
- MC.PA sf: 'PASS (1 flag — capital-allocation CAUTION [P19]; control caveat unpair' -> 'PASS'
- MC.PA memo_version: 'v3 (fresh full ANALYSE at user instruction — FY2017–FY2025 a' -> 'v3'
- NU sf: 'PASS (1 flag — capital-allocation CAUTION)' -> 'PASS'
- COLO-B.CO company: note 'B shares' dropped from the cell (aliases from the assisted file)
- METSO.HE company: note 'Metso Corporation; Metso Outotec Corporation until 2024' dropped from the cell (aliases from the assisted file)
- ROCK-B.CO company: note 'B shares' dropped from the cell (aliases from the assisted file)
- AXFO.ST sf: 'PASS (1 P19 flag — LTIP-hedge buybacks; strict book-pure read would st' -> 'PASS'
- KNIN.SW sf: 'PASS (1 P19 flag — 2023 tranche; Apex & IMC acquisition audits INDETER' -> 'PASS'
- 2502.T memo_version: none in the memo; register Ver v1 used
- 300750.SZ company: note 'CATL; HK dual-listing 3750.HK 2025' dropped from the cell (aliases from the assisted file)
- 300750.SZ quality_future: 'WEAK (provisional — the customer-concentration sentence decides; BKNG ' -> 'WEAK'
- 6501.T sf: 'PASS (1 flag — capital-allocation CAUTION)' -> 'PASS'
- 688825.SS sf: 'PASS (1 flag — P19 CAUTION; P17 INDETERMINATE)' -> 'PASS'
- 7011.T sf: 'PASS (no flag — capital allocation SOUND)' -> 'PASS'
- AD.AS sf: 'PASS (1 P19 flag)' -> 'PASS'
- ADS.DE verdict: 'AVOID (Past WEAK — leverage; SF FAIL — buybacks)' -> 'AVOID'
- APH sf: 'FAIL (capital allocation ADVERSE)' -> 'FAIL'
- ARQ company: note 'formerly Advanced Emissions Solutions, Inc.' dropped from the cell (aliases from the assisted file)
- ARQ sf: 'PASS (P17 INDETERMINATE — severity-changing; P19 CAUTION unpaired)' -> 'PASS'
- AXP quality_past: 'STRONG (documented lender substitution; literal alternate WEAK)' -> 'STRONG'
- BBBY company: note 'f/k/a Beyond, Inc.; f/k/a Overstock.com, Inc.' dropped from the cell (aliases from the assisted file)
- BH company: note 'Class B line; Class A = BH.A' dropped from the cell (aliases from the assisted file)
- COMP sf: 'PASS (P17 INDETERMINATE — pair-risk live; P19 CAUTION unpaired)' -> 'PASS'
- COPN.SW company: note 'formerly Cosmo Pharmaceuticals N.V.' dropped from the cell (aliases from the assisted file)
- CRI sf: 'PASS (1 flag — P17 fiscal-year-read breach; P19 SOUND on an incomplete' -> 'PASS'
- EQNR company: note 'NYSE ADR 1:1; Oslo: EQNR.OL' dropped from the cell (aliases from the assisted file)
- KWY company: note 'formerly Kingsway Financial Services Inc.' dropped from the cell (aliases from the assisted file)
- NOKIA.HE company: note 'NOK ADR 1:1' dropped from the cell (aliases from the assisted file)
- NOVO-B.CO verdict: 'AVOID (Future WEAK; SF FAIL)' -> 'AVOID'
- NOVO-B.CO sf: 'FAIL (flag pair — capital-allocation CAUTION [P19] + related-party fla' -> 'FAIL'
- NOVO-B.CO memo_version: 'v10 (REVIEW — Capital Markets Day 21 Sep 2026 + price delta;' -> 'v10'
- NVDA verdict: 'AVOID (Future WEAK + SF FAIL)' -> 'AVOID'
- S sf: 'PASS (P17 year-read flag standing; normalized lens blind — see E)' -> 'PASS'
- VOW3.DE company: note 'preferred / Vorzugsaktien' dropped from the cell (aliases from the assisted file)
- WEN sf: 'PASS (1 flag — P19 CAUTION; RPT INDETERMINATE)' -> 'PASS'
- SYAB.DE quality_past: 'n/a — not assessed' -> 'n.m.'
- SYAB.DE quality_future: 'n/a — not assessed' -> 'n.m.'
- SYAB.DE sf: 'n/a — not assessed' -> 'n.m.'

## Unit conversions (4)

- GSK.L memo price 19.205 GBP -> 1920.5 GBp
- ULVR.L memo price 45.64 GBP -> 4564 GBp
- PSH.L memo price 37.96 GBP -> 3796 GBp
- SMSH.TA memo price 17.96 ILS -> 1796 ILA

## Price notes (48)

- ROG.SW: SWEEP priced RHHBY, not the key's line; the memo price is used
- SDZ.SW: the key's line is the later CHF 67.04 in the statement
- ULVR.L: the key's line is the later GBP 45.64 in the statement
- ULVR.L: SWEEP priced UNA.AS, not the key's line; the memo price is used
- 8TRA.ST: memo price 'EUR 36.04 (22 Jul 2026, 07:19 UTC; 52-wk range 25.78–37.34)' is not on the key's line or unit (EUR vs SEK): Px owed
- AAPL: memo price '~$308' has no close date
- ABNB: memo price '151.52' has no close date
- AKZA.AS: memo price '€56.28' has no close date
- AMV0.DE: memo price '€35.90' has no close date
- ASSA-B.ST: memo price '347.10' has no close date
- BAYN.DE: memo price '€47.17' has no close date
- BC.MI: memo price '83.56' has no close date
- BN.PA: memo price '€72.24' has no close date
- BNR.DE: memo price '59.10' has no close date
- COST: memo price '951.89' has no close date
- CSG.AS: memo price '€13.60' has no close date
- DLG.MI: memo price '€38.82' has no close date
- DOCU: memo price '$49.18' has no close date
- DSY.PA: memo price '€18.39' has no close date
- ENR.DE: memo price '€152.00' has no close date
- FRE.DE: memo price '42.63' has no close date
- GEN: memo price '26.57' has no close date
- HHH: memo price '$71.67' has no close date
- HLAG.DE: memo price '123.20' has no close date
- HOT.DE: memo price '455.60' has no close date
- HUSQ-B.ST: memo price '37.13' has no close date
- IBM: memo price '218.80' has no close date
- KER.PA: memo price '266.30' has no close date
- KLAR: memo price '$17.36' has no close date
- KSPI: the key's line is the later USD 106.29 in the statement
- LIGHT.AS: memo price '15.98' has no close date
- LIN: memo price '522.97' has no close date
- LLY: memo price '1213.00' has no close date
- LOGI: memo price '$102.91' has no close date
- LULU: memo price '97.50' has no close date
- PYPL: memo price '53.72' has no close date
- SHA0.DE: memo price '8.53' has no close date
- SHOP: memo price '$124.74' has no close date
- SRT3.DE: memo price 'EUR 215.85 (preference) \| EUR 174.00 (ordinary)' has no close date
- SY1.DE: memo price '87.94' has no close date
- TSLA: memo price '425.30' has no close date
- TTWO: memo price '$243.20' has no close date
- UN0.DE: memo price '43.20' has no close date
- V: memo price '$362.13' has no close date
- VSURE.ST: quote unit EUR from the price endpoint (endpoint 2026-10-06: currency EUR, exchangeName STO, longName Verisure plc, regu), not the suffix default SEK
- WISE.L: memo price '$12.03 (WSE close, 5 Aug 2026)' is not on the key's line or unit (USD vs GBp): Px owed
- ZIP: memo price '$4.49' has no close date
- SYAB.DE: memo price 'n/a — no listed security' is not on the key's line or unit (no listed price): Px owed

## Trigger notes (14)

- BRK.B: substitution anchor -> 400
- SDZ.SW: trigger 28 USD is not in the quote unit CHF: owed
- ULVR.L: trigger 17.3 EUR is not in the quote unit GBp: owed
- EPI-A.ST: FCF leg inside the pair caps the upper bound (C6); A line (C4a) -> 60.3
- ATCO-B.ST: FCF leg inside the pair caps the upper bound (C6) -> 39.8
- 1211.HK: trigger 26 CNY is not in the quote unit HKD: owed
- 300750.SZ: FCF leg inside the pair caps the upper bound (C6) -> 162.53
- ADS.DE: trigger not parsed (no CHEAP figure and no anchor price): owed
- BTI: assisted trigger 22.91 (parser: 23)
- KSPI: assisted trigger 87.87 (parser: no CHEAP figure and no anchor price)
- ONON: trigger 6.2 CHF is not in the quote unit USD: owed
- SPOT: trigger 64 EUR is not in the quote unit USD: owed
- VC: FCF leg inside the pair caps the upper bound (C6) -> 83
- WISE.L: trigger 3.7 USD is not in the quote unit GBp: owed

## Trigger differences against the outgoing register (6)

- GSK.L: trigger 908; the outgoing register's Dist +75% implies about 1005.14 (memo wins)
- CSU.TO: trigger 513; the outgoing register's Dist +315% implies about 718.36 (memo wins)
- EPI-A.ST: trigger 60.3; the outgoing register's Dist +318% implies about 63.64 (memo wins)
- ATCO-B.ST: trigger 39.8; the outgoing register's Dist +336% implies about 41.36 (memo wins)
- KNIN.SW: trigger 34; the outgoing register's Dist +437% implies about 40.97 (memo wins)
- INDT.ST: trigger 44.5; the outgoing register's Dist +442% implies about 48.34 (memo wins)

## Core-number validation (205)

- CROX: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 8.9/8.9 ok; ev_oi 8.5/8.5 ok; ev_oi_all_cash 8.3/8.3 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_debt_eq, core_cash
- BRK.B: the memo prints ev_oi n.m. (assisted read: 'the operative gauge is price-to-book')
- BRK.B: accepted core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 42.1/42.1 ok; ev_oi n.m./n.m. ok; ev_oi_all_cash n.m./- no)
- INVE-B.ST: accepted core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf n.m./n.m. ok; ev_oi n.m./n.m. ok; ev_oi_all_cash n.m./n.m. ok)
- SGO.PA: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 11.5/11.5 ok; ev_oi 10.8/10.8 ok; ev_oi_all_cash 9.7/9.7 ok)
- ABEV: accepted core_cash, core_debt_eq, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf -/10.2 no; ev_oi 11.3/11.6 ok; ev_oi_all_cash 10.5/10.7 ok)
- CRCT: the memo prints mcap_fcf 7.0 (assisted read: 'MCap/FCF 7.0× — passes P7')
- CRCT: the memo prints ev_oi 12.9 (assisted read: 'EV/OI 12.9× / 10.2× — fails P8 on both variants')
- CRCT: the memo prints ev_oi_all_cash 10.2 (assisted read: 'EV/OI 12.9× / 10.2× — fails P8 on both variants')
- CRCT: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 7.0/7.0 ok; ev_oi 12.9/12.9 ok; ev_oi_all_cash 10.2/10.2 ok)
- ADBE: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 10.8/10.8 ok; ev_oi 12.9/12.9 ok; ev_oi_all_cash 12.3/12.3 ok)
- 6626.T: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 80.2/80.2 ok; ev_oi 7.3/7.3 ok; ev_oi_all_cash 4.6/4.6 ok)
- GSK.L: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 13.8/13.8 ok; ev_oi 12.3/12.3 ok; ev_oi_all_cash 11.7/11.7 ok); derived from the quoted figures (not printed as such): core_debt_eq, core_cash
- 8002.T: accepted core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 21.0/21.0 ok; ev_oi n.m./n.m. ok; ev_oi_all_cash n.m./n.m. ok)
- TROW: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 15.1/15.1 ok; ev_oi 10.9/10.9 ok; ev_oi_all_cash 9.0/9.0 ok)
- FIE.DE: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 9.4/9.4 ok; ev_oi 12.7/12.7 ok; ev_oi_all_cash 12.0/12.0 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_debt_eq
- INTU: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 11.2/11.2 ok; ev_oi 17.8/17.8 ok; ev_oi_all_cash 16.6/16.6 ok)
- KCR.HE: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 14.1/14.1 ok; ev_oi 14.3/14.3 ok; ev_oi_all_cash 13.6/13.6 ok)
- IP.MI: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 16.0/16.0 ok; ev_oi 13.3/13.3 ok; ev_oi_all_cash 12.2/12.2 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_debt_eq
- BKNG: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 16.1/16.1 ok; ev_oi 18.9/18.9 ok; ev_oi_all_cash 16.9/16.9 ok)
- ESSITY-B.ST: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 22.5/22.5 ok; ev_oi 12.5/12.5 ok; ev_oi_all_cash 12.1/12.1 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_debt_eq
- KALMAR.HE: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 16.9/16.9 ok; ev_oi 12.3/12.3 ok; ev_oi_all_cash 11.1/11.1 ok)
- MC.PA: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 13.7/13.7 ok; ev_oi 14.1/14.1 ok; ev_oi_all_cash 13.4/13.4 ok)
- RBREW.CO: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 12.6/12.6 ok; ev_oi 11.9/11.9 ok; ev_oi_all_cash 11.9/11.9 ok)
- 0700.HK: the memo prints mcap_fcf 22.0 (assisted read: 'MCap/FCF 22.0× strict / 16.8× maintenance')
- 0700.HK: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 22.0/22.0 ok; ev_oi 18.2/18.2 ok; ev_oi_all_cash 16.4/16.4 ok); derived from the quoted figures (not printed as such): core_debt_eq, core_fx
- 6758.T: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 14.2/14.2 ok; ev_oi 16.4/16.4 ok; ev_oi_all_cash 14.9/14.9 ok); derived from the quoted figures (not printed as such): core_debt_eq
- ANDR.VI: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 18.0/18.0 ok; ev_oi 15.4/15.4 ok; ev_oi_all_cash 13.7/13.7 ok); derived from the quoted figures (not printed as such): core_debt_eq
- FDS: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 16.4/16.5 ok; ev_oi 15.7/15.7 ok; ev_oi_all_cash 15.3/15.3 ok)
- BRG.OL: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 27.1/27.1 ok; ev_oi 13.6/13.6 ok; ev_oi_all_cash 13.5/13.5 ok)
- SNA: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 19.3/19.3 ok; ev_oi 15.6/15.6 ok; ev_oi_all_cash 14.4/14.4 ok)
- BVI.PA: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 15.4/15.4 ok; ev_oi 15.9/15.9 ok; ev_oi_all_cash 14.9/14.9 ok)
- QCOM: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 12.2/12.2 ok; ev_oi 13.9/13.9 ok; ev_oi_all_cash 13.2/13.2 ok)
- ROG.SW: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 19.0/19.1 ok; ev_oi 14.4/14.5 ok; ev_oi_all_cash 13.7/13.7 ok); derived from the quoted figures (not printed as such): core_debt_eq
- SCHN.SW: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 19.2/19.5 ok; ev_oi 19.8/20.0 ok; ev_oi_all_cash 16.7/17.0 ok); derived from the quoted figures (not printed as such): core_debt_eq
- 6841.T: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 20.1/20.1 ok; ev_oi 14.7/14.7 ok; ev_oi_all_cash 12.5/12.5 ok)
- NVS: the memo prints ev_oi_all_cash 17.6 (assisted read: 'EV/OI 310,213/17,644 = 17.6× (low)')
- NVS: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 16.5/16.5 ok; ev_oi 18.3/18.3 ok; ev_oi_all_cash 17.6/17.6 ok); derived from the quoted figures (not printed as such): core_debt_eq
- BMI: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 21.9/21.9 ok; ev_oi 20.4/20.4 ok; ev_oi_all_cash 19.9/19.9 ok); derived from the quoted figures (not printed as such): core_debt_eq
- NU: the memo prints mcap_fcf n.m. (assisted read: 'deposit-funded lender (ROE basis; OI/FCF/CE machinery inappl')
- NU: accepted core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf n.m./n.m. ok; ev_oi n.m./n.m. ok; ev_oi_all_cash n.m./n.m. ok)
- AZA.ST: the memo prints mcap_fcf n.m. (assisted read: 'CFO distorted by deposit/insurance flows')
- AZA.ST: accepted core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf n.m./n.m. ok; ev_oi n.m./n.m. ok; ev_oi_all_cash n.m./n.m. ok); derived from the quoted figures (not printed as such): core_shares_diluted
- SDZ.SW: rejected (mcap_fcf 26.6/33.4 no; ev_oi -/28.6 no; ev_oi_all_cash -/19.5 no)
- MORN: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 16.3/16.3 ok; ev_oi 17.3/17.3 ok; ev_oi_all_cash 16.3/16.3 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_debt_eq, core_cash
- ADYEN.AS: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 28.6/28.6 ok; ev_oi 23.5/13.8 no; ev_oi_all_cash 13.8/- no; the single unlabelled EV/OI 13.8 is the all-cash reading)
- 6845.T: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 24.3/24.0 ok; ev_oi 16.0/15.9 ok; ev_oi_all_cash 14.0/13.8 ok)
- DOV: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 23.0/23.0 ok; ev_oi 20.6/20.6 ok; ev_oi_all_cash 19.3/19.3 ok); derived from the quoted figures (not printed as such): core_debt_eq
- COLO-B.CO: the memo prints mcap_fcf 18.0 (assisted read: 'MCap/FCF 18.0×')
- COLO-B.CO: the memo prints ev_oi 16.5 (assisted read: 'EV/OI 16.5× / 16.3×')
- COLO-B.CO: the memo prints ev_oi_all_cash 16.3 (assisted read: 'EV/OI 16.5× / 16.3×')
- COLO-B.CO: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 18.0/18.0 ok; ev_oi 16.5/16.5 ok; ev_oi_all_cash 16.3/16.3 ok)
- THULE.ST: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 29.7/29.7 ok; ev_oi 16.8/16.8 ok; ev_oi_all_cash 16.7/16.7 ok); derived from the quoted figures (not printed as such): core_shares_diluted
- META: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 36.2/35.8 ok; ev_oi 21.4/21.2 ok; ev_oi_all_cash 20.3/20.1 ok); derived from the quoted figures (not printed as such): core_cash
- DCI: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 24.5/24.1 ok; ev_oi 19.7/19.4 ok; ev_oi_all_cash 19.3/19.0 ok)
- SKF-B.ST: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 25.5/25.5 ok; ev_oi 17.3/17.3 ok; ev_oi_all_cash 16.0/16.0 ok); derived from the quoted figures (not printed as such): core_debt_eq
- NMAN.ST: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 28.1/28.1 ok; ev_oi 13.9/13.9 ok; ev_oi_all_cash 12.9/12.9 ok)
- TRI: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 22.8/22.8 ok; ev_oi 23.1/23.1 ok; ev_oi_all_cash 22.8/22.8 ok); derived from the quoted figures (not printed as such): core_debt_eq
- METSO.HE: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 22.4/22.4 ok; ev_oi 21.3/21.3 ok; ev_oi_all_cash 20.7/20.7 ok)
- SAVE.ST: accepted core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf -/- no; ev_oi n.m./n.m. ok; ev_oi_all_cash n.m./n.m. ok)
- LECO: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 28.7/28.0 ok; ev_oi 23.0/22.5 ok; ev_oi_all_cash 22.7/22.2 ok); derived from the quoted figures (not printed as such): core_debt_eq
- SAP.DE: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 22.4/22.4 ok; ev_oi 20.3/20.3 ok; ev_oi_all_cash 19.5/19.5 ok); derived from the quoted figures (not printed as such): core_debt_eq
- BA.L: the memo prints mcap_fcf 26.8 (assisted read: 'MCap/FCF 26.8× (on 2,475; 30.8× on company-defined 2,158)')
- BA.L: the memo prints ev_oi 25.8 (assisted read: 'EV/OI 25.8× / 24.6×')
- BA.L: the memo prints ev_oi_all_cash 24.6 (assisted read: 'EV/OI 25.8× / 24.6×')
- BA.L: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 26.8/26.8 ok; ev_oi 25.8/25.8 ok; ev_oi_all_cash 24.6/24.6 ok); derived from the quoted figures (not printed as such): core_debt_eq, core_oi
- RMS.PA: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 38.2/38.2 ok; ev_oi 24.8/24.8 ok; ev_oi_all_cash 22.9/22.9 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_debt_eq
- SOON.SW: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 24.1/24.0 ok; ev_oi 23.2/23.1 ok; ev_oi_all_cash 22.1/22.0 ok)
- SAND.ST: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 29.1/29.1 ok; ev_oi 23.4/23.4 ok; ev_oi_all_cash 23.2/23.2 ok); derived from the quoted figures (not printed as such): core_debt_eq
- CSU.TO: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 15.5/15.5 ok; ev_oi 24.7/24.7 ok; ev_oi_all_cash 23.1/23.1 ok); derived from the quoted figures (not printed as such): core_debt_eq, core_cash
- EPI-A.ST: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 32.4/32.4 ok; ev_oi 25.4/25.4 ok; ev_oi_all_cash 24.4/24.4 ok); derived from the quoted figures (not printed as such): core_debt_eq
- WTS: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 34.1/34.0 ok; ev_oi 27.6/27.5 ok; ev_oi_all_cash 26.8/26.7 ok)
- 7974.T: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 33.5/33.5 ok; ev_oi 24.5/24.5 ok; ev_oi_all_cash 19.0/19.0 ok)
- ATCO-B.ST: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 35.6/35.6 ok; ev_oi 28.6/28.6 ok; ev_oi_all_cash 28.1/28.1 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_debt_eq, core_cash
- IBKR: accepted core_debt_eq, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf -/n.m. no; ev_oi 32.6/32.6 ok; ev_oi_all_cash -/- no)
- 7936.T: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 40.2/40.2 ok; ev_oi 23.1/23.1 ok; ev_oi_all_cash 22.2/22.2 ok); derived from the quoted figures (not printed as such): core_debt_eq
- ALFA.ST: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 37.9/37.9 ok; ev_oi 21.6/21.6 ok; ev_oi_all_cash 21.0/21.0 ok); derived from the quoted figures (not printed as such): core_debt_eq
- ROCK-B.CO: the memo prints mcap_fcf 52.8 (assisted read: 'Reported basis: EV/OI 38.3× / 37.7×; MCap/FCF 52.8×')
- ROCK-B.CO: the memo prints ev_oi 38.3 (assisted read: 'Reported basis: EV/OI 38.3× / 37.7×; MCap/FCF 52.8×')
- ROCK-B.CO: the memo prints ev_oi_all_cash 37.7 (assisted read: 'Reported basis: EV/OI 38.3× / 37.7×; MCap/FCF 52.8×')
- ROCK-B.CO: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 52.5/52.8 ok; ev_oi 38.2/38.3 ok; ev_oi_all_cash 37.5/37.7 ok); derived from the quoted figures (not printed as such): core_oi
- AXFO.ST: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 11.6/11.6 ok; ev_oi 20.8/20.8 ok; ev_oi_all_cash 20.5/20.5 ok); derived from the quoted figures (not printed as such): core_debt_eq
- KNIN.SW: accepted core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 16.6/16.6 ok; ev_oi 23.6/23.6 ok; ev_oi_all_cash -/23.0 no); derived from the quoted figures (not printed as such): core_debt_eq
- INDT.ST: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 24.0/24.0 ok; ev_oi 25.4/25.4 ok; ev_oi_all_cash 25.1/25.1 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_debt_eq
- LIFCO-B.ST: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 30.9/30.9 ok; ev_oi 29.5/29.5 ok; ev_oi_all_cash 29.2/29.2 ok); derived from the quoted figures (not printed as such): core_debt_eq
- LR.PA: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 27.9/27.9 ok; ev_oi 24.8/24.8 ok; ev_oi_all_cash 23.7/23.7 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_debt_eq
- SIKA.SW: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 23.6/23.6 ok; ev_oi 25.1/25.1 ok; ev_oi_all_cash 24.7/24.7 ok); derived from the quoted figures (not printed as such): core_debt_eq
- AME: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 34.6/34.6 ok; ev_oi 27.2/27.2 ok; ev_oi_all_cash 27.0/27.0 ok); derived from the quoted figures (not printed as such): core_debt_eq
- HUBN.SW: accepted core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 48.6/48.6 ok; ev_oi 38.5/38.5 ok; ev_oi_all_cash -/36.2 no); derived from the quoted figures (not printed as such): core_shares_diluted
- AMZN: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 250.1/250.1 ok; ev_oi 37.8/37.8 ok; ev_oi_all_cash 36.3/36.3 ok)
- 3064.T: accepted core_cash, core_debt_eq, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 48.0/57.4 no; ev_oi 22.7/22.7 ok; ev_oi_all_cash 21.8/21.8 ok); derived from the quoted figures (not printed as such): core_debt_eq
- CRL.MI: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 33.0/33.0 ok; ev_oi 41.3/41.3 ok; ev_oi_all_cash 39.8/39.8 ok); derived from the quoted figures (not printed as such): core_debt_eq, core_cash
- 6861.T: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 52.6/52.6 ok; ev_oi 32.7/32.7 ok; ev_oi_all_cash 30.3/30.3 ok)
- DNP.WA: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 51.9/51.9 ok; ev_oi 15.8/15.8 ok; ev_oi_all_cash 15.3/15.3 ok)
- NESN.SW: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 19.0/19.0 ok; ev_oi 22.1/22.1 ok; ev_oi_all_cash 21.6/21.6 ok); derived from the quoted figures (not printed as such): core_debt_eq
- FAST: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 55.6/55.4 ok; ev_oi 35.5/35.4 ok; ev_oi_all_cash 35.4/35.3 ok); derived from the quoted figures (not printed as such): core_debt_eq
- MYCR.ST: accepted core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 49.3/49.3 ok; ev_oi 31.8/31.8 ok; ev_oi_all_cash -/30.4 no)
- 2330.TW: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 63.0/63.0 ok; ev_oi 32.9/32.9 ok; ev_oi_all_cash 31.0/31.0 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_debt_eq
- RSW.L: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 70.7/70.7 ok; ev_oi 32.3/32.3 ok; ev_oi_all_cash 30.1/30.1 ok)
- HMS.ST: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 37.8/37.8 ok; ev_oi 40.0/39.9 ok; ev_oi_all_cash 39.9/39.9 ok)
- HEI: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 41.5/41.5 ok; ev_oi 38.4/38.4 ok; ev_oi_all_cash 38.2/38.2 ok); derived from the quoted figures (not printed as such): core_shares_diluted
- IFCN.SW: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 70.2/70.2 ok; ev_oi 42.8/42.8 ok; ev_oi_all_cash 41.6/41.6 ok); derived from the quoted figures (not printed as such): core_fx
- SIE.DE: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 20.0/20.0 ok; ev_oi 29.5/29.5 ok; ev_oi_all_cash 28.0/28.0 ok); derived from the quoted figures (not printed as such): core_debt_eq
- 005930.KS: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 59.4/59.4 ok; ev_oi 46.0/46.0 ok; ev_oi_all_cash 43.1/43.1 ok); derived from the quoted figures (not printed as such): core_debt_eq, core_cash
- 1913.HK: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 10.7/10.7 ok; ev_oi 12.3/12.3 ok; ev_oi_all_cash 11.4/11.4 ok); derived from the quoted figures (not printed as such): core_shares_diluted
- 5108.T: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 14.1/14.1 ok; ev_oi 15.9/15.9 ok; ev_oi_all_cash 14.1/14.1 ok)
- 6273.T: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 132.8/132.8 ok; ev_oi 24.1/24.1 ok; ev_oi_all_cash 20.3/20.3 ok); derived from the quoted figures (not printed as such): core_debt_eq
- 6301.T: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 28.2/28.2 ok; ev_oi 14.5/14.5 ok; ev_oi_all_cash 13.7/13.7 ok); derived from the quoted figures (not printed as such): core_debt_eq
- 6367.T: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 25.2/25.2 ok; ev_oi 17.8/17.8 ok; ev_oi_all_cash 15.0/15.0 ok); derived from the quoted figures (not printed as such): core_debt_eq
- 6383.T: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 41.8/41.8 ok; ev_oi 22.4/22.4 ok; ev_oi_all_cash 19.7/19.7 ok); derived from the quoted figures (not printed as such): core_debt_eq
- 6501.T: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 21.3/21.4 ok; ev_oi 23.2/23.2 ok; ev_oi_all_cash 21.5/21.5 ok)
- 6506.T: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 210.2/210.2 ok; ev_oi 29.1/29.1 ok; ev_oi_all_cash 27.9/27.9 ok); derived from the quoted figures (not printed as such): core_debt_eq
- 6702.T: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 27.7/27.7 ok; ev_oi 18.7/18.7 ok; ev_oi_all_cash 17.4/17.4 ok); derived from the quoted figures (not printed as such): core_debt_eq
- 6954.T: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 26.2/26.2 ok; ev_oi 32.9/32.9 ok; ev_oi_all_cash 28.8/28.8 ok)
- 7751.T: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 18.6/18.6 ok; ev_oi 11.2/11.2 ok; ev_oi_all_cash 9.8/9.8 ok); derived from the quoted figures (not printed as such): core_debt_eq
- AAPL: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 46.8/45.8 ok; ev_oi 35.6/34.8 ok; ev_oi_all_cash 35.2/34.4 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_oi
- ABB: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 41.9/41.8 ok; ev_oi 31.0/30.9 ok; ev_oi_all_cash 30.0/30.0 ok); derived from the quoted figures (not printed as such): core_debt_eq
- ABCA.PA: the memo prints ev_oi n.m. (assisted read: 'EV/OI n.m. under the substitution rule')
- ABCA.PA: the memo prints ev_oi_all_cash n.m. (assisted read: 'EV/OI n.m. under the substitution rule')
- ABCA.PA: accepted core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf -/- no; ev_oi n.m./n.m. ok; ev_oi_all_cash n.m./n.m. ok)
- ABNB: accepted core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 20.5/19.6 ok; ev_oi 37.9/36.4 ok; ev_oi_all_cash 33.6/31.7 no)
- ACP.WA: accepted core_cash, core_debt_eq, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf -/7.0 no; ev_oi 15.4/15.4 ok; ev_oi_all_cash 10.9/10.9 ok); derived from the quoted figures (not printed as such): core_debt_eq
- AD.AS: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 8.8/8.8 ok; ev_oi 14.4/14.4 ok; ev_oi_all_cash 13.4/13.4 ok)
- ALE.WA: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 23.5/23.5 ok; ev_oi 21.5/21.5 ok; ev_oi_all_cash 20.3/20.3 ok)
- ALIG.ST: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 19.7/19.7 ok; ev_oi 16.4/16.4 ok; ev_oi_all_cash 15.6/15.6 ok)
- ANF: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 13.1/13.2 ok; ev_oi 9.0/9.0 ok; ev_oi_all_cash 8.1/8.1 ok)
- APH: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 51.2/51.2 ok; ev_oi 41.5/41.5 ok; ev_oi_all_cash 40.6/40.6 ok)
- AS: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 41.8/41.8 ok; ev_oi 32.0/32.0 ok; ev_oi_all_cash 31.0/31.0 ok); derived from the quoted figures (not printed as such): core_debt_eq
- ASML.AS: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 50.3/50.1 ok; ev_oi 49.7/49.5 ok; ev_oi_all_cash 48.6/48.8 ok)
- ASSA-B.ST: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 20.7/20.7 ok; ev_oi 19.5/19.5 ok; ev_oi_all_cash 19.4/19.4 ok); derived from the quoted figures (not printed as such): core_debt_eq
- BBWI: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 4.7/4.7 ok; ev_oi 7.8/7.8 ok; ev_oi_all_cash 7.1/7.1 ok)
- BC8.DE: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 26.8/26.8 ok; ev_oi 13.9/13.9 ok; ev_oi_all_cash 12.5/12.5 ok); derived from the quoted figures (not printed as such): core_debt_eq
- BNR.DE: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 12.7/12.7 ok; ev_oi 19.3/19.3 ok; ev_oi_all_cash 18.0/18.0 ok); derived from the quoted figures (not printed as such): core_debt_eq
- BTI: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 16.2/16.4 ok; ev_oi 13.1/13.2 ok; ev_oi_all_cash 12.7/12.8 ok); derived from the quoted figures (not printed as such): core_debt_eq
- CARL-B.CO: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 17.4/17.4 ok; ev_oi 17.1/17.1 ok; ev_oi_all_cash 16.2/16.2 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_debt_eq
- CDR.WA: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf n.m./n.m. ok; ev_oi 54.2/54.2 ok; ev_oi_all_cash 52.1/52.1 ok); derived from the quoted figures (not printed as such): core_debt_eq, core_fcf
- CON.DE: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 15.3/15.3 ok; ev_oi 79.1/79.1 ok; ev_oi_all_cash 73.0/73.0 ok)
- COST: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 54.0/53.9 ok; ev_oi 41.7/41.4 ok; ev_oi_all_cash 40.3/39.5 ok)
- DBX: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 8.4/8.4 ok; ev_oi 17.1/17.1 ok; ev_oi_all_cash 15.5/15.5 ok)
- DLB: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 13.0/13.0 ok; ev_oi 21.5/21.5 ok; ev_oi_all_cash 18.9/18.9 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_debt_eq, core_cash
- DLG.MI: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 13.1/13.1 ok; ev_oi 14.3/14.3 ok; ev_oi_all_cash 11.6/11.6 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_debt_eq
- EKTA-B.ST: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 12.9/12.9 ok; ev_oi 108.3/108.3 ok; ev_oi_all_cash 94.7/94.7 ok); derived from the quoted figures (not printed as such): core_debt_eq
- ENB.TO: the memo prints ev_oi 26.2 (assisted read: 'EV(consv) 286,505 / OI 10,958 = 26.1× (no-cash variant 26.2×')
- ENB.TO: the memo prints ev_oi_all_cash 26.1 (assisted read: 'EV(consv) 286,505 / OI 10,958 = 26.1× (no-cash variant 26.2×')
- ENB.TO: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 52.1/52.1 ok; ev_oi 26.2/26.2 ok; ev_oi_all_cash 26.1/26.1 ok); derived from the quoted figures (not printed as such): core_debt_eq
- EQNR: accepted core_cash, core_debt_eq, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf -/15.6 no; ev_oi 5.0/5.0 ok; ev_oi_all_cash 4.0/4.0 ok); derived from the quoted figures (not printed as such): core_debt_eq
- FORTUM.HE: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 51.0/51.0 ok; ev_oi 22.7/22.7 ok; ev_oi_all_cash 18.7/18.7 ok); derived from the quoted figures (not printed as such): core_debt_eq
- FTK.DE: accepted core_fcf, core_fx, core_ratio, core_shares_diluted (mcap_fcf 22.7/22.7 ok; ev_oi -/n.m. no; ev_oi_all_cash -/n.m. no)
- G1A.DE: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 24.1/24.1 ok; ev_oi 17.6/17.6 ok; ev_oi_all_cash 17.1/17.1 ok); derived from the quoted figures (not printed as such): core_shares_diluted
- GEBN.SW: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 25.1/25.1 ok; ev_oi 24.8/24.8 ok; ev_oi_all_cash 24.0/24.0 ok)
- GETI-B.ST: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 23.8/23.8 ok; ev_oi 20.1/20.1 ok; ev_oi_all_cash 19.2/19.2 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_debt_eq
- GGG: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 20.3/20.3 ok; ev_oi 19.5/19.5 ok; ev_oi_all_cash 19.4/19.4 ok); derived from the quoted figures (not printed as such): core_debt_eq
- GRMN: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 41.7/41.7 ok; ev_oi 30.4/30.4 ok; ev_oi_all_cash 28.2/28.2 ok)
- HEIA.AS: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 14.6/14.6 ok; ev_oi 18.0/18.0 ok; ev_oi_all_cash 17.2/17.2 ok)
- HFG.DE: accepted core_fcf, core_fx, core_ratio, core_shares_diluted (mcap_fcf 2.5/2.4 ok; ev_oi 10.7/n.m. no; ev_oi_all_cash 8.3/n.m. no)
- HLAG.DE: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 30.8/30.8 ok; ev_oi 30.1/30.1 ok; ev_oi_all_cash 26.4/26.4 ok); derived from the quoted figures (not printed as such): core_debt_eq
- IBE.MC: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf n.m./n.m. ok; ev_oi 20.7/20.7 ok; ev_oi_all_cash 20.0/20.0 ok); derived from the quoted figures (not printed as such): core_shares_diluted
- IBM: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 17.0/17.0 ok; ev_oi 22.0/22.0 ok; ev_oi_all_cash 20.9/20.9 ok); derived from the quoted figures (not printed as such): core_debt_eq
- IEX: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 28.0/28.0 ok; ev_oi 27.6/27.6 ok; ev_oi_all_cash 26.7/26.7 ok); derived from the quoted figures (not printed as such): core_debt_eq
- INRN.SW: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 28.9/28.9 ok; ev_oi 16.0/16.0 ok; ev_oi_all_cash 13.5/13.5 ok); derived from the quoted figures (not printed as such): core_shares_diluted
- KBX.DE: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 24.9/24.9 ok; ev_oi 21.7/21.7 ok; ev_oi_all_cash 19.7/19.7 ok); derived from the quoted figures (not printed as such): core_debt_eq
- KEYS: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 51.9/51.9 ok; ev_oi 79.1/79.1 ok; ev_oi_all_cash 76.1/76.1 ok); derived from the quoted figures (not printed as such): core_debt_eq
- KNEBV.HE: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 22.4/22.4 ok; ev_oi 20.1/20.1 ok; ev_oi_all_cash 19.8/19.8 ok); derived from the quoted figures (not printed as such): core_debt_eq
- KRN.DE: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 13.4/13.4 ok; ev_oi 8.8/8.8 ok; ev_oi_all_cash 7.5/7.5 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_debt_eq
- LLY: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 121.6/121.6 ok; ev_oi 43.1/43.1 ok; ev_oi_all_cash 42.9/42.9 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_debt_eq, core_cash
- LULU: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 11.7/11.7 ok; ev_oi 4.9/4.9 ok; ev_oi_all_cash 4.3/4.3 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_debt_eq
- MA: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 28.7/28.6 ok; ev_oi 26.0/25.9 ok; ev_oi_all_cash 25.4/25.3 ok); derived from the quoted figures (not printed as such): core_debt_eq
- MAERSK-B.CO: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 10.7/10.7 ok; ev_oi 20.4/20.4 ok; ev_oi_all_cash 15.0/15.0 ok); derived from the quoted figures (not printed as such): core_debt_eq
- ML.PA: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 12.7/12.5 ok; ev_oi 13.3/13.2 ok; ev_oi_all_cash 11.8/11.7 ok)
- MONC.MI: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 17.4/17.5 ok; ev_oi 15.4/15.4 ok; ev_oi_all_cash 13.8/13.8 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_debt_eq
- MSFT: accepted core_cash, core_debt_eq, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf -/55.0 no; ev_oi 24.6/24.5 ok; ev_oi_all_cash 24.1/24.0 ok)
- MTD: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 35.3/35.3 ok; ev_oi 29.3/29.3 ok; ev_oi_all_cash 29.2/29.2 ok); derived from the quoted figures (not printed as such): core_debt_eq
- NDSN: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 28.3/28.1 ok; ev_oi 28.8/28.7 ok; ev_oi_all_cash 28.7/28.5 ok)
- NOKIA.HE: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 85.4/85.0 ok; ev_oi 55.6/55.6 ok; ev_oi_all_cash 49.8/49.8 ok); derived from the quoted figures (not printed as such): core_debt_eq
- NOLA-B.ST: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 48.7/48.7 ok; ev_oi 14.9/14.9 ok; ev_oi_all_cash 14.4/14.4 ok)
- NOVO-B.CO: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 38.1/38.1 ok; ev_oi 9.8/9.8 ok; ev_oi_all_cash 9.4/9.4 ok)
- OR.PA: the memo prints ev_oi - (assisted read: 'the no-cash variant is not separately computable')
- OR.PA: accepted core_fcf, core_fx, core_ratio, core_shares_diluted (mcap_fcf 28.9/28.9 ok; ev_oi -/- no; ev_oi_all_cash -/- no)
- PDX.ST: accepted core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 23.2/23.2 ok; ev_oi 93.4/93.4 ok; ev_oi_all_cash -/84.0 no); derived from the quoted figures (not printed as such): core_shares_diluted
- PIRC.MI: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 9.1/9.1 ok; ev_oi 11.4/11.4 ok; ev_oi_all_cash 9.6/9.6 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_debt_eq
- PYPL: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 8.3/8.3 ok; ev_oi 9.8/9.8 ok; ev_oi_all_cash 7.9/7.9 ok)
- RACE.MI: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 43.1/43.1 ok; ev_oi 30.1/30.1 ok; ev_oi_all_cash 29.4/29.4 ok); derived from the quoted figures (not printed as such): core_debt_eq
- RI.PA: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 12.5/12.5 ok; ev_oi 13.2/13.2 ok; ev_oi_all_cash 12.3/12.3 ok)
- ROK: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 40.0/40.0 ok; ev_oi 34.1/33.8 ok; ev_oi_all_cash 33.8/- no; the single unlabelled EV/OI 33.8 is the all-cash reading); derived from the quoted figures (not printed as such): core_debt_eq
- RVLV: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 39.6/39.2 ok; ev_oi 24.1/23.8 ok; ev_oi_all_cash 19.9/19.7 ok)
- SAF.PA: the memo prints ev_oi - (assisted read: '-')
- SAF.PA: the memo prints ev_oi_all_cash 32.6 (assisted read: 'EV/OI = 140,361 ÷ 4,308 = 32.6× (résop)')
- SAF.PA: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 36.1/36.1 ok; ev_oi 34.2/- no; ev_oi_all_cash 32.6/32.6 ok); derived from the quoted figures (not printed as such): core_debt_eq
- STMN.SW: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 52.5/52.5 ok; ev_oi 27.7/27.7 ok; ev_oi_all_cash 27.0/27.0 ok); derived from the quoted figures (not printed as such): core_shares_diluted
- SU.PA: accepted core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 37.3/36.8 ok; ev_oi 28.8/28.5 ok; ev_oi_all_cash -/27.8 no)
- SUN.SW: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 25.8/25.8 ok; ev_oi 16.1/16.1 ok; ev_oi_all_cash 14.2/14.2 ok); derived from the quoted figures (not printed as such): core_debt_eq
- SY1.DE: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 24.4/24.4 ok; ev_oi 32.1/32.1 ok; ev_oi_all_cash 30.0/30.0 ok); derived from the quoted figures (not printed as such): core_debt_eq
- TER: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 136.3/136.3 ok; ev_oi 94.6/94.6 ok; ev_oi_all_cash 94.1/94.1 ok)
- TLX.DE: the memo prints mcap_fcf n.m. (assisted read: 'MCap/FCF = 29,102 ÷ 8,373 = 3.5× — n.m.: CFO for an insurer ')
- TLX.DE: the memo prints ev_oi n.m. (assisted read: '(no-cash-excess) — n.m., NCI at book (Appendix C)')
- TLX.DE: the memo prints ev_oi_all_cash n.m. (assisted read: '(no-cash-excess) — n.m., NCI at book (Appendix C)')
- TLX.DE: accepted core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf n.m./n.m. ok; ev_oi n.m./n.m. ok; ev_oi_all_cash n.m./n.m. ok); derived from the quoted figures (not printed as such): core_shares_diluted
- TRI.PA: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 5.6/5.7 ok; ev_oi 9.3/9.3 ok; ev_oi_all_cash 7.6/7.7 ok)
- TXN: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 103.1/103.1 ok; ev_oi 47.0/47.0 ok; ev_oi_all_cash 45.8/45.8 ok); derived from the quoted figures (not printed as such): core_debt_eq
- VC: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 10.1/10.1 ok; ev_oi 10.2/10.2 ok; ev_oi_all_cash 8.2/8.2 ok); derived from the quoted figures (not printed as such): core_debt_eq
- WEIR.L: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 27.0/27.0 ok; ev_oi 19.6/19.6 ok; ev_oi_all_cash 18.7/18.7 ok); derived from the quoted figures (not printed as such): core_debt_eq
- WINA: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 30.3/29.6 ok; ev_oi 26.0/25.4 ok; ev_oi_all_cash 25.5/24.9 ok)
- WMT: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 60.2/60.2 ok; ev_oi 32.8/32.8 ok; ev_oi_all_cash 32.4/32.4 ok); derived from the quoted figures (not printed as such): core_shares_diluted, core_debt_eq
- ZAB.WA: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 12.6/12.6 ok; ev_oi 18.3/18.3 ok; ev_oi_all_cash 17.8/17.8 ok)
- ZBRA: accepted core_cash, core_debt_eq, core_fcf, core_fx, core_oi, core_ratio, core_shares_diluted (mcap_fcf 21.4/21.4 ok; ev_oi 24.0/24.0 ok; ev_oi_all_cash 23.8/23.8 ok)

## Recomputed multiples more than 0.1 from the memo's print at the memo price (basis differences inside the memo; check at the next REVIEW) (19)

- ABEV: at the memo price the accepted core numbers give ev_oi 11.3 vs 11.6; ev_oi_all_cash 10.5 vs 10.7 (memo print)
- SCHN.SW: at the memo price the accepted core numbers give mcap_fcf 19.2 vs 19.5; ev_oi 19.8 vs 20.0; ev_oi_all_cash 16.7 vs 17.0 (memo print)
- 6845.T: at the memo price the accepted core numbers give mcap_fcf 24.3 vs 24.0; ev_oi_all_cash 14.0 vs 13.8 (memo print)
- META: at the memo price the accepted core numbers give mcap_fcf 36.2 vs 35.8; ev_oi 21.4 vs 21.2; ev_oi_all_cash 20.3 vs 20.1 (memo print)
- DCI: at the memo price the accepted core numbers give mcap_fcf 24.5 vs 24.1; ev_oi 19.7 vs 19.4; ev_oi_all_cash 19.3 vs 19.0 (memo print)
- LECO: at the memo price the accepted core numbers give mcap_fcf 28.7 vs 28.0; ev_oi 23.0 vs 22.5; ev_oi_all_cash 22.7 vs 22.2 (memo print)
- ROCK-B.CO: at the memo price the accepted core numbers give mcap_fcf 52.5 vs 52.8; ev_oi_all_cash 37.5 vs 37.7 (memo print)
- FAST: at the memo price the accepted core numbers give mcap_fcf 55.6 vs 55.4 (memo print)
- AAPL: at the memo price the accepted core numbers give mcap_fcf 46.8 vs 45.8; ev_oi 35.6 vs 34.8; ev_oi_all_cash 35.2 vs 34.4 (memo print)
- ABNB: at the memo price the accepted core numbers give mcap_fcf 20.5 vs 19.6; ev_oi 37.9 vs 36.4 (memo print)
- ASML.AS: at the memo price the accepted core numbers give mcap_fcf 50.3 vs 50.1; ev_oi 49.7 vs 49.5; ev_oi_all_cash 48.6 vs 48.8 (memo print)
- BTI: at the memo price the accepted core numbers give mcap_fcf 16.2 vs 16.4 (memo print)
- COST: at the memo price the accepted core numbers give ev_oi 41.7 vs 41.4; ev_oi_all_cash 40.3 vs 39.5 (memo print)
- ML.PA: at the memo price the accepted core numbers give mcap_fcf 12.7 vs 12.5 (memo print)
- NDSN: at the memo price the accepted core numbers give mcap_fcf 28.3 vs 28.1; ev_oi_all_cash 28.7 vs 28.5 (memo print)
- NOKIA.HE: at the memo price the accepted core numbers give mcap_fcf 85.4 vs 85.0 (memo print)
- RVLV: at the memo price the accepted core numbers give mcap_fcf 39.6 vs 39.2; ev_oi 24.1 vs 23.8; ev_oi_all_cash 19.9 vs 19.7 (memo print)
- SU.PA: at the memo price the accepted core numbers give mcap_fcf 37.3 vs 36.8; ev_oi 28.8 vs 28.5 (memo print)
- WINA: at the memo price the accepted core numbers give mcap_fcf 30.3 vs 29.6; ev_oi 26.0 vs 25.4; ev_oi_all_cash 25.5 vs 24.9 (memo print)

## Held positions (4)

- CROX: zone HOLD · ADD band 94 · sell line 431 · last zone check 2026-10-02 · avg cost [redacted] (from the outgoing Portfolio table)
- TROW: zone HOLD · ADD band 55.5 · sell line 268.6 · last zone check 2026-10-02 · avg cost [redacted] (from the outgoing Portfolio table)
- HFG.DE: zone SELL-FLAG SR2 · ADD band n.m. · sell line n.m. · last zone check 2026-10-05 · avg cost [redacted] (from the outgoing Portfolio table)
- NOVO-B.CO: zone SELL-FLAG SR2 · ADD band n.m. · sell line 697 · last zone check 2026-10-05 · avg cost [redacted] (from the outgoing Portfolio table)

## ISIN gaps (190)

- BRK.B: ISIN not established in the memo (no isin field)
- INVE-B.ST: ISIN not established in the memo (n/a — not established this run (backfill owed))
- SGO.PA: ISIN not established in the memo (no isin field)
- CRCT: ISIN not established in the memo (n/a — not retrieved this session; backfill at REVIEW)
- GSK.L: ISIN not established in the memo (no isin field)
- BABA: ISIN not established in the memo (no isin field)
- FIE.DE: ISIN not established in the memo (no isin field)
- BKNG: ISIN not established in the memo (no isin field)
- ESSITY-B.ST: ISIN not established in the memo (no isin field)
- QCOM: ISIN not established in the memo (no isin field)
- ROG.SW: ISIN not established in the memo (no isin field)
- SCHN.SW: ISIN not established in the memo (no isin field)
- NVS: ISIN not established in the memo (no isin field)
- AZA.ST: ISIN not established in the memo (no isin field)
- SDZ.SW: ISIN not established in the memo (no isin field)
- MORN: ISIN not established in the memo (no isin field)
- ADYEN.AS: ISIN not established in the memo (no isin field)
- ULVR.L: ISIN not established in the memo (no isin field)
- THULE.ST: ISIN not established in the memo (no isin field)
- SKF-B.ST: ISIN not established in the memo (no isin field)
- SAVE.ST: ISIN not established in the memo (no isin field)
- SAP.DE: ISIN not established in the memo (no isin field)
- RMS.PA: ISIN not established in the memo (no isin field)
- SAND.ST: ISIN not established in the memo (no isin field)
- CSU.TO: ISIN not established in the memo (no isin field)
- EPI-A.ST: ISIN not established in the memo (no isin field)
- ATCO-B.ST: ISIN not established in the memo (no isin field)
- IBKR: ISIN not established in the memo (no isin field)
- ALFA.ST: ISIN not established in the memo (no isin field)
- AXFO.ST: ISIN not established in the memo (no isin field)
- KNIN.SW: ISIN not established in the memo (no isin field)
- INDT.ST: ISIN not established in the memo (no isin field)
- LIFCO-B.ST: ISIN not established in the memo (no isin field)
- SIKA.SW: ISIN not established in the memo (no isin field)
- HUBN.SW: ISIN not established in the memo (no isin field)
- NESN.SW: ISIN not established in the memo (no isin field)
- MYCR.ST: ISIN not established in the memo (no isin field)
- 2330.TW: ISIN not established in the memo (n/a — not sourced this session; backfill at next REVIEW (queued))
- IFCN.SW: ISIN not established in the memo (no isin field)
- SIE.DE: ISIN not established in the memo (no isin field)
- 005930.KS: ISIN not established in the memo (no isin field)
- 1211.HK: ISIN not established in the memo (no isin field)
- 1913.HK: ISIN not established in the memo (no isin field)
- 1COV.DE: ISIN not established in the memo (no isin field)
- 244920.KS: ISIN not established in the memo (n/a — not retrieved this session (DART/KIND bot-blocked); KRX pattern )
- 2502.T: ISIN not established in the memo (no isin field)
- 5332.T: ISIN not established in the memo (no isin field)
- 6503.T: ISIN not established in the memo (no isin field)
- 688825.SS: ISIN not established in the memo (n/a — not found (quote sources carry none; backfill at next REVIEW))
- 7213.T: ISIN not established in the memo (n/a — not retrieved this session (backfill at next REVIEW))
- 8TRA.ST: ISIN not established in the memo (no isin field)
- AAPL: ISIN not established in the memo (no isin field)
- ABNB: ISIN not established in the memo (no isin field)
- AD.AS: ISIN not established in the memo (no isin field)
- ADS.DE: ISIN not established in the memo (no isin field)
- AKZA.AS: ISIN not established in the memo (no isin field)
- AMRC: ISIN not established in the memo (n/a — not retrieved this session; backfill at REVIEW)
- AMV0.DE: ISIN not established in the memo (no isin field)
- ANGI: ISIN not established in the memo (no isin field)
- ARHS: ISIN not established in the memo (n/a — not retrieved this session; backfill at REVIEW)
- ARQ: ISIN not established in the memo (n/a — not retrieved this session; backfill owed)
- AS: ISIN not established in the memo (n/a — not retrieved this session (Cayman-incorporated NYSE listing); b)
- ASH: ISIN not established in the memo (n/a — not retrieved this session (SEC CIK 0001674862; backfill at next)
- ASML.AS: ISIN not established in the memo (no isin field)
- ASSA-B.ST: ISIN not established in the memo (no isin field)
- AXP: ISIN not established in the memo (no isin field)
- AZTA: ISIN not established in the memo (n/a — not retrieved this session; backfill at REVIEW)
- BAS.DE: ISIN not established in the memo (no isin field)
- BAYN.DE: ISIN not established in the memo (no isin field)
- BBBY: ISIN not established in the memo (n/a — not verified this session; Beyond-era ISIN US08862E1091 to verif)
- BC.MI: ISIN not established in the memo (no isin field)
- BC8.DE: ISIN not established in the memo (no isin field)
- BEI.DE: ISIN not established in the memo (no isin field)
- BH: ISIN not established in the memo (n/a — not retrieved this session; backfill at REVIEW)
- BILI-A.ST: ISIN not established in the memo (no isin field)
- BKE: ISIN not established in the memo (n/a — not retrieved this session (backfill owed at next touch, §7.1a))
- BN.PA: ISIN not established in the memo (no isin field)
- BNR.DE: ISIN not established in the memo (no isin field)
- BOL.ST: ISIN not established in the memo (no isin field)
- BRZE: ISIN not established in the memo (no isin field)
- BTI: ISIN not established in the memo (no isin field)
- CBLL: ISIN not established in the memo (n/a — not retrieved this session; backfill at REVIEW)
- CDI.PA: ISIN not established in the memo (no isin field)
- CELH: ISIN not established in the memo (no isin field)
- CERT: ISIN not established in the memo (n/a — not verified this session (US-listed; backfill at next touch))
- CON.DE: ISIN not established in the memo (no isin field)
- COPN.SW: ISIN not established in the memo (no isin field)
- COST: ISIN not established in the memo (no isin field)
- CRI: ISIN not established in the memo (n/a — not retrieved this session (backfill at first REVIEW))
- CRM: ISIN not established in the memo (no isin field)
- CSG.AS: ISIN not established in the memo (no isin field)
- DEC.PA: ISIN not established in the memo (no isin field)
- DG.PA: ISIN not established in the memo (no isin field)
- DLG.MI: ISIN not established in the memo (no isin field)
- DOCU: ISIN not established in the memo (no isin field)
- DSY.PA: ISIN not established in the memo (no isin field)
- EKTA-B.ST: ISIN not established in the memo (no isin field)
- EL.PA: ISIN not established in the memo (no isin field)
- ELUX-B.ST: ISIN not established in the memo (no isin field)
- ENB.TO: ISIN not established in the memo (no isin field)
- ENOV: ISIN not established in the memo (n/a — not retrieved this session (backfill at first REVIEW))
- ENR.DE: ISIN not established in the memo (no isin field)
- ERIC-B.ST: ISIN not established in the memo (no isin field)
- EVK.DE: ISIN not established in the memo (no isin field)
- EVO.ST: ISIN not established in the memo (no isin field)
- FIG: ISIN not established in the memo (n/a — not retrieved; backfill owed)
- FLUT: ISIN not established in the memo (n/a — not retrieved this session; §7.1a backfill at next REVIEW)
- FRE.DE: ISIN not established in the memo (no isin field)
- FTK.DE: ISIN not established in the memo (no isin field)
- GBF.DE: ISIN not established in the memo (no isin field)
- GEBN.SW: ISIN not established in the memo (no isin field)
- GEN: ISIN not established in the memo (no isin field)
- GETI-B.ST: ISIN not established in the memo (no isin field)
- GRMN: ISIN not established in the memo (no isin field)
- GTLB: ISIN not established in the memo (no isin field)
- HEN3.DE: ISIN not established in the memo (no isin field)
- HHH: ISIN not established in the memo (no isin field)
- HLAG.DE: ISIN not established in the memo (no isin field)
- HLE.DE: ISIN not established in the memo (no isin field)
- HOT.DE: ISIN not established in the memo (no isin field)
- HUBS: ISIN not established in the memo (no isin field)
- HUSQ-B.ST: ISIN not established in the memo (no isin field)
- HYLN: ISIN not established in the memo (n/a — not retrieved this session; backfill at REVIEW)
- IBM: ISIN not established in the memo (no isin field)
- INIO: ISIN not established in the memo (no isin field)
- INPST.AS: ISIN not established in the memo (no isin field)
- KBX.DE: ISIN not established in the memo (no isin field)
- KER.PA: ISIN not established in the memo (no isin field)
- KLAR: ISIN not established in the memo (no isin field)
- KNEBV.HE: ISIN not established in the memo (no isin field)
- KRN.DE: ISIN not established in the memo (no isin field)
- KSPI: ISIN not established in the memo (n/a — not retrieved (third session; backfill queued in TODO))
- KVYO: ISIN not established in the memo (n/a — not verified this session (backfill at commit))
- LIGHT.AS: ISIN not established in the memo (no isin field)
- LIN: ISIN not established in the memo (no isin field)
- LISN.SW: ISIN not established in the memo (no isin field)
- LLY: ISIN not established in the memo (no isin field)
- LOGI: ISIN not established in the memo (no isin field)
- MA: ISIN not established in the memo (no isin field)
- MICC.AS: ISIN not established in the memo (no isin field)
- MONC.MI: ISIN not established in the memo (no isin field)
- MU: ISIN not established in the memo (no isin field)
- NFLX: ISIN not established in the memo (no isin field)
- NOLA-B.ST: ISIN not established in the memo (n/a — not retrieved this session (8 sources attempted; App. A))
- NVDA: ISIN not established in the memo (no isin field)
- ONON: ISIN not established in the memo (no isin field)
- OPEN: ISIN not established in the memo (n/a — not verified this session (backfill at commit))
- OR.PA: ISIN not established in the memo (no isin field)
- ORCL: ISIN not established in the memo (no isin field)
- PAH3.DE: ISIN not established in the memo (no isin field)
- PDX.ST: ISIN not established in the memo (no isin field)
- PHIA.AS: ISIN not established in the memo (no isin field)
- PIRC.MI: ISIN not established in the memo (no isin field)
- PLTR: ISIN not established in the memo (no isin field)
- PSH.L: ISIN not established in the memo (no isin field)
- RACE.MI: ISIN not established in the memo (no isin field)
- ROK: ISIN not established in the memo (no isin field)
- RUSTA.ST: ISIN not established in the memo (no isin field)
- SAF.PA: ISIN not established in the memo (no isin field)
- SAN.PA: ISIN not established in the memo (no isin field)
- SHA0.DE: ISIN not established in the memo (no isin field)
- SHOP: ISIN not established in the memo (no isin field)
- SPCX: ISIN not established in the memo (no isin field)
- SPOT: ISIN not established in the memo (no isin field)
- SRT3.DE: ISIN not established in the memo (no isin field)
- SY1.DE: ISIN not established in the memo (no isin field)
- TEAM: ISIN not established in the memo (no isin field)
- TENB: ISIN not established in the memo (n/a — not verified this session (backfill at commit))
- TKA.DE: ISIN not established in the memo (no isin field)
- TLX.DE: ISIN not established in the memo (no isin field)
- TRNS: ISIN not established in the memo (n/a — not retrieved this session; backfill at REVIEW)
- TRS: ISIN not established in the memo (n/a — not retrieved this session (backfill at first REVIEW))
- TSLA: ISIN not established in the memo (no isin field)
- TTWO: ISIN not established in the memo (no isin field)
- TUI1.DE: ISIN not established in the memo (no isin field)
- U: ISIN not established in the memo (no isin field)
- UFI: ISIN not established in the memo (n/a — conflicting tier-2 candidates (US9646… CUSIP-implied vs US904677)
- UN0.DE: ISIN not established in the memo (no isin field)
- UNH: ISIN not established in the memo (no isin field)
- V: ISIN not established in the memo (no isin field)
- VOW3.DE: ISIN not established in the memo (no isin field)
- VSURE.ST: ISIN not established in the memo (n/a — not established this run (not printed in AR 2025, Q2 2026 report)
- WEN: ISIN not established in the memo (n/a — not retrieved this session (backfill at first REVIEW))
- WINA: ISIN not established in the memo (n/a — not retrieved this session (backfill at first REVIEW))
- XPEL: ISIN not established in the memo (n/a — not retrieved this session; backfill at REVIEW)
- XRAY: ISIN not established in the memo (n/a — not retrieved this session (backfill at next REVIEW, §7.1a))
- ZIP: ISIN not established in the memo (no isin field)
- ZM: ISIN not established in the memo (no isin field)
- EA: ISIN not established in the memo (no isin field)
- SYAB.DE: ISIN not established in the memo (no isin field)

## Past level sources (121)

- CROX: past 21% ROCE from 'Worst-of-four 10y normalized ROCE 21.0%'
- SGO.PA: past 10.1% ROCE from 'Worst-of-four normalized ROCE 10.07%'
- CRCT: past 12.6% ROCE from 'Worst-of-four normalized ROCE 12.64%'
- 6626.T: past 14.6% ROCE from 'Worst-of-four normalized ROCE 14.6%'
- GSK.L: past 14.5% ROCE from 'Worst-of-four pooled ROCE ≈ 14.5%'
- TROW: past 23.9% ROCE from 'Worst-of-four normalized ROCE 23.9%'
- FIE.DE: past 14.9% ROCE from 'Worst-of-four normalized average ROCE 14.9%'
- INTU: past 15.7% ROCE from 'worst-of-four normalized ROCE moves 15.7%'
- KCR.HE: past 10% ROCE from 'Worst-of-four normalized ROCE is 10.0%'
- IP.MI: past 13.1% ROCE from 'Worst-of-four normalized ROCE is 13.1%'
- ESSITY-B.ST: past 10.3% ROCE from 'worst-of-four ten-year ROCE 10.32%'
- KALMAR.HE: past 14.3% ROCE from 'Worst-of-four normalized ROCE is 14.3%'
- MC.PA: past 14.1% ROCE from 'Worst-of-four normalized ROCE is 14.1%'
- RBREW.CO: past 16.3% ROCE from 'Worst-of-four normalized ROCE 16.3%'
- 6758.T: past 10% ROCE from 'worst-of-four normalized ROCE 10.0%'
- ANDR.VI: past 10.9% ROCE from 'Worst-of-four normalized ROCE is 10.9%'
- FDS: past 21% ROCE from 'worst-of-four ROCE around 21%'
- BRG.OL: past 14.4% ROCE from 'Worst-of-four normalized ROCE is 14.4%'
- SNA: past 18.9% ROCE from 'Worst-of-four normalized ROCE is 18.9%'
- BVI.PA: past 15.2% ROCE from 'Worst-of-four normalized ROCE is 15.15%'
- ROG.SW: past 21% ROCE from 'worst-of-four ROCE, ~21%'
- SCHN.SW: past 20.5% ROCE from 'Worst-of-four normalized ROCE 20.5%'
- 6841.T: past 10.8% ROCE from 'Worst-of-four normalized ROCE is 10.8%'
- NVS: past 15.6% ROCE from 'worst-of-four normalized-average ROCE 15.6%'
- BMI: past 18.9% ROCE from 'worst-of-four average ROCE is 18.9%'
- MORN: past 13.2% ROCE from 'Worst-of-four normalized ROCE 13.2%'
- 6845.T: past 13% ROCE from 'worst-of-four normalized ROCE is 13.0%'
- ULVR.L: past 18.2% ROCE from 'worst-of-four 10-year ROCE of 18.2%'
- DOV: past 12% ROCE from 'worst-of-four average ROCE is 12.0%'
- COLO-B.CO: past 18.7% ROCE from 'worst-of-four normalized ROCE 18.67%'
- THULE.ST: past 16.6% ROCE from 'Worst-of-four normalized ROCE 16.6%'
- META: past 24.7% ROCE from 'Worst-of-four normalised ROCE 24.7%'
- DCI: past 20.4% ROCE from 'worst-of-four normalized ROCE is 20.4%'
- SKF-B.ST: past 11.3% ROCE from 'Worst-of-four normalized ROCE 11.3%'
- NMAN.ST: past 10.6% ROCE from 'Worst-of-four normalized ROCE is 10.6%'
- TRI: past 11.1% ROCE from 'worst-of-four normalized ROCE ~11.1%'
- METSO.HE: past 12.4% ROCE from 'Worst-of-four normalized ROCE is 12.4%'
- SAVE.ST: past 29.2% ROE from 'Worst-of-four normalized ROE 29.2%'
- LECO: past 20.8% ROCE from 'worst-of-four normalized ROCE is 20.8%'
- RMS.PA: past 29.8% ROCE from 'Worst-of-four normalized ROCE 29.8%'
- SOON.SW: past 13.9% ROCE from 'worst-of-four ROCE of 13.9%'
- SAND.ST: past 14% ROCE from 'Worst-of-four normalized ROCE 14.0%'
- CSU.TO: past 17.2% ROCE from 'worst-of-four normalized-average ROCE ≈17.2%'
- EPI-A.ST: past 18.4% ROCE from 'Worst-of-four normalized ROCE 18.4%'
- WTS: past 16% ROCE from 'Worst-of-four normalized ROCE 16.0%'
- 7974.T: past 16.2% ROCE from 'Worst-of-four normalized average ROCE 16.2%'
- ATCO-B.ST: past 24.6% ROCE from 'worst-of-four 10y ROCE 24.6%'
- 7936.T: past 12.8% ROCE from 'Worst-of-four normalized ROCE 12.8%'
- ALFA.ST: past 12.5% ROCE from 'Worst-of-four normalized ROCE 12.5%'
- AXFO.ST: past 16.6% ROCE from 'worst-of-four ROCE 16.6%'
- KNIN.SW: past 23.1% ROCE from 'worst-of-four 10-year ROCE and FCFROCE both 23.1%'
- INDT.ST: past 14.1% ROCE from 'worst-of-four normalized ROCE 14.1%'
- LIFCO-B.ST: past 14.4% ROCE from 'Worst-of-four normalized ROCE 14.4%'
- LR.PA: past 11.6% ROCE from 'Worst-of-four normalized ROCE 11.62%'
- AME: past 12.6% ROCE from 'worst-of-four average ROCE is 12.6%'
- HUBN.SW: past 12.3% ROCE from 'Worst-of-four normalized ROCE 12.3%'
- AMZN: past 11.1% ROCE from 'Worst-of-four normalized average ROCE is 11.1%'
- 3064.T: past 28.4% ROCE from 'worst-of-four normalized ROCE is 28.4%'
- CRL.MI: past 13.9% ROCE from 'Worst-of-four normalized ROCE is 13.9%'
- 6861.T: past 17.7% ROCE from 'worst-of-four normalized ROCE is 17.7%'
- DNP.WA: past 22.1% ROCE from 'Worst-of-four normalized ROCE 22.1%'
- NESN.SW: past 12.6% ROCE from 'Worst-of-four normalized ROCE 12.6%'
- FAST: past 34.3% ROCE from 'worst-of-four normalized ROCE is 34.3%'
- MYCR.ST: past 24.5% ROCE from 'Worst-of-four normalized ROCE 24.5%'
- 2330.TW: past 23.3% ROCE from 'Worst-of-four normalized average ROCE 23.3%'
- RSW.L: past 13.7% ROCE from 'Worst-of-four normalized ROCE is 13.7%'
- HMS.ST: past 16.1% ROCE from 'Worst-of-four normalized ROCE is 16.1%'
- HEI: past 12.6% ROCE from 'Worst-of-four normalized ROCE is 12.6%'
- IFCN.SW: past 22.2% ROCE from 'Worst-of-four normalised ROCE 22.2%'
- 005930.KS: past 10.6% ROCE from 'Worst-of-four 10y normalized ROCE is 10.6%'
- 300750.SZ: past 10.9% ROCE from 'worst-of-four ROCE 10.9%'
- 6383.T: past 14.6% ROCE from 'Worst-of-four normalized ROCE is 14.6%'
- AAPL: past 33.2% ROCE from 'worst-of-four 10-year ROCE of 33.2%'
- ABB: past 13.2% ROCE from 'Worst-of-four normalized ROCE is 13.2%'
- ANF: past 10.8% ROCE from 'Worst-of-four normalized ROCE 10.77%'
- APH: past 18.1% ROCE from 'Worst-of-four ROCE is 18.1%'
- BKE: past 32.7% ROCE from 'Worst-of-four normalized ROCE is 32.7%'
- BOL.ST: past 14.1% ROCE from 'Worst-of-four normalized ten-year ROCE is 14.1%'
- CDR.WA: past 19.3% ROCE from 'Worst-of-four normalized ROCE 19.3%'
- CGNX: past 12% ROCE from 'Worst-of-four normalized ROCE is 12.0%'
- COST: past 19.3% ROCE from 'worst-of-four ROCE 19.3%'
- DLG.MI: past 13.3% ROCE from 'Worst-of-four normalized ROCE 13.3%'
- EVO.ST: past 24.6% ROCE from 'worst-of-four ten-year ROCE of 24.6%'
- FQT.VI: past 11.1% ROCE from 'Worst-of-four normalized ROCE is 11.1%'
- GEBN.SW: past 25.9% ROCE from 'worst-of-four normalized ROCE 25.9%'
- GGG: past 23.5% ROCE from 'worst-of-four average ROCE is 23.5%'
- GOOGL: past 22.7% ROCE from 'Worst-of-four normalized ROCE 22.7%'
- GRMN: past 17.4% ROCE from 'Worst-of-four normalized ROCE 17.4%'
- HLAG.DE: past 17.8% ROCE from 'worst-of-four ROCE of 17.8%'
- KEYS: past 11.1% ROCE from 'Worst-of-four normalized ROCE is 11.1%'
- KNEBV.HE: past 29.5% ROCE from 'worst-of-four normalized ROCE ≈ 29.5%'
- LISN.SW: past 19% ROCE from 'worst-of-four normalized ROCE ≈ 19%'
- LLY: past 19% ROCE from 'Worst-of-four normalized average ROCE 19.0%'
- LOGI: past 27.2% ROCE from 'Worst-of-four normalized averages: ROCE 27.2%'
- LULU: past 33.1% ROCE from 'Worst-of-four ROCE 33.1%'
- MA: past 42.7% ROCE from 'worst-of-four ROCE 42.7%'
- MAERSK-B.CO: past 10.8% ROCE from 'Worst-of-four normalized ROCE ≈ 10.8%'
- MIPS.ST: past 26% ROCE from 'Worst-of-four normalized ROCE is 26.0%'
- MONC.MI: past 17.8% ROCE from 'worst-of-four normalized ROCE 17.8%'
- MSFT: past 24.7% ROCE from 'Worst-of-four normalized average ROCE 24.7%'
- MTD: past 39.9% ROCE from 'Worst-of-four normalized ROCE is 39.9%'
- MU: past 10.7% ROCE from 'Worst-of-four 10y normalized ROCE 10.7%'
- NFLX: past 14.9% ROCE from 'Worst-of-four normalized-average ROCE is 14.9%'
- NOLA-B.ST: past 15.1% ROCE from 'Worst-of-four 10-year normalized ROCE 15.1%'
- NOVO-B.CO: past 56% ROCE from 'Worst-of-four normalized ROCE 56.0%'
- NVDA: past 58.2% ROCE from 'Worst-of-four normalized averages: ROCE 58.2%'
- OR.PA: past 16.6% ROCE from 'Worst-of-four normalized ROCE 16.6%'
- PDX.ST: past 25.3% ROCE from 'worst-of-four ROCE 25.3%'
- PYPL: past 13.2% ROCE from 'Worst-of-four normalized ROCE is 13.2%'
- RACE.MI: past 23.6% ROCE from 'worst-of-four ROCE 23.6%'
- SAF.PA: past 9.9% ROCE from 'Worst-of-four normalised ROCE 9.9%'
- STMN.SW: past 19% ROCE from 'Worst-of-four normalized averages: ROCE 19.0%'
- SU.PA: past 10.4% ROCE from 'Worst-of-four normalized 10y ROCE 10.4%'
- TLX.DE: past 11.4% ROE from 'worst-of-four normalized ROE 11.4%'
- TRI.PA: past 18.2% ROCE from 'Worst of the four normalized averages: ROCE 18.24%'
- TXN: past 30.2% ROCE from 'Worst-of-four average ROCE is 30.2%'
- V: past 21.9% ROCE from 'worst-of-four 10-year ROCE 21.9%'
- VC: past 10.7% ROCE from 'Worst-of-four normalized ROCE 10.68%'
- WMT: past 15% ROCE from 'Worst-of-four ROCE 15.0%'
- ZBRA: past 11% ROCE from 'worst-of-four normalized ROCE of ≈11%'
- EA: past 14.7% ROCE from 'Worst-of-four 10y normalized ROCE 14.7%'

## Assisted rows rejected (0)

None.

## Owed fields per key

| Key | Section | Px source | Core | Owed |
|---|---|---|---|---|
| 6626.T | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| CROX | WATCH · held | SWEEP 2026-10-05 | rebuild-assisted | none |
| SGO.PA | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, core_period, core_oi_basis, core_fcf_basis |
| TROW | WATCH · held | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| ABEV | WATCH | SWEEP 2026-10-05 | rebuild-assisted | mcap_fcf, core_period, core_oi_basis, core_fcf, core_fcf_basis |
| GSK.L | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, model_version, core_fcf_basis |
| ADBE | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| ESSITY-B.ST | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin |
| RBREW.CO | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| FIE.DE | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, model_version |
| KALMAR.HE | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| IP.MI | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| BRG.OL | WATCH | SWEEP 2026-10-05 | rebuild-assisted | sf_reason, core_period, core_oi_basis, core_fcf_basis |
| MC.PA | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| NMAN.ST | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| CRCT | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, core_period, core_oi_basis, core_fcf_basis |
| ROG.SW | WATCH | memo | rebuild-assisted | isin, model_version, core_fcf_basis |
| KCR.HE | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| INTU | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| 6841.T | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| FDS | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| BVI.PA | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| THULE.ST | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, model_version |
| ANDR.VI | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| SNA | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| BKNG | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, core_period, core_oi_basis, core_fcf_basis |
| 6845.T | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| COLO-B.CO | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_oi_basis, core_fcf_basis |
| DNP.WA | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| ULVR.L | WATCH | memo | - | isin, model_version, trigger, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| 0700.HK | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_fx_date |
| MORN | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin |
| 6758.T | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| NVS | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, model_version, core_period, core_oi_basis, core_fcf_basis |
| QCOM | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, past_reason, core_period, core_oi_basis, core_fcf_basis |
| SKF-B.ST | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, model_version, core_period, core_oi_basis, core_fcf_basis |
| AXFO.ST | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, model_version, core_period, core_oi_basis, core_fcf_basis |
| DCI | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| BMI | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| SCHN.SW | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, core_period, core_oi_basis, core_fcf_basis |
| DOV | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| NESN.SW | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin |
| RMS.PA | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin |
| METSO.HE | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| 7936.T | WATCH | SWEEP 2026-10-05 | rebuild-assisted | sf_reason |
| TRI | WATCH | SWEEP 2026-10-05 | rebuild-assisted | none |
| ALFA.ST | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, core_period, core_oi_basis, core_fcf_basis |
| 3064.T | WATCH | SWEEP 2026-10-05 | rebuild-assisted | mcap_fcf, core_period, core_oi_basis, core_fcf, core_fcf_basis |
| BA.L | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_oi_basis, core_fcf_basis |
| SIKA.SW | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, core_period, core_oi_basis, core_fcf_basis |
| LECO | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| SAP.DE | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin |
| SAND.ST | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin |
| META | WATCH | SWEEP 2026-10-05 | rebuild-assisted | none |
| ADYEN.AS | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, model_version |
| KNIN.SW | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, model_version, ev_oi_all_cash, core_period, core_cash, core_oi_basis, core_fcf_basis |
| SOON.SW | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| 7974.T | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| LR.PA | WATCH | SWEEP 2026-10-05 | rebuild-assisted | none |
| CSU.TO | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, model_version, core_fcf_basis, core_fx_date |
| AME | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| INDT.ST | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, model_version |
| EPI-A.ST | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin |
| WTS | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| SIE.DE | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, past_reason, core_period, core_oi_basis, core_fcf_basis |
| ATCO-B.ST | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin |
| LIFCO-B.ST | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, model_version |
| ROCK-B.CO | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_fcf_basis, core_fx_date |
| IBKR | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, past_reason, model_version, mcap_fcf, ev_oi_all_cash, core_period, core_cash, core_oi_basis, core_fcf, core_fcf_basis |
| RSW.L | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| 6861.T | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| 2330.TW | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, core_period, core_oi_basis, core_fcf_basis |
| FAST | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| MYCR.ST | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, ev_oi_all_cash, core_period, core_cash, core_oi_basis, core_fcf_basis |
| AMZN | WATCH | SWEEP 2026-10-05 | rebuild-assisted | sf_reason, core_period, core_oi_basis, core_fcf_basis |
| HUBN.SW | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, ev_oi_all_cash, core_period, core_cash, core_oi_basis, core_fcf_basis |
| HEI | WATCH | SWEEP 2026-10-05 | rebuild-assisted | none |
| HMS.ST | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| CRL.MI | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| IFCN.SW | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, model_version, core_fcf_basis, core_fx_date |
| 8002.T | WATCH | SWEEP 2026-10-05 | rebuild-assisted | core_debt_eq, core_cash, core_fcf_basis |
| AZA.ST | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, model_version, core_debt_eq, core_cash |
| BRK.B | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, past_reason, model_version, core_debt_eq, core_cash, core_fcf_basis |
| INVE-B.ST | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, core_period, core_debt_eq, core_cash |
| NU | WATCH | SWEEP 2026-10-05 | rebuild-assisted | past_reason, core_period, core_debt_eq, core_cash |
| SAVE.ST | WATCH | SWEEP 2026-10-05 | rebuild-assisted | isin, mcap_fcf, core_period, core_debt_eq, core_cash, core_fcf, core_fcf_basis |
| BABA | WATCH | SWEEP 2026-10-05 | - | isin, past_reason, model_version, mcap_fcf, ev_oi, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| SDZ.SW | WATCH | SWEEP 2026-10-05 | - | isin, past_reason, model_version, trigger, mcap_fcf, ev_oi, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| LULU | AVOID-1 | memo | rebuild-assisted | px_date, core_period, core_oi_basis, core_fcf_basis |
| EQNR | AVOID-1 | memo | rebuild-assisted | mcap_fcf, core_period, core_oi_basis, core_fcf, core_fcf_basis |
| BBWI | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| KSPI | AVOID-1 | memo | - | isin, sf_reason, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| KRN.DE | AVOID-1 | memo | rebuild-assisted | isin, model_version, core_period, core_oi_basis, core_fcf_basis |
| ANF | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| TRI.PA | AVOID-1 | memo | rebuild-assisted | sf_reason, core_period, core_oi_basis, core_fcf_basis |
| PYPL | AVOID-1 | memo | rebuild-assisted | px_date, core_period, core_oi_basis, core_fcf_basis |
| VC | AVOID-1 | memo | rebuild-assisted | core_fcf_basis |
| 7751.T | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| PIRC.MI | AVOID-1 | memo | rebuild-assisted | isin, core_period, core_oi_basis, core_fcf_basis |
| 1913.HK | AVOID-1 | memo | rebuild-assisted | isin, model_version |
| HOG | AVOID-1 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| BTI | AVOID-1 | memo | rebuild-assisted | isin, past_reason, model_version, core_fcf_basis |
| RI.PA | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| ML.PA | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| BC8.DE | AVOID-1 | memo | rebuild-assisted | isin, model_version, core_period, core_oi_basis, core_fcf_basis |
| DLG.MI | AVOID-1 | memo | rebuild-assisted | isin, model_version, px_date, core_period, core_oi_basis, core_fcf_basis |
| AD.AS | AVOID-1 | memo | rebuild-assisted | isin, model_version, core_period, core_oi_basis, core_fcf_basis |
| 6301.T | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| NOLA-B.ST | AVOID-1 | memo | rebuild-assisted | isin, core_period, core_oi_basis, core_fcf_basis |
| ACP.WA | AVOID-1 | memo | rebuild-assisted | mcap_fcf, core_period, core_oi_basis, core_fcf, core_fcf_basis |
| MONC.MI | AVOID-1 | memo | rebuild-assisted | isin, model_version, core_period, core_oi_basis, core_fcf_basis |
| 5108.T | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| INRN.SW | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| SUN.SW | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| ALIG.ST | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| CARL-B.CO | AVOID-1 | memo | rebuild-assisted | core_fcf_basis |
| DBX | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| G1A.DE | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| 6367.T | AVOID-1 | memo | rebuild-assisted | sf_reason, core_period, core_oi_basis, core_fcf_basis |
| HEIA.AS | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| ZAB.WA | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| 6702.T | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| BNR.DE | AVOID-1 | memo | rebuild-assisted | isin, model_version, px_date, core_fcf_basis |
| ASSA-B.ST | AVOID-1 | memo | rebuild-assisted | isin, model_version, px_date, core_period, core_oi_basis, core_fcf_basis |
| GGG | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| WEIR.L | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| GETI-B.ST | AVOID-1 | memo | rebuild-assisted | isin, model_version, core_period, core_oi_basis, core_fcf_basis |
| KNEBV.HE | AVOID-1 | memo | rebuild-assisted | isin, core_period, core_oi_basis, core_fcf_basis |
| MAERSK-B.CO | AVOID-1 | memo | rebuild-assisted | core_fcf_basis |
| IBE.MC | AVOID-1 | memo | rebuild-assisted | core_fcf_basis |
| ALE.WA | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| DLB | AVOID-1 | memo | rebuild-assisted | core_fcf_basis |
| KBX.DE | AVOID-1 | memo | rebuild-assisted | isin, model_version, core_period, core_oi_basis, core_fcf_basis |
| IBM | AVOID-1 | memo | rebuild-assisted | isin, model_version, px_date, core_fcf_basis |
| 6383.T | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| FORTUM.HE | AVOID-1 | memo | rebuild-assisted | sf_reason, core_period, core_oi_basis, core_fcf_basis |
| 6501.T | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| ZBRA | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| 6273.T | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| RVLV | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| LISN.SW | AVOID-1 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| MSFT | AVOID-1 | memo | rebuild-assisted | mcap_fcf, core_period, core_oi_basis, core_fcf, core_fcf_basis |
| GEBN.SW | AVOID-1 | memo | rebuild-assisted | isin, core_period, core_oi_basis, core_fcf_basis |
| 300750.SZ | AVOID-1 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| MA | AVOID-1 | memo | rebuild-assisted | isin, model_version, core_period, core_oi_basis, core_fcf_basis |
| WINA | AVOID-1 | memo | rebuild-assisted | isin, past_reason, core_period, core_oi_basis, core_fcf_basis |
| ENB.TO | AVOID-1 | memo | rebuild-assisted | isin, model_version, core_fcf_basis |
| IEX | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| STMN.SW | AVOID-1 | memo | rebuild-assisted | core_fcf_basis |
| ONON | AVOID-1 | memo | - | isin, model_version, trigger, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| NDSN | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| SU.PA | AVOID-1 | memo | rebuild-assisted | ev_oi_all_cash, core_period, core_cash, core_oi_basis, core_fcf_basis |
| 6506.T | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| MTD | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| HLAG.DE | AVOID-1 | memo | rebuild-assisted | isin, model_version, px_date, core_fcf_basis |
| RACE.MI | AVOID-1 | memo | rebuild-assisted | isin, core_fcf_basis |
| GRMN | AVOID-1 | memo | rebuild-assisted | isin, core_fcf_basis |
| ABB | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| AS | AVOID-1 | memo | rebuild-assisted | isin, core_period, core_oi_basis, core_fcf_basis |
| SY1.DE | AVOID-1 | memo | rebuild-assisted | isin, model_version, px_date, core_fcf_basis |
| WMT | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| 6954.T | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| ROK | AVOID-1 | memo | rebuild-assisted | isin, core_fcf_basis |
| SAF.PA | AVOID-1 | memo | rebuild-assisted | isin, core_fcf_basis |
| NEE | AVOID-1 | memo | - | sf_reason, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| AAPL | AVOID-1 | memo | rebuild-assisted | isin, model_version, px_date, core_period, core_oi_basis, core_fcf_basis |
| SRE | AVOID-1 | memo | - | sf_reason, next_review_short, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| ABNB | AVOID-1 | memo | rebuild-assisted | isin, px_date, ev_oi_all_cash, core_cash, core_fcf_basis |
| HEXA-B.ST | AVOID-1 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| APH | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| COST | AVOID-1 | memo | rebuild-assisted | isin, px_date, core_period, core_oi_basis, core_fcf_basis |
| LLY | AVOID-1 | memo | rebuild-assisted | isin, model_version, px_date |
| 005930.KS | AVOID-1 | memo | rebuild-assisted | isin, model_version, core_fcf_basis |
| TXN | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| ASML.AS | AVOID-1 | memo | rebuild-assisted | isin, core_period, core_oi_basis, core_fcf_basis |
| CDR.WA | AVOID-1 | memo | rebuild-assisted | core_fcf_basis |
| NOKIA.HE | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| CON.DE | AVOID-1 | memo | rebuild-assisted | isin, model_version, core_fcf_basis |
| KEYS | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| PDX.ST | AVOID-1 | memo | rebuild-assisted | isin, model_version, ev_oi_all_cash, core_period, core_cash, core_oi_basis, core_fcf_basis |
| TER | AVOID-1 | memo | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| EKTA-B.ST | AVOID-1 | memo | rebuild-assisted | isin, model_version, core_fcf_basis |
| ABCA.PA | AVOID-1 | memo | rebuild-assisted | sf_reason, mcap_fcf, core_period, core_debt_eq, core_cash, core_fcf, core_fcf_basis |
| ARQ | AVOID-1 | memo | - | isin, sf_reason, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| PSH.L | AVOID-1 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| S | AVOID-1 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| TLX.DE | AVOID-1 | memo | rebuild-assisted | isin, model_version, core_period, core_debt_eq, core_cash |
| FTK.DE | AVOID-1 | memo | rebuild-assisted | isin, past_reason, sf_reason, model_version, ev_oi, ev_oi_all_cash, core_period, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf_basis |
| HLN.L | AVOID-1 | memo | - | mcap_fcf, ev_oi, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| OR.PA | AVOID-1 | memo | rebuild-assisted | isin, ev_oi, ev_oi_all_cash, core_period, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf_basis |
| WISE.L | AVOID-1 | memo | - | px, px_date, trigger, mcap_fcf, ev_oi, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| TUI1.DE | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| ERIC-B.ST | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| 7213.T | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| LIGHT.AS | AVOID-2 | memo | - | isin, model_version, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| ANGI | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| NOVO-B.CO | AVOID-2 · held | SWEEP 2026-10-05 | rebuild-assisted | core_period, core_oi_basis, core_fcf_basis |
| BKE | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| EVO.ST | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| PKN.WA | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| EDEN.PA | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| PVH | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| NOMD | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| CSG.AS | AVOID-2 | memo | - | isin, model_version, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| GEN | AVOID-2 | memo | - | isin, model_version, px_date, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| HUSQ-B.ST | AVOID-2 | memo | - | isin, model_version, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| DG.PA | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| BOL.ST | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| GAP | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| APTV | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| AKZA.AS | AVOID-2 | memo | - | isin, model_version, px_date, next_review_short, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| GBF.DE | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| MMB.PA | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| BEI.DE | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| WHR | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| SW.PA | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| WEN | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| FR.PA | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| 2502.T | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| CDI.PA | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| ABM | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| FRE.DE | AVOID-2 | memo | - | isin, model_version, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| 244920.KS | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| SAN.PA | AVOID-2 | memo | - | isin, model_version, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| 3382.T | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| RHIM.L | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| ELUX-B.ST | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| NKE | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| KEX | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| CRI | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| CPR.MI | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| PTC | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| BILI-A.ST | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| ADS.DE | AVOID-2 | memo | - | isin, model_version, trigger, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| PAYO | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| RUSTA.ST | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| CRM | AVOID-2 | memo | - | isin, past_reason, model_version, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| DEC.PA | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| RCO.PA | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| LOGI | AVOID-2 | memo | - | isin, model_version, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| DSY.PA | AVOID-2 | memo | - | isin, model_version, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| EVK.DE | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| UN0.DE | AVOID-2 | memo | - | isin, model_version, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| BN.PA | AVOID-2 | memo | - | isin, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| FQT.VI | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| PHIA.AS | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| MICC.AS | AVOID-2 | memo | - | isin, sf_reason, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| DGE.L | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| WAY | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| ZM | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| UNH | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| TDY | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| NFLX | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| 5332.T | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| ORCL | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| PTON | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| COTY | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| INPST.AS | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| 1211.HK | AVOID-2 | memo | - | isin, model_version, trigger, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| HOT.DE | AVOID-2 | memo | - | isin, model_version, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| EL.PA | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| GPN | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| 6503.T | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| GRND | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| 7309.T | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| KER.PA | AVOID-2 | memo | - | isin, model_version, px_date, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| BC.MI | AVOID-2 | memo | - | isin, model_version, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| V | AVOID-2 | memo | - | isin, model_version, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| HLE.DE | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| LIN | AVOID-2 | memo | - | isin, model_version, px_date, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| 6268.T | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| TRIP | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| 6645.T | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| DOCU | AVOID-2 | memo | - | isin, model_version, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| GOOGL | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| 7011.T | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| RRTL.DE | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| HHH | AVOID-2 | memo | - | isin, model_version, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| VOW3.DE | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| NVDA | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| CAT | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| BAS.DE | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| MGNI | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| SPOT | AVOID-2 | memo | - | isin, model_version, trigger, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| AUTO.OL | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| WWD | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| VSURE.ST | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| SHOO | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| FLUT | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| 6752.T | AVOID-2 | memo | - | sf_reason, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| SMSH.TA | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| TRS | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| DUOL | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| NESTE.HE | AVOID-2 | memo | - | sf_reason, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| NOVT | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| ENR.DE | AVOID-2 | memo | - | isin, model_version, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| BOX | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| WDAY | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| CGNX | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| MIPS.ST | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| CELH | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| CERT | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| INIO | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| SHA0.DE | AVOID-2 | memo | - | isin, model_version, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| SHOP | AVOID-2 | memo | - | isin, model_version, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| CALX | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| UPST | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| MU | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| PATH | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| OKTA | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| ATKR | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| PLTR | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| FRSH | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| TWLO | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| PANW | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| 6324.T | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| TKA.DE | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| TSLA | AVOID-2 | memo | - | isin, model_version, px_date, ev_oi_all_cash, next_review_short, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| HUBS | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| 1COV.DE | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| AIP | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| AMV0.DE | AVOID-2 | memo | - | isin, model_version, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| ASH | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| AXP | AVOID-2 | memo | - | isin, past_reason, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| BAYN.DE | AVOID-2 | memo | - | isin, model_version, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| BBBY | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| BRZE | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| CC | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| COHU | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| COMP | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| COPN.SW | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| COUR | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| CRWD | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| DCO | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| DDOG | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| ENOV | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| FIG | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| FSLY | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| FTRE | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| GTLB | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| KLAR | AVOID-2 | memo | - | isin, model_version, px_date, mcap_fcf, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| KVYO | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| KWY | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| LMND | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| LYFT | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| MBLY | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| NGVT | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| OPEN | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| PAH3.DE | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| RUN | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| SEE.L | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| SNOW | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| SONO | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| SOUN | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| SYM | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| TDOC | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| TEAM | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| TENB | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| TTWO | AVOID-2 | memo | - | isin, model_version, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| U | AVOID-2 | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| UAA | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| UFI | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| WRBY | AVOID-2 | memo | - | core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| XRAY | AVOID-2 | memo | - | isin, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| ZIP | AVOID-2 | memo | - | isin, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| ZIP.AX | AVOID-2 | memo | - | mcap_fcf, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| 688825.SS | AVOID-2 | memo | - | isin, ev_oi, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| 8TRA.ST | AVOID-2 | memo | - | isin, model_version, px, px_date, mcap_fcf, ev_oi, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| AMRC | AVOID-2 | memo | - | isin, mcap_fcf, ev_oi, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| ARHS | AVOID-2 | memo | - | isin, mcap_fcf, ev_oi, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| AZTA | AVOID-2 | memo | - | isin, mcap_fcf, ev_oi, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| BH | AVOID-2 | memo | - | isin, mcap_fcf, ev_oi, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| CBLL | AVOID-2 | memo | - | isin, mcap_fcf, ev_oi, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| HEN3.DE | AVOID-2 | memo | - | isin, past_reason, model_version, mcap_fcf, ev_oi, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| HFG.DE | AVOID-2 · held | SWEEP 2026-10-05 | rebuild-assisted | ev_oi, ev_oi_all_cash, core_period, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf_basis |
| HYLN | AVOID-2 | memo | - | isin, mcap_fcf, ev_oi, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| NET | AVOID-2 | memo | - | mcap_fcf, ev_oi, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| ORSTED.CO | AVOID-2 | memo | - | mcap_fcf, ev_oi, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| SPCX | AVOID-2 | memo | - | isin, model_version, mcap_fcf, ev_oi, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| SRT3.DE | AVOID-2 | memo | - | isin, model_version, px_date, mcap_fcf, ev_oi, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| TRNS | AVOID-2 | memo | - | isin, mcap_fcf, ev_oi, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| XPEL | AVOID-2 | memo | - | isin, mcap_fcf, ev_oi, ev_oi_all_cash, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| EA | DNAF | memo | - | isin, model_version, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |
| SYAB.DE | DNAF | memo | - | isin, model_version, px, px_date, core_period, core_currency, core_unit, core_shares_diluted, core_debt_eq, core_cash, core_oi, core_oi_basis, core_fcf, core_fcf_basis, core_fx, core_fx_date, core_ratio |

## Appendix — assisted file (verbatim)

Each row carries a verbatim memo quote; the rebuild re-checks every quote and every core number.

```csv
key,field,value,quote
005930.KS,core_cash,125847,"EV/OI = 1,881,197 / 43,601 = 43.1× (all-cash) and 2,007,044 / 43,601 = 46.0× (no-cash)"
005930.KS,core_currency,KRW,-
005930.KS,core_debt_eq,37246,"7×OI conservative (no-cash EV) → (7 × 43,601 − 25,239 − 12,007) = ₩267,961bn"
005930.KS,core_fcf,33162,"MCap/FCF = 1,969,798 / 33,162 = 59.4×"
005930.KS,core_fx,1,-
005930.KS,core_fx_date,n.m.,-
005930.KS,core_oi,43601,"EV/OI = 1,881,197 / 43,601 = 43.1× (all-cash) and 2,007,044 / 43,601 = 46.0× (no-cash)"
005930.KS,core_oi_basis,FY2025 reported,-
005930.KS,core_period,FY2025; ordinary-equivalent count (preference at the observed 0.669 price ratio),-
005930.KS,core_ratio,1,-
005930.KS,core_shares_diluted,6364.5,"effective count 6,364.5M ord-equivalents"
005930.KS,core_unit,bn,-
005930.KS,future_reason,2+ forces,"Forces: customer power STRONG (commodity memory, zero switching costs"
0700.HK,core_cash,422552,"all-cash = − 422,552 = 3,962,292"
0700.HK,core_currency,CNY,-
0700.HK,core_debt_eq,493312,"no-cash = MCap 3,891,532 + debt 406,399 + NCI 86,913 = 4,384,844"
0700.HK,core_fcf,176997,"strict 8×176,997/9,244 = RMB 153.2"
0700.HK,core_fcf_basis,FY2025 CFO − all capex (strict),-
0700.HK,core_fx,1.09649,Price HKD 461.60 → RMB 421.0 at 0.912 (assumption)
0700.HK,core_fx_date,-,-
0700.HK,core_oi,241562,"Threshold-implied prices (FY25 OI 241,562; 9,244m shares)"
0700.HK,core_oi_basis,FY2025 reported,-
0700.HK,core_period,FY2025,-
0700.HK,core_ratio,1,-
0700.HK,core_shares_diluted,9244,"MCap (diluted 9,244m) = RMB 3,891,532m"
0700.HK,core_unit,m,-
0700.HK,past_reason,12.1% ROCE,"Worst-of-four normalized ROCE (consistent-presentation OI, FY2018–25) is 12.1%"
0700.HK,printed_mcap_fcf,22.0,MCap/FCF 22.0× strict / 16.8× maintenance
0700.HK,sf_reason,buybacks,Capital allocation: CAUTION — FY2025 repurchases (HK$80
1211.HK,future_reason,2+ forces,"Forces — customer power STRONG adverse (huge choice, near-zero switchi"
1211.HK,past_reason,7.4% ROCE,Worst-of-four normalized ROCE = 7.4%
1913.HK,core_cash,1261676,"FY2025 inputs: OI 1,299,040; FCF 1,043,286 (= net CFO 1,654,258 − capex 610,972); debt 4,824,245; cash 1,261,676; NCI 21,538; preferred nil"
1913.HK,core_currency,EUR,-
1913.HK,core_debt_eq,4845783,"EV/OI = 7, cash-credited → P = (7 × 1,299,040 + 1,261,676 − 4,845,783) ÷ 2,558,824"
1913.HK,core_fcf,1043286,"FY2025 inputs: OI 1,299,040; FCF 1,043,286 (= net CFO 1,654,258 − capex 610,972); debt 4,824,245; cash 1,261,676; NCI 21,538; preferred nil"
1913.HK,core_fcf_basis,FY2025 CFO − capex,-
1913.HK,core_fx,8.916,EUR/HKD 8.916 (28 Jul 2026) → EUR 4.3629/sh
1913.HK,core_fx_date,2026-07-28,EUR/HKD 8.916 (28 Jul 2026) → EUR 4.3629/sh
1913.HK,core_oi,1299040,"FY2025 inputs: OI 1,299,040; FCF 1,043,286 (= net CFO 1,654,258 − capex 610,972); debt 4,824,245; cash 1,261,676; NCI 21,538; preferred nil"
1913.HK,core_oi_basis,FY2025 reported,-
1913.HK,core_period,FY2025,-
1913.HK,core_ratio,1,-
1913.HK,core_shares_diluted,2558.824,"Shares 2,558,824,000 → MCap EUR 11,163,626k / HKD 99,538m"
1913.HK,core_unit,k,-
1913.HK,past_reason,9.4% ROCE,Worst-of-four normalized ten-year average ROCE 9.4%
1COV.DE,future_reason,2+ forces,"Forces: customer power STRONG (tonne-priced grades, low switching cos"
1COV.DE,past_reason,7.4% ROCE,Worst-of-four normalized ROCE 7.4%
1COV.DE,sf_reason,compensation,P17 hard strike: FY2025 net income −EUR 644m and levered FCF −EUR
2330.TW,core_cash,3518013123,"interests NT$41,952,647; cash & STI NT$3,518,013,123 (cash 3,134,218,213 +"
2330.TW,core_currency,TWD,-
2330.TW,core_debt_eq,1110508587,"7 × 1,936,091,677 − 1,068,555,940 − 41,952,647) ÷ 25,931,544 = NT$479.8 - EV/OI leg, all-cash: P = (7 ×"
2330.TW,core_fcf,992418154,"Trigger band. - FCF leg: P = 8 × 992,418,154 ÷ 25,931,544 = NT$306.2 -"
2330.TW,core_fx,1,-
2330.TW,core_fx_date,n.m.,-
2330.TW,core_oi,1936091677,"= NT$306.2 - EV/OI leg, no-cash: P = (7 × 1,936,091,677 − 1,068,555,940 −"
2330.TW,core_ratio,1,-
2330.TW,core_shares_diluted,25931.544,"2026). Diluted weighted-average shares 25,931,544 thousand (H1-2026). EV"
2330.TW,core_unit,k,-
244920.KS,future_reason,2+ forces,Forces: customer power STRONG (carriers and the FSC set commission ra
244920.KS,past_reason,4.4% ROCE,Worst-of-four normalized ROCE 4.4%
244920.KS,sf_reason,compensation,"9bn) — both reads breach, hard strike"
2502.T,past_reason,5.5% ROCE,The normalized average across the sourced window sits ~5.5–6%
2502.T,sf_reason,buybacks,e failure is capital allocation — two independent P19 flags
300750.SZ,aliases,CATL; 3750.HK,"Contemporary Amperex Technology Co., Limited (CATL; HK dual-listing 3750.HK 2025)"
300750.SZ,future_reason,customer conc.,b: OEMs demonstrably in-source cells) → breadth FAIL → WEAK
3064.T,core_cash,41334,"| ¥576 | | EV/OI all-cash | (7 × 46,455 + 41,334 − 41,674 − 371) ÷ 491.79 |"
3064.T,core_currency,JPY,-
3064.T,core_debt_eq,42045,"7 × 46,455 − 41,674 − 371) ÷ 491.79 | ¥576 | | EV/OI all-cash | (7 × 46,455 + 41,334 − 41,674 − 371) ÷ 491.79"
3064.T,core_fcf,21109,"Inputs: - FY2025 lease-adjusted FCF: ¥21,109m (strict ¥17,657m). -"
3064.T,core_fx,1,-
3064.T,core_fx_date,n.m.,-
3064.T,core_oi,46455,"(strict ¥17,657m). - FY2025 adjusted OI: ¥46,455m. - Band share count:"
3064.T,core_ratio,1,-
3064.T,core_shares_diluted,491.79,"OI: ¥46,455m. - Band share count: 491.79m (491.77m net + 0.02m"
3064.T,core_unit,m,-
3064.T,sf_reason,buybacks,"Policy keeps buybacks as the outlet for surplus cash, but no authorisa"
3382.T,past_reason,5.6% ROCE,Worst-of-four normalized ROCE 5.62%
3382.T,sf_reason,flag pair,Two independent flags → SF FAIL (§2·1C pair rule)
5108.T,core_cash,713810,"− 827,015)/1,250m = ¥1,473; all-cash (+713,810) = ¥2,044. Bounds: ¥1,473 /"
5108.T,core_currency,JPY,-
5108.T,core_debt_eq,827015,"¥2,389. EV/OI legs: no-cash (7 × 381,237 − 827,015)/1,250m = ¥1,473; all-cash"
5108.T,core_fcf,373287,"- Threshold-implied prices: FCF leg 8 × 373,287/1,250m = ¥2,389. EV/OI"
5108.T,core_fx,1,-
5108.T,core_fx_date,n.m.,-
5108.T,core_oi,381237,"= ¥2,389. EV/OI legs: no-cash (7 × 381,237 − 827,015)/1,250m = ¥1,473;"
5108.T,core_ratio,1,-
5108.T,core_shares_diluted,1250,"prices: FCF leg 8 × 373,287/1,250m = ¥2,389. EV/OI legs:"
5108.T,core_unit,m,-
5108.T,past_reason,9.2% ROCE,Worst-of-four normalized ROCE 9.15%
5108.T,sf_reason,buybacks,"tal allocation: CAUTION (1 flag) — episodic large buybacks (FY17 ¥150bn, FY19 ¥200bn, FY22 ¥100bn, FY25 ¥30"
5332.T,past_reason,8% ROCE,worst-of-four normalized ROCE is 8.0%
5332.T,sf_reason,buybacks,P19 hard strike: the FY3/2026 buyback
6268.T,past_reason,7.6% ROCE,Worst-of-four normalized ROCE 7.6%
6268.T,sf_reason,flag pair,FAIL (flag pair)
6273.T,core_cash,727123,"¥21,282. - EV/OI all-cash: (7 × 190,558 + 727,123 − 5,000 − 249) / 62.43 ="
6273.T,core_currency,JPY,-
6273.T,core_debt_eq,5249,"7 × 190,558 − 5,000 − 249) / 62.43 = ¥21,282. - EV/OI all-cash: (7 × 190,558 + 727,123 − 5,000 − 249) / 62.43"
6273.T,core_fcf,34532,"/ 142,892 = 32.1× (all-capex 4,585,451 / 34,532 = 132.8×). - EV/OI ="
6273.T,core_fx,1,-
6273.T,core_fx_date,n.m.,-
6273.T,core_oi,190558,"/ 34,532 = 132.8×). - EV/OI = 4,590,700 / 190,558 = 24.1× (no-cash) and"
6273.T,core_ratio,1,-
6273.T,core_shares_diluted,62.43,"## F. Valuation math - Current (¥73,450; 62.43m sh; 30 Jun 2026 balance"
6273.T,core_unit,m,-
6273.T,past_reason,ROCE decline,"5% across FY3/23–26, three consecutive declines, mirrored on the beginning-of-period ser"
6273.T,sf_reason,buybacks,"al allocation is CAUTION: seven straight years of buybacks at 13–28× EV/OI and 22–96× maintenance FCF, with"
6301.T,core_cash,439701,"− 197,659)/901.1m = ¥2,700; all-cash (+439,701) = ¥3,188. Bounds converge"
6301.T,core_currency,JPY,-
6301.T,core_debt_eq,1538690,"7 × 567,323 − 1,341,031 − 197,659)/901.1m = ¥2,700; all-cash (+439,701) = ¥3,188. Bounds converge at ¥2,101"
6301.T,core_fcf,236702,"- Threshold-implied prices: FCF leg 8 × 236,702/901.1m = ¥2,101. EV/OI"
6301.T,core_fx,1,-
6301.T,core_fx_date,n.m.,-
6301.T,core_oi,567323,"= ¥2,101. EV/OI legs: no-cash (7 × 567,323 − 1,341,031 −"
6301.T,core_ratio,1,-
6301.T,core_shares_diluted,901.1,"prices: FCF leg 8 × 236,702/901.1m = ¥2,101. EV/OI legs:"
6301.T,core_unit,m,-
6301.T,past_reason,9.8% ROCE,Worst-of-four normalized ROCE 9.81%
6301.T,sf_reason,buybacks,Capital allocation: CAUTION (1 flag) — buybacks began at scale only at the top of the cycle (FY2
6324.T,future_reason,2+ forces,That is two strong forces
6324.T,past_reason,4.8% ROCE,Worst-of-four normalized ROCE is 4.8%
6324.T,sf_reason,flag pair,FAIL — flag pair
6367.T,core_cash,1132504,"− 66,698)/292.84m = ¥6,859; all-cash (+1,132,504) = ¥10,726. Band: no-cash"
6367.T,core_currency,JPY,-
6367.T,core_debt_eq,896467,"7 × 414,991 − 829,769 − 66,698)/292.84m = ¥6,859; all-cash (+1,132,504) = ¥10,726. Band: no-cash bound ¥6,859"
6367.T,core_fcf,256767,"- Threshold-implied prices: FCF leg 8 × 256,767/292.84m = ¥7,015. EV/OI"
6367.T,core_fx,1,-
6367.T,core_fx_date,n.m.,-
6367.T,core_oi,414991,"= ¥7,015. EV/OI legs: no-cash (7 × 414,991 − 829,769 − 66,698)/292.84m"
6367.T,core_ratio,1,-
6367.T,core_shares_diluted,292.84,"prices: FCF leg 8 × 256,767/292.84m = ¥7,015. EV/OI legs:"
6367.T,core_unit,m,-
6367.T,past_reason,9.1% ROCE,Worst-of-four normalized ROCE 9.1%
6383.T,core_cash,269378,"6,760 − 12) / 385.0 = ¥1,814; all-cash (+ 269,378) = ¥2,514. Band: no-cash"
6383.T,core_currency,JPY,-
6383.T,core_debt_eq,7170,"7 × 100,816 − 398 − 6,760 − 12) / 385.0 = ¥1,814; all-cash (+ 269,378) = ¥2,514. Band: no-cash ¥1,121 /"
6383.T,core_fcf,53930,"balance sheet): MCap/FCF = 2,252,666 / 53,930 = 41.8×; EV/OI = 2,259,836"
6383.T,core_fx,1,-
6383.T,core_fx_date,n.m.,-
6383.T,core_oi,100816,"/ 53,930 = 41.8×; EV/OI = 2,259,836 / 100,816 = 22.4× (no-cash) and"
6383.T,core_ratio,1,-
6383.T,core_shares_diluted,385,"= / 489,069 = 4.61×. - Threshold prices (385.0m diluted shares): FCF leg 8"
6383.T,core_unit,m,-
6383.T,future_reason,customer conc.,Customer breadth FAILS: TSMC took ¥91
6383.T,sf_reason,buybacks,Capital allocation is CAUTION: ¥20bn of repurchases in Aug–Oct 2023 at ≈59× MCap/FCF and 15
6501.T,core_cash,1878846,"- EV/OI leg, all cash: P = (7,923,951 + 1,878,846 − 1,246,028) ÷ 4,487.8m ="
6501.T,core_currency,JPY,-
6501.T,core_debt_eq,1246028,"− 0 − 189,101) ÷ 4,487.8m = (7,923,951 − 1,246,028) ÷ 4,487.8m = ¥1,488. -"
6501.T,core_fcf,1170232,"(FY3/2026, derived, levered, all-capex) ¥1,170,232m; BV ¥6,573,758m; TBV"
6501.T,core_fx,1,-
6501.T,core_fx_date,n.m.,-
6501.T,core_oi,1131993,"multiples. OI (FY3/2026, derived) ¥1,131,993m; FCF (FY3/2026, derived,"
6501.T,core_ratio,1,-
6501.T,core_shares_diluted,4487.8,"close ¥5,503, 6 Aug 2026). Diluted shares 4,487.8m (derived, C9). Balance"
6501.T,core_unit,m,-
6501.T,past_reason,ROCE decline,"88%, so P4 does not fire"
6501.T,sf_reason,buybacks,Capital allocation CAUTION: repurchases run at 17
6503.T,past_reason,7.3% ROCE,Worst-of-four 10y normalized ROCE is 7.3%
6503.T,sf_reason,buybacks,P19 fails it: FY24/25/26 tranches at 19
6506.T,core_cash,57619,"FY2025 OI 47,307; FY2025 FCF 5,930; cash 57,619; debt incl. leases 121,161;"
6506.T,core_currency,JPY,-
6506.T,core_debt_eq,131141,"7 × 47,307 − 121,161 − 9,980) / 259.368m = ¥771 - EV/OI all-cash: (7 × 47,307 + 57,619 − 121,161 − 9,980) /"
6506.T,core_fcf,5930,"May 2026); FY2025 OI 47,307; FY2025 FCF 5,930; cash 57,619; debt incl."
6506.T,core_fx,1,-
6506.T,core_fx_date,n.m.,-
6506.T,core_oi,47307,"259,367,760 (31 May 2026); FY2025 OI 47,307; FY2025 FCF 5,930; cash"
6506.T,core_ratio,1,-
6506.T,core_shares_diluted,259.368,"prices: - FCF leg: 8 × 5,930 / 259.368m = ¥183 - EV/OI no-cash: (7"
6506.T,core_unit,m,-
6506.T,past_reason,ROCE decline,falling for three straight years since FY2022
6506.T,sf_reason,buybacks,"The three buybacks (2018, 2019, 2024) were executed at 61–189× free"
6626.T,core_cash,9619,"/ 9.596 = ¥2,342; all-cash: (7 × 3,535 + 9,619 − 2,271) / 9.596 = ¥3,344."
6626.T,core_currency,JPY,-
6626.T,core_debt_eq,2271,"EV/OI leg no-cash: (7 × 3,535 − 2,271) / 9.596 = ¥2,342;"
6626.T,core_fcf,293,"by rounding: 13.96); strict 23,501 / 293 = 80.2× (reference)."
6626.T,core_fx,1,-
6626.T,core_fx_date,n.m.,-
6626.T,core_oi,3535,"EV all-cash 16,153. EV/OI 25,772 / 3,535 = 7.3× (fails 7 by 4%);"
6626.T,core_ratio,1,-
6626.T,core_shares_diluted,9.596,"band. FCF leg (maintenance): 8 × 1,683 / 9.596 = ¥1,403; FCF leg (strict):"
6626.T,core_unit,m,-
6645.T,future_reason,moat eroding,It is eroding: automation margin fell from
6645.T,past_reason,7.2% ROCE,worst-of-four normalized ROCE is 7.2%
6645.T,sf_reason,flag pair,FAIL (flag pair)
6702.T,core_cash,450366,"− 19,672)/1,730m = ¥1,321; all-cash (+450,366) = ¥1,581. Both bounds ="
6702.T,core_currency,JPY,-
6702.T,core_debt_eq,152766,"7 × 348,329 − 133,094 − 19,672)/1,730m = ¥1,321; all-cash (+450,366) = ¥1,581. Both bounds = ¥1,060 (MCap/FCF"
6702.T,core_fcf,229153,"- Threshold-implied prices: FCF leg 8 × 229,153/1,730m = ¥1,060. EV/OI"
6702.T,core_fx,1,-
6702.T,core_fx_date,n.m.,-
6702.T,core_oi,348329,"= ¥1,060. EV/OI legs: no-cash (7 × 348,329 − 133,094 − 19,672)/1,730m"
6702.T,core_ratio,1,-
6702.T,core_shares_diluted,1730,"prices: FCF leg 8 × 229,153/1,730m = ¥1,060. EV/OI legs:"
6702.T,core_unit,m,-
6702.T,past_reason,record-limited,Severely record-limited (3y)
6702.T,sf_reason,buybacks,Capital allocation: CAUTION (1 flag) — ¥453bn repurchased over FY24–26 with no published worth-referenced
6752.T,future_reason,2+ forces,"Four forces: customer power STRONG, supplier power WEAK, substitutes STRON"
6752.T,past_reason,4.6% ROCE,Worst-of-four normalized ROCE 4.56%
6758.T,core_cash,2170019,"= 16.39× - EV_all-cash = 23,732,559 − 2,170,019 = ¥21,562,540m → EV/OI ="
6758.T,core_currency,JPY,-
6758.T,core_debt_eq,2276277,"7 × 1,447,507 + 2,170,019 − 1,204,171 − 666,427 − 405,679) / 5,917.342 = 10,026,291 / 5,917.342 = ¥1,694 -"
6758.T,core_fcf,1508611,"3/2026 OI ¥1,447,507m and continuing FCF ¥1,508,611m): - MCap = 3,626 ×"
6758.T,core_fx,1,-
6758.T,core_fx_date,n.m.,-
6758.T,core_oi,1447507,"30 Jun 2026 balance sheet, FYE 3/2026 OI ¥1,447,507m and continuing FCF"
6758.T,core_ratio,1,-
6758.T,core_shares_diluted,5917.342,"moves nothing that binds, see A(a) — 5,917.342m diluted, 30 Jun 2026"
6758.T,core_unit,m,-
6758.T,sf_reason,buybacks,The ¥500bn facility is live and drawing hard
6841.T,core_cash,185970,"¥2,143. - EV/OI all-cash leg: (577,885 + 185,970 − 44,884) / 248.714 ="
6841.T,core_currency,JPY,-
6841.T,core_debt_eq,44884,"EV/OI all-cash leg: (577,885 + 185,970 − 44,884) / 248.714 = ¥2,891. -"
6841.T,core_fcf,58269,"12.5× (all-cash). MCap/FCF = 1,170,697 / 58,269 = 20.1×. MCap/BV ="
6841.T,core_fx,1,-
6841.T,core_fx_date,n.m.,-
6841.T,core_oi,82555,"math - Multiples: EV/OI = 1,215,581 / 82,555 = 14.7× (no-cash) and"
6841.T,core_ratio,1,-
6841.T,core_shares_diluted,248.714,"- Trigger band: - FCF leg: 8 × 58,269 / 248.714 = ¥1,874. - EV/OI no-cash"
6841.T,core_unit,m,-
6841.T,sf_reason,buybacks,Buybacks from FY3/24 to FY3/26 ran at 7
6845.T,core_cash,94824,"1,881 + NCI 2,872). - Cash and STI: ¥94,824m. Current multiples: |"
6845.T,core_currency,JPY,-
6845.T,core_debt_eq,25502,"share count: 502.82m. - Debt-like stack: ¥25,502m (borrowings 9,281 + leases"
6845.T,core_fcf,30176,"math Inputs: - FY2025 J-GAAP FCF: ¥30,176m. - FY2025 J-GAAP OI:"
6845.T,core_fx,1,-
6845.T,core_fx_date,n.m.,-
6845.T,core_oi,47304,"FCF: ¥30,176m. - FY2025 J-GAAP OI: ¥47,304m. - Band share count:"
6845.T,core_ratio,1,-
6845.T,core_shares_diluted,502.82,"J-GAAP OI: ¥47,304m. - Band share count: 502.82m. - Debt-like stack:"
6845.T,core_unit,m,-
6845.T,sf_reason,buybacks,Repurchases ran at 18–23× the latest FCF and ≈ 13× EV/OI in
6861.T,core_cash,1426594,"595,759; FY2025 FCF 370,185; cash and STI 1,426,594 (20 Jun 2026); debt,"
6861.T,core_currency,JPY,-
6861.T,core_debt_eq,0,"(20 Jun 2026); debt, preferred and NCI 0. Current multiples: -"
6861.T,core_fcf,370185,"Jun 2026); FY2025 OI 595,759; FY2025 FCF 370,185; cash and STI 1,426,594 (20"
6861.T,core_fx,1,-
6861.T,core_fx_date,n.m.,-
6861.T,core_oi,595759,"242,525,085 (20 Jun 2026); FY2025 OI 595,759; FY2025 FCF 370,185; cash"
6861.T,core_ratio,1,-
6861.T,core_shares_diluted,242.525,"prices: - FCF leg: 8 × 370,185 / 242.525m = ¥12,211 - EV/OI no-cash:"
6861.T,core_unit,m,-
688825.SS,future_reason,customer conc.,Breadth: customer FAIL — top-5 customers 67
688825.SS,past_reason,losses,"on the crude NI/total-assets proxy, −10.0% (FY23), −3.3% (FY24), +2.1% (FY25)"
688825.SS,sf_reason,dilution,"rated returns record to sustain, funded by serial dilutive raises — CAUTION (one flag), not ADVERSE: no live"
6954.T,core_cash,753871,"− 18,076)/933.0m = ¥1,359; all-cash (+753,871) = ¥2,167. Bounds: no-cash"
6954.T,core_currency,JPY,-
6954.T,core_debt_eq,18076,"¥1,970. EV/OI legs: no-cash (7 × 183,763 − 18,076)/933.0m = ¥1,359; all-cash"
6954.T,core_fcf,229715,"- Threshold-implied prices: FCF leg 8 × 229,715/933.0m = ¥1,970. EV/OI"
6954.T,core_fx,1,-
6954.T,core_fx_date,n.m.,-
6954.T,core_oi,183763,"= ¥1,970. EV/OI legs: no-cash (7 × 183,763 − 18,076)/933.0m = ¥1,359;"
6954.T,core_ratio,1,-
6954.T,core_shares_diluted,933,"prices: FCF leg 8 × 229,715/933.0m = ¥1,970. EV/OI legs:"
6954.T,core_unit,m,-
6954.T,past_reason,9.6% ROCE,Worst-of-four normalized ROCE 9.6%
6954.T,sf_reason,buybacks,policy (~57% FY26) plus recurring criterion-free buybacks (FY23 ¥24
7011.T,future_reason,customer conc.,the only buyer of those platforms — one customer far above 10% on an arithmetic floor
7011.T,past_reason,3.9% ROCE,worst-of-four ROCE to 3.93%
7213.T,future_reason,2+ forces,Forces: customer power STRONG (tender buyers
7213.T,past_reason,9.4% ROCE,Worst-of-four normalized ROCE 9.4%
7213.T,sf_reason,buybacks,Capital allocation CAUTION (one flag): the live buyback executes at 2
7309.T,future_reason,customer conc.,Breadth FAIL: the FY2025 yūhō discloses Pa
7309.T,past_reason,ROCE decline,th and a sustained three-year decline in returns
7309.T,sf_reason,buybacks,Capital allocation CAUTION: ¥169bn repurchased FY2021–H1 2026 at 11–25× all-cash EV/OI with no
7751.T,core_cash,618427,"− 282,320)/878.6m = ¥2,378; all-cash (+618,427) = ¥3,082. Bounds converge"
7751.T,core_currency,JPY,-
7751.T,core_debt_eq,1098429,"7 × 455,390 − 816,109 − 282,320)/878.6m = ¥2,378; all-cash (+618,427) = ¥3,082. Bounds converge at ¥1,946"
7751.T,core_fcf,213738,"- Threshold-implied prices: FCF leg 8 × 213,738/878.6m = ¥1,946. EV/OI"
7751.T,core_fx,1,-
7751.T,core_fx_date,n.m.,-
7751.T,core_oi,455390,"= ¥1,946. EV/OI legs: no-cash (7 × 455,390 − 816,109 − 282,320)/878.6m"
7751.T,core_ratio,1,-
7751.T,core_shares_diluted,878.6,"prices: FCF leg 8 × 213,738/878.6m = ¥1,946. EV/OI legs:"
7751.T,core_unit,m,-
7751.T,past_reason,6.1% ROCE,Worst-of-four normalized ROCE 6.12%
7751.T,sf_reason,distributions,2× lower-EV EV/OI) whose FY25 total distributions (¥447
7936.T,core_cash,141431,"EV_all-cash = 3,299,154 − 141,431 = 3,157,723"
7936.T,core_currency,JPY,-
7936.T,core_debt_eq,102569,"EV_no-cash = 3,196,585 + 40,000 + 61,031 + 1,538 = 3,299,154"
7936.T,core_fcf,79614,"FCF leg: P = 8 × 79,614 ÷ 715.6"
7936.T,core_fcf_basis,FY2025 CFO − all capex (strict),-
7936.T,core_fx,1,-
7936.T,core_fx_date,n.m.,-
7936.T,core_oi,142519,"(25 × 142,519 + 141,431 − 101,031 − 1,538) ÷ 715.6"
7936.T,core_oi_basis,FY2025 reported,-
7936.T,core_period,FY2025; BS 2026-06-30,-
7936.T,core_ratio,1,-
7936.T,core_shares_diluted,715.6,"MCap = 4,467 × 715.6m = ¥3,196,585m"
7936.T,core_unit,m,-
7974.T,core_cash,1967908,"= ¥2,186; P_all-cash = (7 × 360,117 + 1,967,908 − 1,155)/1,152.83m = ¥3,893"
7974.T,core_currency,JPY,-
7974.T,core_debt_eq,1155,"EV/OI legs: P_no-cash = (7 × 360,117 − 1,155)/1,152.83m = ¥2,186;"
7974.T,core_fcf,262620,"Threshold-implied prices: FCF leg P = 8 × 262,620/1,152.83m = ¥1,822. EV/OI"
7974.T,core_fx,1,-
7974.T,core_fx_date,n.m.,-
7974.T,core_oi,360117,"= ¥1,822. EV/OI legs: P_no-cash = (7 × 360,117 − 1,155)/1,152.83m ="
7974.T,core_ratio,1,-
7974.T,core_shares_diluted,1152.83,"prices: FCF leg P = 8 × 262,620/1,152.83m = ¥1,822. EV/OI legs:"
7974.T,core_unit,m,-
7974.T,sf_reason,buybacks,"Capital allocation: CAUTION (1 flag) — repurchases are episodic and criterion-free (FY19, FY22, FY"
8002.T,core_currency,JPY,-
8002.T,core_fcf,381908,"context MCap/FCF = 21.0× (FCF 381,908)"
8002.T,core_fx,1,-
8002.T,core_fx_date,n.m.,-
8002.T,core_oi,n.m.,EV/OI n.m. — substitution rule (OI structurally understates
8002.T,core_oi_basis,n.m. — substitution rule (MCap/NI anchor),-
8002.T,core_period,FY3/2026,-
8002.T,core_ratio,1,-
8002.T,core_shares_diluted,1626.8,"¥8,029.9bn (1,626.8m sh ex-treasury)"
8002.T,core_unit,m,-
8002.T,past_reason,12.3% ROE,"Worst normalized ROE (Σ NI ÷ Σ equity, end-basis) 12.3%"
8002.T,sf_reason,buybacks,Capital allocation: CAUTION (1 flag) — buybacks every year since FY22 at rising multiples (~0
8TRA.ST,past_reason,4.4% ROCE,Worst-of-four normalized ROCE is 4.42%
8TRA.ST,sf_reason,acquisitions,The acquisition audit strikes
AAPL,core_cash,54.697,cash+STI $54.697bn
AAPL,core_currency,USD,-
AAPL,core_debt_eq,112.377,debt-equiv $112.377bn
AAPL,core_fcf,98.767,"diluted WA 15.005bn [sourced]; FCF $98.767bn, OI $133.050bn, cash+STI"
AAPL,core_fx,1,-
AAPL,core_fx_date,n.m.,-
AAPL,core_oi,133.05,"WA 15.005bn [sourced]; FCF $98.767bn, OI $133.050bn, cash+STI $54.697bn,"
AAPL,core_ratio,1,-
AAPL,core_shares_diluted,15005,"out 14.687bn [sourced]; FY2025 diluted WA 15.005bn [sourced]; FCF $98.767bn,"
AAPL,core_unit,bn,-
AAPL,sf_reason,compensation,vs the $30m P17 ceiling — STRIKE
ABB,core_cash,5857,"= $18.06. - EV/OI all-cash: (7 × 6,047 + 5,857 − 8,177 − 805 − 506) ÷"
ABB,core_currency,USD,-
ABB,core_debt_eq,9488,"7 × 6,047 − 8,177 − 805 − 506) ÷ 1,818 = $18.06. - EV/OI all-cash: (7 × 6,047 + 5,857 − 8,177 − 805 − 506) ÷"
ABB,core_fcf,4249,"FY2025 continuing flows OI $6,047m, FCF $4,249m): - MCap $177,652m; EV"
ABB,core_fx,1,-
ABB,core_fx_date,n.m.,-
ABB,core_oi,6047,"sheet; FY2025 continuing flows OI $6,047m, FCF $4,249m): - MCap"
ABB,core_ratio,1,-
ABB,core_shares_diluted,1818,"→ EXPENSIVE. Threshold-implied prices (÷ 1,818M diluted): - MCap/FCF leg:"
ABB,core_unit,m,-
ABB,sf_reason,buybacks,if repurchases stop executing above worth
ABCA.PA,core_currency,EUR,-
ABCA.PA,core_fx,1,-
ABCA.PA,core_fx_date,n.m.,-
ABCA.PA,core_oi,n.m.,EV/OI n.m. under the substitution rule
ABCA.PA,core_oi_basis,n.m. — substitution rule (MCap/NI anchor),-
ABCA.PA,core_ratio,1,-
ABCA.PA,core_shares_diluted,59.76,€305.3m (59.62m shares ex-treasury; 59.76m diluted)
ABCA.PA,core_unit,m,-
ABCA.PA,future_reason,2+ forces,Forces: allocator power STRONG (AUM €265m → €245m in a year the funds
ABCA.PA,past_reason,15.2% ROE,15.5% end / 15.2% beginning (worst)
ABCA.PA,printed_ev_oi,n.m.,EV/OI n.m. under the substitution rule
ABCA.PA,printed_ev_oi_all_cash,n.m.,EV/OI n.m. under the substitution rule
ABEV,aliases,ABEV3,Ambev S.A. (ADR; B3: ABEV3)
ABEV,core_cash,3540,"− 569)/15,450 = $1.855; ac (29,232 + 3,540 − 569)/15,450 = $2.084; FCF"
ABEV,core_currency,USD,-
ABEV,core_debt_eq,569,"legs (7 × 4,176 = 29,232): nc (29,232 − 569)/15,450 = $1.855; ac"
ABEV,core_fx,1,-
ABEV,core_fx_date,n.m.,-
ABEV,core_oi,4176,"— informational). Band: EV/OI legs (7 × 4,176 = 29,232): nc (29,232 −"
ABEV,core_ratio,1,-
ABEV,core_shares_diluted,15450,"(7 × 4,176 = 29,232): nc (29,232 − 569)/15,450 = $1.855; ac (29,232 +"
ABEV,core_unit,m,-
ABEV,past_reason,20.6% ROCE,worst-of-four ≈ 20.6%
ABM,future_reason,2+ forces,All four forces call STRONG
ABM,past_reason,6.2% ROCE,Worst-of-four normalised ROCE 6.2%
ABM,sf_reason,compensation,P17 hard strike: FY2025 CEO total $9
ABNB,core_cash,11014,"Operative figures used below — FY2025 OI $2,544M, FCF $4,600M, cash+STI $11,014M, debt $2,000M"
ABNB,core_currency,USD,-
ABNB,core_debt_eq,2000,"Operative figures used below — FY2025 OI $2,544M, FCF $4,600M, cash+STI $11,014M, debt $2,000M"
ABNB,core_fcf,4600,"Operative figures used below — FY2025 OI $2,544M, FCF $4,600M, cash+STI $11,014M, debt $2,000M"
ABNB,core_fx,1,-
ABNB,core_fx_date,n.m.,-
ABNB,core_oi,2544,"Operative figures used below — FY2025 OI $2,544M, FCF $4,600M, cash+STI $11,014M, debt $2,000M"
ABNB,core_oi_basis,FY2025 reported,-
ABNB,core_period,FY2025,-
ABNB,core_ratio,1,-
ABNB,core_shares_diluted,623,"FCF leg 8 × 4,600 ÷ 623 = $59.07"
ABNB,core_unit,m,-
ABNB,past_reason,19% ROCE,ROCE_wc 19–24% since 2022
ABNB,sf_reason,buybacks,The repurchase lever fails
ACP.WA,core_cash,7246,"− 5,467.1)/83.0m = PLN 54.4; all-cash (+7,246.0) = PLN 141.7. The 2.6×"
ACP.WA,core_currency,PLN,-
ACP.WA,core_debt_eq,6790.1,"7 × 1,615.0 − 1,323.0 − 5,467.1)/83.0m = PLN 54.4; all-cash (+7,246.0) = PLN 141.7. The 2.6× bound spread is"
ACP.WA,core_fx,1,-
ACP.WA,core_fx_date,n.m.,-
ACP.WA,core_oi,1615,"prices (EV/OI legs): no-cash (7 × 1,615.0 − 1,323.0 − 5,467.1)/83.0m"
ACP.WA,core_ratio,1,-
ACP.WA,core_shares_diluted,83,"no-cash (7 × 1,615.0 − 1,323.0 − 5,467.1)/83.0m = PLN 54.4; all-cash"
ACP.WA,core_unit,m,-
ACP.WA,past_reason,7.9% ROCE,Worst-of-four normalized ROCE 7.9%
AD.AS,core_cash,3705,"no preferred; NCI nil; cash+STI €3,705m. - EV conservative (no"
AD.AS,core_currency,EUR,-
AD.AS,core_debt_eq,18404,"sheet: - MCap = €32,650m. Gross debt €18,404m (incl. ~€13bn lease"
AD.AS,core_fcf,3699,"on both variants. - MCap/FCF = 32,650 / 3,699 = 8.8× vs ≤ 8 — misses by"
AD.AS,core_fx,1,-
AD.AS,core_fx_date,n.m.,-
AD.AS,core_oi,3542,"€32.93. EV/OI leg, conservative EV: (7 × 3,542 − 18,404) ÷ 898.7 = €7.11 ←"
AD.AS,core_ratio,1,-
AD.AS,core_shares_diluted,898.7,"→ PASS. ## F. Valuation math At €36.33, 898.7m diluted (TTM), FY2025"
AD.AS,core_unit,m,-
AD.AS,past_reason,8.4% ROCE,Worst-of-four normalized ROCE 8.4%
ADBE,core_cash,5630,"− 7,080)/397.5 = $135.50; ac (60,942 + 5,630 − 7,080)/397.5 = $149.67;"
ADBE,core_currency,USD,-
ADBE,core_debt_eq,7080,"legs (7 × 8,706 = 60,942): nc (60,942 − 7,080)/397.5 = $135.50; ac"
ADBE,core_fcf,9780,"− 7,080)/397.5 = $149.67; FCF leg 8 × 9,780/397.5 = $196.83 → EV/OI"
ADBE,core_fx,1,-
ADBE,core_fx_date,n.m.,-
ADBE,core_oi,8706,"distortion — C). Band: EV/OI legs (7 × 8,706 = 60,942): nc (60,942 −"
ADBE,core_ratio,1,-
ADBE,core_shares_diluted,397.5,F. Valuation math Price $265.21 · shares 397.5m · MCap $105.42bn. EV: ac
ADBE,core_unit,m,-
ADBE,past_reason,26% ROCE,worst-of-four ≈ 26–27%
ADBE,sf_reason,compensation,P17 absolute trigger
ADS.DE,past_reason,leverage,"breaches P5, and P6 does not hold"
ADS.DE,sf_reason,buybacks,"Strike — buybacks: €3,501m repurchased 2021–22 at an implied ≈ €223/share (derived) ag"
ADYEN.AS,core_cash,10828.1,"P(EV/OI<7) = (7 × 1,109.9 + 10,828.1 − 252.4) ÷ 31.611 = €580"
ADYEN.AS,core_currency,EUR,-
ADYEN.AS,core_debt_eq,252.4,"P(EV/OI<7) = (7 × 1,109.9 + 10,828.1 − 252.4) ÷ 31.611 = €580"
ADYEN.AS,core_fcf,904.6,"MCap 25,839 ÷ FCF 904.6 = 28.6"
ADYEN.AS,core_fcf_basis,FY2025 reported FCF,-
ADYEN.AS,core_fx,1,-
ADYEN.AS,core_fx_date,n.m.,-
ADYEN.AS,core_oi,1109.9,"EV 15,263 ÷ OI 1,109.9 = 13.8"
ADYEN.AS,core_oi_basis,FY2025 reported,-
ADYEN.AS,core_period,FY2025,-
ADYEN.AS,core_ratio,1,-
ADYEN.AS,core_shares_diluted,31.611,P(MCap/FCF<8) = 8 × 904.6 ÷ 31.611 = €229
ADYEN.AS,core_unit,m,-
ADYEN.AS,past_reason,24.6% ROCE,ROCE_wc was 24.6–45.3% in all seven years
AIP,future_reason,forces: substitutes,substitutes STRONG
AIP,past_reason,losses,"five losses, flat in dollars"
AIP,sf_reason,compensation,Both reads breach → hard strike
AKZA.AS,past_reason,7.6% ROCE,worst-of-four normalized ROCE 7.6%
AKZA.AS,sf_reason,buybacks,P19 fails the gate
ALE.WA,core_cash,2840.7,"4,986.1)/978.84m = PLN 11.57; all-cash (+2,840.7) = PLN 14.47. Bounds: 11.57"
ALE.WA,core_currency,PLN,-
ALE.WA,core_debt_eq,4986.1,"15.75. EV/OI legs: no-cash (7 × 2,330.3 − 4,986.1)/978.84m = PLN 11.57;"
ALE.WA,core_fcf,1927.3,"- Threshold-implied prices: FCF leg 8 × 1,927.3/978.84m = PLN 15.75. EV/OI"
ALE.WA,core_fx,1,-
ALE.WA,core_fx_date,n.m.,-
ALE.WA,core_oi,2330.3,"= PLN 15.75. EV/OI legs: no-cash (7 × 2,330.3 − 4,986.1)/978.84m = PLN"
ALE.WA,core_ratio,1,-
ALE.WA,core_shares_diluted,978.84,"prices: FCF leg 8 × 1,927.3/978.84m = PLN 15.75. EV/OI legs:"
ALE.WA,core_unit,m,-
ALE.WA,past_reason,6.2% ROCE,Worst-of-four normalized ROCE 6.16%
ALE.WA,sf_reason,buybacks,4bn FY2025 buyback at ≈18× MCap/FCF / ≈16× lower-EV EV/OI — above wo
ALFA.ST,core_cash,7831,"147.3; EV/OI ≤ 7 all-cash → (7 × 11,749 + 7,831 − 21,011 − 344) ÷ 413.326m"
ALFA.ST,core_currency,SEK,-
ALFA.ST,core_debt_eq,21355,"7 × 11,749 − 21,011 − 344) ÷ 413.326m = SEK 147.3; EV/OI ≤ 7 all-cash → (7 × 11,749 + 7,831 − 21,011 − 344) ÷"
ALFA.ST,core_fcf,6149,"= SEK 246,474m. MCap/FCF = 232,950 ÷ 6,149 = 37.9×. EV/OI = 21.6× /"
ALFA.ST,core_fx,1,-
ALFA.ST,core_fx_date,n.m.,-
ALFA.ST,core_oi,11749,"119.0 (binds); EV/OI ≤ 7 no-cash → (7 × 11,749 − 21,011 − 344) ÷ 413.326m"
ALFA.ST,core_ratio,1,-
ALFA.ST,core_shares_diluted,413.326,"prices: MCap/FCF ≤ 8 → 8 × 6,149 ÷ 413.326m = SEK 119.0 (binds); EV/OI"
ALFA.ST,core_unit,m,-
ALFA.ST,sf_reason,acquisitions,0× EV/OI (year / normalized) — clearly overpriced on the y
ALIG.ST,core_cash,778,"106.241 = SEK 33.0. All-cash: (7 × 977 + 778 − 3,328) ÷ 106.241 = SEK"
ALIG.ST,core_currency,SEK,-
ALIG.ST,core_debt_eq,3328,"SEK 48.5. - EV/OI leg, no-cash: (7 × 977 − 3,328) ÷ 106.241 = SEK 33.0."
ALIG.ST,core_fcf,644,"F. Valuation math - MCap/FCF = 12,664 ÷ 644 = 19.7× (FY2025 FCF; 3-year"
ALIG.ST,core_fx,1,-
ALIG.ST,core_fx_date,n.m.,-
ALIG.ST,core_oi,977,"14.9×, context only). - EV/OI = 15,992 ÷ 977 = 16.4× (no-cash) · 15,214"
ALIG.ST,core_ratio,1,-
ALIG.ST,core_shares_diluted,106.241,"n.m. (TBV −660). - FCF leg: 8 × 644 ÷ 106.241 = SEK 48.5. - EV/OI leg,"
ALIG.ST,core_unit,m,-
ALIG.ST,past_reason,7.5% ROCE,Worst-of-four normalized ROCE is 7.5%
AME,core_cash,495.4,"229.855 = $41.10. - All-cash: (16,758.0 + 495.4 − 7,036.2 − 274.8) ÷"
AME,core_currency,USD,-
AME,core_debt_eq,7311,"7 × 2,394.0 = 16,758.0. - No-cash: (16,758.0 − 7,036.2 − 274.8) ÷ 229.855 = $41.10. - All-cash: (16,758.0 +"
AME,core_fcf,1671.6,"MCap $57,907m. - MCap/FCF: 57,907 ÷ 1,671.6 (FY2025) = 34.6×; ÷ 1,825.0"
AME,core_fx,1,-
AME,core_fx_date,n.m.,-
AME,core_oi,2394,"OI at EBITDA cap; OI 2,037.0 + 357.1 = 2,394.0): no-cash 65,218.3 ÷"
AME,core_ratio,1,-
AME,core_shares_diluted,229.855,math Price $251.93 (2 Oct 2026). Shares 229.855m (Q2 2026 diluted w-avg;
AME,core_unit,m,-
AME,sf_reason,acquisitions,"0bn, ≈14× EBITDA, debt-funded) is the largest deal in the record"
AMRC,past_reason,3.6% ROCE,Worst-of-four normalized ROCE 3.56%
AMRC,sf_reason,compensation,Both breached — hard strike
AMV0.DE,future_reason,customer conc.,Breadth: customer-side FAIL — largest customer group 22
AMV0.DE,past_reason,losses,Worst-of-four normalized ROCE −1.6%
AMZN,core_cash,122988,"0 | 0 | | Cash & short-term investments | 122,988 (78,213 + 44,775) | 122,988"
AMZN,core_currency,USD,-
AMZN,core_debt_eq,226562,"cross-check) | | Debt & lease total | 226,562 | 251,635 | | Preferred | 0"
AMZN,core_fcf,11194,"| 43.0× | ≤ 8 | | MCap/FCF — all-capex (11,194) | 250.1× | ≤ 8 | | MCap/BV"
AMZN,core_fx,1,-
AMZN,core_fx_date,n.m.,-
AMZN,core_oi,79975,"| |---|---|---| | EV/OI (FY2025 OI 79,975) — no-cash / all-cash |"
AMZN,core_ratio,1,-
AMZN,core_shares_diluted,10903,"Diluted weighted-average shares 10,903m (Q2 2026); shares"
AMZN,core_unit,m,-
ANDR.VI,core_cash,963.6,"€33.53. - EV/OI leg all-cash = (4,079.6 + 963.6 − 766.9 − 4.4) ÷ 98.673 ="
ANDR.VI,core_currency,EUR,-
ANDR.VI,core_debt_eq,771.3,"7 × 582.8 − 766.9 − 4.4) ÷ 98.673 = €33.53. - EV/OI leg all-cash = (4,079.6 + 963.6 − 766.9 − 4.4) ÷ 98.673 ="
ANDR.VI,core_fcf,454.6,"F. Valuation math - MCap/FCF = 8,189.8 ÷ 454.6 = 18.0×. EV/OI = 8,961.1 ÷"
ANDR.VI,core_fx,1,-
ANDR.VI,core_fx_date,n.m.,-
ANDR.VI,core_oi,582.8,"8,189.8 ÷ 454.6 = 18.0×. EV/OI = 8,961.1 ÷ 582.8 = 15.4× (no-cash); 7,997.5"
ANDR.VI,core_ratio,1,-
ANDR.VI,core_shares_diluted,98.673,EXPENSIVE. - Band: - FCF leg = 8 × 454.6 ÷ 98.673 = €36.86. - EV/OI leg
ANDR.VI,core_unit,m,-
ANF,core_cash,619.2,"− cash+STI 619.2 = EV_all-cash 5,653"
ANF,core_currency,USD,-
ANF,core_debt_eq,1292,"MCap 4,980 + debt-equivalent 1,292 (op leases 1,030 LT + 262 current; financial debt zero)"
ANF,core_fcf,378.4,"## F. Valuation math MCap 4,980 / FCF 378.4 = 13.2×. EV/OI: 6,272/699.1"
ANF,core_fx,1,-
ANF,core_fx_date,n.m.,-
ANF,core_oi,699.1,"4,980 / FCF 378.4 = 13.2×. EV/OI: 6,272/699.1 = 8.97× nc; 5,653/699.1 ="
ANF,core_ratio,1,-
ANF,core_shares_diluted,44.43,ac. Threshold-implied: FCF leg 8×378.4÷44.43 = $68.13; EV/OI legs
ANF,core_unit,m,-
ANF,future_reason,forces: entrants,new entrants STRONG
ANGI,future_reason,supplier conc.,Supplier breadth fails on the effective-supplier re
ANGI,past_reason,losses,Worst-of-four normalized ROCE −1.3%
ANGI,sf_reason,compensation,Hard strike
APH,core_cash,5419.1,"÷ 2,578.4 = $8.37; all-cash (41,080.2 + 5,419.1 − 19,507.5) ÷ 2,578.4 ="
APH,core_currency,USD,-
APH,core_debt_eq,19507.5,"stack = 18,811.3 + 565.7 + 121.5 + 9.0 = 19,507.5; no-cash (7 × 5,868.6 −"
APH,core_fcf,4378.1,"Current multiples: MCap/FCF = 224,218 ÷ 4,378.1 = 51.2×; EV/OI = 243,725 ÷"
APH,core_fx,1,-
APH,core_fx_date,n.m.,-
APH,core_oi,5868.6,"÷ 4,378.1 = 51.2×; EV/OI = 243,725 ÷ 5,868.6 = 41.5× (no-cash) / 238,306"
APH,core_ratio,1,-
APH,core_shares_diluted,2578.4,"2026 close, post-split). Diluted shares 2,578.4m (Q2-2026 weighted 1,289.2m"
APH,core_unit,m,-
APH,sf_reason,buybacks,"2×) and the 19% payout are sound, but repurchases are a live, repeated value transfer: FY2024 at"
APTV,future_reason,customer conc.,"ear earlier), the top ten 41%: customer breadth FAILS, waiver denied — these custo"
APTV,past_reason,8.1% ROCE,Worst-of-four normalized ROCE 8.1%
APTV,sf_reason,flag pair,FAIL (flag pair)
ARHS,past_reason,growth,Growth is negative and steep
ARHS,sf_reason,compensation,Comp: P17 hard strike
ARQ,aliases,"Advanced Emissions Solutions, Inc.","Arq, Inc. (formerly Advanced Emissions Solutions, Inc.)"
ARQ,past_reason,losses,Operating income is negative in nine of the ten window years
AS,core_cash,683.7,− 11.4)/581.82m = $6.70; all-cash (+683.7) = $7.88. Bounds: $6.70 /
AS,core_currency,USD,-
AS,core_debt_eq,1012.4,"7 × 701.8 − 1,001.0 − 11.4)/581.82m = $6.70; all-cash (+683.7) = $7.88. Bounds: $6.70 / $7.06 (labelled;"
AS,core_fcf,513.3,- Threshold-implied prices: FCF leg 8 × 513.3/581.82m = $7.06. EV/OI
AS,core_fx,1,-
AS,core_fx_date,n.m.,-
AS,core_oi,701.8,"= $7.06. EV/OI legs: no-cash (7 × 701.8 − 1,001.0 − 11.4)/581.82m ="
AS,core_ratio,1,-
AS,core_shares_diluted,581.82,prices: FCF leg 8 × 513.3/581.82m = $7.06. EV/OI legs:
AS,core_unit,m,-
AS,past_reason,5.6% ROCE,"normalized ROCE 5.6% (end-of-period, with-cash"
ASH,future_reason,2+ forces,Forces: 3 STRONG of 4
ASH,past_reason,losses,worst-of-four normalized average ROCE −0.6%
ASH,sf_reason,flag pair,Flag pair → FAIL
ASML.AS,core_cash,13321.9,"against €3,733.0m returned, cash+STI €13,321.9m → €7,581.5m — logged as a"
ASML.AS,core_currency,EUR,-
ASML.AS,core_debt_eq,4390.9,"EV builds use €3,700m (FY2025 total €4,390.9m less the €693.2m repaid),"
ASML.AS,core_fcf,11084.9,"FY2025 figures: OI €11,301.4m, FCF €11,084.9m, diluted 388.9m, cash+STI"
ASML.AS,core_fx,1,-
ASML.AS,core_fx_date,n.m.,-
ASML.AS,core_oi,11301.4,"year). Operative FY2025 figures: OI €11,301.4m, FCF €11,084.9m, diluted"
ASML.AS,core_ratio,1,-
ASML.AS,core_shares_diluted,388.9,"Threshold-implied prices (FY2025 basis, 388.9m diluted): MCap/FCF ≤ 8 →"
ASML.AS,core_unit,m,-
ASML.AS,past_reason,21% ROCE,Ex-cash ROCE 21–77% across the decade
ASML.AS,sf_reason,buybacks,"The repurchase lever is where this fails, and it fails on all t"
ASSA-B.ST,core_cash,1404,"Cash and equivalents 1,398 + short-term investments 6 = 1,404."
ASSA-B.ST,core_currency,SEK,-
ASSA-B.ST,core_debt_eq,65475,"lease liabilities 1,715 = 65,353. NCI 122."
ASSA-B.ST,core_fcf,18639,"investments 6 = 1,404. OI 23,151. FCF 18,639. BV 101,597. TBV −36,361."
ASSA-B.ST,core_fx,1,-
ASSA-B.ST,core_fx_date,n.m.,-
ASSA-B.ST,core_oi,23151,"+ short-term investments 6 = 1,404. OI 23,151. FCF 18,639. BV 101,597."
ASSA-B.ST,core_ratio,1,-
ASSA-B.ST,core_shares_diluted,1110.776,"price 24 July 2026). Diluted shares 1,110.776m; price SEK 347.10 → MCap"
ASSA-B.ST,core_unit,m,-
ASSA-B.ST,past_reason,ROCE decline,"blem is direction, not level: three consecutive down years in ROCE and two in FCFROCE, driven by"
ATCO-B.ST,core_cash,16129,"EV no-cash-excess = 940,063 + 34,899 + 177 = SEK 975,139m; EV all-cash-excess = SEK 959,010m"
ATCO-B.ST,core_currency,SEK,-
ATCO-B.ST,core_debt_eq,35076,"EV no-cash-excess = 940,063 + 34,899 + 177 = SEK 975,139m; EV all-cash-excess = SEK 959,010m"
ATCO-B.ST,core_fcf,26379,"Operative FY2025 figures: OI MSEK 34,114, FCF MSEK 26,379"
ATCO-B.ST,core_fcf_basis,FY2025 CFO − capex,-
ATCO-B.ST,core_fx,1,-
ATCO-B.ST,core_fx_date,n.m.,-
ATCO-B.ST,core_oi,34114,"Operative FY2025 figures: OI MSEK 34,114, FCF MSEK 26,379"
ATCO-B.ST,core_oi_basis,FY2025 reported,-
ATCO-B.ST,core_period,FY2025; B-equivalent shares at the 31 Jul 2026 A/B prices,-
ATCO-B.ST,core_ratio,1,-
ATCO-B.ST,core_shares_diluted,5345.82,"A 3,309,711,493 + B 1,560,876,032 shares excl. treasury): MCap SEK 940,063m"
ATCO-B.ST,core_unit,m,-
ATCO-B.ST,sf_reason,buybacks,The flag: the FY2024 and FY2025 tranches were nonetheless bought at 23
ATKR,future_reason,2+ forces,Forces: customer power STRONG (distributors consolidate
ATKR,past_reason,ROCE decline,But P4 fires: ROCE fell three consecutive years on both cash treatments (54
ATKR,sf_reason,buybacks,67bn repurchased FY2021–25 at 6
AUTO.OL,future_reason,customer conc.,Breadth FAIL: four distribution partners e
AUTO.OL,past_reason,4.2% ROCE,Worst-of-four normalized ROCE 4.2%
AUTO.OL,sf_reason,compensation,"FAIL — P17 hard strike, plus capital allocation ADVERSE"
AXFO.ST,core_cash,1076.5,"Trigger band: EV/OI leg P = (7 × 3,572.0 + 1,076.5 − 15,674.9 − 322.8) ÷"
AXFO.ST,core_currency,SEK,-
AXFO.ST,core_debt_eq,15997.7,"7 × 3,572.0 + 1,076.5 − 15,674.9 − 322.8) ÷ 216.827 = 10,082.5 ÷ 216.827 = SEK 46.5; MCap/FCF leg P = 8 ×"
AXFO.ST,core_fcf,5021.3,"lower, immaterial) - MCap/FCF = 58,261 ÷ 5,021.3 = 11.6× (threshold 8;"
AXFO.ST,core_fx,1,-
AXFO.ST,core_fx_date,n.m.,-
AXFO.ST,core_oi,3572,"28,044 | 7,388 | 7,208 | | 2025 | 89,152 | 3,572 | 6,751 | 1,730 | 5,021 |"
AXFO.ST,core_ratio,1,-
AXFO.ST,core_shares_diluted,216.827,"(price SEK 268.70, 2026-07-07; diluted WA 216.827m) - MCap = 268.70 × 216.827"
AXFO.ST,core_unit,m,-
AXP,future_reason,breadth,Breadth FAIL decides: WEAK
AXP,sf_reason,compensation,exceeds the US$30m absolute strike
AZA.ST,core_currency,SEK,-
AZA.ST,core_fcf,n.m.,CFO distorted by deposit/insurance flows
AZA.ST,core_fcf_basis,n.m. — deposit-funded,-
AZA.ST,core_fx,1,-
AZA.ST,core_fx_date,n.m.,-
AZA.ST,core_oi,n.m.,EV/OI n.m. (EV meaningless for deposit funding)
AZA.ST,core_oi_basis,n.m. — substitution rule (MCap/NI anchor),-
AZA.ST,core_period,FY2025,-
AZA.ST,core_ratio,1,-
AZA.ST,core_shares_diluted,157.829091,"shares 157,829,091 → MCap SEK 61,301m"
AZA.ST,core_unit,m,-
AZA.ST,past_reason,35.1% ROE,a 35.1% worst-variant normalized ROE
AZA.ST,printed_mcap_fcf,n.m.,CFO distorted by deposit/insurance flows
AZTA,past_reason,losses,every normalized return variant is negative
AZTA,sf_reason,compensation,Comp: P17 hard strike
BA.L,core_cash,3562,"ac (+3,562) = 496p"
BA.L,core_currency,GBP,-
BA.L,core_debt_eq,9204,"EV/OI nc (20,475 − 9,051 − 153)/2,990 = 377p"
BA.L,core_fcf,2475,"MCap/FCF 26.8× (on 2,475; 30.8× on company-defined 2,158)"
BA.L,core_fx,1,-
BA.L,core_fx_date,n.m.,-
BA.L,core_oi,2925,"EV/OI nc (20,475 − 9,051 − 153)/2,990 = 377p"
BA.L,core_period,FY2025,-
BA.L,core_ratio,1,-
BA.L,core_shares_diluted,2990,"Price 2,220p × 2,990m = £66,378m"
BA.L,core_unit,m,-
BA.L,past_reason,10.8% ROCE,worst-of-available normalized ROCE 10.79%
BA.L,printed_ev_oi,25.8,EV/OI 25.8× / 24.6×
BA.L,printed_ev_oi_all_cash,24.6,EV/OI 25.8× / 24.6×
BA.L,printed_mcap_fcf,26.8,"MCap/FCF 26.8× (on 2,475; 30.8× on company-defined 2,158)"
BA.L,sf_reason,acquisitions,5× EBITDA — a hard lower bound of ~19
BAS.DE,future_reason,moat eroding,"integration is a genuine cost moat, but eroding where most of the capital sit"
BAS.DE,past_reason,5.8% ROCE,worst-of-four 10-year normalized ROCE is 5.8%
BAS.DE,sf_reason,buybacks,"P19: the FY2025 tranche (€355m, 8"
BAYN.DE,future_reason,forces: substitutes,substitutes STRONG
BAYN.DE,past_reason,1.5% ROCE,worst-of-four ROCE of 1.5%
BAYN.DE,sf_reason,compensation,"P17 hard strike: FY2025 net income −€3,620m makes 5% of lower(FCF"
BBBY,aliases,"Beyond, Inc.; Overstock.com, Inc.","Bed Bath & Beyond, Inc. (f/k/a Beyond, Inc.; f/k/a Overstock.com, Inc.)"
BBBY,future_reason,2+ forces,substitutes STRONG
BBBY,past_reason,losses,"−62% from the FY2021 peak $2,756m), operating loss $61"
BBBY,sf_reason,compensation,"th negative too), so any more-than-token pay is a hard strike — Executive Chairman/PEO Marcus Lemonis's March-2"
BBWI,core_cash,820,"− 4,713)÷201.56 = $15.72; all-cash (+820) = $19.79. Range width"
BBWI,core_currency,USD,-
BBWI,core_debt_eq,4713,"= $34.33; EV/OI no-cash (7×1,126 − 4,713)÷201.56 = $15.72; all-cash"
BBWI,core_fcf,865,"## F. Valuation math MCap 4,060 / FCF 865 = 4.69× (passes). EV/OI:"
BBWI,core_fx,1,-
BBWI,core_fx_date,n.m.,-
BBWI,core_oi,1126,"/ FCF 865 = 4.69× (passes). EV/OI: 8,773/1,126 = 7.79× no-cash;"
BBWI,core_ratio,1,-
BBWI,core_shares_diluted,201.56,by 0.9%. Threshold-implied: FCF leg 8×865÷201.56 = $34.33; EV/OI no-cash
BBWI,core_unit,m,-
BBWI,past_reason,growth,ΔOI/sh −7.5%/yr geometric
BC.MI,future_reason,forces: suppliers,supplier power STRONG
BC.MI,past_reason,leverage,Leverage breaks it: L/E 267.1% against P5's 200
BC.MI,sf_reason,buybacks,FAIL — P19 hard strike (dilution sterilisation)
BC8.DE,core_cash,452,"= EV conservative 4,649.3; − cash & STI 452.0 = EV all-cash 4,197.3."
BC8.DE,core_currency,EUR,-
BC8.DE,core_debt_eq,758.4,"7 × 335.296 − 755.7 − 2.7)/126.0 = €12.61; all-cash variant €16.20. Binding (both primaries, conservative"
BC8.DE,core_fcf,145.127,Trigger legs: MCap/FCF ≤ 8 → P = 8 × 145.127/126.0 = €9.21; EV/OI ≤ 7
BC8.DE,core_fx,1,-
BC8.DE,core_fx_date,n.m.,-
BC8.DE,core_oi,335.296,€9.21; EV/OI ≤ 7 conservative → P = (7 × 335.296 − 755.7 − 2.7)/126.0 =
BC8.DE,core_ratio,1,-
BC8.DE,core_shares_diluted,126,"## F. Valuation math Price €30.88 × 126.0m = MCap €3,890.9m. MCap/FCF"
BC8.DE,core_unit,m,-
BC8.DE,past_reason,ROCE decline,But the ROCE series declines monotonically from FY2021 on the end-CE basis (14
BEI.DE,past_reason,ROCE decline,Both decline across the window: ROCE 20
BEI.DE,sf_reason,buybacks,FAIL — two P19 hard strikes
BH,aliases,BH.A,Biglari Holdings Inc. (Class B line; Class A = BH.A)
BH,past_reason,losses,"−$3.8m, −$37.5m across 2022–25"
BH,sf_reason,compensation,Comp: hard strike
BILI-A.ST,future_reason,forces: suppliers,supplier power STRONG
BILI-A.ST,past_reason,ROCE decline,Returns in sustained decline: beg-CE ROCE 16
BILI-A.ST,sf_reason,flag pair,FAIL — flag pair (P17 + P19)
BKE,future_reason,forces: substitutes,substitutes STRONG
BKE,sf_reason,compensation,FAIL — P17 proportionality hard strike
BKNG,core_cash,17214,"total debt $20,694m; cash & STI $17,214m; FY2025 OI $8,825m, FCF"
BKNG,core_currency,USD,-
BKNG,core_debt_eq,20694,"751.3805m; MCap $145,971m; total debt $20,694m; cash & STI $17,214m;"
BKNG,core_fcf,9087,"& STI $17,214m; FY2025 OI $8,825m, FCF $9,087m; TTM OI $9,284m, TTM FCF"
BKNG,core_fx,1,-
BKNG,core_fx_date,n.m.,-
BKNG,core_oi,8825,"$20,694m; cash & STI $17,214m; FY2025 OI $8,825m, FCF $9,087m; TTM OI"
BKNG,core_ratio,1,-
BKNG,core_shares_diluted,751.3805,"(close 2026-08-04); shares outstanding 751.3805m; MCap $145,971m; total"
BKNG,core_unit,m,-
BKNG,past_reason,27.5% ROCE,Worst-of-four normalized averages over FY2016–FY2025 are ROCE 27.5%
BKNG,sf_reason,buybacks,"against that, the live tranche executed at 14"
BMI,core_cash,95.7,"÷ 29.142 = $43.21. - All-cash: (1,283.9 + 95.7 − 12.7 − 12.0) ÷ 29.142 ="
BMI,core_currency,USD,-
BMI,core_debt_eq,24.7,"7 × 183.4 = 1,283.9. - No-cash: (1,283.9 − 12.7 − 12.0) ÷ 29.142 = $43.21. - All-cash: (1,283.9 + 95.7 − 12.7"
BMI,core_fcf,169.7,"MCap $3,723.5m. - MCap/FCF: 3,723.5 ÷ 169.7 (FY2025) = 21.9×; ÷ 150.3"
BMI,core_fx,1,-
BMI,core_fx_date,n.m.,-
BMI,core_oi,183.4,"÷ 150.3 (TTM) = 24.8×. - EV/OI (FY2025 OI 183.4): no-cash 3,748.2 ÷ 183.4 ="
BMI,core_ratio,1,-
BMI,core_shares_diluted,29.142,math Price $127.77 (2 Oct 2026). Shares 29.142m (Q2 2026 diluted w-avg;
BMI,core_unit,m,-
BMI,sf_reason,buybacks,Capital allocation is CAUTION. The Q4 2025 buyback ($15m)
BN.PA,future_reason,moat eroding,"cialized Nutrition (Aptamil, Nutricia), eroding in dairy/waters"
BN.PA,past_reason,7.5% ROCE,Worst-of-four normalized ROCE 7.5%
BN.PA,sf_reason,buybacks,P19 repetition hard strike
BNR.DE,core_cash,797.9,"MCap 8,533 + debt(incl leases) 3,325.8 + NCI 34.5 − cash 797.9 = €11,096m (consv)"
BNR.DE,core_currency,EUR,-
BNR.DE,core_debt_eq,3360.3,"MCap 8,533 + debt(incl leases) 3,325.8 + NCI 34.5 − cash 797.9 = €11,096m (consv)"
BNR.DE,core_fcf,673.7,"MCap/FCF 8,533/673.7 = 12.7×"
BNR.DE,core_fx,1,-
BNR.DE,core_fx_date,n.m.,-
BNR.DE,core_oi,617.6,"EV/OI 11,096/617.6 = 18.0× consv / 19.3× no-cash (>7)"
BNR.DE,core_oi_basis,FY2025 reported,-
BNR.DE,core_period,FY2025,-
BNR.DE,core_ratio,1,-
BNR.DE,core_shares_diluted,144.385,"@ €59.10, 144.385m sh: MCap €8,533m; EV consv €11,096m, no-cash €11,893m"
BNR.DE,core_unit,m,-
BNR.DE,past_reason,ROCE decline,3% (2025) — three consecutive declines
BOL.ST,future_reason,breadth,Breadth FAIL
BOL.ST,sf_reason,buybacks,FAIL — P19 hard strike (dilution sterilisation)
BOX,past_reason,losses,every normalized ROCE average is negative
BOX,sf_reason,flag pair,Flag pair → SF FAIL
BRG.OL,core_cash,125,"÷ 99.645 = NOK 67.46; all-cash (9,009 + 125 − 2,287) ÷ 99.645 = NOK"
BRG.OL,core_currency,NOK,-
BRG.OL,core_debt_eq,2287,"= NOK 67.46; all-cash (9,009 + 125 − 2,287) ÷ 99.645 = NOK 68.71; the"
BRG.OL,core_fcf,563,"F. Valuation math - MCap/FCF = 15,265.6 ÷ 563 = 27.1× (replacement-capex"
BRG.OL,core_fx,1,-
BRG.OL,core_fx_date,n.m.,-
BRG.OL,core_oi,1287,"÷ 780 = 19.6×). EV/OI = 17,552.6 ÷ 1,287 = 13.6× (no-cash) /"
BRG.OL,core_ratio,1,-
BRG.OL,core_shares_diluted,99.645,= 2.8×. - FCF leg: all-capex 8 × 563 ÷ 99.645 = NOK 45.20;
BRG.OL,core_unit,m,-
BRK.B,core_currency,USD,-
BRK.B,core_fcf,25042,"MCap/FCF = 1,054,290 / 25,042 = 42.1×"
BRK.B,core_fx,1,-
BRK.B,core_fx_date,n.m.,-
BRK.B,core_oi,n.m.,the operative gauge is price-to-book
BRK.B,core_oi_basis,n.m. — substitution rule (P/B anchor),-
BRK.B,core_period,FY2025,-
BRK.B,core_ratio,1,-
BRK.B,core_shares_diluted,2157.335,"Threshold-implied prices (per Class B share; shares 2,157.335M)"
BRK.B,core_unit,m,-
BRK.B,printed_ev_oi,n.m.,the operative gauge is price-to-book
BRZE,future_reason,no moat,no moat-decides floor available
BRZE,past_reason,ROCE decline,"WEAK — P4 on level, trivially"
BRZE,sf_reason,compensation,P17 hard strike: CEO Magnuson FY2026 total ≈ $14
BTI,core_cash,3843,"P(EV/OI = 7, conservative EV) = (7 × 9,997 + 3,843 − 35,070 − 2,112) ÷ 2,160"
BTI,core_currency,GBP,-
BTI,core_debt_eq,37182,"P(EV/OI = 7, conservative EV) = (7 × 9,997 + 3,843 − 35,070 − 2,112) ÷ 2,160"
BTI,core_fcf,5791,"P(MCap/FCF = 8) = 8 × 5,791 ÷ 2,160 = £21.45 (≈ $28.97)"
BTI,core_fx,1.3506,"GBP/USD 1.3506, 16 Jul 2026 intraday"
BTI,core_fx_date,2026-07-16,"GBP/USD 1.3506, 16 Jul 2026 intraday"
BTI,core_oi,9997,"P(EV/OI = 7, conservative EV) = (7 × 9,997 + 3,843 − 35,070 − 2,112) ÷ 2,160"
BTI,core_oi_basis,FY2025 reported,-
BTI,core_period,FY2025,-
BTI,core_ratio,1,-
BTI,core_shares_diluted,2160,"P(MCap/FCF = 8) = 8 × 5,791 ÷ 2,160 = £21.45 (≈ $28.97)"
BTI,core_unit,m,-
BTI,trigger,22.91,(≈ $22.91)
BVI.PA,core_cash,946,"liabilities 411.1, NCI 46.0, cash + STI 946.0. Current multiples (both EV"
BVI.PA,core_currency,EUR,-
BVI.PA,core_debt_eq,3088.1,"− 411.1 − 0 − 46.0) ÷ 445.0 = (6,946.8 − 3,088.1) ÷ 445.0 = €8.67. - EV/OI"
BVI.PA,core_fcf,824.2,"OI (to 30 Jun 2026) €910.1m; FY2025 FCF €824.2m (company basis,"
BVI.PA,core_fx,1,-
BVI.PA,core_fx_date,n.m.,-
BVI.PA,core_oi,992.4,"MCap €12,655.8m; FY2025 statutory OI €992.4m; TTM OI (to 30 Jun 2026)"
BVI.PA,core_ratio,1,-
BVI.PA,core_shares_diluted,445,"| *430.8* | *241.3* | *71.2* | *157.7* | *445 (TTM)* | *6,992.9* |"
BVI.PA,core_unit,m,-
CALX,past_reason,1.9% ROCE,Worst-of-four normalized ROCE 1.94%
CALX,sf_reason,compensation,P17 hard strike
CARL-B.CO,core_cash,9653,"all-cash (+ 9,653) = DKK 100"
CARL-B.CO,core_currency,DKK,-
CARL-B.CO,core_debt_eq,76430,"EV/OI leg no-cash (7 × 11,430 − 60,112 − 13,452 − 2,866) ÷ 132.54 = DKK 27"
CARL-B.CO,core_fcf,6839,"MCap/FCF = 118,953 ÷ 6,839 = 17.4×"
CARL-B.CO,core_fx,1,-
CARL-B.CO,core_fx_date,n.m.,-
CARL-B.CO,core_oi,11430,"EV/OI = 195,383 ÷ 11,430 = 17.1× (no-cash); 185,730 ÷ 11,430 = 16.2× (all-cash)"
CARL-B.CO,core_oi_basis,FY2025 reported,-
CARL-B.CO,core_period,FY2025; B-equivalent shares at the 2 Oct 2026 A/B prices,-
CARL-B.CO,core_ratio,1,-
CARL-B.CO,core_shares_diluted,138.770,"MCap: A 33,699,252 × 1,025.0 = 34,542; B 98,472,748 × 857.20 = 84,411 → 118,953"
CARL-B.CO,core_unit,m,-
CARL-B.CO,past_reason,9.5% ROCE,Worst-of-four average ROCE is 9.5%
CARL-B.CO,sf_reason,acquisitions,"itvic, bought for about DKK 36bn, roughly 20× its pre-deal operating profit, on debt"
CAT,past_reason,leverage,"Leverage decides: L/E 362% consolidated, 244% on the MP&E-only statements"
CAT,sf_reason,buybacks,Capital allocation ADVERSE: H1 2026 repurchases of $6
CBLL,past_reason,losses,"Two years, both loss-making"
CBLL,sf_reason,compensation,Comp: hard strike
CC,future_reason,2+ forces,Forces: customer power STRONG (TiO2 is a spec-identical commodity
CC,past_reason,3.4% ROCE,Worst-of-four normalized ROCE 3.39%
CC,sf_reason,compensation,P17 hard strike
CDI.PA,past_reason,ROCE decline,"NG, and beginning-CE ROCE has fallen two straight years from the 2023 peak (19"
CDI.PA,sf_reason,acquisitions,Everything adverse sits below: the Tiffany acquisition audit reads 22
CDR.WA,core_cash,1003.0,"no-cash 7 × 470.6/99.91m = PLN 33.0; all-cash (+1,003.0) = PLN 43.0"
CDR.WA,core_currency,PLN,-
CDR.WA,core_debt_eq,0,"no-cash 7 × 470.6/99.91m = PLN 33.0; all-cash (+1,003.0) = PLN 43.0"
CDR.WA,core_fcf,-47.2,MCap/FCF n.m. (FCF −47.2m)
CDR.WA,core_fx,1,-
CDR.WA,core_fx_date,n.m.,-
CDR.WA,core_oi,470.6,"no-cash 7 × 470.6/99.91m = PLN 33.0; all-cash (+1,003.0) = PLN 43.0"
CDR.WA,core_oi_basis,FY2025 reported,-
CDR.WA,core_period,FY2025,-
CDR.WA,core_ratio,1,-
CDR.WA,core_shares_diluted,99.91,PLN 25.5bn (99.91m sh)
CDR.WA,core_unit,m,-
CDR.WA,future_reason,customer conc.,Customer breadth FAIL
CDR.WA,sf_reason,buybacks,cation CAUTION (1 flag) — episodic criterion-free repurchases with one bad print: 2020's PLN 214
CELH,future_reason,customer conc.,"Breadth FAILS on the customer side, and no"
CELH,past_reason,5% ROCE,Worst-of-four normalised average ROCE is 5.03%
CELH,sf_reason,compensation,Breach on both is a P17 hard strike
CERT,past_reason,0.3% ROCE,normalized ROCE ≈ 0.3%
CERT,sf_reason,compensation,Hard strike → SF FAIL
CGNX,future_reason,breadth,Breadth FAILS
CGNX,sf_reason,compensation,P17 is a hard strike: former CEO Willett's FY2025 $8
COHU,past_reason,0.7% ROCE,Worst-of-four normalized ROCE 0.66%
COHU,sf_reason,compensation,P17 hard strike
COLO-B.CO,core_cash,947,"Debt 22,639 (incl. leases 958); cash 947; NCI nil"
COLO-B.CO,core_currency,DKK,-
COLO-B.CO,core_debt_eq,22639,"Debt 22,639 (incl. leases 958); cash 947; NCI nil"
COLO-B.CO,core_fcf,5339,"FCF 8 × 5,339 / 225.17 = 189.7"
COLO-B.CO,core_fx,1,-
COLO-B.CO,core_fx_date,n.m.,-
COLO-B.CO,core_oi,7201,"EV/OI no-cash (7 × 7,201 − 22,639)/225.17 = 123.3"
COLO-B.CO,core_period,FY2025,-
COLO-B.CO,core_ratio,1,-
COLO-B.CO,core_shares_diluted,225.17,"Price 426.10 × 225.17m = MCap 95,945"
COLO-B.CO,core_unit,m,-
COLO-B.CO,printed_ev_oi,16.5,EV/OI 16.5× / 16.3×
COLO-B.CO,printed_ev_oi_all_cash,16.3,EV/OI 16.5× / 16.3×
COLO-B.CO,printed_mcap_fcf,18.0,MCap/FCF 18.0×
COLO-B.CO,sf_reason,acquisitions,allocation CAUTION (1 flag) — Atos Medical at ~27× EBITDA (DKK 16
COMP,future_reason,2+ forces,Forces: customer power STRONG — post-NAR-settlement commission compre
COMP,past_reason,losses,improving monotonically since FY2022 but never positive
COMP,sf_reason,acquisitions,or a low-margin franchise/brokerage complex whose pre-deal standalone OI is not cleanly separable at tier-2
CON.DE,core_cash,1641,"all-cash variant (7 × 2,035 + 1,641 − 6,826 − 224)/200.006 = €44.2"
CON.DE,core_currency,EUR,-
CON.DE,core_debt_eq,7050,"Reported-OI leg: (7 × 272 − 7,050)/200.006 < 0 → n.m."
CON.DE,core_fcf,942,"MCap/FCF = 14,456/942 = 15.3×"
CON.DE,core_fx,1,-
CON.DE,core_fx_date,n.m.,-
CON.DE,core_oi,272,"EV/OI reported = 19,865/272 = 73.0× and 21,506/272 = 79.1×"
CON.DE,core_oi_basis,FY2025 reported (adj-EBIT is the memo's tagged band basis),-
CON.DE,core_period,FY2025,-
CON.DE,core_ratio,1,-
CON.DE,core_shares_diluted,200.006,"@ €72.28 × 200.006m = MCap €14,456m"
CON.DE,core_unit,m,-
CON.DE,past_reason,6.6% ROCE,worst-of-four normalized ROCE 6.6%
COPN.SW,aliases,Cosmo Pharmaceuticals N.V.,Cosmo N.V. (formerly Cosmo Pharmaceuticals N.V.)
COPN.SW,future_reason,customer conc.,Breadth: customer side FAIL — top three customers 25
COPN.SW,past_reason,2.9% ROCE,Worst-of-four normalized ROCE 2.9%
COPN.SW,sf_reason,buybacks,"P19 hard strikes: FY2023 repurchases (221,373 sh @ ~€56"
COST,core_cash,15284,"FCF $7,837m, diluted 444.8m, cash+STI $15,284m, debt $9,935m, equity"
COST,core_currency,USD,-
COST,core_debt_eq,9935,"diluted 444.8m, cash+STI $15,284m, debt $9,935m, equity $29,164m, goodwill"
COST,core_fcf,7837,"$13.93m = 0.18% of the lower leg (FCF $7,837m; the 5% line is $392m);"
COST,core_fx,1,-
COST,core_fx_date,n.m.,-
COST,core_oi,10383,"year). Operative FY2025 figures: OI $10,383m, FCF $7,837m, diluted"
COST,core_ratio,1,-
COST,core_shares_diluted,444.8,"Threshold-implied prices (FY2025 basis, 444.8m diluted): FCF leg $140.95;"
COST,core_unit,m,-
COST,sf_reason,buybacks,The repurchase lever fails on all three ADVERSE limbs
COTY,future_reason,forces: entrants,new entrants STRONG
COTY,past_reason,2.9% ROCE,Worst-of-four normalized ROCE 2.86%
COTY,sf_reason,flag pair,SF FAIL (flag pair: P17 normalized-read breach
COUR,future_reason,moat eroding,r catalog + 175m registered learners) — eroding at the demand line
COUR,past_reason,losses,"improving, never positive"
COUR,sf_reason,compensation,CEO Hart appointed Feb 2025 with a disclosed $34m compensation package (panabee/8-K digest) vs FY2025 ceilings $
CPR.MI,past_reason,8.1% ROCE,Worst-of-four ROCE is 8.1%
CPR.MI,sf_reason,compensation,Hard strike on pay
CRCT,core_cash,256.2,Leases $11.6m; no debt; cash $256.2m
CRCT,core_currency,USD,-
CRCT,core_debt_eq,11.624,EV/OI no-cash (7 × 96.033 − 11.624)/209.44 = $3.15
CRCT,core_fcf,175.813,FCF 8 × 175.813/209.44 = $6.72
CRCT,core_fx,1,-
CRCT,core_fx_date,n.m.,-
CRCT,core_oi,96.033,EV/OI no-cash (7 × 96.033 − 11.624)/209.44 = $3.15
CRCT,core_ratio,1,-
CRCT,core_shares_diluted,209.44,"Price $5.84 × 209.44m = MCap $1,223.1m"
CRCT,core_unit,m,-
CRCT,printed_ev_oi,12.9,EV/OI 12.9× / 10.2× — fails P8 on both variants
CRCT,printed_ev_oi_all_cash,10.2,EV/OI 12.9× / 10.2× — fails P8 on both variants
CRCT,printed_mcap_fcf,7.0,MCap/FCF 7.0× — passes P7
CRI,future_reason,2+ forces,Forces: customer power STRONG — the mass retailers buying the wholesa
CRI,past_reason,growth,net income $256m → $91.8m
CRI,sf_reason,compensation,PASS (1 flag — P17 fiscal-year-read breach; P19 SOUND on an incomplete repurchase record)
CRL.MI,core_cash,126.2,"7 × 81.96 − 119.2 − 50.3 − 5.8) ÷ 112.49 = 398.3 ÷ 112.49 = €3.54. - EV/OI leg, all-cash: (573.7 + 126.3 −"
CRL.MI,core_currency,EUR,-
CRL.MI,core_debt_eq,175.3,"7 × 81.96 − 119.2 − 50.3 − 5.8) ÷ 112.49 = 398.3 ÷ 112.49 = €3.54. - EV/OI leg, all-cash: (573.7 + 126.3 −"
CRL.MI,core_fcf,97.4,"Current multiples: MCap/FCF = 3,211.7 ÷ 97.4 = 33.0×. EV/OI = 3,387.0 ÷"
CRL.MI,core_fx,1,-
CRL.MI,core_fx_date,n.m.,-
CRL.MI,core_oi,81.96,"OI to 30 Jun 2026 is €106.9m (81.96 + 61.74 − 36.77), giving"
CRL.MI,core_ratio,1,-
CRL.MI,core_shares_diluted,112.49,still EXPENSIVE. Threshold-implied prices (112.49m shares): - FCF leg: 8 ×
CRL.MI,core_unit,m,-
CRL.MI,sf_reason,acquisitions,apital allocation is CAUTION: most deals cost 6–16× EBITDA and Cotes (2026) about 8
CRM,sf_reason,buybacks,FAIL (restated) — one strike: buyback discipline
CROX,core_cash,170.3,"MCap $5,854.6M · EV $7,543.8M no-cash / $7,373.5M all-cash"
CROX,core_currency,USD,-
CROX,core_debt_eq,1689.2,"MCap $5,854.6M · EV $7,543.8M no-cash / $7,373.5M all-cash"
CROX,core_fcf,659.2,levered FCF $659.2M
CROX,core_fcf_basis,FY2025 levered FCF,-
CROX,core_fx,1,-
CROX,core_fx_date,n.m.,-
CROX,core_oi,887.6,OI ex-impairment $887.6M
CROX,core_oi_basis,FY2025 ex-impairment,-
CROX,core_period,FY2025; BS Q2 2026,-
CROX,core_ratio,1,-
CROX,core_shares_diluted,47.945075,"shares 47,945,075 · MCap $5,854.6M"
CROX,core_unit,m,-
CROX,sf_reason,buybacks,"CAUTION: no new evidence exists, since the first repurchase tranche under the ≈$2"
CRWD,past_reason,losses,GAAP operating income is negative in all eight public fiscal years
CRWD,sf_reason,compensation,Hard strike on both reads
CSG.AS,future_reason,customer conc.,"Customer breadth FAILS: Ukraine's MoD (€1,343m, 19"
CSG.AS,past_reason,leverage,WEAK (P4: leverage breach without P6 conditions)
CSG.AS,sf_reason,flag pair,But two independent flags force FAIL under §2·1C: (1) RPT scale and timing
CSU.TO,core_cash,3089,"EV/OI = 43,716 / 1,893 = 23.1× (all-cash) · 46,805 / 1,893 = 24.7× (no-cash)"
CSU.TO,core_currency,USD,-
CSU.TO,core_debt_eq,5528,"EV/OI leg (conservative, no-cash) = (7×1,893 − 4,554 − 282 − 692) / 21.1915m"
CSU.TO,core_fcf,2664,"MCap/FCF = 41,277 / 2,664 = 15.5×"
CSU.TO,core_fx,1.4069,"21,191,500 sh; USD/CAD 1.4069"
CSU.TO,core_fx_date,-,-
CSU.TO,core_oi,1893,"EV/OI = 43,716 / 1,893 = 23.1× (all-cash) · 46,805 / 1,893 = 24.7× (no-cash)"
CSU.TO,core_oi_basis,FY2025 reported,-
CSU.TO,core_period,FY2025,-
CSU.TO,core_ratio,1,-
CSU.TO,core_shares_diluted,21.1915,"FCF leg = 8 × 2,664m / 21.1915m = US$1,006 ≈ CAD 1,415"
CSU.TO,core_unit,m,-
DBX,core_cash,1110,"− 3,980)/225.03 = $3.75; ac (4,823.7 + 1,110 − 3,980)/225.03 = $8.68;"
DBX,core_currency,USD,-
DBX,core_debt_eq,3980,"legs (7 × 689.1 = 4,823.7): nc (4,823.7 − 3,980)/225.03 = $3.75; ac"
DBX,core_fcf,930.8,"1,110 − 3,980)/225.03 = $8.68; FCF leg 8 × 930.8/225.03 = $33.09 → EV/OI"
DBX,core_fx,1,-
DBX,core_fx_date,n.m.,-
DBX,core_oi,689.1,"(negative book). Band: EV/OI legs (7 × 689.1 = 4,823.7): nc (4,823.7 −"
DBX,core_ratio,1,-
DBX,core_shares_diluted,225.03,F. Valuation math Price $34.81 · shares 225.03m · MCap $7.83bn. EV: ac
DBX,core_unit,m,-
DBX,past_reason,6% ROCE,worst-of-four ROCE ≈ 6–7.6%
DBX,sf_reason,buybacks,The conduct: repurchases of ≈$1
DCI,core_cash,250.4,"$23.89. - EV/OI leg, all-cash: (4,199.3 + 250.4 − 1,382.7) ÷ 117.9 ="
DCI,core_currency,USD,-
DCI,core_debt_eq,1382.7,"$28.93. - EV/OI leg, no-cash: (7 × 599.9 − 1,382.7) ÷ 117.9 = (4,199.3 −"
DCI,core_fcf,426.3,"(FY2026, $88.65): MCap/FCF = 10,275.4 ÷ 426.3 = 24.1×. EV/OI = 11,658.1 ÷"
DCI,core_fx,1,-
DCI,core_fx_date,n.m.,-
DCI,core_oi,599.9,"÷ 426.3 = 24.1×. EV/OI = 11,658.1 ÷ 599.9 = 19.4× no-cash, 11,407.7 ÷"
DCI,core_ratio,1,-
DCI,core_shares_diluted,117.9,→ EXPENSIVE. Threshold-implied prices (÷ 117.9m diluted): - FCF leg: 8 ×
DCI,core_unit,m,-
DCI,sf_reason,buybacks,Capital allocation CAUTION: buybacks were funded largely from FCF but executed at 16–
DCO,past_reason,2.1% ROCE,Worst-of-four normalized ROCE 2.09%
DCO,sf_reason,compensation,P17 hard strike
DDOG,past_reason,losses,GAAP operating income is negative in seven of eight window years
DDOG,sf_reason,compensation,Hard strike on both reads
DEC.PA,future_reason,2+ forces,"Forces: customer power STRONG (agency-intermediated buying, fluid dis"
DEC.PA,past_reason,3% ROCE,Worst-of-four normalized average ROCE 3.0%
DG.PA,future_reason,2+ forces,Two strong forces in the unit carrying 82% of revenue is
DG.PA,past_reason,8.4% ROCE,Worst-of-four normalised ROCE 8.4%
DG.PA,sf_reason,acquisitions,6× EV/OI and 8
DGE.L,future_reason,moat eroding,"The moat is brand, and it is eroding where it earns most"
DGE.L,past_reason,leverage,A leverage breach without the exemption makes Past
DGE.L,sf_reason,buybacks,3bn and $1bn were spent on buybacks in FY2018–FY2024 at 17–48× earnings
DLB,core_cash,702.6,"EV build (MCap 5,670): EV_nc 5,708.9; EV_ac 5,006.3."
DLB,core_currency,USD,-
DLB,core_debt_eq,38.9,"EV build (MCap 5,670): EV_nc 5,708.9; EV_ac 5,006.3."
DLB,core_fcf,435.9,"MCap/FCF = 5,670 ÷ 435.9 = 13.0"
DLB,core_fx,1,-
DLB,core_fx_date,n.m.,-
DLB,core_oi,265.0,"EV/OI = 5,708.9 ÷ 265.0 = 21.5 (no-cash); 5,006.3 ÷ 265.0 = 18.9 (all-cash)"
DLB,core_oi_basis,FY2025 reported,-
DLB,core_period,FY2025; shares = MCap ÷ price at the memo,-
DLB,core_ratio,1,-
DLB,core_shares_diluted,93.688,"MCap/FCF = 5,670 ÷ 435.9 = 13.0"
DLB,core_unit,m,-
DLB,past_reason,ROCE decline,No sustained decline (P4 clean — OI rising since FY2022)
DLB,sf_reason,buybacks,"P19: CAUTION — a continuous, criterion-free repurchase ladder ($162–567m/yr, every year, ~16–27× on the"
DLG.MI,core_cash,1243243,"| | NCI | €197,801k | | Cash & STI | €1,243,243k | | EV (all-cash-excess) |"
DLG.MI,core_currency,EUR,-
DLG.MI,core_debt_eq,731394,"Debt = 430,559 + 103,034 = 533,593 (leases included). NCI 197,801."
DLG.MI,core_fcf,445755,"| €458,145k | | FY2025 FCF (derived) | €445,755k | Multiples. MCap/FCF"
DLG.MI,core_fx,1,-
DLG.MI,core_fx_date,n.m.,-
DLG.MI,core_oi,458145,"netted) | €6,550,036k | | FY2025 OI | €458,145k | | FY2025 FCF (derived) |"
DLG.MI,core_ratio,1,-
DLG.MI,core_shares_diluted,149.887738,"prices. MCap/FCF ≤ 8 → 8 × 445,755 ÷ 149,887.738 = €23.79. EV/OI ≤ 7 → (7 ×"
DLG.MI,core_unit,k,-
DLG.MI,sf_reason,flag pair,FAIL (flag pair)
DNP.WA,core_cash,954.8,− 472.8)/980.4m = PLN 14.09; all-cash (+954.8) = PLN 15.07. Bounds
DNP.WA,core_currency,PLN,-
DNP.WA,core_debt_eq,472.8,"4.98. EV/OI legs: no-cash (7 × 2,041.3 − 472.8)/980.4m = PLN 14.09;"
DNP.WA,core_fcf,610.4,- Threshold-implied prices: FCF leg 8 × 610.4/980.4m = PLN 4.98. EV/OI
DNP.WA,core_fx,1,-
DNP.WA,core_fx_date,n.m.,-
DNP.WA,core_oi,2041.3,"= PLN 4.98. EV/OI legs: no-cash (7 × 2,041.3 − 472.8)/980.4m = PLN"
DNP.WA,core_ratio,1,-
DNP.WA,core_shares_diluted,980.4,prices: FCF leg 8 × 610.4/980.4m = PLN 4.98. EV/OI legs:
DNP.WA,core_unit,m,-
DOCU,future_reason,no moat,roding at the commodity end — no moat-decides floor
DOCU,past_reason,losses,worst-of-four normalized ROCE is −10.9%
DOCU,sf_reason,buybacks,P19: buybacks above the 20× hard-strike line in four consecuti
DOV,core_cash,1756,"135.553 = $47.40. - All-cash: (9,941.4 + 1,756.0 − 3,260.0 − 256.4) ÷"
DOV,core_currency,USD,-
DOV,core_debt_eq,3516.4,"7 × 1,420.2 = 9,941.4. - No-cash: (9,941.4 − 3,260.0 − 256.4) ÷ 135.553 = $47.40. - All-cash: (9,941.4 +"
DOV,core_fcf,1117.7,"MCap $25,713m. - MCap/FCF: 25,713.0 ÷ 1,117.7 (FY2025) = 23.0×; ÷ 1,176.6"
DOV,core_fx,1,-
DOV,core_fx_date,n.m.,-
DOV,core_oi,1420.2,"÷ 1,176.6 (TTM) = 21.9×. - EV/OI (TTM OI 1,420.2): no-cash 29,229.4 ÷"
DOV,core_ratio,1,-
DOV,core_shares_diluted,135.553,math Price $189.69 (2 Oct 2026). Shares 135.553m (Q2 2026 diluted w-avg;
DOV,core_unit,m,-
DOV,sf_reason,acquisitions,"04bn) cost 25–27× FCF but 19–23× EV/OI, so they are above conservative worth but below t"
DSY.PA,past_reason,9.6% ROCE,Worst-of-four normalized 10y average ROCE is 9.6%
DSY.PA,sf_reason,acquisitions,Acquisition audit: Medidata
DUOL,future_reason,supplier conc.,Supplier breadth fails: Apple processes about 60% o
DUOL,past_reason,1.4% ROCE,worst-of-four average ROCE is 1.4%
DUOL,sf_reason,buybacks,"l allocation is ADVERSE: $70m of 2026 open-market buybacks at $98–112 (about 28× EV/OI, 14× FCF), described"
EDEN.PA,future_reason,2+ forces,Forces: customer power STRONG — merchants have won statutory fee caps
EDEN.PA,past_reason,7% ROCE,Worst-of-four normalized ROCE is 6.97%
EDEN.PA,sf_reason,acquisitions,Reward Gateway (2023) cost ≈25
EKTA-B.ST,core_cash,3189,"shares outstanding ex-treasury 382.083m; diluted 382.216m; FY2026 OI 234; FY2026 FCF 1,392; cash & STI 3,189; total debt 7,331 (incl. leases 1,014); preferred 0; NCI 49"
EKTA-B.ST,core_currency,SEK,-
EKTA-B.ST,core_debt_eq,7380,"EV no-cash-excess = 17,958 + 7,331 + 49 = 25,338"
EKTA-B.ST,core_fcf,1392,"shares outstanding ex-treasury 382.083m; diluted 382.216m; FY2026 OI 234; FY2026 FCF 1,392; cash & STI 3,189; total debt 7,331 (incl. leases 1,014); preferred 0; NCI 49"
EKTA-B.ST,core_fx,1,-
EKTA-B.ST,core_fx_date,n.m.,-
EKTA-B.ST,core_oi,234,"shares outstanding ex-treasury 382.083m; diluted 382.216m; FY2026 OI 234; FY2026 FCF 1,392; cash & STI 3,189; total debt 7,331 (incl. leases 1,014); preferred 0; NCI 49"
EKTA-B.ST,core_oi_basis,FY2026 reported,-
EKTA-B.ST,core_period,FY2026 (Apr–Mar),-
EKTA-B.ST,core_ratio,1,-
EKTA-B.ST,core_shares_diluted,382.216,"shares outstanding ex-treasury 382.083m; diluted 382.216m; FY2026 OI 234; FY2026 FCF 1,392; cash & STI 3,189; total debt 7,331 (incl. leases 1,014); preferred 0; NCI 49"
EKTA-B.ST,core_unit,m,-
EKTA-B.ST,past_reason,7.6% ROCE,Worst-of-four normalised averages FY2021–FY2026: ROCE 7.6%
EKTA-B.ST,sf_reason,distributions,One flag: the SEK 917M dividend held flat through FY2022–FY2024 when it exceeded
EL.PA,past_reason,4.5% ROCE,Worst-of-four normalized averages: ROCE 4.5%
EL.PA,sf_reason,buybacks,"P19 fails the gate several ways: repurchases in six of seven window years, none rescued (rep"
ELUX-B.ST,future_reason,2+ forces,"Forces: customer power STRONG (concentrated NA big-box channel, zero"
ELUX-B.ST,past_reason,5% ROCE,worst-of-four normalized ROCE of 5.0%
ELUX-B.ST,sf_reason,buybacks,"P19 HARD STRIKE: the Oct–Dec 2021 tranche (4,320,057 B shares, SEK 894m, avg 206"
ENB.TO,core_cash,1094,"(debt 106,106 + pref 6,818 + NCI 2,855 − cash 1,094)"
ENB.TO,core_currency,CAD,-
ENB.TO,core_debt_eq,115779,"(debt 106,106 + pref 6,818 + NCI 2,855 − cash 1,094)"
ENB.TO,core_fcf,3297,"MCap/FCF = 171,820 / 3,297 = 52.1×"
ENB.TO,core_fx,1,-
ENB.TO,core_fx_date,n.m.,-
ENB.TO,core_oi,10958,"EV(consv) 286,505 / OI 10,958 = 26.1× (no-cash variant 26.2×)"
ENB.TO,core_oi_basis,FY2025 reported,-
ENB.TO,core_period,FY2025,-
ENB.TO,core_ratio,1,-
ENB.TO,core_shares_diluted,2186,"price 78.60 × 2,186m = MCap 171,820"
ENB.TO,core_unit,m,-
ENB.TO,past_reason,4.2% ROCE,Worst-of-four normalized-average ROCE = 4.2%
ENB.TO,printed_ev_oi,26.2,"EV(consv) 286,505 / OI 10,958 = 26.1× (no-cash variant 26.2×)"
ENB.TO,printed_ev_oi_all_cash,26.1,"EV(consv) 286,505 / OI 10,958 = 26.1× (no-cash variant 26.2×)"
ENOV,past_reason,losses,Worst-of-four ROCE −16.2%
ENOV,sf_reason,compensation,Breach on both: P17 hard strike
ENR.DE,future_reason,2+ forces,Forces tally three strong
ENR.DE,past_reason,0.1% ROCE,worst-of-four normalized average ROCE is 0.1%
ENR.DE,sf_reason,buybacks,FAIL — two independent P19 hard strikes
EPI-A.ST,core_cash,10940,"Operative FY2025 figures: OI SEK 11,925m, FCF SEK 8,680m, cash+STI SEK 10,940m, debt SEK 21,023m, NCI SEK 11m"
EPI-A.ST,core_currency,SEK,-
EPI-A.ST,core_debt_eq,21034,"Operative FY2025 figures: OI SEK 11,925m, FCF SEK 8,680m, cash+STI SEK 10,940m, debt SEK 21,023m, NCI SEK 11m"
EPI-A.ST,core_fcf,8680,"Operative FY2025 figures: OI SEK 11,925m, FCF SEK 8,680m, cash+STI SEK 10,940m, debt SEK 21,023m, NCI SEK 11m"
EPI-A.ST,core_fcf_basis,FY2025 CFO − capex,-
EPI-A.ST,core_fx,1,-
EPI-A.ST,core_fx_date,n.m.,-
EPI-A.ST,core_oi,11925,"Operative FY2025 figures: OI SEK 11,925m, FCF SEK 8,680m, cash+STI SEK 10,940m, debt SEK 21,023m, NCI SEK 11m"
EPI-A.ST,core_oi_basis,FY2025 reported,-
EPI-A.ST,core_period,FY2025,-
EPI-A.ST,core_ratio,1.1702,"A/B ratio 1.1702, so MCap = P_B × 1,348.43m"
EPI-A.ST,core_shares_diluted,1348.43,"A/B ratio 1.1702, so MCap = P_B × 1,348.43m"
EPI-A.ST,core_unit,m,-
EPI-A.ST,sf_reason,buybacks,"ferenced — every mandate since listing authorises repurchase ""in order to fulfill the obligations under Epiro"
EQNR,aliases,EQNR.OL,Equinor ASA (NYSE ADR 1:1; Oslo: EQNR.OL)
EQNR,core_cash,23726,"NCI 74; EV all-cash 101,786 = − cash & STI 23,726 (Jun-2026 interim BS; App"
EQNR,core_currency,USD,-
EQNR,core_debt_eq,32493,"EV no-cash 125,512 = MCap + debt 32,419 + NCI 74"
EQNR,core_fx,1,-
EQNR,core_fx_date,n.m.,-
EQNR,core_oi,25352,"(6,871); EV/OI 4.95× nc / 4.01× ac (OI 25,352); MCap/BV 2.30×; MCap/TBV"
EQNR,core_ratio,1,-
EQNR,core_shares_diluted,2390,"## F. Valuation math MCap 93,019 = 2,390m × $38.92 (7 Aug close). EV"
EQNR,core_unit,m,-
EQNR,past_reason,ROCE decline,What fails is P4's trend limb: three consecutive post-2022 ROCE de
ERIC-B.ST,future_reason,customer conc.,Breadth FAILs on customers: largest ~14% o
ERIC-B.ST,past_reason,4.7% ROCE,Worst-of-four normalized 10y ROCE is 4.74%
ERIC-B.ST,sf_reason,flag pair,Dual-class control paired with value-destructive allocation
ESSITY-B.ST,core_cash,6873,"all-cash-excess = − 6,873 = SEK 224,259m"
ESSITY-B.ST,core_currency,SEK,-
ESSITY-B.ST,core_debt_eq,43027,"EV no-cash = 188,105 + 42,609 + 418 = SEK 231,132m"
ESSITY-B.ST,core_fcf,8356,"188,105 ÷ 8,356"
ESSITY-B.ST,core_fcf_basis,FY2025 CFO − all capex (strict),-
ESSITY-B.ST,core_fx,1,-
ESSITY-B.ST,core_fx_date,n.m.,-
ESSITY-B.ST,core_oi,18531,"231,132 ÷ 18,531"
ESSITY-B.ST,core_oi_basis,FY2025 reported,-
ESSITY-B.ST,core_period,FY2025,-
ESSITY-B.ST,core_ratio,1,-
ESSITY-B.ST,core_shares_diluted,678.587806,"678,587,806 shares"
ESSITY-B.ST,core_unit,m,-
ESSITY-B.ST,sf_reason,buybacks,*Repurchases — the flag:* three consecutive SEK 3bn programm
EVK.DE,future_reason,no moat,No moat with a single durable identif
EVK.DE,past_reason,4.6% ROCE,Worst-of-four normalized average ROCE 4.6%
EVO.ST,future_reason,customer conc.,"Breadth FAIL: largest customer 12% of net revenues, top five 39%"
EVO.ST,sf_reason,acquisitions,The NetEnt purchase
FAST,core_cash,204.7,"− 321.5) / 1,150.28 = $9.69; all-cash (+204.7) = $9.87. The bounds"
FAST,core_currency,USD,-
FAST,core_debt_eq,441.5,"7 × 1,655.7 − 120.0 − 321.5) / 1,150.28 = $9.69; all-cash (+204.7) = $9.87. The bounds converge (1.9% apart);"
FAST,core_fcf,1050.6,"all-cash 58,472.1. - MCap/FCF: 58,235.3 / 1,050.6 = 55.4× (TTM 1,155.9 →"
FAST,core_fx,1,-
FAST,core_fx_date,n.m.,-
FAST,core_oi,1655.7,"1,155.9 → 50.4×). - EV/OI: 58,472.1 / 1,655.7 = 35.3× all-cash; 58,676.8"
FAST,core_ratio,1,-
FAST,core_shares_diluted,1150.28,"3,932.1 = 14.8×. - FCF leg: 8 × 1,050.6 / 1,150.28 = $7.31 — binds. - EV/OI"
FAST,core_unit,m,-
FAST,sf_reason,buybacks,"of free cash flow and debt has fallen, but every repurchase since 2016 ran far above the bargain lines, and"
FDS,core_cash,304.2,"− 1,570)/35.57 = $103.12; ac (5,238.1 + 304.2 − 1,570)/35.57 = $111.68;"
FDS,core_currency,USD,-
FDS,core_debt_eq,1570,"legs (7 × 748.3 = 5,238.1): nc (5,238.1 − 1,570)/35.57 = $103.12; ac"
FDS,core_fcf,617.5,"− 1,570)/35.57 = $111.68; FCF leg 8 × 617.5/35.57 = $138.88 → EV/OI"
FDS,core_fx,1,-
FDS,core_fx_date,n.m.,-
FDS,core_oi,748.3,"audit in E). Band: EV/OI legs (7 × 748.3 = 5,238.1): nc (5,238.1 −"
FDS,core_ratio,1,-
FDS,core_shares_diluted,35.57,F. Valuation math Price $285.57 · shares 35.57m · MCap $10.16bn. EV: ac
FDS,core_unit,m,-
FIE.DE,core_cash,226867,"cash & STI €226,867k"
FIE.DE,core_currency,EUR,-
FIE.DE,core_debt_eq,900451,"(7 × 329,346 + 226,867 − 884,035 − 16,416) ÷ 83,958.471"
FIE.DE,core_fcf,348944,"FCF €348,944k"
FIE.DE,core_fcf_basis,FY2025 CFO − capex,-
FIE.DE,core_fx,1,-
FIE.DE,core_fx_date,n.m.,-
FIE.DE,core_oi,329346,"OI €329,346k"
FIE.DE,core_oi_basis,FY2025 reported,-
FIE.DE,core_period,FY2025,-
FIE.DE,core_ratio,1,-
FIE.DE,core_shares_diluted,83.958471,"shares outstanding 83,958,471 (84,000,000 less 41,529 treasury)"
FIE.DE,core_unit,k,-
FIG,past_reason,losses,"−$877.4m (FY2024, tender RSU charge)"
FIG,sf_reason,compensation,"Hard strike, both reads"
FLUT,future_reason,supplier conc.,supplier breadth fails on look-through — the licens
FLUT,past_reason,1.1% ROCE,Worst-of-four normalized ROCE 1.1%
FLUT,sf_reason,buybacks,"apital allocation is ADVERSE: FY2025's $1,123m of repurchases priced at 78–107× on all four reads, funded alo"
FORTUM.HE,core_cash,3792,"− 3,863 − 81)/897.3m = €2.93; all-cash (+3,792) = €7.16. Bounds: €2.93"
FORTUM.HE,core_currency,EUR,-
FORTUM.HE,core_debt_eq,3944,"7 × 939 − 3,863 − 81)/897.3m = €2.93; all-cash (+3,792) = €7.16. Bounds: €2.93 (EV/OI binds) / €3.04 (FCF leg"
FORTUM.HE,core_fcf,341,- Threshold-implied prices: FCF leg 8 × 341/897.3m = €3.04. EV/OI legs:
FORTUM.HE,core_fx,1,-
FORTUM.HE,core_fx_date,n.m.,-
FORTUM.HE,core_oi,939,"= €3.04. EV/OI legs: no-cash (7 × 939 − 3,863 − 81)/897.3m ="
FORTUM.HE,core_ratio,1,-
FORTUM.HE,core_shares_diluted,897.3,Threshold-implied prices: FCF leg 8 × 341/897.3m = €3.04. EV/OI legs:
FORTUM.HE,core_unit,m,-
FORTUM.HE,past_reason,7% ROCE,worst-of-four normalized ROCE 7.0%
FQT.VI,future_reason,customer conc.,Customer breadth FAILS
FQT.VI,sf_reason,compensation,Both reads breach: a hard strike
FR.PA,future_reason,customer conc.,Breadth FAILS on the customer side
FR.PA,past_reason,4.1% ROCE,Worst-of-four normalized ROCE is 4.13%
FR.PA,sf_reason,buybacks,Capital allocation is CAUTION: repurchases execute at 9
FRE.DE,future_reason,breadth,Breadth FAIL
FRE.DE,past_reason,5.1% ROCE,Worst-of-four normalized ROCE 5.1%
FRSH,future_reason,forces: substitutes,substitutes STRONG
FRSH,past_reason,losses,Σ operating income across the window is −$733.7m
FRSH,sf_reason,compensation,P17 hard strike
FSLY,future_reason,forces: entrants,new entrants STRONG
FSLY,past_reason,losses,No positive year
FSLY,sf_reason,compensation,P17 hard strike: CEO Nightingale FY2024 total $7
FTK.DE,core_currency,EUR,-
FTK.DE,core_fcf,168.6,"Primaries. - MCap / FCF = 3,825.4 ÷ 168.6 = 22.7× vs P7 ≤ 8. (On the"
FTK.DE,core_fx,1,-
FTK.DE,core_fx_date,n.m.,-
FTK.DE,core_oi,221.6,"and the no-cash-excess build (€3,949m ÷ €221.6m = 17.8×) treats €4.4bn of"
FTK.DE,core_ratio,1,-
FTK.DE,core_shares_diluted,107.515,"Finance). Diluted weighted-average shares 107.515m (FY2025) → MCap ≈ €3,825m."
FTK.DE,core_unit,m,-
FTK.DE,future_reason,forces: substitutes,substitutes STRONG
FTRE,future_reason,customer conc.,"Breadth: customers — FAIL: ""one customer accounted for"
FTRE,past_reason,losses,negative on every variant
FTRE,sf_reason,compensation,NI legs negative): breach on both reads → hard strike
G1A.DE,core_cash,333.2,"÷ 162.80 = €25.46; all-cash = (4,407.2 + 333.2 − 262.6) ÷ 162.80 = €27.50"
G1A.DE,core_currency,EUR,-
G1A.DE,core_debt_eq,262.6,"= €25.46; all-cash = (4,407.2 + 333.2 − 262.6) ÷ 162.80 = €27.50 (8%"
G1A.DE,core_fcf,449.7,"F. Valuation math - MCap/FCF = 10,818.2 ÷ 449.7 = 24.1×. EV/OI = 11,080.8 ÷"
G1A.DE,core_fx,1,-
G1A.DE,core_fx_date,n.m.,-
G1A.DE,core_oi,629.6,"÷ 449.7 = 24.1×. EV/OI = 11,080.8 ÷ 629.6 = 17.6× (no-cash); 10,747.7"
G1A.DE,core_ratio,1,-
G1A.DE,core_shares_diluted,162.8,EXPENSIVE. - Band: FCF leg = 8 × 449.7 ÷ 162.80 = €22.10. EV/OI leg no-cash
G1A.DE,core_unit,m,-
G1A.DE,past_reason,8.8% ROCE,Worst-of-four normalized ROCE is 8.8%
G1A.DE,sf_reason,buybacks,"Three buyback programmes (2017–18, 2021–22, 2023–25"
GAP,future_reason,2+ forces,"bstitutes STRONG, new entrants STRONG — two strong forces, no durable moat, mature market"
GAP,past_reason,8.6% ROCE,Worst-of-four normalized ROCE 8.6%
GAP,sf_reason,buybacks,8× EV/OI — nowhere near overpriced — but $601m of buybacks plus $125m of dividends went out against operati
GBF.DE,future_reason,2+ forces,"Forces: customer power STRONG (large process operators, competitive r"
GBF.DE,past_reason,2.1% ROCE,Worst-of-four normalised ROCE 2.07%
GBF.DE,sf_reason,buybacks,FAIL — P19 hard strike
GEBN.SW,core_cash,585.8,"17,637m; EV_all-cash = 17,637 + 1,355 − 585.8 = CHF 18,406m; EV_no-cash ="
GEBN.SW,core_currency,CHF,-
GEBN.SW,core_debt_eq,1355,"MCap CHF 17,637m; EV_all-cash = 17,637 + 1,355 − 585.8 = CHF 18,406m;"
GEBN.SW,core_fcf,702,line of CHF 29.9m on the lower of FCF CHF 702m and NI CHF 597.8m — ~15%
GEBN.SW,core_fx,1,-
GEBN.SW,core_fx_date,n.m.,-
GEBN.SW,core_oi,767.2,"year). Operative FY2025 figures: OI CHF 767.2m, FCF CHF 702.0m, diluted"
GEBN.SW,core_ratio,1,-
GEBN.SW,core_shares_diluted,33.14,math At CHF 532.20 (31 Jul 2026; 33.14m diluted): MCap CHF
GEBN.SW,core_unit,m,-
GEBN.SW,sf_reason,buybacks,The repurchase lever fails on all three limbs
GEN,future_reason,2+ forces,new entrants STRONG
GEN,past_reason,leverage,But leverage is the decider
GEN,sf_reason,flag pair,sition flag sitting on the hard-strike boundary — paired with MoneyLion (2025) ≈$1bn (+CVR) for a barely-GAAP-p
GETI-B.ST,core_cash,3401,"7, all-cash-excess EV → P = (7 × 3,789 + 3,401 − 13,242 − 64) ÷ 272.370 ="
GETI-B.ST,core_currency,SEK,-
GETI-B.ST,core_debt_eq,13306,"7 × 3,789 − 13,242 − 64) ÷ 272.370 = 13,217 ÷ 272.370 = SEK 48.53 ← binds - EV/OI ≤ 7, all-cash-excess EV → P"
GETI-B.ST,core_fcf,2635,"MCap SEK 62,727m. FY2025: OI 3,789; FCF 2,635 (CFO 3,949 − capex 1,314);"
GETI-B.ST,core_fx,1,-
GETI-B.ST,core_fx_date,n.m.,-
GETI-B.ST,core_oi,3789,"272.370m; MCap SEK 62,727m. FY2025: OI 3,789; FCF 2,635 (CFO 3,949 −"
GETI-B.ST,core_ratio,1,-
GETI-B.ST,core_shares_diluted,272.37,"(close 24 Jul 2026); diluted shares 272.370m; MCap SEK 62,727m. FY2025:"
GETI-B.ST,core_unit,m,-
GETI-B.ST,past_reason,6.8% ROCE,Worst-of-four 10y normalized ROCE 6.8%
GGG,core_cash,60.6,"165.724 = $27.78. - All-cash: (4,657.1 + 60.6 − 29.2 − 23.0) ÷ 165.724 ="
GGG,core_currency,USD,-
GGG,core_debt_eq,52.2,"7 × 665.3 = 4,657.1. - No-cash: (4,657.1 − 29.2 − 23.0) ÷ 165.724 = $27.78. - All-cash: (4,657.1 + 60.6 −"
GGG,core_fcf,637.9,"MCap $12,926.5m. - MCap/FCF: 12,926.5 ÷ 637.9 (FY2025) = 20.3×; ÷ 629.5"
GGG,core_fx,1,-
GGG,core_fx_date,n.m.,-
GGG,core_oi,665.3,"629.5 (TTM) = 20.5×. - EV/OI pro-forma (OI 665.3): no-cash 12,978.7 ÷ 665.3"
GGG,core_ratio,1,-
GGG,core_shares_diluted,165.724,math Price $78.00 (2 Oct 2026). Shares 165.724m (Q2 2026 diluted w-avg;
GGG,core_unit,m,-
GGG,future_reason,customer conc.,Breadth fails on the customer side
GGG,sf_reason,acquisitions,"n-out was missed, and Valco was bought at about 14× EBITDA"
GOOGL,future_reason,moat eroding,"creators, dominant in video and cloud, eroding at the query layer"
GOOGL,sf_reason,flag pair,Two flags
GPN,future_reason,forces: suppliers,supplier power STRONG
GPN,past_reason,3.4% ROCE,Worst-of-four normalized ROCE is 3.4%
GPN,sf_reason,buybacks,"5bn repurchase authorization, a $550m ASR, and a $7"
GRMN,core_cash,4134.8,"Operative FY2025 figures: OI $1,876.1m, FCF $1,362.9m, diluted 193.616m, cash and securities $4,134.8m"
GRMN,core_currency,USD,-
GRMN,core_debt_eq,196.0,"EV_lower = 56,881 + 196.0 − 4,134.8 = $52,942m"
GRMN,core_fcf,1362.9,"Operative FY2025 figures: OI $1,876.1m, FCF $1,362.9m, diluted 193.616m, cash and securities $4,134.8m"
GRMN,core_fx,1,-
GRMN,core_fx_date,n.m.,-
GRMN,core_oi,1876.1,"Operative FY2025 figures: OI $1,876.1m, FCF $1,362.9m, diluted 193.616m, cash and securities $4,134.8m"
GRMN,core_oi_basis,FY2025 reported,-
GRMN,core_period,FY2025; BS H1 2026,-
GRMN,core_ratio,1,-
GRMN,core_shares_diluted,193.616,"Operative FY2025 figures: OI $1,876.1m, FCF $1,362.9m, diluted 193.616m, cash and securities $4,134.8m"
GRMN,core_unit,m,-
GRMN,sf_reason,buybacks,The repurchase lever fails on all three limbs
GRND,future_reason,breadth,WEAK — breadth FAIL and the tally each suffice
GRND,past_reason,leverage,"P4 fires on the breach, not the servicing"
GRND,sf_reason,compensation,P17 hard strike
GSK.L,core_cash,4097,"EV/OI: 93,099 / 7,932 = 11.74× (low); 97,196 / 7,932 = 12.25× (high)"
GSK.L,core_currency,GBP,-
GSK.L,core_debt_eq,18129,"EV/OI leg (conservative no-cash) P = (7 × 7,932 − 18,550 + 421) / 4,117 = £9.08"
GSK.L,core_fcf,5714,"MCap/FCF = 79,067 / 5,714 = 13.84×"
GSK.L,core_fx,1,-
GSK.L,core_fx_date,n.m.,-
GSK.L,core_oi,7932,"EV/OI: 93,099 / 7,932 = 11.74× (low); 97,196 / 7,932 = 12.25× (high)"
GSK.L,core_oi_basis,FY2025 reported,-
GSK.L,core_period,FY2025,-
GSK.L,core_ratio,1,-
GSK.L,core_shares_diluted,4117,"Price £19.205 × 4,117m = MCap £79,067m"
GSK.L,core_unit,m,-
GTLB,future_reason,forces: substitutes,substitutes STRONG
GTLB,past_reason,losses,worst-of-four normalized ROCE −21.0%
GTLB,sf_reason,compensation,"P17 hard strike: top FY2026 employee (CRO Steward, $13"
HEI,core_cash,240959,"EV/OI leg, all-cash: (7,132,986 + 240,959 − 3,446,127) ÷ 140,771"
HEI,core_currency,USD,-
HEI,core_debt_eq,3446127,"EV/OI leg, all-cash: (7,132,986 + 240,959 − 3,446,127) ÷ 140,771"
HEI,core_fcf,861380,"Inputs: FY2025 OI 1,018,998; FY2025 FCF 861,380 (all capex)"
HEI,core_fcf_basis,FY2025 CFO − all capex,-
HEI,core_fx,1,-
HEI,core_fx_date,n.m.,-
HEI,core_oi,1018998,"Inputs: FY2025 OI 1,018,998; FY2025 FCF 861,380 (all capex)"
HEI,core_oi_basis,FY2025 reported,-
HEI,core_period,FY2025; HEI-equivalent shares at the 2 Oct 2026 HEI/HEI.A prices,-
HEI,core_ratio,1,-
HEI,core_shares_diluted,118.0703,"EV no-cash (no excess cash) = 35,710,359 + 2,541,173 + 140,721"
HEI,core_unit,k,-
HEIA.AS,core_cash,2831,"= €1.12. - EV/OI leg, all-cash: (23,842 + 2,831 − 23,228) / 548.674 ="
HEIA.AS,core_currency,EUR,-
HEIA.AS,core_debt_eq,23228,"- EV/OI leg, all-cash: (23,842 + 2,831 − 23,228) / 548.674 = €6.28. - The"
HEIA.AS,core_fcf,2610,"548.674m = €38,221m. - MCap/FCF = 38,221 / 2,610 = 14.6×. - EV/OI = 61,449 /"
HEIA.AS,core_fx,1,-
HEIA.AS,core_fx_date,n.m.,-
HEIA.AS,core_oi,3406,"38,221 / 2,610 = 14.6×. - EV/OI = 61,449 / 3,406 = 18.0× no-cash; 58,618 /"
HEIA.AS,core_ratio,1,-
HEIA.AS,core_shares_diluted,548.674,"## F. Valuation math - MCap = €69.66 × 548.674m = €38,221m. - MCap/FCF ="
HEIA.AS,core_unit,m,-
HEIA.AS,past_reason,8.4% ROCE,worst-of-four ROCE is 8.4%
HEN3.DE,sf_reason,buybacks,"FAIL (P19 hard strike), independently disqualifying"
HEXA-B.ST,past_reason,9.3% ROCE,worst-of-four ROCE 9.25%
HFG.DE,core_cash,246.9,the all-cash bound at OI > (754.9 − 246.9) / 7 = €72.6m (pro-forma
HFG.DE,core_currency,EUR,-
HFG.DE,core_debt_eq,754.9,no-cash bound turns positive only at OI > 754.9 / 7 = €107.8m; the all-cash
HFG.DE,core_fcf,142.8,(build in C). - MCap/FCF = 346.5 / 142.8 = 2.43× (PASS ≤ 8).
HFG.DE,core_fx,1,-
HFG.DE,core_fx_date,n.m.,-
HFG.DE,core_oi,104,"| 9,989 | 10,191 | 46.9 | n.m. (FCF −104) | 29.5 | 48.4 | | FY2023 |"
HFG.DE,core_ratio,1,-
HFG.DE,core_shares_diluted,148.3,"144,957,412 (sourced); diluted 148.3m (sourced). MCap = 2.39 ×"
HFG.DE,core_unit,m,-
HFG.DE,future_reason,moat eroding,Moat eroding
HFG.DE,past_reason,6.1% ROCE,worst-of-four normalized ROCE 6.1%
HFG.DE,sf_reason,flag pair,FAIL — flag pair: compensation practice + capital-allocation CAUTION
HHH,future_reason,customer conc.,"dent on homebuilders"" and carries no no-customer->10% sentence — burden unmet, and"
HHH,past_reason,3.2% ROCE,Worst-of-four 10y normalized ROCE 3.2%
HHH,sf_reason,compensation,P17 hard strike: CEO O'Reilly FY2025 total $7
HLAG.DE,core_cash,3475.1,"P = (7 × 933.1 + 3,475.1 − 6,387.4 − 57.0) ÷ 175.76 = €20.27"
HLAG.DE,core_currency,EUR,-
HLAG.DE,core_debt_eq,6444.4,"P = (7 × 933.1 + 3,475.1 − 6,387.4 − 57.0) ÷ 175.76 = €20.27"
HLAG.DE,core_fcf,702.6,"MCap/FCF 21,653.6/702.6 = 30.8×"
HLAG.DE,core_fx,1,-
HLAG.DE,core_fx_date,n.m.,-
HLAG.DE,core_oi,933.1,"P = (7 × 933.1 + 3,475.1 − 6,387.4 − 57.0) ÷ 175.76 = €20.27"
HLAG.DE,core_oi_basis,FY2025 reported,-
HLAG.DE,core_period,FY2025,-
HLAG.DE,core_ratio,1,-
HLAG.DE,core_shares_diluted,175.76,"P = (7 × 933.1 + 3,475.1 − 6,387.4 − 57.0) ÷ 175.76 = €20.27"
HLAG.DE,core_unit,m,-
HLAG.DE,future_reason,2+ forces,"Forces: customer power STRONG (undifferentiated service, transparent"
HLE.DE,future_reason,customer conc.,Breadth FAILS: the segment note shows one
HLE.DE,past_reason,7.1% ROCE,Worst-of-four normalised ROCE 7.1%
HLN.L,past_reason,7.2% ROCE,worst-of-four normalized ROCE 7.22%
HMS.ST,core_cash,47,"SEK 60.1. - EV/OI all-cash: (7 × 762.0 + 47 − 2,311) ÷ 50.273 = SEK"
HMS.ST,core_currency,SEK,-
HMS.ST,core_debt_eq,2311,"50.273m, FY2025 weighted; debt stack 2,311 = 1,943 + 246 + 122): - FCF"
HMS.ST,core_fcf,744.2,"multiples: - MCap/FCF = 28,108.6 ÷ 744.2 = 37.8×. - EV/OI = 30,419.6"
HMS.ST,core_fx,1,-
HMS.ST,core_fx_date,n.m.,-
HMS.ST,core_oi,762,"÷ 744.2 = 37.8×. - EV/OI = 30,419.6 ÷ 762.0 = 39.9× (no-cash); 30,372.6"
HMS.ST,core_ratio,1,-
HMS.ST,core_shares_diluted,50.273,"Threshold-implied prices (diluted shares 50.273m, FY2025 weighted; debt"
HMS.ST,core_unit,m,-
HMS.ST,sf_reason,buybacks,Share-plan repurchases ran at ≈ 25–60× year-end EV/OI
HOG,past_reason,5.8% ROCE,worst-of-four normalized ROCE 5.83%
HOT.DE,past_reason,7.2% ROCE,Worst-of-four normalized ROCE 7.2%
HOT.DE,sf_reason,flag pair,FAIL on a flag pair: (1) parent-directed related-party dealing — Flat
HUBN.SW,core_currency,CHF,-
HUBN.SW,core_debt_eq,1460,"EV/OI conservative leg = (7 × 90,842 − 1,460) ÷ 18,457.510 = CHF 34.37."
HUBN.SW,core_fcf,71890,"| MCap / FCF | 3,495,852 ÷ 71,890 | 48.6× | ≤ 8 | FAIL | | EV"
HUBN.SW,core_fx,1,-
HUBN.SW,core_fx_date,n.m.,-
HUBN.SW,core_oi,90842,"| | EV / OI (conservative) | 3,497,312 ÷ 90,842 | 38.5× | ≤ 7 | FAIL | | EV"
HUBN.SW,core_ratio,1,-
HUBN.SW,core_shares_diluted,18.45751,"Trigger band. MCap/FCF leg = 8 × 71,890 ÷ 18,457.510 = CHF 31.16 (binds); EV/OI"
HUBN.SW,core_unit,k,-
HUBN.SW,sf_reason,buybacks,"*Repurchases — the flag, and it is historical"
HUBS,future_reason,2+ forces,substitutes STRONG
HUBS,past_reason,losses,"10% floor — nine straight years of GAAP operating losses, P18 adjustments included"
HUBS,sf_reason,compensation,Hard strike (P17)
HUSQ-B.ST,future_reason,moat eroding,"in German-speaking Gardena markets, but eroding — a decade of flat operating"
HUSQ-B.ST,past_reason,9.1% ROCE,Worst-of-four normalized 10y ROCE 9.1%
HYLN,future_reason,no moat,Moat: none identified
HYLN,past_reason,losses,Operating losses were $64
HYLN,sf_reason,compensation,Comp: hard strike
IBE.MC,core_cash,6610,"ac (+6,610) = €1.65"
IBE.MC,core_currency,EUR,-
IBE.MC,core_debt_eq,62470,"7 × 9,510 = 66,570 vs debt 62,470"
IBE.MC,core_fcf,n.m.,MCap/FCF | n.m. (FY2025 FCF ≈ −€1.6bn)
IBE.MC,core_fx,1,-
IBE.MC,core_fx_date,n.m.,-
IBE.MC,core_oi,9510,"7 × 9,510 = 66,570 vs debt 62,470"
IBE.MC,core_oi_basis,FY2025 reported (EBIT),-
IBE.MC,core_period,FY2025,-
IBE.MC,core_ratio,1,-
IBE.MC,core_shares_diluted,6490,Price €20.70 · shares 6.49bn · MCap €134.28bn
IBE.MC,core_unit,m,-
IBE.MC,past_reason,6% ROCE,ROCE ≈ 6–7% currently
IBE.MC,sf_reason,buybacks,Buybacks: the standing anti-dilution buyback-and-cancel programme (scrip offset) — executed at
IBKR,core_currency,USD,-
IBKR,core_debt_eq,19,"$4,771M; total equity $20,472M; own debt $19M. - EV/OI (binding"
IBKR,core_fx,1,-
IBKR,core_fx_date,n.m.,-
IBKR,core_oi,4771,"444M; total economic shares ≈1,695M; OI $4,771M; total equity $20,472M;"
IBKR,core_ratio,1,-
IBKR,core_shares_diluted,1695,"Diluted 444M; total economic shares ≈1,695M; OI $4,771M; total equity"
IBKR,core_unit,m,-
IBM,core_cash,13587,"target MCap = 85,841 − 64,607 − 93 + 13,587 = 34,728"
IBM,core_currency,USD,-
IBM,core_debt_eq,64700,"target MCap = 85,841 − 64,607 − 93 + 13,587 = 34,728"
IBM,core_fcf,12102,"MCap/FCF = 205,650 / 12,102 = 17.0×"
IBM,core_fx,1,-
IBM,core_fx_date,n.m.,-
IBM,core_oi,12263,"EV/OI = 256,763 / 12,263 = 20.9× (all-cash-excess), 270,350 / 12,263 = 22.0× (no-cash)"
IBM,core_oi_basis,FY2025 reported,-
IBM,core_period,FY2025,-
IBM,core_ratio,1,-
IBM,core_shares_diluted,939.9,"MCap/FCF ≤ 8 → P = 8 × 12,102 / 939.9 = $103.0"
IBM,core_unit,m,-
IBM,past_reason,8.4% ROCE,Worst-of-four normalised-average ROCE = 8.4%
IEX,core_cash,621.3,"÷ 74.2 = $39.29. - All-cash: (4,895.1 + 621.3 − 1,858.9 − 120.7) ÷ 74.2 ="
IEX,core_currency,USD,-
IEX,core_debt_eq,1979.6,"7 × 699.3 = 4,895.1. - No-cash: (4,895.1 − 1,858.9 − 120.7) ÷ 74.2 = $39.29. - All-cash: (4,895.1 + 621.3 −"
IEX,core_fcf,616.8,"MCap $17,287.9m. - MCap/FCF: 17,287.9 ÷ 616.8 (FY2025) = 28.0×; ÷ 641.5"
IEX,core_fx,1,-
IEX,core_fx_date,n.m.,-
IEX,core_oi,699.3,"÷ 641.5 (TTM) = 26.9×. - EV/OI (FY2025 OI 699.3): no-cash 19,267.5 ÷ 699.3"
IEX,core_ratio,1,-
IEX,core_shares_diluted,74.2,math Price $232.99 (2 Oct 2026). Shares 74.2m (Q2 2026 diluted w-avg;
IEX,core_unit,m,-
IEX,past_reason,ROCE decline,Beginning-of-period ROCE fell three consecutive years: 16
IEX,sf_reason,buybacks,"The H1 2026 buybacks ($150m) cost 23–26× across the four reads, partl"
IFCN.SW,core_cash,131.9,"FY2025: OI 112.3, FCF 67.8, NI 85.8, cash+STI 131.9, debt 50.6, pref/NCI 0"
IFCN.SW,core_currency,USD,-
IFCN.SW,core_debt_eq,50.6,"FY2025: OI 112.3, FCF 67.8, NI 85.8, cash+STI 131.9, debt 50.6, pref/NCI 0"
IFCN.SW,core_fcf,67.8,"FY2025: OI 112.3, FCF 67.8, NI 85.8, cash+STI 131.9, debt 50.6, pref/NCI 0"
IFCN.SW,core_fx,0.813008,"Price CHF 158.2 × 24.451m = MCap CHF 3,868m × 1.23 = USD 4,758m"
IFCN.SW,core_fx_date,-,-
IFCN.SW,core_oi,112.3,"FY2025: OI 112.3, FCF 67.8, NI 85.8, cash+STI 131.9, debt 50.6, pref/NCI 0"
IFCN.SW,core_oi_basis,FY2025 reported,-
IFCN.SW,core_period,FY2025,-
IFCN.SW,core_ratio,1,-
IFCN.SW,core_shares_diluted,24.451,"Price CHF 158.2 × 24.451m = MCap CHF 3,868m × 1.23 = USD 4,758m"
IFCN.SW,core_unit,m,-
INDT.ST,core_cash,1362,"Cash 1,362. EV (all cash excess, lower) = 98,139"
INDT.ST,core_currency,SEK,-
INDT.ST,core_debt_eq,11189,"(7 × 3,916 − 11,183 − 6) ÷ 364,323k"
INDT.ST,core_fcf,3679,"LTM to 30 Jun 2026: OI 3,916; CFO 4,131; net capex 452 → FCF 3,679"
INDT.ST,core_fcf_basis,LTM CFO − net capex,-
INDT.ST,core_fx,1,-
INDT.ST,core_fx_date,n.m.,-
INDT.ST,core_oi,3916,"LTM to 30 Jun 2026: OI 3,916; CFO 4,131; net capex 452 → FCF 3,679"
INDT.ST,core_oi_basis,LTM Q2-2026 reported,-
INDT.ST,core_period,LTM to 2026-06-30,-
INDT.ST,core_ratio,1,-
INDT.ST,core_shares_diluted,364.323,"Shares outstanding 364,323k"
INDT.ST,core_unit,m,-
INIO,future_reason,breadth,Breadth FAIL
INIO,past_reason,9.1% ROCE,Worst-of-four normalized ROCE 9.1%
INIO,sf_reason,control,control plus value-destructive allocation — is the strike
INPST.AS,future_reason,customer conc.,Breadth FAILS twice: Vinted UAB 20
INPST.AS,past_reason,leverage,The decider is leverage
INPST.AS,sf_reason,buybacks,The strike is buybacks
INRN.SW,core_cash,184387,"= CHF 580.2; all-cash (7 × 71,752 + 184,387 − 12,247) / 844.506 = CHF"
INRN.SW,core_currency,CHF,-
INRN.SW,core_debt_eq,12247,"373.7. - EV/OI leg: no-cash (7 × 71,752 − 12,247) / 844.506 = CHF 580.2;"
INRN.SW,core_fcf,39449,"= 1,138.4 / 414.5 = 2.75×. - FCF leg: 8 × 39,449 / 844.506 = CHF 373.7. -"
INRN.SW,core_fx,1,-
INRN.SW,core_fx_date,n.m.,-
INRN.SW,core_oi,71752,"= CHF 373.7. - EV/OI leg: no-cash (7 × 71,752 − 12,247) / 844.506 = CHF"
INRN.SW,core_ratio,1,-
INRN.SW,core_shares_diluted,0.844506,"/ 414.5 = 2.75×. - FCF leg: 8 × 39,449 / 844.506 = CHF 373.7. - EV/OI leg:"
INRN.SW,core_unit,k,-
INRN.SW,past_reason,ROCE decline,WEAK — P4 sustained-decline route
INTU,core_cash,7200,"(primary, audited year-end): cash & STI $7,200m, debt $7,669m, operating"
INTU,core_currency,USD,-
INTU,core_debt_eq,8336,"× 5,884 − 7,669 − 667) ÷ 277 = (41,188 − 8,336) ÷ 277 = 32,852 ÷ 277 ="
INTU,core_fcf,8617,"NCI nil. FY2026 OI $5,884m, FY2026 FCF $8,617m. Current multiples. |"
INTU,core_fx,1,-
INTU,core_fx_date,n.m.,-
INTU,core_oi,5884,"preferred nil, NCI nil. FY2026 OI $5,884m, FY2026 FCF $8,617m."
INTU,core_ratio,1,-
INTU,core_shares_diluted,277,"(close, 27 Aug 2026). Diluted shares 277m (FY2026 weighted-average)."
INTU,core_unit,m,-
INTU,sf_reason,buybacks,"Capital allocation CAUTION, hardened: $5,412m repurchased at ~$514, 24"
INVE-B.ST,core_currency,SEK,-
INVE-B.ST,core_fcf,n.m.,MCap/FCF and EV/OI are n.m. (mark-to-market holding company)
INVE-B.ST,core_fcf_basis,n.m. — holding company (P/adj-NAV anchor),-
INVE-B.ST,core_fx,1,-
INVE-B.ST,core_fx_date,n.m.,-
INVE-B.ST,core_oi,n.m.,MCap/FCF and EV/OI are n.m. (mark-to-market holding company)
INVE-B.ST,core_oi_basis,n.m. — holding company (P/adj-NAV anchor),-
INVE-B.ST,core_ratio,1,-
INVE-B.ST,core_shares_diluted,3063.53,"403.80 × 3,063.53m shares ex-treasury, 30 Jun 2026; both share classes at the B price"
INVE-B.ST,core_unit,m,-
INVE-B.ST,past_reason,13.9% ROE,worst normalized ROE is 13.9%
IP.MI,core_cash,369.6,"€15.25. - EV/OI leg all-cash = (2,355.9 + 369.6 − 739.7 − 10.5) ÷ 105.280 ="
IP.MI,core_currency,EUR,-
IP.MI,core_debt_eq,750.2,"7 × 336.6 − 739.7 − 10.5) ÷ 105.280 = €15.25. - EV/OI leg all-cash = (2,355.9 + 369.6 − 739.7 − 10.5) ÷"
IP.MI,core_fcf,232.5,"F. Valuation math - MCap/FCF = 3,731.1 ÷ 232.5 = 16.0×. EV/OI = 4,481.3 ÷"
IP.MI,core_fx,1,-
IP.MI,core_fx_date,n.m.,-
IP.MI,core_oi,336.6,"3,731.1 ÷ 232.5 = 16.0×. EV/OI = 4,481.3 ÷ 336.6 = 13.3× (no-cash); 4,111.7"
IP.MI,core_ratio,1,-
IP.MI,core_shares_diluted,105.28,EXPENSIVE. - Band: - FCF leg = 8 × 232.5 ÷ 105.280 = €17.67. - EV/OI leg
IP.MI,core_unit,m,-
IP.MI,sf_reason,buybacks,"Capital allocation is CAUTION: buybacks since FY2018 ran at 12–22× EV/OI, mostly recycle"
KALMAR.HE,core_cash,280.2,"÷ 63.9505 = €19.51; all-cash (1,542.8 + 280.2 − 295.4) ÷ 63.9505 ="
KALMAR.HE,core_currency,EUR,-
KALMAR.HE,core_debt_eq,295.4,€17.89. - EV/OI leg: no-cash (7 × 220.4 − 295.4) ÷ 63.9505 = €19.51;
KALMAR.HE,core_fcf,143,"≈€17.9, where FY2025 free cash flow of €143m binds. The verdict flips"
KALMAR.HE,core_fx,1,-
KALMAR.HE,core_fx_date,n.m.,-
KALMAR.HE,core_oi,220.4,"2,423.7 ÷ 143.0 = 16.9×. EV/OI = 2,719.1 ÷ 220.4 = 12.3× (no-cash) / 2,438.9"
KALMAR.HE,core_ratio,1,-
KALMAR.HE,core_shares_diluted,63.9505,÷ 458.9 = 5.3×. - FCF leg: 8 × 143.0 ÷ 63.9505 = €17.89. - EV/OI leg:
KALMAR.HE,core_unit,m,-
KBX.DE,core_cash,1738,"Cash and short-term investments €1,738m. Non-controlling interests"
KBX.DE,core_currency,EUR,-
KBX.DE,core_debt_eq,3160,"7 × 903 − 3,084 − 0 − 76) ÷ 161.2 = 3,161 ÷ 161.2 = €19.61 - EV/OI ≤ 7, all-cash-excess EV: (7 × 903 + 1,738"
KBX.DE,core_fcf,659,nil. Operating income €903m. FCF €659m (interest-reclassified) /
KBX.DE,core_fx,1,-
KBX.DE,core_fx_date,n.m.,-
KBX.DE,core_oi,903,€76m. Preferred nil. Operating income €903m. FCF €659m
KBX.DE,core_ratio,1,-
KBX.DE,core_shares_diluted,161.2,"(XETRA, 22 Jul 2026). Diluted shares 161.2m. Market capitalisation"
KBX.DE,core_unit,m,-
KBX.DE,past_reason,ROCE decline,WEAK — sustained decline on otherwise-ADEQUATE arithmetic
KCR.HE,core_cash,379.9,"÷ 237.763 = €14.27; all-cash = (3,796.8 + 379.9 − 403.4) ÷ 237.763 ="
KCR.HE,core_currency,EUR,-
KCR.HE,core_debt_eq,403.4,€17.50. EV/OI leg no-cash = (7 × 542.4 − 403.4) ÷ 237.763 = €14.27;
KCR.HE,core_fcf,520.1,"F. Valuation math - MCap/FCF = 7,342.1 ÷ 520.1 = 14.1×. EV/OI = 7,745.5 ÷"
KCR.HE,core_fx,1,-
KCR.HE,core_fx_date,n.m.,-
KCR.HE,core_oi,542.4,"7,342.1 ÷ 520.1 = 14.1×. EV/OI = 7,745.5 ÷ 542.4 = 14.3× (no-cash); 7,365.6"
KCR.HE,core_ratio,1,-
KCR.HE,core_shares_diluted,237.763,EXPENSIVE. - Band: FCF leg = 8 × 520.1 ÷ 237.763 = €17.50. EV/OI leg no-cash
KCR.HE,core_unit,m,-
KER.PA,future_reason,moat eroding,and at the profit-dominant House it is eroding — Gucci revenue fell 22% in 2
KER.PA,past_reason,ROCE decline,The decline is the story
KER.PA,sf_reason,acquisitions,"management pursued debt-funded, empire-building M&A into the downturn"
KEX,future_reason,2+ forces,Three strong forces
KEX,past_reason,4.6% ROCE,Worst-of-four normalized average ROCE is 4.6%
KEX,sf_reason,buybacks,Capital allocation is CAUTION: repurchases scaled from $2
KEYS,core_cash,2605,"229 (53 + 176); preferred 0; NCI 0; cash 2,605. - EV. No-cash $69,289m;"
KEYS,core_currency,USD,-
KEYS,core_debt_eq,2746,"7 × 876 − 2,517 − 229) ÷ 173.0 = $19.57. - EV/OI all-cash: (7 × 876 + 2,605 − 2,517 − 229) ÷ 173.0 = $34.63."
KEYS,core_fcf,1281,"Multiples (FY2025). - MCap/FCF: 66,543 ÷ 1,281 = 51.9×. - EV/OI: 69,289 ÷"
KEYS,core_fx,1,-
KEYS,core_fx_date,n.m.,-
KEYS,core_oi,876,"66,543 ÷ 1,281 = 51.9×. - EV/OI: 69,289 ÷ 876 = 79.1× (no-cash) and"
KEYS,core_ratio,1,-
KEYS,core_shares_diluted,173,that the diluted count fell from 191m to 173m. FAIL on the ADVERSE
KEYS,core_unit,m,-
KEYS,sf_reason,buybacks,FY2026 repurchases to July ($520m at $281
KLAR,future_reason,forces: substitutes,threat of substitutes STRONG
KLAR,past_reason,losses,ress-sourced pre-window record confirms losses 2019–2022 (FY2022 op loss ≈ $1
KLAR,sf_reason,compensation,P17 hard strike: CEO Siemiatkowski FY2025 total $45
KNEBV.HE,core_cash,440.5,"EV_all-cash = 26,007 + 869.7 + 29.4 − 440.5 = €26,466m; EV_no-cash ="
KNEBV.HE,core_currency,EUR,-
KNEBV.HE,core_debt_eq,899.1,"7 × 1,336.2 − 869.7 − 29.4) ÷ 519.1 = €16.29; all-cash (7 × 1,336.2 + 440.5 − 869.7 − 29.4) ÷ 519.1 = €17.14;"
KNEBV.HE,core_fcf,1162.1,"= €26,906m. MCap/FCF = 26,007 ÷ 1,162.1 = 22.4×. EV/OI = 19.8× /"
KNEBV.HE,core_fx,1,-
KNEBV.HE,core_fx_date,n.m.,-
KNEBV.HE,core_oi,1336.2,"from v1. Operative FY2025 figures: OI €1,336.2m, FCF €1,162.1m, NI"
KNEBV.HE,core_ratio,1,-
KNEBV.HE,core_shares_diluted,519.1,"Valuation math At €50.10 (31 Jul 2026; ≈519.1m A+B shares, A priced at B"
KNEBV.HE,core_unit,m,-
KNEBV.HE,sf_reason,flag pair,"the second, independent flag: the entrenchment structure"
KNIN.SW,core_currency,CHF,-
KNIN.SW,core_debt_eq,4615,"7 × 1,242 − 4,583 − 32)/118.946 = CHF 34.3 — binding; all-cash variant CHF 40.6. Band: CHEAP < ≈ CHF 34. P12"
KNIN.SW,core_fcf,1492,"28,558 (build in C). MCap/FCF = 24,693/1,492 = 16.6× (thr 8). EV/OI ="
KNIN.SW,core_fx,1,-
KNIN.SW,core_fx_date,n.m.,-
KNIN.SW,core_oi,1242,"12.54 = CHF 100.4; EV/OI conservative (7 × 1,242 − 4,583 − 32)/118.946 = CHF"
KNIN.SW,core_ratio,1,-
KNIN.SW,core_shares_diluted,118.946,"## F. Valuation math At CHF 207.60, 118.946m diluted sh: MCap 24,693."
KNIN.SW,core_unit,m,-
KRN.DE,core_cash,549488,"85,126|261,203|31,593.1|5,042,124|2,183,931|549,488|2,913,429|2,128,386|600,564|"
KRN.DE,core_currency,EUR,-
KRN.DE,core_debt_eq,188668,"bank debt 1,266 + other financial and lease liabilities 187,093 (52,982 current + 134,111 non-current, treated whole as debt-equivalent) + NCI 309"
KRN.DE,core_fcf,261203,"|MCap / FCF|3,494,194 ÷ 261,203|13.38×|≤ 8 (P7)| |EV / OI"
KRN.DE,core_fx,1,-
KRN.DE,core_fx_date,n.m.,-
KRN.DE,core_oi,417053,"|EV / OI (no cash excess)|3,682,862 ÷ 417,053|8.83×|≤ 7 (P8)| |EV / OI"
KRN.DE,core_ratio,1,-
KRN.DE,core_shares_diluted,31.593072,"math At €110.60 (23 Jul 2026) on 31,593.072k diluted shares → MCap"
KRN.DE,core_unit,k,-
KRN.DE,past_reason,9.3% ROCE,worst-of-four normalized ROCE 9.3%
KSPI,past_reason,leverage,Total liabilities are 340% of book at FY2025
KSPI,trigger,87.87,≈ $84.86–87.87
KVYO,past_reason,losses,worst-of-four normalized average ROCE is −17.8%
KVYO,sf_reason,flag pair,Flag pair → FAIL
KWY,aliases,Kingsway Financial Services Inc.,Kingsway Corporation (formerly Kingsway Financial Services Inc.)
KWY,future_reason,2+ forces,new entrants STRONG
KWY,past_reason,losses,Worst-of-four normalized ROCE −0.3%
KWY,sf_reason,compensation,e-than-token pay against no owner earnings is the hard strike
LECO,core_cash,242.4,"− cash 242.4 = EV all-cash 15,915.0"
LECO,core_currency,USD,-
LECO,core_debt_eq,1202.2,"7 × 718.1 − 1,150.1 − 52.1) ÷ 55.875 = (5,026.4 − 1,202.1) ÷ 55.875 = $68.44. - EV/OI leg, all-cash: (5,026.4"
LECO,core_fcf,534.2,"$274.38): - MCap/FCF = 14,955.3 ÷ 534.2 = 28.0×. - EV/OI = 16,157.4"
LECO,core_fx,1,-
LECO,core_fx_date,n.m.,-
LECO,core_oi,718.1,"÷ 534.2 = 28.0×. - EV/OI = 16,157.4 ÷ 718.1 = 22.5× no-cash, 15,915.0 ÷"
LECO,core_ratio,1,-
LECO,core_shares_diluted,55.875,→ EXPENSIVE. Threshold-implied prices (÷ 55.875m diluted): - FCF leg: 8 ×
LECO,core_unit,m,-
LECO,sf_reason,buybacks,Buybacks ran at 15–27× FCF and 15–21× EV/OI with no price
LIFCO-B.ST,core_cash,1878,"EV all-cash-excess = 152,669 − 1,878 = 150,791"
LIFCO-B.ST,core_currency,SEK,-
LIFCO-B.ST,core_debt_eq,11135,"EV conservative = 141,534 + 10,995 + 140 = 152,669"
LIFCO-B.ST,core_fcf,4582,"FCF = CFO 5,124 − capex 542 = 4,582"
LIFCO-B.ST,core_fcf_basis,FY2025 CFO − capex,-
LIFCO-B.ST,core_fx,1,-
LIFCO-B.ST,core_fx_date,n.m.,-
LIFCO-B.ST,core_oi,5170,"(7 × 5,170 + 1,878 − 10,995 − 140) ÷ 454.2163"
LIFCO-B.ST,core_oi_basis,FY2025 reported,-
LIFCO-B.ST,core_period,FY2025,-
LIFCO-B.ST,core_ratio,1,-
LIFCO-B.ST,core_shares_diluted,454.2163,Diluted shares 454.2163m
LIFCO-B.ST,core_unit,m,-
LIGHT.AS,future_reason,2+ forces,"Forces: customer power STRONG (price-buying channels, low switching c"
LIGHT.AS,past_reason,8.3% ROCE,Worst-of-four 10y normalized averages: ROCE 8.3%
LIN,past_reason,8.1% ROCE,Worst-of-four normalized-average ROCE ~8.1%
LIN,sf_reason,buybacks,The strike is P19: FY2025 repurchases of $4
LISN.SW,sf_reason,buybacks,The repurchase lever fails on all three limbs
LLY,core_cash,7.3,"EV/OI: 1,127.4/26.30 = 42.9× (all-excess); 1,134.7/26.30 = 43.1× (no-cash)"
LLY,core_currency,USD,-
LLY,core_debt_eq,43.86,P = (7×26.30 − 42.50 − 1.36 + cash-credit)/0.8993
LLY,core_fcf,8.97,"strict 1,090.8/8.97 = 121.6×"
LLY,core_fcf_basis,FY2025 CFO − all capex (strict),-
LLY,core_fx,1,-
LLY,core_fx_date,n.m.,-
LLY,core_oi,26.30,"EV/OI: 1,127.4/26.30 = 42.9× (all-excess); 1,134.7/26.30 = 43.1× (no-cash)"
LLY,core_oi_basis,FY2025 reported,-
LLY,core_period,FY2025,-
LLY,core_ratio,1,-
LLY,core_shares_diluted,899.3,P = (7×26.30 − 42.50 − 1.36 + cash-credit)/0.8993
LLY,core_unit,bn,-
LLY,sf_reason,buybacks,P19 HARD STRIKE: FY2025 repurchases of $4
LMND,future_reason,2+ forces,Tally 2 STRONG
LMND,past_reason,losses,Net income is negative in all eight reported years
LMND,sf_reason,compensation,"base $685,000) — the loss-leg rule makes this the hard strike, regardless of the normalized read (3y-average le"
LOGI,future_reason,customer conc.,"Breadth: customer test FAIL — Amazon 18%, Ingram Micro 14"
LOGI,sf_reason,buybacks,P19 fails: FY2022 tranche ($89
LR.PA,core_cash,1969.1,"cash & equivalents €1,969.1m"
LR.PA,core_currency,EUR,-
LR.PA,core_debt_eq,7762.5,"(7 × 1,808.5 − 7,724.4 − 38.1) ÷ 266.435233"
LR.PA,core_fcf,1328.1,"operating profit €1,808.5m; FCF €1,328.1m"
LR.PA,core_fcf_basis,FY2025 CFO − capex − capitalised development,-
LR.PA,core_fx,1,-
LR.PA,core_fx_date,n.m.,-
LR.PA,core_oi,1808.5,"operating profit €1,808.5m; FCF €1,328.1m"
LR.PA,core_oi_basis,FY2025 reported,-
LR.PA,core_period,FY2025; BS 2026-06-30,-
LR.PA,core_ratio,1,-
LR.PA,core_shares_diluted,266.435233,"Diluted shares 266,435,233 (FY2025, note 4.1.3)"
LR.PA,core_unit,m,-
LR.PA,sf_reason,buybacks,Capital allocation CAUTION (one flag): no year approaches the ≈25× calibration
LULU,core_cash,1389.7,"shares; MCap $10,794.2m; cash $1,389.7m; borrowings nil; leases"
LULU,core_currency,USD,-
LULU,core_debt_eq,-0,"| + Total borrowings / preferred / NCI | 0.0 | | = EV, no-cash —"
LULU,core_fcf,921.7,"nil; leases $2,141.1m; OI $2,210.6m; FCF $921.7m; BV $4,791.2m; TBV"
LULU,core_fx,1,-
LULU,core_fx_date,n.m.,-
LULU,core_oi,2210.6,"borrowings nil; leases $2,141.1m; OI $2,210.6m; FCF $921.7m; BV"
LULU,core_ratio,1,-
LULU,core_shares_diluted,110.71,"FCF leg, 8× reported — binds | 8 × 921.7 ÷ 110.710 | $66.60 | | FCF leg, 8×"
LULU,core_unit,m,-
LULU,future_reason,2+ forces,"Verdict WEAK, over-determined — two strong forces *and* an eroding moat, either sufficien"
LULU,sf_reason,buybacks,three consecutive tranches at or inside the EV/OI bargain line
LYFT,future_reason,moat eroding,"Moat: second-place network effect, eroding at the autonomous edge"
LYFT,past_reason,losses,Operating income is negative in all ten years
LYFT,sf_reason,buybacks,ocation: CAUTION — $50m (FY2024) + $500m (FY2025) repurchases executed at or below the FCF bargain line and F
MA,core_cash,10898,"− cash+STI 10,898 = 478,858 (all-cash-excess)"
MA,core_currency,USD,-
MA,core_debt_eq,19842,"7 × 18,897 − 19,833 − 9) / 880 = $127.8; all-cash-excess variant $140.1. Binding: EV/OI conservative → strict"
MA,core_fcf,16433,"|---|---|---|---|---| |MCap/FCF|469,914 / 16,433|28.6|≤ 8|3.6×| |EV/OI"
MA,core_fx,1,-
MA,core_fx_date,n.m.,-
MA,core_oi,18897,"8|3.6×| |EV/OI (all-cash)|478,858 / 18,897|25.3|≤ 7|3.6×| |EV/OI"
MA,core_ratio,1,-
MA,core_shares_diluted,880,blocks. Threshold-implied prices (880m diluted [assumption]):
MA,core_unit,m,-
MA,sf_reason,compensation,FAIL — strike: compensation
MAERSK-B.CO,core_cash,19007,"EV/OI leg, all-cash: (7 × 3,500 + 19,007 − 17,472 − 1,135) ÷ 14.474"
MAERSK-B.CO,core_currency,USD,-
MAERSK-B.CO,core_debt_eq,18607,"EV/OI leg, no-cash: (7 × 3,500 − 17,472 − 1,135) ÷ 14.474"
MAERSK-B.CO,core_fcf,4962,"MCap/FCF = 52,857 ÷ 4,962 = 10.7×"
MAERSK-B.CO,core_fx,6.638,"At DKK 24,240 ($3,651.74; USDDKK 6.638 derived; 14.474m shares): MCap $52,857m"
MAERSK-B.CO,core_fx_date,2026-10-02,"DKK 24,240 (close 2 Oct 2026; USDDKK 6.638 derived"
MAERSK-B.CO,core_oi,3500,"EV/OI = 52,457 ÷ 3,500 = 15.0× all-cash; 71,464 ÷ 3,500 = 20.4× no-cash"
MAERSK-B.CO,core_oi_basis,FY2025 reported,-
MAERSK-B.CO,core_period,FY2025,-
MAERSK-B.CO,core_ratio,1,-
MAERSK-B.CO,core_shares_diluted,14.474,"At DKK 24,240 ($3,651.74; USDDKK 6.638 derived; 14.474m shares): MCap $52,857m"
MAERSK-B.CO,core_unit,m,-
MAERSK-B.CO,future_reason,2+ forces,New entrants STRONG
MBLY,future_reason,customer conc.,Breadth: customer-side FAIL — revenue concentrates throug
MBLY,past_reason,losses,GAAP OI is negative in every year
MC.PA,core_cash,12202,"€151.4. - EV/OI leg, all-cash: (119,693 + 12,202 − 44,761) ÷ 494.958 ="
MC.PA,core_currency,EUR,-
MC.PA,core_debt_eq,44761,"EV/OI leg, all-cash: (119,693 + 12,202 − 44,761) ÷ 494.958 = 87,134 ÷"
MC.PA,core_fcf,14307,"F. Valuation math - MCap/FCF: 196,424 ÷ 14,307 = 13.7× (TTM FCF 14,372 →"
MC.PA,core_fx,1,-
MC.PA,core_fx_date,n.m.,-
MC.PA,core_oi,17099,"FCF 14,372 → 13.7×). - EV/OI: 241,185 ÷ 17,099 = 14.1× no-cash; 228,983 ÷"
MC.PA,core_ratio,1,-
MC.PA,core_shares_diluted,494.958,"÷ 26,203 = 7.5×. - FCF leg: 8 × 14,307 ÷ 494.958 = €231.2. - EV/OI leg,"
MC.PA,core_unit,m,-
MC.PA,sf_reason,buybacks,"9bn buyback tranches in 2023, 2025 and H1 2026 with no price criterio"
META,core_cash,90260,"| EV no-cash | $1,763,498m | — | — | | EV all-cash excess | $1,673,238m"
META,core_currency,USD,-
META,core_debt_eq,112318,"+ debt 112,318 (long-term debt 83,664 + operating leases 2,425 current and 26,229 non-current)"
META,core_fcf,46109,"2025 | 200,966 | 83,276 | 115,800 | 69,691 | 46,109 | 2,574"
META,core_fcf_basis,FY2025 CFO − all capex (strict),-
META,core_fx,1,-
META,core_fx_date,n.m.,-
META,core_oi,83276,"2025 | 200,966 | 83,276 | 115,800 | 69,691 | 46,109 | 2,574"
META,core_oi_basis,FY2025 reported,-
META,core_period,FY2025; BS Q2 2026,-
META,core_ratio,1,-
META,core_shares_diluted,2574,"2,548M shares outstanding, 2,574M diluted"
META,core_unit,m,-
META,sf_reason,buybacks,five programme years above the disciplined lines
METSO.HE,aliases,Metso Corporation; Metso Outotec Corporation,Metso Oyj (Metso Corporation; Metso Outotec Corporation until 2024)
METSO.HE,core_cash,383,"= €4.27. - EV/OI all-cash leg: (5,145 + 383 − 1,613) / 828.113 = 3,915"
METSO.HE,core_currency,EUR,-
METSO.HE,core_debt_eq,1613,"- EV/OI all-cash leg: (5,145 + 383 − 1,613) / 828.113 = 3,915 /"
METSO.HE,core_fcf,627,"= 20.7× (all-cash). MCap/FCF = 14,020 / 627 = 22.4×. MCap/BV = 14,020 /"
METSO.HE,core_fx,1,-
METSO.HE,core_fx_date,n.m.,-
METSO.HE,core_oi,735,"math - Multiples: EV/OI = 15,633 / 735 = 21.3× (no-cash) and"
METSO.HE,core_ratio,1,-
METSO.HE,core_shares_diluted,828.113,"= 14,020 / 513 = 27.3×. - Trigger band (828.113m shares): - FCF leg: 8 ×"
METSO.HE,core_unit,m,-
METSO.HE,sf_reason,distributions,Dividends exceeded FCF in FY2022–24 and were debt-funded
MGNI,future_reason,customer conc.,"Breadth: customers FAIL — ""two buyers… contributed to"
MGNI,past_reason,losses,worst-of-four normalized ROCE −3.61%
MGNI,sf_reason,flag pair,FAIL — flag pair
MICC.AS,future_reason,2+ forces,Four binary forces: customer power STRONG (consolidated grocers
MICC.AS,past_reason,leverage,The decisive fault is leverage
MIPS.ST,future_reason,breadth,Breadth FAIL
MIPS.ST,sf_reason,compensation,"trailing three-year read: a breach on both, so a hard strike"
ML.PA,core_cash,3397,"+ 702 + 2,001 + 262), cash and STI €3,397m (2,891 + 506), NCI €6m, no"
ML.PA,core_currency,EUR,-
ML.PA,core_debt_eq,7963,"2,366 − 7,957 − 0 − 6) ÷ 686.4 = (16,562 − 7,963) ÷ 686.4 = €12.53. - EV/OI"
ML.PA,core_fcf,1852,"€2,366m. FCF = FY2025 derived €1,852m. Diluted shares for band"
ML.PA,core_fx,1,-
ML.PA,core_fx_date,n.m.,-
ML.PA,core_oi,2366,"€27,721m. OI = FY2025 as-reported €2,366m. FCF = FY2025 derived"
ML.PA,core_ratio,1,-
ML.PA,core_shares_diluted,686.4,Diluted shares for band arithmetic 686.4m (derived). Current
ML.PA,core_unit,m,-
ML.PA,past_reason,8.4% ROCE,Worst-of-four normalized ROCE 8.39%
ML.PA,sf_reason,buybacks,Capital allocation is CAUTION: repurchases execute at 8
MMB.PA,future_reason,2+ forces,Tally 3 strong
MMB.PA,past_reason,5.1% ROCE,Worst-of-four normalized ROCE is 5.11%
MONC.MI,core_cash,1477405,"€95. Cash and short-term investments €1,477,405. Book value €3,849,694."
MONC.MI,core_currency,EUR,-
MONC.MI,core_debt_eq,1128553,"7 × 913,356 − 1,128,458 − 95) ÷ 271,286 = 5,264,939 ÷ 271,286 = €19.41 - EV/OI leg, all-cash: (7 × 913,356 +"
MONC.MI,core_fcf,740401,"shares 271,286k. OI €913,356. FCF €740,401. Total debt €1,128,458"
MONC.MI,core_fx,1,-
MONC.MI,core_fx_date,n.m.,-
MONC.MI,core_oi,913356,"diluted shares 271,286k. OI €913,356. FCF €740,401. Total debt"
MONC.MI,core_ratio,1,-
MONC.MI,core_shares_diluted,271.286,"treasury. Weighted-average diluted shares 271,286k. OI €913,356. FCF"
MONC.MI,core_unit,k,-
MONC.MI,sf_reason,flag pair,FAIL (flag pair)
MORN,core_cash,523.8,"EV conservative = 7,224 + 1,695.1 + 18.2 + 191.5 − 489.5 − 34.3 = $8,605M"
MORN,core_currency,USD,-
MORN,core_debt_eq,1904.8,"EV conservative = 7,224 + 1,695.1 + 18.2 + 191.5 − 489.5 − 34.3 = $8,605M"
MORN,core_fcf,442.6,"Operative FY2025 figures: OI $526.6M, FCF $442.6M"
MORN,core_fcf_basis,FY2025 CFO − capex,-
MORN,core_fx,1,-
MORN,core_fx_date,n.m.,-
MORN,core_oi,526.6,"Operative FY2025 figures: OI $526.6M, FCF $442.6M"
MORN,core_oi_basis,FY2025 reported,-
MORN,core_period,FY2025; BS Q2 2026,-
MORN,core_ratio,1,-
MORN,core_shares_diluted,37.51353,"37,513,530 shares outstanding"
MORN,core_unit,m,-
MORN,sf_reason,buybacks,"*Repurchases — live, drawing, and priced far better than the"
MSFT,core_cash,76843,"= $128.52; all-cash bound = (1,086,659 + 76,843 − 128,813) ÷ 7,453 ="
MSFT,core_currency,USD,-
MSFT,core_debt_eq,128813,"all-cash bound = (1,086,659 + 76,843 − 128,813) ÷ 7,453 = 1,034,689 ÷"
MSFT,core_fx,1,-
MSFT,core_fx_date,n.m.,-
MSFT,core_oi,155237,"| Arithmetic: no-cash bound = (7 × 155,237 − 40,294 − 88,519) ÷ 7,453"
MSFT,core_ratio,1,-
MSFT,core_shares_diluted,7453,"2026 close), 7,427M shares outstanding, 7,453M diluted, FY2026 basis."
MSFT,core_unit,m,-
MSFT,sf_reason,buybacks,four repurchase years executed at 22.2–25.7× EV/OI
MTD,core_cash,51.4,labelled); preferred 0; NCI 0; cash 51.4; no STI. - EV. No-cash
MTD,core_currency,USD,-
MTD,core_debt_eq,2225.2,"7 × 1,100.6 − 2,112.0 − 113.2) ÷ 20.166 = $271.70. - EV/OI all-cash: + 51.4 gives $274.25. - EV/OI binds. The"
MTD,core_fcf,848.6,"Multiples (FY2025). - MCap/FCF: 29,971.0 ÷ 848.6 = 35.3×. - EV/OI: 32,196.1"
MTD,core_fx,1,-
MTD,core_fx_date,n.m.,-
MTD,core_oi,1100.6,"÷ 848.6 = 35.3×. - EV/OI: 32,196.1 ÷ 1,100.6 = 29.3× (no-cash) and"
MTD,core_ratio,1,-
MTD,core_shares_diluted,20.166,"$1,486.19 (2 Oct 2026). Diluted shares 20.166m (Q2 2026 three-month WA)."
MTD,core_unit,m,-
MTD,sf_reason,buybacks,6bn of repurchases cleared ≈ 25× on all four reads from FY2019 to
MU,future_reason,customer conc.,Breadth FAIL: one customer was 17% of FY20
MU,sf_reason,buybacks,Buybacks strike: FY2024's $300M at $93
MYCR.ST,core_currency,SEK,-
MYCR.ST,core_debt_eq,420,"conservative (no cash excess) = 61,276 + 420 = SEK 61,696m; lower"
MYCR.ST,core_fcf,1242,"|---|---|---|---| | MCap / FCF | 61,276 ÷ 1,242 | 49.3× | ≤ 8 | | EV / OI"
MYCR.ST,core_fx,1,-
MYCR.ST,core_fx_date,n.m.,-
MYCR.ST,core_oi,1940,"≤ 8 | | EV / OI (conservative) | 61,696 ÷ 1,940 | 31.8× | ≤ 7 | | EV / OI"
MYCR.ST,core_ratio,1,-
MYCR.ST,core_shares_diluted,195.3,"− capex 165), NI SEK 1,560m, diluted 195.3m, shares outstanding"
MYCR.ST,core_unit,m,-
MYCR.ST,sf_reason,buybacks,* Repurchases exist solely to deliver stock to LTIP participa
NDSN,core_cash,113.4,"= $56.47; all-cash (7 × 711.7 − 1,818.2 + 113.4) / 56.027 = $58.49. Bounds"
NDSN,core_currency,USD,-
NDSN,core_debt_eq,1818.2,"$94.40. - EV/OI leg: no-cash (7 × 711.7 − 1,818.2) / 56.027 = $56.47;"
NDSN,core_fcf,661.1,"$333.54 × 55.699m = $18,578m. FY2025 FCF 661.1 → MCap/FCF 28.1× (TTM 724.0"
NDSN,core_fx,1,-
NDSN,core_fx_date,n.m.,-
NDSN,core_oi,711.7,"724.0 → 25.7×). - EV no-cash 20,396 / OI 711.7 = 28.7×; EV all-cash 20,283"
NDSN,core_ratio,1,-
NDSN,core_shares_diluted,56.027,n.m. (TBV −673.1). - FCF leg: 8 × 661.1 / 56.027 = $94.40. - EV/OI leg:
NDSN,core_unit,m,-
NDSN,past_reason,ROCE decline,WEAK — a sustained decline forces the downgrade from an ADEQUATE level
NDSN,sf_reason,buybacks,"Capital allocation is CAUTION: repurchases ran 13–29× across the decade, never at the barg"
NEE,past_reason,3% ROCE,normalized ROCE lands ≈ 3–5%
NESN.SW,core_cash,6134,"EV all-cash-excess = 208,374 + 62,845 + 274 − 6,134 = CHF 265,359m"
NESN.SW,core_currency,CHF,-
NESN.SW,core_debt_eq,63119,"EV all-cash-excess = 208,374 + 62,845 + 274 − 6,134 = CHF 265,359m"
NESN.SW,core_fcf,10993,"FY25 FCF CHF 10,993m"
NESN.SW,core_fcf_basis,FY2025 CFO − all capex,-
NESN.SW,core_fx,1,-
NESN.SW,core_fx_date,n.m.,-
NESN.SW,core_oi,12277,"FY25 OI CHF 12,277m"
NESN.SW,core_oi_basis,FY2025 reported,-
NESN.SW,core_period,FY2025,-
NESN.SW,core_ratio,1,-
NESN.SW,core_shares_diluted,2576,"diluted 2,576m"
NESN.SW,core_unit,m,-
NESN.SW,sf_reason,buybacks,"*Repurchases — the flag, and it is historical"
NESTE.HE,future_reason,moat eroding,t: the pretreatment/technology lead has eroded into a commodity spread
NESTE.HE,past_reason,growth,WEAK (P4 — below P3 on the growth limb
NET,past_reason,losses,GAAP operating income is negative in all nine window years
NET,sf_reason,compensation,"No proxy has been filed since v1, so the P17 hard strikes stand exactly as logged: Prince ≈$61m and Zatlyn"
NFLX,future_reason,forces: suppliers,supplier power STRONG
NFLX,sf_reason,compensation,FAIL — strike: executive compensation
NGVT,future_reason,2+ forces,Forces: customer power STRONG (auto-industry purchasing against a com
NGVT,past_reason,4.9% ROCE,Worst-of-four normalized ROCE 4.90%
NGVT,sf_reason,acquisitions,the acquisition record is the write-off itself
NKE,future_reason,moat eroding,"oat: brand, single-source, dominant but eroding — FY2024–26 relative TSR at t"
NKE,past_reason,ROCE decline,"7% across three consecutive years, the terminal reading below even the STRONG"
NKE,sf_reason,buybacks,1bn repurchased at $97
NMAN.ST,core_cash,513.6,"÷ 35.042 = SEK 25.17; all-cash (3,530.1 + 513.6 − 2,648.0) ÷ 35.042 = SEK"
NMAN.ST,core_currency,SEK,-
NMAN.ST,core_debt_eq,2648,"= SEK 25.17; all-cash (3,530.1 + 513.6 − 2,648.0) ÷ 35.042 = SEK 39.83;"
NMAN.ST,core_fcf,155.6,"F. Valuation math - MCap/FCF = 4,366.2 ÷ 155.6 = 28.1×. EV/OI = 7,014.2 ÷"
NMAN.ST,core_fx,1,-
NMAN.ST,core_fx_date,n.m.,-
NMAN.ST,core_oi,504.3,"4,366.2 ÷ 155.6 = 28.1×. EV/OI = 7,014.2 ÷ 504.3 = 13.9× (no-cash) / 6,500.6"
NMAN.ST,core_ratio,1,-
NMAN.ST,core_shares_diluted,35.042,n.m. (TBV −305.8). - FCF leg: 8 × 155.6 ÷ 35.042 = SEK 35.52. - EV/OI leg:
NMAN.ST,core_unit,m,-
NOKIA.HE,aliases,NOK ADR 1:1,Nokia Oyj (NOK ADR 1:1)
NOKIA.HE,core_cash,5130,"− 3,413 − 97)/5,600m = €0.48; all-cash (+5,130) = €1.40. Bounds: €0.48"
NOKIA.HE,core_currency,EUR,-
NOKIA.HE,core_debt_eq,3510,"7 × 885 − 3,413 − 97)/5,600m = €0.48; all-cash (+5,130) = €1.40. Bounds: €0.48 (EV/OI binds) / €0.76 (FCF leg"
NOKIA.HE,core_fcf,535,"- Threshold-implied prices: FCF leg 8 × 535/5,600m = €0.76. EV/OI legs:"
NOKIA.HE,core_fx,1,-
NOKIA.HE,core_fx_date,n.m.,-
NOKIA.HE,core_oi,885,"= €0.76. EV/OI legs: no-cash (7 × 885 − 3,413 − 97)/5,600m ="
NOKIA.HE,core_ratio,1,-
NOKIA.HE,core_shares_diluted,5600,"Threshold-implied prices: FCF leg 8 × 535/5,600m = €0.76. EV/OI legs:"
NOKIA.HE,core_unit,m,-
NOKIA.HE,past_reason,4.7% ROCE,worst-of-four normalized ROCE 4.67%
NOKIA.HE,sf_reason,dilution,"post-announcement price) is a governance-adjacent dilution event — logged as context, not a strike (strategi"
NOLA-B.ST,core_cash,482,"= SEK 19.37; P_all-cash = (7 × 1,024 + 482 − 1,949) / 269.381 = 5,701"
NOLA-B.ST,core_currency,SEK,-
NOLA-B.ST,core_debt_eq,1949,"EV/OI leg: P_no-cash = (7 × 1,024 − 1,949) / 269.381 = 5,219 /"
NOLA-B.ST,core_fcf,273,"EV_all-cash 14,761. - MCap/FCF = 13,294 / 273 = 48.7× (≤ 8 FAIL)."
NOLA-B.ST,core_fx,1,-
NOLA-B.ST,core_fx_date,n.m.,-
NOLA-B.ST,core_oi,1024,"R12M FCF 468:* 28.4×. - EV/OI = 15,243 / 1,024 = 14.9× no-cash; 14,761 /"
NOLA-B.ST,core_ratio,1,-
NOLA-B.ST,core_shares_diluted,269.381,"math @ SEK 49.35 (intraday 2026-08-06), 269.381m diluted, FY2025"
NOLA-B.ST,core_unit,m,-
NOLA-B.ST,sf_reason,flag pair,FAIL — flag pair
NOMD,future_reason,2+ forces,"Forces: customer power STRONG (consolidated grocery, retailer-control"
NOMD,past_reason,6.6% ROCE,Worst-of-four normalized average ROCE over FY2021–FY2025 is 6.58%
NOMD,sf_reason,distributions,FY2025 cash dividends €91.3m
NOVO-B.CO,core_cash,44982,"140,127 (leases in); cash + STI 44,982; diluted shares 4,441.0m;"
NOVO-B.CO,core_currency,DKK,-
NOVO-B.CO,core_debt_eq,140127,"price): FY2025 OI 127,658; borrowings 140,127 (leases in); cash + STI"
NOVO-B.CO,core_fcf,28989,"the all-cash bound; strict all-capex 8 × 28,989 ÷ 4,441.0 = 52.22"
NOVO-B.CO,core_fx,1,-
NOVO-B.CO,core_fx_date,n.m.,-
NOVO-B.CO,core_oi,127658,"(unchanged except price): FY2025 OI 127,658; borrowings 140,127 (leases"
NOVO-B.CO,core_ratio,1,-
NOVO-B.CO,core_shares_diluted,4441,"in); cash + STI 44,982; diluted shares 4,441.0m; price DKK 248.75 (2 Oct"
NOVO-B.CO,core_unit,m,-
NOVO-B.CO,future_reason,customer conc.,Breadth: customers FAIL as written — three US wholesa
NOVO-B.CO,sf_reason,flag pair,FAIL (flag pair — capital-allocation CAUTION [P19] + related-party flag [controller as buyback counterparty and Catalent-site vendor]; no hard strike)
NOVT,future_reason,customer conc.,Breadth fails on the customer side: two me
NOVT,past_reason,7.9% ROCE,worst-of-four average ROCE is 7.9%
NOVT,sf_reason,compensation,FAIL — P17 hard strike
NU,core_currency,USD,-
NU,core_fcf,n.m.,deposit-funded lender (ROE basis; OI/FCF/CE machinery inapplicable)
NU,core_fcf_basis,n.m. — deposit-flow distortion,-
NU,core_fx,1,-
NU,core_fx_date,n.m.,-
NU,core_oi,n.m.,deposit-funded lender (ROE basis; OI/FCF/CE machinery inapplicable)
NU,core_oi_basis,n.m. — substitution rule (MCap/NI anchor),-
NU,core_ratio,1,-
NU,core_shares_diluted,4830,"shares 4,830m (v1 basis)"
NU,core_unit,m,-
NU,printed_mcap_fcf,n.m.,deposit-funded lender (ROE basis; OI/FCF/CE machinery inapplicable)
NU,sf_reason,buybacks,"0bn of Class A repurchases over 12 months (10b-18/10b5-1, ""attractive use"
NVDA,future_reason,customer conc.,Breadth: customer-side FAIL — one direct customer 22% of
NVDA,sf_reason,compensation,CEO pay above the $30M cap for a third straight year
NVS,core_cash,11935,"− cash&STI 11,935 = 310,213 (low)"
NVS,core_currency,USD,-
NVS,core_debt_eq,31068,"debt (borrowings 28,729 + leases 1,920) 30,649 + NCI 419"
NVS,core_fcf,17596,"MCap $291.1bn): MCap/FCF 291,080/17,596 = 16.5×; EV/OI"
NVS,core_fx,1,-
NVS,core_fx_date,n.m.,-
NVS,core_oi,17644,"291,080/17,596 = 16.5×; EV/OI 310,213/17,644 = 17.6× (low) /"
NVS,core_ratio,1,-
NVS,core_shares_diluted,1915,"## F. Valuation math - Current (P=$152, S=1,915m, MCap $291.1bn): MCap/FCF"
NVS,core_unit,m,-
NVS,printed_ev_oi_all_cash,17.6,"EV/OI 310,213/17,644 = 17.6× (low)"
NVS,sf_reason,buybacks,Buybacks PASS with a flag: FY2025 program repurchases (~$115/sh) imply 13
OKTA,past_reason,losses,GAAP operating income is negative in nine of ten window years
OKTA,sf_reason,compensation,Hard strike — both reads
ONON,past_reason,8.2% ROCE,Worst-of-four normalized ROCE 8.2%
OPEN,future_reason,no moat,Tally: 1 STRONG — but no moat exists: the pricing algorithm
OPEN,past_reason,losses,Operating income negative in all five reported years
OPEN,sf_reason,compensation,P17 — hard strike: CEO Nejatian (Sep 2025 hire) received a PRSU pac
OR.PA,core_currency,EUR,-
OR.PA,core_fcf,7161.6,"= €219,575m. - MCap/FCF = 206,911 ÷ 7,161.6 = 28.9× (≤8 FAIL) - EV/OI ="
OR.PA,core_fx,1,-
OR.PA,core_fx_date,n.m.,-
OR.PA,core_oi,8386.5,"= 28.9× (≤8 FAIL) - EV/OI = 219,575 ÷ 8,386.5 = 26.2× on FY2025 operating"
OR.PA,core_ratio,1,-
OR.PA,core_shares_diluted,534.723,"EV/OI ≤ 7 = (7 × 8,386.5 − 12,663.8) ÷ 534.723 = €86.10 (binds); MCap/FCF"
OR.PA,core_unit,m,-
OR.PA,printed_ev_oi,-,the no-cash variant is not separately computable
OR.PA,sf_reason,acquisitions,"*Reinvestment:* runs through acquisition, and FY2026 has been the most active year in the"
ORCL,future_reason,breadth,Breadth fails both sides for the capital-r
ORCL,past_reason,ROCE decline,"10% ADEQUATE, <15% STRONG, in sustained decline)"
ORCL,sf_reason,compensation,Unchanged FAIL — strike is compensation (P17)
ORSTED.CO,future_reason,2+ forces,Forces: customer power STRONG — demonstrated (offtake is won at gover
ORSTED.CO,past_reason,2.3% ROCE,worst-of-four normalized ROCE 2.33%
ORSTED.CO,sf_reason,flag pair,Pair: P17 normalized breach + P19 CAUTION → SF FAIL
PAH3.DE,future_reason,2+ forces,"adverse forces run STRONG (customer choice, substitutes, new entr"
PAH3.DE,past_reason,losses,worst-of-four ROE (≈−1.0%
PAH3.DE,sf_reason,control,The framework treats control as a caveat that becomes a strike
PANW,future_reason,customer conc.,"Breadth: customer-side FAIL on the primary sentence — ""fo"
PANW,past_reason,1.8% ROCE,ROCE lands at 1.8–3.8%
PANW,sf_reason,compensation,"7m) — breach on both reads = hard strike, in the first year the company printed material G"
PATH,past_reason,losses,GAAP OI: five negative years
PATH,sf_reason,flag pair,Flag pair (P17 + P19) → SF FAIL — the TWLO pattern at the same convalescent stage
PAYO,future_reason,forces: substitutes,substitutes STRONG
PAYO,past_reason,8.7% ROCE,Worst-of-four normalized ROCE 8.70%
PAYO,sf_reason,compensation,ormalized — NI leg binds): breach on both reads → hard strike
PDX.ST,core_currency,SEK,-
PDX.ST,core_debt_eq,165236,"EV/OI leg conservative (7 × 145,999 − 165,236) ÷ 105,623 = SEK 8.11;"
PDX.ST,core_fcf,581013,"goodwill). Threshold prices: FCF leg 8 × 581,013 ÷ 105,623 = SEK 44.00;"
PDX.ST,core_fx,1,-
PDX.ST,core_fx_date,n.m.,-
PDX.ST,core_oi,145999,"= SEK 44.00; EV/OI leg conservative (7 × 145,999 − 165,236) ÷ 105,623 = SEK"
PDX.ST,core_ratio,1,-
PDX.ST,core_shares_diluted,105.623,"Threshold prices: FCF leg 8 × 581,013 ÷ 105,623 = SEK 44.00; EV/OI leg"
PDX.ST,core_unit,k,-
PDX.ST,future_reason,customer conc.,"Customer breadth FAIL: one platform, Steam, is 84"
PHIA.AS,past_reason,3.5% ROCE,Worst-of-four normalized averages (FY2016–25): ROCE 3.5%
PHIA.AS,sf_reason,buybacks,Buybacks: hard strike
PIRC.MI,core_cash,1605790,"other current financial assets 79,904 | (1,605,790) | | EV, all cash treated"
PIRC.MI,core_currency,EUR,-
PIRC.MI,core_debt_eq,3136683,"7 × 891,203 − 2,957,794 − 178,889) ÷ 1,084,882 | €2.859 | | EV/OI ≤ 7, all-cash | (7 × 891,203 + 1,605,790 −"
PIRC.MI,core_fcf,776371,"MCap/FCF 9.1× on FY2025 derived FCF of €776,371k. EV/OI 11.4× no-cash and"
PIRC.MI,core_fx,1,-
PIRC.MI,core_fx_date,n.m.,-
PIRC.MI,core_oi,891203,"all-cash on FY2025 operating income of €891,203k. MCap/BV 1.12×. MCap/TBV"
PIRC.MI,core_ratio,1,-
PIRC.MI,core_shares_diluted,1084.882,"| MCap/FCF ≤ 8 | 8 × 776,371 ÷ 1,084,882 | €5.725 | | EV/OI ≤ 7,"
PIRC.MI,core_unit,k,-
PIRC.MI,past_reason,6.2% ROCE,Worst-of-four normalized ROCE 6.2%
PKN.WA,past_reason,growth,WEAK (P4 — below P3 on growth
PKN.WA,sf_reason,flag pair,Two independent flags → SF FAIL (§2·1C pair rule)
PLTR,past_reason,0.4% ROCE,Worst-of-four normalized-average ROCE = 0.4%
PLTR,sf_reason,flag pair,FAIL comes from a flag pair: (1) entrenched dual-class super-voting control (
PSH.L,past_reason,10.5% ROE,Trailing NAV CAGR is 17.3% (10y) but only 10.5% (5y)
PSH.L,sf_reason,RPT,fee = manager-compensation extraction (substance P17 hard strike) + dominant RPT
PTC,past_reason,9.5% ROCE,Worst-of-four normalized ROCE is 9.5%
PTC,sf_reason,flag pair,Capital allocation is CAUTION: flag 2
PTON,future_reason,moat eroding,"mmunity) — real for the remaining base, eroding at a measured 9%/yr"
PTON,past_reason,losses,every normalized ROCE/FCFROCE variant is deeply negative
PTON,sf_reason,compensation,P17 hard strike
PVH,future_reason,2+ forces,Forces decide it
PVH,past_reason,4% ROCE,Worst-of-four normalized average ROCE is 4.0%
PVH,sf_reason,compensation,P17 flag re-tested against the 2027 proxy
PYPL,core_cash,11256,"| | EV/OI ≤ 7, all-cash EV | (7 × 6,065 + 11,256 − 13,400) ÷ 855.461 |"
PYPL,core_currency,USD,-
PYPL,core_debt_eq,13400,"| | EV/OI ≤ 7, no-cash EV | (7 × 6,065 − 13,400) ÷ 855.461 | $33.96 | |"
PYPL,core_fcf,5564,"Operative bases: FY2025 OI 6,065 and FCF 5,564. Reference: TTM to 30 June"
PYPL,core_fx,1,-
PYPL,core_fx_date,n.m.,-
PYPL,core_oi,6065,"MCap $45,955m. Operative bases: FY2025 OI 6,065 and FCF 5,564. Reference:"
PYPL,core_ratio,1,-
PYPL,core_shares_diluted,855.461,"close, Friday 11 September 2026); shares 855.461m → MCap $45,955m. Operative"
PYPL,core_unit,m,-
PYPL,future_reason,supplier conc.,Supplier breadth fails: transaction expense was $15
PYPL,sf_reason,buybacks,Capital allocation is CAUTION: FY2016–22 repurchases were plainly overpriced under allocators who ha
QCOM,core_cash,8304,"15,270 = $171,294M; all-cash-excess EV = − 8,304 = $162,990M. - MCap/FCF ="
QCOM,core_currency,USD,-
QCOM,core_debt_eq,15270,"$156,024M. Conservative EV = 156,024 + 15,270 = $171,294M;"
QCOM,core_fcf,12820,"8,304 = $162,990M. - MCap/FCF = 156,024 ÷ 12,820 = 12.2× (15.0× on TTM FCF"
QCOM,core_fx,1,-
QCOM,core_fx_date,n.m.,-
QCOM,core_oi,12355,"on TTM FCF $10,416M) - EV/OI = 171,294 ÷ 12,355 = 13.9× conservative;"
QCOM,core_ratio,1,-
QCOM,core_shares_diluted,1057,"Valuation math At $147.61 (31 Jul 2026; 1,057M shares outstanding): MCap"
QCOM,core_unit,m,-
QCOM,sf_reason,buybacks,*Repurchases — the flag
RACE.MI,core_cash,1546,"EV all-cash-excess = 60,640 + 2,884 + 8 − 1,546 = €61,986m"
RACE.MI,core_currency,EUR,-
RACE.MI,core_debt_eq,2892,"EV all-cash-excess = 60,640 + 2,884 + 8 − 1,546 = €61,986m"
RACE.MI,core_fcf,1406,"MCap/FCF = 60,640 ÷ 1,406 = 43.1×"
RACE.MI,core_fx,1,-
RACE.MI,core_fx_date,n.m.,-
RACE.MI,core_oi,2110,"EV/OI = 61,986 ÷ 2,110 = 29.4× all-cash-excess"
RACE.MI,core_oi_basis,FY2025 reported,-
RACE.MI,core_period,FY2025,-
RACE.MI,core_ratio,1,-
RACE.MI,core_shares_diluted,178.3,"× 178.3m diluted = MCap €60,640m"
RACE.MI,core_unit,m,-
RACE.MI,sf_reason,buybacks,"*Repurchases — the failure, on all three limbs"
RBREW.CO,core_cash,54,"= DKK 182.0; all-cash P = (7 × 2,202 + 54 − 6,664) / 48.07 = DKK"
RBREW.CO,core_currency,DKK,-
RBREW.CO,core_debt_eq,6664,"257.0. EV/OI leg no-cash P = (7 × 2,202 − 6,664) / 48.07 = DKK 182.0;"
RBREW.CO,core_fcf,1544,"## F. Valuation math MCap/FCF = 19,487 / 1,544 = 12.6× (LTM derived FCF"
RBREW.CO,core_fx,1,-
RBREW.CO,core_fx_date,n.m.,-
RBREW.CO,core_oi,2202,"1,562 → 12.5×). EV/OI no-cash = 26,151 / 2,202 = 11.9×; all-cash = 26,097"
RBREW.CO,core_ratio,1,-
RBREW.CO,core_shares_diluted,48.07,"n.m. Band: FCF leg P = 8 × 1,544 / 48.07 = DKK 257.0. EV/OI leg"
RBREW.CO,core_unit,m,-
RBREW.CO,sf_reason,buybacks,"Capital allocation is CAUTION: the 2020–21 buybacks ran ≈ 23–29× on all four reads, and the platform"
RCO.PA,future_reason,customer conc.,Breadth FAILS on the customer side
RCO.PA,past_reason,ROCE decline,tive per-share growth and the sustained decline in returns each make Past WEAK
RCO.PA,sf_reason,flag pair,FAIL (flag pair: P17 normalized read + capital-allocation CAUTION
RHIM.L,future_reason,2+ forces,"Forces: customer power STRONG, because concentrated steelmakers buy i"
RHIM.L,past_reason,7.4% ROCE,Worst-of-four normalized ROCE is 7.4%
RHIM.L,sf_reason,acquisitions,The live question is the Vesuvius proposal: a debt-funded cash-and-share bid
RI.PA,core_cash,1993,"= €5.66. - EV/OI all-cash: (15,134 + 1,993 − 13,707) / 252.342 = 3,420"
RI.PA,core_currency,EUR,-
RI.PA,core_debt_eq,13707,"€5.66. - EV/OI all-cash: (15,134 + 1,993 − 13,707) / 252.342 = 3,420 /"
RI.PA,core_fcf,1188,"252.342m = €14,792m. - MCap/FCF = 14,792 / 1,188 = 12.5×. - EV/OI = 28,499 /"
RI.PA,core_fx,1,-
RI.PA,core_fx_date,n.m.,-
RI.PA,core_oi,2162,"14,792 / 1,188 = 12.5×. - EV/OI = 28,499 / 2,162 = 13.2× no-cash; 26,506 /"
RI.PA,core_ratio,1,-
RI.PA,core_shares_diluted,252.342,"## F. Valuation math - MCap = €58.62 × 252.342m = €14,792m. - MCap/FCF ="
RI.PA,core_unit,m,-
RI.PA,past_reason,7.8% ROCE,worst-of-four ROCE is 7.8%
RMS.PA,core_cash,12773,"all-cash-excess = − 12,773 = €150,443m"
RMS.PA,core_currency,EUR,-
RMS.PA,core_debt_eq,2352,"EV no-cash = 160,864 + 34 + 2,312 + 6 = €163,216m"
RMS.PA,core_fcf,4213,"160,864 ÷ 4,213"
RMS.PA,core_fcf_basis,FY2025 CFO − capex,-
RMS.PA,core_fx,1,-
RMS.PA,core_fx_date,n.m.,-
RMS.PA,core_oi,6569,"163,216 ÷ 6,569"
RMS.PA,core_oi_basis,FY2025 reported,-
RMS.PA,core_period,FY2025,-
RMS.PA,core_ratio,1,-
RMS.PA,core_shares_diluted,105.036704,"× 105,036,704 diluted = MCap €160,864m"
RMS.PA,core_unit,m,-
RMS.PA,sf_reason,buybacks,*Repurchases — the flag
ROCK-B.CO,core_cash,108,Debt 276 (derived); cash 108 (financial assets 42 excluded from cash
ROCK-B.CO,core_currency,EUR,-
ROCK-B.CO,core_debt_eq,276,Debt 276 (derived); cash 108 (financial assets 42 excluded from cash
ROCK-B.CO,core_fcf,124,FCF 8×124/209.5 = EUR 4.73 (DKK 35.3)
ROCK-B.CO,core_fx,7.46,"Price DKK 232.00 / EUR 31.10 (FX 7.46, Aug 2026); MCap EUR 6,546m"
ROCK-B.CO,core_fx_date,-,-
ROCK-B.CO,core_oi,178,"EV/OI nc (1,246−276)/209.5 = EUR 4.63 (DKK 34.5)"
ROCK-B.CO,core_oi_basis,FY2025 reported,-
ROCK-B.CO,core_period,FY2025,-
ROCK-B.CO,core_ratio,1,-
ROCK-B.CO,core_shares_diluted,209.5,Share count 209.5m (MCap/price implied; 206.81m ex-treasury quoted)
ROCK-B.CO,core_unit,m,-
ROCK-B.CO,past_reason,12.4% ROCE,normalized ROCE 12.37% (end-basis
ROCK-B.CO,printed_ev_oi,38.3,Reported basis: EV/OI 38.3× / 37.7×; MCap/FCF 52.8×
ROCK-B.CO,printed_ev_oi_all_cash,37.7,Reported basis: EV/OI 38.3× / 37.7×; MCap/FCF 52.8×
ROCK-B.CO,printed_mcap_fcf,52.8,Reported basis: EV/OI 38.3× / 37.7×; MCap/FCF 52.8×
ROG.SW,core_cash,15486,"(7×20,958 + 15,486 − 33,197 − 4,078) ÷ 809.254 = CHF 154.4"
ROG.SW,core_currency,CHF,-
ROG.SW,core_debt_eq,37275,"(7×20,958 + 15,486 − 33,197 − 4,078) ÷ 809.254 = CHF 154.4"
ROG.SW,core_fcf,13915,"MCap/FCF = 265,498 ÷ 13,915 = 19.1×"
ROG.SW,core_fx,1,-
ROG.SW,core_fx_date,n.m.,-
ROG.SW,core_oi,20958,"EV/OI = 287,287 ÷ 20,958 = 13.7× (lo) / 14.5× (hi)"
ROG.SW,core_oi_basis,FY2025 reported,-
ROG.SW,core_period,FY2025,-
ROG.SW,core_ratio,1,-
ROG.SW,core_shares_diluted,809.254,Trigger prices per security (809.254m total units)
ROG.SW,core_unit,m,-
ROK,core_cash,468,"EV = 54,297 + 2,614 + 2 + 608 + 423 + 57 − 468 = $57,533M"
ROK,core_currency,USD,-
ROK,core_debt_eq,3704,"EV = 54,297 + 2,614 + 2 + 608 + 423 + 57 − 468 = $57,533M"
ROK,core_fcf,1358,"MCap/FCF = 54,297 ÷ 1,358 = 40.0×"
ROK,core_fx,1,-
ROK,core_fx_date,n.m.,-
ROK,core_oi,1703,"EV/OI = 57,533 ÷ 1,703 = 33.8×"
ROK,core_oi_basis,FY2025 reported,-
ROK,core_period,FY2025,-
ROK,core_ratio,1,-
ROK,core_shares_diluted,113.1,"At $480.08 (31 Jul 2026; 113.1M diluted): MCap $54,297M"
ROK,core_unit,m,-
ROK,past_reason,17.4% ROCE,ROCE_xc 17.4–42.1%
ROK,sf_reason,buybacks,"*Repurchases — the failure, on all three limbs"
RRTL.DE,future_reason,2+ forces,"Forces: customer power STRONG (agency-bought advertising, TV ad reven"
RRTL.DE,past_reason,ROCE decline,"WEAK: a sustained multi-year decline in returns, and negative per-share growth"
RRTL.DE,sf_reason,flag pair,Two flags: FAIL
RSW.L,core_cash,290.9,= £12.61. - EV/OI leg all-cash = (947.3 + 290.9 − 29.5) ÷ 72.757 = £16.61.
RSW.L,core_currency,GBP,-
RSW.L,core_debt_eq,29.5,£6.74. - EV/OI leg no-cash = (7 × 135.3 − 29.5) ÷ 72.757 = £12.61. - EV/OI
RSW.L,core_fcf,61.3,"F. Valuation math - MCap/FCF = 4,336.3 ÷ 61.3 = 70.7×. EV/OI = 4,365.8 ÷"
RSW.L,core_fx,1,-
RSW.L,core_fx_date,n.m.,-
RSW.L,core_oi,135.3,"4,336.3 ÷ 61.3 = 70.7×. EV/OI = 4,365.8 ÷ 135.3 = 32.3× (no-cash); 4,074.8"
RSW.L,core_ratio,1,-
RSW.L,core_shares_diluted,72.757,EXPENSIVE. - Band: - FCF leg = 8 × 61.3 ÷ 72.757 = £6.74. - EV/OI leg
RSW.L,core_unit,m,-
RUN,future_reason,moat eroding,ax-credit and net-metering regime — and eroding: NEM 3
RUN,past_reason,losses,Every year shows negative operating income and negative free cash flow
RUN,sf_reason,flag pair,FAIL — flag pair
RUSTA.ST,past_reason,leverage,Past is WEAK on leverage
RUSTA.ST,sf_reason,buybacks,FAIL — P19 hard strike: dilution-sterilisation
RVLV,core_cash,311.6,= $6.81; all-cash (519.8+311.6−30.9)/71.8 = $11.15. Band
RVLV,core_currency,USD,-
RVLV,core_debt_eq,30.9,= $4.95 ← binds; EV/OI no-cash (519.8−30.9)/71.8 = $6.81; all-cash
RVLV,core_fcf,44.42,- Trigger legs (FY25): FCF 8×44.42/71.8 = $4.95 ← binds; EV/OI
RVLV,core_fx,1,-
RVLV,core_fx_date,n.m.,-
RVLV,core_oi,74.3,"1,740/44.4 = 39.2×. EV/OI: 1,770.9/74.3 = 23.8× no-cash;"
RVLV,core_ratio,1,-
RVLV,core_shares_diluted,71.8,"/ MCap $1,740m / 71.1m out (FY25 wtd dil 71.8m): - MCap/FCF: 1,740/44.4 ="
RVLV,core_unit,m,-
RVLV,past_reason,growth,P3's growth limb fails
S,past_reason,losses,GAAP operating losses in all seven public years
SAF.PA,core_cash,7038,"EV (lower variant) = 141,451 + 5,326 + 622 − 7,038 = €140,361m"
SAF.PA,core_currency,EUR,-
SAF.PA,core_debt_eq,5948,"EV (lower variant) = 141,451 + 5,326 + 622 − 7,038 = €140,361m"
SAF.PA,core_fcf,3921,"MCap/FCF = 141,451 ÷ 3,921 = 36.1× (Safran FCF)"
SAF.PA,core_fx,1,-
SAF.PA,core_fx_date,n.m.,-
SAF.PA,core_oi,4308,"EV/OI = 140,361 ÷ 4,308 = 32.6× (résop)"
SAF.PA,core_oi_basis,FY2025 reported (résultat opérationnel),-
SAF.PA,core_period,FY2025,-
SAF.PA,core_ratio,1,-
SAF.PA,core_shares_diluted,418,"At €338.40 (31 Jul 2026; 418m diluted): MCap €141,451m"
SAF.PA,core_unit,m,-
SAF.PA,printed_ev_oi,-,-
SAF.PA,printed_ev_oi_all_cash,32.6,"EV/OI = 140,361 ÷ 4,308 = 32.6× (résop)"
SAF.PA,sf_reason,buybacks,The repurchase lever fails on all three limbs
SAN.PA,past_reason,7.4% ROCE,Worst-of-four normalized-average 10-year ROCE is 7.4%
SAN.PA,sf_reason,buybacks,FAIL (P19 hard strike)
SAND.ST,core_cash,4958,"(all cash excess) = − 4,958 = SEK 482,725m"
SAND.ST,core_currency,SEK,-
SAND.ST,core_debt_eq,40761,"EV (no cash excess) = 446,922 + 37,121 + 3,569 + 71 = SEK 487,683m"
SAND.ST,core_fcf,15382,"MCap/FCF = 446,922 ÷ 15,382 = 29.1×"
SAND.ST,core_fcf_basis,FY2025 CFO − capex,-
SAND.ST,core_fx,1,-
SAND.ST,core_fx_date,n.m.,-
SAND.ST,core_oi,20809,"487,683 ÷ 20,809 = 23.4×"
SAND.ST,core_oi_basis,FY2025 reported,-
SAND.ST,core_period,FY2025,-
SAND.ST,core_ratio,1,-
SAND.ST,core_shares_diluted,1255.4,"1,255.4m diluted"
SAND.ST,core_unit,m,-
SAND.ST,sf_reason,acquisitions,1× pre-deal operating income on every FX and normalisation re
SAP.DE,core_cash,8220,"EV_A (all cash excess) = 185,274 + 9,755 + 0 + 488 − 8,220 = €187,297"
SAP.DE,core_currency,EUR,-
SAP.DE,core_debt_eq,10243,"EV_A (all cash excess) = 185,274 + 9,755 + 0 + 488 − 8,220 = €187,297"
SAP.DE,core_fcf,8263,"MCap/FCF = 185,274 ÷ 8,263 = 22.4×"
SAP.DE,core_fcf_basis,FY2025 CFO − capex,-
SAP.DE,core_fx,1,-
SAP.DE,core_fx_date,n.m.,-
SAP.DE,core_oi,9617,"EV/OI = 187,297 ÷ 9,617 = 19.5×"
SAP.DE,core_oi_basis,FY2025 reported,-
SAP.DE,core_period,FY2025,-
SAP.DE,core_ratio,1,-
SAP.DE,core_shares_diluted,1175,"1,175m diluted; FY2025 financials, €m"
SAP.DE,core_unit,m,-
SAP.DE,past_reason,12.2% ROCE,Worst-of-four normalized ten-year averages: ROCE 12.2%
SAP.DE,sf_reason,buybacks,"The live €10bn programme has repurchased 16,280,097 shares"
SAVE.ST,core_currency,SEK,-
SAVE.ST,core_fx,1,-
SAVE.ST,core_fx_date,n.m.,-
SAVE.ST,core_oi,n.m.,| EV/OI | — | n.m. | ≤7 |
SAVE.ST,core_oi_basis,n.m. — substitution rule (MCap/NI anchor),-
SAVE.ST,core_ratio,1,-
SAVE.ST,core_shares_diluted,247.28,"At SEK 365.00 (31 Jul 2026; 247.28m derived shares): MCap SEK 90,243m"
SAVE.ST,core_unit,m,-
SAVE.ST,sf_reason,buybacks,The buyback is the marginal excess-capital return on top of a
SCHN.SW,core_cash,4282,"+ NCI 91 − cash and STI: all-cash-excess (4,282) → CHF 23,465m; no cash"
SCHN.SW,core_currency,CHF,-
SCHN.SW,core_debt_eq,779,"7 × 1,384 + 4,282 − 688 − 91) ÷ 107.31 = CHF 122.92. At a blended CHF 251.31 the distance is +144%. 2. Worth"
SCHN.SW,core_fcf,1383,"→ CHF 27,747m. - MCap/FCF = 26,968 ÷ 1,383 = 19.5× (≤8) - EV/OI ="
SCHN.SW,core_fx,1,-
SCHN.SW,core_fx_date,n.m.,-
SCHN.SW,core_oi,1384,"÷ 1,383 = 19.5× (≤8) - EV/OI = 23,465 ÷ 1,384 = 17.0× (all-cash) / 27,747"
SCHN.SW,core_ratio,1,-
SCHN.SW,core_shares_diluted,107.31,Blended CHF 251.31 per instrument on 107.31m. EV = MCap + debt 688 +
SCHN.SW,core_unit,m,-
SCHN.SW,sf_reason,buybacks,*Repurchases — the flag
SDZ.SW,core_currency,CHF,-
SDZ.SW,core_fcf,1101,"0; EV 40,749. FY2025 FCF (CFO−PP&E capex) 1,101; management FCF 1,547; IFRS"
SDZ.SW,core_fx,1,-
SDZ.SW,core_fx_date,n.m.,-
SDZ.SW,core_oi,1425,"1,101; management FCF 1,547; IFRS OI 1,425; core OI 2,094; BV 9,384;"
SDZ.SW,core_ratio,1,-
SDZ.SW,core_shares_diluted,436.8,"(CHF 67.04 × 1.2563); diluted shares 436.8M; MCap 36,788; total debt"
SDZ.SW,core_unit,m,-
SEE.L,future_reason,customer conc.,Customer breadth FAILS: two customers were 23
SEE.L,past_reason,losses,Worst-of-four normalized average ROCE is −30.0%
SEE.L,sf_reason,compensation,P17 hard strike under the loss-leg rule: both owner-earnings legs
SGO.PA,core_cash,5782,"= €39.75; P_all-cash = (7 × 5,293 + 5,782 − 17,614)/489 = €51.57."
SGO.PA,core_currency,EUR,-
SGO.PA,core_debt_eq,17614,"EV/OI leg: P_no-cash = (7 × 5,293 − 17,614)/489 = €39.75; P_all-cash ="
SGO.PA,core_fcf,3464,"multiples (FY25 OI 5,293; FY25 FCF 3,464): EV/OI 57,360/5,293 ="
SGO.PA,core_fx,1,-
SGO.PA,core_fx_date,n.m.,-
SGO.PA,core_oi,5293,"the EV build. Current multiples (FY25 OI 5,293; FY25 FCF 3,464): EV/OI"
SGO.PA,core_ratio,1,-
SGO.PA,core_shares_diluted,489,"(31 Jul 2026 close); shares outstanding 489m (30 Jun 2026, net of"
SGO.PA,core_unit,m,-
SGO.PA,sf_reason,acquisitions,"but GCP (2022, $2.3bn) was bought at ~17× trail"
SHA0.DE,future_reason,customer conc.,Customer breadth FAIL (probable): no positive no->1
SHA0.DE,past_reason,8% ROCE,Worst-of-four 10y normalized ROCE 8.0%
SHA0.DE,sf_reason,compensation,P17 hard strike (mechanical): highest-paid employee (CEO Rosenfel
SHOO,future_reason,2+ forces,Forces: customer power STRONG (those retailers run private-label foot
SHOO,past_reason,growth,The failure is the per-share growth limb
SHOO,sf_reason,compensation,P17 hard strike
SHOP,past_reason,0.5% ROCE,Worst-of-four normalized 10y ROCE 0.47%
SHOP,sf_reason,compensation,FAIL — P17 hard strike
SIE.DE,core_cash,14495,"+ 6,127 = €282,684m; all-cash-excess = − 14,495 = €268,189m; ex-SFS-debt"
SIE.DE,core_currency,EUR,-
SIE.DE,core_debt_eq,62142,"7 × 9,594 − 56,015 − 6,127) ÷ 780.264 = €6.43; all-cash-excess = €25.01; MCap/FCF ≤ 8 = €112.81. Mechanical"
SIE.DE,core_fcf,11003,"= €239,291m. - MCap/FCF = 220,542 ÷ 11,003 = 20.0× (≤8) - EV/OI ="
SIE.DE,core_fx,1,-
SIE.DE,core_fx_date,n.m.,-
SIE.DE,core_oi,9594,"÷ 11,003 = 20.0× (≤8) - EV/OI = 282,684 ÷ 9,594 = 29.5× no-cash / 268,189 ÷"
SIE.DE,core_ratio,1,-
SIE.DE,core_shares_diluted,780.264,"math At €282.65 (Xetra, 31 Jul 2026; 780.264m shares; FY2025"
SIE.DE,core_unit,m,-
SIE.DE,sf_reason,buybacks,*Repurchases — the flag
SIKA.SW,core_cash,625.3,"all-cash: (7 × 1,493.2 − 6,098.1 − 10.4 + 625.3) ÷ 160.729 = CHF 30.92 -"
SIKA.SW,core_currency,CHF,-
SIKA.SW,core_debt_eq,6108.5,"7 × 1,493.2 − 6,098.1 − 10.4) ÷ 160.729 = CHF 27.03 - EV/OI leg, all-cash: (7 × 1,493.2 − 6,098.1 − 10.4 +"
SIKA.SW,core_fcf,1332.5,"36,905.7. - MCap/FCF = 31,422.5 ÷ 1,332.5 = 23.58× (≤8 FAIL) - EV/OI"
SIKA.SW,core_fx,1,-
SIKA.SW,core_fx_date,n.m.,-
SIKA.SW,core_oi,1493.2,"= 23.58× (≤8 FAIL) - EV/OI = 37,531.0 ÷ 1,493.2 = 25.13× no-cash; 36,905.7"
SIKA.SW,core_ratio,1,-
SIKA.SW,core_shares_diluted,160.729,"math At CHF 195.50 (5 Aug 2026), 160.729m diluted: MCap 31,422.5; EV"
SIKA.SW,core_unit,m,-
SIKA.SW,past_reason,14.1% ROCE,Worst-of-four normalized 10y averages: ROCE 14.1%
SIKA.SW,sf_reason,buybacks,"n audits (Parex, MBCC) stay INDETERMINATE, but no repurchase is live, authorised or proposed, and the allocat"
SKF-B.ST,core_cash,9466,"3,825 | 4,567 | 455.6 | 106,422 | 19,269 | 9,466 | 50,754 | 53,558 | 14,412"
SKF-B.ST,core_currency,SEK,-
SKF-B.ST,core_debt_eq,17450,"7 × 7,755 − 15,340 − 2,110) ÷ 455.351 = SEK 80.9 - EV/OI ≤ 7, all-cash-excess (reference only): SEK 101.7"
SKF-B.ST,core_fcf,4567,"|---|---|---|---| | MCap / FCF | 116,479 ÷ 4,567 | 25.5× | ≤ 8 | | EV / OI"
SKF-B.ST,core_fx,1,-
SKF-B.ST,core_fx_date,n.m.,-
SKF-B.ST,core_oi,7755,"8 | | EV / OI (no cash excess) | 133,929 ÷ 7,755 | 17.3× | ≤ 7 | | EV / OI"
SKF-B.ST,core_ratio,1,-
SKF-B.ST,core_shares_diluted,455.351,"prices. - MCap/FCF ≤ 8: P = 8 × 4,567 ÷ 455.351 = SEK 80.2 - EV/OI ≤ 7,"
SKF-B.ST,core_unit,m,-
SMSH.TA,future_reason,customer conc.,Breadth FAIL: the Israeli MoD alone is ≈36
SMSH.TA,past_reason,0.1% ROCE,Worst-of-four normalized ROCE is 0.08%
SNA,core_cash,1644.7,"÷ 52.5 = $151.6; all-cash: (9,293.9 + 1,644.7 − 1,335.0) ÷ 52.5 = $182.9."
SNA,core_currency,USD,-
SNA,core_debt_eq,1335,"$153.2. EV/OI leg, no-cash: (7 × 1,327.7 − 1,335.0) ÷ 52.5 = (9,293.9 −"
SNA,core_fcf,1005.7,"shares 52.5m (Q2 2026); FY2025 FCF 1,005.7 (CFO 1,081.7 − capex 76.0);"
SNA,core_fx,1,-
SNA,core_fx_date,n.m.,-
SNA,core_oi,1327.7,"(CFO 1,081.7 − capex 76.0); FY2025 OI 1,327.7; balance sheet 4 Jul 2026"
SNA,core_ratio,1,-
SNA,core_shares_diluted,52.5,2 Oct 2026); diluted weighted shares 52.5m (Q2 2026); FY2025 FCF
SNA,core_unit,m,-
SNA,sf_reason,buybacks,"every year at 10–15× EV/OI, no worth criterion"
SNOW,future_reason,forces: suppliers,supplier power STRONG
SNOW,past_reason,losses,GAAP operating income is negative in all seven fiscal years
SNOW,sf_reason,buybacks,"The conduct: repurchases of $1,932m (FY2025, 2"
SONO,future_reason,customer conc.,"Breadth: customers — FAIL: ""Best Buy"
SONO,past_reason,losses,Worst-of-four normalized ROCE −1.64%
SONO,sf_reason,compensation,— 3y NI average negative): breach on both reads → hard strike
SOON.SW,core_cash,732.9,"- EV/OI leg, all-cash: P = (7 × 675.8 + 732.9 − 1,718.1 − 22.0) ÷ 59.6 ="
SOON.SW,core_currency,CHF,-
SOON.SW,core_debt_eq,1740.1,"− 1,718.1 − 22.0) ÷ 59.6 = (4,730.6 − 1,740.1) ÷ 59.6 = CHF 50.18 - EV/OI"
SOON.SW,core_fcf,577.2,(no-excess) · FY2025/26 OI 675.8 · FCF 577.2 · diluted shares 59.6m: -
SOON.SW,core_fx,1,-
SOON.SW,core_fx_date,n.m.,-
SOON.SW,core_oi,675.8,"/ 15,617.0 (no-excess) · FY2025/26 OI 675.8 · FCF 577.2 · diluted"
SOON.SW,core_ratio,1,-
SOON.SW,core_shares_diluted,59.6,"OI 675.8 · FCF 577.2 · diluted shares 59.6m: - MCap/FCF = 13,876.9 ÷"
SOON.SW,core_unit,m,-
SOON.SW,sf_reason,buybacks,the FY2022/23 and FY2021/22 tranches are clearly overpriced on every read
SOUN,future_reason,customer conc.,Breadth: customers FAIL
SOUN,past_reason,losses,FY2025 cut the operating loss to $23
SOUN,sf_reason,compensation,P17 hard strike
SPCX,future_reason,breadth,Breadth fails on both sides
SPCX,past_reason,record-limited,far short of P1
SPCX,sf_reason,compensation,FAIL — multiple independent hard strikes
SPOT,future_reason,supplier conc.,"Supplier breadth FAIL: UMG, Sony, Warner and Merlin"
SPOT,past_reason,4.3% ROCE,Worst-of-four normalized ROCE 4.3%
SPOT,sf_reason,buybacks,"P19: hard strike on every executed tranche — FY2025: 768,223 sh @ €571"
SRE,past_reason,3% ROCE,normalized ROCE ≈ 3% on any construction
SRT3.DE,past_reason,9.5% ROCE,Worst-of-four normalized ROCE 9.5%
SRT3.DE,sf_reason,acquisitions,"Polyplus, bought in 2023 for about EUR 2.4bn"
STMN.SW,core_cash,414603,"EV/OI leg, all-cash bound: (3,844,680 + 414,603 − 515,782) ÷ 159,649.305"
STMN.SW,core_currency,CHF,-
STMN.SW,core_debt_eq,515782,"EV/OI leg, all-cash bound: (3,844,680 + 414,603 − 515,782) ÷ 159,649.305"
STMN.SW,core_fcf,280512,"14,716,473 ÷ 280,512"
STMN.SW,core_fx,1,-
STMN.SW,core_fx_date,n.m.,-
STMN.SW,core_oi,549240,"15,232,255 ÷ 549,240"
STMN.SW,core_oi_basis,FY2025 reported,-
STMN.SW,core_period,FY2025; BS 2026-06-30,-
STMN.SW,core_ratio,1,-
STMN.SW,core_shares_diluted,159.649305,"Diluted shares 159,649,305 → MCap CHF 14,716,473k"
STMN.SW,core_unit,k,-
STMN.SW,sf_reason,buybacks,taking the treasury account from CHF 0.4m to CHF 53.2m
SU.PA,core_currency,EUR,-
SU.PA,core_debt_eq,21705,"36.8× (≤8 FAIL). - EV_no-cash = 168,923 + 21,705 = €190,628m → EV/OI ="
SU.PA,core_fcf,4588,"(derived), FY2025 OI €6,699m and FCF €4,588m, 30-Jun-2026 balance"
SU.PA,core_fx,1,-
SU.PA,core_fx_date,n.m.,-
SU.PA,core_oi,6699,"569.3m diluted (derived), FY2025 OI €6,699m and FCF €4,588m,"
SU.PA,core_ratio,1,-
SU.PA,core_shares_diluted,569.3,"outstanding net of 14.795m treasury, 569.3m diluted (derived), FY2025"
SU.PA,core_unit,m,-
SU.PA,sf_reason,buybacks,are met by named forward evidence: the live 2026 tranche prices at 32
SUN.SW,core_cash,843.3,− 367.3) / 33.858 = CHF 42.8; all-cash (+ 843.3) = CHF 67.7. The range is
SUN.SW,core_currency,CHF,-
SUN.SW,core_debt_eq,1582.1,"7 × 433.1 − 1,078.6 − 123.2 − 13.0 − 367.3) / 33.858 = CHF 42.8; all-cash (+ 843.3) = CHF 67.7. The range is"
SUN.SW,core_fcf,209.4,"F. Valuation math - MCap/FCF = 5,407.1 / 209.4 = 25.8×. EV/OI no-cash ="
SUN.SW,core_fx,1,-
SUN.SW,core_fx_date,n.m.,-
SUN.SW,core_oi,433.1,"209.4 = 25.8×. EV/OI no-cash = 6,989.2 / 433.1 = 16.1×; all-cash = 6,145.9"
SUN.SW,core_ratio,1,-
SUN.SW,core_shares_diluted,33.858,/ 545.5 = 9.91×. - FCF leg: 8 × 209.4 / 33.858 = CHF 49.5. - EV/OI leg:
SUN.SW,core_unit,m,-
SUN.SW,past_reason,6.8% ROCE,Worst-of-four normalized ROCE is 6.8%
SW.PA,future_reason,moat eroding,"asing scale and site density, and it is eroding: margin guidance moved 4"
SW.PA,past_reason,9.3% ROCE,worst-of-four normalized ROCE 9.34%
SW.PA,sf_reason,buybacks,Capital allocation is CAUTION: repurchases are plan-bounded and reach 12
SY1.DE,core_cash,1009.8,"Debt (incl leases) €2,630.2m; NCI €22.4m; cash+STI €1,009.8m"
SY1.DE,core_currency,EUR,-
SY1.DE,core_debt_eq,2652.6,"Debt (incl leases) €2,630.2m; NCI €22.4m; cash+STI €1,009.8m"
SY1.DE,core_fcf,503,"MCap/FCF: 24.4× (FCF €503m, int-reclass)"
SY1.DE,core_fx,1,-
SY1.DE,core_fx_date,n.m.,-
SY1.DE,core_oi,465,EV/OI: reported (€465m) 32.1× / 30.0×
SY1.DE,core_oi_basis,FY2025 reported,-
SY1.DE,core_period,FY2025,-
SY1.DE,core_ratio,1,-
SY1.DE,core_shares_diluted,139.772,"Price €87.94 × 139.772m sh = MCap €12,291m"
SY1.DE,core_unit,m,-
SY1.DE,past_reason,7.9% ROCE,worst-of-four normalized ROCE is ~7.9%
SYM,future_reason,customer conc.,Breadth FAIL
SYM,past_reason,losses,Worst-of-four normalized ROCE is −99.7%
SYM,sf_reason,flag pair,P17 normalized-read flag paired with an RPT opacity flag
TDOC,future_reason,forces: entrants,new entrants STRONG
TDOC,past_reason,losses,five losses
TDOC,sf_reason,compensation,malized — FCF single-leg): breach on both reads → hard strike
TDY,future_reason,customer conc.,"7% of FY2025 sales, so breadth fails as written"
TDY,past_reason,7.8% ROCE,worst-of-four average ROCE is 7.8%
TDY,sf_reason,acquisitions,0× pre-deal OI and FCF across the four reads and diluted retu
TEAM,past_reason,losses,"8%) — six of ten years show operating losses, including the three most recent"
TEAM,sf_reason,compensation,"P17 hard strike: highest-paid employee (CRO Brian Duffy, $23"
TENB,past_reason,losses,Operating income negative in all five reported years
TENB,sf_reason,flag pair,Flag pair → FAIL
TER,core_cash,354.829,"→ EV/OI = 94.6×. EV_all-cash = 61,529.1 − 354.829 = $61,174.2m → 94.1×. Both"
TER,core_currency,USD,-
TER,core_debt_eq,136.278,"$28.00; P_all-cash = (4,550.7 + 354.829 − 136.278) ÷ 157.664 = 4,769.25 ÷"
TER,core_fcf,450.4,"shares, FY2025 OI $650.1m and FCF $450.4m, on the 28 Jun 2026"
TER,core_fx,1,-
TER,core_fx_date,n.m.,-
TER,core_oi,650.1,"157.664m diluted shares, FY2025 OI $650.1m and FCF $450.4m, on the 28"
TER,core_ratio,1,-
TER,core_shares_diluted,157.664,"math At $389.39 (5 Aug 2026 close), 157.664m diluted shares, FY2025 OI"
TER,core_unit,m,-
TER,past_reason,21.5% ROCE,Worst ROCE 21.5%
TER,sf_reason,buybacks,v2 named the FY2026 repurchase record as the test
THULE.ST,core_cash,218,"less cash & equivalents 218 = EV 27,349 (all cash excess)"
THULE.ST,core_currency,SEK,-
THULE.ST,core_debt_eq,4274,"P = (7 × 1,640 − 4,274) ÷ 107.838162"
THULE.ST,core_fcf,784,"23,293 ÷ 784"
THULE.ST,core_fcf_basis,FY2025 CFO − capex,-
THULE.ST,core_fx,1,-
THULE.ST,core_fx_date,n.m.,-
THULE.ST,core_oi,1640,"27,567 ÷ 1,640"
THULE.ST,core_oi_basis,FY2025 reported,-
THULE.ST,core_period,FY2025,-
THULE.ST,core_ratio,1,-
THULE.ST,core_shares_diluted,107.838162,"shares 107,838,162, single class"
THULE.ST,core_unit,m,-
TKA.DE,future_reason,2+ forces,Tally = 2 strong
TKA.DE,past_reason,losses,Worst-of-four 10y normalized ROCE is −1.2%
TKA.DE,sf_reason,compensation,P17 hard strike: CEO Miguel López's FY2024/25 total (§162 AktG) o
TLX.DE,core_currency,EUR,-
TLX.DE,core_fcf,n.m.,"MCap/FCF = 29,102 ÷ 8,373 = 3.5× — n.m.: CFO for an insurer is dominated by premium inflow accreting reserves"
TLX.DE,core_fcf_basis,n.m. — insurer float,-
TLX.DE,core_fx,1,-
TLX.DE,core_fx_date,n.m.,-
TLX.DE,core_oi,n.m.,"(no-cash-excess) — n.m., NCI at book (Appendix C)"
TLX.DE,core_oi_basis,n.m. — substitution rule (insurer; P/B anchor),-
TLX.DE,core_ratio,1,-
TLX.DE,core_shares_diluted,258.228991,"shares outstanding 258,228,991; MCap €29,102m"
TLX.DE,core_unit,m,-
TLX.DE,future_reason,2+ forces,"Forces: customer power STRONG (annual renewal, negligible switching c"
TLX.DE,printed_ev_oi,n.m.,"(no-cash-excess) — n.m., NCI at book (Appendix C)"
TLX.DE,printed_ev_oi_all_cash,n.m.,"(no-cash-excess) — n.m., NCI at book (Appendix C)"
TLX.DE,printed_mcap_fcf,n.m.,"MCap/FCF = 29,102 ÷ 8,373 = 3.5× — n.m.: CFO for an insurer is dominated by premium inflow accreting reserves"
TRI,core_cash,577,cash & equivalents $577m
TRI,core_currency,USD,-
TRI,core_debt_eq,3222,"EV/OI leg, no-cash bound: (14,924 − 3,182 − 40) ÷ 438.6"
TRI,core_fcf,2017,"FY2025 OI $2,132m, FY2025 FCF $2,017m"
TRI,core_fcf_basis,FY2025 CFO − capex,-
TRI,core_fx,1,-
TRI,core_fx_date,n.m.,-
TRI,core_oi,2132,"FY2025 OI $2,132m, FY2025 FCF $2,017m"
TRI,core_oi_basis,FY2025 reported,-
TRI,core_period,FY2025; BS 2026-06-30,-
TRI,core_ratio,1,-
TRI,core_shares_diluted,438.6,Diluted shares 438.6M
TRI,core_unit,m,-
TRI,sf_reason,buybacks,A new NCIB filed and executed above ≈$115 restores the ADVERSE liveness conjunct
TRI.PA,core_cash,562.2,"- EV/OI leg, all-cash: P = (7 × 334.3 + 562.2 − 119.3 − 76.1 − 0.8) ÷"
TRI.PA,core_currency,EUR,-
TRI.PA,core_debt_eq,196.2,would be P = (25 × 334.3 + 562.2 − 196.2) ÷ 19.283 = €452.3. ## G.
TRI.PA,core_fcf,517.1,"audited year FY2025: OI €334.3m, FCF €517.1m, net income (group)"
TRI.PA,core_fx,1,-
TRI.PA,core_fx_date,n.m.,-
TRI.PA,core_oi,334.3,"Latest closed audited year FY2025: OI €334.3m, FCF €517.1m, net income"
TRI.PA,core_ratio,1,-
TRI.PA,core_shares_diluted,19.283,≤ 7 hold simultaneously. Diluted shares 19.283m (FY2025 weighted average).
TRI.PA,core_unit,m,-
TRI.PA,future_reason,2+ forces,supplier power STRONG
TRIP,future_reason,2+ forces,Forces: customer power STRONG (duopoly advertisers cutting meta spend
TRIP,past_reason,2.8% ROCE,Worst-of-four normalized ROCE 2.82%
TRIP,sf_reason,compensation,"0×, both reads → hard strike"
TRNS,past_reason,4.8% ROCE,Worst-of-four normalized ROCE 4.83%
TRNS,sf_reason,compensation,Comp: P17 hard strike
TROW,core_cash,4188.3,"/ 213.316 = $64.23; all-cash (13,700.7 + 4,188.3) / 213.316 = 17,889.0 /"
TROW,core_currency,USD,-
TROW,core_debt_eq,1620.9,"12.25×: (12.25 × 2,188.8 + 4,188.3 − 1,620.9) / 213.316 = $137.7; the"
TROW,core_fcf,1479.2,"→ MCap $22,317.1M. FY2025 OI 2,188.8; FCF 1,479.2. BV / TBV at 6/30/26:"
TROW,core_fx,1,-
TROW,core_fx_date,n.m.,-
TROW,core_oi,2188.8,"213.316M → MCap $22,317.1M. FY2025 OI 2,188.8; FCF 1,479.2. BV / TBV at"
TROW,core_ratio,1,-
TROW,core_shares_diluted,213.316,"Price $104.62 (2 Oct 2026 close); shares 213.316M → MCap $22,317.1M. FY2025"
TROW,core_unit,m,-
TROW,sf_reason,buybacks,Capital allocation CAUTION: live repurchases average $94
TRS,future_reason,moat eroding,"costs from tooling and requalification, eroding: a business with a real one d"
TRS,past_reason,4.1% ROCE,Worst-of-four ROCE ≈ 4.1%
TRS,sf_reason,flag pair,Two independent flags → FAIL
TSLA,future_reason,moat eroding,Eroding moat amid unfavourable forces
TSLA,past_reason,ROCE decline,69% from the 2022 peak across three consecutive down years
TSLA,sf_reason,compensation,FAIL — strike: compensation & ownership
TTWO,future_reason,customer conc.,Customer breadth FAIL: five largest customers = 80
TTWO,past_reason,losses,Worst-of-four ROCE −23.1%
TTWO,sf_reason,compensation,"FAIL — P17 hard strike, multiply corroborated"
TUI1.DE,future_reason,2+ forces,Tally 2 strong
TUI1.DE,past_reason,2.9% ROCE,Worst-of-four normalised ROCE 2.9%
TWLO,past_reason,losses,GAAP operating income is negative in nine of ten window years
TWLO,sf_reason,flag pair,Flag pair (P17 + P19) → SF FAIL
TXN,core_cash,7001,"leases 731 (31 Dec 2025), cash & STI 7,001, BV 18,007, TBV 13,363. -"
TXN,core_currency,USD,-
TXN,core_debt_eq,14783,"7 × 6,023 − 14,052 − 731) / 913 = $29.99; all-cash (7 × 6,023 + 7,001 − 14,052 − 731) / 913 = $37.65; width"
TXN,core_fcf,2603,"lines; FY2025 OI 6,023; FCF all-capex 2,603; FCF maintenance basis"
TXN,core_fx,1,-
TXN,core_fx_date,n.m.,-
TXN,core_oi,6023,"913m used for per-share lines; FY2025 OI 6,023; FCF all-capex 2,603; FCF"
TXN,core_ratio,1,-
TXN,core_shares_diluted,913,15 Jul 2026); diluted weighted FY2025 913m used for per-share lines;
TXN,core_unit,m,-
TXN,future_reason,customer conc.,Customer breadth FAILS: one end customer took 12% o
TXN,sf_reason,distributions,"5bn in FY2025 at 28×, $185m in H1 2026), but dividends plus buybacks exceeded all-capex FCF by $3"
U,future_reason,forces: suppliers,supplier/platform power STRONG
U,past_reason,losses,worst-of-four normalized ROCE is −19.0%
U,sf_reason,compensation,P17 hard strike: CEO Bromberg's FY2024 total was $52
UAA,future_reason,2+ forces,Forces: customer power STRONG (wholesale retailers with private label
UAA,past_reason,3.6% ROCE,Worst-of-four normalized ROCE 3.62%
UAA,sf_reason,compensation,P17 hard strike
UFI,future_reason,2+ forces,"Forces: customer power STRONG (commodity-adjacent yarn, brands and kn"
UFI,past_reason,1.8% ROCE,on a zero-NIBCL floor ~1.8–2.0%
UFI,sf_reason,compensation,e-than-token pay against no owner earnings is the hard strike
UN0.DE,future_reason,supplier conc.,Breadth FAILS on the supplier side: the ef
UN0.DE,past_reason,losses,"half of the window was also poor — net losses in 2016 (−€3,234m), 2017 (−€538m) and 2"
UN0.DE,sf_reason,RPT,The two flags are: (1) related-party dealings with the controlling holder of a size no
UNH,future_reason,customer conc.,Customer breadth FAIL: CMS alone is 44% of revenue
UNH,past_reason,ROCE decline,1% — a sustained multi-year decline that forces a downgrade regardless of level — and
UNH,sf_reason,buybacks,at ~3–4× the framework limit price
UPST,future_reason,customer conc.,Breadth: customers FAIL — top three partners = 83% of
UPST,past_reason,losses,Worst-of-four normalized ROCE (FY2021–25) is −9.70%
UPST,sf_reason,flag pair,FAIL — flag pair
V,future_reason,customer conc.,Breadth: customer side FAIL — one client at 11% of net re
V,sf_reason,compensation,FAIL — strike: executive compensation
VC,core_cash,648,"price $104.33, 5 Aug 2026; 26.70m shares; 30 Jun 2026 BS — debt $434m, cash $648m, NCI $78m"
VC,core_currency,USD,-
VC,core_debt_eq,512,"price $104.33, 5 Aug 2026; 26.70m shares; 30 Jun 2026 BS — debt $434m, cash $648m, NCI $78m"
VC,core_fcf,277,MCap/FCF = 10.1× (FY2025 FCF $277m)
VC,core_fx,1,-
VC,core_fx_date,n.m.,-
VC,core_oi,322,EV/OI = 10.24× / 8.23× (FY2025 OI $322m)
VC,core_oi_basis,FY2025 reported,-
VC,core_period,FY2025; BS 2026-06-30,-
VC,core_ratio,1,-
VC,core_shares_diluted,26.70,"price $104.33, 5 Aug 2026; 26.70m shares; 30 Jun 2026 BS — debt $434m, cash $648m, NCI $78m"
VC,core_unit,m,-
VC,future_reason,customer conc.,Breadth FAIL on the customer limb: Ford 23
VC,sf_reason,compensation,"9m target converts the flag to a hard strike — retrieval owed, INDETERMINATE until then"
VOW3.DE,future_reason,2+ forces,But three of four forces are STRONG (unfavourable): customer power (low swi
VOW3.DE,past_reason,3.4% ROCE,Worst-of-four normalized ROCE runs ~3.4%
VOW3.DE,sf_reason,control,What fails is control-and-allocation
VSURE.ST,past_reason,1.4% ROCE,Worst-of-four normalized ROCE 1.4%
VSURE.ST,px_unit,EUR,"endpoint 2026-10-06: currency EUR, exchangeName STO, longName Verisure plc, regularMarketPrice 8.308"
VSURE.ST,sf_reason,compensation,FAIL — P17 hard strike
WAY,past_reason,2.8% ROCE,Worst-of-four normalized ROCE 2.78%
WAY,sf_reason,compensation,"Breach on both reads, both years — hard strike"
WDAY,past_reason,losses,GAAP OI is negative in seven of ten years
WDAY,sf_reason,buybacks,The conduct: FY2026 repurchases of $2
WEIR.L,core_cash,386.6,"= £4.65. - EV/OI all-cash: (1,206.1 + 386.6) / 259.5 = £6.14. - EV/OI"
WEIR.L,core_currency,GBP,-
WEIR.L,core_debt_eq,1845.2,"7 × 435.9 − 1,835.2 − 10.0) / 259.5 = 1,206.1 / 259.5 = £4.65. - EV/OI all-cash: (1,206.1 + 386.6) / 259.5 ="
WEIR.L,core_fcf,248.2,"18.7× (all-cash). - MCap/FCF = 6,695.1 / 248.2 = 27.0×. - MCap/BV ="
WEIR.L,core_fx,1,-
WEIR.L,core_fx_date,n.m.,-
WEIR.L,core_oi,435.9,"math - Multiples: - EV/OI = 8,540.3 / 435.9 = 19.6× (no-cash) and"
WEIR.L,core_ratio,1,-
WEIR.L,core_shares_diluted,259.5,n.m. (TBV −78.1). - Trigger band (259.5m shares): - FCF leg: 8 ×
WEIR.L,core_unit,m,-
WEIR.L,past_reason,5.5% ROCE,Worst-of-four normalized ROCE is 5.5%
WEIR.L,sf_reason,acquisitions,"Micromine (EV £624m, about 20× forward EBITDA) and Townley (£111m) were bought in 2025 with borrowed money"
WEN,future_reason,moat eroding,"Moat Brand, eroding: systemwide sales −3"
WEN,past_reason,6.7% ROCE,Worst-of-four normalized average ROCE is 6.70%
WEN,sf_reason,distributions,"ell, corrected only in August 2026 by halving the dividend"
WHR,future_reason,customer conc.,Breadth: customer-side FAIL — Lowe's ≈15% of consolidated
WHR,past_reason,1.8% ROCE,Worst-of-four normalized ROCE 1.82%
WHR,sf_reason,compensation,ormalized — NI leg binds): breach on both reads → hard strike
WINA,core_cash,25.83,"$1,321.6m; total debt $62.73m; cash $25.83m; preferred and NCI nil;"
WINA,core_currency,USD,-
WINA,core_debt_eq,62.73,"capitalisation $1,321.6m; total debt $62.73m; cash $25.83m; preferred"
WINA,core_fcf,44.705,income $53.94m; FY2025 free cash flow $44.705m; diluted shares 3.685m
WINA,core_fx,1,-
WINA,core_fx_date,n.m.,-
WINA,core_oi,54.594,and NCI nil; FY2025 operating income $54.594m; TTM operating income
WINA,core_ratio,1,-
WINA,core_shares_diluted,3.685,"free cash flow $44.705m; diluted shares 3.685m (FY2025 weighted average,"
WINA,core_unit,m,-
WINA,sf_reason,compensation,9% — a hard strike
WISE.L,past_reason,36% ROE,normalized ROE ≈ 36% against the 10% ADEQUATE floor
WISE.L,sf_reason,flag pair,FAIL on a flag pair
WMT,core_cash,10.729,7.999 = $16.34; P_all-cash = (7 × 29.82 + 10.729 − 71.666 − 6.352) ÷ 7.999 =
WMT,core_currency,USD,-
WMT,core_debt_eq,78.018,7 × 29.82 − 71.666 − 6.352) ÷ 7.999 = $16.34; P_all-cash = (7 × 29.82 + 10.729 − 71.666 − 6.352) ÷ 7.999 =
WMT,core_fcf,14.92,more conservative. - MCap/FCF = 898.6 / 14.92 = 60.2× (≤8 → FAIL).
WMT,core_fx,1,-
WMT,core_fx_date,n.m.,-
WMT,core_oi,29.82,"- EV/OI, both variants = 965.9 / 29.82 = 32.4× (all-cash excess);"
WMT,core_ratio,1,-
WMT,core_shares_diluted,7999,"= 8 × FCF ÷ diluted shares = 8 × 14.92 ÷ 7.999 = $14.92. - EV/OI leg, both"
WMT,core_unit,bn,-
WMT,sf_reason,buybacks,Capital allocation: ADVERSE — clearly overpriced repurchases live in the trailing window (FY2026 all four re
WRBY,past_reason,losses,No positive year
WRBY,sf_reason,compensation,P17 hard strike: highest-paid FY2024 = CFO Miller $3
WTS,core_cash,347.9,/ 33.5 = $87.60; all-cash: (7 × 448.1 + 347.9 − 108.0 − 94.2) / 33.5 =
WTS,core_currency,USD,-
WTS,core_debt_eq,202.2,"at the current price: (363.07 × 33.5 + 202.2) / 7 ≈ $1,766m, 3.9× FY2025"
WTS,core_fcf,356.3,"EV all-cash 11,974.8. MCap/FCF 12,120.5 / 356.3 = 34.0× (threshold 8; FAIR"
WTS,core_fx,1,-
WTS,core_fx_date,n.m.,-
WTS,core_oi,448.1,"ceiling 14.0 — fails). EV/OI 12,322.7 / 448.1 = 27.5× no-cash; 11,974.8 /"
WTS,core_ratio,1,-
WTS,core_shares_diluted,33.5,23.4×. Trigger band. FCF leg: 8 × 356.3 / 33.5 = $85.09. EV/OI leg
WTS,core_unit,m,-
WTS,sf_reason,buybacks,"Capital allocation CAUTION: ten criterion-free repurchase years at 16–32× year FCF, sized to sterilise RSU"
WWD,past_reason,8.8% ROCE,Worst-of-four normalized ROCE is 8.8%
WWD,sf_reason,buybacks,"Capital allocation is ADVERSE: FY2023–FY2025 repurchases cleared 25× on all four reads, FY2026 buying ra"
XPEL,future_reason,supplier conc.,Breadth: FAIL on the supplier limb — the in
XPEL,past_reason,ROCE decline,"1%: three consecutive declines, and the cause is in the balance sheet — capital"
XPEL,sf_reason,compensation,Comp: P17 hard strike on primary data
XRAY,future_reason,customer conc.,Breadth FAILS on the customer side: Henry
XRAY,past_reason,losses,Worst-of-four normalized average ROCE −4.9%
XRAY,sf_reason,buybacks,77bn of repurchases across FY2016–FY2025 executed at 15–33× MCap/FC
ZAB.WA,core_cash,1079,"− 5,147.7)/997.42m = PLN 8.78; all-cash (+1,079.0) = PLN 9.86. Bounds: 8.78 /"
ZAB.WA,core_currency,PLN,-
ZAB.WA,core_debt_eq,5147.7,"19.94. EV/OI legs: no-cash (7 × 1,986.4 − 5,147.7)/997.42m = PLN 8.78;"
ZAB.WA,core_fcf,2485.5,"- Threshold-implied prices: FCF leg 8 × 2,485.5/997.42m = PLN 19.94. EV/OI"
ZAB.WA,core_fx,1,-
ZAB.WA,core_fx_date,n.m.,-
ZAB.WA,core_oi,1986.4,"= PLN 19.94. EV/OI legs: no-cash (7 × 1,986.4 − 5,147.7)/997.42m = PLN"
ZAB.WA,core_ratio,1,-
ZAB.WA,core_shares_diluted,997.42,"prices: FCF leg 8 × 2,485.5/997.42m = PLN 19.94. EV/OI legs:"
ZAB.WA,core_unit,m,-
ZAB.WA,past_reason,leverage,WEAK (P4 — leverage breach
ZBRA,core_cash,157,"− 2,776)/47.31 = $68.27; ac (6,006 + 157 − 2,776)/47.31 = $71.59 —"
ZBRA,core_currency,USD,-
ZBRA,core_debt_eq,2776,"legs at 7 × 858 = 6,006: nc (6,006 − 2,776)/47.31 = $68.27; ac (6,006"
ZBRA,core_fcf,831,26.0×/26.2×. MCap/FCF 21.4× (FY2025 FCF 831); ≈17.8× on guided FY2026
ZBRA,core_fx,1,-
ZBRA,core_fx_date,n.m.,-
ZBRA,core_oi,858,"EV 20,430 ac / 20,587 nc. EV/OI on TTM OI 858: 23.8× ac / 24.0× nc (v1:"
ZBRA,core_ratio,1,-
ZBRA,core_shares_diluted,47.31,"F. Valuation math Price $376.49 · shares 47.31m · MCap $17.81bn. EV 20,430"
ZBRA,core_unit,m,-
ZBRA,future_reason,customer conc.,The breadth FAIL is unchanged and could not ch
ZBRA,sf_reason,buybacks,$568m of repurchases in H1 2026 — ≈$1
ZIP,future_reason,2+ forces,Forces: all four called STRONG (zero-switching-cost per-job buyers
ZIP,past_reason,7.6% ROCE,Worst-of-four normalized ROCE 7.6%
ZIP,sf_reason,compensation,54k (3y-normalized read) — breach on both reads = hard strike
ZIP.AX,future_reason,supplier conc.,"Restated, and the supplier-breadth failure is sharper"
ZIP.AX,past_reason,losses,worst-of-four ROCE −14.1%
ZIP.AX,sf_reason,buybacks,FAIL — repurchase limb alone
ZM,future_reason,forces: substitutes,substitutes STRONG
ZM,past_reason,9.9% ROCE,Worst-of-four normalized ROCE is 9.9%
ZM,sf_reason,buybacks,Buybacks strike twice
```
