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

## LAB-006 — Join Strategy and Data Reduction

- **Origin:** Week 1 Day 2 — Join Internals
- **Question/hypothesis:** A sufficiently small projected build side should permit Broadcast Hash Join and avoid fact-side shuffle/sort; filtering and projection may change the selected strategy, not merely reduce runtime.
- **Exercise:** Create reproducible fact/dimension data. Compare physical plans for a forced/eligible broadcast join and a Sort-Merge Join, then vary build-side projection and filter selectivity without claiming a strategy in advance.
- **Expected evidence:** Input and projected sizes where observable, logical/physical plans, BroadcastExchange, input Exchanges/Sorts, selected join operator, configuration/statistics, and limitations.
- **Environment/tool:** Databricks Free Edition or another available Spark environment.
- **Status:** TODO
- **Result/artifact link:** not run

## LAB-007 — Skew, AQE, and Selective Salting

- **Origin:** Week 1 Day 2 — Join Internals
- **Question/hypothesis:** A hot key should create one/few outlier shuffle partitions; AQE may adapt from runtime partition statistics, while selective salting can distribute the hot key only if the matching side remains join-compatible.
- **Exercise:** Compare an unsalted hot-key join, AQE-enabled behavior where supported, and selective salting with matching-side replication. Measure amplification and validate equality/correctness of outputs.
- **Expected evidence:** Key frequencies, partition/shuffle-read distribution, task-duration distribution, spill where exposed, adaptive plan, salt count rationale, replicated-side row growth, and correctness checks.
- **Environment/tool:** Databricks Free Edition or another available Spark environment; record unsupported metrics explicitly.
- **Status:** TODO
- **Result/artifact link:** not run

## LAB-008 — Join Cardinality and N:M Explosion

- **Origin:** Week 1 Day 2 — Join Internals
- **Question/hypothesis:** Duplicate rows on both sides multiply per-key output according to `LeftCount(K) × RightCount(K)` and can turn an intended N:1 relationship into an N:M correctness and resource problem.
- **Exercise:** Compare a valid N:1 baseline with a controlled duplicate build-side case. Predict and assert per-key and total output counts before considering performance.
- **Expected evidence:** Input key counts, expected cardinality, actual output counts, correctness assertions, plan, resource observations where available, and explicit business invariant.
- **Environment/tool:** Local SQL/Spark test or Databricks Free Edition.
- **Status:** TODO
- **Result/artifact link:** not run

## LAB-009 — Statistics and Join-Plan Regression

- **Origin:** Week 1 Day 2 — Join Internals
- **Question/hypothesis:** Actual build-side size, projection/selectivity, optimizer estimates, or relevant configuration can change a plan from Broadcast Hash Join to Sort-Merge Join; the cause must be isolated rather than assuming stale statistics.
- **Exercise:** If feasible, construct controlled plan comparisons by changing one variable at a time or by comparing available estimates with actual projected data. Do not force a misleading environment demonstration.
- **Expected evidence:** Good/bad physical plans, actual projected relation characteristics, optimizer estimates/statistics where exposed, relevant configuration, controlled variable, and limitations.
- **Environment/tool:** Available Spark environment; mark BLOCKED if estimates cannot be meaningfully controlled or inspected.
- **Status:** TODO
- **Result/artifact link:** not run

## LAB-010 — Partition Pruning and Predicate Shape

- **Origin:** Week 1 Day 3 — Partitioning and Pruning
- **Question/hypothesis:** A predicate that directly constrains a partition column may enable more effective pruning than an equivalent transformed predicate, but actual behavior depends on the engine, version, optimizer, and expression support.
- **Exercise:** Create equivalent direct-range and transformed date predicates where supported. Change one variable at a time and inspect whether pruning occurs.
- **Expected evidence:** Logical/physical plans, partition filters, pushed filters, partitions and files scanned, bytes read, query results, relevant versions/configuration, and limitations.
- **Environment/tool:** Databricks Free Edition or another available Spark environment; capability and exposed metrics not yet verified.
- **Status:** TODO
- **Result/artifact link:** not run

## LAB-011 — Physical Locality and Data Skipping

- **Origin:** Week 1 Day 3 — Partitioning and Pruning
- **Question/hypothesis:** Improved physical locality for selective `customer_id` predicates should make file-level statistics more selective and may reduce files and bytes read compared with equivalent randomly scattered values.
- **Exercise:** Create logically equivalent datasets with poor customer locality and improved customer locality. Run the same selective customer queries.
- **Expected evidence:** Physical layout, collected statistics, files considered/skipped/read, bytes scanned, runtime, identical query results, and environment limitations.
- **Environment/tool:** Databricks Free Edition or another available Spark environment; capability and exposed metrics not yet verified.
- **Status:** TODO
- **Result/artifact link:** not run

## LAB-012 — Small Files and Compaction

- **Origin:** Week 1 Day 3 — Partitioning and Pruning
- **Question/hypothesis:** For equivalent logical data and scan volume, many small files may add discovery, metadata, open, planning, scheduling, and execution overhead relative to fewer larger files.
- **Exercise:** Create logically equivalent many-small-file and fewer-larger-file layouts, preserving controlled variables and required organization.
- **Expected evidence:** File count and size distribution, planning/scan behavior, task count, bytes per task, task-duration distribution, stage/runtime, correctness, and falsifying evidence such as shuffle/spill/skew dominance.
- **Environment/tool:** Databricks Free Edition or another available Spark environment; capability and exposed metrics not yet verified.
- **Status:** TODO
- **Result/artifact link:** not run

## LAB-013 — Repartitioning Cost and Valid Use

- **Origin:** Week 1 Day 3 — Partitioning and Pruning
- **Question/hypothesis:** Unnecessary `repartition()` should add Exchange/shuffle and may increase runtime, while repartitioning may help only when a demonstrated distribution or parallelism problem benefits from redistribution.
- **Exercise:** Compare a baseline with unnecessary repartitioning, then construct a separate controlled case with a demonstrated distribution/parallelism problem and test whether repartitioning addresses it.
- **Expected evidence:** Plans, Exchange operators, stages, shuffle read/write, task distribution, runtime, selected partition counts, correctness, and controlled-variable differences.
- **Environment/tool:** Databricks Free Edition or another available Spark environment; capability and exposed metrics not yet verified.
- **Status:** TODO
- **Result/artifact link:** not run

## LAB-014 — Physical Optimization Correctness Invariants

- **Origin:** Week 1 Day 3 — Partitioning and Pruning
- **Question/hypothesis:** Physical optimizations must preserve equivalent business results for the same input/snapshot even when layout and execution metrics change.
- **Exercise:** For each Day 3 physical optimization, compare before/after outputs using the relevant business invariants before accepting performance evidence.
- **Expected evidence:** Row counts, business keys, duplicates, null behavior, aggregates, business totals, query results, snapshot/input identity, and explicit pass/fail assertions.
- **Environment/tool:** Databricks Free Edition or another available Spark environment; capability and exposed metrics not yet verified.
- **Status:** TODO
- **Result/artifact link:** not run
