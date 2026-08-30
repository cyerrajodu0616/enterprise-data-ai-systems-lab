# Day 01 Experiment

- Status: DEFERRED / NOT RUN
- Problem: Distinguish predicted distributed execution from observed Spark behavior.
- Current design: Conceptual reasoning only; no executable Day 1 implementation exists.
- Hypotheses: Preserved as LAB-001 through LAB-005 in `../../LAB_BACKLOG.md`.
- Expected internal mechanisms: Narrow dependency locality, Exchange/shuffle for key redistribution, task waves under limited slots, hot-key skew, lineage-based recomputation, and duplicate side-effect risk under retry.
- Dataset: not created
- Infrastructure/runtime: not selected or verified
- Execution plan: not captured
- Measurements: not run

Predicted mechanisms are not observations. Execute each backlog item independently and preserve its original hypothesis before recording results.
