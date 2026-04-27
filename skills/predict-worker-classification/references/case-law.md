# Case-law touchstones — worker classification

The leading authorities the skill should consider when weighing
common-law factors. Cite the primary source; supplement with the
practitioner-friendly summaries in IRS Pub 1779 (NOT authority).

## Federal — common-law touchstone cases

### NLRB v. Hearst Publications, Inc., 322 U.S. 111 (1944)
Early articulation of the "economic reality" test for employment
relationships. Largely superseded by statute (the 1947 Taft-Hartley
amendments to the NLRA) but the reasoning informs the IRS's view of
control as the touchstone.

### Community for Creative Non-Violence v. Reid, 490 U.S. 730 (1989)
SCOTUS adopted the common-law agency test for "employee" under the
Copyright Act, listing factors that closely parallel Rev. Rul. 87-41
factors. Often cited in tax cases for the proposition that "no one
factor is determinative."

### Nationwide Mutual Insurance Co. v. Darden, 503 U.S. 318 (1992)
SCOTUS held that "employee" in ERISA, when not defined, takes its
common-law meaning. Reaffirms the Reid common-law agency test as
the federal default.

### Weber v. Commissioner, 103 T.C. 378 (1994), aff'd 60 F.3d 1104
(4th Cir. 1995)
Tax Court's classic application of the common-law factors.

### General Investment Corp. v. United States, 823 F.2d 337 (9th
Cir. 1987)
Examines the right-to-control versus actual-control distinction.

### Ewens & Miller, Inc. v. Commissioner, 117 T.C. 263 (2001)
Walks through the IRS's common-law factors, with extensive § 530
analysis.

## § 530 safe-harbor cases

### Springfield v. United States, 88 F.3d 750 (9th Cir. 1996)
Industry-practice prong of § 530 — what constitutes "long-standing
recognized practice of a significant segment of the industry."

### Lambert's Nursery & Landscaping, Inc. v. United States, 894
F.2d 154 (5th Cir. 1990)
Reasonable-basis prong of § 530.

### Joseph M. Grey Public Accountant, P.C. v. Commissioner, 119
T.C. 121 (2002)
Consistency requirement under § 530 — all similarly-situated
workers must have been treated the same way.

## Industry-specific federal cases

### Trucking
- Trans-Western Express v. Commissioner, T.C. Memo. 1985-561
- Kellie's Mobile Home Repair, T.C. Memo. 1992-462

### Healthcare
- Coyle's Pet Supply v. Commissioner — analog principles for
  professional services.

### Insurance
- Day v. Commissioner, T.C. Memo. 1995-396 — life-insurance agents
  and § 3121(d)(3)(B) statutory-employee status.

## State authority — California ABC test

### Dynamex Operations W. Inc. v. Superior Court, 4 Cal. 5th 903
(2018)
California Supreme Court adopted the ABC test for wage-order
purposes; later codified by AB5 at Cal. Lab. Code § 2775 (2019).

### Vazquez v. Jan-Pro Franchising Int'l, Inc., 10 Cal. 5th 944
(2021)
Confirmed Dynamex applies retroactively.

### S.G. Borello & Sons v. Dep't of Industrial Relations, 48 Cal.
3d 341 (1989)
Pre-Dynamex multi-factor test, still relevant for non-wage-order
ABC contexts (workers' comp, etc.).

## State authority — Massachusetts ABC test

Massachusetts ABC test codified at Mass. Gen. Laws ch. 149, § 148B,
predates California's by decades. Strict ABC test (any prong fails =
employee).

## Citation discipline notes

- Quote ≤ 75 words verbatim from each cited case in the JSON
  sidecar's `quoted_text` field.
- For California cases retrieved via courts.ca.gov / Justia /
  CourtListener, use the canonical URL.
- For Tax Court Memo opinions, retrieve from DAWSON
  (https://dawson.ustaxcourt.gov) and use the DAWSON URL.
- Note: Court of Appeals decisions are `binding_circuit` only in
  the taxpayer's circuit (Golsen rule); flag accordingly.

## Non-authority practitioner aids

These are useful background but NEVER authority:

- IRS Pub 1779 (Independent Contractor or Employee)
  https://www.irs.gov/pub/irs-pdf/p1779.pdf
- IRS Pub 15-A (Employer's Supplemental Tax Guide)
- IRM 4.23 (Employment Tax) — internal practice manual
- DOL Fact Sheet #13 (Employment Relationship Under FLSA) — DOL's
  view, NOT IRS's; useful for FLSA-coordinated state analyses
- Form SS-8 instructions — describes the determination procedure

Tag all of the above as `persuasive_non_authority` (or
`not_authority` for DOL Fact Sheet for tax purposes) in the JSON
sidecar.
