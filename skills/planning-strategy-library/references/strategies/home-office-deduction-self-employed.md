---
name: "Home Office Deduction — Self-Employed (§280A)"
slug: home-office-deduction-self-employed
type: SE Tax
tax_type: EFR
complexity: Medium
irc_sections: ["§280A", "§280A(c)(1)", "§280A(c)(5)"]
forms: ["Form 8829 (actual expense method)"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

§280A allows a self-employed individual to deduct expenses for the
business use of a home, subject to strict eligibility requirements
and limitations. Two methods:

**Simplified Method:**
- $5/square foot × business-use square footage.
- **Maximum 300 square feet** = $1,500 maximum deduction.
- No depreciation; no recapture on sale.
- Annual election (can switch year-to-year).
- Itemized deduction items (mortgage interest, property tax) still
  fully deductible on Schedule A.

**Actual Expense Method (Form 8829):**
- Compute total home expenses: mortgage interest, property tax,
  insurance, utilities, repairs, depreciation.
- Multiply by business-use percentage (typically square footage
  ratio).
- Direct expenses (improvements to home office only): 100%
  deductible.
- Indirect expenses (whole-home utilities, etc.): business %.
- Depreciation portion creates §1250 recapture exposure on sale.
- Itemized deduction items reduced by home-office portion.

§280A(c)(1) eligibility tests (must satisfy ALL):
1. **Regular use** — home office used regularly (not occasionally).
2. **Exclusive use** — area used SOLELY for business; any
   personal use defeats deduction.
3. **One of these:**
   - **Principal place of business** (under §280A(c)(1)(A)) —
     either where most income-producing activity occurs OR where
     administrative/management activities occur AND no other fixed
     location used substantially for those activities.
   - **Meeting customers/clients** (under §280A(c)(1)(B)) —
     regular meeting place.
   - **Separate structure** (under §280A(c)(1)(C)) — separate
     building (detached garage, shed, ADU) used for business.

§280A(c)(5) gross income limit:
- Home office deduction cannot create or increase Schedule C loss.
- Excess carries forward to future years.

§121 interaction:
- Home office depreciation taken since May 6, 1997 must be
  recaptured at sale (max 25% rate) regardless of §121 exclusion.
- Simplified method does NOT create depreciation recapture.

## Primary IRC authority

- §280A — Disallowance of certain expenses in connection with
  business use of home, rental of vacation homes, etc.
- §280A(c)(1) — Exception for business use.
- §280A(c)(5) — Gross income limitation.
- §280A(g) — Augusta Rule (separate strategy #24).
- §121(d)(6) — §121 exclusion does not apply to depreciation
  recapture portion.

## Treasury regulations

- Reg §1.280A-1 through §1.280A-3.

## Key IRS guidance

- Rev. Proc. 2013-13 — Simplified method.
- IRS Publication 587 — Business Use of Your Home.
- Form 8829 instructions.

## Key court decisions

- **Commissioner v. Soliman, 506 U.S. 168 (1993)** — Principal
  place of business analysis pre-1999 amendments.
- **Hamacher v. Commissioner, 94 T.C. 348 (1990)** — Strict
  exclusive-use requirement.

## Eligibility requirements

§280A(c)(1) requirements all must be met:
1. Regular use.
2. Exclusive use.
3. One of: principal place of business, meet customers/clients, or
   separate structure.

## Mechanics — how it works

For Simplified Method:
1. **Measure business-use square footage** (max 300).
2. **Multiply by $5.**
3. **Schedule C direct deduction.**

For Actual Expense Method:
1. **Compute home expenses by category.**
2. **Apply business-use percentage** (square footage typically).
3. **Form 8829 computation.**
4. **§280A(c)(5) gross income limit.**
5. **Carryforward of excess.**
6. **Track depreciation** for §1250 recapture.

## Documentation requirements

- Home office floor plan / square footage.
- Photos showing exclusive-use nature.
- Home expense records (mortgage statements, utility bills, etc.).
- Form 8829 (actual method).
- Depreciation schedule (actual method).

## Common pitfalls / audit risks

- **Exclusive use violation.** Personal use of office area defeats
  entire deduction.
- **"Convenience of employer" test for employees.** Pre-TCJA test
  for employees no longer relevant (no employee home office
  deduction post-§67(g) suspension).
- **Home office in non-deductible business activity.** §280A
  presupposes §162 trade or business.
- **§280A(c)(5) gross income limit.** Cannot create loss; carries
  forward.
- **Depreciation recapture surprise** at sale.
- **Method election.** Annual; can switch.
- **Day-care exception.** §280A(c)(4) special rule for family
  day care.

## Recent legislative changes

- **TCJA (2017)** — Eliminated §67(g) employee home office
  deduction.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §280A
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity generally complete.

## Default confidence band rationale

**HIGH** for properly-documented home offices with clear exclusive
use. Drops to MODERATE for borderline exclusive-use arrangements.

## Cross-references

- `accountable-plan-home-office` (#2) — corporate variant.
- `accountable-plan-self-employed` (#84).
- `augusta-rule-280a-g` (#24) — separate §280A(g) strategy.
- `primary-home-sale-exclusion` (#67) — depreciation recapture
  interaction.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 280A","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section280A","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 280A(c)(5)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section280A","weight":"primary_statute"},
    {"authority_type":"RevProc","citation":"Rev. Proc. 2013-13","url":"https://www.irs.gov/irb","weight":"irs_published"},
    {"authority_type":"SCOTUS","citation":"Commissioner v. Soliman, 506 U.S. 168 (1993)","url":"https://www.supremecourt.gov","weight":"binding_judicial"}
  ]
}
```
