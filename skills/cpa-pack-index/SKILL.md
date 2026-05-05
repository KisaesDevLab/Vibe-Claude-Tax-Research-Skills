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
  research question, asks "is this a hobby", asks about engagement
  letters, audit / review / compilation, SSARS / SAS / SSAE / SOC /
  SQMS standards, AICPA Code of Professional Conduct, FASB ASC /
  GAAP, or ASC 740 / 606 / 842. Make sure to use this skill
  whenever the user mentions tax research, IRS notice, return
  summary, planning ideas, state nexus, a Public Law name,
  engagement letter, AICPA Code, audit standards, attest, SOC,
  GAAP, or ASC.
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
| Asks for an engagement letter (audit / review / compilation / preparation / tax / advisory / bookkeeping / payroll / consulting / SOC / AUP), scope of work, FTC Safeguards Rule clause, indemnification limits | `engagement-letter-library` |
| Asks about AICPA Code of Professional Conduct, ET §1.X, independence, threats and safeguards, §1.295 nonattest services, conflict of interest, confidentiality / subpoena, ethics interpretation | `compliance-aicpa-code` |
| Asks about SSARS, AR-C, compilation, review, preparation engagement, lack-of-independence compilation, going-concern review | `compliance-ssars` |
| Asks about audit standards (SAS / AU-C), AU-C 240 fraud, AU-C 315/330 risk assessment, AU-C 570 going concern, AU-C 600 group audit, audit reporting / qualified or adverse opinion | `compliance-sas-audit` |
| Asks about SOC 1 / SOC 2 / SOC 3, AT-C 105/205/215/320, attestation, agreed-upon procedures (AUP), SQMS 1 firm quality management, SQMS 2 engagement quality reviews | `compliance-attestation-qm` |
| Asks about ASC research generally, FASB, GAAP, ASU effective dates, business combinations (ASC 805), goodwill (ASC 350), changes in estimate (ASC 250), CECL (ASC 326), going concern (ASC 205-40), other ASC topics | `research-financial-reporting` |
| Asks about ASC 740, deferred tax (DTA / DTL), valuation allowance, uncertain tax position (UTP), FIN 48, tax provision, effective tax rate, intraperiod allocation, ASU 2023-09 disclosures | `research-asc-740` |
| Asks about ASC 606 revenue recognition (five-step model, performance obligations, variable consideration, principal vs agent), ASC 842 leases (classification, ROU asset, sale-leaseback) | `research-asc-606-842` |

## Metamorphic routing (Phase 10a — follow-up verbs)

Every specialist skill ends its markdown response with the follow-up-
routing block defined in `shared/follow-up-routing.md`. When the
user replies with one of the bracketed verbs from that block, route
metamorphically — the user is asking to repackage the prior
conclusion or carry it into a downstream artifact, not to start a
new substantive question.

| If the user's reply contains… | Hand off to |
|---|---|
| `memo` / "turn this into a memo" / "draft a memo" | originating research skill, re-emitted in formal memo layout |
| `open-point` / "open point" / "add to open points" / "open as an open point" | dispatcher emits a stand-alone open-point list per `shared/follow-up-routing.md` (no new skill invocation; reads `unresolved_citations[]` from the prior sidecar) |
| `plan` / "carry into a plan" / "start planning" / "what should I do next" | `planning-actions-1040` (1040 context) \| `planning-actions-entity` (1120/1120-S/1065/1041 context) \| `planning-multi-year` (sunset / multi-year scoring) \| `planning-strategy-library` ("what strategies") |
| `workpaper` / "carry into a workpaper" / "build a workpaper" | **placeholder (Phase 10b)** — emit the explanation: "The `workpaper-templates` skill is on the Phase 10b roadmap. The closest existing skills for procedural guidance are `compliance-sas-audit` (audit), `compliance-ssars` (review / compilation / preparation), or `compliance-attestation-qm` (attestation / SOC / SQMS). Choose one or wait for Phase 10b." |
| `resolution` / "carry into a resolution matter" / "open a resolution file" | `notice-response` (notice attached) \| `predict-reasonable-cause` (abatement language) \| `penalty-interest-calc` (dollar computation) \| `tax-research-procedure` (SOL / Tax Court) |
| `return` / "carry into the return process" / "back to the return" | `return-summary-1040` (individual) \| `return-summary-entity` (entity) \| `form-line-explainer` (specific line) \| `due-date-calculator` (deadline) \| `tax-elections-library` (election attachment) |

Routing rules:

- Verb parsing is case-insensitive and tolerant of punctuation.
  `Memo`, `MEMO`, `memo,`, `memo + plan`, `memo and plan` all parse.
- A user reply may contain one verb from each axis (one packaging
  verb + one carry-forward verb). Route both in sequence: package
  first, then carry.
- If the originating skill is already the natural destination for
  the carry-forward verb (e.g., `due-date-calculator` asked to
  "carry to the return process" — already inside the return
  process), emit "no downstream handoff applies — the prior output
  IS the return-process artifact" rather than re-invoking the same
  skill.
- "stop" / blank reply / no bracketed verb → end the chain.

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

After the routing card (and after the specialist's answer when the
dispatcher is operating in metamorphic mode), emit the follow-up-
routing block per `shared/follow-up-routing.md` (Phase 10a). For a
plain routing card, the conclusion echo is the routing decision
itself ("Routed to `<skill>` because `<reason>`").
