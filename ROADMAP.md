# Eight-Week / 56-Day Technical Sharpness Roadmap

This challenge-driven roadmap is directional, not immutable. Interview evidence, prerequisite gaps, experimental findings, and current industry practice may change sequencing. Record material deviations and their evidence here and in `CURRENT_SESSION.md`. Depth matters more than checking boxes.

## Week 1 — Database to Distributed Processing

**Goal:** Reactivate database fundamentals and understand what changes when execution becomes distributed.

### Day 1 — SQL/Oracle Execution -> Distributed Spark Execution

Cover scans, partitions, tasks, stages, lazy execution, network boundaries, and shuffle. Ask what changes when one database engine becomes distributed storage and compute.

### Day 2 — Join Internals

Refresh nested-loop, hash, sort/merge, indexes, and access paths. Compare shuffle, sort-merge, and broadcast joins; explain what data moves and why.

### Day 3 — Partitioning and Pruning

Compare database partitioning with distributed partitions and files. Study partition pruning, data skipping, and over-partitioning.

### Day 4 — Aggregation at Scale

Study `GROUP BY`, partial/local aggregation, shuffle, reducers/final aggregation, and cardinality.

### Day 5 — Spark Query Optimization

Inspect logical and physical plans, Catalyst concepts, statistics, join selection, Adaptive Query Execution, and runtime optimization.

### Day 6 — SQL/Python/PySpark Coding Lab

Implement comparable transformations using SQL, Python where appropriate, and PySpark. Inspect execution rather than only output correctness.

### Day 7 — Performance Debugging Challenge

Diagnose a deliberately slow pipeline. Review coding, internals, Staff-level explanation, and the architecture bridge.

## Week 2 — Build the Enterprise Warehouse Correctly

### Day 8 — Source systems, business requirements, and grain
### Day 9 — Facts, dimensions, star schemas, and normalization trade-offs
### Day 10 — Bronze/raw ingestion, metadata, and auditability
### Day 11 — Silver validation, standardization, and deduplication
### Day 12 — Gold models, aggregates, and serving
### Day 13 — Data quality, reconciliation, and failure boundaries
### Day 14 — Challenge: onboard a source with minimal pipeline changes

## Week 3 — Make the Warehouse Survive Change

### Day 15 — Why full reload stops scaling; incremental processing

### Day 16 — CDC internals

Study database logs plus inserts, updates, and deletes.

### Day 17 — Delta MERGE and idempotent processing
### Day 18 — SCD Types 1/2 and temporal correctness
### Day 19 — Late facts/dimensions and ordering
### Day 20 — Schema evolution, contracts, and compatibility
### Day 21 — Challenge: replay corrupted history without duplicating current state

## Week 4 — Performance at Scale

### Day 22 — Scale evolution: 10M -> hundreds of millions -> billions

Ask what actually changes without fabricating benchmarks.

### Day 23 — Shuffle diagnosis and network movement

### Day 24 — Data skew

Practice detection, identify causes, inspect AQE behavior, compare mitigations, and explain trade-offs.

### Day 25 — Small files, compaction, and read/write implications
### Day 26 — Partitioning, clustering, pruning, and data skipping
### Day 27 — Memory, spill, caching, and serialization
### Day 28 — Challenge: diagnose a dramatically slower pipeline from evidence

## Interview checkpoint

Begin applying and interviewing by the end of Week 4. Interview feedback becomes evidence that may reprioritize Weeks 5–8.

## Week 5 — Orchestration, Reliability, and dbt

### Day 29 — Scheduler versus orchestrator

Explain why orchestration exists and when a simpler scheduler is sufficient.

### Day 30 — Airflow fundamentals

Study DAGs, tasks, dependencies, and scheduling.

### Day 31 — Retries, idempotency, and failure semantics
### Day 32 — Backfills, replay, and partial failure

### Day 33 — dbt fundamentals

Study models, dependency graphs, tests, and documentation.

### Day 34 — Decision lab

Choose among dbt, direct SQL, PySpark, and a platform-native pipeline from requirements, scale, complexity, maintainability, operations, and cost.

### Day 35 — Challenge: recover a failed multi-stage daily pipeline safely

## Week 6 — Unity Catalog and Enterprise Governance

### Day 36 — Why centralized catalogs and governance exist

Compare historical metastore/catalog approaches with modern governance needs.

### Day 37 — Unity Catalog hierarchy

Study metastore, catalog, schema, tables/views, and managed/external concepts.

### Day 38 — Identity

Study users, groups, service principals, and workload identities.

### Day 39 — Privileges, ownership, and least privilege
### Day 40 — Lineage, discovery, and auditability
### Day 41 — Dev/test/prod and cross-domain design

### Day 42 — Governance challenge

Design explicit access boundaries and ownership responsibilities for Finance, Fraud/Risk, Marketing, engineering pipelines, and an AI application.

## Week 7 — Modern Table Architecture and Platform Comparison

### Day 43 — Parquet internals and columnar storage
### Day 44 — Why modern table formats emerged

Compare Delta, Iceberg, and Hudi concepts where useful.

### Day 45 — Transaction logs, metadata, snapshots, and table state
### Day 46 — Schema evolution and partition evolution
### Day 47 — Concurrency, versioning, reproducibility, and time travel
### Day 48 — Databricks vs Snowflake on the same workload
### Day 49 — Challenge: select and defend a platform architecture

## Week 8 — Enterprise Data + AI + Staff Integration

### Day 50 — Governed enterprise data consumption by AI applications
### Day 51 — Structured SQL/API access versus document retrieval
### Day 52 — Data correctness and AI correctness
### Day 53 — Batch, streaming, and CDC decisions for AI workloads
### Day 54 — Security, authorization, and governance boundaries
### Day 55 — End-to-end TCO

Include data, compute, operations, AI, people, and governance.

### Day 56 — Final Staff/Architect challenge

Given an ambiguous requirement spanning large-scale data, multiple sources, analytics, governance, reliability, and AI, clarify requirements before selecting technology. Design the platform, identify trade-offs, specify what must be measured, and defend the recommendation.

## Every day

Use `DAILY_LESSON_TEMPLATE.md`: Refresh -> Internals -> Modern Implementation -> Industry Guidance -> Industry Case Study -> Learner Decision -> Build -> Break -> Measure -> Generalize -> Interview -> Architecture Bridge -> Reflection.

## Roadmap deviations

When an interview, experiment, missing prerequisite, technology change, or challenge justifies deviation, record the reason, evidence, effect on sequencing, and updates made to `CURRENT_SESSION.md`. Do not silently drift.
