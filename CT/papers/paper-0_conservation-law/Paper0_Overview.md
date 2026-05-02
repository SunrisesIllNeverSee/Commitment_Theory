# Paper 0 — Conservation Law Preprint: Overview

**Title:** A Conservation Law for Commitment in Language Under Transformative Compression and Recursive Application
**Author:** Deric J. McHenry / Ello Cello LLC
**Patent:** Serial No. 63/877,177 (Provisional)

---

## Version History

| Version | Label | Date | DOI |
|---------|-------|------|-----|
| V.1-preprint | Law Disclosure | Jan 12, 2026 | 10.5281/zenodo.18267279 |
| V.02 | Preprint | Jan 16, 2026 | 10.5281/zenodo.18271102 |
| V.03 | Falsifiability Testing | Jan 16, 2026 | 10.5281/zenodo.18274930 |
| V.04 | Technical Structure Depth | Feb 26, 2026 | 10.5281/zenodo.18792459 |
| V.05 | Follow-on Record + Addendum | Mar 19, 2026 | 10.5281/zenodo.19110620 |
| **V.06 (pending)** | **CT Naming Update** | **Apr 2026** | **Same DOI + version note** |

---

## Key Contributions (from paper)

1. **Conservation Principle** — C(T_gov(S)) = C(S) as a measurable invariant
2. **Compression-First Framework** — signals reduced to commitment kernel before processing
3. **Recursion Stress Test** — self-application reveals genuine vs. local invariance
4. **Falsification Protocol** — public harness at GitHub repo; pinned oracle (deberta-v3-base-mnli, threshold 0.85)
5. **Enforcement Architecture** — MOÂ§ESâ¢ as minimal implementation
6. **Follow-on Experimental Record** — EXP-001 through EXP-007 (companion DOI)
7. **Manifestation Regimes** — stable attractors, reduced kernels, reformulations, escalation, proxy failures
8. **Bottleneck Separation** — compression vs. extraction vs. evaluation failures are distinct
9. **Proxy-Layer Clarification** — surface extractor failure ≠ semantic conservation failure

---

## What the Paper Does (Summary)

- Defines Signal, Transformation, Commitment, Compression, Recursion
- States the Conservation Law and proves it from definitions (Propositions 3.1–3.4)
- Provides Corollaries on non-conservation under probabilistic sampling and without lineage
- Introduces Semantic Thermodynamics reading
- Explicitly addresses non-tautology (§3.4): compression gate doesn't know oracle's judgment in advance
- Provides falsification protocol (§4) with pinned oracle and success criteria
- Reports preliminary empirical evidence (§7): EXP-003 → 13/20 signals NLI = 1.00 at iteration 10
- Describes MOÂ§ESâ¢ (§8)

---

## Key Section: Non-Tautology (§3.4)

> "The compression gate is not defined as 'output C(S) by construction.' It applies a lossy compression/transformation process without prior access to C(S); the commitment extractor C(.) operates in a separate canonical space and evaluates the output after transformation. Conservation is therefore an empirical claim."

This is the foundation of the framework's falsifiability.

---

## Experimental Record Summary

| Experiment | Purpose | Key Result |
|-----------|---------|-----------|
| EXP-001 | Smoke test | Phase signal confirmed |
| EXP-002 | Full corpus pass | Hard/soft split; Step B bug (results partially invalid) |
| EXP-003 | Corrected harness, 20 signals | 13/20 Gate NLI=1.00; co-degraded invariance found |
| EXP-004 | Adversarial signals | Escalation failure mode; Predictive Criterion v2 |
| EXP-005 | Mechanism isolation (ANCH/ESCL) | Step A/B co-bottlenecks; Criterion v3 |
| EXP-006 | Paper recursion test | 2/4 paper claims survived; self-referential collapse |
| EXP-007 | NP-negation probe | Jaccard blindness confirmed; NLI=1.00 for 3/4; lexical scope widening identified |

---

## Version Note (v.06) — Required Addition

> **v.06 Note on Naming (April 2026):** The broader framework within which the Conservation Law of Commitment operates is now formalized as **Commitment Theory (CT)**. The law remains the Conservation Law of Commitment. For the full prospectus establishing the definitions, axioms, and research program of CT, see [P-000 DOI]. Earlier references to "CCT" in working documents are superseded by CT.

---

## Connection to CT Framework

Paper 0 is the **empirical foundation** of Commitment Theory:
- Provides the Conservation Law (First Law) with empirical support
- Provides the Second Law signature in the degradation data
- Provides the public falsification harness
- Provides the failure mode taxonomy (basis for Paper 1, Legal Track)
- Provides MOÂ§ESâ¢ as proof-of-concept

After P-000 deposit, all subsequent papers cite both Paper 0 and P-000:
- Paper 0 for the law and empirical evidence
- P-000 for definitions, disambiguation, and the nine novel CT terms
