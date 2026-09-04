# GSC Work Queue — TODO.md (v25 · 2026-09-04)

**Purpose.** The single work sink for the project: every future-work item any session surfaces — re-tests, rebuilds, backfills, corporate actions, queue seeds — routes **here**, never into the register's `## Open items` (routing per MODEL §7.1, v4.2.0). This file is *not* authoritative state: `_REGISTER.md` wins on state, `MODEL.md` on rules, memo appendices on per-name detail. Nothing here is a verdict or a recommendation. Framework ideas go to `queue/IDEAS.md`, not here.

**Ticker discipline.** Tickers are suggested keys for convenience; resolved and verified at run time per §7.1a (prior-check on company name + ISIN, never the key alone).

---

## ▶ Next up — external-idea intake, Cluseau Research "Buying the Buyback" (published 3 Sep 2026; queued 2026-09-04)

*Three ANALYSE seeds, user-directed to the top of the queue. Source is a paid third-party research note (tier-3 under §4): **nothing below is sourced financial data** — the "article hook" column restates the author's claims as claims, to be verified or discarded at ANALYSE, never carried into a memo as fact. The note also publishes price targets and position weights; neither is carried here or anywhere in the project. Prior-check per §7.1a run 2026-09-04 on company name against all 320 live register rows and every block in this file: **no collision** for any of the eight names the note mentions. Tickers are suggested keys, resolved and verified with ISIN at run time.*

| # | Key | Company | Sector | Treatment | Article hook (author's claim, unverified) |
|---|---|---|---|---|---|
| 1 | ~~`244920.KS`~~ | A Plus Asset Advisor Co., Ltd. | insurance brokerage (general agency), Korea | **DONE — v1 committed at register v284 (2026-09-04): AVOID on 3 gates, EXPENSIVE.** Ordinary lens confirmed (no §2·1A). Re-tests → named table below | founder-controlled (Kwak family), Align Partners activist stake, first-ever repurchase programme + dividend increase 2026; FSC commission caps as barrier to entry; non-core funeral business and medical-device stake |
| 2 | ~~`ABCA.PA`~~ | ABC arbitrage SA | statistical-arbitrage asset manager / proprietary trading, France | **DONE — v1 committed at register v285 (2026-09-04): AVOID (Future WEAK), FAIR.** §2·1A substitution applied cleanly, non-determinative (both lenses Past ADEQUATE) → instance logged under IDEAS A4. Re-tests → named table below | 31 consecutive profitable years since 1995; ~54% insider ownership; ~66% payout policy with minimum dividend; flagship fund at record YTD performance while share price lags |
| 3 | ~~`6626.T`~~ | SEMITEC Corporation | precision temperature sensors (thin-film thermistors), Japan | **DONE — v1 committed at register v286 (2026-09-04): WATCH, FAIR.** P19 SOUND (three completed programmes at 3–7× EV/OI); P20 active (pre-cycle capex/sales 4.80%); band ≈¥1,403. Re-tests → named table below. **Intake block closed: 1 WATCH, 2 AVOID.** | Ishizuka family ~44%; large net cash; 2023–24 repurchases 3.2%/2.1% then ~10%; peers Ohizumi and Shibaura acquired, leaving SEMITEC one of the last independents; ~80% overseas sales |

*Also named in the note as its own past trades, **not seeded** (all already re-rated 68–169% per the author; two are banks needing the §2·1A basis): Georgia Capital `CGEO.L` (investment holding — screened out by the standing re-seed rule), SE Holdings & Incubations `9478.T`, Modern Dental Group `3600.HK`, Bank of the Ryukyus `8399.T`, Juroku Financial Group `7380.T`. Add on request.*

---

## ⚠ Imminent & overdue — dated re-tests (as of 2026-08-28)

*(Also queued: a MODEL session on IDEAS A1 — the OI-line convention — user-scheduled 2026-08-18, **still not run**; requires a human in the loop and the exact phrase "commit model", so it cannot be executed unattended. A2–A7 stay parked.)*

**CLEARED at register v278 — seven re-tests executed 27–28 Aug, staged then blocked, recovered and committed 2026-08-31. Two verdicts moved:**

1. ~~**7936.T (ASICS) — Q2 FY2026 tanshin, 14 Aug 2026**~~ → **v3 committed. No art. 459 authorisation announced.** Both of the year's candidate slots (13 Feb, 14 Aug) have now passed unused; H1 treasury purchases ¥2m. CAUTION confidence 70% → 80%. WATCH held. ✓ *The v3 sourcing caveat is **withdrawn**: the 28 Aug pass retrieved ASICS's statutory 半期報告書 for the identical period, so every figure is primary and ties on all four §4 anchors. Also closed: H1 FY2025 cash flow via EDINET (**TTM FCF now ¥91,060m**), both buyback notices (**8,072,900 shares for ¥29,999,803,800** — confirming the derived ¥3,716 to the yen), and **FY2025 top pay at ¥419m**, carried as "above ¥400m" since v1.*
2. ~~**TRI (Thomson Reuters) — NCIB expiry, 18 Aug 2026**~~ → **v3 committed. The bid expired unrenewed.** No successor authorisation, no substitute mechanism, verified by two independent retrievals of the IR index. CAUTION confidence 70% → **87%** after a 28 Aug EDGAR sweep of every filing by the registrant in August returned no NCIB document. WATCH held. **New adverse alert: lease liabilities of $241m were retrieved from the Q2 6-K's XBRL notes, pulling the conviction line $116.04 → $115.49 and the band $27.23/$28.55 → $26.68/$28.00 — so the price now sits 9.3% below the line, not 10.8%.** The P17 trailing-3y NI leg is also computed rather than bounded (FY2023–25 sourced).
3. ~~**STMN.SW (Straumann) — H1-2026, 19 Aug 2026**~~ → **v3: VERDICT FLIPPED, WATCH → AVOID, SF PASS → FAIL.** The first pass concluded Straumann publishes no interim financial statements and held WATCH. **That was wrong.** The ad hoc results release is itself a ~30-page document carrying full IAS-34 condensed statements (balance sheet p.15, income statement p.16, cash flow pp.18–19, equity statement p.20, notes 1–12), at a hash-ID URL not guessable from the annual-report path and invisible on the EQS mirror that search surfaces first. They show **treasury purchases of CHF 69,328k in H1 2026** — 2.8× the CHF 24,559k spent in all of FY2025, and 4.2× the CHF 16,605k handed back to plans in the same half — taking the treasury balance from CHF 0.4m to CHF 53.2m, **with no purpose stated anywhere in the document** (two independent full-document searches). Both premises of the CAUTION are falsified: it is not plan-coverage scale, and the treasury account is not a 4,434-share pass-through. All three ADVERSE conjuncts now hold, and §2·1C makes an ADVERSE capital-allocation verdict an SF FAIL in itself. **Confidence ~72%**; the single dissent line is whether unexplained accumulation with no announced programme satisfies "the programme executing." Also new: **CEO transition announced 19 Aug — Christopher Norbye effective 1 Dec 2026**, Daniellot out end-Nov after seven years. Three §4 extraction conflicts resolved. Register: WATCH 68 → 67, AVOID 248 → 249.
4. ~~**ZIP.AX — FY2026 Appendix 4E, 20 Aug 2026**~~ → **v2 committed. ADVERSE held; AVOID on three gates.** Programme 2 executed at ~A$2.02 (materially better than Programme 1's A$2.86, credited) but still ~32× earnings knowable at execution; **a third A$50m programme was authorised on results day** for 14 Sep 2026 – 14 Sep 2027, price not fixed in advance. P17 flag INDETERMINATE — and the 28 Aug pass changed its direction: FY2026's profit gives the normalized read a positive comparator (cap A$3.34m), but the best available CEO figure, **A$3.99m**, breaches it. Secondary and undefined, so unresolved rather than cleared; v2's "lost its arithmetic" is withdrawn. Also closed: **ISIN AU0000218307** (two versions late), goodwill A$200.3m + intangibles A$54.9m so **TBV A$418.2m** is computable, NIBCL A$438.0m, the **A$120.9m buyback cash-flow line** confirming v2's two-programme reconstruction, and the convertible notes (retired June 2024, never an FY2026 item — strike it). Price A$3.05 → **A$2.58**, Dist +316% → +252%.
5. ~~**INTU — FY2026 results, 25 Aug 2026**~~ → **v2 committed. WATCH held, band $118.60–144.59 (+15%).** P19 re-test split: spending nearly doubled to $5,412m (+95%) at 24.4–31.3× EV/OI, but MCap/FCF at 16.5× keeps the conjunctive calibration unmet. **Now a one-limb CAUTION** (price only) — the siblings have two. Past re-derived on the rolled window: worst-of-four ROCE 15.7% → 16.2%. The 28 Aug pass **cut confidence 65% → 60%**: with FY2022–24 free cash flow sourced, the FY2023–25 normalized read — the governing knowable-at-execution basis — computes at **27.4×, above the calibration**, so three of four reads breach and the CAUTION survives on MCap/FCF at 23.4× alone, a 6% margin. It also resolved the CEO-comp extraction conflict with a cause ($36,845,552 SCT Total vs $36,835,552 CD&A recap excluding $10,000 other comp) and surfaced **a new severity-changing INDETERMINATE: founder-director Scott Cook at $1,300,000, all "other compensation", 1.9× the ordinary-seat stop where 2× is a hard strike.** The November proxy now carries two ways to fail SF.

6. ~~**HEXA-B.ST — Q2 2026 re-base, 29 Jul 2026**~~ → **v3 committed. SF FAIL → PASS; AVOID narrows from two gates to one (Past WEAK alone).** v2's P19 strike was a **pre-v4 mechanical sterilisation ladder, not a §2·1C·3 judgment** — re-run on the current test, conjunct (iii) fails outright: **no repurchases since 2023**, treasury frozen at **21,100,000 shares** across both reporting dates, and no purchase line in the H1 2026 cash flow. **Past cannot be re-based, and will not be until FY2027.** Hexagon restated the income statement and cash flow to continuing operations but **not the balance sheet** — the 31 Dec 2025 column is whole-group — so no post-Octave ROCE exists for any completed year and the first comparable pair is FY2027. Both v18 traps held: H1 operating earnings of 2,072.4 MEUR include a **+1,588.0 MEUR capital gain** (Q2-only 251.4 is the clean read), and the word "restated" appears nowhere in the report. Band **SEK 8.95 / 17.84** (99% wide), Dist **+470%**, price SEK 101.75. **EUR/SEK 11.1295 is an external input** — the company states no rate, so every EUR→SEK conversion in the memo is labelled input, not sourced.

7. ~~**GAP — Q2 FY2026, ~26 Aug 2026**~~ → **v2 committed. AVOID on two gates held.** No turnaround: the $676m operating income is **≈$259m ex the $417m IEEPA tariff credit — down ~11%** — on sales −2% and comps −1%; adjusted gross margin +20bp. The brand split corroborates Future WEAK rather than challenging it: Old Navy (>50% of sales) −4% and Athleta −12%, against Gap +10% and Banana Republic +3%. **P19 moves to CAUTION, a flag v1 did not carry**: $601m of buybacks in 26 weeks is **3.9× all of FY2025**, paid alongside $125m of dividends against **$261m of H1 free cash flow** (2.8×), at ~$23.48 with no published criterion — one flag, unpaired, so SF still PASS. **v1's chair-fee caveat is withdrawn** on superseded calibration (chair stop ≈$1.02m against Shattuck's $525,992; the 2026 proxy director table was retrieved in the primary). Band re-anchored on the 1 Aug balance sheet to **$5.76 / $12.62**; **Dist +65% — the narrowest in the batch**, and said so in the memo because price could plausibly arrive before quality does. **Open:** the Q2 10-Q is still unfiled — the Item 5 monthly buyback table converts the derived ~$23.48 into a disclosed average, and is days away.

**STILL OPEN:**

8. ~~**EA outside date 28 Sep 2026**~~ → **CLOSED at register v280.** Take-private by PIF / Silver Lake / Affinity Partners **completed 4 Aug 2026 at $210.00 cash/sh**; common stock ceased trading, delisted from Nasdaq [sourced: EA release 4 Aug 2026, `ea.com/news/ea-announces-completion-of-acquisition`; corroborated `pif.gov.sa`]. Row moved AVOID → DNAF terminal; not held, so no tax event.

9. **PYPL — full REVIEW owed: lapse branch fired 27–28 Aug 2026.** Stripe/Advent abandoned the pursuit [press-sourced: Bloomberg 27 Aug, Axios 28 Aug, Reuters 28 Aug; no 8-K or company statement located — same standing as the approach itself]. De-pinned price: **$53.66 close 28 Aug 2026 (−12.7%)** [sourced: Yahoo Finance]; $56.82 close 3 Sep [2026-09-04 run, stockanalysis]. **v14's "pre-bid low-$40s inside the all-cash band" premise is struck** — the price did not return there; whether ≈$54–57 sits inside CHEAP ≈$33.96–47.12 is a framework question owed at the REVIEW, not an inherited conclusion.

---

## P19 judgment re-test queue — MODEL v4.0.0 §2·1C·3

Tier 1 CLOSED 8/8 (2026-08-06; five flips to WATCH, three ADVERSE holds). **Remaining = Tier 2 mixed pairs** — a P19 re-read alone cannot flip these; the second leg must be tested too:

| Name | Second leg | Status |
|---|---|---|
| AAPL | P17 comp strike | Open — flip requires comp reform; FY2026 10-K ~Oct/Nov 2026, then Jan 2027 proxy |
| MA | P17 comp strike ($35.4m > stop) | Open — 2027 proxy (~Apr 2027) |
| DLG.MI | La Marzocco RPT pair | Open — FY2026 AR (~Mar 2027); hard dates Feb 2028 IPO right / Feb 2029 demerger right |
| PSH.L | Fee extraction | Open — FY2026 AR (~Feb 2027) or any fee change |

Tier 3 (context only, no queue action): WATCH-name P19 flags — INVE-B.ST, FIE.DE, ROG.SW, ULVR.L, KNIN.SW, AXFO.ST, LIFCO-B.ST; pair-risk if a second negative appears.

---

