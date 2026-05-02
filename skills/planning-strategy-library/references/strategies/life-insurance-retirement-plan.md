---
name: "Life Insurance Retirement Plan (LIRP)"
slug: life-insurance-retirement-plan
type: Retirement
tax_type: EFR
complexity: High
irc_sections: ["§7702", "§101(a)", "§72(e)", "§7702A"]
forms: ["Form 1099-R (if distribution becomes taxable)"]
state_specific: true
aggressive: true
caution: true
confidence_default_band: LOW
last_obbba_review: "N/A"
---

> **AGGRESSIVE STRATEGY WARNING:** "Life Insurance Retirement Plan"
> (LIRP) — sometimes marketed as "401(k) Alternative," "Tax-Free
> Retirement Account," "Indexed Universal Life retirement strategy,"
> or "Roth Replacement" — uses an over-funded permanent life
> insurance policy (typically Indexed Universal Life or Whole Life)
> as a retirement accumulation vehicle. The strategy is heavily
> promoted by life insurance agents, often with materially misleading
> claims about returns and tax benefits. Specific risks: (a)
> high insurance costs (mortality, administration, surrender
> charges) significantly reduce actual returns vs. illustrated; (b)
> §7702A Modified Endowment Contract (MEC) classification can
> retroactively eliminate the loan-tax-free benefit; (c) policy
> lapse after substantial loans triggers ordinary income on
> "phantom" gain; (d) lack of regulatory protections and
> transparency relative to qualified plans. Practitioners should
> evaluate LIRPs critically and prefer compliant alternatives
> (Roth IRA, Roth 401(k), Mega Backdoor Roth, defined benefit /
> cash balance) wherever possible.

## Overview

The LIRP structure: an individual purchases a permanent life
insurance policy (typically Indexed Universal Life — IUL — or Whole
Life) and significantly over-funds it relative to the death
benefit. The cash value grows on a tax-deferred basis. At
retirement, the individual takes "tax-free" loans against the
cash value.

Marketed benefits:
1. Tax-deferred growth.
2. Tax-free policy loans (assuming non-MEC).
3. Tax-free death benefit (§101).
4. No income limits or contribution caps (unlike Roth IRA).
5. No required distributions (unlike Traditional IRA).

Reality:
- **High costs.** Mortality charges, administrative fees, surrender
  charges typically consume 10-30% of contributions in early years.
  Net return materially below illustrated.
- **§7702A MEC trap.** Funding too aggressively (more than 7-pay
  test allows) makes contract a MEC; loans become taxable.
- **Lapse risk.** If policy lapses with outstanding loans
  (substantial loans + market downturn + insurance cost increases),
  the entire loan-tax-free framework collapses; ordinary income
  recognized on phantom gain.
- **Surrender charges.** Early termination penalties can eliminate
  20-50% of cash value in first 10-15 years.
- **Investment limitations.** IUL caps and floors limit upside
  participation.
- **Lack of fiduciary protection.** Insurance agent commissions
  often 50%+ of first-year premium.

When LIRPs may be appropriate:
- High-income taxpayers maxed out on qualified plans.
- Need for permanent life insurance.
- Long-term horizon (20+ years).
- Estate planning beneficiary needs.

When LIRPs are inappropriate:
- Substitute for qualified plan / Roth contribution.
- "Free retirement" claims.
- Short investment horizon.
- Low-income taxpayer not maxing out other tax-advantaged accounts.

## Primary IRC authority

- §7702 — Definition of life insurance contract.
- §7702A — Modified endowment contracts.
- §101(a) — Death benefit excluded.
- §72(e) — Annuity / life insurance contract distributions.

## Treasury regulations

- Reg §1.7702-0 through §1.7702-2.
- Reg §1.101-1 through §1.101-7.

## Key IRS guidance

- Notice 2007-78 — §101(j) (when employer-owned).
- IRS Publication 525 — Taxable and Nontaxable Income.

## Key court decisions

- Limited direct case law on the LIRP structure specifically.
- §7702A litigation generally focused on MEC classification.

## Eligibility requirements

For §7702 life insurance treatment:
1. Policy satisfies §7702 cash value accumulation test or
   guideline premium / cash value corridor test.
2. Not a §7702A MEC.

For §72(e) loan tax-free:
1. Non-MEC contract.
2. Loan from cash value (not partial surrender).

## Mechanics — how it works (as marketed)

1. **Purchase permanent life insurance** (IUL, Whole Life, etc.).
2. **Over-fund within §7702 limits.** Pay maximum premium without
   triggering MEC.
3. **Cash value accumulates** through insurance investment options
   (fixed account, indexed account, separate account).
4. **At retirement, take policy loans** against cash value. Not
   currently taxable (assuming non-MEC).
5. **Continue policy through life.** Loans repaid at death from
   death benefit.
6. **Death benefit pays** to beneficiaries tax-free under §101.

## Documentation requirements

- Insurance policy.
- §7702 / §7702A test compliance from carrier.
- Annual policy statements.
- Loan records.

## Common pitfalls / audit risks

- **MEC classification.** §7702A 7-pay test failure makes
  contract a MEC; loans become taxable.
- **Policy lapse.** Outstanding loans + decreasing cash value +
  insurance costs eat the policy alive; lapse triggers ordinary
  income on phantom gain.
- **§409A.** If structured as employer benefit.
- **Insurance cost erosion.** Real returns far below illustrated.
- **Surrender charges.** Early termination expensive.
- **Comparison to alternatives.** Qualified plans, Roth IRA, Mega
  Backdoor Roth all preferable in nearly all cases.

## Recent legislative changes

- No major statutory changes.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §7702
  §7702A Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State insurance regulations and tax treatment vary significantly.

## AICPA SSTS / Circular 230 considerations

Aggressive strategy. Practitioner should:
- Evaluate critically; compare against qualified alternatives.
- Verify §7702 / §7702A status with carrier.
- Document client's understanding of costs and risks.
- Decline to recommend if client has alternative tax-advantaged
  capacity available.

## Default confidence band rationale

**LOW** — Marketing claims often outpace tax substance and economic
reality. Multiple risk vectors. Compliant alternatives generally
preferable.

## Cross-references

- `corporate-owned-vul` (#44) — corporate variant.
- `roth-ira-contributions` (#79) — preferred alternative.
- `roth-ira-conversion` (#80) — preferred alternative.
- `backdoor-roth-extended` (#72) — preferred alternative.
- `defined-benefit-cash-balance` (#73) — preferred alternative.
- `401k-pretax` (#75) — preferred alternative.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 7702","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section7702","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 7702A","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section7702A","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 72(e)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section72","weight":"primary_statute"}
  ]
}
```
