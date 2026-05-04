# Paper 5 — The Commitment Measurement Instrument: A Metrological Framework for Semantic Fidelity

**Track:** CT
**Layer:** 2 (Measurement Science)
**Status:** Data exists; metrological framing needed
**Target Venue:** Foundations of AI / Philosophy of Information / JMLR
**Est. Length:** 10–15 pages
**Dependencies:** Papers 1–4

---

## Abstract

Scientific progress requires not only laws and experimental results but a rigorous account of the instruments used to produce those results. This paper treats the CT measurement harness — the public protocol for measuring commitment conservation using NLI bidirectional entailment — as a scientific instrument and applies the tools of metrology to characterize it. We establish the harness's noise floor (minimum detectable commitment change), adversarial sensitivity (susceptibility to surface-level manipulations that fool the oracle without preserving commitment), oracle independence properties (the degree to which results generalize beyond the specific oracle implementation), calibration protocol, and failure taxonomy at the instrument level. The paper draws on the full experimental record (EXP-001 through EXP-007) and the cross-system results of Paper 4 to characterize the instrument's behavior across a range of inputs, architectures, and signal types. We demonstrate that EXP-006 (self-referential recursion: 2/4 paper claims survive) is best understood as a harness stress test rather than an anomaly — it identifies the conditions under which the instrument itself fails due to commitments that are insufficiently robust to withstand their own recursion. We also describe the SIGSYSTEM oracle (Layer 4) as the instrument's designed successor — a word-level contextual weighting system that will extend the harness's sensitivity and reduce its noise floor. The metrological framing has implications for how the scientific community should interpret CT's experimental record and how the harness should be used, reported, and extended.

---

## Outline

I. **Introduction: Instruments Matter** — Argues that the scientific credibility of CT's empirical record depends on a rigorous characterization of the measurement instrument, not just the results it produces.

II. **Metrological Framework** — Introduces the relevant tools from metrology: noise floor, sensitivity, accuracy, precision, calibration, and the distinction between systematic and random measurement error.

III. **Noise Floor Characterization** — Establishes the minimum detectable commitment change for the CT harness under the NLI oracle; characterizes the floor using EXP-007 data and synthetic adversarial inputs.

IV. **Adversarial Sensitivity** — Demonstrates the harness's susceptibility to specific adversarial constructions (NP-negation, synonym substitution, structural paraphrase) and characterizes which failure modes exploit the oracle's surface-form sensitivity.

V. **Oracle Independence** — Analyzes the degree to which Paper 0's results generalize beyond the specific oracle (microsoft/deberta-v3-base-mnli); uses cross-system data from Paper 4 to bound oracle-specific effects.

VI. **Calibration Protocol and EXP-006 Interpretation** — Provides a calibration protocol for the harness; reinterprets EXP-006 as a harness stress test that reveals a ninth failure mode (recursion collapse when the commitment structure is insufficiently robust).

VII. **The SIGSYSTEM Successor** — Describes the design motivation for SIGSYSTEM as the next-generation oracle; explains how word-level contextual weighting will extend sensitivity and reduce the noise floor without compromising oracle independence.

---

## Key Claims

- The CT measurement harness has a characterizable noise floor, adversarial sensitivity profile, and oracle independence range — treating it as a scientific instrument rather than an evaluation metric improves the credibility and interpretability of CT's experimental record.
- EXP-006 (2/4 paper claims survive self-referential recursion) is a harness stress test, not an anomaly: it identifies the condition under which commitment structures fail by their own recursion, revealing failure mode 9 (recursion collapse).
- The harness's adversarial sensitivity to NP-negation (EXP-007) is a feature, not a bug: it demonstrates the harness distinguishes semantic commitment from lexical surface form, which is necessary for the oracle to be scientifically valid.
- Oracle independence is bounded: results generalize across oracle implementations that support bidirectional entailment, but oracle-specific effects at the noise floor cannot be ruled out without cross-oracle replication.
- SIGSYSTEM (Layer 4) is the designed successor oracle, motivated by the specific limitations of the NLI-based approach identified in this metrological analysis.

---

## Writing Notes

**Venue: JMLR specifically — not "Foundations of AI / Philosophy of Information."** JMLR publishes methods papers with strong empirical validation. The metrology framing is appropriate for JMLR if paired with rigorous uncertainty quantification.

**Related Work:**

- Metrology for ML: Flach & Kull (2015) on calibration; Guo et al. (2017) on temperature scaling — CT's harness needs calibration characterization analogous to classifier calibration
- Evaluation metric reliability: Novikova et al. (2017) on correlation between human and automatic metrics — CT should show correlation between NLI harness scores and human judgment on at least a small subset
- Scientific instrument characterization: GUM (JCGM 100:2008) — the paper explicitly applies GUM's uncertainty framework; must engage it formally, not just cite it

**EXP-006 reframing (Section II or dedicated subsection — this is the paper's most important argumentative move):**
State explicit criteria distinguishing harness stress from Conservation Law failure:

- Conservation Law failure: C(T_gov(S)) ≠ C(S) for a signal S where the Six-Gate Protocol is correctly applied AND the oracle is functioning correctly
- Harness stress: C(T_gov(S)) ≠ C(S) where either (a) the oracle misclassifies the commitment kernel (oracle failure) or (b) the signal's commitment structure is degenerate under self-reference (EXP-006 case — the paper claims conservation of its own claims, which is a different task than claiming conservation of external deontic content)
- The criterion: EXP-006 is harness stress, not Law failure, because the 2/4 failures are in the self-referential category (b), not category (a). The paper must show this classification is principled, not post-hoc.

**GUM uncertainty propagation for NLI:**
The GUM framework assumes continuous measurement outputs with Gaussian uncertainty. NLI bidirectional entailment produces a discrete categorical output (entailment/neutral/contradiction) derived from a softmax probability. Section V must address: (1) how GUM's Type A uncertainty (repeated measurement) applies to repeated harness runs; (2) how GUM's Type B uncertainty (systematic error) applies to known oracle failure modes; (3) what "measurement uncertainty" means for a binary conservation outcome (conserved/not conserved). Recommend: report conservation rates as Bernoulli parameters with Wilson confidence intervals; this is GUM-compatible and appropriate for discrete outcomes.

## Citation Notes

- **Cites:** Paper 0 (harness design, EXP-001 through EXP-007, failure taxonomy); Paper 1 (h_s as baseline for noise floor estimation); Paper 2 (Compression-Fidelity Bound as threshold for harness sensitivity); Paper 3 (governance density ρ* as calibration benchmark); Paper 4 (cross-system data for oracle independence analysis); P-000 (CT definitions); metrology literature (JCGM 100:2008 GUM framework)
- **Cited by:** Layer 4 SIGSYSTEM paper (Paper 5 provides the motivation and specification for SIGSYSTEM); all downstream empirical papers that use the CT harness (L-002, CL-001, CL-002, IS-001)
