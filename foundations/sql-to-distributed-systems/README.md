# Day 1 — Define the Warehouse and Trace Distributed Execution

## Enterprise problem

Design the initial daily customer-order fact from customers, accounts, orders, payments, customer status history, and a partner product feed. Define the business question and grain before writing tables. The inputs include duplicate orders and late payments.

## Core question

What changes when this workload moves from one SQL/Oracle database engine to distributed storage and Spark compute?

## Manual work

1. State the grain, candidate facts/dimensions, business keys, and justified surrogate keys.
2. Sketch Bronze, Silver, and Gold responsibilities.
3. Write a first-pass SQL solution without AI-generated code.
4. Write or outline the equivalent PySpark flow.
5. Predict scans, partitions, tasks, stages, shuffle boundaries, join strategies, network movement, and retry boundaries.
6. Inspect logical and physical plans when the environment is available.

## Experiment proposal

Compare a database-shaped implementation with a distributed implementation on a small reproducible dataset. Record capability classification and leave measurements `not run` until executed. Project how design concerns change at 10 million, 600 million, and billions of rows without presenting projections as measurements.

## Required analogy record

Compare table/file scans, indexes versus pruning/data skipping, database hash joins versus shuffle joins, lookup strategies versus broadcast, optimizer versus Catalyst/AQE, redo logs versus CDC, database partitioning versus distributed layout, materialized views versus managed derived datasets, and database versus lake-format transactions. State similarity, architectural difference, distributed consequence, and where each analogy breaks.

## Deliverables

- requirements and grain statement;
- dimensional-model sketch;
- manual SQL and PySpark attempt;
- predicted and captured plans;
- unfilled experiment record;
- failure/retry and test strategy;
- concise Staff-level explanation.
