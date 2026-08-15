# Day 1 — From SQL/Oracle Execution to Distributed Spark Execution

Day 1 is prepared but intentionally unsolved. Reason before implementation; do not begin with PySpark syntax.

## 1. Problem

Produce a daily customer-order fact from customers, accounts, orders, payments, customer-status history, and a partner product feed containing duplicates and late payments. Define the business question and grain before tables.

## 2. Refresh

Reactivate the SQL/Oracle model: where table and index blocks reside, how access paths and joins are selected, what executes inside one database engine, and how work uses CPU, buffer/cache memory, disk, temporary space, and parallel query processes.

## 3. Internals

Before coding, predict where data resides, what can execute locally, what crosses workers, how files become partitions/tasks/stages, where lazy execution ends, and which operations create network shuffle or retry boundaries.

## 4. Modern implementation

Map the logical workload to distributed Spark only after the prediction. Compare scans, pruning, joins, stages, tasks, shuffle, and failure recovery without claiming database concepts are exact equivalents.

## 5. Industry guidance

Consult current official Spark and Databricks documentation during the lesson; record the exact version and source used.

## 6. Industry case study

Select a source-backed large-scale processing case only if it illuminates Day 1. Record reported facts without copying the architecture blindly.

## 7. Learner decision

Predict the grain, model, execution boundaries, data movement, bottlenecks, and simplest implementation before seeing a solution.

## 8. Coding lab

Manually write a first-pass SQL solution, then outline or implement the PySpark equivalent.

## 9–16. Experiment through reflection

Form a small reproducible hypothesis; record measurements as `not run`; deliberately introduce one scale or data-shape problem; explain observed evidence; generalize the principle; give conceptual, technical, debugging, and Staff-level explanations; identify the architecture decision improved; and record the changed mental model.

## Required outputs

- requirements and grain statement;
- dimensional-model sketch;
- manual SQL and PySpark attempt;
- predicted and captured logical/physical plans;
- experiment record with no fabricated results;
- failure/retry and test strategy;
- architecture-bridge note;
- interview explanation.
