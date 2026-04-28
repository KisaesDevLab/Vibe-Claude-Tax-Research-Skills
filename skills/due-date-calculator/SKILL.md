---
name: due-date-calculator
description: |
  Computes due dates for federal tax returns, extensions, estimated
  taxes, payroll deposits, information returns, gift-tax returns,
  estate-tax returns, and IRS notice deadlines. Handles weekend /
  holiday adjustment under §7503 and §7508 / §7508A disaster
  extensions. Use when the user asks "when is Form X due", "when
  is the deadline for [tax filing]", "estimated-tax due dates", "Q4
  estimated", "extension deadline", "Form 706 due date", or "§7503
  weekend rule". Make sure to use this skill whenever the user
  mentions a tax filing deadline, extension, or §7503.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# due-date-calculator — Federal due-date computation

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `references/due-date-table.md` — comprehensive due-date table
   for federal returns and deposits.

## Operative authority

- IRC §6072 — date for filing income-tax returns.
- IRC §6075 — date for filing estate / gift-tax returns.
- IRC §6151 — time and place for paying tax.
- IRC §6081 — extension of time for filing.
- IRC §6161 — extension of time for paying tax.
- IRC §6654 — failure to pay estimated tax (individual).
- IRC §6655 — failure to pay estimated tax (corporation).
- IRC §7503 — Saturday / Sunday / holiday rule.
- IRC §7508 — combat-zone extensions.
- IRC §7508A — disaster-area extensions.

## Workflow

### 1. Intake

- `tax_form` (e.g., 1040, 1120, 1120-S, 1065, 706, 709, 941, 940).
- `tax_period`: tax year + (for quarterly forms) quarter.
- `taxpayer_facts`: fiscal year vs calendar year; outside-U.S.
  status.
- `relevant_event`: e.g., date of death (Form 706), date of gift
  (Form 709), date of return mailing for refund-claim §6511.

### 2. Due-date computation

For each form type:
- Identify the statutory base deadline.
- Apply §7503 weekend / holiday adjustment.
- Apply §7508A disaster extension if applicable (verify against
  IRS announcements).
- Apply §6081 extension if filed.

Common rules:

| Form | Base deadline (calendar year) |
|---|---|
| 1040 | April 15 |
| 1040 (out of country) | June 15 (automatic, with statement) |
| 1120 | April 15 (calendar year) |
| 1120 (fiscal year) | 15th day of 4th month after year end |
| 1120-S | March 15 (calendar year) |
| 1120-S (fiscal year) | 15th day of 3rd month after year end |
| 1065 | March 15 (calendar year) |
| 1065 (fiscal year) | 15th day of 3rd month after year end |
| 706 | 9 months after date of death |
| 709 | April 15 of following year |
| 941 | Last day of month following quarter end |
| 940 | January 31 of following year |
| W-2 / W-3 to SSA | January 31 (employee copy + e-file SSA) / February 28 (paper SSA) |
| 1099 | January 31 (recipient copy + most filers to IRS for 1099-NEC); March 31 e-file IRS (other 1099) |
| 5500 (employee benefit) | Last day of 7th month after plan year end |

### 3. Extension mechanics

| Form | Extension via | Length | Pays tax? |
|---|---|---|---|
| 1040 | Form 4868 | 6 months (October 15) | No (tax must be paid by April 15 to avoid §6651(a)(2)) |
| 1120 | Form 7004 | 6 months | No |
| 1120-S | Form 7004 | 6 months | No |
| 1065 | Form 7004 | 6 months | No |
| 706 | Form 4768 | 6 months | Tax due 9 months from death; extension may extend payment under §6161 |
| 709 | Form 8892 OR Form 4868 (auto for 1040 filers) | 6 months | No |
| 941 | None (file timely or face FTF) | n/a | n/a |

### 4. §6654 / §6655 estimated-tax due dates

Individual (calendar year):
- Q1: April 15
- Q2: June 15
- Q3: September 15
- Q4: January 15 of following year

Corporate (calendar year):
- Q1: April 15
- Q2: June 15
- Q3: September 15
- Q4: December 15

§6654(d)(1)(B) safe harbors:
- 90% of current-year tax; OR
- 100% of prior-year tax (110% if AGI > $150K).

### 5. §7503 weekend / holiday adjustment

If the deadline falls on a Saturday, Sunday, or legal holiday in
the District of Columbia (or in the state of the IRS Service
Center where the return is filed for paper-filed returns), the
deadline is extended to the next business day.

Federal holidays for 2024-2025:
- New Year's Day: January 1.
- MLK Day: 3rd Monday in January.
- Presidents' Day: 3rd Monday in February.
- Memorial Day: last Monday in May.
- Juneteenth: June 19 (federal holiday since 2021).
- Independence Day: July 4.
- Labor Day: 1st Monday in September.
- Columbus Day: 2nd Monday in October.
- Veterans Day: November 11.
- Thanksgiving: 4th Thursday in November.
- Christmas: December 25.

DC-only Emancipation Day: April 16 — historically pushed Tax Day
to April 17 / 18 in some years (e.g., April 18, 2023; April 18,
2022).

### 6. §6511 refund-claim deadline

§6511(a) — claim filed within LATER of:
- 3 years from filing of return; OR
- 2 years from payment of tax.

§6511(b)(2) look-back: refund limited to tax paid within
applicable look-back window.

### 7. §6213 Tax Court petition deadline

90 days from statutory notice of deficiency (Letter 3219); 150
days if mailed outside U.S. JURISDICTIONAL.

### 8. §6320 / §6330 CDP deadlines

30 days from notice of lien filing or final notice of intent to
levy.

### 9. Conclusion + sidecar

JSON sidecar validates against `shared/output-schema.json`. Cite
the relevant IRC section and IRS Pub 509 (Tax Calendars) as
`persuasive_non_authority` for the calendar.

Confidence band per `shared/confidence-bands.md`. HIGH for clean
deadline computations with retrieved year-specific calendar.

## Hard rules

- Always identify the tax year and base deadline.
- Always apply §7503 weekend / holiday adjustment.
- Always check §7508A disaster announcements via the IRS
  newsroom for the relevant period.
- Distinguish FILE deadlines from PAY deadlines.
- Distinguish ADMINISTRATIVE deadlines (CP2000, 30-day letter)
  from JURISDICTIONAL deadlines (90-day Letter 3219, CDP 30-day).
- Always include the verification checklist appendix.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`. Note that missed jurisdictional
deadlines (§6213, §6320, §6330) are typically fatal absent
equitable tolling under Boechler.
