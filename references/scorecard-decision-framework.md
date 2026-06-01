# Scorecard Decision Framework

This reference defines the decision layer used after the evidence graph,
business thesis, profit/cash-flow quality, valuation, short-risk screen, and
technical setup are complete.

`DecisionScorecard` is a report projection. It does not create new facts and it
does not override source priority. It compresses supported research objects
into an action grade, a binding cap reason, and a trade-plan constraint.

## Design Rule

Do not average numeric scores. Do not build a weighted model that turns weak
evidence into false precision. The final action grade is capped by the weakest
decision-critical blocker.

Use a qualitative grade:

- `A`: evidence quality, valuation odds, momentum, and risk filter all support a
  high-conviction stance.
- `B`: constructive but capped by one material issue.
- `C`: investable only with reduced size, milestone confirmation, or better
  entry.
- `D`: unfavorable balance of evidence, valuation, risk, or technical setup.
- `F`: avoid or no actionable long stance until a blocking issue is resolved.

The grade must always include `binding_cap_reason`.

## Required Objects

`ExpectationRevisionAssessment` captures whether revenue, EBITDA, EPS, FCF,
orders, or guidance are likely to be revised up, revised down, or remain
unconfirmed. It must separate verified guidance from analyst inference.

`MomentumRegimeAssessment` captures monthly, weekly, and daily trend alignment,
volume confirmation, overextension, support/resistance quality, chart
freshness, and whether the chart confirms or contradicts fundamentals.

`ValuationOddsAssessment` compares the current-market-implied expectation with
the report's base case, upside/downside asymmetry, target blockers, and the
fragile assumption behind the primary valuation method.

`RiskFilterAssessment` combines short-seller grade, balance-sheet constraint,
cash-flow quality, debt maturity, dilution, governance, regulatory, and evidence
quality issues. It determines whether the action grade must be capped.

`DecisionScorecard` contains:

- `company_quality`
- `operating_trend`
- `expectation_revision`
- `growth_logic`
- `momentum_state`
- `valuation_odds`
- `risk_filter`
- `action_grade`
- `binding_cap_reason`
- `trade_plan_effect`

## Build Order

Build the scorecard only after these objects exist or are explicitly blocked:

- `BusinessModelThesis`
- `ValueDriverTransition`
- `OrderQualityAssessment`
- `ProfitCashFlowQualityAnalysis`
- `CurrentMarketImpliedBridge`
- `ValuationMethodSelection`
- `EquityBridge`
- `ValuationCase`
- `ShortSellerAssessment`
- `TechnicalSetup`
- `DataGap`

If any required object is blocked, the scorecard can still be produced, but its
grade must state the blocker. A blocked valuation bridge, stale chart, weak
cash conversion, or unresolved debt maturity can cap the action grade even when
the narrative thesis is strong.

## Component Logic

Company quality should reflect the durability of the customer problem, value
capture mechanism, asset or software moat, customer concentration, operating
leverage, and evidence quality.

Operating trend should summarize revenue, margin, backlog/order conversion,
capacity utilization, working capital, cash conversion, and debt pressure.

Expectation revision should ask whether the next measurable update is more
likely to improve or weaken market expectations. Use filings, formal guidance,
earnings calls, and reliable market data before secondary commentary.

Growth logic should summarize why the company can grow profitably, not merely
why the end market may grow.

Momentum state should translate K-line structure into confirmation,
distribution, exhaustion, accumulation, or no clear setup.

Valuation odds should state whether current price already discounts the base
case, whether upside requires multiple expansion, and whether the downside is
protected by assets, cash flow, backlog, or balance-sheet strength.

Risk filter should name the issue that prevents a higher grade. Typical caps
include weak order evidence, unexplained OCF shortfall, share-count uncertainty,
debt maturity risk, elevated short-seller risk, stale technical levels, or
valuation already pricing the upside scenario.

## Thesis Grade Versus Trade Grade

Separate business attractiveness from trade action. A company can have a strong
business thesis and a lower action grade if the chart is extended, current price
already discounts the ramp, customer conversion is not yet visible, or dilution
is unresolved.

Use this decision chain:

```text
business quality -> operating proof -> cash-flow proof -> valuation odds ->
short-risk filter -> momentum state -> action grade
```

The `binding_cap_reason` must be the first issue that prevents a higher action
grade. Do not let a compelling industry narrative override a weak cap reason.

## Action Grade Workflow

Apply caps in this order:

1. Start from thesis quality and company-specific control point.
2. Apply evidence quality cap.
3. Apply order quality cap.
4. Apply operating proof cap.
5. Apply cash-flow quality cap.
6. Apply valuation cap.
7. Apply short-risk cap.
8. Apply technical setup cap.
9. Set final grade to the lowest decision-critical cap.
10. State binding cap reason and trade-plan effect.

Grade cap matrix:

| Blocker | Max grade |
|---|---|
| no company-specific control point | C |
| weak order evidence drives valuation | C |
| target blocked by share count, net debt, or senior claims | C |
| negative cash conversion unexplained | C |
| high short-risk D/F | D/F |
| stale chart drives trade plan | D |
| valuation already prices alpha case | C+ / B- |

The scorecard must make the cap visible. A strong narrative cannot override a
missing evidence bridge.

## Action Trigger Matrix Integration

After the action grade is set, translate it into an `ActionTriggerMatrix`.
The matrix must show what changes the grade and what changes position size.

Required fields:

- `trigger_variables`
- `buy_or_start_conditions`
- `wait_conditions`
- `add_conditions`
- `trim_conditions`
- `stop_or_downgrade_conditions`
- `price_stop`
- `thesis_stop`
- `catalyst_stop`

The scorecard should not end with a static letter grade. It should show the
next evidence event that would raise, lower, or keep the grade capped.

## Position-Size Translation

Translate grade into action:

- `A`: normal maximum size only if valuation upside and technical invalidation
  are both clear.
- `B`: constructive but use partial size or wait for a better entry.
- `C`: reduced size, milestone-dependent, or trade only around defined levels.
- `D`: observe, avoid new long exposure, or wait for evidence repair.
- `F`: no actionable long stance.

When TP1 is close to major resistance, the scorecard should allow partial
profit-taking even if the business thesis remains intact.

## Report Placement

Do not add a separate default scorecard section. Place the compact scorecard
summary in `Core Conclusion` when it helps frame the report, and place the final
action grade and position-size effect in `Technical Structure And Trade Plan`.

The trade plan must state:

- action grade
- binding cap reason
- stance
- position size effect
- entry, stop, TP1, and TP2 or observation stance
- catalyst and invalidation

The scorecard can support a separate `scorecard_summary` output view, but the
default `full_report` remains the canonical 12-section report defined in
`contracts/report_sections.yaml`.
