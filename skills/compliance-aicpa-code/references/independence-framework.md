# ET §1.200 — Independence: threats-and-safeguards walk

The AICPA Code's independence rule (ET §1.200) is built on a
**conceptual framework** rather than a closed rules list. The
practitioner identifies threats, evaluates whether they are at an
acceptable level, and applies safeguards if not. Independence is
"impaired" when threats cannot be reduced to an acceptable level
even with safeguards.

This file catalogs the seven threat categories (six per AICPA, with
"undue influence" carved out separately in some treatments) and the
common fact patterns + safeguards practitioners encounter.

## Threat categories (ET §1.210)

1. **Self-review threat** — auditing the firm's own work product.
   *Example:* firm prepared the journal entries that will be tested
   in the audit.
2. **Advocacy threat** — promoting client's position to a degree that
   objectivity is or appears compromised.
   *Example:* firm represents client in litigation against a third
   party while also auditing the financial statements.
3. **Familiarity threat** — long association or close personal
   relationship reduces professional skepticism.
   *Example:* engagement partner has been on the audit for 12 years;
   senior staff member's spouse works in client controllership.
4. **Self-interest threat** — financial or other interest impairs
   objectivity.
   *Example:* loan from an attest client to firm partner; equity
   interest in an attest client.
5. **Undue influence threat** — client pressure / gifts / threats
   compromise judgment.
   *Example:* client offers tickets to a major sporting event;
   client threatens to switch firms unless adjustment is dropped.
6. **Management participation threat** — firm performs management
   functions for the attest client.
   *Example:* firm acts as outsourced controller for an audit
   client.
7. **Adverse interest threat** — interests of firm and client are in
   opposition.
   *Example:* firm has filed a malpractice claim against client;
   client has sued firm.

## Common fact patterns

### Loans and financial relationships (ET §1.260)

- **Loan FROM attest client to firm/partner**: generally prohibits
  independence unless under permitted-loan exceptions (auto loan
  collateralized by auto, residential mortgage at market terms with
  client lender, ordinary course credit card with $10K balance cap,
  bank deposits within FDIC limits + immaterial). Otherwise:
  independence impaired.
- **Loan TO attest client**: prohibited (creates self-interest +
  advocacy threats).
- **Equity interest in attest client (direct)**: prohibits
  independence regardless of materiality.
- **Indirect interest** (mutual fund holding): permitted if
  immaterial AND the firm cannot exercise material influence.

### Family / household relationships (ET §1.270)

- **Immediate family member** (spouse, dependent) of covered member
  works at attest client in a key position (CFO, controller, audit
  committee chair, anyone with ability to influence financial
  statements): independence impaired. Period.
- **Close relative** (parent, sibling, non-dependent child) in a key
  position: threat at potentially-not-acceptable level; safeguards
  required (different engagement team, EQR, removal from key
  decisions).

### Long association (ET §1.250)

- Engagement partner / lead auditor on attest engagement for
  successive years: familiarity threat increases. AICPA does not
  mandate hard rotation for nonissuer audits (PCAOB 5-year rotation
  applies to issuer audits only). Safeguards include rotation,
  EQR, peer review.
- AICPA Quality Management standards (SQMS 1) require firm-level
  partner rotation policies appropriate to firm size and engagement
  risk.

### Nonattest services to attest clients (ET §1.295)

See `references/nonattest-services-1295.md`. The §1.295 walk is the
gatekeeper that prevents most management-participation and self-
review threats from impairing independence.

### Gifts and entertainment (ET §1.285)

- Reasonable hospitality (occasional meal, modest sports tickets):
  acceptable.
- Lavish gifts, vacation trips, large-value tickets: undue influence
  threat at potentially-not-acceptable level; decline.

### Fee dependence (ET §1.230)

- If fees from a single attest client exceed a substantial portion
  of total firm fees (no bright-line rule; AICPA practice-aid
  threshold is often cited as 15%+ over multiple years for partner-
  level dependence), self-interest threat increases. Safeguards
  include EQR, peer review, partner rotation.

### Contingent fees and commissions (ET §1.510, §1.520)

- Contingent fees: **prohibited** for attest clients and for the
  preparation of any original or amended return (§1.510.001 with
  narrow exceptions, e.g., representing client before IRS Appeals
  on a position already taken).
- Commissions: **prohibited** if the firm performs attest services
  for the same client. Disclosure required when permitted.

## Safeguards catalog

When threats are not at an acceptable level:

1. **Created by the profession / standards / regulation**
   - Continuing professional education
   - Peer review
   - SQMS 1 firm-level quality management
2. **Implemented by the client**
   - Audit committee / governance with industry expertise
   - Internal control over financial reporting
   - Client policies prohibiting hiring of audit partners
3. **Implemented by the firm**
   - Separate engagement teams for attest and nonattest services
   - Engagement Quality Review (SQMS 2)
   - Partner / staff rotation
   - Firm-wide independence policies and monitoring
   - Withdrawal from problematic relationships before engagement
   - Hot review

## When independence is impaired

If threats cannot be reduced to an acceptable level even with
safeguards:
- **Decline** the attest engagement before acceptance.
- **Withdraw** from the attest engagement if the impairment arises
  mid-engagement.
- For compilation engagements without independence (AR-C 80.27),
  issue a **lack-of-independence disclaimer** in the compilation
  report; this is the only engagement type that permits continuation
  without independence.

## Documentation

ET §1.295 requires written documentation of threats identified,
safeguards applied, and the conclusion that independence is or is
not impaired. The engagement file should include:

- [ ] Threat identification log (categories + facts).
- [ ] Severity evaluation (acceptable level or not).
- [ ] Safeguards applied (specific to the threat).
- [ ] Conclusion (independent / impaired).
- [ ] Date of evaluation; reviewer signature for non-routine matters.

## Cross-references

- For nonattest service screens, see `nonattest-services-1295.md`.
- For state-board overlays (CA, NY, TX known stricter), see
  `state-board-overlay.md`.
- For SOC engagement independence (AT-C), see
  `compliance-attestation-qm` skill.
- For audit-specific independence consultations, see
  `compliance-sas-audit` skill.

## Authority

Cite from the AICPA Code of Professional Conduct online text:
https://www.aicpa-cima.com/topic/ethics/code-of-professional-conduct.
Tag `authority_domain: professional_conduct`,
`authority_type: AICPA_Code`, `weight: binding_on_member`. Pin-cite
to specific ET section (e.g., "ET §1.260.020").
