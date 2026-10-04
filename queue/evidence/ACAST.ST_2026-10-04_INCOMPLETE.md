# INCOMPLETE evidence: ACAST.ST, Acast AB (publ), 2026-10-04

- run: ANALYSE routine, D 2026-10-04, T 0538, base 446eb1417a1d060e054910b2abe1fb918478ed10, MODEL v4.4.1
- identity: Acast AB (publ), Nasdaq Stockholm main market (moved from First North Premier Growth Market; IPO 17 Jun 2021 at SEK 38), ticker ACAST, ISIN **SE0015960935** (sourced: Annual Report 2025, "The Share" page). Prior check: no `memos/*/` file carries this ISIN or the name "Acast", and no register row matches the name.
- **No verdict.** The data-completeness gate (README §5, D3) stopped the run before any gate was called.

## Why INCOMPLETE: named gaps

The P1 window is FY2016–FY2025, with 11 balance sheets from FY2015 to FY2025. Acast has been an operating company since 2014 and is the same legal entity before and after the IPO, so the pre-IPO years exist. They are not history-limited. This run retrieved FY2020–FY2025 (six income/cash-flow years and seven balance sheets, counting the FY2019 closing equity only from the AR2021 equity statement). The June 2021 IPO prospectus publishes audited IFRS statements for FY2018–FY2020, but the run could not retrieve it. That makes this a record-limited shortfall where more years are published, so D3 applies.

| Needed | Status | Where it exists |
|---|---|---|
| FY2020–FY2025 statements | **retrieved**: annual reports 2021–2025 (PDF) | storage.mfn.se, linked from the mfn.se/a/acast release pages |
| FY2018–FY2019 statements (FY2017 balance sheet) | **not retrieved** | IPO prospectus, approved by Finansinspektionen 7 Jun 2021, "available on investors.acast.com" (press release 7 Jun 2021) |
| FY2015–FY2017 statements | **not retrieved** | statutory annual reports filed with Bolagsverket (pre-IFRS for some years; to confirm) |
| Remuneration report 2025, RPT note (Gate 1C) | not worked (run stopped first) | AGM 2026 documents on mfn.se; AR2025 note on related parties |
| Current price (Gate 2) | not retrieved (run stopped first) | any Nasdaq Stockholm quote endpoint |

## Hosts tried

- `investors.acast.com`: a Next.js stub. The rendered data carries only about/contact/press slugs and no document links. `/en/reports-and-presentations` and `/en/financial-reports` return 404.
- `mfn.se/a/acast/acast-announces-offering-of-shares-and-publishes-prospectus-…`: the release page has no prospectus attachment. Its storage.mfn.se PDF is the press release only.
- `web.archive.org` (CDX for investors.acast.com and its GCS bucket): the agent proxy reset the connection twice (`ws_closed_mid_exchange`).
- 3 exploratory searches (P14) looking for a prospectus mirror (ABG Sundal Collier, Carnegie, Nordnet, FI register) turned up no direct PDF.

**Fix for the next run:** an attended session gets the English prospectus (June 2021) and, if they are wanted, the FY2015–FY2017 Bolagsverket accounts. Alternatively, Jakub decides that pre-prospectus years count as history-limited for a 2021 IPO. Then reset the queue line.

## Sourced figures: consolidated IFRS statements (SEK thousand)

