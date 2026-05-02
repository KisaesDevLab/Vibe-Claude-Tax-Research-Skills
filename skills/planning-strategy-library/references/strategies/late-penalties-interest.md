---
name: "Late Filing / Late Payment Penalty and Interest Management"
slug: late-penalties-interest
type: Credit/Payment
tax_type: CREDIT
complexity: Medium
irc_sections: ["§6651", "§6601", "§6404", "§6664(c)"]
forms: ["Form 843 (penalty abatement claim)"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

This strategy addresses penalty and interest management — primarily
penalty abatement and interest reduction — when taxpayers find
themselves with late-filed or late-paid returns. The mechanisms:

1. **First-time abatement (FTA)** under IRM 20.1.1.3.6.1: One-time
   abatement of certain failure-to-file, failure-to-pay, and
   failure-to-deposit penalties for taxpayers with clean compliance
   history (3 prior tax years with no penalties; current
   filing/payment compliance).
2. **Reasonable cause** under §6651(a)(1) and §6664(c): Penalties
   abated for "reasonable cause and not willful neglect."
3. **Interest abatement under §6404(e):** Interest on tax may be
   abated if attributable to "ministerial or managerial" delay by
   the IRS. Limited to delays in IRS performance, not initial
   determinations.
4. **§6601 interest accrual:** Interest on underpayments at
   federal short-term rate plus 3% (small business C corps and
   underpayments above $100K large corporate underpayment use
   different rates).

The §6651 penalties:
- **§6651(a)(1) failure to file:** 5% per month, max 25%, of unpaid
  tax.
- **§6651(a)(2) failure to pay:** 0.5% per month, max 25%, of unpaid
  tax. Reduces failure-to-file by failure-to-pay during overlapping
  months.
- **§6651(a)(3) failure to pay assessment:** 0.5% per month, max
  25%, after notice of assessment.

The §6662 accuracy-related penalties (20% generally, 40% for
gross valuation overstatements) are addressed in `predict-reasonable-
cause` (predict skill) and `penalty-abatement` (#66).

## Primary IRC authority

- **§6651** — Failure to file return or pay tax.
- **§6601** — Interest on underpayment.
- **§6404** — Abatements (interest).
- **§6404(e)** — Interest abatement for IRS error or delay.
- **§6664(c)** — Reasonable cause defense to accuracy penalty.

## Treasury regulations

- **Reg §301.6651-1** — Failure to file or pay.
- **Reg §301.6404-2** — Interest abatement.

## Key IRS guidance

- **IRM 20.1** — Penalty Handbook.
- **IRM 20.1.1.3.6.1** — First-Time Abate (FTA).
- **Rev. Proc. 84-35** — Small partnership failure to file
  reasonable cause.
- **IRS Penalty Relief Information**:
  https://www.irs.gov/payments/penalty-relief

## Key court decisions

- **United States v. Boyle, 469 U.S. 241 (1985)** — Reliance on
  attorney/CPA to file is NOT reasonable cause for late filing
  (taxpayer's nondelegable duty).
- **In re Carlson, 126 F.3d 915 (7th Cir. 1997)** — Reasonable
  cause analysis.

## Eligibility requirements

For first-time abate (FTA):
1. Penalty is failure to file, failure to pay, or failure to
   deposit.
2. No penalty assessed in prior 3 tax years (penalty-free history).
3. Currently filed (or filed extension) and paid (or arranged
   payment).

For reasonable cause:
1. Taxpayer exercised "ordinary business care and prudence" but
   was nevertheless unable to file or pay on time.
2. Documented circumstances: serious illness, death, natural
   disaster, records destruction, IRS/postal delays, reliance on
   CPA for substantive tax position (NOT for filing).
3. Boyle limit: reliance on agent for filing alone is not
   reasonable cause.

For §6404(e) interest abatement:
1. Interest attributable to delay in IRS performing ministerial or
   managerial act.
2. No significant aspect of error attributable to taxpayer.

## Mechanics — how it works

For FTA:
1. **Verify clean compliance history** (last 3 years).
2. **Request FTA orally** during phone contact with IRS, OR
3. **Submit Form 843** for FTA abatement.
4. IRS typically grants if requirements met.

For reasonable cause:
1. **Document circumstances** (medical records, records of
   destruction, etc.).
2. **Submit Form 843** with detailed reasonable cause statement.
3. IRS evaluates against Boyle and IRM 20.1 standards.

For §6404(e):
1. **Identify specific IRS delay**.
2. **Submit Form 843** with delay documentation.

## Documentation requirements

- Form 843 with detailed explanation.
- Supporting documentation (medical, disaster, etc.).
- Compliance history showing FTA eligibility.

## Common pitfalls / audit risks

- **Boyle preclusion.** Reliance on CPA/attorney to file is not
  reasonable cause.
- **Failure to demonstrate "ordinary business care and prudence."**
  Generic statements rejected.
- **Interest cannot be abated for taxpayer error.** §6404(e)
  applies only to IRS-side delay.
- **§6651(a)(2) reduction** of FTF by FTP — taxpayers and
  practitioners often miscalculate.
- **Failure to request FTA first.** FTA is automatic; reasonable
  cause is not. Use FTA when available.

## Recent legislative changes

- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §6651
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State penalty regimes are independent. Each state has its own
abatement procedures.

## AICPA SSTS / Circular 230 considerations

Standard diligence; practitioner should pursue FTA before
reasonable cause when both available.

## Default confidence band rationale

**HIGH** for FTA when eligibility is clear. **MODERATE** for
reasonable cause depending on documentation strength.

## Cross-references

- **`penalty-abatement`** (#66) — broader penalty abatement
  framework.
- **`predict-reasonable-cause`** (predict skill).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 6651",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section6651",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 6404(e)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section6404",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRM",
      "citation": "IRM 20.1.1.3.6.1, First Time Abate (FTA)",
      "url": "https://www.irs.gov/irm/part20",
      "weight": "persuasive_non_authority"
    },
    {
      "authority_type": "SCOTUS",
      "citation": "United States v. Boyle, 469 U.S. 241 (1985)",
      "url": "https://www.supremecourt.gov",
      "weight": "binding_judicial"
    }
  ]
}
```
