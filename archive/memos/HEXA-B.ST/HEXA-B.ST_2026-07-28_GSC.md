---
ticker: HEXA-B.ST
company: Hexagon AB (publ)
exchange: Nasdaq Stockholm
currency: EUR (reporting) / SEK (quotation)
memo_date: 2026-07-28
memo_version: v2
model_version: v3.11.0
price_at_memo: SEK 85.54 (28 Jul 2026, 15:29 UTC); EUR/SEK 11.0338
mcap_at_memo: SEK 231.4bn ≈ EUR 20,974m
verdict: AVOID
quality_past: WEAK
quality_future: ADEQUATE
sf: FAIL
cheapness: EXPENSIVE
window: "FY2016–FY2025 (10y); P19 tranche-years FY2020–FY2023"
trigger_band: "provisional ≈ SEK 6.2 (EV/OI no-cash) / SEK 14.2 (all-cash) on FY25 continuing reported OI — basis not clean until the Q2 2026 interim"
next_review: "Q2 2026 interim, 29 July 2026 08:00 CET — first post-Octave basis; re-base Past and Cheapness then"
position: —
---

# HEXA-B.ST — Hexagon AB: GSC Memo

## 1. Verdict

| Gate | Result | Change vs v1 |
|---|---|---|
| Understanding | **PASS** | — |
| Quality — past | **WEAK** | — (basis still provisional) |
| Quality — future | **ADEQUATE** | — |
| Shareholder-friendliness | **FAIL** (P19 hard strike) | strike re-derived on price |
| Cheapness | **EXPENSIVE** | price +3.8% |
| **FINAL** | **AVOID** | **unchanged** |

**Narrow scope.** This is the shareholder-friendliness re-test the register queue asked for, not a re-derivation of the name. Hexagon publishes its Q2 2026 interim tomorrow morning, 29 July at 08:00 CET — the first clean post-Octave basis, which v1 named as the event that makes the Past and Cheapness arithmetic honest. Nothing in this version touches those gates, and a fuller pass belongs after tomorrow's numbers.

On the queue question: the strike survives. v1 struck on sterilisation being price-independent, and it no longer is — it flags, and escalates only where the sterilising year breaches 14× EV/OI or 16× MCap/FCF. v1 recorded the cash consideration per tranche as undisclosed and therefore the multiples as not computable, which under the old rule did not matter and under the new one decides everything. The share counts are disclosed, so the fallback applies: test each tranche-year across its full trading range. All four clear the line at every price they touched. Even valuing Hexagon at market capitalisation alone — no debt added, which flatters a company carrying EUR 2.8–4.1bn of it — the cheapest day of each year reads 14.2×, 25.4×, 18.6× and 16.3× against a 14× line. Add the debt and the 2020 trough goes to 17.7×. The finding is robust, not indeterminate, and it strikes twice over: sterilisation escalates, and four flagged tranche-years independently trip the repetition limb.

The verdict was never in doubt — Past is WEAK on its own — but the SF column is now correct rather than merely right.

## 2. Understanding

Unchanged from v1. **PASS.**

## 3. Quality — past record

Unchanged from v1 and deliberately not revisited: worst-of-four ROCE 9.25% against the 10% floor, FCFROCE 7.50% against 8%, and a sustained decline from 11.4% to 6.4% that forces the downgrade regardless of level. The clean post-separation capital base arrives tomorrow. **WEAK.**

## 4. Quality — future

Unchanged from v1: breadth passes both legs at 0.7% largest customer, one strong force in substitutes, switching-cost moat, stable. **ADEQUATE.**

## 5. Shareholder-friendliness

Compensation clean at 1.02% of the 5% line, related-party dealings clean, acquisition audit INDETERMINATE on undisclosed target profitability. The buyback strike is re-derived below on price rather than purpose and holds on two independent limbs. Redemption still fails — limb (a) absent, limb (c) only partial with the strike-era chair still in post. **FAIL.**

## 6. Price

| Basis for OI | EV/OI (no-cash) | EV/OI (all-cash) |
|---|---|---|
| FY2025 continuing reported 692.8 *(binding)* | **35.1×** | **32.2×** |
| FY2025 adjusted EBIT1 1,072.5 *(reference only)* | 22.7× | 20.8× |
| FY2025 group reported 924.4 *(mismatched to price)* | 26.3× | 24.2× |

**EXPENSIVE**, provisional. MCap/FCF remains not computable — no continuing-operations cash-flow statement exists yet. Band on the binding basis is **SEK 6.2 on the no-cash EV bound and SEK 14.2 on the all-cash bound**; v1 printed only the latter and labelled it the conservative variant, which it is not — see C. Both are moot until tomorrow.

