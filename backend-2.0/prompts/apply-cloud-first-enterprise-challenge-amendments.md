# Apply Cloud-First, Enterprise-Challenge Amendments

## Context

Commit `b96250c` initialized the lab correctly against the original request, but the amendment changes the primary organizing principle. The lab must now lead with difficult enterprise warehouse/lakehouse challenges rather than product curricula, operate as a cloud-first personal project with GitHub as the durable source of truth, use Databricks Free Edition only where supported, and add Airflow, dbt, and broken-system debugging explicitly.

Preserve the original strengths: internals, evidence, manual coding fluency, SQL/Python/PySpark, Databricks, Delta Lake, Unity Catalog, architecture bridge, and interview journal. Do not claim current Databricks Free Edition capabilities that have not been verified; use a capability ledger and mark items `verify in current environment`.

## Exact changes

### 1. Replace `README.md` lines 1–50

Before: use the exact `README.md` lines 1–50 snapshot in Appendix A.

After:

```markdown
# Enterprise Data & AI Systems Lab

This personal, cloud-first repository is the **Technical Sharpness** companion to `enterprise-ai-architecture-playbook`. The playbook develops architectural judgment; this lab develops implementation fluency, performance intuition, debugging skill, and experimental evidence.

It is for an experienced Senior/Lead Data Engineer rebuilding and extending Staff-level depth while preparing to interview within approximately one month. It is not a bootcamp, certification guide, technology checklist, or collection of disconnected tutorials.

## Primary learning model

Build an enterprise warehouse/lakehouse and progressively make it survive realistic enterprise problems:

`Operational Sources -> Ingestion -> Bronze/Raw -> Silver/Validated -> Gold/Business -> BI / API / AI`

Start with the business and engineering problem. Determine what breaks, why it breaks internally, which resource becomes constrained, the simplest credible response, how to test it, what complexity and cost it adds, what happens at 10x scale, and how another platform would approach it.

Technologies follow problems. Do not use Spark when SQL is sufficient, Airflow when a native schedule is enough, dbt merely because it exists, streaming when batch satisfies the requirement, CDC while full refresh remains acceptable, or complex partitioning without evidence.

## Cloud-first personal lab

GitHub is the durable source of truth for code, SQL, PySpark, Python, dbt models, Airflow DAGs, tests, configuration templates, architecture notes, experiment definitions/results, and interview notes. No workflow should depend on one workstation.

Databricks Free Edition is the initial execution environment where its verified capabilities are sufficient. Each challenge classifies work as **implement and test**, **partially simulate**, or **architecture/design only**. Do not add paid infrastructure to imitate enterprise scale; complexity and cost must earn their place.

## Engineering responsibilities

- Airflow coordinates work, dependencies, retries, schedules, and backfills; it does not become a container for transformation logic.
- dbt organizes SQL models, dependencies, tests, documentation, and SQL-oriented lineage.
- Spark/Databricks performs distributed computation and execution.
- Delta provides transactional table and storage semantics.
- Unity Catalog provides catalog, access, governance, discovery, and lineage capabilities where supported.

The choice among direct SQL, dbt, PySpark, and Databricks-native pipelines depends on workload, complexity, scale, team capability, testing, maintainability, operations, and cost.

## Coding and evidence

Manual Practice preserves independent SQL, Python, PySpark, debugging, and execution-plan fluency. AI-Assisted Engineering is allowed for larger delivery work, but generated code must be understood and tested, architecture decisions remain human-owned, and performance claims require measured evidence. The objective is **AI-augmented engineering capability, not AI dependency**.

Never invent benchmark results. Separate measured observations from scale projections and architecture reasoning.

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

### 2. Replace `LEARNING_GUIDELINES.md` lines 1–53

Before: use the exact `LEARNING_GUIDELINES.md` lines 1–53 snapshot in Appendix A.

After:

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

### 3. Replace `CODING_PRACTICE_GUIDELINES.md` lines 1–25

Before: use the exact `CODING_PRACTICE_GUIDELINES.md` lines 1–25 snapshot in Appendix A.

After:

```markdown
# Coding Practice Guidelines

