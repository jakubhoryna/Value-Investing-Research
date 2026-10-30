# NWL.MI — NewPrinces S.p.A. — INCOMPLETE evidence (ANALYSE 2026-10-30)

Run: ANALYSE routine, D 2026-10-30, T 1941, base 058feca992504383e06a604af8ed735cc71465ab, MODEL v4.7.0. No verdict.

## Named gap

**INCOMPLETE (group build exceeds budget)** (routines/README.md §5; MODEL §8.7 item 6). NewPrinces (formerly Newlat Food) is a group (MODEL §2 Group Gate 0). It has two material controlled listed subsidiaries: Princes Group plc (London, `PRN.L`; the 2024 acquisition of the Princes Limited group, floated 31 Oct 2025 at 475p, market cap ≈ £1,162m at the offer price) and Centrale del Latte d'Italia S.p.A. (Euronext Milan, `CLI.MI`). It also has a new Italian grocery retail unit (Carrefour Italia, now Princes Retail / GS, consolidated from 1 Dec 2025, EV ≈ €1bn). Revenue is reported in seven product business units plus Distribution. The FY2025 press release gives pro forma revenue of €6.5bn against €2.96bn consolidated. The FY2025 Distribution line covers one month and holds 11.3% of revenue.

The group build has these parts:
- B4 with P29 weights and S. Princes Group plc sits inside several product segments, so its base has to be carved out pro rata (MODEL §2 Group grades).
- One Appendix D block per material unit.
- The NCI of both listed subsidiaries at the higher of market and book.
- The allocation-across-the-parts table.
- A ten-year record, FY2016–FY2025 with balance sheets from 31 Dec 2015. Newlat Food listed in Oct 2019, so the pre-IPO years come from the prospectus's audited statements, or are history-limited.
- An acquisition stop on four deals in the trailing three fiscal years and the live year: Princes Limited (2024), Princes Ready to Drink / Diageo Operations Italy (€101m, 30 Sep 2025), Plasmon from Kraft Heinz (cash €124.4m, 31 Dec 2025) and Carrefour Italia (EV ≈ €1bn, 1 Dec 2025).
- The P20 constructed build. It is unavailable in deal years without acquired-revenue disclosure.

That cannot be finished inside one routine run.

## Dependency check (MODEL §2 Group dependencies)

| Part | Kind | Key (price endpoint, 2026-10-30) | Own memo | Status for the parent |
|---|---|---|---|---|
| Princes Group plc | controlled listed subsidiary | `PRN.L` — LSE, GBp, "Princes Group plc", 345.0 | none (no `memos/`, `archive/memos/` or register match on name) | ungradeable: memo missing |
| Centrale del Latte d'Italia S.p.A. | controlled listed subsidiary (named "listed on Euronext Milan" in the FY2025 release) | `CLI.MI` — MIL, EUR, "Centrale del Latte d'Italia S.p.A.", 3.92 | none | ungradeable: memo missing |

NewPrinces' economic share in each is not established this run (owed from the FY2025 annual report's scope-of-consolidation note). Princes Group plc's share of group revenue is plainly above a third: UK revenue alone is 54.2% of FY2025 revenue. So when the build is done, Princes Group plc alone may carry more than ⅓ of the P29 base. That would make the group Future WEAK (`sub dependency`) unless its own memo lands first. This is a pointer, not a finding.

## Identity

- Company: NewPrinces S.p.A. (formerly Newlat Food S.p.A.), Reggio Emilia; Euronext STAR Milan; endpoint `NWL.MI` → `exchangeName` MIL, `currency` EUR, `longName` "NewPrinces S.p.A.", close 21.90 on 2026-10-30.
- ISIN: n/a — not established in this run. No ISIN for this issuer was printed in the documents read (the one ISIN in the 0474-series notices, IT0193425001, belongs to their issuer, not verified as NewPrinces).
- No prior: no `memos/*/` or `archive/memos/*/` front matter matches Newprinces, Newlat or Princes; no register row matches.

## Sourced figures (primary; € thousand unless stated)

Source: NewPrinces press release "Approval FY 2025", 31 Mar 2026 (regulated release 2195-16-2026, eMarket Storage `20260331_180632.pdf`), annex consolidated statements.

**Income statement**

| Item | FY2025 | FY2024 |
|---|---|---|
| Revenue from contracts with customers | 2,959,932 | 1,641,109 |
| — of which from related parties | 21,157 | n/a — not disclosed |
| Cost of sales | (2,404,768) | (1,369,726) |
| — of which to related parties | (347,306) | (2,644) |
| Gross operating profit | 555,164 | 271,383 |
| Selling and distribution expenses | (185,845) | (123,973) |
| Administrative expenses | (264,791) | (104,704) |
| Net write-downs of financial assets | (2,839) | (374) |
| Other revenue and income | 15,433 | 7,555 |
| Income from business combinations | 319,728 | 158,156 |
| Other operating costs | (6,083) | (7,673) |
| Operating profit (reported) | 430,768 | 200,372 |
| Financial income | 51,115 | 12,224 |
| Financial expenses | (71,698) | (42,432) |
| Equity-method result | 141 | (19) |
| Profit before tax | 410,327 | 170,145 |
| Income tax | (26,895) | (7,205) |
| Net profit | 383,432 | 162,940 |
| — to minorities | 8,338 | 2,308 |
| — to the group | 375,094 | 160,632 |
| Diluted EPS (€) | 8.71 | 3.66 |

