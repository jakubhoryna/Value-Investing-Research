# MHA.L — MHA plc — INCOMPLETE evidence (ANALYSE 2026-10-30)

Run: ANALYSE routine, D 2026-10-30, T 2203, base df90d8bacf21ea8205ac432deabfcf436645e028, MODEL v4.7.0. No verdict.

## Named gap

**INCOMPLETE (record-limited: admission-document FY2022–FY2024 accounts unretrievable)** (routines/README.md §5 D3; MODEL §2·1A, §8.7 item 6).

MHA plc (company no. 16268837) listed on AIM on 15 April 2025 after a group reorganisation of 11 April 2025 (share-for-share acquisition of MHA Advisory Ltd, MacIntyre Hudson Holdings Ltd and MHA Audit Services LLP; designated member of MHA Member LLP). Its first statutory accounts are FY2026 (year to 31 March 2026), with FY2025 as a merger-accounted comparative of the "Pre-Reorganisation Group" (MacIntyre Hudson LLP and MacIntyre Hudson Holdings Ltd), "prepared on the same basis as the historical financial information in the Company's AIM Admission Document dated 10 April 2025" (FY2026 CFO's review).

That admission document carries **audited combined historical financial information for the three years to 31 March 2024** (a 95-page financial section). Audited carve-out or combined statements start the record (MODEL §2·1A), so FY2022–FY2024 exist and are published: this is a record-limited shortfall, not history-limited, and the D3 gate stops the run. The document sits only on the issuer's IR host, www.mha.co.uk, which returned HTTP 403 to the run (not retried or circumvented). The FY2025 combined accounts (posted September 2025, FY2024 comparatives) sit on the same host.

What the missing years decide: the per-share series cannot start before FY2026 in any case (no shares before the reorganisation; the filer prints no FY2025 EPS), and FY2026 L/E is 205.5% (below), so Past is WEAK on every reading of the record. But the J6 limb (a) test (three consecutive ROCE or FCFROCE declines, the last in one of the two latest years) and therefore the Past reason cell (`ROCE decline` precedes `leverage` in the §7.1 vocabulary) depend on FY2022–FY2024, as do B1–B3. The run does not fill them with an assumption.

**Basis warning for the attended build.** FY2022–FY2025 are on the partnership basis: partner remuneration was an allocation of profit, not an expense (FY2025 £73,765k allocated to members' accounts; members' interests were liabilities and equity was £12,899k at 31 Mar 2025). FY2026 charges partner compensation as an expense. J1 OI is as reported in each year; the filer says statutory profit for the two years is "not directly comparable".

## Sourced figures — FY2026 annual report (£'000)

Sources: preliminary results RNS, 21 Jul 2026 (Investegate, full statements and notes; stated as expected to equal the audited accounts); Annual Report & Accounts 2026 filed at Companies House 11 Aug 2026 (114-page scanned PDF; pages read: contents, highlights, Directors' Remuneration Report pp. 55–56).

| Item | FY2026 | FY2025 (comparative, LLP basis) |
|---|---|---|
| Revenue | 251,363 | 224,151 |
| Client expenses and disbursements | (11,065) | (8,466) |
| Other operating income (commissions, compensation payments) | 373 | 1,891 |
| Administrative expenses | (201,042) | (138,151) |
| Operating profit before non-underlying items (APM) | 39,629 | 79,425 |
| Non-underlying items | (2,344) | 6,843 |
| Operating profit (lowest operating subtotal) | 37,285 | 86,268 |
| — of which gain on bargain purchase (J3/J1: a gain, removed when positive) | 1,144 | 6,843 |
| J1 OI, derived (operating profit − bargain-purchase gain) | 36,141 | 79,425 |
| Finance income / expense | 642 / (1,600) | 812 / (1,294) |
| Profit before tax | 36,327 | 85,872 |
| Profit for the year | 28,091 | 83,072 |
| Employee benefit expense (incl. partner compensation charged as expense) | 148,505 | 89,902 |
| Depreciation PP&E / amortisation intangibles / ROU | 1,213 / 1,519 / 3,643 | 888 / 1,130 / 3,411 |
| Share-based payment expense | 2,454 | – |

Non-underlying FY2026: share-based payment 318; amortisation of deemed remuneration (BTSEE) 2,135; gain on bargain purchase (1,144); AIM listing cost 1,035.

Revenue by service line FY2026 (FY2025): Audit & Assurance 124,483 (113,889); Tax 46,283 (40,805); Advisory 70,878 (61,384); Wealth 9,719 (8,073). Organic growth 6.4%, acquisitive 5.8%. One operating segment (professional services; note 6). No customer above 10% of revenue in FY2026 or FY2025 (note 4). Recurring revenue ≈ 87%.

Balance sheet, 31 Mar 2026 (31 Mar 2025): total assets 167,432 (137,593); cash 28,531 (18,768); trade and other receivables 87,052 (72,949), incl. contract assets 25,940 (14,594); PP&E 5,465 (4,846); ROU assets 17,247 (17,314); intangibles 26,772 (21,548); trade payables 5,597 (2,423); other payables 36,008 (67,415); social security and other taxes 9,058 (6,791); accruals 10,416 (9,676); contract liabilities 15,246 (6,470); deferred consideration current 2,178 (1,621), non-current 322 (1,832); borrowings 3,177 (1,150); lease liabilities 19,750 (19,677); provisions 7,433 (5,257) = lease dilapidations 2,483 (2,432, unwinding in finance costs) + claims and regulatory 4,950 (2,825); current tax 2,504 (2,382); total liabilities 112,633 (124,694); equity 54,799 (12,899), no NCI line.

Cash flow FY2026 (FY2025): cash generated from operations 82,868 (70,945); tax paid (10,164) ((1,848)); net cash from operations 72,704 (69,097); PP&E (978) ((2,028)); intangibles (13); initial ROU payments (52); acquisition of subsidiaries net (2,974); interest paid in financing: borrowings (44) ((96)), leases (1,034) ((972)), other (523) ((110)); payments to members (66,788) ((70,138)); loan note paid to partners (76,800); capital invested by members 15,262; capital repaid to members (14,548); share issue 98,012, costs (7,296); dividends (2,570) ((3,980)).

**FCF basis question for the attended build.** Reported CFO (72,704) includes an "increase in trade and other payables" of 39,525 while the payables balance fell by 15,893; payments to members (66,788) sit in financing. The filer's "adjusted operating cash conversion" (operating cash flow before tax adjusted for MHA Member LLP balances ÷ operating profit before non-underlying items) is 115% (FY2025 89%). Derived readings, labelled: as reported, CFO − interest paid moved in − capex = 70,060; on the filer's member-adjusted conversion, 1.15 × 39,629 − 10,164 − 1,601 − 1,043 ≈ 32,765 (± ≈ 0.2m for the rounded 115%). The split of payments to members between pre-IPO allocations and post-IPO compensation is not disclosed in the documents read. P20: capex 1,043 is below the PP&E depreciation floor (1,213), so maintenance capex = all capex in FY2026 whatever π.

Shares: 286,899,495 in issue at 21 Aug 2026 (AGM result RNS); 287,059,568 after the 28 Sep 2026 allotment (Companies House SH01, capital £2,870,595.68 at 1p). EBT holds 34,928,451 (12.17%, TR-1 notice). FY2026 weighted diluted 254,122,079 (options 1,064,554, warrants 227,514). Options: 750,000 nominal-cost LTIP options.

Deals: BTSEE (Baker Tilly South East Europe), completed 10 Aug 2025: consideration €5,875k (£5,081k) plus acquisition equity compensation €21,456k (£18,556k) treated as deemed remuneration; fair value of net assets £6,225k; bargain purchase gain £1,144k; contributed revenue £12.8m and PBT £1.1m to 31 Mar 2026; pro forma group revenue £257.7m, PBT £36.8m. MS UAE (Moore Stephens LLC and Moore Stephens Consulting LLC), completed 2 Apr 2026: AED 30m (£6.2m), 50% cash, 50% shares, plus ≈ AED 2.4m on completion accounts.

## Gate 1C inputs (Directors' Remuneration Report, AR 2026 pp. 55–56)

| FY2026 | Base salary | Partner fixed profit share | Partner variable profit share | Vesting of share awards | Benefits | Pension | Total |
|---|---|---|---|---|---|---|---|
| Rakesh Shaunak (CEO) | 15,000 | 335,000 | 318,269 | 153,095 | 0 | 0 | £821,364 |
| Steve Moore (CFO) | 15,000 | 335,000 | 261,435 | 107,166 | 0 | 0 | £718,601 |
| Geoff Barnes (Chair) | 81,780 | – | – | – | – | – | £81,780 |
| Linda Main / Sir Bob Neill (NEDs) | 60,614 each | – | – | – | – | – | £60,614 each |

LTIP on Admission (nominal-cost options, 3-year EPS and TSR conditions, TSR 8%–16% CAGR): maximum value £500,000 (Shaunak) and £350,000 (Moore) at the placing price. A grant-basis year total for Shaunak, derived (salary + profit shares + LTIP grant), would be £1,168,269; the P17 proportionality line on FY2026 NI (£28,091k) is £1,404,550. FY2026 is the only pay year (no directors' pay before the plc).

Directors' interests at 31 Mar 2026: Shaunak 5,121,413 (1.79%), Moore 4,548,233 (1.59%); NEDs 10,000 each. Management 9,669,646 shares = 3.37% of 287,059,568 (≥ 1%). Interim dividends of £230k paid to related parties (note 31). No controlling party (company note 13).

## Gate 2 inputs (indicative, at px; not a verdict)

Price endpoint: MHA.L — exchangeName LSE, currency GBp, "MHA PLC ORD 1P", close 139.5 on 2026-10-30; first trade 2025-04-15; no split events. MCap ≈ £400.45m (139.5p × 287,059,568). Debt-equivalents 27,910 (borrowings 3,177 + leases 19,750 + deferred consideration 2,500 + dilapidations 2,483). EV/OI on the derived J1 OI 36,141: no-cash 11.9, all-cash 11.1. No interim after 31 Mar 2026 yet (H1 FY2027 due late 2026).

Derived returns FY2026, for orientation only: NIBCL 42,821 (trade payables, taxes, accruals, contract liabilities, current tax; other payables 36,008 stay in CE, burden of proof); CE_wc 124,611, CE_xc 96,080; ROCE end-of-period 29.0% (wc) / 37.6% (xc); on beginning CE 32.9% / 39.7%. L/E 205.5% (FY2025 966.7%, members' interests as liabilities).

## Hosts tried

- www.mha.co.uk/investors — HTTP 403 (WebFetch); admission document and FY2025 accounts not retrieved. Not circumvented.
- www.investegate.co.uk — preliminary results RNS 21 Jul 2026: retrieved.
- find-and-update.company-information.service.gov.uk — MHA plc filing history and the FY2026 full accounts PDF (scanned images; read visually): retrieved.
- query1.finance.yahoo.com — MHA.L chart: retrieved.

## For the attended build

Take the AIM admission document (10 Apr 2025) and the FY2025 combined accounts from a browser (mha.co.uk/investors/investor-information), then build FY2022–FY2026 (5 years, with the FY2021 balance sheet if printed), the J6 test on ROCE and FCFROCE, and the FCF reading of payments to members.
