# Ontology Framework

This reference turns the report Skill into an ontology-driven research workflow.
The report is the final view. The source of truth is an object graph of
evidence, claims, article-thesis maps, opportunity archetypes, demand and
scarcity assessments, metrics, orders, assets, debt, valuation cases,
short-risk signals, profit/cash-flow quality, decision scorecards, technical
setups, data gaps, and report sections.

## Design Principle

Do not model the report outline as the core system. Model the real research
objects first, then project them into the fixed report sections.

The central object is the evidence-backed `Claim`. A claim can be a verified
fact, inference, scenario assumption, or opinion. Material claims must be linked
to evidence before they can support valuation, risk, technical levels, or final
trade recommendations.

## Core Object Graph

Use the lightweight ontology files in `ontology/`:

- `ontology/object_types.yaml`
- `ontology/link_types.yaml`
- `ontology/action_types.yaml`
- `ontology/functions.yaml`
- `ontology/workflow_gates.yaml`

Research objects move through the research lakehouse described in
`references/research-lakehouse-framework.md`: Bronze source snapshots, Source
Index partitions, Silver validated evidence, Gold analysis products, and Report
View projections.

Minimum object layer:

- `ResearchSettings`
- `UserHypothesis`
- `ResearchRun`
- `ArticleThesisMap`
- `ThesisPathReplay`
- `OpportunityArchetype`
- `DemandExpansionAssessment`
- `ScalingDifficultyAssessment`
- `ScarcityBottleneckAssessment`
- `CommercializationPathAssessment`
- `Company`
- `Security`
- `SourceDocument`
- `SourceSnapshot`
- `SourcePartition`
- `EvidencePartition`
- `EvidenceItem`
- `Claim`
- `ConflictResolution`
- `MetricObservation`
- `BusinessModelThesis`
- `ValueDriverTransition`
- `OperatingLeverageMap`
- `ContractOrder`
- `OrderQualityAssessment`
- `AssetFacility`
- `DebtInstrument`
- `DilutionInstrument`
- `FinancialQualityAssessment`
- `ProfitCashFlowQualityAnalysis`
- `CurrentMarketImpliedBridge`
- `ValuationMethodSelection`
- `EquityBridge`
- `ValuationCase`
- `ShortRiskSignal`
- `ShortSellerAssessment`
- `FalsificationPattern`
- `TechnicalSetup`
- `PositionSizingRationale`
- `ExpectationRevisionAssessment`
- `MomentumRegimeAssessment`
- `ValuationOddsAssessment`
- `RiskFilterAssessment`
- `DecisionScorecard`
- `TradePlan`
- `IncrementalRefreshPlan`
- `ActionExecution`
- `GateResult`
- `OutputView`
- `DataGap`
- `Report`
- `ReportSection`

## Claim Standard

Every material claim needs:

- `claim_text`
- `claim_type`
- `evidence_status`
- `source_strength`
- `materiality`
- `freshness_status`
- `confidence`
- `blocked_by_data_gap`

If `materiality` is `high`, at least one `EvidenceItem` must support or
contradict the claim before it can be used in a report section. Unsupported
high-materiality claims become `DataGap` objects.

## Link Standard

The most important links are:

- `ResearchSettings -> configures_run -> ResearchRun`
- `UserHypothesis -> tests_hypothesis -> Claim`
- `ArticleThesisMap -> replays_thesis_path -> ThesisPathReplay`
- `ThesisPathReplay -> tested_by_claims -> Claim`
- `OpportunityArchetype -> routes_company -> Company`
- `DemandExpansionAssessment -> supports_opportunity -> OpportunityArchetype`
- `ScalingDifficultyAssessment -> scaling_supports_opportunity -> OpportunityArchetype`
- `ScarcityBottleneckAssessment -> scarcity_supports_opportunity -> OpportunityArchetype`
- `CommercializationPathAssessment -> commercialization_supports_opportunity -> OpportunityArchetype`
- `SourceDocument -> contains -> EvidenceItem`
- `SourcePartition -> partitions_source -> SourceSnapshot`
- `SourcePartition -> routes_to_evidence -> EvidenceItem`
- `EvidenceItem -> derives_from -> SourceSnapshot`
- `EvidenceItem -> supports -> Claim`
- `EvidenceItem -> contradicts -> Claim`
- `EvidenceItem -> invalidates -> Claim`
- `EvidencePartition -> pruned_by_partition -> EvidenceItem`
- `Claim -> feeds -> BusinessModelThesis`
- `ContractOrder -> supports -> ValuationCase`
- `OrderQualityAssessment -> constrains -> ValuationCase`
- `DebtInstrument -> affects_equity_bridge -> EquityBridge`
- `DilutionInstrument -> affects_target_price -> EquityBridge`
- `EquityBridge -> bridges_to_target_price -> ValuationCase`
- `ProfitCashFlowQualityAnalysis -> cash_quality_supports_valuation -> ValuationCase`
- `ProfitCashFlowQualityAnalysis -> cash_quality_flags_short_risk -> ShortRiskSignal`
- `ShortRiskSignal -> discounts -> ValuationCase`
- `TechnicalSetup -> constrains -> TradePlan`
- `ExpectationRevisionAssessment -> expectation_feeds_scorecard -> DecisionScorecard`
- `MomentumRegimeAssessment -> momentum_feeds_scorecard -> DecisionScorecard`
- `ValuationOddsAssessment -> valuation_odds_feeds_scorecard -> DecisionScorecard`
- `RiskFilterAssessment -> risk_filter_feeds_scorecard -> DecisionScorecard`
- `DecisionScorecard -> scorecard_constrains_trade -> TradePlan`
- `ValuationCase -> valuation_constrains_trade -> TradePlan`
- `ShortSellerAssessment -> short_risk_constrains_trade -> TradePlan`
- `DataGap -> blocks -> Claim`
- `IncrementalRefreshPlan -> refreshed_by -> ActionExecution`
- `ResearchRun -> executes -> ActionExecution`
- `ActionExecution -> records_gate_result -> GateResult`
- `OutputView -> projects_view -> ReportSection`
- `ReportSection -> cites -> EvidenceItem`

The link verbs matter. They force the agent to distinguish evidence, causality,
valuation effects, blockers, and final report citations.

## Action Standard

Use actions as workflow transactions:

- `CaptureResearchSettings`
- `StartResearchRun`
- `AttachSourceDocument`
- `BuildSourcePartitions`
- `BuildEvidencePartitions`
- `ExtractEvidence`
- `MapArticleThesis`
- `BuildThesisPathReplay`
- `RouteOpportunityArchetype`
- `RunFourPartOpportunityTest`
- `NormalizeOperatingObjects`
- `ClassifyClaim`
- `ResolveConflictingFacts`
- `BuildBusinessModelThesis`
- `DetectSourceChange`
- `IncrementalRefresh`
- `GradeOrderQuality`
- `ReconcileFinancials`
- `AnalyzeProfitCashFlowQuality`
- `ReconcileShareCountAndEV`
- `InferCurrentMarketPricing`
- `SelectPrimaryValuationMethod`
- `BuildValuationCase`
- `BuildEquityBridge`
- `RunShortRiskScreen`
- `ValidateTechnicalSetup`
- `BuildDecisionScorecard`
- `BuildTradePlan`
- `GenerateReportSection`
- `SelectOutputView`
- `FinalizeReport`

Each action reads defined object types and writes defined object types. This
prevents a report from being produced directly from unstructured source text.

## Function Standard

Calculations and repeatable decisions belong in functions:

- enterprise value
- FCFF and FCFE
- risk-adjusted backlog value
- order-quality grade
- cash-conversion score
- cash-quality bridge
- working-capital cycle assessment
- SBC-adjusted FCF per share
- order-to-revenue bridge
- re-rating bridge
- funding bridge
- debt-safety score
- valuation-method selection
- target-price blocker detection
- explicit equity bridge calculation
- short-risk grade
- falsification lens
- decision scorecard construction
- action-grade cap determination
- technical freshness check
- position sizing from stop distance
- source conflict detection
- materiality classification
- material metric extraction
- outside thesis extraction
- opportunity archetype routing
- demand expansion assessment
- scaling difficulty assessment
- scarcity bottleneck assessment
- commercialization visibility assessment
- gate-result classification
- output-view selection

