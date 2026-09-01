# Day 02 Lesson — Join Internals

- Conceptual Learning: COMPLETE
- Reasoning Exercises: COMPLETE
- Coding Practice: DEFERRED
- Experiment: DEFERRED
- Measured Evidence: NONE
- Roadmap topic: Join Internals
- Capability classification: partially simulate; runtime capability not yet verified
- Deferred labs: LAB-006 through LAB-009 in `../../LAB_BACKLOG.md`

All numeric scenarios below are conceptual examples supplied during the lesson unless explicitly labeled as learner production experience.

## 1. Problem

Choose and debug join strategies without jumping from one visible symptom to a configuration fix. Separate data correctness, data reduction, optimizer estimates, data movement, task/partition distribution, and legitimate resource constraints.

## 2. Refresh — traditional join selection

### Scenario / question

ORDERS has 1B rows and CUSTOMERS has 5M rows; initially neither is indexed or sorted. Which join is appropriate?

### My reasoning

Row counts alone were insufficient; projected size and available compute/memory mattered. Hash join appeared preferable because nested loop could require expensive repeated access and sort-merge introduced CPU, memory, and I/O for sorting.

### What was correct

The reasoning compared prerequisite work and did not treat row count as byte size. Hash join commonly builds on the smaller input and probes with the larger input.

### Correction / refinement

Join algorithm and access path must be reasoned together. Nested loop can be reasonable when an index/selective access path makes repeated lookup cheap. A hash build has representation overhead beyond serialized/raw bytes. Sort-merge can spill and need not hold the entire dataset in memory; existing ordering makes it more attractive.

### Staff/Lead vocabulary and principle

Do not only ask which algorithm is cheaper. Ask which expensive prerequisite work—lookup access, hashing, partitioning, or ordering—has already been done.

### Interview version

“I would compare projected bytes, access paths, existing ordering, memory, and selectivity. With no useful access path or ordering, building a hash relation on the smaller side is a candidate, but I would not select from row counts alone.”

## 3. Internals — Broadcast Hash Join

### Scenario / question

ORDERS is 1 TB and CUSTOMERS is initially small. Can moving CUSTOMERS avoid moving the fact?

### My reasoning

Broadcast the smaller customer relation so the 1 TB orders relation can be probed without hash-partitioning both inputs.

### What was correct

CUSTOMERS is the build side; ORDERS is the probe side. The build relation is distributed and represented as a hash structure. Probe rows can be streamed/processed against it; the full 1 TB probe side need not fit in memory at once. Broadcast Hash Join still contains `BroadcastExchange` but can remove the two hash-partitioning Exchanges and Sorts associated with a Sort-Merge Join.

### Correction / refinement

Broadcast feasibility is not `row count` or `on-disk size < executor memory`. Consider projected bytes, serialized transfer, in-memory hashed relation, replication to workers, execution memory, concurrent workload, and runtime overhead. Serialized/on-disk size is not equal to in-memory hash-table size. Build keys need not be unique; duplicates produce multiple matches rather than “latest wins.”

### Staff/Lead vocabulary and principle

Sort-Merge Join pays for ordering so it can merge. Hash Join pays for a hash structure so it can probe.

## 4. Modern implementation — reduce data before movement

### Projection

CUSTOMERS grew conceptually from about 150 MB to 6 GB because wide columns were projected, with unchanged row count. The learner proposed selecting only the two needed attributes and reassessing size.

Correct: `row count != data size`. Projection can change the physical strategy by making a build side broadcast-eligible. `SELECT *` can cause a double regression: broadcast becomes unattractive, and the replacement shuffle join now scans, serializes, shuffles, sorts, spills, and outputs wider rows.

### Filtering

For NJ/active customers, the learner proposed filtering before Exchange/join so irrelevant rows do not travel. Refinement: early filter plus projection may eliminate the fact-side shuffle/sort by making broadcast feasible.

Use: `business requirement -> filter -> project -> re-evaluate size -> choose join strategy`.

### Predicate pushdown distinction

Predicate pushdown may prevent irrelevant source data from being read. Even without source-level pushdown, a Spark `Filter` before Exchange/join can reduce join work. The Staff-level diagnostic question is: “At what point in the physical plan was the data actually reduced?”

## 5. Sort-Merge Join internals

Conceptual plan on both inputs:

`Scan -> Exchange hashpartitioning(join_key) -> Sort -> SortMergeJoin`

One logical redistribution requirement is represented by Exchange/shuffle operators on both inputs. Exchange solves data location: matching keys reach corresponding partitions. Hash partitioning does not order rows inside those partitions. Sort solves data ordering so the merge can proceed.

## 6. Join skew and partition sizing

### Scenario / reasoning

One hot customer represents about 35% of one conceptual input. The learner reasoned that one task takes much longer and more executors do not split records for the same hash key.

### Refinement

Say “one task is processing a disproportionately large shuffle partition,” not “one executor is slow.” A slow executor alone does not prove skew. Required evidence includes task-duration distribution, shuffle-read/partition sizes, key-frequency distribution, and spill/memory evidence.

Adding executors increases capacity but does not inherently split one hot-key partition. Increasing normal shuffle partitions can improve general parallelism, but `hash(HOT)` still routes HOT together. Too few partitions and skew are different problems:

- **Skew:** most partitions are similar; one/few are extreme outliers.
- **Generally oversized partitions:** most/all partitions are similarly large; additional partition-level parallelism may help.

## 7. Salting

Selective salting changes HOT to `(HOT,0)`, `(HOT,1)`, and so on, allowing fact records to spread. Correctness requires the other side to remain join-compatible. For an N:1 relationship, replicate the matching dimension row across the same salt values and join on `(customer_id, salt)`.

Salting amplifies the replicated side. If it already has many HOT rows, bucket replication can become enormous. Ask: “Can I split the hot side, and what does maintaining join correctness cost on the other side?”

Salt bucket count is evidence-driven, not a multiple of executor count. Measure hot-key volume and unsalted partition behavior, choose a target based on healthy task size/runtime, memory/spill, execution slots, scheduling overhead, and replication, then measure again. Perfect slot utilization is not the same as minimum job runtime.

## 8. Adaptive Query Execution

AQE means **Adaptive Query Execution**, not Adaptive Query Engine. Static optimization asks what is expected before execution. Adaptive execution uses runtime stage/shuffle evidence to reconsider parts of physical execution. It need not know the business identity `customer_id = HOT`; a disproportionately large shuffle partition can be enough for adaptive skew handling. AQE skew handling is not automatic salting.

Escalation: `reduce unnecessary data -> choose simplest valid join -> accept required shuffle -> verify skew -> investigate AQE -> selective manual salting only if still required`.

## 9. Statistics and plan regression

If yesterday used Broadcast Hash Join and today uses Sort-Merge Join without intentional application change, investigate in order:

1. actual projected build-side volume/width;
2. environment/configuration;
3. optimizer statistics/estimates;
4. projection changes;
5. filter selectivity or ability to reduce early.

Database bridge: bad statistics can cause bad cardinality/size estimates and a poor physical plan. Distinguish actual relation size from optimizer-estimated size; forcing broadcast before explaining the regression can treat the symptom.

## 10. Join cardinality and correctness

For key K: `Output(K) = LeftCount(K) × RightCount(K)`.

Three left rows and three right rows yield nine matches. The supplied conceptual example of 10M HOT rows by 500K HOT rows implies five trillion logical matches. This is arithmetic, not a measured workload.

- **Input skew:** one/few partitions receive disproportionate input.
- **Cardinality explosion:** duplicate/many-to-many matches multiply output, even if input partitions appear manageable.

The first question is whether the business intends N:M—not how to make Spark process the exploded result faster.

Build-side uniqueness is not required by hash join. One order joined to three customer rows returns three rows unless business/query logic resolves versions. Never assume “last/latest wins” or that `MAX(timestamp)` is the valid rule without defined semantics.

## 11. Learner production experience — Amex

The learner described a prior Amex join that was effectively N×N. Available Spark resources initially processed the growing workload; around the third month, continued growth caused OOM. Investigation found the N×N/cardinality explosion. No additional implementation, size, metric, date, or business detail is asserted.

Interview lesson: resource increases can temporarily mask a cardinality defect; multiplicative output eventually overwhelms the system as data grows.

## 12. Correctness before optimization

Conceptual production scenario: expected `SALES N:1 CUSTOMERS`; C999 has 2M sales rows and 25 active customer rows despite an invariant of exactly one active customer per ID.

Order of action: investigate why the invariant failed; determine the valid record using defined rules; restore N:1; validate C999; rerun/measure representative workload; only then investigate legitimate skew. Source, ingestion, CDC, SCD/version processing, or active-record logic are investigation areas—not asserted causes.

Do not salt your way around incorrect business data.

## 13. Stop, Assess, Then Answer

`Observation -> Known -> Assumption -> Missing Evidence -> Inspect / Ask -> Conditional Diagnosis -> Recommendation -> Validation`

Hidden assumption: “CUSTOMERS join key is unique.” It matters because a supposed N:1 join becomes N:M if false. Ask for expected business cardinality and verify actual per-key counts. A Staff-level answer makes this conditional before selecting a join optimization.

Avoid vague “it depends.” Say: “I do not have enough information to choose yet. I would check X and Y because they determine Z. If X is true, I would choose A; otherwise I would investigate B.”

## 14. Interview explanation

See `interview-cheat-sheet.md`. Core diagnostic order:

`What changed? -> Is cardinality correct? -> Are filters/projections minimal and early? -> Which plan and why? -> Where does data move? -> What do task/partition metrics show? -> Oversized partitions or skew? -> Can AQE help? -> Only then manual salting`

Diagnose before tuning. Restore the simplest valid execution path before adding a workaround for a more expensive path.

## 15. Architecture bridge

The learner can now evaluate join strategy from business cardinality, projected bytes, prerequisites, estimates, data movement, runtime distribution, and correctness. Architecture conclusions that depend on runtime performance remain unresolved until LAB-006 through LAB-009 execute.

## 16. Reflection

The major change is from immediately solving a plausible assumption to explicitly stopping, classifying uncertainty, collecting discriminating evidence, and giving a conditional recommendation in precise Staff/Lead vocabulary.
