# Day 03 Architect/Engineer Challenge Review

## 1. Partition pruning

- **Correct:** Connected a partition-key predicate with avoiding irrelevant data.
- **Refinement:** Partitioning alone is insufficient; predicate shape and optimizer support determine elimination.
- **Staff vocabulary:** The optimizer may prune partitions that cannot satisfy a usable partition-key predicate.

## 2. Index versus skipping

- **Correct:** Used a database index as an analogy for avoiding work.
- **Refinement:** Never guarantee index use; B-tree access and metadata-based skipping are different mechanisms.
- **Staff vocabulary:** Statistics can eliminate files/blocks that cannot match without locating an exact row.

## 3. Table, file, and execution partitions

- **Correct:** Separated persistent organization, storage objects, and runtime task units.
- **Refinement:** Never mechanically equate table partition size with Spark input partition size.
- **Staff vocabulary:** Layout elimination and runtime parallelism are separate decision layers.

## 4. High-cardinality partitioning

- **Correct:** Asked for workload, correlation, cardinality, distribution, and skew evidence.
- **Refinement:** Fragmentation and small files do not inherently imply shuffle.
- **Staff vocabulary:** Choose physical organization from dominant predicates plus data-distribution evidence.

## 5. UUIDs

- **Correct:** Recognized that overlapping ranges can weaken min/max skipping.
- **Refinement:** UUID is not inherently unsuitable for clustering; physical locality determines metadata selectivity.
- **Staff vocabulary:** Trace physical locality → metadata selectivity → skipping effectiveness.

## 6. Changed workload

- **Correct:** Refused to recluster from filter frequency alone.
- **Refinement:** Frequency and selectivity are each insufficient without current scan/skipping evidence.
- **Staff vocabulary:** Treat poor product locality as a hypothesis until execution evidence confirms excess scanning.

## 7. Small-file diagnosis

- **Correct:** Compared healthy/degraded executions and asked whether ingestion changed.
- **Refinement:** Correlation is not proof; test file/task overhead against shuffle, spill/GC, skew, scan growth, pruning, and other stages.
- **Staff vocabulary:** Similar bytes with radically more files/tasks makes useful bytes per task and orchestration overhead diagnostic.

## 8. Remediation and prevention

- **Correct:** Sought a one-time repair and a durable write-path response.
- **Refinement:** Say compact/rewrite, not repartition, for file remediation. A 20 MB batch cannot independently produce 128 MB of data.
- **Staff vocabulary:** Balance freshness outcome, cadence, file behavior, and maintenance cost.

## 9. Predicate shape

- **Correct:** Put the execution plan before prescription.
- **Refinement:** Functions do not universally disable pruning; behavior depends on engine/version/optimizer.
- **Staff vocabulary:** Inspect partition filters and scan metrics to determine whether pruning occurred.

## 10. Production regression

- **Correct:** Investigated before setting a partition count.
- **Refinement:** Acknowledge unchanged code as Known and investigate remaining variables.
- **Staff vocabulary:** `repartition()` introduces redistribution and must address a demonstrated distribution/parallelism problem.

## 11. Architect challenge

- **Correct:** Classified Known, missing evidence, diagnosis, candidates, and validation.
- **Refinement:** Candidate layout changes are not decisions before causal evidence and correctness checks.
- **Staff vocabulary:** Separate scan/layout from runtime distribution and validate the intended bottleneck.

## 12. Liquid clustering

- **Correct:** Asked what happens to historical data after key evolution.
- **Refinement:** Changed keys do not imply instant historical reorganization; migration scope has explicit cost.
- **Staff vocabulary:** Flexibility changes how migration is managed; it does not eliminate migration cost.

## Remaining gaps

- No Day 3 SQL/PySpark implementation or test.
- No executed Day 3 experiment.
- No measured Day 3 physical plan, partition-filter, file, scan, task, shuffle, spill, or runtime evidence.
- LAB-010 through LAB-014 remain TODO.
