# Add Durable Daily Learning Packages

## Context

The current repository requires daily coding, experiments, debugging, and reflection, but it does not require a persisted end-of-day HTML recap, quiz, or standardized implementation package. Add a repository contract that stores every completed day's artifacts in GitHub without creating 56 empty directories or generating answers before the learner attempts the work.

## Exact changes

### 1. Update `README.md` lines 39–60

Before:

```markdown
## Repository map

- `enterprise-challenges/` — primary learning sequence and challenge catalog.
- `enterprise-data-platform/` — the evolving warehouse/lakehouse implementation.
- `coding/` — manual SQL, Python, and PySpark practice.
- `debugging/` — broken-system diagnosis using evidence and regression tests.
- `orchestration/airflow/` — orchestration decisions and Airflow artifacts.
- `transformations/dbt/` — SQL transformation, testing, and documentation artifacts.
- `databricks/` — Spark, Delta, performance, CDC, Unity Catalog, and governance mechanisms.
- `experiments/` — reproducible experiment definitions and measured results.
- `industry-case-studies/` — source-backed cases organized by engineering problem.
- `ai-integration/` — governed enterprise data for AI.
- `snowflake/` — later workload-based comparison.
- `interview-journal/` — interview evidence and targeted follow-up.
- `DAILY_LESSON_TEMPLATE.md` — the reusable lesson structure.
- `REFERENCES.md` — durable foundations, current official documentation, and curated engineering sources.
- `RESUME_PROTOCOL.md` — deterministic continuation from a new session.

Start with `RESUME_PROTOCOL.md`, `CURRENT_SESSION.md`, `ROADMAP.md`, the current challenge, and the Day 1 proposal.
```

After:

```markdown
## Repository map

- `enterprise-challenges/` — primary learning sequence and challenge catalog.
- `enterprise-data-platform/` — the evolving warehouse/lakehouse implementation.
- `coding/` — manual SQL, Python, and PySpark practice.
- `debugging/` — broken-system diagnosis using evidence and regression tests.
- `orchestration/airflow/` — orchestration decisions and Airflow artifacts.
- `transformations/dbt/` — SQL transformation, testing, and documentation artifacts.
- `databricks/` — Spark, Delta, performance, CDC, Unity Catalog, and governance mechanisms.
- `experiments/` — reproducible experiment definitions and measured results.
- `industry-case-studies/` — source-backed cases organized by engineering problem.
- `daily-artifacts/` — committed end-of-day lessons, quizzes, implementations, evidence, and HTML recaps.
- `ai-integration/` — governed enterprise data for AI.
- `snowflake/` — later workload-based comparison.
- `interview-journal/` — interview evidence and targeted follow-up.
- `DAILY_LESSON_TEMPLATE.md` — the reusable lesson structure.
- `DAILY_ARTIFACT_GUIDELINES.md` — the required end-of-day package contract.
- `REFERENCES.md` — durable foundations, current official documentation, and curated engineering sources.
- `RESUME_PROTOCOL.md` — deterministic continuation from a new session.

Start with `RESUME_PROTOCOL.md`, `CURRENT_SESSION.md`, `ROADMAP.md`, the current challenge, and the current day's committed package when one exists.
```

### 2. Append to `DAILY_LESSON_TEMPLATE.md` after line 35

Before:

```markdown
## 16. Reflection

What changed in my mental model?
```

After:

```markdown
## 16. Reflection

What changed in my mental model?

## End-of-day package

Before marking the day complete, create `daily-artifacts/day-XX/` from `daily-artifacts/_template/` and finish:

- `lesson.md` — completed reasoning and notes;
- `quiz.md` — questions and the learner's answers;
- `quiz-review.md` — reviewed answers and explanations, added only after the attempt;
- `implementation/` — SQL, Python, PySpark, configuration, and tests actually produced;
- `experiment.md` — hypothesis, setup, execution, and measurements;
- `results.md` — observed evidence, failures, and conclusions;
- `recap.html` — portable visual recap linking to the source artifacts.

Update `CURRENT_SESSION.md`, then commit and push the package. A day is not `complete` until this durable package exists or the session record explains why an artifact is not applicable.
```

### 3. Replace `ROADMAP.md` lines 155–157

Before:

```markdown
## Every day

Use `DAILY_LESSON_TEMPLATE.md`: Refresh -> Internals -> Modern Implementation -> Industry Guidance -> Industry Case Study -> Learner Decision -> Build -> Break -> Measure -> Generalize -> Interview -> Architecture Bridge -> Reflection.
```