## Named re-tests & backfills — migrated from register `## Open items` 2026-08-18

*One line per name; detail lives in the memo appendices and row cells (they are authoritative). Dated items also appear in the calendar below.*

| Name | Owed | When / trigger |
|---|---|---|
| KSPI | **Three items closed at v3 (2026-09-01) — do not re-queue:** 1H26 repurchase count (737,578 ADS @ ₸38,461, interim note 14), 1H26 owners/NCI NI split (₸506,127m / ₸4,669m), and the "no interim cash-flow statement" claim (there is one — financial-information 6-K exhibit, not the earnings exhibit). **Still open:** FY2016–FY2020 audited rebuild (record-limited, liftable — v1 FY2019 equity anchor ₸295,622m proves pre-2020 statements exist; KASE filings / F-1); **FY2021–FY2022 total interest expense and capex** (new — would extend the operating-lens returns series from 3y to 5y; FY2023 20-F carries both); ISIN (never captured, three sessions); outside-director fees (INDETERMINATE, three sessions); interim intangibles split (PP&E+intangibles combined → TBV is a range); Hepsi Bank PPA once published | FY2026 20-F ~Mar 2027; rebuilds any time (no web dependency on results) |
| 244920.KS | **Record-limited 5y (FY2021–25, S&P via stockanalysis) — FY2015–FY2020 rebuild from DART 사업보고서/감사보고서 (statements exist; DART, KIND and `aplusga.com` all bot-blocked from the sandbox 2026-09-04, so the §4 tier-2 acceptance test was never run — first touch with primary access must tie out revenue/OI/equity/NFP for FY2025 + one earlier year before anything else).** Also owed: FY2025 and FY2026 top-pay table (P17 strike rests on a press quotation of the FY2024 report — ≈₩985m); RPT note; carrier-level commission split (Future breadth call); composition of ₩145bn "other" liabilities (NIBCL call); subject of the FY2022 ₩82bn disposal gain; FY2023 ₩33.5bn capex; dividend history FY2021–24 (aggregator conflict); ISIN; buyback completion count and average price (trust to 13 Jan 2027) | FY2026 business report (~Mar 2027); rebuild any time primary access exists |
| 6626.T | **Record-limited 5y (FY3/22–26) — FY3/2017–FY3/2021 rebuild from the yūhōs on the kabupro EDINET mirror** (`kabupro.jp/edp/<date>/S100G70M|S100DHHX|S100AOEY|S1007WRV|S1009SF5.pdf` — FY3/19, FY3/18, FY3/17 reports and the FY3/16 & FY3/15 corrections; OI, capex, NIBCL, cash per year; would test whether w-o-4 ROCE 14.6% holds across the 2016–21 cycle); **P17 top-pay** (bounded ≤ ¥99.9m vs ¥84m P20 fiscal-year cap — ask IR or wait for a ≥ ¥100m disclosure); Q1 FY3/27 balance sheet for EV refresh (primary-interim-debt rule); **the Future call** — customer force WEAK on checklist vs STRONG on observed concessions is the memo's stated dissent line; re-argue on the FY3/27 Vision-successor plan; treasury disposition (1.78m shares, 15.6%, uncancelled); any new buyback after 24 Mar 2026 | Q2 FY3/27 tanshin ~Nov 2026; FY3/27 yūhō ~Jun 2027; rebuild any time |
| ABCA.PA | **P17 highest-paid employee undisclosed** (CEO €0.41m passes at 0.36×; cap €1.13m; a senior quant could exceed it — ask IR / FY2026 AFR); **FY2016–FY2020 NI and equity** from the archived AFRs (all on the company site) for the exact Σ NI ÷ Σ equity beginning-variant and a 10y EPS/BV growth read (only company ROE is 10y today); AFR 2025 pp. 39–160 unread — financial-instrument risk note (leverage at Quartys, counterparties), treasury-share movements, auditors' report; 2027 AGM scrip-dividend resolution and take-up; H1-2026 (22 Sep 2026) Momentum 2028 cost line vs plan and AUM | 22 Sep 2026 interim; FY2026 AFR ~Apr 2027 |
| 7213.T | P17 severity-changing INDETERMINATE (thresholds ¥58.9m/¥76.5m vs ¥49.8m six-director avg — a disclosed top total above either read pairs → SF FAIL, 3-gate AVOID); ISIN; FY3/27 Q1 BS; buyback count post 18-Jun-2026 | next touch / yūhō |
| APTV | FY2016–FY2018 window extension (record-limited: FY2019–FY2025 = 7y, caps Past at ADEQUATE; note the pre-Dec-2017 perimeter includes Delphi Technologies, so a true 10y Aptiv-perimeter window first exists at FY2027); continuing-ops FY2025 OI (Q2-26 10-Q Note 21) for a genuine TTM band base; RPT note, outside-director fees, insider ownership — all INDETERMINATE | FY2026 10-K ~Feb 2027 + 2027 proxy |
| 0700.HK | FY2016–17 statements + FY2018–20 CFO rebuild; 2025 AR emoluments note resolves P17 INDETERMINATE (>US$40m top pay pairs → SF FAIL) | FY2026 AR ~Mar 2027 |
| KEX | FY2016–FY2020 balance sheets + 31-Dec-2020 BS → 10y window rebuild (lifts the record-limited cap; beg-of-period variants currently run 4y); backvaluing worksheet once the prior cycle is in the record; FY2022/FY2024 buyback tranche prices (unmeasured, P19) | FY2026 10-K ~Feb 2027 |
| LULU | FY2016–FY2020 window rebuild (lifts the 5y record-limited cap set at v1, previously unrouted; beg-of-period variants run 4y); O'Neill comp package (P17) | FY2026 10-K ~Mar 2027 / 2027 proxy |
| ZBRA | P19 live ADVERSE path: FY26 repurchases > FY26 FCF on rising leverage → SF FAIL (2-gate AVOID, removes fulfilment-distributor flip path); H1 avg price INDETERMINATE | FY2026 10-K ~Feb 2027 |
| NET | $1,293.3m converts current at 30-Jun-26 — settlement/refinance path; ex-restructuring loss-margin trend | Q3 2026 ~Nov |
| BKNG | P15 supplier look-through (Google share of $8,186m marketing) decides Future; App. D re-run on the P16 binary schema (v1 used a non-P16 LOW/MED/HIGH five-force) | FY2026 10-K ~Feb 2027 |
| SW.PA | Band disappears on guided FY26 margin (7×OI < debt+leases+NCI — DEC.PA case); P4 + P19 re-test; Bellon coordination-agreement renewal; P17 bounded→measure at URD-2026 | results 23 Oct 2026 |
| SIE.DE | Past re-test under the captive-finance basis once IDEAS A2 is decided; Healthineers spin vote forces full quality re-base | FY2026 ~Dec / AGM Feb 2027 |
| 6758.T | Restated-comparative P20 re-run; FYE3/25 continuing FCF from the 20-F equity note; FYE3/19–23 repurchase counts INDETERMINATE; H1 ¥500bn-facility re-test | H1 FY3/27, 10 Nov 2026 |
| SOON.SW | Successor-programme watch (72% undrawn, expired Apr-25); Sennheiser close + pre-deal OI; chair comp; P4 one decline from firing | H1 FY26/27 ~Nov 2026 |
| SU.PA | CMD deck primary retrieval (€2.5–3.5bn envelope is tier-3); Cognite/AiDASH audits; FY23/24 counts; H1 lease liability | next touch |
| TER | Q3 10-Q execution read (~Oct); FY2026 10-K full-year P19; insider-sale volume vs P17 "most of their shares"; MultiLane audit | Oct 2026 / 10-K |
| WMT | 10-K "no expiration" sentence verbatim; TTM FCF (Q1 capex); Q2 FY27 date verify; P17 rests on one-time inducement grant — lapse at 2027 proxy + CAUTION re-read → possible SF PASS | Q2 FY27 / 2027 proxy |
| NOLA-B.ST | Flip is one dated event: FY2026 FCF > ≈SEK 295m clears the P17 year read → WATCH; CEO-transition severance is the numerator risk; ISIN n/a after 8 sources | FY2026 AR ~Apr 2027 |
| WISE.L | £405m tranche price/volume + trust/treasury split vs stated 40/60; Class B sunset re-test (Articles/2025 circular/20-F); highest-paid employee; RPT note; LSE line refresh | H1 FY2027 ~Nov 2026 |
| LR.PA | All acquisition audits INDETERMINATE (Avtron the only priced deal); FY16–22/FY24 repurchase prices; chair-seat norm survey | URD 2026 ~Apr 2027 |
| SIKA.SW | Parex/MBCC/Finja/Akkim audits (MBCC statutory accounts via Bundesanzeiger not yet attempted); **P4 live — 3rd consecutive decline at FY2026 → Past WEAK independently of price** | FY2026 AR |
| SGO.PA | CEO FY2025 comp (URD French-only); FY2020–23 purchased-share counts; CSR/Fosroc/Ovniver audits; **re-verdict risk under IDEAS A1** | FY2026 ~Feb 2027 |
| DG.PA (VINCI) | Cobra IS / Gatwick / 2024 airports / FM Conway audits | URD 2026 ~Feb 2027 |
| EL.PA | FY2020 tranche purpose; FY2024 execution count/price; GrandVision FY2017 OI; Supreme audit | URD 2026 ~Mar 2027 |
| DEC.PA | APN Outdoor >20× strike INDETERMINATE (FY2015–17 statutory EBIT unretrievable — delisted) | if source surfaces |
| CRCT | FY2025 SCT retrieval — equity grants above ≈$2.5m breach both reads → **WATCH turns AVOID** | FY2026 10-K ~Mar 2027 |
| CRI | FY2016–24 repurchase tranche pricing (a third of the company retired while OI fell 71%) — bad execution → CAUTION, pairs with standing P17 flag → SF FAIL | next touch |
| NGVT | P17 INDETERMINATE, ceilings straddle a typical package — live pair risk with P19 CAUTION | FY2026 10-K |
| WINA | Primary SCT tie-out (strike rests on secondary figure at 1.2% margin) | next touch |
| VC · UPST | FY2025 SCT retrieval converts flag → strike | next touch |
| KVYO | Exact FY2025 SCT (flag margin ≈6–10% — could clear → P19 flag stands alone → **SF flips PASS**); Shopify RPT terms | next touch |
| TENB | FY2026 SCT re-read (3y P17 line rises with FCF); ISIN verify | FY2026 10-K |
| OPEN | SCT allocation of the $741m CEO package; ISIN verify; primary tie-out completion | next touch |
| DLB | FY2026 10-K window-roll re-test of bound-proof Past WEAK (w-o-4 9.1–9.9% vs 10% floor) + customer-concentration disclosure; ISIN re-verify; FY16–20 NIBCL liftable | ~Nov 2026 |
| SHA0.DE · BAYN.DE | P17 at next touch (v3.4.0-queue remnants) | next touch |
| ENR.DE | €2bn programme purpose | FY2026 AR ~Dec |
| OR.PA | P4 3rd-decline re-test; Galderma 20% (€4.2bn) + Kering Beauté/Creed audits; FY2016/18 gross counts + sterilisation quantum; Aesop pre-deal OI (Natura filings) | FY2026 |
| RMS.PA | FY2017/FY2020 tranches (AR2017/URD2020); **P4 — 3rd decline at FY2026 fires**; family % of capital/votes | FY2026 |
| PIRC.MI | IFRS 10 control determination re-test (Camfin–MPI agreement lapsed 28-Feb-26; carried 9–6) | FY2026 AR |
| MONC.MI | FY2016–20 record rebuild (issuer CDN blocks bulk retrieval); P17/RPT verify | next REVIEW |
| EPI-A.ST | FY2018–20 ARs (5y→8y); mandate purpose + 4th refusal year; Stanley audit | FY2026 AR |
| FIE.DE | Shopko audit re-test (>20× INDETERMINATE); window rolls to 9y | FY2026 AR ~Apr 2027 |
| FTK.DE | Supplier-breadth evidence; FY2020–21 SARs-era comp quantum | FY2026 |
| KRN.DE | Current-provisions NIBCL call (9.26% vs 10.03%); FY2026 window roll clears 10% on both | FY2026 AR |
| ASSA-B.ST | HHI (2023) multiple re-test (>20× INDETERMINATE, 3y 19.3–21.8×) | FY2026 AR |
| ESSITY-B.ST | BSN multiple INDETERMINATE; May-2026 SEK 3bn programme as 3rd tranche-year | FY2026 ~21 Jan 2027 |
| GETI-B.ST | Paragonix multiple; supplier breadth; SF PASS rests on zero buybacks ever | FY2026 AR |
| SKF-B.ST | **P4 — 3rd decline fires → Past WEAK**; John Sample multiple; Lex Asea separation ~Q4 2026 resets basis (re-underwrite both entities) | Q4 2026 / FY2026 AR |
| INDT.ST | **P4 — 3rd straight decline at FY2026 → Past WEAK/AVOID**; re-read FY2026 acquisition cohort | FY2026 AR |
| MYCR.ST | FY2026 acquisition cohort + supplier spend; P19 de-minimis + sterilisation re-test | FY2026 AR |
| HFG.DE | FY2015-end BS if the Nov-2017 IPO prospectus surfaces (beginning-CE legs record-limited); §162 Compensation Report 2025 (P17 INDETERMINATE) | next REVIEW |
| 6702.T | FY2017–FY2023 OI/NIBCL/capex rebuild (IR archive purged; 3y window carried); FY24 OI vintage question | next REVIEW |
| 6367.T | FY17 capital-employed inputs + Mar-16 NIBCL from FY17/FY18 tanshin (9y carried) | next REVIEW |
| Japan comp bounds | Exact top-exec comp for 7974.T, 6367.T, 6954.T, 6301.T, 5108.T, 7751.T (all clear P17 on bounds); 7974.T outside-director fees + FY18–21 intangibles alignment | first REVIEW each |
| ABEV | **FCF tie-out — band-moving** | FY2026 ~Feb 2027 |
| 300750.SZ (CATL) | Full AR tie-out (coherence-accepted tier-2); customer-concentration table is Future-deciding | FY2026 AR |
| CERT | Primary tie-out | next touch |
| LYFT · TENB · LMND · OPEN | Record rebuilds liftable (LYFT FY16–18 S-1/early 10-Ks; TENB FY18–20); LMND/OPEN primary line-item tie-outs incomplete | next touch |
| v3.7.0 App-F restatements | BABA, 2330.TW, AMZN, LIFCO-B.ST, TROW, BKNG, ROG.SW, FIE.DE, ULVR.L, AXFO.ST, NVS — memo App. F restates the labelled no-cash/all-cash band at next REVIEW; IBKR upper bound not derivable (logged judgment, single figure) | next REVIEW each |

