# MVP menu data

Public recipe and scoring updates for Meat. Vegetables. Pasta.
This repository contains published menu data and its validation tools. The Unity
app source, player saves, notes, credentials and signing files do not belong here.

**Download:** https://raw.githubusercontent.com/semiclipse/mvp-menu-data/main/latest.json

## Publish a balance update

1. In the private Unity project, stop Play Mode. Edit the nine recipe assets and
   **MVP > Select Menu and Scoring**. Keep recipe IDs stable when renaming dishes.
2. Increase **Menu Revision** (1, 2, 3...) and update **Menu Version** (e.g. 1.0.1)
   and **Release Notes**. Revision controls ordering; version is the player label.
3. Choose **MVP > Export Menu Update**, selecting this repository's local folder.
   Unity writes `latest.json` and a new `releases/italian-rNNNNNN.json`.
4. Run `python3 tools/validate.py`, then review, commit and push both JSON files
   together. GitHub Actions repeats validation and detects rewritten archives.
5. Players choose **Menu > Menu updates > Check for updates**, then **Use for
   future sheets**. Start a new sheet to use the new recipes. The version appears
   below MVP on the sheet. Existing games keep their recipe/scoring snapshot.

You can also edit the JSON directly or ask the connected assistant to publish a
new menu. Copy the latest file, increase revision, modify the data, validate and
write identical latest/archive files in one commit. Menu data downloaded by the
app does not edit the private Unity Inspector assets; keep those in sync when
working in both places. The app selects the highest valid cached/bundled revision.

## Roll back a bad balance change

Copy an earlier archived menu into a **new, higher revision**. Add notes explaining
the rollback, update its version label, validate and publish it as above. Never
change or delete a published archive or reduce the latest revision.

## Data contract (schema 1)

- `schemaVersion`: 1. Incompatible formats require an app update/new schema.
- `menuId`: `italian`; `revision`: positive integer; `version`: up to 24 letters,
  digits, dots, underscores or hyphens, beginning with a letter or digit.
- `title`: 1–80 characters; `notes`: up to 400 characters.
- `recipes`: exactly nine, left-to-right/top-to-bottom. Each has a stable lowercase
  `id` (up to 64 letters/digits/_/-), `title` (1–64), `description` (0–400),
  `points` (0–1000), and `costs` containing `ingredient` + `amount` pairs.
- Ingredient names: `Meat`, `Vegetables`, `Pasta`, `Seafood`, `Cheese`, `Sauce`.
  Each type appears at most once per dish; each quantity is 1–12, total 1–24.
- `columnNames`, `rowNames`: three labels each (1–32 characters).
- `columnIngredients`: three valid ingredient names for the column icons.
- `scoring`: `wastePenalty`, `rowBonus`, `columnBonus`, `firstServiceBonus` (0–1000),
  `closingThreshold` (1–20), `ruinedCountsForCollections` and
  `allResolvedTriggersClosing` (booleans).
- Limit: 128 KiB UTF-8 per menu. No new ingredients, artwork, code or URLs inside
  menu data. New mechanics, artwork, app controls or board sizes require an app build.

## Delivery behavior

The app checks only when asked, downloads without authentication, previews the
update, validates it before saving, and caches it for offline use. Failed checks
keep the existing menu. A corrupt primary cache falls back to a valid backup or
bundled menu. GitHub's raw-file cache may delay visibility briefly: retry later.

This is a lightweight feed for a small playtest group, not a live multiplayer
service. For larger distribution we can keep the schema and archived releases
and move the endpoint to a CDN in a future app build. This repository is public
and readable by anyone. No player data is sent to it.

## Validation

`python3 tools/validate.py` uses only Python's standard library. CI also compares
release archives to the prior commit. To make CI a mandatory merge gate, configure
GitHub branch protection/rulesets; merely adding a workflow does not prevent a
repository owner from pushing invalid data. The app independently validates feeds.
