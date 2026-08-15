# Initialize the Enterprise Data & AI Systems Lab

## Feature context

The repository currently contains only `README.md` with the single line `# enterprise-data-ai-systems-lab` (line 1) and commit `16dcb35 Initial commit`. It needs to become the Technical Sharpness companion to `enterprise-ai-architecture-playbook`: a coherent, experiment-driven learning system for an experienced Senior/Lead Data Engineer preparing for Staff/Principal Data and AI/Data Architecture interviews in approximately one month.

The repository must emphasize first-principles reasoning, manual coding fluency, realistic enterprise data-platform work, measured evidence, Databricks/Delta Lake/Unity Catalog depth, and governed AI integration. It must not become a bootcamp, certification notebook, disconnected tutorial collection, or source of invented benchmark results.

## Exact changes

### 1. Replace `README.md` line 1

Before:

```markdown
# enterprise-data-ai-systems-lab
```

After:

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

### 2. Add `LEARNING_GUIDELINES.md`

New file; no prior lines.

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

### 3. Add `CODING_PRACTICE_GUIDELINES.md`

New file; no prior lines.

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

### 4. Add `ARCHITECTURE_LAB_BRIDGE.md`

New file; no prior lines.

```markdown
# Architecture ↔ Lab Bridge

The two repositories have distinct responsibilities.

`enterprise-ai-architecture-playbook` asks: Why? What business outcome and requirements matter? What architecture, trade-offs, TCO, and risk follow? What evidence would change the decision?

`enterprise-data-ai-systems-lab` asks: How does the mechanism work internally? Can it be implemented? What happens under load and failure? What does measurement show? What is the technical cost? Does evidence support the architectural assumption?

Use this loop:

`Architecture question -> technical hypothesis -> experiment -> evidence -> architectural refinement`

For each bridge item, record:

- architecture question and decision at risk;
- testable technical hypothesis;
- experiment link and controlled variables;
- observed evidence, including limitations;
- effect on performance, cost, governance, security, and operations;
- whether the architecture decision is retained, refined, or rejected.
```

### 5. Add `ROADMAP.md`

New file; no prior lines.

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

### 6. Add `CURRENT_SESSION.md`

New file; no prior lines.

```markdown
# Current Session

**Program:** Technical Sharpness Track

**Career direction:** Staff/Lead Data Engineer with strong AI systems capability, progressing toward AI/Data Architecture.

**Immediate goal:** Begin interviewing/applying within approximately one month.

**Current focus:** Week 1 — distributed systems mental-model and coding refresh.

**Next:** Technical Sharpness Day 1 — From SQL/Oracle Execution to Distributed Spark Execution.

**Parallel program:** `enterprise-ai-architecture-playbook` continues independently as the Architecture Judgment track.
```

### 7. Add `foundations/sql-to-distributed-systems/README.md`

New file; no prior lines.

```markdown
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

### 8. Add `foundations/distributed-systems-mental-model/README.md`

New file; no prior lines.

```markdown
# Distributed Systems Mental Model

Build explanations around physical work: where bytes live, where computation runs, what crosses the network, what is serialized, which metadata is consulted, how parallelism is bounded, and what is retried after failure.

Use this area to connect scans, partitions, tasks, stages, shuffle, joins, spill, skew, lazy evaluation, Catalyst, Adaptive Query Execution, and driver/executor responsibilities. Every note must include a failure boundary and an experiment that could challenge the mental model.
```

### 9. Add `enterprise-data-platform/README.md`

New file; no prior lines.

```markdown
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

### 10. Add `databricks/README.md`

New file; no prior lines.

```markdown
# Databricks Track

Databricks is the primary first-phase platform. Study mechanisms before commands.

- `spark-internals/`: driver/executor model, partitions, tasks, stages, lazy evaluation, shuffle, plans, Catalyst, AQE, memory, spill, skew, and joins.
- `delta-lake/`: transactions, enforcement/evolution, MERGE, updates/deletes, snapshots/versioning, time travel, change patterns, layout, concurrency, and reproducibility.
- `performance/`: controlled tests of scan, layout, shuffle, join, skew, caching, UDF, and repartition choices.
- `cdc-incremental/`: watermarks, CDC, inserts/updates/deletes, late events, idempotency, replay, ordering, and schema changes.
- `unity-catalog/`: centralized governance, hierarchy, principals, privileges, ownership, lineage, discovery, governed data and files, jobs, environments, sharing, and AI implications.
- `governance/`: policy design, operational ownership, auditability, classification, privilege sprawl, incorrect grants, and lineage limitations.
```

### 11. Add `databricks/unity-catalog/README.md`

New file; no prior lines.

```markdown
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

### 12. Add `experiments/README.md`

New file; no prior lines.

```markdown
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

### 13. Add `ai-integration/README.md`

New file; no prior lines.

