# MONC.MI — Moncler S.p.A. — INCOMPLETE evidence (REVIEW 2026-10-08)

- Run: REVIEW, D 2026-10-08, T 0056, base 5b6f9616a92a0f1d3152276766d9842586b36311, MODEL v4.5.2
- Prior memo: `memos/MONC.MI/` v1 (memo_date 2026-07-28, model below v4.5.0), Past graded on FY2021–FY2025 (5y, record-limited)
- Pick: `▶ Method re-tests v4.5.0` (priority 1b)
- No verdict. Orientation only for the next run (MODEL §8.7 item 6, D3).

## Named gap

**P1 window: FY2016–FY2019 statements not retrieved.** The P1 window needs FY2016–FY2025 (with the FY2015 balance sheet). FY2020–FY2025 are retrievable from the ESEF filings below. FY2016–FY2019 exist as published annual reports, but every copy found sits on `www.monclergroup.com`, and that host returns HTTP 403 to this run's clients (curl, with or without browser headers, and WebFetch). The shortfall is record-limited (the years exist and are audited), so under README §5 / MODEL §8.7 item 6 the run is INCOMPLETE rather than proceeding on a 6-year record.

## Hosts tried

| Host | Result |
|---|---|
| `www.monclergroup.com` (IR page; `wp-content/uploads/2016/07/Moncler-Annual-Report-2019.pdf`; `wp-content/uploads/2019/04/Moncler_Annual-Report-2018_ENG.pdf`) | HTTP 403 (curl with browser headers; WebFetch 403) |
| `web.archive.org` (CDX and root) | connection reset at the egress proxy (unreachable from this environment) |
| `filings.xbrl.org` (ESEF, LEI 815600EBD7FB00525B20) | 200 — FY2021–FY2025 annual-report xBRL-JSON (FY2020 comparatives in the FY2021 filing) |
| `query1.finance.yahoo.com` | 200 — price |

Located but unretrievable (URLs from search, all on the blocked host): `wp-content/uploads/2016/07/Moncler-Annual-Report-2019.pdf`, `wp-content/uploads/2016/07/Relazione-Finanziaria-Annuale-2018-5.pdf`, `wp-content/uploads/2016/07/Relazione-Finanziaria-Annuale-2017.pdf`, `wp-content/uploads/2016/07/BILANCIO_MONCLER_2015_ITA_A4.pdf`. An attended session can download these in a browser (AR2019 carries FY2018 comparatives, AR2017 carries FY2016; AR2015/2016 for the FY2015 balance sheet).

## Sourced figures — ESEF xBRL (filings.xbrl.org), EUR 000, IFRS as reported

| FY | Revenue | Operating result | CFO | PP&E purchases (investing) | Net PP&E (YE) | Total assets | Trade & other current payables | Cash & equivalents | Equity attrib. | Goodwill | Other intangibles | NI attrib. | Diluted EPS (EUR) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2020 | 1,440,409 | 368,821 | 406,450 | 92,561 | 802,987 | 2,756,612 | 211,903 | 923,498 | 1,627,048 | 155,582 | 282,308 | 300,351 | 1.18 |
| 2021 | 2,046,103 | 579,220 | 865,314 | 131,828 | 913,322 | 4,267,989 | 348,953 | 932,718 | 2,498,986 | 603,417 | 1,070,074 | 393,533 | 1.47 |
| 2022 | 2,602,890 | 774,547 | 662,577 | 169,853 | 1,074,490 | 4,639,312 | 482,425 | 882,254 | 2,902,170 | 603,417 | 1,086,706 | 606,697 | 2.24 |
| 2023 | 2,984,217 | 893,839 | 914,865 | 176,423 | 1,082,480 | 4,992,020 | 538,586 | 998,799 | 3,214,335 | 603,417 | 1,096,473 | 611,931 | 2.26 |
| 2024 | 3,108,924 | 916,324 | 989,506 | 195,195 | 1,250,879 | 5,504,590 | 540,914 | 1,187,978 | 3,586,580 | 603,417 | 1,106,784 | 639,596 | 2.36 |
| 2025 | 3,132,128 | 913,356 | 960,515 | 220,114 | 1,498,380 | 5,959,504 | 527,322 | 1,226,277 | 3,849,694 | 603,417 | 1,108,645 | 626,670 | 2.31 |

- Tie-out: revenue, operating result, CFO, capex, total assets and payables for FY2021–FY2025 equal the prior memo's B1 (tier-2 series accepted there on its FY2025/FY2022 anchors). ESEF `Cash and cash equivalents` excludes short-term investments (the prior memo's cash + STI: FY2025 €1,477,405k).
- Repurchases (ESEF `PaymentsToAcquireOrRedeemEntitysShares`): FY2022 €48,352k; FY2023 €0. Not tagged at the default context for other years.
- Not extracted this run (needed for the v4.5.0 re-test; available in the ESEF filings): lease liabilities, the CE split of other current liabilities, intangible-asset capex and capitalised software, depreciation of PP&E and amortisation of software (P20 floor), the FY2025 related-party note, the treasury-share movement.

## Price

MONC.MI, endpoint currency EUR, exchange MIL: close €43.53 on 2026-10-06 (the 2026-10-07 bar had no close at fetch time).

## P14

Exploratory searches: 2 (budget ~2). Due-check operations: 0 (priority 1b needs none). Primary retrieval: 3 ESEF filings, 1 price GET; 4 blocked primary URLs.
