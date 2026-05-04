# CL-002 — Three Regimes of Commitment Stability: Modal-Anchored, Relational-Structural, and Compression-Boundary Signals

**Track:** MISC — Computational Linguistics
**Layer:** 3 (Application)
**Status:** Data complete — REQUIRES circularity fix before writing (see Blocking Gap)
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

## Writing Notes

**Related Work:**

- Modal semantics: von Fintel (2006) on deontic modality; Kratzer (1991) on modality in natural language — the modal-anchored regime classification is grounded in this literature; cite and engage, don't just list
- Information-theoretic text classification: Jurafsky & Martin Ch. 4 on naive Bayes and text classification — the classification algorithm should be compared to or built on these methods
- Text complexity measures: Kincaid-Flesch readability; linguistic complexity literature — compression-boundary regime correlates with linguistic complexity; engage to show the regime captures something these measures don't

**Journal of Semantics — engagement with formal modality (if targeting that venue):**
Add a subsection in Section III: "Modal-Anchored Signals and Kratzer's Ordering Source." Show how CT's modal-anchored regime maps onto Kratzer's formal semantics: the modal base and ordering source of a deontic modal operator ("shall," "must") determine the worlds accessible for the commitment kernel. CT's conservation of this kernel corresponds to preservation of the ordering source across transformations. This is the bridge that earns the Journal of Semantics submission.

**Accuracy claims in Key Claim 5:**
After resolving the circularity (cross-validation or held-out partition), update Key Claim 5 with the actual number: "A classification algorithm achieves [X]% accuracy (95% CI: [Y]-[Z]%) on the CT corpus using [cross-validation/held-out partition], demonstrating regime-separability pending validation on external corpora."

## Blocking Gap — Circularity in Classification Algorithm

**The problem:** Section VI describes a signal classification algorithm that is evaluated for accuracy "on the CT corpus." The CT corpus (EXP-001 through EXP-007) is also the dataset used to define and characterize the three regimes (Sections III–V). Training and evaluating on the same dataset produces a circularity: the algorithm is optimized to recover the categories it was built to discover, and the accuracy figure is not generalizable.

NLE and Journal of Semantics reviewers will reject on this basis. It must be fixed before writing begins.

**Fix — choose one of two approaches:**

**Approach A: Held-out test partition (preferred)**
- Split EXP-001 through EXP-007 corpus into train (70%), dev (15%), test (15%) before regime characterization begins
- Define the three regimes using train+dev data only
- Report algorithm accuracy exclusively on the held-out test partition
- This partition must be documented in Section II and must be done before any regime analysis begins — it cannot be retrofitted after the fact
- Practical note: with 20 signals in EXP-003 and smaller counts in other experiments, a 70/15/15 split yields roughly 14/3/3 signals — very small test set; accuracy figures will have high variance and must be reported with confidence intervals

**Approach B: Cross-validation (acceptable alternative)**
- Use k-fold cross-validation (k=5 recommended given corpus size) across all EXP-001 through EXP-007 signals
- Report mean accuracy ± standard deviation across folds
- Note in Section VI that cross-validation is used due to corpus size constraints; acknowledge generalizability limits
- This avoids the circularity without requiring a separate test partition, but the small corpus size means results are still preliminary

**Recommendation:** Approach B is more honest given the corpus size. Approach A is more rigorous but the test set will be too small for meaningful accuracy claims. Either way, the accuracy claim "sufficient for practical deployment" (Key Claim 5) must be hedged to "demonstrates regime-separability on the CT corpus, pending validation on external corpora."

**Action before writing:** Implement whichever approach is chosen, compute the accuracy figure with uncertainty bounds, then update Section VI and Key Claim 5 with the actual numbers.

---

## Citation Notes

- **Cites:** Paper 0 (Conservation Law, experimental corpus, failure taxonomy); Paper 2 (Compression-Fidelity Bound); CL-001 (failure mode taxonomy); P-000 (CT definitions); formal semantics literature on modality (von Fintel, Kratzer); relational semantics literature
- **Cited by:** Paper 3 (Governance Density uses regime taxonomy to define regime-specific ρ*); Paper 5 (Measurement Instrument uses regime classification for harness calibration); L-002 (empirical legal study uses regime classification for civil rights corpus analysis); IS-002 (archival application uses regime taxonomy for preservation risk classification)
