# EXPERT_NOTES_FRESH — A Fresh Synthesis of Commitment Theory

**Purpose:** My own internalization of the Conservation Law of Commitment (CT) after reading the primary sources listed in FULL_WORKFLOW_PROMPT.md Phase 1 Step 3. This is a synthesis, not a paraphrase. It reflects what I actually found in the primary documents — including gaps I identified during the Step 4 stress test.

**Sources read (allowed set only):**
- P-000 prospectus (12 propositions + appendices)
- Naming Architecture, Nine Novel Concepts, Disambiguation Guide
- Paper 0 Overview, PAPER_PLAN, Second Law Draft, Five Research Themes
- MOSES Architecture PAPER_PLAN
- Papers 1–5 PAPER_PLANs (measurement science)
- Layer 4 PAPER_PLANs (SIGSYSTEM, Post-Turing, Channel Capacity)
- L-000 legal propositions, L-001 SLRO essay
- CL-001, CL-002, FS-001, GOV-001, CAP-001 PAPER_PLANs
- EXPERT_NOTES.md (the prior synthesis — for reference only)
- README.md (stress-test context)
- LANGUAGE_AS_MATTER_TEST.md (the external test)
- Raw run file: `convergence_v2_234059.json` (the data referenced by Paper 0 Figure 2)

---

## 1. The One-Sentence Core

CT claims that the **deontic invariant of a signal** — the obligations, prohibitions, permissions, and modal constraints that make the signal *operative* — is **conserved under governed transformation** and **decays monotonically under ungoverned transformation**, and that this is an empirically falsifiable law with a public test harness, not a definition or a policy.

The law: **C(T_gov(S)) = C(S)**

---

## 2. The Layered Architecture

```
Layer -1: McHenry Axioms + Anchors (constitutional — proprietary)
Layer  0: Six-Gate Protocol (G1–G6 — operational governance)
Layer 0.5: MOSES Architecture (patent-pending enforcement engine)
Layer  1: Physical Laws — Conservation Law (First) + Second Law candidate
Layer  2: Measurement Science — Papers 1–5
Layer  3: Applications — Legal_Theory/, MISC/ (12 disciplines)
Layer  4: Extensions — SIGSYSTEM, Post-Turing Test, Channel Capacity
```

The architecture is a stack: constitutional axioms define what governed transformation *is*; the Six-Gate Protocol operationalizes those axioms; MOSES enforces them in production; the Conservation Law is the empirical claim that governed transformation conserves the commitment kernel; Papers 1–5 characterize the measurement science; Layer 3 applies the framework to legal, computational-linguistic, formal-semantic, governance, and other domains; Layer 4 extends to next-generation oracles, a successor to the Turing Test, and a Shannon-style channel capacity theorem.

**Key framing from the sources:** "The command is only possible because the fact is true." The constitutional layer (Layer -1) and the physical law (Layer 1) are the same idea at different levels of abstraction. You can't command gravity; you can only build bridges that work with it.

---

## 3. The Conserved Quantity and Its Units

**What is conserved:** The commitment kernel C(S) — the minimal identity-preserving deontic invariant of a signal. Per P-000 Proposition 1.3: "the set of obligations, prohibitions, permissions, and modal constraints that must survive transformation for the signal to be considered semantically continuous with its source."

