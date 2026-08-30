# Day 01 Lesson

- Conceptual Learning: COMPLETE
- Reasoning Exercises: COMPLETE
- Coding Practice: DEFERRED
- Experiment: DEFERRED
- Roadmap topic: SQL/Oracle Execution -> Distributed Spark Execution
- Enterprise challenge: Initial warehouse design
- Capability classification: partially simulate; runtime capability not yet verified
- Deferred labs: LAB-001 through LAB-005 in `../../LAB_BACKLOG.md`

## 1. Problem

Move from reasoning about execution inside one SQL/Oracle database engine to reasoning about work distributed across Spark partitions, tasks, stages, executors, and execution slots. The goal was to predict data movement, failure behavior, and retry risk before writing PySpark.

## 2. Refresh

The familiar database model concentrates access paths, joins, CPU, memory/buffer cache, disk, temporary space, and parallel processes under one engine. Spark retains logical ideas such as scans, filters, projections, joins, and aggregation, but physical work is split across data partitions and scheduled tasks. Similar logical operations therefore do not imply identical physical execution.

## 3. Internals

The working model became:

`Data -> Partitions -> Tasks -> Stages -> Executors / execution slots`

An action triggers lazy work. Narrow dependencies can remain partition-local. A wide dependency requires records to be redistributed, creating an Exchange/shuffle boundary and a new stage. Executors provide processes and resources; cores or available slots bound concurrent task execution. When runnable tasks exceed slots, scheduling can require task waves. Those behaviors were reasoned about, not measured.

## 4. Modern Implementation

### Narrow transformations

- **Learner reasoning:** Scan, filter, and projection can preserve partition locality; filter and projection appeared effectively one-to-one at the partition level.
- **Challenge/refinement:** They are narrow when an output partition depends on a limited input partition and records do not need redistribution. Row counts may change, and optimizer behavior must still be confirmed from the physical plan.
- **Generalized principle:** Before optimizing Spark code, ask whether the operation requires data movement.

### Shuffle and Exchange

The learner developed this sequence:

`records distributed across input partitions -> grouping requirement -> hash partition by key -> Exchange -> network shuffle -> new shuffle partitions`

A `groupBy` plus aggregation commonly requires equal keys to meet. Local/partial aggregation may reduce transferred records, but the actual plan determines the operators used.

### Data skew

- **Learner reasoning:** A hot key such as `c-hot` can concentrate much more data in one shuffle partition. Adding another executor does not necessarily split a key already assigned to one partition.
- **Refinement:** The oversized partition can create one expensive task and a straggler; the stage waits for all tasks. Relevant evidence would include data distribution, partition/task sizes, durations, spill, and uneven task completion.
- **Generalized principle:** More aggregate capacity does not automatically fix indivisible or badly partitioned work.

## 5. Industry Guidance

No external documentation was captured during this conceptual session. Current Spark/Databricks behavior must be verified when the deferred labs run; no version-specific claim is treated as observed evidence here.

## 6. Industry Case Study

Not required for this conceptual session. No company scale or architecture claim was introduced.

## 7. Learner Decision

Predict the physical boundary before implementation: scans, filters, and projections may remain local; grouping by key may introduce Exchange and shuffle. Treat the prediction as a hypothesis until `explain()` and runtime evidence confirm it.

## 8. Coding Lab

DEFERRED. No SQL or PySpark implementation was executed or preserved. The required work is tracked in LAB-001 through LAB-005.

## 9. Experiment

DEFERRED. Five falsifiable lab items are recorded in `../../LAB_BACKLOG.md`. Expected mechanisms are not results.

## 10. Measurement

None. Runtime, task count, executor/core count, shuffle size, spill, partition size, and task duration were not measured.

## 11. Break It

Two failure modes were reasoned through:

1. `lost intermediate partition -> lineage -> rerun required upstream work -> recreate missing output`
2. `task executes -> external action -> task fails -> retry -> duplicate action risk`

The first is conditional: Spark can recompute recoverable intermediate output from lineage when dependencies and sources remain available; not every failure has the same recovery scope. The second motivates idempotency for side effects. Only a safe synthetic sink may be used in LAB-005.

## 12. Explain the Result

There is no experimental result. The conceptual conclusion is that deterministic transformations are generally safer to retry or recompute than non-idempotent external effects. This remains reasoning until tested in a controlled environment.

## 13. Generalize

Distributed performance and correctness depend on the shape and boundaries of work, not only on total resources. Identify data movement, indivisible partitions, retry boundaries, and side effects before selecting an optimization.

## 14. Interview Explanation

- **Short conceptual:** Spark divides data into partitions and runs tasks in stages. Wide operations move data through a shuffle; narrow operations can often remain local.
- **Detailed technical:** A grouping requirement can hash-partition records by key, introduce an Exchange, transfer and serialize records, and create new shuffle partitions. A hot key can overload one partition and produce a straggler.
- **Production debugging:** Inspect the physical plan and per-task evidence for Exchange, uneven input/shuffle sizes, duration, and spill. Do not assume adding executors fixes a single skewed partition.
- **Staff-level:** Design retryable computation to be deterministic and make external effects idempotent or deduplicated. Separate expected behavior from measured evidence before making architecture decisions.

## 15. Architecture Bridge

The learner is better equipped to assess where a distributed design introduces network boundaries, skew risk, recomputation cost, and duplicate-action risk. No architecture recommendation should cite Day 1 as empirical evidence until the backlog labs run.

## 16. Reflection

The mental model changed from one engine choosing and executing a plan to a scheduler coordinating partitioned work across stages and execution slots. The key question is now not just “what operator runs?” but “where does data move, how is work divided, and what happens when a unit is retried or lost?”
