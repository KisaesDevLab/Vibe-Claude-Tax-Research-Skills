---
name: "Donor Advised Fund (DAF)"
slug: donor-advised-fund
type: Itemized Ded
tax_type: EFR
complexity: Low
irc_sections: ["§170", "§4966", "§4967"]
forms: ["Form 8283", "Schedule A"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

A Donor Advised Fund (DAF) is a charitable giving vehicle
administered by a §501(c)(3) sponsoring organization (typically a
community foundation or commercial entity like Fidelity Charitable,
Schwab Charitable, Vanguard Charitable). The donor:

1. **Contributes cash or appreciated property** to the DAF (treated
   as gift to public charity).
2. **Receives immediate §170 deduction** at FMV for appreciated
   long-term property (subject to 30% AGI limit) or up to 60% AGI
   for cash.
3. **Avoids capital gain** on appreciated property contributed.
4. **Recommends grants** to qualified charities over time.
5. **DAF assets grow tax-free.**

DAFs are particularly valuable for:
- **Tax-bunching strategy** — concentrate multiple years' giving
  into one year for itemizing benefit.
- **Year-end planning flexibility** — make deduction this year,
  decide grants later.
- **Privacy** — DAF can grant anonymously.
- **Investment management** — DAF invests assets pending grants.

DAF disadvantages:
- **No required distribution timeline** — can hold for decades.
- **Annual fees** — typically 0.6%-1.0% of assets.
- **Sponsoring organization controls** ultimate grant decisions
  (donor recommendations are advisory).
- **No reversion** — once contributed, assets cannot return to donor.

§4966 / §4967 impose restrictions:
- Grants from DAF must be to qualified §170(c) public charity.
- Grants providing substantial private benefit to donor or related
  party trigger excise tax.
- §4967 — prohibits grants that result in more-than-incidental
  benefit to donor.

## Primary IRC authority

- §170(a) — Charitable contribution deduction.
- §170(b) — AGI limits.
- §4966 — Excise tax on certain DAF distributions.
- §4967 — Excise tax on prohibited benefits.
- §509(a)(1)-(3) — Public charity status (DAF sponsor must be).
- §4943 — Excess business holdings (DAF prohibited from holding).

## Treasury regulations

- Reg §1.170A-1 through §1.170A-17.
- Reg §53.4966 (proposed; pending) — DAF distributions.

## Key IRS guidance

- **Notice 2017-73** — Anti-abuse rules for DAF distributions
  to satisfy donor's personal pledges.
- **Proposed Regulations REG-142338-07 (2023)** — DAF rules
  modernization.

## Key court decisions

- **Fairbairn v. Fidelity Investments Charitable Gift Fund, 5 F.4th
  1097 (9th Cir. 2021)** — DAF sponsor's discretion to ignore donor
  recommendations upheld; donor has no enforceable right.

## Eligibility requirements

For DAF contribution:
1. Gift to qualified §501(c)(3) sponsoring organization.
2. Substantiation per §170(f)(8) and (11).
3. Long-term holding for FMV deduction on appreciated property.

For DAF grants:
1. Recipient is §170(c) qualified public charity.
2. No more-than-incidental benefit to donor or related party.
3. Not used to satisfy donor's personal pledge.

## Mechanics — how it works

1. **Open DAF account.** Application with sponsoring organization.
2. **Contribute cash or appreciated property.** Brokerage transfer
   for stocks; deed for real estate; cash via check or wire.
3. **Receive acknowledgment letter** for §170 substantiation.
4. **Deduct on Schedule A** subject to AGI limits.
5. **Recommend grants** over time to qualified charities.
6. **DAF processes recommendations** (usually within 1-2 weeks).
7. **DAF invests assets** per donor's investment recommendation.

## Documentation requirements

- DAF acknowledgment letter (§170(f)(8)).
- Form 8283 if non-cash >$500.
- Qualified appraisal if non-cash >$5,000 (publicly-traded
  exception).
- Brokerage transfer / deed records.

## Common pitfalls / audit risks

- **Treating recommendation as binding pledge.** §4967 problem if
  DAF grant satisfies donor's personal pledge.
- **Personal benefit.** Grants providing more-than-incidental
  benefit to donor (e.g., tickets, dinners with substantial value)
  trigger §4967.
- **Bunching strategy missed.** Failure to coordinate giving with
  itemization threshold.
- **Substantiation errors.** Forgetting acknowledgment letter or
  appraisal.

## Recent legislative changes

- **Notice 2017-73** — DAF anti-abuse rules.
- **2023 Proposed Regs** — Modernization of DAF rules.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA DAF §4966
  Pub L 119-21]`. Working assumption: no major DAF changes.

## State conformity considerations

State conformity to §170 generally complete.

## Default confidence band rationale

**HIGH** — DAFs are well-established charitable vehicle with clear
statutory framework.

## Cross-references

- `charitable-donation-appreciated` (#51).
- `charitable-planning` (#53).
- `qcd` (#78) — alternative for IRA owners.
- `gifting-stock` (#46).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 170","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section170","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 4966","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section4966","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 4967","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section4967","weight":"primary_statute"},
    {"authority_type":"Notice","citation":"Notice 2017-73","url":"https://www.irs.gov/irb","weight":"irs_published"},
    {"authority_type":"CtAppeals","citation":"Fairbairn v. Fidelity Investments Charitable Gift Fund, 5 F.4th 1097 (9th Cir. 2021)","url":"https://www.courtlistener.com","weight":"binding_circuit"}
  ]
}
```
