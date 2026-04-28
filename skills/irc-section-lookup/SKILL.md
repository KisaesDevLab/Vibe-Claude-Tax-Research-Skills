---
name: irc-section-lookup
description: |
  Resolves IRC section references and Public Law popular names to
  canonical USC text and identifies legislative-history artifacts.
  Implements the Public-Law-to-USC workflow per shared/legislation-
  tracking.md: when the user references a Public Law by popular name
  (TCJA, IRA, OBBBA, SECURE 2.0, CARES Act, ARPA) or by Public Law
  number, uses the USC Popular Name Tool and Classification Tables
  to resolve all affected USC sections. Use when the user asks
  "what does §X say", "look up §X", "what changed under TCJA",
  "OBBBA", "Inflation Reduction Act", "SECURE 2.0", "Public Law
  117-169", "JCT Bluebook", "Bluebook for §X", "Greenbook for §Y",
  or "Classification Tables". Make sure to use this skill whenever
  the user mentions an IRC section by number, a Public Law by
  popular name or number, or asks about legislative history.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# irc-section-lookup — IRC + Public Law resolution

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `shared/legislation-tracking.md` — Public-Law-to-USC workflow.
6. `references/legislation-tracking.md` — implementation of the
   Public-Law-to-USC workflow per shared/legislation-tracking.md
   (per BUILD_PLAN).
7. `references/subtitle-map.md` — IRC Subtitles A–K mapping (per
   BUILD_PLAN).

## Operative authority

- IRC (Title 26 USC).
- USC Popular Name Tool:
  https://uscode.house.gov/popularnames/popularnames.htm
- USC Classification Tables:
  https://uscode.house.gov/classification/tables.shtml
- USC Cite Checker: https://uscode.house.gov/cite.xhtml
- USC USLM (canonical text):
  https://uscode.house.gov/browse/prelim@title26
- JCT publications: https://www.jct.gov/publications/
- Treasury Greenbook:
  https://home.treasury.gov/policy-issues/tax-policy/revenue-proposals
- CBO: https://www.cbo.gov/topics/taxes
- Federal Register IRS feed:
  https://www.federalregister.gov/agencies/internal-revenue-service

## Workflow

### 1. Intake

Two primary input modes:

#### Mode A: section-number lookup
User asks "what does §X say" or "look up §X" with an IRC section.

#### Mode B: Public-Law lookup
User asks about TCJA, OBBBA, IRA, SECURE 2.0, CARES Act, ARPA, or
similar by popular name OR by Public Law number.

Both modes may be combined (e.g., "what did TCJA do to §199A?").

### 2. Section-number resolution (Mode A)

For a clean §-number lookup:

1. Fetch USLM canonical text from
   `https://uscode.house.gov/browse/prelim@title26`.
2. Note the IRC subtitle / chapter / subchapter / part / subpart
   classification (use `references/subtitle-map.md`).
