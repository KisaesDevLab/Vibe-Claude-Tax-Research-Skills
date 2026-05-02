---
name: "Corporate-Owned VUL ('No-Limits Roth IRA')"
slug: corporate-owned-vul
type: Income Shifting
tax_type: EFR
complexity: High
irc_sections: ["§7702", "§101(a)", "§101(j)", "§72(e)"]
forms: ["Form 8925 (Employer-Owned Life Insurance Reporting)"]
state_specific: true
aggressive: true
caution: true
confidence_default_band: LOW
last_obbba_review: "N/A"
---

> **AGGRESSIVE STRATEGY WARNING:** "Corporate-Owned VUL" — sometimes
> marketed as "No-Limits Roth IRA" or "401(h) Plan" — uses an
> over-funded permanent life insurance policy owned by an employer
> to provide tax-deferred wealth accumulation. Specific risks:
> (a) §101(j) Employer-Owned Life Insurance rules require notice
> and consent before issuance or death benefit becomes ordinary
> income; (b) IRS attention to over-funded life insurance vehicles
> as deferred compensation under §409A; (c) potential constructive
> dividend treatment; (d) reasonable compensation issues if
> excessive premiums substitute for compensation; (e) state
> insurance regulations. Marketers oversell the "No-Limits Roth"
> framing — the structure is fundamentally life insurance with
> substantial costs and regulatory complexity, not a Roth substitute.

## Overview

Structure: closely-held corporation purchases VUL on executive's
life. Corporation pays substantial premiums, "over-funded" relative
to death benefit, building cash value tax-deferred. At retirement,
executive takes loans against cash value (loans not taxable). At
death, death benefit pays to corporation tax-free (§101); through
complex structuring, value flows to family.

Marketing claims:
1. Tax-deferred growth (similar to 401(k)).
2. Tax-free policy loans (similar to Roth).
3. Tax-free death benefit (§101).
4. No income limits or contribution limits.

Reality:
- Insurance costs (mortality, administration, surrender charges)
  significantly reduce returns.
- §101(j) Employer-Owned Life Insurance rules subject death benefit
  to ordinary income unless specific notice and consent followed.
- §7702A modified endowment contract (MEC) rules can change loan
  tax treatment.
- §409A may apply if structured as deferred compensation.
- Reasonable compensation issues if excessive premiums.
- IRS scrutiny of over-funded life insurance schemes.

## Primary IRC authority

- §7702 — Definition of life insurance contract.
- §101(a) — Death benefit excluded from income.
- §101(j) — Employer-owned life insurance; notice and consent
  required for §101(a) exclusion.
- §72(e) — Annuity / life insurance contract distribution.
- §7702A — Modified endowment contract.
- §409A — Deferred compensation.

## Treasury regulations

- Reg §1.7702-0 through §1.7702-2 — Life insurance definition.
- Reg §1.101-1 through §1.101-7 — §101 implementation.

## Key IRS guidance

- Notice 2007-78 — §101(j) employer-owned life insurance.
- Notice 2009-48 — §101(j) further guidance.

## Eligibility requirements

§101(j) preservation of §101(a):
1. **Notice and consent** before issuance: employee notified in
   writing of insurance, amount, employer beneficiary; written
   consent obtained. Form 8925 required.
2. **Insured is highly compensated employee** at time of issuance,
   OR §101(j)(2)(B) exception applies.

§7702 life insurance treatment:
1. Policy satisfies §7702 cash value accumulation test or
   guideline premium / cash value corridor test.
2. Not a §7702A MEC.

## Mechanics — how it works (as marketed)

1. **Corporation purchases VUL** on executive's life. Substantial
   premium.
2. **§101(j) notice and consent** obtained; Form 8925 filed.
3. **Premium payments continue** for years; cash value grows
   tax-deferred.
4. **At retirement, executive borrows against cash value** —
   policy loans not currently taxable (assuming non-MEC).
5. **Death benefit at executive's death** — tax-free to
   corporation under §101 (assuming §101(j) compliance).
6. **Family receives wealth via supplemental structure** — split-
   dollar arrangement, executive bonus plan, or other vehicle.

## Documentation requirements

- Insurance policy.
- §101(j) notice and consent.
- Form 8925 annual reporting.
- Board resolutions.
- §7702 testing documentation.

## Common pitfalls / audit risks

- **§101(j) compliance failure.** Death benefit becomes ordinary
  income to corporation.
- **MEC classification.** Loans become taxable.
- **Reasonable compensation.** Excessive premiums in lieu of wages
  recharacterized.
- **Constructive dividend.** Personal benefit recharacterized.
- **§409A.** If structured as deferred compensation.
- **State insurable interest rules.** Some states require
  documented insurable interest.
- **Promoter overstatement.** Marketed returns and tax benefits
  often overstate after-cost economics.

## Recent legislative changes

- No major statutory changes recent.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §101 §7702
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State insurance regulations and tax treatment vary significantly.

## AICPA SSTS / Circular 230 considerations

Aggressive strategy. Insist on §101(j) notice and consent and
Form 8925; verify §7702 / §7702A status with carrier; document
business purpose for corporate ownership; recommend Form 8275
disclosure; caution client against promoter oversimplifications.

## Default confidence band rationale

**LOW** — Marketing claims often outpace tax substance; multiple
audit risk vectors; no clear safe harbor for "No-Limits Roth"
structure.

## Cross-references

- `life-insurance-retirement-plan` (#74) — closely-related
  individual variant.
- `reasonable-comp-corp-owners` (#21).
- `401k-pretax` (#75) — compliant alternative.
- `solo-401k-employer-contributions` (#82) — compliant alternative.
- `defined-benefit-cash-balance` (#73) — compliant alternative.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 101(j)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section101","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 7702","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section7702","weight":"primary_statute"},
    {"authority_type":"Notice","citation":"Notice 2007-78","url":"https://www.irs.gov/irb","weight":"irs_published"},
    {"authority_type":"Notice","citation":"Notice 2009-48","url":"https://www.irs.gov/irb","weight":"irs_published"}
  ]
}
```
