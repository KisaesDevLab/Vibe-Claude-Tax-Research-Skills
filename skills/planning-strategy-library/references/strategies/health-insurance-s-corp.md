---
name: "Health Insurance for S Corporation 2%+ Shareholders"
slug: health-insurance-s-corp
type: Business - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§162(l)", "§1372", "§3121(a)(2)(B)"]
forms: ["Form W-2 (Box 1 inclusion)", "Form 1040 above-the-line §162(l) deduction"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

The S corporation 2%+ shareholder health insurance treatment is one
of the most frequently mishandled compliance items in small-business
tax preparation. The rules are statutory and the IRS guidance is
clear, but the treatment differs from W-2 employee health insurance
in counterintuitive ways:

1. The S corporation pays the premium (or reimburses the
   shareholder under Notice 2008-1 procedures).
2. The premium is included in the 2%+ shareholder-employee's W-2
   Box 1 (federal wages) but **excluded** from Box 3 (Social
   Security wages) and Box 5 (Medicare wages).
3. The shareholder-employee then deducts the premium above-the-line
   on Form 1040 under §162(l), eliminating the federal income tax
   impact.
4. The S corporation deducts the premium as compensation under §162.

Net result: federal income tax is zero (W-2 inclusion offset by
§162(l) deduction); FICA is saved on both employer and employee
sides because the premium is excluded from Box 3 and Box 5; state
income tax treatment varies by state.

The strategy works because §1372 treats 2%+ S corporation
shareholder-employees as partners for fringe benefit purposes,
denying them §106 exclusion. But §162(l) gives self-employed
individuals (including 2%+ S corp shareholders per §1372) an
above-the-line deduction for health insurance.

## Primary IRC authority

- **§1372** — 2%+ S corp shareholders treated as partners for fringe
  benefit purposes.
  https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1372
- **§162(l)** — Self-employed health insurance deduction
  (above-the-line on Schedule 1 of Form 1040).
- **§3121(a)(2)(B)** — Exclusion of payments under §106 from
  Social Security wages (and corresponding exclusion under
  §3306(b)(2) for FUTA and §3401(a) for income tax withholding —
  but income tax inclusion under §162 compensation treatment for
  shareholder-employees).
- **§106** — Employer-provided health coverage exclusion (does NOT
  apply to 2%+ S corp shareholders due to §1372).

## Treasury regulations

- **Reg §1.162(l)-1** — Self-employed health insurance deduction
  rules.
- **Reg §31.3121(a)(2)-1** — Social Security wage exclusion for
  payments under §106.

## Key IRS guidance

- **Notice 2008-1** — Specific S corporation health insurance
  rules. Provides the procedural framework and confirms the W-2
  inclusion / §162(l) deduction structure.
  https://www.irs.gov/irb/2008-02_IRB
- **Rev. Rul. 91-26** — Treatment of S corporation shareholder
  health insurance as compensation.
- **Announcement 92-16** — Additional S corp shareholder health
  insurance guidance.
- **Chief Counsel Advice 200912059** — Detailed application of
  Notice 2008-1.

## Key court decisions

- **Swope v. Commissioner, T.C. Memo. 1985-516** — S corp
  shareholder denied §106 exclusion.
- **Gulley v. Commissioner, T.C. Memo. 1995-122** — Failure to
  include premium in W-2 defeated §162(l) deduction (statutory
  conditioning).

## Eligibility requirements

1. **Shareholder owns more than 2% of S corporation stock** at any
   time during the taxable year. §1372(b).
2. **Premium paid by S corporation** OR **paid by shareholder and
   reimbursed by S corporation** under a plan established by the
   corporation. Notice 2008-1.
3. **Premium included in W-2 Box 1** of the shareholder-employee
   for the year. Without W-2 inclusion, no §162(l) deduction is
   available. Notice 2008-1.
4. **Plan established by the S corporation.** Notice 2008-1
   originally required premiums paid in name of corporation;
   subsequent guidance allows premiums in name of shareholder if
   corporation reimburses.
5. **§162(l) limits.** Deduction limited to earned income from the
   S corporation (the shareholder's W-2 compensation from that
   corporation). Cannot exceed corporation-derived earned income.

## Mechanics — how it works

1. **Adopt the plan.** Corporate resolution confirming health
   insurance plan covering 2%+ shareholders.
2. **Pay or reimburse premiums during the year.** Either
   corporation pays carrier directly or shareholder pays and
   submits for reimbursement.
3. **Year-end W-2 preparation.** Add total annual premium to Box 1.
   Do NOT add to Box 3 (Social Security wages) or Box 5 (Medicare
   wages). Box 14 commonly used to disclose the amount.
4. **Form 1040 preparation.** Shareholder claims §162(l) deduction
   on Schedule 1 line 17 (above-the-line). Deduction limited to
   earned income from corporation.
5. **State considerations.** Most states follow federal treatment;
   some (Pennsylvania historically) had unique rules.

## Documentation requirements

- Corporate resolution adopting plan.
- Insurance policy or carrier statements.
- If reimbursement structure: receipts and reimbursement records.
- W-2 prepared with proper Box 1 inclusion and Box 3/5 exclusion.
- Schedule 1 supporting §162(l) calculation.

## Common pitfalls / audit risks

- **Failure to include premium in W-2 Box 1.** Without inclusion,
  §162(l) deduction is denied per Notice 2008-1. Common error.
- **Inclusion in Box 3 and Box 5.** Costs FICA unnecessarily.
- **Coverage for shareholder-employee less than 2%.** Such
  shareholders are W-2 employees and §106 exclusion applies; do
  NOT include in Box 1.
- **Ineligibility for spouse coverage.** §162(l) covers the
  shareholder, spouse, and dependents.
- **Family attribution.** §1372 attributes ownership: a 2%+
  shareholder's spouse, children, parents, and grandparents are
  also treated as 2%+ shareholders if any family member is.
- **§162(l) earned income limit.** Deduction cannot exceed earned
  income from the corporation. Insufficient W-2 wages means
  some premium is non-deductible.
- **Coordination with §125 cafeteria plan.** 2%+ shareholders are
  ineligible for §125 plans (statutory). Common error to allow
  pre-tax election.

## Recent legislative changes

- No material recent changes; the framework has been stable since
  Notice 2008-1.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §1372 §162(l)
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity to §162(l) is generally complete. **California**
has historically followed §162(l). **Pennsylvania** has unique S
corporation income treatment but generally conforms to §162(l).
Verify state stub for SALT details.

## AICPA SSTS / Circular 230 considerations

Standard practitioner diligence. The most common error — omitting
W-2 inclusion — creates a real compliance exposure. Practitioner
should review every 2%+ S corp shareholder's W-2 for proper
inclusion at year-end.

## Default confidence band rationale

**HIGH** — explicit statutory framework (§1372, §162(l)) and clear
IRS guidance (Notice 2008-1). Drops to MODERATE only when
shareholder ownership is borderline 2% (family attribution issues)
or earned income limitation creates partial deduction situations.

## Cross-references

- **`group-health-insurance`** (#8) — non-2%+-shareholder
  treatment.
- **`hra-merp`** (#11) — alternative reimbursement structure.
- **`health-insurance-self-employed`** (#87) — sole proprietor /
  partner variant.
- **`reasonable-comp-corp-owners`** (#21) — interaction with
  reasonable compensation analysis.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 1372",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1372",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 162(l)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section162",
      "weight": "primary_statute"
    },
    {
      "authority_type": "Notice",
      "citation": "Notice 2008-1",
      "url": "https://www.irs.gov/irb/2008-02_IRB",
      "weight": "irs_published"
    },
    {
      "authority_type": "RevRul",
      "citation": "Rev. Rul. 91-26",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    }
  ]
}
```