J1 pointer, not a ruling. The reported operating profit carries bargain-purchase "income from business combinations": 2025 €319.7m (Princes Ready to Drink €58.7m; Princes Retail €261.0m; provisional PPA) and 2024 €158.2m (Princes Limited). This is a gain of ambiguous character (J3: leaves when positive). Operating profit before that line is 111,040 (2025) and 42,216 (2024), derived (430,768 − 319,728; 200,372 − 158,156). That ties to the presentation's "adjusted EBIT €111m vs €42.2m".

**Revenue by business unit (FY2025 / FY2024):** Dairy 334,788 / 334,686 · Foods 743,014 / 433,154 · Drinks 391,740 / 150,106 · Fish 409,659 / 201,026 · Italian Products 402,195 / 343,389 · Oils 328,546 / 163,722 · Distribution 334,787 / – · Other 15,203 / 15,026. Presentation note: Oils' margin is on a 50% basis (Princes/ADM joint venture).

**By geography (FY2025 / FY2024):** Italy 780,797 / 398,240 · Germany 146,958 / 146,448 · UK 1,603,794 / 721,423 · Other 428,384 / 374,998.

**By channel (FY2025):** large-scale retail 2,449,230 (82.7%) · B2B partners 270,311 · food services 240,390. Large-scale retail at 82.7% makes the P15 customer test (any retailer > 10%; silence = concentration) decisive. The customer table is owed.

**Balance sheet (31 Dec 2025 / 31 Dec 2024)**

| Item | 2025 | 2024 |
|---|---|---|
| PP&E | 1,044,447 | 560,456 |
| Right-of-use assets | 314,770 | 93,050 |
| Intangible assets | 232,465 | 141,307 |
| Investment property | 67,917 | 0 |
| Investments in associates | 8,359 | 10,090 |
| Inventories | 828,143 | 486,942 |
| Trade receivables | 357,413 | 258,544 |
| Current financial assets at FVTPL | 49,346 | 1,576 |
| Financial receivables at amortised cost (all from related parties) | 55,647 | 263,775 |
| Cash and cash equivalents | 1,333,450 | 455,135 |
| Assets held for sale | 10,000 | – |
| Total assets | 4,543,143 | 2,356,504 |
| Equity attributable to the group | 803,842 | 333,111 |
| Minority interests | 167,345 | 65,530 |
| Total equity | 971,187 | 398,641 |
| Non-current financial liabilities | 940,076 | 581,229 |
| Non-current lease liabilities | 266,944 | 79,758 |
| Shareholder loans (all related parties) | 173,994 | 206,100 |
| Current financial liabilities | 193,608 | 385,486 |
| Current lease liabilities | 135,895 | 20,230 |
| Trade payables | 1,506,293 | 559,229 |
| — of which to related parties | 63,653 | 3,782 |
| Provisions (staff; risks and charges) | 59,614; 80,097 | 13,056; 3,723 |
| Deferred tax liabilities | 57,207 | 48,578 |
| Other current liabilities | 151,531 | 55,526 |
| Total liabilities (derived: total assets − total equity) | 3,571,956 | 1,957,863 |

**Cash flow (FY2025 / FY2024):** CFO 594,431 / 279,498, including Δ trade payables +331,633 / +72,800 (the Carrefour Italia consolidation month). PP&E capex (195,254) / (23,056). Intangibles capex (1,461) / (3,433). Plasmon acquisition (124,433). Net cash acquired: Carrefour 175,117, Diageo 6,603, Princes Limited (2024) 5,737. Disposals of financial assets +161,386 / (240,360). IPO of Princes Group plc +220,417 (equity: group +125,684, minorities +94,733). Net interest paid (14,787) / (12,410), in financing (IFRS: to move into CFO before FCF). Own shares (12,672) / (5,758).

## Pointers for the attended build (not findings)

- **Gate 1C RPT (·2).** The controller-linked items are large: FY2025 related-party cost of sales €347.3m (FY2024 €2.6m); shareholder loans from related parties €174.0m (FY2024 €206.1m); financial receivables from related parties €55.6m (FY2024 €263.8m); related-party trade payables €63.7m. P27 materiality and the counterparties (Newlat Group SA / the Mastrolia family, per the presentation's "family controlled") are owed from the related-party note and the remuneration report.
- **Votes versus economics.** Check for loyalty shares (maggiorazione del voto) in the corporate-governance report.
- **Leverage (P5).** L/E at 31 Dec 2025 ≈ 3,571,956 ÷ 803,842 = 444% (derived, BV = group equity), above the 200% flag level. A P6 test is owed.
- **Treasury shares.** Purchases of €12.7m (2025) and €5.8m (2024) need the worth test; the AGM of 27 Apr 2026 renewed the authorisation.

## Documents read (uncounted, primary)

1. eMarket Storage `20260331_180632.pdf`: FY2025 approval press release with annex statements (23 pp).
2. eMarket Storage `20260331_180650.pdf`: FY2025 earnings presentation (44 pp; scanned for segment and IPO facts only).
3. eMarket Storage `20260331_180801/180802/180925/180926.pdf`: same-day regulated notices (titles only).

Price endpoint (uncounted): `NWL.MI`, `PRN.L`, `CLI.MI` (plus two unmatched probes, `PRIN.L` and `PGP.L`). Exploratory searches: 1 of ~5.

## Owed documents (attended)

- Annual financial reports FY2019–FY2025 (newprinces.it investor center / eMarket Storage) and the Oct 2019 IPO prospectus for FY2016–FY2018: B1–B3, P20, J1/J3 per year, the G6 test (associates; the Princes/ADM oils JV).
- 2026 H1 report: TTM and the interim balance sheet for EV.
- Remuneration report 2026 (Art. 123-ter TUF), corporate-governance report, related-party note.
- Princes Group plc prospectus / FY2025 annual report (for its own memo, `PRN.L`); Centrale del Latte d'Italia FY2025 annual report (`CLI.MI`).
