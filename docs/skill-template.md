# `<skill-name>` — SKILL.md template

Copy this template into `skills/<skill-name>/SKILL.md` for any new skill.
Replace every `<...>` placeholder. Keep the body ≤ 500 lines; push longer
content into `references/<topic>.md` files one level deep.

```yaml
---
name: <kebab-case-name>            # ≤ 64 chars, no "anthropic"/"claude"
description: |
  <Third-person, declarative one-paragraph description, ≤ 1024 chars.
  Front-load the use case. State concrete trigger phrases users say.
  Include "Use when ..." and at least three example user phrasings.
  No first/second person; no XML angle brackets; no audit-lottery
  language. Make sure to use this skill whenever the user mentions
  <trigger keyword 1>, <trigger keyword 2>, <trigger keyword 3>.>
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---
```

## Read before output
Before producing any output, read these files in order:
1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `shared/legislation-tracking.md` (when this skill touches recent
   Public Laws or current law affected by post-2024 legislation)
6. `references/<topic>.md` for this skill (one level deep)
7. (If this is a state research skill) the relevant
   `references/states/<XX>.md` based on the user's jurisdiction.

## Workflow

### 1. Intake
Collect the minimum facts needed to answer. Use the intake schema
below. If a fact is missing and material, request it; if non-material,
proceed with a labeled assumption. For state research skills, capture
the taxpayer's state explicitly (`taxpayer_state` in the sidecar).

### 2. Analysis
Map facts to authorities using the hierarchy. For each contested
proposition, list authorities supporting and contrary, with weight.

### 3. Conclusion
State the conclusion. Assign `confidence_band` per
`shared/confidence-bands.md`. Note disclosure recommendation.

### 4. Authorities
Cite primary sources only. Every entry includes
`authority_type, citation, url, retrieved_date, quoted_text, weight`.
Use the `[CITATION NEEDED — search: <query>]` sentinel rather than
fabricating.

### 5. JSON sidecar
Emit a JSON object validating against `shared/output-schema.json`
following the markdown response. State research skills additionally
populate `state_files_consulted`. Skills that consult Public Laws
populate `public_laws_consulted`.

## Hard rules
- Never fabricate citations.
- Never claim Chevron deference for Treasury Regs (post-Loper Bright).
- Never recommend a position with a SPECULATIVE band.
- Always include the verification checklist.
- For state work: cap confidence at LOW when relying solely on a
  `status: stub` state file.
- Tax Foundation, Tax Policy Center, blogs, and other current-
  awareness sources never drive a band assignment.
- Free-source citation discipline cannot detect implicit overrules
  with comprehensive coverage. Note this in the verification
  checklist for high-stakes positions.
- Keep this SKILL.md ≤ 500 lines; push longer content to references/.

## Verification checklist (appendix)
The practitioner using this output must complete the checklist in
`shared/compliance.md` before relying on the result, including the
negative-treatment-review residual responsibility for high-stakes
positions.

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers two
orthogonal handoffs — package the result as a memo or open-point
list, and carry the conclusion forward into a plan, workpaper,
resolution matter, or return process — and is the dispatcher's hook
for chaining to the next specialist skill.
