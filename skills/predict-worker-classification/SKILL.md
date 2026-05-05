---
name: predict-worker-classification
description: |
  Predicts whether a worker should be classified as an employee
  (W-2) or an independent contractor (1099) for federal tax
  purposes, applying the IRS three-category test (behavioral
  control, financial control, relationship of the parties) and the
  Rev. Rul. 87-41 twenty common-law factors, and flagging §530
  relief eligibility. Returns a confidence band and authority
  citations. Use when the user asks "is this person an employee or
  contractor", "should I issue a W-2 or 1099", "the worker / driver
  / consultant / nurse / hairstylist / programmer is …", "we have a
  §530 safe-harbor question", "Form SS-8", "California AB5", "ABC
  test", or asks about reclassification risk. Make sure to use this
  skill whenever the user mentions worker classification, 1099 vs
  W-2, contractor vs employee, ABC test, common-law factors, or
  Section 530.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# predict-worker-classification — Employee vs independent contractor

Flagship prediction skill. Returns one of `employee`, `contractor`,
or `mixed` (different services classified differently), with a
confidence band and § 530 / state ABC-test addenda.

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `references/factors-20.md` — Rev. Rul. 87-41 twenty factors
6. `references/case-law.md` — leading cases by factor pattern

For California or other ABC-test states, also load
`skills/tax-research-state-income/references/states/<XX>.md` (the
state-specific employment definition lives there; for now Phase 3
stubs link to the canonical agency).

## Workflow

### 1. Intake

Capture:

- `service_description`: what the worker actually does
- `client_industry`: e.g., trucking, healthcare, construction,
  professional services
- `worker_type_label`: how the parties currently treat the worker
  (W-2, 1099-NEC, 1099-MISC box 7 legacy, none)
- `behavioral_control_signals`: who instructs / trains / sets work
  schedule
- `financial_control_signals`: who provides tools, expenses, profit
  / loss exposure, services to other clients
- `relationship_signals`: written contract, benefits, permanency,
  integration with regular business operations
- `taxpayer_state`: needed for ABC-test states (CA, MA, NJ, IL, CT,
  others)
- `prior_1099_filings`: relevant to § 530 safe harbor
- `historical_treatment`: how this worker / class of workers has
  been treated previously
- `industry_practice`: relevant to § 530 reasonable-basis prong

### 2. Analysis

Apply the modern **three-category test** (per IRS guidance):

1. **Behavioral control** — instructions, training, evaluation
   systems, location.
2. **Financial control** — significant investment, unreimbursed
   expenses, opportunity for profit or loss, services available to
   the market, method of payment.
3. **Relationship of the parties** — written contracts,
   employee-type benefits, permanency, integration.

Cross-reference Rev. Rul. 87-41's **twenty common-law factors** in
`references/factors-20.md` to identify factor-specific weight.

### 3. § 530 safe-harbor screen (federal only)

§ 530 of the Revenue Act of 1978 (uncodified) bars federal
reclassification by the IRS if the taxpayer:
1. Reasonably relied on (a) judicial precedent, (b) past audit, (c)
   industry practice, OR (d) other reasonable basis;
2. Filed all required Forms 1099 consistent with treatment as a
   contractor; AND
3. Treated all similarly-situated workers as contractors.

If § 530 applies, the federal reclassification risk drops to LOW
even if the common-law analysis tilts to "employee." Note this
explicitly. § 530 does NOT protect against state reclassification.

### 4. State-specific addendum

For ABC-test states (CA Lab. Code § 2775, MA, NJ, others), also
apply the ABC test:

- A: free from control and direction in performance of work.
- B: work is outside the usual course of the hiring entity's
  business.
- C: customarily engaged in an independently established trade,
  occupation, or business.

If any prong is not satisfied, the worker is an employee for state
employment-tax / wage-and-hour purposes — even if the federal IRS
test would classify as a contractor.

CA AB5 codified Dynamex; reference the per-state file at
`skills/tax-research-state-income/references/states/CA.md` (status
may still be `stub`; cap state confidence at LOW until promoted).

### 5. Conclusion

State the predicted classification with confidence band per
`shared/confidence-bands.md`. Examples:

- HIGH: Tight common-law signal + § 530 not implicated + no ABC-test
  state.
- MODERATE: Common-law signal mixed; § 530 may apply; state
  determination consistent.
- LOW: Common-law tilts to employee; § 530 safe harbor uncertain;
  industry-practice prong weak.
- SPECULATIVE: Mixed signals + state ABC test fails + § 530 not
  available — recommend Form SS-8 determination.

Recommend Form SS-8 when the worker or the firm wants an IRS
determination, noting the request typically takes 6 months and the
IRS often defers when a taxpayer files for relief from past
liabilities.

### 6. Authorities

Cite:

- IRC § 3121(d)(2) (employee = common-law employee)
- IRC § 3508 (statutory non-employees: real-estate agents, direct
  sellers)
- Treas. Reg. § 31.3121(d)-1 (common-law employee definition)
- Rev. Rul. 87-41 (twenty common-law factors)
- § 530 of the Revenue Act of 1978 (uncodified — record the
  citation with `authority_type: StatutesAtLarge`)
- Leading cases on point (see `references/case-law.md`)
- For California: CA Lab. Code § 2775; Dynamex Operations W. Inc. v.
  Superior Court, 4 Cal. 5th 903 (2018); AB5

For each, populate the JSON sidecar with `authority_type, citation,
url, retrieved_date, quoted_text (≤75 words), weight`.

### 7. JSON sidecar

Emit JSON validating against `shared/output-schema.json`. Include:

- `task.intake.worker_type_label`, `task.intake.service_description`
- `analysis` = three-category summary + § 530 outcome + ABC outcome
- `conclusion` = "employee" | "contractor" | "mixed"
- `confidence_band`, `band_rationale`
- `disclosure_recommended` (typically false for a classification
  recommendation — disclosure is informational, not a return
  position)
- `authorities[]`
- `state_files_consulted[]` (CA / MA / NJ when implicated)

## Hard rules

- Never produce a classification recommendation without applying
  both the federal three-category test AND the state ABC test in
  ABC-test states.
- Never assert § 530 protection without confirming all three prongs
  and noting that § 530 is federal-only.
- Never claim Chevron deference for Treas. Reg. § 31.3121(d)-1.
- Drop one band for state conclusions when the state file is
  `status: stub`.
- Form SS-8 is informational; the SS-8 determination is binding only
  on the IRS for the specific facts. Disclose this caveat.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`. For high-stakes engagements (large
worker pool, multi-year exposure, or aggressive § 530 reliance),
include the negative-treatment-review residual responsibility.

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
