# Stock Research Report — Compact Orchestration Skill

Compact orchestration skill for analyst-style public-company deep research
reports. It can still use specialized analysis skills, but the report contract
now starts from the current repricing dispute, replays outside thesis paths,
routes the opportunity archetype, tests demand/scaling/scarcity/commercialization,
and ends with a concrete trade plan.

## What It Does

Instead of outputting four separate reports, this skill produces **one unified
causal memo** that matches the style of professional equity research analysts.
Outside articles and user notes are research-path inputs only; material claims
must be checked against primary or high-quality sources.

## Core Additions

- Outside thesis replay before drafting.
- Opportunity archetype routing before valuation.
- Four-part opportunity test: demand expansion, scaling difficulty,
  bottleneck/scarcity, commercialization visibility.
- One primary valuation method and current-market-implied bridge.
- Position sizing tied to evidence quality, short risk, and stop distance.
- Optional companion skills may accelerate research, but the compact Skill is
  self-contained and the final report must still follow the canonical
  12-section contract.
- Alpha-thesis overlay: mispricing thesis, correct valuation denominator,
  company control point, demand proxy ladder, operating machine, revision
  bridge, proof catalyst, broken-thesis signal, and trade action.

## Usage

```
Use $stock-research-report to analyze [TICKER]
```

Optional parameters:
- Focus areas: "focus on valuation" or "focus on business transformation"
- Bloomberg data: Attach screenshots for higher-precision analysis

## Output Format

Single report or .docx file with default sections:

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

## Key Design Principles

- **Narrative-first**: Reads like one analyst wrote it, not four AI skills
- **Opinionated**: Clear investment conclusions, not hedged probabilities
- **Concise**: 8-12 pages, not 20+
- **Embedded analysis**: Short-seller risk = one line; technicals = 1-2 paragraphs
- **Actionable conclusion**: Position size, target price, stop-loss, catalyst

## License

MIT
