# Day 02 Quiz Review

## 1. Traditional selection

- **Correct:** Compared projected size and prerequisite cost, not just row count.
- **Refinement:** Nested loop must be paired with access-path reasoning; sort-merge can spill and becomes attractive when ordering already exists.
- **Staff vocabulary:** Ask which expensive prerequisite work has already been done.

## 2. Broadcast

- **Correct:** Identified build/probe roles and avoided moving the 1 TB probe side through join shuffle.
- **Refinement:** Broadcast still has `BroadcastExchange`; account for in-memory hash representation, replication, concurrent memory pressure, and overhead. Build keys need not be unique.

## 3. Data reduction

- **Correct:** `row count != data size`; reduce rows/columns before data movement.
- **Refinement:** Filtering/projection can change the join strategy, not merely shave runtime. Source predicate pushdown and an early Spark Filter are distinct.

## 4. Sort-Merge Join

- **Correct:** Exchange solves location and Sort solves ordering.
- **Refinement:** One logical redistribution requirement appears physically as Exchange/shuffle on both inputs.

## 5. Skew

- **Correct:** Distinguished hot-key concentration from aggregate capacity.
- **Refinement:** A slow executor is only an observation. Diagnose a straggler task using task duration, shuffle read, partition size, key frequency, and spill evidence.

## 6. Salting and AQE

- **Correct:** Preserved join compatibility and recognized replicated-side cost; AQE uses runtime evidence.
- **Refinement:** Bucket count should target measured work, not executor multiples or perfect slot use. AQE skew handling is different from salting.

## 7. Cardinality and correctness

- **Correct:** Applied `LeftCount(K) × RightCount(K)` and placed business intent before tuning.
- **Refinement:** Never assume “latest wins” or arbitrary deduplication. Encode the defined valid-record rule.

## 8. Reasoning discipline

- **Correct:** Identified build-key uniqueness as a hidden assumption.
- **Refinement:** State known, unknown, missing evidence, conditional diagnosis, recommendation, and validation before answering.

## Remaining gaps

- No Day 2 SQL/PySpark implementation or test.
- No physical plan, statistics, Spark UI, shuffle, spill, task, AQE, or benchmark evidence.
- LAB-006 through LAB-009 remain TODO.