This personal project develops strong AI-assisted engineering while preserving independent coding, debugging, and reasoning.

## Manual Practice

1. Read the enterprise problem before seeing a generated solution.
2. Write the core SQL, Python, or PySpark manually.
3. Read the execution plan and predict data movement.
4. Explain time complexity, memory, failure behavior, and tests.
5. Diagnose broken pipelines from evidence before requesting a fix.

Regularly work without AI assistance to remain ready for interviews and production debugging. Prioritize SQL, Python, PySpark, broken-pipeline repair, execution plans, and performance reasoning.

## AI-Assisted Engineering

Codex/Claude-style assistance is allowed for larger enterprise-project delivery. Understand generated code, add appropriate tests, explain important decisions, measure performance claims, and retain ownership of architecture.

## Practice domains

- **SQL:** complex joins, windows, CTEs, deduplication, incremental processing, SCD Types 1/2, temporal correctness, quality, aggregation, and plans.
- **Python:** data structures, generators, typing, modules, pytest, file/API handling, errors, concurrency concepts, memory efficiency, and maintainability.
- **PySpark:** transformations, joins, windows, partitions, repartition/coalesce, shuffle, skew, broadcast, persistence, built-ins versus UDFs, plans, incremental work, and failure diagnosis.

The objective is **AI-augmented engineering capability, not AI dependency**.
```

### 4. Replace `ROADMAP.md` lines 1–35

Before: use the exact `ROADMAP.md` lines 1–35 snapshot in Appendix A.

After:

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

### 5. Replace `CURRENT_SESSION.md` lines 9–11

Before:

```markdown
**Current focus:** Week 1 — distributed systems mental-model and coding refresh.

**Next:** Technical Sharpness Day 1 — From SQL/Oracle Execution to Distributed Spark Execution.
```

After:

```markdown
**Current focus:** Week 1 — Build It Correctly: initial enterprise warehouse design and distributed execution.

**Next:** Technical Sharpness Day 1 — define warehouse grain and trace a realistic SQL/Oracle-shaped workload into distributed Spark execution.
```

### 6. Replace `enterprise-data-platform/README.md` lines 1–20

Before: use the exact `enterprise-data-platform/README.md` lines 1–20 snapshot in Appendix A.

After:

```markdown
# Enterprise Warehouse/Lakehouse Project

Build one coherent fictional enterprise warehouse/lakehouse and progressively make it survive realistic enterprise problems.

## Sources and domains

- Operational database: customers, accounts, products, orders/transactions, payments, and status history.
- Files: vendor transactions, partner reference feeds, and historical bulk extracts.
- Events: application, customer activity, and transaction events.
- External API: reference or enrichment data.

`Operational Sources -> Ingestion -> Bronze/Raw -> Silver/Validated -> Gold/Business -> BI / API / AI`

## Modeling standard

Define business process and grain before tables. Use fact tables, dimensions, business and surrogate keys where justified, SCD Types 1/2, transaction/history data, and reference data. Explain normalization versus dimensional choices and layer responsibilities.

## Scale and evolution

Synthetic generators may create progressively larger datasets for distributed experiments, but large physical datasets are never required merely for appearance. Record measured results separately from projections. The challenge catalog introduces multiple sources, hundreds of millions of conceptual fact rows, reload limits, history, late and duplicate data, schema change, quality failures, skew, small files, backfills, governance, failures, transformation sprawl, environments, and AI access.

Before adding CDC ask: **Why CDC instead of batch, and which business requirement justifies the complexity?**
```

### 7. Replace `databricks/README.md` lines 1–10

Before: use the exact `databricks/README.md` lines 1–10 snapshot in Appendix A.

After:

```markdown
# Databricks Implementation Area

Databricks is the initial primary implementation platform, using Free Edition where verified capabilities are sufficient. This directory supports enterprise challenges; it is not the roadmap.

Maintain a capability ledger per challenge:

- **Implement and test** — supported and verified in the current environment.
- **Partially simulate** — a reduced experiment can test the core mechanism.
- **Architecture/design only** — enterprise behavior cannot be reproduced credibly or economically here.

Do not infer Free Edition features or add paid infrastructure for appearances. Verify current support before implementation.

