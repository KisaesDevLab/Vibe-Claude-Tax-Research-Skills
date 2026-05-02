---
name: cpa-pack-index
description: |
  Always-on dispatcher for the Vibe CPA Skills pack. Routes a CPA's
  question to the correct specialist skill (research, prediction,
  summary, planning, utility, compliance) and reads shared rules of
  the road before any specialist runs. Use when the user opens a tax
  conversation, asks "which skill should I use", references a Public
  Law popular name (TCJA, IRA, OBBBA, SECURE 2.0, CARES Act, ARPA),
  pastes a notice, drops a return PDF, asks a federal or state
  research question, asks "is this a hobby", "is this person an
  employee or 1099", "can my client take §199A", "what changed in
  §174 under OBBBA", or asks for year-end planning. Make sure to use
  this skill whenever the user mentions tax research, IRS notice,
  return summary, planning ideas, state nexus, or a Public Law name.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob
---

# cpa-pack-index — Dispatcher

This is the always-on entry point for the Vibe CPA Skills pack. It
does no substantive analysis itself; it (1) reads the shared rules of
the road, (2) classifies the user's request, and (3) hands off to the
right specialist skill.

## Read before output (every turn)

Before any classification or hand-off, read:

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `shared/legislation-tracking.md` (if the user mentioned a Public
   Law popular name or number, or asked "what changed under …")

The specialist skill will then load any topic-specific references.

## Routing table

| If the user… | Hand off to |
|---|---|
| Asks a federal Code/Reg/case question or wants substantive research | `tax-research-federal` |
| Asks an entity-tax question (C-corp, S-corp, partnership, LLC choice) | `tax-research-entity` |
| Asks about employment-tax, payroll, FICA/FUTA, household employee | `tax-research-payroll` |
| Asks an international, treaty, GILTI, FTC, FBAR/FATCA, FDII, or expat question | `tax-research-international` |
| Asks about audits, statutes of limitation, Tax Court procedure, CDP, IRS practice | `tax-research-procedure` |
| Asks about a STATE income-tax position, residency, PTET, conformity, NY convenience rule | `tax-research-state-income` |
| Asks about state sales/use tax, Wayfair nexus, marketplace facilitator, SaaS taxability | `tax-research-state-salesuse` |
| Asks about estate, gift, GST, Form 706 / 709, basis step-up | `tax-research-estate-gift` |
| Asks "is this person W-2 or 1099" | `predict-worker-classification` |
| Asks "is this a hobby or business" | `predict-hobby-loss` |
| Asks "is owner comp reasonable" (S-corp, C-corp) | `predict-reasonable-comp` |
| Asks about real estate professional status | `predict-real-estate-pro` |
| Asks about §469 material participation | `predict-material-participation` |
| Asks about §199A QBI eligibility / SSTB | `predict-qbi-eligibility` |
| Asks about §1031 like-kind exchange qualification | `predict-1031-qualification` |
| Asks about economic substance / sham transaction | `predict-economic-substance` |
| Asks about debt vs equity (advances to a closely-held entity) | `predict-debt-vs-equity` |
| Asks about innocent spouse / §6015 relief | `predict-innocent-spouse` |
| Asks about §6651 / §6662 reasonable cause / first-time abatement | `predict-reasonable-cause` |
| Asks about §41 R&D / §174 R&E credit qualification | `predict-r-and-d-credit` |
| Pastes / uploads a Form 1040 or asks for an individual return summary | `return-summary-1040` |
| Pastes / uploads an entity return (1120, 1120-S, 1065, 1041) | `return-summary-entity` |
| Pastes an IRS notice (CP/LTR/4564/etc.) | `notice-response` |
| Asks "what should this individual do this year" | `planning-actions-1040` |
| Asks "what should this entity do this year" | `planning-actions-entity` |
| Asks for multi-year scenario planning, sunset/effective-date scoring | `planning-multi-year` |
| Asks "what strategies are available for …" or "give me ideas for …" | `planning-strategy-library` |
| Asks about S-corp owner planning, Form 1120-S line strategies, accountable-plan reimbursements to a 2%+ shareholder, Augusta Rule, S-corp owner reasonable comp | `s-corp-strategy-catalog` |
| Asks about Schedule C / SMLLC default planning, Form 8829 home office, §105 HRA spouse, hire-your-child sole prop, rent-from-spouse, heavy-vehicle + home-office combo, §274(c) foreign travel | `schedule-c-strategy-catalog` |
| Asks about a tax election by name, IRC section, or Rev. Proc. (e.g., "§83(b)", "§754", "QSST", "Rev. Proc. 2013-30 late S"), or asks for sample election attachment language | `tax-elections-library` |
| Asks "what does §X say" or references a Public Law popular name | `irc-section-lookup` |
| Asks "what does Reg §1.X-Y say" or references a TD | `treas-reg-lookup` |
| Asks "what is line N on Form X" | `form-line-explainer` |
| Asks about a deadline / due date / extension | `due-date-calculator` |
| Asks for §6651/§6654/§6662 penalty + interest computation | `penalty-interest-calc` |
| Asks about SSTS, Circular 230, written-advice standards, disclosure forms | `compliance-ssts-circular230` |

## Public-Law trigger phrases (high-confidence)

If the user's request contains any of these, route to
`irc-section-lookup` first (which will then chain to the substantive
skill via `tax-research-federal` or `planning-multi-year`):

- TCJA, Tax Cuts and Jobs Act, P.L. 115-97
- CARES Act, P.L. 116-136
- American Rescue Plan, ARPA, P.L. 117-2
- Inflation Reduction Act, IRA, P.L. 117-169
- SECURE 2.0, Pub. L. 117-328 div. T
- One Big Beautiful Bill Act, OBBBA, P.L. 119-XX
- "what changed in §X under <act>", "post-<act> rule", "current law"

## Hard rules

- This skill emits NO substantive tax analysis. Its only job is to
  classify and hand off.
- It always loads the four core shared rules first (citation
  discipline, authority hierarchy, confidence bands, compliance).
- For state questions, if the user has not given a state code,
  prompt for the jurisdiction before invoking the state specialist.
- For multi-issue questions, decompose and route each issue.
- Never fabricate citations. If the user has cited an authority that
  doesn't appear to exist, flag it before routing.

## Output

A short routing card:

```
Routing: <skill-name>
Reason: <one line>
Citations to verify (if any): <Public-Law popular names, state codes>
```

Then hand off to the specialist; the specialist produces the markdown
+ JSON sidecar.

## Verification checklist (appendix)

The dispatcher does no substantive work, so the specialist's checklist
applies. The dispatcher only confirms:
- [ ] The four shared rules of the road were loaded.
- [ ] State code captured for state-tax questions.
- [ ] Public-Law popular names routed via `irc-section-lookup` when
      legislative-history workflow is implicated.
- [ ] Negative-treatment-review residual responsibility was forwarded
      to the specialist.

The full SSTS / Circular 230 verification checklist lives in
`shared/compliance.md` and is completed by the specialist skill.
