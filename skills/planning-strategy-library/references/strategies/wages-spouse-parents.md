---
name: "Wages to Spouse, Non-Dependents, and Parents"
slug: wages-spouse-parents
type: Income Shifting
tax_type: EFR
complexity: Low
irc_sections: ["§162(a)(1)", "§3121"]
forms: ["W-2"]
state_specific: true
caution: true
confidence_default_band: MODERATE
last_obbba_review: "N/A"
---

> **Caution:** Wages to family members must reflect bona fide
> services and reasonable compensation. The IRS will challenge
> family employment lacking substance.

## Overview

Hiring spouse, parents, or other non-dependent family members in
a family business creates several distinct planning opportunities:

1. **Tax-bracket income shifting** — when family member is in
   lower bracket.

2. **§162 business deduction** — wages deductible to business;
   subject to §162(a)(1) reasonableness.

3. **HRA / §105 plan eligibility** — see `hra-merp` (#11). The
   classic structure: spouse employed by sole proprietor; family
   §105 HRA reimburses spouse for family medical costs.

4. **Spousal Roth IRA contribution** — spouse with earned income
   can contribute to own Roth IRA.

5. **Spousal retirement plan participation** — spouse-employee
   eligible for SEP-IRA, Solo 401(k), defined benefit, or qualified
   retirement plans of business.

6. **§3121 spouse FICA exemption** — for sole proprietorship
   only, spouse is generally NOT exempt from FICA (unlike children
   under 18). However, §3121(b)(3) exempts spouse-employed by sole
   prop from FUTA only (post-1988 amendment is limited; verify
   current rule).

7. **§3121(b) services on the farm** — limited family farm
   exemptions.

For elderly parents, hiring as employees can:
- Provide them income.
- Cover medical costs through §105 HRA.
- Qualify them for retirement plan participation.

## Primary IRC authority

- §162(a)(1) — Reasonable compensation deduction.
- §3121 — FICA wage definitions.
- §3121(b)(3)(B) — Spouse FUTA exemption (sole prop only).
- §3306(c)(5) — FUTA exemption.
- §219 — IRA contribution rules.

## Treasury regulations

- Reg §1.162-7 — Reasonable compensation.
- Reg §31.3121(b)(3)-1 — Family employment.

## Key IRS guidance

- IRS Publication 15.
- IRS Publication 535.

## Key court decisions

- **Albers v. Commissioner, T.C. Memo. 2007-144** — Bona fide
  spouse employment upheld.
- **Shellito v. Commissioner, 437 F.3d 1255 (10th Cir. 2006)** —
  Spouse employment denied for lack of substance.
- See cases under #21 reasonable compensation.

## Eligibility requirements

For §162 deduction:
1. Bona fide services performed.
2. Reasonable compensation for services.
3. Compliance with employment law (workers' compensation, state
   wage requirements).

For HRA / §105 plan:
1. Spouse is bona fide employee with documented duties.
2. §105 plan covers all employees (typically just spouse).
3. Plan reimburses spouse for family medical costs.

For spousal IRA:
1. Spouse has earned income from family business.
2. Annual contribution limit applies.

## Mechanics — how it works

1. **Document employment.** Job description; pay rate; hours;
   responsibilities.
2. **Pay reasonable wages.** Industry comparables.
3. **Issue W-2.** Withhold federal/state income tax and FICA
   (FICA generally applies to spouses).
4. **Establish §105 HRA** if applicable.
5. **Enroll in retirement plans** as employee.
6. **Document substance** through ongoing records.

## Documentation requirements

- Employment agreement / job description.
- Time records.
- Pay records.
- W-2.
- §105 plan documents (if applicable).
- Reasonable compensation analysis.

## Common pitfalls / audit risks

- **No actual services.** Spouse must do real work.
- **Excessive wages.** Reasonableness scrutinized.
- **§3121 confusion.** FICA generally applies to spouse wages
  (only specific FUTA exemption for sole prop).
- **§105(h) discrimination** if HRA structured unevenly.
- **Failure to file payroll tax returns.** Form 941 / 944 / W-2.

## Recent legislative changes

- No material recent changes.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA family
  employment Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State family employment rules vary; state workers' comp
requirements typically apply.

## Default confidence band rationale

**MODERATE** — fact-intensive substance requirement. HIGH for
substantive, well-documented spouse employment. LOW for token
arrangements.

## Cross-references

- `hiring-kids` (#49).
- `hra-merp` (#11) — primary partner strategy.
- `reasonable-comp-corp-owners` (#21).
- `roth-ira-contributions` (#79).
- `solo-401k-employer-contributions` (#82).
- `defined-benefit-cash-balance` (#73).
- `income-shifting-family-member` (#48).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 162(a)(1)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section162","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 3121(b)(3)(B)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section3121","weight":"primary_statute"},
    {"authority_type":"TaxCt","citation":"Albers v. Commissioner, T.C. Memo. 2007-144","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"CtAppeals","citation":"Shellito v. Commissioner, 437 F.3d 1255 (10th Cir. 2006)","url":"https://www.courtlistener.com","weight":"binding_circuit"}
  ]
}
```
