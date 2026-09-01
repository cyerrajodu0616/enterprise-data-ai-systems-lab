# Day 02 — Five-Minute Join Internals Interview Cheat Sheet

## Stop, Assess, Then Answer

`Observation -> Known -> Assumption -> Missing Evidence -> Inspect / Ask -> Conditional Diagnosis -> Recommendation -> Validation`

Never silently convert an unknown into a fact. Avoid “it depends.” Say:

> The decision depends primarily on X and Y. I do not have those values yet, so I would check X because it determines __ and Y because it determines __. If they show __, I would choose A; otherwise I would investigate B. I would validate with __.

## Join Strategy Quick Decision

### Broadcast Hash Join

- Attractive when the **projected, filtered build side** is safe and economical to distribute and hash.
- Smaller side builds the hash relation; larger probe-side rows can be processed without the whole probe fitting in memory.
- Cost/risk: `BroadcastExchange`, network replication, in-memory hash expansion, worker memory pressure, concurrency, runtime overhead.
- Avoid deciding from row count or serialized/on-disk size alone.

### Sort-Merge Join

- `Exchange` on both inputs solves key location; `Sort` solves within-partition ordering; merge consumes ordered streams.
- Attractive when broadcast is unsuitable, shuffle is legitimate, or useful partitioning/ordering already exists.
- Cost/risk: network, serialization, sorting, memory, spill, and skew.
- Phrase: “Sort-Merge pays for ordering so it can merge; Hash Join pays for a hash structure so it can probe.”

### Nested Loop

- Do not reject from algorithm name alone. Pair it with access path and selectivity.
- Indexed/selective repeated lookup can be reasonable; unindexed repeated scans can be disastrous.

## First Checks When a Join Becomes Slow

1. What changed—data volume/width/distribution, code, filter/projection, config, or statistics?
2. Is expected versus actual join cardinality correct?
3. Are rows and columns reduced as early as possible?
4. Which physical plan was selected, and why?
5. Compare actual projected size with optimizer estimates.
6. Where are Exchanges, Sorts, and BroadcastExchange?
7. Inspect task-duration, shuffle-read, partition-size, spill, and key-frequency distributions.
8. Is the problem generally oversized partitions or one/few skewed outliers?
9. Can AQE handle verified runtime skew?
10. Add manual salting only if simpler/correct paths remain insufficient.

Diagnose before tuning. Restore the simplest valid execution path first.

## Skew vs Oversized Partitions

- **Skew:** one/few outliers; a straggler task processes a disproportionately large shuffle partition. More executors or normal shuffle partitions do not inherently split one hot key.
- **Generally oversized:** most/all partitions are similarly large; more partition-level parallelism may help.

## Join Cardinality

`Output(K) = LeftCount(K) × RightCount(K)`

- Validate intended 1:1, N:1, 1:N, or N:M before tuning.
- Duplicate build keys do not cause “latest wins”; they produce multiple matches.
- If expected N:1 becomes N:M, fix the semantic/data-quality violation before performance mitigation.

## AQE Before Manual Salting

AQE means Adaptive Query Execution. It can use runtime shuffle statistics to adapt parts of physical execution, including evidence of oversized partitions, without semantic knowledge of the business hot key. It is not automatic salting.

## Salting

- Helps split a verified hot key by changing the partitioning key.
- Matching side must contain compatible salt values; otherwise matches are lost.
- Replication amplifies the matching side; measure that cost and output correctness.
- Choose buckets using hot volume, healthy task evidence, memory/spill, available execution slots, overhead, and amplification—not a magic number or executor multiple.

## Vocabulary Upgrade

- Not “one executor is slow”; say “a straggler task is processing a disproportionately large shuffle partition.”
- Not “add executors”; distinguish insufficient aggregate capacity from an indivisible/skewed partition.
- Not “5M rows is small”; assess projected bytes, in-memory hash representation, replication, memory pressure, and concurrency.
- Not “increase shuffle partitions for skew”; it improves general parallelism but does not inherently split a hot hash key.
- Not “Spark produces too many rows”; validate expected versus actual cardinality and possible N:M multiplication.
- Not “deduplicate customers”; identify the violated invariant and valid record using defined data semantics.
- Not “filter first because faster”; reduce rows/columns before movement and reassess whether a simpler join becomes feasible.
- Not “AQE knows the hot customer”; AQE can identify outlier shuffle partitions from runtime statistics.
- Not “force broadcast”; explain why the optimizer stopped choosing it before overriding the plan.

## Seven Stop-and-Assess Examples

1. **Broadcast:** Known: 5M rows. Missing: projected bytes, hash representation, worker memory, estimates/config. Conditional choice only after checking them.
2. **Slow executor:** A slow executor/task does not prove skew. Inspect task durations, shuffle read, partition sizes, key frequency, and spill.
3. **Add executors:** First distinguish insufficient aggregate compute from one indivisible hot-key partition.
4. **More shuffle partitions:** First distinguish uniformly large partitions from outliers; normal partition count does not split one HOT hash key.
5. **Output explosion:** Compare expected N:1 with actual N:M using per-key counts before sizing Spark.
6. **Duplicate customers:** Do not arbitrarily deduplicate; establish the invariant violation and valid record rule.
7. **Broadcast disappeared:** Compare actual projected size, filters/projection, estimates/statistics, and config between good/bad runs before forcing broadcast.

## 60-Second Interview Answer

> I start by asking what changed and validating expected versus actual join cardinality, because an N:1 relationship that became N:M is a correctness problem that resource tuning can mask. Then I verify filters and projections are minimal and early, inspect the physical plan, and explain why Spark selected broadcast, sort-merge, or another strategy using actual projected size, estimates, and configuration. I locate Exchanges, Sorts, and BroadcastExchange, then inspect task-level runtime, shuffle-read, partition-size, spill, and key-frequency distributions. That distinguishes generally oversized partitions from true hot-key skew. I prefer the simplest correction—restore cardinality, reduce data, or recover a valid broadcast path—then evaluate AQE for verified skew. I use selective salting only when evidence shows it is still necessary, preserving join compatibility and measuring replication cost and correctness.

## Production Story Pattern — Amex

- **Situation:** A growing join workload at Amex initially completed with the available Spark resources.
- **Task:** Investigate why continued growth eventually caused OOM around the third month.
- **Action:** The investigation identified an effective N×N join/cardinality explosion.
- **Result/lesson:** Resource capacity had temporarily masked a multiplicative semantic/cardinality defect. Validate expected versus actual cardinality before treating the issue as Spark sizing. No additional metrics or implementation details are claimed.
