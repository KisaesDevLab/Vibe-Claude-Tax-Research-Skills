---
name: "Hiring Kids — Self-Employed (Sole Prop / Partnership) Variant"
slug: hiring-kids-self-employed
type: SE Tax
tax_type: EFR
complexity: Medium
irc_sections: ["§3121(b)(3)(A)", "§162", "§3306(c)(5)", "§3401(a)(4)"]
forms: ["W-2", "Schedule C / 1065"]
state_specific: true
caution: true
confidence_default_band: MODERATE
last_obbba_review: "N/A"
---

> **Caution:** This strategy is subject to the same fact-intensive
> substance requirements as #49 (corporate context). Wages must be
> for bona fide work performed at reasonable compensation, with
> contemporaneous documentation. Eller and Denman cases established
> the standard. Family employment lacking substance is denied.

## Overview

Self-employed variant of hiring kids strategy (#49), with the
critical advantage of §3121(b)(3) FICA exemption applying to
children under 18 employed by parent's:

1. **Sole proprietorship** (Schedule C), OR
2. **Partnership where ALL partners are parents** (single set of
   parents).

The FICA exemption produces these benefits stacked together:

1. **Child receives W-2 wages** taxed at child's bracket (typically
   0% up to standard deduction $14,600 for 2024).
2. **No FICA** on those wages (15.3% savings vs. corporate or
   non-qualifying structure).
3. **No FUTA** on wages to children under 21 (§3306(c)(5)).
4. **Sole prop / partnership deducts wages** on Schedule C / Form
   1065 — reducing both income tax base AND SE tax base.
5. **Child can fund Roth IRA** up to lesser of earned income or
   $7,000 (2024).

Combined effect: parent shifts $14,600 to child at 0% bracket;
parent saves SE tax (15.3%) on full $14,600 (because Schedule C
profit reduced); $14,600 funds Roth IRA for child.

§3121(b)(3) FICA exemption does NOT apply to:
- Children employed by parent-owned C corporation.
- Children employed by parent-owned S corporation.
- Children employed by partnership where any partner is not the
  child's parent.
- Children of a single member LLC taxed as a corporation.

For LLC: default partnership treatment (multi-member) or
disregarded entity (single-member with parent as sole owner) — both
qualify for §3121(b)(3) FICA exemption when child is employed by
parent.

## Primary IRC authority

- §3121(b)(3)(A) — FICA exemption for child under 18 employed by
  parent in unincorporated business.
- §3306(c)(5) — FUTA exemption (under 21).
- §3401(a)(4) — Income tax withholding exemption (limited).
- §162 — Trade or business expense.
- §1402 — SE tax (interaction).
- §1(g) — Kiddie tax (does NOT apply to earned income).

## Treasury regulations

- Reg §31.3121(b)(3)-1 — FICA family employment.
- Reg §31.3306(c)(5)-1 — FUTA family employment.
- Reg §1.162-7 — Reasonable compensation.

## Key IRS guidance

- IRS Publication 15 — Employer's Tax Guide.
- IRS Publication 51 — Agricultural Employer's Tax Guide.
- IRS Publication 334 — Tax Guide for Small Business.

## Key court decisions

- **Eller v. Commissioner, 77 T.C. 934 (1981)** — Wages to child
  must be reasonable.
- **Denman v. Commissioner, 48 T.C. 439 (1967)** — Family employment
  must reflect actual services.

## Eligibility requirements

For §162 deduction:
1. Bona fide work performed.
2. Reasonable compensation.
3. Compliance with child labor laws.
4. Documentation.

For §3121(b)(3) FICA exemption:
1. Child under age 18.
2. Employed by parent's sole proprietorship OR partnership where
   ALL partners are parents.
3. Does NOT apply to corporation (C or S) or LLC taxed as
   corporation.

## Mechanics — how it works

1. **Identify legitimate work** appropriate for child's age.
2. **Establish work agreement.** Job description, hourly rate, pay
   schedule.
3. **Track hours and tasks** contemporaneously.
4. **Pay wages on regular schedule.** Direct deposit or check.
5. **§3121(b)(3) FICA exemption** applies to sole prop / parent-only
   partnership.
6. **W-2 issued at year-end.** With FICA boxes (Box 3, 5)
   appropriately blank or zero for FICA-exempt wages.
7. **Child files own return** if required.
8. **Roth IRA contribution** funded by child or parent up to earned
   income / annual limit.

## Documentation requirements

- Job description and work agreement.
- Time records (contemporaneous).
- Pay records (direct deposit confirmations, canceled checks).
- W-2 issued with proper Box 3, 5 treatment for FICA-exempt wages.
- Records establishing reasonableness.
- State child labor law compliance.

## Common pitfalls / audit risks

- **No actual work** (Eller/Denman pattern).
- **Unreasonable compensation.**
- **Reconstructed time records.**
- **Corporation employment.** §3121(b)(3) FICA exemption does NOT
  apply; common error.
- **LLC taxed as corporation.** Same — FICA exemption lost.
- **Multi-member partnership with non-parent partner.** FICA
  exemption lost.
- **State child labor law violation.**
- **Withholding errors.** Federal income tax may be required.
- **W-2 vs. 1099.** Children should be W-2 employees; FICA
  exemption applies to W-2 only.
- **Spouse-as-non-parent partnership.** If business structured as
  partnership with spouse, all partners are parents and exemption
  preserved.

## Recent legislative changes

- No material recent changes.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §3121
  family employment Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity to §3121 family employment exemption varies.
State child labor laws layer additional restrictions.

## AICPA SSTS / Circular 230 considerations

Family employment is fact-intensive. Practitioner should: verify
work substance; document reasonableness; advise on child labor law
compliance; recommend Form W-2 (not 1099) for clarity.

## Default confidence band rationale

**MODERATE** — fact-intensive. HIGH for properly-documented,
reasonable, substantive employment. LOW for token employment of
young children with high pay and minimal documented work.

## Cross-references

- `hiring-kids` (#49) — corporate context.
- `wages-spouse-parents` (#50).
- `roth-ira-contributions` (#79).
- `income-shifting-family-member` (#48).
- `reasonable-comp-corp-owners` (#21).
- `hra-merp` (#11) — interaction with family HRA structures.
- `minimize-self-employment-tax` (#90).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 3121(b)(3)(A)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section3121","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 162(a)(1)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section162","weight":"primary_statute"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 31.3121(b)(3)-1","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"},
    {"authority_type":"TaxCt","citation":"Eller v. Commissioner, 77 T.C. 934 (1981)","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"TaxCt","citation":"Denman v. Commissioner, 48 T.C. 439 (1967)","url":"https://www.ustaxcourt.gov","weight":"judicial"}
  ]
}
```
