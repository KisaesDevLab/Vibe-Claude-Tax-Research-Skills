# Legislation-tracking pointer

This skill ALWAYS uses `shared/legislation-tracking.md` as the
canonical workflow for resolving Public-Law popular names to USC
sections and identifying authoritative legislative-history
artifacts.

## When to load shared/legislation-tracking.md

- User mentions a Public Law popular name (TCJA, IRA, OBBBA,
  SECURE 2.0, CARES Act, ARPA, etc.).
- User mentions a Public Law number (Pub. L. 115-97, Pub. L.
  117-169, Pub. L. 119-XX, etc.).
- User asks "what's current law on §X" where recent legislation
  may have amended the underlying statute.
- Multi-year projection requires sunset / phase-out / phase-in
  analysis.

## Reconciliation-bill scoring context

Multi-year planning frequently encounters reconciliation bills
that:
- Originate under §310(d) Congressional Budget Act reconciliation
  procedures (Senate 51-vote majority).
- Are constrained by the Byrd Rule (§313 of the Congressional
  Budget Act) which limits non-budgetary provisions and prohibits
  net-revenue effects beyond the budget window.

Practical implication: provisions enacted via reconciliation
often:
- Sunset at the end of the budget window (typically 10 years).
- Have phase-down schedules (e.g., §168(k) bonus depreciation).
- Are paired with pay-fors that may also sunset.

When projecting beyond a budget window, the practitioner must:
1. Identify the budget window of the enacting Public Law.
2. Apply the sunset / phase-down schedule explicitly in the
   projection.
3. Note legislative uncertainty around extension.
4. Avoid recommending irreversible strategies that depend on
   speculative extensions.

## CBO scoring posture

CBO score of a pending bill describes projected revenue effects
ASSUMING ENACTMENT. It is NOT interpretive authority on the
meaning of an enacted statute.

When a CBO score accompanies an enacted bill, it becomes part of
the legislative-history record and is tagged `CBOReport` /
`legislative_history`. When a CBO score accompanies a pending
bill, tag `CBOReport` / `persuasive_non_authority` for descriptive
use only.

## Greenbook posture

Treasury Greenbooks (General Explanations of the
Administration's Fiscal Year Revenue Proposals) describe what
the Administration PROPOSED. They are tagged:
- `Greenbook` / `legislative_history` ONLY if the proposal became
  enacted law in substantively the same form.
- `Greenbook` / `persuasive_non_authority` for purely descriptive
  use of pre-enactment proposals.

## JCT Bluebook posture

The Joint Committee on Taxation publishes the General Explanation
("Bluebook") for each major tax act. The Bluebook is the
gold-standard legislative-history source for an enacted Public
Law:
- Authority type: `JCT_BlueBook`.
- Weight: `legislative_history`.
- Effective: typically published 6-12 months after enactment.

Cite the Bluebook for any legislative-history-supported
interpretation of an enacted Public Law.

## Common Public Laws relevant to multi-year planning

Verify Public Law numbers via the USC Popular Name Tool:
https://uscode.house.gov/popularnames/popularnames.htm

| Popular name | Public Law | Year | Notable horizon |
|---|---|---|---|
| TCJA | Pub. L. 115-97 | 2017 | Most individual provisions sunset 12/31/2025 absent extension |
| CARES Act | Pub. L. 116-136 | 2020 | NOL, §163(j) temporary relief mostly expired |
| Consolidated Appropriations Act 2021 | Pub. L. 116-260 | 2020 | PPP / ERC framework |
| ARPA | Pub. L. 117-2 | 2021 | One-year-only credits mostly expired |
| Infrastructure Investment and Jobs Act | Pub. L. 117-58 | 2021 | Modest tax provisions; ERC retired post-Q3 2021 |
| Inflation Reduction Act | Pub. L. 117-169 | 2022 | §55 CAMT, §4501 buyback, energy credits, §174 untouched |
| SECURE 2.0 | Pub. L. 117-328 div. T | 2022 | RMD age 73 (2023) → 75 (2033); catch-up changes |
| CHIPS Act | Pub. L. 117-167 | 2022 | §48D advanced-manufacturing credit |
| OBBBA | Pub. L. 119-XX | 2025 | TCJA permanence framework — verify final form |

## Workflow integration

When this skill projects multi-year tax liability:

1. Identify all material Public Laws with effective-date
   sensitivity within the horizon.
2. Use `shared/legislation-tracking.md` workflow to:
   - Confirm Public Law number via Popular Name Tool.
   - Pull Classification Table for affected USC sections.
   - Verify current text of each affected USC section.
   - Identify legislative-history artifacts (Bluebook, committee
     reports, Greenbook, CBO score) where relevant.
3. Apply phase-down / sunset / phase-in adjustments year-by-year.
4. Document Public Laws in `public_laws_consulted[]` of the JSON
   sidecar with at least:
   - `public_law` number.
   - `popular_name`.
   - `classification_tables_url`.
   - `affected_irc_sections[]`.

5. Note any legislative uncertainty in the analysis section.

## Don't

- Don't model speculative legislation as if enacted.
- Don't rely on a Greenbook proposal as authority unless the
  proposal became enacted law.
- Don't quote a CBO score as interpretive authority on statutory
  meaning.
- Don't assume reconciliation-bill sunsets won't happen — model
  them explicitly.
