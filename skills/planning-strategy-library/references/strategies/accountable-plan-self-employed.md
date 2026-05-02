---
name: "Accountable Plan Equivalent for Self-Employed"
slug: accountable-plan-self-employed
type: SE Tax
tax_type: EFR
complexity: Low
irc_sections: ["§162", "§280A", "§274"]
forms: ["Schedule C / Schedule SE"]
state_specific: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

Sole proprietors do NOT have an "accountable plan" structure
because there is no separate entity to reimburse the proprietor.
Schedule C reflects the proprietor's business, so business
expenses are simply Schedule C deductions — no reimbursement
mechanism needed or available.

The Schedule C equivalent of an accountable plan is direct
deduction of all eligible business expenses on Schedule C,
including:
- Home office (using §280A simplified method or actual expenses).
- Business vehicle (#88).
- Business cell phone (#5).
- Office supplies, software, subscriptions.
- Travel, meals (50%).
- Professional development.
- Insurance (business).

The strategic point of this file: many sole proprietors
inadvertently miss home office, vehicle, and other expenses that
would be reimbursed through accountable plan if they were S-corp
owners. Schedule C deduction captures equivalent benefit; just
use different mechanism (direct deduction, not reimbursement).

Single-member LLC (default disregarded entity) follows Schedule C.
Single-member LLC electing C corp or S corp treatment uses
accountable plan structure (#2, #22, #23).

For partners (multi-member LLC, partnership): Unreimbursed
Partnership Expenses (UPE — #56) plays the accountable plan role
with specific partnership-agreement requirement.

## Primary IRC authority

- §162 — Trade or business expenses.
- §280A — Business use of home.
- §280A(c)(5) — Home office gross income limit.
- §274 — Substantiation requirements.

## Treasury regulations

- Reg §1.162-1 through §1.162-29.
- Reg §1.280A-2.
- Reg §1.274-5T.

## Key IRS guidance

- IRS Publication 535 — Business Expenses.
- IRS Publication 587 — Business Use of Your Home.
- IRS Publication 463 — Travel, Gift, and Car Expenses.

## Eligibility requirements

For Schedule C deduction:
1. Self-employed individual or single-member LLC (disregarded).
2. Expense is ordinary and necessary §162.
3. Substantiation per §6001 / §274.

For §280A home office:
1. Regular and exclusive use for business.
2. Principal place of business OR meet customers/clients OR
   separate structure.

## Mechanics — how it works

1. **Direct deduction on Schedule C.** No reimbursement structure;
   expenses paid directly by business or by proprietor (no
   distinction).
2. **Home office:** Form 8829 actual expenses or simplified $5/sf
   method (max 300 sf = $1,500).
3. **Vehicle:** Standard mileage or actual expenses (#88).
4. **Substantiate per category.**
5. **Reduce Schedule C net profit accordingly.**
6. **Reduces SE tax base** as well as income tax.

## Documentation requirements

- Receipts and substantiation.
- Mileage log (vehicle).
- Home office allocation worksheet.
- Form 8829 (if home office actual expense method).

## Common pitfalls / audit risks

- **Personal use creep.** Personal expenses on business return.
- **Inadequate substantiation.** §274(d) for vehicle, travel, M&E.
- **Home office regular and exclusive use.** Strict.
- **§280A(c)(5) limit.** Home office deduction can't create or
  increase Schedule C loss.
- **Self-employed health insurance §162(l).** Above-the-line on
  Schedule 1, not on Schedule C.

## Recent legislative changes

- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §162 §280A
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity generally complete.

## Default confidence band rationale

**HIGH** — straightforward Schedule C mechanics.

## Cross-references

- `accountable-plan-home-office` (#2) — corporate variant.
- `home-office-deduction-self-employed` (#88).
- `business-vehicle-self-employed` (#88).
- `cell-phone-expenses` (#5).
- `unreimbursed-partnership-expenses` (#56) — partnership variant.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 162","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section162","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 280A","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section280A","weight":"primary_statute"}
  ]
}
```
