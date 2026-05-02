---
name: "401(k) Pre-Tax (and Roth) Employee Deferral"
slug: 401k-pretax
type: Retirement
tax_type: EFR
complexity: Low
irc_sections: ["§401(k)", "§402(g)", "§414(v)"]
forms: ["W-2 Box 12 Code D (pre-tax) or AA (Roth)"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

§401(k) cash or deferred arrangement allows employees to elect
salary reduction (pre-tax) or designated Roth (after-tax)
contributions to 401(k) plan, with employer match and profit
sharing additions allocated by formula.

2024 limits:
- **§402(g) employee deferral:** $23,000 ($30,500 with §414(v)
  catch-up over 50).
- **§415(c) total annual additions:** $69,000 ($76,500 with
  catch-up; includes employee + employer + profit sharing).
- **Compensation limit §401(a)(17):** $345,000.

SECURE 2.0 (2022) created additional catch-up provisions:
- **Age 60-63 enhanced catch-up:** $11,250 (2024 — verify; replaces
  standard $7,500 catch-up for that age band).
- **Mandatory Roth catch-up for high earners** (>$145K prior-year
  comp; effective 2026 per SECURE 2.0 originally; delayed by IRS).

Coordination:
- **§402(g) limit applies across all 401(k)/403(b)/457(b) plans.**
- Employee with multiple employers must coordinate.
- §401(k) excludable from Box 1; FICA still applies (Box 3, 5).

Key planning levers:
1. **Max deferral** to §402(g) limit.
2. **Roth vs. pre-tax** based on current vs. expected retirement
   bracket.
3. **Employer match capture** — at minimum contribute enough to
   capture full match.
4. **Mega Backdoor Roth (#72)** — if plan permits after-tax
   contributions.
5. **Coordinate with HSA, FSA** for total tax-advantaged dollars.

## Primary IRC authority

- §401(k) — Cash or deferred arrangements.
- §401(m) — Matching contributions.
- §402(g) — Limitation on elective deferrals.
- §414(v) — Catch-up contributions.
- §415(c) — Annual additions limit.
- §401(a)(17) — Compensation limit.
- §402A — Designated Roth contributions.

## Treasury regulations

- Reg §1.401(k)-1 through §1.401(k)-6.
- Reg §1.401(m)-1.
- Reg §1.402(g)-1.
- Reg §1.414(v)-1.
- Reg §1.402A-1 through §1.402A-2.

## Key IRS guidance

- Rev. Proc. 2024-XX (annual COLA) — limits.
- Notice 2014-54 — In-plan Roth conversions.
- IRS Publication 560 — Retirement Plans for Small Business.

## Eligibility requirements

For employee deferrals:
1. Eligible employee under plan terms.
2. Within §402(g) annual limit (across all plans).
3. Compensation up to §401(a)(17) limit.

## Mechanics — how it works

1. **Plan election** — designate deferral percentage and
   pre-tax/Roth allocation.
2. **Pre-tax deferral reduces W-2 Box 1.**
3. **Roth deferral does NOT reduce Box 1.**
4. **FICA still applies** (Box 3, 5) regardless.
5. **Employer match per plan formula.**
6. **Year-end W-2** reports deferrals in Box 12.
7. **Form 1099-R at distribution.**

## Documentation requirements

- Plan summary.
- Deferral election form.
- W-2 Box 12 codes.
- 1099-R at distribution.

## Common pitfalls / audit risks

- **§402(g) excess deferrals.** Multi-employer scenarios; correct
  by April 15 of following year via §402(g)(2)(A) corrective
  distribution.
- **§415(c) annual additions limit exceeded.** Excess corrected
  per Rev. Proc.
- **§401(k) ADP / ACP testing.** Highly compensated employees
  (HCEs) limited if plan fails testing.
- **Safe harbor 401(k)** avoids ADP/ACP testing but requires
  specific employer contributions.
- **Roth in-plan conversion** — once converted, cannot be undone
  (post-TCJA).
- **§72(t) early distribution penalty** for distributions before
  age 59½ (with exceptions).

## Recent legislative changes

- **SECURE Act (2019)** — Various provisions.
- **SECURE 2.0 (2022)** — Enhanced catch-ups; mandatory Roth
  catch-up for high earners; emergency distributions; etc.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §401(k)
  §402(g) Pub L 119-21]`. Working assumption: standard limits
  preserved.

## State conformity considerations

State conformity to §401(k) generally complete; state tax of
distributions varies.

## Default confidence band rationale

**HIGH** — clear statutory framework.

## Cross-references

- `solo-401k-employer-contributions` (#82).
- `backdoor-roth-extended` (#72) — Mega Backdoor variant.
- `roth-ira-contributions` (#79).
- `defined-benefit-cash-balance` (#73).
- `sep-ira` (#76).
- `simple-ira` (#77).
- `employer-benefit-package-review` (#71).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 401(k)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section401","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 402(g)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section402","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 414(v)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section414","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 415(c)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section415","weight":"primary_statute"}
  ]
}
```
