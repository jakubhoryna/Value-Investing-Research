# SES.MI — SeSa S.p.A. — INCOMPLETE evidence (ANALYSE 2026-10-30)

Run: ANALYSE routine, D 2026-10-30, T 1903, base 6fe510021a7004351b3f57399cb1be9c70cab69b, MODEL v4.7.0. No verdict.

## Named gap

**INCOMPLETE (group build exceeds budget)** (routines/README.md §5; MODEL §8.7 item 6). SeSa is a group (MODEL §2 Group Gate 0) with four material units on its FY2026 segmentation (sourced revenue below): ICT VAS, SSI and Green VAS are each ≥ 10% of revenue. Business Services (4.4% of revenue) is likely material on Σ positive segment results (Q1 FY2027 EBITDA 8.6 of the four units' 63.8; segment EBIT not extracted). The group build needs B4 with weights and S, one Appendix D block per material unit, and the allocation-across-the-parts table, on top of a ten-year record (FYE 30 April; balance sheets April 2016 to April 2026). That record has to come from integrated annual reports for a serial acquirer: deals every year with minority put and earn-out liabilities, NCI and equity-accounted investees (a G6 class). It also needs the P20 constructed build, which turns on organic or acquired-revenue disclosure in deal years. That cannot be finished inside one routine run.

A retrieval constraint compounds it. sesa.it returns HTTP 403 to direct downloads from the sandbox (bot protection). The issuer's annual reports are linked there (ESEF/XHTML and PDF) and reachable only through a summarising fetch, which cannot support exact extraction (MODEL §4 extraction-conflict rule). The 29 Jul 2026 eMarket Storage filing is the publication notice only: the Integrated Annual Report itself is not attached. The attended build should take the annual reports FY2016/17–FY2025/26 from a browser or from the eMarket Storage ESEF filings.

## Sourced figures (primary; Eu thousand unless stated)

From the Q1 FY2027 press release, 14 Sep 2026 (interim report to 31 Jul 2026; euroborsa.it copy of the regulated release `20260914_189176_1_.pdf`):

| Item | Q1 FY2027 (3m to 31 Jul 2026) | Q1 FY2026 (3m to 31 Jul 2025) |
|---|---|---|
| Net revenue | 886,731 | 829,135 |
| Revenue and other income | 901,081 | 845,729 |
| EBITDA (APM) | 65,261 | 60,675 |
| D&A of tangible and intangible assets | (14,086) | (12,745) |
| Provisions | (996) | (670) |
| EBIT Adjusted (APM; before PPA amortisation — never the J1 line) | 50,179 | 47,260 |
| PPA amortisation (customer lists, know-how) | (8,737) | (8,700) |
| EBIT (reported; lowest operating subtotal shown — J1 candidate) | 41,442 | 38,560 |
| Net financial charges | (7,606) | (6,781) |
| FX gains/losses | (20) | (509) |
| Equity-accounted result | 100 | 101 |
| Net result | 25,391 | 23,483 |
| — attributable to group | 23,336 | 21,583 |

Segment revenue and other income, Q1 FY2027: ICT VAS 536.9m; SSI 212.9m; Green VAS 127.4m; Business Services 40.8m. Segment EBITDA: ICT VAS 24.6m; SSI 22.9m; Green VAS 7.7m; Business Services 8.6m.

Balance sheet, 31 Jul 2026 (vs 30 Apr 2026): cash and equivalents 532,471 (576,313); equity attributable to group 477,367 (460,252); NCI 69,683 (68,984); total equity 547,050 (529,236); total equity and liabilities 2,354,610 (2,331,564); equity-accounted investments 14,437 (14,529); non-current debts and commitments to minority holders for acquisitions (earn-outs, puts, deferred prices) 93,454 (111,834); current ones 29,033 (31,336). Reported net financial position: net debt Eu 23.4m at 31 Jul 2026; net cash Eu 149.8m excluding "IFRS debts" (minority-holder liabilities and IFRS 16 lease liabilities, 173.3m). Share capital Eu 37,126,927.50. Live programme: a buyback under the AGM authorisation of 27 Aug 2026, cycle up to Eu 5m.

FY2026 (year to 30 Apr 2026), from the 29 Jul 2026 eMarket Storage notice: consolidated revenue Eu 3,620.8m (+7.9%); SSI 908.8m, Business Services 158.5m, ICT VAS 2,254.7m, Green VAS 412.2m, Corporate and Digital Ecosystem 67.5m; 6,770 staff. Controlled by ITH S.p.A. (not verified this run).

Price endpoint: SES.MI — exchangeName MIL (Milan), currency EUR, "SeSa S.p.A.", close 90.85 on 2026-10-30; no split events in the 1-month range.

## Hosts tried

- www.sesa.it — HTTP 403 to curl (bot protection; robots.txt does not exclude the paths). WebFetch reached the reports page, which lists only the Q1 FY2027 interim by link.
- www.emarketstorage.it — reachable; 20260729_187443.pdf is the publication notice (6 pages), not the report.
- euroborsa.it — reachable; Q1 FY2027 press release retrieved.
- www.1info.it — connection reset.

## Not established

ISIN (not read from a primary document this run); the ten-year statements; segment EBIT and segment assets; deal list and consideration; pay tables (Relazione sulla remunerazione); holdings and the votes structure (increased voting rights not verified).
