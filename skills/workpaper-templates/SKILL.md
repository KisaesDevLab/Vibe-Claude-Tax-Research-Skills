---
name: workpaper-templates
description: |
  Generates audit / review / compilation / preparation / attestation
  workpaper scaffolds: PBC list, tickmark legend, lead sheets,
  alphanumeric indexing convention, plus engagement-specific
  overlays per AU-C §230, AR-C §60.A24–.A29, and AT-C §105.A57–.A66.
  Outputs are template frameworks with `[BRACKETED FIELDS]` paired
  with required-documentation checklists tied to the operative AICPA
  standard and the AU-C §220 / AR-C §60.31 supervisory-review
  framework. PCAOB AS 1215 (issuer audits) and Yellow Book GAGAS
  routed externally. Use when the user asks "build me a workpaper",
  "PBC list", "tickmark legend", "lead sheets", "audit workpapers",
  "review workpaper file", "compilation workpapers", "indexing
  convention", "workpaper retention", or carries a conclusion forward
  into a workpaper. Make sure to use this skill whenever the user
  mentions workpaper, PBC, tickmark, lead sheet, AU-C 230, AR-C
  60.A24, or AT-C 105.A57.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# workpaper-templates — Engagement workpaper scaffolds

Template-generating skill (engagement-letter-library pattern).
Produces the structural workpaper scaffolds — PBC list, tickmark
legend, lead sheets, indexing convention — and the engagement-type
overlay (audit / review / compilation / preparation / attestation)
that the firm uses to populate its actual engagement file.

**Hard rule, prominent:** outputs are *template frameworks*, not
a substitute for performing the engagement. The actual procedures,
evidence, judgments, and conclusions are the practitioner's
responsibility. Workpaper documentation must support each
conclusion; a missing workpaper is a documentation deficiency
under AU-C §230 / AR-C §60.A26 / AT-C §105.A59.

## Read before output

1. `shared/citation-discipline.md` — fabrication ban; the
   `authority_domain: professional_conduct` ladder.
2. `shared/authority-hierarchy.md` — Professional Standards
   subsection (AU-C / AR-C / AT-C / SQMS as `binding_on_member`).
3. `shared/confidence-bands.md` — band assignment.
4. `shared/compliance.md` — engagement-letter required-elements
   module + AICPA Code module.
5. `references/pbc-list.md` — standard PBC categories by
   engagement type and industry.
6. `references/tickmark-legend.md` — common tickmark symbols and
   their meanings.
7. `references/lead-sheet.md` — F/S-line-to-workpaper rollforward
   structure.
8. `references/indexing-convention.md` — alphanumeric indexing
   (permanent file + current file).
9. `references/<engagement-type>-variant.md` — engagement-specific
   documentation overlay (audit / review / compilation).

## Operative authority

- **Audit documentation:** AU-C §230 (Audit Documentation).
  AICPA Statements on Auditing Standards — currently effective:
  https://www.aicpa-cima.com/resources/download/aicpa-statements-on-auditing-standards-currently-effective
- **SSARS documentation:** AR-C §60.A24–.A29 (general principles —
  documentation), §70 / §80 / §90 engagement-specific paragraphs.
  AICPA SSARS — currently effective:
  https://www.aicpa-cima.com/resources/download/aicpa-ssarss-currently-effective
- **Attestation documentation:** AT-C §105.A57–.A66 (Concepts
  Common to All Attestation Engagements — engagement
  documentation).
- **Firm-level engagement file retention:** SQMS 1 — A Firm's
  System of Quality Management — engagement-file retention
  policies; SQMS 2 — engagement quality reviews.
- **Workpaper-review supervisory framework:** AU-C §220 (Quality
  Control for an Engagement); AR-C §60.31; AT-C §105 .A66.

Cite all of the above as `authority_domain: professional_conduct`,
`weight: binding_on_member`, with `authority_type: AICPA_SAS`,
`AICPA_SSARS`, `AICPA_SSAE`, or `AICPA_SQMS` as appropriate.

PCAOB AS 1215 (Audit Documentation — issuer audits) is **out of
scope**; route to PCAOB externally. Yellow Book GAGAS engagement
documentation is **out of scope**; route to GAO externally.

## Workflow

### 1. Intake

- `engagement_type`: audit | review | compilation | preparation |
  attestation-examination | attestation-review | aup | unsure
- `entity_type`: nonissuer (default) | issuer (route to PCAOB
  externally) | governmental (route to GAGAS externally) |
  nonprofit | employee-benefit-plan
- `industry`: free text — drives PBC list customization (e.g.,
  manufacturing → inventory rollforward + cost accounting; SaaS →
  ASC 606 contract review; real estate → ASC 842 lease schedule;
  not-for-profit → restricted-net-asset rollforward)
