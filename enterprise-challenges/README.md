# Enterprise Challenge Catalog

This is the primary learning sequence. Every challenge extends the same warehouse/lakehouse, starts from a business requirement, uses the simplest credible design, and introduces technology only when justified.

## Sequence

1. **Initial Warehouse Design** — requirements, grain, facts, dimensions, normalization versus dimensional models, and Bronze/Silver/Gold responsibilities.
2. **Multiple Source Systems** — contracts, schema differences, metadata-driven ingestion, reconciliation, and ownership.
3. **Hundreds of Millions of Rows** — distributed scans, partitions, shuffle, joins, memory, network, and layout using economical measured experiments plus labeled scale reasoning.
4. **Full Reload Becomes Too Expensive** — watermarks, CDC, idempotency, MERGE, and inserts/updates/deletes.
5. **Customer/Account History** — SCD Types 1/2, temporal correctness, and late dimension changes.
6. **Late-Arriving Transactions** — event versus processing time, correction, reconciliation, and replay.
7. **Duplicate Deliveries** — keys, deduplication, idempotency, and honest exactly-once guarantees.
8. **Schema Evolution** — additive/breaking change, contracts, compatibility, and blast radius.
9. **Bad Data** — validation, quarantine, observability, reconciliation, and ownership.
10. **Join Skew** — plans, imbalance, AQE, broadcast, and justified salting.
11. **Small Files** — metadata overhead, compaction, write patterns, read amplification, and layout.
12. **Large Backfill** — isolated replay, capacity, idempotency, recovery, and cost without destabilizing normal work.
13. **Multi-Team Governance** — catalogs, schemas, ownership, privileges, service identities, least privilege, lineage, and domains.
14. **Sensitive Data** — access boundaries, masking/filtering concepts where supported, auditability, and responsibility.
15. **Pipeline Failure** — orchestration, retries, dependencies, recovery, backfills, idempotency, alerts, and evidence.
16. **Transformation Sprawl** — dbt organization, SQL tests, dependencies, docs, lineage, and Spark/dbt boundaries.
17. **Dev/Test/Prod** — isolation, CI/CD design, catalog/schema strategy, configuration, test data, and permissions.
18. **Enterprise Data for AI** — governed authoritative data, metadata, authorization, lineage, evaluation, and data-quality effects on AI correctness.

Do not implement every challenge at initialization. Create a challenge directory only when work begins, using the experiment and debugging standards.
