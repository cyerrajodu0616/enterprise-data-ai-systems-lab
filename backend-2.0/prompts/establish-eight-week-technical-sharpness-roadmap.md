# Establish the Eight-Week Technical Sharpness Roadmap

## Context and reconciliation

The current `agent/cloud-first-enterprise-challenges` branch already contains strong cloud-first, enterprise-challenge, Databricks Free Edition, Airflow/dbt responsibility, debugging, experiment, Unity Catalog, and Day 1 material. Preserve it rather than recreating the repository.

The new request conflicts with the current repository in three places:

1. `ROADMAP.md` is four weeks (38 lines); the request requires eight weeks and 56 visible days.
2. `LEARNING_GUIDELINES.md` is challenge-driven but does not explicitly encode Refresh → Internals → Modern → Industry Guidance → Industry Case Study → Build → Break → Measure → Generalize → Interview.
3. `CURRENT_SESSION.md` has only six fields and cannot independently resume a new session.

No conflict exists in the architecture bridge, cloud-first policy, enterprise project, technology roles, challenge-first organization, experiment discipline, or manual/AI-assisted coding policy. Extend these without overwriting their intent.

## Exact changes

### 1. Update `README.md` lines 39–53

Before:

```markdown
## Repository map

- `enterprise-challenges/` — primary learning sequence and challenge catalog.
- `enterprise-data-platform/` — the evolving warehouse/lakehouse implementation.
- `coding/` — manual SQL, Python, and PySpark practice.
- `debugging/` — broken-system diagnosis using evidence and regression tests.
- `orchestration/airflow/` — orchestration decisions and Airflow artifacts.
- `transformations/dbt/` — SQL transformation, testing, and documentation artifacts.
- `databricks/` — Spark, Delta, performance, CDC, Unity Catalog, and governance mechanisms.
- `experiments/` — reproducible experiment definitions and measured results.
- `ai-integration/` — governed enterprise data for AI.
- `snowflake/` — later workload-based comparison.
- `interview-journal/` — interview evidence and targeted follow-up.

Start with `ROADMAP.md`, `CURRENT_SESSION.md`, the challenge catalog, and the Day 1 proposal.
```

After:

```markdown
## Repository map

- `enterprise-challenges/` — primary learning sequence and challenge catalog.
- `enterprise-data-platform/` — the evolving warehouse/lakehouse implementation.
- `coding/` — manual SQL, Python, and PySpark practice.
- `debugging/` — broken-system diagnosis using evidence and regression tests.
- `orchestration/airflow/` — orchestration decisions and Airflow artifacts.
- `transformations/dbt/` — SQL transformation, testing, and documentation artifacts.
- `databricks/` — Spark, Delta, performance, CDC, Unity Catalog, and governance mechanisms.
- `experiments/` — reproducible experiment definitions and measured results.
- `industry-case-studies/` — source-backed cases organized by engineering problem.
- `ai-integration/` — governed enterprise data for AI.
- `snowflake/` — later workload-based comparison.
- `interview-journal/` — interview evidence and targeted follow-up.
- `DAILY_LESSON_TEMPLATE.md` — the reusable lesson structure.
- `REFERENCES.md` — durable foundations, current official documentation, and curated engineering sources.
- `RESUME_PROTOCOL.md` — deterministic continuation from a new session.

Start with `RESUME_PROTOCOL.md`, `CURRENT_SESSION.md`, `ROADMAP.md`, the current challenge, and the Day 1 proposal.
```

### 2. Replace `LEARNING_GUIDELINES.md` lines 1–41

Before:

```markdown
# Learning Guidelines

The unit of learning is a difficult enterprise problem, not a product feature. For every challenge answer:

1. What business or engineering problem are we solving?
2. What breaks in the current or simple design?
3. Why does it break internally?
4. Which physical resource becomes the bottleneck: CPU, memory, disk I/O, network, serialization, metadata, or parallelism?
5. What is the simplest credible solution?
6. Why should it perform better?
7. How can we prove that experimentally?
8. What complexity did we introduce?
9. What are the operational consequences?
10. What does it cost?
11. What happens at 10x scale?
12. How would another platform solve the same problem?
13. What principle generalizes to another problem?

For every mechanism, also identify its simplest mental model, internals, trade-off, failure boundary, older database analogy, and where that analogy breaks. Never accept “broadcast join is faster” without explaining physical data movement, workload conditions, executor-memory risk, and the measurements needed to test it.

## Technology admission rule

Every technology must answer: **What problem did this solve that the simpler architecture could not?** Complexity and cost must earn their place.

## Evidence and scale

- State a falsifiable hypothesis before execution.
- Record dataset shape/size, runtime, infrastructure, settings, code revision, plan, and constraints.
- Record only observed runtime, scans, shuffle, task distribution, spill, files, resource indicators, and cost.
- Label results `not run` until executed.
- Separate measured results from hypothetical scale projections.
- Progress from small local data to medium and larger distributed experiments when economical, then reason explicitly about 10 million, 600 million, and billions of rows.
- Preserve negative or surprising results.

## Capability classification

For each challenge record one status: **implement and test**, **partially simulate**, or **architecture/design only**. Verify platform capabilities in the current Databricks Free Edition environment; do not infer or fabricate availability.

## Daily challenge pattern

Problem -> current design -> failure -> internals -> bottleneck -> simplest solution -> manual exercise -> hypothesis -> experiment -> measurements -> diagnosis -> trade-offs -> operations -> cost -> 10x scale -> platform comparison -> generalization -> interview explanation -> reflection.
```

After:

```markdown
# Learning Guidelines

The learner is an experienced data engineer refreshing and extending technical depth. The unit of learning is a difficult enterprise problem, not a product feature.

## Learning sequence

### Refresh

Reactivate relevant SQL, Oracle, traditional-database, and prior data-engineering knowledge. Do not restart from beginner assumptions.

### Internals

Explain physical work across CPU, memory, disk, network, serialization, metadata, processes, workers, parallelism, partitions, and files. When two approaches appear to use similar data and infrastructure, identify what work was avoided, moved, parallelized, precomputed, cached, pruned, indexed, broadcast, or reorganized.

### Modern approach

Explain how distributed and cloud systems solve the same class of problem. Use older database concepts as learning analogies, always stating similarity, architectural difference, and where the analogy breaks.

### Industry guidance

Identify current authoritative guidance in this order: official documentation or specification, authoritative book or paper, then credible engineering material. A large company's design is not automatically an industry standard.

### Industry case study

Choose real cases only when relevant. Record the original source, publication date, reported scale, problem, constraints, architecture, rationale, operations, trade-offs, company-specific elements, generalized principle, and applicability to this lab. Never invent details or scale.

### Build, break, and measure

Implement the concept, then deliberately introduce scale, skew, bad data, duplicates, schema change, late data, failures, backfills, permission problems, or regressions. Measure plans, runtime, scans, shuffle, spill, task distribution, files, latency, correctness, and cost where available. Never invent results.

### Generalize and interview

Ask where the principle applies elsewhere. Explain it briefly, technically, as a production incident, and as a Staff-level design decision.

## Challenge questions

For every challenge ask what problem exists, what breaks, why it breaks internally, which resource constrains it, the simplest credible solution, why it should work, how to prove it, complexity/operations/cost introduced, 10x-scale behavior, another platform's approach, and the generalized principle.

## Technology admission rule

Every technology must answer: **What problem did this solve that the simpler architecture could not?** Complexity and cost must earn their place.

## Evidence and scale

- State a falsifiable hypothesis before execution.
- Record dataset shape/size, runtime, infrastructure, settings, code revision, execution plan, and constraints.
- Label results `not run` until executed.
- Separate measured results from hypothetical projections.
- Progress economically from small to distributed experiments, then reason explicitly about 10 million, hundreds of millions, and billions of rows.
- Preserve negative and surprising results.

## Capability classification

For each challenge record **implement and test**, **partially simulate**, or **architecture/design only**. Verify current Databricks Free Edition capabilities rather than inferring them.

## Evidence hierarchy

`Durable concept -> mental model`

`Official documentation/specification -> current behavior`

`Industry case study -> one organization's response to a real problem`

