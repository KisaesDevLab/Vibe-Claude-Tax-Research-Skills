# Follow-up routing

Every skill output ends with the verification checklist (per
`shared/compliance.md`) and then with the follow-up-routing block
defined here. The block is markdown only — it does NOT modify the
JSON sidecar. The user's reply to the block triggers a fresh skill
invocation, which produces its own sidecar.

The dispatcher (`skills/cpa-pack-index/SKILL.md` "Metamorphic
routing" sub-table) recognizes the bracketed verbs in the user's
reply and routes to the destination skill.

## Mandatory output block (verbatim format)

Append this block to the end of the markdown response, after the
verification checklist appendix and before the JSON sidecar fence.
Substitute `<skill-name>` with the skill that produced the output.
Substitute `<one-line conclusion>` with a ≤ 25-word echo of the
conclusion so the routing target has context if the user replies.

```
---

## Next steps (follow-up routing)

This output is a draft from `<skill-name>`. Two follow-ups are
available — pick zero, one, or both:

**Package** the result as:
- `memo` — formal memorandum (issue, facts, analysis, conclusion,
  authorities) suitable for the engagement file
- `open-point` — items still requiring client confirmation, citator
  review, or additional research; reads from the
  `unresolved_citations` sidecar field plus any factual gaps surfaced
  during analysis

**Carry** the conclusion forward into:
- `plan` — planning actions, multi-year projection, or strategy
  library lookup
- `workpaper` — accounting / audit / review / compilation workpaper
  scaffold *(scaffold ships in Phase 10b; today this verb routes to a
  placeholder explanation)*
- `resolution` — IRS notice response, reasonable-cause request,
  penalty / interest computation, or Tax Court procedure
- `return` — return summary, line explainer, due-date calculation,
  or election attachment

Reply with one or two of the bracketed verbs (e.g., "memo + plan",
"open-point", "carry to resolution") and the dispatcher will route
this conclusion forward. Reply "stop" or leave blank to end the
chain here.

Conclusion echo: <one-line conclusion>
```

## Routing destinations (read by the dispatcher)

| Verb | Destination skill(s) | Notes |
|---|---|---|
| `memo` | originating research skill (re-emits in formal memo layout) | All 11 research skills already produce memo-shaped markdown; the verb is a formatting pass + header injection |
| `open-point` | dispatcher emits a stand-alone open-point list | Reads `unresolved_citations[]` from the prior sidecar; no new skill invocation needed |
| `plan` | `planning-actions-1040` \| `planning-actions-entity` \| `planning-multi-year` \| `planning-strategy-library` | Disambiguate by entity context: 1040 → individual; 1120/1120-S/1065 → entity; multi-year sunset → multi-year; "what strategies" → strategy library |
| `workpaper` | **placeholder** (Phase 10b) | Today: dispatcher emits an explanation noting the `workpaper-templates` skill is on the Phase 10b roadmap and offers `compliance-sas-audit` / `compliance-ssars` / `compliance-attestation-qm` as the closest existing skills for procedural guidance |
| `resolution` | `notice-response` \| `predict-reasonable-cause` \| `penalty-interest-calc` \| `tax-research-procedure` | Disambiguate by user signal: notice attached → notice-response; abatement language → reasonable-cause; dollar computation → penalty-interest-calc; SOL / Tax Court → tax-research-procedure |
| `return` | `return-summary-1040` \| `return-summary-entity` \| `form-line-explainer` \| `due-date-calculator` \| `tax-elections-library` | Disambiguate by entity / line / date / election keyword |

Reply parsing is case-insensitive and tolerant of punctuation: `Memo`,
`MEMO`, `memo,`, `memo + plan`, `memo and plan` all parse to the same
verb set.

## Open-point branch — stand-alone format

When the user picks `open-point`, the dispatcher emits the following
block from the prior sidecar without invoking a new specialist:

```
## Open points carried forward from <skill-name> (<generated_at>)

### Unresolved citations
<for each item in unresolved_citations[]>
- **<proposition>** — search: `<search>` (logged <date>)

### Factual gaps surfaced during analysis
<for each labeled assumption in the prior analysis>
- **<assumption>** — confirm with client / source documents

### Citator gaps (residual practitioner responsibility)
<emit only if negative_treatment_review_required: true>
- Independent citator check on every cited case (KeyCite / Shepards /
  BCite / Citator 2nd) — free-source pack cannot detect implicit
  overrules.
- Confirmation that each cited Rev. Rul. / Notice / Procedure has not
  been modified, superseded, obsoleted, or revoked.
- Confirmation that each cited Treasury Regulation has not been
  amended since the retrieved_date.

This open-point list is an engagement-file artifact. Pair it with
the prior memo when the engagement closes.
```

## Hard rules

- The follow-up-routing block is appended to EVERY skill's markdown
  response, including the dispatcher's own routing card.
- The block does not appear inside the JSON sidecar; it is markdown
  continuation only.
- The `workpaper` verb routes to the Phase 10b placeholder until that
  skill ships. The placeholder must explicitly name the gap so the
  practitioner is not misled into expecting workpaper output.
- The block must not invent destinations. If the originating skill
  has already exhausted its handoff target (e.g., `due-date-calculator`
  asked to "carry to a return process" — already inside the return
  process), the dispatcher recognizes the loop and emits "no
  downstream handoff applies" rather than re-invoking the same skill.
- The `<one-line conclusion>` echo is ≤ 25 words. Longer echoes
  defeat the routing target's context window.

## Gap: workpaper destination (Phase 10b candidate)

The pack does not yet ship a `workpaper-templates` skill. Phase 10b
is scoped to deliver:
- `skills/workpaper-templates/SKILL.md`
- `references/{pbc-list, tickmark-legend, lead-sheet, indexing-convention,
  audit-variant, review-variant, compilation-variant}.md`
- 3 eval cases.

Until Phase 10b ships, the `workpaper` verb routes to a placeholder
explanation in the dispatcher.
