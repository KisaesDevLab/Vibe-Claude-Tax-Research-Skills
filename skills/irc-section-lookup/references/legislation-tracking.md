# Public-Law-to-USC workflow — implementation

This file implements the workflow specified in
`shared/legislation-tracking.md`. Follow this implementation
exactly when the user asks about a Public Law popular name or
Public Law number.

## Step-by-step

### Step 1: Resolve to Public Law number

If the user gave a popular name:

1. Fetch the Popular Name Tool at
   `https://uscode.house.gov/popularnames/popularnames.htm`.
2. Search for the popular name (case-insensitive).
3. Record the Public Law number and Statutes-at-Large citation
   (e.g., "Pub. L. 117-169, 136 Stat. 1818").

If the user gave a Public Law number, skip to step 2.

### Step 2: Retrieve Classification Table

1. Fetch the Classification Tables index at
   `https://uscode.house.gov/classification/tables.shtml`.
2. The Classification Tables are organized by Congress. Identify
   the Congress for the Public Law:
   - 115th Congress (2017-2018) → TCJA, etc.
   - 116th Congress (2019-2020) → CARES Act, CAA 2021, etc.
   - 117th Congress (2021-2022) → ARPA, IIJA, IRA, SECURE 2.0,
     CHIPS Act.
   - 118th Congress (2023-2024) → various.
   - 119th Congress (2025-2026) → OBBBA.
3. Navigate to the table for the relevant Congress.
4. Locate the entry for the Public Law.
5. The table lists every USC section the Public Law amended,
   added, or repealed.
6. Record the Classification Tables URL in the JSON sidecar.

### Step 3: Verify each affected section's current text

For each affected USC section:

1. Fetch the current text from
   `https://uscode.house.gov/browse/prelim@title26`.
2. Navigate to the specific section (e.g., 26 U.S.C. § 199A).
3. Confirm the text is post-amendment by checking:
   - The "Editorial Notes" / "Amendments" annotations near the
     end of the section.
   - The dates of amendments listed.
4. Cite as `IRC` with `weight: primary_statute`. Include
   `quoted_text` (≤75 words) of the operative subsection /
   paragraph. Include `pin_cite`.

### Step 4: Locate legislative-history artifacts

#### JCT Bluebook

1. Fetch JCT publications at `https://www.jct.gov/publications/`.
2. Search for the Bluebook covering the Public Law (typically
   titled "General Explanation of [the Public Law]").
3. Bluebooks publish 6-12 months after enactment. For very recent
   Public Laws (e.g., OBBBA 2025), the Bluebook may not yet be
   available; fall back to committee reports.
4. Cite as `JCT_BlueBook` with `weight: legislative_history`.
   Include `quoted_text` (≤75 words).

#### Committee reports

1. Fetch from:
   - House Ways & Means: `https://waysandmeans.house.gov/`
   - Senate Finance: `https://www.finance.senate.gov/`
   - congress.gov for the bill's report numbers (search by bill
     number, then look at report references).
2. The Conference Report (when applicable) is often the most
   useful interpretive source.
3. Cite as `LegHistory` with `weight: legislative_history`.
   Include the report number (e.g., "H.R. Rep. No. 115-409
   (2017)").

#### Treasury Greenbook

1. Fetch from
   `https://home.treasury.gov/policy-issues/tax-policy/revenue-proposals`.
2. The Greenbook is the Administration's General Explanations of
   the Administration's Fiscal Year Revenue Proposals.
3. **Caveat**: The Greenbook describes what the Administration
   PROPOSED. Tag as `Greenbook` / `legislative_history` ONLY if
   the proposal became enacted law in substantively the same
   form. Otherwise tag `Greenbook` /
   `persuasive_non_authority` for descriptive use only.

#### CBO scoring report

1. Fetch from `https://www.cbo.gov/topics/taxes` or
   `https://www.cbo.gov/cost-estimates`.
2. The CBO score describes projected revenue effects.
3. **Caveat**: CBO scores are not interpretive authority on the
   meaning of the enacted statute. Tag as `CBOReport` /
   `legislative_history` only when the score accompanied the
   enacted bill (i.e., the CBO score for the bill that became the
   Public Law). Tag `CBOReport` / `persuasive_non_authority`
   for pre-enactment descriptive use.

### Step 5: Check for proposed regulations and Treasury Decisions

1. Fetch the Federal Register IRS feed at
   `https://www.federalregister.gov/agencies/internal-revenue-service`.
2. Search for the relevant USC section or Public Law-related
   keyword.
3. Identify:
   - Proposed regulations (REG-XXXXXX).
   - Final regulations / Treasury Decisions (TD XXXX).
   - Notices of public hearing.
4. Tag the issuance as `TreasuryDecision` / `regulation` for the
   issuance vehicle in the Federal Register; tag the codified rule
   as `TreasReg` / `regulation` once it appears in the eCFR.
5. The Federal Register IRS feed is the freshness-check companion
   to DAWSON Today's Opinions / Today's Orders.

### Step 6: Cite Checker (optional)

For any USC citation that may have been renumbered or
reclassified, use the Cite Checker at
`https://uscode.house.gov/cite.xhtml`:

1. Enter the citation.
2. Confirm the citation resolves to current section text.
3. Note any renumbering that has occurred.

## Output template

For Public-Law lookups, the JSON sidecar should look like:

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
        "26 U.S.C. § 45",
        "26 U.S.C. § 48",
        "26 U.S.C. § 30D"
      ]
    }
  ],
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "26 U.S.C. § 55(b)(2)",
      "url": "https://uscode.house.gov/browse/prelim@title26",
      "retrieved_date": "2026-04-27",
      "quoted_text": "[verbatim ≤75 words]",
      "pin_cite": "subsection (b)(2)",
      "weight": "primary_statute"
    },
    {
      "authority_type": "JCT_BlueBook",
      "citation": "JCT, General Explanation of Tax Legislation Enacted in the 117th Congress (Pub. L. 117-169, the Inflation Reduction Act of 2022)",
      "url": "https://www.jct.gov/publications/",
      "retrieved_date": "2026-04-27",
      "quoted_text": "[verbatim ≤75 words]",
      "weight": "legislative_history"
    }
  ]
}
```

## Common practitioner errors to avoid

- Quoting a popular name without verifying the Public Law number.
- Skipping the Classification Tables and missing affected USC
  sections.
- Citing the Greenbook for an UN-enacted proposal as if it were
  enacted-law legislative history.
- Citing CBO scoring of pending bills as legislative history.
- Failing to check the Federal Register IRS feed for post-
  enactment Treasury Decisions.
- Quoting USLM text without checking for amendments.
- Missing the IRS Cite Checker step for renumbered sections.

## Workflow checklist

For a Public-Law lookup:

- [ ] Public Law number verified via Popular Name Tool.
- [ ] Classification Tables fetched for relevant Congress.
- [ ] Each affected USC section's current text retrieved from
  USLM.
- [ ] JCT Bluebook checked (or noted as not yet published).
- [ ] Committee reports identified.
- [ ] Greenbook tag verified (legislative_history vs.
  persuasive_non_authority).
- [ ] CBO score tag verified (legislative_history vs.
  persuasive_non_authority).
- [ ] Federal Register IRS feed checked for post-enactment TDs /
  proposed regs.
- [ ] `public_laws_consulted[]` populated in JSON sidecar.
- [ ] All cited authorities have `quoted_text` (≤75 words),
  `retrieved_date`, `weight`.