| Line | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|
| Net sales | 591,530 | 1,025,702 | 1,390,366 | 1,636,371 | 1,943,701 | 2,516,851 |
| EBIT (operating profit/loss, as reported) | −148,538 | −221,646 | −352,643 | −258,618 | −57,511 | −18,035 |
| Profit/loss for the year | −172,222 | −300,394 | −286,375 | −179,679 | 78,215 | −112,411 |
| CFO (interest paid already inside CFO) | −188,800 | −106,578 (AR2021); −121,806 (AR2022 restated) | −294,284 | −28,135 | 34,390 | 62,176 |
| Capex: equipment + intangibles | 18,211 | 34,719 | 42,756 | 53,157 | 63,253 | 66,238 |
| **FCF derived = CFO − capex** `[derived]` | −207,011 | −141,297 / −156,525 | −337,040 | −81,292 | −28,863 | −4,062 |
| Acquisitions (cash) | — | — | 209,549 | — | 11,118 | 36,124 + 14,347 deferred |
| Average shares, diluted (thousand) | 126,369 (post 50:1 split) | 157,256 | 179,685 | 181,068 | 187,732 | 181,547 |
| Total assets | 687,638 | 1,864,981 | 1,862,735 | 1,724,265 | 2,010,074 | 2,124,055 |
| Accounts payable | 50,012 | 101,101 | 122,030 | 145,161 | 174,727 | 261,334 |
| Other payables | 45,579 | 53,564 | 132,329 | 78,521 | 114,161 | 139,163 |
| Accrued expenses and prepaid income | 131,532 | 156,070 | 231,751 | 301,994 | 285,556 | 378,590 |
| Current tax liabilities | 874 | 2,894 | n/a, not extracted | n/a, not extracted | 3,738 | 3,732 |
| Cash and cash equivalents | 288,599 | 1,364,751 | 867,757 | 759,463 | 713,704 | 589,334 |
| Bank loans | 100,361 | — | — | — | — | — |
| Lease liabilities (non-current + current) | 32,769 + 13,994 | 23,177 + 24,054 | 11,624 + 17,097 | 34 + 21,914 | 117,709 + n/a | 103,330 + 32,052 (current per Q2 2026 report comparatives) |
| Equity, owners of parent (no NCI) | 305,905 | 1,494,808 | 1,307,880 | 1,143,823 | 1,267,731 | 1,181,277 |
| Goodwill | 24,485 | 27,094 | 351,046 | 337,744 | 369,918 | 380,572 |
| Other intangibles | 27,303 | 43,318 | 89,706 | 95,851 | 97,178 | 103,076 |

- FY2019 closing equity is 218,255 (AR2021 equity statement, opening 1 Jan 2020). No other FY2019 balance-sheet line was retrieved.
- **Extraction conflicts, to be resolved at the next run (§4 rule):** (1) FY2021 CFO is −106,578 in AR2021 and −121,806 in AR2022, which carries a `**` restatement footnote. (2) The Q2 2026 report's FY2025 comparatives show EBIT −23,575 and total assets 2,117,507, against AR2025's −18,035 and 2,124,055. This is an apparent restatement and has not been explained.
- **Customer concentration (P15 input):** AR2025 note 3 says "The Group has a customer relationship that represents more than 10% of the Group's net sales during the financial year. Revenues amounted to SEK 366,853 thousand", which is 14.6% of FY2025 net sales `[derived]`. AR2022, AR2023 and AR2024 each state that no individual customer or group of customers represents more than 10% of total sales.
- **Interim, 30 Jun 2026 (Q2 2026 report):** cash 629,538; total assets 2,246,110; lease liabilities 89,928 non-current + 34,882 current; Q2 EBIT 31,607 and H1 EBIT 36,264; H1 CFO 89,715; Q2 net sales 775,551.
- Shares: 182,465,260 issued per the draft evidence (AR2025). Not re-verified this run.

## Sources retrieved (6 primary documents)
- Annual Reports 2021, 2022, 2023, 2024 and 2025: storage.mfn.se (`8ddbcecf…/acast-annual-report-2021.pdf`, `15f9ae4d…/acast-annual-report-2022.pdf`, `ab704c39…/acast-annual-report-2023.pdf`, `580d9d7f…/acast-annual-report-2024.pdf`, `99586309…/acast-ar-2025-eng-final-260417.pdf`)
- Interim report Q2 2026: storage.mfn.se `e15299a8…/acast-q2-2026-eng.pdf`
- Press release 7 Jun 2021 (prospectus announcement): storage.mfn.se `496ca120…`

*Evidence note: not a memo, not investment advice.*
