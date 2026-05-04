# ASC 105-10 — GAAP hierarchy (authoritative vs. non-authoritative)

ASC 105-10 establishes that the FASB Accounting Standards
Codification is the **single source of authoritative U.S. GAAP**
for non-governmental entities. Pre-codification GAAP was a multi-
tier hierarchy; post-codification it is a two-tier framework.

## Two tiers

### Tier 1 — Authoritative GAAP

The FASB ASC. Specifically:
- All content within the Codification.
- ASUs that have become effective (codified into the relevant ASC
  topic upon effective date).
- Pre-codification GAAP (SFAS, EITF, SOP, TPB, FIN, FSP, AcSEC
  pronouncements, SEC SAB) ONLY to the extent the content was
  carried forward into ASC verbatim or by explicit reference.

Cite as `authority_domain: gaap`, `authority_type: FASB_ASC`,
`weight: gaap_codified`.

### Tier 2 — Non-authoritative

Per ASC 105-10-05-2:
- FASB Concepts Statements (CON 1, CON 2, CON 5, CON 6, CON 7,
  CON 8). These describe the conceptual framework but are NOT
  authoritative.
- AICPA Technical Practice Aids (TPAs) NOT codified into ASC.
- SEC SAB / accounting bulletins for nonissuers (persuasive
  only).
- Pronouncements of other standard-setters in their respective
  contexts (GASB, IASB / IFRS, PCAOB, IPSAS).
- Industry practices and accounting textbooks.

Cite as `authority_domain: gaap`, `authority_type: FASB_Concepts /
AICPA_TPA`, `weight: gaap_non_authoritative`.

## Pre-codification → ASC mapping

The 2009 Codification renumbered legacy GAAP into the ASC structure.
Common mappings:

| Legacy | Current ASC |
|---|---|
| SFAS 5 | ASC 450 (Contingencies) |
| SFAS 13 | ASC 840 (Leases — superseded by ASC 842) |
| SFAS 109 | ASC 740 (Income Taxes) |
| FIN 48 | ASC 740-10-25 (UTP recognition) + 740-10-50 (disclosures) |
| SFAS 141 / SFAS 141R | ASC 805 (Business Combinations) |
| SFAS 142 | ASC 350 (Intangibles — Goodwill) |
| SFAS 144 | ASC 360 (PP&E impairment) |
| SFAS 157 | ASC 820 (Fair Value Measurement) |
| SFAS 158 | ASC 715 (Pension / Postretirement) |
| SFAS 159 | ASC 825 (Fair Value Option) |
| SFAS 168 | ASC 105 (the Codification itself) |
| ASU 2014-09 | ASC 606 (Revenue from Contracts with Customers) |
| ASU 2016-02 | ASC 842 (Leases) |
| ASU 2016-13 | ASC 326 (CECL) |

When citing post-Codification, use the ASC paragraph reference,
not the legacy SFAS/FIN/SOP number.

## Pre-codification grandfathering

For pre-2009 EITF / SFAS / SOP / TPB content carried forward into
ASC:
- The codified ASC location is the citation.
- Tag as `weight: gaap_codified` (the content was codified).
- The legacy reference number may be cited in parentheses for
  practitioner navigation (e.g., "ASC 740-10-25 (formerly FIN
  48)").

For pre-2009 content NOT carried forward into ASC:
- Effectively superseded; do not cite.
- Tag any unusual citation as `weight: gaap_pre_codification_grandfathered`
  with explicit weight_override_rationale.

## Concepts Statements — non-authoritative use

Concepts Statements (CON) describe the FASB's conceptual framework:
- CON 1 — Objectives of Financial Reporting (superseded by CON 8
  Ch. 1).
- CON 2 — Qualitative Characteristics (superseded by CON 8 Ch. 3).
- CON 5 — Recognition and Measurement.
- CON 6 — Elements of Financial Statements.
- CON 7 — Using Cash Flow and PV in Accounting Measurements.
- CON 8 — Conceptual Framework (Ch. 1, 3, 4, 7, 8).

When ASC is silent on a matter, practitioners may consult Concepts
Statements for conceptual guidance, but the citation is
`gaap_non_authoritative`. Cannot serve as the closest authority
for an ASC conclusion.

## SEC SAB (persuasive for nonissuers)

SEC Staff Accounting Bulletins articulate SEC staff views on
specific accounting matters for issuers. Examples:
- SAB 99 (materiality)
- SAB 104 (revenue recognition; largely subsumed by ASC 606)
- SAB Topic 11.M (effects of recently issued accounting standards)
- SAB 121 (cryptocurrency; rescinded as of January 2025)

For nonissuer reporters, SAB content is persuasive only. Tag as
`weight: gaap_non_authoritative`. For SEC issuer reporters, SAB
is binding on the registrant for SEC filing purposes but is still
not part of authoritative GAAP under ASC 105.

## EITF abstracts (post-codification)

The Emerging Issues Task Force discusses emerging issues. The EITF
issues abstracts that, upon ratification by FASB, are codified
into the ASC. Once codified, cite the ASC location.

Pre-codification EITF that was carried forward: cite the codified
ASC location with `gaap_pre_codification_grandfathered`
weight_override_rationale where the legacy reference is necessary
for practitioner navigation.

## AICPA TPAs (Technical Practice Aids)

AICPA TPAs address specific industry / topic questions. They are
non-authoritative for GAAP but are widely consulted. Tag as
`authority_type: AICPA_TPA`, `authority_domain: gaap`,
`weight: gaap_non_authoritative`.

## Authority

- ASC 105-10-05-2 (the two-tier hierarchy itself):
  cite as `authority_type: FASB_ASC`, `weight: gaap_codified`.
- The hierarchy applies to all other ASC research.
