# Paper 2 — The Compression-Fidelity Bound: An Information-Theoretic Limit on Semantic Losslessness

**Track:** CT
**Layer:** 2 (Measurement Science)
**Status:** BLOCKED — formal proof needed; C(S) info-theoretic formalization required first
**Target Venue:** NeurIPS / ICML / IEEE Transactions on Information Theory
**Est. Length:** 8–12 pages
**Dependencies:** Paper 1

---

## Abstract

Every semantic compression operation faces a fundamental tension: shorter representations are more efficient but risk losing the action-binding content that makes meaning consequential. This paper establishes the Compression-Fidelity Bound — an information-theoretic lower bound on the representation length required to preserve the commitment kernel C(S) of a semantic object S. The bound is the semantic analog of Shannon's source coding theorem: just as Shannon's theorem gives the minimum bit length for lossless data compression, the Compression-Fidelity Bound gives the minimum semantic length below which commitment loss is inevitable. We derive the bound using the semantic entropy rate h_s (Paper 1) and the formal definition of the commitment kernel (Paper 0). Empirically, we demonstrate the bound using the compression-boundary signals identified in EXP-003 and EXP-007 — signals whose commitment kernel collapses sharply at a length threshold, with stable conservation above the bound and monotonic decay below it. The bound has direct practical implications: AI summarization systems, document compression pipelines, and any system that must preserve legal, contractual, or regulatory meaning while reducing text length must respect the Compression-Fidelity Bound or accept commitment loss as a design consequence. We provide a method for estimating the bound for a given semantic object using the CT measurement harness, making the bound operationally useful without requiring access to the formal proof machinery.

---

## Outline

I. **Introduction** — Frames the compression-fidelity tension and positions the Compression-Fidelity Bound as the semantic analog of Shannon's source coding theorem.

II. **Background: Shannon's Source Coding Theorem and Its Limits** — Reviews the classical theorem and its assumptions; identifies the gap between bit-level losslessness and semantic losslessness.

III. **Formal Statement of the Bound** — States and proves the Compression-Fidelity Bound; connects it to the semantic entropy rate h_s and the kernel complexity measure κ(S).

IV. **Empirical Demonstration** — Uses compression-boundary signals from EXP-003 and EXP-007 to demonstrate the bound empirically; shows the sharp transition from conservation to decay at the threshold.

V. **Operational Estimation Method** — Provides a protocol for estimating the Compression-Fidelity Bound for a given semantic object using the CT measurement harness, without requiring access to the proof machinery.

VI. **Implications for AI System Design** — Discusses the bound's implications for summarization, contract compression, regulatory text processing, and any AI pipeline that reduces text length while claiming to preserve meaning.

VII. **Conclusion** — Summarizes the bound, its proof, and its operational significance; positions it as a necessary constraint for any semantically responsible compression system.

---

## Key Claims

- There exists a minimum representation length below which commitment loss is inevitable — the Compression-Fidelity Bound — derivable from the semantic entropy rate and kernel complexity.
- The Compression-Fidelity Bound is the semantic analog of Shannon's source coding theorem: it defines the minimum semantic length for lossless commitment preservation, just as Shannon's theorem defines the minimum bit length for lossless data compression.
- Empirical evidence from the CT measurement harness shows a sharp transition from commitment conservation to monotonic decay at the compression boundary, consistent with the theoretical bound.
- The bound is operationally estimable for any given semantic object using the public CT harness, making it practically applicable to AI system design and evaluation.
- AI systems that compress text below the Compression-Fidelity Bound cannot guarantee commitment preservation regardless of governance protocol — the bound is a physical constraint, not a design choice.

---

## Writing Notes

**Related Work:**

- Shannon source coding theorem: Shannon (1948); Cover & Thomas Ch. 5 — the paper must derive the analog formally, not just invoke the analogy
- Semantic communication literature: Bao et al. (2011) on joint source-channel coding for semantic fidelity; Shi et al. (2021) on semantic communications — distinguish CT: CT measures deontic commitment, not semantic similarity or task performance
- Text compression with semantic constraints: Grangier & Auli (2018) on semantic text exchange; summarization fidelity literature — these are engineering approaches; CT provides the theoretical lower bound
- Information bottleneck: Tishby et al. (2000) — CT's bound is in the same spirit but applied to deontic content rather than task-relevant information

**Representation length vs. semantic length:**
Section III must define "representation length" precisely. Token count is the obvious measure but is model-dependent. Options: (a) character count (model-independent but rough); (b) token count under a fixed tokenizer (model-dependent but precise); (c) compressed bit length (model-independent, theoretically motivated). Recommend: use character count for the empirical results and provide a conversion note for token-based systems. The bound should be stated in terms of a length measure that does not presuppose a specific model.

**Empirical sharp transition:**
EXP-003 and EXP-007 show signals that collapse at a threshold. Report whether the threshold is universal (same length for all signals) or signal-dependent (each signal has its own threshold). If signal-dependent, the bound is a function of the signal's kernel complexity κ(S) — which is the correct formulation. If universal, the paper makes a stronger claim that will need more empirical support.

## Blocking Gap — Must Resolve Before Writing

**The problem:** C(S) as currently defined is a deterministic function of a specific text. Shannon's source coding theorem requires a *random variable* drawn from a *probability distribution* over a source alphabet. The proof in Section III cannot be constructed until C(S) is formalized as an information-theoretic object.

**What needs to be defined:**
1. **The semantic source** — a probability distribution P over semantic objects in a domain D (e.g., legal provisions drawn uniformly from a statutory corpus). S is then a random variable S ~ P.
2. **The commitment kernel distribution** — C(S) for S ~ P defines a distribution over commitment kernels. This is the "source" in the Shannon analog.
3. **The semantic entropy** — H(C(S)) under P, which should equal h_s as defined operationally in Paper 1 (this equality must be proven, not assumed).
4. **The coding scheme** — a function mapping semantic objects to "compressed representations," with a well-defined length measure. This is not token count — it must be defined in terms meaningful to the commitment kernel.
5. **The theorem statement** — once these four items are defined, the Compression-Fidelity Bound becomes: the expected codeword length for any commitment-lossless code is at least H(C(S)).

**Path forward:** Define P as a corpus distribution (matching the EXP-003 signal corpus). Show h_s = H(C(S)) under P empirically using the existing data. State the bound as an expected-length result. The "minimum representation length" becomes the Shannon entropy of the commitment kernel distribution under P. This sidesteps the need for a universal coding theorem over all possible semantic objects and makes the claim empirically grounded.

**Who resolves this:** This is the paper's central theoretical contribution. It must be worked out before Section III can be written. No writing should begin on Paper 2 until this formalization exists.

---

## Citation Notes

- **Cites:** Paper 0 (kernel definition, EXP-003, EXP-007 compression-boundary data); Paper 1 (semantic entropy rate h_s); P-000 (CT definitions); Shannon (1948) source coding theorem; Cover & Thomas, *Elements of Information Theory*
- **Cited by:** Paper 3 (Governance Density uses the bound to define when governance is sufficient); Paper 5 (Measurement Instrument uses the bound to characterize harness sensitivity at compression boundary); L-002 (empirical legal study uses bound to identify at-risk statutory provisions); CL-002 (compression-boundary regime classification)