- `framework`: GAAP | tax basis | cash basis | contractual basis |
  regulatory basis | other-special-purpose
- `prior_year_engagement`: continuing | first-year | predecessor-
  to-successor (drives opening-balance / predecessor-auditor
  procedures under AU-C §510)
- `accounting_system`: e.g., QuickBooks Online, Xero, Sage
  Intacct, NetSuite, manual — drives PBC export instructions
- `materiality_known`: yes (provide) | no (will set during planning)
- `firm_workpaper_software`: e.g., CCH ProSystem fx Engagement,
  Caseware, Thomson Reuters Practice CS, Karbon, manual file —
  drives indexing-convention compatibility notes

### 2. Issuer / governmental routing screen

If `entity_type = issuer`: route to PCAOB externally:

> "PCAOB AS 1215 governs issuer-audit documentation. See
> https://pcaobus.org/oversight/standards/auditing-standards/details/AS1215.
> Out of scope here; this skill emits AU-C-based templates only."

If `entity_type = governmental` and engagement is governed by
GAGAS / Single Audit: route externally:

> "Yellow Book (GAGAS) overlays AICPA AU-C documentation
> requirements for governmental audits. See
> https://www.gao.gov/yellowbook. Out of scope here."

### 3. Engagement-type routing

- audit → `references/audit-variant.md` + AU-C §230
- review → `references/review-variant.md` + AR-C §90 +
  AR-C §60.A24
- compilation → `references/compilation-variant.md` + AR-C §80 +
  AR-C §60.A24
- preparation → `references/compilation-variant.md` (preparation
  uses a compressed compilation-style file; AR-C §70 documentation
  is minimal — engagement letter + retained F/S; route to
  `compliance-ssars` if the user needs the engagement-procedure
  walk)
- attestation-examination | attestation-review | aup →
  `references/audit-variant.md` analogue + AT-C §105.A57; consider
  routing to `compliance-attestation-qm` for SQMS / engagement-
  quality-review overlay
- unsure → ask: "What level of service does the engagement
  require? (a) audit, reasonable assurance; (b) review, limited
  assurance; (c) compilation, no assurance; (d) preparation, no
  report; (e) attestation engagement (specify subject matter)."

### 4. Standard components (apply to every engagement)

For every engagement type, emit four standard components:

**a. PBC list** — from `references/pbc-list.md`. Customize by
engagement type, industry, and framework. PBC list goes to client
typically 3–6 weeks before fieldwork; tracks each item with
`requested_date`, `received_date`, `received_by`, `WP_index`.

**b. Tickmark legend** — from `references/tickmark-legend.md`.
Single page applied to every workpaper in the engagement. Common
tickmarks: cross-foot (CF), agree to TB (✓), agree to confirmation
(C), traced to bank statement (BS), traced to subsequent payment
(SP), recalculated (R), examined invoice (I), verbal inquiry (V),
no exception (NE).

**c. Lead sheet structure** — from `references/lead-sheet.md`.
F/S-line-driven rollforward: beginning balance → movements (with
WP cross-references) → ending balance → tied to TB. One lead
sheet per F/S caption; sub-leads for material accounts.

**d. Indexing convention** — from `references/indexing-convention.md`.
Permanent file (PF-1 articles, PF-2 bylaws, PF-3 minutes, PF-4
contracts, etc.) + current file (alphanumeric — A=Cash, B=AR,
C=Inventory, D=Fixed Assets, E=Investments, F=Prepaid, G=Other
Assets; H–J=Equity; K–L=Liabilities; M=Debt; N=Income/Loss
sections; etc.). Adapt to firm software conventions.

### 5. Engagement-specific overlay

Walk the relevant `references/<engagement-type>-variant.md`. The
overlay specifies:

- Required planning documents (engagement letter, independence
  evaluation, materiality memo for audits, risk-assessment memo,
  fraud-inquiry memo for audits).
- Required substantive workpapers tied to AU-C §330 / AR-C §90.18
  procedures.
- Going-concern documentation per AU-C §570 / AR-C §90.65.
- Reporting documentation (draft report, management rep letter,
  governance communication for audits per AU-C §260).
- Subsequent-events review (AU-C §560 for audits; AR-C §90.81 for
  reviews; AR-C §80.A15 for compilations).
- Wrap-up documentation: review notes (preparer/reviewer/partner),
  open-items list, points-forward memo for next year.

### 6. Documentation sufficiency rule

Per AU-C §230.08 / AR-C §60.A26 / AT-C §105.A59, documentation
must be sufficient to enable an experienced auditor (or
practitioner) without prior connection to the engagement to
understand:

