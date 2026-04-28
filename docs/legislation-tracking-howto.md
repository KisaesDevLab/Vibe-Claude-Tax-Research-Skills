# Legislation tracking — practitioner how-to

The Vibe CPA Skills pack tracks Public-Law impact via the
canonical workflow in `shared/legislation-tracking.md`. This
document is the practitioner-facing guide.

## When to invoke

Trigger phrases (see `shared/legislation-tracking.md` for canonical
list):

- Public Law popular names: TCJA, IRA, OBBBA, SECURE 2.0, CARES,
  ARPA, etc.
- Public Law numbers: Pub. L. 117-169, Pub. L. 119-XX, etc.
- "What changed in §X under [recent legislation]?"
- "What's current law on [topic]?"
- Multi-year planning involving sunset / phase-out / phase-in
  provisions.

## The 6-step workflow

### Step 1: Resolve to Public Law number

If the user gave a popular name, fetch the Popular Name Tool:
https://uscode.house.gov/popularnames/popularnames.htm

If the user gave a Public Law number, skip to step 2.

### Step 2: Retrieve Classification Table

Fetch the Classification Tables index:
https://uscode.house.gov/classification/tables.shtml

Navigate to the table for the Public Law's congressional session.
Identify every USC section the Public Law amended, added, or
repealed. Record the Classification Table URL in the JSON sidecar.

### Step 3: Verify each affected section's current text

For each affected USC section, fetch from:
https://uscode.house.gov/browse/prelim@title26

Confirm the text is post-amendment by checking the Editorial Notes
/ Amendments annotations.

Cite as `IRC` with `weight: primary_statute`. Include
`quoted_text` (≤75 words) of the operative subsection / paragraph.

### Step 4: Locate legislative-history artifacts

In order of authoritativeness:

1. **JCT Bluebook** at https://www.jct.gov/publications/.
   - Tag as `JCT_BlueBook` / `legislative_history`.
   - Note: typically published 6-12 months after enactment.
2. **Committee reports** (House Ways & Means, Senate Finance,
   Conference) at:
   - https://waysandmeans.house.gov/
   - https://www.finance.senate.gov/
   - congress.gov for bill-level report references.
   - Tag as `LegHistory` / `legislative_history`.
3. **Treasury Greenbook** at
   https://home.treasury.gov/policy-issues/tax-policy/revenue-proposals.
   - Tag as `Greenbook` / `legislative_history` ONLY if proposal
     enacted in same form. Otherwise `Greenbook` /
     `persuasive_non_authority`.
4. **CBO scoring report** at https://www.cbo.gov/topics/taxes.
   - Tag as `CBOReport` / `legislative_history` only when score
     accompanied the enacted bill. Otherwise `CBOReport` /
     `persuasive_non_authority`.

### Step 5: Check Federal Register IRS feed

Fetch from
https://www.federalregister.gov/agencies/internal-revenue-service.

Search for the relevant USC section or Public Law-related keyword.
Identify:
- Proposed regulations (REG-XXXXXX).
- Final regulations / Treasury Decisions (TD XXXX).
- Notices of public hearing.

Tag the issuance as `TreasuryDecision` / `regulation`.

### Step 6: Cite Checker (optional)

For any USC citation that may have been renumbered or
reclassified, use the Cite Checker at
https://uscode.house.gov/cite.xhtml.

## JSON sidecar output

For Public-Law-touching questions, populate
`public_laws_consulted[]`:

```json
{
  "public_laws_consulted": [
    {
      "public_law": "Pub. L. 117-169",
      "popular_name": "Inflation Reduction Act of 2022",
      "classification_tables_url": "https://uscode.house.gov/classification/tables.shtml [specific table URL]",
      "affected_irc_sections": [
        "26 U.S.C. § 55",
        "26 U.S.C. § 4501",
        "26 U.S.C. § 30D"
      ]
    }
  ]
}
```

## Common Public Laws — quick reference

Verify against the Popular Name Tool at retrieval time.

| Popular name | Public Law | Year | Notable IRC topics |
|---|---|---|---|
| TCJA | Pub. L. 115-97 | 2017 | §199A QBI; §163(j); §168(k); §174 (capitalization); §1400Z |
| CARES Act | Pub. L. 116-136 | 2020 | NOL; §163(j) relaxation |
| CAA 2021 | Pub. L. 116-260 | 2020 | PPP; ERC |
| ARPA | Pub. L. 117-2 | 2021 | §6428B Recovery Rebate; CTC expansion (1 year) |
| IIJA | Pub. L. 117-58 | 2021 | ERC retired post-Q3 2021 |
| CHIPS Act | Pub. L. 117-167 | 2022 | §48D advanced-manufacturing credit |
| IRA | Pub. L. 117-169 | 2022 | §55 corporate AMT; §4501 buyback excise; §30D EV |
| SECURE 2.0 | Pub. L. 117-328 div. T | 2022 | §401(a)(9) RMD age; §414(v) catch-up |
| OBBBA | Pub. L. 119-XX | 2025 | TCJA permanence framework |

## Practitioner discipline

When a multi-year projection touches a sunset / phase-out /
phase-in provision, the practitioner must:

1. Identify the Public Law(s) governing the provision.
2. Document Public Laws in `public_laws_consulted[]`.
3. Apply phase-down / sunset / phase-in adjustments year by year.
4. Note legislative uncertainty in any projection beyond 24 months.
5. Re-walk the workflow when new legislation enacts.

## Caveats

- **Greenbook**: describes proposed legislation. Tag as
  `legislative_history` ONLY if the proposal became enacted law in
  the same form. Otherwise tag `persuasive_non_authority`.
- **CBO score**: describes projected revenue effects. Not
  interpretive authority on statutory meaning.
- **Reconciliation bills**: typically constrained by Byrd Rule
  (§313 of the Congressional Budget Act); often sunset at end of
  budget window. Model sunsets explicitly.

## When the JCT Bluebook is unavailable

Bluebooks publish 6-12 months after enactment. For very recent
Public Laws (e.g., OBBBA 2025):
- Use committee reports + conference report as fallback.
- Cite the underlying statute as primary authority.
- Note the absence of Bluebook commentary in the analysis.

## Workflow checklist

For a Public-Law lookup or Public-Law-affected analysis:

- [ ] Public Law number verified via Popular Name Tool.
- [ ] Classification Tables fetched for relevant Congress.
- [ ] Each affected USC section's current text retrieved from USLM.
- [ ] JCT Bluebook checked (or noted as unavailable).
- [ ] Committee reports identified.
- [ ] Greenbook tag verified (legislative_history vs.
  persuasive_non_authority).
- [ ] CBO score tag verified.
- [ ] Federal Register IRS feed checked for post-enactment TDs /
  proposed regs.
- [ ] `public_laws_consulted[]` populated in JSON sidecar.
- [ ] All cited authorities have `quoted_text` (≤75 words),
  `retrieved_date`, `weight`.
- [ ] Sunset / phase-out / phase-in schedule documented in
  multi-year projections.

## See also

- `shared/legislation-tracking.md` — canonical workflow.
- `skills/irc-section-lookup/SKILL.md` — primary user-facing skill.
- `skills/planning-multi-year/SKILL.md` — multi-year projection.
- `skills/tax-research-federal/references/legislative-history.md` —
  federal-research-specific application.
