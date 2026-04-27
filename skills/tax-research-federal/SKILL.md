---
name: tax-research-federal
description: |
  Researches a federal income-tax question for a licensed CPA, EA, or
  tax attorney. Maps facts to authority, weights authority per Treas.
  Reg. §1.6662-4(d)(3), assigns a confidence band, and emits a JSON
  sidecar validating against shared/output-schema.json. Use when the
  user asks "research §X for me", "what's the current law on Y",
  "find me authority for Z", "is there a Rev. Rul. on …",
  "what did the Tax Court say about …", "Tax Cuts and Jobs Act / IRA /
  OBBBA / SECURE 2.0 changes to §X", "legislative history of §X", or
  pastes a fact pattern asking for a memorandum-style answer. Make
  sure to use this skill whenever the user mentions IRC, Treas. Reg.,
  Rev. Rul., Rev. Proc., Notice, PLR, Tax Court, circuit-court, JCT
  Bluebook, Greenbook, or CBO score.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# tax-research-federal — Federal income-tax research

Flagship research skill. Produces a memorandum-style answer with
explicit authority weighting, confidence band, disclosure flag, and
a JSON sidecar.

## Read before output

Before producing any output, read in order:

1. `shared/citation-discipline.md` — fabrication ban, sentinel format,
   negative-treatment-detection limitation.
2. `shared/authority-hierarchy.md` — weights, Loper Bright, Golsen.
3. `shared/confidence-bands.md` — band definitions and decay rules.
4. `shared/compliance.md` — SSTS / Circular 230 checklist.
5. `shared/legislation-tracking.md` — when the question touches a
   recent Public Law (TCJA, CARES, ARPA, IRA, SECURE 2.0, OBBBA, or
   any post-2024 amendment).
6. `references/authority-weights.md` — federal-specific weighting notes.
7. `references/retrieval-checklist.md` — order of operations.
8. `references/legislative-history.md` — JCT Bluebook, committee
   reports, Greenbook, CBO workflow when the question implicates
   legislative-history reasoning.

## Workflow

### 1. Intake

Capture the minimum facts needed. Default intake schema:

- `taxpayer_type`: individual | C-corp | S-corp | partnership |
  trust | estate | tax-exempt | other
- `taxpayer_circuit`: e.g., "9th Cir." (for Golsen weighting)
- `tax_year`: integer
- `issue`: free text
- `prior_positions`: any reliance facts material to penalty analysis
- `dollar_amount_at_issue`: integer | "n/a" (for materiality)
- `public_laws_implicated`: list of popular names if user mentioned
  any (route via `irc-section-lookup` first if so)

If a fact is missing and material (e.g., taxpayer's circuit for a
Court-of-Appeals split question), request it. Otherwise, proceed with
a labeled assumption.

### 2. Analysis

Walk the authority hierarchy in this order:

1. **Statute** — IRC text at uscode.house.gov USLM. Quote the
   operative subsection/paragraph.
2. **Regulations** — eCFR Title 26. Distinguish final / temporary /
   proposed. Flag `chevron_replaced: true` for any reg interpreting
   ambiguous statutory text post-Loper Bright.
3. **Binding judicial** — Supreme Court, then Court of Appeals
   binding in the taxpayer's circuit (Golsen), then Tax Court / DCt /
   Court of Federal Claims.
4. **IRS published** — Rev. Ruls., Rev. Procs., Notices,
   Announcements (IRB-published).
5. **Legislative history** — JCT Bluebook → committee reports →
   conference report → Greenbook (only `legislative_history` weight
   if proposal enacted in same form) → CBO score.
6. **Written determinations** — PLR, TAM, CCA, GCM, AOD, FSA,
   Office Memorandum, Information Letter (citable, but `§ 6110(k)(3)`
   no precedential value to other taxpayers).
7. **Persuasive non-authority** — IRS Pubs, IRM, Forms/Instructions,
   ATG, ISP Coordinated Issue Papers, IRS News Releases. Never the
   closest authority; cap conclusions to "describes IRS practice"
   unless paired with higher-tier authority.
8. **Not authority** — treatises, blogs, AI summaries.

For each contested proposition, list authorities supporting AND
contrary, with weight. Identify any circuit split.

### 3. Conclusion

State the conclusion in one paragraph. Assign `confidence_band` per
`shared/confidence-bands.md`:

- HIGH (≥ 70% / "should" or "will") — primary statute on point + no
  contrary controlling authority.
- MODERATE (~ 40–50% / "substantial authority") — well-supported by
  authority but contrary authority exists OR Reg-only basis on a
  Loper-Bright-vulnerable interpretation.
- LOW (~ 20–35% / "reasonable basis") — supportable but vulnerable;
  recommend Form 8275 / 8275-R disclosure.
- SPECULATIVE — do not recommend.

Note disclosure forms recommended (8275 / 8275-R / 8886) and any
penalty exposure under § 6662(b).

### 4. Authorities

Every cited authority MUST appear in the JSON sidecar with all
required fields: `authority_type, citation, url, retrieved_date,
quoted_text (≤75 words), weight`. When a primary source is
unreachable, emit the sentinel pattern documented in
`shared/citation-discipline.md` rather than fabricating; record an
entry in `unresolved_citations[]` simultaneously.

For Public-Law-touching questions, populate `public_laws_consulted[]`
with the popular name, Public Law number, classification-tables URL,
and `affected_irc_sections[]` per `shared/legislation-tracking.md`.

### 5. JSON sidecar

Emit a JSON object validating against `shared/output-schema.json`,
following the markdown response. Include
`negative_treatment_review_required: true` for any high-stakes
position (dollar amount > $50K, novel argument, or position that
relies on a Tax Court or Court of Appeals case as the closest
authority).

## Hard rules

- Never fabricate IRC sections, Reg cites, case names, PLR numbers,
  Public Law numbers, or quoted-text excerpts.
- Never claim Chevron deference for Treasury Regs (post-Loper Bright,
  144 S. Ct. 2244 (2024)). Use Skidmore framework.
- Never recommend a position with a SPECULATIVE band.
- Never let TaxProf Blog, Procedurally Taxing, Tax Foundation, Tax
  Policy Center drive the band. They are `not_authority` or at most
  `persuasive_non_authority`.
- Never use a PLR/TAM/CCA/GCM/AOD/FSA/Office-Memo/Info-Letter as the
  closest authority for a high-band conclusion (drop one band per
  decay rule).
- For state questions, decline and route to `tax-research-state-income`
  or `tax-research-state-salesuse`.
- For estate/gift, route to `tax-research-estate-gift`.
- For procedure (audits, SoL, Tax Court rules, DAWSON), route to
  `tax-research-procedure`.
- Always include the verification checklist appendix.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist from
`shared/compliance.md` (SSTS § 1.1, § 2.3; Circular 230 § 10.22,
§ 10.35, § 10.37; negative-treatment review residual responsibility).
