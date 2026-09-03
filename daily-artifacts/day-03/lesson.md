# Day 03 Lesson — Partitioning and Pruning

- Conceptual Learning: COMPLETE
- Reasoning Exercises: COMPLETE
- Coding Practice: DEFERRED
- Experiment: DEFERRED
- Measured Evidence: NONE
- Roadmap topic: Partitioning and Pruning
- Capability classification: partially simulate; runtime capability not yet verified
- Deferred labs: LAB-010 through LAB-014 in `../../LAB_BACKLOG.md`

All scale examples below are conceptual learning scenarios unless explicitly labeled as learner-provided production evidence. No Day 3 lab, execution plan, file scan, or benchmark was run.

## 1. Problem

Design and diagnose physical data organization without confusing table partitions, files, and runtime execution partitions or prescribing layout changes before establishing where work is spent. The goal is to eliminate irrelevant data safely, preserve correctness, and make every performance claim conditional on workload and execution evidence.

## 2. Refresh — partition pruning fundamentals

### Scenario / question

A hypothetical ORDERS table contains `order_id`, `customer_id`, `order_date`, `country`, `product_id`, and `amount`. It has 5 billion rows across ten years and is partitioned monthly on `order_date`. What should happen for an August 2026 query?

### My reasoning

The engine should not need to scan all 5 billion rows when the predicate aligns with the partition key.

### Correction / refinement

Because the predicate constrains the partition key, the optimizer may perform partition pruning and eliminate irrelevant partitions from the scan. Partitioning alone does not guarantee reduced scanning: the predicate must let the engine identify partitions that can safely be eliminated.

### Staff/Lead principle

“When predicates constrain the partition key in a form the optimizer can use, partition pruning can eliminate irrelevant partitions before scanning.”

## 3. Database index versus distributed data skipping

### My reasoning

When `customer_id = 12345` was added, I initially mapped the Oracle solution to an index on `customer_id`.

### Correction / refinement

Do not say the database definitely uses that index. The optimizer chooses an access path using selectivity, statistics, index structure, clustering/locality, and estimated cost.

A traditional B-tree lookup is not the same mechanism as distributed file-level skipping. Parquet/Delta implementations may use file or row-group statistics such as minimum and maximum values to eliminate data that cannot match. Relevant statistics can come from Parquet metadata, Delta metadata/log information, or other engine-maintained metadata; do not claim Spark necessarily opens every file header.

`Partition pruning → Data skipping → Predicate filtering`

- **Partition pruning:** eliminate coarse physical partitions.
- **Data skipping:** eliminate files or blocks inside the remaining candidate data.
- **Predicate filtering:** evaluate data that still must be read.

Data skipping primarily identifies what can safely be avoided; it does not necessarily locate the exact physical row containing a match.

## 4. Table partitions, physical files, and Spark execution partitions

### Table partition

Persistent physical/logical organization of table data, commonly selected for coarse-grained elimination.

### Physical file

A Parquet/Delta file stored within the table layout. File organization affects metadata overhead, data skipping, file-open cost, I/O behavior, and small-file behavior.

### Spark execution partition

A runtime unit of parallel processing associated with tasks. `repartition()` changes execution/data distribution and normally introduces a shuffle.

A logical table partition can contain many files and can be processed by many Spark tasks. Table partition size must not be mechanically targeted to Spark input partition size.

Small files do not inherently cause shuffle. They can increase discovery/listing, metadata processing, file-open, task-planning, scheduling, and execution overhead. Shuffle comes from operations that require data redistribution.

## 5. Over-partitioning and workload evidence

### Scenario / my challenge

With approximately 80 million customers, partitioning directly by `customer_id` could create extreme physical fragmentation. My initial concerns included partition count, small files, tasks, and shuffle. I then asked for evidence before choosing another column: actual filter breakdown and combinations, correlations between dimensions, whether the same products occur across countries, cardinality, distribution, and skew.

### Correction / refinement

High-cardinality physical partitioning can create metadata and operational problems, but small files do not automatically imply shuffle. Table partitions, files, and execution partitions must be evaluated separately.

### Staff/Lead principle

Physical organization should be driven by workload and data-distribution evidence, not merely column cardinality or intuition.

## 6. Physical locality and data skipping

The hypothetical workload was 70% recent 30–90 day queries, 15% customer queries across about two years, 10% product/date queries, and 5% other. Date is therefore an important candidate for coarse elimination, but this is not a final architecture decision.

Creating 80 million customer partitions is unnecessary to improve customer access. If customer identifiers are randomly scattered across every file, file-level ranges may overlap broadly and skip little. Better physical locality can make statistics more selective.

`Partitioning → coarse-grained elimination`

`Clustering / physical organization → improve locality`

