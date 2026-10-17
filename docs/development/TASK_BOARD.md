# MVP menu data task board — 2026-10-17

Follow the [README](../../README.md) contract. Use [the task template](TASK_TEMPLATE.md) for a proposed update.

| Priority | Status | Task and acceptance gate | Dependencies / area |
|---|---|---|---|
| P1 | Blocked on app compatibility | Decide Playtest 2 schema/endpoint route. Acceptance: v1 clients cannot consume v2 rules and v2 client validates chosen route. | Unity `v2/playtest-2`; feed/client code |
| P2 | Ready when compatible | Publish a new revision. Acceptance: stable IDs, matching latest/new archive, validator and app preview pass; old archives unchanged. | Compatible client/data contract; JSON, CI |
