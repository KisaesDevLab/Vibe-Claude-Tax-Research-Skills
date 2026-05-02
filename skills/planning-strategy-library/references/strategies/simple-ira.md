---
name: "SIMPLE IRA (Savings Incentive Match Plan for Employees)"
slug: simple-ira
type: Retirement
tax_type: EFR
complexity: Low
irc_sections: ["§408(p)", "§402(g)"]
forms: ["Form 5304-SIMPLE or Form 5305-SIMPLE"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

SIMPLE IRA is a retirement plan designed for small employers (≤100
employees who received ≥$5,000 compensation in prior year). Key
features:

2024 limits:
- **Employee deferral:** $16,000 ($19,500 with catch-up over 50).
- **Employer contribution:** Either:
  - 3% of compensation matching contribution (for participating
    employees), OR
  - 2% of compensation nonelective contribution (for ALL eligible
    employees).
- **§401(a)(17) compensation limit** — $345,000.

The 3% match has a temporary reduction option (down to 1%) in 2 of
any 5 years.

SECURE 2.0 added:
- **Roth contributions** to SIMPLE IRA permitted (effective 2024).
- **Higher catch-up** for ages 60-63: 50% additional ($24,000
  total elective + $7,500 enhanced catch-up = up to $24,000;
  verify exact 2025/2026 implementation).
- **Higher employer match** option for some plans.

Eligibility (default):
- Compensation ≥$5,000 in any 2 prior years.
- Expected to earn ≥$5,000 current year.

Compared to SEP-IRA:
- SIMPLE allows employee deferrals (SEP does not).
- SIMPLE has lower contribution limits than SEP at higher comp.
- SIMPLE simpler than 401(k); no nondiscrimination testing.

Compared to 401(k):
- SIMPLE simpler administration but lower limits.
- SIMPLE early-withdrawal penalty 25% in first 2 years (vs. 10%).

## Primary IRC authority

- §408(p) — SIMPLE retirement accounts.
- §408(p)(2) — Contribution limits.
- §402(g) — Elective deferral limits.
- §72(t)(6) — 25% early withdrawal in first 2 years.

## Treasury regulations

- Reg §1.408-7.

## Key IRS guidance

- IRS Publication 560.
- Form 5304-SIMPLE / Form 5305-SIMPLE.

## Eligibility requirements

For employer:
1. Trade or business with ≤100 employees who received ≥$5,000
   prior year compensation.
2. No other qualified retirement plan (with limited exceptions).
3. Plan adopted by October 1 (or for new business, as soon as
   practicable).

For employee (default):
1. ≥$5,000 in compensation in any 2 prior years.
2. Expected to earn ≥$5,000 current year.

## Mechanics — how it works

1. **Adopt plan** by October 1 (Form 5304-SIMPLE or 5305-SIMPLE).
2. **Notify employees** of plan terms and election period.
3. **Annual employee election** (60-day window before plan year).
4. **Employee deferrals** via salary reduction.
5. **Employer contributes match (3%)** for participating employees
   OR **nonelective (2%)** for all eligible.
6. **Form 5305-SIMPLE plan document** kept on file (no annual IRS
   filing).
7. **Form W-2 Box 12 Code S** for employee SIMPLE deferrals.

## Documentation requirements

- Form 5304-SIMPLE or 5305-SIMPLE.
- Annual employee notice.
- Employee elections.
- W-2 Box 12 Code S.

## Common pitfalls / audit risks

- **2-year rule.** First 2 years of SIMPLE participation: rollover
  to non-SIMPLE IRA triggers 25% early withdrawal penalty (§72(t)(6))
  + ordinary income. Wait 2 years before any rollover.
- **§402(g) limit** lower than 401(k). Plan participants comparing.
- **Employer cannot have other plan** (with limited exceptions).
- **100-employee limit.** Growth past limit triggers transition
  period.
- **Match formula commitment.** 3% match committed for full year.

## Recent legislative changes

- **SECURE Act (2019)** — Various modifications.
- **SECURE 2.0 (2022)** — Roth contributions; higher employer
  match option; enhanced catch-ups.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §408(p)
  Pub L 119-21]`. Working assumption: standard rules preserved.

## State conformity considerations

State conformity generally complete.

## Default confidence band rationale

**HIGH** — straightforward statutory framework.

## Cross-references

- `sep-ira` (#76) — alternative for small business.
- `401k-pretax` (#75) — alternative for higher contribution
  capacity.
- `solo-401k-employer-contributions` (#82) — alternative for
  no-employee businesses.
- `roth-ira-contributions` (#79).
- `traditional-ira-contributions` (#83).
- `backdoor-roth-extended` (#72) — pro-rata interaction.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 408(p)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section408","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 402(g)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section402","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 72(t)(6)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section72","weight":"primary_statute"}
  ]
}
```
