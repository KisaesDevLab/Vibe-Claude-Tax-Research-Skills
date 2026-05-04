# Common clauses — engagement-letter cross-cutting language

Clauses that recur across multiple engagement types. Each entry
includes a starting template and a flag for engagement-types where
modification is required.

## Fee and billing

### Hourly
> "Our fees for this engagement will be billed at the standard
> hourly rates of [TIER] in effect at the time the services are
> rendered. As of the date of this letter, the rates are: Partner
> [$RATE], Manager [$RATE], Senior [$RATE], Staff [$RATE]. The
> client agrees to be invoiced [MONTHLY / UPON COMPLETION OF
> PHASES / OTHER]. Invoices are due within [NN] days of issuance.
> Past-due balances accrue interest at [STATE-PERMITTED RATE]."

### Fixed fee
> "Our fee for this engagement is a fixed fee of [$AMOUNT],
> payable as follows: [SCHEDULE]. The fixed fee covers [SCOPE].
> Out-of-scope work will be billed at standard hourly rates with
> client's prior written agreement to the additional scope."

### Contingent (NOT permitted for attest, return preparation, or
amended returns under AICPA Code §1.510)
> "[Contingent fees are NOT permitted for this engagement type
> per AICPA Code §1.510. If the engagement is one of the narrow
> exceptions (representing client before IRS Appeals on a position
> already taken; a position raised by examiner without prior
> taxpayer initiation), specialized contingent-fee language is
> required and firm counsel must review.]"

### Retainer
> "Client agrees to pay a retainer of [$AMOUNT] upon execution of
> this engagement letter. The retainer will be applied against
> fees and disbursements as they are incurred. Any unused portion
> will be returned upon engagement completion."

## Out-of-pocket expenses

> "In addition to fees, the client will reimburse the firm for
> reasonable out-of-pocket expenses (travel, postage, third-party
> data services, file-storage costs over [N] years, etc.) on
> presentation of receipts."

## Dispute resolution

### Mediation/arbitration
> "The parties agree to submit any disputes arising from this
> engagement to mediation in [CITY, STATE] before [PROVIDER].
> If mediation is unsuccessful, disputes will be settled by
> binding arbitration administered by the American Arbitration
> Association under its Commercial Arbitration Rules."

### Court / governing law
> "This engagement letter is governed by the laws of [STATE],
> and any disputes not resolved through mediation/arbitration
> will be brought exclusively in the courts of [COUNTY], [STATE]."

NOTE: Some states limit mandatory pre-dispute arbitration
provisions in professional services contracts. CA, IL, NY have
disclosure requirements. Firm counsel should confirm enforceability
in `engagement_state`.

## Termination

> "Either party may terminate this engagement upon [NN] days
> written notice. Upon termination, the client will pay for all
> work performed through the termination date, including
> reasonable transition expenses. The firm will return client
> records within [NN] days of termination, subject to applicable
> liens for unpaid fees (state-by-state enforceability)."

NOTE: AICPA Code §1.400.001 requires return of client records on
termination subject to applicable lien rights; some states limit
the lien.

## Confidentiality

> "The firm will maintain the confidentiality of client
> information per AICPA Code §1.700 and applicable state-bar /
> state-board rules. Disclosure is permitted only with client
> consent, in response to validly-issued subpoena (with prior
> notice to client where lawful), in connection with peer review
> (with appropriate confidentiality agreement), and as otherwise
> required by law. For tax engagements, IRC §7216 disclosure
> consent will be obtained for any third-party use of return
> information."

## Records retention

> "The firm will retain workpapers and engagement files for
> [NUMBER] years from the engagement completion date in
> accordance with firm retention policy and applicable
> regulatory requirements (AICPA / state board / IRS for tax
> engagements / SQMS 1 quality management system)."

NOTE: AICPA SAS / AT-C / AR-C generally require minimum 5-year
retention; state boards and IRS may require longer. Litigation
hold or subsequently-discovered facts may extend retention.

## Subcontractors / specialists

> "The firm may engage [SPECIALISTS / SUBCONTRACTORS / OTHER
> AICPA-MEMBER FIRMS] to perform portions of this engagement.
> The firm remains responsible for the engagement output. Client
> consents to disclosure to such parties as necessary for the
> engagement, subject to appropriate confidentiality agreements."

## Use of firm name and report restrictions

> "Client may use the firm's report in [SPECIFIED CONTEXTS].
> Use of the firm's report or work product in [PROHIBITED
> CONTEXTS] requires prior written consent. Any modification of
> the firm's report or work product requires firm consent."

For SOC reports and certain attestation engagements, restricted-use
language is more specific (named parties; agreement to take
responsibility for sufficiency of procedures).

## Force majeure

> "Neither party will be in breach for delay or failure caused by
> events beyond reasonable control (acts of God, war, terrorism,
> regulatory change, pandemic-related restrictions, cyber attack
> on either party). The party affected will notify the other and
> use reasonable efforts to resume performance."

## E-signature

> "This engagement letter may be executed electronically. The
> parties agree that electronic signatures are valid and binding
> under the federal E-SIGN Act and applicable state UETA / UETA
> equivalent."

NOTE: E-SIGN and UETA generally permit electronic signatures for
business contracts. Some specific document types (wills, certain
court filings) require wet signatures. Tax-specific: IRS Form 8879
e-file authorization has its own e-signature rules.

## Successors and assigns

> "This engagement letter is binding on the parties and their
> respective successors and assigns. Neither party may assign
> rights or obligations without prior written consent of the
> other."

## Severability

> "If any provision of this engagement letter is held
> unenforceable, the remaining provisions remain in full force
> and effect."

## Entire agreement

> "This engagement letter (with any incorporated exhibits) is the
> entire agreement between the parties regarding the engagement
> and supersedes prior negotiations, representations, and
> agreements."

## Authority citation pattern

When the engagement letter cites or references AICPA standards,
include in the JSON sidecar:
- `authority_type: AICPA_SAS / AICPA_SSARS / AICPA_SSAE` for
  attest standards.
- `authority_type: AICPA_Code` for confidentiality, fees,
  contingent-fee references.
- `authority_type: AICPA_PracticeAid` for AICPA practice-aid
  templates referenced in firm engagement letter library.
- `authority_domain: professional_conduct`, `weight: binding_on_member`
  (or `practice_aid` for practice aids).

For tax-specific (IRC §7216, FTC Safeguards Rule, state UPL),
cite under appropriate authority_type and domain.
