# Skill Merge Policy

Use this policy when incorporating rules from older companion Skills, compacted
copies, outside prompts, or new Skill drafts.

## Merge Unit

Do not paste full external Skills into `SKILL.md`. Distill useful material into
one or more of these units:

- reference rule
- manifest object
- gate
- validator check
- eval case
- output-view section contract

## Compatibility Checks

A candidate rule can enter the Skill only if it satisfies all checks:

- Evidence-compatible: no unsupported facts enter the final report.
- Advice boundary-compatible: output remains research, scenarios, and decision
  considerations, not personalized financial advice.
- Self-contained: no runtime dependency on another standalone Skill.
- License-compatible: copied or adapted text can be redistributed.
- Non-duplicative: it adds a new rule, gate, object, or testable condition.
- Testable: it can be expressed in a validator, fixture, or eval case.
- Report-compatible: it does not break the canonical report contract.
- Freshness-aware: volatile data requires current sources or a blocked result.

## Canonical Module Targets

Map candidate content into the existing modules:

| Candidate capability | Merge target |
| --- | --- |
| Business or fundamental analysis | `business-model-framework.md` and `workflow-contract.md` |
| Opportunity discovery or theme routing | `opportunity-discovery-framework.md` and `contracts/gates.yaml` |
| Article or outside-thesis replay | `article-thesis-distillation-framework.md` |
| Valuation or financial modeling | `valuation-framework.md` and `profit-cash-flow-quality-framework.md` |
| Short-seller or forensic risk | `short-seller-risk-framework.md` |
| Technical analysis or trade execution | `technical-analysis-framework.md` |
| Decision summary or grading | `scorecard-decision-framework.md` |

## Rejection Rule

Reject content that relies on unsourced claims, proprietary unavailable data,
black-box forecasts that override evidence gates, or instructions that produce
module-stitched reports instead of one integrated memo.
