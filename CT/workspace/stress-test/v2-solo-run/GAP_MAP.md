# Gap Map — Path from 43 to 55

**Date:** 2026-07-08
**Current score:** 43/69 (Promising)
**Target score:** 55/69 (Established)
**Gap:** 12 points

---

## Score Breakdown by Requirement

| Requirement | Max | Current | Target | Gap |
|-------------|-----|---------|--------|-----|
| 1. Defined conserved quantity | 12 | 7 | 9 | 2 |
| 2. Symmetry / invariance | 12 | 5 | 9 | 4 |
| 3. Independent measurement | 15 | 8 | 12 | 4 |
| 4. Falsifiability | 15 | 12 | 12 | 0 |
| 5. Empirical asymmetry | 15 | 11 | 13 | 2 |
| **Total** | **69** | **43** | **55** | **12** |

Requirements 4 (Falsifiability) is already at target. The gap is concentrated in Requirements 2, 3, 1, and 5.

---

## Score Breakdown by Question

| Question | Current (0-3) | Target (0-3) | Gap | Tier |
|----------|---------------|--------------|-----|------|
| Q1.1 (what is conserved) | 3 | 3 | 0 | — |
| Q1.2 (units/dimension) | 1 | 2 | 1 | 3 |
| Q1.3 (theory-independent) | 2 | 2 | 0 | — |
| Q1.4 (minimal case) | 1 | 2 | 1 | 2 |
| Q2.1 (the symmetry) | 2 | 3 | 1 | 3 |
| Q2.2 (continuous/discrete) | 0 | 1 | 1 | 3 |
| Q2.3 (Lagrangian) | 0 | 1 | 1 | 3 |
| Q2.4 (symmetry breaking) | 3 | 3 | 0 | — |
| Q3.1 (instrument named) | 3 | 3 | 0 | — |
| Q3.2 (independence) | 2 | 3 | 1 | 1 |
| Q3.3 (different instrument) | 1 | 3 | 2 | 1 |
| Q3.4 (uncertainty) | 1 | 2 | 1 | 1 |
| Q3.5 (calibration) | 1 | 2 | 1 | 2 |
| Q4.1 (falsifying observation) | 3 | 3 | 0 | — |
| Q4.2 (pre-registration) | 2 | 2 | 0 | — |
| Q4.3 (adversarial tests) | 2 | 3 | 1 | 2 |
| Q4.4 (law vs instrument) | 2 | 3 | 1 | 2 |
| Q4.5 (scope boundary) | 3 | 3 | 0 | — |
| Q5.1 (the asymmetry) | 3 | 3 | 0 | — |
| Q5.2 (empirical demo) | 2 | 3 | 1 | 1 |
| Q5.3 (reproducibility) | 1 | 2 | 1 | 1 |
| Q5.4 (effect size) | 2 | 3 | 1 | 1 |
| Q5.5 (novel predictions) | 3 | 3 | 0 | — |
| **Total** | **43** | **55** | **12** | |

---

## Tier 1: Immediately Achievable (Existing Infrastructure)

These actions require no new theory, no new math, no new formalization. They use the existing harness, existing corpus, existing oracle. A competent researcher could do them in weeks.

### Action 1: Cross-Oracle Replication

| Attribute | Detail |
|-----------|--------|
| **Addresses** | Q3.2 (+1), Q3.3 (+2), Q5.3 (+1) |
| **Points gained** | +4 |
| **What** | Run the same EXP-003 experiments with a different NLI model (RoBERTa-MNLI, BART-MNLI, or a human judge). Show the same governed/ungoverned asymmetry. |
| **Why it matters** | This is the single most impactful experiment. It directly addresses the independence concern (the oracle is the same substrate class as the system being measured). If a different oracle produces the same 65%-vs-decay asymmetry, the independence argument strengthens from "architecturally different" to "replicated across independent instruments." |
| **Effort** | Low. The harness is public, the corpus is deposited, alternative NLI models are open-source (HuggingFace). |
| **Estimated time** | 2-4 weeks |
| **Dependency** | None |
| **Risk** | If a different oracle produces a *different* asymmetry, the independence claim weakens. But this is exactly what the test wants to know — and either result is scientifically valuable. |

