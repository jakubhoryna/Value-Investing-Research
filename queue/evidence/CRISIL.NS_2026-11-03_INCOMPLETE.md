# CRISIL.NS — INCOMPLETE evidence (resumable record, second overrun)

## 1. Header

| Field | Value |
|---|---|
| Key | CRISIL.NS (CRISIL Limited; NSE `CRISIL`, BSE 500092) |
| ISIN | INE007A01025 (carried from the 2026-11-01 record: AR23 PDF p. 102, AR21 PDF p. 79) |
| Job | ANALYSE (routine) |
| D · T | 2026-11-03 · 2132 (Europe/Prague) |
| Base sha | 2982b4e42f7d49c6c3648131d83ad53f66fd9ed8 |
| Live model_version | v4.8.0 |
| Prior memo | none (no `memos/CRISIL.NS/`, no `archive/memos/CRISIL.NS/`; no register row or memo `company:`/`isin:` matches "CRISIL" or INE007A01025) |
| Named gap | `INCOMPLETE (group build exceeds budget)` — **second overrun** |
| Resumes | `queue/evidence/CRISIL.NS_2026-11-01_INCOMPLETE.md` (partial 2026-11-01). Both records stay until the memo lands. |

**Why it overran again.** The resume re-fetched the six annual reports (AR16, AR17, AR19, AR21, AR23, AR24, AR25; BSE URLs as in the 2026-11-01 record, plus AR16 below) and settled the G6 classification, the P31 test, the P18 lease test with its PVs, the narrow NIBCL inputs for FY2015–FY2019, the FVOCI dividend series and the FY2022–FY2025 diluted counts (section 3). What remains — the per-year P20 build (D&A split and k for ten years), the two Appendix D unit blocks, the Appendix E pay, RPT and alignment worksheets, the allocation-across-the-parts table (its window needs AR22), the interim balance sheet and TTM test, then B1–B3 on both G6 readings and the memo itself — does not fit the rest of a ~90-minute run. Per `routines/README.md` §5 this is the second overrun: an attended group build is owed.

Units: ₹ lakh (1 lakh = ₹0.1m), consolidated Ind AS, fiscal years ending 31 December, unless stated. PDF page = the file's page index.

## 2. Sources retrieved this run (primary; P14: 0 exploratory operations)

