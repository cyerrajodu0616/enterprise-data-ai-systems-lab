# Add the Forward-Deployed Builds Layer

## Context

The committed repository already has an eight-week/56-day fundamentals roadmap, controlled experiments, enterprise challenges, daily evidence packages, and an architecture bridge. Add a third practical layer without replacing or renumbering the roadmap.

Current learner state remains Week 1, Day 1 prepared but not complete. The uncommitted `daily-artifacts/day-01/` scaffold and `backend-2.0/prompts/complete-technical-sharpness-day-01.md` belong to the interrupted Day 1 task and must remain untouched and unstaged for this change.

## Files changed

- Modify `README.md`.
- Modify `LEARNING_GUIDELINES.md`.
- Modify `ROADMAP.md`.
- Modify `ARCHITECTURE_LAB_BRIDGE.md`.
- Add `forward-deployed-builds/README.md`.
- Add `forward-deployed-builds/BUILD_TEMPLATE.md`.
- Do not modify `CURRENT_SESSION.md`; adding documentation does not constitute learner progress.

## 1. Update `README.md`

### Insert after line 37

Before:

```markdown
Never invent benchmark results. Separate measured observations from scale projections and architecture reasoning.

## Repository map
```

After:

```markdown
Never invent benchmark results. Separate measured observations from scale projections and architecture reasoning.

## Three practical layers

1. **Technical Fundamentals** develop coding fluency, data-platform internals, and implementation judgment.
2. **Experiments and Evidence** test technical hypotheses through prediction, controlled execution, observation, and explanation.
3. **Forward-Deployed Builds** test whether an ambiguous customer problem can become a working, integrated, production-oriented system under explicit constraints.

The layers reinforce one another but are not interchangeable: a coding challenge tests implementation ability, an experiment tests a technical hypothesis, and a Forward-Deployed Build tests delivery of a measurable customer outcome.

## Repository map
```

### Insert in repository map after current line 50 (`daily-artifacts/`)

Before:

```markdown
- `daily-artifacts/` — committed end-of-day lessons, quizzes, implementations, evidence, and HTML recaps.
- `ai-integration/` — governed enterprise data for AI.
```

After:

```markdown
- `daily-artifacts/` — committed end-of-day lessons, quizzes, implementations, evidence, and HTML recaps.
- `forward-deployed-builds/` — discovery-to-production builds driven by ambiguous customer problems.
- `ai-integration/` — governed enterprise data for AI.
```

## 2. Update `LEARNING_GUIDELINES.md`

### Insert after line 3

Before:

```markdown
The learner is an experienced data engineer refreshing and extending technical depth. The unit of learning is a difficult enterprise problem, not a product feature.

## Learning sequence
```

After:

```markdown
The learner is an experienced data engineer refreshing and extending technical depth. The unit of learning is a difficult enterprise problem, not a product feature.

## Three-layer learning system

- **Technical Fundamentals:** learn and practice the mechanism.
- **Experiments and Evidence:** predict, run, observe, explain, and generalize a technical hypothesis.
- **Forward-Deployed Builds:** discover an ambiguous customer problem, define measurable success, build the simplest viable system, integrate and break it, evaluate it, and prepare it for production constraints.

Forward-Deployed Builds must begin with an intentionally incomplete request. Classify every material statement as **Known**, **Assumption**, **Open Question**, or **Hypothesis**. Do not reveal a final architecture before learner discovery and alternatives analysis.

Before adding major technology, ask: **What is the simplest solution that satisfies the business requirement?** Consider SQL, an API, deterministic logic, full-text or existing enterprise search, and a simple LLM call before adding RAG, vectors, agents, MCP, multiple models, queues, Kubernetes, or other complexity.

## Learning sequence
```

### Insert after current evidence hierarchy final sentence (line 68 before insertion)

Before:

```markdown
Do not confuse these evidence types.
```

After:

```markdown
Do not confuse these evidence types.

## Forward-deployed evidence

For every significant build use `Predict -> Run -> Observe -> Explain -> Generalize` for failure experiments. Separate:

- **System correctness:** deterministic behavior, integration contracts, security, reliability, and operational correctness.
- **Model quality:** structured-output validity, retrieval and answer quality, tool selection, hallucination/failure classification, and human review where needed.
- **Business outcome:** whether the system improves the explicitly defined customer success metric.

Never infer business ROI from a technically successful prototype.
```

## 3. Update `ROADMAP.md`

### Insert between line 159 and `## Roadmap deviations` at line 161

Before:

```markdown
End by committing a durable package under `daily-artifacts/day-XX/` containing the completed lesson, attempted quiz and reviewed answers, implementation and tests, experiment and measured results, and a self-contained `recap.html`. Follow `DAILY_ARTIFACT_GUIDELINES.md`; never fabricate results or publish solutions before the learner's attempt.

## Roadmap deviations
```

After:

