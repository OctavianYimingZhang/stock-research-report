# Opportunity Discovery Framework

This reference defines how the Skill decides what kind of investment question it
is answering before drafting a report. The report should not force every issuer
through the same emphasis. It should route the company by opportunity archetype,
then set the evidence burden, section weight, valuation method, and action-grade
cap from that route.

## Opportunity Archetype

Create an `OpportunityArchetype` object before valuation:

- `scarcity_bottleneck`
- `policy_protected_supply_chain`
- `customer_funded_capacity_ramp`
- `operating_leverage_recovery`
- `order_backlog_repricing`
- `strategic_asset_optional_value`
- `levered_residual_equity`
- `early_commercialization`
- `mature_infrastructure_compounder`
- `commodity_or_resource_processing`

If no archetype is supported, classify the issuer as `industry_beta` or
`watchlist_only` and cap the action grade until a company-specific mechanism is
verified.

## Routing Rules

Use `scarcity_bottleneck` when the thesis depends on unique capacity,
qualification, process know-how, supply-chain chokepoint, regulated access, or
customer approval.

Use `policy_protected_supply_chain` when the thesis depends on law, subsidy,
national security, tariffs, domestic-content rules, procurement preferences, or
regulated sourcing.

Use `customer_funded_capacity_ramp` when a plant, mine, factory, fleet, fab,
production line, or data center must scale and the funding source is central.

Use `operating_leverage_recovery` when fixed-cost absorption, utilization,
cycle recovery, or mix shift drives earnings more than new demand.

Use `order_backlog_repricing` when the market is repricing recognized revenue,
binding purchase orders, contracted backlog, or customer-funded commitments.

Use `strategic_asset_optional_value` when hard assets, permits, licenses,
location, reserves, data, or infrastructure create downside floor or strategic
optionality.

Use `levered_residual_equity` when debt, preferred stock, warrants,
convertibles, or maturity walls can absorb most upside or block a per-share
target.

Use `early_commercialization` when the company is moving from prototype, pilot,
or framework agreement to revenue, orders, and cash conversion.

Use `mature_infrastructure_compounder` when durable cash flow, reinvestment
rate, pricing power, and capital allocation matter more than a single catalyst.

Use `commodity_or_resource_processing` when spread, cost curve, reserve quality,
processing margin, logistics, or policy-linked supply drives value.

## Four-Part Opportunity Test

Every high-conviction thesis must create these objects:

- `DemandExpansionAssessment`
- `ScalingDifficultyAssessment`
- `ScarcityBottleneckAssessment`
- `CommercializationPathAssessment`

The test asks:

1. Demand expansion:
   - What end demand is growing?
   - Who is spending?
   - Why now?
   - Is this structural demand or cyclical rebound?

2. Scaling difficulty:
   - Why can supply not expand quickly?
   - Which barrier matters: certification, qualification, capex, build time,
     yield, customer approval, regulation, financing, or channel access?

3. Bottleneck or scarcity:
   - Which exact value-chain node is scarce?
   - Why does this company control, relieve, or monetize that scarcity?
   - Is scarcity technical, capacity-based, policy-based, customer-based,
     asset-based, financing-based, or channel-based?
   - Is it temporary, cyclical, or structural?

4. Commercialization visibility:
   - What evidence converts the thesis into revenue and cash?
   - Separate recognized revenue, binding purchase order, contracted backlog,
     paid reservation, customer prepayment, framework, pilot, MOU, LOI,
     pipeline, and management aspiration.

If any part fails, the report may still be useful, but the conclusion must be
observation, watchlist, scenario, or capped conviction unless valuation already
prices the equity as a discounted option.

## Section Emphasis

The archetype changes the report emphasis:

- scarcity and policy routes require industry-chain and bottleneck depth
- capacity-ramp routes require asset, funding, utilization, and execution depth
- order routes require order-quality and order-to-revenue depth
- levered routes require debt, maturity, dilution, and residual-equity depth
- mature compounders require reinvestment, cash conversion, and capital
  allocation depth

The final report still uses one integrated voice. The archetype should shape
emphasis, not create a visible module dump.
