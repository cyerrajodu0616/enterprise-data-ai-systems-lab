# Day 03 — Five-Minute Partitioning and Pruning Interview Cheat Sheet

## Stop, Assess, Then Answer

`Observation → Known → Assumption → Missing Evidence → Inspect / Ask → Conditional Diagnosis → Recommendation → Validation`

Never turn an unknown into a fact. State which evidence changes the decision.

## Elimination pipeline

`Partition pruning → Data skipping → Predicate filtering`

- Pruning removes coarse table partitions when usable predicates constrain partition keys.
- Skipping uses metadata/statistics to remove files or blocks that cannot match.
- Filtering evaluates remaining data. Skipping does not necessarily locate the exact matching row.

## Do not confuse these layers

| Concept | Meaning | Primary performance effect |
|---|---|---|
| Table partition | Persistent logical/physical grouping | Coarse elimination and layout fragmentation |
| Physical file | Parquet/Delta storage object | Metadata, file opens, I/O, and skipping selectivity |
| Spark execution partition | Runtime task work unit | Parallelism, distribution, scheduling, and shuffle |

A table partition can contain many files and use many tasks. Do not target table-partition size to Spark input-partition size mechanically.

## Physical-layout decision

`Workload → predicate combinations → selectivity → distribution/correlation → current locality and skipping → maintenance cost → experiment → measure`

High cardinality alone neither chooses nor rejects a layout. Filter frequency alone is insufficient; selectivity alone is insufficient. First measure whether current organization already avoids the right data.

## Small-file diagnosis

Strong candidate evidence: similar bytes scanned, radically more files considered/read and tasks, collapsed bytes/task, and added planning/scheduling time after a known tiny-file ingestion change.

Compare file count/size distribution, files considered/read, bytes scanned, tasks, bytes/task, duration distribution, stage time, and scheduler overhead.

Falsifiers: shuffle or spill/GC dominates; a few skewed tasks dominate; scan bytes increased; pruning regressed; another stage owns the latency.

## Compaction is not repartitioning

- **Compaction/rewrite:** repairs stored file layout.
- **`repartition()`:** redistributes runtime data and normally adds shuffle.

For small frequent batches: `freshness outcome → cadence → file behavior → maintenance cost`. Preserve a justified SLA; do not weaken it only to manufacture larger files.

## Predicate/pruning diagnostic order

1. Inspect the physical plan.
2. Inspect partition filters and pushed filters.
3. Count selected partitions and files considered/skipped/read.
4. Compare bytes scanned.
5. Recommend predicate changes only from observed engine/version behavior.

Do not claim `YEAR(order_date)` always prevents pruning.

## Liquid clustering and history

Ask whether frequent/selective predicates suffer from poor current locality and excess scan, whether statistics cover them, and whether the skipping gain offsets maintenance.

Changing keys does not imply every historical file is instantly reorganized. Compare historical access range, old-layout performance, rewrite/reclustering cost, and business requirement; choose incremental evolution, targeted history, or broader reorganization and measure.

## Vocabulary Upgrade

- Not “Partitioning means Spark doesn't scan the whole table.” Say: “When predicates constrain the partition key in a form the optimizer can use, partition pruning can eliminate irrelevant partitions before scanning.”
- Not “Spark reads the header and finds the correct file.” Say: “The engine may use file-level or row-group metadata/statistics to eliminate files or blocks that cannot satisfy the predicate.”
- Not “Small files cause shuffle.” Say: “Small files can increase metadata, file-open, planning, and scheduling overhead. Shuffle is caused by data redistribution requirements.”
- Not “Repartition it to improve performance.” Say: “First establish whether execution partitioning or data distribution is the bottleneck; `repartition()` introduces redistribution and should solve an identified parallelism/distribution problem.”
- Not “Random IDs mean stats won't work.” Say: “Poor physical locality can produce broad or overlapping statistics that reduce data-skipping selectivity.”
- Not “Use liquid clustering because Databricks recommends it.” Say: “Evaluate whether the workload contains frequent/selective predicates for which the existing physical organization causes excessive scanning, and whether improved locality would materially improve data skipping.”

## Staff/Lead phrases

- “I would validate that assumption first.”
- “That is a hypothesis; I would confirm it from the execution evidence.”
- “I would compare the healthy and degraded execution.”
- “I would identify where the additional latency is introduced before changing the physical layout.”
- “I would separate the scan/layout problem from the runtime distribution problem.”
- “I would validate both correctness and performance.”
- “I would not optimize physical layout without understanding the dominant access patterns.”

## 60-second interview answer

> I start with expected correctness and dominant access patterns. Then I inspect the physical plan, partition filters, selected partitions, files considered, skipped and read, bytes scanned, tasks, bytes per task, duration distribution, and stage timing. That separates coarse pruning, file-level skipping, file-management overhead, and runtime redistribution. Similar bytes with vastly more files and tasks supports a small-file overhead hypothesis, while shuffle, spill, skew, increased scan volume, or another slow stage could falsify it. I use compaction for stored-file remediation and `repartition()` only for a demonstrated runtime distribution problem. Any layout or clustering change remains conditional on workload, selectivity, current locality, maintenance cost, and historical access. I validate equivalent results first, then verify that the intended causal bottleneck improved.
