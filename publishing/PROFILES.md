# Author Profiles — Master Table

**Author of record:** Deric J. McHenry
**Affiliation:** Ello Cello LLC

---

## Active Profiles

| Service | Status | ID / URL | ORCID-Connected | Notes |
|---------|--------|----------|-----------------|-------|
| ORCID | _[in progress]_ | _[paste your ORCID iD here, format: 0000-0000-0000-0000]_ | — (this IS the canonical iD) | The root identity. Every other service connects to this. |
| The Lens | _[in progress]_ | _[paste Lens Profile URL here]_ | _[Y / N]_ | Profile Builder tier. **Combined researcher + inventor profile.** Only ORCID service that covers patents. Set up 2026-05-05. |
| DataCite | _[pending]_ | — | _[Y / N]_ | Auto-handles Zenodo DOIs once ORCID is on the deposit. No separate account needed — it's a passive integration. |
| OpenAIRE | _[pending]_ | _[OpenAIRE profile URL]_ | _[Y / N]_ | Pulls Zenodo + SSRN + EU sources. Free. Recommended. |

## Deferred (set up later)

| Service | When to set up | Why deferred |
|---------|----------------|--------------|
| Crossref Metadata Search | After L-001 publishes in Stanford Law Review Online | Crossref indexes publisher DOIs only — nothing to index until a journal publishes you |
| Scopus / Elsevier | Only if needed for academic appointment | Paywalled, only indexes curated venues, irrelevant unless an h-index is being requested |
| Web of Science | Only if needed for academic appointment | Same as Scopus. Stanford LRO online supplement may or may not be in Emerging Sources Citation Index — check after publication. |
| HAL | Skip unless you have French-affiliated co-authors | French open-archive |
| JaLC | Skip unless you have Japanese-affiliated co-authors | Japan DOI registry |
| Redalyc | Skip | Spanish/Portuguese journals only |
| MLA Bibliography | Skip | Humanities citation index — not relevant for CT/AI/legal |
| Research Data Australia | Skip | Australian datasets only |
| BASE (Bielefeld) | Skip — duplicates OpenAIRE coverage | Open-access aggregator, redundant with OpenAIRE |
| DOE OSTI.GOV | Skip | US Dept. of Energy works only |
| DNB (German National Library) | Skip | German publications only |
| GND Network | Skip | German library authority |
| ISNI | Skip | Mostly redundant with ORCID |

---

## ORCID Sync Status

When each service is connected, mark which ones successfully pushed to ORCID:

| Service | Push Direction | Confirmed working |
|---------|----------------|-------------------|
| The Lens | Lens → ORCID | _[Y / N / pending]_ |
| DataCite | DataCite → ORCID | _[Y / N / pending]_ |
| OpenAIRE | OpenAIRE → ORCID | _[Y / N / pending]_ |

To verify a sync worked: visit `orcid.org/[your-iD]`, check the "Works" section, look for the source field on each entry — it should name the service that pushed it.

---

## ORCID Record Contents (Target State)

When fully set up, your ORCID record should display:

**Works:**
- Paper 0 — Conservation Law preprint (Zenodo DOI 10.5281/zenodo.18792459) — source: DataCite
- P-000 — Propositions Prospectus (when deposited to Zenodo) — source: DataCite
- L-000 — Legal Propositions (when deposited to SSRN + Zenodo) — source: OpenAIRE / DataCite
- L-001 — SLRO Essay (when published) — source: Crossref
- Each future paper as it deposits

**Patents:**
- Serial No. 63/877,177 (Provisional) — source: The Lens

**Identifiers:**
- ORCID iD (canonical)
- Lens Profile ID
- Possibly: DataCite ID, OpenAIRE ID

---

## Update Protocol

Edit this file whenever:

- A profile is created → add row, mark status
- A profile syncs to ORCID → update the sync table
- A profile is abandoned/canceled → mark status as "Inactive" with date
- A new identifier is added → add row to the appropriate section

Do **not** store passwords, API keys, or credentials in this file. IDs and URLs only.
