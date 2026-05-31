# Bull-Bear-Risk-Manager Debate Loop

Adversarial resolution pattern lifted from TauricResearch/TradingAgents v0.2 (Apache-2.0), adapted for Claude skill orchestration.

The single-biggest reliability gap in LLM equity research is **confirmation bias** — the writer finds the facts that support whatever thesis they drifted into first. Adversarial debate forces the writer to actually steelman the opposing view before reaching a verdict.

---

## When to Trigger the Debate Loop

The orchestrator should run this loop AFTER Phase 2 (Content Inventory) and BEFORE Phase 3 (Narrative Composition) whenever ANY of the following triggers fire:

- [ ] Valuation target > **2× current price** (conviction check needed)
- [ ] Valuation target < **0.7× current price** (conviction check on a short)
- [ ] Sub-reports disagree (e.g., risk-analysis grade D while fundamentals Block E says "strong catalyst stack")
- [ ] Company is pre-revenue or pre-profit (frontier archetype)
- [ ] User explicitly requests "council mode" / "bull-bear debate" / "second opinion"
- [ ] Short-seller skill triggered Full Audit Mode

For clean mid-cap names with stable earnings and <20% upside, skip the debate loop and write directly.

---

## The Three Roles

### Bull Case Agent
**Prompt**: "You are a growth-oriented long-only analyst. Given the content inventory for [TICKER], build the most compelling **long thesis** possible. Lean into multi-year secular drivers, operating leverage, re-rating potential. Steelman — don't strawman."

**Required output**:
- 3-bullet thesis with specific mechanisms
- 12-18 month target price with derivation
- Single most important catalyst with date
- What would make this thesis work

### Bear Case Agent
**Prompt**: "You are a value-discipline short-biased analyst. Given the same content inventory, build the most compelling **short or avoid thesis**. Focus on cyclicality, margin compression, competitive erosion, management red flags, valuation risk. Steelman — don't strawman."

**Required output**:
- 3-bullet thesis with specific mechanisms
- Downside price target with derivation
- Single most important risk event with date
- What would make this thesis right

### Risk Manager (Resolver)
**Prompt**: "You are a portfolio risk manager. Read both the bull and bear cases. Your job is to produce a SINGLE decision: **buy, hold, trade-only, or avoid**. Consider:
- Which side has more *specific, dated* evidence?
- Where does the evidence **weight of evidence** actually point?
- What is the risk:reward on a base-case sized position?
- Is there a *specific catalyst* that would resolve the debate one way or the other in <90 days? If yes, is the optionality asymmetric?

Output format:
- **Verdict** (one posture: 买入 / 持有 / 观望 / 回避)
- **Weight of evidence** (3-5 sentences citing specific bullet from each side)
- **Crux**: single catalyst that resolves the debate, with date
- **Recommended position size** (X-Y%) + **entry zone** + **stop**"

---

## Dispatch Pattern

```
Phase 2 (Content Inventory) completes → 
  IF debate trigger fires →
    Dispatch 2 agents in parallel:
      Agent B1: Bull Case (general-purpose, given full inventory)
      Agent B2: Bear Case (general-purpose, given full inventory)
    WAIT for both to return.
    THEN dispatch:
      Agent RM: Risk Manager (given both outputs)
    RM output becomes a hidden context block for Phase 3.
  Phase 3 (Narrative Composition) uses RM verdict as the report's position + direction.
```

**Cost note**: This adds 3 agent round-trips (~30-60s wall time, modest token cost). Only worth it when the trigger conditions fire.

---

## How the RM Output Feeds the Report

The Risk Manager output is **not a separate report section**. It informs:

- **评级** in 交易计划 (single posture, reflects RM verdict)
- **建议仓位** in 交易计划 (RM's sizing recommendation)
- **90 天内最重要催化剂** in 交易计划 (RM's "crux" event)
- The **我与市场的分歧** paragraph (RM's "weight of evidence" reasoning, distilled to 1-2 sentences)

If the RM verdict conflicts with the direction the Phase 1 sub-reports were leaning, **trust the RM**. The whole point of the debate loop is to catch confirmation bias.

---

## Anti-Pattern: Visible Debate

The bull/bear/RM outputs must NOT appear in the final report as three separate sections with visible labels. If the reader sees "Bull Case / Bear Case / Resolution", the orchestrator failed.

The debate is an internal scaffold. The output is one analyst's voice.

---

## Reference Implementations

- TauricResearch/TradingAgents v0.2 — `tradingagents/agents/risk_manager_prompt.py`
- virattt/ai-hedge-fund — multi-persona council (bull/bear/macro/micro)
- investor-council.md (this skill's existing council pattern) — 7 personas for larger debates

---

## Example Trigger Resolution

```
Ticker: BZAI
Sub-report state:
  - Fundamentals: "88% China revenue, Kuwait ransomware contract pending"
  - Risk Analysis: Full Audit Mode triggered (3 flags: auditor change, going concern, restatement)
  - Valuation: Frontier archetype, wide scenarios $0.40-$4.50
  
Debate trigger: YES (pre-profit + full audit + wide scenarios)

Bull Case: "Frontier AI at edge; 88% China can pivot to US if $250M shelf funds domestic MIL contracts; 
  Kuwait deal proves governmental traction; $3.50 if Kuwait announces Q3"
Bear Case: "Going concern warning; cash runway 4 quarters; China MIIT sanctions tail risk; 
  shelf dilutes 40%; $0.40 on any credible peer announcement"
  
Risk Manager Verdict: 观望 (Trade-Only)
  Weight of evidence: Binary near-term; Kuwait announcement is the crux (expected 2026-Q2);
    going-concern overrides bull case until equity raise lands with sub-$3 strike.
  Crux: Kuwait contract announcement (2026-Q2, likely by end of June)
  Size: 1-2% tactical only; no core position
  Entry: $1.80-2.10 if pullback after rally; no entry on strength
  Stop: $1.45 (below Q1 2026 low)
```

The RM verdict of "观望" feeds directly into 交易计划, even though the bull case looked exciting.
