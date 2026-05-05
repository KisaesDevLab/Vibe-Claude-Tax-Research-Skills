---
name: predict-innocent-spouse
description: |
  Predicts whether a requesting spouse will obtain relief from joint
  and several liability under IRC §6015(b) (traditional innocent-
  spouse relief), §6015(c) (separation of liability allocation), or
  §6015(f) (equitable relief). Applies the Rev. Proc. 2013-34
  threshold-conditions-and-streamlined-relief framework, the
  Lantz / Mannella regulatory-deadline holdings as superseded by the
  IRS's 2-year rule abandonment for §6015(f), and the §6015(e) Tax
  Court review pathway. Use when the user asks "innocent spouse",
  "§6015", "Form 8857", "joint liability relief", "separation of
  liability", "equitable relief", "abusive spouse tax relief", or
  "spousal abuse tax debt". Make sure to use this skill whenever
  the user mentions innocent spouse, §6015, Form 8857, or relief
  from joint liability.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# predict-innocent-spouse — §6015 relief from joint liability

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `references/relief-pathways.md` — §6015(b) / (c) / (f) factors,
   Rev. Proc. 2013-34, abuse-and-financial-control overlay.

## Operative authority

- IRC §6013(d)(3) — joint and several liability default for joint
  returns.
- IRC §6015(a) — election framework for relief from joint liability.
- IRC §6015(b) — traditional innocent-spouse relief.
- IRC §6015(c) — separation-of-liability allocation (separated /
  divorced / no longer member of household for 12 months).
- IRC §6015(f) — equitable relief catch-all.
- IRC §6015(e) — Tax Court review with 90-day petition window from
  notice of final determination.
- Rev. Proc. 2013-34 — threshold conditions, streamlined relief,
  facts-and-circumstances factors.
- Pullins v. Commissioner, 136 T.C. 432 (2011) — knowledge factor
  application in spousal-abuse context.

## Workflow

### 1. Intake

- `request_type`: §6015(b) / (c) / (f) / all three (Form 8857
  permits all three concurrently)
- `joint_return_year`
- `understatement_or_unpaid_balance`: §6015(b)/(c) require an
  understatement; §6015(f) covers both understatements and
  underpayments (Rev. Proc. 2013-34)
- `marital_status_history`: married, separated, divorced, deceased
- `knowledge_or_reason_to_know`: did the requesting spouse know or
  have reason to know of the erroneous item / unpaid liability
- `economic_hardship_facts`: would relief mitigate economic
  hardship for the requesting spouse
- `abuse_history`: physical / psychological / financial control;
  Rev. Proc. 2013-34 §4.03(2)(c)(ii) treats abuse as overriding
  the knowledge factor
- `compliance_with_subsequent_returns`: requesting spouse has
  filed and paid for years after the relief year (a streamlined-
  relief condition)
- `transferred_assets`: any disqualifying asset transfers to/from
  the requesting spouse (§6015(c)(3)(C))

### 2. Threshold conditions (Rev. Proc. 2013-34 §4.01)

For ANY §6015 relief:
1. Joint return filed for the year at issue.
2. Relief unavailable under §6015(b) or (c), OR (b)/(c) considered.
3. No fraudulent transfer of assets between the spouses.
4. No knowing participation in fraud.
5. No transfer of disqualified assets (§6015(c)(3)(C)).
6. Income tax liability (NOT a non-tax debt collected through
   refund offset).
7. Filed Form 8857 within the time limit (currently 10 years from
   first collection activity for §6015(f); for §6015(b) and (c),
   2 years from first collection activity).

### 3. §6015(b) traditional innocent-spouse

Conjunctive requirements:
1. Joint return filed.
2. Understatement attributable to erroneous items of nonrequesting
   spouse.
3. Requesting spouse did not know AND had no reason to know of
   the understatement.
4. Inequitable to hold the requesting spouse liable.
5. Election within 2 years of first collection activity.

"Reason to know" is the heart: would a reasonable person in the
requesting spouse's position have known? Pullins and progeny treat
spousal abuse as overriding the imputed-knowledge inference.

### 4. §6015(c) separation-of-liability allocation

Available only if:
1. Joint return filed.
2. Spouse divorced, legally separated, or living apart for ≥ 12
   months.
3. Election within 2 years of first collection activity.
4. No transfer of property between spouses with a principal
   purpose of tax avoidance (§6015(c)(3)(B)).

Allocates the deficiency as if separate returns had been filed,
limited to items attributable to the nonrequesting spouse. Actual-
knowledge bar (§6015(c)(3)(C)): if the requesting spouse had
ACTUAL knowledge (not just reason to know), the allocation is
denied for items of which she had actual knowledge.

### 5. §6015(f) equitable relief

Catch-all for taxpayers who do not qualify under (b) or (c).
Threshold conditions plus the Rev. Proc. 2013-34 §4.03 facts-and-
circumstances factors:

- Marital status (separated/divorced favors relief).
- Economic hardship if relief denied.
- Knowledge or reason to know of the item / underpayment.
- Legal obligation under divorce decree.
- Significant benefit received from the item.
- Compliance with tax laws after the year at issue.
- Mental or physical health.
- Abuse — overrides knowledge / control factors.

§6015(f) request available for both understatements AND
underpayments; the 2-year deadline historically applied was
abandoned by the IRS in 2011 (Notice 2011-70) and replaced with
the §6502 collection statute as the deadline (effectively 10
years from assessment).

### 6. Streamlined relief (Rev. Proc. 2013-34 §4.02)

If all conditions met, IRS will grant relief without facts-and-
circumstances analysis:
1. No longer married OR ≥ 12 months separated.
2. Economic hardship if relief denied (using §6343(e) standards).
3. No knowledge / reason to know of the item / underpayment;
   abuse / financial control overrides.

### 7. Conclusion

Confidence band per `shared/confidence-bands.md`:

- HIGH: streamlined-relief conditions clearly met (no longer
  married + economic hardship + no knowledge + no abuse override
  needed).
- MODERATE: §6015(b) / (c) requirements likely met but
  reason-to-know analysis is fact-driven.
- LOW: knowledge factor problematic but abuse-override / equitable
  relief plausible.
- SPECULATIVE: requesting spouse benefited substantially and
  knew of the items; recommend exhaust other options first.

### 8. Authorities + sidecar

Cite §6015(b) / (c) / (f), Rev. Proc. 2013-34, Pullins, and any
case law specific to the fact pattern. JSON sidecar validates
against `shared/output-schema.json`.

For an abuse-overlay case, populate the unredacted facts in the
analysis and explicitly flag the abuse override. Form 8857
includes a section for confidential abuse disclosure.

## Hard rules

- Never recommend a spouse remain liable when abuse is present
  without first walking the abuse-override under Rev. Proc.
  2013-34 §4.03(2)(c)(ii).
- Always file Form 8857 even if the predicted band is LOW; there
  is no penalty for a denied request, and the §6015(e) Tax Court
  pathway preserves later review.
- Never assert the 2-year deadline for §6015(f); it was abandoned
  in 2011.
- Drop one band when the requesting spouse received substantial
  benefit from the item.
- Drop one band when the requesting spouse had actual (not
  constructive) knowledge.
- For requests denied at the appeals level, explain the §6015(e)
  90-day Tax Court petition window.

## Verification checklist (appendix)

End with the SSTS / Circular 230 checklist from
`shared/compliance.md`. For abuse cases, also flag practitioner
duty to facilitate disclosure (Form 8857 has an explicit
confidentiality regime).

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
