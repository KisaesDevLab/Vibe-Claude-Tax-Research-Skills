# ASC 842 — ROU Asset and Lease Liability (Lessee subsequent measurement)

For non-short-term leases, the lessee recognizes:
- A right-of-use (ROU) asset.
- A lease liability.

## Initial measurement (ASC 842-20-30)

### Lease liability
- PV of remaining lease payments (per `asc-842-classification.md`).
- Discount using rate implicit / lessee's IBR / risk-free (if
  PCC elected).

### ROU asset
- Lease liability AT INCEPTION (i.e., the PV of lease payments).
- PLUS: any lease payments made at or before lease commencement.
- LESS: any lease incentives received.
- PLUS: any initial direct costs (incremental costs that would
  not have been incurred if the lease had not been obtained — e.g.,
  commissions, payments to existing tenant for vacating).

## Subsequent measurement — Operating lease

### Lease liability
- Each period, accrue interest on the lease liability using the
  initial discount rate.
- Reduce the lease liability for cash payments made.

### ROU asset
- Single straight-line lease expense each period for the lease.
- Lease expense = total lease payments / lease term (straight-
  line).
- Accretion of lease liability (interest) + reduction of ROU asset
  amortization = single lease expense.
- ROU asset is reduced by the difference between cash paid and
  interest accreted.

Mathematically:
- Period interest expense = Lease liability × rate.
- Period ROU amortization = Straight-line lease expense - period
  interest.
- The ROU amortization is what makes the IS expense straight-line
  even though the lease liability accretes more interest in early
  years.

### Income statement impact
- Single line: lease expense.
- All operating cash outflow.

## Subsequent measurement — Finance lease

### Lease liability
- Same as operating: interest accretion + payments.

### ROU asset
- Amortized straight-line over the SHORTER OF:
  - The useful life of the underlying asset (if the lessee will
    obtain ownership or is reasonably certain to exercise a
    bargain purchase).
  - The lease term.
- Separate amortization expense.

### Income statement impact
- Separate amortization expense AND interest expense.
- Total expense FRONT-LOADED (interest declines as principal is
  paid down; amortization is straight-line).
- Cash flow: principal portion = FINANCING activity; interest
  portion = operating (or financing, per accounting policy).

## Lease modifications (ASC 842-10-25-8 through -25-12)

### Modification accounted for as separate contract
If a modification:
- Increases the scope by adding the right to use one or more
  underlying assets, AND
- Lease payments increase commensurate with the standalone price
  of the additional ROU,
THEN: account as a SEPARATE contract.

### Modification not accounted for as separate contract
Re-measure on the modification date:
- Update discount rate to reflect the modified contract.
- Re-measure lease liability based on modified payments.
- Adjust ROU asset:
  - Decrease ROU proportional to decrease in lease liability if
    scope decreases — recognize gain or loss.
  - Increase ROU for increase in lease liability if scope changes
    in another manner.

## Reassessment

Triggered by:
- Change in lessee's assessment of an option (renewal, purchase).
- Resolution of contingency affecting lease term.
- Change in residual value guarantee likelihood.
- Change in index or rate used for variable payments — only
  occurs upon a true reassessment trigger, NOT a routine rate
  change (those go through current-period income statement).

When triggered: re-measure lease liability using current discount
rate; adjust ROU asset.

## Sale-leaseback (ASC 842-40)

Two-step analysis:

### Step 1 — Is the transfer a sale under ASC 606?
- Did the buyer-lessor obtain control of the asset?
- If buyer-lessor's only "purchase" is the leaseback → no control
  transfer, no sale.
- If a substantive purchase happened (buyer-lessor has rights to
  benefits, can sell to third parties, etc.) → sale.

### Step 2 — Apply applicable framework

If a sale:
- Seller-lessee derecognizes the asset.
- Recognizes a sale (gain/loss measured per ASC 606).
- Recognizes the leaseback as a new lease per ASC 842 (operating
  or finance based on the five tests).

If NOT a sale (failed sale-leaseback):
- Seller-lessee retains the asset on its balance sheet.
- Treats the financing as a debt obligation.
- Cash received = financing inflow; cash paid back = financing
  outflow + interest expense.

## Lessor accounting (ASC 842-30) — brief overview

Lessor classifies leases as:
- **Sales-type lease**: similar to a sale; recognize sale revenue
  at lease commencement; cost of revenue.
- **Direct financing lease**: lessor finances the asset;
  recognize interest income over time.
- **Operating lease**: lessor retains the asset on books;
  recognize lease income straight-line.

Five tests for sales-type vs. direct financing vs. operating
analogous to lessee tests but applied differently. See ASC
842-10-25-3 and ASC 842-30 for full criteria.

## Disclosure (ASC 842-20-50)

For lessees:
- Maturity analysis of lease liabilities (5-year + thereafter).
- Weighted-average remaining lease term.
- Weighted-average discount rate.
- Components of lease cost (operating, finance — separately
  amortization and interest, variable, short-term, sublease).
- Cash paid for leases.
- ROU assets obtained in exchange for new lease liabilities.
- Lease modifications and re-measurements.

## ASU effective dates

- ASU 2016-02 (initial standard): PBE Jan. 1, 2019; non-PBE
  Jan. 1, 2022.
- ASU 2018-10, 2018-11, 2019-01, 2019-10, 2020-05 (various
  improvements / deferrals): align with above.
- ASU 2020-02 + ASU 2020-05: COVID-related deferrals (relevant
  history but adopted for nearly all reporters by now).
- ASU 2021-05 (lessor — sales-type lease classification when
  variable payments are not exclusively dependent on
  reference index): effective for PBE 2021, non-PBE 2022.
- ASU 2021-09 (PCC alternative — risk-free rate by class of
  underlying asset rather than entity-wide): private-company
  effective date, election permitted.

## Cross-references

- Lease classification: `asc-842-classification.md`.
- ASC 606 revenue (when contract has lease and non-lease
  components): `asc-606-five-step-model.md`.

## Authority

Cite ASC 842-20 / 842-30 / 842-40 paragraphs as
`authority_type: FASB_ASC`, `authority_domain: gaap`,
`weight: gaap_codified`. Pin-cite to specific paragraph.
