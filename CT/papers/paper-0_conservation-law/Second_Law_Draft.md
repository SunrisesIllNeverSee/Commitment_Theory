# Second Law of Semantic Entropy — Candidate Statement

**Status:** Candidate — needs formal empirical validation
**Evidence Base:** EXP-003 degradation curves, Theorem 6.2 in Paper 0
**Target:** Formalize within Paper 1, or as standalone short paper

---

## Proposed Statement

> For any ungoverned transformation sequence T_ungov^(n), the commitment content C(S^(n)) decreases monotonically with n, and the rate of semantic entropy production is strictly positive.
>
> Formally: Let H_C(S) = -log(Fid(S, S_0)) be the semantic entropy of a signal relative to its original commitment. For ungoverned transformations:
>
> **ΔH_C > 0 for each step n → n+1**
>
> with cumulative entropy after n steps bounded below by Ω(σ√n), where σ² is the per-step drift variance.

---

## Relationship to First Law

| First Law | Second Law |
|-----------|------------|
| C(T_gov(S)) = C(S) | C(T_ungov^(n)(S)) < C(S) for n ≥ 1 |
| Governed transformations conserve commitment | Ungoverned transformations dissipate commitment |
| Meaning is invariant | Meaning decays irreversibly |
| Compression gate enforces zero drift | Without gate, drift accumulates without bound |

---

## Physical Analogy

| Thermodynamics | CT |
|---------------|-----|
| First Law: Energy is conserved | First Law: Commitment is conserved under governance |
| Second Law: Entropy increases in isolated system | Second Law: Semantic entropy increases without governance |
| Third Law: Absolute zero unattainable | Candidate Third Law: Compression limit L_min below which conservation fails (Theorem 6.3) |

---

## Empirical Support (from Paper 0)

- **EXP-003, Gate condition:** NLI = 1.00 for 13/20 signals at iteration 10 (First Law confirmed)
- **EXP-003, Baseline/Compression:** NLI degrades measurably by iteration 5, sharply by iteration 10 (Second Law signature)
- **Theorem 6.2 (Paper 0):** Drift variance σ² accumulation modeled; per-step drift leads to O(σ√n) cumulative entropy

---

## Relationship to McHenry Axioms / Blackhole Law

| Second Law | Blackhole Law (Anchor I) |
|------------|--------------------------|
| Describes: semantic entropy is inevitable under ungoverned transformation | Enforces: corrupted signals consumed at the event horizon |
| Physical law | Constitutional enforcement mechanism |
| Explains why the Blackhole is necessary | Instantiates the quarantine of Second Law consequences |

---

## Failure Modes as Second Law Evidence

Each documented failure mode (obligation escalation, scope widening, exception dropping, etc.) is an empirical signature of the Second Law — deontic content decaying through ungoverned transformation steps.

- Escalation: "may" → "shall" (modal drift)
- Scope widening: "room A" → "any room" (quantifier drift)
- Exception dropping: qualifier omitted (content loss)
- Frame inversion: prohibition → obligation (semantic inversion)

---

## Publication Plan

- **Option A:** Include as Theorem within Paper 1 (Semantic Entropy Rate)
- **Option B:** Standalone short paper in information theory / physics-of-information venue
- **Recommendation:** Option A first; elevate to standalone after Paper 1 establishes the empirical foundation.
