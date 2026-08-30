# Forward-Deployed Builds

## Purpose

Forward-Deployed Builds develop the ability to take an ambiguous enterprise/customer problem through discovery, requirements, architecture alternatives, implementation, integration, failure testing, evaluation, observability, governance, cost/latency analysis, productionization, measurement, and generalization.

They complement Technical Fundamentals and Experiments and Evidence. They also generate implementation evidence that can be transferred to `enterprise-ai-architecture-playbook` without silently changing architecture decisions there.

## Distinction

- A **coding challenge** tests implementation ability.
- An **experiment** tests a technical hypothesis.
- A **Forward-Deployed Build** tests whether we can deliver a production-oriented system for an ambiguous customer problem with measurable success and explicit constraints.

## Learning loop

`Customer Problem -> Discovery -> Known / Assumption / Open Question / Hypothesis -> Business Success Metric -> Simplest Viable Solution -> Alternatives -> Architecture -> Implementation -> Integration -> Failure Testing -> AI Evaluation -> Observability -> Security/Governance -> Cost/Latency -> Productionization -> Measurement -> Generalization -> Architecture Bridge`

The learner reasons first. Do not provide the final architecture or complete implementation before discovery, alternatives, and a learner proposal.

## Build progression

### Build 1 — Enterprise Data/API Service

Start after Week 2/Day 14. Solve a messy enterprise-data problem without AI using production Python, typing, project structure, FastAPI/REST where justified, SQL, validation, tests, errors, retries/timeouts, configuration, logging, Docker, and latency measurement. Prove that not every customer problem needs AI.

### Build 2 — AI-Assisted Enterprise Query

Start after Week 4 and only after a non-AI baseline exists. Add an LLM where a testable value hypothesis justifies it. Practice structured outputs, tool calling, governed SQL/data access, authorization, evaluation data, hallucination testing, latency, token usage, and approximate cost. Compare against the non-AI baseline.

### Build 3 — Enterprise Knowledge Assistant

Start during Week 8 after Day 51. Introduce unstructured information and compare direct document access, keyword/full-text search, long context, and RAG. Add embeddings, vector retrieval, hybrid search, or reranking only when requirements or evidence justify them. Measure retrieval quality, answer correctness, latency, token use, and operational complexity.

### Build 4 — Enterprise Agent Workflow

Start after Week 8. Introduce multiple tools, workflow state, MCP where justified, human approval, retries, idempotency, recovery, audit trails, and evaluation. Deliberately test tool, model, authorization, and duplicate-action failures.

### Build 5 — Production Deployment

Productionize one previous build according to explicit deployment requirements. Introduce cloud deployment, CI/CD, secrets, IAM, OAuth/OIDC, networking, queues, caching, metrics, tracing/OpenTelemetry, load tests, scaling, runbooks, incident scenarios, and—only if justified—Kubernetes or Terraform fundamentals.

### Build 6 — Ambiguous Customer Challenge

Receive only a realistic customer scenario. Lead discovery, classify unknowns, define success, propose alternatives, select and build the simplest viable solution, integrate, measure, harden, and defend it as an FDE interview/customer engagement.

## Customer and simplicity rules

Every build starts with an incomplete customer request. Never invent scale, QPS, document count, latency, accuracy, infrastructure, security, ROI, or cost. Classify claims as **Known**, **Assumption**, **Open Question**, or **Hypothesis**.

Before complex technology, test whether SQL, an API, deterministic rules, full-text/existing enterprise search, or a simple LLM call satisfies the requirement.

## Build, break, measure

Before each failure test ask what should happen, why, and what evidence would confirm or refute it. Then use `Predict -> Run -> Observe -> Explain -> Generalize` for database/API/model timeouts, malformed responses, duplicates, stale data, partial tool failures, rate limits, hallucinations, retrieval misses, authorization failures, duplicate agent actions, restarts, and unavailable dependencies as applicable.

## Evaluation

For AI builds distinguish system correctness, model quality, and business outcomes. Use golden datasets/expected outputs where justified and evaluate structured validity, retrieval, answer correctness, tool selection, hallucination/failure classes, latency, tokens, approximate cost, and human judgment where necessary.

## Completion criteria

A build is complete only when it includes discovery and classification, a business success metric, simplicity test and alternatives, learner-proposed architecture, working tested implementation, integration contracts, deliberate failure evidence, applicable AI evaluation, observability, security/governance, cost/latency evidence, production/runbook concerns, findings, interview reasoning, and an Architecture Bridge. Unknown or unexecuted items must be explicit.