`Our experiment -> evidence for our workload`

`Architecture decision -> requirements + evidence + constraints`

Do not confuse these evidence types.
```

### 3. Update headings in `CODING_PRACTICE_GUIDELINES.md`

Before lines 5 and 15:

```markdown
## Manual Practice
```

```markdown
## AI-Assisted Engineering
```

After:

```markdown
## Manual Practice Mode
```

```markdown
## AI-Assisted Engineering Mode
```

No other coding-policy content changes; the existing policy already satisfies the request.

### 4. Replace `ROADMAP.md` lines 1–38

Before: the exact current file is:

```markdown
# Four-Week Enterprise Challenge Roadmap

The roadmap sequences problems, not products. Each week extends the same warehouse/lakehouse, includes manual coding and debugging, and produces evidence or clearly labeled design reasoning.

## Week 1 — Build It Correctly

**Theme:** From traditional database execution to distributed enterprise data processing.

Build the initial warehouse: requirements, source contracts, dimensional grain, facts/dimensions, ingestion, and Bronze/Silver/Gold responsibilities. Refresh SQL, Python, and PySpark while studying partitions, stages/tasks, shuffle, joins, and plans.

**Core question:** What changes when processing moves from one database engine to distributed storage and compute?

## Week 2 — Make It Survive Change

Introduce full-reload limits, incremental watermarks, CDC inserts/updates/deletes, SCD, late facts/dimensions, duplicate delivery, idempotency, schema evolution, data quality, reconciliation, and replay.

**Core question:** How do we maintain correctness when enterprise data continuously changes?

## Week 3 — Make It Scale and Govern It

Challenge the platform with larger volumes, partitioning, pruning, shuffle, skew, broadcast, AQE, small files, and Delta layout. Introduce multi-team and sensitive-data governance through Unity Catalog problems. Add Airflow when coordination becomes necessary and dbt when SQL transformation sprawl demands organization, testing, and documentation.

**Core question:** How do we keep the platform performant, governable, and operable as data, workloads, and teams grow?

## Week 4 — Make It Production-Capable and AI-Ready

Practice large backfills, failure/recovery, observability, retries, testing, CI/CD design, dev/test/prod isolation, cost/TCO, governed AI access, system design, Staff-level debugging, and interview explanation.

**Core question:** Can this system survive real production operations, and can I defend its architecture?

## Operating rhythm

- Choose the next challenge from `enterprise-challenges/README.md`.
- Classify it as implement/test, partially simulate, or architecture/design only.
- Attempt core code manually; use AI assistance during delivery and review.
- Record experiments without invented results.
- Add technology only when the simpler design fails a stated requirement.
- End with a debugging scenario, architecture implication, and interview-journal update.
```

After: create `# Eight-Week / 56-Day Technical Sharpness Roadmap` with the following exact structure and day titles. Preserve the detailed topics from the user request beneath each day; do not collapse days into weekly summaries.

