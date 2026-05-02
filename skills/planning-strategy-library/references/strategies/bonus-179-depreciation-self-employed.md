---
name: "Bonus / §179 Depreciation — Self-Employed Maximization"
slug: bonus-179-depreciation-self-employed
type: SE Tax
tax_type: EFR
complexity: Medium
irc_sections: ["§168", "§168(k)", "§179", "§280F"]
forms: ["Form 4562", "Schedule C"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Self-employed application of bonus depreciation and §179 expensing
parallels corporate context (#12) but with Schedule C mechanics
and unique self-employment considerations:

1. **§179 election limited to net business income.** Cannot create
   or increase Schedule C loss.
2. **§168(k) bonus has NO income limit** — can create loss.
3. **§461(l) excess business loss** — limits net business loss
   to threshold ($305K single / $610K MFJ for 2024); excess becomes
   NOL.
4. **SE tax interaction** — depreciation reduces Schedule C net
   profit, reducing both income tax base AND SE tax base.

OBBBA reportedly restored 100% bonus depreciation. Verify via
Classification Tables.

Self-employed strategic considerations:
- **Heavy SUV strategy** — vehicles >6,000 lbs GVWR escape §280F;
  $30,500 §179 (2024 SUV limit) plus remaining basis at §168(k)
  bonus.
- **Equipment purchases** — §179 first up to net income; §168(k)
  bonus on remainder.
- **§263A UNICAP** for inventory production.
- **De minimis safe harbor (#28)** for items under threshold.

## Primary IRC authority

- §168 — MACRS.
- §168(k) — Bonus depreciation.
- §179 — Expensing election.
- §179(b)(3) — Income limitation.
- §280F — Luxury auto cap.
- §461(l) — Excess business losses.
- §263A — UNICAP.

## Treasury regulations

- Reg §1.168(k)-2 — Bonus depreciation.
- Reg §1.179-1 through §1.179-6.
- Reg §1.263(a)-1, -2, -3 — Tangible property regs.
- Reg §1.461-1 — Timing.

## Key IRS guidance

- Rev. Proc. 2019-08, 2019-13 — §168(k) procedural.
- Rev. Proc. 2020-25 — QIP CARES Act fix.
- IRS Publication 946 — How to Depreciate Property.

## Eligibility requirements

For §168(k) bonus:
1. Tangible property class life ≤20 years.
2. Acquired and placed in service after applicable date.
3. NOT acquired from related party.

For §179:
1. Tangible §1245 property (including off-the-shelf software).
2. Limited categories of §1250 (real property).
3. Acquired by purchase from unrelated party.
4. Election made on Form 4562.
5. Subject to §179(b)(3) taxable income limit.

## Mechanics — how it works

1. **Identify capital expenditures.**
2. **Apply tangible property regulations** (capitalize vs.
   expense).
3. **De minimis safe harbor** for items under threshold.
4. **§179 first** up to net business income limit.
5. **§168(k) bonus** on remainder.
6. **§280F limit** for light passenger autos.
7. **§461(l) excess business loss** — net loss limited to threshold.
8. **State decoupling** — track separately for major decoupling
   states.
9. **Form 4562.**

## Documentation requirements

- Asset acquisition records.
- Placed-in-service dates.
- Form 4562.
- For SUVs: GVWR documentation.

## Common pitfalls / audit risks

- **§179 income limit.** Cannot create loss; carryforward.
- **§168(k) bonus + §461(l).** Bonus can create loss but
  §461(l) limits net business loss.
- **Related-party acquisition.** §168(k) excluded.
- **Placed in service before year end.** Must be ready and
  available for use.
- **State decoupling.** CA, NY, NJ, MA, MD, MN, PA require
  add-back.
- **§280F luxury auto.** Light passenger autos capped.

## Recent legislative changes

- **TCJA (2017)** — Used property eligible; §179 expansion.
- **CARES Act (2020)** — QIP fix.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §168(k)
  100% bonus Pub L 119-21]`. Restoration significantly increases
  benefit.

## State conformity considerations

Major decoupling states require state add-back tracking.

## Default confidence band rationale

**HIGH** — clear statutory framework.

## Cross-references

- `bonus-and-section-179-depreciation` (#12) — corporate context.
- `business-vehicle-self-employed` (#85).
- `de-minimis-safe-harbor` (#28).
- `de-minimis-safe-harbor-self-employed` (#93).
- `cost-segregation-extended` (#41).
- `nol-carryback-carryforward` (#15).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 168(k)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section168","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 179","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section179","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 461(l)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section461","weight":"primary_statute"}
  ]
}
```