3. Identify amendments: USC text shows amendment annotations.
4. Use the Cite Checker
   (https://uscode.house.gov/cite.xhtml) for any potentially
   renumbered or reclassified section.
5. Output: cite as `IRC` with `weight: primary_statute` per
   shared/citation-discipline.md. Include `quoted_text` (≤75
   words), `pin_cite` (subsection / paragraph), `retrieved_date`.

### 3. Public-Law resolution (Mode B)

Implements `shared/legislation-tracking.md` workflow:

1. **Resolve to Public Law number**: if user gave popular name,
   fetch the Popular Name Tool at
   `https://uscode.house.gov/popularnames/popularnames.htm`.
   Record the Public Law number and Statutes-at-Large citation.

2. **Retrieve Classification Table**: fetch Classification Tables
   index at `https://uscode.house.gov/classification/tables.shtml`.
   Navigate to the table for the Public Law's congressional
   session. Identify every USC section the Public Law amended,
   added, or repealed.

3. **Verify each affected section's current text**: for each
   affected USC section, fetch current text from USLM. Confirm
   text is post-amendment.

4. **Locate legislative-history artifacts**: in order of
   authoritativeness:
   - **JCT Bluebook** for the relevant Congress at
     `https://www.jct.gov/publications/`. Bluebooks typically
     published 6-12 months after enactment.
   - **Committee reports** (House Ways & Means, Senate Finance,
     Conference) via `https://waysandmeans.house.gov/`,
     `https://www.finance.senate.gov/`, or congress.gov.
   - **Treasury Greenbook** (only if proposal enacted) at
     `https://home.treasury.gov/policy-issues/tax-policy/revenue-proposals`.
   - **CBO scoring report** (only if accompanying enacted bill)
     at `https://www.cbo.gov/topics/taxes`.

5. **Check for proposed regulations and Treasury Decisions**:
   Fetch Federal Register IRS feed at
   `https://www.federalregister.gov/agencies/internal-revenue-service`
   for proposed and final rules implementing the Public Law.

6. **Output**: populate `public_laws_consulted[]` with Public Law,
   popular name, Classification Tables URL, affected IRC sections,
   and any legislative-history artifacts.

### 4. Common Public Laws — quick reference

Verify against the Popular Name Tool at retrieval time. This
table is a quick reference, not authority.

| Popular name | Public Law | Year | Notable IRC topics |
|---|---|---|---|
| Tax Cuts and Jobs Act (TCJA) | Pub. L. 115-97 | 2017 | §199A QBI; §163(j); §168(k); §174 (capitalization-and-amortization for years after 2021); §1400Z OZ; §245A territorial DRD; §951A GILTI; §250 FDII; §59A BEAT |
| CARES Act | Pub. L. 116-136 | 2020 | NOL carryback restoration; §163(j) relaxation; §172 carryback; §168(k) QIP fix |
| Consolidated Appropriations Act 2021 | Pub. L. 116-260 | 2020 | PPP deductibility; ERC extension |
| American Rescue Plan Act (ARPA) | Pub. L. 117-2 | 2021 | §6428B Recovery Rebate; CTC expansion (1 year) |
| Infrastructure Investment and Jobs Act (IIJA) | Pub. L. 117-58 | 2021 | ERC retired post-Q3 2021; cryptocurrency reporting expansion |
| CHIPS and Science Act | Pub. L. 117-167 | 2022 | §48D advanced-manufacturing investment credit |
| Inflation Reduction Act (IRA) | Pub. L. 117-169 | 2022 | §55 corporate AMT; §4501 stock-buyback excise; §45 PTC; §48 ITC; §30D EV credit |
| SECURE 2.0 | Pub. L. 117-328 div. T | 2022 | §401(a)(9) RMD age progression; §414(v) catch-up; Roth catch-up for high earners |
| One Big Beautiful Bill Act (OBBBA) | Pub. L. 119-XX | 2025 | TCJA permanence framework; §174 R&E modifications; §163(j) modifications; many extenders |

The OBBBA Public Law number should be verified against the Popular
Name Tool at retrieval time.

### 5. Conclusion + sidecar

JSON sidecar validates against `shared/output-schema.json`.

For Mode A (section lookup):
- `authorities[]` with at least one IRC entry.
- Optional: relevant Treasury Regulations.

For Mode B (Public-Law resolution):
- `public_laws_consulted[]` with `public_law`, `popular_name`,
  `classification_tables_url`, `affected_irc_sections[]`.
- `authorities[]` with affected IRC sections and any
  legislative-history artifacts cited (`JCT_BlueBook`,
  `LegHistory`, `Greenbook`, `CBOReport`).

Confidence band per `shared/confidence-bands.md`. Statutory text
retrieved fresh from USLM merits HIGH; reliance on the
quick-reference table without verification merits MODERATE.

## Hard rules

- Always verify Public Law numbers against the Popular Name Tool
  at retrieval time.
- Always fetch Classification Tables for full list of affected
  USC sections.
- Always pull current USLM text for each affected section before
  stating "current law".
- Tag Greenbook citations as `Greenbook` /
  `legislative_history` ONLY if the proposal became enacted law
  in substantively the same form. Otherwise tag
  `persuasive_non_authority`.
- Tag CBO scores as `CBOReport` / `legislative_history` only
  when the score accompanied the enacted bill. Otherwise tag
  `persuasive_non_authority`.
- Always include the verification checklist appendix.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`. Note that statutory text retrieved
from USLM is canonical; Treasury Decisions and proposed
regulations affecting the section may post-date the retrieval —
flag the Federal Register IRS feed as the staleness check.