## 7. Risks & thesis-breakers

Unchanged from v1: Waygate at an undisclosed multiple, a smaller and less diversified post-separation group, low-end substitution in Geosystems, AEON unpriced, and Melker Schörling's 42.6% of votes with the strike-era CEO now chairing.

## 8. Flip conditions & next review

Unchanged and double-locked. Past needs worst-of-four ROCE above 10% on a clean post-separation base — plausible, since the distributed businesses carried disproportionate goodwill, but it needs two or three audited years. The P19 strike needs all three redemption limbs, and the chair who presided over the tranche-years remains. **Next review: tomorrow's Q2 2026 interim**, which re-bases Past and Cheapness; then the FY2026 annual report for Waygate.

*Framework output, not investment advice.*

---

# APPENDIX

## A. Sources & data gaps

**New this version.** Yahoo Finance chart API: HEXA-B.ST current price and daily history 2019–2026, EURSEK daily over the same span, used to build the fiscal-year trading ranges in euro terms for the tranche-year test. One exploratory search establishing that the Q2 2026 interim is scheduled for 29 July 2026 at 08:00 CET — i.e. it has **not** yet been published, so no results delta exists to incorporate and v1's provisional basis stands unchanged. All v1 sources carry forward.

**Gap partially closed.** v1 logged per-tranche cash consideration as undisclosed and the multiples as not computable. The cash is still undisclosed, but the finding no longer depends on it: share counts are disclosed and the range test resolves the question without a derived price. Recorded as closed-by-fallback rather than closed-by-retrieval.

**Gaps carried forward.** (1) Per-tranche repurchase cash — AR2020–AR2023 cash-flow statements would give it; not needed for the finding. (2) Continuing-operations cash-flow statement — arrives tomorrow. (3) Waygate, Infor EAM and ETQ pre-deal profitability — undisclosed, INDETERMINATE. (4) Post-spin equity is derived, not sourced.

**Search budget (P14, REVIEW ~2 exploratory).** One exploratory search. Price and FX series are directed retrieval, uncounted per §4. Within budget.

## B. Financial record

B1–B3 unchanged from v1. No new fiscal year has closed and the Q2 interim is not yet out. Denominators used below are B1 as filed: operating income 787.0 (FY2020), 1,009.8 (FY2021), 1,286.7 (FY2022), 1,216.0 (FY2023); derived FCF 991.2, 932.0, 820.0, 853.6; gross interest-bearing debt derived as capital employed less equity — 2,773.3, 3,012.9, 3,928.0, 4,140.3.

## C. Calculation notes

**Trigger-band variant labelling.** v1 printed a single band of SEK 14.27 and called it the conservative EV variant, using the formula that adds cash and short-term investments back. Adding cash back produces the *lower* enterprise value and therefore the *higher* implied price — that is the all-cash-excess variant, the flattering one. The genuinely conservative no-cash bound is SEK 6.17. The two are printed together above as the labelled-range rule requires. This is the cash-add-back self-contradiction already logged as an open MODEL-mode item; v1 followed the formula as written and mislabelled the result, and both readings are moot here at a 4–12× miss.

**Tranche-year test without a derived price.** Where the repurchase count cannot be derived the framework tests the year across its full trading range and accepts the finding only if it holds at every price. Here the inverse holds — counts are disclosed, consideration is not — and the same fallback is the right instrument. Two deliberate conservatisms in the company's favour: daily lows in SEK are converted at that day's EUR/SEK rather than a year-average rate, and market capitalisation is used as the enterprise-value floor with no debt added, which understates every multiple. The finding survives both.

**Bias check.** Live: **consistency**. v1's strike was correct under the rule then in force and the temptation was to leave the SF column alone, since the AVOID verdict rests independently on Past being WEAK and no amount of P19 work can change the answer. That is precisely the reasoning that leaves a wrong derivation sitting in the register — the queue exists because the rule changed, not because the verdict was in doubt. Handled by running the range test on its merits and by being explicit that this version is scoped to one gate. **Miscontrast** noted and resisted in the other direction: EUR 48–92m of annual repurchases is small against a EUR 21bn company, but size enters only through de-minimis, which is run below and which sterilisation does not reach. No judgment in this memo is born of a bias.

## D. Future-performance worksheet

Unchanged from v1. Customer power WEAK, supplier power WEAK, substitutes **STRONG**, new entrants WEAK; tally 1 strong, contained. Switching-cost moat, stable. Market growth MIXED.

