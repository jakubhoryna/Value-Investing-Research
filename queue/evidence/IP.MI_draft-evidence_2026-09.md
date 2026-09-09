# EVIDENCE NOTE — Interpump Group S.p.A. (`IP.MI`)

**Status at extraction (2026-09-09):** no live register row. **Provenance:** primary-sourced candidate dossier sections from the 2026-09-08 → 09-09 scheduled runs (those runs had read the live MODEL v4.2.0 or worked evidence-only). No verdict, gate or computed GSC figure is carried; return-on-capital variants in these dossiers are the runs' own constructions — recompute under §2·1A. Serial acquirer (FY2025 organic −0.7% vs +2.3% acquired, per dossier) — Gate 1C acquisition audit; EUR 59.3m gap between cash-netted net debt and stated NFP to reconcile.
**Delete this file once the proper memo is committed** (routing per `queue/TODO.md` v26).

---
### ⟪ `claude_2026-09-08_register-flags-FX-route-and-candidate-dossiers_v1.md` → 5.1 Interpump Group (BIT:IP) — Bucket Q priority 2 ⟫
**Source: FY2025 preliminary results presentation, 13 February 2026, from the company's own document store** `[primary]`.

| Measure | FY2025 | FY2024 |
|---|---|---|
| Net sales | **EUR 2,070.7m** (−0.4%) | EUR 2,078.4m |
| — organic / acquisitions / FX | **−0.7% / +2.3% / −2.0%** | |
| Hydraulics | EUR 1,355.0m (−3.7%; organic −4.1%) | EUR 1,407.5m |
| Water Jetting | EUR 715.7m (+6.7%; organic +6.3%) | EUR 670.9m |
| EBITDA | EUR 461.9m (+1.2%) | EUR 456.6m |
| EBITDA margin | **22.3%** | 22.0% |
| EBIT | EUR 336.6m | EUR 337.8m |
| **EBIT margin** | **16.3%** `[computed]` | 16.3% `[computed]` |
| Net income | EUR 209.7m (**−8.2%** `[computed]`) | EUR 228.5m |
| Free cash flow | **EUR 220m** — record | EUR 205m |
| Net financial position | EUR 291.1m | EUR 409.0m |
| Leverage | 0.6× (**NFP/EBITDA 0.63×** `[computed]`) | |

**FY2026 guidance:** sales −2% to +3% organic, **plus ≈2% from acquisitions**; EBITDA margin *"consolidation of excellence"*; a third consecutive FCF record targeted.

**The one observation that matters for how this name is queued.** `TODO-queue_v4` flags Interpump as a *"PARTIAL serial-acquirer, so a partial Q8 caution."* **FY2025 quantifies it: organic −0.7% against +2.3% from acquisitions — every point of top-line came from purchase, and none from the existing business.** Guidance repeats the shape for FY2026 (≈2% acquisition contribution). **That is not "partial"; on this year's evidence the growth is entirely acquisitive**, which puts the name squarely in the population MODEL question 8 documents the framework as mis-measuring. `[computed, on one year]` — **one year is not a record, and the FY2021–24 organic/acquisition split should be obtained before the caution is upgraded.**

**Still needed before a memo:** equity and total capital employed (absent from the preliminary release — the **Annual Financial Report 2025, 30 April 2026**, is at the same document store and was not fetched this run); goodwill and acquired intangibles, which decide the four CE variants and are the whole question on a serial acquirer; the share count; a dated price. **Nothing here computes a return on capital, because the denominator was not obtained. Do not infer one from the margin.**

### ⟪ `claude_2026-09-08_NKE-buyback-evidence-flag-closures-round2_v1.md` → 3. Interpump — the capital base, and a 12.95-point question-8 spread ⟫
**Source: Interpump Group Annual Financial Report 2025 (30 April 2026), company document store** `[primary]`. Completes the dossier opened at `register-flags…_v1` §5.1.