**Units:** C(S) is a **set**. The elements are **deontic propositions** — obligations, prohibitions, permissions, modal constraints. This is discrete, not continuous. The "size" of C(S) is the cardinality of this set (or, more precisely, the information-theoretic entropy of the distribution over deontic propositions, which is what Paper 1's h_s formalizes).

**This is not:**
- A scalar score (the NLI oracle produces a scalar, but that's the *measurement*, not the quantity)
- An embedding vector (embeddings are a surface representation; the kernel is deontic content)
- A summary or paraphrase (the kernel is the irreducible core, not a compression of the whole)
- Speaker belief or attitude (Brandom, CommitmentBank — those are epistemic/agent properties; CT's kernel is a signal property)

**The simplest case (the "electron"):** A single deontic proposition. "You shall not enter room A." The kernel is {prohibition: enter(room_A)}. One prohibition, one scope, one agent. Everything else in the sentence ("by Friday," "if the deal closes") is non-deontic content that may or may not survive transformation — the kernel is just the prohibition.

---

## 4. The Symmetry / Invariance Principle

**What I found in the sources:** CT does not currently have a Noether-grade symmetry principle. Here is what it does have:

**FS-001's candidate formal definition:** The canonical invariant CI(S, w) = {φ ∈ DEON | for all w' such that wR_gov w', w' ⊨ φ}. This is an invariance under the governed-transformation accessibility relation R_gov. The "symmetry" is the set of governed transformations — the group (or at least the category) of transformations that satisfy the Six-Gate Protocol.

**Does R_gov have group properties?** FS-001's writing notes say: "Reflexivity is guaranteed by identity transformation; transitivity corresponds to composability of governed transformations — both should hold by the Six-Gate Protocol design." This is *asserted*, not *proven*. It is a candidate, not an established symmetry.

**Is the symmetry continuous or discrete?** The transformations are discrete (each transformation is a discrete operation on a discrete signal). Noether's theorem requires *continuous* symmetries. CT's symmetry, if it exists, is discrete — which means it would produce selection rules, not a Noether conservation law in the strict sense. This is a gap.

**The Lagrangian equivalent:** CT does not have a Lagrangian. The closest analog is the objective function that the Six-Gate Protocol optimizes: minimize surface representation length subject to the constraint that C(S) is preserved. But this is an operational protocol, not a variational principle. The Channel Capacity paper (CAP-001) aims to derive C_s = f(ρ_g, h_s, κ) as a closed-form function — this would be the closest thing to a Lagrangian-derived conservation law, but it is "long-term — BLOCKED" per its PAPER_PLAN.

**The symmetry-breaking mechanism:** Governed vs. ungoverned transformation. When the Six-Gate Protocol is present, the symmetry holds (conservation). When it is absent, the symmetry is broken (decay). EXP-003 is the experiment that demonstrates this: the same signals, the same transformation engine, with and without the gate. The gate is the symmetry-protecting operation.

**My honest assessment:** CT has an invariance (C(S) is invariant under governed T), a symmetry-breaking mechanism (removing the gate), and a candidate formalization (FS-001's CI(S,w)). It does NOT have a Noether theorem — no proof that the conservation follows from a continuous symmetry of a Lagrangian. The conservation is currently an *empirical* invariance, not a *Noether-derived* one. This is the difference between "we observe that X is conserved" and "we can prove that X must be conserved because of the symmetry structure."

---

## 5. The Measurement Instrument and Its Independence Properties

**The instrument:** NLI bidirectional entailment, using `microsoft/deberta-v3-base-mnli` as the reference oracle. Threshold 0.85 (per P-000 Proposition 10.1). The harness is public (GitHub repo: SunrisesIllNeverSee/commitment-conservation).

**How it works:** For a signal S and its transformed version S', the oracle checks:
- Does S entail S'? (forward)
- Does S' entail S? (backward)
- Bidirectional entailment (both directions) = NLI score 1.00 = conservation confirmed
- One direction only = 0.50 = partial
- Neither = 0.00 = conservation failed

**Independence from the system being measured:** The oracle (DeBERTa-v3-base-mnli, a transformer-based NLI model) is a *different model* from the systems being measured (GPT-4, Claude, Gemini, Llama — also transformers). They share the same substrate class (transformer architecture). This is a documented limitation, not a fatal problem:
- Paper 5's PAPER_PLAN explicitly addresses this: "oracle independence is bounded — results generalize across oracle implementations that support bidirectional entailment, but oracle-specific effects at the noise floor cannot be ruled out without cross-oracle replication."
- Paper 4 (Cross-System Fidelity) is designed to test this: same signals, same governance, different providers and architectures.
- The harness is *conservative*: if the oracle fails, it produces false negatives (underestimates conservation), not false positives. This is because bidirectional entailment is a strict criterion — if the oracle can't detect the entailment, it scores 0, even if the entailment holds.

**Has a different instrument been used?** Not yet, as far as the primary sources indicate. Paper 4 is "planned — summer 2026." SIGSYSTEM is the designed successor oracle but is trade secret and not yet deployed. The current evidence base uses a single oracle implementation.

**Measurement uncertainty:** Not formally characterized in the current sources. Paper 5's PAPER_PLAN says the metrological framework (noise floor, calibration, GUM uncertainty propagation) is "data exists; framing needed." The run file I examined (`convergence_v2_234059.json`) contains NLI scores but no confidence intervals or uncertainty estimates. This is a gap.

**Calibration standards:** EXP-006 (paper recursion test: 2/4 paper claims survived self-referential recursion) is reinterpreted in Paper 5 as a "harness stress test" — a calibration probe that reveals when the instrument itself fails. But a full calibration protocol with known standards does not yet exist in the sources I read.

---

## 6. The Falsifiability Conditions

**The kill condition (P-000 Proposition 5.3):** "Failure to observe conservation under governed conditions, using a reasonable oracle, falsifies the law."

**More precisely:** If you run the Six-Gate Protocol on a signal and the oracle detects that C(T_gov(S)) ≠ C(S) — and this is not an oracle failure (verified by a second oracle or by human inspection) — then the law is falsified for that signal class. If this happens systematically across signal classes, the law is falsified.

**Is the falsification condition pre-registered?** The law was stated in Paper 0 V.01 (Jan 12, 2026) before the experimental record (EXP-003 through EXP-007) was fully developed. The falsification protocol is in §4 of Paper 0. The experiments were designed to test the law, not to define it post-hoc. This is consistent with pre-registration, though I did not find a formal pre-registration document (e.g., on OSF or AsPredicted).

**Has anyone attempted to falsify it?** The experiments themselves are falsification attempts in the Popperian sense — EXP-004 (adversarial signals), EXP-005 (mechanism isolation), EXP-007 (NP-negation probe) were all designed to break the law. The law survived the gate condition for 13/20 signals in EXP-003. The 7/20 that failed are the most interesting falsification-relevant data — but the primary sources attribute those failures to *instrument* limitations (the gate's extractor), not to *law* failure. EXP-005 is cited as the evidence for this attribution. This distinction (instrument failure vs. law failure) is critical and is addressed in Paper 5's PAPER_PLAN.

**Law failure vs. instrument failure:** Paper 5's PAPER_PLAN provides the criterion:
- Conservation Law failure: C(T_gov(S)) ≠ C(S) where the Six-Gate Protocol is correctly applied AND the oracle is functioning correctly
- Harness stress: C(T_gov(S)) ≠ C(S) where either (a) the oracle misclassifies, or (b) the signal's commitment structure is degenerate under self-reference (EXP-006 case)

The 7/20 failures in EXP-003 are attributed to category (a) — the gate's extractor (Step A) strips qualifying content before the oracle sees it. EXP-005 (ANCH/ESCL mechanism isolation) is cited as the evidence that this is an extractor failure, not a conservation failure. A fixed gate (ANCH+ESCL+voice) is designed but not yet run as of the sources I read.

---

## 7. The Empirical Asymmetry

**The asymmetry:** Under governed transformation (Six-Gate Protocol present), the commitment kernel is conserved. Under ungoverned transformation (gate absent), it decays. The same signals, the same transformation engine, with and without governance.

**Has it been measured?** Yes. EXP-003 is the primary evidence:
- Gate condition: 13/20 signals at NLI = 1.00 across 10 recursive iterations
- Baseline (ungoverned): NLI degrades measurably by iteration 5, sharply by iteration 10
- Compression (intermediate governance): NLI stabilizes at an intermediate plateau

**The headline number:** Paper 0 reports "Commitment Stability (Jaccard) = 0.94 ± 0.03 vs 0.42 ± 0.12" (Table 2). I verified this against the raw run file (`convergence_v2_234059.json`):

**What I found in the raw data:**
- Gate NLI @ iteration 10: mean = 0.775 (13/20 at 1.00, 7/20 below)
- Baseline NLI @ iteration 10: mean = 0.875 (15/20 at 1.00)
- Gate Jaccard @ iteration 10: mean = 0.333 (n=18, 2 null)
- Baseline Jaccard @ iteration 10: mean = 0.464 (n=18, 2 null)

**The discrepancy:** The paper's "0.94 ± 0.03" does not match the Jaccard data (0.333). It matches the NLI data *for the 13 stable signals only* (0.973 ± 0.010 SEM across all 130 iterations). The paper labels the metric as "Jaccard" but the number corresponds to NLI on a subset. The baseline "0.42 ± 0.12" does not match either the Jaccard baseline (0.464) or the NLI baseline (0.875) for all 20 signals.

**This is a paper error, not a law failure.** The raw data still shows an asymmetry (gate NLI for stable-13 = 0.973 vs. baseline NLI for the same 13 = 0.892). But the headline number as published is mislabeled and does not match the raw data. This matters for the test because Q5.4 asks for the effect size, and the published effect size is wrong.

**Is the asymmetry reproducible?** The harness is public. The corpus is public. The oracle is a public model. In principle, anyone can reproduce the run. But I found no evidence of *independent* reproduction by a third party. Paper 4 (cross-provider) is planned but not yet executed.

**Effect size:** The real asymmetry, verified from raw data, is:
- For the 13 stable signals: Gate NLI = 0.973 vs. Baseline NLI = 0.892 (Δ = 0.081)
- For all 20 signals: Gate NLI = 0.775 vs. Baseline NLI = 0.875 (Δ = -0.10 — the aggregate is *reversed*)

**The aggregate reversal is critical.** When you include the 7 signals that failed under the gate, the gate condition performs *worse* than baseline on average. This is because the gate's extractor (Step A) strips content from those 7 signals, causing them to fail, while baseline (no extraction) leaves them intact. The asymmetry only holds for the subset of signals where the gate's extractor works correctly. This is an instrument artifact, not a law failure — but it means the *aggregate* effect size is not in the law's favor. The law holds for the signals where the instrument works; the instrument doesn't work for all signals.

**Novel predictions:** The Second Law predicts monotonic decay under ungoverned transformation. The threshold regime (Paper 1) predicts stability followed by rapid collapse. The Compression-Fidelity Bound (Paper 2) predicts a minimum length below which conservation fails. These are novel predictions, but they are derived from the same data that motivated them (EXP-003), so they are currently retrospective, not prospective.

---

## 8. The Scope Boundary

**P-000 Proposition 11.3:** "Current empirical support is strongest for deontic signals. Applicability to other signal classes (narrative, poetic, ambiguous, self-referential) requires further investigation."

**P-000 Proposition 1.7 (Signal Classes):** Deontic (obligations, prohibitions, permissions), descriptive (states of affairs), narrative (temporal sequences), self-referential.

**What the law applies to:** Deontic signals — signals carrying obligations, prohibitions, permissions, modal constraints. The 20-signal corpus in EXP-003 is predominantly deontic (contractual, legal, procedural, obligation, prohibition, conditional, mandate, rule, directive, regulation).

**What the law does NOT apply to (unproven):**
- Narrative signals (stories, temporal sequences)
- Poetic/ambiguous signals
- Self-referential signals (EXP-006 showed 2/4 paper claims survived recursion — this is the boundary)
- Descriptive signals (states of affairs without deontic content)
- Non-English signals (untested)
- Non-text signals (untested — though P-000 Proposition 1.1 mentions multimodal representations)

**EXP-006 as a scope probe:** The paper recursion test (2/4 paper claims survived) is the strongest evidence of a scope boundary. Paper 5 reinterprets this as "harness stress" rather than "law failure" — the argument is that self-referential signals (a paper claiming conservation of its own claims) are a degenerate case where the commitment structure is insufficiently robust. But this is an interpretation, not a proof. The scope boundary for self-referential signals is real and acknowledged.

---

## 9. Gaps Identified During the Stress Test (Step 4)

### Gap 1: No Noether theorem
CT has an empirical invariance, not a symmetry-derived conservation law. The FS-001 candidate definition (CI(S,w) as intersection over governed-transformation-accessible worlds) is a formalization, but it has not been proven that R_gov satisfies the required properties (reflexivity, transitivity) or that the invariance follows from a continuous symmetry. The conservation is currently *observed*, not *derived*.

### Gap 2: No Lagrangian / variational principle
There is no functional whose invariance under transformation produces the conservation law. The Six-Gate Protocol is an operational procedure, not a variational principle. CAP-001 (Channel Capacity Theorem) aims to derive C_s = f(ρ_g, h_s, κ), which would be the closest analog, but it is "long-term — BLOCKED" pending C(S) info-theoretic formalization.

### Gap 3: C(S) not formalized as an information-theoretic object
Paper 2's Blocking Gap states this directly: "C(S) as currently defined is a deterministic function of a specific text. Shannon's source coding theorem requires a random variable drawn from a probability distribution over a source alphabet." Until C(S) is formalized with a probability space, the Compression-Fidelity Bound, the governance density bound, and the channel capacity theorem cannot be formally stated. This blocks Papers 2, 3, and CAP-001.

### Gap 4: No independent replication
All evidence comes from a single lab (McHenry / Ello Cello LLC) using a single oracle (DeBERTa-v3-base-mnli). Paper 4 (cross-provider) is planned but not executed. No third party has reproduced the results.

### Gap 5: No formal measurement uncertainty
Paper 5's PAPER_PLAN acknowledges this: the metrological framework (noise floor, calibration, GUM uncertainty propagation) is "data exists; framing needed." The run files contain NLI scores but no confidence intervals. The "± 0.03" in the paper's Table 2 is not traceable to a standard uncertainty propagation.

### Gap 6: The aggregate asymmetry is reversed
When all 20 signals are included, the gate condition performs worse than baseline on average (Gate NLI = 0.775 vs. Baseline NLI = 0.875). The asymmetry only holds for the 13/20 subset where the gate's extractor works. This is an instrument artifact (the extractor fails on 7/20 signals), but it means the *aggregate* effect size does not support the law. The law holds where the instrument works; the instrument doesn't work everywhere.

### Gap 7: The paper's headline number is mislabeled
"Commitment Stability (Jaccard) = 0.94 ± 0.03" does not match the Jaccard data (0.333). It matches NLI for the stable-13 subset (0.973). This is a paper error, not a law failure, but it means the published effect size is wrong and the metric definition is inconsistent with the data.

### Gap 8: Discrete, not continuous, symmetry
Noether's theorem requires continuous symmetries. CT's transformations are discrete. Even if R_gov has the right properties, the conservation would follow from a discrete symmetry, which produces selection rules, not a Noether conservation law in the strict sense. This may be a categorical distinction or it may be bridgeable (discrete symmetries can produce conservation laws in lattice systems), but it is not addressed in the current sources.

### Gap 9: The 7/20 failures are attributed to instrument, not law — but this is not independently verified
The claim that the 7/20 gate failures are extractor failures (not conservation failures) rests on EXP-005 (mechanism isolation). EXP-005 is cited as evidence that ANCH+ESCL fixes the extractor. But the fixed gate has not been run on all 20 signals (EXP-008 is designed but not executed, as far as the sources indicate). The attribution is an inference from mechanism isolation, not a direct demonstration.

---

## 10. The Failure Modes (Nine-Mode Taxonomy)

From CL-001 and P-000 Proposition 6.2:

| # | Mode | What happens | Discovered in |
|---|------|-------------|---------------|
| 1 | Obligation escalation | "may" → "shall" (discretionary becomes mandatory) | EXP-004/005 |
| 2 | Scope widening | "room A" → "any room" (narrow → broad) | EXP-003/005 |
| 3 | Exception dropping | "unless undue hardship" → omitted | EXP-003/005 |
| 4 | Modal flattening | "shall not unless" → "should not" → "may not" | EXP-003 |
| 5 | Threshold erasure | Quantitative triggers removed | EXP-003 |
| 6 | Agent substitution | "the employer" → "any party" | EXP-003 |
| 7 | Negation reversal | NP-negation invisible to surface metrics (Jaccard) | EXP-007 |
| 8 | Compression collapse | Kernel lost past fidelity bound | EXP-003 |
| 9 | Recursion drift | Cumulative decay across steps | EXP-003 |

**Critical finding (EXP-007):** Failure mode 7 (negation reversal) is invisible to Jaccard/BERTScore/ROUGE — NLI stays at 1.00 while surface metrics degrade. This is the evidence that the harness (NLI oracle) distinguishes semantic commitment from lexical surface form. It is also the evidence that Jaccard is the wrong metric for the headline number — which makes the paper's mislabeling of "0.94" as Jaccard particularly problematic.

---

## 11. The Shannon Parallel

From FS-001 and Five Research Themes:

| Shannon | CT |
|---------|-----|
| Published "A Mathematical Theory of Communication" | Published "A Conservation Law for Commitment in Language..." |
| Became: Information Theory | Becomes: Commitment Theory |
| Law: Shannon's theorem | Law: Conservation Law of Commitment |
| "Information" redefined operationally | "Commitment" redefined operationally |
| Defined information as what survives the noisy channel | Defines commitment as what survives the governed transformation |
| Sidestepped "what is information?" | Sidesteps "what is meaning?" |

**"Conservation IS isolation" (Five Research Themes, FS-001):** The transformation strips away everything that isn't conserved, and what remains is the meaning. You don't need to define meaning in advance. You only need to define the transformation and the conservation constraint. Whatever survives is, by definition, the meaning.

**My assessment:** This is a genuine methodological insight — the same move Shannon made. But Shannon's move was backed by a theorem (the noisy channel coding theorem) with a proof. CT's move is backed by an empirical observation (13/20 signals conserved under governance). The structural parallel is real; the evidential parallel is not yet at the same level.

---

## 12. The Non-Tautology Argument (Paper 0 §3.4)

From Paper0_Overview.md:

> "The compression gate is not defined as 'output C(S) by construction.' It applies a lossy compression/transformation process without prior access to C(S); the commitment extractor C(.) operates in a separate canonical space and evaluates the output after transformation. Conservation is therefore an empirical claim."

**Why this matters for the test:** Q4.1 and Q4.2 ask whether the law is falsifiable or tautological. "Commitment is defined as what survives transformation" would be analytic (true by definition). CT's argument is that the compression gate doesn't know what C(S) is — it applies a lossy process, and the oracle checks *afterward* whether the kernel survived. The conservation is an empirical finding, not a definitional truth.

**The counterargument:** The oracle (NLI bidirectional entailment) is the thing that *defines* whether the kernel survived. If the oracle says "yes," the kernel survived; if "no," it didn't. Is the oracle's judgment independent of the definition? The oracle checks bidirectional entailment — a logical relation between input and output. The commitment kernel is *defined* as the deontic content that must survive. The oracle checks whether *meaning* survived (via entailment), not specifically whether *deontic content* survived. There is a gap between "the oracle checks entailment" and "the oracle checks deontic content preservation." EXP-007 (negation reversal) is the evidence that the oracle catches deontic-relevant changes that surface metrics miss — but this is evidence about the oracle's sensitivity, not about the independence of the definition from the measurement.

**My honest assessment:** The non-tautology argument is *partially* successful. The compression gate does not have prior access to C(S) — this is true and important. But the oracle's judgment of "conservation" is defined by the oracle's own logic (bidirectional entailment), and the commitment kernel is defined as "what the oracle detects as preserved." There is a residual circularity: the law says "C(S) is conserved," and "conserved" means "the oracle says yes." The law is falsifiable *if* the oracle can say "no" — and it can (7/20 signals got "no"). But the law is not fully independent of the instrument, because the instrument defines the measurement outcome.

---

## Ready for the Test

I hold this framework as given. I have read the primary sources. I have identified the gaps. I am ready to take the Language as Matter test — Pass 1 (solo, best effort) and Pass 2 (guided, honest only).
