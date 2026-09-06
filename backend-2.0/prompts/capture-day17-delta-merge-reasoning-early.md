# Capture Day 17 Delta MERGE reasoning early, out of sequence

## Verified repository state and sequencing decision

The repository was fast-forwarded to `origin/main` commit `4b41422` before planning. The only pre-existing untracked file is `daily-artifacts/.DS_Store`; preserve it untouched and never stage it.

The user explicitly resolved the roadmap conflict by directing this lesson to Day 17 as an intentional early/out-of-sequence conceptual completion.

- `CURRENT_SESSION.md:13-15` records Day 3 complete and **Week 1 Day 4 — Aggregation at Scale** next.
- `CURRENT_SESSION.md:88-92` repeats Day 4 as the next lesson and states it has not started.
- `ROADMAP.md:21-23` defines Day 4 as Aggregation at Scale.
- `ROADMAP.md:51-53` defines Day 16 as CDC internals.
- `ROADMAP.md:55` defines Day 17 as Delta MERGE and idempotent processing.
- No Day 16 or Day 17 artifact directories currently exist.
- `LAB_BACKLOG.md` ends with LAB-014 at lines 149-157.
- `index.html:84-103` contains Day 1–3 cards.

Do not change `ROADMAP.md`, mark Day 4 complete, create Day 16 artifacts, or mark Day 16 complete. Create the standard package at `daily-artifacts/day-17/`; this is the existing repository convention, not a parallel structure.

## Status and evidence boundary

Use these exact Day 17 states everywhere:

- Conceptual Learning: `COMPLETE EARLY / OUT OF SEQUENCE`
- Reasoning Exercises: `COMPLETE EARLY / OUT OF SEQUENCE`
- Coding Practice: `DEFERRED / TODO`
- Experiment: `DEFERRED / NOT RUN`
- Measured Evidence: `NONE`
- Deferred lab: `LAB-015`

The supplied runtime, phase timing, file counts, conflict counts, SLAs, and reported chunking outcome are **lesson-provided scenario evidence**. They are not measurements produced in this repository and must never be presented as a completed lab or generally proven result. The write-amplification arithmetic uses explicit lesson assumptions.

## Current primary references

Use primary documentation with a checked date of 2026-09-06:

- Databricks, **Upsert into a Delta Lake table using merge**: https://docs.databricks.com/aws/en/delta/merge
- Databricks, **Isolation levels and write conflicts**: https://docs.databricks.com/aws/en/optimizations/isolation
- Databricks, **Isolation levels**: https://docs.databricks.com/aws/en/optimizations/isolation/isolation-levels
- Databricks, **Best practices: Delta Lake**: https://docs.databricks.com/aws/en/delta/best-practices
- Databricks, **Data skipping**: https://docs.databricks.com/aws/en/tables/data-skipping
- Databricks, **Use liquid clustering for tables**: https://docs.databricks.com/aws/en/delta/clustering
- Databricks, **ACID guarantees**: https://docs.databricks.com/aws/en/lakehouse/acid

Bound all version-sensitive claims. In particular:

- Official MERGE guidance requires source preprocessing when multiple source rows ambiguously match one target row; duplicate-match evaluation differs between Runtime 16.0+ and 15.4 LTS and below.
- Delta writes are atomic: a failed conflicting transaction does not become a partially visible table version.
- Conflict behavior depends on isolation level, runtime, table features, predicates, and row-level concurrency support. The supplied “same immutable Parquet file conflicts” example is a conventional copy-on-write scenario, not a universal claim about all current Databricks configurations.
- Liquid clustering by `customer_id` is only a candidate to test; do not promise MERGE improvement.

## New Day 17 package

Create the existing required package structure:

1. `daily-artifacts/day-17/lesson.md`
2. `daily-artifacts/day-17/quiz.md`
3. `daily-artifacts/day-17/quiz-review.md`
4. `daily-artifacts/day-17/interview-cheat-sheet.md`
5. `daily-artifacts/day-17/experiment.md`
6. `daily-artifacts/day-17/results.md`
7. `daily-artifacts/day-17/implementation/README.md`
8. `daily-artifacts/day-17/recap.html`

All are new files, so no before blocks exist.

### `daily-artifacts/day-17/lesson.md`

Begin with this exact block:

