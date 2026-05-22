# Business Model Framework

This reference defines how the report analyzes company business logic. It is
not a generic company description template. The goal is to explain why the
company exists, how it captures value, and what changes the value driver.

## Evidence Standard

Use these source classes in order:

1. issuer filings and audited reports
2. issuer investor presentations and earnings-call transcripts
3. regulator, exchange, government, or court records
4. customer, supplier, partner, or counterparty disclosures
5. reliable market data and industry datasets
6. high-quality secondary research

User-provided prior reports are style references only.

## Core Questions

Every business-model section must answer:

- What economic problem does the company solve?
- Who pays, and what cost or risk do they avoid by paying?
- What was the old value driver?
- What is the new value driver?
- What structural change explains the transition?
- How does the company capture value instead of merely riding industry growth?
- What evidence would prove the transition is not working?

## Business Logic Pattern

Write the business-model logic as a causal chain:

```text
Customer problem -> product or service -> value captured by company ->
revenue denominator -> margin mechanism -> cash-flow pattern -> valuation method
```

Do not stop at labels such as "AI beneficiary", "defense supplier",
"turnaround", "platform", or "scarce resource". Labels are allowed only after
the mechanism is explicit.

## Old Driver To New Driver

Strong reports usually identify a concrete transition rather than a generic
theme. Abstract transition types include:

- legacy end-market cycle -> higher-complexity end-market
- low-value manufacturing -> technology/process premium
- third-party supply dependency -> controlled domestic or strategic supply
- retail/channel business -> enterprise or government procurement
- single-product exposure -> multi-product cash-flow base
- concept-stage capacity -> contracted production
- commodity beta -> integrated resource and processing margin

For a new company, identify whether a real transition exists. If there is no
transition, explicitly state the steady-state business logic and the margin
variable that matters now.

## Value Capture Tests

Industry growth is not enough. The report must show why the company captures
some of that growth.

Use at least two of these tests:

- customer switching cost
- certification or qualification status
- manufacturing bottleneck
- technology/process capability
- geographic or policy advantage
- cost curve position
- distribution or channel control
- backlog/order visibility
- recurring consumable or service attachment
- scarce license, permit, or regulated asset

If none can be verified, say the thesis is industry-beta rather than company
alpha.

## TAM And Market Share

For each key market:

- name the market or segment
- give TAM or a defensible proxy if exact TAM is not available
- estimate company share if supported
- name the closest competitors
- explain the specific reason the company wins or loses design-ins/orders

If TAM or market-share figures are not available from reliable sources, do not
invent them. Use relative size language and mark the data gap.

## Operating Logic

Show how the business logic turns into P&L:

- unit of sale: wafer, tester, system, drone component, ton, pound, MW, module,
  subscription, transaction, patient visit, loan, or other unit
- capacity: facility, current status, ramp date, utilization
- pricing: ASP, realized commodity price, contract price, reimbursement rate,
  take rate, subscription price
- cost: unit cost, fixed-cost base, capex, depreciation, SG&A
- operating leverage: how much incremental gross profit/EBITDA comes from each
  unit of additional revenue
- bottleneck: the one physical, regulatory, commercial, or financial constraint
  that can block the thesis

## Customers And Orders

Use named customers when disclosed. If not disclosed, use segment, geography,
or end-market proxies and state the limitation.

Order quality hierarchy:

```text
recognized revenue > binding purchase order > firm backlog >
commercial contract > capacity reservation with payment > IDIQ/framework >
pilot/MOU/LOI > management aspiration
```

Only recognized revenue, binding POs, firm backlog, or paid reservations can
normally support a valuation denominator. IDIQ/framework agreements can support
scenario discussion but need conversion evidence.

## Required Business Tables

Use compact tables only where they reduce ambiguity.

Customer/order table:

```markdown
| Customer or counterparty | Evidence type | Amount/share | Timing | Valuation usability |
|---|---:|---:|---:|---|
| [name] | binding PO/backlog/revenue/etc. | [value] | [period] | high/medium/low |
```

Capacity table:

```markdown
| Facility/asset | Current status | Current capacity | Target capacity | Date | Contracted? |
|---|---|---:|---:|---|---|
```

## Section Exit Standard

The section is complete only if a reader can answer:

- what the company sells
- why customers need it
- why this company captures value
- what variable most changes revenue and margin
- what observable would break the thesis

End with:

`**Business judgment**: [Company] value change depends on [driver], the current stage is [stage], and the key verification variable is [observable].`
