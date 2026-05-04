# Out-of-scope external pointers — GASB / IFRS / PCAOB

This pack targets U.S. GAAP for non-governmental, non-public,
non-IFRS reporters. Other frameworks are out of scope.

## GASB (Governmental Accounting Standards Board)

State and local governmental entities apply GASB's Codification
of Governmental Accounting and Financial Reporting Standards,
NOT FASB ASC.

- GASB home: https://gasb.org
- GASB Codification: https://gars.gasb.org

When the user mentions a governmental entity (state, county, city,
school district, special district, public university, public
hospital, water/sewer authority), route to GASB externally:
> "Governmental entities apply GASB Codification, not FASB ASC.
> See https://gars.gasb.org. This pack does not produce GASB
> work product."

For Single-Audit / Yellow-Book / federal-grant audit work, see
GAO Yellow Book externally:
> "Yellow Book / GAGAS standards apply to government / federal-
> grant audits. See https://www.gao.gov/yellowbook. Out of scope."

## IFRS (International Financial Reporting Standards)

IFRS reporters apply standards issued by the IASB.

- IFRS Foundation: https://www.ifrs.org
- IFRS Sustainability Disclosure Standards (ISSB): also at IFRS
  Foundation.

When the user mentions an IFRS reporter (foreign private issuer
filing IFRS with SEC; IFRS-applying private company; IFRS as a
secondary framework), route externally:
> "IFRS reporters apply IASB-issued standards, not FASB ASC. See
> https://www.ifrs.org. This pack does not produce IFRS work
> product. For dual-reporting U.S. GAAP / IFRS reconciliation,
> consult specialty resources."

## PCAOB (Public Company Accounting Oversight Board)

PCAOB AS standards govern audits of issuers (SEC-registered
public companies and other PCAOB-registered audits). Note: PCAOB
governs the AUDIT, not the GAAP itself; SEC issuers still apply
ASC for their financial statements (with SEC overlays via SAB,
S-X, S-K).

- PCAOB home: https://pcaobus.org
- PCAOB AS standards: https://pcaobus.org/oversight/standards

When the user mentions issuer ICFR / SOX 404(b) / SEC-registered
audit, route audit questions externally; ASC research can still
be performed in this skill for the underlying GAAP.

## SEC (Securities and Exchange Commission)

SEC issues:
- Regulation S-X (financial reporting requirements for filings).
- Regulation S-K (non-financial disclosure requirements).
- Staff Accounting Bulletins (SAB) — non-authoritative for ASC
  but practically binding on registrants.
- Industry Guides.
- Staff guidance (no-action letters, CDIs).

For nonissuer-pack scope, SEC overlays are persuasive only. For
SEC registrant work, route to specialty SEC resources externally.

## IIA (Internal Audit)

The Institute of Internal Auditors issues International Standards
for the Professional Practice of Internal Auditing.

- IIA standards: https://www.theiia.org/en/standards

Out of scope for this pack (which targets external CPA firms, not
in-house internal auditors).

## AICPA Cybersecurity Risk Management Reporting

The AICPA's separate cybersecurity reporting framework is distinct
from SOC 2 (which uses Trust Services Criteria). Route specialized
cybersecurity reporting questions externally.

## Authority

For any pointer above:
- Cite the URL with `authority_type: AICPA_PracticeAid` or generic
  external (not formally part of any authority_type enum).
- Tag `weight_override_rationale: "out of scope; external pointer
  only"`.
- Use only as routing context, not as substantive authority.
