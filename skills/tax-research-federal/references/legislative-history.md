# Legislative history workflow (federal)

Specialization of `shared/legislation-tracking.md` for federal
research. Read this when the user asks "what was the intent",
"committee report", "JCT Bluebook", or any question implicating a
specific recent Public Law (TCJA, CARES, ARPA, IRA, SECURE 2.0,
OBBBA, etc.).

## Step 1 — Resolve the Public Law

1. Popular Name Tool — https://uscode.house.gov/popularnames/popularnames.htm
2. Record the Public Law number and Statutes at Large citation.
3. Sidecar: append a `public_laws_consulted[]` entry with `public_law`
   and `popular_name`.

## Step 2 — Classification Tables

1. Index — https://uscode.house.gov/classification/tables.shtml
2. Locate the table for the Public Law's congressional session.
3. Identify every USC Title 26 section the Public Law amended,
   added, or repealed.
4. Sidecar: populate `classification_tables_url` and
   `affected_irc_sections[]`.

## Step 3 — Verify current text

For each affected section:

1. Pull current text from
   https://uscode.house.gov/browse/prelim@title26.
2. Confirm the text reflects the amendment.
3. Cite as `IRC` / `primary_statute`.

## Step 4 — Authoritative legislative-history artifacts

In order of weight:

### 4a. JCT Bluebook

- https://www.jct.gov/publications/
- Bluebooks typically published 6–12 months after enactment.
- Cite as `JCT_BlueBook` / `legislative_history`.
- If a Bluebook does not yet exist for OBBBA (or any other recent
  Act), record the sentinel pattern documented in
  `shared/citation-discipline.md` keyed to `JCT Bluebook <Public Law>`.

### 4b. Committee reports

- House Ways & Means: https://waysandmeans.house.gov
- Senate Finance: https://www.finance.senate.gov
- Conference reports: same source or congress.gov by report number.
- Cite as `LegHistory` / `legislative_history`.
- Especially probative when statute text is ambiguous (e.g., what
  Congress meant by "specified service trade or business" in
  § 199A(d)(2)).

### 4c. Treasury Greenbook

- https://home.treasury.gov/policy-issues/tax-policy/revenue-proposals
- **Caveat**: Greenbooks describe what the Administration *proposed*.
  Tag carefully:
  - `Greenbook` / `legislative_history` ONLY if the proposal became
    enacted law in substantively the same form.
  - `Greenbook` / `persuasive_non_authority` for descriptive use of
    pre-enactment proposals.

### 4d. CBO scoring report

- https://www.cbo.gov/topics/taxes
- https://www.cbo.gov/cost-estimates
- **Caveat**: CBO scores describe projected revenue effects, not the
  meaning of the enacted statute. Tag:
  - `CBOReport` / `legislative_history` only when the score
    accompanied the enacted bill.
  - `CBOReport` / `persuasive_non_authority` for descriptive use of
    pre-enactment scores.

## Step 5 — Treasury Decisions and proposed regs

After legislation enacts, Treasury typically issues proposed regs,
then final regs, via Treasury Decisions in the Federal Register:

1. https://www.federalregister.gov/agencies/internal-revenue-service
2. Cite the issuance as `TreasuryDecision` / `regulation`.
3. Cite the codified rule (after publication in eCFR Title 26) as
   `TreasReg` / `regulation`.

## Step 6 — Statutes at Large mapping

Use Table III at https://uscode.house.gov/table3/table3years.htm to
trace any USC section back to its enacting Statutes at Large. Cite as
`StatutesAtLarge` / `primary_statute` if you need to quote the
original enacted text (rare; the codified IRC text is canonical for
substantive analysis).

## Step 7 — Cite Checker

For any USC citation that may have been renumbered, use Cite Checker
at https://uscode.house.gov/cite.xhtml.

## Common patterns

### TCJA (Pub. L. 115-97)

- §199A QBI deduction (added)
- §163(j) interest limitation (rewritten)
- §168(k) bonus depreciation (100% phased to 80%/60%/...) — note
  recent OBBBA modifications
- §1400Z Opportunity Zones (added)
- Pre-TCJA "Estate Tax Repeal" carryover-basis NOT enacted; basis
  step-up under §1014 retained.

### IRA (Pub. L. 117-169)

- §55 corporate AMT (rewritten — applies to corps with AFSI > $1B)
- §4501 stock buyback excise tax (added)
- §45 PTC and §48 ITC (extended and modified)
- §30D EV credit (rewritten)

### SECURE 2.0 (Pub. L. 117-328 div. T)

- §401(a)(9) RMD age (raised from 72 to 73 in 2023, 75 in 2033)
- §408A Roth catch-up (mandatory for high earners ≥ $145K in 2024+)
- §408(d)(8) QCD limits indexed
- Saver's Match replacement of Saver's Credit

### OBBBA (Pub. L. 119-XX)

Verify Public Law number against the Popular Name Tool; some details
were still being scored at JCT/CBO at retrieval time.

- TCJA permanence of various individual rate provisions
- §174 R&E expense modifications (verify retention vs.
  capitalization)
- §163(j) interest-limitation modifications
- Bonus depreciation retention under §168(k)

When citing OBBBA changes, consult JCT for the most recent
explanation; flag staleness if the Bluebook isn't yet published.
