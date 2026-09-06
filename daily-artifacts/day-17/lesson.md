# Day 17 Lesson — Delta MERGE and Idempotent Processing

- Sequence status: COMPLETED EARLY / OUT OF SEQUENCE
- Conceptual Learning: COMPLETE
- Reasoning Exercises: COMPLETE
- Coding Practice: DEFERRED / TODO
- Experiment: DEFERRED / NOT RUN
- Measured Evidence: NONE
- Roadmap topic: Delta MERGE and idempotent processing
- Day 16 dependency: CDC internals remains NOT STARTED; this lesson assumes the supplied PostgreSQL WAL → Debezium → Kafka → Bronze Delta contract and does not complete Day 16
- Deferred lab: LAB-015 in `../../LAB_BACKLOG.md`

All performance, conflict, SLA, and workload numbers below are supplied lesson scenarios unless explicitly labeled as arithmetic assumptions. No Day 17 Databricks implementation, benchmark, Spark UI analysis, conflict simulation, or measurement was executed in this repository.

## 1. Business outcome and invariants

### Question and learner reasoning

Before choosing which CDC record wins, identify the producer, its guarantees, and the field that orders committed source changes. The target `customer_current` is a 2 TB Delta table receiving 25 million daily records. It must expose exactly one authoritative current state per `customer_id` for customer service, billing eligibility, and regulatory reporting.

### Mentor refinement

The required result is the latest committed customer state from PostgreSQL—not the row with an arbitrary latest timestamp. The supplied path is PostgreSQL WAL → Debezium → Kafka → Bronze Delta. `source_sequence` is the authoritative ordering signal; `event_timestamp` is application-provided and non-authoritative, while `ingestion_timestamp` records arrival only. The MERGE, currently matched on `customer_id`, grew from 25 to 90 minutes and retries sometimes produced unexpected values. CDC has a 15-minute freshness SLA and backfill has a 24-hour SLA.

### Staff/Architect principle

Define the business result and producer ordering contract before designing deduplication.

## 2. Day 16 CDC dependency boundary

Day 16 remains a future lesson. It must validate WAL/Debezium/Kafka ordering and delivery, event identity, delete representation, snapshots, and schema evolution. Day 17 consumes the supplied contract without claiming those guarantees were verified or teaching the future Day 16 material.

## 3. Source cardinality and authoritative ordering

### Learner reasoning

Multiple records for one customer in a batch should be reduced to the highest authoritative sequence before MERGE.

```python
from pyspark.sql import Window, functions as F

window = Window.partitionBy("customer_id").orderBy(
    F.col("source_sequence").desc()
)

deduplicated = (
    source
    .withColumn("source_rank", F.row_number().over(window))
    .filter(F.col("source_rank") == 1)
    .drop("source_rank")
)
```

### Mentor refinement

This creates one source row per target key, but equal sequences need a deterministic contract. Equal sequence with different payload is a CDC contract violation to quarantine, not an arbitrary tie to resolve.

### Staff/Architect principle

Deterministic source cardinality prevents ambiguous multiple matches inside one batch.

## 4. Target sequence guard

Use the exact state-transition guard:

```sql
source.source_sequence > target.last_source_sequence
```

A lower sequence is stale, an equal sequence is a duplicate/retry, and only a higher sequence can modify current state. Source deduplication protects within a batch; the target sequence guard protects across batches, retries, and late arrivals.

## 5. Delete tombstones and resurrection prevention

Keep a minimal tombstone rather than removing all evidence of the business key: a protected/approved key, `is_deleted`, `last_source_sequence`, deletion timestamp, and source/audit metadata. Null or remove unnecessary PII. Preserve the original event in immutable Bronze subject to retention policy.

| Sequence case | Correct current-state behavior |
|---|---|
| `DELETE 504`, then late `UPDATE 503` | `503 > 504` is false; preserve tombstone. |
| Unmatched `DELETE 504`, then late `INSERT 501` | Insert minimal tombstone; reject 501. |
| Duplicate `DELETE 504` | Equal sequence; no state change. |
| `ACTIVE 505` | Newer by ordering; business policy decides whether transition is allowed. |

