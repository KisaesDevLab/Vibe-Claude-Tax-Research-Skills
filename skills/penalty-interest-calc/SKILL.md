---
name: penalty-interest-calc
description: |
  Computes federal tax penalty and interest exposure for failure-to-
  file (§6651(a)(1)), failure-to-pay (§6651(a)(2)), failure-to-
  deposit (§6651(a)(3)), accuracy-related (§6662), fraud (§6663),
  estimated-tax (§6654 / §6655), and trust-fund recovery (§6672).
  Also computes interest under §6601 / §6621. Use when the user
  asks "how much penalty", "what's the interest", "compute §6651
  penalty", "estimated-tax penalty", "§6662 accuracy", "§6663
  fraud", "AFR", "federal short-term rate", or "compounding". Make
  sure to use this skill whenever the user mentions a penalty
  computation, interest computation, or §6601 / §6621.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# penalty-interest-calc — Penalty + interest computation

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `references/penalty-rates-and-rules.md` — penalty types,
   rates, ceilings, abatement pathways.

## Operative authority

- IRC §6601 — interest on underpayments.
- IRC §6621 — federal short-term rate + 3% (general); + 5% for
  large corporate underpayments.
- IRC §6651 — FTF / FTP / FTD penalties.
- IRC §6654 — individual estimated-tax penalty.
- IRC §6655 — corporate estimated-tax penalty.
- IRC §6662 — accuracy-related penalty (20% / 40%).
- IRC §6663 — fraud penalty (75%).
- IRC §6672 — TFRP (100% trust-fund liability).
- IRC §6699 — partnership / S-corp late-filing.

## Workflow

### 1. Intake

- `tax_period`: tax year + (for quarterly) quarter.
- `original_due_date`.
- `actual_filing_date` and `actual_payment_date`.
- `unpaid_tax_amount`.
- `understatement_amount` (for §6662 / §6663).
- `cause_alleged`: for abatement screening.
- `compliance_history`: for FTA screening.

### 2. §6651 family

#### §6651(a)(1) FTF (failure-to-file)

- 5% per month (or fraction of month) on the unpaid tax.
- Maximum 25% of unpaid tax (5 months × 5%).
- §6651(a)(1) FTF and §6651(a)(2) FTP cannot exceed 5%/month
  combined (the FTF rate is reduced by the FTP rate when both
  apply in the same month).
- §6651(f) — increased to 15% / month / max 75% if failure is
  fraudulent.
- §6651(g) minimum penalty (when 60+ days late and tax > $0):
  the LESSER of $510 (2024 — verify year-specific) or 100% of
  unpaid tax.

#### §6651(a)(2) FTP (failure-to-pay)

- 0.5% per month (or fraction) on the unpaid tax.
- Maximum 25% of unpaid tax.
- §6651(d) reduced rate of 0.25% / month if installment
  agreement in effect.
- §6651(d) increased rate of 1.0% / month after IRS issues
  intent-to-levy notice and waits 10 days.

#### §6651(a)(3) FTD (failure-to-deposit)

- 2% / 5% / 10% / 15% based on lateness:
  - 1-5 days late: 2%.
  - 6-15 days late: 5%.
  - > 16 days late: 10%.
  - Within 10 days of IRS demand notice: 15%.

### 3. §6662 accuracy-related

- 20% on the underpayment portion.
- 40% under §6662(h) for gross-valuation-misstatement, §6662(i)
  for non-disclosed economic-substance-doctrine-failed
  transaction, §6662(j) for non-disclosed foreign-financial-
  asset underpayment.
- §6664(c) reasonable-cause defense (NOT available for
  §6662(b)(6) per §6664(c)(2)).

### 4. §6663 fraud

- 75% on the underpayment portion.
- §6663(b) — IRS bears burden of proof by clear and convincing
  evidence.
- §6664(c) reasonable-cause defense available BUT incongruent
  with fraud finding.

### 5. §6654 individual estimated-tax penalty

- Computed quarter-by-quarter as the federal short-term rate +
  3% on the underpayment for each quarter.
- §6654(d)(1)(B) safe harbors:
  - 90% of current-year tax;
  - 100% of prior-year tax (110% if AGI > $150K).
- §6654(e) waivers:
  - First-year retiree (age 62+) or first-year disability.
  - Casualty / disaster.
  - §6654(e)(3) IRS-determined unusual circumstances.

Compute via Form 2210 (annualized-installment method or
short-method).

### 6. §6655 corporate estimated-tax penalty

Similar to §6654 but for corporations. Computed via Form 2220.

§6655(d) — large corporations (taxable income ≥ $1M in any of 3
prior years) must base estimates on current-year tax (90% safe
harbor only; 100%-prior-year safe harbor unavailable except
Q1).

### 7. §6601 interest

- Federal short-term rate + 3% (§6621(a)(2)).
- Compounded daily (§6622).
- For C-corp underpayments > $100,000: §6621(c) "hot interest"
  = federal short-term + 5%.
- Posted quarterly by the IRS (Rev. Rul. published before each
  quarter).

### 8. §6672 TFRP

- 100% of trust-fund liability.
- Personal liability against responsible persons.
- Joint and several with §6672(d) abatement and §6672(e)
  contribution rights.

### 9. §6699 / §6698 partnership / S-corp late-filing

- $245 per partner / shareholder per month (2024 — verify year-
  specific) with a 12-month maximum for §6699.
- §6698 partnership: same per-partner / per-month structure.
- FTA available under IRM 20.1.1.3.6 (verify current expansion).

### 10. Conclusion + sidecar

JSON sidecar validates against `shared/output-schema.json`.
Provide a quantified penalty + interest computation. Cite §§6601,
6621, 6651, 6654, 6655, 6662, 6663, 6672, 6699 as applicable.

Confidence band per `shared/confidence-bands.md`. HIGH for clean
penalty arithmetic with retrieved year-specific rates.

## Hard rules

- Always retrieve year-specific federal short-term rate from the
  IRS quarterly Rev. Rul. before computing interest.
- Always compound interest daily under §6622.
- Always screen FTA before quoting §6651 penalty as final.
- Always note §6664(c) reasonable-cause defense availability for
  §6662 penalties.
- Always include the verification checklist appendix.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`. Note that interest under §6404(e)(1)
is generally non-abatable except in narrow ministerial-act
provisions.

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
