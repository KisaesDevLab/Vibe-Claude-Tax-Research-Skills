---
name: "Penalty Abatement (Comprehensive)"
slug: penalty-abatement
type: Personal - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§6651", "§6662", "§6664(c)", "§6707A", "§6699", "§6698"]
forms: ["Form 843", "Form 8857 (innocent spouse)"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

Comprehensive penalty abatement reference, expanding on #37 (FTA
and reasonable cause for §6651). This file addresses additional
penalty types and abatement mechanisms:

**§6662 Accuracy-Related Penalty (20%; 40% gross valuation):**
- Negligence or disregard of rules/regulations.
- Substantial understatement of income tax.
- Substantial valuation misstatement.
- Substantial overstatement of pension liabilities.
- Substantial estate/gift tax valuation understatement.
- Disallowance of treaty position without disclosure.
- Reasonable cause defense under §6664(c).

**§6707A Reportable Transaction Penalty:**
- Failure to disclose listed or reportable transaction on Form
  8886.
- $10,000 minimum / $50,000 maximum / $100,000 listed transactions.
- Limited reasonable cause defense.

**§6698 Failure to File Partnership Return:**
- $235 per partner per month (2024); maximum 12 months.
- Rev. Proc. 84-35 small partnership reasonable cause exception.

**§6699 Failure to File S Corp Return:**
- $235 per shareholder per month; max 12 months.
- Reasonable cause exception.

**§6694 Preparer Penalty:**
- Understatement due to unreasonable position.
- Reasonable cause defense and reasonable belief standard.

**§6701 Aiding and Abetting Penalty:**
- $1,000 / $10,000 (corp) per document.
- Limited abatement.

**Innocent Spouse Relief (§6015):**
- Three categories: §6015(b) traditional; §6015(c) separation of
  liability; §6015(f) equitable relief.
- Form 8857.

## Primary IRC authority

- §6651 — Failure to file/pay (see #37).
- §6662 — Accuracy-related penalty.
- §6662A — Listed transaction penalty.
- §6664(c) — Reasonable cause defense.
- §6694 — Preparer penalty.
- §6698 — Failure to file partnership return.
- §6699 — Failure to file S corp return.
- §6707A — Reportable transaction penalty.
- §6015 — Innocent spouse relief.
- §6404(e) — Interest abatement (see #37).

## Treasury regulations

- Reg §1.6662-1 through §1.6662-7.
- Reg §1.6664-1 through §1.6664-4.
- Reg §1.6707A-1.
- Reg §1.6015-1 through §1.6015-9.

## Key IRS guidance

- IRM 20.1 — Penalty Handbook (comprehensive).
- IRM 20.1.1.3.6.1 — First-Time Abate.
- Rev. Proc. 84-35 — Small partnership reasonable cause.

## Key court decisions

- **United States v. Boyle, 469 U.S. 241 (1985)** — Reliance on
  agent for filing not reasonable cause.
- **Klein v. Commissioner, 149 T.C. 341 (2017)** — Reasonable
  cause analysis.

## Mechanics — how it works

For §6662 penalty abatement:
1. **Identify category** of accuracy-related penalty.
2. **Reasonable cause and good faith** defense under §6664(c).
3. **Adequate disclosure** via Form 8275 / 8275-R may eliminate
   substantial understatement penalty even without reasonable
   cause.
4. **Form 843** with detailed statement.

For §6698 / §6699 partnership/S corp late filing:
1. **First-time abate** if eligible.
2. **Rev. Proc. 84-35 small partnership** — partnerships with ≤10
   partners; all partners filed timely; allocation per partnership
   agreement.
3. **Form 843** with reasonable cause explanation.

For innocent spouse:
1. **Form 8857.**
2. **Three categories** under §6015.
3. **2-year filing deadline** (generally) from first IRS collection
   activity.

## Documentation requirements

- Form 843 (most penalties) or Form 8857 (innocent spouse).
- Detailed reasonable cause statement.
- Supporting documentation.
- Compliance history (FTA eligibility).

## Common pitfalls / audit risks

- **§6662 reliance defense.** Reliance on tax advice from competent
  preparer can be reasonable cause IF preparer was given full
  facts.
- **§6707A no reasonable cause.** Listed transaction penalty has
  very limited reasonable cause defense; disclosure is the safe
  harbor.
- **Innocent spouse 2-year deadline.** Generally strict.
- **Adequate disclosure standard.** §6662(d)(2)(B) requires
  reasonable basis AND disclosure for substantial understatement
  protection.

## Recent legislative changes

- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA penalties
  Pub L 119-21]`. Working assumption: no major changes.

## State conformity considerations

States have parallel penalty regimes; abatement procedures vary.

## Default confidence band rationale

**HIGH** for FTA-eligible cases. **MODERATE** for reasonable cause
based on documentation.

## Cross-references

- `late-penalties-interest` (#37).
- `predict-reasonable-cause` (predict skill).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 6662","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section6662","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 6664(c)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section6664","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 6015","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section6015","weight":"primary_statute"},
    {"authority_type":"RevProc","citation":"Rev. Proc. 84-35","url":"https://www.irs.gov/irb","weight":"irs_published"},
    {"authority_type":"SCOTUS","citation":"United States v. Boyle, 469 U.S. 241 (1985)","url":"https://www.supremecourt.gov","weight":"binding_judicial"}
  ]
}
```
