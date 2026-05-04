# Paper 0 — A Conservation Law for Commitment in Language Under Recursive AI Transformation

**Track:** CT
**Layer:** 1 (Physical Law)
**Status:** Published v.05 (Zenodo DOI: 10.5281/zenodo.18792459); v.06 naming update pending
**Target Venue:** Zenodo preprint; targeting NeurIPS / ICML / AI journal
**Est. Length:** 8,000–12,000 words
**Dependencies:** None (foundational)

---

## Abstract

This paper establishes a conservation law for semantic commitment in language under recursive AI transformation. We define the commitment kernel C(S) of a semantic object S as its deontic core — the obligations, prohibitions, permissions, and modal constraints that constitute its action-binding content — and prove that under governed transformation T_gov, C(T_gov(S)) = C(S): the commitment kernel is conserved. Under ungoverned transformation, we demonstrate empirically that commitment decays monotonically, yielding a candidate Second Law of Semantic Entropy (ΔH_C > 0). The Conservation Law is established through seven experiments (EXP-001 through EXP-007) using a public measurement harness with NLI bidirectional entailment (microsoft/deberta-v3-base-mnli) as oracle. Key results: 13 of 20 signals achieved NLI bidirectional entailment score of 1.00 across 10 recursive transformation iterations under the gate condition (EXP-003). A negation probe (EXP-007) demonstrates that the harness distinguishes semantic commitment from lexical surface form — Jaccard similarity degraded while NLI remained at 1.00 for 3 of 4 signals, confirming that conservation is a property of meaning, not of wording. Theorem 6.2 implies the Second Law candidate. A nine-mode failure taxonomy characterizes the ways commitment degrades under ungoverned transformation. We establish oracle independence as a design property: the Conservation Law is testable with any oracle that supports bidirectional entailment. The harness is public and all results are reproducible; this paper is an invitation to falsify.

---

## Outline

I. **Introduction** — Frames the problem of semantic drift under AI transformation and states the Conservation Law as the paper's central contribution.

II. **Formal Framework** — Defines the commitment kernel C(S), governed transformation T_gov, the Six-Gate Protocol (G1–G6), and the measurement oracle; distinguishes commitment kernel from meaning-in-general.

III. **Experimental Design** — Describes the measurement harness, signal corpus (EXP-001 through EXP-007), oracle selection rationale, and replication protocol.

IV. **Results** — Reports experimental outcomes: EXP-003 (10-step recursion, 13/20 signals at NLI=1.00 under gate condition), EXP-007 (NP-negation probe distinguishing commitment from surface form), and EXP-006 (self-referential recursion failure: 2/4 paper claims survive, establishing failure mode 9).

V. **The Conservation Law and Second Law** — States and proves Theorem 6.1 (Conservation Law) and Theorem 6.2 (Second Law candidate); connects the decay function to Shannon entropy rate.

VI. **Failure Taxonomy** — Enumerates and characterizes the nine failure modes: obligation escalation, scope widening, exception dropping, modal flattening, threshold erasure, agent substitution, negation reversal, compression collapse, and recursion drift.

VII. **Oracle Independence and Falsifiability** — Demonstrates that the Conservation Law does not depend on the specific oracle implementation; states falsification conditions explicitly and directs readers to the public harness.

---

## Key Claims

- The commitment kernel C(S) is formally definable and operationally measurable using NLI bidirectional entailment as an oracle, independently of any particular model or architecture.
- Under governed transformation (Six-Gate Protocol), the commitment kernel is conserved across recursive iteration: 13/20 signals achieved perfect conservation across 10 recursive steps.
- Under ungoverned transformation, commitment decays monotonically — the rate and character of this decay constitute the empirical foundation for the Second Law of Semantic Entropy.
- The harness distinguishes semantic commitment from lexical surface form: the NP-negation probe (EXP-007) shows that lexical similarity can degrade while commitment is preserved, and vice versa.
- The Conservation Law is falsifiable: a single well-constructed experiment demonstrating commitment conservation without governance would refute it, and the public harness makes such an attempt tractable.

---

## Writing Notes

**Related Work (required — absence triggers desk rejection at NeurIPS/ICML):**

- Faithfulness metrics in NLG evaluation: Maynez et al. (2020) on faithfulness/factuality; Honovich et al. on factuality probes; Kryscinski et al. on consistency
- Semantic textual similarity benchmarks: STS-B, SICK-R — show CT measures something these miss
- Logical consistency in summarization: Falke et al. (2019); Cao et al. (2022)
- Constitutional AI / preference alignment literature: Bai et al. (2022) — CT operates at a different level (transformation fidelity vs. value alignment)
- Semantic communication: Qin et al. (2021), Xie et al. (2021) — distinguish CT from information-theoretic semantic communication

**Oracle rationale (Section III — will be a focal point for reviewers):**
Write a dedicated subsection: "Why NLI Bidirectional Entailment?" Address: (1) bidirectional entailment as the strongest available logical equivalence criterion for natural language; (2) DeBERTa-v3-base-mnli specifically — chosen for MNLI benchmark performance + inference speed; (3) known failure modes: paraphrase detection (partially addressed by EXP-007), abstract/concrete shifts, quantifier scope; (4) why these failure modes do not invalidate the conservation result (the harness is conservative — false negatives produce underestimates of conservation, not overestimates).

**Clarify the 7/20 result (abstract and Section IV):**
13/20 signals at NLI=1.00 under governance. The other 7: report what happened. Options — (a) they achieved conservation at lower NLI scores (partial conservation), (b) they failed conservation under both governed and ungoverned conditions (baseline difficulty), (c) they showed conditional conservation (governance improved but did not achieve 1.00). This is not a weakness to hide — it is the harness's calibration data. Report it directly.

**Baseline comparison for NeurIPS/ICML:**
Plan a Table 1: ROUGE-1, ROUGE-L, BERTScore, Jaccard similarity, NLI unidirectional, NLI bidirectional — applied to the same signals under the same transformations. Show that ROUGE and BERTScore fail to detect commitment loss in the negation reversal case (EXP-007). This is the paper's empirical contribution to NLP methodology, not just to CT.

## Citation Notes

- **Cites:** McHenry Axioms (Layer -1); Six-Gate Protocol (Layer 0); P-000 (CT definitions); microsoft/deberta-v3-base-mnli (oracle); Shannon (1948) channel capacity and entropy rate (conceptual analog)
- **Cited by:** P-000 (bidirectional); Paper 1 (semantic entropy rate); Paper 2 (compression-fidelity bound); Paper 3 (governance density); Paper 4 (cross-system fidelity); Paper 5 (measurement instrument); MO§ES architecture paper; all Legal_Theory papers; CL-001; CL-002; IS-001; COM-001; GOV-001
