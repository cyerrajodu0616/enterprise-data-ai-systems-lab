# Databricks Implementation Area

Databricks is the initial primary implementation platform, using Free Edition where verified capabilities are sufficient. This directory supports enterprise challenges; it is not the roadmap.

Maintain a capability ledger per challenge:

- **Implement and test** — supported and verified in the current environment.
- **Partially simulate** — a reduced experiment can test the core mechanism.
- **Architecture/design only** — enterprise behavior cannot be reproduced credibly or economically here.

Do not infer Free Edition features or add paid infrastructure for appearances. Verify current support before implementation.

- `spark-internals/`: execution evidence for partitions, stages, shuffle, joins, memory, spill, skew, Catalyst, and AQE.
- `delta-lake/`: transactional semantics, MERGE, changes, history, layout, and concurrency.
- `performance/`: challenge-driven performance experiments.
- `cdc-incremental/`: correctness under continuous change.
- `unity-catalog/` and `governance/`: problem-driven access, ownership, lineage, and operational governance.