After:

```markdown
## Every day

Use `DAILY_LESSON_TEMPLATE.md`: Refresh -> Internals -> Modern Implementation -> Industry Guidance -> Industry Case Study -> Learner Decision -> Build -> Break -> Measure -> Generalize -> Interview -> Architecture Bridge -> Reflection.

End by committing a durable package under `daily-artifacts/day-XX/` containing the completed lesson, attempted quiz and reviewed answers, implementation and tests, experiment and measured results, and a self-contained `recap.html`. Follow `DAILY_ARTIFACT_GUIDELINES.md`; never fabricate results or publish solutions before the learner's attempt.
```

### 4. Update `CURRENT_SESSION.md` lines 48–50

Before:

```markdown
## Artifacts created

- Repository guidelines, challenge catalog, roadmap, experiment standard, and Day 1 proposal.
```

After:

```markdown
## Artifacts created

- Repository guidelines, challenge catalog, roadmap, experiment standard, Day 1 proposal, and reusable daily-package template.
- No completed `daily-artifacts/day-XX/` package exists yet because Day 1 has not started.
```

### 5. Update `RESUME_PROTOCOL.md` lines 7–14 and line 26

Before:

```markdown
1. `CURRENT_SESSION.md`
2. `LEARNING_GUIDELINES.md`
3. `CODING_PRACTICE_GUIDELINES.md`
4. `ROADMAP.md`
5. the current week's README/material
6. the current enterprise challenge
7. relevant experiment results
8. `ARCHITECTURE_LAB_BRIDGE.md`
```

After:

```markdown
1. `CURRENT_SESSION.md`
2. the most recent completed package under `daily-artifacts/day-XX/`, including `recap.html` and source artifacts
3. `LEARNING_GUIDELINES.md`
4. `CODING_PRACTICE_GUIDELINES.md`
5. `ROADMAP.md`
6. the current week's README/material
7. the current enterprise challenge
8. relevant experiment results
9. `ARCHITECTURE_LAB_BRIDGE.md`
```

Before line 26:

```markdown
Continue without resetting the program. At the end of every meaningful session, update `CURRENT_SESSION.md` with completed concepts/code/experiments, measured evidence, unresolved questions, project state, interview gaps, artifacts, next lesson, and recommended resume files.
```

After:

```markdown
Continue without resetting the program. At the end of every meaningful session, update `CURRENT_SESSION.md` with completed concepts/code/experiments, measured evidence, unresolved questions, project state, interview gaps, artifacts, next lesson, and recommended resume files. At the end of every completed day, also verify and commit the required `daily-artifacts/day-XX/` package.
```

### 6. Add `DAILY_ARTIFACT_GUIDELINES.md`

New file; no prior lines.

```markdown
# Daily Artifact Guidelines

Every completed roadmap day must be recoverable from GitHub without relying on chat history or one workstation.

## Package lifecycle

1. At the start of a day, copy `daily-artifacts/_template/` to `daily-artifacts/day-XX/`.
2. Keep `quiz-review.md` unanswered until the learner submits `quiz.md`.
3. Store real SQL, Python, PySpark, dbt, Airflow, configuration, and tests under `implementation/`; link shared project code rather than duplicate it.
4. Record experiment hypotheses before execution and observed results afterward.
5. Generate `recap.html` only from completed, reviewed source artifacts.
6. Open the HTML locally and verify content, links, code formatting, responsive layout, and accessibility basics.
7. Update `CURRENT_SESSION.md`, commit, and push.

## Required package

```text
daily-artifacts/day-XX/
  lesson.md
  quiz.md
  quiz-review.md
  implementation/
    README.md
  experiment.md
  results.md
  recap.html
```

## Quiz policy

Use conceptual, execution-plan, implementation, debugging, and Staff-level design questions. The learner answers first. `quiz-review.md` then records corrections, reasoning, and remaining gaps; it is not a hidden answer key generated in advance.

## HTML recap policy

`recap.html` is a portable study artifact, not the source of truth. It must be self-contained HTML/CSS with no required CDN or external runtime and must link to the Markdown, implementation, test, and experiment files. Include problem, mental-model change, key internals, visual explanation where useful, quiz review, implementation summary, evidence, failure/debugging lesson, interview explanation, architecture bridge, and next step. Clearly label unexecuted experiments and hypothetical projections.

## Completion rule

A day is complete only when its package is reviewed, the HTML renders correctly, evidence is honest, `CURRENT_SESSION.md` is updated, and everything is committed and pushed. If an artifact is not applicable, explain why in `lesson.md` rather than leaving an ambiguous placeholder.
```

