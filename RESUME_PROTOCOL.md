# New-Session Resume Protocol

Committed GitHub state is the source of truth. Conversation memory may supplement it but must never silently override it.

## Read in order

1. `CURRENT_SESSION.md`
2. the most recent completed package under `daily-artifacts/day-XX/`, including `recap.html` and source artifacts
3. `LEARNING_GUIDELINES.md`
4. `CODING_PRACTICE_GUIDELINES.md`
5. `ROADMAP.md`
6. the current week's README/material
7. the current enterprise challenge
8. relevant experiment results
9. `ARCHITECTURE_LAB_BRIDGE.md`

## Resume response

Before continuing, state:

1. where the learner stopped;
2. completed versus incomplete work;
3. unresolved evidence and questions;
4. the next roadmap topic;
5. any repository inconsistency that must be resolved.

Continue without resetting the program. At the end of every meaningful session, update `CURRENT_SESSION.md` with completed concepts/code/experiments, measured evidence, unresolved questions, project state, interview gaps, artifacts, next lesson, and recommended resume files. At the end of every completed day, also verify and commit the required `daily-artifacts/day-XX/` package.
