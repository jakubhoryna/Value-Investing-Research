# Exchange suffix verification for MODEL v4.5.0 §7.1a (2026-10-06)

**What this is.** The evidence behind the §7.1a suffix table (decision 10: every exchange the SWEEP price endpoint serves is admissible). One GET per symbol to the SWEEP endpoint, `query1.finance.yahoo.com/v8/finance/chart/{symbol}?range=5d&interval=1d`, from an attended build session on 2026-10-06. Recorded: the endpoint's `exchangeName` and `currency` (the `px_unit` rule) and the date of the last daily bar. Prices are not carried. A suffix is **served** when the symbol returns a bar from the last 5 trading days and the expected currency.

## Served (the §7.1a table)

| Suffix | Venue | Symbol | exchangeName | currency | Last bar |
|---|---|---|---|---|---|
| (none) | US line | AAPL | NMS | USD | 2026-10-05 |
| (US class share) | NYSE, dot key, hyphen query | BRK-B (key BRK.B) | NYQ | USD | 2026-10-05 |
| `.TO` | Toronto | CSU.TO | TOR | CAD | 2026-10-05 |
| `.V` | TSX Venture | LMN.V | VAN | CAD | 2026-10-05 |
| `.CN` | Canadian Securities Exchange | URL.CN | CNQ | CAD | 2026-10-05 |
| `.NE` | Cboe Canada | AAPL.NE | NEO | CAD | 2026-10-05 |
| `.PA` | Paris | ABCA.PA | PAR | EUR | 2026-10-06 |
| `.AS` | Amsterdam | AD.AS | AMS | EUR | 2026-10-06 |
| `.BR` | Brussels | UCB.BR | BRU | EUR | 2026-10-06 |
| `.LS` | Lisbon | JMT.LS | LIS | EUR | 2026-10-06 |
| `.IR` | Euronext Dublin | KRZ.IR | ISE | EUR | 2026-10-06 |
| `.MI` | Milan | BC.MI | MIL | EUR | 2026-10-06 |
| `.MC` | Madrid | IBE.MC | MCE | EUR | 2026-10-06 |
| `.DE` | Xetra | SAP.DE | GER | EUR | 2026-10-06 |
| `.VI` | Vienna | ANDR.VI | VIE | EUR | 2026-10-06 |
| `.HE` | Helsinki | FORTUM.HE | HEL | EUR | 2026-10-06 |
| `.AT` | Athens | ETE.AT | ATH | EUR | 2026-10-06 |
| `.TL` | Tallinn | LHV1T.TL | TAL | EUR | 2026-10-06 |
| `.RG` | Riga | SAF1R.RG | RIS | EUR | 2026-10-06 |
| `.VS` | Vilnius | APG1L.VS | LIT | EUR | 2026-10-06 |
| `.SW` | SIX Swiss | NESN.SW | EBS | CHF | 2026-10-06 |
| `.ST` | Stockholm | 8TRA.ST | STO | SEK | 2026-10-06 |
| `.CO` | Copenhagen | CARL-B.CO | CPH | DKK | 2026-10-06 |
| `.OL` | Oslo | AUTO.OL | OSL | NOK | 2026-10-06 |
| `.IC` | Iceland | ARION.IC | ICE | ISK | 2026-10-05 |
| `.L` | London | BA.L | LSE | GBp | 2026-10-06 |
| `.WA` | Warsaw | ACP.WA | WSE | PLN | 2026-10-06 |
| `.PR` | Prague | CEZ.PR | PRA | CZK | 2026-10-06 |
| `.BD` | Budapest | OTP.BD | BUD | HUF | 2026-10-06 |
| `.RO` | Bucharest | TLV.RO | BVB | RON | 2026-10-06 |
| `.IS` | Istanbul | THYAO.IS | IST | TRY | 2026-10-06 |
| `.TA` | Tel Aviv | SMSH.TA | TLV | ILA | 2026-10-06 |
| `.SR` | Saudi Exchange (Tadawul) | 2222.SR | SAU | SAR | 2026-10-06 |
| `.AE` | Dubai (DFM) | EMAAR.AE | DFM | AED | 2026-10-06 |
| `.QA` | Qatar | QNBK.QA | DOH | QAR | 2026-10-06 |
| `.KW` | Kuwait (Boursa) | NBK.KW | KUW | KWF | 2026-10-06 |
| `.JO` | Johannesburg | NPN.JO | JNB | ZAc | 2026-10-06 |
| `.NS` | NSE India | TCS.NS | NSI | INR | 2026-10-06 |
| `.BO` | BSE India | TCS.BO | BSE | INR | 2026-10-06 |
| `.T` | Tokyo | 2502.T | JPX | JPY | 2026-10-06 |
| `.HK` | Hong Kong | 0700.HK | HKG | HKD | 2026-10-06 |
| `.SS` | Shanghai | 688825.SS | SHH | CNY | 2026-09-30 (Golden Week holiday) |
| `.SZ` | Shenzhen | 300750.SZ | SHZ | CNY | 2026-09-30 (Golden Week holiday) |
| `.TW` | Taiwan (TWSE) | 2330.TW | TAI | TWD | 2026-10-06 |
| `.TWO` | Taipei Exchange (TPEx) | 6488.TWO | TWO | TWD | 2026-10-06 |
| `.KS` | Korea (KOSPI) | 005930.KS | KSC | KRW | 2026-10-06 |
| `.KQ` | Korea (KOSDAQ) | 247540.KQ | KOE | KRW | 2026-10-06 |
| `.SI` | Singapore | D05.SI | SES | SGD | 2026-10-06 |
| `.JK` | Indonesia (Jakarta) | BBCA.JK | JKT | IDR | 2026-10-06 |
| `.BK` | Thailand (SET) | PTT.BK | SET | THB | 2026-10-06 |
| `.KL` | Bursa Malaysia | 1155.KL | KLS | MYR | 2026-10-06 |
| `.VN` | Vietnam (HOSE) | VNM.VN | VSE | VND | 2026-10-06 |
| `.AX` | Australia (ASX) | ZIP.AX | ASX | AUD | 2026-10-06 |
| `.NZ` | New Zealand (NZX) | FPH.NZ | NZE | NZD | 2026-10-06 |
| `.SA` | São Paulo (B3) | VALE3.SA | SAO | BRL | 2026-10-05 |
| `.MX` | Mexico (BMV) | WALMEX.MX | MEX | MXN | 2026-10-05 |
| `.BA` | Buenos Aires | GGAL.BA | BUE | ARS | 2026-10-05 |
| `.SN` | Santiago | SQM-B.SN | SGO | CLP | 2026-10-05 |
| `.CL` | Colombia (BVC) | ECOPETROL.CL | BVC | COP | 2026-10-05 |

