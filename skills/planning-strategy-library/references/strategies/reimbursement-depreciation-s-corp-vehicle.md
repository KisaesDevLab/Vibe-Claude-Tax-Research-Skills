---
name: "Reimbursement of Depreciation Expenses — S Corp Owner Vehicle"
slug: reimbursement-depreciation-s-corp-vehicle
type: Business - Other
tax_type: EFR
complexity: High
irc_sections: ["§62(a)(2)(A)", "§168", "§280F", "§274(d)"]
forms: ["Form 4562 (corporate level if corp owns vehicle)"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
caution: true
confidence_default_band: MODERATE
last_obbba_review: "N/A"
---

## Overview

This strategy addresses an intricate question: how should an S
corporation owner-employee handle vehicle ownership and
depreciation? Three structures are common:

1. **Owner owns vehicle; corporation reimburses standard mileage
   rate.** Simplest. Owner reports nothing; corporation deducts.
   Owner cannot also claim depreciation personally because IRS
   standard mileage rate includes a depreciation component.
2. **Owner owns vehicle; corporation reimburses actual expenses
   (including depreciation share).** Complex. Owner must compute
   depreciation; corporation reimburses business-use share. Owner's
   personal depreciation tracking required.
3. **Corporation owns vehicle.** Corporation depreciates fully
   subject to §280F luxury auto caps. Owner-employee personal use
   creates W-2 inclusion (compensation income) for personal
   commuting and personal use — measured under Reg §1.61-21
   (annual lease value or vehicle cents-per-mile rule).

The strategy file's name implies structure #2, which is the most
complex variant. The strategic question: can the corporation's
accountable plan reimburse the owner-employee for depreciation on
the owner's personally-owned vehicle? Generally yes, under Reg
§1.62-2, with §274(d) substantiation. The mechanics require:

1. Owner determines the vehicle's depreciable basis.
2. Annual depreciation computed (subject to §280F luxury auto
   limits if light passenger auto).
3. Business-use percentage applied.
4. Corporation reimburses owner the business-use depreciation
   share.
5. Owner does not also claim depreciation directly (no double-
   dipping).

The §280F luxury auto caps at the owner level limit the
depreciation that can be reimbursed. Heavy SUV (>6,000 lbs GVWR)
and heavy truck planning escapes §280F caps.

The structure is uncommon in practice. Most practitioners prefer
either standard mileage rate reimbursement (simplest) or
corporation ownership (cleanest). The actual-expense-with-
depreciation reimbursement structure has multiple compliance
failure points.

## Primary IRC authority

- **§62(a)(2)(A)** — Accountable plan.
- **§168** — MACRS.
- **§280F** — Luxury auto caps.
- **§274(d)** — Substantiation.

## Treasury regulations

- **Reg §1.62-2** — Accountable plan.
- **Reg §1.280F-1T through §1.280F-7** — Luxury auto.
- **Reg §1.274-5T** — Substantiation.
- **Reg §1.61-21** — Personal use of corporate-owned vehicle (for
  structure #3).

## Key IRS guidance

- **Rev. Proc. 2019-46** — Standard mileage rate.
- **Annual Rev. Proc. on §280F luxury auto caps.**

## Key court decisions

- See cases under #4.

## Eligibility requirements

For the depreciation-reimbursement structure:
1. Owner personally owns the vehicle.
2. Vehicle used in S corp business activity.
3. Accountable plan adopted by S corp.
4. §274(d) substantiation maintained.
5. Owner depreciation tracked personally; reimbursed amount
   not separately claimed by owner.
6. §280F luxury auto caps applied at owner level.

## Mechanics — how it works

1. **Document vehicle ownership.**
2. **Establish depreciation method.** Generally MACRS 5-year for
   passenger autos. §168(k) bonus and §179 considerations.
3. **Apply §280F caps if light passenger auto.**
4. **Compute annual depreciation × business-use percentage.**
5. **Submit reimbursement request to corporation.**
6. **Corporation reimburses; owner does not separately deduct
   depreciation.**
7. **Track basis for eventual sale.** Reimbursed depreciation
   reduces basis (effectively), creating gain on sale.

## Documentation requirements

- Vehicle title.
- Depreciation schedule (cost basis, prior depreciation).
- §274(d) mileage logs.
- Reimbursement records.
- Accountable plan documents.

## Common pitfalls / audit risks

- **Double-dipping.** Owner cannot claim depreciation personally
  AND receive depreciation reimbursement.
- **§280F coordination.** Limits must be applied.
- **Standard mileage rate vs. actual expense locked in.** Standard
  mileage rate in year 1 prevents actual-expense method later. The
  reimbursement method should be consistent.
- **Personal use creep.** Business-use percentage must be tracked
  and documented.

## Recent legislative changes

- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §168(k)
  100% bonus depreciation Pub L 119-21]`. If 100% bonus restored,
  significant impact on first-year reimbursement.

## State conformity considerations

State decoupling on §168(k) bonus requires state-level
adjustment.

## AICPA SSTS / Circular 230 considerations

Multi-step compliance with several failure points. Practitioner
should evaluate whether structure #1 (standard mileage rate) or #3
(corporation ownership) is simpler and produces similar economic
result.

## Default confidence band rationale

**MODERATE** — multiple compliance points; substance is sound but
execution is error-prone. Drops to LOW if §280F or substantiation
issues arise.

## Cross-references

- **`accountable-plan-home-office`** (#2).
- **`business-vehicle-usage`** (#4) — primary vehicle strategy.
- **`bonus-and-section-179-depreciation`** (#12).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 280F",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section280F",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 168",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section168",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.62-2",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    }
  ]
}
```
