# Incremental Refresh Framework

This reference defines how the Skill updates a prior research graph when only
some sources changed. It avoids rewriting the full report when a targeted
refresh is enough.

## Refresh Principle

New information should refresh only dependent objects unless a source change
invalidates the whole thesis.

Use `SourceSnapshot`, `SourcePartition`, `ResearchRun`, `EvidencePartition`,
and `IncrementalRefreshPlan` to determine what changed and what must be
recomputed.

## Source Change Routing

| Changed source | Objects to refresh |
|---|---|
| annual filing | source map, business model, debt, governance, risk factors, full valuation |
| interim filing | financials, cash conversion, debt, share count, valuation |
| earnings call | guidance, orders, management claims, business transition, valuation assumptions |
| investor presentation | assets, capacity, backlog narrative, customer claims, lower-priority evidence |
| regulator, court, or short report | short-risk signals, valuation discount, position size, risk factors |
| OHLCV or chart | technical setup and trade plan |
| market price only | current-market-implied bridge, upside/downside, trade plan |

## Incremental Refresh Plan

An `IncrementalRefreshPlan` must state:

- changed source snapshot
- affected source partitions
- affected partitions
- stale objects
- objects to recompute
- gates to rerun
- report sections to update

If affected objects cannot be isolated, fall back to a full research rerun and
record why.

## Dependency Refresh Workflow

Use this workflow when a new source arrives:

1. Identify the changed source and source class.
2. Identify affected claims and source partitions.
3. Identify affected objects:
   - `AlphaDiscovery`
   - `OpportunityArchetype`
   - `TechnicalMechanismPrimer`
   - `OperatingMachine`
   - `DemandProxyMap`
   - `EarningsRevisionBridge`
   - `ValuationCase`
   - `EarlyWarningDashboard`
   - `CatalystLinkedTradePlan`
4. Mark stale objects and stale claims.
5. Recompute dependent objects or explicitly block them.
6. Preserve unchanged sections with valid lineage.
7. If a high-materiality claim changes, rerun the full report.
8. If only price/chart changed, refresh current-implied valuation and trade plan.
9. If only a new order appears, refresh demand proxy, operating machine,
   revision bridge, valuation, catalyst, and trade plan.

## Stale Object Handling

When a source supersedes an older source:

- mark old evidence as superseded, not deleted
- mark derived claims as stale until refreshed
- rerun the gates connected to stale claims
- block conclusions if stale evidence still drives valuation or technical
  levels

## Incremental Gate

The `IncrementalRefreshGate` passes only when:

- changed source class is identified
- affected source partitions are identified
- affected partitions are identified
- stale objects are marked
- dependent objects are recomputed or explicitly blocked
- unchanged report sections retain valid lineage

## Report Implication

If only technical data changed, do not rewrite business-model prose. If only a
filing updated debt or share count, refresh valuation and trade plan before
changing the thesis. If a source invalidates a high-materiality claim, rerun the
full graph.
