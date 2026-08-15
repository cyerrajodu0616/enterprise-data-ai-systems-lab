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
