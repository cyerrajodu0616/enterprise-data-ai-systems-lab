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
- `industry-case-studies/` — source-backed cases organized by engineering problem.
- `ai-integration/` — governed enterprise data for AI.
- `snowflake/` — later workload-based comparison.
- `interview-journal/` — interview evidence and targeted follow-up.
- `DAILY_LESSON_TEMPLATE.md` — the reusable lesson structure.
- `REFERENCES.md` — durable foundations, current official documentation, and curated engineering sources.
- `RESUME_PROTOCOL.md` — deterministic continuation from a new session.

Start with `RESUME_PROTOCOL.md`, `CURRENT_SESSION.md`, `ROADMAP.md`, the current challenge, and the Day 1 proposal.
