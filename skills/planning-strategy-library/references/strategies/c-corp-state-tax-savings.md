---
name: "C Corporation State Tax Savings"
slug: c-corp-state-tax-savings
type: Credit/Payment
tax_type: CREDIT
complexity: Medium
irc_sections: ["§164", "§7701", "§482"]
forms: ["State corporate income tax returns"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: MODERATE
last_obbba_review: "N/A"
---

## Overview

C corporation state tax planning involves multiple strategic levers
to minimize state-level tax burden:

1. **Nexus management.** Avoiding state nexus where possible;
   establishing favorable nexus where economically substantive.
2. **Apportionment optimization.** State apportionment formulas
   (typically based on payroll, property, sales — though many
   states have moved to single-sales-factor) can be optimized
   through structural decisions.
3. **State of incorporation / commercial domicile.** Some states
   (Nevada, Delaware, Wyoming) have no corporate income tax;
   incorporation there alone does not avoid taxation in operating
   states (nexus follows operations) but can affect commercial
   domicile and certain tax characterizations.
4. **Holding company structures.** Delaware, Nevada, and other
   no-tax states sometimes used for IP holding companies that
   license to operating subsidiaries (subject to §482 transfer
   pricing and state addback rules).
5. **State tax credits.** R&D credits, jobs credits, investment
   credits, film credits — vary substantially by state.
6. **Combined / unitary reporting.** Multistate operations may face
   combined reporting requirements that limit shifting; understand
   whether each state requires combined or separate filing.
7. **Public Law 86-272 protection.** Federal law that limits state
   income tax on out-of-state sellers whose only in-state activity
   is solicitation of sales of tangible personal property. Has been
   significantly narrowed by states (e.g., MTC's 2021 statement;
   California, NY, NJ adoptions) for digital and SaaS activities.

## Primary IRC authority

- **§164** — State and local taxes deductible (no $10K cap for C
  corps; the cap applies only to individuals).
- **§482** — Transfer pricing.
- **§7701** — Definitions.

## State authority

State-by-state. Reference state stub files.

## Treasury regulations

- **Reg §1.482-1 through §1.482-9** — Transfer pricing.

## Key federal authority

- **Public Law 86-272 (15 U.S.C. §§ 381-384)** — Solicitation-only
  protection.
- **Quill Corp. v. North Dakota, 504 U.S. 298 (1992)** —
  Substantial nexus pre-Wayfair.
- **South Dakota v. Wayfair, Inc., 138 S. Ct. 2080 (2018)** —
  Eliminated physical presence requirement; established economic
  nexus framework.

## Key state guidance and developments

- **MTC Statement on Public Law 86-272 (revised August 2021)** —
  States MTC's position that internet activities (cookies, mobile
  apps, customer support chat) exceed mere solicitation. Widely
  adopted by states.
- **California FTB TAM 2022-01** — Adopted MTC position.
- **New York Tax Bulletin TB-CT-816** — Adopted MTC position.

## Eligibility requirements

Vary by strategy. Common considerations:
1. State nexus determination (each state's rules).
2. Apportionment factor application.
3. P.L. 86-272 protection (if applicable).
4. Combined / separate filing methodology (state-specific).

## Mechanics — how it works

1. **Multistate footprint analysis.** Determine nexus in each state.
2. **Apportionment review.** Optimize factor mix (single-sales vs.
   three-factor; throwback rules; cost-of-performance vs.
   market-based sourcing for services).
3. **Holding company evaluation.** §482-compliant licensing of IP
   from holding company to operating subsidiaries.
4. **State credit utilization.** Survey credits in operating states.
5. **Wayfair compliance.** Track economic nexus thresholds in each
   state where economic activity occurs.
6. **P.L. 86-272 review.** Especially for online businesses
   post-MTC 2021 statement.
7. **Annual review.** State law changes affect prior-year planning.

## Documentation requirements

- Multistate apportionment workpapers.
- §482 transfer pricing documentation (if intercompany).
- State tax credit applications.
- P.L. 86-272 activity tracking.

## Common pitfalls / audit risks

- **Holding company addback rules.** Many states (NJ, IL, MA, PA,
  WI) require addback of intercompany interest, royalties, etc.
- **Combined/unitary reporting.** Cannot shift income across
  related entities in combined-reporting states.
- **P.L. 86-272 erosion.** State adoption of MTC 2021 position
  may eliminate prior planning.
- **Single-sales-factor states.** Significantly different from
  three-factor states; sourcing rules become critical.
- **Economic nexus.** Wayfair-driven tracking required in 50 states.

## Recent legislative changes

- **Wayfair (2018)** — Economic nexus framework.
- **MTC 2021 statement** — P.L. 86-272 erosion.
- **Many state-level changes** — single-sales-factor adoptions,
  PTET enactments, throwback repeals.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA state tax
  Pub L 119-21]`. Federal-level OBBBA impact on state taxation
  generally limited.

## State conformity considerations

This entire strategy is fundamentally state-by-state.

## AICPA SSTS / Circular 230 considerations

Multistate planning requires careful documentation and regular
review for state law changes.

## Default confidence band rationale

**MODERATE** — fact and state-specific. HIGH for established
positions in conforming states; LOW for aggressive positions
challenging post-Wayfair / post-MTC 2021 frameworks.

## Cross-references

- **`ptet-salt-workaround`** (#17) — pass-through variant.
- **`state-tax-savings`** (#40) — individual variant.
- **`income-shifting-to-c-corp`** (#47).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 482",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section482",
      "weight": "primary_statute"
    },
    {
      "authority_type": "SCOTUS",
      "citation": "South Dakota v. Wayfair, Inc., 138 S. Ct. 2080 (2018)",
      "url": "https://www.supremecourt.gov",
      "weight": "binding_judicial"
    }
  ]
}
```
