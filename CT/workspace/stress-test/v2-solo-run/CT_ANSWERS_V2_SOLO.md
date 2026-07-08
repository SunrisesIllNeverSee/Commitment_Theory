# CT Answers V2 — Solo Run

**Test:** Language as Matter — External Validity Test
**Answered from:** CT primary sources (P-000, Paper 0, Papers 1-5, Layer 4, Legal track, MISC track, Expert Notes)
**Date:** 2026-07-08
**Mode:** CT held as true. Answers from within the framework. Honest about gaps.

---

## Requirement 1: A Defined Conserved Quantity

### Q1.1 — What exactly is conserved? Define it in one sentence without using the word "commitment" or referencing your own measurement tools.

The deontic kernel of a signal — the minimal set of obligations, prohibitions, permissions, and modal constraints that must survive a transformation for the signal to remain semantically continuous with its source — is conserved under governed transformation.

**CT source:** P-000 Proposition 1.3 defines C(S) as "the minimal identity-preserving deontic invariant of the signal — the set of obligations, prohibitions, permissions, and modal constraints that must survive transformation for the signal to be considered semantically continuous with its source." The Nine Novel Concepts document defines it as "the irreducible core of operative meaning." The constraint here is that I cannot use the word "commitment" — CT's own term is "commitment kernel," but the substance is the deontic invariant: the obligations, prohibitions, permissions, and modal constraints. That is what is conserved.

### Q1.2 — What are its units or dimension?

**CT does not currently specify units or a dimension for C(S).** This is an acknowledged gap.

CT defines C(S) operationally — as the output of a measurement procedure (NLI bidirectional entailment, threshold 0.85) — rather than as a dimensioned physical quantity. The current measurement produces a binary outcome (conserved / not conserved) or a scalar fidelity score in [0, 1], not a quantity with physical units.

Paper 2 (Compression-Fidelity Bound) acknowledges this as a blocking gap: "C(S) as currently defined is a deterministic function of a specific text. Shannon's source coding theorem requires a random variable drawn from a probability distribution over a source alphabet. The proof in Section III cannot be constructed until C(S) is formalized as an information-theoretic object." Paper 2's path forward proposes defining C(S) under a corpus distribution P, yielding H(C(S)) — the Shannon entropy of the commitment kernel distribution — as the relevant information-theoretic quantity. If that formalization succeeds, the natural "unit" would be bits (Shannon entropy), placing C(S) in the same dimension as information itself.

Paper 1 defines the semantic entropy rate h_s as a Shannon-style entropy rate, which would carry units of bits per transformation step. The kernel complexity κ(S) is referenced in the channel capacity work (CAP-001, Layer 4 Channel Capacity) as a parameter of C_s = f(ρ_g, h_s, κ), but its units are not yet specified.

