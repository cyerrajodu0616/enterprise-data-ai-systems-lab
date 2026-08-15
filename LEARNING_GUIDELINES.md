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
