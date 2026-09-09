# EVIDENCE NOTE — Verisure plc (`VSURE.ST`)

**Status at extraction (2026-09-09):** no live row.
**Provenance:** extracted verbatim from the 2026-09-05 → 09-08 scheduled-run drafts listed below, which were written against a framework **reconstructed from the book, not from the live `MODEL.md`** (TRACK/PASS verdicts, "ROIC"/"invested capital" on the drafts' own basis, EV/EBIT trigger lines). **Every verdict, gate call, multiple and trigger in those drafts is void and has been dropped by construction here; only sections carrying sourced figures, tables, business description, open data gaps and sources are carried.** Figures labelled `[computed]` are the drafts' own arithmetic on their own basis — re-derive under §2·1A/§5, never adopt. Tier-2 figures still require the §4 acceptance test; anything below is a starting point for retrieval, not an accepted series.
**Key:** `VSURE.ST` per §7.1a suffix convention (the drafts used exchange-prefix keys, e.g. `OM:`, `SWX:`, `XTRA:`). Run the §7.1a prior-check on company name + ISIN before any ANALYSE. IPO Oct 2025 — history-limited window certain; PE-era leverage and subscriber-acquisition capitalisation are the Gate 1A questions.
**Delete this file once the proper memo is committed** (routing per `queue/TODO.md` v26).

**Source drafts:** `claude_2026-09-05_memo_VSURE_verisure_v1.md`, `claude_2026-09-06_research_krones-verisure-evidence-triggers_v1.md`

---


## ⟪ from `claude_2026-09-05_memo_VSURE_verisure_v1.md` ⟫

### Verdict — *sourced lines and tables only; verdict prose dropped*
Verisure is the first name in this queue where a genuinely good operating business trades at a multiple a value framework can engage with: **8.0x EV / LTM adjusted EBITDA, 4.0x EV / ARR, 31% below its October 2025 IPO price** `[computed]`. The installed base is a 74.1%-margin annuity `[sourced]` with attrition that has been flat at 7.4% for three years — against roughly 12% for other monitored-alarm operators on the company's own benchmarking `[claim]`. The private-equity balance sheet has been substantially dismantled: net debt fell from €7,587m to €4,913m, leverage from 4.9x to 2.7x, and the ratings went B1/B+ to Ba1/BB+ and then to a first investment-grade BBB− from Fitch in June 2026 `[sourced]`.
**But I am not recommending diligence, because gate 2 turns on a number the company does not disclose.** Verisure capitalises roughly a third of what it spends acquiring each customer, and since January 2022 it has amortised those capitalised costs straight-line and **no longer writes them off when the customer cancels** `[sourced, Midholding AR 2022]`. **The amortisation life is not stated in any primary source I could reach.** A widely-cited third-party figure of 15 years is unverified. That single input determines whether reported earnings mean anything and how much of the €3,947m customer-portfolio intangible is exposed if attrition rises.

### Gate 1 — Do I understand it?
**Pass, and the segment disclosure is unusually good.**

Verisure installs monitored alarm systems in homes and small businesses and charges a monthly subscription. It is #1 in nine of its top ten geographies `[claim]` and, per the IPO prospectus, its portfolio was **"over five times larger than the second largest player"** in Europe at end-2024 `[sourced]` — independently corroborated by Berg Insight, which ranks the European monitored market Verisure, Prosegur, EPS/Homiris, Sector Alarm `[sourced]`.

Critically, the company reports the two halves of the business separately, which is exactly the disclosure this model needs:

| Q2 2026 `[sourced]` | Revenue | Adjusted EBITDA | Margin |
|---|---|---|---|
| **Portfolio Services** (the installed base) | €913.2m | **€676.6m** | **74.1%** |
| **Customer Acquisition** (the growth engine) | €84.2m | **−€214.0m** | — |
| Adjacencies | — | €5.1m | — |
| **Group** | €1,023.6m | €467.7m | 45.7% |

**This is the single most important structural fact in the file.** Group EBITDA margin of 45.7% is the net of a 74%-margin annuity and a loss-making customer-acquisition operation. The reported margin understates the base and overstates nothing — the opposite of the usual situation.

Geography `[sourced, FY2025]`: Iberia & Nordics €1,998.9m, Other Europe €1,340.4m, Latin America €344.9m (9%), Central & other €61.2m. Note **Iberia and Nordics are reported as one segment**, so France- or Spain-only lines do not exist, and **EBITDA by geography is not disclosed at all** — the company segments profitability by business model, not region.

---

#### The unit economics, as disclosed
| Metric | Q2 2026 | Q2 2025 | FY2025 | FY2024 |
|---|---|---|---|---|
| Customers (k) `[sourced]` | 6,377 | 5,831 | 6,171.4 | 5,611.7 |
| ARPU (€/month) | **48.2** | 46.6 | 46.6 | 45.6 |
| EPC — EBITDA per customer (€/month) | **35.71** | 34.4 | 34.3 | 33.1 |
| **Attrition, LTM** | **7.4%** | 7.4% | 7.4% | 7.4% |
| **CPA (€)** | **1,644** | 1,474 | 1,514 | 1,438 |
| **Acquisition multiple** | **3.8x** | 3.6x | 3.7x | 3.6x |
| CPA capitalisation rate | **32.8%** | 35.4% | 35.5% | 36.8% |

The company's cohort claim: ~15-year average customer lifetime and an estimated **~20% unlevered IRR over 15 years** `[claim]`. A 7.4% attrition rate implies a mean life of **13.5 years** `[computed]`, so the 15-year assumption is not obviously stretched. **Attrition flat at 7.4% through 2023–2026 is the strongest single fact in the bull case** — it is the load-bearing assumption and it has held through a European consumer squeeze.

#### But three things are moving the wrong way — *sourced lines and tables only; verdict prose dropped*
**First, the acquisition multiple is at the top of its own historic corridor.** CPA rose **+11.6% year on year** in Q2 2026 (+8.5% excluding rebranding) while EPC rose only **+3.8%** `[sourced]`. The multiple has drifted 3.6x → 3.7x → 3.8x, and the company's stated historic corridor is **3.3x–3.8x** `[claim]`. Verisure is paying more per customer and earning proportionally less from each one. Management's defence — *"chasing easy volume today is just tomorrow's attrition"* `[commentary, Q2 2026 call]` — is credible and also concedes the point.
**Second, ARPU has no real pricing power.** The company's own disclosed **10-year ARPU CAGR is 2.0%** `[sourced]`, and recent growth is +2.4% constant currency. **That is a business raising prices at or slightly below eurozone inflation.** Management states there is *"NO frontbook-backbook dynamic"* — new customers join at portfolio ARPU `[claim]` — which is genuinely good (no hidden repricing cliff) but also means there is no latent pricing reservoir to harvest. **Any thesis requiring ARPU to outrun inflation is assuming something the ten-year record does not show.**
**Third, the organic front end is close to flat.** Gross new installations grew **+0.6% year on year in Q2 2026** (218.6k vs 217.3k) and +1.6% in H1 `[sourced]`. Total customers are still +9.4%, but that is a slowly-churning base plus the acquired ADT Mexico portfolio — which itself added **~7bps to attrition** `[sourced]`. ARR growth of +12.2% is running well ahead of new installations, meaning growth is increasingly price and acquisition rather than organic addition.

#### Returns on capital — the fork
| Measure `[computed]` | Value |
|---|---|
| Invested capital (equity €8,913.5m + net debt €4,912.8m) | €13,826m |
| Return on invested capital, on LTM adjusted EBIT €1,032.1m | **7.5%** |
| Return on invested capital, on FY2025 IFRS operating profit €298.7m | **2.2%** |

Both are true and they measure different things. The *cohort* economics are excellent — 3.8x acquisition multiple, ~20% claimed unlevered IRR. The *entity* earns 7.5% pre-tax on the capital actually committed, because successive leveraged buyouts left **€7,722.6m of goodwill and €3,947.1m of customer-portfolio intangible** on the balance sheet `[sourced, 30.06.2026]`. **Intangibles are 80.1% of total assets and tangible book is roughly −€4,176m** `[computed]`.

This is the third name in this run with the same shape — Alimak (ROCE 10% including goodwill, 22.7% excluding) and Mips post-Koroyd. In each case a good operating business sits inside an entity capitalised at a level that makes the consolidated return ordinary. **The framework has to price the entity, not the cohort.**

#### The accounting question — the hard gate
Verisure capitalises two things `[sourced]`: alarm equipment installed at customer premises (tangible fixed assets, where it retains ownership), and the incremental direct costs of obtaining new customer contracts (intangible fixed assets).

The good news is better than a sceptic would assume: the **CPA capitalisation rate is 32.8% and falling from 35.4%** `[sourced]` — roughly two-thirds of acquisition spend is already expensed through EBITDA, which is why Customer Acquisition shows −€214.0m. FY2025 customer-acquisition capex was €597.9m of €981m total group capex `[sourced]`, so ~61% of all capex is subscriber acquisition rather than maintenance.

**The gap is the amortisation life.** The Midholding 2022 annual report discloses only that from January 2022 the group *"simplified our treatment of direct costs … which are no longer written-off upon customer cancellation. Instead … these capitalized costs now follow a straight-line amortization approach (over a shorter life period than before)"* `[sourced]`. **No primary source states the number of years.** An independent analyst asserts 15 years and equipment write-downs at ~4% of sales `[claim, unverified]`.

Straight-lining acquisition intangibles over a long life while no longer writing them off on cancellation is precisely the policy that flatters early-year earnings and leaves little headroom if attrition rises. **This is the number to demand.**

The IFRS check keeps everything honest: **Verisure plc lost €255.9m in FY2025 and €184.9m in FY2024**, and only turned a €65.7m profit in H1 2026 after the interest bill collapsed `[sourced]`.

#### Financial strength
**Pass, and this is the strongest part of the file.** The transformation is real, not cosmetic `[all sourced]`:

- Net debt €7,587m (Dec 2024) → **€4,912.8m** (Jun 2026), −€2,674m
- Leverage **4.9x → 2.7x**, inside the 2.5–2.75x 2026 guidance
- Ratings B1/B+ → Ba1/BB+ (Oct 2025) → **first investment grade, Fitch BBB− (Jun 2026)**
- Weighted average cost of debt 4.9% → **~4.25%**, with €200–220m of annual interest savings vs 2024, guided to the upper end
- **No debt maturities until May 2030** `[commentary, Q2 2026 call]`
- The 7.125% legacy pre-IPO bond and the 5.250% 2029 notes are both retired

Two residual observations. **Cash is remarkably thin at €36.7m** against €4.9bn of debt — normal for a working-capital-negative subscription model, but there is no buffer independent of the €950m revolver (€944m total liquidity). And **the deleveraging came overwhelmingly from the €3.1bn equity raise, not from cash generation** — which is the correct way to read it.

---

### Gate 3 — Is it cheap? — *sourced lines and tables only; verdict prose dropped*
Inputs `[sourced]`: price €9.146 (2026-09-04, MarketScreener); 1,033,962,264 shares outstanding (30.06.2026); net debt €4,912.8m (30.06.2026).
| Measure | Value |
|---|---|
| Market capitalisation | **€9,457m** `[computed]` |
| Enterprise value | **€14,369m** `[computed]` |
| **EV / LTM adjusted EBITDA (€1,803.1m)** | **8.0x** `[computed]` |
| LTM adjusted EBIT (952.9 − 466.6 + 545.8) | €1,032.1m `[computed]` |
| **EV / LTM adjusted EBIT** | **13.9x** `[computed]` |
| **EV / ARR (€3,619.8m)** | **4.0x** `[computed]` |
| LTM free cash flow (−54 + 97.3 + 95.3) | €138.6m → **1.5% yield** `[computed]` |
| LTM adjusted EPS (0.35 − 0.15 + 0.28) | €0.48 → **P/E 19.1x** `[computed]` |
| IFRS earnings | **Loss-making FY2024 and FY2025** `[sourced]` |
| EV per customer (6,377k) | €2,253 `[computed]` |
| Price vs €13.25 IPO | **−31.0%** `[computed]` |
**The free-cash-flow yield of 1.5% is the number that stops this being a buy today, and it is also the number most likely to be misread.** Reported FCF is suppressed by discretionary growth spend, not by a weak business — the company itself presents a bridge (*adjusted operating cash flow → less customer acquisition → less attrition-replacement investment → **adjusted operating cash flow before portfolio growth** → less organic growth investment → FCF*) designed to make exactly that argument `[sourced]`.
**But the populated euro split between "attrition replacement" and "organic growth" investment is not disclosed** `[sourced absence]`. That split is the difference between a business whose maintenance capex is modest and steady-state cash flow is large, and one where most of the spend is simply standing still against 7.4% churn. **I will not estimate it, and no steady-state FCF figure appears in this memo as a result.** It is the second question for IR and it is arguably more important than the first.

### Open items and data gaps
- **Amortisation life of capitalised customer-acquisition costs: not disclosed in any primary source.** The "15 years" in circulation is an unverified third-party claim. Equipment depreciation life likewise not found.
- **Euro components of the "adjusted operating cash flow before portfolio growth" bridge: not disclosed.** Structure published, figures not.
- **Hellman & Friedman's current stake: not found on any post-31-December-2025 basis.** The August 2026 placing seller was not named; one broker assessed it as an IPO anchor investor rather than the sponsor `[claim]`.
- **Net subscriber additions are derived, not disclosed** (FY2025 +559.7k, Q2 2026 +99k, both arithmetic on two sourced figures).
- **A euro lifetime-value figure is not published** — the company expresses lifetime value as an unlevered IRR only.
- **EBITDA or margin by geography: not disclosed.** France- and Spain-only revenue lines do not exist (Iberia & Nordics is one segment).
- **A Verisure market-share percentage: not disclosed** — only penetration of TAM/SAM and the relative "5x the second largest" statement.
- Year-by-year debt maturity schedule not found (only "no maturities until May 2030"); Term Loan A and B maturity dates and margins not found.
- **Unresolved inconsistency:** the Q2 2026 report lists Senior Secured Notes of €525.0m at 4.125% due 2032, while the Q2 earnings release describes a post-period **€1,000m** note at the same coupon and maturity issued to repay the 5.250% notes. May be two tranches or an extraction artefact — **verify against the audited note.**
- The strongest published bear case is an independent research Substack, flagged as outside the project source hierarchy; its two key accounting claims are unverified against filings. A JP Morgan Overweight with an €18.40 target (18 Nov 2025) is badly stale against a €9.15 price and is recorded as market context only.
- No screener or third-party fair-value model was used.

### Sources
- [Verisure Q2 2026 earnings release (2026-07-30)](https://www.verisure.com/system/files/private_pdf/2026-07/verisure-plc-earnings-release-q2-2026.pdf)
- [Verisure Q2 2026 report](https://www.verisure.com/system/files/private_pdf/2026-07/verisure-plc-report-q2-2026.pdf)
- [Verisure Q2 2026 results presentation](https://www.verisure.com/system/files/private_pdf/2026-07/verisure-plc-results-presentation-q2-2026.pdf)
- [Verisure Q2 2026 earnings call transcript](https://www.verisure.com/system/files/private_pdf/2026-07/verisure-plc-q2-2026-earnings-call-transcript.pdf)
- [Verisure Q4 2025 earnings release (2026-02-12)](https://www.verisure.com/system/files/private_pdf/2026-02/verisure-plc-earnings-release-q4-2025.pdf)
- [Verisure Q4 2025 report](https://www.verisure.com/sites/gv/files/news_files/q-report-verisure-plc-q4-2025-260211.pdf)
- [Verisure company presentation, November 2025](https://www.verisure.com/system/files/private_pdf/2025-11/verisure-company-presentation-2025.pdf)
- [Verisure IPO pricing announcement (2025-10-08)](https://www.verisure.com/press-releases/regulatory/verisure-announces-the-offering-price-for-its-initial-public-offering-which-has-been-set-at-eu13-25-per-share-trading-on-nasdaq-stockholm-commences-today)
- [Verisure prospectus and price range announcement](https://www.verisure.com/press-releases/regulatory/verisure-announces-price-range-and-publishes-prospectus-for-its-initial-public-offering-on-nasdaq-stockholm)
- [Verisure largest shareholders (31.12.2025)](https://www.verisure.com/largest-shareholders)
- [Moody's and S&P upgrades following IPO (2025-10-21)](https://www.verisure.com/press-releases/verisure-credit-rating-upgraded-by-moody-s-and-s-p-following-initial-public-offering)
- [Fitch first investment-grade rating (2026-06-16)](https://news.cision.com/verisure-plc/r/verisure-assigned-its-first-investment-grade-rating-by-fitch,c4364483)
- [Verisure Midholding AB annual report 2022 (acquisition-cost accounting policy)](https://www.verisure.com/system/files/private_pdf/2025-08/verisure-midholding-group-annual-report-2022.pdf)
- [Verisure Midholding AB Q4 2024 report](https://www.verisure.com/system/files?file=private_pdf/2025-02/verisure-midholding-ab-quarterly-report-q4-2024.pdf)
- [Berg Insight, Home and Small Business Security System Market, 15th ed. (Feb 2026)](https://media.berginsight.com/2026/02/02170356/bi-security15-ps.pdf)
- [MarketScreener — VSURE quote, 2026-09-04](https://www.marketscreener.com/quote/stock/VERISURE-PLC-196294215/)
- [MarketScreener — August 2026 accelerated bookbuild](https://www.marketscreener.com/news/verisure-slides-after-shareholder-sells-stake-at-a-discount-ce7f50dfdd80f225)
- [MarketScreener — lock-up expiry commentary (2026-04)](https://www.marketscreener.com/news/dnb-carnegie-slim-prospects-for-verisure-divestments-following-lock-up-expiry-di-ce7e51d3dc8efe23)

*Framework output, not investment advice.*


## ⟪ from `claude_2026-09-06_research_krones-verisure-evidence-triggers_v1.md` ⟫

#### 1.1 The ROCE series: ANSWERED, and better than the item asked for — *sourced lines and tables only; verdict prose dropped*
|Period|ROCE|Source|
|---|---|---|
|FY2020|**−2.2%**|Krones Corporate IR Presentation 2025|
|FY2021|**10.0%**|same|
|FY2022|**14.1%**|same|
|FY2023|**16.3%**|same; corroborated by the 2028-targets release (3 Jul 2024)|
|FY2024|**18.2%**|same|
|FY2025|**19.1%**|Annual Report 2025, "Strategy and management system"|
|Q1 2026|17.6% (PY 20.5%)|Q1 release, 8 May 2026|
|H1 2026|**17.7% (PY 19.0%)**|H1 release, 29 Jul 2026|
|FY2026 guidance|19–20%|H1 release, 29 Jul 2026|
|2028 target|>20%|2028-targets release, 3 Jul 2024|

#### 1.3 The lifecycle-service split: CONFIRMED NOT DISCLOSED
Checked in three primary documents — the Corporate IR Presentation 2025, the Annual Report 2025 strategy section, and the H1 2026 release. **None discloses LCS revenue in euros, LCS as a share of group revenue, or LCS margin against new-machine margin.**

What *is* disclosed is qualitative and adjacent:

- ">1,000 MSAs" (modular service agreements) and ">200 lines connected", growing at **>15% CAGR 2021–2025** — Corporate IR Presentation 2025
- the stated ambition that "in the medium to long term, three out of every four new machines and lines will be supported by our own service team" — Annual Report 2025

**Read carefully, the second of those is an admission.** A company targeting three-in-four service attachment *in the medium to long term* is telling you it is not there now, and it declines to say where it is. **The growth rate is disclosed and the base is not.** That is a deliberate disclosure choice, and it means the LCS question cannot be resolved from public filings by any amount of further searching.

**Effect on the queue:** item 4's first half stops being a research task and becomes an IR question — which is where it started. **Do not re-attempt it as desk research on a future run.** The two IR questions to ask are: LCS revenue in EUR for FY2025, and LCS gross or contribution margin against the group average.

#### 2.1 The capex definition: ANSWERED — *sourced lines and tables only; verdict prose dropped*
|Q1 2026|EUR m|
|---|---|
|Capex — intangible assets|130.3|
|Capex — property, plant & equipment|127.6|
|**Total capex**|**258.2**|
|of which customer acquisition, material|85.8|
|of which customer acquisition, direct cost|68.6|
|**Customer acquisition, total**|**154.4**|

#### 2.4 A mechanical event the register must handle: Verisure goes ex-dividend this week
Verisure declared its **first** dividend on **30 July 2026**: €0.10 per share, ~€103m total, **record date 10 September 2026, payment 17 September 2026** — so the shares go ex on or about **9 September 2026**.

**€0.10 on the EUR 9.15 close is 1.09%.** *Arithmetic on two sourced figures.*

This is not a verdict event and it fires no review. It is a register-hygiene item: **from 9 September, any price comparison spanning the ex-date — including the "% above 52-week low" column proposed last run — steps down about 1.1% for reasons that have nothing to do with the business.** Verisure's own trigger is evidence-based and unaffected. Flagged so it is not mistaken for a move.

---

### 3. What this changes in the queue — *sourced lines and tables only; verdict prose dropped*
|Item|Was|Now|
|---|---|---|
|**4a — Krones LCS split**|top research item|**IR only.** Confirmed undisclosed across three primary documents. Do not re-attempt as desk research.|
|**4b — Krones ROCE series**|top research item|**Done.** FY2020–FY2025 obtained with the definition. FY2019 outstanding and low-value.|
|**NEW — Krones ROCE basis**|—|**Quantify the goodwill exclusion against the balance sheet.** Desk task, one subtraction. Feeds a new MODEL question on gate 2.|
|**5a — Verisure capex definition**|file-deciding|**Done**, and it produced a sharper replacement question: gross adds vs net adds, and cost per gross add.|
|**5b — Verisure amortisation life**|file-deciding|**Not found in four documents.** Check the AR 2025 intangibles note on a PC first; then IR.|


---
*Evidence note — not a memo, not investment advice.*
