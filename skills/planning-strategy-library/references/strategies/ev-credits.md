---
name: "Electric Vehicle Tax Credits (§30D, §25E, §45W)"
slug: ev-credits
type: Credit/Payment
tax_type: CREDIT
complexity: High
irc_sections: ["§30D", "§25E", "§45W"]
forms: ["Form 8936", "Schedule A of Form 8936", "Form 8910"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

The Inflation Reduction Act (IRA) of 2022 substantially overhauled
the EV credit framework. The current structure (subject to OBBBA
modifications):

1. **§30D Clean Vehicle Credit:** Up to $7,500 for new clean
   vehicles. Conditions:
   - **$3,750** for vehicles meeting critical minerals requirement
     (post-2024: 50%; rising annually).
   - **$3,750** for vehicles meeting battery components requirement
     (post-2024: 60%; rising annually).
   - Income limits: Modified AGI ≤$300K MFJ / $225K HoH / $150K
     single (lookback to either current or prior year, whichever
     better).
   - MSRP limits: $80K SUVs/trucks/vans; $55K cars.
   - Final assembly in North America.
   - Foreign Entity of Concern (FEOC) restrictions.
2. **§25E Used Clean Vehicle Credit:** Up to $4,000 (or 30% of
   purchase price, lesser of). Conditions:
   - Vehicle priced ≤$25,000.
   - Used by qualified taxpayer for first time.
   - Income limits: $150K MFJ / $112,500 HoH / $75K single.
3. **§45W Commercial Clean Vehicle Credit:** Up to $7,500 (light
   vehicles) or $40,000 (heavy vehicles >14,000 lbs GVWR). For
   business-use vehicles. No income or MSRP limits.

The credits became transferable to dealers at point of sale starting
2024 (§30D(g)(2)) — buyers can take credit as immediate purchase
discount rather than wait until tax filing.

OBBBA may have substantially modified or terminated EV credits.
Verify via Classification Tables.

## Primary IRC authority

- **§30D** — New Clean Vehicle Credit.
- **§30D(d)** — Critical minerals requirement.
- **§30D(e)** — Battery components requirement.
- **§30D(f)** — Income and MSRP limits.
- **§30D(g)** — Transfer to dealer election.
- **§25E** — Used Clean Vehicle Credit.
- **§45W** — Commercial Clean Vehicle Credit.

## Treasury regulations

- **Reg §1.30D-1 through §1.30D-6** — Final regulations issued
  2024.
- **Reg §1.25E-1** — Used clean vehicle.
- **Reg §1.45W-1** — Commercial clean vehicle.

## Key IRS guidance

- **Notice 2023-1** — Initial guidance on §30D after IRA.
- **Rev. Proc. 2023-33** — Dealer transfer mechanics.
- **Rev. Proc. 2024-26** — FEOC clarification.
- **IRS Fuel Economy and Environment Labels** — MSRP and
  classification.
- **DOE/EPA fueleconomy.gov** — Eligible vehicle list.

## Key court decisions

- Limited dispute area; relatively new framework.

## Eligibility requirements

For §30D (new vehicle):
1. New, qualifying clean vehicle.
2. Final assembly in North America.
3. Critical minerals + battery components requirements.
4. Income below threshold.
5. MSRP below threshold.
6. Transfer to dealer election (optional).

For §25E (used vehicle):
1. Vehicle ≥2 model years older than year of purchase.
2. Vehicle priced ≤$25,000.
3. First sale to qualified buyer.
4. Income below threshold.

For §45W (commercial):
1. Vehicle used in business.
2. Acquired for use, not resale.
3. Made by qualifying manufacturer.
4. No income/MSRP limits.

## Mechanics — how it works

1. **Pre-purchase verification.** Confirm vehicle qualifies
   (fueleconomy.gov; manufacturer documentation).
2. **Income lookback.** Use lower of current or prior year MAGI for
   §30D and §25E.
3. **Transfer election (if applicable).** Buyer transfers credit
   to dealer at point of sale; receives discount.
4. **Form 8936** with return.
5. **Recapture.** Vehicle ceasing to qualify or income exceeding
   threshold (post-purchase) may trigger recapture.

## Documentation requirements

- Manufacturer certification.
- VIN registration.
- Purchase agreement showing MSRP and final assembly.
- Form 8936 / 8936-A.
- Income documentation supporting threshold.

## Common pitfalls / audit risks

- **Critical minerals / battery components changes.** Annual
  thresholds increase; vehicle eligible in 2024 may not qualify in
  2025.
- **FEOC restrictions.** Vehicles with battery components from
  foreign entities of concern (post-2024 critical minerals; 2025
  battery) disqualify.
- **Income threshold.** Spouse income aggregation; current-year
  vs. prior-year lookback flexibility.
- **MSRP determination.** "Manufacturer's suggested retail price"
  is the key; not invoice price.
- **Transfer to dealer election** is irrevocable.
- **Recapture if ceased to qualify.**

## Recent legislative changes

- **IRA (2022)** — Created the modern §30D / §25E / §45W framework.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA EV credits
  §30D §25E §45W Pub L 119-21 classification table]`. Reports
  indicate significant OBBBA modifications, possibly including
  early termination, modified income limits, or expanded categories.
  This is one of the most consequential OBBBA verifications
  practitioners need to perform.

## State conformity considerations

State EV credits (CA Clean Vehicle Rebate Project, CO state
credits, etc.) may be additional or independent of federal.

## AICPA SSTS / Circular 230 considerations

EV credit changes are dynamic; practitioner should verify current-
year rules at time of advice. Income lookback and transfer-to-
dealer election require careful planning.

## Default confidence band rationale

**HIGH** for vehicles clearly meeting requirements. Drops to
MODERATE for borderline income, MSRP, or critical minerals/battery
component qualifications.

## Cross-references

- **`misc-tax-credits`** (#38).
- **`business-vehicle-usage`** (#4) — interaction with §45W.
- **`bonus-and-section-179-depreciation`** (#12) — interaction
  with depreciation.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 30D",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section30D",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 25E",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section25E",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 45W",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section45W",
      "weight": "primary_statute"
    },
    {
      "authority_type": "Notice",
      "citation": "Notice 2023-1",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    },
    {
      "authority_type": "RevProc",
      "citation": "Rev. Proc. 2023-33",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    }
  ]
}
```
