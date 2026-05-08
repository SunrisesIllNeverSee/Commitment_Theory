# Publishing Automation

Tooling for keeping the publishing layer (DEPOSITS.md, ORCID, DataCite, OpenAIRE, Lens) in sync. Designed to be portable: when this folder eventually moves to `~/Desktop/Publishing_Hub/automation/`, paths resolve relative to the script so nothing breaks.

## Scripts

### `sync_check.py` — drift detector

Pulls live state from public APIs and diffs against `publishing/DEPOSITS.md`. Reports:

- DataCite works missing from `DEPOSITS.md` (you deposited but didn't log)
- DOIs in `DEPOSITS.md` not on DataCite (typos / stale / non-DataCite registrar)
- DataCite works missing from ORCID (auto-push gap — fix at orcid.org settings)
- DataCite works missing from OpenAIRE (harvester lag — usually self-resolves)
- Possible duplicate deposits (same title, multiple DOIs — the FMS-2.0 / P-000 case)

**Run:**

```bash
python3 publishing/scripts/sync_check.py
python3 publishing/scripts/sync_check.py --report publishing/sync_report.md
python3 publishing/scripts/sync_check.py --skip-openaire   # if OpenAIRE is slow
```

**Requirements:** Python 3.10+. No external packages. No API keys. All endpoints are public read-only.

**ORCID iD is hard-coded** at the top of the script. If you ever set up a second ORCID account or a co-author wants their own report, edit `ORCID_ID` (or accept that as a future CLI flag).

## Suggested cadence

- Weekly during active publishing cycles (Paper 0 versions, P-000, L-001 submission)
- Before any new Zenodo deposit — confirms the previous deposit synced before adding a new one
- Monthly otherwise

## When to move to Publishing_Hub

Once `sync_check.py` has been run successfully against the live record and the output matches expectations, this whole folder is ready to migrate to `~/Desktop/Publishing_Hub/automation/`. The script's `SCRIPT_DIR` / `PUBLISHING_DIR` resolution means you only need to update the parent `DEPOSITS.md` path or move `DEPOSITS.md` along with it.