**Honest assessment:** CT has an operationally defined conserved quantity but not yet a dimensioned one. The information-theoretic formalization (Paper 2's blocking gap) is the path to units, and the natural candidate is bits — but this is not yet established.

### Q1.3 — Can it be defined by someone who disagrees with your theory? (i.e., is the definition theory-independent, or does it only make sense within CT?)

Partially. The *components* of the conserved quantity are theory-independent; the *framing* as a conserved invariant is CT's contribution.

The components — obligations, prohibitions, permissions, modal constraints — are standard objects from deontic logic (von Wright, 1951) and formal semantics (von Fintel, Kratzer). A researcher who rejects CT entirely can still identify the deontic content of a signal: "shall not sublease without written consent" contains a prohibition and a condition. That is not CT-proprietary. The Disambiguation Guide explicitly notes: "CT does not reinvent deontic categories. It asks a new question: are they conserved?"

The *question* CT asks — whether this deontic content survives transformation — is also independently meaningful. A critic can ask "does the prohibition survive summarization?" without accepting that the answer constitutes a conservation law. The empirical procedure (extract deontic content, transform, extract again, check bidirectional entailment) is reproducible by anyone with the harness.

What is CT-specific is the *claim* that the survival of this content under governed transformation constitutes a conservation *law* (in the physics sense), and the theoretical apparatus built around that claim (the Six-Gate Protocol, MOSES, the Second Law, the Shannon parallel). A skeptic can perform the measurement without accepting the law-status of the result.

**FS-001** formalizes the commitment kernel as a "canonical invariant" within intensional semantics: CI(S, w) = {φ ∈ DEON | for all w' such that wR_gov w', w' ⊨ φ} — the set of deontic propositions holding in every world reachable via governed transformation. This definition uses only standard possible-worlds semantics (accessible worlds, deontic modality) plus CT's governed-transformation relation R_gov. The deontic propositions and the possible-worlds framework are not CT's invention; only R_gov is.

**Honest assessment:** The conserved quantity's components are theory-independent (deontic logic, formal semantics). The claim that their survival constitutes a conservation law is CT's. The measurement procedure is reproducible by non-believers. The formal invariant definition (FS-001) uses standard semantic machinery plus one CT-specific relation. This is partial theory-independence — stronger than pure circularity, weaker than full theory-independence.

### Q1.4 — What is the minimal case — the simplest possible signal that carries the conserved quantity?

A single deontic operator with its scope. The simplest case CT identifies is a prohibition: **"shall not."**

From the Expert Notes and the failure mode taxonomy, the minimal commitment-bearing signals are modal-anchored — those whose kernel is carried by modal operators. The simplest is a bare prohibition: "X shall not Y." This carries one deontic element (a prohibition) and nothing else. If the "shall not" survives transformation, the kernel is conserved. If it becomes "should not" (modal flattening, failure mode 4) or "shall" (modal frame inversion), the kernel is violated.

A slightly richer minimal case — and the one CT uses as its canonical example — is **"reasonable accommodation unless undue hardship"** (from the ADA). This carries an obligation (accommodate) plus a limiting exception (unless undue hardship). It is minimal in the sense that it contains exactly two deontic elements (obligation + exception), and the exception-dropping failure mode (mode 3) is precisely the case where one element is lost. This is CT's "electron" in the sense that it is the smallest case where conservation is non-trivial: a single "shall not" either survives or doesn't, but the two-element case shows that *partial* loss (exception dropped, obligation retained) is the characteristic failure mode.

From CL-002's regime classification, the modal-anchored regime — signals whose kernel is carried by modal operators — exhibits the highest conservation rates under governance. This is the regime where the conserved quantity is most cleanly isolable.

**Honest assessment:** CT identifies modal-anchored signals as the simplest case and "shall not" as the minimal deontic element. The framework has not formally proven that this is the absolute minimum (could a sub-modal element carry deontic content?), but operationally, a single modal operator is the simplest signal the harness tests.

---

## Requirement 2: A Symmetry or Invariance Principle

### Q2.1 — What is the symmetry? What transformation leaves the system's action (or equivalent functional) invariant?

The symmetry is **invariance under governed transformation** — the transformation group T_gov leaves C(S) invariant by definition of the conservation law: C(T_gov(S)) = C(S) for all T_gov in the governed transformation class.

More precisely: the "symmetry" in CT is the set of transformations that preserve the commitment kernel. A transformation T is in the symmetry group if and only if it satisfies the Six-Gate Protocol (G1-G6) — that is, if it passes through the constitutional constraints designed to preserve C(S). The conserved quantity C(S) is invariant under this group of transformations.

This is structurally analogous to how Noether's theorem works: the conserved current is invariant under the symmetry group. In CT, the "symmetry group" is the class of governed transformations, and C(S) is the conserved current.

However, **CT does not explicitly frame this as a Noether symmetry.** CT's framing is empirical (the law is a discovered regularity, P-000 Proposition 5) and operational (the Six-Gate Protocol defines the governed class), not derived from a symmetry principle. The symmetry is implicit in the structure — governed transformations are defined as those that preserve C(S), and the law states that they do — but CT has not formally shown that a continuous symmetry *generates* the conservation, in the Noether sense. The relationship is: CT defines a class of transformations (governed) and observes empirically that C(S) is invariant under that class. Whether this invariance *arises from* a deeper symmetry (the way energy conservation arises from time-translation symmetry) is an open question CT has not addressed.

FS-001's formalization offers the closest analog: the governed transformation induces an accessibility relation R_gov on possible worlds, and CI(S, w) is the intersection of deontic extensions across all R_gov-accessible worlds. The "symmetry" is the invariance of CI(S, w) across the orbit of R_gov-accessible worlds. But this is a semantic invariance, not a Noether-type symmetry derived from a variational principle.

**Honest assessment:** CT has an invariance (C(S) is invariant under the governed transformation class) but has not identified a Noether-type continuous symmetry that *generates* the conservation. The invariance is defined operationally (Six-Gate Protocol) and observed empirically, not derived from a symmetry principle. This is a significant gap relative to the physics standard.

### Q2.2 — Is the symmetry continuous or discrete?

**CT does not specify whether the symmetry is continuous or discrete.** The question has not been addressed in CT's documents.

The governed transformation class is defined by the Six-Gate Protocol — a discrete set of six gates. A transformation either passes all six (governed) or doesn't (ungoverned). This suggests a *discrete* structure: the symmetry group is defined by a discrete set of constraints, not a continuous parameter.

However, Paper 3 (Governance Density) introduces governance density ρ_g as a continuous parameter — the ratio of constraint operations to transformation operations — and derives a sparsity bound ρ* such that conservation holds for ρ_g ≥ ρ* and fails for ρ_g < ρ*. This suggests a *continuous* transition: as governance density increases past the threshold, conservation "turns on." If ρ_g is a continuous parameter and conservation depends on it continuously, the symmetry might be continuous in ρ_g.

But Paper 3 is BLOCKED (inherits Paper 2's formalization gap), so this continuous characterization is theoretical, not established.

If Noether's theorem strictly requires continuous symmetries (which is the standard reading), and CT's symmetry is discrete (gate-pass/fail), then CT's conservation would not be a Noether-type conservation law. It would be more analogous to a discrete symmetry producing a selection rule — which, as the test notes, is "not a conservation law in the Noether sense."

**Honest assessment:** CT has not addressed this question. The operational structure (Six-Gate Protocol) suggests discrete symmetry. The theoretical aspiration (governance density as continuous parameter) suggests continuous. This is unresolved and is a genuine gap relative to the Noether requirement.

### Q2.3 — What is the equivalent of the Lagrangian?

**CT does not have an explicit Lagrangian or equivalent variational functional.** This is not addressed in any CT document.

The closest analog CT offers is the **governance density functional** — the relationship C_s = f(ρ_g, h_s, κ) from the Semantic Channel Capacity theorem (CAP-001, Layer 4 Channel Capacity). This functional relates the semantic channel capacity to governance density, semantic entropy rate, and kernel complexity. If one were to seek a CT Lagrangian, the natural candidate would be a functional whose extremization under the governance constraint yields the conservation law — but CT has not constructed this.

Another candidate: the **fidelity functional** Fid(S, S') = degree to which C(S') matches C(S), as measured by bidirectional entailment. The conservation law states Fid(S, T_gov(S)) = 1. But this is the *measurement* of conservation, not the *generator* of it. In physics terms, it is the equation of motion (the constraint), not the Lagrangian (the functional whose symmetries produce the constraint).

FS-001's canonical invariant definition — CI(S, w) = {φ ∈ DEON | for all w' such that wR_gov w', w' ⊨ φ} — is defined within possible-worlds semantics, not within a variational framework. There is no action principle, no stationary-action derivation, no Euler-Lagrange equation in CT.

The Shannon parallel offers a structural analogy but not a Lagrangian: Shannon's channel capacity theorem is an optimization result (maximize mutual information over input distributions), which *is* a variational problem. If CT's semantic channel capacity theorem (CAP-001) is eventually proven, it would be a variational result in the same sense — maximizing commitment transmission rate over governance configurations. But CAP-001 is long-term and BLOCKED.

**Honest assessment:** CT does not have a Lagrangian equivalent. This is a fundamental gap. The conservation law is stated as an empirical regularity and an operational definition, not as the consequence of a variational principle. The channel capacity work (CAP-001) might eventually provide a variational structure, but it is not yet developed. CT cannot currently answer this question.

### Q2.4 — Does the conservation fail when the symmetry is broken?

**Yes — and this is the core empirical claim of CT.** This is the strongest part of CT's case relative to the physics criteria.

The "symmetry" (governed transformation) is broken when governance is absent (ungoverned transformation). When the symmetry is broken, conservation fails: C(T_ungov(S)) ≠ C(S). This is the Second Law of Semantic Entropy (P-000 Proposition 6): under ungoverned transformation, the commitment kernel decays monotonically (ΔH_C > 0), with cumulative entropy Ω(σ√n).

The testable prediction is explicit: if you remove the Six-Gate Protocol (break the symmetry), commitment is NOT conserved. If you apply the Six-Gate Protocol (preserve the symmetry), commitment IS conserved. The asymmetry between governed and ungoverned conditions is the empirical signature of the law.

EXP-003 demonstrates this directly: under the Gate condition, 13/20 signals achieved NLI = 1.00 across 10 recursive iterations. Under baseline/compression conditions (governance absent), NLI degraded measurably by iteration 5 and sharply by iteration 10. The conservation fails when the symmetry (governance) is broken.

Paper 3 (Governance Density) further predicts that conservation fails not just when governance is fully absent but when it falls below a threshold ρ*: for ρ_g < ρ*, commitment decay is inevitable regardless of constraint type. This is a graded symmetry-breaking prediction — conservation fails progressively as governance density drops below the sparsity bound.

**Honest assessment:** This is well-addressed. CT's central empirical claim is precisely that conservation fails when the symmetry (governance) is broken. The Second Law formalizes the failure mode. EXP-003 provides direct evidence. Paper 3's governance density threshold provides a graded failure prediction (though not yet empirically tested). This is the strongest answer in the symmetry requirement.

---

## Requirement 3: An Independent Measurement Instrument

### Q3.1 — What instrument measures the conserved quantity? Name it.

The current instrument is the **CT measurement harness** (also called the Commitment Conservation Harness, CCH), using **NLI bidirectional entailment** via the `microsoft/deberta-v3-base-mnli` model at threshold 0.85 as its oracle.

The harness procedure (from P-000 Proposition 10.1, Paper 0, Paper 5):
1. Extract the commitment kernel from the source signal
2. Apply the transformation
3. Extract the commitment kernel from the output
4. Check bidirectional entailment: does the output entail the source AND does the source entail the output?
5. If both directions entail, NLI = 1.00, conservation confirmed. If not, conservation failed.

The next-generation instrument is **SIGSYSTEM** — a word-level contextual weighting oracle that distinguishes deontic signal words from noise words. SIGSYSTEM's architecture is trade secret; its functional contract is: input S → output σ(S) ∈ [0,1] (proportion of content that is deontic signal vs. noise). SIGSYSTEM is not yet deployed as the primary oracle.

### Q3.2 — Is the instrument independent of the system being measured? (Specifically: if the conserved quantity is in language, and the instrument is a language model, is that independent?)

**Partially.** This is a nuanced question that CT addresses explicitly but does not fully resolve.

The *current* oracle (DeBERTa-v3-base-mnli) is a language model measuring whether language preserved its deontic content. The system being measured is typically also a language model (GPT-4, Claude, etc.) performing the transformation. So the oracle and the system being measured are the same *type* of system (neural language models). This is the independence concern the question raises.

CT's argument for independence rests on several distinctions:

1. **Architectural independence:** DeBERTa-v3-base is a different architecture from the LLMs being tested (GPT-4, Claude, Gemini). It is a smaller, purpose-built NLI model, not a general-purpose generative model. It was not trained on the transformation task; it was trained on MNLI (Multi-Genre Natural Language Inference). The oracle and the transformer are different models with different training objectives.

2. **Functional independence:** The oracle does not perform transformations. It only judges entailment between two texts. The system being measured performs the transformation. The oracle evaluates the result. They serve different functions in the pipeline.

3. **Oracle independence by design (P-000 Proposition 10.3):** "The oracle is a measurement instrument, not the law itself. Any party may substitute a stronger oracle. The law's validity does not depend on any single oracle." The law is defined independently of the oracle; the oracle is a measurement tool, not the definition of the conserved quantity.

4. **Paper 5 (Measurement Instrument) oracle independence analysis:** "Oracle independence is bounded: results generalize across oracle implementations that support bidirectional entailment, but oracle-specific effects at the noise floor cannot be ruled out without cross-oracle replication." Paper 4 (Cross-System Fidelity) is designed to test whether results generalize across providers and architectures.

**The honest concern:** Both the oracle and the system being measured are language models operating on language. They share a substrate class. A critic could argue that any NLI model has systematic blind spots (e.g., negation scope, quantifier ambiguity) that align with the blind spots of generative LLMs, producing correlated errors that mimic conservation. CT's EXP-007 (NP-negation probe) partially addresses this: it shows that the oracle *detects* a failure mode (negation reversal) that surface metrics miss, demonstrating the oracle is not simply tracking surface similarity. But this does not prove the oracle is independent of the LLM substrate class.

SIGSYSTEM is designed to address this by operating at the word level with explicit signal/noise weighting, but it is not yet deployed.

**Honest assessment:** CT acknowledges the independence question and provides architectural and functional arguments for independence, plus oracle independence by design (any NLI oracle can be substituted). But the current oracle is the same substrate class (language model) as the systems being measured. Cross-oracle replication (Paper 4's program) is planned but not yet executed. This is partial independence — stronger than self-confirmation (the oracle is a different model with a different purpose), weaker than full ontological independence (both are language models).

### Q3.3 — Can a different instrument (one you didn't build or choose) measure the same quantity and get the same result? Has this been done?

**The design permits it; the empirical verification has not yet been completed.**

P-000 Proposition 10.3 (Oracle Independence): "The oracle is a measurement instrument, not the law itself. Any party may substitute a stronger oracle. The law's validity does not depend on any single oracle."

Paper 0 Section VII (Oracle Independence and Falsifiability): "The Conservation Law is testable with any oracle that supports bidirectional entailment." The harness is public (GitHub repo: github.com/SunrisesIllNeverSee/commitment-conservation), so any researcher can substitute a different NLI model (e.g., RoBERTa-MNLI, BART-MNLI, a human judge, or a formal theorem prover) and run the same experiments.

Paper 5 (Measurement Instrument) states: "Oracle independence is bounded: results generalize across oracle implementations that support bidirectional entailment, but oracle-specific effects at the noise floor cannot be ruled out without cross-oracle replication."

**Has this been done?** Not yet, based on the documents available. Paper 4 (Cross-System Fidelity) is "Planned — Summer 2026" and is designed to test conservation across providers (GPT-4, Claude, Gemini, Llama) — but this tests whether the *transformation* generalizes across systems, not whether the *oracle* generalizes. The cross-oracle replication (running the same experiments with a different NLI model) is identified as necessary by Paper 5 but has not been executed.

The harness is public and the corpus is deposited (Zenodo DOI: 10.5281/zenodo.19105225), so the *capability* for independent verification exists. But the *act* of independent verification — a different party using a different oracle to reproduce the results — is not documented in the current CT corpus.

**Honest assessment:** The design supports instrument substitution (any bidirectional entailment oracle). The harness and corpus are public, enabling independent replication. But cross-oracle replication has not yet been performed. This is "claimed by design but not yet demonstrated."

### Q3.4 — What is the measurement uncertainty?

**CT does not currently state a formal measurement uncertainty for individual conservation measurements.** Paper 5 (Measurement Instrument) identifies this as needed work and proposes a framework for it.

The current measurement produces a binary outcome: NLI bidirectional entailment = 1.00 (conserved) or < 1.00 (not conserved), with threshold 0.85. The "uncertainty" in the current framework is:

1. **Signal-level uncertainty:** 13/20 signals achieved NLI = 1.00 under governance (EXP-003). The other 7 did not. The conservation rate is 65% (13/20) under the Gate condition. This is a Bernoulli parameter; the Wilson 95% confidence interval for 13/20 is approximately [43.2%, 82.9%]. Paper 5's writing notes recommend: "report conservation rates as Bernoulli parameters with Wilson confidence intervals; this is GUM-compatible and appropriate for discrete outcomes."

2. **Oracle uncertainty:** The NLI model (DeBERTa-v3-base-mnli) has known failure modes — paraphrase detection, abstract/concrete shifts, quantifier scope. Paper 0's writing notes acknowledge: "the harness is conservative — false negatives produce underestimates of conservation, not overestimates." This is a systematic error bound in one direction: the oracle may *fail to detect* conservation (false negative) but is argued to not *falsely report* conservation (false positive). This asymmetry is claimed but not formally quantified.

3. **Noise floor:** Paper 5 proposes characterizing the harness's noise floor (minimum detectable commitment change) using EXP-007 data and synthetic adversarial inputs. This characterization is planned but not yet completed.

4. **GUM framework:** Paper 5 proposes applying the GUM (JCGM 100:2008) uncertainty framework, addressing Type A uncertainty (repeated measurement) and Type B uncertainty (systematic error from known oracle failure modes). This is the metrologically correct approach but is not yet implemented.

**Honest assessment:** CT does not have a stated measurement uncertainty. The empirical data (13/20, 65% conservation rate) allows a Wilson confidence interval to be computed, and Paper 5 identifies the GUM framework as the right approach. But no formal uncertainty analysis has been conducted. This is a gap relative to the physics standard (every physical measurement has a stated uncertainty).

### Q3.5 — What happens when the instrument fails? Do you have calibration standards for your oracle?

**CT has partial calibration evidence but not a formal calibration protocol.**

Paper 5 (Measurement Instrument) is the document that addresses this most directly. Key points:

1. **EXP-006 as harness stress test:** EXP-006 (paper recursion test: 2/4 paper claims survived self-referential recursion) is reinterpreted in Paper 5 not as a conservation law failure but as a harness stress test — it identifies conditions under which the instrument itself fails due to commitments that are insufficiently robust to withstand their own recursion. Paper 5 establishes explicit criteria: "Conservation Law failure: C(T_gov(S)) ≠ C(S) where the Six-Gate Protocol is correctly applied AND the oracle is functioning correctly. Harness stress: C(T_gov(S)) ≠ C(S) where either (a) the oracle misclassifies the commitment kernel (oracle failure) or (b) the signal's commitment structure is degenerate under self-reference."

2. **EXP-007 as oracle validation:** EXP-007 (NP-negation probe) demonstrates that the oracle *can* detect a failure mode (negation reversal) that surface metrics (Jaccard, BERTScore, ROUGE) cannot. This is evidence the oracle is measuring something real, not just tracking surface similarity. But it also reveals the oracle's sensitivity profile — it detects some failures and misses others.

3. **Known oracle failure modes:** Paper 0's writing notes identify: paraphrase detection (partially addressed by EXP-007), abstract/concrete shifts, quantifier scope. These are known calibration issues. Paper 5 proposes a calibration protocol but it is not yet implemented.

4. **Adversarial sensitivity:** Paper 5 Section IV characterizes the harness's susceptibility to specific adversarial constructions (NP-negation, synonym substitution, structural paraphrase) and characterizes which failure modes exploit the oracle's surface-form sensitivity. This is a partial calibration — it identifies what the oracle is *bad* at.

5. **SIGSYSTEM as designed successor:** Paper 5 and the SIGSYSTEM paper plan describe SIGSYSTEM as motivated by the specific limitations of the NLI-based approach identified in the metrological analysis. The instrument's known failure modes are the design requirements for its successor.

**Calibration standards:** CT does not have a formal calibration standard (a reference signal with known conservation status against which the oracle is regularly tested). Paper 5 proposes a calibration protocol but it is not yet implemented. The closest thing to a calibration standard is the EXP-003 corpus itself — 20 signals with known governance conditions and measured conservation outcomes. But this is the measurement set, not an independent calibration standard.

**Honest assessment:** CT has identified when the instrument fails (EXP-006, EXP-007) and has proposed a framework for calibration (Paper 5, GUM). But it does not yet have a formal calibration protocol or a reference standard. The distinction between "law failed" and "instrument failed" is articulated in principle (Paper 5) but not yet operationalized in a calibration procedure. This is partial — the thinking is there, the implementation is not.

---

## Requirement 4: Falsifiability with Specified Failure Conditions

### Q4.1 — State the specific observation that would falsify your conservation law. Not "it might fail" — the exact result that would kill it.

**P-000 Proposition 5.3 (Falsifiability):** "The law is falsifiable. A public test harness and corpus are available. Any party may substitute a stronger oracle or design adversarial signals. Failure to observe conservation under governed conditions, using a reasonable oracle, falsifies the law."

The specific falsifying observation: **A signal S, transformed under the Six-Gate Protocol (governed transformation T_gov), where the oracle (any reasonable NLI bidirectional entailment model) reports that C(T_gov(S)) ≠ C(S) — i.e., the commitment kernel is not conserved despite governance being correctly applied.**

More concretely: if a researcher constructs a signal, applies the full Six-Gate Protocol (compression, lineage verification, fidelity verification, recursion testing, consumption/metabolism, custodial sovereignty), and the NLI bidirectional entailment score between the source kernel and the transformed kernel drops below 1.00 (or below the 0.85 threshold), the law is falsified for that signal. If this happens reproducibly across multiple signals and multiple oracles, the law is falsified.

The inverse falsification (from the test's perspective): if commitment is conserved under *ungoverned* transformation — i.e., if removing governance does NOT produce decay — the governed/ungoverned asymmetry that is the law's empirical signature disappears, and the law loses its content. P-000 Proposition 6 (Second Law) predicts ΔH_C > 0 under ungoverned transformation; if ΔH_C = 0 under ungoverned transformation, the Second Law is falsified, and the First Law's content (conservation is specifically under *governed* transformation) is undermined.

**Honest assessment:** CT states the falsification condition explicitly (Proposition 5.3): failure to observe conservation under governed conditions with a reasonable oracle. The condition is specific and operational. The inverse (conservation without governance) would also falsify the asymmetry. This is well-addressed.

### Q4.2 — Is the falsification condition stated before the data is examined? (Pre-registration.)

**Partially.** The falsification condition (Proposition 5.3) is stated in P-000, which was written after the experimental data (EXP-001 through EXP-007) was collected. The experiments were conducted first; the formal prospectus stating the falsification condition was written afterward.

However, the structure of the experiments themselves provides a form of pre-registration:

1. **EXP-003 was designed with a fixed protocol:** 20 signals, 10 recursive iterations, Gate condition vs. baseline/compression conditions. The success criterion (NLI = 1.00) was defined by the oracle's output, not adjusted post-hoc. The 13/20 result was not cherry-picked — all 20 signals were tested and reported, including the 7 that did not achieve perfect conservation.

2. **The harness is public and pinned:** The oracle (microsoft/deberta-v3-base-mnli) and threshold (0.85) are specified. The GitHub repo (github.com/SunrisesIllNeverSee/commitment-conservation) contains the harness code. A researcher attempting falsification uses the same instrument, preventing post-hoc instrument adjustment.

3. **EXP-006 as pre-registration of a failure:** The paper recursion test (2/4 claims survived) was designed to test the law on its own claims. The result (2/4 failures) was reported honestly, not suppressed. This is evidence that the framework reports failures, not just successes.

4. **The standing invitation (Proposition 11.2):** "CT is offered as a falsifiable framework. Critics are invited to identify signals where governed transformation fails to conserve commitment, substitute stronger oracles, and design adversarial transformations." This is an open falsification invitation, not a closed claim.

**The honest concern:** The law was formulated after the data was collected. The conservation result was observed first; the formal claim of law-status came after. This is discovery, not pre-registered hypothesis testing. In particle physics, conservation laws are often discovered from data and then subjected to increasingly precise tests — the pre-registration standard applies to the *tests*, not the initial discovery. CT's initial discovery is post-hoc by nature. The falsification condition is stated for *future* tests, which is the relevant standard.

**Honest assessment:** The falsification condition is stated for future tests (anyone can attempt falsification with the public harness). The initial discovery was post-hoc (data first, law formulation second). This is normal for discovery but does not meet the strict pre-registration standard for the original claim. Future falsification attempts would meet the standard. Partial.

### Q4.3 — Has anyone attempted to falsify it? (Not confirm — falsify. Has someone designed an adversarial test specifically to break it?)

**Yes — CT's own experimental program includes adversarial falsification attempts.** No *external* falsification attempts are documented, but the internal program was designed to stress-test the law.

1. **EXP-004 (Adversarial signals):** Explicitly designed to construct signals that would break the conservation law. Result: identified the "escalation failure mode" — a way the law *does* fail under specific conditions. This is an adversarial test that found a failure mode, not just a confirmation.

2. **EXP-005 (Mechanism isolation):** Designed to isolate which components of the governance protocol are necessary for conservation (and which are not). Result: identified Step A / Step B co-bottlenecks — conditions under which conservation fails because specific governance steps are missing. This is a falsification-adjacent test: it identifies the boundary conditions where the law breaks.

3. **EXP-006 (Paper recursion test):** Designed to test whether the law's own claims survive self-referential recursion. Result: 2/4 paper claims did NOT survive. This is a direct falsification attempt on the law itself — and it partially succeeded. The law failed on 2/4 of its own claims under self-referential recursion. CT's response (Paper 5) is to classify this as "harness stress" rather than "law failure," arguing that self-referential recursion is a different task than external deontic content preservation. But the test was designed to falsify, and it found failures.

4. **EXP-007 (NP-negation probe):** Designed to test whether the oracle can be fooled by surface-level manipulations that preserve surface similarity while violating commitment. Result: the oracle was NOT fooled (NLI = 1.00 for 3/4 signals while Jaccard degraded). But this is an oracle-validation test, not a law-falsification test.

**External falsification:** No external party has yet attempted falsification. The harness is public, but the framework is new (Paper 0 published March 2026). The standing invitation (Proposition 11.2) is open but not yet taken up by independent researchers.

**Honest assessment:** CT has conducted internal adversarial tests (EXP-004, EXP-005, EXP-006) that were designed to break the law and found specific failure modes. EXP-006 is the strongest case — it found 2/4 failures in self-referential recursion. No external falsification attempts have been made yet. The internal attempts are genuine adversarial tests, not just confirmations, but they are conducted by the law's own author, which limits independence.

### Q4.4 — What is the difference between "the law failed" and "the instrument failed"?

**CT addresses this directly in Paper 5 but the distinction is articulated in principle, not yet fully operationalized.**

Paper 5 (Measurement Instrument) Section VI establishes explicit criteria:

- **Conservation Law failure:** C(T_gov(S)) ≠ C(S) for a signal S where the Six-Gate Protocol is correctly applied AND the oracle is functioning correctly. This means: governance was properly implemented, the oracle accurately measured the kernels, and the kernels genuinely differ. The law failed.

- **Harness stress (instrument failure):** C(T_gov(S)) ≠ C(S) where either:
  - (a) The oracle misclassifies the commitment kernel (oracle failure — the instrument is wrong), OR
  - (b) The signal's commitment structure is degenerate under self-reference (EXP-006 case — the signal itself is pathological, not the law)

The criterion for EXP-006 specifically: "EXP-006 is harness stress, not Law failure, because the 2/4 failures are in the self-referential category (b), not category (a). The paper must show this classification is principled, not post-hoc."

**The concern:** This distinction risks being post-hoc. If a measurement fails, CT classifies it as either "law failed" (if the oracle is working and the signal is normal) or "instrument failed" (if the oracle is broken or the signal is pathological). But the classification depends on independent verification of (a) oracle functioning and (b) signal normality — and CT does not yet have independent calibration standards for either.

In physics, the distinction is made via calibration: you test the detector against known standards before trusting its measurements. CT does not yet have a calibration standard (see Q3.5). Without a calibration standard, the distinction between "law failed" and "instrument failed" rests on argument rather than procedure.

Paper 5 acknowledges this: "The paper must show this classification is principled, not post-hoc." The principled criterion offered is: self-referential recursion (EXP-006) is a categorically different task from external deontic content preservation. A paper claiming conservation of *its own claims* under recursion is testing whether the claims are robust to self-reference, not whether the conservation law holds for external deontic content. This is a reasonable distinction but it is argument-based, not calibration-based.

**Honest assessment:** CT articulates the distinction (Paper 5) and offers a principled criterion (self-referential vs. external content). But the distinction is not yet operationalized via calibration standards. The risk of post-hoc classification is real and acknowledged. This is partial — the thinking is correct, the implementation is incomplete.

### Q4.5 — What class of signals does the law NOT apply to? (Every physical law has a scope.)

**Yes — CT explicitly states its scope boundary.**

P-000 Proposition 11.3 (Known Boundary Conditions): "Current empirical support is strongest for deontic signals. Applicability to other signal classes (narrative, poetic, ambiguous, self-referential) requires further investigation."

P-000 Proposition 1.7 (Signal Classes): "Signals may be classified by their deontic structure: deontic (obligations, prohibitions, permissions), descriptive (states of affairs), narrative (temporal sequences), and self-referential. CT's empirical support is strongest for deontic signals; applicability to other classes requires further investigation."

The scope boundary is: **the law is established for deontic signals** (signals carrying obligations, prohibitions, permissions, modal constraints). It is NOT established for:

- **Descriptive signals** (states of affairs — "the sky is blue"): no deontic content to conserve
- **Narrative signals** (temporal sequences — "she walked to the store, then bought milk"): no deontic kernel in the CT sense
- **Poetic/aesthetic signals**: meaning is not primarily deontic
- **Ambiguous signals**: multiple possible kernels, conservation is ill-defined
- **Self-referential signals** (EXP-006): the signal's content is about itself, creating a recursion pathology

CL-002's three-regime classification further refines the scope within deontic signals:
- **Modal-anchored** (highest conservation): kernel carried by modal operators
- **Relational-structural** (intermediate): kernel carried by relational predicates
- **Compression-boundary** (sharp threshold): kernel sensitive to representation length

The law's scope is deontic signals, with conservation strength varying by regime. Non-deontic signals are outside the current scope.

**Honest assessment:** This is well-addressed. CT explicitly states its scope boundary (Proposition 11.3), identifies the signal classes it does and does not cover (Proposition 1.7), and provides a within-scope refinement (CL-002's three regimes). The scope is honest and bounded. This is one of CT's strongest answers.

---

## Requirement 5: Empirical Asymmetry

### Q5.1 — What is the asymmetry? Under what conditions is the quantity conserved, and under what conditions is it NOT conserved?

**This is CT's core empirical claim and is stated with maximum clarity.**

The asymmetry is **governed vs. ungoverned transformation**:

- **Under governed transformation** (T_gov: transformation passing through the Six-Gate Protocol): C(T_gov(S)) = C(S). The commitment kernel is conserved. (First Law — P-000 Proposition 5)

- **Under ungoverned transformation** (T_ungov: transformation lacking the Six-Gate constraints): C(T_ungov(S)) < C(S) for n ≥ 1 iterations. The commitment kernel decays monotonically. ΔH_C > 0 per step. Cumulative entropy Ω(σ√n). (Second Law — P-000 Proposition 6)

The conditions are operationally distinguishable: a transformation is governed if it passes through G1 (compression to kernel), G2 (lineage verification), G3 (fidelity verification by independent oracle), G4 (recursion testing), G5 (blackhole consumption/metabolism), and G6 (custodial sovereignty). A transformation is ungoverned if it lacks these constraints — e.g., an LLM summarizing a statute with no fidelity verification, no lineage tracking, and no oracle check.

The asymmetry is not merely "sometimes conserved, sometimes not." It is structurally determined: governance (the presence of the Six-Gate constraints) is the condition for conservation; absence of governance is the condition for decay. This is analogous to the thermodynamic asymmetry: energy is conserved in an isolated system (First Law), entropy increases in an isolated system (Second Law). CT's analog: commitment is conserved under governance (First Law), semantic entropy increases without governance (Second Law).

**Honest assessment:** This is the strongest, most clearly articulated part of CT. The asymmetry is explicit, operationally defined, and structurally grounded. Full marks on clarity of the asymmetry statement.

### Q5.2 — Has the asymmetry been demonstrated empirically? (Not theorized — measured. Do you have data showing conservation under condition A and decay under condition B?)

**Yes.** EXP-003 is the primary demonstration.

**EXP-003 (corrected harness, 20 signals, 10 recursive iterations):**
- **Gate condition (governed):** 13/20 signals achieved NLI bidirectional entailment = 1.00 across all 10 recursive iterations. Conservation demonstrated under governance.
- **Baseline/Compression conditions (ungoverned):** NLI degraded measurably by iteration 5, sharply by iteration 10. Decay demonstrated without governance.

The same 20 signals were tested under both conditions, providing a direct within-subject comparison. The asymmetry is not between different signal sets — it is between different transformation conditions on the same signals.

Additional evidence:
- **EXP-007 (NP-negation probe):** Demonstrated that the asymmetry operates at the semantic level, not the surface level. Under transformation, Jaccard similarity degraded (surface change) while NLI = 1.00 for 3/4 signals (commitment preserved). This shows the conservation/decay asymmetry is about deontic content, not lexical form.
- **EXP-004 (adversarial signals):** Identified specific conditions (escalation failure mode) where governance fails to prevent decay — refining the boundary of the asymmetry.
- **EXP-005 (mechanism isolation):** Identified which governance steps are necessary for conservation (Step A / Step B co-bottlenecks) — characterizing the mechanism of the asymmetry.

**Scale of evidence:** 3,950 runs total across all experiments, 57 signals, 181 condition-signal configurations (from L-000 Preface and P-000 Proposition 5.2). EXP-003 specifically: 20 signals × 10 iterations × multiple conditions.

**Honest assessment:** The asymmetry has been demonstrated empirically. EXP-003 provides direct within-subject evidence: same signals, governed condition (13/20 conserved) vs. ungoverned condition (measurable decay by iteration 5, sharp decay by iteration 10). The evidence is pilot-scale (20 signals in EXP-003) but real and measured, not merely theorized. The asymmetry is demonstrated within limits (pilot scale, deontic signals only).

### Q5.3 — Is the asymmetry reproducible? (If someone else sets up condition A and condition B, do they get the same asymmetry?)

**The design supports reproducibility; external reproduction has not yet been documented.**

Reproducibility infrastructure:
1. **Public harness:** GitHub repo (github.com/SunrisesIllNeverSee/commitment-conservation) contains the measurement harness code.
2. **Pinned oracle:** microsoft/deberta-v3-base-mnli at threshold 0.85 — a specific, publicly available model. Anyone can download and run it.
3. **Public corpus:** Experimental record deposited at Zenodo (DOI: 10.5281/zenodo.19105225). The signals and configurations are available.
4. **Fixed protocol:** Six-Gate Protocol, 10 recursive iterations, NLI bidirectional entailment — the procedure is fully specified.

A researcher who downloads the harness, the corpus, and the oracle should be able to reproduce EXP-003's results: 13/20 signals at NLI = 1.00 under Gate condition, decay under baseline/compression.

**Has this been done?** Based on the available documents, no external reproduction has been documented. The framework is new (Paper 0 published March 2026, P-000 written April 2026). The standing invitation to falsify (Proposition 11.2) is open but not yet taken up.

Paper 4 (Cross-System Fidelity) is designed to test reproducibility across providers (GPT-4, Claude, Gemini, Llama) — but this is planned for Summer 2026 and has not been executed.

**Honest assessment:** The asymmetry is reproducible *in principle* (public harness, pinned oracle, deposited corpus, fixed protocol). External reproduction has not yet been documented. The infrastructure for reproducibility is strong; the empirical verification of reproducibility by independent parties is pending. This is "designed for reproducibility but not yet independently reproduced."

### Q5.4 — What is the effect size? (In physics, the asymmetry between conservation and violation is infinite — it NEVER happens. What is your asymmetry? 0.94 vs 0.42? What are the confidence intervals?)

**The effect size is large but not infinite. Conservation is not universal under governance — it holds for 65% of tested signals under the Gate condition.**

From EXP-003:
- **Governed condition (Gate):** 13/20 signals achieved NLI = 1.00 (perfect conservation) across 10 recursive iterations. Conservation rate: 65%.
- **Ungoverned condition (Baseline/Compression):** NLI degraded measurably by iteration 5, sharply by iteration 10. The exact conservation rate under ungoverned conditions is not stated as a single number in the documents, but the description ("degrades measurably by iteration 5, sharply by iteration 10") indicates substantial decay — likely well below 65% by iteration 10.

**The asymmetry in raw terms:** 65% conservation under governance vs. substantial decay without governance. The effect size is the difference in conservation rates between the two conditions. If ungoverned conservation at iteration 10 is, say, 20-30% (inferred from "sharp degradation"), the effect size would be approximately 35-45 percentage points.

**Confidence intervals:** For 13/20 (65%), the Wilson 95% confidence interval is approximately [43.2%, 82.9%]. This is a wide interval due to the small sample size (n=20). Paper 1's writing notes acknowledge: "Paper 1's entropy rate estimate is derived from EXP-003 (20 signals, 10 steps). For NeurIPS/ICML, this must be characterized explicitly as 'pilot-scale evidence.'" The expanded corpus plan (100+ signals, 20+ steps) would narrow this interval.

**Comparison to physics standard:** In physics, conservation laws hold with infinite precision — energy is *never* observed to be non-conserved in a closed system. CT's conservation holds for 65% of signals under governance, not 100%. This is a fundamental difference: CT's law is probabilistic, not absolute. The 7/20 signals that did not achieve NLI = 1.00 under governance represent either (a) law failures (governance was insufficient for those signals), (b) instrument failures (the oracle misclassified), or (c) signal-specific factors (the signal's commitment structure was too complex for the governance protocol to preserve). Paper 0's writing notes address this: "The other 7: report what happened. This is not a weakness to hide — it is the harness's calibration data."

**The Second Law effect size:** The decay rate under ungoverned transformation is characterized as Ω(σ√n) cumulative entropy, where σ² is per-step drift variance. The specific value of σ² is not stated in the documents — it would be estimated from EXP-003's degradation curves, which is Paper 1's contribution. Paper 1 is "Data exists; drafting" — the formal decay rate has not been published.

**Honest assessment:** The effect size is large (65% vs. substantial decay) but not infinite. The confidence interval is wide ([43.2%, 82.9%] for the governed condition) due to small sample size. The law is probabilistic, not absolute — 7/20 signals did not achieve perfect conservation under governance. The formal decay rate (σ²) is not yet published. This is real evidence with a real effect size, but it does not meet the physics standard of infinite asymmetry. It meets the standard of a measurable, large effect with stated (if wide) confidence intervals.

### Q5.5 — Does the asymmetry make a novel prediction? (A law that only explains what you've already observed is retrospective. Does your law predict something you haven't tested yet?)

**Yes — CT makes several novel predictions that have not yet been tested.**

1. **Governance density threshold (Paper 3):** There exists a sparsity bound ρ* such that conservation holds for ρ_g ≥ ρ* and fails for ρ_g < ρ*, regardless of constraint type. This predicts that governance can be *reduced* below the full Six-Gate Protocol while maintaining conservation, down to a minimum threshold — and that below that threshold, conservation fails regardless of what constraints remain. This has not been tested (Paper 3 is BLOCKED, "new experiments required — vary gate count").

2. **Cross-provider conservation (Paper 4):** Under governance, conservation rates should be statistically indistinguishable across AI providers (GPT-4, Claude, Gemini, Llama) and architectures. This predicts that the law is substrate-agnostic — the model performing the transformation doesn't matter, only the governance protocol does. This has not been tested (Paper 4 is "Planned — Summer 2026").

3. **Compression-Fidelity Bound (Paper 2):** There exists a minimum representation length below which commitment loss is inevitable, regardless of governance. This predicts a sharp threshold: above the bound, conservation is achievable; below it, conservation is impossible. EXP-003 and EXP-007 show signals that collapse at a threshold, but the formal bound has not been derived or systematically tested (Paper 2 is BLOCKED).

4. **Threshold regime in decay (Paper 1):** Commitment decay under ungoverned transformation follows a threshold model — stability in early iterations followed by rapid collapse — rather than smooth linear or exponential degradation. This predicts that a system may appear to preserve meaning for many iterations while silently approaching a collapse point. Paper 1 has data (EXP-003) but the formal model has not been published.

5. **Regime-specific governance (CL-002):** Different signal regimes (modal-anchored, relational-structural, compression-boundary) require different governance strategies. This predicts that uniform governance is suboptimal — targeting modal operators for modal-anchored signals, relational predicates for relational-structural signals, and length thresholds for compression-boundary signals will outperform uniform governance. This has not been tested.

6. **Semantic channel capacity (CAP-001):** There is a maximum rate at which commitment can be preserved through a governed transformation channel, as a function of governance density, semantic entropy rate, and kernel complexity. This predicts a capacity limit analogous to Shannon's channel capacity — you cannot transmit commitment faster than C_s regardless of governance. This is long-term and untested.

**Honest assessment:** CT makes multiple novel, untested predictions. The governance density threshold (Paper 3), cross-provider conservation (Paper 4), and compression-fidelity bound (Paper 2) are the most immediately testable. The threshold decay regime (Paper 1) has preliminary data but no formal model. These are genuine novel predictions — they predict phenomena that have not been observed, derived from the law's structure. This is a strong answer: the law is not merely retrospective.

---

## Scoring Summary (Self-Assessment)

| Requirement | Max | Self-Score | Assessment |
|-------------|-----|------------|------------|
| 1. Defined conserved quantity | 12 | 7 | Components defined and theory-independent; no units/dimension; minimal case identified |
| 2. Symmetry / invariance principle | 12 | 5 | Invariance identified; no Noether symmetry; no Lagrangian; symmetry-breaking well-addressed |
| 3. Independent measurement | 15 | 8 | Instrument named; partial independence argued; cross-oracle replication not done; no formal uncertainty; partial calibration |
| 4. Falsifiability | 15 | 11 | Falsification condition explicit; internal adversarial tests conducted; law/instrument distinction articulated; scope boundary explicit |
| 5. Empirical asymmetry | 15 | 11 | Asymmetry clear and demonstrated; reproducible in principle; effect size measured (wide CI); novel predictions made |
| **Total** | **69** | **42** | **Promising — empirical foundation exists but gaps remain** |

### Self-score breakdown by question:

| Question | Self-Score (0-3) | Rationale |
|----------|------------------|-----------|
| Q1.1 | 3 | Conserved quantity defined without using "commitment" or measurement tools |
| Q1.2 | 1 | No units specified; information-theoretic formalization is planned but not done |
| Q1.3 | 2 | Components theory-independent; framing as "law" is CT-specific; partial |
| Q1.4 | 1 | Minimal case identified ("shall not") but not formally proven minimal |
| Q2.1 | 2 | Invariance under governed transformation identified; not a Noether symmetry |
| Q2.2 | 0 | Not addressed; continuous vs. discrete unresolved |
| Q2.3 | 0 | No Lagrangian equivalent; fundamental gap |
| Q2.4 | 3 | Conservation fails when symmetry (governance) broken; well-documented |
| Q3.1 | 3 | Instrument named (NLI harness + DeBERTa + SIGSYSTEM) |
| Q3.2 | 2 | Architectural/functional independence argued; same substrate class; partial |
| Q3.3 | 1 | Design permits substitution; cross-oracle replication not done |
| Q3.4 | 1 | No formal uncertainty; Wilson CI computable from data; GUM framework proposed |
| Q3.5 | 1 | Failure modes identified (EXP-006, EXP-007); no formal calibration protocol |
| Q4.1 | 3 | Falsification condition explicit and specific (Proposition 5.3) |
| Q4.2 | 2 | Falsification condition stated for future tests; initial discovery post-hoc |
| Q4.3 | 2 | Internal adversarial tests conducted (EXP-004/5/6); no external attempts |
| Q4.4 | 2 | Distinction articulated (Paper 5); not operationalized via calibration |
| Q4.5 | 3 | Scope boundary explicit (Proposition 11.3); signal classes enumerated |
| Q5.1 | 3 | Asymmetry explicit and operationally defined |
| Q5.2 | 2 | Demonstrated empirically (EXP-003); pilot-scale (20 signals) |
| Q5.3 | 1 | Reproducible in principle; not yet independently reproduced |
| Q5.4 | 2 | Effect size measured (65% vs. decay); wide CI; not infinite |
| Q5.5 | 3 | Multiple novel untested predictions (Papers 2, 3, 4, CAP-001) |

**Recount: 3+1+2+1 + 2+0+0+3 + 3+2+1+1+1 + 3+2+2+2+3 + 3+2+1+2+3 = 7 + 5 + 8 + 12 + 11 = 43**

Wait, let me recount carefully:

- Req 1: Q1.1=3, Q1.2=1, Q1.3=2, Q1.4=1 → 7
- Req 2: Q2.1=2, Q2.2=0, Q2.3=0, Q2.4=3 → 5
- Req 3: Q3.1=3, Q3.2=2, Q3.3=1, Q3.4=1, Q3.5=1 → 8
- Req 4: Q4.1=3, Q4.2=2, Q4.3=2, Q4.4=2, Q4.5=3 → 12
- Req 5: Q5.1=3, Q5.2=2, Q5.3=1, Q5.4=2, Q5.5=3 → 11

**Total: 7 + 5 + 8 + 12 + 11 = 43**

| Requirement | Max | Self-Score | Assessment |
|-------------|-----|------------|------------|
| 1. Defined conserved quantity | 12 | 7 | Components defined, theory-independent; no units; minimal case identified |
| 2. Symmetry / invariance principle | 12 | 5 | Invariance identified; no Noether symmetry; no Lagrangian; symmetry-breaking strong |
| 3. Independent measurement | 15 | 8 | Instrument named; partial independence; no cross-oracle replication; no formal uncertainty |
| 4. Falsifiability | 15 | 12 | Falsification explicit; adversarial tests done; scope boundary explicit; law/instrument distinction partial |
| 5. Empirical asymmetry | 15 | 11 | Asymmetry clear and demonstrated; pilot-scale; novel predictions; not yet reproduced |
| **Total** | **69** | **43** | **Promising — empirical foundation exists but gaps remain** |

---

## Where CT Scores Highest

**Requirement 4 (Falsifiability): 12/15** — CT's strongest area. The falsification condition is explicit (Proposition 5.3), the scope boundary is stated (Proposition 11.3), internal adversarial tests were conducted (EXP-004/5/6), and the law/instrument distinction is articulated (Paper 5). The main gap is pre-registration (the law was formulated after the data) and the lack of external falsification attempts.

**Requirement 5 (Empirical Asymmetry): 11/15** — CT's second strongest area. The governed/ungoverned asymmetry is the core empirical claim, demonstrated in EXP-003, and generates multiple novel predictions. The main gaps are pilot-scale evidence (20 signals), wide confidence intervals, no external reproduction, and the law being probabilistic (65%, not 100%) rather than absolute.

## Where the Gaps Are

**Requirement 2 (Symmetry/Invariance): 5/12** — CT's weakest area. CT has an invariance (C(S) is invariant under governed transformation) but:
- No Noether-type continuous symmetry that *generates* the conservation
- No Lagrangian or variational principle
- The continuous/discrete question is unresolved
- The invariance is defined operationally (Six-Gate Protocol) and observed empirically, not derived from a symmetry principle

This is the fundamental gap: CT has a conservation *observation* (the quantity doesn't change under certain conditions) but not a conservation *law* in the Noether sense (the quantity doesn't change *because* a symmetry forces it not to). The conservation is enforced by a protocol (the Six-Gate), not generated by a symmetry of nature. A critic could argue this makes CT's "law" an engineering guarantee, not a physical law — the conservation holds because the gates are designed to make it hold, not because a symmetry of the system forces it.

**Requirement 1 (Defined conserved quantity): 7/12** — The conserved quantity is defined and its components are theory-independent, but it lacks units/dimension (the information-theoretic formalization is a blocking gap in Paper 2), and the minimal case is identified but not formally proven minimal.

**Requirement 3 (Independent measurement): 8/15** — The instrument is named and partial independence is argued, but: cross-oracle replication has not been done, no formal measurement uncertainty is stated, and no calibration protocol is implemented. The oracle is the same substrate class (language model) as the systems being measured.

---

## Post-Answer Reflection

### Which questions were easiest to answer from CT's existing material?

- **Q1.1 (what is conserved):** Immediately answerable from P-000 Proposition 1.3. The deontic kernel definition is crisp and well-articulated.
- **Q2.4 (does conservation fail when symmetry breaks):** This is CT's core claim — the governed/ungoverned asymmetry. EXP-003 provides direct evidence. The Second Law formalizes the failure.
- **Q4.1 (falsification condition):** P-000 Proposition 5.3 states it explicitly. The public harness makes it operational.
- **Q4.5 (scope boundary):** P-000 Proposition 11.3 states it explicitly. The signal class enumeration (Proposition 1.7) and CL-002's regime classification provide depth.
- **Q5.1 (the asymmetry):** The governed/ungoverned distinction is the framework's spine. Stated everywhere, clearly and consistently.
- **Q5.5 (novel predictions):** Papers 2, 3, 4, and CAP-001 are essentially untested predictions. The research program is forward-looking.

### Which questions exposed gaps in CT's current formulation?

- **Q1.2 (units/dimension):** CT has no units for C(S). The information-theoretic formalization (Paper 2's blocking gap) is the path to units, but it is unresolved. This is a fundamental gap — a conserved quantity without units is an operational concept, not a physical quantity.
- **Q2.2 (continuous vs. discrete symmetry):** Not addressed anywhere in CT. The Six-Gate Protocol suggests discrete; governance density suggests continuous. Unresolved.
- **Q2.3 (Lagrangian equivalent):** CT has no variational principle. The conservation is stated as an empirical regularity and enforced by a protocol, not derived from a Lagrangian. This is the deepest gap — without a Lagrangian, CT cannot claim Noether-type law status. The channel capacity work (CAP-001) might eventually provide a variational structure, but it is long-term and blocked.
- **Q3.3 (cross-oracle replication):** The design permits it, but it hasn't been done. The framework is new, but this is a critical gap for establishing independence.
- **Q3.4 (measurement uncertainty):** No formal uncertainty analysis. Paper 5 proposes GUM but hasn't implemented it. The 13/20 result has a wide Wilson CI that CT has not reported.
- **Q3.5 (calibration standards):** No formal calibration protocol. The law/instrument distinction (Paper 5) is articulated in principle but not operationalized.
- **Q5.4 (effect size):** The 65% conservation rate is real but wide-CI and pilot-scale. The law is probabilistic, not absolute — a fundamental difference from physics conservation laws.

### Where did I have to stretch CT's claims to fit the physics criteria?

- **Q2.1 (the symmetry):** I characterized the governed transformation class as a "symmetry group" and C(S) as the "conserved current," drawing the Noether analogy. CT does not use this framing. The invariance is real, but calling it a "symmetry" in the Noether sense is my interpretation, not CT's claim. CT calls it a "conservation law" and an "empirical regularity," not a symmetry-derived conservation.
- **Q1.3 (theory-independence):** I argued that the deontic components are theory-independent (deontic logic) while the law-status claim is CT-specific. This is a reasonable distinction but stretches the "theory-independent" criterion — the *question* "does the deontic content survive transformation?" is theory-independent, but the *answer* "yes, and this constitutes a conservation law" is CT's.
- **Q3.2 (instrument independence):** I argued for architectural and functional independence while acknowledging the same-substrate-class concern. CT's argument for independence is real but not as strong as the physics standard (a balance measuring mass is ontologically distinct from mass; an NLI model measuring language is not ontologically distinct from language).
- **Q4.2 (pre-registration):** I argued that the public harness and pinned oracle provide a form of pre-registration for *future* tests, even though the initial discovery was post-hoc. This is a reasonable standard for discovery but stretches the strict pre-registration criterion.

---

*End of solo run. CT held as true. Gaps reported honestly.*
