# Paper 3 — Governance Density Optimization: The Minimum Constraint Set for Commitment Conservation

**Track:** CT
**Layer:** 2 (Measurement Science)
**Status:** BLOCKED — depends on Paper 2's C(S) info-theoretic formalization
**Target Venue:** AAMAS / FAccT / AIES
**Est. Length:** 8–10 pages
**Dependencies:** Papers 1–2

---

## Abstract

The Conservation Law of Commitment states that C(T_gov(S)) = C(S) under governed transformation. But governance is not binary — it is a spectrum. This paper asks: what is the minimum governance overhead required to guarantee commitment conservation? We define governance density ρ_g as the ratio of constraint operations to transformation operations in a governed transformation pipeline and derive a sparsity bound — the minimum ρ_g below which conservation fails regardless of the constraint type applied. The result establishes that CT-compliant systems need not be maximally constrained, only sufficiently constrained: there exists a governance threshold ρ* such that for ρ_g ≥ ρ*, C(T_gov(S)) = C(S), and for ρ_g < ρ*, commitment decay is inevitable. We derive ρ* as a function of transformation depth, semantic entropy rate h_s (Paper 1), and the Compression-Fidelity Bound (Paper 2). The Six-Gate Protocol (G1–G6) is shown to be one instance of a ρ_g ≥ ρ* governance structure, not the unique instance. This has direct implications for AI system engineering: governance can be sparse without being insufficient, and unnecessary constraint overhead can be eliminated without sacrificing conservation guarantees. We provide an algorithm for constructing minimum governance sets for arbitrary transformation pipelines, making the results immediately applicable to AI system design.

---

## Outline

I. **Introduction** — Motivates the governance density question: how much governance is enough, and how do we know when we have it?

II. **Formal Definition of Governance Density** — Defines ρ_g, the constraint-to-transformation ratio; characterizes the space of valid constraint types within the CT framework.

III. **The Sparsity Bound** — States and proves the sparsity bound: the minimum governance density ρ* required for commitment conservation; derives ρ* as a function of h_s, the Compression-Fidelity Bound, and transformation depth.

IV. **The Six-Gate Protocol as One Instance** — Demonstrates that the Six-Gate Protocol satisfies ρ_g ≥ ρ* and is therefore sufficient for conservation, but not the unique sufficient governance structure.

V. **Algorithm for Minimum Governance Set Construction** — Provides a constructive algorithm for identifying the minimum constraint set for a given transformation pipeline; discusses computational complexity.

VI. **Empirical Validation** — Uses CT harness data to test the sparsity bound predictions; identifies governance configurations that cross the ρ* threshold and reports the predicted vs. observed commitment conservation rates.

VII. **Implications for AI System Engineering** — Discusses the practical implications of the sparsity bound for AI governance design: governance can be right-sized without sacrificing conservation guarantees.

---

## Key Claims

- There exists a minimum governance density ρ* such that for ρ_g ≥ ρ*, commitment is conserved, and for ρ_g < ρ*, commitment decay is inevitable regardless of constraint type.
- The sparsity bound ρ* is a function of transformation depth, semantic entropy rate, and the Compression-Fidelity Bound — all of which are empirically estimable using the CT harness.
- The Six-Gate Protocol is one valid governance instance, not the unique sufficient governance structure; the paper characterizes the full space of valid instances.
- CT-compliant systems can be minimally constrained rather than maximally constrained: governance overhead can be reduced to ρ* without sacrificing conservation guarantees.
- The minimum governance set construction algorithm is computationally tractable for realistic transformation pipelines, making the results applicable to deployed AI systems.

---

## Blocking Gap — Must Resolve Before Writing

**Inherited from Paper 2:** The governance sparsity bound ρ* is derived as a function of h_s and the Compression-Fidelity Bound. Both of those depend on C(S) being formalized as an information-theoretic object with a probability space (see Paper 2's Blocking Gap). Until that formalization exists, the derivation of ρ* in Section III cannot be stated formally.

**Additional gap specific to Paper 3:** The algorithm for constructing a minimum governance set (Section V) operates on a "transformation pipeline" — but the plan does not define what a transformation pipeline is formally. This must be specified before the algorithm can be described:
- What are the atomic transformation operations?
- What is the domain over which ρ_g is computed (token operations? semantic operations? gate invocations)?
- Is ρ_g a ratio over a fixed pipeline or over a stochastic transformation process?

**Resolution dependency:** Paper 2's C(S) formalization resolves the ρ* derivation. The transformation pipeline definition is independent and can be resolved separately — it is the more tractable of the two gaps and should be addressed first.

---

## Citation Notes

- **Cites:** Paper 0 (Conservation Law, Six-Gate Protocol); Paper 1 (semantic entropy rate h_s); Paper 2 (Compression-Fidelity Bound); P-000 (CT definitions, Layer -1 axioms)
- **Cited by:** Paper 4 (Cross-System Fidelity uses governance density to compare governance across architectures); Paper 5 (Measurement Instrument uses ρ* to characterize harness governance requirements); MO§ES architecture paper (MO§ES is analyzed as a ρ_g ≥ ρ* instance); GOV-001 (comparative governance analysis uses ρ* as a benchmark for evaluating other governance frameworks)
