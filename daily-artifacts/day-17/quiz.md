# Day 17 Architect/Staff Challenge — Learner Reasoning

- Sequence status: COMPLETED EARLY / OUT OF SEQUENCE
- Implementation: DEFERRED / NOT RUN

## Business outcome

I first establish the producer and authoritative ordering field. The outcome is one current state per customer reflecting the latest committed operational-source change.

## Correctness

I deduplicate each batch to one row per `customer_id` by highest `source_sequence`, quarantine equal-sequence/different-payload violations, then require `source.source_sequence > target.last_source_sequence`. Lower is stale and equal is a retry.

I retain minimal delete tombstones to block resurrection. A newer active event is ordered by sequence but accepted or rejected by reactivation policy. I distinguish last seen, applied, and rejected sequence and do not advance applied state for rejection.

Complete after-images may be independent; partial changes can depend on rejected history, so I isolate only that key and reconcile/replay it.

## Performance and layout

I separate source deduplication, target scan, rewrite, and commit. High scan breadth suggests testing improved `customer_id` locality—not high-cardinality partitioning or an unproven guarantee. I validate correctness and representative scan evidence.

I distinguish broad update footprint from write amplification: the lesson assumptions imply about 250 MB logical change versus 307 GB rewritten, roughly 1,228×. No-op filtering reduces rewrites but can discard an ordering boundary.

## Concurrency and SLA

A conflicting transaction fails atomically and the complete deterministic MERGE retries against the latest snapshot. I first characterize logical versus physical contention. Because CDC has the tighter SLA, I prioritize it and run resumable deterministic backfill chunks sized to fit the measured safe window. Seven minutes is the supplied scenario calculation, not repository evidence.

## Stop condition

Stop when both business SLAs are measurably satisfied; monitor conflicts, retries, headroom, progress, scanning, rewriting, and small files, with explicit reopen conditions.
