# Run note — ANALYSE BAJAJ-AUTO.NS — 2026-11-06 1803

- Job: ANALYSE · Key: BAJAJ-AUTO.NS (Bajaj Auto Limited, ISIN INE917I01010)
- D: 2026-11-06 · T: 1803 (Europe/Prague)
- Base sha: 4b78cfe4733f1f9f4aebe5956654c96be6615427 · model_version v4.8.0 read at preflight
- Preflight: guard live (canary refused), one repository, ledger read (223 rows). Pick: the `▶ Group dependencies` lines ABBN.SW and ATCO-B.ST fail check (a), because both have current memos, so both are recorded `memo exists`. SUNDRMFAST.NS was claimed (open PR #360 `[running]`). BAJAJ-AUTO.NS's partial line (2026-11-03) was taken first. No prior under name or ISIN.
- Status: complete. Memo v1 written, AVOID (Future + SF). This run resumed the first-overrun record and finished the group build.

**Written:** `memos/BAJAJ-AUTO.NS/BAJAJ-AUTO.NS_2026-11-06_GSC.md` (v1; group of two units and the controlled listed subsidiary Bajaj Mobility; STD; G6 above the P31 line; funding pairing A governs) and `queue/rows/2026-11-06_1803_ANALYSE_BAJAJ-AUTO.NS.md`, which carries `BMAG.SW` as a group dependency (memo missing). Deleted `queue/evidence/BAJAJ-AUTO.NS_2026-11-03_INCOMPLETE.md`.

**Failed or limited:**
- H1 FY2027 results not retrieved: api.bseindia.com HTTP 403 (Akamai), nseindia.com bot check, and the IR site lists no quarterlies. Gate 2 uses the audited FY2026 balance sheet.
- India CPI series not retrieved (data.gov.in HTTP 403), so P20 falls to all capex (tier 3).
- BMAG's own annual reports were not opened. The KTM pre-deal record comes from the acquirer's PBAG summaries.

**Needs Jakub:**
- Two IDEAS candidates in the row file: how a captive-finance memo's core fields carry the funding pairing; and whether a step-acquisition through an unlisted holding company of a listed target reads the listed target's P3 record (ADVERSE here) or as a private target (CAUTION).