```markdown
# Day 17 Lesson — Delta MERGE and Idempotent Processing

- Sequence status: COMPLETED EARLY / OUT OF SEQUENCE
- Conceptual Learning: COMPLETE
- Reasoning Exercises: COMPLETE
- Coding Practice: DEFERRED / TODO
- Experiment: DEFERRED / NOT RUN
- Measured Evidence: NONE
- Roadmap topic: Delta MERGE and idempotent processing
- Day 16 dependency: CDC internals remains NOT STARTED; this lesson assumes the supplied PostgreSQL WAL → Debezium → Kafka → Bronze Delta contract and does not complete Day 16
- Deferred lab: LAB-015 in `../../LAB_BACKLOG.md`

All performance, conflict, SLA, and workload numbers below are supplied lesson scenarios unless explicitly labeled as arithmetic assumptions. No Day 17 Databricks implementation, benchmark, Spark UI analysis, conflict simulation, or measurement was executed in this repository.
```

Use these exact sections and preserve question → learner reasoning → mentor challenge/refinement → Staff/Architect principle:

1. `## 1. Business outcome and invariants`
2. `## 2. Day 16 CDC dependency boundary`
3. `## 3. Source cardinality and authoritative ordering`
4. `## 4. Target sequence guard`
5. `## 5. Delete tombstones and resurrection prevention`
6. `## 6. Reactivation, rejection, and sequence state`
7. `## 7. Independent versus dependent later events`
8. `## 8. Performance diagnosis before layout changes`
9. `## 9. Target layout candidate and success conditions`
10. `## 10. Write amplification`
11. `## 11. No-op CDC events and ordering boundaries`
12. `## 12. Concurrent writers and deterministic retries`
13. `## 13. Diagnose conflicts before retry policy`
14. `## 14. SLA-driven workload coordination`
15. `## 15. Backfill chunk sizing`
16. `## 16. Stop condition and monitoring`
17. `## 17. Vocabulary Upgrade`
18. `## 18. Architect/Staff challenge`
19. `## 19. Interview answer`
20. `## 20. Architecture bridge, open questions, and reflection`

Required content:

- Record the exact scenario: `customer_current`, 2 TB, 25M daily CDC records, one authoritative current state per `customer_id`, current match on `customer_id`, runtime 25→90 minutes, occasional retry value anomalies, PostgreSQL WAL → Debezium → Kafka → Bronze Delta, `source_sequence` authoritative ordering signal, application `event_timestamp` non-authoritative, `ingestion_timestamp` arrival-only, CDC SLA 15 minutes, backfill SLA 24 hours, and customer-service/billing-eligibility/regulatory consumers.
- State the business result as the latest committed customer state from the operational source. Never call `source_sequence` a date.
- Reference Day 16 as a future prerequisite for validating WAL/Debezium/Kafka ordering, delivery, event identity, delete representation, snapshot, and schema guarantees. Do not teach or mark complete the future Day 16 lesson.
- Preserve the exact target guard `source.source_sequence > target.last_source_sequence`: lower is stale, equal is duplicate/retry, only higher can modify current state.
- Explain both protections: deterministic source cardinality inside a batch and target sequence guarding across batches/retries/late arrivals.
- Include this PySpark example and state that an additional deterministic tie contract is required if equal sequences can occur:

```python
from pyspark.sql import Window, functions as F

window = Window.partitionBy("customer_id").orderBy(
    F.col("source_sequence").desc()
)

deduplicated = (
    source
    .withColumn("source_rank", F.row_number().over(window))
    .filter(F.col("source_rank") == 1)
    .drop("source_rank")
)
```