```markdown
# Eight-Week / 56-Day Technical Sharpness Roadmap

This challenge-driven roadmap is directional, not immutable. Interview evidence, prerequisite gaps, experimental findings, and current industry practice may change sequencing. Record material deviations and their evidence in this file and `CURRENT_SESSION.md`. Depth matters more than checking boxes.

## Week 1 — Database to Distributed Processing

**Goal:** Reactivate database fundamentals and understand what changes when execution becomes distributed.

1. Day 1 — SQL/Oracle Execution -> Distributed Spark Execution
2. Day 2 — Join Internals
3. Day 3 — Partitioning and Pruning
4. Day 4 — Aggregation at Scale
5. Day 5 — Spark Query Optimization
6. Day 6 — SQL/Python/PySpark Coding Lab
7. Day 7 — Performance Debugging Challenge

**Weekly review:** coding, internals, Staff-level explanation, and architecture bridge.

## Week 2 — Build the Enterprise Warehouse Correctly

8. Day 8 — Source systems, business requirements, and grain
9. Day 9 — Facts, dimensions, star schemas, and normalization trade-offs
10. Day 10 — Bronze/raw ingestion, metadata, and auditability
11. Day 11 — Silver validation, standardization, and deduplication
12. Day 12 — Gold models, aggregates, and serving
13. Day 13 — Data quality, reconciliation, and failure boundaries
14. Day 14 — Challenge: onboard a source with minimal pipeline changes

## Week 3 — Make the Warehouse Survive Change

15. Day 15 — Why full reload stops scaling; incremental processing
16. Day 16 — CDC logs, inserts, updates, and deletes
17. Day 17 — Delta MERGE and idempotent processing
18. Day 18 — SCD Types 1/2 and temporal correctness
19. Day 19 — Late facts/dimensions and ordering
20. Day 20 — Schema evolution, contracts, and compatibility
21. Day 21 — Challenge: replay corrupted history without duplicating current state

## Week 4 — Performance at Scale

22. Day 22 — Scale evolution: 10M -> hundreds of millions -> billions
23. Day 23 — Shuffle diagnosis and network movement
24. Day 24 — Data skew, detection, AQE, mitigation, and trade-offs
25. Day 25 — Small files, compaction, and read/write implications
26. Day 26 — Partitioning, clustering, pruning, and data skipping
27. Day 27 — Memory, spill, caching, and serialization
28. Day 28 — Challenge: diagnose a dramatically slower pipeline from evidence

## Interview checkpoint

Begin applying and interviewing by the end of Week 4. Interview feedback becomes evidence that may reprioritize Weeks 5–8.

## Week 5 — Orchestration, Reliability, and dbt

29. Day 29 — Scheduler versus orchestrator
30. Day 30 — Airflow DAGs, tasks, dependencies, and scheduling
31. Day 31 — Retries, idempotency, and failure semantics
32. Day 32 — Backfills, replay, and partial failure
33. Day 33 — dbt models, dependency graph, tests, and documentation
34. Day 34 — Decision lab: dbt vs SQL vs PySpark vs platform-native pipeline
35. Day 35 — Challenge: recover a failed multi-stage daily pipeline safely

## Week 6 — Unity Catalog and Enterprise Governance

36. Day 36 — Why centralized catalogs and governance exist
37. Day 37 — Metastore/catalog/schema/object hierarchy and managed/external concepts
38. Day 38 — Users, groups, service principals, and workload identities
39. Day 39 — Privileges, ownership, and least privilege
40. Day 40 — Lineage, discovery, and auditability
41. Day 41 — Dev/test/prod and cross-domain design
42. Day 42 — Governance challenge for Finance, Fraud/Risk, Marketing, pipelines, and an AI application

## Week 7 — Modern Table Architecture and Platform Comparison

43. Day 43 — Parquet internals and columnar storage
44. Day 44 — Why modern table formats emerged; Delta/Iceberg/Hudi concepts
45. Day 45 — Transaction logs, metadata, snapshots, and table state
46. Day 46 — Schema evolution and partition evolution
47. Day 47 — Concurrency, versioning, reproducibility, and time travel
48. Day 48 — Databricks vs Snowflake on the same workload
49. Day 49 — Challenge: select and defend a platform architecture

## Week 8 — Enterprise Data + AI + Staff Integration

50. Day 50 — Governed enterprise data consumption by AI applications
51. Day 51 — Structured SQL/API access versus document retrieval
52. Day 52 — Data correctness and AI correctness
53. Day 53 — Batch, streaming, and CDC decisions for AI workloads
54. Day 54 — Security, authorization, and governance boundaries
55. Day 55 — End-to-end data/compute/operations/AI/people/governance TCO
56. Day 56 — Final ambiguous enterprise Data + AI Staff/Architect challenge

## Every day

Use `DAILY_LESSON_TEMPLATE.md`: Refresh -> Internals -> Modern Implementation -> Industry Guidance -> Industry Case Study -> Learner Decision -> Build -> Break -> Measure -> Generalize -> Interview -> Architecture Bridge -> Reflection.

## Roadmap deviations

When an interview, experiment, missing prerequisite, technology change, or challenge justifies deviation, record the reason, evidence, effect on sequencing, and updates made to `CURRENT_SESSION.md`. Do not silently drift.
```