### Action 2: Formal Measurement Uncertainty (GUM Framework)

| Attribute | Detail |
|-----------|--------|
| **Addresses** | Q3.4 (+1) |
| **Points gained** | +1 |
| **What** | Implement the GUM (JCGM 100:2008) framework Paper 5 already proposes. Report Wilson confidence intervals for all conservation rates. Characterize the noise floor using EXP-007 data. Report Type A uncertainty (repeated measurement) and Type B uncertainty (systematic oracle error). |
| **Why it matters** | Every physical measurement has a stated uncertainty. CT has the data (13/20) and the framework (GUM) but has not done the analysis. This is a reporting gap, not a fundamental gap. |
| **Effort** | Low-medium. The statistical work is straightforward (Wilson intervals, bootstrap CIs for degradation curves). |
| **Estimated time** | 1-2 weeks |
| **Dependency** | None — data exists |
| **Risk** | None. Reporting uncertainty can only strengthen credibility, even if the intervals are wide. |

### Action 3: Scale to 100+ Signals

| Attribute | Detail |
|-----------|--------|
| **Addresses** | Q5.2 (+1), Q5.4 (+1) |
| **Points gained** | +2 |
| **What** | Expand from 20 signals to 100+. Run the same Gate vs. baseline/compression design. Report conservation rates with narrowed confidence intervals. |
| **Why it matters** | The wide CI ([43.2%, 82.9%] for 13/20) is the main weakness of the empirical evidence. With 100 signals, a 65% conservation rate would have a CI of roughly [55%, 74%] — much tighter. The effect size claim becomes much stronger. |
| **Effort** | Medium. Requires constructing or sourcing 80+ additional deontic signals (legal provisions, contract clauses, regulatory requirements). The harness already exists. |
| **Estimated time** | 4-8 weeks |
| **Dependency** | Signal corpus construction |
| **Risk** | If the conservation rate drops substantially at scale (e.g., from 65% to 40%), the law weakens. But this is important to know. |

**Tier 1 total: +7 points (43 → 50). Moves CT to upper "promising" but not yet "established."**

---

## Tier 2: Substantial Work, Achievable (Moderate Effort)

These actions require new experimental design, new protocols, or external collaboration. They are achievable with current infrastructure but require more than just running existing experiments harder.

### Action 4: Calibration Standards

| Attribute | Detail |
|-----------|--------|
| **Addresses** | Q3.5 (+1), Q4.4 (+1) |
| **Points gained** | +2 |
| **What** | Establish a set of reference signals with known conservation status: signals that always conserve (modal-anchored, simple deontic), signals that always fail (compression-boundary below threshold), and signals at the boundary. Use these to calibrate the oracle before each experiment. Operationalize the law/instrument distinction with a procedure, not just an argument. |
| **Why it matters** | Without calibration standards, the distinction between "law failed" and "instrument failed" rests on argument, not procedure. This is the gap that makes EXP-006's 2/4 failures ambiguous. |
| **Effort** | Medium. Requires identifying or constructing reference signals, running them repeatedly, establishing expected outcomes. |
| **Estimated time** | 4-6 weeks |
| **Dependency** | None, but benefits from Action 3 (more signals to choose from) |
| **Risk** | Low. Calibration standards are universally beneficial. |

### Action 5: External Falsification Attempt

| Attribute | Detail |
|-----------|--------|
| **Addresses** | Q4.3 (+1) |
| **Points gained** | +1 |
| **What** | Get an independent researcher (not Deric, not someone who has read CT's documents) to design an adversarial test specifically to break the law. Brief them on the harness (not on CT's claims). Have them design and run adversarial tests. Report the result regardless of outcome. |
| **Why it matters** | Internal adversarial tests (EXP-004/5/6) are genuine but conducted by the law's own author. External falsification is the gold standard. The harness is public; this needs outreach, not new infrastructure. |
| **Effort** | Medium. Requires finding a willing independent researcher and managing the collaboration. |
| **Estimated time** | 4-8 weeks (mostly waiting for the external researcher) |
| **Dependency** | None, but benefits from Actions 1-3 (stronger base for the external researcher to test) |
| **Risk** | The external researcher might find a falsification. But this is the point — and either result is scientifically valuable. |

