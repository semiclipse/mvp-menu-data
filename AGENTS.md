# MVP menu data agent guide

This public repository publishes recipe/scoring JSON for Meat. Vegetables. Pasta.; it is not the Unity app. The [README](README.md) defines the schema, export/publish flow and rollback rule. The active Unity Playtest 2 branch has a different rules direction; inspect [current setup baseline](docs/development/CURRENT_STATE.md) before proposing menu updates.

Edit `latest.json` and a new immutable `releases/italian-rNNNNNN.json` together only for an authorized compatible publication. Preserve stable recipe IDs, revision ordering and published archives. Run `python3 tools/validate.py`; the GitHub Actions workflow also checks release history. There are no Unity scenes, Editor tests or device checks here; verify app compatibility separately in the Unity repository.

Read [task board](docs/development/TASK_BOARD.md), [workflow](docs/development/AI_WORKFLOW.md) and [task template](docs/development/TASK_TEMPLATE.md). Check Git status and baseline, use a scoped branch, record exact validation, and request review of data and app compatibility before integrating. Never edit old release files, reduce the revision, add player data/secrets, or publish a v2 schema into the v1 endpoint without explicit authorization and a compatible app route.
