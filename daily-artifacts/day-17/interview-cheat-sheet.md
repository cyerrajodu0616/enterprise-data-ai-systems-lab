# Day 17 — Five-Minute Delta MERGE and Idempotency Interview Cheat Sheet

**Status:** conceptual reasoning completed early/out of sequence; hands-on LAB-015 TODO.

## Correctness spine

`authoritative source order → deterministic source cardinality → target sequence guard → policy-valid transition → idempotent current state`

- `source_sequence` orders source changes; timestamps do not substitute for it.
- Deduplicate each batch to one source row per key; quarantine equal sequence/different payload.
- Apply only when `source.source_sequence > target.last_source_sequence`.
- Keep minimal tombstones to prevent stale-state resurrection.
- Separate `last_seen_sequence`, `last_applied_sequence`, and `last_rejected_sequence`.

| Incoming event | Tombstone at 504 | Result |
|---|---:|---|
| UPDATE 503 | yes | stale; reject |
| INSERT 501 after unmatched DELETE | yes | stale; reject |
| DELETE 504 retry | yes | duplicate; no-op |
| ACTIVE 505 | yes | newer; apply or quarantine by policy |

Complete authoritative after-images may be independent. Partial updates/commands may depend on prior state; isolate that key and reconcile/replay it.

## Performance evidence

| Phase | Supplied scenario |
|---|---:|
| Dedup | 8 min |
| Scan/match | 55 min |
| Rewrite | 24 min |
| Commit | 3 min |

40,000 total files, 38,000 scanned, 2,400 rewritten, 250,000 changed customers. Scan breadth measures lookup/layout cost. Rewrite footprint measures touched immutable files. Write amplification compares physical rewrite to logical change: assumed 307 GB / 250 MB ≈ 1,228×.

Liquid clustering on `customer_id` is a candidate to test, never a promised result. No-op filtering trades fewer writes for loss of observed sequence unless ordering/checkpoint or separate sequence-state guarantees exist.

## Concurrency and coordination

Without applicable row-level concurrency, conventional copy-on-write changes to disjoint rows in one file may contend. A conflict fails atomically; retry the complete deterministic transaction against the latest snapshot. Databricks row-level concurrency can reduce same-file/different-row conflicts when documented requirements are met, including Runtime 14.3 LTS+, an unpartitioned table, and deletion vectors enabled. Deletion vectors are not universal; enabling them upgrades the table protocol and requires compatible clients.

First validate available concurrency and residual conflicts. If coordination remains necessary, safe backfill window = CDC interval − p95 CDC duration − buffer = 15 − 6 − 2 ≈ 7 minutes. Pilot deterministic checkpointed chunks, prioritize CDC, and validate both SLAs.

## Managed-platform choices

- **Databricks:** AUTO CDC uses `KEYS`, `SEQUENCE BY`, and `APPLY AS DELETE WHEN` for managed SCD Type 1 or Type 2 processing; sequencing handles out-of-order arrival. Its temporary SCD2 tombstones and configurable retention are not the same as the lesson's business tombstone policy. Prefer it when it expresses the contract; justify manual MERGE for exceptional policy or unsupported requirements.
- **Delta physical behavior:** Without deletion vectors a row change can rewrite its containing file. Deletion vectors may defer that rewrite. Evaluate protocol/client compatibility, liquid clustering, and row-level concurrency before custom coordination.
- **Snowflake:** Streams expose `METADATA$ACTION`, `METADATA$ISUPDATE`, and `METADATA$ROW_ID`; UPDATE appears as a DELETE/INSERT pair. Use Streams + Tasks + MERGE for procedural DML/control and Dynamic Tables for supported declarative SELECT pipelines. Stream offsets do not establish an external source's business order; retain an external sequence for out-of-order CDC.

> Start with the correctness contract: authoritative key, authoritative ordering, delete semantics, replay horizon, and reactivation policy. On Databricks, prefer AUTO CDC when it expresses those requirements; then evaluate deletion vectors, liquid clustering, and row-level concurrency before creating custom workload coordination. On Snowflake, choose between Streams + Tasks + MERGE and a declarative Dynamic Table based on required DML and control. Custom logic must earn its operational cost.

## Industry patterns

- Netflix DBLog: watermark-coordinated snapshots with transaction-log CDC and resumable chunks.
- LinkedIn Brooklin: bootstrap and transaction-boundary support plus isolation of downstream consumers from operational stores.
- Uber DBEvents: bootstrap plus incremental ingestion and schema-governed standardized events.
- Airbnb SpinalTap: reliable low-latency CDC distributing standardized events.

These sources do not document use of this lesson's exact tombstone schema. Full citations are in the [Day 17 lesson](lesson.md#primary-references), all accessed 2026-09-06.

## Vocabulary Upgrade

- “Late-arriving event” or “out-of-order event,” not “lag data.”
- “Authoritative ordering signal,” not “authoritative date freshness.”
- “Target sequence guard.”
- “Deterministic source cardinality.”
- “Deletion tombstone.”
- “Prevent stale-state resurrection.”
- “Last seen, last applied, and last rejected sequence.”
- “Broad update footprint.”
- “Write amplification.”
- “Physical file contention versus business-key conflict.”
- “Retry the complete deterministic transaction against the latest snapshot.”
- “Pilot workload coordination and validate both SLAs.”
- “The largest deterministic chunk that fits inside the safe concurrency window.”
- “Stop optimizing when the measured business requirement is satisfied.”

## 60–90 second answer

**Business outcome:** Maintain exactly one authoritative current customer state reflecting the latest committed PostgreSQL change.

**Correctness controls:** I use the producer's source sequence, deterministic batch cardinality, a target sequence guard, and tombstones. Sequence decides freshness; policy decides transition validity.

**Performance evidence:** I separate dedup, target scan, rewrite, and commit and compare files/bytes scanned with physical bytes rewritten versus logical changes.

**Decision:** I would prefer managed AUTO CDC when it expresses the contract, then evaluate deletion vectors, locality, and row-level concurrency before adding custom workload coordination. On Snowflake, I would choose procedural Streams + Tasks + MERGE or a declarative Dynamic Table from the required DML and control.

**Trade-off:** Skipping no-op attribute updates saves rewrites but may lose observed sequence state; clustering and chunking also impose maintenance/commit costs.

**What would change the decision:** Managed-semantic gaps, feature/client incompatibility, SLA pressure, greater retry cost, continuous backfills, new writers, small-file growth, or representative measurements that disprove the hypothesis.
