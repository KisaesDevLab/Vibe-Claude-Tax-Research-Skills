---
name: tax-research-payroll
description: |
  Federal payroll-tax research skill covering FICA (§3101 / §3111),
  FUTA (§3301), federal income-tax withholding (§3402), Trust Fund
  Recovery Penalty (§6672), Form 941 reporting, employee vs.
  contractor classification interplay (routes to predict-worker-
  classification), and §530 safe harbor. Use when the user asks
  "payroll tax question", "FICA", "FUTA", "Form 941", "TFRP",
  "Trust Fund Recovery Penalty", "withholding", "§3402", "wage
  base", "household employer", "Schedule H", or "§3508 statutory
  non-employee". Make sure to use this skill whenever the user
  mentions FICA, FUTA, payroll tax, Form 941, TFRP, withholding,
  or wage base.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# tax-research-payroll — Federal payroll-tax research

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `references/withholding-and-fica.md` — §3402 / §3101 / §3111
   mechanics, wage-base / additional-Medicare math.
6. `references/tfrp-and-collection.md` — §6672 personal liability,
   §6020(b) substitute returns, §7501 trust-fund concept.

## Operative authority

- IRC §3101 — FICA (employee share: 6.2% OASDI to wage base; 1.45%
  Medicare uncapped; 0.9% Additional Medicare on wages > $200K
  single / $250K MFJ).
- IRC §3111 — FICA (employer share: 6.2% / 1.45%).
- IRC §3301 — FUTA (employer-only; 6% to first $7,000 wage base;
  net 0.6% after state credit).
- IRC §3401–§3402 — federal income-tax withholding.
- IRC §3508 — statutory non-employees (qualifying real-estate
  agents and direct sellers).
- IRC §6672 — Trust Fund Recovery Penalty (TFRP).
- §530 of the Revenue Act of 1978 (uncodified) — federal worker-
  classification safe harbor.
- Treas. Reg. §31.3121(d)-1 — common-law employee.
- Notice 2009-26 — additional Medicare withholding.
- Pub. 15 (Circular E) — withholding rules and tables.

## Workflow

### 1. Intake

- `employer_type`: business, household, agricultural, foreign
- `employee_classification_question`: route to
  `predict-worker-classification` if disputed
- `tax_period`: quarter / year
- `wage_facts`: total wages, withheld amounts, employer share paid
- `compliance_history`: prior 941 / 944 / 940 filings, assessments,
  TFRP history
- `state_employer_facts`: state UI, state income tax withholding
  (route state-specific to `tax-research-state-income`)

### 2. Classification gate

If the question turns on whether a worker is an employee or
contractor, route to `predict-worker-classification` for the three-
category common-law analysis and §530 safe-harbor screen.

### 3. FICA / FUTA / withholding mechanics

For employee wages:
1. **OASDI (6.2% each side)**: wage base for the year (verify
   year-specific Rev. Proc. or SSA announcement).
2. **Medicare (1.45% each side)**: uncapped.
3. **Additional Medicare (0.9% employee-only)**: wages > $200K
   threshold; employer withholds when ANY single employee's wages
   exceed $200K regardless of filing status.
4. **FUTA (6% employer-only)**: first $7,000 of wages per employee
   per year. Net 0.6% after full state-UI credit.
5. **Federal income-tax withholding**: per Form W-4 and Pub. 15
   tables.

### 4. Trust Fund Recovery Penalty (§6672)

§7501 designates withheld tax as a trust-fund liability. §6672
imposes 100% penalty on responsible persons who willfully fail to
collect, account for, or pay over.

**Responsible person**: anyone with authority and responsibility
to collect, truthfully account for, and pay over the trust-fund
tax. Multiple responsible persons can each be liable for the
entire amount (joint-and-several).

**Willfulness**: voluntary, conscious, intentional act —
encompasses paying other creditors when trust-fund liability is
known and unpaid.

§6672 procedure: Letter 1153, Form 4180 interview, opportunity
for appeals review before assessment. Practitioners should engage
at the Form 4180 interview stage; admissions there can be
dispositive.

### 5. Common employer obligations

Form 941 — quarterly federal income tax / FICA. Due last day of
month following quarter end.
Form 940 — annual FUTA. Due January 31.
Form W-2 / W-3 — January 31 to employees; February 28 paper / March 31
e-file to SSA.
Form 945 — non-payroll income-tax withholding (e.g., backup
withholding, gambling winnings, retirement distributions).
Form 944 — annual employer return (small employers ≤ $1,000
annual employment-tax liability, by IRS designation).

### 6. Household employers (Schedule H)

§3121(a)(7) — domestic-service exception applies if cash wages
< $2,800 per employee for 2024 (verify year-specific). Above
threshold, FICA and FUTA apply.

Schedule H filed with Form 1040; estimated tax may be required to
avoid §6654 penalty.

### 7. §3508 statutory non-employees

Direct sellers and qualifying real-estate agents are NOT
employees for FICA / FUTA / withholding even if they would be
common-law employees. Conditions:
- Substantially all remuneration directly related to sales or
  output (not hours).
- Written contract specifying treatment as non-employee.

### 8. Conclusion + sidecar

Confidence band per `shared/confidence-bands.md`. Cite §§3101,
3111, 3301, 3402, 3508, 6672, 7501, relevant Treas. Regs., and
Pub. 15 (`persuasive_non_authority`). JSON sidecar validates
against `shared/output-schema.json`.

## Hard rules

- Never quote a wage base / threshold without retrieving the year-
  specific Rev. Proc. / SSA announcement.
- Never let Pub. 15 drive a confidence band; use as
  `persuasive_non_authority` only.
- Never claim Chevron deference for Treas. Reg. §31.3121.
- For TFRP cases, advise client to engage counsel before Form 4180
  interview.
- For state employer issues, route to `tax-research-state-income`.
- Always include the verification checklist appendix.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`. For TFRP cases, include the
negative-treatment-review residual practitioner responsibility.

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