- `spark-internals/`: execution evidence for partitions, stages, shuffle, joins, memory, spill, skew, Catalyst, and AQE.
- `delta-lake/`: transactional semantics, MERGE, changes, history, layout, and concurrency.
- `performance/`: challenge-driven performance experiments.
- `cdc-incremental/`: correctness under continuous change.
- `unity-catalog/` and `governance/`: problem-driven access, ownership, lineage, and operational governance.
```

### 8. Replace `databricks/unity-catalog/README.md` lines 1–18

Before: use the exact `databricks/unity-catalog/README.md` lines 1–18 snapshot in Appendix A.

After:

```markdown
# Unity Catalog: Problem-Driven Governance

Begin with access problems, not GRANT syntax:

- Finance can read aggregated financial data.
- A restricted team can access transaction-level data.
- Another domain can use behavioral data but not sensitive fields.
- Pipeline service identities can write only their assigned layers.
- An AI application can access only approved governed datasets.

Use these scenarios to study catalog/schema/table hierarchy, ownership, users/groups/service identities, privileges, least privilege, lineage, discovery, auditability, environment/domain design, and governed AI access. Classify each exercise by what the current environment can implement, simulate, or only design.

A governance product does not create good governance. Record policy ownership, grant approval and review, privilege-sprawl risk, incorrect grants, lineage limitations, operational processes, and organizational responsibility.
```

### 9. Replace `experiments/README.md` lines 1–31

Before: use the exact `experiments/README.md` lines 1–31 snapshot in Appendix A.

After:

```markdown
# Experiment Record

Copy this structure for performance or scalability experiments. Never invent measurements; use `not run` until execution.

## Problem
## Current design
## Hypothesis
## Why we expect the change to work internally
## Dataset
## Infrastructure/runtime
## Execution plan
## Measurements
## Result
## Explanation
## Trade-offs
## Operational impact
## Cost implication
## Where this technique stops working
## Generalization
## Architecture implication

Always distinguish measured observations from hypothetical 10x or enterprise-scale reasoning. Relevant evidence may include runtime, scan volume, shuffle bytes, task distribution, spill, file count, CPU/memory indicators, and measurable cost.
```

### 10. Replace `foundations/sql-to-distributed-systems/README.md` lines 1–26

Before: use the exact `foundations/sql-to-distributed-systems/README.md` lines 1–26 snapshot in Appendix A.

After:

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

### 11. Add `enterprise-challenges/README.md`

New file; no prior lines.

```markdown
# Enterprise Challenge Catalog

This is the primary learning sequence. Every challenge extends the same warehouse/lakehouse, starts from a business requirement, uses the simplest credible design, and introduces technology only when justified.

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

### 12. Add `orchestration/airflow/README.md`

New file; no prior lines.

```markdown
# Airflow Orchestration

Introduce Airflow when an enterprise challenge needs cross-system coordination, explicit dependencies, schedules, retries, parameters, backfills, failure handling, observability, dynamic workflows, or external Databricks job/pipeline orchestration.

**Airflow coordinates work; it should not become an uncontrolled container for business transformation logic.** Compare it with a simpler native scheduler before adoption.

Practice DAGs, task dependencies, retries, idempotency, backfills, parameters, recovery, monitoring, and the boundary between orchestration and transformation. Add runnable DAGs only when a challenge requires them.
```

### 13. Add `transformations/dbt/README.md`

New file; no prior lines.

```markdown
# dbt Transformation Engineering

Introduce dbt when SQL model sprawl creates a need for dependency management, tests, documentation, model organization, and SQL-oriented lineage. dbt is not the scheduler and not a universal transformation mandate.

Responsibility map:

`Airflow -> orchestration`

`dbt -> SQL transformation/model dependency/testing/documentation`

`Spark/Databricks -> distributed computation/execution`

`Delta -> transactional table/storage semantics`

`Unity Catalog -> governance/catalog/access/lineage capabilities`

Choose direct SQL, dbt, PySpark, or a Databricks-native pipeline based on workload, complexity, scale, team capability, testing, maintainability, operations, and cost.
```

### 14. Add `debugging/README.md`

New file; no prior lines.

