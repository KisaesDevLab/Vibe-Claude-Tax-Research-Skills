---
name: planning-strategy-library
description: |
  Catalog of 30 CPA-vetted federal and state tax-planning
  strategies covering individual, entity, real-estate, and estate
  / gift contexts. Each strategy entry documents IRC section,
  eligibility criteria, mechanics, citations, state interplay,
  and Dirty-Dozen / Listed-Transaction warnings where applicable.
  Routes downstream substantive analysis to research / prediction
  skills. Use when the user asks "what tax strategies are
  available", "list of tax strategies", "show me the strategy for
  X", "QSBS strategy", "Roth conversion ladder", "GRAT", "DAF",
  or "strategy library". Make sure to use this skill whenever the
  user asks for a catalog or library of tax strategies, or asks
  about a specific strategy by name.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# planning-strategy-library — 30-strategy catalog

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `shared/legislation-tracking.md` — for any post-2024 legislation
   affecting strategy eligibility.
6. `shared/strategy-list.md` — canonical strategy index.
7. `references/index.md` — strategy index with cross-references.
8. The relevant `references/strategies/<slug>.md` for the
   strategy in question.

## Workflow

### 1. Intake

- `client_facts`: relevant facts (income, entity type, state,
  age, marital status, etc.).
- `strategy_query`: specific strategy by name, slug, or topic.
- `state_residency`.

### 2. Strategy lookup

Match the query to a strategy slug per `shared/strategy-list.md`.
Load the corresponding `references/strategies/<slug>.md`.

### 3. Eligibility analysis

Walk the strategy's eligibility criteria against client facts.
Identify any gaps or contraindications.

### 4. Mechanics walk

Walk the strategy's mechanics: deadlines, election forms,
disclosures, ongoing maintenance.

### 5. Citation chain

Cite IRC section, Treasury Regulations, relevant Rev. Rul. /
Rev. Proc. / Notice, and any case law.

### 6. State interplay

If the strategy has state-specific eligibility (PTET, §1202,
§1031, REPS state PAL, ABC-test states), route to
`tax-research-state-income` or `tax-research-state-salesuse`
per-state file.

### 7. Recent-legislation impact

If the strategy is materially affected by post-2024 legislation
(OBBBA, etc.), use `shared/legislation-tracking.md` workflow to
verify current law via Classification Tables.

### 8. Conclusion + sidecar

JSON sidecar validates against `shared/output-schema.json`.
- `conclusion`: strategy applicability + recommended next steps.
- `confidence_band`: per `shared/confidence-bands.md`.
- `authorities[]`: IRC + Treas. Reg. + Rev. Proc. / Notice.
- `state_files_consulted[]` if state interplay.
- `public_laws_consulted[]` if recent-legislation impact.
- `disclosure_forms[]`: 8275 / 8275-R / 8886 if applicable.

## Hard rules

- Never recommend a strategy on the Dirty-Dozen / Listed-
  Transaction list (§831(b) micro-captives, syndicated
  conservation easements, monetized installment sales,
  charitable LLC structures). These are explicitly excluded
  from the library; route to `predict-economic-substance` and
  `compliance-ssts-circular230` if a client raises one.
- Always check state interplay for strategies marked ✓ in
  `shared/strategy-list.md`.
- Always check recent-legislation impact for strategies marked
  ✓ in `shared/strategy-list.md`.
- Drop one band when state interplay relies on a `status: stub`
  per-state file.
- Drop one band when recent legislation may have modified the
  strategy and the user has not confirmed which Public Law's
  posture applies.
- Always include the verification checklist appendix.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`. For high-stakes strategies (six-
figure plus benefit, novel application), include the negative-
treatment-review residual practitioner responsibility.

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