## E. Shareholder-friendliness evidence

### 1. Compensation & ownership — clean, unchanged

CEO Anders Svensson EUR 6,302.9k against a 5% line of EUR 30.87m on the lower of net income attributable to parent (617.4) and levered FCF (851.7) — **1.02%**, no strike; ≈US$7.3m against the ≈US$40m trigger. Chair Ola Rollén EUR 254.4k ≈ US$295k against the US$666k floor-default stop. The CEO figure includes EUR 4,518.2k of make-whole on a July 2025 start; the fattest number is used regardless and both readings pass. Melker Schörling AB at 21.5% of capital and 42.6% of votes remains a documented caveat, unpaired.

### 2. Related-party transactions — clean, unchanged

AR2025 note 32 discloses no significant related-party transactions; associate balances immaterial. The PwC fee rise to EUR 17.4m from 6.9m is attributed to the Octave separation. **No flag.**

### 3. Buybacks — **P19 HARD STRIKE (sterilisation escalated; repetition independently)**

**Purpose — unchanged and unambiguous.** All 21,100,000 Class B shares held at 31 December 2025 were repurchased for one disclosed purpose. AR2025: *"The purpose of the repurchase is to ensure Hexagon's undertakings in respect of the long-term incentive programme."* The AGM authorisation cites capital structure, acquisition financing and incentive hedging — never worth. Sterilisation flag attaches to each year, at any size.

**Escalation test — range basis.** Consideration per tranche is undisclosed, so each year is tested across its full trading range. Market capitalisation is used as the enterprise-value floor; the debt-inclusive reads are shown alongside.

| FY | Shares repurchased | Year low (EUR) | MCap at low | **MCap/OI at low** | MCap/OI at avg | EV/OI at low, debt included |
|---|---|---|---|---|---|---|
| 2020 | 4,522,000 | 4.34 | 11,159 | **14.2×** | 25.7× | 17.7× |
| 2021 | 4,828,000 | 9.85 | 25,682 | **25.4×** | 32.3× | 28.4× |
| 2022 | 6,450,000 | 8.87 | 23,997 | **18.6×** | 23.4× | 21.7× |
| 2023 | 5,300,000 | 7.31 | 19,793 | **16.3×** | 21.6× | 19.7× |

Share counts are post-split; 2020's 646,000 pre-split shares are stated on the 7:1 basis. Every year clears the 14× flag line at its cheapest day, before any debt is added, and FY2020 — the tightest — clears it by 1.4% on the floor read and by 26% once the EUR 2,773m of debt Hexagon actually carried is included. **The finding is robust across every price in every tranche-year: sterilisation escalates to a hard strike.**

**Repetition — independent second route.** Four flagged tranche-years inside the window, none of which approaches the rescue lines of 7× EV/OI or 8× MCap/FCF. The v3.9.0 repetition limb strikes on two. The strike therefore does not depend on the sterilisation reading at all.

**Four-denominator de-minimis test (register requirement), bounded.** Consideration is undisclosed, so each year is tested at its **maximum possible** cash — shares repurchased at that year's high. Relief requires falling below 5% of all four denominators.

| FY | Max possible cash (EURm) | % year FCF | % 3y-norm FCF | % year OI | % 3y-norm OI | Result |
|---|---|---|---|---|---|---|
| 2020 | 48.8 | 4.92% | 6.50% | 6.20% | 5.62% | **not de-minimis** |
| 2021 | 72.4 | 7.76% | 8.26% | 7.17% | 8.07% | **not de-minimis** |
| 2022 | 92.3 | 11.25% | 10.09% | 7.17% | 8.98% | **not de-minimis** |
| 2023 | 61.9 | 7.26% | 7.13% | 5.09% | 5.29% | **not de-minimis** |

Every year breaches on at least three denominators at the most favourable possible spend, so no year qualifies however the actual consideration fell. FY2020 is the only year clearing any leg — 4.92% of that year's free cash flow — and fails the other three. De-minimis does not reach sterilisation in any case; the test is run because the repetition limb is size-sensitive and it is not relieved either.

**Worth check and redemption — unchanged.** The worth check clears flags, never hard strikes, and v3.11.0 has since made explicit that a downgraded strike cannot be cleared by it either. Redemption fails: **(a)** no worth-referenced criterion in any mandate; **(b)** 2024 and 2025 saw no repurchases, but with a purpose that was never worth-referenced, non-use is not evidenced refusal — the treasury holding was simply adequate; **(c)** partial only, with the CEO turned over in July 2025 and the CFO in July 2026, but Ola Rollén — CEO through 2000–2022 and chair across every tranche-year — still in the chair, and the controlling holder unchanged. Partial satisfaction changes nothing.

