# Contributing

Contributions are welcome. Please follow these guidelines:

## What to Contribute

- report-structure improvements
- reference-framework improvements
- validation rules that prevent weak generated reports
- bug reports for missing sections, unsupported facts, weak valuation bridges,
  stale chart levels, or incomplete trade plans

## How to Contribute

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with `python3 scripts/validate.py`
5. Submit a pull request

## Standards

- Keep the Skill self-contained.
- Do not add runtime dependencies on standalone companion Skills.
- Do not embed prior report company names, tickers, or temporary calibration
  targets as triggers.
- Keep GitHub-facing text in English.
- Keep source, valuation, short-risk, and technical-analysis rules enforceable
  through validation wherever practical.