`Data-skipping statistics → exploit locality to eliminate unnecessary data`

`Predicate filtering → process what remains`

## 7. UUID and random-key correction

### My initial reasoning

I initially reasoned that UUID minimum/maximum statistics might not help.

### Correction / refinement

UUIDs do not automatically make clustering ineffective. Random values scattered across every file can yield broad or overlapping ranges and weak skipping. If UUIDs have deterministic ordering and are physically organized accordingly, file statistics can still become selective for equality or range elimination.

The real chain is `physical locality → metadata selectivity → skipping effectiveness`, not `UUID → bad for clustering`.

## 8. Changing workloads

When product queries became dominant, I did not immediately recommend reclustering. I asked how long the change had existed, whether it was sustained or temporary, whether a consumer changed, which queries were slow, whether they also had date predicates, how much data/files were scanned versus skipped, their selectivity, and where the bottleneck occurred.

**Hypothesis:** A sustained product-heavy workload combined with poor product locality may cause excess scanning. This remains unverified until execution evidence supports it.

## 9. Small-file production diagnosis

### Learner-provided production evidence

Healthy execution was approximately 40 seconds, 900 files considered, 120 files read, 11 GB read, and about 90 scan tasks. Degraded execution was approximately four minutes, 180,000 files considered, 95,000 files read, 12 GB read, and dramatically more scan tasks. The known change was new ingestion behavior producing many tiny files every 15 minutes.

My first questions were whether ingestion changed and whether files read correlated with the small files. Correlation is evidence, not proof.

Because scan bytes remained similar while file and task counts increased radically and useful bytes per task collapsed, file discovery/metadata, file-open, planning, and task-scheduling overhead became a strong root-cause candidate.

Compare task count, bytes per task, task-duration distribution, stage duration, file count, file-size distribution, files considered/read, bytes scanned, and scheduler/task-launch overhead where visible.

Evidence that would falsify or weaken this hypothesis includes downstream shuffle dominating runtime, spill or garbage collection dominating, a few skewed tasks dominating, bytes scanned growing substantially, pruning regressing, or another stage accounting for most added latency.

## 10. Remediation versus prevention

My initial remediation was to “one-time repartition the old small files.” The accurate action is: compact or rewrite existing small files into fewer appropriately sized files while preserving required logical/physical organization. `repartition()` is not a synonym for compaction.

If each 15-minute ingestion batch has only about 20 MB, Spark cannot manufacture a 128 MB output file without accumulating or rewriting more data. The trade-off is:

`freshness requirement → ingestion cadence → file behavior → compaction/maintenance cost`

Validate whether the 20-minute freshness SLA is tied to a measurable business outcome and whether it applies uniformly to all consumers. If justified, preserve it, observe file distribution and query overhead, and introduce compaction or optimized writes only when evidence supports the cost.

## 11. Predicate shape and pruning

For a direct `order_date` range predicate versus `YEAR(order_date)` / `MONTH(order_date)`, do not universally claim that functions prevent pruning. Inspect the physical plan and scan metrics to determine whether pruning occurred and which partition filters were pushed into the scan. Then establish how many partitions/files were selected before recommending a predicate rewrite.

## 12. Production regression diagnostic discipline

In the conceptual regression, runtime changed from about 20 to 75 minutes, input volume and cluster were approximately unchanged, code was **Known** to be unchanged, and files changed only from about 2,000 to 2,100. A proposal to repartition to 500 partitions is premature.

Inspect source behavior, the execution plan, partition selection and filters, task count, bytes per task, task durations, distribution/skew, statistics/metadata, physical layout, runtime configuration, plan differences, shuffle read/write, spill, and stage timing.

`repartition()` introduces a shuffle and should solve an identified distribution or parallelism problem, not serve as a generic performance fix.

## 13. Architect/Engineer challenge

The hypothetical table has 5 billion rows, day/country/product-category partitioning, about 3 million files with many below 5 MB, mostly recent queries, frequent `customer_id` filters, rare product-category filters, customer IDs randomly distributed across files, 15-minute ingestion, and an unverified 20-minute freshness requirement.

### Known

- Customer IDs are randomly distributed across files.
- Product category is physically partitioned but rarely filtered.
- Millions of files exist and many are very small.
- Ingestion runs every 15 minutes and most queries use recent ranges.

Random distribution across files is expected to produce poor customer locality and broad/overlapping file statistics, reducing skipping selectivity; it does not prove that statistics cannot work.

### Missing evidence

- Whether ingestion caused the small files or partition fragmentation amplified them.
- Current partition/file-statistic selectivity and where latency occurs.
- Customer/data skew and business justification for the freshness requirement.

### Diagnosis

