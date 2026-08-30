# Architecture ↔ Lab Bridge

The two repositories have distinct responsibilities.

`enterprise-ai-architecture-playbook` asks: Why? What business outcome and requirements matter? What architecture, trade-offs, TCO, and risk follow? What evidence would change the decision?

`enterprise-data-ai-systems-lab` asks: How does the mechanism work internally? Can it be implemented? What happens under load and failure? What does measurement show? What is the technical cost? Does evidence support the architectural assumption?

Use this loop:

`Architecture question -> technical hypothesis -> experiment -> evidence -> architectural refinement`

For each bridge item, record:

- architecture question and decision at risk;
- testable technical hypothesis;
- experiment link and controlled variables;
- observed evidence, including limitations;
- effect on performance, cost, governance, security, and operations;
- whether the architecture decision is retained, refined, or rejected.

## Forward-Deployed Builds boundary

Forward-Deployed Builds own discovery artifacts, prototypes, implementations, integrations, failure observations, evaluations, measurements, and production-readiness evidence. They may reveal that an assumption is wrong or that an alternative deserves consideration.

The Architecture Playbook remains the source of truth for architecture decisions. A successful prototype or lab experiment does not automatically become an architecture decision. Transfer only the evidence, constraints, unknowns, and candidate implications for consideration through:

`Architecture Question -> Technical Hypothesis -> Lab Experiment or Build -> Evidence -> Architecture Refinement`