```markdown
# Broken-System Debugging

Use the diagnostic chain:

`Symptom -> evidence -> execution behavior -> root cause -> fix -> regression test`

Exercises should include a 5x Spark slowdown, a straggling task, unexpected join shuffle, duplicate incremental records, incorrect MERGE history, retry-driven duplicates, dbt row explosion, lost partition pruning, downstream schema breakage, lost service-principal access, and a backfill that corrupts current state.

Do not reveal the root cause before the learner inspects plans, logs, data shape, lineage, configuration, or test failures. Every resolved incident needs a regression test and an operational prevention note.
```

## Revised tree

```text
README.md
LEARNING_GUIDELINES.md
CODING_PRACTICE_GUIDELINES.md
ARCHITECTURE_LAB_BRIDGE.md
ROADMAP.md
CURRENT_SESSION.md
enterprise-challenges/README.md
enterprise-data-platform/...
coding/{sql,python,pyspark}/
debugging/README.md
orchestration/airflow/README.md
transformations/dbt/README.md
databricks/{spark-internals,delta-lake,performance,cdc-incremental,unity-catalog,governance}/
experiments/...
ai-integration/...
snowflake/comparative-learning/
interview-journal/
docs/
```

## Significant changes from initialization

- Enterprise challenges become primary navigation; technology directories remain implementation references.
- GitHub/cloud-first persistence and Databricks Free Edition capability classification are explicit.
- The central project is explicitly a dimensional enterprise warehouse/lakehouse.
- Airflow, dbt, and debugging receive purposeful learning areas.
- The roadmap is organized as correctness, change, scale/governance, and production/AI readiness.
- Day 1 begins with requirements and grain before distributed execution.

## Verification before any commit

1. Re-read both attachment specifications and every changed file.
2. Run `git diff --check`.
3. Run `rg -n "technology checklist|GitHub|Free Edition|implement and test|partially simulate|architecture/design only|Airflow coordinates|dbt|Symptom -> evidence|Never invent|grain" --glob '*.md'`.
4. Confirm the revised tree contains no empty challenge directory collection.
5. Confirm original coding, internals, Databricks, Delta, Unity Catalog, architecture bridge, and interview requirements remain represented.
6. Confirm no current Free Edition capability is claimed without verification.
7. Show the user the revised tree, roadmap, challenge sequence, responsibility map, Day 1 proposal, and significant changes.
8. Do not commit until the user approves this reconciliation.

## Assumptions avoided

- No cloud provider, Databricks feature entitlement, runtime, cluster size, dbt adapter, or Airflow deployment model is selected.
- No performance result or enterprise-scale measurement is claimed.
- Existing experiment subdirectories remain because they map to concrete challenge evidence; new challenges remain catalog entries until started.

## Appendix A — Exact before snapshots

### `README.md` lines 1–50