Inspect plans, partition filters and partitions selected, files considered/skipped/read, bytes scanned, tasks, bytes/task, duration distribution, and shuffle/skew/spill where applicable. Separate pruning/layout, file fragmentation, skipping, runtime distribution, and other stages.

### Candidate simplest changes — not decisions

1. Remove low-value/high-fragmentation `product_category` partitioning if evidence supports it.
2. Improve customer locality within relevant data.
3. Compact/rewrite existing small files.
4. Prevent recurrence through ingestion/write-layout changes while preserving justified freshness.

### Validation

Correctness first: compare relevant row counts, business keys, duplicates, nulls, aggregates, totals, and query results on equivalent input/snapshots. Then compare `partitions selected → files considered → files skipped/read → bytes scanned → tasks → bytes/task → task-duration distribution → stage/runtime`. Not every metric must decline; the intended bottleneck must improve without changing results.

## 14. Liquid clustering from fundamentals

Traditional partitioning asks which coarse boundaries to create. Clustering asks which values need better physical locality so statistics can eliminate irrelevant data.

`Query workload → predicates and combinations → selectivity and distribution → current locality → excess scan? → potential skipping gain → maintenance cost → experiment → measure`

Frequency alone is insufficient: frequently filtered `country` may be poorly selective. Selectivity alone is insufficient: first determine whether the current layout already skips effectively. Compare files considered, skipped and read plus bytes scanned.

Databricks documentation checked 2026-09-03 states that changing liquid-clustering keys affects subsequent writes and `OPTIMIZE`, but does not automatically rewrite existing data. Historical performance and migration cost therefore remain separate decisions. Choose incremental evolution, targeted historical reclustering/rewrite, or broader reorganization from the historical access range, old-layout performance, business requirement, and rewrite cost—then measure.

Flexibility in physical organization does not remove migration cost; it changes how migration can be managed.

Primary references: [Databricks data skipping](https://docs.databricks.com/aws/en/tables/data-skipping), [Databricks liquid clustering](https://docs.databricks.com/aws/en/delta/clustering), and [Apache Spark Parquet partition discovery](https://spark.apache.org/docs/latest/sql-data-sources-parquet.html).

## 15. Vocabulary Upgrade

- Instead of “Partitioning means Spark doesn't scan the whole table,” say “When predicates constrain the partition key in a form the optimizer can use, partition pruning can eliminate irrelevant partitions before scanning.”
- Instead of “Spark reads the header and finds the correct file,” say “The engine may use file-level or row-group metadata/statistics to eliminate files or blocks that cannot satisfy the predicate.”
- Instead of “Small files cause shuffle,” say “Small files can increase metadata, file-open, planning, and scheduling overhead. Shuffle is caused by data redistribution requirements.”
- Instead of “Repartition it to improve performance,” say “First establish whether execution partitioning or data distribution is the bottleneck; `repartition()` introduces redistribution and should solve an identified parallelism/distribution problem.”
- Instead of “Random IDs mean stats won't work,” say “Poor physical locality can produce broad or overlapping statistics that reduce data-skipping selectivity.”
- Instead of “Use liquid clustering because Databricks recommends it,” say “Evaluate whether the workload contains frequent/selective predicates for which the existing physical organization causes excessive scanning, and whether improved locality would materially improve data skipping.”

Interview phrases: “I would validate that assumption first.” “That is a hypothesis; I would confirm it from the execution evidence.” “I would compare the healthy and degraded execution.” “I would identify where the additional latency is introduced before changing the physical layout.” “I would separate the scan/layout problem from the runtime distribution problem.” “I would validate both correctness and performance.” “I would not optimize physical layout without understanding the dominant access patterns.”

## 16. Interview explanation

Start with the business access patterns and expected correctness. Inspect the plan, partition filters, selected partitions, files considered/skipped/read, bytes scanned, tasks, bytes/task, duration distribution, and stage timing. Separate coarse pruning, file-level skipping, file-management overhead, and runtime redistribution. Change layout only after evidence identifies the bottleneck, then validate equivalent results and the intended causal metric.

## 17. Architecture bridge

The learner can now evaluate when static partitioning, physical locality/clustering, compaction, or runtime repartitioning addresses a demonstrated problem. Architecture conclusions still require LAB-010 through LAB-014 evidence and an explicit freshness/business requirement.

## 18. Reflection and open questions

The mental model changed from “partitioned means less scan” to evidence-driven layered elimination and from generic repartitioning to distinct storage-layout and runtime-distribution decisions.

Open questions: Which metrics does the available environment expose? Did pruning and skipping actually occur? What causes current file fragmentation? Which columns have collected/useful statistics? Which stage owns latency? Is there distribution skew? Is the 20-minute SLA justified and uniform? What historical range would need reorganization after clustering-key changes?
