---
name: tax-research-procedure
description: |
  Federal tax-procedure research skill covering audits, statutes of
  limitations (assessment §6501; collection §6502; refund claims
  §6511), Tax Court litigation, CDP (Collection Due Process) §6320 /
  §6330, summons and §7602 power, Appeals procedure, IRS notice and
  protest mechanics, DOJ Tax Division roles, and DAWSON / Today's
  Opinions freshness signals. Use when the user asks "audit
  procedure", "SOL", "statute of limitations", "Tax Court", "CDP
  hearing", "collection due process", "Appeals", "summons",
  "§7602", "DAWSON", "DOJ tax", "refund claim §6511", "§6411 NOL
  carryback", "tentative refund", or "TFRA appeals". Make sure to
  use this skill whenever the user mentions audit procedure, Tax
  Court, CDP, Appeals, summons, or statute of limitations.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# tax-research-procedure — Audits, SOL, Tax Court, Appeals

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `references/sol-and-assessment.md` — §6501 / §6502 / §6511 with
   tolling and exceptions.
6. `references/tax-court-rules.md` — Tax Court jurisdiction,
   pleading, discovery, trial, appeals.
7. `references/doj-tax-division.md` — DOJ Tax Division civil and
   criminal roles.
8. `references/irs-data-book-audit-rates.md` — IRS Data Book audit
   rates and trends (persuasive_non_authority for client-
   communication context).
9. `references/dawson-freshness-feeds.md` — DAWSON Today's Opinions
   / Today's Orders freshness signals for negative-treatment-
   detection mitigation.

## Operative authority

- IRC §6501 — period of limitation on assessment.
- IRC §6502 — collection statute (10 years).
- IRC §6511 — refund-claim deadline.
- IRC §6320 — CDP for liens.
- IRC §6330 — CDP for levies.
- IRC §6213 — petition to Tax Court (90-day letter / 150-day for
  out-of-country).
- IRC §7602 — IRS summons authority.
- IRC §7605 — restrictions on examinations.
- IRC §7430 — recovery of administrative and litigation costs.
- IRC §7602(d) / §7611 / §7491 — specific procedural provisions.
- IRC §6411 — tentative refund (carryback).
- Tax Court Rules of Practice and Procedure.
- IRM Part 5 — Collecting Process; Part 8 — Appeals; Part 35 —
  Tax Court Litigation.

## Workflow

### 1. Intake

- `procedural_posture`: at exam / unagreed / 30-day letter / 90-day
  letter / Tax Court petition / CDP / collection
- `tax_year(s)` at issue and assessment dates
- `taxpayer_circuit`
- `dollars_at_issue` and small-case (S-case) eligibility
  (§7463 — ≤ $50K)
- `relevant_dates`: filing, examination opening, notice issuance,
  petition deadlines
- `protective_filings`: protective claim under §6511(a) preserved

### 2. Statute-of-limitations gate

§6501(a) — 3 years from later of return filing or due date.
§6501(c) — exceptions:
- (1) False or fraudulent return: no SOL.
- (3) Failure to file return: no SOL until return filed.
- (4) Substantial omission of income: 6-year SOL (§6501(e)).
- (8) Listed transactions and reportable transactions: 1-year
  extension after disclosure.
- (10) Unfiled or amended foreign-information returns: 3-year
  extension (§6501(c)(8)).

§6501(b) flush — early-filed returns are deemed filed on the due
date.

§6502 — 10-year collection statute starting at assessment date.

§6511 — refund claim:
- 3 years from return filing OR
- 2 years from tax payment, whichever is LATER.
- §6511(a) protective claim must specify grounds.

### 3. Tax Court jurisdiction

§6213(a) — petition within 90 days of statutory notice of
deficiency (150 days if addressed outside the U.S.). Filing in
Tax Court suspends collection.

§7442 — Tax Court has jurisdiction over deficiencies in income,
estate, gift, generation-skipping transfer, and excise taxes.

§7459 — Tax Court decisions become final 90 days after entry
unless timely appealed.

Small-tax-case (S-case) procedure under §7463:
- Available for amounts ≤ $50,000 per year.
- Streamlined procedures.
- Decision NOT appealable.

### 4. CDP — §6320 / §6330

§6320 — pre-lien CDP. Notice of Federal Tax Lien filed; taxpayer
has 30 days to request CDP hearing.

§6330 — pre-levy CDP. Final Notice of Intent to Levy issued;
taxpayer has 30 days.

CDP issues:
- Verification that procedure followed.
- Spousal defenses (innocent-spouse).
- Challenges to underlying liability ONLY if taxpayer did not
  receive a prior opportunity to challenge.
- Collection alternatives (installment agreement, OIC, CNC).

CDP determination appealable to Tax Court (post-2006 amendments).

### 5. Audit procedure

IRS contact letter → opening conference → IDRs (Information
Document Requests) → audit findings → 30-day letter (Form 4549 /
4549-A) → if unagreed, statutory notice of deficiency (90-day
letter).

§7602(a) summons authority. Practitioners should:
- Track IDR responses and deadlines.
- Engage Appeals before 90-day letter when possible (Appeals
  Conference under IRM 8.1).
- Preserve §7430 claims by tracking administrative-cost-eligible
  positions.

### 6. Appeals

Appeals' mission: resolve cases without litigation.
- Hazards-of-litigation analysis available.
- Settlement authority delegated (typically through Form 870
  variants).
- §6404(g) suspension of interest if Appeals delays > 18 months
  (limited applicability).

§7430 — taxpayer may recover administrative costs if the IRS
position was not substantially justified AND the taxpayer
substantially prevailed.

### 7. DOJ Tax Division

Civil litigation:
- Refund suits in District Court / Court of Federal Claims.
- §7401 collection suits.
- §7403 quiet-title actions.
- §7402 injunctions.

Criminal:
- §7201 evasion.
- §7202 willful failure to collect / pay over (TFRP companion).
- §7203 willful failure to file.
- §7206 fraud and false statements.

Practitioners must be aware that DOJ Tax involvement signals
escalation; coordinate with criminal-tax counsel.

### 8. Tax Court freshness signals

DAWSON (Tax Court's e-filing system) publishes:
- Today's Opinions
- Today's Orders

Practitioners should consult DAWSON Today's Opinions / Today's
Orders for freshness signals on cited authorities. See
`references/dawson-freshness-feeds.md` for procedural details.

### 9. Conclusion + sidecar

Confidence band per `shared/confidence-bands.md`. Cite IRC, Treas.
Regs., Tax Court rules, IRM, and case law. JSON sidecar validates
against `shared/output-schema.json`.

## Hard rules

- Always confirm the assessment / petition / refund-claim
  deadline before any procedural recommendation. Missed deadlines
  are jurisdictional.
- Always note whether the taxpayer has a CDP right that has not
  been exhausted.
- Drop one band when relying on an unappealed Tax Court Memorandum
  decision.
- Drop one band when DAWSON Today's Opinions / Today's Orders
  reflect contradicting recent activity.
- Never rely on the IRS Data Book to justify a procedural
  recommendation; cite for client-communication context only.
- Always include the verification checklist appendix.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`. ALWAYS include the negative-treatment-
review residual practitioner responsibility for procedural
positions.
