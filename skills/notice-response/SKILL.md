---
name: notice-response
description: |
  Drafts an IRS-notice response: identifies the notice type (CP /
  Letter / LT), determines the deadline, frames the response strategy
  (agree, partial agree, disagree, request additional time, request
  CDP), and produces a well-organized response letter with cited
  authorities. Routes to specialized skills (predict-reasonable-cause,
  predict-innocent-spouse, tax-research-procedure) for substantive
  positions. Use when the user asks "respond to this IRS notice",
  "CP2000", "CP14", "Letter 525", "Letter 950", "Notice of
  Deficiency", "30-day letter", "90-day letter", "what does this
  notice mean", "draft a notice response", or "audit response
  letter". Make sure to use this skill whenever the user mentions
  IRS notice, CP notice, Letter NN, audit response, or
  notice-response letter.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# notice-response — IRS notice triage and response

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `references/notice-catalog.md` — common CP / Letter / LT
   notices with deadlines and response paths.
6. `references/response-templates.md` — letter-format scaffolds.

## Workflow

### 1. Intake

Gather:
- `notice_id`: e.g., CP2000, CP14, CP504, Letter 525, Letter 950,
  Letter 1058, Letter 3219, Letter 1153, etc.
- `notice_date`: critical for deadline computation.
- `tax_year(s)` at issue.
- `proposed_or_assessed_amount`.
- `notice_text`: full text or scanned image; extract and preserve.
- `taxpayer_facts`: prior compliance, payment history, return
  positions taken.

### 2. Notice triage

Identify the notice category:

#### CP series — automated correspondence

CP2000 — proposed adjustment based on third-party-information
matching (W-2, 1099, K-1). 30-day response window. Does NOT count
as statutory notice of deficiency.

CP2501 — request for clarification before CP2000.

CP14 — first balance-due notice; 21 days to pay or call.

CP501 / CP503 / CP504 — collection escalation series; CP504 is
final pre-levy notice for state tax refund offset.

CP90 / CP91 — Final Notice of Intent to Levy and Notice of Your
Right to a Hearing (CDP — §6330).

#### Letter series — examination and adjudicatory

Letter 525 — Examination Report (30-day letter); response window
30 days to agree or appeal to Appeals.

Letter 692 — request for response to Letter 525.

Letter 915 — examination report.

Letter 950 — 30-day letter for excise / employment.

Letter 1058 — Final Notice of Intent to Levy (parallel to CP90).

Letter 1153 — Trust Fund Recovery Penalty proposed assessment;
60-day window for protest to Appeals.

Letter 3172 — Notice of Federal Tax Lien filing (CDP — §6320).

Letter 3219 — Statutory Notice of Deficiency (90-day letter, 150
days outside U.S.). JURISDICTIONAL Tax Court petition deadline.

Letter 4314C — request for missing return.

LT11 — Final notice for outstanding return.

#### LT series — automated collection

LT11 — final notice with intent to levy; CDP rights.

### 3. Deadline computation

Compute the response deadline. Common deadlines:

| Notice | Deadline | Statute |
|---|---|---|
| CP2000 | 30 days | none (administrative) |
| Letter 525 (30-day letter) | 30 days | administrative |
| Letter 1058 / CP90 (CDP) | 30 days | §6330(a) |
| Letter 3172 (CDP — lien) | 30 days | §6320(a) |
| Letter 1153 (TFRP) | 60 days | §6672 / IRM |
| Letter 3219 (stat notice) | 90 days (150 outside U.S.) | §6213(a) |

Calendar the deadline immediately. Missed CDP / 90-day deadlines
can be jurisdictionally fatal.

### 4. Response-path selection

| Posture | Path |
|---|---|
| Agree with notice | sign Form 870 / 4549 / similar; pay or arrange payment |
| Partial agree | itemized response identifying agreed and disputed adjustments |
| Disagree (CP2000) | written response with substantiating documentation |
| Disagree (Letter 525) | request Appeals Conference (Pub. 5) |
| Statutory Notice (Letter 3219) | Tax Court petition within 90 days |
| TFRP (Letter 1153) | protest to Appeals within 60 days |
| Levy / lien (CDP) | CDP request within 30 days |
| Penalty assessment | reasonable-cause / FTA request → route to `predict-reasonable-cause` |
| Joint-liability spouse defense | route to `predict-innocent-spouse` |

### 5. Substantive position routing

- Reasonable-cause / FTA → `predict-reasonable-cause`.
- Innocent-spouse → `predict-innocent-spouse`.
- Worker-classification / TFRP → `predict-worker-classification`
  + `tax-research-payroll`.
- Statute-of-limitations defense → `tax-research-procedure`.
- §7430 cost recovery → `tax-research-procedure`.
- Levy / lien CDP → `tax-research-procedure`.
- ESD / §6662(b)(6) → `predict-economic-substance`.

### 6. Drafting

Use the format in `references/response-templates.md`:

1. Letter heading with taxpayer name, EIN/SSN (redacted in any
   draft; final letter has full information), tax year, notice
   number, response deadline.
2. Statement of position: agree / partial agree / disagree.
3. Statement of facts.
4. Application of law to facts (cite authorities).
5. Documentation list (attached or referenced).
6. Specific request: abatement, appeals conference, hearing, etc.
7. Closing: signature, date, contact information.

### 7. Conclusion + sidecar

JSON sidecar validates against `shared/output-schema.json`. The
`conclusion` is the response strategy (e.g., "Recommend Appeals
Conference request with substantiation of charitable-contribution
deductions; cite §170(f)(8) substantiation requirements and
§6664(c)(1) reasonable-cause defense.").

`confidence_band` reflects the merits of the substantive position.
Cite authorities supporting the response position.

## Hard rules

- Always confirm the deadline FIRST before drafting. Missed
  deadlines (90-day, CDP) are jurisdictionally fatal.
- Always run the FTA screen for §6651 family penalties; many
  practitioners miss this easy path.
- Never recommend non-response on a Letter 3219 (90-day letter);
  even a "no merit" position should preserve Tax Court rights.
- Never sign Form 872 (consent to extend SOL) without
  understanding the consequence; it CAN be the right move but
  should be deliberate.
- Never address a Letter 1153 without considering joint-and-
  several §6672 liability and contribution rights.
- For Letter 3219, file petition AS A PROTECTIVE MATTER even if
  settlement is in progress; the deadline does not toll for
  ongoing negotiations.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`. For high-stakes notice responses
(six-figure assessment, criminal-investigation overlay), include
the negative-treatment-review residual practitioner responsibility.

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
