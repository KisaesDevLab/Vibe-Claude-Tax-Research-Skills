---
name: "Business Vehicle Usage — Self-Employed"
slug: business-vehicle-self-employed
type: SE Tax
tax_type: EFR
complexity: Medium
irc_sections: ["§162", "§168", "§179", "§280F", "§274(d)"]
forms: ["Schedule C", "Form 4562"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Self-employed business vehicle deduction parallels #4 (corporate
context) but with Schedule C mechanics. Two methods:

**Standard Mileage Rate Method (2024: 67¢/mile business):**
- Apply rate × business miles.
- Includes implicit depreciation; cannot also depreciate vehicle.
- Year-1 election locks in for vehicle's life (with limited
  exceptions).
- Simpler; no vehicle expense tracking.

**Actual Expense Method:**
- Track all vehicle expenses (gas, oil, maintenance, insurance,
  registration).
- Apply business-use percentage.
- Depreciation per §168 / §179 / §168(k).
- §280F luxury auto cap if light passenger auto ≤6,000 lbs GVWR.
- Heavy SUV (>6,000 lbs) escapes §280F cap; full §179 / §168(k)
  bonus available.

Strategic considerations:
- **Heavy SUV strategy** — vehicles >6,000 lbs GVWR escape §280F;
  immediate §179 expensing up to $30,500 (2024 SUV limit) plus
  remaining basis at §168(k) bonus rate.
- **OBBBA 100% bonus restoration** — if confirmed, full
  first-year deduction on heavy SUV.
- **Standard mileage simplicity** — for low-cost vehicles or low
  business mileage.
- **Year-1 method election** — affects vehicle's deductibility
  for life.

§274(d) substantiation:
- **Mileage log:** date, destination, business purpose, miles.
- **Contemporaneous** preferred; reconstructed records routinely
  rejected.
- **Apps:** MileIQ, Everlance acceptable if used contemporaneously.

## Primary IRC authority

- §162 — Trade or business expenses.
- §168 — MACRS.
- §168(k) — Bonus depreciation.
- §179 — Expensing.
- §280F — Luxury auto cap.
- §274(d) — Substantiation.

## Treasury regulations

- Reg §1.162-2.
- Reg §1.168-1 through §1.168(k)-2.
- Reg §1.280F-1T through §1.280F-7.
- Reg §1.274-5T.

## Key IRS guidance

- Rev. Proc. 2019-46 — Standard mileage.
- Annual Rev. Proc. on §280F luxury auto caps.
- IRS Publication 463 — Travel, Gift, and Car Expenses.

## Eligibility requirements

For deduction:
1. Vehicle used in business activity.
2. §274(d) substantiation.
3. Method election (standard mileage or actual).

## Mechanics — how it works

1. **Track business use percentage.**
2. **Choose method:**
   - Standard Mileage: 67¢/mile (2024) × business miles.
   - Actual Expense: total expenses × business use %.
3. **Year-1 election** is significant — affects future years.
4. **Form 4562** for depreciation (actual method).
5. **§280F cap** for light passenger auto.
6. **Heavy SUV §179.**
7. **Schedule C deduction.**

## Documentation requirements

- Mileage log (contemporaneous).
- Vehicle records (purchase, financing, repairs, insurance).
- Form 4562 (actual method).
- Title and registration.

## Common pitfalls / audit risks

- **Inadequate mileage logs.** §274(d) is unforgiving.
- **Personal use creep.** Reduces business %.
- **Standard vs. actual lock-in.** Year-1 election affects vehicle's
  life.
- **§280F luxury auto cap miscalculation.**
- **Heavy SUV vs. light vehicle.** GVWR distinction critical.
- **State decoupling on §168(k) bonus.** Track state separately.
- **§179 carryforward.** Section 179 cannot create loss; carries
  forward.

## Recent legislative changes

- **TCJA (2017)** — Used vehicles eligible for §168(k); QIP fix
  later.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §168(k)
  100% bonus Pub L 119-21]`. 100% bonus restoration significantly
  affects this strategy.

## State conformity considerations

State decoupling on §168(k) bonus widely. State auto deduction
rules vary.

## Default confidence band rationale

**HIGH** for properly-documented vehicles. Drops to MODERATE for
borderline business-use percentages or §274(d) substantiation
issues.

## Cross-references

- `business-vehicle-usage` (#4) — corporate context.
- `bonus-and-section-179-depreciation` (#12).
- `bonus-179-depreciation-self-employed` (#89).
- `accountable-plan-self-employed` (#84).
- `reimbursement-depreciation-s-corp-vehicle` (#23).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 162","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section162","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 280F","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section280F","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 179","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section179","weight":"primary_statute"},
    {"authority_type":"RevProc","citation":"Rev. Proc. 2019-46","url":"https://www.irs.gov/irb","weight":"irs_published"}
  ]
}
```
