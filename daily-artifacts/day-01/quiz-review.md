# Day 01 Quiz Review

## Review status

Reviewed from the learner reasoning preserved in `quiz.md`. No coding attempt or measured result is implied.

## 1. Execution hierarchy

- **Correct:** Partitions define units of data work; tasks execute stage work for partitions; stages are separated by shuffle boundaries; executor resources limit concurrent tasks.
- **Refinement:** A core is commonly associated with a concurrent task slot, but exact scheduling and exposed parallelism are environment-dependent and must be observed.
- **Follow-up:** LAB-002.

## 2. Narrow and wide dependencies

- **Correct:** Filter and projection generally do not require records to move between partitions; grouping by key commonly requires redistribution.
- **Refinement:** “One-to-one” is useful intuition for dependencies, not a guarantee about equal row counts or every optimized physical plan. Narrow means each output partition depends on a limited input partition without required cross-partition redistribution.
- **Follow-up:** LAB-001.

## 3. Skew

- **Correct:** A hot key can produce an oversized shuffle partition, a straggler task, and a stage-level wait. More executors alone may not subdivide that partition.
- **Refinement:** Skew must be demonstrated from actual distribution and per-task evidence; it was not measured in Day 1.
- **Follow-up:** LAB-003.

## 4. Recomputation

- **Correct:** Lineage can allow Spark to recompute required upstream work for recoverable lost intermediate output.
- **Refinement:** Recovery scope depends on the failure, available lineage, source availability, and runtime behavior. Avoid claiming that every intermediate failure avoids broader restart.
- **Follow-up:** LAB-004.

## 5. Retry and side effects

- **Correct:** A retry after an externally visible action can duplicate the business effect when the action is non-idempotent.
- **Refinement:** Deterministic computation and idempotent/deduplicated sinks address different aspects of safety. Test only with a synthetic or non-consequential sink.
- **Follow-up:** LAB-005.

## Remaining gaps

- No SQL or PySpark attempt exists.
- No physical plan was captured.
- No runtime, shuffle, spill, task-wave, skew, or recovery metric was measured.
