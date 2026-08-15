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
