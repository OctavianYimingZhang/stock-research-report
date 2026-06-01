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
3. Run the Required Run-Level Workflow in `references/workflow-contract.md`; do not skip from source collection directly to prose.
4. Run the Alpha Discovery Phase and create one clear thesis spine before collecting section prose.
5. Collect sources: latest annual/interim filings, earnings releases, transcripts, investor presentations, segment disclosures, balance-sheet data, peer data, price/volume data, and relevant industry sources.
6. Build an evidence register: claim, source, date, metric period, extraction note, confidence level, and unresolved conflicts.
7. Replay outside thesis paths only as hypotheses; verify or reject them against primary and high-quality sources.
8. Route the opportunity archetype and mispricing archetype, then run the four-part opportunity test: demand expansion, scaling difficulty, bottleneck scarcity, and commercialization visibility.
9. Analyze business logic, customer/order quality, operations, financial quality, valuation, short-risk, technical setup, and the decision scorecard in one causal sequence.
10. Draft the report with citations beside the claims they support. Keep assumptions explicit.
11. Run local validation scripts only when producing or changing repository artifacts.

## Required Run-Level Workflow

Every full report run must create or explicitly block the same object chain:

```text
ResearchSettings -> SourcePreflight -> SourceSnapshot -> SourcePartition
-> ArticleThesisMap -> ThesisPathReplay -> AlphaDiscovery -> ThesisSpine
-> TechnicalMechanismPrimer -> OpportunityArchetype -> MispricingAssessment
-> CompanyControlPointAssessment -> OperatingMachine -> DemandProxyMap
-> ProfitCashFlowQualityAnalysis -> EarningsRevisionBridge -> ValuationCase
-> ShortSellerAssessment -> EarlyWarningDashboard -> TechnicalSetup
-> CatalystLinkedTradePlan -> DecisionScorecard -> FinalReport
```

The flow fails closed. A missing object does not disappear; it becomes a
`DataGap`, gate warning, or blocker that caps valuation, position size, action
grade, or trade levels.

## Alpha Discovery Phase

Before drafting, identify the investment mispricing path:

1. What does the market currently believe?
2. What is the non-consensus or under-modeled variable?
3. What value-chain bottleneck makes the company relevant now?
4. What company-specific control point converts the bottleneck into economics?
5. Which operating metric will revise first: revenue, gross margin, EBITDA, EPS, FCF, orders, or multiple?
6. What would prove the thesis wrong within 1-4 quarters?

Do not proceed to final prose until the report has one clear thesis spine:

```text
non-consensus variable -> industry bottleneck -> company control point
-> order, capacity, or customer evidence -> revenue, margin, or cash-flow path
-> valuation denominator change -> catalyst -> disconfirming evidence
-> trade action
```

If no alpha spine exists, classify the idea as watchlist or research-only.

Required output objects:

- `AlphaDiscovery`: market belief, non-consensus variable, proof path, and broken-thesis signal.
- `MispricingAssessment`: suspected market error and correct valuation denominator.
- `ThesisSpine`: causal path from bottleneck to trade action.
- `CompanyControlPointAssessment`: why the issuer captures economics rather than industry beta.

`AlphaDiscoveryGate` blocks a high-conviction conclusion when any of these are
missing, unsupported, or contradicted by primary evidence.

## Investor Memo Skeleton

Before final prose, assemble this skeleton:

```text
opening investment dispute
-> thesis spine / mispricing table
-> technical or policy mechanism primer when needed
-> value-chain control point
-> demand proxy and order-quality ladder
-> operating machine and operating leverage bridge
-> EPS/EBITDA/FCF revision bridge
-> current-price-implied valuation
-> alpha/base/broken case set
-> early warning dashboard
-> catalyst-linked trade plan
```

Each section must end with a decision-useful judgment or a blocked conclusion.

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
