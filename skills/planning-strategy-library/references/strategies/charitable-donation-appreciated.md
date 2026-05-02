---
name: "Charitable Donation of Appreciated Assets"
slug: charitable-donation-appreciated
type: Itemized Ded
tax_type: EFR
complexity: Medium
irc_sections: ["§170", "§170(b)", "§170(e)"]
forms: ["Form 8283", "Schedule A"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Donating long-term appreciated property to qualified charitable
organizations produces a powerful tax benefit:

1. **Deduct FMV** of donated property under §170.
2. **Avoid capital gain tax** on appreciation (gain not realized).
3. **Charity receives full FMV** — sells without tax (§501(c)(3)
   exempt).

The structure works only for **long-term capital gain property**
(held >1 year). Short-term property is limited to basis under
§170(e)(1)(A). Ordinary income property (inventory, depreciable
business property recapture portions, art created by donor) is
also limited to basis.

AGI limitations under §170(b) (post-TCJA / post-OBBBA):
- **Cash to public charity:** 60% of AGI.
- **Long-term capital gain property to public charity:** 30% of
  AGI (FMV deduction).
- **Long-term capital gain property to private non-operating
  foundation:** 20% of AGI; FMV deduction generally limited to
  publicly-traded securities; otherwise basis.
- **Cash to private foundation:** 30% of AGI.

Excess carries forward 5 years.

Common applications:
- Appreciated publicly-traded stock to public charities.
- Appreciated real estate (with qualified appraisal).
- Closely-held business stock (with appraisal; limited deductibility
  if >50% of stock retained).
- Tangible personal property (related-use rule: full FMV only if
  used by charity in its exempt function; otherwise basis).

## Primary IRC authority

- §170(a) — Charitable contribution deduction allowed.
- §170(b) — Percentage limits.
- §170(c) — Qualified charitable organizations.
- §170(e) — Reduction of deduction for ordinary income / short-
  term property.
- §170(f)(8) — Substantiation: contemporaneous written acknowledgment
  for $250+.
- §170(f)(11) — Appraisal requirements for property >$5,000.
- §170(f)(16) — Special rule for property contributed to
  conservation purposes.
- §170(f)(17) — Bank record / written communication for cash <$250.
- §170(f)(18) — Recapture rule.
- §1011(b) — Bargain sale to charity.

## Treasury regulations

- Reg §1.170A-1 through §1.170A-17 — Comprehensive charitable
  contribution rules.
- Reg §1.170A-13 — Substantiation.
- Reg §1.170A-16 — Substantiation of charitable contributions of
  property.

## Key IRS guidance

- IRS Publication 526 — Charitable Contributions.
- IRS Publication 561 — Determining the Value of Donated Property.
- Form 8283 instructions.

## Key court decisions

- **Hewitt v. Commissioner, 109 T.C. 258 (1997), aff'd, 166 F.3d
  332 (4th Cir. 1998)** — Conservation easement charitable
  contribution requirements.
- **Pankratz v. Commissioner, 64 T.C. 924 (1975)** — Tangible
  personal property valuation.
- **Estate of Halby v. Commissioner, T.C. Memo. 2009-204** —
  Donor's basis when retaining interest.

## Eligibility requirements

1. **Qualified charitable organization** under §170(c).
2. **Long-term holding period** (>1 year) for FMV deduction.
3. **Substantiation:**
   - Contemporaneous written acknowledgment for $250+.
   - Form 8283 Section A for $501-$5,000.
   - Form 8283 Section B + qualified appraisal for >$5,000
     (publicly-traded securities exception).
4. **AGI limit not exceeded** (excess carries forward).
5. **Itemize on Schedule A** (no above-the-line; eliminated post-2021).

## Mechanics — how it works

1. **Identify long-term appreciated property.**
2. **Verify charity is §170(c) qualified.**
3. **Transfer property** before sale.
   - Publicly-traded stock: brokerage transfer.
   - Real estate: deed transfer.
   - Closely-held: stock certificate; subject to redemption rules
     (Rev. Rul. 78-197).
4. **Charity sells (typically tax-free under §501).**
5. **Substantiate.** Acknowledgment letter from charity; Form 8283
   if applicable; appraisal if >$5,000.
6. **Deduct FMV** on Schedule A subject to AGI limits.

## Documentation requirements

- Charity acknowledgment letter (must be received before earlier
  of return filing or due date).
- Form 8283 Section A or B as applicable.
- Qualified appraisal for property >$5,000 (with publicly-traded
  exception).
- Brokerage transfer records / deed.
- Charity §170(c) status (IRS Tax Exempt Organization Search).

## Common pitfalls / audit risks

- **Sell first, donate proceeds.** Triggers capital gain;
  defeats FMV deduction.
- **Short-term property.** Limited to basis.
- **Inadequate substantiation.** Single largest issue. §170(f)(8)
  contemporaneous written acknowledgment is unforgiving.
- **No appraisal for >$5,000.** Disallows entire deduction.
- **Tangible personal property without related use.** Basis only.
- **Ordinary income property.** Inventory, art created by donor,
  depreciation recapture portion — limited to basis.
- **Private foundation rules.** 20% / 30% limits and basis
  limitations.
- **Pre-arranged sale.** Charity bound to sell at predetermined
  price triggers anticipatory assignment of income.
- **Quid pro quo.** Donor receiving substantial benefit reduces
  deduction.

## Recent legislative changes

- **CARES Act / CAA 2021 (2020-2021)** — Temporary $300/$600
  above-the-line cash deduction (now expired).
- **CARES Act 100% AGI limit** for cash to public charity (now
  reverted to 60%).
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §170
  Pub L 119-21]`. Working assumption: standard percentage limits
  preserved.

## State conformity considerations

State conformity to §170 generally complete. **California**
allows charitable deduction; some states (TX, FL, etc.) have no
state income tax so deduction not relevant.

## AICPA SSTS / Circular 230 considerations

Substantiation discipline is critical. Practitioner should verify
acknowledgment letters, appraisals, and §170(c) charity status.

## Default confidence band rationale

**HIGH** for properly-substantiated gifts of long-term appreciated
property. Drops to MODERATE for valuation issues or related-use
determinations on tangible personal property.

## Cross-references

- `gifting-stock` (#46).
- `donor-advised-fund` (#54).
- `charitable-planning` (#53).
- `qcd` (#78) — IRA-based alternative.
- `family-limited-partnership` (#55) — interaction with charitable
  planning.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 170","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section170","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 170(e)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section170","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 170(f)(11)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section170","weight":"primary_statute"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.170A-13","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"}
  ]
}
```
