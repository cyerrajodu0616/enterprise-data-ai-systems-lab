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