| Ref | Document | URL |
|---|---|---|
| AR25 | Integrated Annual Report 2025 | bseindia.com/xml-data/corpfiling/AttachHis/5ca06d60-aff0-4016-981c-caf1990aecad.pdf |
| AR24 | Annual Report 2024 | bseindia.com/xml-data/corpfiling/AttachHis/3efc592d-0a2e-4b79-8158-6f0f50180319.pdf |
| AR23 | Annual Report 2023 | bseindia.com/xml-data/corpfiling/AttachHis/9b8b42ca-53ea-43a2-9070-108e429872cf.pdf |
| AR21 | Annual Report 2021 | bseindia.com/bseplus/AnnualReport/500092/72949500092.pdf |
| AR19 | Annual Report 2019 | bseindia.com/bseplus/AnnualReport/500092/5000921219.pdf |
| AR17 | Annual Report 2017 | bseindia.com/bseplus/AnnualReport/500092/5000921217.pdf |
| AR16 | Annual Report 2016 (Indian GAAP; FY2016 and FY2015) | bseindia.com/bseplus/AnnualReport/500092/5000921216.pdf |
| PX | query1.finance.yahoo.com/v8/finance/chart/CRISIL.NS — currency INR, exchangeName NSI, longName "CRISIL Limited", instrumentType EQUITY; meta regularMarketPrice 4,419.40 at 2026-11-03 09:59:53 UTC (the session's last trade); daily closes 4,516.60 (2026-10-30), 4,548.40 (2026-11-02); no split events | — |

## 3. Figures settled or added this run

### 3a. Item table (new items; every 2026-11-01 item stands as recorded there)

| item | FY | value | unit | source |
|---|---|---|---|---|
| CARE Ratings stake purchase: 26,22,430 shares, 8.9% of CARE's equity, bought June 2017 in Canara Bank's bid process; "an investment in the excellent long-term prospects of the credit rating sector … no special rights" | 2017 | text | text | AR17 PDF p. 62, Board's report ("Particulars of loans, guarantees or investments") |
| Investment in CARE Ratings (cash outflow) | 2017 | 43,389 | ₹ lakh | AR17 PDF p. 153, consolidated cash-flow statement, investing |
| Non-current investments: unquoted equity (NCDEX 3,002; CARICRA 37) / quoted | 2015 | 3,039 / 0 | ₹ lakh | AR17 PDF p. 172, note 7A (1 Jan 2016 column) |
| Same (NCDEX 3,512; CARICRA 45) / quoted | 2016 | 3,557 / 0 | ₹ lakh | AR17 PDF p. 172, note 7A |
| Same (NCDEX 3,521; CARICRA 149) / CARE 34,940 | 2017 | 3,670 / 34,940 | ₹ lakh | AR17 PDF p. 172, note 7A |
| Non-current investments: unquoted equity / quoted (CARE) | 2018 | 3,483 / 25,876 | ₹ lakh | AR19 PDF p. 161, note 6 |
| Same | 2019 | 3,324 / 16,756 | ₹ lakh | AR19 PDF p. 161, note 6 |
| Same | 2020 | 3,237 / 13,791 | ₹ lakh | AR21 PDF p. 194, note 7 |
| Same | 2021 | 3,299 / 16,239 | ₹ lakh | AR21 PDF p. 194, note 7 |
| Same | 2022 | 3,161 / 15,916 | ₹ lakh | AR23 PDF p. 196, note 8 |
| Same | 2023 | 2,858 / 24,955 | ₹ lakh | AR23 PDF p. 196, note 8; AR24 PDF p. 193, note 9 |
| Same (NCDEX 2,680; CARICRA 106) / CARE 36,180 | 2024 | 2,786 / 36,180 | ₹ lakh | AR25 PDF p. 241, note 9A |
| Same (NCDEX 3,700; CARICRA 116; Online PSB Loans 3,631) / CARE 41,956 | 2025 | 7,447 / 41,956 | ₹ lakh | AR25 PDF p. 241, note 9A |
| Online PSB Loans: 168,327 shares, 4.08% of its capital, acquired 4 June 2025 for 3,325 | 2025 | 3,325 | ₹ lakh | AR25 PDF p. 242, note 9.2 |
| Dividend recognised on FVOCI equity (in other income) | 2016 / 2017 | 47 / 321 | ₹ lakh | AR17 PDF p. 173, note 7 footnote |
| Same | 2018 / 2019 | 1,448 / 761 | ₹ lakh | AR19 PDF p. 161, note 6.2 |
| Same | 2020 / 2021 | 433 / 429 | ₹ lakh | AR21 PDF p. 194, note 7.1 |
| Same | 2022 / 2023 | 272 / 839 | ₹ lakh | AR23 PDF p. 196, note 8.1 |
| Same | 2024 / 2025 | 472 / 498 | ₹ lakh | AR25 PDF p. 242, note 9.1 |
| Current investments (all mutual-fund units at FVTPL: liquid, money-market, low/ultra-short duration, banking & PSU, corporate-bond and gilt funds) | 2025 / 2024 | 68,643 / 106,441 | ₹ lakh | AR25 PDF p. 241–242, note 9B |
| Deposits with remaining maturity < 12 months (of which 59 under lien for bank guarantees) | 2025 / 2024 | 33,587 / 93 | ₹ lakh | AR25 PDF p. 248, note 18 |
| Trade payables (MSE + others) | 2019 / 2018 | 7,546 (3 + 7,543) / 6,477 (26 + 6,451) | ₹ lakh | AR19 PDF p. 141, consolidated balance sheet |
| Tax liabilities (current) | 2017 / 2016 / 2015 | 1,001 / 866 / 591 | ₹ lakh | AR17 PDF p. 151, consolidated balance sheet |
| Trade payables | 2015 | 3,735 | ₹ lakh | AR17 PDF p. 151 (1 Jan 2016 column) |
| Borrowings (non-current 4; short-term 258) | 2019 | 262 | ₹ lakh | AR19 PDF p. 141 |
| Other bank balances / other current financial assets | 2017 | 4,709 / 13,888 | ₹ lakh | AR17 PDF p. 151 |
| Operating-lease commitments ≤1y / 1–5y / >5y; expense recognised | 2019 | 6,519 / 15,768 / 2,950; 7,155 | ₹ lakh | AR19 PDF p. 184, note 39 |
| Same | 2018 | 5,704 / 18,378 / 2,604; 6,416 | ₹ lakh | AR19 PDF p. 184, note 39 |
| Same | 2017 | 5,248 / 6,411 / 2,071; 5,853 | ₹ lakh | AR17 PDF p. 195, note 37 |
| Same | 2016 | 4,524 / 9,819 / 3,790; 5,801 | ₹ lakh | AR17 PDF p. 195, note 37 |
| Same (printed in rupees: 487,742,982 / 1,009,007,658 / 63,562,905) | 2015 | 4,877 / 10,090 / 636 | ₹ lakh | AR16 PDF p. 169, consolidated operating-lease note (Indian GAAP) |
| Lease liabilities: transition 1 Jan 2020 22,167; closing 2020 22,413; closing 2021 13,214; interest recognised 1,410 (2020), 893 (2021); payments 6,791 (2020), 5,823 (2021) | 2020–2021 | as listed | ₹ lakh | AR21 PDF p. 214, note 39.1 |
| D&A: PP&E 3,584 / 2,775; right-of-use 5,077 / 2,080; intangibles 4,191 / 2,140 | 2025 / 2024 | as listed | ₹ lakh | AR25 PDF p. 255, note 34 |
| Intangibles amortisation by class FY2025: software 2,674; brand 235; database 391; customer relationships 891 (FY2024: software 885; brand 226; database 253; customer relationships 776) | 2025 / 2024 | as listed | ₹ lakh | AR25 PDF p. 239, note 6 |
| Net software (capitalised) / intangibles under development (software) | 2025 / 2024 | 5,102 / 2,821; 1,585 / 5,375 | ₹ lakh | AR25 PDF p. 239, notes 6 and 7 |
| Diluted weighted shares | 2025 / 2024 | 73,129,988 / 73,126,051 | shares | AR25 PDF p. 275, EPS note |
| Diluted weighted shares | 2023 / 2022 | 73,106,836 / 73,051,258 | shares | AR23 PDF p. 227, EPS note |
| Segmentation: three reportable segments (Rating, Research, Advisory) | 2021 | text | text | AR21 PDF p. 188, note 2 (segment policy) |
| Segmentation: two reportable segments (Ratings services; Research, Analytics and Solutions) | 2023 | text | text | AR23 PDF p. 190, note 2 (segment policy) |
| GAC: "a vital analytical, research, data, and tech services hub for S&P Global … support S&P Global Ratings (SPGR) teams in Americas, EMEA, and APAC"; "Largest and key data, analytics, and research partner for S&P Global Ratings"; 1,300+ staff, seven centres; reported in Ratings ("global analytical services" in the Ratings segment description) | 2025 | text | text | AR25 PDF p. 12 (GAC page); AR25 PDF p. 83 (MD&A "GAC continued to drive surveillance delegation … increased support to S&P in new areas beyond Ratings"); note 39 segment description |

### 3b. Derived this run (each labelled; inputs in 3a or the 2026-11-01 record)

| item | FY | value | unit | source |
|---|---|---|---|---|
| Implied lease rate (interest recognised ÷ average of transition and closing liability) | 2020 | 6.33% | % | derived: AR21 note 39.1 (1,410 ÷ avg(22,167; 22,413)); CRISIL has no debt and prints no incremental borrowing rate as a figure — the attended build confirms or replaces this as "the disclosed recent cost of debt" |
| P18 test: commitments ÷ total assets | 2015 / 2016 / 2017 / 2018 / 2019 | 11.7% / 13.1% / 9.2% / 16.3% / 14.9% | % | derived: lease rows above ÷ total assets (2026-11-01 record) |
| P18 result | 2015–2019 | capitalise FY2015, FY2016, FY2018, FY2019; FY2017 below 10% (not capitalised) | — | derived |
| PV of commitments at 6.33% (1–5y lump spread evenly over years 2–5; beyond-5 lump spread at the year-5 rate until exhausted) | 2015 / 2016 / 2017 / 2018 / 2019 | 13,187 / 14,764 / 11,534 / 22,029 / 20,924 | ₹ lakh | derived: discounting the commitment rows above at 6.33% (a /tmp script, not committed; re-run by the attended build) |
| Imputed interest r × opening PV (OI add-back in capitalised years) | 2016 / 2018 / 2019 | 834 / 730 / 1,393 | ₹ lakh | derived (FY2018 on the FY2017 PV, a PV computed although FY2017 is not capitalised; the attended build decides whether to use the opening PV or the year's average, and logs it) |
| G6 class carrying value ÷ total assets | 2015 … 2025 | 2.3, 2.6, 25.8, 18.0, 11.9, 7.7, 7.8, 6.7, 8.4, 9.9, 10.7 | % | derived: class rows above ÷ total assets |
| G6 class income (FVOCI dividends) ÷ exclude-reading OI candidate | 2016 … 2025 | 0.1, 0.8, 3.4, 1.8, 1.1, 0.9, 0.4, 1.1, 0.6, 0.5 | % | derived; the OI candidate is pre-P18 (the capitalised years' OI rises by the imputed interest, which lowers these ratios) |
| S&P Global group share of Ratings-segment revenue, if all S&P services sit in Ratings | 2025 / 2024 | 44.2% (47,593 ÷ 107,663) / 42.8% (38,904 ÷ 90,915) | % | derived: 2026-11-01 record (note 40 sums; note 39 segment revenue); the split of S&P revenue between segments is not printed |
| Floor items for P20 (PP&E depreciation + software amortisation) | 2025 / 2024 | 6,258 / 3,660 | ₹ lakh | derived: note 34 PP&E line + note 6 software line |

## 4. Readings settled (on the live rules; the attended build re-reads each)

- **Lens: STD.** No banking or insurance licence; CRISIL is a SEBI-registered credit rating agency and a research and analytics provider (AR25 business review, note 39). FI fails at its first condition. Not a bank or insurer that fails FI, no licensed insurer or deposit-funded bank unit, and total assets are not more than half unlisted stakes or S3 securities (class ≤ 25.8% of TA in every year), so none of STD's special rules applies. Appendix C logs this.
- **CARE Ratings is S3, not S2.** It is immaterial (≈ 1.3% of CRISIL's MCap, P22) and listed, so S2 unless strategic. The filer bought it as "an investment in the excellent long-term prospects of the credit rating sector" and has carried it at FVOCI since 2017 without trading it; CARE is a direct competitor (another SEBI-registered agency). Under J13, the long-term framing reads as "long-term" under the H/S3 definition: S3, no credit at Gate 2, a G6 class in Gate 1A. The unquoted stakes (NCDEX, CARICRA, Online PSB Loans) are S3 in any case. ICRA (1 share) is nil.
- **G6 / P31: above the line from FY2017.** The carrying-value limb fails at every balance-sheet date FY2017–FY2025 (6.7%–25.8% of TA); the income limb holds in every year (≤ 3.4%). So B2 and B3 run both readings over the whole window (the classes are tested together and the line is crossed): exclude both (dividends out of OI and FCF, class carrying value out of CE in both cash variants) and include both (FVOCI dividends in OI; the same amounts in FCF, CFO not carrying them since the cash-flow statement books dividends received in investing — received taken equal to recognised, logged, or nothing added where the receipt cannot be placed, J13). Fair-value changes go through OCI and never reach OI on either reading; no impairment or disposal loss on class assets is booked in P&L in the window (to confirm per year in the attended build).
- **NIBCL: narrow build, harsher.** Trade payables + current tax liabilities only. Accrued expenses, contract liabilities (deferred revenue) and employee payables sit inside "other financial liabilities" and "other current liabilities" without a split read this run; burden of proof leaves them in CE, which lowers ROCE. The attended build may take the default NIBCL from notes 26/27 and equivalents; if the narrow build already clears every bar, the default cannot lower the grade.
- **Cash for CE_xc and the all-cash EV:** cash and cash equivalents, plus mutual-fund units at market × 0.9 (S1: none is a government money-market fund or bill), plus FY2025 term deposits < 12 months at carrying (33,528 = 33,587 − 59 under lien). Other bank balances (unpaid-dividend and lien accounts) are never cash. Other financial assets in earlier years stay in CE unless a note shows deposits ≤ 12 months.
- **P18:** capitalise FY2015, FY2016, FY2018 and FY2019 at the PVs above; FY2017 stays uncapitalised. In capitalised years: CE and total liabilities rise by the PV, OI rises by r × PV (imputed interest), FCF = CFO − maintenance capex + lease payments − imputed interest. FY2020 onward under Ind AS 116: lease interest paid moves from financing into CFO before FCF; lease liabilities are debt-equivalents in CE, EV and L/E.
- **P20 orientation:** k needs net PP&E + capitalised software (+ software under development) per year, acquired intangibles (brand, database, customer relationships, technology, tradename, platform) out. The floor is PP&E depreciation + software amortisation; ROU depreciation and acquired-intangible amortisation are excluded. FY2025 floor 6,258 against capex 7,340; FY2024 floor 3,660 against capex 17,316. Deal years: FY2018 Pragmatix (5,600, below 1% of EV — reported revenue usable, logged), FY2020 Greenwich Associates (25,117; test against 1% of EV at the time — above it, the year needs acquired-revenue disclosure or takes all capex), FY2025 PriceMetrix (29,397 ≈ 0.9% of MCap at px, 4,419.40 × 73.13m shares ≈ ₹323.2 bn = 32.3 lakh lakh, derived; test at the FY2025 EV).
- **Units for Gate 0 and Future:** Ratings services (29.5% of FY2025 revenue) carries the GAC, CRISIL's captive service hub for S&P Global Ratings; Research, Analytics and Solutions (70.5%) carries global research and risk solutions, Coalition Greenwich benchmarking (with PriceMetrix from November 2025) and India research. Breadth: S&P Global entities are one customer under common control (§2·1B) at 13.0% of FY2025 consolidated revenue (derived) and, if all of it sits in Ratings, ≈ 44% of that unit's revenue. The filer's group statement is per legal entity; the common-control aggregation is the harsher reading (J13), so the flag is the Ratings unit's (the IDEAS candidate of 2026-11-01 asks for a one-line rule). R7: S&P is CRISIL's controller and the price-setter of its own purchases, so condition (3), pricing power over the concentrated customer, has no evidence so far; unless the attended build finds it, the concentration is a STRONG customer-power call for Ratings, ADEQUATE only with named containment and no other STRONG force (P16).
- **Allocation across the parts:** the two-segment structure is reported from AR23 (FY2023, with FY2022 comparatives) at the latest; FY2021 and earlier are on three segments. The window starts at the earliest year-end AR22 or AR23 reports or restates on the two-segment basis; if that leaves fewer than three fiscal years it is INDETERMINATE (b). FY2024–FY2025 segment results and assets are in the 2026-11-01 record.

## 5. Scope still owed (attended group build, in this order)

- [ ] Re-open the governing figures of both records (AR25 PDF p. 217–220 statements; note 39 p. 262–264) and the AR17/AR19/AR21/AR23/AR24 statements for each window year.
- [ ] P20 per FY2016–FY2025: D&A split (PP&E, software, ROU, acquired intangibles) from each AR's PP&E and intangibles notes; net PP&E + capitalised software + software under development for k; India CPI per calendar year (World Bank FP.CPI.TOTL.ZG or MOSPI, named); acquired revenue for Greenwich (AR20/AR21, deal note) and PriceMetrix (AR25 note 45.3); EV at each deal date for the 1% test.
- [ ] B1–B3 on both G6 readings with the P18 adjustments above; four-way averages on both windows (worst of eight), J6 on each reading, growth reads (i) and (ii), L/E (lease PV in the numerator in capitalised years; total liabilities 159,850 at FY2025).
- [ ] B4: segment revenue, results and assets FY2023–FY2025 (FY2023 from AR24 note 39); P29 weights on segment results after allocating the unallocable D&A and expenditure if the note allows, else revenue weights; read AR22 for the earliest two-segment year (allocation window).
- [ ] Appendix D, Ratings: GAC revenue share (MD&A segment discussion), S&P pricing basis (transfer pricing, shareholder approval of material RPTs in the AGM notice), domestic ratings market position by evidenced share, the R7 worksheet, four forces, moat (SEBI registration; issuer-pay, regulation-mandated ratings), market growth.
- [ ] Appendix D, RAS: parts and their sizes (GR&RS, Coalition Greenwich, India research), customer evidence (group statement covers it unless a unit discloses concentration), forces (banks' in-house India captives as substitutes; KPO entrants), moat, market; J13 harsher call where parts are unsized or within 10pp.
- [ ] Appendix E: per-person pay FY2023–FY2025 for the MD & CEO (Amish Mehta from 1 Oct 2023? verify), the prior MD & CEO and the CFOs (Board's report Annexure on managerial remuneration; AR25 PDF p. ≈ 98–102 ratio table); director fees (highest: Shyamala Gopinath 107 in FY2025, note 40) against the cap; management holdings (Amish Mehta 6.49% of what — the line at AR25 text ≈ PDF p. 98 is a pay-increase ratio, not a holding: read the CG report shareholding of directors and KMP); shareholding pattern (S&P entities ≈ 66.6%); RPT reading of the S&P services and of the small payments to S&P (subscription fees 362, rent 288); dividends paid record (payout vs FCF); buy-back check (none found so far); acquisition stop for PriceMetrix and Greenwich (earlier window, allocators).
- [ ] Gate 2: latest interim balance sheet (30 Jun 2026 half-year statement of assets and liabilities, BSE results filing) for debt-equivalents (lease liabilities; gratuity net of plan assets if unfunded) and cash; Q3 2026 results for the TTM test (TTM replaces FY2025 only when lower); diluted shares; px 4,419.40 (2026-11-03) or the attended run's own; trigger band and averaged readings; CARE and the unquoted stakes earn no credit (S3).
- [ ] Psychology check; memo; `lint-memo`; row file with `## Register row (new)` from `row-from-memo --table`.

*Framework output, not investment advice.*
