# PROJECT STATUS — MVP Menu Data (supporting repository)

**Snapshot:** 2026-10-30 · Baseline: `main` · GitHub/documentation review; no client download or app compatibility testing performed here.

## 1. Current playable state
**Not a playable game.** Public, versioned schema-1/v1 Italian menu JSON feed for the separate MVP Unity score sheet, with `latest.json`, immutable archived release(s), a standard-library validator, and GitHub Actions checks. The active Playtest 2 client is developed in `semiclipse/Meat-Vegetables-Pasta`, not this repository.

## 2. Last human-verified milestone
The repository records a successful `python3 tools/validate.py` run on October 17 for the existing v1 data. It does **not** record a fresh human-verified client-download / v2 compatibility acceptance.

## 3. Biggest unverified feature
The schema/endpoint compatibility path for v2. Do not allow incompatible v2 content to be served to v1 clients; never rewrite old release JSON.

## 4. Next specific task
Define a v2 endpoint/schema contract together with the Unity client owner, prove v1 clients cannot receive incompatible data, and only then propose a separately validated new revision. Preserve v1 `latest.json` and immutable `releases/` untouched until approved.

## 5. Active branches / PR blockers
No open PRs at snapshot. This repository's `docs/development/TASK_BOARD.md` marks v2 publication **blocked on app compatibility**; the Unity project has parallel `v2/playtest-2` and `codex/playtest2-mobile-app` development branches to reconcile.

---
**Maintenance:** Update on changed publishing capability, proven compatibility, newly validated release, or a blocker change; a successful JSON validator is not client acceptance.
