# Deposits Log

Chronological record of every preprint, repository, or journal deposit. Add new rows at the top.

---

## Active Deposits

| Date | Item | Version | Venue | DOI / URL | License | Source File | ORCID Synced |
|------|------|---------|-------|-----------|---------|-------------|--------------|
| 2026-04-20 | P-000 — Propositions Prospectus | V.1 | Zenodo + SSRN | [10.5281/zenodo.20031715](https://doi.org/10.5281/zenodo.20031715) / [10.2139/ssrn.6734283](https://doi.org/10.2139/ssrn.6734283) | CC-BY 4.0 | [CT/papers/P-000_prospectus/](../CT/papers/P-000_prospectus/) | Y (manually added to ORCID) |
| 2026-03-19 | Paper 0 — Public Recursive Transformation Harness | 1.0.0 | Zenodo | [10.5281/zenodo.19109397](https://doi.org/10.5281/zenodo.19109397) | CC-BY 4.0 | (external — Commitment_Conservation/harness/) | Y (manually added to ORCID) |
| 2026-03-19 | Paper 0 — Conservation Law preprint | v.05 | Zenodo | [10.5281/zenodo.20029607](https://doi.org/10.5281/zenodo.20029607) | CC-BY 4.0 | (external — Commitment_Conservation/paper/v05/main.md) | Y (ORCID correct, verified via academic-sync audit) |
| 2026-03-19 | Paper 0 — Experimental Record (EXP-001 to EXP-007) | 1.0.0 | Zenodo | [10.5281/zenodo.19105225](https://doi.org/10.5281/zenodo.19105225) | CC-BY 4.0 | (external — experimental data) | Y (manually added to ORCID) |
| 2026-03-18 | Commitment Conservation in Financial Signals | v1.0 | Zenodo | [10.5281/zenodo.19102589](https://doi.org/10.5281/zenodo.19102589) | CC-BY 4.0 | (external) | Y (on ORCID, but Zenodo has WRONG ORCID — needs fix via web UI) |
| 2026-03-02 | Floating Moat Standard (FMS-2.0) | FMS-2.0 | Zenodo | [10.5281/zenodo.18841110](https://doi.org/10.5281/zenodo.18841110) | CC-BY 4.0 | (external) | Y (manually added to ORCID) |
| 2026-05-01 | L-001 — SLRO Essay | Submitted | Stanford Law Review Online (Vol. 79) | _[pending publication]_ | _[publisher TBD]_ | [Legal_Theory/papers/L-001_SLRO/Slro_paper_final.md](../Legal_Theory/papers/L-001_SLRO/Slro_paper_final.md) | _[N — flips Y after publication via Crossref]_ |

---

## Pending Deposits (Action Required)

| Item | Target Venue | Blocking Action | Owner |
|------|--------------|-----------------|-------|
| Paper 0 — v.06 update | Zenodo (existing record, new version) | Apply CT naming update across the v.05 source; add v.06 note | User |
| L-000 — Legal Propositions | SSRN + Zenodo | ✅ CCT→CT naming fixed. Ready to deposit via `academic-sync deposit` | User (generate PDF + run CLI) |

---

## Future Deposits (Calendar)

| Estimated Window | Item | Venue |
|------------------|------|-------|
| When written | Papers 1-5 | arXiv (CS/AI) + Zenodo |
| When written | MOSES Architecture | arXiv + Zenodo (with patent coordination) |
| When written | L-002 | SSRN + Zenodo |
| When written | L-007 | SSRN + Zenodo (after journal acceptance) |
| When written | CL-001, CL-002 | arXiv + ACL Anthology (after acceptance) |
| When written | IS-001 | Zenodo (preprint), then publisher (JASIST) |

---

## Deposit Checklist Template

Before any deposit, verify:

- [ ] Document is final (post-review, post-CT naming)
- [ ] ORCID iD is in the deposit form's author field
- [ ] License is set (CC-BY 4.0 unless otherwise specified)
- [ ] DOI / version note is added to internal references (PAPER_PLAN.md citation notes)
- [ ] Cross-references to other CT papers use updated DOIs
- [ ] Deposit file (PDF or markdown source) matches the working copy in repo
- [ ] Declaration of Interest, Funder, Ethics statements ready (for SSRN especially)

After deposit:

- [ ] Add row to the table above
- [ ] Note the DOI in the paper's PAPER_PLAN.md citation notes
- [ ] Verify ORCID record updates within 24 hours; if not, manually trigger sync via The Lens / OpenAIRE / DataCite
- [ ] Update root [TODO.md](../TODO.md) if this completes a tracked todo

---

## Known Zenodo Metadata Issues (as of 2026-06-30)

Verified via `academic-sync audit` (5 surfaces: Zenodo, ORCID, Crossref, DataCite, OpenAIRE).

| Deposit | Issue | Fix | Method |
|---------|-------|-----|--------|
| 19102589 (Financial Signals) | Wrong ORCID on creator (`0009-0007-3367-9864`) | Fix to `0009-0002-9904-5390` | Zenodo web UI (API has format migration issue) |
| 19109397 (Harness) | Missing ORCID on creator | Add `0009-0002-9904-5390` | Zenodo web UI |
| All 6 deposits | Zero related identifiers (cross-links) | Add 10 cross-links across 4 deposits | Zenodo web UI or `academic-sync fix-crosslinks` |
| All 6 deposits | Not in any Zenodo community | Join communities (see below) | Zenodo web UI |

**Note:** The Zenodo API has a metadata format migration issue — old records use
`name`/`affiliation` format, new version drafts need `person_or_org.family_name`
format. The API doesn't auto-convert, causing 500 errors. The Zenodo web UI
handles this automatically. Use the web UI for metadata edits until Zenodo
fixes the API.

### Communities to Join

| Community | UUID | Relevance |
|-----------|------|-----------|
| Zenodo (general) | `7647d230-c830-4664-a4c8-9afd95fc5003` | All deposits |
| OpenAIRE | `ba70ad9d-2576-43ee-a438-ad42b4249797` | All deposits (auto-indexing) |
| Natural Language Processing | `3eec7ae6-7230-439d-b9eb-58b23297fa67` | Conservation Law, Experimental Record, Harness |
| Machine Learning | `a08bc0ac-2893-4afd-870a-a77bd348c84c` | Conservation Law, Harness |
| Open Science | `8b1df34a-6496-448c-b109-7cff4f9572b1` | All deposits |

### OpenAIRE Status

All 6 deposits are indexed in OpenAIRE. Resource types are correct (Dataset,
Software, Preprint). ORCID not yet picked up by OpenAIRE (harvesting lag —
will resolve on next harvest cycle after Zenodo ORCID fixes are applied).
