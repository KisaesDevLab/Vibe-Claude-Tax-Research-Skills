---
name: form-line-explainer
description: |
  Explains a specific line, box, or schedule on a federal tax form
  with cite to the relevant IRC section, Treas. Reg., and Form
  Instructions. Covers Form 1040 / 1120 / 1120-S / 1065 / 706 /
  709 / 941 / 940 / Schedule A / B / C / D / E / 8949 / 8606 /
  4562 / 4797 / 8825 / 8865 / 5471 / 5472 / 8938 and most major
  forms. Use when the user asks "what does Form X line N mean",
  "explain Schedule [letter] Line N", "how do I report X on Form
  Y", or "what's the difference between W-2 Box 1 and Box 3". Make
  sure to use this skill whenever the user mentions a Form
  number + line number + question.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# form-line-explainer — Form line / box / schedule explainer

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`

## Operative authority

- IRC sections governing the underlying tax computation.
- Treasury Regulations governing the reporting requirement.
- Form Instructions (`authority_type: Instructions` /
  `weight: persuasive_non_authority`).
- Form Form itself (`authority_type: Form` /
  `weight: persuasive_non_authority`).

## Workflow

### 1. Intake

- `form_id`: e.g., 1040, 1120, 1120-S, 1065, 706, 709, 941, 940,
  Schedule A, B, C, D, E, 8949, 8606, 4562, 4797, 5471, 8938, etc.
- `tax_year`: critical because line numbers change with form
  revisions.
- `line_or_box_number`.
- `user_question`: what they want to understand.

### 2. Form retrieval

1. Fetch the year-specific form and instructions from
   `https://www.irs.gov/forms-instructions`.
2. Locate the specific line / box.
3. Read the year-specific instructions for that line.

### 3. Citation chain

For each line, the citation chain typically is:
1. **IRC section**: the underlying statutory rule (e.g., §61
   gross income for Form 1040 Line 1a).
2. **Treasury Regulation**: the implementing rule (e.g.,
   §1.61-2 for compensation income).
3. **Form Instructions**: the IRS's procedural guidance.
4. **Form itself**: the structured reporting requirement.

### 4. Worked example

For a common question:
- "What's the difference between W-2 Box 1 and Box 3?"
- Box 1 = federal-income-tax-withholding wages
  (§3401(a) wages + §125 cafeteria plan reductions).
- Box 3 = OASDI wages (§3121(a) wages, capped at OASDI base;
  pre-tax 401(k) contributions IS in Box 3 because §3121(a) does
  NOT exclude §401(k) deferrals).
- Common difference: §401(k) elective deferrals reduce Box 1 but
  not Box 3.
- §125 cafeteria-plan elections reduce both.
- Cite §3121(a), §3401(a), §401(k), §125.

### 5. Conclusion + sidecar

JSON sidecar validates against `shared/output-schema.json`. Cite
the IRC section + Treas. Reg. + Form Instructions + Form. The
Form Instructions and Form are `persuasive_non_authority`; pair
with a higher-tier authority for the underlying tax rule.

Confidence band per `shared/confidence-bands.md`. HIGH for
clean form-line interpretations with retrieved current-year
instructions.

## Hard rules

- Always confirm year-specific form revision; line numbers
  change.
- Form Instructions are `persuasive_non_authority`; pair with
  IRC / Treas. Reg.
- Never claim Chevron deference for Form Instructions.
- For complex / multi-step calculations (e.g., AMT, Schedule J
  income averaging for farmers), break into steps citing each
  authority.
- Always include the verification checklist appendix.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`. Note that Form Instructions are
persuasive but do NOT bind the IRS or courts on the underlying
tax rule.

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