### 4. Acquisition audit — triggered, INDETERMINATE, unchanged

Negative tangible book value triggers the audit. Waygate (USD 1.45bn on ~USD 630m of revenue, April 2026), Infor EAM and ETQ all lack disclosed pre-deal profitability. **INDETERMINATE** — heightened scrutiny and a named re-test at the FY2026 annual report, never a pair-completer. The FY2025 impairment of EUR 206.1m of overlapping technology from Septentrio and Geomagic remains corroborating evidence of allocation quality without being a finding.

### 5. Dividends & capital allocation — unchanged

DPS EUR 0.14 proposed for FY2025 against 0.07 in 2016; payout modest and consistent. Capital employed rose from 6,440 to 14,422 while reported operating earnings rose from 736 to 924 — retention at a 6–9% incremental return, which is the substance of the WEAK past verdict rather than a separate strike.

**Verdict: FAIL** — one hard strike on two independent limbs. Tests 1, 2 and 5 clean; acquisition audit indeterminate.

## F. Valuation math

**Current** (SEK 85.54, EUR/SEK 11.0338, both 28 Jul 2026; 2,705.478m diluted shares). MCap = **EUR 20,974m** (SEK 231.4bn). EV no-cash = 20,974 + 3,254.0 debt + 50.3 preferred + 32.0 NCI = **24,310**; all-cash-excess = − 1,978.1 = **22,332**.

Multiples are in §6. Every basis fails P8 by a factor of three to five, and the ranking is unchanged by the 3.8% price move.

**Trigger band**, FY2025 continuing reported OI of 692.8, both bounds printed:

| Leg | Implied price |
|---|---|
| EV/OI ≤ 7, no-cash EV | **SEK 6.17** |
| EV/OI ≤ 7, all-cash-excess EV | SEK 14.24 |

The strict all-pass line is the no-cash bound at SEK 6.17, **1,286% below today**. No P12 edge — reserved for Past = STRONG. Qualifier-implied prices, context only: 3 × BV/share ≈ SEK 148 reported, ≈ SEK 66 on derived post-spin equity. **The band remains provisional** — the denominator still contains Design & Engineering and the balance sheet still contains Octave. Register `Trigger band` and `Dist %` print `—` per §7.1.

Not held → no sell-flag line.

## G. Change log

- **v2 — 2026-07-28 — REVIEW under MODEL v3.11.0, scoped to the shareholder-friendliness gate.** Triggered by the register's v3.9.0 P19 queue, where HEXA-B sat as an SF-column item — the verdict cannot move while Past is WEAK. **Verdict AVOID unchanged; SF FAIL unchanged; no gate verdict moved.** v1's strike rested on sterilisation being price-independent, which v3.9.0 ended; it now flags and escalates only above 14× EV/OI or 16× MCap/FCF. v1 had logged per-tranche cash as undisclosed and the multiples as not computable — under the new rule that is decisive, so the §2·1C range fallback was run instead. **All four tranche-years breach at every price they touched**, using market capitalisation as an EV floor with no debt added: 14.2× (FY2020), 25.4× (FY2021), 18.6× (FY2022), 16.3× (FY2023) at the annual lows, and 17.7× for FY2020 once its EUR 2,773m of debt is included. Robust, not indeterminate. The v3.9.0 repetition limb strikes independently on four flagged tranche-years. Four-denominator de-minimis run per the register requirement, bounded at each year's maximum possible spend — none qualifies. **Q2 2026 confirmed not yet published**: it lands 29 July 2026 at 08:00 CET, so v1's provisional Past and Cheapness basis is unchanged and a re-base belongs to the next pass, tomorrow. **Correction:** v1 printed a single trigger band of SEK 14.27 labelled the conservative EV variant; the cash-add-back formula produces the all-cash-excess bound, and the conservative no-cash bound is SEK 6.17 — both now printed, and the underlying formula contradiction remains an open MODEL-mode item. Price refreshed to SEK 85.54.
- **v1 — 2026-07-24 — initial ANALYSE.** Verdict **AVOID** on two independent gates: Past **WEAK** (worst-of-four ROCE 9.25%, FCFROCE 7.50%, sustained decline 11.4% → 6.4%, ΔOI/share +1.78%) and SF **FAIL** (P19 dilution-sterilisation, then price-independent). Future ADEQUATE, Cheapness EXPENSIVE at 30.8–33.7× EV/OI. Basis flagged provisional pending the first post-Octave interim.

*Framework output, not investment advice.*
