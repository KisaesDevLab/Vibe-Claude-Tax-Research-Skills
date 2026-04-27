---
name: predict-reasonable-comp
description: |
  Predicts whether a closely-held corporation's compensation paid
  to a shareholder-employee is reasonable under IRC §162(a)(1) for
  C-corp deduction purposes, or sufficient for S-corp wage / FICA
  exposure. Applies the multi-factor Mayson Manufacturing /
  Independent-Investor / Watson framework. Use when the user asks
  'is this comp reasonable', 'S-corp owner W-2 too low',
  'C-corp owner-employee bonus deduction', 'Watson reasonable
  comp', 'IRS audit on compensation', or 'Form 1120-S salary
  question'. Make sure to use this skill whenever the user mentions
  reasonable compensation, S-corp salary, C-corp owner bonus, or
  shareholder-employee comp.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# predict-reasonable-comp

## Read before output

1. `shared/citation-discipline.md` — fabrication ban, sentinel
   pattern, negative-treatment-detection limitation.
2. `shared/authority-hierarchy.md` — weights, Loper Bright, Golsen.
3. `shared/confidence-bands.md` — band definitions and decay rules.
4. `shared/compliance.md` — SSTS / Circular 230 checklist.
5. `references/` for this skill.

## Operative authority

- IRC §162(a)(1) — ordinary and necessary trade or business
  expenses; reasonable allowance for personal services actually
  rendered.
- IRC §1366(a) (S-corp) and §316 (constructive dividend, C-corp).
- Treas. Reg. §1.162-7 — what constitutes reasonable compensation.
- Watson v. United States, 668 F.3d 1008 (8th Cir. 2012) — S-corp
  recharacterization framework.

## Workflow

### 1. Intake

- Entity type (C-corp, S-corp).
- Owner-employee role and time devoted.
- Total compensation (W-2 + bonuses + 401(k) match + benefits).
- Distributions / dividends paid in the same year.
- Industry, company size, location, comparable-position data.

### 2. Multi-factor analysis

For C-corps, apply the Mayson Manufacturing factors (or relevant
circuit's standard):
- Employee qualifications and experience
- Nature, extent, and scope of duties
- Comparison with comparable positions
- Size and complexity of business
- Salary history relative to gross income
- Internal consistency

For S-corps, apply the Watson framework:
- Reasonable comp must be paid before distributions are recognized
  for FICA purposes
- IRS focuses on 'replacement cost' analogy

### 3. Independent-investor test

Where applicable (especially 7th Cir. — Exacto Spring Corp.,
Menard, Eberl's): would an independent investor have approved the
compensation given the corporate return?

### 4. Conclusion

State the predicted IRS position and recommended adjustment.
Confidence band per shared/confidence-bands.md. Note any
disclosure recommendations.

### Final step — JSON sidecar

Emit a JSON object validating against `shared/output-schema.json`.
Required fields: `skill, version, generated_at, task, conclusion,
confidence_band, authorities, verification_checklist`. Every
authority entry includes `authority_type, citation, url,
retrieved_date, quoted_text (≤75 words), weight`. When a primary
source is unreachable, emit the sentinel pattern documented in
`shared/citation-discipline.md` and record an entry in
`unresolved_citations[]`.

## Hard rules

- Never fabricate citations — IRC sections, case names, Reg cites,
  Public Law numbers, or quoted excerpts.
- Never claim Chevron deference for Treasury Regs (post-Loper Bright).
- Never let TaxProf Blog, Procedurally Taxing, Tax Foundation, or
  Tax Policy Center drive a confidence band.
- Never recommend a position with a SPECULATIVE band.
- Drop one band when a written determination (PLR/TAM/CCA/GCM/AOD/
  FSA/Office-Memo/Info-Letter) is the closest authority.
- Drop one band when an authority's retrieved_date > 365 days in a
  fast-moving area.
- Always include the verification checklist appendix.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md` (SSTS § 1.1, § 2.3; Circular 230
§ 10.22, § 10.35, § 10.37). For high-stakes positions, include the
negative-treatment-review residual practitioner responsibility.
