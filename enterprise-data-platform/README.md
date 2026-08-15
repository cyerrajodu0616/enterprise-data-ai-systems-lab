# Enterprise Data Platform Project

Use one fictional enterprise across the whole lab.

## Sources and flow

- Operational database: customers, accounts, products, orders/transactions, payments, and status history.
- Files: vendor transactions, partner reference feeds, and historical bulk extracts.
- Events: application, customer activity, and transaction events.
- External API: reference or enrichment data.

`Sources -> Ingestion -> Raw/Bronze -> Validated/Silver -> Business/Gold -> BI / API / AI`

## Evolution

Introduce duplicate ingestion, late records, malformed data, schema evolution, CDC inserts/updates/deletes, idempotency, ordering, replay, backfills, SCD changes, quality failures, skew, large joins, small files, poor partitioning, expensive transformations, concurrency, regressions, lineage, access control, and cost trade-offs as explicit requirements—not random demos.

Before adding CDC, answer: **Why are we using CDC instead of batch, and what business requirement justifies the added complexity?**

Use the subdirectories for requirements, source systems, data model, ingestion, Bronze, Silver, Gold, quality, and operations artifacts only when a real exercise needs them.
