# Publishing Infrastructure — Session Context

Read this at the start of any session involving:

- Setting up a new author profile (ORCID integration, Lens, DataCite, OpenAIRE, etc.)
- Depositing a paper (Zenodo, SSRN, arXiv)
- Patent filing or status changes
- Updating identifiers across the program

---

## The Three Layers

```
Identity → Distribution → Discovery
  ORCID     Zenodo/SSRN     Lens/OpenAIRE/Crossref/DataCite
```

1. **Identity:** ORCID is the canonical author ID. Everything else either pushes to ORCID or is keyed off the ORCID iD.
2. **Distribution:** Where the artifact actually lives — Zenodo (preprints, datasets, anything with a DOI), SSRN (legal preprints), arXiv (CS/AI preprints), publisher journals (final published versions).
3. **Discovery:** Aggregators that index from Distribution and surface in Identity. **DataCite** indexes Zenodo. **OpenAIRE** indexes Zenodo + SSRN + EU repos. **Crossref** indexes publisher DOIs (journals). **The Lens** indexes patents + scholarly works.

## Why This Architecture Matters for CT

Commitment Theory has an unusual publication shape: a **patent** (Serial No. 63/877,177 — MO§ES™) plus a **theoretical research program** (the Conservation Law and 31 papers). Most ORCID services handle one but not both. **The Lens is the only ORCID integration that covers patents.** Without it, the patent and the science are not visibly linked — which matters because the IP strategy depends on showing that the open law and the proprietary implementation come from the same source.

## Author Identifiers — Priority Order

Set up in this order:

1. **ORCID** — canonical iD (https://orcid.org). Everything else connects to this.
2. **DataCite** — auto-pushes Zenodo DOIs to ORCID. Required if Paper 0 (Zenodo DOI 10.5281/zenodo.18792459) is to flow into ORCID at all.
3. **OpenAIRE** — broader catchment than DataCite alone. Pulls Zenodo + SSRN + EU sources. Free.
4. **The Lens** — only service that handles patents. Profile Builder tier (free, doesn't expire). Connect both researcher and inventor profiles.
5. **Crossref Metadata Search** — flip on after L-001 publishes in Stanford Law Review Online (or any journal).
6. **WoS / Scopus** — defer until needed for academic appointments. Both are paywalled and only index curated venues.

## Distribution — Where Things Get Deposited

| Item Type | Primary Venue | Why |
|-----------|---------------|-----|
| CT theoretical preprints (Paper 0, Papers 1-5, MOSES, etc.) | Zenodo | Free DOI, auto-flows to DataCite/OpenAIRE/ORCID |
| CS/AI preprints (Papers 1-5 specifically) | arXiv (after Zenodo) | Discipline-specific discovery |
| Legal preprints (L-000, L-007, L-008) | SSRN + Zenodo dual | SSRN reaches legal scholars; Zenodo gives DOI |
| Submitted journal papers (L-001 SLRO) | Publisher (Stanford LRO) — Zenodo postprint after | Publisher owns formal version; postprint preserves open access |
| Patents | USPTO (filed); The Lens (indexed) | Standard patent process |

## What to Track in DEPOSITS.md

For every deposit, record:

- **Date** of deposit
- **Item** (paper ID + version)
- **Venue**
- **DOI** (or other identifier)
- **Source file path** in this repo
- **License** at deposit (CC-BY 4.0 unless specified otherwise)
- **ORCID-attached?** (yes/no — must be yes for the auto-push to work)

## What to Track in PATENTS.md

For the patent track:

- Serial number
- Filing type (Provisional / Non-provisional / PCT / National Phase)
- Filing date
- Status (Pending / Office Action / Issued / Abandoned)
- Title
- Lens link (once indexed)
- Notes on prosecution actions

## Common Mistakes to Avoid

- **Don't deposit before ORCID iD is on the deposit form.** If you forget, the work won't auto-push to ORCID and you'll have to manually claim it later.
- **Don't deposit Paper 0 again on Zenodo.** It already has DOI 10.5281/zenodo.18792459. New versions go on the existing record as version updates, not as new deposits.
- **Don't put SSRN deposits before they have CT naming.** L-000 was drafted under "CCT" — must be CT before depositing or the deposit becomes a permanent record of outdated naming.
- **Don't store passwords here.** Account login info goes in your password manager. PROFILES.md tracks IDs and URLs only.

## Cross-References

- Active editorial work / writing todos → root [TODO.md](../TODO.md)
- Paper-specific deposit checklists → each paper's PAPER_PLAN.md
- Existing P-000 deposit checklist → [CT/papers/P-000_prospectus/P-000_Deposit_Checklist.md](../CT/papers/P-000_prospectus/P-000_Deposit_Checklist.md)
- Patent strategy memo → [CT/workspace/patent-strategy/Patent_Strategy.md](../CT/workspace/patent-strategy/Patent_Strategy.md)