```markdown
End by committing a durable package under `daily-artifacts/day-XX/` containing the completed lesson, attempted quiz and reviewed answers, implementation and tests, experiment and measured results, and a self-contained `recap.html`. Follow `DAILY_ARTIFACT_GUIDELINES.md`; never fabricate results or publish solutions before the learner's attempt.

## Forward-Deployed Build milestones

Forward-Deployed Builds consume the roadmap; they do not replace focused fundamentals days. See `forward-deployed-builds/README.md` for completion criteria and the full dependency map.

- **After Week 2:** Build 1 — Enterprise Data/API Service. Prerequisites: requirements, grain, source modeling, Bronze/Silver/Gold boundaries, SQL/Python practice, validation, and tests. Start only after Day 14 is reviewed.
- **After Week 4:** Build 2 — AI-Assisted Enterprise Query. Prerequisites: a non-AI service baseline, incremental correctness, execution/performance evidence, and an explicit value hypothesis for an LLM.
- **During Week 8 after Day 51:** Build 3 — Enterprise Knowledge Assistant. Evaluate direct access, full-text search, and long context before embeddings or RAG.
- **After Week 8:** Build 4 — Enterprise Agent Workflow, only when multiple tools and stateful coordination are justified.
- **After Build 4:** Build 5 — Production Deployment of one earlier system, driven by real deployment requirements rather than a DevOps checklist.
- **Capstone:** Build 6 — Ambiguous Customer Challenge. The learner receives the scenario, not the architecture, and must lead discovery through measurement and defense.

Each milestone reuses fundamentals, coding, experiments, and enterprise-project artifacts. Do not begin Build 1 while `CURRENT_SESSION.md` remains before Week 2 completion.

## Roadmap deviations
```

## 4. Update `ARCHITECTURE_LAB_BRIDGE.md`

### Append after line 20

Before:

```markdown
- whether the architecture decision is retained, refined, or rejected.
```

After:

```markdown
- whether the architecture decision is retained, refined, or rejected.

## Forward-Deployed Builds boundary

Forward-Deployed Builds own discovery artifacts, prototypes, implementations, integrations, failure observations, evaluations, measurements, and production-readiness evidence. They may reveal that an assumption is wrong or that an alternative deserves consideration.

The Architecture Playbook remains the source of truth for architecture decisions. A successful prototype or lab experiment does not automatically become an architecture decision. Transfer only the evidence, constraints, unknowns, and candidate implications for consideration through:

`Architecture Question -> Technical Hypothesis -> Lab Experiment or Build -> Evidence -> Architecture Refinement`
```

## 5. Add `forward-deployed-builds/README.md`

New file; no prior lines.

```markdown
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
```

## 6. Add `forward-deployed-builds/BUILD_TEMPLATE.md`

New file; no prior lines.

```markdown
# Forward-Deployed Build Template

## Metadata

- Build:
- Status: discovery
- Roadmap prerequisites:
- Capability classification:

## 1. Customer Problem
## 2. Discovery
## 3. Known
## 4. Assumptions
## 5. Open Questions
## 6. Hypotheses
## 7. Business Success Metric
## 8. Simplest Solution
## 9. Alternatives
## 10. Architecture
## 11. Implementation Plan
## 12. Build
## 13. Failure Experiments

For each: prediction, reason, confirming/refuting evidence, execution, observation, explanation, and generalization.

## 14. Measurements

Label unexecuted measurements `not run`; never replace them with estimates presented as observations.

## 15. AI Evaluation

Separate system correctness, model quality, and business outcome. Mark not applicable for non-AI builds with an explanation.

## 16. Security/Governance
## 17. Cost/Latency
## 18. Operational Concerns
## 19. Findings
## 20. Generalization
## 21. Interview Questions

- Why this architecture?
- Which simpler alternative was rejected, and why?
- What failed, and how was it measured?
- What changes at 10x load?
- How would cost be reduced?
- How would the system be secured and deployed into a customer environment?
- What changes under stricter latency or data-residency requirements?

## 22. Architecture Bridge

- What did implementation teach us?
- Which assumptions were wrong?
- What evidence was obtained?
- Which decisions might the evidence influence?
- What remains unknown?
- At what scale or constraint could the recommendation change?
- What should be transferred to the Architecture Playbook for consideration?

## 23. Reflection
```

## Verification

1. Confirm the existing 56-day headings and order are unchanged.
2. Confirm Build 1 is gated until after Day 14 and current Day 1 progress is preserved.
3. Confirm the README, guidelines, roadmap, bridge, overview, and template link to valid paths.
4. Confirm coding challenges, experiments, and builds remain distinct.
5. Confirm the Architecture Playbook owns decisions and this repo owns implementation evidence.
6. Confirm no customer scale, benchmark, cost, accuracy, infrastructure, or ROI is invented.
7. Confirm the learner must propose before receiving solutions.
8. Run `git diff --check` and inspect all changed files.
9. Show the user the final file changes and three-layer summary.
10. Do not commit or push until the user separately authorizes publication.

## Staging safety

The existing untracked Day 1 plan and `daily-artifacts/day-01/` are unrelated. Do not modify, delete, or stage them as part of this change.
