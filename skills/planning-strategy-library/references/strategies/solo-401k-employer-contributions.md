---
name: "Solo 401(k) Employer Contributions"
slug: solo-401k-employer-contributions
type: SE Tax
tax_type: EFR
complexity: Medium
irc_sections: ["§401(k)", "§401(c)", "§415(c)", "§401(a)(17)", "§164(f)"]
forms: ["Form 5500-EZ (if assets >$250K)", "Schedule SE"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Solo 401(k) (also "Individual 401(k)" or "Self-Employed 401(k)")
is a 401(k) plan covering only the business owner (and possibly
spouse). The plan combines:

1. **Employee deferral** under §402(g): up to $23,000 ($30,500
   catch-up over 50) for 2024.
2. **Employer profit sharing** under §401(c): up to 25% of comp
   (20% of NESE for self-employed).
3. **Combined cap** under §415(c): $69,000 ($76,500 with catch-up)
   for 2024.

For solo business owners, this is generally the most powerful
retirement plan structure — combining employee deferral with
employer profit sharing maximizes total contributions while
remaining administratively simple.

Roth 401(k) component:
- Employee deferral can be Roth (or pre-tax, or split).
- Employer profit sharing must be pre-tax (until SECURE 2.0
  permitted Roth match — verify implementation).

Mega Backdoor Roth via Solo 401(k):
- Some Solo 401(k) plans permit after-tax (NOT Roth) contributions
  beyond §402(g) limit.
- After-tax can be converted to Roth via in-plan or distribution.
- Effectively allows additional $46,000+ Roth annually.

Form 5500-EZ filing required if plan assets exceed $250,000 at
year-end (or if final plan year).

Key advantage over SEP-IRA: Solo 401(k) allows owner to defer
$23,000+ on top of employer contribution; SEP-IRA only allows
employer contribution.

Key disadvantage: more administrative complexity than SEP-IRA;
plan adoption deadline traditionally December 31 of plan year
(SECURE Act extended to tax filing deadline for some elements
but employee deferral requires plan in place during year).

## Primary IRC authority

- §401(k) — Cash or deferred arrangements.
- §401(c) — Self-employed individuals.
- §402(g) — Elective deferral limit.
- §414(v) — Catch-up.
- §415(c) — Annual additions.
- §401(a)(17) — Compensation cap.
- §401(m) — Matching.
- §402A — Designated Roth.

## Treasury regulations

- Reg §1.401(k)-1 through §1.401(k)-6.
- Reg §1.401(c)(2)-1.
- Reg §1.402(g)-1.

## Key IRS guidance

- IRS Publication 560.
- Form 5500-EZ instructions.

## Eligibility requirements

For Solo 401(k):
1. Self-employed business owner.
2. No employees other than spouse (and limited part-time exclusions).
3. Plan adopted by deadline (employee deferral requires plan
   adoption by year-end of plan year; employer profit sharing by
   tax filing deadline).
4. Plan document (prototype/volume submitter typically used).

## Mechanics — how it works

1. **Adopt Solo 401(k) plan** by year-end (for deferral) and tax
   filing deadline (for profit sharing).
2. **Compute NESE** per Schedule SE.
3. **Employee deferral** up to §402(g) limit.
4. **Employer profit sharing** up to 20% of NESE.
5. **Combined ≤ §415(c) limit.**
6. **Form 5500-EZ if assets >$250K.**
7. **Roth deferral component** if elected.

## Documentation requirements

- Plan document.
- Plan adoption resolution.
- Annual contribution worksheet.
- Form 5500-EZ if applicable.
- Custodian statements.

## Common pitfalls / audit risks

- **Plan not adopted by year-end** for current-year employee
  deferral.
- **Hire of employee** triggers nondiscrimination testing and
  potential conversion to traditional 401(k).
- **§415(c) limit.** Combined employee + employer + after-tax.
- **§401(a)(17) compensation cap.**
- **Form 5500-EZ filing.** Required when assets >$250K.
- **Excess deferral.** §402(g) corrective distribution by April 15.
- **Spouse-employee.** Spouse can also defer if employed by
  business.
- **Pro-rata rule trap (Backdoor Roth).** Solo 401(k) balance NOT
  counted in IRA pro-rata (because it's not an IRA).

## Recent legislative changes

- **SECURE Act (2019)** — Plan adoption deadline extended for
  employer contributions.
- **SECURE 2.0 (2022)** — Various enhancements; Roth match
  permitted; SIMPLE Roth.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §401(k)
  Pub L 119-21]`. Working assumption: standard rules preserved.

## State conformity considerations

State conformity generally complete.

## Default confidence band rationale

**HIGH** — clear statutory framework.

## Cross-references

- `401k-pretax` (#75) — employee-side detail.
- `sep-ira-self-employed` (#81) — simpler alternative.
- `defined-benefit-cash-balance` (#73) — higher contribution
  alternative.
- `backdoor-roth-extended` (#72) — Mega Backdoor variant.
- `minimize-self-employment-tax` (#90).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 401(k)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section401","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 401(c)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section401","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 402(g)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section402","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 415(c)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section415","weight":"primary_statute"}
  ]
}
```