**Standing session rules (pending codification at MODEL v4.2.0):** ISIN backfill at every REVIEW touch (§7.1a); primary tie-outs owed on every coherence-accepted memo from the 2026-08-07/09 cohorts (91 names) at their first REVIEW; prefer primary interim debt for EV inputs; regulated utilities are screened out at queue stage, never seeded for ANALYSE.

- **GPN (Global Payments, US37940X1028-input)** — added 2026-08-27 (v1 ANALYSE, AVOID/3 gates): (a) FY2016–FY2020 record rebuild (window record-limited 5y; cap liftable); (b) 2026/2027 proxy backfill — RPT section, outside-director fees, insider ownership %, and CEO-comp extraction conflict ($20.31m vs $17.42m) resolved against the DEF 14A itself; (c) FY2021–FY2025 repurchase share counts from 10-K equity notes (tranche prices currently derived ±10–15%); (d) Worldpay announced EBITDA multiple (Apr-2025 deck) as hard lower bound on pre-deal EV/OI; (e) verify ISIN. Trigger: FY2026 10-K (~Feb 2027) REVIEW or earlier touch.

- **7936.T (ASICS)** — added 2026-08-27 (v3 REVIEW, WATCH held): (a) **⚠ primary tanshin tie-out owed and material** — the Q2 FY2026 PDF was unreachable (assets.asics.com 403; release.tdnet.info robots-blocked), so every B/C/F figure this version came from a TDnet mirror (finance.biggo.jp, doc ID 140120260813520035); retrieve the primary and tie out the four §4 anchors; (b) the 24-Dec-2025 completion notice remains unretrieved two versions running (cumulative share count unconfirmed); (c) the Nov-2025 authorisation terms still rest on secondary news; (d) H1 FY2025 cash flow not retrieved → TTM FCF not computable; (e) exact FY2025 top-pay figure + individual outside-director fees at the FY2026 有報 (~Mar 2027); (f) 25,571,333 treasury shares (3.48% of issued) held uncancelled since Feb-2025 — capital-structure question, not a negative. Trigger: Q3 tanshin ~Nov 2026 / FY2026 tanshin ~Feb 2027.

- **TRI (Thomson Reuters)** — added 2026-08-27 (v3 REVIEW, WATCH held): (a) a TSX-stamped Notice of Intention (or its absence) could not be inspected — SEDAR+ unreachable; confirm the non-renewal against a TSX source at the next touch; (b) **standing price-and-event watch, not a calendar item** — the shares sit 10.8% below the ≈$116 conviction line, so any NCIB filing is verdict-relevant at any time; (c) carried: FY2021–24 tranche prices INDETERMINATE, acquisition audits INDETERMINATE, P17 3y NI leg bounded, lease liabilities not separately retrieved, Global Print discontinued-ops re-basing at FY2026.

- **STMN.SW (Straumann)** — added 2026-08-27 (v3 REVIEW, WATCH held): (a) **cadence correction — strike the H1 treasury-movement item**: Straumann publishes no standalone half-year financial report, so the movement is answerable only at the FY AR; (b) the §4 primary-interim-debt rule is **formally unsatisfied** for this name and the reason is structural — no interim balance sheet exists, and the disclosed cash (CHF 381.0m) and net cash position (CHF 34.7m) were deliberately not used to derive debt because the net-cash definition is undisclosed and the two readings diverge by ~CHF 169m of leases; (c) H1-2025 capex and FCF comparatives unreliable pending the AR (both extract as CHF 113.0m — an implausible collision); (d) carried: per-tranche treasury counts and prices, FY2025 goodwill/intangibles split, the lease-vs-borrowings note, the FY2025 treasury-usage discrepancy, FY2015 lease commitments; (e) P4 second-decline test at the FY2026 close — currently reading favourably. Trigger: FY2026 AR ~24 Feb 2027 (sole test).

- **INTU (Intuit)** — added 2026-08-27 (v2 REVIEW, WATCH held): (a) **FY2026 10-K, ~early Sep 2026** — Item 5 monthly table closes the Q4 tranche INDETERMINATE (shares and average price undisclosed; Q4 cash ~$2,039m derived by subtraction), plus the full-year repurchase count, the current portion of operating lease liabilities and the customer-concentration sentence; (b) **FY2026 proxy, ~Nov 2026 — gate-deciding**: a CEO total above ≈$40m is a P17 flag that pairs with the P19 CAUTION and FAILs SF; also closes the director-fee table and the FY2025 extraction conflict ($36,835,552 vs $36,845,552); (c) FY2023/FY2024 FCF unretrieved → the MCap/FCF normalized read stays bounded; (d) per-year NIBCL FY2017–FY2023 unretrieved → ROCE stays a bounded construction; (e) ISIN primary confirmation owed.

- **ZIP.AX (Zip Co)** — added 2026-08-27 (v2 REVIEW, AVOID/3 gates held): (a) **immediate and retrievable — the FY2026 Annual Report** (lodged 20 Aug 2026) was readable only to ~p.43–55 of 167, blocking the remuneration report (pp. 67–96), the statutory financial report (from p. 98), the share count, the intangibles note for TBV, the RPT note and the statutory cash-flow wording; this is a tooling failure, not a disclosure failure; (b) **ISIN never captured — two versions running** (§7.1a); (c) Programme 2's average price is derived (~A$2.02), not disclosed, and its exact close date is bracketed; (d) a "steps up the buyback" headline could not be read — an upsize looks unlikely on the disclosed totals but is not ruled out; (e) convertible-notes redemption date/amount unconfirmed; NCI line not found; (f) merchant revenue concentration still INDETERMINATE; (g) price is five sessions stale (A$3.05, 20 Aug) — a sweep refreshes Dist %. Trigger: AR re-retrieval now; 1H FY2027 (~Feb 2027) for the first execution under the 14 Sep programme.

- **FLUT (Flutter Entertainment, ISIN not captured)** — added 2026-08-31 (v1 ANALYSE, AVOID/3 gates): (a) **Snaitech pre-acquisition operating income** — the Snai deal multiple is logged INDETERMINATE (consideration ~$2.6bn / €2.3bn is sourced; pre-deal OI is not); take it from the FY2025 10-K business-combination note or Snaitech's pre-deal statutory accounts, then re-run the Gate-1C acquisition audit. (b) DEF 14A 2026-04-16 backfill — outside-director fees (US 2026 stops ≈$672k ordinary / ≈$1.02m chair-lead) and the related-party-transactions section, both unretrieved and therefore unscored; insider ownership %. (c) FY2025 income statement and cash-flow statement direct from the 10-K: FY2025 OI $615m, CFO $1,184m and the capex split currently rest on the accepted tier-2 series plus primary corroboration, because Item 8 sits beyond the fetch window. (d) FY2025 full-year repurchase share count from the 10-K equity note — the tranche is read on the derived H1 average of $249.4. (e) Verify ISIN. **Not owed:** FY2016–FY2020 is not a rebuild candidate on the same terms as other record-limited names — those years exist only as IFRS/GBP accounts for a pre-Stars, pre-FanDuel-consolidation perimeter with no US GAAP restatement, so a rebuild would produce a basis-inconsistent series; confirm the relabel to history-limited at the next touch and the ADEQUATE cap becomes permanent. Trigger: FY2026 10-K (~Feb 2027), or Q3'26 results (~Nov 2026) if the US revenue trend inflects.
---

## Corporate actions / RECONCILE queue

- **Corporate-actions sweep of the full register — OVERDUE** (delistings, renames, re-keys, spin-offs, closed deals across 308 names; two of the last fifteen backlog names had already ceased to exist as listings).
- **BBBY → NXH re-key** when the Neighborhood Intelligence rename is effective (key frozen BBBY per §7.1a; re-key is a RECONCILE act, logged).
- **INPST.AS** — delists on offer settlement (H2 2026): archive the row.
- **SKF-B.ST Automotive Lex Asea separation** ~Q4 2026 — basis reset, both entities re-underwritten.
- ~~**EA**~~ — **closed 4 Aug 2026**, $210.00 cash/sh, delisted (EA release). DNAF terminal row at register v280; no tax event (not held).
- **PYPL (PayPal) — Stripe/Advent approach LAPSED 27–28 Aug 2026** (Bloomberg/Axios/Reuters; no 8-K; the $60.50 bid had been rejected as undervaluing). Lapse branch fired → **full REVIEW owed at the de-pinned price** (≈$54–57, 28 Aug–3 Sep) — see item 9 above. The v14 "low-$40s inside the band" premise is struck, not carried.

