# Legislation tracking

Workflow for tracing recent Public Laws to the USC sections they
amended, and for identifying authoritative legislative-history
artifacts. Used by `irc-section-lookup`, `tax-research-federal`, and
`planning-multi-year`.

## When to invoke this workflow

- User mentions a Public Law by its popular name: "TCJA", "Inflation
  Reduction Act", "OBBBA", "SECURE 2.0", "American Rescue Plan",
  "CARES Act", "Tax Cuts and Jobs Act", etc.
- User mentions a Public Law by number: "Pub. L. 117-169",
  "P.L. 119-XX", "Public Law 115-97", etc.
- User asks "what changed in [§ X] under [recent legislation]".
- User asks for "current law" on a topic where recent legislation
  may have amended the underlying statute.
- A planning skill is scoring a strategy whose eligibility depends on
  a sunset, phase-out, or amendment effective in a tax year > 2024.

## Workflow

### 1. Resolve the Public Law

If user gave a popular name:
1. Fetch the **Popular Name Tool** at
   `https://uscode.house.gov/popularnames/popularnames.htm`.
2. Locate the act by name; record its Public Law number and Statutes
   at Large citation.

If user gave a Public Law number, skip to step 2.

### 2. Retrieve the Classification Table

1. Fetch the **Classification Tables** index at
   `https://uscode.house.gov/classification/tables.shtml`.
2. Navigate to the table for the Public Law's congressional session.
3. Identify every USC section the Public Law amended, added, or
   repealed.
4. Record the table URL in the JSON sidecar's
   `public_laws_consulted[].classification_tables_url` field.
5. Record affected sections in
   `public_laws_consulted[].affected_irc_sections`.

### 3. Verify each affected section's current text

For each affected USC section:
1. Fetch the current section from
   `https://uscode.house.gov/browse/prelim@title26` (USLM canonical).
2. Confirm the text is post-amendment.
3. Cite as `IRC` with `weight: primary_statute` and pin to the
   specific subsection/paragraph.

### 4. Locate authoritative legislative-history artifacts

In order of authoritativeness:

1. **JCT Bluebook** for the relevant Congress at
   `https://www.jct.gov/publications/`. Bluebooks are typically
   published 6–12 months after enactment. Cite as `JCT_BlueBook`
   with `weight: legislative_history`.

2. **Committee reports** (House Ways & Means, Senate Finance,
   Conference). Find via:
   - `https://waysandmeans.house.gov/`
   - `https://www.finance.senate.gov/`
   - Or via congress.gov for the bill's report numbers.
   Cite as `LegHistory` with `weight: legislative_history`.

3. **Treasury Greenbook** (Administration's Fiscal Year Revenue
   Proposals) at
   `https://home.treasury.gov/policy-issues/tax-policy/revenue-proposals`.
   - **Caveat**: Greenbooks describe what the Administration *proposed*.
     Tag as `Greenbook`/`legislative_history` ONLY if the proposal
     became enacted law in substantively the same form. Otherwise tag
     `Greenbook`/`persuasive_non_authority` for descriptive use only.

4. **CBO scoring report** at `https://www.cbo.gov/topics/taxes` or
   `https://www.cbo.gov/cost-estimates`.
   - **Caveat**: CBO scores describe projected revenue effects. They
     are not interpretive authority on the meaning of the enacted
     statute. Tag as `CBOReport`/`legislative_history` only when the
     score accompanied the enacted bill. Tag
     `CBOReport`/`persuasive_non_authority` for descriptive use of
     pre-enactment scores.

### 5. Check for proposed regulations and Treasury Decisions

After legislation enacts, Treasury typically issues proposed
regulations, then final regulations. Check:

1. **Federal Register IRS feed** at
   `https://www.federalregister.gov/agencies/internal-revenue-service`
   for proposed and final rules implementing the Public Law.
2. **Treasury Decisions** are the issuance vehicle in the Federal
   Register; the codified rule appears in eCFR. Tag the issuance as
   `TreasuryDecision`/`regulation` and the codified rule as
   `TreasReg`/`regulation`.

### 6. Cite Checker (optional sanity check)

For any USC citation that may have been renumbered or reclassified,
use the **Cite Checker** at `https://uscode.house.gov/cite.xhtml` to
verify the citation resolves to current section text.

## Output requirements

When this workflow is exercised, the JSON sidecar MUST populate:
- `public_laws_consulted[]` with at least `public_law` and
  `popular_name` for each Public Law referenced.
- `classification_tables_url` for each Public Law (the URL of the
  specific table consulted).
- `affected_irc_sections[]` listing every USC § the Public Law
  amended that is material to the analysis.

## Common Public Laws — quick reference

| Popular name | Public Law | Year | Notable IRC topics |
|---|---|---|---|
| Tax Cuts and Jobs Act (TCJA) | Pub. L. 115-97 | 2017 | §199A QBI; §163(j) interest limit; §168 bonus depreciation; §1400Z OZ |
| CARES Act | Pub. L. 116-136 | 2020 | NOL changes; §163(j) relaxation; §172 carryback restoration |
| Consolidated Appropriations Act 2021 | Pub. L. 116-260 | 2020 | PPP deductibility; ERC extension |
| American Rescue Plan Act | Pub. L. 117-2 | 2021 | §6428B Recovery Rebate; CTC expansion (1 year) |
| Inflation Reduction Act (IRA) | Pub. L. 117-169 | 2022 | §55 corporate AMT; §4501 stock buyback; §45 PTC; §48 ITC; §30D EV |
| SECURE 2.0 | (in Pub. L. 117-328 div. T) | 2022 | §401(a)(9) RMD age; §408A Roth catch-up |
| One Big Beautiful Bill Act (OBBBA) | (Pub. L. 119-XX) | 2025 | TCJA permanence; many extenders; §174 R&E; §163(j) modifications |

The Public Law number for OBBBA should be verified against the
Popular Name Tool at retrieval time — this table is a quick
reference, not authority.

## Related skills

- **`irc-section-lookup`**: implements steps 1–3 and 6 as the user-
  facing primary path.
- **`tax-research-federal`**: implements steps 4–5 as part of
  legislative-history workflow.
- **`planning-multi-year`**: consults this file when scoring
  strategies whose eligibility depends on sunset/effective-date
  provisions.
- **`compliance-ssts-circular230`**: references the IRS Guidance
  Primer at
  `https://www.irs.gov/newsroom/understanding-irs-guidance-a-brief-primer`
  for malpractice-defense scaffolding.
