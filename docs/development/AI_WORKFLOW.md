# Multi-agent development workflow

GitHub branches, pull requests, and repository documents are the durable record. Chat history and agent identity are not project authority. Read `AGENTS.md`, the linked design and current-state documents, and the relevant code before taking a task.

## Start a task

Use [TASK_TEMPLATE.md](TASK_TEMPLATE.md) for substantial work. Give it an ID, player outcome, scope, affected files, acceptance criteria, dependencies, and checks. Inspect `git status`, current branch, and recent commits before editing. Preserve uncommitted work. Use a scoped branch from the appropriate current baseline; do not silently switch a collaborator's checkout.

For sequential work, the first agent stops writing and records branch, commit, changed files, results, and next steps in the task or a concise `HANDOFF.md`. The next agent inspects the branch and diff before continuing. If an agent loses access or time, leave a coherent partial commit when appropriate and identify unfinished or unverified work. A provider change requires no special conversion.

For parallel work, use separate branches and separate clones or Git worktrees. Assign nonoverlapping files and integration points up front. Never let agents edit the same working tree at once. Coordinate shared scene, prefab, package, and asset files serially. If branches conflict, inspect both intentions and resolve on an integration branch; rerun affected checks and Unity inspection. Preserve recoverable partial work before retrying a failed approach.

## Review and integrate

Open a GitHub pull request with the task outcome, acceptance criteria, changed areas, tests actually run, and manual gates. A reviewer compares the diff to the task and architecture, checks regressions and maintainability, and recommends merge, revision, or rejection. Major gameplay, architecture, save/network, and risky Unity asset changes merit independent review and real Editor/device testing. Trivial documentation changes can use a lighter review. Human approval is required before significant changes enter `main`; do not force-push, rewrite history, alter releases, or change protected settings as a convenience.

Report code compilation, automated tests, Editor Play, standalone build, visual inspection, controller, network, and device checks separately. Never infer a runtime result from syntax or compilation alone. Update the task status and current-state document only with evidence from the checked-out branch.
