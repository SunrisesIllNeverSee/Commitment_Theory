# Paper 4 — Cross-Provider Fidelity: Conservation Law Generalization Across AI Providers and Architectures

**Track:** CT
**Layer:** 2 (Measurement Science)
**Status:** Planned — scoped to cross-provider + cross-architecture only (8–10 pages)
**Target Venue:** ACL / EMNLP
**Est. Length:** 8–10 pages
**Dependencies:** Papers 1–3
**Deferred to companion papers:** cross-language, cross-domain, cross-modality (see Scope Note)

---

## Abstract

The Conservation Law of Commitment makes a strong model-agnostic claim: C(T_gov(S)) = C(S) governs the transformation, not the model performing the transformation. This paper tests that claim empirically across AI providers (GPT-4, Claude, Gemini, Llama) and architectures (autoregressive transformers of varying scale). We apply the CT measurement harness with the Six-Gate Protocol governance structure and measure commitment conservation rates across providers and architectures on a shared signal corpus. The central prediction is that conservation rates under governance should be statistically indistinguishable across providers and architectures, while ungoverned decay rates may vary. We test the model-agnosticism prediction, characterize architecture-sensitive vs. governance-sensitive failure modes, and bound the scope conditions under which CT's model-agnostic claim holds. Cross-language, cross-domain, and cross-modality generalization are deferred to a companion paper — each is a full experimental program that warrants independent treatment.

---

## Outline

I. **Introduction** — States CT's model-agnosticism claim; motivates cross-provider/architecture empirical evidence as the first test; notes deferred dimensions.

II. **Experimental Design** — Describes the shared signal corpus; provider selection (GPT-4, Claude, Gemini, Llama); architecture range (varying scale within and across providers); governance protocol (Six-Gate Protocol, fixed ρ_g for cross-system comparability); confound controls (separating architecture effect from training data effect).

III. **Cross-Provider Results** — Conservation rates under governance across four providers; ungoverned decay rates across four providers; statistical test of model-agnosticism prediction; failure mode frequency distribution per provider.

IV. **Cross-Architecture Results** — Conservation rates across model scales (7B, 13B, 70B, 175B parameter ranges); tests whether ρ* varies by scale; identifies architecture-sensitive vs. governance-sensitive failure modes.

V. **Confound Analysis** — Separates architecture effect from training data effect; tests whether conservation differences across providers are attributable to architecture or corpus; discusses limitations.

VI. **Scope Conditions** — Characterizes the conditions under which model-agnosticism holds and does not hold; identifies which failure modes require architecture-specific governance extensions; discusses implications for CT's generality claim.

VII. **Toward Companion Papers** — Summarizes what cross-language, cross-domain, and cross-modality extensions would require; positions this paper as Paper 4a in a multi-paper cross-system program.

---

## Key Claims

- Under governance (Six-Gate Protocol, ρ_g ≥ ρ*), commitment conservation rates are statistically indistinguishable across AI providers and architectures — supporting CT's model-agnosticism claim within the cross-provider/architecture scope of this paper.
- Ungoverned commitment decay rates vary by architecture: some architectures are more semantically conservative than others, but none achieve conservation without governance.
- The nine-mode failure taxonomy from Paper 0 generalizes cross-architecturally: the same failure modes appear across providers, though their frequency distribution varies by provider and scale.
- Architecture effect and training data effect are separable confounds in cross-provider conservation rate differences; the paper characterizes the relative contribution of each.
- Cross-language, cross-domain, and cross-modality generalization are deferred to companion papers; this paper provides the cross-provider/architecture foundation on which those extensions build.

---

## Citation Notes

- **Cites:** Paper 0 (Conservation Law, failure taxonomy, model-agnosticism claim); Paper 1 (h_s for characterizing ungoverned decay by architecture); Paper 2 (Compression-Fidelity Bound as baseline); Paper 3 (ρ* as governance benchmark for cross-system comparison); P-000 (CT definitions)
- **Cited by:** Paper 5 (Measurement Instrument uses cross-system results to characterize oracle generalization); MO§ES architecture paper (cross-system fidelity is a design requirement for MO§ES); L-004 (policy brief uses cross-system evidence to argue for universal CT governance standard); GOV-001 (comparative governance analysis uses cross-system evidence)
