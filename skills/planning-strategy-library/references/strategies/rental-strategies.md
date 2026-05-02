---
name: "Rental Real Estate Strategies (Umbrella)"
slug: rental-strategies
type: Business - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§469", "§280A", "§168", "§121", "§1031", "§199A", "§1411"]
forms: ["Schedule E", "Form 8582"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

This strategy file is the umbrella reference for rental real estate
planning, cross-referencing the more specific rental strategies in
the library. Rental real estate is unusually rich in tax planning
opportunities because it sits at the intersection of:

1. **§469 Passive Activity Loss rules** — including the per-se
   passive characterization (§469(c)(2)), the active-participation
   $25K offset (§469(i)), the real-estate-professional exception
   (§469(c)(7)), grouping (Reg §1.469-4), and self-rental
   recharacterization (Reg §1.469-2(f)(6)).
2. **§280A vacation home rules** — limiting deductions when
   personal use is significant.
3. **§168 / §168(k) / §179 / Cost Segregation** — accelerated
   depreciation on improvements and components.
4. **§1031 Like-Kind Exchange** — deferral on disposition.
5. **§121 Primary Residence Exclusion** — interaction with rental
   conversion.
6. **§199A Qualified Business Income** — Notice 2019-07 safe
   harbor for rental real estate enterprise.
7. **§1411 NIIT** — application to net rental income.

This file consolidates the cross-references and identifies which
specific strategy file to consult for each rental scenario.

## Primary IRC authority

See umbrella-referenced files.

## Strategic decision tree

**Q1: Is the property short-term rental (avg customer use ≤7 days)?**
- Yes → see `short-term-rental` (#26). STR is not a rental activity
  under Temp. Reg §1.469-1T(e)(3); material participation analysis
  determines passive characterization.
- No → continue.

**Q2: Is taxpayer a real estate professional?**
- Yes → see `real-estate-professional-extended` (#20) and
  `predict-real-estate-pro`. Make §469(c)(7)(A) election; rentals
  treated as nonpassive if material participation per rental (or
  aggregated under election).
- No → continue.

**Q3: Below $150K MAGI?**
- Yes → see `active-participation-real-estate` (#3). $25K offset
  available with active participation (lower bar than material
  participation).
- No → continue.

**Q4: Suspended passive losses to absorb?**
- Yes → see `passive-income-pigs` (#16). Or wait for §469(g)
  release on disposition. Or see `grouping-of-activities` (#9).

**Q5: Considering disposition?**
- Yes → see `1031-like-kind-exchange` (#1) for deferral; or
  `installment-sale` (#33); or §121 exclusion if converted to
  primary residence (`primary-home-sale-exclusion` #67).

**Q6: New purchase?**
- See `cost-segregation-extended` (#41) for engineering study to maximize
  bonus / §179.

**Q7: §199A planning?**
- See `qbi-deduction` (#19) and Notice 2019-07 rental real estate
  safe harbor (250 hours of rental services).

## Mechanics — how it works (general)

1. **Maintain separate books per property.** Track income, expenses,
   capital improvements, depreciation, repairs vs. improvements
   under tangible property regs.
2. **Annual passive activity tracking.** Form 8582; track suspended
   losses by activity.
3. **Year-end planning.**
   - Bonus / §179 on improvements.
   - Cost-seg study for new acquisitions.
   - PTET if entity-structured.
   - §1031 planning if disposing.
4. **State PTET election** if entity-structured (interaction with
   #17).

## Cross-references

- **`active-participation-real-estate`** (#3)
- **`real-estate-professional-extended`** (#20)
- **`grouping-of-activities`** (#9)
- **`passive-income-pigs`** (#16)
- **`short-term-rental`** (#26)
- **`1031-like-kind-exchange`** (#1)
- **`cost-segregation-extended`** (#41)
- **`installment-sale`** (#33)
- **`qbi-deduction`** (#19)
- **`primary-home-sale-exclusion`** (#67)
- **`niit-minimization`** (#69)
- **`ptet-salt-workaround`** (#17)

## Authorities (JSON sidecar fragment)

This file is a router; specific authorities live in the cross-
referenced files.

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 469",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section469",
      "weight": "primary_statute"
    }
  ]
}
```
