---
name: "Flexible Spending Account (Health and Dependent Care)"
slug: flexible-spending-account
type: Personal - Other
tax_type: EFR
complexity: Low
irc_sections: ["§125", "§129", "§105"]
forms: ["W-2 (Box 10 dependent care; pre-tax §125 reduction)"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Flexible Spending Accounts (FSAs) are §125 cafeteria plan components
allowing employees to elect pre-tax salary reduction for specific
expense reimbursement:

**Health Care FSA (HCFSA):**
- Up to $3,200 (2024) salary reduction.
- Pre-tax: reduces Box 1, Box 3 (Social Security wages), Box 5
  (Medicare wages).
- Reimburses §213(d) qualified medical expenses.
- "Use it or lose it" with limited rollover (up to $640 in 2024)
  or 2.5-month grace period (employer choice; not both).

**Dependent Care FSA (DCFSA):**
- Up to $5,000 (single or MFJ; $2,500 if MFS).
- Pre-tax: reduces Box 1, Box 3, Box 5.
- Reimburses qualified dependent care expenses for children under
  13 or incapacitated dependents.
- Coordinates with §21 child and dependent care credit (each dollar
  through DCFSA reduces credit-eligible expenses).
- Box 10 of W-2 reports DCFSA contributions.

**Limited-Purpose FSA (LPFSA):**
- Reimburses dental and vision only.
- Compatible with HSA (#63) — allows individual to participate in
  HDHP+HSA AND have an LPFSA simultaneously.

The FSA election is locked at the start of the year (limited
change-in-status events permit mid-year changes per Reg §1.125-4).

## Primary IRC authority

- §125 — Cafeteria plans.
- §129 — Dependent care assistance.
- §105 — Health plan reimbursement.
- §213(d) — Medical care definition.
- §21 — Child and dependent care credit.

## Treasury regulations

- Reg §1.125-1 through §1.125-7.
- Reg §1.129-1.

## Key IRS guidance

- IRS Publication 502 — Medical and Dental Expenses.
- IRS Publication 503 — Child and Dependent Care Expenses.
- IRS Publication 969 — HSAs, MSAs, FSAs, HRAs.
- Notice 2013-71 — FSA carryover rules.
- Rev. Proc. 2024-XX (annual COLA) — FSA limits.

## Eligibility requirements

1. Employer offers §125 cafeteria plan with FSA component.
2. Annual election made before plan year.
3. For DCFSA: care necessary for taxpayer (and spouse if MFJ) to
   be employed or actively seeking employment.

## Mechanics — how it works

1. **Annual open enrollment.** Employee elects FSA contribution.
2. **Pre-tax salary reduction** throughout year.
3. **Reimbursement requests** with receipts for qualified expenses.
4. **Year-end deadline** — claims must be incurred by year end (or
   grace period); claims must be filed by run-out deadline (typically
   90 days after year end).
5. **DCFSA-§21 credit coordination** — same expenses cannot be both
   reimbursed by DCFSA and claimed for credit.

## Documentation requirements

- §125 plan document.
- Annual election form.
- Receipts for reimbursed expenses.
- Form W-2 with proper box reporting.

## Common pitfalls / audit risks

- **Use-it-or-lose-it forfeiture.** Unused balance generally
  forfeits at year end (subject to limited carryover or grace
  period).
- **Mid-year election change.** Limited to qualifying events.
- **HSA + HCFSA conflict.** Standard HCFSA disqualifies HSA
  contribution; LPFSA permits HSA participation.
- **DCFSA over-funding.** Cannot exceed lesser of $5,000, earned
  income, or spouse's earned income.
- **DCFSA-§21 credit double-counting.**
- **Owner-employee 2%+ S corp shareholder.** Cannot participate in
  §125 plans.

## Recent legislative changes

- **CAA 2021 / ARPA 2021** — Temporary FSA flexibility (extended
  rollovers, mid-year changes). Most temporary provisions expired.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §125 §129
  Pub L 119-21]`. Working assumption: standard limits preserved.

## State conformity considerations

State conformity to §125 generally complete.

## Default confidence band rationale

**HIGH** — clear statutory framework.

## Cross-references

- `hsa-optimization` (#63).
- `hra-merp` (#11).
- `group-health-insurance` (#8).
- `health-insurance-s-corp` (#10).
- `employer-benefit-package-review` (#71).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 125","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section125","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 129","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section129","weight":"primary_statute"},
    {"authority_type":"Notice","citation":"Notice 2013-71","url":"https://www.irs.gov/irb","weight":"irs_published"}
  ]
}
```
