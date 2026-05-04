---
name: research-asc-606-842
description: |
  ASC 606 (Revenue from Contracts with Customers) and ASC 842
  (Leases) research. Covers ASC 606 five-step model, performance
  obligations, variable consideration, principal-vs-agent, contract
  modifications; ASC 842 lessee/lessor classification, ROU asset
  recognition, sale-leaseback, short-term lease exception. Bundled
  because they are the two highest-volume judgment-heavy GAAP
  topics CPA firms research jointly. Routes other ASC topics to
  research-financial-reporting and ASC 740 to research-asc-740.
  Use when the user asks "ASC 606", "revenue recognition", "five-
  step model", "performance obligation", "variable consideration",
  "principal vs agent", "ASC 842", "lease classification", "ROU
  asset", "operating vs finance lease", "sale-leaseback", or
  "lessee accounting". Make sure to use this skill whenever the
  user mentions ASC 606, ASC 842, revenue recognition, or lease
  accounting under U.S. GAAP.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# research-asc-606-842 — Revenue & Leases

The two most-frequently-researched ASC topics. ASC 606 supersedes
substantially all of ASC 605 (industry-specific exceptions
remain for some narrow areas). ASC 842 supersedes ASC 840.

## Read before output

1. `shared/citation-discipline.md` — authority_domain: gaap.
2. `shared/authority-hierarchy.md` — GAAP authority subsection.
3. `shared/confidence-bands.md` — band assignment.
4. `shared/compliance.md` — GAAP research scaffolding.
5. `references/asc-606-five-step-model.md` — the framework.
6. `references/asc-606-variable-consideration.md` — VC, constraint,
   and modifications.
7. `references/asc-606-principal-vs-agent.md` — control evaluation.
8. `references/asc-842-classification.md` — five tests for lessee
   classification (operating vs finance).
9. `references/asc-842-rou-assets.md` — ROU asset / lease liability
   measurement, subsequent reporting, lease modifications.

## Operative authority

- ASC 606 (effective for PBE 2018, non-PBE 2019).
- ASC 842 (effective for PBE 2019, non-PBE 2022).
- Cite as `authority_domain: gaap`, `authority_type: FASB_ASC`,
  `weight: gaap_codified`. Pin-cite to specific paragraph.

## Workflow

### 1. Intake

- `topic`: revenue (ASC 606) | leases (ASC 842)
- `entity_type`: nonissuer | issuer | governmental (route to GASB)
- `framework`: U.S. GAAP | IFRS (route externally for IFRS 15 / 16)
- `industry`: e.g., SaaS, manufacturing, construction, healthcare,
  real estate (drives industry-specific considerations)
- `transaction_or_contract`: brief description
- `issue`: free text
- `tax_year` / `fiscal_year_end`: for ASU effective-date analysis

### 2. Topic routing

- **ASC 606** → walk `references/asc-606-*.md` files.
- **ASC 842** → walk `references/asc-842-*.md` files.
- **Other ASC** → route to `research-financial-reporting`.
- **ASC 740** (income tax) → route to `research-asc-740`.

### 3. ASC 606 — Five-step model

For each contract:
1. Identify the contract.
2. Identify the performance obligations.
3. Determine the transaction price.
4. Allocate the transaction price to performance obligations.
5. Recognize revenue when (or as) the entity satisfies a
   performance obligation.

Walk `references/asc-606-five-step-model.md` for each step's
key judgments.

### 4. ASC 606 — Common judgment areas

- **Variable consideration**: rebates, discounts, refunds,
  returns, performance bonuses. Estimation methods: expected-
  value or most-likely-amount. Constraint: included only to the
  extent it is probable a significant reversal will not occur.
  Walk `references/asc-606-variable-consideration.md`.
- **Principal vs. agent**: control of the specified good or
  service before transfer. Walk
  `references/asc-606-principal-vs-agent.md`.
- **Contract modifications**: as-modified contract vs. separate
  contract; treatment depends on whether the modification adds
  distinct goods/services and pricing.
- **License revenue (functional vs. symbolic)**: ASC 606-10-55-
  54+ for licenses of intellectual property.
- **SaaS / cloud arrangements**: hosted vs. on-premise; software
  license vs. service contract; over-time vs. point-in-time.

### 5. ASC 842 — Lease classification

For LESSEES, ALL leases (other than short-term and certain
low-value) recognize a right-of-use (ROU) asset and a lease
liability. The classification determines income statement and
cash flow presentation:

**Operating lease**: straight-line lease expense; ROU asset
amortization is the plug to achieve straight-line.

**Finance lease (formerly capital)**: separate amortization of
ROU asset (typically straight-line) and interest on lease
liability — front-loaded total expense.

Five tests (any one met → finance):
1. Transfer of ownership at end.
2. Bargain purchase option (reasonably certain to exercise).
3. Lease term ≥ 75% of remaining economic life.
4. PV of lease payments + residual ≥ 90% of fair value.
5. Underlying asset is so specialized that it has no alternative
   use to the lessor.

Walk `references/asc-842-classification.md`.

### 6. ASC 842 — ROU asset and lease liability

- Initial measurement: PV of lease payments using the rate
  implicit in the lease (if known) or the lessee's incremental
  borrowing rate.
- Subsequent measurement: lease liability accretes interest;
  ROU asset is amortized.
- Lease modifications: re-measurement triggers vs. new contract.
- Sale-leaseback: ASC 842-40.
- Short-term lease (≤ 12 months) elective exemption: expense
  straight-line; no ROU asset.

Walk `references/asc-842-rou-assets.md`.

### 7. Disclosure requirements

ASC 606-10-50: revenue disaggregation, contract balances,
performance obligations, transaction price allocated to remaining
performance obligations, significant judgments, costs to obtain /
fulfill.

ASC 842-20-50: maturities of lease liabilities, weighted-average
discount rate, weighted-average remaining lease term, finance and
operating lease cost components, cash paid for leases.

### 8. Conclusion

State the recognition / measurement / presentation / disclosure
conclusion. Confidence band per `shared/confidence-bands.md`.

ASC 606 conclusions often land MODERATE because the principles-
based model produces fact-specific judgments. ASC 842 lessee
classification is more rules-based (five tests), so HIGH band is
common.

### 9. JSON sidecar

`authority_domain: gaap` for ASC 606 / 842 citations.
`verification_checklist_gaap` populated.

## Hard rules

- Never apply ASC 605 (legacy) to a contract within ASC 606
  scope.
- Never apply ASC 840 (legacy) to a lease within ASC 842 scope.
- Never apply IFRS 15 / IFRS 16 to a U.S. GAAP reporter.
- Always verify ASU effective dates before stating current rule.
- Always evaluate principal vs. agent on a control-of-good basis
  (NOT a payment-flow basis).
- Always evaluate variable-consideration constraint at each
  reporting date.
- Always require lessee to recognize ROU asset for non-short-term
  leases.

## Verification checklist (appendix)

End the markdown response with the GAAP research scaffolding
module from `shared/compliance.md`.
