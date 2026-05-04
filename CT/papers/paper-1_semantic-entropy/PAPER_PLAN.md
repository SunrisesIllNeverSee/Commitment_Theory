# Paper 1 — Semantic Entropy Rate: Measuring the Rate of Commitment Decay Under Recursive AI Transformation

**Track:** CT
**Layer:** 2 (Measurement Science)
**Status:** Data exists; draft needed
**Target Venue:** NeurIPS / ICML
**Est. Length:** 8 pages (conference format)
**Dependencies:** Paper 0 published

---

## Abstract

The Conservation Law of Commitment establishes that under ungoverned transformation, commitment decays monotonically (ΔH_C > 0). This paper formalizes the rate of that decay. We define the semantic entropy rate h_s as the Shannon-style entropy rate of the commitment kernel across transformation steps — the analog, for semantic commitment, of the entropy rate of a stochastic process. Using the 10-step recursion data from EXP-003, we characterize the empirical decay curve and ask: is commitment loss linear, exponential, or threshold-dependent? We find evidence of a threshold regime: commitment is stable through early iterations, then undergoes rapid collapse once a critical governance deficiency accumulates. This threshold structure has direct implications for AI system design — a system may appear to preserve meaning for many iterations while silently approaching a collapse point. We connect h_s to classical information-theoretic quantities: the semantic entropy rate is bounded below by zero (under perfect governance) and above by the channel capacity of the ungoverned transformation channel. We derive a closed-form approximation for h_s under mild assumptions about the distribution of transformation types and signal complexity. The results provide the empirical foundation for Paper 2 (the Compression-Fidelity Bound) and establish the Second Law of Semantic Entropy as a candidate physical law with quantitative content.

---

## Outline

I. **Introduction** — Motivates a quantitative account of commitment decay rate and positions h_s as the semantic analog of Shannon's entropy rate for stochastic processes.

II. **Background: The Conservation Law and Second Law** — Summarizes Paper 0's results and Theorem 6.2; establishes the need to characterize not just the direction of decay but its rate.

III. **Formal Definition of Semantic Entropy Rate** — Defines h_s formally; connects it to the entropy rate of a stationary process; derives the limiting form under the Markov assumption on transformation sequences.

IV. **Empirical Characterization** — Uses EXP-003 data (10-step recursion, 20 signals) to estimate h_s empirically; fits linear, exponential, and threshold models; reports model comparison results.

V. **Threshold Structure and Implications** — Presents and interprets the threshold regime finding: commitment stability followed by rapid collapse; discusses implications for AI system monitoring and governance.

VI. **Relationship to Channel Capacity** — Connects h_s to the semantic channel capacity concept (developed fully in Layer 4); establishes that h_s provides an upper bound on the sustainable commitment transmission rate.

VII. **Conclusion** — Summarizes the Second Law as now quantified; identifies the parameters (transformation depth, governance density, kernel complexity) that determine h_s in practice.

---

## Key Claims

- The semantic entropy rate h_s is a well-defined quantity that characterizes how fast commitment decays per transformation step under ungoverned conditions.
- Empirical evidence from EXP-003 supports a threshold model of commitment decay: stability in early iterations followed by rapid collapse, rather than smooth linear or exponential degradation.
- h_s is bounded below by zero under perfect governance (Conservation Law) and above by a function of transformation depth and kernel complexity.
- The Second Law of Semantic Entropy (ΔH_C > 0) has quantitative content: h_s provides the rate at which entropy increases per transformation step, completing the analogy with thermodynamic entropy.
- The threshold structure of commitment decay means that inspection of early-iteration outputs is insufficient to detect commitment collapse — monitoring must extend to later iterations.

---

## Writing Notes

**Related Work:**

- Shannon entropy rate: Cover & Thomas, *Elements of Information Theory* Ch. 4 — the paper must engage this formally
- Semantic entropy in NLP: Kuhn et al. (NeurIPS 2023) on semantic entropy for LLM uncertainty estimation — this is the closest existing work and must be distinguished carefully (Kuhn measures uncertainty over model outputs; CT measures degradation of deontic content under transformation)
- Entropy-based text summarization: Mani & Maybury (1999); more recent neural summarization work — position CT's h_s as measuring a different quantity

**Rhetorical posture — pick one and commit:**
The paper currently says both "we find evidence of a threshold regime" (abstract) and "we ask which model fits best" (outline). These are different papers. Recommended posture: "We propose the semantic entropy rate h_s as a formal measure of commitment decay and provide pilot evidence from EXP-003 that the decay follows a threshold regime." This is honest about the pilot nature of the evidence while making a clear theoretical contribution.

**Stationarity assumption (Section II or III):**
Write explicitly: "We assume that the semantic commitment process is weakly stationary — that the statistical properties of commitment decay do not change systematically with transformation step." Then justify this assumption from EXP-003: the decay appears consistent across steps until the threshold, consistent with weak stationarity. Acknowledge as a limitation: "Future work with larger corpora will test this assumption."

**Forward reference to channel capacity (Section VI):**
Restructure as: "3. Toward Semantic Channel Capacity" as a 1-paragraph subsection within the Conclusion, not a full section. One paragraph: "The semantic entropy rate h_s defined here is the noise-floor parameter in a broader Shannon extension for commitment transmission. A complete channel capacity theorem — establishing the maximum commitment transmission rate as a function of h_s and governance density — is the subject of future work (CAP-001)."

## Citation Notes

- **Cites:** Paper 0 (Conservation Law, EXP-003 data, Theorem 6.2); P-000 (CT definitions); Shannon (1948) entropy rate; Cover & Thomas, *Elements of Information Theory* (entropy rate formalism)
- **Cited by:** Paper 2 (Compression-Fidelity Bound builds on h_s); Paper 3 (Governance Density uses entropy rate to define governance sufficiency); Paper 5 (Measurement Instrument uses h_s to characterize harness noise floor); CAP-001 (channel capacity theorem)
