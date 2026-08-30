# Technical Sharpness Lab Backlog

This file is the durable source of truth for deferred coding and experiments. It prevents a discussed or predicted mechanism from being mistaken for experimentally verified behavior.

## Status and completion rules

Statuses are `TODO`, `IN PROGRESS`, `BLOCKED`, and `DONE`. Never place a predicted result in a result field.

When executing a lab:

1. preserve the original hypothesis;
2. record environment and configuration;
3. record the dataset and controlled variables;
4. record actual observations separately from interpretation;
5. link implementation, plans, metrics, and results;
6. mark the item `DONE` only after evidence is durable;
7. update prior conclusions if evidence contradicts them.

## LAB-001 — Narrow vs Wide Transformation

- **Origin:** Week 1 Day 1 — SQL/Oracle Execution -> Distributed Spark Execution
- **Question/hypothesis:** Filter and projection should preserve partition locality, while operations requiring redistribution by key should introduce an Exchange/shuffle boundary.
- **Exercise:** Create a small reproducible Spark dataset. Compare physical plans for scan, filter, projection, and `groupBy` plus aggregation using `explain()` or the available Spark plan-inspection mechanism.
- **Expected evidence:** Physical plans, Exchange operators, shuffle boundary, partition information where available, and execution metrics where available.
- **Environment/tool:** Databricks Free Edition or another available Spark environment.
- **Status:** TODO
- **Result/artifact link:** not run

## LAB-002 — Task Waves and Parallelism

- **Origin:** Week 1 Day 1 — SQL/Oracle Execution -> Distributed Spark Execution
- **Question/hypothesis:** When runnable tasks exceed available execution slots, tasks should execute in multiple scheduling waves.
- **Exercise:** Create enough partitions to exceed available execution parallelism and observe scheduling behavior where exposed.
- **Expected evidence:** Partition count, task count, observable execution parallelism, and task scheduling behavior. Do not infer executor or core counts.
- **Environment/tool:** Databricks Free Edition or another available Spark environment.
- **Status:** TODO
- **Result/artifact link:** not run

## LAB-003 — Shuffle Skew

- **Origin:** Week 1 Day 1 — SQL/Oracle Execution -> Distributed Spark Execution
- **Question/hypothesis:** A disproportionately frequent key can create an oversized shuffle partition and a straggler task.
- **Exercise:** Generate synthetic data with a hot key such as `c-hot`, run `groupBy(key)`, and compare hot-key work with normal-key work.
- **Expected evidence:** Generated distribution, execution plan, partition/task data sizes, task durations, spill, and skew evidence where available. Record unavailable metrics as limitations.
- **Environment/tool:** Databricks Free Edition or another available Spark environment.
- **Status:** TODO
- **Result/artifact link:** not run

## LAB-004 — Lineage and Recomputation

- **Origin:** Week 1 Day 1 — SQL/Oracle Execution -> Distributed Spark Execution
- **Question/hypothesis:** Spark can reconstruct recoverable lost intermediate data by rerunning necessary lineage rather than always restarting the entire application.
- **Exercise:** Determine what controlled failure or recomputation behavior can safely and realistically be demonstrated. Document the limitation if the available environment cannot support a meaningful test.
- **Expected evidence:** Controlled failure setup, relevant plan or lineage, observed recovery behavior, rerun scope where visible, and environment limitations.
- **Environment/tool:** Available Spark environment; capability not yet verified.
- **Status:** TODO
- **Result/artifact link:** not run

## LAB-005 — Retry and Side-Effect Safety

- **Origin:** Week 1 Day 1 — SQL/Oracle Execution -> Distributed Spark Execution
- **Question/hypothesis:** Retryable distributed computation combined with a non-idempotent external side effect creates duplicate business-action risk; an idempotency key or deduplication mechanism should prevent duplicate application.
- **Exercise:** Use only a safe simulation such as a test table, synthetic counter, mock API, or test file/log sink. Compare retry without idempotency against retry with an idempotency key or deduplication.
- **Expected evidence:** Safe test setup, induced retry/failure, sink state before and after, duplicate behavior, deduplicated behavior, and limitations.
- **Environment/tool:** Local test harness or available Spark environment. Never use real payments or consequential systems.
- **Status:** TODO
- **Result/artifact link:** not run
