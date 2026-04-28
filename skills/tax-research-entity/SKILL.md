---
name: tax-research-entity
description: |
  Federal entity-tax research skill covering subchapter C (corporate)
  and subchapter K (partnership / LLC) issues, plus subchapter S
  (S-corporation) elections and qualifications. Produces a
  memorandum-style answer with explicit authority weighting,
  confidence band, disclosure flag, and JSON sidecar. Distinguishes
  itself from tax-research-federal by routing entity-specific
  questions (formation, distributions, redemptions, partnership
  basis, §704(b) allocations, §1366 S-corp items, §332/§368
  reorganizations, check-the-box). Use when the user asks "C-corp
  question", "S-corp question", "partnership tax question",
  "§332 liquidation", "§368 reorganization", "§754 election",
  "§704(b)", "§743", "check-the-box", or "Form 8832 election". Make
  sure to use this skill whenever the user mentions C-corp, S-corp,
  partnership, LLC tax, subchapter C / K / S, or entity-level tax
  questions.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# tax-research-entity — Subchapter C / K / S research

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `shared/legislation-tracking.md` — TCJA changes to §163(j),
   §245A, §951A, §250; OBBBA permanence and modifications.
6. `references/subchapter-c.md` — corporate distributions,
   redemptions, §332 liquidations, §368 reorganizations.
7. `references/subchapter-k.md` — partnership formation,
   allocations, distributions, §754 / §743 / §734 mechanics.
8. `references/subchapter-s.md` — eligibility, elections, §1366
   pass-through, §1377 termination.
9. `references/check-the-box.md` — Treas. Reg. §301.7701-1 through
   -3 entity-classification framework.

## Workflow

### 1. Intake

- `taxpayer_entity_type`: C-corp, S-corp, LLC (single-member or
  multi-member), partnership (LP, GP, LLP), disregarded entity
- `subchapter`: C, K, S, mixed
- `issue`: free text
- `tax_year`
- `taxpayer_state` and `taxpayer_circuit` (Golsen)
- `transaction_facts`: formation, redistribution, redemption,
  liquidation, reorganization, sale, purchase, conversion

### 2. Subchapter routing

Identify the controlling subchapter and load the relevant
references file. For mixed-subchapter transactions (e.g., a
C-corp parent of a partnership-form subsidiary), walk both.

### 3. Authority hierarchy walk

Same as `tax-research-federal`:

1. **Statute** — IRC text at uscode.house.gov USLM.
2. **Regulations** — eCFR Title 26. Distinguish final / temporary
   / proposed. Flag `chevron_replaced: true` for any reg
   interpreting ambiguous statute post-Loper Bright.
3. **Binding judicial** — SCOTUS, then Court of Appeals binding
   in the taxpayer's circuit (Golsen), then Tax Court / DCt /
   Court of Federal Claims.
4. **IRS published** — Rev. Ruls., Rev. Procs., Notices,
   Announcements (IRB-published).
5. **Legislative history** — JCT Bluebook, committee reports,
   conference reports, Greenbook (only if proposal enacted),
   CBO scoring (only if accompanying enacted bill).
6. **Written determinations** — PLR, TAM, CCA, GCM, AOD, FSA,
   Office Memorandum, Information Letter (citable, but
   §6110(k)(3) no precedential value to other taxpayers).
7. **Persuasive non-authority** — IRS Pubs, IRM, Forms /
   Instructions, ATG (Audit Technique Guides — partnerships,
   S-corps, and reorganizations have published ATGs).

### 4. Conclusion

Confidence band per `shared/confidence-bands.md`. Note that
entity reorganization and §704(b)-allocation questions often have
binding circuit splits; identify the taxpayer's circuit before
weighting.

### 5. Authorities + sidecar

Every cited authority appears in the JSON sidecar with all
required fields. JSON validates against
`shared/output-schema.json`. Include
`negative_treatment_review_required: true` for high-stakes
positions.

For Public-Law-touching questions (TCJA, OBBBA), populate
`public_laws_consulted[]`.

## Hard rules

- Never fabricate IRC sections, Reg cites, case names, or PLR
  numbers.
- Never claim Chevron deference for entity-tax Treas. Regs (post-
  Loper Bright Skidmore review).
- Never let TaxProf Blog, Procedurally Taxing, Tax Foundation, or
  Tax Policy Center drive a confidence band.
- Drop one band when relying on an Audit Technique Guide as the
  closest authority.
- For state entity issues, route to `tax-research-state-income`
  (e.g., PTET elections, S-corp recognition variations).
- Always include the verification checklist appendix.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`. Note the negative-treatment-review
residual practitioner responsibility for high-stakes entity
positions.