Functions should return either a value, a grade, or a blocking data gap.

## Workflow Gates

Before report composition, pass these gates:

- Lakehouse Layer Gate: Bronze, Source Index, Silver, Gold, and Report View
  boundaries are respected
- Settings Gate: runtime settings are complete and user hypotheses are not
  treated as evidence
- Article Map Gate: outside thesis paths are extracted and independently tested
- Opportunity Archetype Gate: issuer route is supported or capped
- Four-Part Opportunity Gate: demand expansion, scaling difficulty,
  bottleneck/scarcity, and commercialization visibility pass or block
- Evidence Gate: material claims have evidence links
- Lineage Gate: material conclusions trace to source snapshots
- Partition Coverage Gate: relevant evidence partitions are available or
  blocked
- Source Priority Gate: conflicting facts follow the source-priority order
- Order Gate: order evidence is graded and weak order signals do not support
  valuation without conversion proof
- Financial Gate: net income, OCF, working capital, and cash conversion are
  reconciled
- Profit Cash Flow Quality Gate: OCF, EBITDA, FCF, capex, SBC, dilution, and
  owner FCF are reconciled or explicitly blocked
- Debt Gate: cash, debt, maturity, interest, dilution, and share count feed the
  equity bridge
- Equity Bridge Gate: target price is blocked unless EV, cash, senior claims,
  non-operating assets, and diluted shares reconcile
- Valuation Gate: current-market-implied expectation appears before the target
- Short Risk Gate: elevated short risk affects valuation or position sizing
- Technical Gate: chart date, adjusted status, entry, stop, and take-profit are
  supported or blocked
- Decision Scorecard Gate: action grade and binding cap reason are supported by
  underlying analysis objects
- Freshness Gate: stale objects cannot drive valuation or technical levels
- Incremental Refresh Gate: changed sources refresh dependent objects or trigger
  a full rerun
- Output View Gate: output view changes projection without changing the source
  graph
- Data Gap Gate: blocked conclusions are not forced into the report

Gate results use `pass`, `warn`, `block`, `fail`, or `not_applicable`. Store the
status, reason, affected objects, blocked conclusions, and required user input
in `GateResult` through `ActionExecution`.

## Report Projection

The final report sections should read from the object graph:

- `Core Conclusion`: current dispute, action stance, position-size logic,
  upside variable, and invalidation
- `Why This Stock Exists Now`: article-thesis map, thesis-path replay, demand
  expansion, and current market attention trigger
- `Industry Chain And Bottleneck`: opportunity archetype, scaling difficulty,
  scarcity node, and scarcity duration
- `Company Position In The Chain`: company role, payer, customer avoided cost
  or risk, and industry-beta versus company-alpha judgment
- `Business Model Logic`: business model claims, value-driver transition, and
  operating leverage map
- `Scarcity And Moat Assessment`: scarcity bottleneck assessment and
  replication barriers
- `Customers, Orders, And Commercialization Path`: counterparties, orders,
  commercialization path, order quality, and order-to-revenue bridge
- `Operations, Capacity, And Execution Quality`: assets, facilities, capacity,
  capex, utilization, execution bottleneck, and margin at scale
- `Financial Quality, Assets, Debt, And Dilution`: metrics, assets, debt,
  dilution, financial quality, profit/cash-flow quality, and cash runway
- `Valuation And Market-Implied Expectation`: current-implied bridge, selected
  method, equity bridge, valuation cases, re-rating condition, and downside
  floor
- `Catalysts, Risks, And Falsification`: short-risk signals, short-seller
  assessment, falsification pattern, data gaps, and high-risk claims
- `Technical Structure And Trade Plan`: technical setup, freshness gate,
  position-sizing rationale, decision scorecard, and trade plan

Do not let a section own facts that are absent from the graph. Sections cite
evidence-backed claims.
