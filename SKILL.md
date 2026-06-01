---
name: stock-research-report
description: Build source-backed public-company deep research reports, valuation context, risk reviews, and investment memo drafts from current filings, market data, transcripts, and cited evidence.
---

# Stock Deep Research Report

Use this skill when the user asks for deep research on a listed company, ticker, sector, equity thesis, earnings setup, valuation context, risk review, or public-company investment memo.

## Operating rules

- Treat every factual claim as source-bound. Use primary filings, company investor-relations materials, exchange disclosures, earnings transcripts, and reputable market data before secondary commentary.
- Use current sources when prices, guidance, estimates, ownership, valuation multiples, macro data, or company leadership may have changed.
- Separate verified facts, calculations, estimates, and interpretation.
- State source dates and reporting periods.
- Do not provide personalized financial advice. Frame conclusions as research, scenarios, and decision considerations.
- If evidence is insufficient or conflicting, say so and keep the conclusion blocked or conditional.

## Workflow

1. Define scope: ticker/company, exchange, report date, time horizon, target audience, required depth, and whether the user wants a full report or a focused section.
2. Apply `contracts/report_sections.yaml` and `contracts/gates.yaml` as the canonical report contract before drafting.
3. Collect sources: latest annual/interim filings, earnings releases, transcripts, investor presentations, segment disclosures, balance-sheet data, peer data, price/volume data, and relevant industry sources.
4. Build an evidence register: claim, source, date, metric period, extraction note, confidence level, and unresolved conflicts.
5. Replay outside thesis paths only as hypotheses; verify or reject them against primary and high-quality sources.
6. Route the opportunity archetype and run the four-part opportunity test: demand expansion, scaling difficulty, bottleneck scarcity, and commercialization visibility.
7. Analyze business logic, customer/order quality, operations, financial quality, valuation, short-risk, technical setup, and the decision scorecard in one causal sequence.
8. Draft the report with citations beside the claims they support. Keep assumptions explicit.
9. Run local validation scripts only when producing or changing repository artifacts.

## Report structure

Use this canonical `full_report` order unless the user requests a narrower output view:

1. Core Conclusion
2. Why This Stock Exists Now
3. Industry Chain And Bottleneck
4. Company Position In The Chain
5. Business Model Logic
6. Scarcity And Moat Assessment
7. Customers, Orders, And Commercialization Path
8. Operations, Capacity, And Execution Quality
9. Financial Quality, Assets, Debt, And Dilution
10. Valuation And Market-Implied Expectation
11. Catalysts, Risks, And Falsification
12. Technical Structure And Trade Plan

## Repository resources

Read only the files needed for the user request:

- `contracts/report_sections.yaml`: canonical output-view section contracts.
- `contracts/gates.yaml`: gate requirements and blocker rules.
- `references/workflow-contract.md`: canonical run order and module boundaries.
- `references/skill-merge-policy.md`: rules for integrating older, compacted, or outside Skill material.
- `references/business-model-framework.md`: business model and segment analysis.
- `references/evidence-indexing-framework.md`: evidence register and source traceability.
- `references/incremental-refresh-framework.md`: updating an existing report with new filings or market data.
- `references/opportunity-discovery-framework.md`: screening and idea discovery.
- `references/profit-cash-flow-quality-framework.md`: earnings quality and cash conversion checks.
- `references/quality-calibration-loop.md`: report quality review.
- `references/report-style-patterns.md`: formatting and writing patterns.
- `references/scorecard-decision-framework.md`: scoring discipline.
- `references/short-seller-risk-framework.md`: short-risk review.
- `references/technical-analysis-framework.md`: optional price/volume analysis.
- `references/user-intake-settings-framework.md`: user preference and scope settings.
- `references/valuation-framework.md`: valuation process.
- `references/article-thesis-distillation-framework.md`: turning source articles into thesis notes.

## Local commands

- `python3 scripts/validate.py`: repository sanity check.
- `python3 scripts/validate_settings.py`: settings schema/profile check.
- `python3 scripts/validate_contracts.py`: contract consistency check.
- `python3 scripts/validate_report_output.py --view full_report <report.md>`: report format check.
- `python3 scripts/validate_research_manifest.py <manifest.json>`: source-manifest check.
- `python3 scripts/validate_report_against_manifest.py <report.md> <manifest.json>`: report-to-source consistency check.