### Action 6: Resolve the 7/20 Failures

| Attribute | Detail |
|-----------|--------|
| **Addresses** | Q5.4 (indirect), Q4.4 (indirect) |
| **Points gained** | Indirect — strengthens existing answers |
| **What** | Analyze the 7 signals that did not achieve NLI = 1.00 under governance. For each: was it a law failure (governance insufficient), an instrument failure (oracle misclassified), or a signal-specific factor (kernel too complex, compression-boundary regime)? Report the classification with evidence. |
| **Why it matters** | The 65% conservation rate is the fundamental challenge. If the 7 failures are explained (e.g., all 7 are compression-boundary signals that hit the bound), then the law's scope is refined: "100% within scope, 0% at the boundary." If unexplained, the law is probabilistic, not absolute. |
| **Effort** | Medium. Requires reanalysis of EXP-003 data, possibly re-running the 7 signals with additional diagnostics. |
| **Estimated time** | 2-4 weeks |
| **Dependency** | None |
| **Risk** | If the 7 failures are genuinely unexplained, the law's status weakens. But knowing this is better than not knowing. |

### Action 7: Formalize the Minimal Case

| Attribute | Detail |
|-----------|--------|
| **Addresses** | Q1.4 (+1) |
| **Points gained** | +1 |
| **What** | Formally prove (or argue rigorously) that "shall not" (a single prohibition) is the minimal deontic element carrying the conserved quantity. Show that no sub-modal element can carry deontic content. Alternatively, identify an even simpler case. |
| **Why it matters** | The test asks for "your electron" — the simplest case. CT identifies "shall not" but doesn't prove it's minimal. A formal argument (even if not a proof) would strengthen this from "identified" to "established." |
| **Effort** | Low-medium. This is a conceptual/philosophical argument, not an experimental one. |
| **Estimated time** | 1-2 weeks |
| **Dependency** | None |
| **Risk** | None. |

**Tier 2 total: +4 points (50 → 54). At the threshold of "established" but not quite over it.**

---

## Tier 3: Fundamental — The Real Barrier

These actions require new mathematics, new theoretical frameworks, or work that CT has not yet attempted. They are the difference between "promising empirical regularity" and "established conservation law." They may not all be achievable.

### Action 8: Units / Dimension for C(S) (Unblock Paper 2)

| Attribute | Detail |
|-----------|--------|
| **Addresses** | Q1.2 (+1 or +2) |
| **Points gained** | +1 to +2 |
| **What** | Formalize C(S) as an information-theoretic object. Paper 2's blocking gap: define C(S) under a corpus distribution P, yielding H(C(S)) — the Shannon entropy of the commitment kernel distribution. The natural unit is bits. Show h_s = H(C(S)) empirically. State the Compression-Fidelity Bound as an expected-length result. |
| **Why it matters** | A conserved quantity without units is an operational concept, not a physical quantity. This is the difference between "this thing is preserved" and "this quantity is conserved." Without units, CT cannot claim physics-level law status. |
| **Effort** | High. This is Paper 2's explicitly flagged blocking gap. Requires defining a probability distribution over semantic objects, showing the entropy equality empirically, and stating the bound. The path is laid out in Paper 2's PAPER_PLAN but has not been executed. |
| **Estimated time** | 3-6 months |
| **Dependency** | None, but this unblocks Paper 3 (governance density), CAP-001 (channel capacity), and potentially the symmetry/Lagrangian gaps. |
| **Risk** | The formalization might not work. C(S) might not be cleanly formalizable as a random variable under a corpus distribution. But this is the keystone — if it works, everything downstream unblocks. |
| **Strategic note** | **This is the single highest-leverage action in the entire gap map.** Resolving Paper 2's blocking gap unblocks the mathematical program and potentially addresses Q1.2, Q2.1, Q2.2, Q2.3 simultaneously. If Deric does one thing, it should be: get a co-author who can do the information-theoretic formalization. |