```markdown
# Governed Enterprise Data for AI

This track tests how enterprise data can serve AI systems through structured SQL/API access and document/knowledge retrieval. It connects data quality to AI correctness, metadata and authorization to context construction, lineage to auditability, and evaluation datasets to measurable behavior.

Future experiments should combine structured and unstructured context, enforce consumer authorization, test retrieval and answer quality, and measure AI-related cost. Use the same enterprise platform so the evidence can refine decisions in `enterprise-ai-architecture-playbook`.
```

### 14. Add `snowflake/comparative-learning/README.md`

New file; no prior lines.

```markdown
# Snowflake Comparative Learning

Begin this track after the initial Databricks phase. Ask: **How does Snowflake solve the same business and data-engineering problem differently?**

Compare compute/storage separation, workload isolation, pruning and organization, concurrency, incremental transformations, governance, cost model, operational abstraction, SQL-centric engineering, and platform-managed optimization. Evaluate by workload, organizational capability, cost, governance, operations, and business requirement—not a generic “which is better?” verdict.
```

### 15. Add `interview-journal/README.md`

New file; no prior lines.

```markdown
# Interview Journal

Let actual interview evidence evolve the study plan. Organize entries with topic tags for SQL, Python, Spark, distributed systems, Databricks, Unity Catalog, data modeling, system design, AI/data architecture, and behavioral/leadership.

## Entry template

- Date and role/company context:
- Topic tags:
- Question:
- Initial answer:
- Missing knowledge:
- Improved answer:
- Technical lesson triggered:
- Architecture lesson triggered:
- Practice or experiment to schedule:
```

### 16. Add purposeful `.gitkeep` files only for planned artifact directories

New files; no prior lines. Each file should be empty. Add these exact paths so the requested learning areas exist without unnecessary placeholder READMEs:

```text
coding/sql/.gitkeep
coding/python/.gitkeep
coding/pyspark/.gitkeep
enterprise-data-platform/requirements/.gitkeep
enterprise-data-platform/source-systems/.gitkeep
enterprise-data-platform/data-model/.gitkeep
enterprise-data-platform/ingestion/.gitkeep
enterprise-data-platform/bronze/.gitkeep
enterprise-data-platform/silver/.gitkeep
enterprise-data-platform/gold/.gitkeep
enterprise-data-platform/quality/.gitkeep
enterprise-data-platform/operations/.gitkeep
databricks/spark-internals/.gitkeep
databricks/delta-lake/.gitkeep
databricks/performance/.gitkeep
databricks/cdc-incremental/.gitkeep
databricks/governance/.gitkeep
experiments/joins/.gitkeep
experiments/partitioning/.gitkeep
experiments/skew/.gitkeep
experiments/files/.gitkeep
experiments/incremental-processing/.gitkeep
experiments/udf-performance/.gitkeep
ai-integration/structured-access/.gitkeep
ai-integration/retrieval/.gitkeep
ai-integration/evaluation/.gitkeep
ai-integration/governance/.gitkeep
docs/diagrams/.gitkeep
docs/references/.gitkeep
```

## Gotchas and constraints

- Do not add benchmark numbers or imply any experiment has run.
- Do not pre-solve the Day 1 exercise; prepare its scenario, questions, and deliverables.
- Keep the architecture repository focused on decisions and this repository focused on mechanisms, implementation, measurement, and failure behavior.
- Keep coding practice first-class and explicitly preserve manual practice.
- Databricks is primary for month one; Snowflake is a later comparison.
- Unity Catalog must include organizational and operational limits, not only product features.
- Empty `.gitkeep` files are deliberate structure markers; do not add dozens of empty READMEs.
- Do not add generated datasets, dependencies, infrastructure claims, or platform-specific commands during initialization.

## Verification before commit

1. Run `find . -path './.git' -prune -o -type f -print | sort` and compare the output with the paths above.
2. Run `rg -n "bootcamp|HealthSure|benchmark|Unity Catalog|Learning Mode|Delivery Mode|AI-augmented|Day 1|four-week|Week 1" --glob '*.md'` and inspect every result in context.
3. Confirm every performance record is a hypothesis/template and no result is claimed.
4. Confirm all required major areas exist and no purposeless placeholder documents were added.
5. Run `git diff --check`.
6. Run `git status --short` and ensure only initialization files are included.
7. Review the entire diff.

After verification, stage only the initialization paths and commit with:

```text
chore: initialize enterprise data and AI systems lab
```

Before committing, report the proposed directory tree, key files, four-week roadmap summary, and assumptions to the user as requested.

## Confirmed assumptions

- The fictional enterprise remains intentionally unnamed so its domain can evolve without colliding with HealthSure or the architecture playbook.
- Repository initialization prepares Day 1 but does not provide its completed solution.
- Platform access, runtime versions, cloud, cluster sizing, data volumes, and benchmark outcomes are intentionally unspecified until observed.
- Directories that have no meaningful introductory content are represented by `.gitkeep`; substantive READMEs exist only at learning-flow boundaries.
