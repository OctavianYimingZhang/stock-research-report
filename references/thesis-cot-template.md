# Thesis Chain-of-Thought Template

Lifted from AI4Finance-Foundation/FinRobot (Apache-2.0, MIT), adapted for Claude skill orchestration.

FinRobot uses a three-layer reasoning scaffold — Data-CoT → Concept-CoT → Thesis-CoT — to force a deep-research agent to walk from raw disclosure to investable thesis. This file codifies that pattern for internal use by the `stock-research-report` orchestrator during Phase 3 composition.

**This is not an output format.** It is a *thinking* framework the orchestrator uses internally before writing. The final report is a single cohesive narrative.

---

## Layer 1: Data-CoT (Ground Truth)

Before writing any thesis, pin down what is *known* vs *inferred* vs *estimated*. This layer answers: "What do we actually have?"

### Checklist per ticker

- [ ] **Revenue** — last 3 FY + LTM, segment breakdown if disclosed
- [ ] **Profitability** — gross margin, EBITDA margin, net margin trajectory
- [ ] **Balance sheet** — cash, debt, debt maturity schedule, working capital
- [ ] **Cash flow** — OCF, capex, FCF trajectory; any unusual items
- [ ] **Share count + ownership** — fully diluted shares, insider %, top 5 13F
- [ ] **Management guidance** — most recent, dated, quoted
- [ ] **Industry context** — TAM, growth rate, top 3 competitors with market share
- [ ] **Key customers** — named, or end-market proxy if undisclosed
- [ ] **Key contracts / backlog** — total $, delivery schedule
- [ ] **Catalyst schedule** — earnings dates, pipeline milestones, industry events
- [ ] **Analyst consensus** — revenue, EPS, target price, rating distribution
- [ ] **Technical state** — trend, key levels, pattern, volume confirmation

### Data quality stamps (attached to each item)

- ✅ **Disclosed** — from 10-K / 10-Q / 8-K / earnings call, with source
- ⚠️ **Inferred** — derived from disclosed inputs (e.g., segment % × total)
- 🔮 **Estimated** — modeled based on industry comps (flagged as estimate)
- ❓ **Unknown** — legitimately missing, not fabricated

**Rule**: Data-CoT items without a quality stamp are forbidden from use in Concept-CoT or Thesis-CoT.

---

## Layer 2: Concept-CoT (Business Mechanics)

This layer answers: "What is the engine, and what drives it?"

### Required concept sections

1. **Revenue engine decomposition**
   - Unit of sale (lb, MW, kWh, license, handset, wafer, etc.)
   - Price per unit (trend direction with 3-yr history)
   - Volume per unit (trend, capacity ceiling, utilization)
   - Mix (premium vs commodity, recurring vs one-time)

2. **Margin engine**
   - Gross margin structural driver (is it scale? mix? pricing? cost input?)
   - Operating leverage ratio (incremental revenue : incremental operating income)
   - Fixed-cost base ($M that sets the breakeven)

3. **Growth engine**
   - Capacity-driven (need new facility), product-driven (need new SKU), adoption-driven (market penetrates from X% to Y%), or share-gain (take from named peer)
   - The constraint: what limits growth? capacity, demand, supply chain, regulation, talent?

4. **Durability engine**
   - Moat type: scale, network effect, switching cost, cost advantage, brand, regulatory, customer captivity, patent
   - Moat evidence: specific quantifiable signal (gross margin stability, customer retention, market-share stability, pricing power)

5. **Capital allocation engine**
   - Where does FCF go? capex, buyback, dividend, M&A, debt paydown?
   - Track record: ROIC on last 3 major capital decisions

### Concept-CoT output format (internal)

A 5-point bulleted digest (NOT prose) that the writer references during Thesis-CoT composition. Example:

```
Revenue engine: lb × $price/lb × grade mix; 2026 guidance 240 Klb @ ~$80/lb = ~$19M
Margin engine: ~45% gross structural (recent mine restart lowered cash cost to $65/lb);
   incremental operating leverage 60% (fixed mill cost base ~$4M/yr)
Growth engine: commodity-price re-rating (stage 1) + volume ramp from 240 → 800 Klb by 2028
Durability engine: NRC-licensed conventional mill + DOE HALEU contract (regulatory moat,
   5-year replication cost)
Capital allocation: all FCF reinvested until 2027 capacity build done;
   no dividend, no buyback expected
```

---

## Layer 3: Thesis-CoT (Investable Claim)

This layer answers: "What is the trade, and why is the market wrong?"

### The thesis must contain

1. **One-sentence investment claim**: *"Long [TICKER] at $X to $Y target, driven by [specific mechanism] over [specific timeframe]."*

2. **Non-consensus disagreement**: Where does your view differ from the sell-side consensus? Specify:
   - **What the market sees**: [X sentiment]
   - **What the market misses**: [specific gap]
   - **When it gets priced in**: [date-anchored catalyst]

3. **Risk: reward math**:
   - Downside: $[Z] (-X%), driven by [specific trigger]
   - Base: $[target] (+Y%), driven by [specific mechanism]
   - Upside: $[bull] (+Z%), driven by [optional layer]
   - Skew: "3:1 R/R on base case" or similar

4. **Position posture**:
   - Size: X% of portfolio (single range 5 pp wide max)
   - Entry: specific zone with trigger
   - Stop: specific level with thesis-invalidation logic
   - Exit: specific level at target with partial scaling rule

5. **90-day catalyst spotlight**: Single named event with date and expected market reaction.

### Thesis-CoT checklist (before writing)

- [ ] Is the claim a **declarative sentence**, not a conditional?
- [ ] Does the market-wrong section identify something **specific** (mechanism, timing, multiple choice) rather than "market is cautious"?
- [ ] Does the R/R math use **single numbers**, not triangulated ranges?
- [ ] Is the catalyst **dated** (YYYY-MM or YYYY-Q#)?
- [ ] Would a sophisticated portfolio manager know how to trade this immediately?

If any fail, the thesis is underdeveloped. Return to Concept-CoT and deepen.

---

## How the Orchestrator Uses This

During Phase 3 (Narrative Composition), the orchestrator runs Data-CoT → Concept-CoT → Thesis-CoT *internally* (not as visible output) to produce the Phase 3 content inventory, then weaves the result into themed sections.

The three layers DO NOT appear in the final report. They guide the writer toward coherent, conviction-laden prose.

### Integration with themed structure

| Layer | Primary section it populates |
|-------|------------------------------|
| Data-CoT | 财务数据, 客户与订单 (raw facts), 公司简介 (identity facts) |
| Concept-CoT | 业务逻辑 (engine story), 运营逻辑 (mechanics) |
| Thesis-CoT | 估值情况 (claim + wrong-market), 交易计划 (posture), 风险提示 (invalidation triggers) |

### Anti-pattern

Do **not** output the three layers as report sections. That would violate the themed-structure rule. If a reader can see Data/Concept/Thesis labels in the report, the orchestrator failed.

---

## Reference

- AI4Finance-Foundation/FinRobot (2024, arXiv 2411.08804) — the multi-layer CoT paper
- TauricResearch/TradingAgents v0.2 — Researcher role uses a parallel structure
- Buffett-Munger mental-model literature (worldly-wisdom stacking)
