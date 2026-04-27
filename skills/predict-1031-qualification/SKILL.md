---
name: predict-1031-qualification
description: |
  Predicts whether a §1031 like-kind exchange of real property will
  qualify for tax-deferral treatment under IRC §1031 as amended by
  TCJA. Covers the held-for-productive-use-or-investment requirement,
  identification (45-day) and exchange (180-day) timelines, qualified
  intermediary mechanics, related-party traps under §1031(f), boot
  recognition, reverse exchanges (Rev. Proc. 2000-37), and the post-
  TCJA real-property-only restriction. Use when the user asks "will
  this 1031 qualify", "like-kind exchange", "45-day identification",
  "qualified intermediary", "QI", "delayed exchange", "reverse
  exchange", "boot", or "1031 related-party". Make sure to use this
  skill whenever the user mentions §1031, like-kind exchange, 1031
  exchange, or QI.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# predict-1031-qualification — §1031 like-kind exchange

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `shared/legislation-tracking.md` — TCJA (Pub. L. 115-97) §13303
   restricted §1031 to real property held for productive use in a
   trade or business or for investment, effective for exchanges
   after 12/31/2017.
6. `references/timelines-and-traps.md` — 45/180 deadlines, related-
   party rules, reverse-exchange safe harbor, boot computation.

## Operative authority

- IRC §1031 (post-TCJA: real property only).
- IRC §1031(f) — related-party limitations.
- Treas. Reg. §1.1031(a)-1 through §1.1031(k)-1.
- Treas. Reg. §1.1031(k)-1(g)(4) — qualified-intermediary safe
  harbor.
- Rev. Proc. 2000-37 — reverse-exchange safe harbor (parking
  arrangement).
- Rev. Proc. 2003-39 — multiple-property reverse exchanges.
- Starker v. United States, 602 F.2d 1341 (9th Cir. 1979) —
  delayed-exchange foundational case (now codified in §1031(a)(3)).

## Workflow

### 1. Intake

- `relinquished_property_description`: real property held for
  productive use in a trade/business or for investment
- `replacement_property_description`: same character requirement
- `relinquished_sale_date` / `replacement_close_date` for timeline
  testing
- `qualified_intermediary_used`: yes/no (and identity)
- `taxpayer_constructive_receipt_facts`: did the taxpayer at any
  point have access to or rights over the proceeds
- `related_party_facts`: §267(b) / §707(b) relationships
- `boot_facts`: cash received, debt relief net of debt assumed,
  non-like-kind property
- `is_reverse_or_improvement_exchange`: parking arrangement details
- `state_conformity`: not all states conform — check per-state file
  if state taxation is at issue

### 2. Held-for-productive-use-or-investment test

§1031(a)(1) requires both relinquished AND replacement property to
be held "for productive use in a trade or business or for
investment". A primary residence does NOT qualify; a second home
held primarily for personal use does NOT qualify (Rev. Proc.
2008-16 provides a safe harbor for vacation homes that meet
specific personal-use limits).

Foreign real property is NOT like-kind to U.S. real property
(§1031(h)).

Post-TCJA real-property-only: §1031 no longer applies to personal
property exchanges (vehicles, equipment, livestock, art, etc.).

### 3. Timing rules (§1031(a)(3))

- **45-day identification**: written, signed identification of
  replacement property delivered within 45 calendar days after the
  transfer of the relinquished property. Three-property rule OR
  200% rule OR 95% rule (§1.1031(k)-1(c)(4)).
- **180-day completion**: receipt of replacement property within
  180 calendar days after transfer of relinquished property (or
  the due date of the return for the year of transfer including
  extensions, whichever is earlier).

Both deadlines are JURISDICTIONAL — no equitable extension absent
a presidentially-declared disaster (Notice 2024-XX type relief).

### 4. Qualified-intermediary safe harbor

Treas. Reg. §1.1031(k)-1(g)(4) provides safe harbor against
constructive receipt: the QI must:
- Not be a disqualified person (§1.1031(k)-1(k)).
- Hold proceeds in a "qualified escrow" or "qualified trust" or
  similar arrangement.
- Restrict the taxpayer's rights to receive, pledge, borrow against,
  or otherwise benefit from the proceeds.

Disqualified persons: agent of the taxpayer (attorney, CPA,
broker, real-estate agent who has acted for the taxpayer within 2
years prior to the transaction), or related parties under §267(b)
/ §707(b).

### 5. Related-party rule (§1031(f))

If the exchange is with a related person (§267(b) / §707(b)):
- Both parties must hold the received property for ≥ 2 years.
- Earlier disposition triggers gain recognition retroactively.
- Exceptions: death, involuntary conversion, tax-avoidance not the
  principal purpose.
- Triangular structures (§1031(f)(4)): where the taxpayer
  transfers to a QI who then exchanges with a related party,
  IRS has invoked §1031(f)(4) to deny non-recognition. See Teruya
  Brothers v. Commissioner, 124 T.C. 45 (2005), aff'd 580 F.3d
  1038 (9th Cir. 2009).

### 6. Boot

§1031(b): boot received recognized to the extent of gain. Boot
includes cash, non-like-kind property, and net debt relief (debt on
relinquished property minus debt assumed on replacement property).

Compute:
- Recognized gain = lesser of realized gain OR boot received.
- Basis of replacement = old basis + recognized gain - boot
  received + boot given.

### 7. Reverse exchange (Rev. Proc. 2000-37)

Parking arrangement: an Exchange Accommodation Titleholder (EAT)
takes title to either the replacement OR the relinquished
property. Safe harbor requires:
- Written agreement reflecting the parking arrangement.
- 45-day identification of relinquished property (mirror rule).
- 180-day total parking period.
- Various other conditions (qualified-indicia-of-ownership rules).

### 8. Conclusion

Confidence band per `shared/confidence-bands.md`:

- HIGH: clear held-for-investment posture; QI used; deadlines met;
  no related-party issues; minimal boot.
- MODERATE: tight on a deadline; minor boot; QI structure
  conservative.
- LOW: related-party concerns; aggressive vacation-home posture;
  reverse exchange with EAT discipline questions.
- SPECULATIVE: missed deadline (kiss of death), constructive
  receipt by taxpayer, primary-residence component.

State conformity should be verified separately when state tax is
material; some states (e.g., CA's clawback rule under Cal. Rev. &
Tax. Code §18032) impose post-deferral reporting obligations even
where federal §1031 applies.

### 9. Authorities + sidecar

Cite §1031, relevant Treas. Regs., Rev. Proc. 2000-37, and any
case law. JSON sidecar validates against
`shared/output-schema.json`.

For TCJA-affected propositions (real-property-only), populate
`public_laws_consulted[]`.

## Hard rules

- Never assert a §1031 exchange qualifies without confirming the
  45-day and 180-day deadlines.
- Never rely on a QI structure without checking
  disqualified-person rules under §1.1031(k)-1(k).
- Never apply post-TCJA §1031 to personal property.
- Drop one band for related-party transactions even within the
  §1031(f) safe harbor.
- Never claim Chevron deference for Treas. Reg. §1.1031(k)-1.
- Foreign real property is excluded; §1031(h) is statutory.
- For CA exchanges, flag the §18032 clawback reporting requirement.

## Verification checklist (appendix)

End with the SSTS / Circular 230 checklist from
`shared/compliance.md`. For high-stakes positions (six-figure plus
deferred gain), include the negative-treatment-review residual
practitioner responsibility.
