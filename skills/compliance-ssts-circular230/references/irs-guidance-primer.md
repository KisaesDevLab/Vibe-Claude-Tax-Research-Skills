# IRS Guidance Primer — for malpractice-defense scaffolding

## Source

IRS "Understanding IRS Guidance — A Brief Primer":
https://www.irs.gov/newsroom/understanding-irs-guidance-a-brief-primer

## Authority status

- `authority_type: IRSNewsRelease`
- `weight: persuasive_non_authority`

The IRS's own characterization of the guidance hierarchy is NOT
authority; the IRS does not (and cannot) bind itself or the
courts as to the weight given to its own pronouncements. However,
the Primer is useful as a malpractice-defense scaffolding artifact
because it:

- Tracks the AICPA SSTS / Circular 230 expectations.
- Aligns with Treas. Reg. §1.6662-4(d)(3)(iii) authority hierarchy.
- Provides a client-facing explanation of why some IRS
  pronouncements are more reliable than others.

## What the Primer covers

The Primer describes the various forms of IRS guidance:

### Regulations

- Regulations are issued by Treasury (signed by Secretary or
  Assistant Secretary) with the force of law unless held invalid.
- Final regulations.
- Temporary regulations (3-year limit per §7805(e)).
- Proposed regulations.

### Revenue Rulings

- Official interpretations of the Code, Treasury Regulations, and
  treaties.
- Published in the Internal Revenue Bulletin.
- Authoritative; binding on IRS personnel.
- Not binding on courts or taxpayers.

### Revenue Procedures

- Statements of procedure that affect taxpayer rights or duties.
- Published in the IRB.
- Examples: Rev. Proc. 2013-30 (S-corp late-election relief);
  Rev. Proc. 2019-38 (rental-real-estate safe harbor).

### Notices and Announcements

- Public pronouncement on substantive or procedural matter.
- Published in the IRB.
- Notices typically substantive; Announcements typically
  procedural / news.

### Private Letter Rulings (PLRs)

- Written determination on the application of law to a specific
  set of facts.
- Issued at taxpayer request.
- §6110(k)(3) — no precedential value to other taxpayers.
- Cite as `PLR` / `written_determinations`.

### Technical Advice Memoranda (TAMs)

- Written determination issued in response to a request from an
  IRS examination office.
- §6110(k)(3) — no precedential value to other taxpayers.

### Chief Counsel Advice (CCA)

- Written advice prepared by the IRS Office of Chief Counsel.
- §6110 — disclosed but no precedential value to other taxpayers.

### Forms and Instructions

- Procedural guidance for taxpayers.
- Tag as `Form` or `Instructions` /
  `weight: persuasive_non_authority`.

### Internal Revenue Manual (IRM)

- IRS's internal procedural guide.
- Tag as `IRM` / `weight: persuasive_non_authority`.

### Audit Technique Guides (ATG)

- IRS guides for examiners on specific industries.
- Tag as `ATG` / `weight: persuasive_non_authority`.

## Why the Primer matters

Even though the Primer is `persuasive_non_authority`, it serves
several important functions for the practitioner:

1. **Client communication**: provides a plain-language
   explanation of why the practitioner relies on some IRS
   pronouncements more than others.

2. **Engagement-letter risk disclosure**: cite the Primer when
   describing the firm's research methodology.

3. **Malpractice defense**: demonstrates that the practitioner's
   research aligned with the IRS's own characterization of the
   guidance hierarchy.

4. **Authority weighting**: when no other tier of authority is
   available, the Primer's characterization of a specific
   guidance type can support a confidence-band determination.

## How to use the Primer in compliance-ssts-circular230

1. When advising a client about authority weight, cite the IRS's
   own characterization for transparency.
2. When drafting an engagement letter, reference the Primer in
   the methodology description.
3. When constructing a malpractice-defense file, include the
   Primer reference alongside Treas. Reg. §1.6662-4(d)(3)(iii).
4. NEVER use the Primer as the closest authority for a contested
   position; pair with a higher-tier authority.

## Citation format

```json
{
  "authority_type": "IRSNewsRelease",
  "citation": "IRS, 'Understanding IRS Guidance — A Brief Primer'",
  "url": "https://www.irs.gov/newsroom/understanding-irs-guidance-a-brief-primer",
  "retrieved_date": "[YYYY-MM-DD]",
  "quoted_text": "[verbatim ≤75 words]",
  "weight": "persuasive_non_authority"
}
```

## Cross-references

- `shared/authority-hierarchy.md` — full Treas. Reg.
  §1.6662-4(d)(3)(iii) hierarchy.
- `shared/citation-discipline.md` — required fields per citation
  entry.
- `shared/compliance.md` — full SSTS / Circular 230 checklist
  template.
- `shared/confidence-bands.md` — confidence-band-to-authority
  mapping.
