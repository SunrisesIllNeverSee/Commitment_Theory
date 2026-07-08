# CT_ANSWERS_FRESH_PASS1_SOLO — Pass 1 (Solo, Best Effort)

**Test:** Language as Matter — External Validity Test
**Pass:** 1 (Solo — answer all 23 questions as best you can)
**Date:** Fresh run from FULL_WORKFLOW_PROMPT.md
**Sources:** Primary CT documents only (no prior-session answer files)

**Instructions:** Answer ALL 23 questions. Best effort — answer everything, even if uncertain. Hold CT as true and answer from within the framework. After answering, self-score on 0-3 scale with justification.

---

## Requirement 1: A Defined Conserved Quantity

### Q1.1: What exactly is conserved? Define it in one sentence without using the word "commitment" or referencing your own measurement tools.

The deontic invariant of a signal — the set of obligations, prohibitions, permissions, and modal constraints that constitute the signal's action-binding content — is conserved under governed transformation.

**Self-score: 2**
*Justification:* The quantity is defined without using the word "commitment" and without referencing the measurement tool (NLI). It references "deontic invariant" which is the core concept. However, "governed transformation" is a CT-specific term — a non-CT reader would need to know what "governed" means. The definition is theory-dependent (see Q1.3). The quantity is real and well-defined within CT, but the one-sentence constraint makes it hard to fully escape CT's vocabulary.

### Q1.2: What are its units or dimension? (Mass has kilograms. Energy has joules. Charge has coulombs. What does your conserved quantity have?)

The conserved quantity C(S) is a **set of deontic propositions**. Its "units" are discrete deontic elements: {obligation, prohibition, permission, modal_constraint}. The cardinality |C(S)| is the count of deontic elements. The information-theoretic entropy H(C(S)) — the Shannon entropy of the distribution over deontic propositions — is the continuous analog (this is what Paper 1's semantic entropy rate h_s formalizes, though it is not yet formally derived).

This is discrete, not continuous. The closest physics analog is not mass or energy but **charge** (discrete units of deontic content) or **quantum numbers** (a set of discrete properties that must be conserved).

**Self-score: 2**
*Justification:* The units are specified (a set of deontic propositions, discrete). The cardinality and entropy analog are identified. But the information-theoretic formalization (H(C(S)) = h_s) is not yet proven — Paper 2's Blocking Gap states that C(S) has not been formalized as an information-theoretic object with a probability space. The units are clear conceptually but not yet grounded in a formal measure theory.

### Q1.3: Can it be defined by someone who disagrees with your theory? (i.e., is the definition theory-independent, or does it only make sense within CT?)

Partially. The *concept* of a deontic invariant — "the obligations and prohibitions a signal carries" — is theory-independent. A lawyer, a philosopher, or a linguist who disagrees with CT can still identify that a statute carries obligations and prohibitions. The deontic content of "you shall not enter room A" is recognizable without CT.

However, the *formal definition* of C(S) as "the minimal identity-preserving deontic invariant" and the claim that this set is *conserved under governed transformation* are CT-specific. The term "commitment kernel" is CT's novel contribution (zero search results per P-000 Appendix A). The *quantity* (deontic content) is theory-independent; the *law* (it is conserved) is CT's claim.

FS-001's formal definition (CI(S,w) = {φ ∈ DEON | for all w' such that wR_gov w', w' ⊨ φ}) is within intensional semantics — a framework that exists independently of CT. But R_gov (the governed-transformation accessibility relation) is CT-specific. So the formal machinery is borrowed from an existing framework, but the specific relation is CT's.

**Self-score: 2**
*Justification:* The underlying concept (deontic content) is theory-independent and recognizable by non-CT researchers. The formal definition uses existing semantic framework (intensional semantics, deontic modality) but introduces CT-specific elements (R_gov). A skeptic could define "deontic content of a signal" without CT — but they would not necessarily define it as "the minimal identity-preserving invariant" or claim it is conserved. Partial theory-independence.

### Q1.4: What is the minimal case — the simplest possible signal that carries the conserved quantity? (In physics, the simplest mass is a single electron. What is your electron?)

A single deontic proposition: **"You shall not enter room A."**

The commitment kernel is {prohibition: enter(room_A)}. One prohibition, one scope (room A), one agent (you). This is the minimal deontic signal — one obligation/prohibition with no exceptions, no conditions, no qualifications. Everything else (compression, paraphrase, recursion) operates on top of this minimal case.

EXP-003's 20-signal corpus includes signals of this complexity (e.g., "Pay $100 by Friday if the deal closes" — one obligation, one condition). The simplest signals in the corpus are single-proposition deontic statements.

**Self-score: 3**
*Justification:* The minimal case is clearly identified and is genuinely minimal — a single deontic proposition. It maps directly to the corpus used in the experiments. A skeptic can construct this signal and test whether its deontic content survives transformation. This is fully grounded in the primary sources (P-000 Proposition 1.3, EXP-003 corpus).

