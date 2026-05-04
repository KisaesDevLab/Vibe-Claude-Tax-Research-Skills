# ASC 606 — Five-Step Model

ASC 606 (Revenue from Contracts with Customers) implements a
single principles-based model for revenue recognition.

## Step 1 — Identify the contract (ASC 606-10-25-1)

A contract exists when:
- Approved by both parties (writing, oral, or implied by customary
  business practices).
- Identifies each party's rights regarding the goods/services.
- Identifies payment terms.
- Has commercial substance (i.e., risk, timing, or amount of cash
  flow expected to change as a result of the contract).
- Probable that the entity will collect substantially all of the
  consideration.

If any criterion fails, no contract exists; consideration
received is recognized as deposit/liability until criteria are
met or refunded.

## Step 2 — Identify performance obligations (ASC 606-10-25-14)

Performance obligation: a promise to transfer to the customer
either:
- A distinct good or service (or distinct bundle).
- A series of distinct goods/services that are substantially the
  same and have the same pattern of transfer.

A good/service is **distinct** if BOTH:
- Customer can benefit from it on its own or with readily
  available resources (capable of being distinct).
- The promise is separately identifiable from other promises in
  the contract (distinct in the context of the contract).

"Separately identifiable" considerations (ASC 606-10-25-21):
- Significant integration of the goods/services.
- Significant modification or customization.
- Highly interdependent or interrelated.

## Step 3 — Determine the transaction price (ASC 606-10-32-2)

Transaction price = amount of consideration the entity expects to
be entitled to in exchange for transferring promised
goods/services, EXCLUDING amounts collected on behalf of third
parties (e.g., sales taxes).

Adjust for:
- **Variable consideration** (rebates, discounts, returns,
  bonuses, etc.): estimate using expected-value or most-likely-
  amount; apply the constraint.
- **Significant financing component** (timing of payment vs.
  performance differs by ≥ 1 year, generally).
- **Noncash consideration**: measure at fair value.
- **Consideration payable to a customer** (rebates, credits):
  reduce transaction price unless in exchange for a distinct
  good/service.

Walk `references/asc-606-variable-consideration.md` for VC.

## Step 4 — Allocate transaction price to performance obligations (ASC 606-10-32-28)

Allocate based on relative **standalone selling prices** (SSP).

Determining SSP:
- Observable price when the entity sells the good/service
  separately.
- If not observable: estimate using
  - Adjusted market assessment.
  - Expected cost plus margin.
  - Residual approach (limited use; only when SSP is highly
    variable or uncertain).

Discount allocation: if a discount relates to one or more (but
not all) performance obligations, allocate to those specific
obligations rather than all.

Variable consideration allocation: if VC relates to one or more
specific performance obligations, allocate accordingly.

## Step 5 — Recognize revenue (ASC 606-10-25-23)

Revenue recognized when (or as) entity satisfies a performance
obligation by transferring control of the good/service.

### Over time vs. point in time

**Over time** (ASC 606-10-25-27) if any one of:
- Customer simultaneously receives and consumes benefits as the
  entity performs (e.g., routine services, cleaning).
- Entity creates or enhances an asset the customer controls as
  it is created/enhanced.
- Entity's performance does NOT create an asset with alternative
  use to the entity AND the entity has an enforceable right to
  payment for performance to date.

**Point in time** otherwise. Indicators of transfer of control
(ASC 606-10-25-30):
- Present right to payment.
- Legal title.
- Physical possession.
- Significant risks and rewards of ownership.
- Customer acceptance.

### Methods for over-time revenue (ASC 606-10-25-31)

- Output method (units delivered, milestones, surveys of work
  performed).
- Input method (costs incurred, hours expended, time elapsed) —
  most common in practice; ensure inputs faithfully depict
  transfer of control (resource-cost-plus-mark-up may not).

## Common contract types

### Product sales
- Single performance obligation typically.
- Point in time when customer takes control (delivery, FOB
  shipping vs. FOB destination matters).
- Returns / right of return: variable consideration with
  constraint.

### Services (typical)
- Over-time recognition typically.
- Input method (time elapsed, hours).

### Subscription / SaaS
- Single hosted-software performance obligation often (functional
  IP).
- Recognize over the subscription term ratably.
- Implementation services: separate performance obligation if
  distinct; if not distinct, combined.
- Set-up fees: deferred and recognized over the customer
  relationship period.

### Construction / long-term contracts
- Often a single performance obligation if highly integrated.
- Over-time recognition with input method (cost-to-cost).
- Variable consideration includes change orders, claims,
  contingent payments.

### Licenses of intellectual property (ASC 606-10-55-54+)
- **Functional IP**: standalone functionality independent of
  entity's ongoing activities. Point-in-time recognition.
- **Symbolic IP**: derives substantially all of its utility from
  the entity's continuing involvement (e.g., brand licenses,
  franchise rights). Over-time recognition.

## Costs

- **Costs to obtain a contract** (commissions to salespeople):
  capitalize if expected to be recovered; amortize over period
  of expected benefit. Practical expedient: expense if
  amortization period is ≤ 1 year.
- **Costs to fulfill a contract**: capitalize if directly relate
  to a contract, generate / enhance resources used to satisfy
  performance obligations, expected to be recovered.

## Cross-references

- Variable consideration: `asc-606-variable-consideration.md`.
- Principal vs. agent: `asc-606-principal-vs-agent.md`.
- ASC 842 leases (note: lease components within a contract are
  evaluated under ASC 842, NOT ASC 606): `asc-842-classification.md`.

## Authority

Cite ASC 606-10 paragraphs as `authority_type: FASB_ASC`,
`authority_domain: gaap`, `weight: gaap_codified`. Pin-cite to
specific paragraph (e.g., "ASC 606-10-25-23").
