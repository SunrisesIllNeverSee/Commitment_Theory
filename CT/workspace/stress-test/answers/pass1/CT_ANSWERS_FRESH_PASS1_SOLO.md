# CT Answers — Pass 1 (Solo, Best Effort)

**Date:** 2026-07-08
**Posture:** CT held as true. Answering from within the framework as an expert. Drawing from primary sources, not just the expert notes summary.

---

## Requirement 1: A Defined Conserved Quantity

### Q1.1: What exactly is conserved? Define it in one sentence without using the word "commitment" or referencing your own measurement tools.

The deontic invariant of a signal — the set of obligations, prohibitions, permissions, and modal constraints that constitute its action-binding content — is conserved under governed transformation and decays under ungoverned transformation.

**Self-score: 2.** The quantity is defined without using "commitment" or referencing measurement tools. It references "deontic" which is a term from modal logic (theory-independent). However, "governed transformation" is a CT-specific term — someone who disagrees with CT would need to understand what makes a transformation "governed." The definition is partially theory-independent (deontic content is a standard concept) but partially theory-dependent (governed/ungoverned is CT's distinction).

### Q1.2: What are its units or dimension?

C(S) is a **set** — a discrete collection of deontic propositions. The elements are individual obligations, prohibitions, permissions, and modal constraints. From P-000 Proposition 1.3: C(S) is "the set of obligations, prohibitions, permissions, and modal constraints that must survive transformation."

The units are **deontic propositions** — individual action-binding statements. "The employer shall provide reasonable accommodation" is one element. "Unless doing so would impose an undue hardship" is another. The kernel is the set of all such elements.

This is discrete, not continuous. It is set-valued, not scalar. The natural measure is set cardinality |C(S)| or set overlap (Jaccard similarity between C(S) and C(T(S))).

**Self-score: 2.** The units are clearly stated (deontic propositions, set-valued, discrete). This is honest and grounded in P-000 Proposition 1.3. However, set-valued conserved quantities are unusual in physics — most conserved quantities are scalar or vector. The framework would benefit from an information-theoretic measure (entropy of the set, or information content), but that formalization is explicitly blocked (Paper 2's blocking gap). The units exist and are defined, but they lack the precision of physical units (kilograms, joules, coulombs).

### Q1.3: Can it be defined by someone who disagrees with your theory?

Partially yes. The concept of "deontic content" — obligations, prohibitions, permissions — is standard in modal logic, deontic logic, and legal theory. Von Fintel, Kratzer, and the entire field of deontic modality use these concepts without reference to CT. A philosopher or legal scholar who rejects CT entirely can still identify the deontic content of a signal: "this statute imposes an obligation to accommodate, subject to an undue-hardship exception."

However, the specific claim that this deontic content is *conserved under governed transformation* is CT's contribution. Someone who disagrees with CT can define the quantity (deontic content) but would not necessarily agree that it is conserved, or that "governed transformation" is a meaningful category.

The definition of the quantity (deontic invariant) is largely theory-independent. The conservation claim is theory-dependent. This is the correct structure — the quantity is defined before the law is claimed, which is what the non-tautology condition (§3.4) requires.

**Self-score: 2.** The quantity can be defined by a theory-independent actor (deontic content is standard). But the specific extraction (which propositions count as "deontic") and the conservation claim are CT-specific. The definition is partially theory-independent, which is sufficient for the quantity to exist — but the boundary between "deontic" and "non-deontic" content is not always sharp (what about descriptive content that implies an obligation?).

### Q1.4: What is the minimal case — the simplest possible signal that carries the conserved quantity?

The simplest deontic signal is a single prohibition: **"Do not enter."** 

This signal carries one deontic proposition: a prohibition on entering. The commitment kernel is C(S) = {¬enter}. This is the electron — the simplest case where the conserved quantity exists.

An even simpler case: **"Shall."** A single modal operator carrying obligation. But this is degenerate — it lacks an object. The minimal non-degenerate case is a modal operator + a predicate: "shall pay," "must not enter," "may access."

From the canonical corpus (EXP-003), the simplest signals are single-obligation provisions like "Pay $100 by Friday if the deal closes" (the "contractual" signal). The kernel is {obligation to pay $100, condition: deal closes, deadline: Friday}.

**Self-score: 2.** The minimal case is clearly identified (single deontic proposition: a prohibition or obligation). This is grounded in the corpus. However, the "electron" analogy is imperfect — in physics, the electron is fundamental and indivisible. In CT, a single deontic proposition can sometimes be decomposed (is "shall not enter without permission" one proposition or two?). The minimal case exists but the indivisibility is not as clean as in particle physics.

---

## Requirement 2: A Symmetry or Invariance Principle

### Q2.1: What is the symmetry? What transformation leaves the system's action (or equivalent functional) invariant?

The symmetry is **invariance under governed transformation**. The commitment kernel C(S) is invariant under the group of transformations T_gov that satisfy the Six-Gate Protocol (compression, lineage verification, fidelity verification, recursion testing, consumption/metabolism, custodial sovereignty).

From FS-001's candidate formal definition:

> CI(S, w) = {φ ∈ DEON | for all w' such that wR_gov w', w' ⊨ φ}

where R_gov is the accessibility relation induced by governed transformations on possible worlds. The commitment kernel is the set of deontic propositions that hold in every world reachable from w via governed transformation.

The symmetry group is the set of governed transformations {T_gov} under composition. The invariant is C(S) — the deontic content that survives all such transformations.

**Self-score: 2.** The symmetry is stated clearly and formally (FS-001's candidate definition). The invariance is well-defined: C(S) is invariant under the group of governed transformations. However, the formal definition is explicitly a *candidate* — FS-001 is BLOCKED on confirming it. The group properties (reflexivity from identity, transitivity from composability) are argued from the Six-Gate Protocol design but not formally proven. The symmetry is stated but not yet mathematically established.

### Q2.2: Is the symmetry continuous or discrete?

The symmetry is **discrete**. Transformations are discrete operations — each transformation is a distinct step (summarize, paraphrase, compress). The recursion depth n is a discrete parameter (n = 1, 2, 3, ... 10). There is no continuous parameter that generates the symmetry group.

This is a significant issue for the Noether framework. Noether's theorem requires *continuous* symmetries to produce conserved currents. Discrete symmetries produce selection rules, not conservation laws in the Noether sense.

CT's response would be: the Shannon parallel. Shannon's information theory also deals with discrete quantities (bits, discrete alphabets) and produces conservation-like results (source coding theorem, channel coding theorem) without requiring Noether's theorem. CT follows Shannon's approach, not Noether's. The conservation is established empirically and information-theoretically, not through a Noether-style symmetry theorem.

However, this means CT does not have a Noether-style derivation of its conservation law. The conservation is observed and formalized, not derived from a continuous symmetry. This is a structural difference from physics conservation laws.

**Self-score: 1.** The symmetry is discrete, which means Noether's theorem does not directly apply. CT acknowledges this implicitly by following the Shannon parallel rather than the Noether framework. But the test specifically asks about Noether's theorem, and the honest answer is that CT's symmetry is discrete and therefore does not produce a conserved current in the Noether sense. The framework has an invariance principle but not a Noether-style derivation. This is a real gap.

### Q2.3: What is the equivalent of the Lagrangian?

CT does not currently have a Lagrangian or equivalent variational principle. The framework has:
- A conserved quantity: C(S)
- An invariance principle: C(T_gov(S)) = C(S)
- A symmetry group: {T_gov} under composition
- An empirical law: the conservation holds under governance, fails without it

But it does NOT have:
- A Lagrangian L whose symmetries produce the conservation
- A variational principle (action functional whose extrema give the dynamics)
- A Noether current derived from the symmetry

The closest candidate is the **semantic channel capacity** C_s = f(ρ_g, h_s, κ) from CAP-001, which relates governance density, semantic entropy rate, and kernel complexity. But this is a capacity theorem (Shannon-style), not a Lagrangian (Noether-style). And it is long-term and blocked on Papers 1-5.

The framework's position is that it follows Shannon, not Noether. Shannon didn't need a Lagrangian to establish information theory — he defined the invariant (information) operationally and proved coding theorems. CT defines the invariant (commitment) operationally and aims to prove conservation theorems. But the test asks for the Lagrangian equivalent, and the honest answer is: it doesn't exist yet.

**Self-score: 0.** No Lagrangian exists. No variational principle exists. No Noether current exists. The framework has an invariance but not the mathematical machinery that produces conservation laws from symmetries in physics. This is the deepest formal gap. The CAP-001 channel capacity theorem is the long-term candidate, but it is blocked and follows Shannon, not Noether.

### Q2.4: Does the conservation fail when the symmetry is broken?

Yes. The symmetry-breaking mechanism is the transition from governed to ungoverned transformation. Under governed transformation (symmetry present), C(T_gov(S)) = C(S). Under ungoverned transformation (symmetry broken), C(T_ungov(S)) < C(S) — the kernel decays monotonically (Second Law of Semantic Entropy).

EXP-003 is designed to test this: the Gate condition (governed) vs. Baseline condition (ungoverned). The prediction is that Gate preserves the kernel while Baseline degrades it.

However, the EXP-003 data shows a complication: Baseline NLI@10 = 0.875 (15/20 at 1.00) vs. Gate NLI@10 = 0.775 (13/20 at 1.00). The ungoverned condition shows MORE conservation than the governed condition on the NLI metric. This appears to contradict the symmetry-breaking prediction.

The framework's interpretation: the NLI oracle is too permissive — it reports "entailed" when commitment has actually drifted. The Jaccard metric (which is more sensitive to surface changes) shows Gate = 0.333 vs. Baseline = 0.464, which also doesn't show the expected pattern. The 7/20 gate failures are attributed to instrument failures (EXP-005: ANCH and ESCL mechanisms), not law failures.

The honest assessment: the symmetry-breaking prediction is stated but not cleanly demonstrated in the controlled experiment. The preliminary results (Table 2: 0.94 vs 0.42) show the expected pattern, but the controlled follow-on (EXP-003) does not replicate it on the NLI metric.

**Self-score: 1.** The symmetry-breaking mechanism is clearly stated (governed → ungoverned). The prediction is testable. But the empirical demonstration is problematic — the controlled experiment (EXP-003) does not cleanly show the predicted asymmetry on the NLI metric. The preliminary results do, but they come from a different corpus and may use a different metric computation. The conservation *should* fail when the symmetry is broken, but the data is mixed.

---

## Requirement 3: An Independent Measurement Instrument

### Q3.1: What instrument measures the conserved quantity?

The reference oracle is **microsoft/deberta-v3-base-mnli** — a public, open-source natural language inference model that evaluates bidirectional entailment. The threshold is Pr(S ⇒ S') > 0.85 AND Pr(S' ⇒ S) > 0.85.

The measurement protocol:
1. Extract the commitment kernel from the source signal using a modal-pattern sieve (public proxy extractor E(.))
2. Extract the commitment kernel from the transformed signal
3. Evaluate bidirectional entailment between the two kernels
4. Score: 1.00 = both directions hold, 0.50 = one direction, 0.00 = neither

The harness is public at github.com/SunrisesIllNeverSee/commitment-conservation. The oracle is pinned by commit hash. The corpus is public.

**Self-score: 3.** The instrument is named, public, open-source, pinned, and reproducible. This is the strongest part of the framework. Anyone can run the harness with the same oracle and get the same results.

### Q3.2: Is the instrument independent of the system being measured?

Partially. The oracle (DeBERTa-v3-base-mnli) is architecturally separate from the measured systems (GPT-4, Claude, Gemini, Llama):
- Different model family (DeBERTa vs. GPT/Claude/Gemini/Llama)
- Different training data (MNLI benchmark vs. general web)
- Different parameter count (~400M vs. 100B+)
- Different purpose (entailment classification vs. text generation)

However, they share the same substrate class: **all are transformer-based neural networks**. The oracle is a transformer evaluating whether other transformers preserved meaning. This is a real limitation — in physics, you don't measure mass with mass, or charge with charge. The instrument and the measured system share a fundamental architecture.

The framework's response (Paper 5): the oracle measures a different *property* (entailment) than the measured systems *produce* (transformation). The shared substrate is a documented limitation, not a fatal flaw — the question is whether the shared substrate introduces systematic bias, and that requires cross-oracle replication (Paper 4, planned but not executed).

The oracle is also swappable — any party may substitute a stronger oracle. The law's validity does not depend on any single oracle. But no alternative oracle has been tested.

**Self-score: 2.** The instrument is partially independent — different model family, different training, different purpose. But the shared transformer substrate is a real limitation. The independence is a design property, not yet empirically validated. The oracle is swappable in principle, but no alternative has been tested. This is "demonstrated within limits."

### Q3.3: Can a different instrument measure the same quantity and get the same result? Has this been done?

In principle, yes — the oracle is swappable. The equivalence relation ~ is external and replaceable. Any NLI model that supports bidirectional entailment can serve as oracle. A human evaluator can serve as oracle. A formal logic system can serve as oracle for formalized signals.

In practice, **this has not been done**. All experimental data comes from one oracle (deberta-v3-base-mnli) operated by one person (the author). No independent party has run the harness. No alternative oracle has been tested. Cross-oracle replication is planned (Paper 4) but not executed.

The framework explicitly acknowledges this: "Oracle independence is bounded: results generalize across oracle implementations that support bidirectional entailment, but oracle-specific effects at the noise floor cannot be ruled out without cross-oracle replication" (Paper 5 plan).

**Self-score: 1.** The instrument is swappable in principle, and the protocol explicitly invites alternative oracles. But no alternative has been tested, and no independent party has replicated. This is "claimed but not demonstrated."

### Q3.4: What is the measurement uncertainty?

The framework reports results with basic statistics:
- EXP-003 Gate NLI@10: mean = 0.775, SEM = 0.077, n = 20
- EXP-003 Gate Jaccard@10: mean = 0.333, SEM = 0.084, n = 18
- Paper Table 2: 0.94 ± 0.03 (preliminary run, different corpus)

However, the framework does NOT have:
- A formal noise floor characterization (Paper 5 is planned but not written)
- GUM (Guide to the Expression of Uncertainty in Measurement) compliance
- Type A uncertainty (repeated measurement uncertainty) formally separated from Type B uncertainty (systematic error)
- Calibration against a standard
- Wilson confidence intervals for the binary conservation outcomes (Paper 5 plan mentions this but it's not done)

The measurement uncertainty is reported as basic descriptive statistics (mean ± SEM) but not as a formal metrological uncertainty budget. The NLI oracle produces a discrete output (entailment/neutral/contradiction) derived from softmax probabilities — the uncertainty propagation from softmax to binary conservation outcome is not formalized.

**Self-score: 1.** Basic statistics are reported (mean, SEM). But there is no formal metrological uncertainty framework, no noise floor characterization, no calibration standard, no GUM compliance. The uncertainty is reported informally but not characterized to scientific instrument standards. Paper 5 plans this but has not been written.

### Q3.5: What happens when the instrument fails? Do you have calibration standards?

The framework has identified specific instrument failure modes:
- **NP-negation blindness (EXP-007):** The NLI oracle reports entailment when noun-phrase negation has been dropped. Jaccard catches this (degrades) but NLI doesn't.
- **Co-degraded invariance (EXP-003):** NLI = 1.00 masks real qualifier loss when both source and transformed signals are impoverished.
- **Modal frame inversion (EXP-005, ANCH condition):** Anchor preservation without frame preservation inverts polarity — the oracle may not catch this.
- **Self-referential collapse (EXP-006):** The harness fails when the commitment structure is insufficiently robust to withstand its own recursion.

The framework distinguishes "law failure" from "instrument failure" (Paper 5 plan):
- **Law failure:** C(T_gov(S)) ≠ C(S) when the Six-Gate Protocol is correctly applied AND the oracle is functioning correctly.
- **Instrument failure:** C(T_gov(S)) ≠ C(S) where either (a) the oracle misclassifies the kernel, or (b) the signal's commitment structure is degenerate.

However, **there are no formal calibration standards**. In physics, a detector is calibrated against known standards (particle beams of known energy, radioactive sources of known activity). CT has no analogous calibration standard — no "gold standard" set of signals with known commitment kernels against which the oracle is tested. The framework explicitly removed the gold set (per the README: "Gold set removed — would contaminate the principle — humans don't define matter"). This is a principled decision but leaves the instrument without calibration.

**Self-score: 1.** Instrument failure modes are identified and classified. The law-failure vs. instrument-failure distinction is stated. But there are no formal calibration standards, and the gold set was removed on principle. The instrument can fail in known ways, but there is no independent standard against which to calibrate it. This is "claimed but not demonstrated."

---

## Requirement 4: Falsifiability with Specified Failure Conditions

### Q4.1: State the specific observation that would falsify your conservation law.

From Paper 0 §4.3, the framework is falsified if any of the following hold:

1. **Compression + lineage systems fail:** If MOSES(TM) exhibits drift comparable to probabilistic systems (commitment stability < 0.7 after 10 iterations).
2. **Probabilistic systems succeed:** If probabilistic systems without compression maintain high commitment stability (> 0.9 after 10 iterations).
3. **Alternative mechanisms:** If an alternative mechanism (not based on compression or lineage) achieves comparable or better commitment stability.

The specific observable: F_10(S) < τ (with τ = 0.85) for a non-trivial fraction of samples under the pinned suite T_pub at recursion depth n=10 under enforced (compression+lineage) conditions.

Attractor rejection: if outputs converge to generic boilerplate while failing to preserve extracted commitments, this is counted as falsification, not conservation.

**Self-score: 3.** The falsification conditions are specific, quantitative, and stated in the paper. The kill conditions are explicit: stability < 0.7 under governance, or stability > 0.9 without governance. This is the strongest falsifiability statement in the framework. The conditions are externally verifiable — anyone can run the harness and check.

### Q4.2: Is the falsification condition stated before the data is examined?

Yes. The falsification protocol was published in V.03 (January 16, 2026, DOI 10.5281/zenodo.18274930) — labeled "Falsifiability Testing." The follow-on controlled experiments (EXP-003 through EXP-007) were conducted in March 2026. The falsification conditions were published approximately two months before the controlled experimental data was generated.

The V.03 preprint explicitly states the falsification conditions, the pinned suite, the public observable, and the refutation conditions. The subsequent experiments were designed to test these pre-registered conditions.

**Self-score: 3.** The falsification conditions were pre-registered in V.03 (Jan 16, 2026) before the controlled experiments (March 2026). This is genuine pre-registration. The DOI chain provides verifiable timestamps.

### Q4.3: Has anyone attempted to falsify it?

The author has conducted adversarial tests designed to break the law:
- **EXP-004:** Adversarial signals designed to trigger failure modes (escalation, scope widening)
- **EXP-005:** Mechanism isolation — ANCH and ESCL conditions designed to isolate which gate components fail
- **EXP-006:** Self-referential recursion — paper claims about the law itself subjected to the law's own test (2/4 survived — a genuine falsification attempt that found a real failure mode)
- **EXP-007:** NP-negation probe — designed to test whether the oracle can detect semantic negation drops

However, **no independent party has attempted to falsify the law**. All adversarial tests were designed and run by the author. The harness is public and the invitation to falsify is standing, but no external replication or adversarial test has been conducted.

EXP-006 is particularly notable: the author subjected the paper's own claims to the conservation test, and 2 of 4 claims failed. This is a genuine falsification attempt that found a real boundary (self-referential collapse). The framework honestly reports this as a failure mode rather than hiding it.

**Self-score: 2.** The author has conducted genuine adversarial tests (EXP-004 through EXP-007), including self-application (EXP-006) that found real failures. But no independent party has attempted falsification. The adversarial tests are real but self-administered. This is "partially met" — the intent and mechanism are there, but independent falsification has not occurred.

### Q4.4: What is the difference between "the law failed" and "the instrument failed"?

The framework explicitly addresses this (Paper 5 plan):

- **Conservation Law failure:** C(T_gov(S)) ≠ C(S) for a signal S where the Six-Gate Protocol is correctly applied AND the oracle is functioning correctly.
- **Harness stress / instrument failure:** C(T_gov(S)) ≠ C(S) where either (a) the oracle misclassifies the commitment kernel (oracle failure), or (b) the signal's commitment structure is degenerate under self-reference (EXP-006 case).

The 7/20 gate failures in EXP-003 are classified as instrument failures based on EXP-005's mechanism isolation: ANCH (anchor preservation without frame preservation) and ESCL (obligation escalation) are identified as the failure mechanisms. EXP-005 proved that these are Step A/B co-bottlenecks — the extraction step fails, not the conservation itself.

However, the distinction between "law failure" and "instrument failure" is made *by the framework itself*, not by an independent arbiter. In physics, if you measure a violation of energy conservation, you check your detector against calibration standards. CT has no calibration standards (the gold set was removed). The distinction is principled but not independently verifiable.

The EXP-003 baseline anomaly (baseline NLI > gate NLI) further complicates this: if the instrument is failing, it's failing in a way that makes the ungoverned condition look BETTER than the governed condition, which is the opposite of what you'd expect from an instrument designed to detect governance benefits.

**Self-score: 1.** The distinction is stated and the mechanism (EXP-005) is identified. But the distinction is made by the framework itself, not by an independent arbiter, and there are no calibration standards to verify it. The EXP-003 baseline anomaly makes the distinction harder to maintain. This is "claimed but not demonstrated" — the framework claims the 7/20 failures are instrument failures, but cannot independently prove it.

### Q4.5: What class of signals does the law NOT apply to?

From P-000 Proposition 11.3: "Current empirical support is strongest for deontic signals. Applicability to other signal classes (narrative, poetic, ambiguous, self-referential) requires further investigation."

Signal classes (P-000 Proposition 1.7):
- **Deontic** (obligations, prohibitions, permissions) — STRONGEST support, the law's primary scope
- **Descriptive** (states of affairs) — unproven
- **Narrative** (temporal sequences) — unproven
- **Self-referential** — tested in EXP-006, 2/4 survived (known failure mode: self-referential collapse)

The law explicitly does NOT claim to apply to:
- Poetic or literary language (no deontic content)
- Ambiguous signals (kernel extraction unreliable)
- Signals without action-binding content
- Self-referential signals where the commitment structure is insufficiently robust

The scope boundary is honest and clearly stated. The law is a law of deontic content, not of all meaning.

**Self-score: 3.** The scope boundary is explicit, honest, and grounded in the experimental record. The law applies to deontic signals and explicitly does not claim to apply to narrative, poetic, or ambiguous signals. The self-referential failure mode (EXP-006) is reported honestly. This is fully met.

---

## Requirement 5: Empirical Asymmetry

### Q5.1: What is the asymmetry? Under what conditions is the quantity conserved, and under what conditions is it NOT conserved?

- **Condition A (conserved):** Governed transformation — compression + lineage (MOSES(TM) / Six-Gate Protocol). The commitment kernel is conserved: C(T_gov(S)) = C(S).
- **Condition B (not conserved):** Ungoverned transformation — probabilistic transformation without governance gates. The commitment kernel decays: C(T_ungov(S)) < C(S), with ΔH_C > 0 per step (Second Law).

The asymmetry is governance: with the Six-Gate Protocol, commitment is conserved; without it, commitment decays. This is the central empirical claim.

**Self-score: 2.** The asymmetry is clearly stated and the conditions are well-defined. The governed/ungoverned distinction is operationally clear (Six-Gate Protocol present or absent). However, the asymmetry is stated as a binary (governed vs. ungoverned) when the framework also acknowledges governance density is a spectrum (Paper 3: ρ_g). The binary framing is a simplification.

### Q5.2: Has the asymmetry been demonstrated empirically?

The paper's Table 2 reports: Commitment Stability (n=10) = 0.94 ± 0.03 (compression+lineage) vs. 0.42 ± 0.12 (probabilistic). This is a large asymmetry (0.52 separation).

However, this number comes from the **preliminary run** (175 items: 100 sentences, 50 code snippets, 25 proofs), not from the controlled experiment EXP-003 (20 signals, 10 iterations).

The controlled experiment EXP-003 shows:
- Gate NLI@10: 0.775 (13/20 at 1.00)
- Baseline NLI@10: 0.875 (15/20 at 1.00)
- Gate Jaccard@10: 0.333
- Baseline Jaccard@10: 0.464

**The controlled experiment does NOT show the expected asymmetry on the NLI metric.** Baseline (ungoverned) NLI is HIGHER than Gate (governed) NLI. The Jaccard metric also does not show the expected pattern.

The preliminary results show the asymmetry; the controlled experiment does not replicate it. This is a significant empirical gap.

The framework's interpretation: the 7/20 gate failures are instrument failures (EXP-005), and the baseline's high NLI is because the NLI oracle is too permissive (it says "entailed" when commitment has actually drifted). But this interpretation is made by the framework itself, not independently verified.

**Self-score: 1.** The asymmetry is claimed (Table 2: 0.94 vs 0.42) but the controlled experiment (EXP-003) does not cleanly demonstrate it. The NLI metric shows the REVERSE of the predicted pattern. The preliminary results show the asymmetry but come from a different corpus. This is "claimed but not demonstrated" in the controlled setting.

### Q5.3: Is the asymmetry reproducible?

The asymmetry has been observed in the preliminary run (Table 2) but NOT replicated in the controlled experiment (EXP-003). The preliminary run used 175 items; EXP-003 used 20 signals. The metric may differ between runs (the 0.94 is labeled "Jaccard" in Table 2 but EXP-003 Jaccard is 0.333).

No independent party has attempted reproduction. The harness is public, so reproduction is possible in principle, but it has not been done.

The framework plans EXP-008 (combined ANCH+ESCL gate + Step C voice constraint) to fix the 7/20 instrument failures. EXP-005 predicts 5-6 of the 7 failures will recover. But EXP-008 has not been run.

**Self-score: 1.** The asymmetry is not reproducible across the framework's own runs (preliminary vs. controlled). No independent reproduction exists. The planned fix (EXP-008) has not been executed. This is "claimed but not demonstrated."

### Q5.4: What is the effect size?

The paper claims: 0.94 ± 0.03 vs. 0.42 ± 0.12 = 0.52 separation (preliminary run).

The controlled experiment shows: Gate NLI@10 = 0.775 ± 0.077 vs. Baseline NLI@10 = 0.875 ± 0.050 = -0.10 separation (REVERSED).

The Jaccard metric: Gate = 0.333 ± 0.084 vs. Baseline = 0.464 ± 0.086 = -0.13 separation (REVERSED).

The effect size in the controlled experiment is NEGATIVE — the ungoverned condition shows more conservation than the governed condition. This directly contradicts the law's prediction.

The paper's headline number (0.94 vs 0.42) comes from a different run with a different corpus and possibly a different metric computation. The provenance of the 0.94 number is unclear — it does not match the EXP-003 Jaccard (0.333) or NLI (0.775) for the gate condition.

**Self-score: 1.** The effect size is stated (0.52 separation) but comes from the preliminary run, not the controlled experiment. The controlled experiment shows a REVERSED effect (-0.10 on NLI). The confidence intervals are reported as SEM but not as formal uncertainty bounds. The headline number's provenance is unclear. This is "claimed but not demonstrated."

### Q5.5: Does the asymmetry make a novel prediction?

Yes. The law makes several novel, testable predictions:

1. **EXP-008 prediction:** If the ANCH+ESCL gate fix is applied, 5-6 of the 7 instrument failures should recover, bringing Gate NLI@10 from 13/20 to 18-19/20. This is a specific, quantitative prediction that can be tested by running EXP-008.

2. **Cross-system prediction (Paper 4):** Under governance, conservation rates should be statistically indistinguishable across AI providers (GPT-4, Claude, Gemini, Llama). Under ungoverned conditions, decay rates may vary by architecture. This is testable by running the harness across providers.

3. **Compression-Fidelity Bound prediction (Paper 2):** There exists a minimum representation length below which commitment loss is inevitable. Signals compressed below this bound should collapse sharply, while signals above it should be conserved. This is testable by varying compression levels.

4. **Governance density prediction (Paper 3):** There exists a minimum governance density ρ* below which conservation fails regardless of constraint type. This is testable by varying the number of gates applied.

5. **Regime-specific prediction (CL-002):** Modal-anchored signals should be most conserved under governance and most vulnerable to modal flattening without it. Compression-boundary signals should show a sharp threshold. This is testable by classifying signals by regime and comparing conservation rates.

These are genuine novel predictions — they predict specific outcomes that haven't been tested yet. The framework is not purely retrospective.

**Self-score: 2.** The framework makes several novel, testable predictions (EXP-008, cross-system, compression-fidelity bound, governance density, regime-specific). These are specific and quantitative. However, none have been tested yet — they are all planned but not executed. The predictions exist but are unvalidated. This is "partially met."

---

## Scoring Summary

| Requirement | Max Score | My Score | Assessment |
|-------------|-----------|----------|------------|
| 1. Defined conserved quantity | 12 | 8 | Partially met — quantity defined, units stated, minimal case identified, but theory-independence is partial |
| 2. Symmetry / invariance principle | 12 | 3 | Weak — invariance stated but not proven, symmetry is discrete (not Noether-compatible), no Lagrangian, symmetry-breaking not cleanly demonstrated |
| 3. Independent measurement | 15 | 8 | Partially met — instrument is public and named, but independence is limited (shared substrate), no alternative tested, no formal uncertainty, no calibration standards |
| 4. Falsifiability | 15 | 10 | Strong — falsification conditions specific and pre-registered, scope boundary explicit, but no independent falsification attempts, law-vs-instrument distinction not independently verifiable |
| 5. Empirical asymmetry | 15 | 6 | Weak — asymmetry claimed but controlled experiment shows reversed effect, no independent reproduction, effect size provenance unclear, novel predictions exist but untested |
| **Total** | **69** | **35** | **Frame, not law** |

---

## Self-Assessment

My solo score: **35 / 69 — Frame, not law.**

The framework has the *structure* of a conservation law:
- A defined conserved quantity (deontic invariant, set-valued)
- A stated invariance principle (candidate, not proven)
- An independent measurement instrument (public, but shared substrate)
- Explicit falsifiability conditions (pre-registered, publicly testable)
- A claimed empirical asymmetry (governed vs. ungoverned)

But the *empirical foundation* is insufficient:
- The controlled experiment (EXP-003) does not cleanly demonstrate the predicted asymmetry — baseline NLI is higher than gate NLI
- The headline number (0.94 vs 0.42) comes from a preliminary run, not the controlled experiment, and its provenance is unclear
- No independent replication exists
- The formal foundation has a deep gap (no Lagrangian, no Noether theorem, C(S) not formalized information-theoretically)
- The symmetry is discrete, not continuous (Noether's theorem doesn't apply)
- The instrument independence is limited (shared transformer substrate)
- No calibration standards exist

The framework is at the "frame" stage — the structure is there, the falsifiability is genuine, the scope is honest, but the empirical grounding is insufficient to call it a law. The gap between frame and law is primarily empirical (the asymmetry needs to be clean and replicated) and formal (the invariance needs to be proven, not just stated).

**What would move it up:**
1. Run EXP-008 (fixed gate) — if 5-6 of 7 failures recover, the gate-vs-baseline asymmetry becomes clean
2. Independent replication — if an external party runs the harness and gets the same results
3. Cross-oracle testing — if a non-transformer oracle (human evaluators, formal logic) confirms the NLI results
4. Formal invariance proof — if FS-001's candidate definition is confirmed and the group properties are proven
5. Clarify the 0.94 number — either show it comes from EXP-003 with a specific metric computation, or correct the paper to use the controlled experiment numbers

**What would move it down:**
1. If EXP-008 shows the gate fix doesn't recover the failures — the 7/20 are law failures, not instrument failures
2. If independent replication fails to find the asymmetry
3. If the baseline NLI > gate NLI pattern replicates with a different oracle — suggesting the law doesn't hold even under governance
4. If the 0.94 number cannot be traced to any legitimate computation — a paper error that undermines credibility