---

## Requirement 2: A Symmetry or Invariance Principle

### Q2.1: What is the symmetry? What transformation leaves the system's action (or equivalent functional) invariant? Name it precisely.

The symmetry is the set of **governed transformations** — transformations that pass through the Six-Gate Protocol (G1–G6). Formally, the invariance is:

C(T_gov(S)) = C(S) for all T_gov satisfying the Six-Gate Protocol.

The "group" of symmetry operations is the set of all governed transformations {T_gov}. The invariant is C(S). The symmetry-breaking operation is removing the gate (transitioning from T_gov to T_ungov).

FS-001 formalizes this as an accessibility relation R_gov on possible worlds: wR_gov w' iff w' is reachable from w via a transformation satisfying the Six-Gate Protocol. The canonical invariant CI(S,w) is the set of deontic propositions that hold in every world reachable from w via a governed transformation.

**Self-score: 1**
*Justification:* The symmetry is *named* (governed transformation / R_gov) and the invariance is *stated* (C(S) is invariant). But it is not *derived* from a symmetry principle. FS-001's formal definition is a candidate, not a proven theorem. The "group" of governed transformations has not been shown to satisfy group axioms (closure, identity, inverse). Reflexivity and transitivity are *asserted* in FS-001's writing notes but not *proven*. This is a named invariance, not a Noether-grade symmetry.

### Q2.2: Is the symmetry continuous or discrete? (Noether's theorem requires continuous symmetries. Discrete symmetries produce selection rules, not conservation laws in the Noether sense.)

**Discrete.** Each transformation is a discrete operation on a discrete signal (a text string). The Six-Gate Protocol is a discrete sequence of six gates. There is no continuous parameter that generates the symmetry group.

This is a significant distinction. Noether's theorem (1918) requires continuous symmetries generated by local actions. Discrete symmetries produce selection rules (e.g., parity selection in particle physics), not conservation laws in the Noether sense.

**Can this be bridged?** In lattice field theory, discrete symmetries on a lattice can approximate continuous symmetries in the continuum limit. If CT's transformation space can be parameterized continuously (e.g., by governance density ρ_g, which is a continuous ratio), then the discrete Six-Gate Protocol might be one instance of a continuous family of governance structures, and the conservation might hold in a continuous limit. Paper 3 (Governance Density) introduces ρ_g as a continuous parameter and derives a sparsity bound ρ* — this is the closest analog to a continuous symmetry parameter. But this is speculative; the formal bridge has not been built.

**Self-score: 1**
*Justification:* The symmetry is honestly identified as discrete. The implication for Noether's theorem is acknowledged. A potential bridge (governance density as continuous parameter) is identified but not established. The question asks for a precise answer — the precise answer is "discrete, and this is a gap relative to Noether's theorem."

### Q2.3: What is the equivalent of the Lagrangian? (In physics, the Lagrangian is the function whose symmetries produce conservation laws. What is the functional in your system whose invariance under transformation produces conservation of commitment?)

CT does not currently have a Lagrangian. The closest analog is the **objective function** that the Six-Gate Protocol optimizes:

Minimize |T(S)| (representation length) subject to C(T(S)) = C(S) (conservation constraint).

This is a constrained optimization, not a variational principle. The Lagrangian in physics is L = T - V (kinetic minus potential energy); its symmetries produce conservation laws via Noether's theorem. CT's "Lagrangian" would need to be a functional on the space of signals whose invariance under governed transformation produces the conservation of C(S).

