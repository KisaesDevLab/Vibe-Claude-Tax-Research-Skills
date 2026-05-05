---
name: predict-debt-vs-equity
description: |
  Predicts whether an instrument issued by a corporation will be
  characterized as debt (deductible interest, basis recovery) or
  equity (non-deductible distributions, return-of-capital basis
  ordering) under IRC §385 and the multi-factor common-law tests.
  Applies the 11- to 13-factor judicial framework (Roth Steel,
  Slappey Drive, Indmar, Estate of Mixon), §385(c)(1) consistency
  rule, and the §163(j) interaction. Use when the user asks "is
  this debt or equity", "shareholder loan", "thin capitalization",
  "debt characterization", "advance to controlled corporation",
  "§385", "shareholder advance", or "Roth Steel factors". Make sure
  to use this skill whenever the user mentions debt vs equity,
  shareholder loan, §385, intercompany advance, or thin
  capitalization.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# predict-debt-vs-equity — §385 + common-law characterization

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `references/judicial-factors.md` — multi-circuit factor lists,
   leading cases, §385(c) consistency rule.

## Operative authority

- IRC §385 — Treasury authorized to issue regulations distinguishing
  debt from equity; final regulations limited to documentation
  rules under §385 (§1.385-1, -2, -3, -3T, -4) plus partial relief
  in subsequent guidance.
- IRC §385(c)(1) — issuer's characterization is binding on the
  issuer and holders, but NOT on the IRS (one-way street).
- IRC §163(j) — interest deduction limit (post-TCJA) interacts
  with debt characterization; if instrument is recharacterized as
  equity, the would-be interest is non-deductible and the §163(j)
  computation is unaffected.
- IRC §385(b) factors (statutory): written unconditional promise to
  pay, subordination, debt-to-equity ratio, convertibility,
  relationship between holdings.
- Common-law multi-factor tests (vary by circuit):
  - 5th Cir.: 13 factors, Estate of Mixon v. United States, 464
    F.2d 394 (5th Cir. 1972).
  - 6th Cir.: 11 factors, Roth Steel Tube Co. v. Commissioner, 800
    F.2d 625 (6th Cir. 1986); Indmar Products Co. v. Commissioner,
    444 F.3d 771 (6th Cir. 2006).
  - 11th Cir.: 13 factors, Slappey Drive Indus. Park v. United
    States, 561 F.2d 572 (5th Cir. 1977) — adopted by 11th Cir.
- Treas. Reg. §1.385-3 — "covered debt instruments" anti-avoidance
  rules for funded acquisitions.

## Workflow

### 1. Intake

- `instrument_description`: term, rate, security, repayment terms
- `issuer_facts`: corporate form, capitalization
- `holder_facts`: shareholder / sister entity / unrelated
- `documentation_status`: written promissory note, security
  agreement, board minutes
- `payment_history`: actual interest paid, principal repaid, any
  forbearance
- `taxpayer_circuit`: for Golsen application of factor list
- `is_intercompany_within_consolidated_group`: §1.385 documentation
  rules apply only to "expanded affiliated group" issuers above
  thresholds

### 2. Statutory framework

§385(b) authorizes Treasury to consider:
1. Written unconditional promise to pay a sum certain on demand
   or specified date with fixed-rate interest.
2. Subordination to or preference over indebtedness of the
   corporation.
3. Ratio of debt to equity of the corporation.
4. Convertibility into stock.
5. Relationship between holdings of stock and holdings of the
   instrument.

Treasury regulations finalized in 2016 cover:
- §1.385-1: definitions and consistency.
- §1.385-2: documentation requirements (effective for instruments
  issued on or after 1/1/2018; further delayed via Notice 2017-36
  and final §1.385-2 not enforced as initially proposed).
- §1.385-3 / -3T: covered-debt-instrument rules — recharacterize
  certain debt issued in connection with distributions or
  acquisitions within an expanded affiliated group as stock.
- §1.385-4: consolidated-group adjustments.

The §1.385-2 documentation rules were significantly delayed and
relaxed; practitioners should verify current effective-date status
before relying on documentation-rule exceptions.

### 3. Common-law factor analysis

The "Roth Steel" 11-factor framework (6th Cir.) is representative;
identify the binding circuit and apply its specific factor list:

1. The names given to the instruments.
2. The presence or absence of a fixed maturity date.
3. The source of the payments.
4. The right to enforce payment.
5. Participation in management.
6. Status equal to or inferior to that of regular corporate
   creditors.
7. The intent of the parties.
8. "Thin" or adequate capitalization.
9. Identity of interest between creditor and stockholder.
10. Source of interest payments.
11. Ability of corporation to obtain loans from outside lending
    institutions.

For shareholder advances to closely-held corporations, factor 9
(identity of interest), factor 8 (capitalization), and factor 11
(ability to borrow externally) are typically dispositive.

### 4. Documentation and behavior

- Written promissory note with specified maturity, interest rate,
  payment schedule.
- Board resolution authorizing the loan.
- Security agreement / collateral if available.
- Actual payments of interest on schedule (not just accrual).
- Repayments not contingent on corporate profitability.
- Loan terms commercially reasonable (rate at AFR or higher;
  §1274 / §7872 interaction for below-market loans).

### 5. §385(c)(1) consistency

The issuer's characterization on its books and the holder's
treatment must be consistent. If the issuer treats the instrument
as debt and deducts interest, the holder must report interest
income. The IRS is NOT bound by the issuer's characterization but
the consistency rule prevents whipsawing the same instrument to
issuer's and holder's combined benefit.

### 6. §163(j) interaction (post-TCJA)

If the instrument is debt, §163(j) limits the issuer's interest
deduction to the sum of business interest income + 30% of ATI +
floor-plan financing interest. Recharacterization to equity
removes the deduction entirely (no §163(j) computation needed) but
also affects E&P computation and constructive-distribution analysis
under §301.

### 7. Conclusion

Confidence band per `shared/confidence-bands.md`:

- HIGH: written note + market-rate interest + actual payments +
  thin-cap not implicated + arm's-length covenants.
- MODERATE: written documentation present but some payments
  forborne; thin-cap concerns moderate; closely-held but
  documented.
- LOW: undocumented advance; payments deferred indefinitely;
  thin-cap acute; identity of interest dominant.
- SPECULATIVE: no documentation; payments triggered only by
  profits; subordination beyond market norms.

### 8. Authorities + sidecar

Cite §385, relevant Treas. Regs., and circuit-specific factor
cases. JSON sidecar validates against `shared/output-schema.json`.

## Hard rules

- Never assert debt characterization without a written instrument
  and documented payment history (or equivalent contemporaneous
  documentation).
- Never claim Chevron deference for Treas. Reg. §1.385-1 through
  §1.385-4 (post-Loper Bright Skidmore review).
- Drop one band when documentation is reconstructive or when
  payments have been deferred indefinitely.
- §385(c)(1) binds the issuer/holder but never the IRS — flag this
  one-way-street limitation.
- For instruments below applicable AFR, layer §1274 / §7872 below-
  market-loan analysis on top of debt-vs-equity.

## Verification checklist (appendix)

End with the SSTS / Circular 230 checklist from
`shared/compliance.md`. Flag negative-treatment-review residual
responsibility for high-stakes positions (large interest
deductions or recharacterization-driven E&P consequences).

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
