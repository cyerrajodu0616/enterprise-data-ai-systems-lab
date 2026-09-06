# LAB-015 — Delta CDC MERGE Correctness, Performance, and Concurrency

- Status: TODO / NOT RUN
- Backlog: [LAB-015](../../LAB_BACKLOG.md)
- Environment/setup: TODO / NOT RUN
- Execution: TODO / NOT RUN
- Measurements: TODO / NOT RUN

## Hands-on checklist

- [ ] Generate CDC test events containing duplicates and out-of-order events.
- [ ] Deduplicate by authoritative `source_sequence`; quarantine equal-sequence/different-payload input.
- [ ] Implement sequence-guarded `MERGE`.
- [ ] Test duplicate retries, matched deletes, unmatched-delete tombstones, late updates after deletion, legitimate reactivation, and terminal-delete quarantine.
- [ ] Test independent versus dependent later events.
- [ ] Capture rows updated, copied, inserted, and deleted.
- [ ] Capture files scanned and rewritten where exposed.
- [ ] Measure logical change volume versus physical rewrite volume.
- [ ] Simulate or document concurrent-writer conflict behavior for the actual runtime/table configuration.
- [ ] Implement deterministic, checkpointed, resumable backfill chunks.
- [ ] Verify correctness before and after any layout change.

## Expected assertions—not results

- Lower/equal sequences never overwrite newer state; equal-sequence conflicting payload is quarantined.
- Tombstones prevent late resurrection; policy controls higher-sequence reactivation.
- Retrying the same immutable batch produces the same state.
- A dependent event blocks only its key; unrelated keys continue.
- Conflicting failed transactions leave no partial table version.
- Layout and coordination changes preserve identical customer state and accepted sequence.
- Both CDC and backfill SLAs must pass before accepting workload coordination.

All assertions remain predictions until LAB-015 is executed.
