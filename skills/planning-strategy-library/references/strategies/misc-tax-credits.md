---
name: "Miscellaneous Tax Credits (Umbrella Reference)"
slug: misc-tax-credits
type: Credit/Payment
tax_type: EFR
complexity: Medium
irc_sections: ["§38", "§44", "§45A", "§45F", "§45R", "§45S", "§51", "§129"]
forms: ["Form 3800 (General Business Credit)", "credit-specific forms"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

This file is the umbrella reference for federal tax credits beyond
the major credits given separate strategy files (R&D #39, EV #36,
§1202 QSBS #43, Education Credits #61, Adoption #58). The General
Business Credit under §38 aggregates many.

Credits commonly missed by practitioners and small businesses:

1. **§51 Work Opportunity Tax Credit (WOTC).** Up to $2,400 per
   eligible new hire (more for veterans, long-term unemployed,
   etc.). 9 target groups including SNAP recipients, ex-felons,
   designated community residents, qualified veterans. Requires
   IRS Form 8850 within 28 days of hire.

2. **§45F Employer-Provided Child Care Credit.** 25% of qualified
   child care facility expenditures + 10% of qualified resource
   and referral expenditures, up to $150,000 annual cap.

3. **§45R Small Business Health Care Tax Credit.** Up to 50% of
   premiums for small employers using SHOP. See #8.

4. **§45S Paid Family and Medical Leave Credit.** 12.5% to 25% of
   wages paid to qualifying employees on FMLA leave.

5. **§44 Disabled Access Credit.** 50% of eligible access
   expenditures between $250 and $10,250, max $5,000.

6. **§47 Rehabilitation Credit (Historic).** 20% of qualified
   rehabilitation expenditures on certified historic structures.

7. **§129 Dependent Care Assistance Programs.** Up to $5,000 of
   pre-tax employer-provided child care benefits.

8. **§45A Indian Employment Credit.** Targeted credit for hiring
   enrolled members of Indian tribes.

9. **State and local credits.** R&D, jobs, investment, film,
   enterprise zone — vary substantially by state.

## Primary IRC authority

- §38 — General business credit.
- §39 — Carryback and carryforward of unused credits.
- §44 — Disabled access credit.
- §45A — Indian employment credit.
- §45F — Employer-provided child care credit.
- §45R — Small employer health insurance credit.
- §45S — Paid family and medical leave credit.
- §47 — Rehabilitation credit.
- §51 — WOTC.
- §52 — Special rules for §51.
- §129 — Dependent care assistance.

## Treasury regulations

- Reg §1.38-1 through §1.39-2 — General business credit.
- Reg §1.51-1 — WOTC.
- Reg §1.45F-1 (proposed) — Child care.
- Reg §1.129-1 — Dependent care.

## Key IRS guidance

- IRS Publication 334 — Tax Guide for Small Business.
- Form 5884 instructions — WOTC.
- Form 8881 — Pension Plan Startup Costs Credit.
- Form 8882 — Employer-Provided Child Care Facilities Credit.
- Form 8826 — Disabled Access Credit.

## Eligibility requirements

Vary by credit. See specific credit forms.

## Mechanics — how it works

1. **Annual credit inventory.** Review available credits each year.
2. **Pre-screen for WOTC** at hiring (Form 8850 within 28 days).
3. **Compute each credit** on respective form.
4. **Aggregate on Form 3800** (General Business Credit).
5. **Apply tax liability limits** (§38(c)).
6. **Carryback / carryforward** unused credits per §39 (1-year
   carryback, 20-year carryforward, generally).

## Documentation requirements

Vary. Generally requires Form 8850 (WOTC), plan documents (child
care, dependent care), employee certifications, payment records.

## Common pitfalls / audit risks

- **WOTC pre-screening missed.** 28-day window from hire date.
- **General business credit limit.** §38(c) limits credit to tax
  liability less tentative minimum tax.
- **§45R complex computation** — small business health credit
  intricate phase-outs.

## Recent legislative changes

- **TCJA (2017)** — Created §45S paid leave credit.
- **CARES / CAA 2021 / IRA 2022** — Various extensions and
  modifications.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA tax credits
  Pub L 119-21]`. Numerous credit modifications likely.

## State conformity considerations

State credits are independent.

## Default confidence band rationale

**HIGH** for properly-documented credits.

## Cross-references

- `r-and-d-credit-strategy` (#39).
- `ev-credits` (#36).
- `adoption-incentives` (#58).
- `group-health-insurance` (#8) — §45R.
- `hiring-kids` (#49).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 38","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section38","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 51","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section51","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 45F","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section45F","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 45S","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section45S","weight":"primary_statute"}
  ]
}
```