- The nature, timing, and extent of procedures performed.
- The results of procedures and the audit evidence (or, for
  SSARS, the F/S-preparation evidence) obtained.
- Significant matters arising and conclusions reached on them,
  and the significant professional judgments made.

Each lead sheet, sub-lead, and procedure workpaper must satisfy
this standard. The skill flags weak documentation patterns:
- "Tested — no exceptions" without scope description → deficiency.
- Tickmarks without a legend on the workpaper → deficiency.
- A conclusion without underlying support → deficiency.

### 7. Workpaper-review supervisory framework

Per AU-C §220.18 / AR-C §60.31:

- **Preparer:** the staff member who performed the procedure
  signs and dates the workpaper.
- **Reviewer:** a more-experienced engagement-team member reviews
  for sufficiency, conclusion support, and adherence to firm
  methodology. Signs and dates with reviewer initials.
- **Engagement partner:** reviews critical workpapers and signs off
  on the engagement file as a whole. For SQMS 2-required
  engagements, an Engagement Quality Reviewer (EQR) performs an
  independent review of significant judgments.

Three-sign-off pattern: prepared / reviewed / partner-approved.
Document any review notes raised and how cleared.

### 8. Retention

- AU-C §230.16: assemble the final engagement file within 60 days
  after the report-release date; retain at least 5 years from the
  report release date.
- AICPA practice (and many state-board rules): 7 years.
- SQMS 1: firm-level retention policies extend or align with the
  longer of state-board, regulatory, or firm-policy minimum.
- Statute-of-limitations exposure (malpractice): often longer than
  AU-C §230.16; firm counsel sets the firm-wide retention horizon.

### 9. Output

Generate the workpaper scaffold package:

1. **Engagement summary** — entity, framework, period, partner,
   manager, in-charge, anticipated report date.
2. **PBC list** — customized table per `references/pbc-list.md`.
3. **Tickmark legend** — single-page reference.
4. **Lead-sheet template (master)** — one row per F/S caption,
   linked to current-file index.
5. **Indexing convention** — permanent file + current file
   structure.
6. **Engagement-specific overlay** — audit / review / compilation
   variant document set.
7. **Required-documentation checklist** — per engagement type,
   tied to the operative AICPA standard.
8. **Practitioner notes** — flag documentation-sufficiency
   reminders, retention period, supervisory-review pattern.

Conclude with: "This is a TEMPLATE FRAMEWORK. The firm must
customize each scaffold to match firm methodology, software,
client industry, and engagement-specific judgments. Workpaper
templates do NOT substitute for performing the engagement; the
actual procedures, evidence, judgments, and conclusions are the
practitioner's responsibility."

### 10. Conclusion + sidecar

- `legal_review_required: false` (workpapers are firm-internal —
  contrast engagement letters which are client-facing legal
  documents).
- `verification_checklist_engagement` populated.
- Confidence band: typically MODERATE (template framework
  correctness) when the engagement is standard. HIGH for
  conventional GAAP audits / SSARS engagements; LOW when the
  engagement involves novel framework, complex consolidation,
  multi-component group audits, or industry-specific methodology
  the firm has not encountered.
- Cite the operative AICPA standard with
  `authority_domain: professional_conduct`,
  `weight: binding_on_member`.

## Hard rules

- Output is a TEMPLATE FRAMEWORK, not a substitute for performing
  the engagement. The actual procedures, evidence, judgments, and
  conclusions are the practitioner's responsibility.
- Never represent that a populated workpaper template constitutes
  audit / review / compilation evidence; evidence is what the
  practitioner gathers and tests.
- Never apply PCAOB AS 1215 documentation requirements — route
  externally for issuer audits.
- Never apply Yellow Book GAGAS documentation requirements — route
  externally for governmental engagements with federal-grant
  exposure.
- Never claim Chevron or Skidmore deference for AU-C / AR-C /
  AT-C / SQMS standards.
- Always require a signed engagement letter (AU-C §210 / AR-C
  §60.A21 / AT-C §105.A18) before populating workpaper templates;
  a workpaper file without an engagement letter is missing the
  predicate documentation.
- Always include the documentation-sufficiency rule (AU-C §230.08
  / AR-C §60.A26 / AT-C §105.A59) as a practitioner reminder in
  the output.
- Always include the supervisory-review three-sign-off pattern
  (preparer / reviewer / partner) per AU-C §220 / AR-C §60.31.
- Always note retention horizon: AU-C §230.16 (5 years) is the
  floor; AICPA practice (7 years) and state-board rules often
  longer; firm policy controls.

## Verification checklist (appendix)

End the markdown response with the engagement-letter required-
elements module + AICPA Code module from `shared/compliance.md`.
SSTS / Circular 230 applies only when the engagement is paired
with a tax engagement.

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
