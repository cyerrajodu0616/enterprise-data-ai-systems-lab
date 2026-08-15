# Experiment Standard

Each experiment compares a controlled choice and records evidence without invented results.

## Template

### Question and hypothesis

State what should happen, why, and what observation would disprove it.

### Setup

Record data size and shape, infrastructure, runtime, configuration, code/query revision, and constraints.

### Execution

Record exactly what ran and how repeatability was handled.

### Measurements

Record relevant runtime, scan volume, shuffle bytes, task distribution, spill, file count, CPU/memory indicators, and measurable cost. Use `not run` until executed.

### Explanation

Explain the observed behavior through physical work and note uncertainty.

### Architectural implication

State the production condition under which the result matters and where it may not generalize.

Initial comparison areas are broadcast versus shuffle join, good versus poor partitioning, pruning versus broad scans, small versus appropriately sized files, full versus incremental processing, skewed versus balanced joins, built-ins versus Python UDFs, justified cached reuse versus uncached reuse, and unnecessary versus controlled repartitioning.
