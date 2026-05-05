---
name: compliance-ssars
description: |
  Walks Statements on Standards for Accounting and Review Services
  (SSARS) for a given engagement. Routes between AR-C 60 (general
  principles), AR-C 70 (preparation), AR-C 80 (compilation), and
  AR-C 90 (review) based on engagement scope. Produces required-
  procedures checklist, going-concern considerations, lack-of-
  independence handling for compilations, and review-engagement
  inquiry/analytical-procedure scope. Routes audits to
  compliance-sas-audit and other attest engagements to
  compliance-attestation-qm. Use when the user asks "compilation",
  "review engagement", "AR-C", "SSARS", "preparation engagement",
  "review report", "compilation report", "going concern review",
  "no assurance", or "limited assurance". Make sure to use this
  skill whenever the user mentions SSARS, AR-C, compilation,
  review, preparation, or limited-assurance engagements.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# compliance-ssars — SSARS engagement standards (AR-C)

Routes between the four SSARS engagement types and applies the
required procedures and reporting standards for each. SSARS
applies to **nonissuer** entities; issuer engagements fall under
PCAOB AS (out of scope — route externally).

## Read before output

1. `shared/citation-discipline.md` — fabrication ban; the
   `authority_domain: professional_conduct` ladder.
2. `shared/authority-hierarchy.md` — Professional Standards subsection
   (Phase 9): SSARS / AR-C as `binding_on_member`.
3. `shared/confidence-bands.md` — band assignment.
4. `shared/compliance.md` — AICPA Code module + engagement-letter
   required-elements module.
5. `references/ar-c-60.md` — general principles for all SSARS
   engagements.
6. `references/ar-c-70-preparation.md` — preparation engagements
   (no report).
7. `references/ar-c-80-compilation.md` — compilation engagements
   (no assurance, includes lack-of-independence handling).
8. `references/ar-c-90-review.md` — review engagements (limited
   assurance via inquiry + analytical procedures).

## Operative authority

- AICPA SSARS — currently effective:
  https://www.aicpa-cima.com/resources/download/aicpa-ssarss-currently-effective
- Cite as `authority_domain: professional_conduct`,
  `authority_type: AICPA_SSARS`, `weight: binding_on_member`.

## Workflow

### 1. Intake

- `engagement_type`: preparation | compilation | review | unsure
- `entity_type`: nonissuer (required for SSARS) | issuer (route to
  PCAOB externally) | governmental (route to GASB / Yellow Book
  externally)
- `independence_status`: independent | not independent (drives
  AR-C 80.27 lack-of-independence path; precludes AR-C 90 review)
- `financial_statement_framework`: GAAP | tax basis | cash basis |
  contractual basis | regulatory basis | other-special-purpose
- `going_concern_indicators`: list any indicators (recurring losses,
  negative cash flow, debt-covenant violation, loss of major
  customer, etc.)
- `engagement_letter_status`: signed | drafted | not yet — required
  before any SSARS engagement begins (AR-C 60.A21)

### 2. Issuer / governmental routing screen

If `entity_type = issuer`: route to PCAOB externally (out of scope).
If `entity_type = governmental` and the engagement is governed by
GAGAS / Single Audit: route to GAO Yellow Book externally. SSARS
applies to nonissuer attest review/compilation/preparation only.

### 3. Engagement-type routing

Based on `engagement_type` and the level of service the practitioner
will provide:

- **Preparation (AR-C 70)** — practitioner prepares financial
  statements but provides NO assurance and issues NO report. Each
  page of the F/S must include "no assurance is provided" or a
  similar statement. See `references/ar-c-70-preparation.md`.
- **Compilation (AR-C 80)** — practitioner assists in presenting
  financial statements but provides NO assurance. Issues a
  compilation report. May be performed without independence (with
  required disclosure). See `references/ar-c-80-compilation.md`.
- **Review (AR-C 90)** — practitioner provides LIMITED assurance via
  inquiry + analytical procedures. Issues a review report.
  Independence is REQUIRED (no "lack of independence" path).
  See `references/ar-c-90-review.md`.

If `engagement_type = unsure`, ask the user: "What level of service
does the client need? (a) prepared statements only, no report;
(b) compilation, no assurance, with report; (c) review, limited
assurance, with report; (d) audit." Route accordingly. Audit → route
to `compliance-sas-audit`.

### 4. AR-C 60 general principles (apply to all SSARS engagements)

Walk `references/ar-c-60.md`:

- [ ] Engagement letter signed before work commences (AR-C 60.A21).
- [ ] Practitioner has competence and capabilities (AR-C 60.16).
- [ ] Practitioner complies with relevant ethical requirements
      (AICPA Code; route to `compliance-aicpa-code` for threats /
      §1.295 / state overlay).
- [ ] Documentation sufficient to support the report or NO-report
      conclusion.
- [ ] Quality control under SQMS 1 / SQMS 2 (route to
      `compliance-attestation-qm` for firm-level QM scaffolding).

### 5. Engagement-specific procedures

Walk the relevant `references/ar-c-NN-*.md` file.

### 6. Going-concern considerations

For compilation and review engagements (NOT preparation):
- AR-C 80.A24 (compilation): if practitioner becomes aware of
  conditions or events that raise substantial doubt about the
  entity's ability to continue as a going concern, and management
  has not addressed them in the financial statements, the
  practitioner should request management to consider the matter.
  If management refuses, modify or withdraw.
- AR-C 90.65 (review): the practitioner is required to perform
  going-concern procedures consistent with the financial reporting
  framework's going-concern guidance (GAAP: ASC 205-40). If
  substantial doubt exists and is not adequately disclosed, modify
  the review report (emphasis-of-matter or qualified conclusion as
  appropriate).

### 7. Reporting

- Preparation: no report; "no assurance is provided" legend on each
  page (AR-C 70.14).
- Compilation: compilation report per AR-C 80.A8 / .A9; lack-of-
  independence disclosure per AR-C 80.27 if applicable.
- Review: review report per AR-C 90.A99–.A116; modifications for
  GAAP departures, scope limitations, going-concern uncertainty.

### 8. Conclusion

State the engagement-type recommendation (or confirmation), the
required procedures the firm will perform, and the report wording
(by reference to the AR-C illustrative example).

Confidence band per `shared/confidence-bands.md`. SSARS engagements
typically land HIGH or MODERATE on the binding-on-member ladder
because the standards are explicit. LOW band applies when
independence is on the line, going-concern uncertainty is unsettled,
or the engagement type is being elevated mid-engagement.

### 9. JSON sidecar

Emit JSON validating against `shared/output-schema.json`. Use:
- `authority_domain: professional_conduct`.
- `verification_checklist_engagement` populated (engagement letter
  signed, scope clear, fee disclosed, FTC Safeguards if firm
  qualifies as financial institution, lack-of-independence
  disclosure if applicable).

## Hard rules

- Never permit a review engagement when the firm is not independent
  (AR-C 90 has no lack-of-independence path; route to compilation
  with §1.295 lack-of-independence disclosure or decline).
- Never sign a SSARS report without a signed engagement letter.
- Never claim "audit assurance" or "reasonable assurance" in a
  compilation or review report — those are AU-C terms.
- Never apply SSARS to issuer engagements; route to PCAOB.
- Never let an AICPA Practice Aid drive the closest-authority
  citation; always cite the AR-C section directly.

## Verification checklist (appendix)

End the markdown response with the engagement-letter required-
elements module from `shared/compliance.md` and the AICPA Code
module if independence threats were evaluated. The
SSTS/Circular-230 checklist applies only when the engagement is
also a tax engagement.

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