```markdown
# Enterprise Data & AI Systems Lab

This repository is the **Technical Sharpness** companion to `enterprise-ai-architecture-playbook`. The playbook develops architectural judgment; this lab develops the implementation fluency, performance intuition, and experimental evidence needed to test that judgment.

It is designed for an experienced Senior/Lead Data Engineer rebuilding and extending Staff-level depth while preparing to interview within approximately one month. It is not a bootcamp, certification guide, or collection of disconnected tutorials.

## Outcomes

- Rebuild SQL, Python, and PySpark fluency through data/platform-engineering problems.
- Explain distributed execution from first principles: scans, partitions, stages, tasks, shuffle, joins, spill, skew, retries, and query plans.
- Build an evolving enterprise lakehouse from operational, file, event, and API sources through Bronze, Silver, Gold, and governed consumers.
- Develop hands-on Databricks, Delta Lake, CDC, data-quality, performance, cost, and Unity Catalog judgment.
- Connect traditional database knowledge to distributed systems without treating analogies as exact equivalences.
- Demonstrate how governed enterprise data supports reliable AI systems.

## How learning works

Every important mechanism starts with the problem it solves, a simple mental model, its internals, the physical bottleneck it changes, its trade-offs and failure limits, and an experiment that can prove or disprove the claim. Performance results belong in experiment records only after measurement; never invent them.

Coding has two modes. In **Learning Mode**, attempt the core implementation manually before asking AI to review it. In **Delivery Mode**, AI-assisted implementation is allowed, but generated code must be understood, important behavior must be tested, and architecture decisions remain the learner's responsibility. The objective is **AI-augmented engineering capability, not AI dependency**.

## Enterprise project

The lab evolves one fictional enterprise platform rather than a set of unrelated demos:

`Operational DB + Files + Events + External API -> Ingestion -> Bronze -> Silver -> Gold -> BI / API / AI`

The same platform introduces duplicate ingestion, malformed and late data, CDC inserts/updates/deletes, schema evolution, replay, backfills, SCD changes, skew, large joins, small files, concurrency, governance, lineage, access control, and cost trade-offs. Exercises progress from local data to larger distributed runs and enterprise-scale design reasoning.

## Primary platform and comparisons

Databricks is the first-month implementation platform. Spark internals, Delta Lake, incremental processing, performance engineering, and Unity Catalog are core—not optional—tracks. Snowflake is introduced later as a workload-based comparison: how it solves the same business problem differently in compute, organization, governance, concurrency, operations, and cost.

## Repository map

- `LEARNING_GUIDELINES.md` — the reasoning and evidence standard.
- `CODING_PRACTICE_GUIDELINES.md` — Learning Mode, Delivery Mode, and practice expectations.
- `ARCHITECTURE_LAB_BRIDGE.md` — the feedback loop between architecture and experiments.
- `ROADMAP.md` — the four-week intensive sequence.
- `CURRENT_SESSION.md` — the active focus and next lesson.
- `foundations/` — database-to-distributed analogies and distributed mental models.
- `coding/` — SQL, Python, and PySpark practice.
- `enterprise-data-platform/` — the evolving project and its lifecycle areas.
- `databricks/` — Spark, Delta, CDC, performance, governance, and Unity Catalog.
- `experiments/` — repeatable measurement records.
- `snowflake/` — later comparative learning.
- `ai-integration/` — governed structured access, retrieval, evaluation, and AI governance.
- `interview-journal/` — evidence-driven interview reflection.

Start with `ROADMAP.md`, `CURRENT_SESSION.md`, and the Day 1 lesson in `foundations/sql-to-distributed-systems/README.md`.
```

### `LEARNING_GUIDELINES.md` lines 1–53

```markdown
# Learning Guidelines

This lab rebuilds technical judgment, not API recall. For every important technology, pattern, or optimization, work through this sequence:

1. What problem existed before this mechanism?
2. What is the simplest useful mental model?
3. How does it work internally?
4. Which physical resource or bottleneck changes: CPU, memory, disk I/O, network, serialization, metadata, or parallelism?
5. Why should it perform better?
6. What trade-off does it introduce?
7. When does it stop working?
8. What older database or data-engineering concept does it resemble?
9. Where is that analogy inaccurate?
10. How can the principle transfer to another problem?
11. How can the claim be proven experimentally?

Never accept an unsupported statement such as “a broadcast join is faster.” Identify what data movement changes, the workload and size assumptions, executor-memory risk, the failure boundary, and the measurements needed to validate it.

## Evidence standard

- State a falsifiable hypothesis before running an experiment.
- Record data shape and size, platform/runtime, compute configuration, relevant settings, code or query version, and constraints.
- Capture runtime, scan volume, shuffle bytes, task distribution, spill, file count, CPU/memory indicators, and cost when measurable and relevant.
- Separate observations from explanations and architectural implications.
- Never invent results. Mark experiments `not run` until evidence exists.
- Preserve surprising or negative results; they often reveal the real boundary of a technique.

## Scale progression

Run the same conceptual workload at a small local scale, a medium scale, and a larger distributed scale when infrastructure permits. Then reason explicitly—without fabricating measurements—about changes required at 10 million, 600 million, and several billion rows.

## Analogy discipline

Traditional database knowledge is a starting point, not a translation table. Every comparison must state the conceptual similarity, architectural difference, effect of distributed compute, and point where the analogy breaks.

## Daily lesson pattern

1. Business or engineering problem
2. Existing mental model
3. New concept
4. Internals
5. Old-system analogy
6. Where the analogy breaks
7. Hands-on coding exercise
8. Performance hypothesis
9. Experiment
10. Measurements
11. Failure analysis
12. Cost implications
13. Operational implications
14. Generalization to another problem
15. Interview explanation
16. Reflection
```

