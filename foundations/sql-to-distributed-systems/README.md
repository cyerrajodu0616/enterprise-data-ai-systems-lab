# Day 1 — From SQL/Oracle Execution to Distributed Spark Execution

## Primary question

What changes when a query that once ran inside one database engine must execute across many machines?

## Scenario

The fictional enterprise must combine orders, payments, customer status history, and a partner product feed to produce a daily customer-order view. The data contains duplicates and late payments. Begin with a database-shaped solution, then inspect how the same logical work becomes scans, partitions, tasks, stages, joins, shuffle, and network movement in Spark.

## Learning path

Use `LEARNING_GUIDELINES.md` and the daily lesson pattern. The learner should inspect both logical and physical plans, identify wide transformations, predict data movement and failure/retry boundaries, and explain why distributed execution changes optimization. Do not pre-solve the exercise during repository initialization.

## Required analogy record

For each comparison—full table scan versus distributed file/partition scan, index lookup versus pruning/data skipping, database hash join versus shuffle join, small lookup strategy versus broadcast, database optimizer versus Catalyst/AQE, redo/change log versus CDC, database partitioning versus distributed layout, materialized view versus managed derived data, and database transaction versus transactional lake format—record similarity, difference, distributed consequence, and where the analogy breaks.

## Day 1 deliverables

- hand-written first-pass SQL and PySpark approach;
- predicted stages, shuffle boundaries, and bottlenecks;
- captured logical and physical plans;
- an experiment hypothesis and unfilled measurement record;
- failure/retry and testing notes;
- a concise Staff-level interview explanation.
