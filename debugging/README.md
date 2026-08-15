# Broken-System Debugging

Use the diagnostic chain:

`Symptom -> evidence -> execution behavior -> root cause -> fix -> regression test`

Exercises should include a 5x Spark slowdown, a straggling task, unexpected join shuffle, duplicate incremental records, incorrect MERGE history, retry-driven duplicates, dbt row explosion, lost partition pruning, downstream schema breakage, lost service-principal access, and a backfill that corrupts current state.

Do not reveal the root cause before the learner inspects plans, logs, data shape, lineage, configuration, or test failures. Every resolved incident needs a regression test and an operational prevention note.
