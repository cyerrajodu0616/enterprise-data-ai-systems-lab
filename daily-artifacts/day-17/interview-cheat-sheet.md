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

In conventional copy-on-write, disjoint keys in one file may contend. A conflict fails atomically; retry the complete deterministic transaction against the latest snapshot. Current behavior depends on runtime, isolation, table features, predicates, and row-level concurrency.

Safe backfill window = CDC interval − p95 CDC duration − buffer = 15 − 6 − 2 ≈ 7 minutes. Pilot deterministic checkpointed chunks, prioritize CDC, and validate both SLAs.

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

**Decision:** I would test better customer-key locality and coordinate deterministic backfill chunks around CDC's tighter SLA.

**Trade-off:** Skipping no-op attribute updates saves rewrites but may lose observed sequence state; clustering and chunking also impose maintenance/commit costs.

**What would change the decision:** SLA pressure, greater retry cost, continuous backfills, new writers, small-file growth, or representative measurements that disprove the hypothesis.
