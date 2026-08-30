# Day 01 Quiz Attempt

These entries preserve the learner's reasoning from the completed conceptual session. They are not reconstructed claims of code execution.

## 1. Conceptual

**Question:** How do partitions, tasks, stages, executors, and execution slots relate?

**Learner reasoning:** Data is divided into partitions; tasks work on partitions; tasks are grouped into stages; executors run tasks using available cores or slots. If tasks exceed slots, work must occur in waves. Lazy work starts when an action requires a result.

## 2. Execution plan

**Question:** Which operations should remain local, and where should a network boundary appear?

**Learner reasoning:** Scan, filter, and projection can preserve partition locality. A grouping requirement brings equal keys together, so hash partitioning can introduce `Exchange hash partition`, network shuffle, and new shuffle partitions.

## 3. Skew debugging

**Question:** What happens when `c-hot` is disproportionately frequent, and why might another executor not solve it?

**Learner reasoning:** The hot key can land in one oversized shuffle partition, causing one expensive task and a straggler. The stage waits for that task. Another executor does not necessarily divide work already concentrated in one partition. Look for uneven task/partition sizes, task time, and spill.

## 4. Failure recovery

**Question:** What can happen when intermediate shuffle output is lost?

**Learner reasoning:** Spark can use lineage to determine how the data was produced, rerun required parent work, and recreate missing output rather than necessarily restarting the whole application.

## 5. Implementation safety

**Question:** Why are external side effects dangerous inside retryable tasks?

**Learner reasoning:** A task might perform the action, fail before completion is acknowledged, and then retry, producing the action twice. Deterministic/idempotent processing is safer for retries.

## 6. Staff-level decision

**Question:** What can be predicted before execution, and what requires evidence?

**Learner reasoning:** We can predict likely locality and shuffle boundaries from operation semantics. The actual physical operators and runtime behavior must be confirmed with the plan and metrics; predictions are not measurements.