The numbered list above is the exact required roadmap skeleton; no day may be omitted. Add the following exact topic details beneath the named days:

```markdown
### Day 1 details
- scans;
- partitions;
- tasks;
- stages;
- lazy execution;
- network boundaries;
- shuffle.

### Day 2 details
- refresh nested-loop, hash, sort/merge, indexes, and access paths;
- compare shuffle, sort-merge, and broadcast joins;
- explain what data moves and why.

### Day 3 details
- database partitioning;
- distributed partitions and files;
- partition pruning and data skipping;
- over-partitioning.

### Day 4 details
- GROUP BY;
- partial/local aggregation;
- shuffle;
- reducers/final aggregation;
- cardinality.

### Day 5 details
- logical and physical plans;
- Catalyst concepts and statistics;
- join selection;
- Adaptive Query Execution and runtime optimization.

### Day 6 details
- implement comparable SQL, Python where appropriate, and PySpark transformations;
- inspect execution, not only output correctness.

### Day 7 details
- diagnose a deliberately slow pipeline;
- review coding, internals, Staff-level explanation, and architecture bridge.

### Day 16 details
- database logs;
- inserts, updates, and deletes.

### Day 24 details
- detection and causes;
- AQE and mitigation;
- trade-offs.

### Days 29–35 details
- distinguish scheduler from orchestrator and justify orchestration;
- Airflow DAGs, tasks, dependencies, scheduling, retries, idempotency, failure semantics, backfills, replay, and partial failure;
- dbt models, dependency graph, tests, and documentation;
- decide among dbt, direct SQL, PySpark, and platform-native pipelines;
- recover a failed multi-stage daily pipeline safely.

### Days 36–42 details
- compare historical metastore/catalog approaches with modern governance needs;
- metastore, catalog, schema, tables/views, and managed/external concepts;
- users, groups, service principals, and workload identities;
- privileges, ownership, and least privilege;
- lineage, discovery, and auditability;
- dev/test/prod and cross-domain access;
- design explicit access and ownership for Finance, Fraud/Risk, Marketing, engineering pipelines, and an AI application.

### Days 43–49 details
- Parquet internals and columnar storage;
- why table formats emerged and useful Delta/Iceberg/Hudi comparisons;
- logs, metadata, snapshots, state, schema/partition evolution, concurrency, versioning, reproducibility, and time travel;
- compare Databricks and Snowflake on the same workload;
- select and defend a platform architecture from requirements.

### Days 50–56 details
- governed enterprise data consumption by AI;
- structured SQL/API access versus document retrieval;
- data correctness and AI correctness;
- batch, streaming, and CDC choices for AI workloads;
- security, authorization, and governance boundaries;
- end-to-end data, compute, operations, AI, people, and governance TCO;
- final ambiguous enterprise requirement spanning scale, sources, analytics, governance, reliability, and AI: clarify before selecting technology, design, identify trade-offs, specify measurements, and defend the recommendation.
```

### 5. Replace `CURRENT_SESSION.md` lines 1–13

Before:

```markdown
# Current Session

**Program:** Technical Sharpness Track

**Career direction:** Staff/Lead Data Engineer with strong AI systems capability, progressing toward AI/Data Architecture.

**Immediate goal:** Begin interviewing/applying within approximately one month.

**Current focus:** Week 1 — Build It Correctly: initial enterprise warehouse design and distributed execution.

**Next:** Technical Sharpness Day 1 — define warehouse grain and trace a realistic SQL/Oracle-shaped workload into distributed Spark execution.

**Parallel program:** `enterprise-ai-architecture-playbook` continues independently as the Architecture Judgment track.
```

After:

```markdown
# Current Session

## Program

Technical Sharpness Track — durable technical companion to `enterprise-ai-architecture-playbook`.

## Career direction and timing

Staff/Lead Data Engineer with strong AI systems capability, progressing toward AI/Data Architecture. Begin applying/interviewing by approximately the end of Week 4.

## Current week/day

Week 1, Day 1 — SQL/Oracle Execution -> Distributed Spark Execution.

## Status

Prepared; lesson not started.

## Concepts completed

- Repository learning model and evidence discipline established.

## Coding completed

None yet.

## Experiments completed

None yet.

## Measured evidence

None yet. Do not infer results from planned experiments.

## Unresolved questions

- Which parts of Day 1 are supported in the current Databricks Free Edition workspace?
- What small reproducible dataset should establish the initial baseline?

## Enterprise-project state

Conceptual source domains and Bronze/Silver/Gold flow exist. Grain, physical model, datasets, and pipelines are not yet implemented.

## Interview gaps discovered

None recorded yet.

## Artifacts created

- Repository guidelines, challenge catalog, roadmap, experiment standard, and Day 1 proposal.

## Next lesson

Begin Day 1 from the existing SQL/Oracle mental model. Predict physical execution and network boundaries before writing PySpark.

## Read before resuming

1. `RESUME_PROTOCOL.md`
2. `LEARNING_GUIDELINES.md`
3. `CODING_PRACTICE_GUIDELINES.md`
4. `ROADMAP.md`
5. `foundations/sql-to-distributed-systems/README.md`
6. `enterprise-challenges/README.md`
7. `ARCHITECTURE_LAB_BRIDGE.md`

## Parallel program

`enterprise-ai-architecture-playbook` continues independently as the Architecture Judgment track.
```

### 6. Replace `foundations/sql-to-distributed-systems/README.md` lines 1–36

Before:

```markdown
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
```

After:

```markdown
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
```

### 7. Replace `enterprise-challenges/README.md` lines 5–26

Preserve lines 1–3. Before:

```markdown
## Sequence

1. **Initial Warehouse Design** — requirements, grain, facts, dimensions, normalization versus dimensional models, and Bronze/Silver/Gold responsibilities.
2. **Multiple Source Systems** — contracts, schema differences, metadata-driven ingestion, reconciliation, and ownership.
3. **Hundreds of Millions of Rows** — distributed scans, partitions, shuffle, joins, memory, network, and layout using economical measured experiments plus labeled scale reasoning.
4. **Full Reload Becomes Too Expensive** — watermarks, CDC, idempotency, MERGE, and inserts/updates/deletes.
5. **Customer/Account History** — SCD Types 1/2, temporal correctness, and late dimension changes.
6. **Late-Arriving Transactions** — event versus processing time, correction, reconciliation, and replay.
7. **Duplicate Deliveries** — keys, deduplication, idempotency, and honest exactly-once guarantees.
8. **Schema Evolution** — additive/breaking change, contracts, compatibility, and blast radius.
9. **Bad Data** — validation, quarantine, observability, reconciliation, and ownership.
10. **Join Skew** — plans, imbalance, AQE, broadcast, and justified salting.
11. **Small Files** — metadata overhead, compaction, write patterns, read amplification, and layout.
12. **Large Backfill** — isolated replay, capacity, idempotency, recovery, and cost without destabilizing normal work.
13. **Multi-Team Governance** — catalogs, schemas, ownership, privileges, service identities, least privilege, lineage, and domains.
14. **Sensitive Data** — access boundaries, masking/filtering concepts where supported, auditability, and responsibility.
15. **Pipeline Failure** — orchestration, retries, dependencies, recovery, backfills, idempotency, alerts, and evidence.
16. **Transformation Sprawl** — dbt organization, SQL tests, dependencies, docs, lineage, and Spark/dbt boundaries.
17. **Dev/Test/Prod** — isolation, CI/CD design, catalog/schema strategy, configuration, test data, and permissions.
18. **Enterprise Data for AI** — governed authoritative data, metadata, authorization, lineage, evaluation, and data-quality effects on AI correctness.

Do not implement every challenge at initialization. Create a challenge directory only when work begins, using the experiment and debugging standards.
```

