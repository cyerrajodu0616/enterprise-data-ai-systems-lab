# Amend Day 17 with the Industry and Vendor Reference layer

## Context and verified state

The Day 17 conceptual package was merged to `main` in PR #8 at merge commit `d18b3ce`. The repository is synchronized with `origin/main`; the only pre-existing untracked file is `daily-artifacts/.DS_Store`, which must remain untouched and unstaged.

Day 17 currently preserves the foundational reasoning but lacks the curriculum's explicit comparison to current managed platforms and primary engineering publications. The current full-file rewrite and same-file contention statements are qualified as conventional copy-on-write behavior, yet they need the concrete deletion-vector and row-level-concurrency requirements now documented by Databricks.

Do not modify `ROADMAP.md`, complete Day 16, complete LAB-015, change the next lesson from Week 1 Day 4 — Aggregation at Scale, or fabricate measurements. This is a documentation correction to the existing `daily-artifacts/day-17/` package, not a new lesson or parallel structure.

## Primary sources and evidence rules

Use descriptive Markdown links and state `Accessed 2026-09-06` for each reference. Treat vendor documentation as current documented platform behavior, engineering publications as organization-specific examples, the existing performance numbers as lesson-supplied scenario evidence, and cross-platform recommendations as architectural inference.

Required sources:

1. Databricks, [AUTO CDC INTO (pipelines)](https://docs.databricks.com/aws/en/ldp/developer/ldp-sql-ref-apply-changes-into)
2. Databricks, [Change data capture and snapshots](https://docs.databricks.com/aws/en/data-engineering/what-is-cdc)
3. Databricks, [Deletion vectors in Databricks](https://docs.databricks.com/aws/en/tables/features/deletion-vectors)
4. Databricks, [Row-level concurrency](https://docs.databricks.com/aws/en/optimizations/isolation/row-level-concurrency)
5. Databricks, [Use liquid clustering for tables](https://docs.databricks.com/aws/en/tables/clustering)
6. Snowflake, [Introduction to streams](https://docs.snowflake.com/en/user-guide/streams-intro)
7. Snowflake, [Introduction to streams and tasks](https://docs.snowflake.com/en/user-guide/data-pipelines-intro)
8. Snowflake, [Decision guide for dynamic tables](https://docs.snowflake.com/en/user-guide/dynamic-tables/decision-guide)
9. Netflix, [DBLog: A Watermark Based Change-Data-Capture Framework](https://arxiv.org/abs/2010.12597)
10. LinkedIn, [Open sourcing Brooklin: Near real-time data streaming at scale](https://www.linkedin.com/blog/engineering/open-source/brooklin-open-source)
11. Uber, [DBEvents: A Standardized Framework for Efficiently Ingesting Data into Uber's Apache Hadoop Data Lake](https://www.uber.com/us/en/blog/dbevents-ingestion-framework/)
12. Airbnb, [SpinalTap](https://airbnb.tech/opensource/spinaltap/)

Verified source constraints:

- AUTO CDC requires `KEYS` and `SEQUENCE BY`; the sequence determines logical event order and enables out-of-order handling. `APPLY AS DELETE WHEN` identifies delete events. SCD Type 1 keeps current state; SCD Type 2 keeps history with `__START_AT`/`__END_AT`. Databricks documents temporary underlying tombstones for out-of-order SCD Type 2 delete handling and configurable retention through `pipelines.cdc.tombstoneGCThresholdInSeconds`.
- Without deletion vectors, a conventional row modification rewrites its Parquet file. Delta deletion vectors must be enabled, client read/write support varies, and enabling them upgrades the table protocol; do not imply universal availability. They record row changes as metadata/soft deletes and defer physical rewrite until operations such as `OPTIMIZE`, purge, or eligible compaction.
- Current row-level concurrency resolves some conflicts when different rows in one file are changed. The documented requirements include Databricks Runtime 14.3 LTS+, an unpartitioned table, and deletion vectors enabled. Metadata and other documented limitations still apply.
- A Snowflake Stream stores an offset, exposes row changes between transactional points, and adds `METADATA$ACTION`, `METADATA$ISUPDATE`, and `METADATA$ROW_ID`. An UPDATE is represented as DELETE and INSERT rows with `METADATA$ISUPDATE = TRUE`. This offset is not evidence of the originating database's business order; when externally produced events can arrive out of order, retaining an external authoritative source sequence is an architectural requirement/inference.
- Snowflake Tasks run SQL/procedures on schedules or triggers; Streams + Tasks + MERGE provide procedural DML and orchestration control. Dynamic Tables provide a declarative SELECT with managed refresh/dependencies/incremental processing, but are read-only and do not support MERGE; use Streams/Tasks for DML, custom retries/orchestration, SCD Type 2, or complex upserts.
- Netflix DBLog documents transaction-log CDC plus watermark-coordinated full-state selection; selects run in tracked chunks that can pause/resume with minimal source impact.
- LinkedIn Brooklin documents low-latency database change streams, isolation of downstream applications from operational stores, bootstrap support, and transaction-boundary preservation by applicable connectors.
- Uber DBEvents documents bootstrap plus incremental ingestion, batchable/incremental bootstrap, MySQL binary-log events in commit order, Avro-standardized change events, and schema governance.
- Airbnb's primary SpinalTap page supports only the narrower claim that it is a reliable, low-latency, general-purpose CDC service propagating standardized events to downstream consumers. Do not attribute bootstrap, watermarks, transaction boundaries, or a tombstone schema to SpinalTap from this page.

## File 1: `daily-artifacts/day-17/lesson.md`

### A. Qualify write amplification and concurrency

At current lines 116-118, preserve this exact source anchor:

```markdown
## 10. Write amplification

The fraction of files rewritten describes a broad update footprint. Write amplification compares physical bytes rewritten with logical bytes changed. Under explicit lesson assumptions: 250,000 rows × 1 KB ≈ 250 MB logical change; 2,400 files × 128 MB ≈ 307 GB physical rewrite; approximately 1,228× amplification. These are arithmetic assumptions, not repository or production measurements.
```

Extend it immediately afterward with documented facts: conventional updates without deletion vectors may rewrite the entire containing Parquet file; deletion vectors can record affected rows and reduce the immediate full-file rewrite; physical rewrite is deferred rather than eliminated; Delta tables do not universally have deletion vectors; enabling them upgrades table protocol; readers/writers must be compatible. Cite the deletion-vector source inline.

At current lines 126-130, preserve this exact source anchor:

```markdown
## 12. Concurrent writers and deterministic retries

In the supplied conventional copy-on-write case, Jobs A and B read version 100; A changes C101, B changes C900, and both rows occupy one immutable Parquet file. A commits version 101. B's stale transaction fails atomically and must retry the complete deterministic MERGE against the latest snapshot—not recover one task or file.

Safe retries require an immutable source batch, deterministic deduplication, sequence guards, idempotent tombstones, and bounded retry. Actual conflict behavior depends on runtime, isolation, table features, predicates, and row-level concurrency; same-file conflict is not universal across current configurations.
```

Replace it with a section that explicitly labels the scenario as behavior **without applicable row-level concurrency**. Explain documented current row-level concurrency and its requirements/limitations. Preserve deterministic whole-transaction retry for conflicts that still occur. State that workload coordination remains a fallback and operational control after evaluating available concurrency—not the first assumption when row-level concurrency already addresses disjoint-row contention. Cite row-level concurrency and deletion vectors inline.

At current lines 136-140, adjust workload coordination consistently. Preserve the supplied SLA scenario and deterministic chunk reasoning, but make its decision order: validate current table/runtime concurrency → observe residual conflicts → use coordination where needed.

### B. Add managed-platform and industry sections

Insert after current `## 16. Stop condition and monitoring` and before current `## 17. Vocabulary Upgrade`. Renumber the existing Vocabulary, Challenge, Interview, and Architecture sections to 21–24 so the new material becomes:

```markdown
## 17. Databricks managed CDC: AUTO CDC versus manual MERGE

## 18. Snowflake equivalent: Streams, Tasks, MERGE, and Dynamic Tables

## 19. Representative industry practices

## 20. Our design versus current managed platforms
```

Day 17 section 17 must:

- explain `KEYS`, `SEQUENCE BY`, `APPLY AS DELETE WHEN`, SCD Type 1, and SCD Type 2 at the level supported above;
- state that AUTO CDC uses the sequence column to handle out-of-order events;
- distinguish Databricks-managed temporary SCD2 tombstones and configurable retention from this lesson's proposed business current-state tombstone schema;
- compare AUTO CDC to manual MERGE without claiming one is universally superior;
- recommend AUTO CDC when the managed semantics express the verified key/order/delete/history contract;
- justify custom MERGE only for requirements AUTO CDC cannot express, unusual transition/quarantine/state models, unsupported environments, or evidence-backed operational constraints; and
- keep custom logic's burden explicit: source cardinality, ordering, tombstones, replay, testing, metrics, upgrades, and retries.

Day 17 section 18 must explain the three Stream metadata columns and update DELETE/INSERT pair, transactional offset semantics, Tasks, procedural Streams + Tasks + MERGE, declarative Dynamic Tables, and the external-source-sequence caveat. Never say a Snowflake Stream offset reconstructs the original source's business ordering.

Day 17 section 19 must use a table with `Publication`, `Documented practice`, and `Generalizable lesson`. Include only the source-supported facts for Netflix DBLog, LinkedIn Brooklin, Uber DBEvents, and Airbnb SpinalTap. Cover the requested practices across the table where sources support them, but do not force every practice onto every company. Explicitly state that none of these sources establishes use of this lesson's exact tombstone schema.

Day 17 section 20 must include this exact column structure:

| Concern | Foundational/manual approach | Databricks approach | Snowflake approach | Decision trigger |
|---|---|---|---|---|

Include at least: key/order, deletes/history, out-of-order handling, physical updates, concurrency, bootstrap/incremental processing, orchestration/control, and evidence/operational cost.

End section 20 with this exact recommendation:

> Start with the correctness contract: authoritative key, authoritative ordering, delete semantics, replay horizon, and reactivation policy. On Databricks, prefer AUTO CDC when it expresses those requirements; then evaluate deletion vectors, liquid clustering, and row-level concurrency before creating custom workload coordination. On Snowflake, choose between Streams + Tasks + MERGE and a declarative Dynamic Table based on required DML and control. Custom logic must earn its operational cost.

### C. References and evidence taxonomy

Replace the current final single-paragraph reference line with a `## Primary references` list containing all 12 required descriptive links and `Accessed 2026-09-06`. Retain existing relevant MERGE/isolation/best-practice/ACID references in a separate `Additional Databricks references` list rather than dropping them.

Add a compact legend near the new material:

- **Documented fact:** directly supported by a cited source.
- **Lesson scenario:** supplied numbers or outcomes, not repository measurement.
- **Architectural inference:** recommendation derived from requirements plus documented capabilities.

## File 2: `daily-artifacts/day-17/interview-cheat-sheet.md`

After current lines 37-40 (`## Concurrency and coordination`), add compact sections titled `## Managed-platform choices` and `## Industry patterns`.

Cover AUTO CDC key/order/delete/SCD/tombstone behavior, deletion vectors and row-level concurrency qualifications, Snowflake Stream metadata/update pairs and platform-choice rule, and the Netflix/LinkedIn/Uber/Airbnb generalizable patterns. Add the exact refined recommendation as a blockquote. Add the 12-reference list with access date, or link to a dedicated reference section in `lesson.md` while retaining enough descriptive source names for offline clarity.

Update the 60–90 second answer so the Decision and What would change sections consider managed functionality before custom MERGE/layout/workload coordination.

## File 3: `daily-artifacts/day-17/quiz-review.md`

At current lines 46-52, preserve this source anchor:

```markdown
## Concurrency, workload coordination, and stopping

**Correct:** Retry the complete deterministic transaction and prioritize the tighter CDC SLA with checkpointed backfill chunks.

**Refinement:** Current row-level concurrency depends on runtime/table/isolation configuration. Measure both SLAs and chunk overhead.

**Staff vocabulary:** Physical file contention versus business-key conflict; safe concurrency window; evidence-based stop condition.
```

Revise it to establish the platform-first decision order and add `## Managed platform and industry reference gap` documenting AUTO CDC, deletion vectors, row-level concurrency, Snowflake alternatives, and representative industry patterns as required refinements—not lab results.

## File 4: `daily-artifacts/day-17/recap.html`

Current line 18 contains the compact performance section and line 19 contains concurrency. Qualify both with deletion-vector and row-level-concurrency facts. Add internal navigation link `Platforms` and a new semantic section with `id="platforms"`, visible in all relevant study modes, containing:

- Databricks AUTO CDC versus manual MERGE;
- deletion vectors and row-level concurrency requirements;
- Snowflake Streams/Tasks/MERGE versus Dynamic Tables;
- an accessible five-column `Our design versus current managed platforms` decision table;
- a four-company industry-practice comparison;
- the exact refined recommendation; and
- descriptive external primary-reference links marked `Accessed 2026-09-06` in the secondary provenance area.

Preserve the current responsive shell, theme, mode filtering, search, details expansion, semantic landmarks, no-JavaScript readability, evidence boundary, Day 16 incomplete status, LAB-015 TODO, and Day 4 next status.

## File 5: `LEARNING_GUIDELINES.md`

The applicable permanent rule belongs in this repository-wide governing file, under `## Day completion and deferred evidence`, after the current paragraph at lines 98-100.

Before anchor copied from source:

```markdown
When a deferred experiment is executed, preserve its original hypothesis; record the environment, configuration, and dataset; separate actual observations from interpretation; link the artifacts; mark the lab `DONE`; and revise earlier conclusions when evidence contradicts them.
```

Insert:

```markdown
### Industry and vendor reference completion check

Every completed Technical Sharpness lesson must:

- include current official Databricks or Snowflake references when relevant;
- examine at least one credible production implementation from a major engineering organization when public primary evidence exists;
- clearly separate documented fact, lesson scenario, and architectural inference; and
- check current official documentation before relying on platform behavior that may have changed.
```

## File 6: `CURRENT_SESSION.md`

Make additive wording changes only. At current line 43, expand the Day 17 completed-concepts bullet to include managed Databricks CDC, deletion vectors/row-level concurrency, Snowflake choices, and industry patterns. In `## Interview gaps discovered`, record that platform capabilities must be checked before recommending custom coordination. Do not alter lines 13-15, 29-31, or 98-102: Day 4 remains next, Day 16 remains incomplete, and Day 17 hands-on work remains pending.

## Files that remain unchanged

- `ROADMAP.md`
- `LAB_BACKLOG.md` status and result for LAB-015
- `daily-artifacts/day-17/experiment.md`, `results.md`, and `implementation/README.md`
- all Day 1–3 and Day 16 paths
- `index.html` (the existing Day 17 route and description remain valid)
- `.github/workflows/pages.yml`
- `daily-artifacts/.DS_Store`

## Verification and commit

1. Re-read the entire amended `daily-artifacts/day-17/lesson.md` for internal consistency.
2. Verify all 12 required primary links are present, descriptive, and marked `Accessed 2026-09-06`.
3. Search Day 17 for universal claims that all updates rewrite complete files, all same-file changes conflict, all Delta tables have deletion vectors, all eligible writes use row-level concurrency, Snowflake offsets determine source business order, or named companies use this tombstone schema.
4. Confirm documented fact, lesson scenario, and architectural inference remain separated; do not convert source claims into measured lab results.
5. Confirm AUTO CDC temporary tombstones are not conflated with the lesson's business tombstones.
6. Confirm workload coordination is a fallback/control after current concurrency evaluation.
7. Run `python3 scripts/validate_tutorial_index.py`; expect four indexed tutorials.
8. Verify every Day 17 Markdown/HTML relative link and all external primary-reference URLs.
9. Validate HTML language, title, viewport, one H1, semantic landmarks, responsive table behavior, visible focus, reduced motion, and no-JavaScript readability.
10. Serve the root and Day 1–3/17 recaps locally and require HTTP 200.
11. Confirm `ROADMAP.md` and the LAB-015 status/result are unchanged; confirm `CURRENT_SESSION.md` still resumes at Day 4.
12. Run `git diff --check`, review the complete diff, and leave `.DS_Store` unstaged.

After approval, create a correction branch from synchronized `main`, implement only these reviewed changes, and commit with:

```text
docs: add Day 17 industry and vendor references
```

Push and create a PR only when authentication is already configured and repository policy permits it. Never force push or merge without explicit user direction.
