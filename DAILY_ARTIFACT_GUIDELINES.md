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

Use `daily-artifacts/_template/recap.html` as the required interactive shell for every completed day. Primary navigation must stay inside the HTML study experience; links to Markdown, implementation, experiments, results, and backlog belong in a secondary **Source files and evidence provenance** area.

Use progressive enhancement: the complete lesson must remain readable when JavaScript is unavailable. Meaningful interaction may support internal navigation, study-mode filtering, search, disclosure, and interview practice; avoid decorative animation that does not improve learning. Preserve semantic landmarks, keyboard operation, visible focus, reduced-motion support, responsive layout, adequate contrast, honest evidence labels, and resolvable source links.

Every new completed tutorial at `daily-artifacts/day-XX/recap.html` must be linked from the root `index.html` in the same change. It must include a declared document language, a non-empty title, a viewport meta tag, and an `<h1>` heading. Run `python3 scripts/validate_tutorial_index.py` before committing; GitHub Pages deployment must fail when a completed tutorial is missing from the index or any of these accessibility basics is absent.

## Completion rule

A day is complete only when its package is reviewed, the HTML renders correctly, the tutorial is linked from `index.html`, `scripts/validate_tutorial_index.py` passes, evidence is honest, `CURRENT_SESSION.md` is updated, and everything is committed and pushed. If an artifact is not applicable, explain why in `lesson.md` rather than leaving an ambiguous placeholder.
