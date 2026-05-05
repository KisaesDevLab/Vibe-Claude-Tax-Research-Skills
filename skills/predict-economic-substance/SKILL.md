---
name: predict-economic-substance
description: |
  Predicts whether a transaction will withstand economic-substance
  scrutiny under IRC §7701(o) (codified by Health Care and Education
  Reconciliation Act of 2010, Pub. L. 111-152). Applies the
  conjunctive two-prong test (objective economic effect AND
  subjective non-tax purpose), the §6662(b)(6) and (i) 20%/40%
  strict-liability accuracy penalties, and the limited "relevance"
  filter under IRS Notice 2014-58. Use when the user asks "will this
  pass economic substance", "§7701(o)", "ESD codified", "Coltec",
  "Compaq", "intermountain test", "non-tax business purpose",
  "20% or 40% penalty", or "Notice 2014-58". Make sure to use this
  skill whenever the user mentions economic substance, sham, business
  purpose, or §7701(o).
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# predict-economic-substance — §7701(o) doctrine

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `shared/legislation-tracking.md` — §7701(o) added by Pub. L.
   111-152 (HCERA 2010); §6662(b)(6), §6662(i) by same.
6. `references/judicial-history.md` — pre-codification cases
   (Frank Lyon, Coltec, Compaq, Andantech, ACM Partnership) and
   post-codification application (Bank of NY Mellon, AIG/IES Indus.).

## Operative authority

- IRC §7701(o) — codified economic-substance doctrine.
- IRC §6662(b)(6) — 20% accuracy penalty for ESD-disallowed
  transactions; §6662(i) elevates to 40% for non-disclosed.
- Reasonable-cause defense at §6664(c) does NOT apply to a §6662(i)
  penalty (strict liability for non-disclosed ESD-failed
  transactions per §6664(c)(2)).
- IRS Notice 2014-58 — relevance and "principal-or-similar-tax-
  purpose" guidance.
- Pre-codification cases: Frank Lyon Co. v. United States, 435
  U.S. 561 (1978); Coltec Indus. v. United States, 454 F.3d 1340
  (Fed. Cir. 2006); Compaq Computer Corp. v. Commissioner, 277
  F.3d 778 (5th Cir. 2001); ACM Partnership v. Commissioner, 157
  F.3d 231 (3d Cir. 1998).

## Workflow

### 1. Intake

- `transaction_description`: full structure
- `tax_attribute_at_issue`: deduction, credit, gain shifting,
  basis-shifting, loss recognition, etc.
- `non_tax_business_purpose`: the asserted non-tax rationale
- `pre-tax_economic_outcomes`: profit / loss exposure absent the
  tax benefit; meaningful change in economic position
- `disclosure_status`: Form 8275 / 8275-R / 8886 filed or
  contemplated
- `taxpayer_circuit`: relevant for which pre-codification cases
  bind under Golsen

### 2. Relevance filter (Notice 2014-58)

Before applying §7701(o), determine whether the doctrine is
"relevant". §7701(o)(5)(C): "Whether economic substance doctrine is
relevant ... shall be made in the same manner as if this subsection
had never been enacted."

The IRS will assert relevance only when "facts and circumstances are
similar to" the pre-codification line of cases. Do NOT apply
§7701(o) to:
- Routine business choices among legally permitted alternatives
  (e.g., choice of entity, debt vs equity, lease vs purchase) when
  the choice produces meaningful non-tax effects.
- Tax-motivated but congressionally-blessed structures (e.g.,
  §1031, §351, §721, §368, low-income-housing credits, R&D credit).

Notice 2014-58 reaffirms that the IRS Large Business & International
(LB&I) Director must approve any economic-substance assertion; field
agents may not raise §7701(o) without internal sign-off.

### 3. Two-prong conjunctive test (§7701(o)(1))

A transaction has economic substance only if BOTH:

1. **Objective**: The transaction changes in a meaningful way
   (apart from federal income tax effects) the taxpayer's
   economic position.
2. **Subjective**: The taxpayer has a substantial purpose (apart
   from federal income tax effects) for entering into such
   transaction.

§7701(o)(2): potential for profit IS taken into account in the
objective prong only if the present value of the reasonably
expected pre-tax profit is substantial in relation to the present
value of the expected net tax benefits.

State and local tax effects: §7701(o)(3) — a state or local tax
benefit related to a federal tax effect is treated AS a federal tax
effect (i.e., does not save the transaction).

Financial-accounting / book-tax-difference benefits: §7701(o)(4) —
financial accounting benefits arising from a reduction in federal
income tax are NOT taken into account.

### 4. Pre-codification case overlay

Pre-codification, courts applied the doctrine differently:
- 4th, 5th, 6th, 8th Cir.: disjunctive — either prong sufficient.
- 3rd, 11th Cir.: conjunctive — both prongs required.
- §7701(o)(1) codifies the conjunctive approach, ending the split.

For transactions structured PRE-2010 still in litigation, identify
the taxpayer's circuit and the contemporaneous test applied.

### 5. Penalty exposure (§6662(b)(6) / (i))

- §6662(b)(6): 20% accuracy penalty on the underpayment
  attributable to ESD disallowance.
- §6662(i): 40% if the ESD-failed transaction was NOT adequately
  disclosed (Form 8275, 8275-R, or 8886).
- §6664(c)(2): reasonable-cause defense unavailable for §6662(b)(6)
  if non-disclosure 40% applies — STRICT LIABILITY.
- Recommend Form 8275 / 8275-R disclosure on any transaction
  vulnerable to ESD even in a LOW-band posture.
- Listed transactions (§6707A) and reportable transactions (§6011)
  trigger separate penalty regimes (Form 8886).

### 6. Conclusion

Confidence band per `shared/confidence-bands.md`:

- HIGH: clear non-tax business purpose, meaningful pre-tax economic
  effect, congressionally-blessed structure (§1031, §351, etc.).
- MODERATE: business purpose is real but the tax benefit dominates
  in dollar terms; pre-tax profit potential is positive but modest.
- LOW: tax benefit substantially exceeds pre-tax profit; structure
  resembles pre-codification ACM Partnership / Coltec patterns.
  Disclosure mandatory.
- SPECULATIVE: tax benefit is the entire economic point; recommend
  do not proceed.

§6662(b)(6) cannot reach HIGH on a Treasury-Reg-only basis without
a pre-codification controlling case (Loper Bright posture).

### 7. Authorities + sidecar

Cite §7701(o), §6662(b)(6) and (i), §6664(c)(2), Notice 2014-58,
and the relevant pre-codification cases binding in the taxpayer's
circuit. JSON sidecar validates against `shared/output-schema.json`.
Include `negative_treatment_review_required: true` for any high-
stakes position.

## Hard rules

- Never assert ESD passes solely because the transaction has any
  non-tax purpose; the substantial-purpose / meaningful-change
  thresholds are conjunctive AND quantitative.
- Never invoke a 40% strict-liability defense; §6664(c)(2) is
  unforgiving.
- Always recommend Form 8275 / 8275-R / 8886 disclosure where
  applicable to keep §6662(i) at 20% rather than 40%.
- Drop one band when the transaction relies on a Tax Court
  Memorandum opinion as the closest authority.
- Drop one band when the structure resembles ACM Partnership or
  Coltec / Compaq patterns.
- Never claim Chevron deference for any Treasury Reg interpreting
  §7701(o).

## Verification checklist (appendix)

End with the SSTS / Circular 230 checklist from
`shared/compliance.md`. ALWAYS include the negative-treatment-
review residual practitioner responsibility for §7701(o) work
given the strict-liability penalty regime.

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
