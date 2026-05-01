# Document Revision Guide — CCT → CT Rename

**Effective:** April 15, 2026
**Change:** All documents that used "CCT" or "Commitment Conservation Theory" must be updated

---

## Global Find-and-Replace Rules

| Find | Replace |
|------|---------|
| `Commitment Conservation Theory (CCT)` | `Commitment Theory (CT)` |
| `Commitment Conservation Theory` | `Commitment Theory` |
| `CCT` (as theory abbreviation) | `CT` |
| `cct-paper-roadmap` | `ct-publication-roadmap` |
| `CCT Propositions` | `CT Propositions` |

**Do NOT replace:**
- `Conservation Law of Commitment` — keep unchanged
- `Commitment Conservation Harness (CCH)` — keep unchanged (CCH is the measurement instrument, not the theory)

---

## File-by-File Instructions

### Paper 0 (Zenodo — Published)
- **Action:** Issue v.06 version update
- **Add note:** "v.06 Note on Naming (April 2026): The broader framework is now formalized as Commitment Theory (CT). The law remains the Conservation Law of Commitment. For the full prospectus, see P-000 DOI forthcoming."
- **Update keywords:** Add "commitment theory" to Zenodo metadata

### Experimental Record (Zenodo — Published)
- **Action:** Add note to README
- **Add note:** "Note on Framework Naming: The experiments documented in this record support the Conservation Law of Commitment, which is the first law of Commitment Theory (CT). Earlier references to 'CCT' are deprecated."
- **Update keywords:** Add "commitment theory" to Zenodo metadata

### L-000 (Legal Propositions — Draft)
- **File:** Rename to `L-000_CT_Legal_Propositions.md`
- **Title:** Change to "Propositions of Commitment Theory for Legal Applications"
- **Body:** Replace all "CCT" → "CT"
- **Add preface:** "Note on Naming: This document applies Commitment Theory (CT). CT's foundational prospectus is [P-000 DOI]. Earlier references to 'CCT' are superseded."
- **Add disambiguation §:** Per P-000 §2 language

### SLRO Essay (L-001 — Submission Ready)
- **Section V, first mention of CT:** Add footnote: "Commitment Theory (CT) is a falsifiable, empirically tested framework for meaning preservation. The law within the theory is the Conservation Law of Commitment. For the foundational prospectus, see [Author], Propositions of Commitment Theory: A Research Prospectus (Apr. 2026) (Zenodo DOI forthcoming). The term 'commitment' as used in CT is distinct from its use in cryptography, philosophy of language, and organizational psychology."
- **Remove:** Any remaining "CCT" references (search and verify)

### CT Roadmap (cct-paper-roadmap-v2.md)
- **Rename file:** `ct-publication-roadmap.md`
- **Title:** Change to "Commitment Theory — Complete Publication Roadmap"
- **Body:** Replace all "CCT" → "CT"
- **Add foundational premise note:** "Framework renamed from CCT to CT. See Naming_Architecture.md for rationale."

### Website (signomy.xyz)
- **governance page:** Update to reference "Commitment Theory (CT)" as underlying framework
- **vault page:** No change needed (Vault and MOÂ§ESâ¢ names unchanged)
- **All "CCT" references:** Update to "CT"

### GitHub Repository
- **URL:** https://github.com/SunrisesIllNeverSee/commitment-conservation (path unchanged — fine)
- **README:** Add naming note at top
- **Keywords/topics:** Add "commitment-theory"

---

## What Does NOT Change

| Item | Reason |
|------|--------|
| Conservation Law of Commitment | The law name is correct and distinct |
| Commitment Conservation Harness (CCH) | The instrument name — not the theory abbreviation |
| MOÂ§ESâ¢ architecture name | Unchanged |
| Six Fold Flame | Unchanged |
| Vault Artifact | Unchanged |
| Paper 0 title | Keep original published title |
| GitHub repo URL path | "commitment-conservation" is fine for the repo |

---

## Version Control Notes

When issuing updates to published Zenodo records:
- Keep all prior versions visible (Zenodo preserves version history)
- Add version label: "v.06 — CT Naming Update"
- Cross-link P-000 DOI in all updated records
- Do not delete or retract prior versions
