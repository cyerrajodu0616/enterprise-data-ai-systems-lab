# Enterprise Warehouse/Lakehouse Project

Build one coherent fictional enterprise warehouse/lakehouse and progressively make it survive realistic enterprise problems.

## Sources and domains

- Operational database: customers, accounts, products, orders/transactions, payments, and status history.
- Files: vendor transactions, partner reference feeds, and historical bulk extracts.
- Events: application, customer activity, and transaction events.
- External API: reference or enrichment data.

`Operational Sources -> Ingestion -> Bronze/Raw -> Silver/Validated -> Gold/Business -> BI / API / AI`

## Modeling standard

Define business process and grain before tables. Use fact tables, dimensions, business and surrogate keys where justified, SCD Types 1/2, transaction/history data, and reference data. Explain normalization versus dimensional choices and layer responsibilities.

## Scale and evolution

Synthetic generators may create progressively larger datasets for distributed experiments, but large physical datasets are never required merely for appearance. Record measured results separately from projections. The challenge catalog introduces multiple sources, hundreds of millions of conceptual fact rows, reload limits, history, late and duplicate data, schema change, quality failures, skew, small files, backfills, governance, failures, transformation sprawl, environments, and AI access.

Before adding CDC ask: **Why CDC instead of batch, and which business requirement justifies the complexity?**
