# ASC 740-20 — Intraperiod Allocation

ASC 740-20 governs how income tax expense / benefit is allocated
within a period among:
- Continuing operations.
- Discontinued operations.
- Other comprehensive income (OCI) — incl. items presented in
  AOCI.
- Items charged or credited directly to equity (e.g., APIC pool
  for stock compensation, contributed capital).
- Cumulative effects of accounting changes.

## The "incremental" allocation method (ASC 740-20-45-7)

Tax effects of items OUTSIDE continuing operations are allocated
to those items based on the INCREMENTAL effect approach:

1. **First**, allocate to continuing operations (using continuing-
   operations pretax book income × statutory rate, plus
   permanent differences).
2. **Then**, allocate to other items (discontinued ops, OCI,
   equity) based on their incremental effect on the total tax
   computed.

The incremental effect = total tax with the item INCLUDED minus
total tax with the item EXCLUDED.

## "Backwards tracing" (ASC 740-20-45-11)

When an OCI / equity item that originally went through OCI / equity
later affects continuing operations (e.g., AFS gain originally OCI
becomes realized P&L on sale), the related tax effect generally
follows the underlying item's path:
- Original OCI tax → reverses through OCI when realized.
- Equity item tax → reverses through equity.

EXCEPT for the "stranded tax effects" issue arising from rate
changes (ASU 2018-02 permits reclassification from AOCI to
retained earnings for stranded effects).

## Special case: changes in valuation allowance

ASC 740-10-45-22: Changes in VA generally allocated to continuing
operations EVEN IF the underlying DTA originated in OCI / equity,
EXCEPT changes that result from items recognized in OCI / equity
in the same period.

This is a significant departure from "tracing" — VA changes flow
through continuing operations even when the underlying DTA does
not. This produces volatility in continuing-operations effective
tax rate.

## Special case: change in tax law / rate

ASC 740-10-45-15: Changes in enacted tax rates / law affect DTAs
and DTLs as discrete events recognized in continuing operations
in the period of enactment.

EXCEPT items underlying DTAs / DTLs related to OCI: rate-change
effect on those DTLs / DTAs flows through OCI, not continuing
operations. (Subject to ASU 2018-02 reclassification.)

## Discontinued operations (ASC 740-20-45-12)

When a component of an entity is classified as held-for-sale
(discontinued operation per ASC 205-20):
- Tax effect of pretax book income / loss of the component
  allocated to discontinued operations.
- Allocation based on the incremental effect.

## Equity / APIC pool for stock compensation (ASU 2016-09)

ASU 2016-09 simplified the accounting for excess tax benefits
and tax deficiencies on stock-based compensation:
- Excess tax benefits and tax deficiencies recognized in INCOME
  TAX EXPENSE (continuing operations) — NOT through APIC.
- Eliminated the "APIC pool" concept that previously absorbed
  shortfalls.

This is a notable departure from pre-ASU 2016-09 practice. PBE
adopted Dec. 15, 2016; non-PBE Dec. 15, 2017.

## Effect on the effective tax rate (ETR)

Intraperiod allocation directly affects the ETR (continuing
operations tax / continuing operations pretax income). Items
that increase or decrease the continuing-operations tax without
proportional pretax effect cause ETR volatility:
- VA changes flow through continuing operations.
- Excess tax benefits / shortfalls on stock-based compensation
  flow through continuing operations.
- Discrete items (rate change, return-to-provision adjustments,
  windfall items).

ETR = Continuing-operations tax expense / continuing-operations
pretax income.

## Disclosures

ASC 740-10-50 + ASU 2023-09 require:
- Components of income tax expense (continuing operations,
  discontinued operations, OCI, equity).
- Reconciliation of statutory rate to ETR (with categorical
  detail under ASU 2023-09 effective date).
- Significant discrete items.

## Cross-references

- DTA / DTL: `dta-dtl.md`.
- VA: `valuation-allowances.md`.
- Disclosures: `disclosures.md`.
- ASC 205-20 discontinued operations: `research-financial-reporting`.

## Authority

Cite ASC 740-20 paragraphs as `authority_type: FASB_ASC`,
`authority_domain: gaap`, `weight: gaap_codified`. Pin-cite to
specific paragraph (e.g., "ASC 740-20-45-7").
