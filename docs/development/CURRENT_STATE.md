# Current setup baseline — 2026-10-17

This setup branch starts from `main` at `07c5511`. The repository contains `latest.json`, immutable `releases/italian-r000001.json`, standard-library `tools/validate.py`, and a GitHub Actions validation workflow. The checked-in feed is schema 1, revision 1, for the v1 rules. This setup pass did not publish data or test a client download.

`python3 tools/validate.py` passed during this setup inspection for the single release and current latest file.

The Unity project's active `v2/playtest-2` branch calls for changed ending and scoring behavior. Its handoff explicitly warns against putting that data into this live v1 feed before a compatible app build and endpoint/schema strategy. Treat that as a release blocker, not a request to rewrite `latest.json`. Use a separate task with app validation and human review for any publication.

## Handoff

Keep release 1 immutable. The local validator passed; no client download or v2 compatibility test was performed.