### `CODING_PRACTICE_GUIDELINES.md` lines 1–25

```markdown
# Coding Practice Guidelines

Coding fluency is a first-class outcome. Practice should resemble production data/platform engineering rather than optimize only for puzzle solving.

## Learning Mode

1. Read the problem before seeing a full solution.
2. Implement the core SQL, Python, or PySpark logic manually.
3. Explain time complexity, memory implications, data movement, failure behavior, and testing strategy.
4. Use Codex or Claude Code afterward to review, find bugs, challenge complexity, suggest alternatives, explain performance, and propose tests.
5. Request a complete solution only when deliberately ending the manual attempt.

Periodically complete exercises without AI assistance to preserve interview, debugging, and whiteboard fluency.

## Delivery Mode

AI-assisted coding is allowed for larger project work. Review every generated change, test important components, and be able to explain the implementation and its failure modes. Do not delegate architecture decisions blindly.

## Practice domains

- **SQL:** complex joins, windows, CTEs, recursive reasoning where useful, deduplication, incremental processing, SCD Types 1 and 2, temporal queries, plans, quality checks, aggregation, and performance reasoning.
- **Python:** data structures, iterators/generators, typing, justified classes, modules, pytest, file/API processing, errors, concurrency concepts, memory-efficient processing, and maintainability.
- **PySpark:** DataFrame transformations, joins, windows, partitioning, repartition/coalesce, shuffle, skew, broadcast, persistence, built-ins versus UDFs, plans, incremental workloads, and debugging failures.

The policy is simple: **AI-augmented engineering capability, not AI dependency.**
```

### `ROADMAP.md` lines 1–35

```markdown
# Four-Week Technical Sharpness Roadmap

This is an intensive starting sequence, not the end of the lab. Each week combines manual coding, internals, experiments, project evolution, and interview articulation.

## Week 1 — Distributed Systems + Coding Refresh

Focus on SQL, Python, the Spark execution model, partitions, shuffle, joins, skew, plans, and the first Bronze-to-Gold project flow. Start with Day 1: **From SQL/Oracle Execution to Distributed Spark Execution**.

Outcome: rebuild coding fluency and a physical mental model for distributed data execution.

## Week 2 — Modern Databricks Data Platform

Focus on Delta Lake transactions and versioning, MERGE, schema change, incremental processing and CDC, deletes and late data, layout, quality, Unity Catalog, governance, performance, and cost.

Outcome: design, build, debug, govern, and explain a modern Databricks enterprise pipeline.

## Week 3 — Enterprise Data + AI Integration

Focus on governed structured access, document/evidence retrieval, evaluation datasets, data quality and AI correctness, metadata, authorization, lineage, security, and AI cost measurement.

Outcome: demonstrate Data + AI engineering grounded in governed enterprise data, not generic chatbot development.

## Week 4 — Staff Engineer Integration + Interviews

Focus on system design, scale evolution, performance diagnosis, data and AI/data architecture, SQL/Python/PySpark practice, debugging, cost, operations, leadership articulation, and interview simulation.

Outcome: be ready to interview for Staff/Lead Data Engineer, appropriate Principal Data Engineer, Staff Data/AI Engineer, AI/Data Platform, and Data & AI Architect roles.

## Weekly operating rhythm

- Begin with one architecture or business question.
- Attempt core coding manually in Learning Mode.
- Run or design a controlled experiment and record only measured evidence.
- Extend the same enterprise platform rather than start an unrelated tutorial.
- Finish with an interview explanation and update the interview journal.
```

### Remaining exact before snapshots

The following are copied verbatim from the current files and are short enough to verify directly:

```markdown
<!-- enterprise-data-platform/README.md lines 1–20 -->
# Enterprise Data Platform Project

Use one fictional enterprise across the whole lab.

## Sources and flow

- Operational database: customers, accounts, products, orders/transactions, payments, and status history.
- Files: vendor transactions, partner reference feeds, and historical bulk extracts.
- Events: application, customer activity, and transaction events.
- External API: reference or enrichment data.

`Sources -> Ingestion -> Raw/Bronze -> Validated/Silver -> Business/Gold -> BI / API / AI`

## Evolution

Introduce duplicate ingestion, late records, malformed data, schema evolution, CDC inserts/updates/deletes, idempotency, ordering, replay, backfills, SCD changes, quality failures, skew, large joins, small files, poor partitioning, expensive transformations, concurrency, regressions, lineage, access control, and cost trade-offs as explicit requirements—not random demos.

Before adding CDC, answer: **Why are we using CDC instead of batch, and what business requirement justifies the added complexity?**

Use the subdirectories for requirements, source systems, data model, ingestion, Bronze, Silver, Gold, quality, and operations artifacts only when a real exercise needs them.
```

```markdown
<!-- databricks/README.md lines 1–10 -->
# Databricks Track

Databricks is the primary first-phase platform. Study mechanisms before commands.

- `spark-internals/`: driver/executor model, partitions, tasks, stages, lazy evaluation, shuffle, plans, Catalyst, AQE, memory, spill, skew, and joins.
- `delta-lake/`: transactions, enforcement/evolution, MERGE, updates/deletes, snapshots/versioning, time travel, change patterns, layout, concurrency, and reproducibility.
- `performance/`: controlled tests of scan, layout, shuffle, join, skew, caching, UDF, and repartition choices.
- `cdc-incremental/`: watermarks, CDC, inserts/updates/deletes, late events, idempotency, replay, ordering, and schema changes.
- `unity-catalog/`: centralized governance, hierarchy, principals, privileges, ownership, lineage, discovery, governed data and files, jobs, environments, sharing, and AI implications.
- `governance/`: policy design, operational ownership, auditability, classification, privilege sprawl, incorrect grants, and lineage limitations.
```

```markdown
<!-- databricks/unity-catalog/README.md lines 1–18 -->
# Unity Catalog Learning Track

Study why centralized catalog and governance capabilities exist; metastore/catalog/schema/table hierarchy; managed and external data; users, groups, and service principals; grants, privileges, ownership, least privilege, workspace/data boundaries, lineage, discovery, governed tables/views/files, job identities, environment separation, auditability, classification/tagging where supported, cross-domain sharing, and AI-system access.

## Exercise sequence

1. Design logical catalogs for environments and domains.
2. Create schemas and governed tables.
3. Define human and service roles.
4. Implement least privilege.
5. Demonstrate allowed and denied access.
6. Trace transformation lineage and document its limits.
7. Design service-identity access.
8. Design dev/test/prod governance.
9. Model cross-domain sharing.
10. Explain governance effects on an AI application consuming enterprise data.

Unity Catalog does not automatically solve governance. Every exercise must identify ownership processes, policy authors, operational responsibility, incorrect-grant risk, privilege sprawl, lineage gaps, and organizational responsibilities.
```

```markdown
<!-- experiments/README.md lines 1–31 -->
# Experiment Standard

Each experiment compares a controlled choice and records evidence without invented results.

## Template

### Question and hypothesis

State what should happen, why, and what observation would disprove it.

### Setup

Record data size and shape, infrastructure, runtime, configuration, code/query revision, and constraints.

### Execution

Record exactly what ran and how repeatability was handled.

### Measurements

Record relevant runtime, scan volume, shuffle bytes, task distribution, spill, file count, CPU/memory indicators, and measurable cost. Use `not run` until executed.

### Explanation

Explain the observed behavior through physical work and note uncertainty.

### Architectural implication

State the production condition under which the result matters and where it may not generalize.

Initial comparison areas are broadcast versus shuffle join, good versus poor partitioning, pruning versus broad scans, small versus appropriately sized files, full versus incremental processing, skewed versus balanced joins, built-ins versus Python UDFs, justified cached reuse versus uncached reuse, and unnecessary versus controlled repartitioning.
```

```markdown
<!-- foundations/sql-to-distributed-systems/README.md lines 1–26 -->
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
```
