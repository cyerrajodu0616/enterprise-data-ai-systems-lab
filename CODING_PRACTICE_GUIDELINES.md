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