---
- **ABB — Rotork acquisition CONFIRMED, ~$5.5bn, announced 16 Jul 2026.** Surfaced while de-duplicating the re-seed block: the ABB row's `AR-2026` re-test already names "Rotork/Advantics closing multiples", and this is the deal. Rotork (`ROR.L`) is therefore **struck from the candidate universe** — it is an ABB P19 input, not a name to analyse. [ABB release](https://new.abb.com/news/detail/137499/abb-expands-automation-offering-with-acquisition-of-rotork)
- **Candidate-stage strikes, 2026-08-28** (found by the corporate-action pass over the re-seed block; none has a register row, so none needs a row action — logged so they are not re-seeded): **`ITRK.L` Intertek** — EQT recommended cash offer £60.00/share, Rule 2.7 on 18 Jun 2026, **shareholders approved 6 Aug 2026**, delisting pending ([Rule 2.7](https://www.intertek.com/siteassets/investors/offer/rule-2.7-announcement-dated-18-june-2026.pdf) · [court/GM result](https://www.investegate.co.uk/announcement/rns/intertek-group--itrk/results-of-court-meeting-and-general-meeting/9709222)). **`SDF.AX` Steadfast Group** — binding scheme with the Amwins / Dragoneer / KKR consortium at A$6.00 cash, signed ~21–22 Aug 2026 ([report](https://www.insurancebusinessmag.com/au/news/breaking-news/steadfast-signs-binding-deal-with-us-consortium-587005.aspx)). All three deal figures are sourced, not derived.

## Re-seeding the ANALYSE queue — user decision (option (c) now carries stock, v17)

- **(a) Run the named re-test backlog above as REVIEW work** — highest value per hour; every name is a delta, not a build. **Still the recommended first call**: the ~50-name backlog is dated, verdict-moving and already half-sourced, where every name in the two new blocks is a cold build.
- **(b) The corporate-actions sweep** — cheap, mechanical, prevents quiet rot. **Now overdue and demonstrably load-bearing:** the 2026-08-28 pass over the candidate block alone caught three live take-privates (Rotork, Intertek, Steadfast) and a fourth already inside the register's own ABB row. Two of the last fifteen backlog names had already ceased to exist as listings. The same rot is running through the 319 live rows unchecked.
- **(c) A new ANALYSE market block** — **no longer an open question: 239 names are now queued above**, 58 from the top-100 coverage audit and 181 from the re-seed universe, across fifteen markets. Utilities are not seeded (standing screen). Sequencing is a user call; the note under Flags sets out what the register's shape argues for.

---

## Coverage audit — global top 100 by market cap (snapshot 2026-08-28)

*Source: companiesmarketcap.com global ranking, retrieved 2026-08-28 (sourced data; ranks only — **no market-cap figures are carried into this file**, and the ranking itself is a third-party aggregation, tier-3 under §4, adequate for a coverage checklist and for nothing else). Matched against all 317 register rows on **company name, not the ticker key** (§7.1a) — cross-listings resolved, so Roche→`ROG.SW`, Novartis→`NVS`, Tencent→`0700.HK`, TSMC→`2330.TW`, Novo Nordisk→`NOVO-B.CO` all count as covered.*

**Result: 42 of the top 100 carry a register row; 58 do not.** The gap is not random — it is concentrated in exactly the three groups the project has never seeded: mega-cap banks and insurers, the semiconductor complex, and state-controlled Asian and Gulf issuers.

**Framing, stated plainly: this is a coverage audit, not a candidate screen.** Size is neither a quality nor a cheapness signal, and nothing here has been pre-judged on any gate. The value of working the list is that each absence becomes a recorded decision instead of an oversight — an AVOID row saves future time under §7.1 exactly as a WATCH row does.


### Tier A — ordinary GSC treatment — 37 names

Analysable on the standard machinery. Ranks are companiesmarketcap positions at the 2026-08-28 snapshot; no market-cap figures are carried into this file.

| # | Key | Company | Country | Note |
|---|---|---|---|---|
| 8 | `AVGO` | Broadcom Inc. | USA | semiconductors |
| 17 | `000660.KS` | SK hynix Inc. | South Korea | memory — cyclical; chaebol governance |
| 19 | `AMD` | Advanced Micro Devices, Inc. | USA | semiconductors |
| 22 | `XOM` | Exxon Mobil Corporation | USA | oil & gas — P4 cyclicality (EQNR precedent) |
| 23 | `JNJ` | Johnson & Johnson | USA | pharma & medtech |
| 27 | `INTC` | Intel Corporation | USA | semiconductors |
| 28 | `ABBV` | AbbVie Inc. | USA | pharma |
| 30 | `CSCO` | Cisco Systems, Inc. | USA | networking |
| 35 | `LRCX` | Lam Research Corporation | USA | semicap |
| 36 | `CVX` | Chevron Corporation | USA | oil & gas — P4 cyclicality |
| 37 | `KO` | The Coca-Cola Company | USA | beverages |
| 38 | `AMAT` | Applied Materials, Inc. | USA | semicap |
| 39 | `CAT` | Caterpillar Inc. | USA | construction & mining equipment |
| 41 | `MRK` | Merck & Co., Inc. | USA | pharma |
| 42 | `GE` | GE Aerospace | USA | aero engines — perimeter reset (3-way split) |
| 48 | `PG` | The Procter & Gamble Company | USA | household & personal care |
| 50 | `HD` | The Home Depot, Inc. | USA | home improvement retail |
| 52 | `DELL` | Dell Technologies Inc. | USA | IT hardware |
| 54 | `PM` | Philip Morris International Inc. | USA | tobacco / nicotine |
| 58 | `RTX` | RTX Corporation | USA | aerospace & defence |
| 60 | `ARM` | Arm Holdings plc | UK | semiconductor IP — ADR line; SoftBank majority |
| 66 | `AZN` | AstraZeneca PLC | UK | pharma |
| 67 | `GEV` | GE Vernova Inc. | USA | power equipment — 2024 spin, short record |
| 68 | `ANET` | Arista Networks, Inc. | USA | networking |
| 71 | `SHEL` | Shell plc | UK | oil & gas — P4 cyclicality |
| 72 | `BHP` | BHP Group Limited | Australia | mining — NO PRECEDENT in register; user call |
| 73 | `TXN` | Texas Instruments Incorporated | USA | analog semiconductors |
| 75 | `KLAC` | KLA Corporation | USA | semicap |
| 77 | `AMGN` | Amgen Inc. | USA | biopharma |
| 78 | `TMO` | Thermo Fisher Scientific Inc. | USA | life-science tools |
| 81 | `TM` | Toyota Motor Corporation | Japan | autos — ADR; local line 7203.T |
| 88 | `SNDK` | Sandisk Corporation | USA | NAND storage — 2025 WDC spin, short record |
| 89 | `MRVL` | Marvell Technology, Inc. | USA | semiconductors |
| 91 | `ITX.MC` | Industria de Diseno Textil, S.A. (Inditex) | Spain | apparel retail — also on the ES re-seed block |
| 93 | `VZ` | Verizon Communications Inc. | USA | telecom |
| 97 | `APH` | Amphenol Corporation | USA | connectors & interconnect |
| 100 | `2454.TW` | MediaTek Inc. | Taiwan | fabless semis — also on the TW re-seed block |

### Tier B — financials, substitution basis required — 12 names

**Do not queue these onto the industrial CE/EV/TBV machinery.** The KSPI v1→v2 lesson (TODO v13): a pre-v3 memo priced a deposit-funded lender on industrial mechanics and the §2·1A substitution rule moved the band from $42–52 to ≈$98 with no change in the business. Every name here is a deposit- or premium-funded balance sheet.

| # | Key | Company | Country | Note |
|---|---|---|---|---|
| 16 | `JPM` | JPMorgan Chase & Co. | USA | FINANCIAL — substitution basis |
| 32 | `BAC` | Bank of America Corporation | USA | FINANCIAL — substitution basis |
| 45 | `HSBC` | HSBC Holdings plc | UK | FINANCIAL — substitution basis; ADR, local HSBA.L |
| 47 | `MS` | Morgan Stanley | USA | FINANCIAL — substitution basis |
| 53 | `GS` | The Goldman Sachs Group, Inc. | USA | FINANCIAL — substitution basis |
| 59 | `RY` | Royal Bank of Canada | Canada | FINANCIAL — substitution basis; also on the CA re-seed block |
| 63 | `WFC` | Wells Fargo & Company | USA | FINANCIAL — substitution basis |
| 69 | `MUFG` | Mitsubishi UFJ Financial Group, Inc. | Japan | FINANCIAL — substitution basis; ADR, local 8306.T |
| 85 | `C` | Citigroup Inc. | USA | FINANCIAL — substitution basis |
| 90 | `SAN.MC` | Banco Santander, S.A. | Spain | FINANCIAL — KEY COLLISION: SAN.PA is Sanofi; key Madrid line |
| 96 | `TD` | The Toronto-Dominion Bank | Canada | FINANCIAL — substitution basis |
| 98 | `ALV.DE` | Allianz SE | Germany | FINANCIAL — insurer; substitution basis |

### Tier C — state-controlled; SF gate structurally compromised — 9 names

The four shareholder-friendliness tests (§2·1C) read a proxy that either does not exist in comparable form or describes a controlling state owner. Recommend a **standing screen-out**, logged once, rather than nine Gate-0 abbreviated memos — but that is a user decision, not a framework output.

| # | Key | Company | Country | Note |
|---|---|---|---|---|
| 9 | `2222.SR` | Saudi Arabian Oil Company (Saudi Aramco) | Saudi Arabia | STATE — .SR not in §7.1a suffix table |
| 34 | `601939.SS` | China Construction Bank Corporation | China | STATE bank — SF gate structurally compromised |
| 44 | `601288.SS` | Agricultural Bank of China Limited | China | STATE bank — SF gate structurally compromised |
| 46 | `1398.HK` | Industrial and Commercial Bank of China Limited | China | STATE bank — SF gate structurally compromised |
| 55 | `601988.SS` | Bank of China Limited | China | STATE bank — SF gate structurally compromised |
| 74 | `600519.SS` | Kweichow Moutai Co., Ltd. | China | STATE-controlled (Guizhou province) |
| 79 | `0857.HK` | PetroChina Company Limited | China | STATE — SF gate structurally compromised |
| 86 | `IHC.AE` | International Holding Company PJSC | UAE | STATE-linked holding — .AE not in §7.1a suffix table |
| 87 | `0941.HK` | China Mobile Limited | China | STATE — SF gate structurally compromised |

---

---

## ANALYSE queue re-seed — candidate universe (built 2026-08-28)

*Answers the standing re-seed question below, option (c). **181 names, none of which has a register row** — de-duplicated against all 317 rows live at the 2026-08-28 snapshot, on company name per §7.1a, not on the ticker key. **Re-verified 2026-08-31 against the two rows added since** — SEE.L (Seeing Machines) and FLUT (Flutter Entertainment): neither appears in either block, and a core-name sweep of all 319 live company names against both blocks returns no collision. Tickers are suggested keys, resolved and verified with ISIN at run time. Selection rule applied: understandable business · long continuous record under a stable perimeter · structurally decent returns or a durable niche · family/founder/anchor control welcome. Screened out at source: utilities and regulated networks (standing screen), pure-play miners, oil & gas E&P, REITs, closed-end funds and pure investment holdings, SPAC-derived names, and anything with under ~5 years of standalone statements. **No figures are carried here by design** — nothing below is sourced financial data, and no name below has been valued, screened for cheapness, or pre-judged on any gate.*


### United Kingdom (.L) — 26 names

| Key | Company | Sector | Why queued |
|---|---|---|---|
| `SPX.L` | Spirax Group plc | thermal energy / niche pumps | installed steam base drives self-renewing aftermarket |
| `HLMA.L` | Halma plc | safety & environmental tech | decentralised regulation-driven niches, long compounding record |
| `IMI.L` | IMI plc | flow control & automation | mission-critical engineered components, aftermarket pull-through |
| `RSW.L` | Renishaw plc | precision metrology | founder-family anchor control, measurement-IP moat |
| `HILS.L` | Hill & Smith PLC | infrastructure products, galvanizing | local-scale galvanizing and road-safety niches, cash-generative |
| `DPLM.L` | Diploma PLC | value-added industrial distribution | essential low-cost consumables, sticky specification, disciplined bolt-ons |
| `BNZL.L` | Bunzl plc | outsourced business supplies | dull consolidation of a fragmented category, decades of statements |
| `RS1.L` | RS Group plc | industrial & electronics distribution | high-service low-order-value model, very long record |
| `HWDN.L` | Howden Joinery Group plc | trade kitchens | trade-only depot model, vertically integrated |
| `EXPN.L` | Experian plc | credit data & analytics | reciprocal-data bureau with entrenched network effects |
| `REL.L` | RELX PLC | professional information & analytics | subscription info embedded in customer workflow |
| `SGE.L` | The Sage Group plc | SME accounting & payroll software | high switching costs, among the longest UK software records |
| `RMV.L` | Rightmove plc | property portal | two-sided marketplace dominance, negligible capital intensity |
| `AUTO.L` | Auto Trader Group plc | automotive portal | dominant audience position, demonstrated pricing power |
| `SCT.L` | Softcat plc | IT value-added reseller | negative working capital, culture-driven, consistent record |
| `CCC.L` | Computacenter plc | IT infrastructure services | founder-anchored, conservative balance sheet, multi-decade record |
| `CRW.L` | Craneware plc | US hospital revenue-cycle software | founder-led niche SaaS, contracted recurring revenue [AIM] |
| `OXIG.L` | Oxford Instruments plc | scientific instruments | research-instrument niches with service annuity |
| `GNS.L` | Genus plc | animal genetics | royalty-like genetics licensing, hard-to-copy biological asset |
| `VCT.L` | Victrex plc | PEEK polymers | specified-in qualification-gated moat, habitually net cash |
| `GAW.L` | Games Workshop Group PLC | owned-IP miniatures & licensing | wholly owned IP, vertically integrated, fanatical customer base |
| `DGE.L` | Diageo plc | premium spirits | aged hard-to-replicate brand portfolio, structural pricing power |
| `DNLM.L` | Dunelm Group plc | homewares retail | founder-family control, vertically integrated own-brand |
| `BAG.L` | A.G. BARR p.l.c. | soft drinks | family-anchored heritage brands, conservatively financed |
| `RAT.L` | Rathbones Group Plc | discretionary wealth management | FINANCIAL — substitution basis; real fee-earning operating business |
| `IGG.L` | IG Group Holdings plc | retail trading platform | FINANCIAL — substitution basis; founder-built, transparent revenue drivers |

### Canada (.TO) — 15 names

| Key | Company | Sector | Why queued |
|---|---|---|---|
| `CNR.TO` | Canadian National Railway Company | rail freight | duopoly network, decades of statements, structurally high returns |
| `TFII.TO` | TFI International Inc. | road transport & logistics | founder-run LTL consolidator, disciplined acquisition record |
| `TIH.TO` | Toromont Industries Ltd. | equipment distribution & services | protected CAT dealer territory, recurring parts-and-service |
| `RCH.TO` | Richelieu Hardware Ltd. | building products distribution | founder-led, debt-light, long uninterrupted record |
| `WSP.TO` | WSP Global Inc. | engineering & professional services | asset-light consulting roll-up, proven integration playbook |
| `ATD.TO` | Alimentation Couche-Tard Inc. | convenience retail & fuel | founder-anchored global consolidator, understandable unit economics |
| `MRU.TO` | Metro Inc. | food & pharmacy retail | steady regional grocery and drug franchise, consistent record |
| `CTC.A.TO` | Canadian Tire Corporation, Limited | general merchandise retail | family-anchored dual-class, owned brands, dealer network |
| `DOL.TO` | Dollarama Inc. | value retail | dominant domestic dollar-store format, high returns on capital |
| `CCL.B.TO` | CCL Industries Inc. | specialty packaging & labels | Lang-family controlled serial acquirer, long compounding record |
| `ENGH.TO` | Enghouse Systems Limited | enterprise software | conservative net-cash software acquirer, founder-led allocation |
| `GIB.A.TO` | CGI Inc. | IT & business consulting | founder-anchored dual-class, buy-and-build plus buybacks |
| `TVK.TO` | TerraVest Industries Inc. | diversified industrial manufacturing | small-cap serial acquirer of unglamorous niches, anchor control |
| `SJ.TO` | Stella-Jones Inc. | treated wood infrastructure products | utility poles and railway ties, repeat replacement demand |
| `IFC.TO` | Intact Financial Corporation | P&C insurance | FINANCIAL — substitution basis; leading domestic underwriter |

### Australia (.AX) — 15 names

| Key | Company | Sector | Why queued |
|---|---|---|---|
| `WES.AX` | Wesfarmers Limited | diversified retail & industrial | long-record capital allocator, explicit return-on-capital discipline |
| `JBH.AX` | JB Hi-Fi Limited | consumer electronics retail | low-cost high-turn model, long record of high returns |
| `NCK.AX` | Nick Scali Limited | furniture retail | founder-family anchored, vertically integrated, simple |
| `REH.AX` | Reece Limited | plumbing & HVAC distribution | Wilson-family control, decades of continuous statements |
| `SNL.AX` | Supply Network Limited | commercial vehicle parts distribution | very simple aftermarket distributor, long record [small-cap] |
| `ARB.AX` | ARB Corporation Limited | automotive accessories | founder-anchored brand, net cash, durable niche |
| `BRG.AX` | Breville Group Limited | consumer appliances | owned-brand franchise, long record, global distribution runway |
| `COH.AX` | Cochlear Limited | implantable medical devices | large installed base, recurring processor upgrade revenue |
| `BXB.AX` | Brambles Limited | pallet pooling & logistics | scale network in reusable pallets, understandable unit economics |
| `ALQ.AX` | ALS Limited | testing, inspection & certification | recurring lab testing; note minerals-division commodity cycle |
| `TNE.AX` | TechnologyOne Limited | public-sector enterprise software | founder-anchored, net cash, very high retention |
| `HSN.AX` | Hansen Technologies Limited | billing & customer-care software | sticky mission-critical software, disciplined serial acquirer |
| `OCL.AX` | Objective Corporation Limited | government & regulatory software | founder-controlled, net cash, niche public-sector vendor |
| `AUB.AX` | AUB Group Limited | insurance broking & agencies | asset-light broker network; PE approach lapsed, still independent |
| `CDA.AX` | Codan Limited | detection & communications electronics | anchor-influenced, durable niche in metal detection and tactical radio |

### United States — industrial & specialty tail — 39 names

| Key | Company | Sector | Why queued |
|---|---|---|---|
| `CGNX` | Cognex Corporation | machine vision | dominant niche in vision-guided inspection, asset-light |
| `NOVT` | Novanta Inc. | photonics & precision motion | designed-in components, long lifecycles, sticky OEM relationships |
| `ATS` | ATS Corporation | factory automation integration | pure-play automation with growing installed-base service annuity |
| `ESE` | ESCO Technologies Inc. | test chambers, filtration, aero instruments | portfolio of small defensible niches with qualified-position pull-through |
| `KEYS` | Keysight Technologies, Inc. | electronic test & measurement | entrenched standard in RF/comms test, software and calibration pull |
| `MTD` | Mettler-Toledo International Inc. | precision weighing & lab instruments | textbook installed-base plus service annuity, very long record |
| `BMI` | Badger Meter, Inc. | flow measurement & water metering | replacement-cycle demand, structurally high returns, unbroken record |
| `LFUS` | Littelfuse, Inc. | circuit protection & sensors | designed-in content, long qualification cycles |
| `VPG` | Vishay Precision Group, Inc. | precision sensors & foil resistors | narrow engineered niches, long pre-history [small-cap] |
| `CTS` | CTS Corporation | sensors & actuators | long-lived engineered components, diversifying away from transport |
| `ALNT` | Allient Inc. | precision motion control | small-cap motion specialist, multi-decade record, stable perimeter |
| `MOG.A` | Moog Inc. | precision motion & fluid control | aftermarket-heavy engineered content, dual-class anchored voting |
| `WWD` | Woodward, Inc. | energy control & motion systems | very long record, sole-source positions, strong aftermarket pull |
| `IPGP` | IPG Photonics Corporation | industrial fiber lasers | vertically integrated founder-built; returns compressed — value not quality screen |
| `OSIS` | OSI Systems, Inc. | security screening & optoelectronics | certification-driven niches with service and consumables tails |
| `GGG` | Graco Inc. | fluid handling equipment | premium-priced niche equipment, distributor lock-in, long high-return record |
| `NDSN` | Nordson Corporation | precision dispensing systems | razor/blade parts-and-consumables pull-through on installed base |
| `DCI` | Donaldson Company, Inc. | filtration & replacement filters | classic aftermarket annuity, multi-decade continuous statements |
| `SSD` | Simpson Manufacturing Co., Inc. | structural connectors & anchors | code-specified products creating switching friction |
| `WTS` | Watts Water Technologies, Inc. | flow control valves | replacement-driven demand, dual-class with family voting control |
| `GRC` | The Gorman-Rupp Company | industrial & municipal pumps | family-anchored, conservatively financed, exceptionally long record |
| `OFLX` | Omega Flex, Inc. | flexible metal hose & gas piping | single narrow niche, very high returns, majority anchor holder |
| `LECO` | Lincoln Electric Holdings, Inc. | welding equipment & consumables | consumables attach rate on installed equipment, century-long record |
| `SNA` | Snap-on Incorporated | professional tools & diagnostics | franchised van channel is a durable distribution moat |
| `FELE` | Franklin Electric Co., Inc. | water & fuel pumping systems | replacement-led demand, long record, disciplined bolt-ons |
| `FAST` | Fastenal Company | fastener & MRO distribution | onsite/vending model embeds it in customer plants |
| `MSM` | MSC Industrial Direct Co., Inc. | metalworking & MRO distribution | dual-class family voting control, vending stickiness |
| `AIT` | Applied Industrial Technologies, Inc. | bearings & power transmission distribution | technical-service distribution with fluid-power value-add |
| `WSO` | Watsco, Inc. | HVAC/R distribution | replacement-driven, founder-family controlled, disciplined consolidation |
| `POOL` | Pool Corporation | pool supplies distribution | consumables-dominated demand, scale in a fragmented channel |
| `RELL` | Richardson Electronics, Ltd. | specialty components distribution | founder-family super-voting control, net-cash habit, legacy niches |
| `EVI` | EVI Industries, Inc. | commercial laundry equipment distribution | founder-led roll-up with parts-and-service pull-through |
| `DOV` | Dover Corporation | diversified decentralised industrial | long-standing decentralised model, consumables-weighted mix |
| `AME` | AMETEK, Inc. | electronic instruments & electromechanical | disciplined bolt-ons funded from internal cash, high returns |
| `IEX` | IDEX Corporation | fluidics & health/science niches | decentralised acquirer of small high-margin flow niches |
| `HEI` | HEICO Corporation | aerospace aftermarket parts | family-controlled dual-class, decades of low-multiple acquisitions |
| `TDY` | Teledyne Technologies Incorporated | instrumentation & digital sensing | disciplined acquirer with deliberate deleveraging after each deal |
| `CSW` | CSW Industrials, Inc. | specialty industrial products | small-cap decentralised acquirer; ticker changed CSWI to CSW (2025) |
| `KAI` | Kadant Inc. | process equipment & consumables | parts-and-consumables majority of revenue, steady bolt-ons |

### Norway (.OL) — 10 names

| Key | Company | Sector | Why queued |
|---|---|---|---|
| `KOG.OL` | Kongsberg Gruppen ASA | defence & maritime technology | decades of statements in sonar, missiles, maritime automation |
| `TOM.OL` | TOMRA Systems ASA | reverse vending & sensor sorting | global installed base generating recurring service revenue |
| `BOUV.OL` | Bouvet ASA | IT consulting | capital-light Nordic consultancy, unbroken profitable record |
| `BRG.OL` | Borregaard ASA | specialty biochemicals from wood | niche lignin and cellulose products with few substitutes |
| `ORK.OL` | Orkla ASA | branded consumer goods / holding hybrid | consolidated Nordic brands, Canica (Hagen) anchor control |
| `ATEA.OL` | Atea ASA | IT infrastructure distribution | entrenched Nordic and Baltic public-sector position |
| `AFG.OL` | AF Gruppen ASA | construction & civil engineering | unusually long record of decent returns for a contractor |
| `MEDI.OL` | Medistim ASA | medical devices | narrow durable niche in intraoperative flow measurement |
| `WAWI.OL` | Wallenius Wilhelmsen ASA | ro-ro shipping & vehicle logistics | multi-decade record, Wallenius/Wilhelmsen family anchors |
| `ODF.OL` | Odfjell SE | chemical tankers & tank terminals | family-controlled specialist, record spanning a century |

### Spain (.MC) — 9 names

| Key | Company | Sector | Why queued |
|---|---|---|---|
| `AMS.MC` | Amadeus IT Group, S.A. | travel technology | entrenched distribution and airline IT, high switching costs |
| `VIS.MC` | Viscofan, S.A. | food casings | world leader across all four casing technologies, single niche |
| `VID.MC` | Vidrala, S.A. | glass container packaging | founding-family control, freight-protected regional plants |
| `CIE.MC` | CIE Automotive, S.A. | automotive components | multi-technology tier-two, anchor shareholders, acquisitive record |
| `FDR.MC` | Fluidra, S.A. | pool & wellness equipment | family-anchored, aftermarket-weighted on a large installed base |
| `MCM.MC` | Miquel y Costas & Miquel, S.A. | specialty paper | family-controlled thin and cigarette papers, conservatively financed |
| `LOG.MC` | Logista Holdings, S.A. | Iberian distribution | near-unavoidable network, negative working capital; Imperial controls |
| `EBRO.MC` | Ebro Foods, S.A. | branded food | global rice and pasta brands, stable anchor shareholders |
| `PSG.MC` | Prosegur Compania de Seguridad, S.A. | security services | family-controlled, long record in guarding, alarms, cash handling |

### Belgium (.BR) — 8 names

| Key | Company | Sector | Why queued |
|---|---|---|---|
| `LOTB.BR` | Lotus Bakeries NV | branded food | Boone family control, single-brand global rollout, very long record |
| `MELE.BR` | Melexis NV | automotive semiconductors | family-anchored via Xtrion, fab-lite sensor niche, high-return record |
| `DIE.BR` | D'Ieteren Group SA | vehicle glass & auto distribution | genuine operating subsidiaries, family control over centuries |
| `EVS.BR` | EVS Broadcast Equipment SA | broadcast technology | narrow live-sports replay niche, long record, net cash |
| `COLR.BR` | Colruyt Group N.V. | food retail | family control, decades built on lowest-price discipline |
| `UCB.BR` | UCB SA | biopharmaceuticals | family-controlled via Tubize, immunology and neurology portfolio |
| `BEKB.BR` | NV Bekaert SA | steel wire transformation | global leader in steel cord, family reference shareholder |
| `ACKB.BR` | Ackermans & van Haaren NV | marine engineering, construction, banking | FINANCIAL leg — substitution basis; consolidated DEME/CFE operating subs |

### Austria (.VI) — 7 names

| Key | Company | Sector | Why queued |
|---|---|---|---|
| `ANDR.VI` | Andritz AG | plant engineering & equipment | large installed base driving rising aftermarket and service share |
| `WIE.VI` | Wienerberger AG | building materials | world's largest brick maker, freight-protected local plants |
| `MMK.VI` | Mayr-Melnhof Karton AG | cartonboard & folding cartons | family-controlled, vertically integrated, decades of statements |
| `PAL.VI` | Palfinger AG | truck-mounted cranes | family control, global leader with dealer and service network |
| `DOC.VI` | DO & CO Aktiengesellschaft | airline & event catering | founder-controlled, sticky long-dated contracts |
| `STR.VI` | Strabag SE | construction | Haselsteiner family plus anchors, conservative for a contractor |
| `FQT.VI` | Frequentis AG | air-traffic control & public-safety comms | mission-critical systems, very long product lives; listed 2019 (short record) |

### Ireland (.IR) — 4 names

| Key | Company | Sector | Why queued |
|---|---|---|---|
| `KRZ.IR` | Kerry Group plc | taste & nutrition ingredients | R&D-embedded, specification-locked customer relationships |
| `KRX.IR` | Kingspan Group plc | insulation | founder-family (Murtagh) anchor, leadership in insulated panels |
| `IR5B.IR` | Irish Continental Group plc | ferry shipping & container logistics | multi-decade Irish Sea corridor record, owned tonnage |
| `OIZ.IR` | Origin Enterprises plc | agri-input distribution & agronomy | long record as crop-input distributor and agronomy adviser |

### Portugal (.LS) — 2 names

| Key | Company | Sector | Why queued |
|---|---|---|---|
| `JMT.LS` | Jeronimo Martins, SGPS, S.A. | food retail | Soares dos Santos family control, dominant Polish and Portuguese formats |
| `COR.LS` | Corticeira Amorim, S.G.P.S., S.A. | cork | Amorim family control, world leader in cork stoppers over generations |

### South Korea (.KS) — 9 names

| Key | Company | Sector | Why queued |
|---|---|---|---|
| `009150.KS` | Samsung Electro-Mechanics Co., Ltd. | electronic components | defensible high-end MLCC position; chaebol affiliate, customer concentration |
| `018260.KS` | Samsung SDS Co., Ltd. | IT services & logistics BPO | asset-light enterprise IT; heavy related-party revenue is the flag |
| `012330.KS` | Hyundai Mobis Co., Ltd. | auto components | high-margin aftermarket parts franchise; chaebol governance flag |
| `010120.KS` | LS ELECTRIC Co., Ltd. | electrical equipment | switchgear and automation supplier, not a utility; family-controlled |
| `014680.KS` | Hansol Chemical Co., Ltd. | specialty chemicals | hydrogen peroxide and semiconductor precursors to domestic fabs |
| `111770.KS` | Youngone Corporation | outdoor apparel manufacturing | founder-built outerwear OEM, sticky brand-customer relationships |
| `000100.KS` | Yuhan Corporation | pharmaceuticals | among Korea's oldest pharma, foundation-anchored, clean balance sheet |
| `004370.KS` | Nongshim Co., Ltd. | packaged food | dominant domestic instant-noodle brands, multi-decade statements |
| `003230.KS` | Samyang Foods Co., Ltd. | packaged food | export brand transformed economics; past governance record warrants scrutiny |

### Taiwan (.TW) — 8 names

| Key | Company | Sector | Why queued |
|---|---|---|---|
| `2308.TW` | Delta Electronics, Inc. | power electronics | founder-built power-conversion franchise, decades of statements |
| `2395.TW` | Advantech Co., Ltd. | industrial computing | founder-controlled, design-in industrial PC niche, high returns |
| `2207.TW` | Hotai Motor Co., Ltd. | auto distribution | exclusive Toyota distributor for Taiwan; captive finance complicates accounts |
| `2912.TW` | President Chain Store Corporation | convenience retail | dominant Taiwan network; Uni-President group control |
| `1476.TW` | Eclat Textile Co., Ltd. | technical textiles | vertically integrated functional-fabric supplier; customer concentration |
| `9910.TW` | Feng Tay Enterprises Co., Ltd. | footwear manufacturing | decades-long contract manufacturer; single-customer dependence |
| `2360.TW` | Chroma ATE Inc. | test & measurement | founder-controlled instrument maker, narrow niches, high returns |
| `8464.TW` | Nien Made Enterprise Co., LTD. | window coverings | family-controlled made-to-order blinds; US housing-channel concentration |

### India (.NS) — 15 names

| Key | Company | Sector | Why queued |
|---|---|---|---|
| `TCS.NS` | Tata Consultancy Services Limited | IT services | multi-decade record, asset-light, structurally high returns |
| `PERSISTENT.NS` | Persistent Systems Limited | IT services | consistent engineering-services record; live cross-border bid is a flag |
| `TITAN.NS` | Titan Company Limited | jewellery, watches, eyewear | branded retail taking share from unorganised market; Tata-promoted |
| `MARICO.NS` | Marico Limited | household & personal care | founder-family control, category leadership in hair and coconut oils |
| `PAGEIND.NS` | Page Industries Limited | innerwear apparel | exclusive Jockey/Speedo licensee; licence-renewal dependence is the flag |
| `PIDILITIND.NS` | Pidilite Industries Limited | adhesives & specialty chemicals | family-controlled owner of a branded industrial consumable |
| `VINATIORGA.NS` | Vinati Organics Limited | specialty chemicals | promoter-controlled global niche leader; product concentration flag |
| `DIVISLAB.NS` | Divi's Laboratories Limited | APIs & custom synthesis | promoter-controlled, cost-position-led niche, multi-decade record |
| `AIAENG.NS` | AIA Engineering Limited | industrial consumables | global niche in high-chrome grinding media; supplier to miners, not a miner |
| `CUMMINSIND.NS` | Cummins India Limited | industrial machinery | engines and gensets with entrenched service network; MNC-parent RPT flag |
| `ELGIEQUIP.NS` | Elgi Equipments Limited | air compressors | family-controlled, long record, service-and-spares annuity |
| `SUNDRMFAST.NS` | Sundram Fasteners Limited | auto components | TVS-family controlled fastener and forging supplier, multi-decade record |
| `CRISIL.NS` | CRISIL Limited | ratings & analytics | asset-light franchise; majority-owned by global parent, ratings arm regulated |
| `ABBOTINDIA.NS` | Abbott India Limited | pharmaceuticals | very long Indian record, asset-light branded generics; MNC RPT/royalty flag |
| `BAJAJ-AUTO.NS` | Bajaj Auto Limited | two- and three-wheelers | family-controlled, high returns; KTM consolidation resets perimeter |

### Singapore (.SI) — 7 names

| Key | Company | Sector | Why queued |
|---|---|---|---|
| `BSL.SI` | Raffles Medical Group Ltd | healthcare services | founder-controlled hospital and clinic network, multi-decade record |
| `V03.SI` | Venture Corporation Limited | electronics manufacturing & design | design-led partner in regulated end-markets, historically net cash |
| `558.SI` | UMS Integration Limited | semiconductor equipment components | founder-controlled precision machining; single-customer concentration |
| `AP4.SI` | Riverstone Holdings Limited | cleanroom gloves | family-controlled, differentiated cleanroom niche, long record |
| `Y92.SI` | Thai Beverage Public Company Limited | beverages | dominant Thai spirits franchise; leverage and complex structure flags |
| `S63.SI` | Singapore Technologies Engineering Ltd | aerospace & defence services | aircraft MRO and P2F conversion annuity; Temasek majority — user call |
| `OV8.SI` | Sheng Siong Group Ltd | grocery retail | family-controlled, owns much of its store estate, consistent record |

### Hong Kong (.HK) — 7 names

| Key | Company | Sector | Why queued |
|---|---|---|---|
| `0669.HK` | Techtronic Industries Company Limited | power tools & outdoor equipment | multi-decade record, strong professional-tool brand franchise |
| `0303.HK` | VTech Holdings Limited | consumer electronics & learning products | founder-controlled, historically net cash, high-return niches |
| `0522.HK` | ASMPT Limited | semiconductor assembly equipment | multi-decade record in back-end equipment; verify parent stake |
| `2313.HK` | Shenzhou International Group Holdings Limited | knitwear manufacturing | founder-controlled vertically integrated supplier to global brands |
| `2020.HK` | ANTA Sports Products Limited | sportswear | founder-family controlled brand builder; holds ~40%+ of register name `AS` (per that row's own SF cell) |
| `1929.HK` | Chow Tai Fook Jewellery Group Limited | jewellery retail | family-controlled, franchise-led store network atop a far older business |
| `0327.HK` | PAX Global Technology Limited | payment terminals | long record, historically high returns and net cash; confirm no state linkage |

---

---

## Scheduled reviews — near-term calendar

*Refreshed 2026-08-09 against register v248 rows; v10 adds the overdue markers above and re-points the Q1–Q2 2027 detail pointer (the register's Open items no longer carry it). Non-authoritative: the register wins. Dated triggers only; price alerts live in the rows.*

**Aug 2026 — ~~7936.T Q2 tanshin 14 Aug~~ · ~~TRI NCIB expiry 18 Aug~~ · ~~STMN.SW H1 19 Aug~~ · ~~ZIP.AX FY26 Appx 4E 20 Aug~~ · ~~INTU FY2026 25 Aug~~ all CLEARED at register v278 (committed 2026-08-31).** Still open from this month: **GAP Q2 10-Q filed 28 Aug 2026 — Item 5 monthly buyback tie-out owed (closes the named INDETERMINATE; per 2026-09-04 run)** · **HEXA-B.ST Q2 re-base (29 Jul — blocked on primary PDFs)** · BABA FY2027 Q1 · ADYEN.AS H1 · PAH3.DE H1 · WMT Q2 FY27 10-Q · TEAM FY2026 10-K (OI inflection + P19 on the $1.5bn 2024 programme) · CELH Q2 10-Q · RUSTA.ST AR 25/26 · BNR.DE H1 (optional) · 1211.HK H1 (optional). **None of these nine was touched this session** — the five dated re-tests consumed the run.
**Sep 2026:** **FDS FY2026 results 30 Sep 2026** (FY ended 31 Aug; scheduling release 2 Sep — first Viswanathan-era print; make-whole SCT = named P17 strike risk) · PANW FY2026 results released 1 Sep, **10-K not yet filed** (first CyberArk-consolidated statements pending) · ~~UFI FY2026 10-K~~ **filed 26 Aug 2026** (retrievable) · ~~CRM Q2 FY27~~ **reported 26 Aug 2026, 10-Q same day** (optional; ~1 week earlier than FY26 precedent) · LULU Q2 print 3 Sep (P19 CAUTION re-test; O'Neill eff. 8 Sep) · NKE: **DEF 14A filed 15 Jul 2026 — retrievable now** (dated second-flag document); **AGM 8 Sep 2026**; Q1 FY2027 10-Q ~Sep/Oct · RUSTA.ST AGM 18 Sep (P19 authorisation watch) · ~~EA deal outside date 28 Sep~~ **closed 4 Aug — struck** · INTU FY2026 10-K **still unfiled as of 4 Sep** (FY25 precedent 3 Sep; Item 5 closes the Q4 tranche INDETERMINATE). *Dates per the 2026-09-04 run-plan verification (`claude/2026-09-04_run-plan-and-queue-verification_v1.md` §4–6).*
**Oct 2026:** COST FY2026 10-K ~early Oct (completed programme year; Jan-2027 expiry the natural re-test) · MU FY2026 10-K ~Oct (band re-anchor only) · TER Q3 10-Q ~Oct · MSFT FY2026 proxy ~Oct (P17 absolute-trigger flag) · EL.PA Q3 20 Oct (informational) · **SW.PA FY2026 results 23 Oct** (band removal + P4 + P19) · AAPL FY2026 10-K ~Oct/Nov.
**Nov 2026:** NET Q3 ~Nov (converts path) · **6758.T H1 FY3/27 10 Nov** (¥500bn facility re-test) · SOON.SW H1 ~Nov (successor programme) · **DLB FY2026 10-K ~Nov** (window-roll re-test — the most interesting near-dated flip) · QCOM FY2026 10-K ~Nov (falling-base re-anchor + CAUTION re-test) · ROK FY2026 10-K ~Nov · V FY2026 10-K ~Nov (11%-client disclosure) · ATKR · AZTA · SONO · COLO-B.CO FY2025/26 (L/E at the P5 line) · 7974.T Q2 · 8002.T H1 (¥100bn pgm execution multiple) · EKTA-B.ST H1 · WISE.L H1 FY2027 (the £405m tranche price) · **TRI.PA FY2026 results ~25 Nov** (first buyback year; closest AVOID at +7.7%) · SCHN.SW repurchase-cessation watch (programme to Nov 2026) · PANW 2026 proxy.
**Dec 2026 / Q4:** ENR.DE FY2026 AR ~Dec (first clean-cycle year + €2bn/€6bn P19 re-test) · SIE.DE FY2026 ~Dec (tranche + CAUTION re-test; Feb-2027 AGM Healthineers spin vote → full quality re-base) · SKF-B.ST Lex Asea ~Q4 · TKA.DE, TUI1.DE FY2026 ARs (informational) · INPST.AS settlement → delist/archive · BAYN.DE Roundup settlement approval + post-Durnell provisioning.
**Q1–Q2 2027 — FY2026 annual season:** the bulk of the 69-name WATCH list re-anchors, including all four held names (and the HFG / NOVO-B decisions if still open), plus the named re-test backlog above — P19 dual-reads (SCHN.SW, GEBN.SW, SAF.PA, TER, MORN, GRMN, SU.PA), acquisition-audit INDETERMINATEs (FIE.DE, ASSA-B.ST, ESSITY-B.ST, GETI-B.ST, EPI-A.ST, MYCR.ST, KRN.DE), P4 third-decline tests (INDT.ST, SKF-B.ST, CELH, RMS.PA, OR.PA, SIKA.SW), **EQNR FY2026 ~Feb 2027** (the P4-break case; IDEAS A6), ABEV FY2026 + band-moving FCF tie-out, NU FY2026, **0700.HK AR ~Mar 2027** (record rebuild + P17 resolution), CATL FY2026 AR, ADBE FY2026 10-K ~Jan, **ZBRA FY2026 10-K ~Feb 2027** (named ADVERSE path), CRCT FY2026 10-K (SCT — verdict-moving), and the FY2027 10-K cluster (CRWD, SNOW, OKTA, PATH, S, WDAY ~Mar 2027) — **detail: "Named re-tests & backfills" above + memo appendices.**

---

## Overnight / delayed-run design (draft — for later recycling)

Design sketch for an unattended runner that processes this queue on a schedule. Not built yet; finalise later.

**Substrate.** Claude Code in headless mode (`claude -p`) driven by a **scheduled GitHub Action** (`on: schedule: cron`). This reuses the existing repo-native pipeline — `MODEL.md` as the operative framework, `_REGISTER.md` as state, §7.4a as the commit protocol — rather than re-plumbing it into a bespoke script. Same agent loop (bash, web fetch, git), no human in the loop. Alternatives: plain `cron` on a local/cloud box running the same `claude -p` call, or Claude Code Routines for clock-triggered runs. Cost for a nightly list of a few dozen names is single-digit dollars.

**Flow.**
1. Runner reads this file's queue section (mode + name).
2. Session-start: load PAT from secret, fetch live `MODEL.md` + `_REGISTER.md`.
3. Process each name **strictly sequentially** through the five-gate pipeline.
4. Commit each memo, then merge the register — one runner, sequential writes only.
5. Clear processed names from the queue; emit a JSON run summary (`--output-format json`, per-name verdict + `total_cost_usd`).

**Non-negotiable guardrails for unattended operation.**
- **Data-completeness gate.** If the inputs for the four CE variants / cheapness legs are not cleanly sourced, emit an `INCOMPLETE` stub memo flagged for human review and skip the verdict. Never fill a gap with an assumption to finish a row.
- **Sequential register I/O.** No fan-out. Parallel jobs PUT-ing `_REGISTER.md` manufacture exactly the collisions §7.4a exists to catch.
- **MODEL-mode lockout.** Runner handles ANALYSE / REVIEW / SWEEP only. Framework changes stay a human-only, exact-phrase "commit model" gate; runner has no write access to `instructions/`.
- **Commit-time compliance re-measure** (v4.2.0): P13 word count, §7.1 cell caps, four-gates-only check, no register-wide superlatives — unattended runs drift ~10–65% over P13 and their own in-run compliance claims are not evidence.
- Secrets (`ANTHROPIC_API_KEY`, PAT) as repo secrets, never in workflow files; `--allowedTools` scoped to EDGAR / Yahoo / GitHub.
- **Retrieval doctrine from the Aug-2026 runs:** primary results releases are the backbone (a Q4 release carries two full years of statements in one document and survives the URL-must-be-surfaced-by-search constraint); tier-2 columns must tie to a primary figure before their headers are trusted; per-filer productive channels are logged in each memo's App. A (e.g. Hitachi results library; Panasonic press-release PDFs; MHI tanshin archive; Lagardère interim reports; Trigano results releases). **US-domestic-filer addendum (FLUT, 2026-08-31):** for SEC filers the **10-Q is the efficient primary route**, not the 10-K — Item 1 Financial Statements is the first content in a 10-Q and therefore inside the fetch window, while a 10-K's Item 8 sits ~80 pages past it and truncates away. A 10-Q's comparative columns carry the prior fiscal year-end balance sheet in full, which alone satisfies three of the four §4 tie-out anchors plus the net-financial-position composite. Also logged: in this sandbox `bash` cannot reach `data.sec.gov` (proxy `host_not_allowed`) and `web_fetch` rejects any URL not first surfaced by a search, so the XBRL companyfacts/companyconcept endpoints are unavailable — plan the retrieval around searchable filing URLs.

**The real bottleneck is data, not scheduling.** The SEC-filer path is deterministic and safe to automate. The European and Japanese non-SEC names depend on primary-report PDF extraction — the fragile, judgment-heavy path where an unattended run is most likely to silently produce a wrong verdict. Harden those fetchers (or route them to `INCOMPLETE`) before trusting overnight output on this universe.

---

## Backlog — closure record

*Kept as a record of what was worked, not as a queue. Every name below carries a register row and a committed memo.*

- **Switzerland 13/13** (v2) · **Germany 30/30** (v2) · **Netherlands 3/3** (v2) · **Sweden 25/25** (v3) · **Italy 6/6** (v4) · **France 16/16** (v6) · **Japan majors 9/9** (v7).
- **Finland 4/4** · **Poland 6/6** · **United Kingdom 2/2** · **Denmark 3/3** · **Brazil 2/2** (all-WATCH) · **Energy 5/5** (0 WATCH; EQNR the near-miss) — all v8.
- **United States 72/72** (v8), closed 07–09 Aug 2026. Struck rather than analysed: UDMY, OLPX (dead listings), ZM (duplicate).

---

## Flags


- **Korean primary filings are unreachable from the sandbox (logged 2026-09-04, 244920.KS v1):** `dart.fss.or.kr` and `wcomp/comp.fnguide.com` refuse on robots, `kind.krx.co.kr` on bot detection, the issuer's own IR site on robots; `englishdart` was not reachable either. Every `.KS` ANALYSE in the re-seed block (9 names) and any KSPI-style Korean-listed name will hit the same wall — tier-2 series can be built (stockanalysis/S&P carries 5y for KRX) but cannot be accepted under §4. **Options for the user:** (a) an OpenDART API key (`opendart.fss.or.kr`, free registration) — would need `opendart.fss.or.kr` added to the sandbox allow-list; (b) Korean primaries uploaded to the chat as PDF/HTML for the session; (c) accept provisional tier-2 memos for Korean names with a standing rebuild flag, as done for 244920.KS. Until decided, Korean ANALYSE output carries a provisional label.
- **⚠ USER DECISION — rotate the GitHub PAT.** Three independent retrieval agents, working on unrelated names and none prompted to look, each surfaced the same observation this session: **the fine-grained PAT is stored in plaintext in the Claude project instructions**, where it is visible to anything that reads that context. The bootstrap's own terms already require rotation "after sharing any chat or this project, and on any suspicion of exposure." Nothing indicates misuse, and the token's blast radius is bounded by design (single repo, Contents read/write only, ≤90-day expiry) — but three unprompted flags is itself the suspicion the term contemplates. **Recommended: rotate at github.com/settings/personal-access-tokens, update the token line in the project instructions, and re-paste.** No repo change is needed and no session action is taken without the user's instruction. *(Raised 2026-08-27; carries until the user closes it.)*
- **Retrieval-environment constraint — new, and it shapes what can be scheduled.** Three classes of primary source refused this session: **network-policy 403s** at the egress proxy (assets.asics.com, api.alertir.com, mb.cision.com, data.sec.gov, efts.sec.gov), **robots.txt blocks** (release.tdnet.info, sec.gov/cgi-bin/browse-edgar), and **fetch-approval gates** that time out unanswered in an unattended run (investors.hexagon.com, s204.q4cdn.com, sec.gov/Archives directory listings, several live-quote pages). Company IR sites that render via JavaScript (Straumann, Zip) return empty shells. **Consequence for the overnight-runner design below: the data-completeness gate is not a theoretical guardrail — it fired twice today**, on Hexagon and Gap, and would have produced two wrong verdicts had it not. Log which hosts work per filer in each memo's Appendix A, as the retrieval doctrine already requires.
- **✓ "Cartara" → Certara (CERT) — CONFIRMED by user 2026-08-18.** Flag closed; the CERT row stands (AVOID, two gates, analysed 2026-08-09).
- **Bed Bath & Beyond** — resolved by evidence, analysed as **BBBY** (AVOID, three gates); **NXH re-key pending** the rename's effectiveness (see Corporate actions).

---
- **⚠ FRAMEWORK GAP — §7.1a suffix table has no key for five of the markets queued above. 23 names are blocked on it.** The suffix-always convention enumerates 28 exchanges; it omits **India (`.NS`/`.BO`), Ireland (`.IR`), Portugal (`.LS`), Saudi Arabia (`.SR`) and Abu Dhabi (`.AE`)**. Affected: 15 India + 4 Ireland + 2 Portugal in the re-seed block, plus `2222.SR` Saudi Aramco and `IHC.AE` in the coverage audit. The convention exists so the key doubles as the SWEEP price lookup, so this cannot be patched per-name at ANALYSE time without breaking that guarantee. **This is a framework change: it needs a MODEL session and the exact words "commit model" — it is not inferable and not covered by auto-commit.** Parked as an entry for `queue/IDEAS.md`; the 23 names stay queued but are **not runnable** until it lands.
- **Key collision — Banco Santander.** `SAN.PA` is already taken by **Sanofi** in the register. Santander must key `SAN.MC` (Madrid) or its NYSE line, resolved at ANALYSE, never by string-append (§7.1a).
- **Cross-holding — `2020.HK` ANTA Sports.** ANTA holds ~40%+ of **Amer Sports (`AS`)**, an existing register row whose SF cell already carries an unpaired "ANTA ~40%+ caveat". Analysing ANTA touches that caveat from the other side; run them as a pair, not independently.
- **Corporate-action status UNVERIFIED — 16 Korea/Taiwan candidates.** `009150.KS` `018260.KS` `012330.KS` `010120.KS` `014680.KS` `111770.KS` `000100.KS` `004370.KS` `003230.KS` · `2395.TW` `2207.TW` `2912.TW` `1476.TW` `9910.TW` `2360.TW` `8464.TW`. These cleared group-level sweeps with no hits, but KRX/TWSE corporate actions (physical splits, spin-offs, tender offers) are disclosed locally and poorly indexed in English. **Not called clean** — verify per-name at ANALYSE before spending a build. `2308.TW` Delta Electronics *is* verified clean.
- **Perimeter / event flags carried on otherwise-clean candidates** (still queued, warning attached): `CRW.L` Bain approach rebuffed 2025 · `WSP.TO` TRC acquisition, largest ever · `TFII.TO` US redomicile announced then abandoned · `ATD.TO` Seven & i proposal withdrawn Jul 2025 · `DIE.BR` Belron strategic review, Rothschild engaged Mar 2026 · `KRZ.IR` Kerry Dairy Ireland 70% sold · `ORK.OL` Orkla India IPO'd Nov 2025 · `BAJAJ-AUTO.NS` KTM/PIERER control acquired Nov 2025 · `2020.HK` 29% of PUMA agreed Jan 2026 · `ESE` SM&P acquisition Apr 2025 · `558.SI` Bursa Malaysia secondary listing · `Y92.SI` F&N/Frasers share swap · `0522.HK` KKR privatisation talks ended 2024 (recurrence risk) · `GEV` and `SNDK` are recent spins with short standalone records.
- **What the register's shape argues for (analysis, not a recommendation).** Coverage by exchange suffix across the 317 rows live at the 2026-08-28 snapshot (319 now): US 154 · Germany 34 · Sweden 28 · France 22 · Japan 18 · Switzerland 13 · Netherlands 9 · Poland 6 · **UK 6** · Italy 5 · Denmark 5 · Finland 4 · Hong Kong 3 · **Canada 2** · Taiwan, Israel, Shanghai, Shenzhen, Madrid, Korea, **Australia 1 each** · Norway, Belgium, Austria, Ireland, Portugal, India, Singapore **0**. Germany has 34 rows and the UK 6, against comparable universes of quality industrials — that gap is an artefact of the block order the project happened to run, not a judgment anyone made. The UK, Canada and Australia blocks are where the marginal name is most likely to be both new and analysable on existing machinery.

---

## Change log
- **v25 — 2026-09-04** — 6626.T (SEMITEC) v1 ANALYSE committed at register v286: **WATCH** — Past ADEQUATE (w-o-4 ROCE 14.6%, FCFROCE 9.2%; 5y record-limited), Future ADEQUATE (one contained strong force — Asian entrants in appliances/OA; switching-cost moat from design-in qualification, stable in automotive/medical; the customer-force call is the logged dissent line), SF PASS with zero flags (P19 **SOUND**: FY3/24–26 repurchases ¥3.8bn retiring 15.6% of shares at 3.0–7.0× EV/OI and 5–8× normalized FCF, cash-funded; DOE dividend; no M&A; P17 INDETERMINATE but bounded — no individual ≥ ¥100m vs an ¥84m P20-basis cap; Ishizuka family 46.1%; Seto-group RPT 2% of COGS). **P20 active** — capex/sales 3.4% → 10.3% with ¥5.4bn of plant guided for FY3/27–28; pre-cycle anchor 4.80%; maintenance FCF ¥1,683m vs strict ¥293m. FAIR at ¥2,449 (14.0× maintenance FCF, 7.3×/4.6× EV/OI); CHEAP < ≈ ¥1,403 (FCF leg binds both variants); Dist +75%, slotting between TROW and ADBE. **Primaries read directly** — FY3/26 yūhō via the kabupro EDINET mirror (`semitec.co.jp` HTML pages are robots-blocked but its PDF uploads and the mirror are not), two IR decks, Q3 tanshin; §4 acceptance test passed on four anchors for FY3/25–26. **Process finding:** for Japanese names, `kabupro.jp/edp/` serves the full EDINET PDF where EDINET itself and the issuer's HTML are unreachable — a reusable route. Intake block from Cluseau Research closed: 244920.KS AVOID, ABCA.PA AVOID, 6626.T WATCH. v24 archived → `queue/archive/TODO_v24_2026-09-04.md`.
- **v24 — 2026-09-04** — ABCA.PA (ABC arbitrage) v1 ANALYSE committed at register v285: **AVOID on Future WEAK** — three STRONG forces (fund allocators: AUM €265m → €245m in a +8–10% year; financing counterparties: leverage sits under prime-broker agreements inside the unconsolidated Quartys; competition for alpha: ROE 25–50% in 2007–11 → 10–18% since 2017), no moat source. Past ADEQUATE under the §2·1A substitution (company ROE 10y avg 15.8%; Σ NI/Σ equity 15.2–15.5%; EPS −3.3%/yr FY2021–25). SF PASS with one P19 CAUTION (Momentum 2028 €15–25m cumulative cost + scrip-dividend seed-capital plan; equity plans 7.4% of shares on a €15m hurdle); P17 CEO 0.36× cap, highest-paid employee INDETERMINATE; insiders 40.4% (the intake note's "54%" is the float). FAIR at €5.12 (12.2× NI, 1.80× BV); CHEAP < ≈€3.36 (8× NI; P/B 1.2× ≈ €3.41 converges). **Primaries read directly** — AFR 2025 pp. 1–38, results release, company data pages; §4 tier-2 test: S&P revenue anchor rejected (€59.94m vs €59.7m), NI/equity/net-cash anchors accepted; Fiscal.ai FY2021 balance sheet corrupt, rejected. Next-up item 2 struck; 6626.T remains. One named-re-test row added. IDEAS v3 adds ABCA.PA as a non-determinative A4 instance. v23 archived → `queue/archive/TODO_v23_2026-09-04.md`.
- **v23 — 2026-09-04** — 244920.KS (A Plus Asset Advisor) v1 ANALYSE committed at register v284: **AVOID on three gates** — Past WEAK (worst-of-four ROCE 4.4%, FCFROCE 1.1%, on a 5y record-limited window; robust to the NIBCL call), Future WEAK (customer and agent bargaining power both STRONG; carrier-concentration sentence not retrievable; moat eroding), SF FAIL (P17 hard strike: Chairman's FY2024 pay ≈₩985m vs caps ₩124m/₩94m on both reads, press-quoted from the business report; P19 CAUTION on non-core M&A, a ₩22bn FY2024 securities loss and an uncompleted first buyback). EXPENSIVE at ₩13,960 (EV/OI 16.1×/11.3×, MCap/FCF 14.5×); band ≈₩2,228–7,694, 71% wide on ₩140bn cash + ₩91.5bn NCI. **Process finding:** every Korean primary source is bot-blocked from the sandbox — the §4 acceptance test could not run and the S&P series is used provisionally; new standing flag under Flags with three options for the user; one named-re-test row added. Next-up item 1 struck; ABCA.PA and 6626.T remain. v22 archived → `queue/archive/TODO_v22_2026-09-04.md`.
- **v22 — 2026-09-04** — **External-idea intake, user-directed to the top of the queue.** Three ANALYSE seeds from Cluseau Research, "Buying the Buyback" (3 Sep 2026): A Plus Asset Advisor `244920.KS`, ABC arbitrage `ABCA.PA`, SEMITEC `6626.T` — new `## ▶ Next up` block above the dated re-tests. All three keys are on the §7.1a suffix table; §7.1a prior-check on company name against the 320 live register rows and this file: clean. Article figures carried only as labelled, unverified author claims; its price targets and weights not carried. Five further names the note cites as its own past trades are listed as **not seeded** (one investment holding, two banks). No register row touched; no memo written; no framework file touched. v21 archived → `queue/archive/TODO_v21_2026-09-04.md`.
- **v21 — 2026-09-04** — **RECONCILE-lite at register v280 — two corporate-action rows were stale on the day the 28-Aug batch was assembled.** (A) EA close fired: take-private completed 4 Aug 2026 at $210 cash, delisted → AVOID row moved to DNAF terminal, no tax event (not held). (B) PYPL lapse fired: Stripe/Advent dropped the pursuit 27–28 Aug (press only, no 8-K) → full REVIEW owed at ≈$54–57; v14's low-$40s premise struck. (C) Sep calendar corrected: CRM reported 26 Aug, NKE DEF 14A filed 15 Jul / AGM 8 Sep, FDS 30 Sep; PANW 10-K unfiled, UFI 10-K 26 Aug, GAP 10-Q 28 Aug, INTU 10-K unfiled as of 4 Sep. Register counts re-measured to actual rows (320 = W67/A251/D2 — v277–v279 front matter had understated WATCH by one). No memo written; no framework file touched.
- **v20 — 2026-09-01** — KSPI v3 committed at register v279. **A user-directed lens change, not a business change: WATCH → AVOID.** The §2·1A financial-institution substitution was set aside and the industrial machinery run instead; Past fails on leverage (L/E 340% FY2025 / 353% 1H26 against the 200% flag, with P6's carve-out unmet because the borrowing is retail deposits funding a loan book, not repurchase funding) and independently on a three-year uninterrupted ROCE decline. **The lens is the whole flip** — no deposit-taker passes the literal leverage test, and the balance-sheet condition v2 relied on still holds. Routed to IDEAS A2, of which this is now the most consequential instance: the first where the two readings give opposite *final verdicts* rather than one gate. **Three method findings.** (1) The user's directed cash-flow check was right to run and did not bear out as suspected — v2's FY2025 FCF of ₸491,098m correctly excluded the Hepsiburada consideration — but it exposed a larger problem: reported CFO embeds the loan-book/deposit gap, so FCF swings ₸1,056bn → ₸486bn → ₸491bn → ₸953bn on trading that did not move that way. TTM FCF is **₸952,971m**, taking MCap/FCF from v2's 18.7× to **9.6×**. Both bases now carried and labelled at every use. (2) **v2's EV/OI "n.m., 5.4×–11.4× spread" was an inconsistency, not uncertainty** — deposits added to EV while their interest cost stayed deducted from the denominator. Paired financing-blind the metric is 6.7×–7.8× and becomes the binding band leg. Worth sweeping any other memo that marked EV/OI n.m. on a deposit funder. (3) **A v2 data gap was a retrieval miss, not a disclosure gap:** Kaspi furnishes two 6-K exhibits within days of each other, and the interim financial-information exhibit carries a full IAS-34 cash-flow statement, the NCI split and the buy-back share count that v2 recorded as unavailable. Standing lesson: for foreign private issuers, check for a second 6-K before recording a disclosure gap. Band ≈$98 → ≈₸39,000/$86; Dist +8% → +21%. All figures computed in tenge — third-party USD/KZT quotes for late August diverge 455–477, so USD uses the ADS-implied cross of 454.89 and distances are FX-invariant. **Re-merged onto live head:** the session base was v18; a parallel 2026-08-28 recovery landed v19 (the 239-name coverage-audit and re-seed blocks) between fetch and PUT, and §7.4a base verification caught it — renumbered v19 → v20 with no work lost on either side. v19 archived → `queue/archive/TODO_v19_2026-08-31.md`.
- **v19 — 2026-08-31** — **The second orphaned 2026-08-28 file, recovered.** A parallel session that day built its own TODO **v17** on the same live v16 base as the re-test batch — same number, different base, neither pushed because both sessions hit the identical dead write leg (`api.github.com` 502/403). The re-test batch was recovered first (v18); this is the other half. Additive only, exactly as its manifest promised — nothing in v16 or v18 is deleted or rewritten. Adds: **a global top-100 coverage audit** (58 uncovered names, tiered A 37 ordinary / B 12 financials needing the §2·1A substitution basis / C 9 state-controlled where the SF gate is structurally compromised); **an ANALYSE queue re-seed of 181 candidates across 15 markets**, de-duplicated on company name against every register row per §7.1a; the rewritten `Re-seeding` section (option (c) now carries stock); two corporate actions (ABB/Rotork ~$5.5bn confirmed 16 Jul 2026; two candidate-stage take-private strikes); and six flags. **Blocking item, not resolvable here: 23 of the queued names have no §7.1a key** — the suffix table carries nothing for India (`.NS`), Ireland (`.IR`), Portugal (`.LS`), Saudi Arabia (`.SR`) or Abu Dhabi (`.AE`). The key doubles as the SWEEP price lookup, so it cannot be patched per-name at ANALYSE without breaking that guarantee. This is a MODEL change and needs a dedicated session and the exact words "commit model" — never inferred, never bundled. `2222.SR` and `IHC.AE` are among the blocked. Two further flags carried forward: the **Banco Santander key collision** (`SAN.PA` is already Sanofi — Santander must key `SAN.MC`), and **PAT rotation, now unactioned across four sessions.** **Carried forward verbatim in substance from the re-seed's own v17 entry, which never became a committed version and would otherwise be lost:** the coverage audit was matched on company name and cross-listing per §7.1a against all 317 then-live rows and found **42 of the top 100 covered, 58 not** (source: companiesmarketcap.com global ranking, retrieved 2026-08-28 — ranks only, no market-cap figures carried, tier-3 under §4 and adequate for a coverage question); it is framed explicitly as **coverage completeness, not a candidate screen — size is neither a quality nor a cheapness signal**. The corporate-action pass over the candidate block caught **three live take-privates the name-generation pass had called clean** — Rotork (ABB, ~$5.5bn, 16 Jul 2026), Intertek (EQT £60.00 cash, Rule 2.7 on 18 Jun 2026, shareholders approved 6 Aug 2026), Steadfast (Amwins/Dragoneer/KKR, A$6.00 cash, ~21 Aug 2026) — all struck. **Two process findings worth keeping:** a first-pass "clean" means only "clean by that route", the v16 retrieval lesson restated on the queue side; and the Rotork deal was already sitting inside the register's own ABB row, matching only because the de-dup ran over row text rather than the ticker column — a de-dup keyed on the ticker column alone would have missed it. The re-seed's own `## PUSH-STATE` section is dropped as spent — the state it described no longer exists. Two stale register references corrected v276/v277 → v278. v18 archived → `queue/archive/TODO_v18_2026-08-31.md`.
- **v18 — 2026-08-31** — **The blocked 2026-08-28 batch, recovered and re-merged.** Seven REVIEWs closed at register v278 (TRI v3, 7936.T v3, INTU v2, STMN.SW v3, ZIP.AX v2, HEXA-B.ST v3, GAP v2). One verdict moved — **STMN.SW WATCH→AVOID**, SF PASS→FAIL on a P19 ADVERSE (H1-2026 treasury purchases CHF 69,328k, 2.8× the FY2025 full year, unexplained, located in the interim statements the v2 session could not reach). One gate cleared — **HEXA-B.ST SF FAIL→PASS**, v2's P19 strike being a pre-v4 mechanical-ladder artefact against nil repurchases since 2023; AVOID narrows to Past alone. TRI, 7936.T and INTU held WATCH; ZIP.AX and GAP held AVOID with a new P19 CAUTION on GAP. **Why this sat for three days:** the 2026-08-28 session's write leg was dead — `api.github.com` 502 through the sandbox proxy, `git push` 403 on the authorized-repo set — so eleven files were staged as §6.5 paste-blocks and nothing was pushed. Read access was fine, which is what made the batch trustworthy on recovery. The staged register was numbered v277 against a v275 base; live had since moved to v276 (SEE.L) and v277 (FLUT), so the seven rows were re-merged memo-wins onto live head and renumbered v278, and the staged TODO v19 became v18 — its own draft v17/v18 never existed as committed versions and are collapsed into this entry. **Standing lesson:** a staged batch is not a committed batch, and a version number assigned before the push is a guess. Any session ending in paste-blocks must leave the recovery instruction where the *next* session will trip over it — the register or TODO change log, not only a manifest file. v17 archived → `queue/archive/TODO_v17_2026-08-31.md`.
- **v17 — 2026-08-31** — FLUT (Flutter Entertainment) v1 ANALYSE committed at register v277. AVOID on three gates: Past WEAK (worst-of-four normalized ROCE 1.08% — $1.1bn of cumulative FY2021–25 operating income against a >$20bn capital base that is 78% goodwill and acquired intangibles; L/E 216.7%; BV/sh −10.3% p.a.), Future WEAK (4/4 forces STRONG; supplier breadth FAIL on the look-through call that the licensing state is the effective supplier; moat eroding), SF FAIL (P19 **ADVERSE** — FY2025's $1,123m of repurchases priced at 78–107× on all four reads, debt-funded alongside $2,688m of M&A against $412m of framework FCF; programme still live in H1 2026 at 32–54× with no published price criterion). **Two method findings worth keeping.** (1) The aggregator's capex line carried property and equipment only ($105m FY2025) and its headline FCF of $1,079m omitted $667m of intangible and capitalised-software purchases — framework FCF is $412m, a 2.6× overstatement that would have moved MCap/FCF from 42.9× to 16.4× and, on a marginal name, the verdict; the §4 tie-out passed on four exact FY2025 anchors and still did not protect the capex line, so **anchors validate balance-sheet splits, not cash-flow definitions**. (2) P17's dual read ran half-blind on both legs (net income negative in FY2025 and on the 3y average) and the CEO's $19.70m came within 4% of the $20.6m fiscal-year bar on the corrected FCF basis — on the aggregator's inflated FCF the bar would have been $54.0m. A rejected data basis can acquit as easily as convict. One backfill row added (Snai pre-deal OI INDETERMINATE, proxy director fees + RPT, FY2025 statements direct from the 10-K, buyback share count, ISIN), plus a US-domestic-filer retrieval addendum. v16 archived → `queue/archive/TODO_v16_2026-08-27.md`.
- **v16 — 2026-08-27** — *(entry reconstructed at v17: v16 bumped the header and added the GPN backfill block but committed no change-log line — an integrity gap, logged rather than silently carried.)* GPN (Global Payments) v1 ANALYSE committed at register v275, AVOID on three gates. One backfill block added: FY2016–FY2020 record rebuild, 2026/2027 proxy backfill including the CEO-comp extraction conflict, FY2021–25 repurchase share counts, the Worldpay EBITDA multiple as a lower bound on pre-deal EV/OI, and ISIN verification. v15 archived → `queue/archive/TODO_v15_2026-08-27.md`.
- **v15 — 2026-08-23** — LULU (lululemon) v3 REVIEW committed at register v269. Verdict AVOID unchanged but now on **one gate** (Future WEAK): v2's mechanical P19 hard strike was re-tested under the v4.0.0 §2·1C·3 judgment protocol and flipped **SF FAIL → PASS (1 flag, capital-allocation CAUTION)** — ADVERSE fails its still-expensive conjunct (stock 5.6–6.3× EV/OI; the live Q1 FY2026 tranche executed at $162.86 ≈ 7.6–7.8× EV/OI, the bargain line), the FY2023–24 overpayment held as pattern evidence. LULU is the fifth of the v4.0.0 §8.4 pure-SF P19 flips (PYPL was the fourth, same session). One backfill row added: FY2016–FY2020 window rebuild (lifts the 5y record-limited cap, previously unrouted) + O'Neill's FY2026 comp package (P17, once disclosed). ISIN backfilled (US5500211090). Calendar token corrected — the 3 Sep print is Q2, the last pre-O'Neill quarter (she is effective 8 Sep), not her first. Band ≈$64 unchanged. Re-merged repeatedly this session through §7.4a base-verification collisions with parallel KSPI, BKE and PYPL commits; memo PUT was independent and already committed. v14 archived → `queue/archive/TODO_v14_2026-08-23.md`.
- **v14 — 2026-08-23** — PYPL (PayPal) v3 REVIEW committed at register v268. One corporate-action row added: the press-reported Stripe/Advent approach ($60.50 rejected; no 8-K, unconfirmed) — deal-completes and deal-lapses branches both named, since a lapse puts the pre-bid price inside the all-cash band with no gate improved. Process note: v2's SF FAIL was a **pure artefact of the retired P19 strike ladder** — re-run under the v4.0.0 judgment protocol the same evidence gives CAUTION and the gate passes. This is the fourth such flip; the v4.0.0 §8.4 scan flagged ~44 P19-driven pure-SF AVOIDs still carrying pre-v4 verdicts, and PYPL confirms the scan list is real work, not housekeeping. Also logged: repurchase timing vs the undisclosed sale process is INDETERMINATE — re-test at the FY2026 10-K. v13 archived → `queue/archive/TODO_v13_2026-08-23.md`.
- **v13 — 2026-08-23** — KSPI (Kaspi.kz) v2 REVIEW committed at register v266. One backfill row added: FY2016–FY2020 rebuild (record-limited 5y window — liftable, unlike a history-limited cap), ISIN, and four INDETERMINATE items (1H26 repurchase count, outside-director fees, 1H26 owners/NCI split, interim intangibles split). Process note: v1 was pre-v3 and priced a deposit-funded lender on the industrial CE/EV/TBV machinery; the §2·1A substitution rule moved the band $42–52 → ≈$98 and Dist +67% → +8% with **no change in the business**. Worth a standing check — any pre-v3 memo on a bank, insurer or securities-heavy holdco carries the same latent error. Candidates to sweep for it at next touch: the financial-institution rows generally (BRK.B, INVE-B.ST, AZA.ST, NU, IBKR). v12 archived → `queue/archive/TODO_v12_2026-08-18.md`.
- **v12 — 2026-08-18** — KEX (Kirby) v1 ANALYSE committed at register v261. One backfill row added: 10y record rebuild (window is 5y record-limited — SEC/aggregator retrieval limits logged in memo App A), backvaluing worksheet, and the two unmeasured P19 tranche years (FY2022, FY2024). Also logged at commit: register v258–v260 (ASH, APTV, XRAY) left the front-matter counts drifting one low and the AVOID section header five low; re-measured and corrected at v261 (313 = WATCH 69 · AVOID 243 · DNAF 1). Three-way parallel-commit collision detected by §7.4a base verification and re-merged onto live head; memo PUT was independent and not re-run.
- **v11 — 2026-08-18** — APTV (Aptiv) v1 ANALYSE committed at register v258. One named re-test row added: FY2016–FY2018 window extension (record-limited cap; pre-Dec-2017 perimeter is Delphi Automotive incl. Powertrain, so a clean 10y window first exists at FY2027), continuing-ops FY2025 OI for a TTM band base, and three INDETERMINATE SF items (RPT, director fees, insider ownership). Routed here rather than to the register per §7.1. Versigent (EDS) spin 1 Apr 2026 logged as a perimeter break under HOG treatment — the FY2026 10-K is the first clean post-spin record. v10 archived → `queue/archive/TODO_v10_2026-08-18.md`.
- **v10 — 2026-08-18** — **Open-items migration (register v257 RECONCILE).** The register's 108-item `## Open items` section was cleared to 3 user-decision one-liners; every work item landed here: the "Named re-tests & backfills" table (≈50 names, one line each), the Corporate actions / RECONCILE queue (sweep OVERDUE, BBBY→NXH, INPST.AS, Lex Asea, EA), overdue markers on 7936.T (14 Aug, unworked) and HEXA-B.ST (29 Jul re-base), and standing session rules pending MODEL v4.2.0. Calendar carried from v9 with the Q1–Q2 2027 detail pointer re-aimed at this file (the register no longer carries the detail). Framework questions went to **`queue/IDEAS.md` v1 (new)** — 7 verdict-affecting entries with book-grounded recommendations, 6 codifications in the v4.2.0 draft, calibration observations. Runner-design guardrails gain the commit-time compliance re-measure and the retrieval doctrine from the Aug-2026 runs. Purpose statement rewritten: this file is the single work sink; nothing routes to the register's Open items again. v9 archived → `queue/archive/TODO_v9_2026-08-09.md`. User decisions folded same-day (2026-08-18): Cartara→CERT confirmed (flag closed); HFG SELL-FLAG deferred to FY2026 results; entry dates waived (portfolio cells "n/a — not tracked"); MODEL session on IDEAS A1 scheduled.
- **v9 — 2026-08-09** — Two REVIEWs committed at register v249 (NET v2, ZBRA v2, both AVOID unchanged); fold-in obligations closed; NET converts item added (~Nov); ZBRA band ≈$68–72, FY2026 10-K now a P19 re-test with a named ADVERSE path; ZIP.AX 20 Aug restored to Priority; queue status CLOSED; three process findings logged. v8 archived.
- **v8 — 2026-08-09** — **THE ANALYSIS QUEUE IS CLOSED.** 94-name backlog fully worked (62 at register v247 + 29 in this commit + flag resolutions); every market block closed; ZM struck as duplicate; BBBY resolved by evidence; "Cartara"→CERT by assumption (confirmation owed); calendar refreshed against v248; re-seeding is a user decision. v7 archived.

*Older logs: `queue/archive/` TODO_v* snapshots.*
