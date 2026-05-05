# Lead sheets

A lead sheet is the F/S-line summary that links the trial balance
to the engagement workpaper file. One lead sheet per material F/S
caption; lead sheets aggregate sub-leads (account-level workpapers)
and all the substantive procedures that support the caption.

## Master lead-sheet structure

For every F/S caption (e.g., "Cash and cash equivalents", "Accounts
receivable, net", "Property and equipment, net"), produce a lead
sheet with this structure:

```
[ENTITY NAME]
[CAPTION] — Lead sheet
For the [year/period] ended [date]
WP index: [e.g., A — Cash]

----------------------------------------------------------------
Beginning balance (PY audited / reviewed / per prior WP):  $X,XXX
   Movements during the period:                                  
     [Movement 1 — e.g., deposits from operations]    +$X,XXX  →  WP A-2
     [Movement 2 — e.g., disbursements]                -$X,XXX  →  WP A-3
     [Movement 3 — e.g., transfers]                    -$X,XXX  →  WP A-4
   Ending balance (per current TB):                        $X,XXX
   Tied to TB account [account number]:                          ✓
----------------------------------------------------------------
Materiality at the F/S level:                                $X,XXX
Performance materiality:                                     $X,XXX
Caption assessed risk:                                       Low / Medium / High
Significant-risk indicator:                                  Yes / No

Procedures performed at this level:
  [ ] Risk assessment for this caption (planning WP).
  [ ] Substantive procedures responsive to RMM.
  [ ] Subsequent-events review (cutoff).
  [ ] Going-concern indicators screen (if applicable).

Cross-references:
  Sub-lead WPs:    A-1, A-2, A-3, ..., A-n
  Substantive procedure WPs:    A-1.1, A-2.1, ..., A-n.1
  Confirmation responses (if any):    A-CONFIRM
  Tickmark legend:    A-0

Conclusion at caption level:
  [ ] All material procedures performed.
  [ ] No exceptions noted (or: exceptions noted — see [WP ref]).
  [ ] Caption presented in accordance with [framework].

Prepared by:  ___________________  Date: ___________________
Reviewed by:  ___________________  Date: ___________________
Partner:      ___________________  Date: ___________________
----------------------------------------------------------------
```

## Sub-lead structure

Sub-leads decompose the lead-sheet caption into account-level
detail. For a single F/S caption (e.g., "Cash"), sub-leads might be:

| Sub-lead | Index | Account | Source |
|---|---|---|---|
| Cash — operating | A-1 | 1010 | Bank rec, bank confirmation |
| Cash — payroll | A-2 | 1020 | Bank rec, bank confirmation |
| Cash — money market | A-3 | 1030 | Investment statement |
| Restricted cash — escrow | A-4 | 1040 | Escrow agreement, statement |

Each sub-lead carries its own beginning → movements → ending
rollforward and its own procedures section.

## Lead-sheet completeness check

For every F/S caption:

- [ ] Beginning balance ties to PY audited / reviewed F/S (or PY
      compilation in a recurring SSARS engagement).
- [ ] Ending balance ties to current TB.
- [ ] Movements between BB and EB are reconciled and explained.
- [ ] Each movement that is material is supported by a sub-lead or
      a substantive procedure WP.
- [ ] Lead sheet ties to the F/S caption that will appear on the
      issued report.
- [ ] Caption-level materiality is documented and the procedures
      performed reflect that level.

## Common F/S captions and their lead-sheet indices

The lead-sheet index aligns with the indexing convention (see
`indexing-convention.md`):

| Lead-sheet caption | Typical index |
|---|---|
| Cash and cash equivalents | A |
| Accounts receivable, net | B |
| Inventory | C |
| Prepaid expenses | F |
| Property and equipment, net | D |
| Right-of-use lease assets (ASC 842) | D-2 (or as firm prefers) |
| Investments | E |
| Goodwill | E-2 |
| Other intangible assets, net | E-3 |
| Other assets | G |
| Accounts payable | K |
| Accrued expenses | K-2 |
| Lease liability (ASC 842) | L-2 |
| Income taxes payable / deferred | T (or N — firm preference) |
| Long-term debt | M |
| Equity | H |
| Revenue | R |
| Cost of revenue | S |
| Operating expenses | E (income statement; firms often use "OE") |
| Income tax expense | T (income statement) |
| Other income / loss | OI |

## Lead sheet vs. workpaper-program crosswalk

The lead sheet documents the **conclusion** for the caption. The
workpaper program (audit) or inquiry/analytical-procedure schedule
(review) documents the **procedures performed** that support the
conclusion. Lead sheet without a procedure WP is a deficiency;
procedure WP without a lead-sheet conclusion is a deficiency.

## Lead-sheet review pattern

Reviewers focus on:

1. Does the BB → EB rollforward reconcile?
2. Are the procedures performed sufficient given the assessed risk?
3. Does the conclusion follow from the procedures and evidence?
4. Are there open items that should be cleared before sign-off?
5. Is the documentation sufficient to enable an experienced
   practitioner without prior connection to understand what was
   done and what was concluded (AU-C §230.08 / AR-C §60.A26)?

The lead sheet is typically the partner-review focal point; sub-
leads receive senior-staff or manager review.
