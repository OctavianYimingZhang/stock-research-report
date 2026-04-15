# Commodity Math Template — Bottom-Up Unit Economics

This template exists because the previous version of this skill failed Silas's test on mining/commodity names. The skill must do **bottom-up unit math** for commodity and capacity-driven businesses — not just cite consensus EBITDA numbers.

## When to Use This Template

Activate for any of these archetypes:
- Mining: uranium (UUUU), antimony (UAMY), gold, silver, copper, lithium, rare earths
- Energy: oil & gas E&P, LNG, coal, hydrogen (FCEL), nuclear fuel
- Commodity chemicals: sulfuric acid, caustic soda, chlor-alkali
- Semiconductor capacity plays: foundries, memory (TSEM, TSM, MU)
- Capacity-driven industrials: steel, cement, aluminum, solar panels
- Power generation / data centers: $/MW names (IREN, CLSK, RIOT)

## The Template

### Step 1: Unit Volume × Price × Cost

For each material product or byproduct, build a **P × V − C** table:

```
| Product | 2025A Volume | 2026E Volume | Realized Price | Unit Cost | Unit Margin | EBITDA |
|---------|-------------|-------------|---------------|-----------|-------------|--------|
| U3O8    | 1.0M lb     | 2.0M lb     | $75/lb        | $35/lb    | $40/lb      | $80M   |
| Vanadium| 150k lb     | 300k lb     | $8/lb         | $4/lb     | $4/lb       | $1.2M  |
| REE oxides | 0 | 500 t | $30,000/t | $18,000/t | $12,000/t | $6M |
| Byproduct: HMS | $15M | $20M | — | — | ~20% margin | $4M |
| **Total** | — | — | — | — | — | **$91.2M** |
```

**Sources for each input:**
- **Volume**: Production guidance from earnings calls, 10-K/10-Q operational sections, resource/reserve reports
- **Realized price**: Current spot × hedge book adjustment, or long-term contract price
- **Unit cost**: All-in sustaining cost (AISC) from filings, or cost per ton × recovery %
- **Unit margin**: Price − cost (do not assume, compute it)

### Step 2: Byproduct Credits

For mining/industrial, byproducts can be **10-30% of total EBITDA**. NEVER skip them.

Examples:
- UUUU: HMS revenue (rutile + ilmenite + zircon) from uranium ops
- UAMY: silver + copper byproduct from JV with Americas Gold and Silver (51% profit share)
- UAMY: sulfuric acid as byproduct of antimony smelting — Silas's specific complaint was that the skill missed this
- Copper mines: gold/silver/molybdenum credits
- Uranium mines: vanadium credits

**Required output row:**
```
| Byproduct | 2026E Volume | Price | Margin | Credit to Primary Product Cost |
|-----------|-------------|-------|--------|-------------------------------|
| Sulfuric acid | 100k t | $120/t | 60% | -$7.2M (lowers antimony AISC by $2/lb) |
| Silver from JV | 200k oz | $35/oz | 40% | +$2.8M (51% share) |
```

### Step 3: Operating Leverage Decomposition

For companies with significant fixed cost bases, show the **incremental margin walk**:

```
From 2024 to 2025:
- Revenue change: +$82M (from $106M SiPho to $228M SiPho)
- Gross profit change: +$62M (from $X to $Y)
- Incremental gross margin: 62/82 = 76%
- SG&A change: +$8M (largely fixed)
- EBITDA change: +$54M
- Incremental EBITDA margin: 54/82 = 66%

Interpretation: each incremental dollar of revenue drops $0.66 to EBITDA — this is what "operating leverage release" looks like.
```

Silas specifically asked: "有好的核心是三个领域，运营杠杆的释放..." — this decomposition IS operating leverage release quantified.

### Step 4: Forward EBITDA Derivation

Combine steps 1-3 to derive forward EBITDA with explicit assumptions:

```
2026E EBITDA bridge (UAMY illustrative):

Base 2025 EBITDA                                        $12M
  + Antimony volume ramp (Thompson Falls 100→300 t/mo)  +$38M
  + Antimony price hold at $20/lb (vs $15 avg 2025)     +$15M
  + Byproduct credits (sulfuric acid + silver JV)       +$10M
  + Bolivia smelter restart                             +$8M
  − Higher capex → depreciation                         -$3M
  − Inflation on cash costs                             -$5M
= 2026E EBITDA                                          $75M

Sanity checks:
- Implied EBITDA margin: 75 / 125 = 60%  → consistent with peer range
- Implied incremental EBITDA margin on +$100M revenue: 63 / 100 = 63%  → tight
- Compared to management guide of $125M revenue and "positive EBITDA by Q3": in the same zip code
```

### Step 5: Peer Multiple Target Price

Only after Steps 1-4 are done, derive the target price using peer multiples:

```
Peer set: MP Materials (rare earths), Perpetua Resources (antimony/gold)

| Peer | 2026E EV/EBITDA | Comment |
|------|----------------|---------|
| MP Materials | 14x | Defense supplier, domestic critical minerals |
| Perpetua | 18x | Scarcity premium, DoD funded |
| Median | 16x | — |

Target EV = 2026E EBITDA × peer median multiple
         = $75M × 16x
         = $1.2B

Target Market Cap = Target EV − Net Debt
                  = $1.2B − $0.1B (UAMY has net cash)
                  = $1.3B

Target Price per Share = $1.3B / 129M diluted shares = ~$10

Catalyst to re-rate: Q1 2026 Thompson Falls 投产 + Q2 DoD Phase 2 order
```

### Key Rules

1. **Never skip bottom-up math when data permits.** If you cannot find production guidance, ASK the user for Bloomberg data — don't just fall back to consensus.

2. **Always include byproduct credits.** Mining and chemical companies frequently have >15% of EBITDA from byproducts. Missing them is a major error.

3. **Show operating leverage quantitatively.** "Operating leverage release" without numbers is a buzzword. Show the incremental margin walk.

4. **Target price derivation must be transparent.** Every input (EBITDA, multiple, peer set, net debt, share count) must be visible. No averaging across 9 methods.

5. **Catalyst-to-rerating**: What specific event (earnings beat, contract award, capacity milestone) moves the stock from current multiple to target multiple?

## Silas's 4-Point Core Framework (Memorize This)

Per the Slack feedback, a good commodity analysis has:

1. **运营杠杆的释放** — Quantitative operating leverage decomposition (Step 3 above)
2. **主要商品价格 × 产量增量** — Bottom-up volume × price math (Step 1)
3. **副产品增量** — Byproduct credits with dollar value (Step 2)
4. **Forward EBITDA → 同行倍数 → 目标价** — Bottom-up EBITDA derivation + peer multiple (Steps 4-5)

If the final report is missing ANY of these four on a commodity/mining name, the skill has failed its core test.
