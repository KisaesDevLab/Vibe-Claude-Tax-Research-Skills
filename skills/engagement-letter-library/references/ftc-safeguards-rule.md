# FTC Safeguards Rule — Required clause for tax engagements

The FTC Safeguards Rule (16 CFR Part 314) applies to all tax
preparers as "financial institutions" under the GLBA. The
strengthened 2023 version (effective June 2023) imposes
affirmative requirements on the firm. Engagement letters for tax
engagements should reference the firm's program.

## Coverage trigger

A firm is a "financial institution" under 16 CFR §314.2 if it
significantly engages in:
- Tax preparation services for individuals or businesses.
- Other financial activities as defined in 12 CFR §225.28.

This includes: tax preparation firms, CPAs preparing returns,
enrolled agents, payroll services with tax-filing components.

## Required program elements (16 CFR §314.4)

A written information security program (WISP) must include:

1. **Designated Qualified Individual** — responsible for the
   program; reports periodically to senior management.
2. **Risk assessment** — written assessment of foreseeable risks
   and threats; updated as needed.
3. **Safeguards** — to control identified risks:
   - Access controls (authentication, MFA where appropriate).
   - Encryption of customer information in transit and at rest
     (or compensating controls).
   - Secure development practices for in-house applications.
   - Multi-factor authentication for systems with customer
     information.
   - Procedures for secure disposal.
   - Procedures for change management.
   - Logging and monitoring.
4. **Service provider oversight** — written contracts with service
   providers requiring them to maintain appropriate safeguards.
5. **Incident response plan** — documented procedures for
   identifying, containing, mitigating, recovering from, and
   reporting security events.
6. **Training** — periodic security training for personnel.
7. **Periodic reporting** — at least annual report by Qualified
   Individual to board / governance.

## Engagement letter clause (template)

> **Data Security and FTC Safeguards Rule**
>
> The firm is a "financial institution" under the FTC Safeguards
> Rule (16 CFR Part 314) and has implemented a written
> information security program (WISP) in compliance with the
> Rule. The WISP includes a Qualified Individual with overall
> responsibility, periodic risk assessments, safeguards including
> access controls and encryption, oversight of service providers,
> and an incident response plan.
>
> Client information will be protected consistent with the WISP.
> The firm will:
> - Maintain administrative, physical, and technical safeguards
>   for client information.
> - Limit access to client information to firm personnel and
>   authorized service providers with a need to know.
> - Notify the client of any security event affecting the
>   client's information consistent with applicable law and the
>   firm's incident response plan.
> - Use service providers (cloud storage, tax software, e-file
>   transmitters) only under written contracts requiring
>   appropriate safeguards.
>
> Client agrees to:
> - Provide information to the firm via secure channels (e.g.,
>   encrypted portal, encrypted email).
> - Not transmit sensitive information (SSN, bank account
>   numbers, etc.) via unencrypted email.
> - Notify the firm promptly of any suspected security event
>   affecting the engagement.

## State data-breach overlay

In addition to FTC Safeguards Rule, state breach-notification laws
apply (in all 50 states + DC). The engagement letter clause is a
floor; firm should track state-specific notification timelines
(typically 30–60 days from discovery) and content requirements.

Notable state overlays:
- California Consumer Privacy Act (CCPA) for clients with
  California residents in their workforce / customer base.
- New York SHIELD Act with reasonable security requirements.
- Massachusetts 201 CMR 17 with prescriptive WISP requirements.
- Virginia Consumer Data Protection Act.
- Colorado Privacy Act.
- Utah Consumer Privacy Act.

## Audit / review interaction

For audit and review engagements (independence-required), the
service-organization auditor controls evaluation may interact with
the firm's own safeguards under SQMS 1 / SQMS 2. Firm should not
co-mingle attest-engagement client information with non-attest
client information beyond what the firm's WISP permits.

## Tax preparer-specific provisions

- IRC §7216 disclosure consent for any third-party use of return
  information (including disclosure to lender, CPA-firm
  affiliate, related entity).
- Form W-9 / W-7 (for ITIN) collection and storage with
  appropriate safeguards.
- E-file: PTIN, EFIN, MeF transmitter compliance with IRS
  requirements (e-file requirements for paid preparers under
  §6011(e), §6695, Pub. 1345 e-file procedures).

## Penalties for non-compliance

- FTC enforcement action under 15 USC §6801 (GLBA Title V).
- State attorney general action (state breach laws).
- Civil liability for affected consumers.
- Reputational and engagement-loss damage.
- Possible AICPA disciplinary action under Code §1.400 if breach
  involves disclosure of client information without proper
  safeguards.

## Cross-references

- Confidentiality (AICPA Code §1.700): `compliance-aicpa-code` skill.
- §7216 disclosure consent for tax engagements:
  `compliance-ssts-circular230` skill.
- Service organization controls (SOC 2 mapped to Trust Services
  Criteria — Security, Confidentiality): `compliance-attestation-qm`.
- State-specific privacy / breach laws: state-board overlay file.

## Authority

- 16 CFR Part 314 (Safeguards Rule):
  https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314
- FTC compliance guide:
  https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know

Cite the Safeguards Rule as `authority_type: TreasReg`-equivalent
under tax_position domain (since it's a federal regulation), or as
a separate professional-conduct citation depending on engagement.
For engagement-letter authoring purposes, cite as a regulatory
requirement that the firm represents it complies with.