### 7. Add the reusable template package

Add these new files with the exact content below. Do not create `day-01` yet because the lesson has not started.

#### `daily-artifacts/README.md`

```markdown
# Daily Artifacts

Completed learning days live here as `day-01` through `day-56`. Create a day from `_template/` when the lesson starts and commit it only with honest status and evidence. See `DAILY_ARTIFACT_GUIDELINES.md`.
```

#### `daily-artifacts/_template/lesson.md`

```markdown
# Day XX Lesson

- Status: not started
- Roadmap topic:
- Enterprise challenge:
- Capability classification:

Use the 16 sections in `DAILY_LESSON_TEMPLATE.md`. Replace this instruction with the completed lesson rather than retaining empty headings.
```

#### `daily-artifacts/_template/quiz.md`

```markdown
# Day XX Quiz Attempt

Record conceptual, execution-plan, implementation, debugging, and Staff-level design questions, followed by the learner's first answers. Do not add reviewed solutions here.
```

#### `daily-artifacts/_template/quiz-review.md`

```markdown
# Day XX Quiz Review

Complete only after the learner attempts `quiz.md`. For each response record what was correct, what needs correction, the reasoning, and the follow-up gap.
```

#### `daily-artifacts/_template/implementation/README.md`

```markdown
# Day XX Implementation

Store or link the SQL, Python, PySpark, dbt, Airflow, configuration, and tests produced today. Explain how to run them and which work was completed manually versus with AI assistance.
```

#### `daily-artifacts/_template/experiment.md`

```markdown
# Day XX Experiment

- Problem:
- Current design:
- Hypothesis:
- Expected internal mechanism:
- Dataset:
- Infrastructure/runtime:
- Execution plan:
- Measurements: not run
```

#### `daily-artifacts/_template/results.md`

```markdown
# Day XX Results

- Status: not run
- Observed evidence:
- Explanation:
- Trade-offs:
- Operational impact:
- Cost implication:
- Failure boundary:
- Generalization:
- Architecture implication:
```

#### `daily-artifacts/_template/recap.html`

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Day XX Technical Sharpness Recap</title>
  <style>
    :root { color-scheme: light dark; font-family: system-ui, sans-serif; line-height: 1.5; }
    body { max-width: 72rem; margin: auto; padding: 2rem; }
    nav, section { margin-block: 1.5rem; }
    code { font-family: ui-monospace, monospace; }
  </style>
</head>
<body>
  <header><h1>Day XX Technical Sharpness Recap</h1><p>Status: not started</p></header>
  <nav aria-label="Source artifacts">
    <a href="lesson.md">Lesson</a> · <a href="quiz.md">Quiz</a> ·
    <a href="quiz-review.md">Quiz review</a> · <a href="experiment.md">Experiment</a> ·
    <a href="results.md">Results</a> · <a href="implementation/README.md">Implementation</a>
  </nav>
  <main>
    <section><h2>Problem and mental-model change</h2><p>Complete after the lesson.</p></section>
    <section><h2>Internals and visual explanation</h2><p>Complete after the lesson.</p></section>
    <section><h2>Quiz and implementation</h2><p>Complete after review.</p></section>
    <section><h2>Evidence and debugging</h2><p>No experiment has run.</p></section>
    <section><h2>Interview and architecture bridge</h2><p>Complete after reflection.</p></section>
    <section><h2>Next step</h2><p>Update from the roadmap and current session.</p></section>
  </main>
</body>
</html>
```

## Verification and publication

1. Confirm no `day-01` package exists before Day 1 begins.
2. Confirm the template contains all eight required artifact paths.
3. Validate `recap.html` as parseable HTML and inspect it visually in a browser.
4. Confirm quiz answers are not pre-generated.
5. Confirm the roadmap, lesson template, resume protocol, current session, and README all enforce the package.
6. Run `git diff --check`.
7. Show the user the resulting tree and policy before committing.
8. After approval, commit with `docs: add durable daily learning artifacts`, push the existing branch, and update PR #1.

## Assumptions

- HTML recaps are static and self-contained so they remain portable across machines.
- Markdown and implementation files remain the source of truth; HTML is a reviewed study view.
- Daily packages are created as days start or finish, not pre-created for all 56 days.
- A quiz review is produced only after the learner attempts the quiz.