The source sequence determines which event is newer. Business policy determines whether the newer state transition is valid.

## 6. Reactivation, rejection, and sequence state

If reactivation is legitimate, apply the higher-sequence active state. If deletion is terminal, preserve the tombstone, quarantine `ACTIVE 505`, alert the source owner, and never silently restore the customer. Make quarantine idempotent with event identity or sequence.

Track distinct meanings: `last_seen_sequence` is the greatest observed; `last_applied_sequence` is the greatest accepted state transition; `last_rejected_sequence` records rejected events. A rejection must not advance `last_applied_sequence`.

## 7. Independent versus dependent later events

A complete authoritative after-image may be independently validated and applied. A partial update or business command may depend on rejected state. For dependent events, isolate only the affected key, buffer/quarantine later events for it, continue unrelated customers, reconcile from a corrected event or authoritative snapshot, then replay in order.

Ordering tells us which event came later. Event semantics tell us whether it can be processed independently.

## 8. Performance diagnosis before layout changes

The lesson supplied this scenario evidence:

| Phase | Time |
|---|---:|
| Source deduplication | 8 minutes |
| Target scanning and matching | 55 minutes |
| Rewriting affected files | 24 minutes |
| Delta commit | 3 minutes |

The target has 40,000 files; 38,000 are scanned and 2,400 rewritten for 250,000 changed customers whose identifiers are randomly distributed. Measure total files, files skipped/scanned, bytes scanned, files removed/added, rows updated/inserted/deleted/copied unchanged, source rows before/after deduplication, scan/rewrite/commit time, skew, spill, and retries where exposed.

## 9. Target layout candidate and success conditions

Do not partition directly by high-cardinality `customer_id`, and do not assume event-date partitioning suits a current-state table. Liquid clustering by `customer_id` is a candidate because MERGE and point lookups use it, but declaring a key does not instantly reorganize history. Changed keys may span the key space, so test a representative MERGE.

Accept a layout only with identical customer state, identical latest accepted sequence per customer, no deleted-customer resurrection, fewer files/bytes scanned, lower scan time, and no unacceptable small-file or write regression.

## 10. Write amplification

The fraction of files rewritten describes a broad update footprint. Write amplification compares physical bytes rewritten with logical bytes changed. Under explicit lesson assumptions: 250,000 rows × 1 KB ≈ 250 MB logical change; 2,400 files × 128 MB ≈ 307 GB physical rewrite; approximately 1,228× amplification. These are arithmetic assumptions, not repository or production measurements.

## 11. No-op CDC events and ordering boundaries

Of 25 million records, the scenario says 250,000 change attributes and 24.75 million have identical attributes but newer sequences. Prefer preventing unnecessary source writes, but log CDC may correctly emit UPDATE operations with unchanged values. Never discard immutable Bronze.

Skipping target updates avoids sequence-only file rewrites but loses the newest observed ordering boundary unless validated Kafka per-key ordering and checkpoint guarantees supply it. If the target stores only changed state, name the field `last_applied_change_sequence`. A compact sequence-state table is another option, but introduces a stateful component and needs evidence.

## 12. Concurrent writers and deterministic retries

In the supplied conventional copy-on-write case, Jobs A and B read version 100; A changes C101, B changes C900, and both rows occupy one immutable Parquet file. A commits version 101. B's stale transaction fails atomically and must retry the complete deterministic MERGE against the latest snapshot—not recover one task or file.

Safe retries require an immutable source batch, deterministic deduplication, sequence guards, idempotent tombstones, and bounded retry. Actual conflict behavior depends on runtime, isolation, table features, predicates, and row-level concurrency; same-file conflict is not universal across current configurations.

## 13. Diagnose conflicts before retry policy