### Action 9: Identify the Symmetry

| Attribute | Detail |
|-----------|--------|
| **Addresses** | Q2.1 (+1), Q2.2 (+1 or +2) |
| **Points gained** | +2 to +3 |
| **What** | Determine whether CT's conservation arises from a continuous symmetry (Noether-type) or a discrete symmetry (selection-rule-type). If continuous: identify the symmetry group and the conserved current formally. If discrete: argue for why discrete symmetry is the correct framework for language, and why the Noether requirement is a category error. |
| **Why it matters** | This is the deepest gap. Without a symmetry that *generates* the conservation, CT has an observation, not a law. The conservation is currently enforced by a protocol (Six-Gate), not derived from a symmetry. |
| **Effort** | Very high. This may require mathematical work CT has not yet attempted. The channel capacity work (CAP-001) might provide a variational structure, but CAP-001 is blocked by Papers 1-3. |
| **Estimated time** | 6-12 months (or may not be achievable) |
| **Dependency** | Action 8 (Paper 2 unblock) — the symmetry question depends on having a formalized quantity to work with |
| **Risk** | This may not be achievable. Language may not have a Noether-type symmetry. If it doesn't, CT needs to argue for a different standard of "law" — one that is mathematically rigorous but not physics-identical. |
| **Alternative path** | If Noether is inapplicable, argue that the Shannon standard (channel capacity as variational result) is the correct standard for information-like systems. This requires completing CAP-001, which requires Action 8. |

### Action 10: Construct the Lagrangian Equivalent

| Attribute | Detail |
|-----------|--------|
| **Addresses** | Q2.3 (+1 or +2) |
| **Points gained** | +1 to +2 |
| **What** | Identify or construct a functional whose invariance under transformation produces the conservation law. Candidates: (a) the governance density functional C_s = f(ρ_g, h_s, κ), (b) the fidelity functional Fid(S, S') = bidirectional entailment degree, (c) a channel capacity optimization (maximize commitment transmission rate over governance configurations). Show that extremizing or constraining this functional yields C(T_gov(S)) = C(S). |
| **Why it matters** | In physics, the Lagrangian is the function whose symmetries produce conservation laws. Without it, CT cannot claim Noether-type law status. |
| **Effort** | Very high. The most speculative item. CT has not attempted this. The Shannon parallel suggests it might be possible (channel capacity is a variational result), but the construction is not obvious. |
| **Estimated time** | 6-12 months (or may not be achievable) |
| **Dependency** | Action 8 (Paper 2 unblock) and Action 9 (symmetry identification) — the Lagrangian depends on knowing what the symmetry is |
| **Risk** | This may not be achievable. If CT's conservation is protocol-enforced rather than symmetry-derived, there may be no Lagrangian. In that case, CT is an engineering result (we can build systems that preserve commitment) not a physical law (the universe's structure forces conservation). |
| **Alternative path** | If no Lagrangian exists, argue that the channel capacity theorem (CAP-001) serves the same role — it is a variational result (optimization over governance configurations) that implies conservation. This is not a Lagrangian in the Noether sense, but it is a variational principle in the Shannon sense. |

**Tier 3 total: +4 to +7 points (54 → 58-61). Crosses the "established" threshold — but only if achievable.**

---

## Critical Path