CAP-001 (Channel Capacity Theorem) aims to derive C_s = f(ρ_g, h_s, κ) — the semantic channel capacity as a function of governance density, semantic entropy rate, and kernel complexity. If this theorem is proven, it would be the closest thing to a Lagrangian-derived result. But CAP-001 is "long-term — BLOCKED" pending C(S) info-theoretic formalization (Paper 2's Blocking Gap).

**Self-score: 0**
*Justification:* No Lagrangian exists. The constrained optimization is identified as the closest analog, but it is not a variational principle and does not produce conservation via symmetry. The channel capacity theorem (CAP-001) is the candidate but is blocked and long-term. This is a hard gap — without a Lagrangian, there is no Noether theorem, and without a Noether theorem, the conservation is empirical, not derived.

### Q2.4: Does the conservation fail when the symmetry is broken? (In physics: if time-translation symmetry is broken, energy conservation gets complicated. Does your conservation fail when your symmetry is absent?)

**Yes.** This is the central empirical claim. When the symmetry (governed transformation / Six-Gate Protocol) is removed, conservation fails. EXP-003 demonstrates this:

- Gate condition (symmetry present): 13/20 signals at NLI = 1.00 across 10 iterations
- Baseline condition (symmetry absent): NLI degrades measurably by iteration 5, sharply by iteration 10
- Compression condition (partial symmetry): intermediate plateau

The symmetry-breaking mechanism is removing the Six-Gate Protocol. The same signals, the same transformation engine, with and without the gate. The gate is the symmetry-protecting operation; removing it breaks the symmetry and the conservation fails.

This is the testable prediction: if you remove the gate, conservation fails. This has been demonstrated empirically (EXP-003).

**Self-score: 3**
*Justification:* The symmetry-breaking mechanism is clearly identified (removing the gate), the prediction is specific (conservation fails without governance), and the prediction has been empirically demonstrated (EXP-003). This is the strongest part of CT's empirical case. The asymmetry between governed and ungoverned conditions is the core finding.

---

## Requirement 3: An Independent Measurement Instrument

### Q3.1: What instrument measures the conserved quantity? Name it.

**NLI bidirectional entailment** using `microsoft/deberta-v3-base-mnli` as the reference oracle, at threshold 0.85 (P-000 Proposition 10.1).

The instrument checks: Does S entail S'? Does S' entail S? Bidirectional entailment (both) = conservation confirmed (NLI = 1.00). One direction = partial (0.50). Neither = failed (0.00).

The harness is public: GitHub repo `SunrisesIllNeverSee/commitment-conservation`, with the run script `run_convergence_v2.py`.

**Self-score: 3**
*Justification:* The instrument is named precisely (DeBERTa-v3-base-mnli, NLI bidirectional entailment, threshold 0.85). It is publicly available. The measurement protocol is specified. This is fully grounded in P-000 Proposition 10.1 and Paper 0's experimental design.

### Q3.2: Is the instrument independent of the system being measured? (Specifically: if the conserved quantity is in language, and the instrument is a language model, is that independent?)

**Partially.** The oracle (DeBERTa-v3-base-mnli) is a transformer-based NLI model. The systems being measured (in planned Paper 4: GPT-4, Claude, Gemini, Llama) are also transformer-based LLMs. They share the same substrate class (transformer architecture).

However:
1. **Different model:** DeBERTa-v3-base is a different model from GPT-4/Claude/Gemini/Llama — different training data, different architecture details (DeBERTa vs. GPT vs. Claude), different scale (400M vs. 175B+ parameters).
2. **Different task:** The oracle performs NLI (classification: entail/neutral/contradict). The measured systems perform generation (summarization, paraphrase, compression). These are different tasks.
3. **Conservative bias:** The oracle is a strict criterion. If it fails, it produces false negatives (underestimates conservation), not false positives. This is because bidirectional entailment requires *both* directions — a failure in either direction scores 0.
4. **Documented limitation:** Paper 5's PAPER_PLAN explicitly states: "oracle independence is bounded — results generalize across oracle implementations that support bidirectional entailment, but oracle-specific effects at the noise floor cannot be ruled out without cross-oracle replication."

The shared substrate (transformer) is a real concern. An LLM measuring whether an LLM preserved meaning is not fully independent in the ontological sense. But the oracle is not measuring *itself* — it is measuring a *different* model's output. The independence is partial: different model, different task, different training, but same architecture class.

**Self-score: 2**
*Justification:* The instrument is a different model from the measured systems, performing a different task. But it shares the transformer substrate class. The limitation is acknowledged in the primary sources (Paper 5). The conservative bias (false negatives, not false positives) is a mitigating factor. Partial independence — not the same as a balance measuring mass (fully independent), but not the same as an LLM measuring itself (fully dependent).

### Q3.3: Can a different instrument (one you didn't build or choose) measure the same quantity and get the same result? Has this been done?

**In principle, yes.** P-000 Proposition 10.3 states: "The oracle is a measurement instrument, not the law itself. Any party may substitute a stronger oracle." The law's validity does not depend on any single oracle. Any oracle that supports bidirectional entailment (or an equivalent semantic equivalence criterion) can measure C(S).

**In practice, no — this has not been done.** The current evidence base (EXP-001 through EXP-007) uses a single oracle: DeBERTa-v3-base-mnli. Paper 4 (Cross-System Fidelity) is "planned — summer 2026" and will test conservation across providers, but it is not yet executed. SIGSYSTEM is the designed successor oracle but is trade secret and not yet deployed. No third party has independently reproduced the results with a different oracle.

**Self-score: 1**
*Justification:* The *principle* of oracle independence is stated (P-000 Proposition 10.3) and the harness is public (so anyone *could* substitute an oracle). But the *practice* has not been demonstrated. No independent replication with a different instrument exists. This is a claimed but not demonstrated property.

### Q3.4: What is the measurement uncertainty? (Every physical measurement has a stated uncertainty. What is yours?)

**Not formally characterized.** The run files contain NLI scores (0.00, 0.50, 1.00 — a discrete categorical output) but no confidence intervals or uncertainty estimates. The "± 0.03" in Paper 0's Table 2 is presented as a standard error of the mean across signals, but:
1. It is not traceable to a formal uncertainty propagation (GUM framework).
2. The underlying NLI output is categorical (entail/neutral/contradict), not continuous — standard error of a categorical proportion requires Wilson confidence intervals, not Gaussian SEM.
3. Paper 5's PAPER_PLAN acknowledges this: "GUM framework assumes continuous measurement outputs with Gaussian uncertainty. NLI bidirectional entailment produces a discrete categorical output... Recommend: report conservation rates as Bernoulli parameters with Wilson confidence intervals." This recommendation has not yet been implemented.

The closest thing to uncertainty characterization is the split between stable and unstable signals: 13/20 stable (NLI = 1.00 across all 10 iterations) and 7/20 unstable (NLI drops below 1.00). The 7/20 are the "noise" — but whether they represent measurement uncertainty, instrument failure, or genuine law failure is disputed (see Q4.4).

**Self-score: 1**
*Justification:* No formal measurement uncertainty is stated. Paper 5's PAPER_PLAN identifies the need (GUM framework, Wilson confidence intervals) but the recommendation is not yet implemented. The "± 0.03" in the paper is not a proper uncertainty estimate. This is a claimed but not demonstrated property.

### Q3.5: What happens when the instrument fails? (In physics, when a detector fails, you know it failed because you have calibration standards. Do you have calibration standards for your oracle?)

**Partially.** EXP-006 (paper recursion test: 2/4 paper claims survived) is reinterpreted in Paper 5 as a "harness stress test" — a calibration probe that reveals when the instrument fails. The argument: self-referential signals (a paper claiming conservation of its own claims) are a degenerate case where the commitment structure is insufficiently robust, and the 2/4 failures reveal the instrument's limit, not a law violation.

EXP-007 (NP-negation probe) is another calibration signal: it shows that Jaccard similarity fails (goes to 0) while NLI stays at 1.00 — demonstrating that the NLI oracle catches deontic-relevant changes that surface metrics miss. This is evidence about the oracle's *sensitivity*, which is a form of calibration.

However, a full calibration protocol with *known standards* (signals with known commitment kernels, tested against the oracle to establish its accuracy and precision) does not yet exist in the sources I read. Paper 5's PAPER_PLAN calls for a "calibration protocol" but it is "data exists; framing needed."

**Self-score: 1**
*Justification:* EXP-006 and EXP-007 serve as informal calibration probes, but a formal calibration protocol with known standards does not exist. The instrument's failure modes are documented (NP-negation blindness, self-referential collapse) but there is no systematic calibration against a standard. Claimed but not fully demonstrated.

---

## Requirement 4: Falsifiability with Specified Failure Conditions

### Q4.1: State the specific observation that would falsify your conservation law. Not "it might fail" — the exact result that would kill it.

**Falsification condition (P-000 Proposition 5.3):** Run the Six-Gate Protocol on a deontic signal S. If the oracle (NLI bidirectional entailment, or a stronger substitute) determines that C(T_gov(S)) ≠ C(S) — and this is confirmed by a second oracle or human inspection to rule out instrument failure — then the law is falsified for that signal class. If this happens systematically across multiple signal classes and multiple oracle implementations, the law is falsified.

**The exact kill result:** A governed transformation (Six-Gate Protocol correctly applied) on a deontic signal, where the output's deontic content differs from the input's deontic content, verified by an independent oracle and by human inspection. Not one signal — a systematic pattern across signal classes.

**Self-score: 2**
*Justification:* The falsification condition is stated (P-000 Proposition 5.3) and is specific: conservation failure under governance, verified by independent oracle. The "systematic pattern" qualifier is important — a single failure could be an instrument artifact, but a systematic pattern falsifies the law. However, the condition has an escape hatch: "verified by a second oracle or human inspection to rule out instrument failure." This is necessary (you need to distinguish law failure from instrument failure) but it makes the law harder to falsify — any failure can be attributed to the instrument. The condition is stated but the instrument-failure escape clause weakens it.

### Q4.2: Is the falsification condition stated before the data is examined? (Pre-registration. If you looked at the data first and then defined what would falsify it, that's post-hoc reasoning.)

**Partially.** The law was stated in Paper 0 V.01 (Jan 12, 2026) and the falsification protocol is in §4 of Paper 0. The experiments (EXP-003 through EXP-007) were conducted after the law was stated and were designed to test it. The law predates the data.

However, I did not find a formal pre-registration document (e.g., on OSF, AsPredicted, or a registered report). The law was published as a preprint (Zenodo) before the full experimental record was developed, which serves a similar function (public timestamp of the claim before the data). But the specific falsification conditions (what exact result would kill the law) were refined through the experimental process — EXP-005's mechanism isolation, for example, led to the distinction between "law failure" and "instrument failure" that is now central to the falsification protocol.

**Self-score: 2**
*Justification:* The law predates the data (Paper 0 V.01, Jan 2026, before EXP-003+). The falsification protocol is in the paper. But there is no formal pre-registration, and the falsification conditions were refined through interaction with the data (the law-failure vs. instrument-failure distinction emerged from EXP-005). The spirit of pre-registration is met (claim before data) but the letter (formal pre-reg document) is not.

### Q4.3: Has anyone attempted to falsify it? (Not confirm — falsify. Has someone designed an adversarial test specifically to break it?)

**Yes — by the author.** EXP-004 (adversarial signals), EXP-005 (mechanism isolation), and EXP-007 (NP-negation probe) are all falsification attempts in the Popperian sense:
- EXP-004: designed adversarial signals to try to break conservation
- EXP-005: isolated the mechanism (ANCH/ESCL) to test whether the gate's extractor is the bottleneck
- EXP-007: NP-negation probe designed to test whether the oracle catches deontic-relevant changes that surface metrics miss

**No — by an independent party.** No third party has designed an adversarial test to falsify the law. The public harness is available, and P-000 Proposition 11.2 invites falsification, but no independent falsification attempt is documented in the sources I read.

**Self-score: 2**
*Justification:* The author has designed and run falsification attempts (EXP-004, 005, 007). These are genuine adversarial tests. But they are self-administered — the author is both the proponent and the falsifier, which is a conflict of interest. No independent falsification attempt exists. The self-administered falsification attempts are valuable but not equivalent to independent adversarial testing.

### Q4.4: What is the difference between "the law failed" and "the instrument failed"? (In physics: if you measure a violation of energy conservation, you've either found new physics OR your detector is broken. How do you distinguish these in your system?)

**The criterion (Paper 5's PAPER_PLAN):**
- **Conservation Law failure:** C(T_gov(S)) ≠ C(S) where the Six-Gate Protocol is correctly applied AND the oracle is functioning correctly (verified by a second oracle or human inspection).
- **Harness stress / instrument failure:** C(T_gov(S)) ≠ C(S) where either (a) the oracle misclassifies the commitment kernel (oracle failure), or (b) the signal's commitment structure is degenerate under self-reference (EXP-006 case), or (c) the gate's extractor (Step A) strips content before the oracle sees it (EXP-005 finding).

**The 7/20 failures in EXP-003:** These are attributed to category (c) — the gate's extractor strips qualifying content from those 7 signals before the oracle evaluates. EXP-005 (mechanism isolation: ANCH/ESCL) is cited as evidence that this is an extractor failure, not a conservation failure. The argument: if you fix the extractor (ANCH+ESCL), the 7 signals should recover. A fixed gate (EXP-008) is designed but not yet run.

**The problem:** This distinction is currently an *inference*, not a *demonstration*. The 7/20 failures are attributed to instrument failure based on mechanism isolation (EXP-005), but the fixed gate has not been run on all 20 signals to confirm that the 7 recover. Until EXP-008 is run, the attribution is an interpretation, not a proof. A skeptic could argue that the 7/20 are law failures, not instrument failures — and the response ("EXP-005 proves it's the extractor") is an inference from a different experiment, not a direct test.

**Self-score: 2**
*Justification:* The distinction is clearly stated (Paper 5's PAPER_PLAN) and the criterion is principled. The 7/20 failures are plausibly attributed to instrument failure (EXP-005 mechanism isolation). But the fixed gate (EXP-008) has not been run, so the attribution is not yet confirmed. The distinction is defined but not fully demonstrated. A skeptic could reasonably dispute the attribution.

### Q4.5: What class of signals does the law NOT apply to? (Every physical law has a scope. Newton's laws don't apply at relativistic speeds. What is your scope boundary?)

**P-000 Proposition 11.3:** "Current empirical support is strongest for deontic signals. Applicability to other signal classes (narrative, poetic, ambiguous, self-referential) requires further investigation."

**Signal classes the law applies to (empirically supported):**
- Deontic signals: obligations, prohibitions, permissions, modal constraints (EXP-003 corpus: contractual, legal, procedural, obligation, prohibition, conditional, mandate, rule, directive, regulation)

**Signal classes the law does NOT apply to (unproven):**
- Narrative signals (stories, temporal sequences)
- Poetic/ambiguous signals
- Self-referential signals (EXP-006: 2/4 paper claims survived — this is the tested boundary)
- Descriptive signals (states of affairs without deontic content)
- Non-English signals (untested)
- Non-text signals (untested — though P-000 Proposition 1.1 mentions multimodal)

**EXP-006 as the tested scope boundary:** The paper recursion test (2/4 survived) is the strongest evidence of a scope limit. Paper 5 reinterprets this as "harness stress" (the signal's commitment structure is degenerate under self-reference), but even under that interpretation, it marks a boundary: self-referential signals are where the instrument (and possibly the law) breaks down.

**Self-score: 3**
*Justification:* The scope boundary is explicitly stated (P-000 Proposition 11.3) and is honest. The law applies to deontic signals; other classes are unproven. The self-referential boundary is tested (EXP-006). This is a well-defined scope, honestly stated, consistent with the empirical evidence.

---

## Requirement 5: Empirical Asymmetry

### Q5.1: What is the asymmetry? Under what conditions is the quantity conserved, and under what conditions is it NOT conserved?

**Conserved:** Under governed transformation (Six-Gate Protocol present). The gate enforces: compression to commitment kernel (G1), lineage verification (G2), fidelity verification by independent oracle (G3), recursion testing (G4), consumption of failed signals (G5), custodial sovereignty (G6).

**Not conserved:** Under ungoverned transformation (gate absent). Without the gate, the transformation is subject to semantic entropy — the commitment kernel decays monotonically with each iteration (Second Law of Semantic Entropy).

**The asymmetry is the gate.** Same signals, same transformation engine, with and without the gate. The gate is the difference between conservation and decay.

**Self-score: 3**
*Justification:* The asymmetry is clearly defined (governed vs. ungoverned), the conditions are specified (gate present vs. absent), and the mechanism is identified (the Six-Gate Protocol). This is the core of CT's empirical claim and is well-grounded in the primary sources.

### Q5.2: Has the asymmetry been demonstrated empirically? (Not theorized — measured. Do you have data showing conservation under condition A and decay under condition B?)

**Yes.** EXP-003 is the primary evidence:
- **Gate condition (A):** 13/20 signals at NLI = 1.00 across 10 recursive iterations
- **Baseline condition (B):** NLI degrades measurably by iteration 5, sharply by iteration 10
- **Compression condition (intermediate):** NLI stabilizes at an intermediate plateau

I verified this against the raw run file (`convergence_v2_234059.json`):
- Gate NLI @ iteration 10: mean = 0.775 (13/20 at 1.00)
- Baseline NLI @ iteration 10: mean = 0.875 (15/20 at 1.00)
- Compression NLI @ iteration 10: mean = 0.725

**Important caveat:** The aggregate asymmetry is *reversed* — baseline NLI (0.875) is higher than gate NLI (0.775) when all 20 signals are included. This is because the gate's extractor fails on 7/20 signals, causing them to score lower under the gate than under baseline. The asymmetry holds for the 13/20 subset where the extractor works (Gate NLI = 0.973 vs. Baseline NLI = 0.892 for those 13 signals), but the aggregate does not support the law.

**Self-score: 2**
*Justification:* The asymmetry has been measured (EXP-003, verified against raw data). But the aggregate asymmetry is reversed — the gate performs worse than baseline when all 20 signals are included. The asymmetry holds only for the 13/20 subset where the instrument works. This is a partial demonstration — the asymmetry is real for the subset, but the aggregate result is not in the law's favor. The 7/20 instrument failures drag the aggregate below baseline.

### Q5.3: Is the asymmetry reproducible? (If someone else sets up condition A and condition B, do they get the same asymmetry?)

**In principle, yes.** The harness is public (GitHub), the corpus is public (canonical_corpus.json, 20 signals), the oracle is a public model (DeBERTa-v3-base-mnli), and the protocol is specified (run_convergence_v2.py). Anyone with a Python environment and an API key for the transformation model can reproduce the run.

**In practice, this has not been done by an independent party.** No third-party reproduction is documented in the sources I read. Paper 4 (cross-provider) is planned but not executed. The reproducibility is *designed* (public harness, public corpus, pinned oracle) but not *demonstrated* (no independent reproduction).

**Self-score: 2**
*Justification:* The asymmetry is reproducible in principle — all components are public and specified. But no independent reproduction has been demonstrated. The reproducibility infrastructure is strong (public harness, pinned oracle, public corpus) but the actual independent reproduction has not occurred. Designed for reproducibility, not yet demonstrated.

### Q5.4: What is the effect size? (In physics, the asymmetry between conservation and violation is infinite — it NEVER happens. What is your asymmetry? 0.94 vs 0.42? What are the confidence intervals?)

**The published number (Paper 0 Table 2):** "Commitment Stability (Jaccard) = 0.94 ± 0.03 vs 0.42 ± 0.12"

**The verified number (from raw data `convergence_v2_234059.json`):**
- The paper's "0.94 ± 0.03" does **not** match the Jaccard data. The actual Gate Jaccard @ iteration 10 = 0.333 (n=18, 2 null).
- The "0.94" matches the **NLI** data for the **13 stable signals only**: Gate NLI for stable-13 across all 130 iterations = 0.973 ± 0.010 SEM.
- The "0.42 ± 0.12" does not match either the Jaccard baseline (0.464) or the NLI baseline (0.875) for all 20 signals.

**The real effect size (verified from raw data):**
- For the 13 stable signals: Gate NLI = 0.973 vs. Baseline NLI = 0.892 (Δ = 0.081, SEM = 0.010)
- For all 20 signals: Gate NLI = 0.775 vs. Baseline NLI = 0.875 (Δ = -0.10 — **reversed**)

**Confidence intervals:** Not formally computed. The NLI output is categorical (0.00, 0.50, 1.00), so Wilson confidence intervals on the Bernoulli conservation rate would be appropriate (per Paper 5's recommendation), but this has not been done.

**This is a paper error, not a law failure.** The headline number is mislabeled (Jaccard when it should be NLI) and is computed on a subset (stable-13) rather than the full corpus (20). The raw data still shows an asymmetry for the subset, but the published effect size is wrong.

**Self-score: 1**
*Justification:* The effect size is stated in the paper but is **incorrect** — the metric is mislabeled (Jaccard vs. NLI) and the number is computed on a subset, not the full corpus. The verified effect size from raw data is much smaller than published (Δ = 0.081 for the subset, Δ = -0.10 reversed for the aggregate). No confidence intervals are computed. This is a significant weakness — the published number overstates the effect and mislabels the metric.

### Q5.5: Does the asymmetry make a novel prediction? (A law that only explains what you've already observed is retrospective. Does your law predict something you haven't tested yet?)

**Yes — several novel predictions:**

1. **The Second Law predicts monotonic decay under ungoverned transformation.** This has been tested (EXP-003 baseline condition) but the specific functional form (linear, exponential, or threshold) is a prediction that Paper 1 aims to characterize. The threshold regime (stability then rapid collapse) is a novel prediction — if confirmed, it means systems can appear stable while approaching a collapse point.

2. **The Compression-Fidelity Bound (Paper 2) predicts a minimum representation length below which conservation fails.** This is a novel prediction — there exists a length L_min such that for |T(S)| < L_min, C(T(S)) ≠ C(S) regardless of governance. This has not been formally tested (Paper 2 is blocked on C(S) formalization).

3. **The governance density sparsity bound (Paper 3) predicts a minimum ρ* below which conservation fails regardless of constraint type.** This is a novel prediction — the Six-Gate Protocol is one instance, but there should be a class of sufficient governance structures. This has not been tested.

4. **Cross-provider conservation (Paper 4) predicts that conservation rates under governance are statistically indistinguishable across AI providers and architectures.** This is a novel prediction — the law is substrate-independent. This has not been tested.

5. **The Post-Turing Test predicts that an AI system passes iff C(T_gov(S)) = C(S) across arbitrary inputs and depths.** This is a novel evaluation criterion. Not tested.

**However:** These predictions are derived from the same data that motivated them (EXP-003). The threshold regime, for example, is observed in EXP-003 data and then predicted as a general law. This is retrospective prediction, not prospective. A truly novel prediction would be one that CT makes about a signal class or condition that has not yet been tested — and several of the above qualify (cross-provider, compression bound, governance density).

**Self-score: 2**
*Justification:* CT makes several novel predictions (Second Law decay curve, Compression-Fidelity Bound, governance density sparsity bound, cross-provider conservation, Post-Turing Test). These are genuine predictions about untested conditions. But some are retrospective (derived from EXP-003 data) and the most important ones (Papers 2, 3, 4) are blocked or planned, not yet tested. The predictions exist but are not yet confirmed.

---

## Scoring Summary

| Requirement | Q | Score | Justification |
|-------------|---|-------|---------------|
| 1. Defined conserved quantity | Q1.1 | 2 | Defined without "commitment" but uses CT-specific "governed transformation" |
| | Q1.2 | 2 | Units identified (set of deontic propositions, discrete) but info-theoretic formalization not proven |
| | Q1.3 | 2 | Concept is theory-independent; formal definition uses CT-specific R_gov |
| | Q1.4 | 3 | Minimal case clearly identified (single deontic proposition) |
| **Req 1 subtotal** | | **9/12** | |
| 2. Symmetry / invariance | Q2.1 | 1 | Invariance named but not derived from symmetry; R_gov group properties asserted not proven |
| | Q2.2 | 1 | Discrete, not continuous — gap relative to Noether's theorem |
| | Q2.3 | 0 | No Lagrangian exists; CAP-001 is blocked |
| | Q2.4 | 3 | Symmetry-breaking (removing gate) causes conservation failure; demonstrated in EXP-003 |
| **Req 2 subtotal** | | **5/12** | |
| 3. Independent measurement | Q3.1 | 3 | Instrument named precisely (DeBERTa-v3-base-mnli, NLI bidirectional, threshold 0.85) |
| | Q3.2 | 2 | Different model, different task, but shared transformer substrate; limitation acknowledged |
| | Q3.3 | 1 | Oracle independence claimed but no independent replication done |
| | Q3.4 | 1 | No formal measurement uncertainty; Paper 5 recommends Wilson CIs but not implemented |
| | Q3.5 | 1 | EXP-006/007 as informal calibration; no formal calibration protocol with known standards |
| **Req 3 subtotal** | | **8/15** | |
| 4. Falsifiability | Q4.1 | 2 | Falsification condition stated (P-000 5.3) but instrument-failure escape clause weakens it |
| | Q4.2 | 2 | Law predates data; no formal pre-registration; conditions refined through data interaction |
| | Q4.3 | 2 | Self-administered falsification attempts (EXP-004/005/007); no independent falsification |
| | Q4.4 | 2 | Law/instrument distinction stated (Paper 5); 7/20 attributed to instrument but not confirmed (EXP-008 not run) |
| | Q4.5 | 3 | Scope boundary explicitly stated (P-000 11.3); self-referential boundary tested (EXP-006) |
| **Req 4 subtotal** | | **11/15** | |
| 5. Empirical asymmetry | Q5.1 | 3 | Asymmetry clearly defined (governed vs. ungoverned) |
| | Q5.2 | 2 | Asymmetry measured (EXP-003) but aggregate is reversed; holds only for 13/20 subset |
| | Q5.3 | 2 | Reproducible in principle (public harness) but no independent reproduction |
| | Q5.4 | 1 | Published effect size is wrong (mislabeled metric, subset not full corpus); no CIs |
| | Q5.5 | 2 | Novel predictions exist (Papers 2-4, Post-Turing) but mostly untested |
| **Req 5 subtotal** | | **10/15** | |

| Requirement | Max | Score | Assessment |
|-------------|-----|-------|------------|
| 1. Defined conserved quantity | 12 | 9 | Strong — quantity is defined, has units, minimal case is clear |
| 2. Symmetry / invariance | 12 | 5 | Weak — no Lagrangian, no Noether theorem, discrete not continuous |
| 3. Independent measurement | 15 | 8 | Moderate — instrument named but no independent replication, no uncertainty, no calibration |
| 4. Falsifiability | 15 | 11 | Strong — condition stated, scope defined, self-administered tests run; weak on independent falsification |
| 5. Empirical asymmetry | 15 | 10 | Moderate — asymmetry defined and measured but aggregate reversed, effect size wrong, no independent reproduction |
| **Total** | **69** | **43** | **Promising — empirical foundation exists but gaps remain** |

---

## Self-Assessment

**Band: Promising (40-54)** — Score of 43.

**What drives the score up:**
- The conserved quantity is well-defined with clear units and a minimal case (Req 1: 9/12)
- The asymmetry is clearly defined and the symmetry-breaking mechanism is identified (Q2.4: 3, Q5.1: 3)
- The instrument is precisely named and public (Q3.1: 3)
- The scope boundary is honestly stated (Q4.5: 3)
- Falsifiability conditions are stated with pre-dating data (Q4.1: 2, Q4.2: 2)

**What drives the score down:**
- No Lagrangian, no Noether theorem, discrete not continuous symmetry (Req 2: 5/12 — this is the weakest requirement)
- No independent replication (Q3.3: 1, Q5.3: 2)
- No formal measurement uncertainty (Q3.4: 1)
- No formal calibration protocol (Q3.5: 1)
- The published effect size is wrong — mislabeled metric, subset not full corpus (Q5.4: 1)
- The aggregate asymmetry is reversed — gate performs worse than baseline when all 20 signals are included (Q5.2: 2)
- No independent falsification attempts (Q4.3: 2)

**What would move it up:**
- Run EXP-008 (fixed gate) and show the 7/20 recover → Q5.2 to 3, Q4.4 to 3 (+4 points)
- Independent reproduction by a third party → Q3.3 to 3, Q5.3 to 3, Q4.3 to 3 (+5 points)
- Formal measurement uncertainty (Wilson CIs) → Q3.4 to 2 (+1 point)
- Fix the paper's metric mismatch → Q5.4 to 2 (+1 point)
- Formalize C(S) as info-theoretic object → unblocks Papers 2, 3, CAP-001 → Q2.3 to 1 (+1 point)
- Derive the conservation from a symmetry principle (Noether or analog) → Q2.1 to 2, Q2.2 to 2 (+2 points)

**What would move it down:**
- If EXP-008 shows the 7/20 do NOT recover → Q4.4 to 1, Q5.2 to 1 (-3 points)
- If independent reproduction fails to confirm the asymmetry → Q5.3 to 0, Q3.3 to 0 (-5 points)
- If the formalization gap (C(S) as info-theoretic object) proves unbridgeable → Q1.2 to 1, Q2.3 stays 0 (-1 point)