- Equal sequence plus different payload is a contract violation to quarantine, not an arbitrary tie to resolve.
- Specify minimal deletion tombstones: protected/approved key, `is_deleted`, `last_source_sequence`, deletion timestamp, and audit/source metadata; null/remove unnecessary PII; retain original event in immutable Bronze subject to retention policy.
- Walk through DELETE 504 / UPDATE 503, unmatched DELETE 504 / late INSERT 501, duplicate DELETE 504, and ACTIVE 505. State: source sequence determines newer; business policy determines transition validity.
- Distinguish `last_seen_sequence`, `last_applied_sequence`, and `last_rejected_sequence`; rejected events do not advance applied sequence. Make quarantine idempotent with event ID or sequence.
- For later events, distinguish complete authoritative after-images from dependent partial updates/commands. Isolate affected customer keys only; buffer/quarantine dependent later events, continue other customers, reconcile from corrected event or authoritative snapshot, and replay in order.
- Preserve scenario timing: dedup 8 min, target scan/match 55, rewrite 24, commit 3; total files 40,000, scanned 38,000, rewritten 2,400, distinct changed customers 250,000, randomly distributed IDs. Require the full supplied measurement list.
- Reject direct high-cardinality partitioning and unproven event-date partitioning for the current-state table. Liquid clustering on `customer_id` is a candidate because merge/point lookup use it, but declaring a key does not instantly reorganize history and representative MERGE evidence is required.
- Preserve all six layout success conditions from the supplied request.
- Explain update footprint versus write amplification and copy-on-write immutability. Show the lesson arithmetic: 250k × 1 KB ≈ 250 MB logical; 2,400 × 128 MB ≈ 307 GB physical; ≈1,228×. Label every input and result as an assumption, not production measurement.
- Preserve the 25M/250k/24.75M no-op scenario. Prefer source prevention when possible but explain why WAL/log CDC may correctly emit no-op UPDATEs. Do not discard Bronze. Explain sequence-only persistence cost, reliance on validated Kafka per-key ordering/checkpoint guarantees if skipped, `last_applied_change_sequence` naming, and the optional compact sequence-state table plus its complexity.
- For Jobs A/B at version 100 and same-file C101/C900 scenario, describe conventional copy-on-write conflict, atomic failure, and complete deterministic retry against the latest snapshot. Add the current-platform qualification about row-level concurrency and isolation/table configuration.
- Safe retry requirements: immutable batch, deterministic dedup, sequence guards, idempotent tombstones, bounded retry.
- Preserve conflict evidence: 47/52 weekly conflicts during backfill; distinct customer keys sometimes share files; CDC 15-minute SLA; backfill 24-hour SLA; pause/resume safe; CDC retry can take 25 minutes. Require job/type/frequency/window/keys/files/logical-vs-physical/retry-cost/history/SLA evidence.
- Preserve CDC priority and checkpointed deterministic backfill chunks. Replan each chunk against latest snapshot and measure both SLAs.
- Preserve chunk example: interval 15, p95 CDC 6, buffer 2, safe window ≈7 minutes. Use largest deterministic chunk reliably fitting the window; no unordered `LIMIT`; align with layout where practical; explain too-small chunk overhead.
- Label the 7-minute/18-hour/95%-conflict-reduction outcome as supplied lesson evidence, not repository measurement. Record the stop decision and every reopen condition.
- Include every required Vocabulary Upgrade phrase verbatim:
  - “Late-arriving event” or “out-of-order event,” not “lag data.”
  - “Authoritative ordering signal,” not “authoritative date freshness.”
  - “Target sequence guard.”
  - “Deterministic source cardinality.”
  - “Deletion tombstone.”
  - “Prevent stale-state resurrection.”
  - “Last seen, last applied, and last rejected sequence.”
  - “Broad update footprint.”
  - “Write amplification.”
  - “Physical file contention versus business-key conflict.”
  - “Retry the complete deterministic transaction against the latest snapshot.”
  - “Pilot workload coordination and validate both SLAs.”
  - “The largest deterministic chunk that fits inside the safe concurrency window.”
  - “Stop optimizing when the measured business requirement is satisfied.”
- The Architect/Staff challenge must integrate correctness, deletion/reactivation, dependency, performance, layout, write amplification, concurrency, SLA coordination, chunking, monitoring, and decision reopening without turning candidates into final universal architecture.
- Add the exact 60–90 second answer structure: Business outcome; Correctness controls; Performance evidence; Decision; Trade-off; What changes the decision.
- End with open questions: actual producer ordering/delivery contract; equal-sequence conflict policy; delete retention/PII policy; reactivation policy; after-image completeness; runtime/table features/isolation; row-level concurrency; current file statistics/layout; measured write amplification; no-op ordering guarantees; conflict cost; chunk-size distribution; SLA headroom.

### `daily-artifacts/day-17/quiz.md` and `quiz-review.md`

