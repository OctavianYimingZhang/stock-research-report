# Workflow Contract

This file is the canonical run order for the Skill. Other references define
domain rules; this file defines how those rules are sequenced.

## Required Run-Level Workflow

```text
PHASE 0 - Intake
Input: ticker/company, report date, output view, horizon, user focus, uploaded notes.
Output: ResearchSettings, UserHypothesis, SourcePreflight.
Gate: company identity resolved or blocked.

PHASE 1 - Source Preflight
Actions: list required source classes; fetch latest filings, earnings release,
transcript, investor deck, price data, and relevant customer, policy, or
counterparty sources; mark unavailable sources as DataGap.
Output: SourceSnapshot list, SourcePartition list, DataGap list.
Gate: SourcePriorityGate.

PHASE 2 - Outside Thesis Replay
Actions: extract outside thesis, claimed proof, missing proof, primary-source
verification result, and confirmed/partial/unsupported/contradicted components.
Output: ArticleThesisMap, ThesisPathReplay.
Gate: ArticleMapGate.

PHASE 3 - Alpha Discovery
Actions: identify why the stock matters now, reconstruct market belief,
identify possible mispricing, select correct valuation denominator, identify
company control point, and define proof path plus broken-thesis signal.
Output: AlphaDiscovery, ThesisSpine, MispricingAssessment.
Gate: AlphaDiscoveryGate.

PHASE 4 - Mechanism Primer
Actions: explain old system, bottleneck, new architecture or policy shift, why
the customer pays, company position in the value chain, and economic translation.
Output: TechnicalMechanismPrimer, ValueChainControlMap.
Gate: MechanismGate.

PHASE 5 - Opportunity Routing
Actions: select primary archetype, optional secondary archetype, run
demand/scaling/scarcity/commercialization tests, and determine action-grade cap.
Output: OpportunityArchetype and four opportunity assessment objects.
Gate: OpportunityRouteGate and FourPartOpportunityGate.

PHASE 6 - Business And Company Control
Actions: define old value driver, new value driver, company-specific control
point, alpha versus beta status, and falsification observable.
Output: BusinessModelThesis, ValueDriverTransition, CompanyControlPointAssessment.

PHASE 7 - Operating Machine
Actions: map assets, facilities, capacity, ramp date, capex, funding, customer
commitment, revenue conversion, margin conversion, cash conversion, and failure date.
Output: OperatingMachine, CapacityRampBridge, FundingBridge.

PHASE 8 - Demand Proxy And Orders
Actions: collect demand signals, classify order evidence, identify customer and
legal strength, build conversion path, assign valuation use, and define trigger.
Output: DemandProxyMap, OrderQualityAssessment.

PHASE 9 - Financial Quality
Actions: build trend table; reconcile net income to OCF and EBITDA to FCF;
separate recurring/non-recurring cash; calculate owner FCF and per-share FCF;
check dilution, debt, maturities, capex, and working capital.
Output: ProfitCashFlowQualityAnalysis, DebtDilutionAssessment.

PHASE 10 - Earnings Revision Bridge
Actions: establish current earnings base, identify revenue and margin revision
variables, identify operating leverage, bridge to EBITDA/EPS/FCF, locate first
revision quarter, and define downside revision trigger.
Output: EarningsRevisionBridge.
Gate: RevisionBridgeGate.

PHASE 11 - Valuation
Actions: reverse-engineer current price, select one primary method, build
current-implied/base-proof/alpha/broken cases, build equity bridge, and block
targets when share count, net debt, senior claims, or order quality are unresolved.
Output: CurrentMarketImpliedBridge, ValuationMethodSelection, AlphaCaseSet,
EquityBridge, ValuationCase.

PHASE 12 - Risk / Short / Falsification
Actions: build plausible short attack narrative, separate fact/allegation/
inference, test customer/revenue/cash/governance/debt/promotion risk, build
early warning dashboard, and apply valuation or size effect.
Output: ShortSellerAssessment, RiskFilterAssessment, EarlyWarningDashboard,
FalsificationPattern.

PHASE 13 - Technical And Trade
Actions: load current OHLCV or chart screenshot, record chart date and adjusted
status, identify monthly/weekly/daily structure, support/resistance, catalyst
links, entry, stop, TP1, TP2, add/trim, and evidence/stop-based size.
Output: TechnicalSetup, CatalystLinkedTradePlan, PositionSizingRationale.

PHASE 14 - Decision Scorecard
Actions: start from thesis quality, then apply operating proof, order proof,
cash-flow, valuation, risk, and technical caps. The final grade is the lowest
decision-critical cap.
Output: DecisionScorecard.

PHASE 15 - Report Assembly
Actions: build investor memo skeleton, write the 12 canonical sections, end
each section with a decision-useful judgment, run Conviction Style Pass, and
run Anti-Checklist Reconstruction Pass.
Output: FinalReport.

PHASE 16 - Validation
Actions: validate output structure, manifest object graph, report-manifest
lineage, blockers, and no unsupported outside thesis promoted to final fact.
Output: ValidationResult.
```

## Alpha Discovery Objects

Before final prose, create or block:

- `AlphaDiscovery`
- `TechnicalMechanismPrimer`
- `MispricingAssessment`
- `MispricingThesis`
- `ThesisSpine`
- `CompanyControlPoint`
- `CompanyControlPointAssessment`
- `DemandProxyLadder`
- `DemandProxyMap`
- `OperatingMachineTable`
- `OperatingMachine`
- `RevisionBridge`
- `EarningsRevisionBridge`
- `AlphaCase`
- `AlphaCaseSet`
- `MaterialityEvidenceMatrix`
- `BrokenThesisCase`
- `EarlyWarningDashboard`
- `CatalystLinkedTradePlan`

## Investor Memo Skeleton

Use this hidden skeleton before projecting the 12 report sections:

```text
opening investment dispute
-> market belief and mispricing thesis
-> correct valuation denominator
-> mechanism primer
-> value-chain control table
-> company control point
-> demand proxy ladder
-> operating machine table
-> EPS/EBITDA/FCF revision bridge
-> current-price-implied bridge
-> alpha/base/broken case table
-> short attack narrative and early warnings
-> catalyst-linked trade table
```

If a report has facts but not this causal skeleton, rewrite before final output.

## Source Priority

Use primary filings, issuer materials, exchange or regulator records, earnings
transcripts, and reliable market data before secondary commentary. Outside
articles and user thesis notes may route the investigation, but they cannot
support material facts until verified.

## Module Boundary

Modules produce objects and gate results, not independent mini-reports. The
final projection must read as one causal investment memo. Do not expose hidden
object labels unless the user asks for an evidence ledger or a blocked section
requires a compact label.

## Blocker Rule

When a gate blocks a conclusion, continue only with non-blocked sections. Keep
target prices, trade levels, action grades, and high-conviction conclusions
blocked until the missing input is identified or resolved.
