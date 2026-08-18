# Migration Map — Commitment_Theory

**Installed:** 2026-08-18
**Mode:** migrate
**Profile:** research

## Existing structure preserved

All existing root directories declared in `allowed_root_dirs_extra`:
- `academic-research/`, `CT/`, `inbox/`, `Legal_Theory/`, `MISC/`,
  `pipeline/`, `publishing/`, `source-threads/`

## Existing root files preserved

- `FULL_WORKFLOW_PROMPT.md` — workflow prompt document
- `TODO.md` — task list

## Pre-existing coordination

No prior `system-devin/`, `.coord/`, or `Devins_Plans/` existed.
No prior `AGENTS.md` existed — standard AGENTS.md installed fresh.
Canonical DREP installed at `system-devin/`.

## Canon context

- Authority role: `evidence_source`
- Canon contexts: `commitment-theory`
- Authority owner: `search_authority`

## Migration steps (before enforce)

1. [ ] Clean `_final` version-suffix duplicates in paper directories
2. [ ] Resolve duplicate paper copies across directories
3. [ ] Remove or archive `CT.zip` at root if present
4. [ ] Remove or archive BFG report if tracked
5. [ ] Move loose root docs (`FULL_WORKFLOW_PROMPT.md`, `TODO.md`) to `docs/`
6. [ ] Run `repo_check.py --ci` until clean
7. [ ] Switch REPO.yaml mode from `migrate` → `enforce`

## Enforce readiness

NOT READY — requires migration steps above.
