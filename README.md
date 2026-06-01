# Stock Deep Research Skill

A Codex Skill for source-backed public-company research reports.

## What it does

- Builds company research reports from filings, transcripts, presentations, market data, and cited evidence.
- Separates verified facts, calculations, assumptions, and interpretation.
- Supports business-model analysis, financial-quality review, valuation scenarios, short-risk review, and technical context.
- Forces an alpha-thesis spine: market mispricing, company control point, demand proxy, revision bridge, proof event, broken-thesis signal, and trade action.
- Adds asset-financing adapters for subscription fleets, tax-credit monetization, project-finance cadence, management metrics, and action-trigger matrices.
- Maintains a source log so report claims can be traced to evidence.

## Skill entrypoint

Use [`SKILL.md`](SKILL.md). The remaining files are optional resources loaded only when a task needs them.

## Repository layout

| Path | Purpose |
| --- | --- |
| `SKILL.md` | Agent-facing operating instructions. |
| `contracts/` | Machine-readable report-section and gate contracts. |
| `references/` | Focused analysis frameworks. |
| `config/` | User settings schema and default profile. |
| `scripts/` | Local checks and report utilities. |
| `evals/` | Public regression fixtures for report behavior. |

## Local checks

```bash
python3 scripts/validate.py
python3 scripts/validate_settings.py
python3 scripts/validate_contracts.py
python3 scripts/validate_report_output.py --view full_report evals/fixtures/report-contract-fixture.md
python3 scripts/validate_report_output.py --view valuation_memo evals/fixtures/valuation_memo.md
python3 scripts/validate_report_output.py --view trade_plan_only evals/fixtures/trade_plan_only.md
python3 scripts/validate_research_manifest.py evals/fixtures/report-contract-fixture.manifest.json
python3 scripts/validate_report_against_manifest.py evals/fixtures/report-contract-fixture.md evals/fixtures/report-contract-fixture.manifest.json
```

## Architecture

`SKILL.md` is the entry layer. `config/` defines run settings. `contracts/`
defines canonical output sections and gates. `references/` defines domain
rules. `scripts/` validates the repository, contracts, reports, and research
manifests. `evals/` stores synthetic regression cases.

Older companion Skills and compacted copies are not runtime dependencies. Their
useful ideas must be distilled into a reference rule, manifest object, gate,
validator, or eval case.

## Evidence standard

Prefer primary sources. When a claim depends on estimates, assumptions, or secondary commentary, label it as such and cite the supporting source.

## License

See [`LICENSE`](LICENSE).