```
Action 8 (Paper 2 unblock — units/dimension)
  ├── Unblocks Paper 3 (governance density threshold)
  ├── Unblocks CAP-001 (channel capacity theorem)
  ├── Addresses Q1.2 (+1-2)
  └── Enables Action 9 (symmetry identification)
        ├── Addresses Q2.1, Q2.2 (+2-3)
        └── Enables Action 10 (Lagrangian equivalent)
              └── Addresses Q2.3 (+1-2)

Parallel track (no dependency on Tier 3):
  Action 1 (cross-oracle replication)     → +4
  Action 2 (GUM uncertainty)              → +1
  Action 3 (scale to 100+ signals)        → +2
  Action 4 (calibration standards)        → +2
  Action 5 (external falsification)       → +1
  Action 6 (resolve 7/20 failures)        → indirect
  Action 7 (formalize minimal case)       → +1
```

**The parallel track alone (Tier 1 + Tier 2) gets CT to 54 — one point short of "established."**

**The critical path (Action 8 → 9 → 10) is needed to cross the threshold.** But even partial progress on Action 8 (formalizing C(S) as an information-theoretic object, even without the full proof) could gain +1 on Q1.2, which would bring the total to 55.

**The keystone is Action 8.** Everything in Tier 3 depends on it. And it unblocks the entire downstream mathematical program (Papers 2, 3, CAP-001).

---

## The Question Behind the Question

The test applies physics standards (Noether, Lagrangian, continuous symmetry) to language. This is the right thing to do for an external validity test. But it raises a question the test doesn't address: **is the physics standard the only valid standard for a conservation law?**

Language is a discrete, combinatorial, human-constructed system. The mathematical frameworks that apply to physical systems (continuous symmetries, Lagrangians, Noether's theorem) may not apply. The relevant frameworks may be:

- **Information theory (Shannon):** conservation as a coding theorem, not a Noether symmetry. CT is already on this path (Paper 2, CAP-001).
- **Combinatorics / discrete math:** conservation as a selection rule, not a continuous symmetry. The Six-Gate Protocol is a discrete constraint set.
- **Formal semantics / modal logic:** conservation as an invariant across accessible worlds (FS-001's CI(S,w)). This is a semantic invariance, not a physical one.

If the right framework is information-theoretic, then:
- The "Lagrangian" equivalent is the channel capacity optimization
- The "symmetry" is the invariance of channel capacity under oracle substitution
- The "units" are bits (Shannon entropy of the commitment kernel distribution)

This is a different kind of law than Noether conservation, but it is not less rigorous. Shannon's theorems are rigorous without being Noether-type.

**The path to "established" may not be "find the Noether symmetry" but "prove the channel capacity theorem and show it implies conservation."** That is the Shannon path, and CT is already on it. The barrier is that CAP-001 is blocked by Papers 1-3, which are blocked by Paper 2's formalization gap.

**Paper 2 is the keystone.** Resolving it would unblock the mathematical program and potentially address the symmetry, Lagrangian, and units gaps simultaneously — not by finding Noether symmetries, but by establishing the Shannon-standard equivalent.

---

## Summary: What Is Needed to Close the Gap

| Priority | Action | Points | Effort | Dependency |
|----------|--------|--------|--------|------------|
| 1 | Cross-oracle replication | +4 | Low | None |
| 2 | GUM uncertainty framework | +1 | Low | None |
| 3 | Scale to 100+ signals | +2 | Medium | Signal corpus |
| 4 | Calibration standards | +2 | Medium | None |
| 5 | External falsification | +1 | Medium | Independent researcher |
| 6 | Resolve 7/20 failures | indirect | Medium | None |
| 7 | Formalize minimal case | +1 | Low | None |
| **8** | **Paper 2 unblock (units/dimension)** | **+1-2** | **High** | **Info-theory co-author** |
| 9 | Identify symmetry | +2-3 | Very high | Action 8 |
| 10 | Construct Lagrangian | +1-2 | Very high | Actions 8, 9 |

**Tier 1 + Tier 2 (Actions 1-7): +11 points → 54. One point short.**
**Tier 3 (Action 8 alone): +1-2 → 55-56. Crosses the threshold.**

**The single most important thing Deric can do: get a co-author who can formalize C(S) as an information-theoretic object (Action 8).** That one act unblocks the mathematical program and crosses the "established" threshold. Everything else is either empirical work (doable now) or depends on Action 8.

---

*End of gap map.*
