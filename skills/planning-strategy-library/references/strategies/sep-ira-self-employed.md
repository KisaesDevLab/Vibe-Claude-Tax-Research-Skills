---
name: "SEP-IRA — Self-Employed Owner Maximization"
slug: sep-ira-self-employed
type: SE Tax
tax_type: EFR
complexity: Low
irc_sections: ["§408(k)", "§415(c)", "§401(a)(17)", "§164(f)"]
forms: ["Schedule SE", "Schedule 1 (deduction)"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

SEP-IRA strategy for sole proprietors, single-member LLCs, and
partners. Distinct considerations vs. employee-side SEP (#76):

1. **Deduction is above-the-line on Schedule 1.**
2. **Self-employed effective rate:** 25% of compensation = 20% of
   net earnings from self-employment (NESE).
3. **Compensation calculation:**
   - Net earnings from SE = Schedule C net profit × 92.35%.
   - Less ½ SE tax deduction.
   - Less SEP contribution (circular calculation).
4. **Maximum deductible contribution** = NESE × 20% (after ½ SE tax
   deduction), subject to §415(c) $69,000 (2024) and §401(a)(17)
   $345,000 compensation cap.

For partnerships and multi-member LLCs:
- SEP contribution is from partnership; pre-K-1 calculation.
- Each partner's contribution determined by partnership agreement.

Key planning advantage: SEP-IRA is the simplest plan for solo
business owners with no employees. Setup, ongoing administration,
and IRS reporting are minimal compared to 401(k) or DB plans.

For solo business with desire for higher contributions, consider:
- **Solo 401(k) (#82)** — adds $23,000 employee deferral capacity
  ($30,500 with catch-up over 50) on top of employer profit
  sharing.
- **Defined benefit / cash balance (#73)** — much higher
  contributions for older owners.

## Primary IRC authority

- §408(k) — Simplified employee pension.
- §415(c) — Annual additions limit.
- §401(a)(17) — Compensation limit.
- §164(f) — ½ SE tax deduction.
- §401(c)(2) — Net earnings from self-employment.

## Treasury regulations

- Reg §1.408-7.
- Reg §1.401(c)(2)-1.

## Key IRS guidance

- IRS Publication 560 — Retirement Plans for Small Business.
- IRS Publication 334 — Tax Guide for Small Business.
- Form 5305-SEP / 5305A-SEP.

## Eligibility requirements

For self-employed:
1. Net earnings from self-employment.
2. Plan adopted by tax filing deadline.
3. SEP-IRA established at custodian.

## Mechanics — how it works

1. **Compute Schedule C net profit** (or partnership earnings).
2. **Compute SE tax** on Schedule SE (15.3% on first $168,600
  Social Security wage base 2024; 2.9% Medicare on remainder; 0.9%
  Additional Medicare).
3. **Net earnings from SE** = SE income × 92.35%.
4. **Deductible ½ SE tax** = ½ × SE tax.
5. **Compensation for SEP purposes** = NESE - ½ SE tax.
6. **Maximum SEP contribution** = Compensation × (0.25 / 1.25) =
   Compensation × 20%.
7. **Contribute to SEP-IRA** by tax filing deadline (with
   extensions).
8. **Deduct on Schedule 1** as adjustment to income.

## Documentation requirements

- Schedule C / Schedule SE / Schedule K-1.
- SEP plan adoption (Form 5305-SEP or custom).
- Annual contribution computation worksheet.
- IRA custodian statements.

## Common pitfalls / audit risks

- **20% vs. 25% confusion.** 25% applies to W-2 employees; 20%
  applies to NESE.
- **§415(c) limit.** $69,000 (2024) total annual additions.
- **§401(a)(17) compensation cap.** $345,000 (2024).
- **Circular calculation.** Deducted SEP reduces NESE basis.
- **Multiple businesses.** §415(c) aggregated across all
  controlled businesses.
- **Pro-rata rule trap.** SEP balance counted in Backdoor Roth
  pro-rata calculation.

## Recent legislative changes

- **SECURE Act (2019)** — Plan adoption deadline.
- **SECURE 2.0 (2022)** — SEP Roth permitted (verify
  implementation).
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §408(k)
  Pub L 119-21]`. Working assumption: standard rules preserved.

## State conformity considerations

State conformity generally complete.

## Default confidence band rationale

**HIGH** — straightforward statutory framework.

## Cross-references

- `sep-ira` (#76) — employee-side detail.
- `solo-401k-employer-contributions` (#82) — preferred if
  deferral capacity desired.
- `defined-benefit-cash-balance` (#73) — higher contribution
  alternative.
- `backdoor-roth-extended` (#72) — pro-rata rule trap.
- `minimize-self-employment-tax` (#90).
- `traditional-ira-contributions` (#83).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 408(k)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section408","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 415(c)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section415","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 401(a)(17)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section401","weight":"primary_statute"}
  ]
}
```
