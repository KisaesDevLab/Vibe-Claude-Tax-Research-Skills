# Audit-engagement workpaper variant (AU-C)

The audit variant builds on the standard scaffold (PBC list +
tickmark legend + lead sheets + indexing) and adds the
audit-specific planning, risk-assessment, fraud-inquiry, going-
concern, and reporting documentation required by the AU-C
clarified standards.

This variant is for **nonissuer** audits only. Issuer audits
follow PCAOB AS standards (out of scope — route externally).
Yellow Book / GAGAS audits add governmental-overlay documentation
(out of scope — route externally).

## Required planning workpapers

Every audit file must include each of the following in the
planning section (100-series).

### 110 — Engagement letter
Per AU-C §210. Signed before fieldwork begins. Attached:
preceding-period engagement letter for context (continuing
engagements).

### 120 — Independence assessment
Per AICPA Code §1.200 (threats-and-safeguards conceptual
framework). Documented threats considered (self-review, advocacy,
familiarity, self-interest, undue influence, management
participation), safeguards applied, and conclusion that
independence is at an acceptable level. State-board overlay
applied when engagement state is in CA / NY / TX (or other
stricter jurisdictions per `shared/sources.json`
state_boards_of_accountancy).

### 130 — Risk-assessment memo
Per AU-C §315. Documents the auditor's understanding of the
entity, its environment, and its system of internal control,
including:

- Industry, regulatory, and other external factors.
- Nature of the entity (operations, ownership, governance,
  financing, accounting).
- Objectives, strategies, and related business risks.
- Measurement and review of financial performance.
- The control environment, risk-assessment process, information
  system relevant to financial reporting, control activities, and
  monitoring of controls.

The memo identifies and assesses risks of material misstatement
(RMM) at:
- The financial-statement level.
- The relevant-assertion level for material classes of
  transactions, account balances, and disclosures.

### 140 — Materiality determination memo
Per AU-C §320. Documents:
- Materiality at the F/S level (typically a percentage of pre-tax
  income, revenue, or total assets — firm methodology governs).
- Performance materiality (a percentage of materiality, e.g., 50–
  75%).
- Trivial-threshold (clearly trivial misstatements).
- Materiality applied to particular classes of transactions /
  account balances / disclosures where lower materiality applies.
- Reassessment of materiality during the audit if circumstances
  change.

### 150 — Audit plan / strategy
Per AU-C §300. Includes:
- Scope, timing, and direction of the audit.
- Audit-team composition and supervisory plan.
- Materiality determination reference.
- Significant-risk identification (AU-C §315.27).
- Planned response: tests of controls and/or substantive
  procedures by relevant assertion.

### 160 — Fraud-inquiry memo
Per AU-C §240. Documents:
- Engagement-team discussion (AU-C §240.15) of how the F/S could
  be susceptible to fraud given the facts.
- Inquiries of management and those charged with governance about
  fraud risks.
- Identified fraud risks (revenue recognition is presumed under
  AU-C §240.26 — the rebuttal must be documented if the auditor
  concludes the presumption does not apply).
- Management override of controls — non-rebuttable; required
  procedures for every audit per AU-C §240.32.
- Specific responses to identified fraud risks at the assertion
  level.

### 170 — Going-concern indicators
Per AU-C §570 and ASC 205-40. Required when indicators are
present (recurring losses, negative cash flow, debt-covenant
violation, loss of major customer, etc.). Documents:
- Indicators identified.
- Management's evaluation of the entity's ability to continue as
  a going concern.
- Management's mitigation plans (if applicable) and the
  evaluation of whether mitigation is probable.
- Auditor conclusion: substantial doubt resolved (proceed with
  unmodified opinion + emphasis-of-matter when ASC 205-40
  disclosure is adequate) OR substantial doubt unresolved
  (modify the opinion).

## Required substantive workpapers

Every material F/S caption gets:
- Lead sheet (caption letter — e.g., `A`).
- Sub-leads as needed.
- Substantive procedures responsive to the assessed RMM at the
  relevant-assertion level.
- For tests of details: scope-statement, sample-selection memo,
  results, conclusion.
- For analytical procedures: expectation development, results,
  follow-up of significant differences (AU-C §520).
- For confirmations: confirmation log + responses + alternative
  procedures if applicable (AU-C §505).

## Required wrap-up workpapers

### 900 — Subsequent-events review
Per AU-C §560. Covers from period-end through the report-release
date. Procedures: review of post-period bank statements, review
of post-period AR collections / AP disbursements, inquiry of
management about subsequent events, review of subsequent
litigation / regulatory developments.

### 910 — Management representation letter
Per AU-C §580. Required of every audit. Dated as of the report-
release date. Signed by management (typically CEO and CFO).
Required representations specific to AU-C §580.10 + engagement-
specific representations.

### 920 — Governance communication
Per AU-C §260. Delivered to those charged with governance
(typically audit committee or board for entities with such
oversight). Topics: significant findings, significant accounting
policies, judgments, estimates, audit-adjustments, uncorrected
misstatements, written representations, illegal acts identified,
and other items per AU-C §260.A12.

### 930 — Draft F/S
The F/S draft as of the report-release date. Tied to the lead
sheets and supporting workpapers.

### 940 — Draft audit report
Per AU-C §700–§706 (unmodified) or §705 (modified). Identifies
the framework, materiality, opinion. Emphasis-of-matter or
key audit matters (KAM) as applicable.

### 950 — EQR review (SQMS 2 when required)
Per SQMS 2. Required for: listed entities, entities of public
interest as defined by the firm's QM system, and other
engagements specified by firm policy. Independent reviewer (not
an engagement-team member) reviews significant judgments,
F/S, and report. Sign-off on independent review before report
release.

### 960 — Open-items / points-forward
Items not resolved that should be addressed in the next year's
engagement. Examples: prior-year audit-adjustment carryover,
pending tax-position resolution, expected accounting-standard
adoption next period.

### 970 — Engagement file lock-down memo
Per AU-C §230.16. Documents the assembly of the final engagement
file within 60 days after the report-release date. After
lock-down, no documentation is added without a documented reason
(AU-C §230.A21–.A24).

## Documentation sufficiency reminders

Per AU-C §230.08, an experienced auditor without prior connection
to the engagement must be able to understand:

- The nature, timing, and extent of audit procedures.
- The audit results and audit evidence obtained.
- Significant matters and conclusions reached, including the
  significant professional judgments made.

Tested-no-exceptions documentation patterns: every test must
document scope, results, and conclusion. "Tested — no exceptions"
is insufficient.

## AU-C §220 supervisory-review pattern

Three sign-offs per workpaper:
- **Preparer** — staff who performed the procedure.
- **Reviewer** — manager or senior who reviewed before partner.
- **Partner** — engagement partner approves the file.

For SQMS 2-required engagements, an Engagement Quality Reviewer
(EQR) provides an independent review of significant judgments
and the F/S / report before issuance.

## Retention

Per AU-C §230.16: 5 years from report-release date is the floor.
AICPA practice is 7 years; many state-board rules align or extend.
Firm policy controls the longer of the applicable minimums.
