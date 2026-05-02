---
name: "State Tax Savings (Individual Planning)"
slug: state-tax-savings
type: Credit/Payment
tax_type: CREDIT
complexity: Medium
irc_sections: ["§164"]
forms: ["State income tax returns"]
state_specific: true
confidence_default_band: MODERATE
last_obbba_review: "2025-07-04"
---

## Overview

State tax planning for individuals encompasses several strategies:

1. **Domicile / residency planning.** Establishing domicile in a
   no-income-tax state (FL, TX, NV, WA, WY, SD, AK, TN). Requires
   substantial change in life circumstances; states aggressively
   audit residency claims (NY notorious for "convenience-of-
   employer" rule and 183-day tests).

2. **Convenience-of-employer rule mitigation.** NY, PA (modified),
   DE, NE tax wages sourced to employer's state of in-office
   operation, even if employee works remotely from another state.

3. **PTET pass-through (#17).** SALT cap workaround for
   pass-through income.

4. **State PTE-like alternatives** — composite returns,
   withholding, pass-through entity-level tax elections.

5. **State-specific credits.** Residential energy, child care,
   education, dependent care, EITC supplements.

6. **Charitable contribution credits / deductions.** Many states
   offer credits for state-targeted charitable giving (HI renewable
   energy fund, AZ school choice credits, GA qualified school).

7. **Multi-state allocation.** Careful allocation can minimize
   overall state tax burden.

## Primary IRC authority

- §164 — State and local taxes.
- §164(b)(6) — $10,000 SALT cap (TCJA; possibly modified by OBBBA).

## Key federal authority

- **Comptroller of Treasury v. Wynne, 575 U.S. 542 (2015)** —
  Dormant Commerce Clause; states must offer credit for taxes paid
  to other states.
- **Edward A. Zelinsky v. Tax Appeals Tribunal, 1 N.Y.3d 85
  (2003)** — NY convenience-of-employer rule narrowing.

## Mechanics — domicile change

1. **Document substantive life changes.** Move primary residence,
   change driver's license, register to vote, change bank accounts,
   doctors, dentists, schools, club memberships.
2. **Track day count.** 183-day test for statutory residency.
3. **Sever ties to old state.** Sell or rent former primary
   residence; transfer professional licenses; disengage from
   old-state organizations.
4. **Avoid trips to old state.** Especially for high-income
   taxpayers facing residency audit.
5. **Address "abode" test.** Some states (NY) have permanent abode
   test even for non-domiciliaries.

## Mechanics — convenience-of-employer mitigation

1. **Establish bona fide office in employee's state.** Documented
   business need.
2. **Employer cooperation.** Employer must require (not merely
   accommodate) home-state work.
3. **Time tracking.** Document specific days worked in each state.

## Documentation requirements

- For domicile: lease/deed, utility bills, voter registration,
  driver's license, healthcare records, school enrollment, vehicle
  registration, tax filings showing change.
- For multi-state allocation: time and location tracking; income
  source documentation.

## Common pitfalls / audit risks

- **Incomplete domicile change.** NY and CA routinely challenge
  claimed domicile changes. The "5 primary factors" (home, time,
  items near and dear, active business involvement, family) are
  scrutinized.
- **Day-counting failures.** 183-day rules.
- **Statutory residency abode trap.** Even non-domiciliaries can
  be "statutory residents" if permanent abode + >183 days.
- **NY convenience-of-employer.** Telecommuters from NJ, CT, PA
  may still be NY-source-taxed.
- **Aggressive multistate allocation.** State combined-reporting
  rules may collapse aggressive shifts.

## Recent legislative changes

- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA SALT cap
  §164(b)(6) Pub L 119-21]`. SALT cap modifications would
  significantly affect this strategy area.

## State conformity considerations

This entire strategy is state-by-state.

## Default confidence band rationale

**MODERATE** — fact and state-specific. HIGH for substantive
domicile changes with strong documentation; LOW for quasi-domicile
moves intended to dodge tax without genuine life changes.

## Cross-references

- `ptet-salt-workaround` (#17).
- `c-corp-state-tax-savings` (#35).
- `primary-home-sale-exclusion` (#67).
- All state stub files.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 164","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section164","weight":"primary_statute"},
    {"authority_type":"SCOTUS","citation":"Comptroller of Treasury v. Wynne, 575 U.S. 542 (2015)","url":"https://www.supremecourt.gov","weight":"binding_judicial"}
  ]
}
```
