# Coding Practice Guidelines

This personal project develops strong AI-assisted engineering while preserving independent coding, debugging, and reasoning.

## Manual Practice Mode

1. Read the enterprise problem before seeing a generated solution.
2. Write the core SQL, Python, or PySpark manually.
3. Read the execution plan and predict data movement.
4. Explain time complexity, memory, failure behavior, and tests.
5. Diagnose broken pipelines from evidence before requesting a fix.

Regularly work without AI assistance to remain ready for interviews and production debugging. Prioritize SQL, Python, PySpark, broken-pipeline repair, execution plans, and performance reasoning.

## Stop, assess, then answer

Before proposing a code, configuration, or infrastructure change:

1. state the observed symptom;
2. separate known facts from assumptions and hypotheses;
3. identify missing evidence and how to collect it;
4. give a conditional recommendation;
5. state what would change the decision;
6. define validation.

Avoid reflexive prescriptions such as adding memory/executors, increasing partitions, broadcasting a “small” table, salting, deduplicating, or relying on an optimizer without evidence that distinguishes the underlying causes.

## AI-Assisted Engineering Mode

Codex/Claude-style assistance is allowed for larger enterprise-project delivery. Understand generated code, add appropriate tests, explain important decisions, measure performance claims, and retain ownership of architecture.

## Practice domains

- **SQL:** complex joins, windows, CTEs, deduplication, incremental processing, SCD Types 1/2, temporal correctness, quality, aggregation, and plans.
- **Python:** data structures, generators, typing, modules, pytest, file/API handling, errors, concurrency concepts, memory efficiency, and maintainability.
- **PySpark:** transformations, joins, windows, partitions, repartition/coalesce, shuffle, skew, broadcast, persistence, built-ins versus UDFs, plans, incremental work, and failure diagnosis.

The objective is **AI-augmented engineering capability, not AI dependency**.
