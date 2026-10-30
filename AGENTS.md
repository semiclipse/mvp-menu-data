# MVP menu data agent guide

This public repository publishes recipe/scoring JSON for Meat. Vegetables. Pasta.; it is not the Unity app. The [README](README.md) defines the schema, export/publish flow and rollback rule. The active Unity Playtest 2 branch has a different rules direction; inspect [current setup baseline](docs/development/CURRENT_STATE.md) before proposing menu updates.

Edit `latest.json` and a new immutable `releases/italian-rNNNNNN.json` together only for an authorized compatible publication. Preserve stable recipe IDs, revision ordering and published archives. Run `python3 tools/validate.py`; the GitHub Actions workflow also checks release history. There are no Unity scenes, Editor tests or device checks here; verify app compatibility separately in the Unity repository.

Read [task board](docs/development/TASK_BOARD.md), [workflow](docs/development/AI_WORKFLOW.md) and [task template](docs/development/TASK_TEMPLATE.md). Check Git status and baseline, use a scoped branch, record exact validation, and request review of data and app compatibility before integrating. Never edit old release files, reduce the revision, add player data/secrets, or publish a v2 schema into the v1 endpoint without explicit authorization and a compatible app route.

## Portfolio Pulse status maintenance

The root [PROJECT_STATUS.md](PROJECT_STATUS.md) is the short, evidence-based **portfolio checkpoint**, not a replacement for the design document, roadmap, issue tracker, or task board. Read it alongside the latest branch/PR state at the start of a new task; the snapshot may be stale.

**Update PROJECT_STATUS.md in the same scoped branch/PR when** a meaningful feature milestone is integrated; a creator actually verifies or rejects a milestone; the biggest unverified feature, next specific task, or branch/PR blocker materially changes. Do **not** rewrite it for every micro-commit, docs typo, or routine refactor. A status update should be small and reviewed with the change that warrants it.

Keep exactly these five easy-to-scan headings: **Current playable state; Last human-verified milestone; Biggest unverified feature; Next specific task; Active branches / PR blockers.** Put an as-of date and baseline branch near the top. Separate **implemented**, **automated-tested**, **Unity Editor/simulator-tested**, **real-device or human-playtested**, and **proposed**; for this data repository, the first heading means delivery capability, not gameplay. Never claim an unrun test, unobserved visual, or unapproved rule is verified. On feature branches, say explicitly what remains unmerged; never imply that branch-only work is on `main`.

When the task board or old current-state notes disagree with GitHub history, flag the conflict and reconcile with actual code/PR evidence rather than silently marking stale work complete. Preserve save/version compatibility and release blockers. The point is to let ChatGPT's **Portfolio Pulse** review locate the true next move in seconds. Codex reads this through `AGENTS.md`; Claude reads this guide through `CLAUDE.md`.
