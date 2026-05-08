# publishing

Author identity, deposit infrastructure, and patent tracking for the Commitment Theory program. This is **not** where papers live — papers live in `CT/`, `Legal_Theory/`, and `MISC/`. This folder tracks the *distribution and identity layer* underneath them.

## Files

| File | Purpose |
|------|---------|
| [CLAUDE.md](CLAUDE.md) | Session context — read this when working on any profile setup, deposit, or patent action |
| [PROFILES.md](PROFILES.md) | Master table of every author identifier (ORCID, Lens, DataCite, OpenAIRE, Zenodo, SSRN, Crossref, WoS, Scopus) with status, IDs, URLs, and ORCID sync state |
| [DEPOSITS.md](DEPOSITS.md) | Chronological log of every preprint/repository deposit with DOI, version, date, and source file path |
| [PATENTS.md](PATENTS.md) | Patent filing log — serial numbers, status, dates, Lens links |

## What goes here vs. elsewhere

| Belongs here | Belongs elsewhere |
|--------------|-------------------|
| ORCID iD setup notes | Paper drafts → track folders |
| Lens / DataCite / OpenAIRE account info | Source threads → source-threads/ |
| Zenodo deposit DOIs and dates | Active editorial todos → root TODO.md |
| Patent serial numbers and prosecution status | Pipeline outputs → academic-research/pipeline/ |
| Account credentials reminders (NOT passwords) | Submitted manuscripts → Legal_Theory/papers/[paper]/ |

## Workflow

When something gets a new identifier, deposit, or patent action:

1. Update the relevant file (PROFILES, DEPOSITS, or PATENTS)
2. Cross-reference from the affected paper's `PAPER_PLAN.md` (e.g., add the Zenodo DOI to citation notes)
3. If it changes ORCID state, also note in `PROFILES.md`
