# Learning Guidelines

The learner is an experienced data engineer refreshing and extending technical depth. The unit of learning is a difficult enterprise problem, not a product feature.

## Three-layer learning system

- **Technical Fundamentals:** learn and practice the mechanism.
- **Experiments and Evidence:** predict, run, observe, explain, and generalize a technical hypothesis.
- **Forward-Deployed Builds:** discover an ambiguous customer problem, define measurable success, build the simplest viable system, integrate and break it, evaluate it, and prepare it for production constraints.

Forward-Deployed Builds must begin with an intentionally incomplete request. Classify every material statement as **Known**, **Assumption**, **Open Question**, or **Hypothesis**. Do not reveal a final architecture before learner discovery and alternatives analysis.

Before adding major technology, ask: **What is the simplest solution that satisfies the business requirement?** Consider SQL, an API, deterministic logic, full-text or existing enterprise search, and a simple LLM call before adding RAG, vectors, agents, MCP, multiple models, queues, Kubernetes, or other complexity.

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

## Forward-deployed evidence

For every significant build use `Predict -> Run -> Observe -> Explain -> Generalize` for failure experiments. Separate:

- **System correctness:** deterministic behavior, integration contracts, security, reliability, and operational correctness.
- **Model quality:** structured-output validity, retrieval and answer quality, tool selection, hallucination/failure classification, and human review where needed.
- **Business outcome:** whether the system improves the explicitly defined customer success metric.

Never infer business ROI from a technically successful prototype.
