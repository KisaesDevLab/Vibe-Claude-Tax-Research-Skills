---
name: "Self-Employed Health Insurance Deduction (§162(l))"
slug: health-insurance-self-employed
type: SE Tax
tax_type: EFR
complexity: Low
irc_sections: ["§162(l)"]
forms: ["Schedule 1 (above-the-line deduction)"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

§162(l) provides an above-the-line deduction for health insurance
premiums paid by self-employed individuals. The deduction is
"above-the-line" on Schedule 1 of Form 1040, reducing AGI (not
just taxable income), and is available without itemizing.

The deduction covers:
- Medical, dental, and qualified long-term care insurance.
- For taxpayer, spouse, dependents, and §152(f)(2) children
  under age 27.

Key features:
1. **Above-the-line** — reduces AGI; benefits non-itemizers.
2. **Earned income limit** — deduction cannot exceed earned income
   from the trade or business that established the plan.
3. **Plan establishment** — plan must be in name of business OR
   in name of self-employed individual.
4. **NOT subject to SE tax reduction** — the deduction reduces
   income tax base but does NOT reduce SE tax base under
   §1402(a)(12). Common practitioner error.
5. **Coordination with §125 cafeteria plan** — sole proprietor
   cannot participate in §125 plan (must use §162(l) instead).
6. **Coordination with marketplace premium tax credit** —
   deduction reduces MAGI for §36B premium tax credit phaseout
   computation.
7. **§1402(a)(12) reduction** — no longer available; pre-2010
   special rule allowed deduction in computing SE tax was
   eliminated.

For S corp 2%+ shareholders: §162(l) applies via §1372 special
rule — see `health-insurance-s-corp` (#10).

For partners: §162(l) applies if partnership pays premium and
includes in K-1 guaranteed payment.

## Primary IRC authority

- §162(l) — Special rules for health insurance costs of self-
  employed individuals.
- §162(l)(1)(A) — Deduction equal to amount paid.
- §162(l)(2) — Earned income limitation.
- §162(l)(5) — Coordination with other rules.
- §1372 — S corp 2%+ shareholders treated as partners (interaction).
- §1402(a)(12) — Treatment for SE tax (deduction NOT allowed in
  computing SE tax post-2010).

## Treasury regulations

- Reg §1.162(l)-1 — Self-employed health insurance deduction.

## Key IRS guidance

- IRS Publication 535 — Business Expenses.
- IRS Publication 502 — Medical and Dental Expenses (for §213
  comparison).

## Eligibility requirements

1. **Self-employed individual** with net earnings from
   self-employment, OR partner in partnership, OR 2%+ S corp
   shareholder.
2. **Insurance plan established in name of business** OR in name
   of self-employed individual (post-Notice 2008-1 expansion).
3. **Eligible for employer-subsidized coverage NOT available** —
   if taxpayer or spouse eligible for subsidized coverage from
   another job, deduction unavailable for that month.
4. **Earned income from the business** establishing the plan ≥
   premium amount.

## Mechanics — how it works

1. **Verify plan establishment.** Sole proprietor: in name of
   individual is acceptable post-Notice 2008-1.
2. **Pay premium.** Direct payment by individual or by business.
3. **Compute earned income limit.** Self-employed: NESE less ½ SE
   tax less retirement plan contributions.
4. **Deduct on Schedule 1 line 17** — above-the-line.
5. **Coordinate with marketplace premium tax credit** — circular
   calculation under §36B because deduction reduces MAGI which
   affects credit which affects deduction.

## Documentation requirements

- Insurance policy and premium statements.
- Earned income computation worksheet.
- For S corp 2%+ shareholders: W-2 with proper Box 1 inclusion
  (#10).
- For partners: K-1 with guaranteed payment for premium.

## Common pitfalls / audit risks

- **Earned income limit.** Deduction cannot exceed business
  earnings from plan-establishing entity.
- **Multiple businesses.** Plan established by Business A;
  deduction limited to Business A earned income, not aggregate.
- **Eligibility for subsidized coverage.** Disqualifies for any
  month either spouse eligible for employer subsidy.
- **§125 coordination error.** Sole prop cannot use §125 cafeteria
  plan; must use §162(l).
- **§1402(a)(12) pre-2010 method.** Old practice of deducting in
  SE tax base was eliminated; some practitioners still incorrectly
  apply.
- **§213 itemized deduction.** Same premiums cannot be both
  §162(l) and §213.
- **Marketplace premium tax credit interaction.** Circular
  calculation requires care.

## Recent legislative changes

- **No material recent changes.**
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §162(l)
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity to §162(l) generally complete.

## Default confidence band rationale

**HIGH** — clear statutory framework.

## Cross-references

- `health-insurance-s-corp` (#10) — S corp variant.
- `group-health-insurance` (#8).
- `hra-merp` (#11).
- `hsa-optimization` (#63).
- `accountable-plan-self-employed` (#84).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 162(l)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section162","weight":"primary_statute"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.162(l)-1","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"}
  ]
}
```