After:

```markdown
## Sequence

1. Initial warehouse design.
2. Multiple heterogeneous sources.
3. Hundreds of millions of rows.
4. Full reload becomes too expensive.
5. Inserts, updates, and deletes.
6. SCD Types 1 and 2.
7. Late-arriving facts and dimensions.
8. Duplicate source deliveries.
9. Idempotency.
10. Schema evolution.
11. Bad-data quarantine.
12. Data reconciliation.
13. Join skew.
14. Excessive shuffle.
15. Small-file problems.
16. Poor partitioning and data layout.
17. Memory and spill problems.
18. Large historical backfills.
19. Pipeline failures.
20. Retry and replay correctness.
21. Transformation sprawl.
22. Multi-team governance.
23. Sensitive-data access.
24. Dev/test/prod separation.
25. Cost/performance trade-offs.
26. Governed enterprise data for AI.

Technologies are introduced only when these problems require them. Create a challenge directory only when work begins, using the experiment, case-study, and debugging standards.
```

### 8. Add `DAILY_LESSON_TEMPLATE.md`

New file; no prior lines. Include these exact sections:

```markdown
# Daily Lesson Template

## Metadata

- Week/day:
- Enterprise challenge:
- Capability classification:
- Status: not started

## 1. Problem
## 2. Refresh
## 3. Internals
## 4. Modern Implementation
## 5. Industry Guidance
## 6. Industry Case Study
## 7. Learner Decision
## 8. Coding Lab
## 9. Experiment
## 10. Measurement
## 11. Break It
## 12. Explain the Result
## 13. Generalize
## 14. Interview Explanation

- Short conceptual:
- Detailed technical:
- Production debugging:

## 15. Architecture Bridge

What architecture decision am I now better equipped to make?

## 16. Reflection

What changed in my mental model?
```

### 9. Add `industry-case-studies/README.md`

New file; no prior lines.

```markdown
# Industry Case Studies

Organize cases by engineering problem, not company. Add a problem directory only when a lesson needs a relevant case; do not create company fan pages or empty category scaffolding.

## Case template

- Engineering problem:
- Company:
- Original source URL:
- Publication date:
- Reported scale:
- Constraints:
- Architecture:
- Why it was chosen:
- Trade-offs:
- Operational consequences:
- Company-specific elements:
- Generalized principle:
- What did not generalize:
- Relevance to our enterprise lab:

Prefer original engineering blogs, papers, conference talks, or official technical publications. Never invent scale, architecture, or outcomes. A case is evidence of one response under particular constraints, not an architecture prescription.

Expected problem categories include large-scale processing, skew, CDC, orchestration, data quality, table formats, governance, streaming, and backfills, created only as evidence is added.
```

### 10. Add `REFERENCES.md`

New file; no prior lines.

