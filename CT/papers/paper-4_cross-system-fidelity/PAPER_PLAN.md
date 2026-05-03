# Paper 4 — Cross-System Fidelity: Conservation Law Generalization Across AI Architectures, Providers, and Modalities

**Track:** CT
**Layer:** 2 (Measurement Science)
**Status:** Planned
**Target Venue:** ACL / EMNLP / Applied AI venues
**Est. Length:** 8–10 pages
**Dependencies:** Papers 1–3

---

## Abstract

The Conservation Law of Commitment makes a strong model-agnostic claim: C(T_gov(S)) = C(S) governs the transformation, not the model performing the transformation. This paper tests that claim empirically across multiple AI providers (GPT-4, Claude, Gemini, Llama), architectures (autoregressive transformers of varying scale), languages (English, Spanish, French, Mandarin), domain types (legal, medical, contractual, bureaucratic), and modalities (text, structured data, speech-to-text). We apply the CT measurement harness (Paper 5 framework) with the Six-Gate Protocol governance structure and measure commitment conservation rates across each dimension. The central prediction of CT's model-agnosticism is that conservation rates under governance should be statistically indistinguishable across providers and architectures, while ungoverned decay rates may vary by architecture. We report results for each cross-system dimension, test the model-agnosticism prediction, and characterize the cases where conservation fails to generalize — identifying which failure modes (from the nine-mode taxonomy) are architecture-sensitive and which are governance-sensitive. The paper also tests cross-language generalization: does the Conservation Law hold when the semantic object is transformed across language boundaries? Results have implications for the deployment of CT governance in multilingual and multimodal AI systems and confirm or bound the scope of CT's model-agnostic claim.

---

## Outline

I. **Introduction** — States CT's model-agnosticism claim and motivates the need for cross-system empirical evidence.

II. **Experimental Design** — Describes the signal corpus, provider selection, architecture range, language selection, and domain types; explains the cross-modality protocol for speech-to-text inputs.

III. **Cross-Provider Results** — Reports commitment conservation rates under governance across GPT-4, Claude, Gemini, and Llama; tests the model-agnosticism prediction statistically.

IV. **Cross-Architecture Results** — Reports conservation rates across architectures of varying scale; tests whether governance density requirements (ρ*) vary by architecture.

V. **Cross-Language and Cross-Domain Results** — Reports conservation rates across languages and domain types; identifies failure modes that are language-sensitive or domain-sensitive.

VI. **Cross-Modality Results** — Reports conservation rates for speech-to-text modality transitions; characterizes the additional governance requirements for modality-crossing transformations.

VII. **Implications for CT's Model-Agnosticism Claim** — Assesses the overall evidence for and against model-agnosticism; identifies the scope conditions under which the Conservation Law generalizes and the conditions under which it requires extension.

---

## Key Claims

- Under governance (Six-Gate Protocol, ρ_g ≥ ρ*), commitment conservation rates are statistically indistinguishable across AI providers and architectures — supporting CT's model-agnosticism claim.
- Ungoverned commitment decay rates vary by architecture: some architectures are more semantically conservative than others, but none achieve conservation without governance.
- Cross-language commitment conservation holds for languages with robust modal and deontic vocabulary but degrades for languages or registers with underspecified modal systems.
- Cross-modality transitions (speech-to-text, structured-to-prose) require higher governance density (ρ_g > ρ*_text) to achieve conservation — the modality boundary introduces additional entropy.
- The nine-mode failure taxonomy from Paper 0 generalizes cross-architecturally: the same failure modes appear across providers, though their frequency distribution varies.

---

## Citation Notes

- **Cites:** Paper 0 (Conservation Law, failure taxonomy, model-agnosticism claim); Paper 1 (h_s for characterizing ungoverned decay by architecture); Paper 2 (Compression-Fidelity Bound as baseline); Paper 3 (ρ* as governance benchmark for cross-system comparison); P-000 (CT definitions)
- **Cited by:** Paper 5 (Measurement Instrument uses cross-system results to characterize oracle generalization); MO§ES architecture paper (cross-system fidelity is a design requirement for MO§ES); L-004 (policy brief uses cross-system evidence to argue for universal CT governance standard); GOV-001 (comparative governance analysis uses cross-system evidence)
