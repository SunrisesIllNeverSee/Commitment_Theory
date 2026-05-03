# CL-002 — Three Regimes of Commitment Stability: Modal-Anchored, Relational-Structural, and Compression-Boundary Signals

**Track:** MISC — Computational Linguistics
**Layer:** 3 (Application)
**Status:** Data complete — can write now
**Target Venue:** Natural Language Engineering / Journal of Semantics
**Est. Length:** 8,000–12,000 words
**Dependencies:** Paper 0 published; CL-001 beneficial

---

## Abstract

Analysis of the CT experimental record (EXP-001 through EXP-007) reveals that semantic objects do not fail uniformly — they fail in regime-specific ways. This paper identifies and characterizes three regimes of commitment stability under recursive AI transformation. Modal-anchored signals — those whose commitment kernel is carried primarily by modal operators ("shall," "must," "shall not," "is entitled to") — exhibit the highest conservation rates under CT governance and are specifically vulnerable to modal flattening (failure mode 4) under ungoverned transformation. Relational-structural signals — those whose kernel is carried by relational predicates ("discriminates against," "is entitled to reasonable accommodation," "has a right to") — exhibit intermediate stability and are specifically vulnerable to agent substitution (failure mode 6) and scope widening (failure mode 2). Compression-boundary signals — those whose kernel is sensitive to representation length, often because it is carried by exception clauses or threshold specifications — exhibit the sharpest conservation/loss boundary: stable above the Compression-Fidelity Bound (Paper 2) and rapidly collapsing below it. The three-regime taxonomy has direct implications for NLP system design: systems that must preserve semantic commitment can be designed with regime-specific governance — targeting modal operators for modal-anchored signals, relational predicates for relational-structural signals, and length thresholds for compression-boundary signals — rather than applying uniform governance across all signal types. We provide a signal classification algorithm that assigns a new semantic object to a regime using features extractable without the full CT harness.

---

## Outline

I. **Introduction: Why Signals Fail Differently** — Frames the regime classification question: the failure taxonomy identifies how signals fail, but the regime classification identifies which signals are at risk of which failures.

II. **Data and Classification Methodology** — Describes the CT experimental corpus (EXP-001 through EXP-007); explains the regime classification methodology; defines modal-anchored, relational-structural, and compression-boundary signal types operationally.

III. **Regime 1: Modal-Anchored Signals** — Characterizes the modal-anchored regime: high conservation under governance, specific vulnerability to modal flattening under ungoverned transformation; provides examples and conservation rate data.

IV. **Regime 2: Relational-Structural Signals** — Characterizes the relational-structural regime: intermediate stability, specific vulnerability to agent substitution and scope widening; provides examples and conservation rate data.

V. **Regime 3: Compression-Boundary Signals** — Characterizes the compression-boundary regime: sharp conservation/loss boundary at the Compression-Fidelity Bound; high sensitivity to compression operations; provides examples and conservation rate data; connects to Paper 2.

VI. **Signal Classification Algorithm** — Provides an algorithm for classifying a new semantic object into a regime using extractable features (modal operator presence and density, relational predicate structure, representation length relative to estimated fidelity bound); evaluates algorithm accuracy on the CT corpus.

VII. **Implications for NLP System Design** — Discusses how the regime taxonomy enables regime-specific governance design: targeted modal protection for modal-anchored signals, relational structure preservation for relational-structural signals, length constraint enforcement for compression-boundary signals.

---

## Key Claims

- Semantic objects fail in regime-specific ways under AI transformation: the three-regime taxonomy (modal-anchored, relational-structural, compression-boundary) predicts which failure modes a given signal is most vulnerable to.
- Modal-anchored signals exhibit the highest conservation rates under CT governance but are specifically vulnerable to modal flattening — the failure mode that converts prohibitions into preferences into permissions.
- Compression-boundary signals exhibit a sharp, threshold-dependent conservation/loss boundary at the Compression-Fidelity Bound — consistent with Paper 2's theoretical prediction — making them predictably safe above the bound and predictably unsafe below it.
- The regime taxonomy enables right-sized governance: systems can target governance resources at the specific vulnerability profile of each signal type rather than applying uniform constraint across all transformations.
- A signal classification algorithm using extractable features assigns new signals to regimes with sufficient accuracy for practical deployment in AI governance systems.

---

## Citation Notes

- **Cites:** Paper 0 (Conservation Law, experimental corpus, failure taxonomy); Paper 2 (Compression-Fidelity Bound); CL-001 (failure mode taxonomy); P-000 (CT definitions); formal semantics literature on modality (von Fintel, Kratzer); relational semantics literature
- **Cited by:** Paper 3 (Governance Density uses regime taxonomy to define regime-specific ρ*); Paper 5 (Measurement Instrument uses regime classification for harness calibration); L-002 (empirical legal study uses regime classification for civil rights corpus analysis); IS-002 (archival application uses regime taxonomy for preservation risk classification)
