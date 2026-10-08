# SGO.PA — Compagnie de Saint-Gobain S.A. — INCOMPLETE evidence (REVIEW 2026-10-08)

- Run: REVIEW, D 2026-10-08, T 0611, base 428f48234846afb72fd7e69a954d159b3438f353, MODEL v4.5.2
- Prior memo: `memos/SGO.PA/` v1 (memo_date 2026-08-03, MODEL v4.0.0). It has no machine fields and no ISIN.
- Pick: `▶ Method re-tests v4.5.0` (priority 1b). The same key also carries a SWEEP review request (move −18.7%, sweep 2026-10-05).
- No verdict. This file is orientation only for the attended re-test (MODEL §8.7 item 6, D3).

## Named gap

**Method re-test exceeds budget.** The prior is below v4.5.0, so the REVIEW must re-test every v4.5.0 method rule (MODEL §8.2 step 3). For this name that means:

1. **J1 OI rebuild for FY2016–FY2025.** The prior graded Past on the "Operating income" line. J1 takes the lowest operating subtotal, which is "Business income": Operating income less non-operating costs, less capital gains and losses on disposals, asset write-downs and the impact of changes in Group structure (PPA amortisation included). Under J3, net disposal gains then leave OI in any year where they are positive.
2. **P20 maintenance capex for every year.** The filer discloses "o/w additional capacity investments" (tier 1). The floor is operating D&A excluding right-of-use depreciation.
3. **The R9 pay table.** This needs the FY2023–25 per-person totals from the French-only URD remuneration chapter.
4. **The acquisition stop.** Deals in FY2023–25 and the live year: CSR (2024, a listed ASX target, so its own last annual reports and P3 record are needed), FOSROC and Cemix (2025), Bailey and Building Products of Canada/Kaycan, the North-American waterproofing deal finalised on 1 Oct 2026, Xypex and QSI Peru.
5. **The full worth table** on J1 OI and maintenance-capex FCF.
6. **The EV refresh.** Net pension obligation and NCI are now debt-equivalents, and both are absent from the prior's EV.

The primary IR host is behind a browser-verification wall, so this cannot finish inside one routine run.

## Hosts tried

| Host | Result |
|---|---|
| `www.saint-gobain.com` (finance/publications, regulated-information, `sites/saint-gobain.com/files/media/document/FY_2025_ENG-a.pdf`) | HTTP 403, "Verifying your browser…" (curl with browser headers) |
| `echanges.dila.gouv.fr` (AMF OPENDATA, `ECO/2026/02/FCECO081081_20260226.pdf`, the FY2025 results release) | directory listing 200; the PDF returned an empty reply (twice) |
| `webdisclosure.com` (FY2025 results release, regulated-information distributor) | 200, used below |
| `stockopedia.com` (RNS copies: FY2024 annual results release; H1 2025 half-year release) | 200, used below |
| `filings.xbrl.org` (ESEF, LEI NFONVGN05Z0FMN5PEC35) | 200: French URD xBRL for FY2021, FY2022, FY2023 and FY2025 (FY2024 not listed). These are the route for an attended rebuild of FY2020–FY2025 |
| `query1.finance.yahoo.com` | 200, price |

## Sourced figures (EUR m; results releases, regulated information)

| FY | Sales | Operating income | Non-operating costs | Disposals, write-downs, structure | Business income | Capex (release) | o/w additional capacity | Operating D&A | ROU depreciation |
|---|---|---|---|---|---|---|---|---|---|
| 2023 | 47,944 | 5,251 | −236 | −784 | 4,231 | 2,029 | 837 | 1,986 | 692 |
| 2024 | 46,571 | 5,304 | −236 | −691 | 4,377 | 2,049 | 842 | 2,137 | 727 |
| 2025 | 46,483 | 5,293 | −231 | −511 | 4,551 | 2,049 | 877 | 2,141 | 747 |

- FY2025 composition of the −511: asset write-downs −216 (mainly disposals and site closures), PPA intangible amortisation −290, disposal losses and structure impacts −5. FY2024: −291 / −233 / −167. Net disposal results are losses in both years, so J3 removes nothing there.
- Capex on the cash-flow statement (prior memo B1) is FY2024 2,083 and FY2025 2,174. The release figure (2,049) is lower; the attended rebuild must reconcile the two.
- Sum of Business income over FY2016–FY2025, carried from the prior memo's Appendix C: 31,328. The prior's worst-of-four ROCE on that line was 7.70% (FY2016–25), against 10.07% on Operating income.
- FY2025 segments (from 1 Jul 2025 the organisation is fully regional; the former High Performance Solutions segment no longer reports): Northern Europe 13,783 · Southern Europe, ME & Africa 16,068 · Americas 12,957 · Asia-Pacific 5,256 · internal −1,581. Each is above 10% of sales. "Industrial solutions" (5,855) is printed only at group level. The Gate 0 one-level decomposition and Group Gate 0 still have to be written.

## Price

SGO.PA: endpoint currency EUR, exchange PAR, "Compagnie de Saint-Gobain S.A."; €64.76 regular-market close on 2026-10-07 (prior closes 67.14 on 2026-10-06 and 66.12 on 2026-10-05); no split events.
