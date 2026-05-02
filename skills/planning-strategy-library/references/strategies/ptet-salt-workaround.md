---
name: "Pass-Through Entity Tax (PTET) — SALT Cap Workaround"
slug: ptet-salt-workaround
type: Business - Other
tax_type: EFR
complexity: High
irc_sections: ["§164(b)(6)", "§164"]
forms: ["State PTE election forms (varies by state)", "K-1s adjusted for PTET credit"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

The Pass-Through Entity Tax (PTET) is the most consequential state
tax planning strategy of the 2020s. It is a state-level workaround
to TCJA's $10,000 cap on state and local tax (SALT) deductions
under §164(b)(6). The mechanism: a partnership or S corporation
elects to pay state income tax at the entity level (entity-level
state tax is fully deductible federally as a §162 business
expense), with the entity's owners receiving a state tax credit
for their share of the PTET paid. The result: the entity's owners
effectively get full federal deduction for state income tax that
otherwise would have been capped at $10,000.

The IRS validated the structure in **Notice 2020-75** (issued
November 9, 2020): "specified income tax payments" made by a
partnership or S corporation to a state are deductible by the
entity in computing its non-separately stated taxable income.
This Notice essentially blessed the workaround that approximately
36 states (and counting) have now enacted.

State variation is enormous:
- **Mandatory vs. elective:** Most are elective; CA's was elective
  through 2025; NY's is annual elective; Minnesota's was originally
  mandatory then elective.
- **Election timing:** Some require election by entity due date;
  others by extended due date; some allow late election.
- **Calculation methodology:** Some apply state's top individual
  rate; others apply graduated rates; others use unique formulas.
- **Credit mechanism:** Some give 100% credit at owner level;
  some give partial.
- **Resident vs. nonresident:** Some apply only to resident owners;
  some both.
- **Coordination with composite/withholding:** State-by-state.

For practitioners, the PTET decision is one of the most consequential
year-end planning decisions for pass-through entities. The state
stub files in `tax-research-state-income/references/states/<XX>.md`
should track each state's PTET regime in detail.

## Primary IRC authority

- **§164(b)(6)** — $10,000 SALT cap (TCJA-created; OBBBA may have
  modified — verify).
- **§164** — Taxes generally deductible.
- **§162** — Business expense deduction.

## State authority

PTET is fundamentally state law. Each state's PTET statute and
regulations govern. Reference state-specific stubs for citations.

## Treasury regulations

No federal Treasury Regulation specifically addresses PTET (the
issue is a state-tax characterization).

## Key IRS guidance

- **Notice 2020-75** — Specified income tax payments by partnerships
  and S corporations are deductible at the entity level.
  https://www.irs.gov/irb/2020-49_IRB
- The Notice validated the structure but stopped short of issuing
  full regulations.

## Key court decisions

- No major federal case law specifically addressing PTET (because
  Notice 2020-75 effectively settled federal treatment).

## Eligibility requirements

Vary by state. Common requirements:
1. Entity is a partnership or S corporation.
2. Owners include at least some individuals (some states bar
   non-PTE owners or require all-individual ownership).
3. Election made within state-specific deadline.
4. Entity pays the PTET in the year claimed.

## Mechanics — how it works

1. **Identify state PTET regimes** for each state where the
   pass-through entity operates or has resident owners.
2. **Run cost-benefit analysis.**
   - Federal benefit: PTET amount × owner's marginal federal rate
     × percentage of owner's SALT cap that PTET avoids.
   - State cost: any difference between PTET rate and what the
     owner would have paid as resident.
   - Coordination cost: AMT, NIIT, basis tracking.
3. **Make the election by deadline** (varies by state).
4. **Pay the PTET.** Entity makes payment to state.
5. **Adjust K-1s.** Reduce ordinary income by PTET; increase basis
   adjustment.
6. **Owner claims credit at state level.** Effectively eliminates
   owner's individual state tax on the related income.
7. **Federal Schedule K reporting.** PTET deduction reduces income
   passed through to owners. Owner's federal AGI is reduced
   accordingly.

## Documentation requirements

- State PTET election forms.
- Entity-level PTET payment records.
- Adjusted K-1s reflecting PTET deduction.
- State return reflecting PTET payment.
- Owner state return claiming PTET credit.

## Common pitfalls / audit risks

- **Election deadline missed.** State-specific deadlines are strict.
- **Wrong year payment.** Cash basis entities must actually pay in
  the deduction year.
- **Federal/state coordination.** Owner basis adjustments,
  estimated payment recalculation, AMT, NIIT all interact.
- **Resident vs. nonresident issues.** Some states' PTET applies
  only to resident owners' shares; need careful entity allocation.
- **Multiple-state owner.** PTET benefit calculation across states
  is complex.
- **Composite return interaction.** PTET typically replaces
  composite/nonresident withholding regimes.

## Recent legislative changes

- **TCJA (2017)** — Created $10,000 SALT cap effective 2018.
- **Notice 2020-75 (November 2020)** — Federal validation of PTET
  structure.
- **Wave of state PTET enactments 2018-2024** — Now ~36 states
  plus DC.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA SALT cap
  §164(b)(6) Pub L 119-21]`. Reports indicate OBBBA modified the
  SALT cap. Possible scenarios: (a) increased to $40,000; (b)
  eliminated; (c) made permanent. PTET utility depends on the
  specific OBBBA SALT cap treatment. Verify via Classification
  Tables.

## State conformity considerations

PTET is fundamentally state-by-state. Track in per-state stub
files. Major variations:
- **CA SB 113 / AB 150** — California PTET; up to 9.3% rate;
  elective.
- **NY S2509 / Tax Law §860** — New York PTET; graduated rates.
- **NJ BAIT** — New Jersey Business Alternative Income Tax.
- **MA Chapter 269 of 2021 Acts** — Massachusetts 4% PTE excise.

## AICPA SSTS / Circular 230 considerations

PTET decisions are major year-end planning events. Practitioner
should run formal cost-benefit analysis and document.

## Default confidence band rationale

**HIGH** — Notice 2020-75 explicitly validated the structure;
state legislation provides clear statutory basis. Drops to
MODERATE only for unusual structures or election timing edge cases.

## Cross-references

- **`state-tax-savings`** (#40) — broader state planning.
- **`c-corp-state-tax-savings`** (#35) — C corp variant.
- All state stub files at
  `skills/tax-research-state-income/references/states/<XX>.md`.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 164(b)(6)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section164",
      "weight": "primary_statute"
    },
    {
      "authority_type": "Notice",
      "citation": "Notice 2020-75",
      "url": "https://www.irs.gov/irb/2020-49_IRB",
      "weight": "irs_published"
    }
  ]
}
```
