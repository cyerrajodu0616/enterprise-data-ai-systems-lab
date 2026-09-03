# Day 03 Architect/Engineer Challenge — Learner Reasoning

These entries preserve reasoning supplied from the completed session. They do not imply code or lab execution.

## 1. August 2026 partition pruning

**Question:** For 5 billion ORDERS rows across ten years, monthly partitioned by `order_date`, should an August 2026 query scan everything?

**My reasoning:** It should not need to scan all rows when the predicate aligns with the partition key.

## 2. Database index versus file-level skipping

**Question:** What changes when `customer_id = 12345` is added?

**My reasoning:** I initially mapped the Oracle solution to an index on `customer_id`, then separated optimizer-selected index access from file/row-group statistics that can eliminate impossible candidates.

## 3. Three physical concepts

**Question:** Are table partitions, files, and Spark execution partitions interchangeable?

**My reasoning:** No. A table partition is persistent organization, files live within it, and execution partitions define runtime task work. A table partition can contain many files and use many tasks.

## 4. Eighty million customers

**Question:** Should the table be partitioned by 80 million customer IDs?

**My reasoning:** I challenged the fragmentation risk and asked for filter mixes, combinations, correlations, cardinality, distribution, and skew before selecting a column.

## 5. UUID/random-key correction

**Question:** Do UUIDs make statistics useless?

**My reasoning:** I initially doubted UUID min/max usefulness. The refinement was that scattered physical placement—not the UUID type itself—creates overlapping ranges and weak skipping.

## 6. Product-heavy workload change

**Question:** Should a newly product-heavy workload trigger immediate reclustering?

**My reasoning:** No. I first ask whether it is sustained, which consumer changed, which queries are slow, whether date predicates remain, what is scanned/skipped, selectivity, and the actual bottleneck.

## 7. Small-file evidence

**Question:** What does similar scan volume but radically more files and tasks suggest?

**My reasoning:** I first asked whether ingestion changed and whether read files correlated with small files. The stronger candidate is file-management, open, planning, and scheduling overhead, but correlation alone is not proof.

## 8. Compaction, repartition, and freshness

**Question:** How should old small files be repaired and recurrence prevented?

**My reasoning:** I initially said “one-time repartition.” The accurate remediation is compact/rewrite. Prevention must balance a justified freshness SLA, ingestion cadence, file behavior, and maintenance cost.

## 9. Predicate shape

**Question:** Is `YEAR(order_date)` always worse than a direct range?

**My reasoning:** I would inspect the physical plan, partition filters, pushed filters, and scan metrics before claiming whether pruning occurred in the actual engine/version.

## 10. Twenty-to-seventy-five-minute regression

**Question:** Should we immediately repartition to 500 partitions?

**My reasoning:** No. Code is known unchanged. I would inspect source behavior, plan, partition selection, filters, tasks, bytes/task, durations, layout, statistics, shuffle/spill, and stage timing first.

## 11. Final architect challenge

**Question:** How would you approach 5 billion rows, day/country/product-category partitions, about 3 million files, poor customer locality, and 15-minute ingestion?

**My reasoning:** Separate Known from missing evidence; diagnose pruning/layout, files, skipping, and runtime distribution; evaluate simpler partitioning, customer locality, compaction, and ingestion prevention only as candidates; validate correctness before causal performance metrics.

## 12. Liquid-clustering evolution

**Question:** If clustering keys change, what happens to old files and historical queries?

**My reasoning:** New work may use the changed strategy, but historical data is not assumed to reorganize instantly. I would compare historical access needs and old-layout performance with targeted or broader rewrite cost before choosing a migration path.
