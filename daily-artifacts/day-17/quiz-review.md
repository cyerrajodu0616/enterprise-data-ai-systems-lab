# Day 17 Architect/Staff Challenge — Review

- Sequence status: COMPLETED EARLY / OUT OF SEQUENCE
- Evidence: conceptual review only; implementation NOT RUN

## Business outcome and ordering

**Correct:** The answer starts from the authoritative current-state outcome and source ordering contract.

**Refinement:** Validate the Day 16 delivery, identity, snapshot, delete, and schema guarantees later.

**Staff vocabulary:** Authoritative ordering signal; latest committed operational-source state.

## Deduplication, guard, and deletion

**Correct:** Deterministic source cardinality and the target sequence guard solve different boundaries. Tombstones prevent stale resurrection.

**Refinement:** Equal-sequence/different-payload cases require quarantine. Ordering does not decide whether reactivation is valid.

**Staff vocabulary:** Target sequence guard; deletion tombstone; last seen, last applied, and last rejected sequence.

## Event dependencies

**Correct:** Only the affected key is isolated while unrelated customers continue.

**Refinement:** Require authoritative after-image completeness before bypassing a rejected event.

**Staff vocabulary:** Event semantics determine independent processability.

## Scan, layout, and amplification

**Correct:** Scan and rewrite are diagnosed separately, and clustering remains a test candidate.

**Refinement:** Report update footprint separately from physical/logical write amplification, and validate all layout claims on representative MERGE work.

**Staff vocabulary:** Broad update footprint; write amplification; evidence-driven locality.

## No-ops and ordering state

**Correct:** Avoiding identical-attribute target updates can reduce rewrites.

**Refinement:** It is safe only with validated per-key ordering/checkpoints or explicit sequence state; Bronze remains immutable.

**Staff vocabulary:** `last_applied_change_sequence`; ordering boundary.

## Concurrency, workload coordination, and stopping

**Correct:** Retry the complete deterministic transaction and prioritize the tighter CDC SLA with checkpointed backfill chunks.

**Refinement:** Current row-level concurrency depends on runtime/table/isolation configuration. Measure both SLAs and chunk overhead.

**Staff vocabulary:** Physical file contention versus business-key conflict; safe concurrency window; evidence-based stop condition.

## Remaining gaps

Day 16 CDC guarantees are unverified. No Day 17 implementation, metrics, conflict simulation, or layout benchmark exists. LAB-015 remains TODO.