Every returned `currency` equals the table's Unit column.

## Served, never a key

German regional venues return fresh SAP quotes in EUR: `.F` (FRA), `.MU` (MUN), `.SG` (STU), `.DU` (DUS), `.HM` (HAM), `.HA` (HAN). A German line keys on Xetra `.DE`.

## Not served or stale (data-access gap, never a framework block)

| Venue | Symbol tried | Result |
|---|---|---|
| Abu Dhabi ADX | IHC.AD | 404 — no data |
| Philippines | SM.PS | 404 — no data |
| Colombo | JKH.N0000.CM | 404 — no data |
| Nairobi | SCOM.NR | 404 — no data |
| Lagos | DANGCEM.LG | 404 — no data |
| Ljubljana | KRKG.LJ | 404 — no data |
| Zagreb | HT.ZA | 404 — no data |
| Berlin | SAP.BE | 404 — no data |
| Cairo | COMI.CA | stale, last bar 2024-07-23 |
| Karachi | OGDC.KA | stale, last bar 2024-07-23 |
| Lima | CREDITC1.LM | stale, last bar 2019-06-28, no currency |

A first Riga symbol (GRD1R.RG) returned 404; SAF1R.RG returned a fresh bar, so `.RG` is served.

## Findings on served venues

- `MASTERPLAST.BD` (Masterplast, TODO block C2): last bar 2024-07-19. Budapest is served (OTP.BD is fresh), the name is not: a data-access note, stale under §8.3.
- `COPN.SW` (Cosmo Pharmaceuticals, a register key): last bar 2026-08-14, more than 5 trading days old. SIX is served (NESN.SW is fresh). The next SWEEP marks it stale; check the listing at the name's next touch.
- `IHC.AE` (International Holding Company, TODO coverage audit): IHC trades on Abu Dhabi ADX, which the endpoint does not serve; `.AE` is Dubai DFM. It stays a data-access item.
