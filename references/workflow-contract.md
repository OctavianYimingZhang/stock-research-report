# Workflow Contract

This file is the canonical run order for the Skill. Other references define
domain rules; this file defines how those rules are sequenced.

## Canonical Flow

```text
intake/settings
-> source preflight
-> source partitions
-> evidence extraction
-> outside thesis replay
-> opportunity routing
-> four-part opportunity test
-> business, operations, customers, and orders
-> profit/cash-flow quality
-> valuation and equity bridge
-> short-risk and falsification
-> technical setup and trade plan
-> decision scorecard
-> report projection
-> validation
```

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