Use the established challenge convention from Day 3. Title the attempt `# Day 17 Architect/Staff Challenge — Learner Reasoning` and explicitly label it completed early/out of sequence with no implementation. Preserve the learner's original reasoning across at least these topics: business outcome, target sequence guard, source dedup, tombstones, reactivation, dependent events, scan diagnosis, layout, write amplification, no-ops, concurrent retry, conflict evidence, SLA priority, chunk sizing, and stop condition.

The review must mirror those topics with **Correct**, **Refinement**, and **Staff vocabulary**, ending with Remaining gaps: Day 16 CDC guarantees unverified; no Day 17 implementation, metrics, conflict simulation, or layout benchmark; LAB-015 TODO.

### `daily-artifacts/day-17/interview-cheat-sheet.md`

Title it `# Day 17 — Five-Minute Delta MERGE and Idempotency Interview Cheat Sheet`. Include:

- business invariant and source-ordering hierarchy;
- source cardinality + target guard;
- tombstone transition table for the four sequence cases;
- seen/applied/rejected sequence distinction;
- independent/dependent event decision;
- performance phase and measurement table;
- scan versus rewrite versus write-amplification distinction;
- no-op trade-off;
- conventional conflict plus current concurrency qualification;
- SLA coordination/chunk formula;
- all Vocabulary Upgrades;
- the polished 60–90 second answer in the six requested labeled parts.

### `daily-artifacts/day-17/experiment.md`

Use a detailed LAB-015 plan, but mark every setup/execution/measurement field `TODO / NOT RUN`. Link `../../LAB_BACKLOG.md`. Include expected assertions without results and enumerate all requested hands-on work:

- generate CDC test events with duplicates and out-of-order events;
- deduplicate using an authoritative source sequence;
- implement sequence-guarded `MERGE`;
- test duplicate retry behavior, matched delete, unmatched-delete tombstone, late update after deletion, legitimate reactivation, and terminal-delete quarantine;
- test independent versus dependent later events;
- capture rows updated, copied, inserted, and deleted;
- capture files scanned and rewritten where exposed;
- measure logical change volume versus physical rewrite volume;
- simulate or document concurrent-writer conflict behavior;
- implement deterministic resumable backfill chunks; and
- verify correctness before and after any layout change.

### `daily-artifacts/day-17/results.md`

State: not run; no repository observations; no Databricks implementation, plans, metrics, concurrency simulation, correctness assertion, or benchmark. Separate lesson-supplied scenario evidence and arithmetic from lab evidence. Point to LAB-015.

### `daily-artifacts/day-17/implementation/README.md`

State `DEFERRED / TODO`; no SQL/PySpark/MERGE/table layout/concurrency/backfill implementation exists. Link LAB-015 and say code/run instructions are added only when executed.

### `daily-artifacts/day-17/recap.html`

Match the current `daily-artifacts/day-03/recap.html` design system and interactive behavior exactly: same tokens, responsive rules, theme, internal navigation, search, study modes, expand/collapse, answer reveal, progressive enhancement, visible focus, semantic landmarks, and reduced motion.

It must clearly show `Day 17 · completed early / out of sequence`, conceptual/reasoning complete, coding/experiment TODO, evidence none, Day 16 not complete, and Day 4 still next. Cover correctness pipeline, tombstone state transitions, performance evidence, write-amplification arithmetic, concurrency/retry, workload coordination, Vocabulary Upgrade, open questions, and interview answer. Link every Day 17 package file plus LAB_BACKLOG in source provenance.

## Existing file updates

### 1. Append LAB-015 to `LAB_BACKLOG.md`

**File:** `LAB_BACKLOG.md`, after current lines 149-157.

Before anchor copied from source:

```markdown
## LAB-014 — Physical Optimization Correctness Invariants

- **Origin:** Week 1 Day 3 — Partitioning and Pruning
- **Question/hypothesis:** Physical optimizations must preserve equivalent business results for the same input/snapshot even when layout and execution metrics change.
- **Exercise:** For each Day 3 physical optimization, compare before/after outputs using the relevant business invariants before accepting performance evidence.
- **Expected evidence:** Row counts, business keys, duplicates, null behavior, aggregates, business totals, query results, snapshot/input identity, and explicit pass/fail assertions.
- **Environment/tool:** Databricks Free Edition or another available Spark environment; capability and exposed metrics not yet verified.
- **Status:** TODO
- **Result/artifact link:** not run
```