The lesson reports 47 of 52 weekly conflicts occur during daily backfill, even though CDC and backfill touch distinct customers sometimes stored in shared files. CDC retries can take 25 minutes. Inspect jobs, conflict type, frequency/window, keys/files, logical versus physical contention, retry/wasted compute, transaction history, and SLA priority before prescribing retries.

## 14. SLA-driven workload coordination

Prioritize CDC's 15-minute SLA. Pause/resume the 24-hour backfill as deterministic, idempotent, independently committed checkpointed chunks; replan each resumed chunk against the latest snapshot. Measure both workloads so coordination does not merely move the SLA violation.

## 15. Backfill chunk sizing

With a 15-minute CDC interval, 6-minute p95 duration, and 2-minute buffer, the supplied safe backfill window is approximately 7 minutes. Choose the largest deterministic chunk reliably fitting the window. Avoid unordered `LIMIT`; prefer checkpointed ranges such as `customer_id` ranges and align with layout where practical. Tiny chunks add startup, commit, log, small-file, and repeated-rewrite overhead.

## 16. Stop condition and monitoring

The lesson—not this repository—reports seven-minute chunks completing backfill in 18 hours, satisfying both SLAs and reducing conflicts 95%. That supports stopping redesign while monitoring conflict frequency, retry cost, SLA headroom, progress, scanning, rewriting, and small files.

Reopen if CDC nears 15 minutes, backfill nears 24 hours, conflicts/retries materially rise, backfills become continuous, aborted cost matters, writers are added, or chunking increases small files/write amplification.

## 17. Vocabulary Upgrade

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

## 18. Architect/Staff challenge

Design correctness first: establish the source contract, deterministic source cardinality, target guard, tombstone/reactivation policy, and dependency handling. Diagnose scan, rewrite, and write amplification separately. Treat layout as a measured candidate. Qualify concurrency behavior, retry the whole deterministic transaction, and coordinate writers from both SLAs. Size deterministic chunks from observed duration, monitor causal metrics, and state which evidence would reopen the decision.

## 19. Interview answer

**Business outcome:** Keep exactly one authoritative current state per customer from the latest committed PostgreSQL change.

**Correctness controls:** Use the authoritative source sequence, deterministic per-batch deduplication, a target sequence guard, and tombstones that prevent stale resurrection while separating ordering from transition policy.

**Performance evidence:** Separate source deduplication, target scan, rewrite, and commit; inspect files and bytes scanned/replaced and logical versus physical change.

**Decision:** Pilot key locality and coordinate deterministic backfill chunks around the tighter CDC SLA.

**Trade-off:** Sequence-only updates preserve observed ordering but can amplify writes; skipping them needs validated ordering/checkpoint guarantees or separate sequence state.

**What would change the decision:** Reopen for SLA pressure, rising retry/conflict cost, continuous backfills, new writers, small-file growth, or representative measurements that reject the layout hypothesis.

## 20. Architecture bridge, open questions, and reflection

Correct CDC state is a state-machine and contract problem before it is a MERGE syntax problem. Remaining questions: actual producer ordering/delivery; equal-sequence conflict policy; delete retention/PII; reactivation; after-image completeness; runtime/table features/isolation and row-level concurrency; current file statistics/layout; measured amplification; no-op ordering; conflict cost; chunk distribution; and SLA headroom.

Primary references checked 2026-09-06: [Databricks MERGE](https://docs.databricks.com/aws/en/delta/merge), [isolation and conflicts](https://docs.databricks.com/aws/en/optimizations/isolation), [isolation levels](https://docs.databricks.com/aws/en/optimizations/isolation/isolation-levels), [Delta best practices](https://docs.databricks.com/aws/en/delta/best-practices), [data skipping](https://docs.databricks.com/aws/en/tables/data-skipping), [liquid clustering](https://docs.databricks.com/aws/en/delta/clustering), and [ACID guarantees](https://docs.databricks.com/aws/en/lakehouse/acid).
