---
name: "SEP-IRA (Simplified Employee Pension)"
slug: sep-ira
type: Retirement
tax_type: EFR
complexity: Low
irc_sections: ["§408(k)", "§415(c)"]
forms: ["Form 5305-SEP (model document)"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Simplified Employee Pension (SEP-IRA) is a retirement plan
permitting employer contributions to traditional IRAs of eligible
employees. Strengths:

1. **Easy setup** — Form 5305-SEP model document; no Form 5500
   filing.
2. **Employer-only contributions** (no employee deferrals).
3. **Up to 25% of compensation** (effectively 20% for self-
   employed due to SE tax interaction).
4. **§415(c) limit** — $69,000 (2024).
5. **§401(a)(17) compensation limit** — $345,000 (2024).
6. **No nondiscrimination testing** if uniform percentage
   contributed.
7. **Plan adoption flexibility** — by tax filing deadline of
   employer.

Eligibility (default):
- Age 21+.
- Worked at least 3 of last 5 years.
- Earned at least $750 (2024).

Constraint: SEP-IRA is funded entirely from employer; if the
business has employees, the same percentage must be contributed
for all eligible employees. This makes SEP-IRA economically
unattractive for businesses with substantial employee headcount
relative to owner.

For solo / no-employee businesses, SEP-IRA is straightforward and
cost-effective. For businesses with employees, Solo 401(k)
alternative often better (allows owner to defer separately
without parallel employee contribution requirement).

SEP-IRA cannot offer Roth treatment (until SECURE 2.0 — verify if
implemented; SIMPLE-IRA Roth was added by SECURE 2.0).

## Primary IRC authority

- §408(k) — Simplified employee pension.
- §408(k)(2) — Eligibility requirements.
- §408(k)(3) — Contribution limits.
- §415(c) — Annual additions limit.
- §401(a)(17) — Compensation limit.

## Treasury regulations

- Reg §1.408-7 through §1.408-8.

## Key IRS guidance

- IRS Publication 560 — Retirement Plans for Small Business.
- Form 5305-SEP / Form 5305A-SEP (instructions).

## Eligibility requirements

For employer:
1. Trade or business with earned income.
2. Plan adopted by tax filing deadline.
3. Form 5305-SEP or custom plan document.

For employee (default; can be more generous):
1. Age 21+.
2. Worked at least 3 of last 5 years.
3. Earned at least $750 (2024).

## Mechanics — how it works

1. **Adopt SEP plan.** Form 5305-SEP for prototype; adoption by
   tax filing deadline.
2. **Establish SEP-IRA** at any IRA custodian for each eligible
   employee.
3. **Contribute employer portion.** Up to 25% of compensation per
   employee (uniform percentage for all eligible).
4. **For self-employed:** effective rate is 20% of net earnings
   from self-employment after deduction for ½ SE tax.
5. **Tax deduction** to employer in year of contribution.
6. **No employee deferrals** under SEP-IRA.

## Documentation requirements

- Plan adoption (Form 5305-SEP or custom).
- Annual contribution allocation worksheet.
- Form W-2 (Box 12 not required for SEP-IRA; Box 13 "Retirement
  Plan" checked).
- IRA custodian statements.

## Common pitfalls / audit risks

- **Eligibility confusion.** Default is age 21 + 3 of 5 years;
  employer can be more generous (less restrictive eligibility) but
  not more restrictive.
- **Uniform percentage.** Same % for all eligible.
- **§401(a)(17) compensation cap.** Comp above $345K (2024) not
  considered.
- **Dual-coverage trap.** Employee in SEP-IRA + 401(k) — combined
  §415(c) limit applies.
- **Self-employed effective rate.** 25% of comp = 20% of net SE
  earnings (after ½ SE tax deduction).
- **Plan termination.** Not as flexible as 401(k); SEP balance
  is in IRA.

## Recent legislative changes

- **SECURE Act (2019)** — Plan adoption deadline extended.
- **SECURE 2.0 (2022)** — Various technical changes; SEP Roth
  added (verify implementation).
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §408(k)
  Pub L 119-21]`. Working assumption: standard rules preserved.

## State conformity considerations

State conformity generally complete.

## Default confidence band rationale

**HIGH** — straightforward statutory framework.

## Cross-references

- `solo-401k-employer-contributions` (#82) — preferred for
  no-employee businesses with deferral capability.
- `simple-ira` (#77) — alternative for small businesses.
- `401k-pretax` (#75).
- `defined-benefit-cash-balance` (#73).
- `sep-ira-self-employed` (#81).
- `traditional-ira-contributions` (#83).
- `backdoor-roth-extended` (#72) — pro-rata interaction.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 408(k)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section408","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 415(c)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section415","weight":"primary_statute"}
  ]
}
```