Append `## LAB-015 — Delta CDC MERGE Correctness, Performance, and Concurrency` with the standard Origin, Question/hypothesis, Exercise, Expected evidence, Environment/tool, Status, and Result/artifact fields. The Exercise must include every hands-on item from the user request. Use `Status: TODO` and `Result/artifact link: not run`.

### 2. Update `CURRENT_SESSION.md` without advancing scheduled position

**File:** `CURRENT_SESSION.md`.

Preserve these exact source facts:

```markdown
**Week 1, Day 3 — Partitioning and Pruning: conceptual/reasoning COMPLETE**

Next: **Week 1, Day 4 — Aggregation at Scale**
```

and:

```markdown
## Next lesson

**Week 1, Day 4 — Aggregation at Scale**

Study `GROUP BY`, partial/local aggregation, shuffle, reducers/final aggregation, and cardinality. Day 4 has not started.
```

Make only additive Day 17 state changes:

- Add an `## Early / out-of-sequence completion` section after current Status (after line 25): Day 17 conceptual/reasoning complete early; Day 16 and scheduled Days 4–16 not complete; Day 17 implementation/experiment/measurements pending as LAB-015; next roadmap lesson remains Day 4.
- Add a concise Day 17 concept bullet group without replacing current Day 3 concepts.
- Add LAB-015 to Outstanding Lab Backlog.
- Add Day 17 remaining interview/evidence gaps.
- Add the Day 17 package to Artifacts created.
- Add Day 17 recap, cheat sheet, and LAB-015 to Read before resuming while keeping Day 3 artifacts and Day 4 next.

### 3. Add Day 17 to `index.html`

**File:** `index.html`, insert after current Day 3 card at lines 97-102 and before line 103.

Before anchor copied from source:

```html
      <article class="card">
        <div class="status">Week 1 · Day 3</div>
        <h2>Partitioning and Pruning</h2>
        <p>Partition pruning, data skipping, physical locality, small-file diagnosis, clustering, and evidence-driven layout decisions.</p>
        <a class="button" href="daily-artifacts/day-03/recap.html">Open Day 3 recap</a>
      </article>
```

Insert:

```html
      <article class="card">
        <div class="status">Week 3 · Day 17 · Completed early</div>
        <h2>Delta MERGE and Idempotent Processing</h2>
        <p>CDC ordering, sequence guards, tombstones, late arrivals, write amplification, deterministic retries, and SLA-driven writer coordination.</p>
        <a class="button" href="daily-artifacts/day-17/recap.html">Open Day 17 recap</a>
      </article>
```

## Files that must remain unchanged

- `ROADMAP.md`
- all existing `daily-artifacts/day-01/`, `day-02/`, and `day-03/` files
- `daily-artifacts/_template/`
- no `daily-artifacts/day-16/` directory
- `.github/workflows/pages.yml`
- `daily-artifacts/.DS_Store`

## Verification and commit

1. Run `python3 scripts/validate_tutorial_index.py`; expect four indexed tutorial pages.
2. Verify every Day 17 Markdown and HTML relative link resolves.
3. Serve `/`, Day 1–3, and Day 17 over HTTP and require 200 responses.
4. Verify Day 17 CSS and interaction script match Day 3 exactly.
5. Check HTML language, title, one H1, semantic landmarks, focus/reduced-motion rules, keyboard-native controls, and no-JavaScript readability.
6. Exercise theme, search, mode filtering, expand/collapse, and answer reveal if a browser is available. State any browser limitation honestly.
7. Search for unsupported completion/measurement claims, Day 16 completion, Day 4 completion, `source_sequence` called a date, arbitrary equal-sequence tie resolution, hard-delete-only design, partial failed-transaction recovery, universal same-file conflict claims, or promised clustering performance.
8. Confirm every LAB-015 field remains TODO/not run and all expected assertions are predictions.
9. Confirm `ROADMAP.md` is byte-for-byte unchanged and `CURRENT_SESSION.md` still resumes at Day 4.
10. Run `git diff --check`, review the full diff, and exclude `.DS_Store`.

After approval and implementation, create a feature branch from synced `main` and commit only these files using:

```text
docs: capture Day 17 Delta MERGE reasoning early
```

Push the branch only after the commit succeeds, the worktree contains no unexpected tracked changes, authentication is configured, and repository policy permits it. Never force push. Do not create a PR unless separately requested.