**Balance sheet at 31-12-2025, EUR thousands** `[primary]`: shareholders' equity **2,110,101** (2024: 2,019,337) · goodwill **865,841** (837,798) · other intangible assets **74,060** (76,896) · cash and equivalents **415,704** (392,637) · current financial liabilities **265,308** (247,644) · non-current financial liabilities **500,823** (587,872).

**Income statement 2025 / 2024** `[primary]`: operating profit **336,564** / 337,814 · financial expenses **(65,326)** / (62,380) · income taxes **(89,139)** / (82,562) · net profit **209,709** / 228,470 · **EPS EUR 1.955 / 2.124**.

**Shares** `[primary]`: **108,823,000 issued**; **2,494,087 treasury (2.291%)**; **106,328,913 net** `[computed]`. *(Tie-out: 209,709 ÷ 1.955 = 107,268k weighted-average shares, which sits between the net and issued counts as it should)* `[computed]`.

### ⟪ `claude_2026-09-08_NKE-buyback-evidence-flag-closures-round2_v1.md` → 3.1 The four capital-employed variants and what they do to the answer ⟫
`[computed, EUR thousands]` Gross financial debt 265,308 + 500,823 = **766,131**. Less cash 415,704 = **net financial debt 350,427**.

**⚠ Note a EUR 59,327k discrepancy against the company's own stated net financial position of EUR 291,100k** (from the FY2025 preliminary release). **The difference is presumably other financial assets or receivables included in the company's NFP definition and not in a cash-only netting** `[assumption — the composition was not obtained]`. **Both are shown below so the choice is visible rather than buried.**

| Capital base | EUR thousands |
|---|---|
| (i) Equity + net financial debt (cash-netted) | **2,460,528** |
| (ii) Equity + company-stated NFP | 2,401,201 |
| (iii) (i) less goodwill | **1,594,687** |
| (iv) (i) less goodwill and other intangibles | **1,520,627** |

**Effective tax rate** `[computed]`: pre-tax 336,564 − 65,326 = 271,238; tax 89,139 ⇒ **32.86%**. **NOPAT = 336,564 × (1 − 0.3286) = 225,969.**

| Return | Basis | Result |
|---|---|---|
| **EBIT / (i)** | pre-tax, goodwill included | **13.68%** |
| EBIT / (ii) | pre-tax, company NFP | 14.02% |
| **EBIT / (iii)** | pre-tax, ex-goodwill | **21.11%** |
| **EBIT / (iv)** | pre-tax, ex-goodwill and intangibles | **22.13%** |
| **NOPAT / (i)** | after-tax, goodwill included | **9.18%** |
| NOPAT / (iii) | after-tax, ex-goodwill | 14.17% |
| NOPAT / (iv) | after-tax, ex-goodwill and intangibles | 14.86% |
| ROE | net profit / equity | 9.94% |

**The spread is 9.18% to 22.13% — 12.95 percentage points, one company, one year, four defensible bases.** `[computed]`

**Why this is the single most useful datapoint this run produced for MODEL question 8.** The question's existing evidence is cross-sectional: Krones 19.1% ex-goodwill against KION 7.7% inclusive; the beverages set where the basis **inverted the ranking** of three companies. **Interpump adds a clean single-name spread on a mid-sized serial acquirer with a moderate — not extreme — intangible load: goodwill and other intangibles are EUR 939,901k, or 44.5% of equity** `[computed]`, **against the 90.4% and 94.6% of Hexagon and AutoStore.** **So the 12.95-point spread is what the framework meets at a NORMAL acquisitive balance sheet, not an extreme one** — which makes the question broader than the Bucket N block implies.

**None of these is a verdict.** The framework's worst-of-four ROCE is computed from the four CE variants **as MODEL.md defines them**, and the definitions above are this run's arithmetic on the disclosed balance sheet, not the framework's. **Recompute at the PC with MODEL.md open. The value here is that the inputs are now assembled and primary.**

**Still missing for a memo:** a dated price and market capitalisation (gate-3 inputs — not obtained); total assets; the FY2021–24 organic-versus-acquisition split flagged at `register-flags…_v1` §7 item 36; and the composition of the company's NFP definition.

---


---
*Evidence note — not a memo, not investment advice.*
