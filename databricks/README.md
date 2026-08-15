# Databricks Track

Databricks is the primary first-phase platform. Study mechanisms before commands.

- `spark-internals/`: driver/executor model, partitions, tasks, stages, lazy evaluation, shuffle, plans, Catalyst, AQE, memory, spill, skew, and joins.
- `delta-lake/`: transactions, enforcement/evolution, MERGE, updates/deletes, snapshots/versioning, time travel, change patterns, layout, concurrency, and reproducibility.
- `performance/`: controlled tests of scan, layout, shuffle, join, skew, caching, UDF, and repartition choices.
- `cdc-incremental/`: watermarks, CDC, inserts/updates/deletes, late events, idempotency, replay, ordering, and schema changes.
- `unity-catalog/`: centralized governance, hierarchy, principals, privileges, ownership, lineage, discovery, governed data and files, jobs, environments, sharing, and AI implications.
- `governance/`: policy design, operational ownership, auditability, classification, privilege sprawl, incorrect grants, and lineage limitations.