```markdown
# Learning References

References support labs; they are not prerequisites to read cover-to-cover. Map selected chapters or pages to the day that needs them.

## Durable foundations

- Martin Kleppmann, *Designing Data-Intensive Applications* — storage, replication, partitioning, transactions, batch, streams, and distributed-systems reasoning.
- Bill Chambers and Matei Zaharia, *Spark: The Definitive Guide* — conceptual Spark foundations; validate version-sensitive behavior against current Spark documentation.
- Joe Reis and Matt Housley, *Fundamentals of Data Engineering* — lifecycle and architecture perspective.

## Current primary documentation

- [Apache Spark documentation](https://spark.apache.org/documentation/)
- [Databricks documentation](https://docs.databricks.com/)
- [Delta Lake documentation](https://docs.delta.io/)
- [Unity Catalog documentation](https://docs.databricks.com/aws/en/data-governance/unity-catalog/)
- [Apache Airflow documentation](https://airflow.apache.org/docs/)
- [dbt documentation](https://docs.getdbt.com/)
- [Apache Iceberg documentation](https://iceberg.apache.org/docs/latest/)
- [Snowflake documentation](https://docs.snowflake.com/)

Current official documentation or specifications win for version-sensitive behavior. Record the version/date consulted during a lesson.

## Industry engineering sources

Add high-quality original sources only when a lesson needs them. Store structured notes under `industry-case-studies/`; do not initialize this section with random blog links.

## Evidence hierarchy

Durable concept builds the mental model; official documentation establishes current behavior; an industry case shows one organization's response; our experiment supplies evidence for our workload; an architecture decision combines requirements, evidence, and constraints.
```

Official documentation destinations were checked against primary sites during planning on 2026-08-15. Do not pin transient product versions in this initialization.

### 11. Add `RESUME_PROTOCOL.md`

New file; no prior lines.

```markdown
# New-Session Resume Protocol

Committed GitHub state is the source of truth. Conversation memory may supplement it but must never silently override it.

## Read in order

1. `CURRENT_SESSION.md`
2. `LEARNING_GUIDELINES.md`
3. `CODING_PRACTICE_GUIDELINES.md`
4. `ROADMAP.md`
5. the current week's README/material
6. the current enterprise challenge
7. relevant experiment results
8. `ARCHITECTURE_LAB_BRIDGE.md`

## Resume response

Before continuing, state:

1. where the learner stopped;
2. completed versus incomplete work;
3. unresolved evidence and questions;
4. the next roadmap topic;
5. any repository inconsistency that must be resolved.

Continue without resetting the program. At the end of every meaningful session, update `CURRENT_SESSION.md` with completed concepts/code/experiments, measured evidence, unresolved questions, project state, interview gaps, artifacts, next lesson, and recommended resume files.
```

## Resulting tree additions

```text
DAILY_LESSON_TEMPLATE.md
REFERENCES.md
RESUME_PROTOCOL.md
industry-case-studies/
  README.md
```

No files or directories are deleted. `ARCHITECTURE_LAB_BRIDGE.md` remains unchanged because it already contains the required two-track distinction and exact bridge loop.

## Review, commit, and PR behavior

Before implementation commit:

1. Re-read the current branch and both prior initialization prompts.
2. Confirm all 56 numbered days are visible exactly once.
3. Confirm Week 6 is entirely Unity Catalog/governance.
4. Confirm Weeks 1–4 support interviewing and Weeks 5–8 deepen Staff/Architect scope.
5. Confirm the daily template contains all 16 sections.
6. Confirm the resume protocol and current session can restart from repository state alone.
7. Confirm no benchmark or company fact is invented.
8. Confirm all documentation links are primary official destinations.
9. Run `git diff --check` and inspect the complete diff.
10. Show the user the tree, roadmap summary, changed-file list, conflicts, assumptions, and Day 1 starting point before committing.

After user approval, commit with `docs: establish eight-week technical sharpness roadmap`, push the existing feature branch, and update the existing draft PR rather than opening a duplicate PR.

## Assumptions

- The existing draft PR remains the publication target.
- The eight-week plan supersedes the four-week plan while retaining the end-of-Week-4 interview checkpoint.
- Industry-case directories remain uncreated until a sourced case exists; the README documents expected categories.
- Day 1 remains a prepared prompt, not a completed lesson or generated solution.
