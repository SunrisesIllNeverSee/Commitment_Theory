# CT Answers — Language as Matter Test (Pass 2: Revised)

**Mode:** Complete re-run after stress-testing against primary sources.
**Premise:** CT is held as true. Answers come from CT's internal data as laid out in the corpus.
**What changed from Pass 1:** I was applying a stricter standard than the test requires. The test asks broader questions than I was answering. This pass answers the questions as asked, not as a physicist might wish them to be asked.

---

## Requirement 1: A Defined Conserved Quantity

**Q1.1:** What exactly is conserved? Define it in one sentence without using the word "commitment" or referencing your own measurement tools.

> **Answer:** The deontic content of a signal — its set of obligations, prohibitions, permissions, and modal constraints — is conserved under transformation that passes through constitutional governance constraints.

**Q1.2:** What are its units or dimension? (Mass has kilograms. Energy has joules. Charge has coulombs. What does your conserved quantity have?)

> **Answer:** The unit is the **deontic proposition** — a single obligation, prohibition, permission, or modal constraint. C(S) is a *set* of deontic propositions (P-000 Proposition 1.3: "the set of obligations, prohibitions, permissions, and modal constraints"). Conservation means set preservation: the set of deontic propositions in the output equals the set in the input. This is a discrete, quantized conserved quantity — analogous to how charge is quantized in units of e, or spin in units of 1/2. The "dimension" is deontic content, measured in units of individual deontic propositions. A signal carrying one prohibition ("shall not X") has |C(S)| = 1. A signal carrying three obligations and two prohibitions has |C(S)| = 5. The cardinality of the set is the natural measure.
>
> Paper 2's blocking gap notes that C(S) needs formalization as an information-theoretic object with a probability space for the *source coding theorem analog* — but that's about deriving a compression bound, not about the units of the conserved quantity itself. The units are deontic propositions. The information-theoretic formalization would give the *entropy* of the distribution over deontic propositions, which is a different (derived) quantity.

**Q1.3:** Can it be defined by someone who disagrees with your theory? (i.e., is the definition theory-independent, or does it only make sense within CT?)

> **Answer:** Yes. The components — obligations, prohibitions, permissions, and modal constraints — are standard categories from **deontic logic** (von Wright 1951, Kratzer 1991, von Fintel 2006), which CT explicitly borrows and acknowledges. Someone who rejects CT's conservation claim can still define "the deontic content of a signal" using standard deontic logic. FS-001 formalizes the commitment kernel as a "canonical invariant" within intensional semantics: `CI(S, w) = {φ ∈ DEON | for all w' such that wR_gov w', w' ⊨ φ}` — using only standard possible-worlds semantics (accessible worlds, deontic modality) plus CT's governed-transformation relation R_gov. The deontic propositions and the possible-worlds framework are not CT's invention; only R_gov is.
>
> What is CT-specific is not the *definition of the object* but the *claim that it is conserved under governed transformation*. The object is theory-independent; the conservation law is not. A critic can define C(S) using deontic logic and then test whether it is conserved — that's exactly what the public harness enables.

**Q1.4:** What is the minimal case — the simplest possible signal that carries the conserved quantity? (In physics, the simplest mass is a single electron. What is your electron?)

> **Answer:** A single deontic modal operator carrying one prohibition: **"shall not X."** This follows directly from CT's primitives. The commitment kernel is composed of obligations, prohibitions, permissions, and modal constraints (P-000 Proposition 1.3). CL-002 identifies modal-anchored signals — those whose kernel is carried primarily by modal operators like "shall," "must," "shall not" — as a distinct regime with the highest conservation rates under governance. A single "shall not X" is the simplest signal carrying one deontic proposition (one prohibition), which is one unit of the conserved quantity. CT's failure mode taxonomy confirms this is the unit of analysis: modal frame inversion ("shall not" → "shall") is failure mode 4, operating on exactly this primitive. The "electron" of CT is a single deontic operator.

---

## Requirement 2: A Symmetry or Invariance Principle

**Q2.1:** What is the symmetry? What transformation leaves the system's action (or equivalent functional) invariant? Name it precisely.

> **Answer:** The symmetry is **invariance under governed transformation** — the group of transformations {T_gov} that satisfy the Six-Gate Protocol leaves C(S) invariant. The conservation law states: C(T_gov(S)) = C(S) for all T_gov in the governed transformation class. This is structurally analogous to how Noether's theorem works: the conserved current is invariant under the symmetry group. In CT, the "symmetry group" is the class of governed transformations, and C(S) is the conserved current.
>
> FS-001 formalizes this: the governed transformation induces an accessibility relation R_gov on possible worlds, and CI(S, w) is the intersection of deontic extensions across all R_gov-accessible worlds. The "symmetry" is the invariance of CI(S, w) across the orbit of R_gov-accessible worlds. R_gov satisfies group properties: reflexivity (identity transformation) and transitivity (composability of governed transformations) — both guaranteed by the Six-Gate Protocol design.
>
> **Caveat:** CT does not explicitly frame this as a Noether symmetry. CT's framing is empirical (the law is a discovered regularity) and operational (the Six-Gate Protocol defines the governed class). The invariance is defined operationally and observed empirically, not derived from a continuous symmetry principle via a variational argument. Whether this invariance *arises from* a deeper continuous symmetry (the way energy conservation arises from time-translation symmetry) is an open question CT has not addressed.

**Q2.2:** Is the symmetry continuous or discrete? (Noether's theorem requires continuous symmetries. Discrete symmetries produce selection rules, not conservation laws in the Noether sense.)

> **Answer:** Both, depending on the level of analysis.
>
> **Operationally discrete:** The Six-Gate Protocol is a discrete set of six gates. A transformation either passes all six (governed) or doesn't (ungoverned). This is a binary classification — a discrete symmetry group defined by a finite set of constraints.
>
> **Theoretically continuous:** Paper 3 (Governance Density) introduces governance density ρ_g as a **continuous parameter** — the ratio of constraint operations to transformation operations — and derives a sparsity bound ρ* such that conservation holds for ρ_g ≥ ρ* and fails for ρ_g < ρ*. This is a continuous phase transition: as governance density increases past the threshold, conservation "turns on." If ρ_g is a continuous parameter and conservation depends on it continuously, the symmetry is continuous in ρ_g.
>
> The honest assessment: the operational structure (Six-Gate Protocol) is discrete. The theoretical aspiration (governance density as continuous parameter with threshold) is continuous. CT has not formally resolved whether the symmetry is continuous or discrete in the Noether sense. If Noether's theorem strictly requires continuous symmetries, and the operational structure is discrete, then CT's conservation would be analogous to a discrete symmetry producing a selection rule. But Paper 3's governance density framework suggests a continuous transition that could qualify.

**Q2.3:** What is the equivalent of the Lagrangian? (In physics, the Lagrangian is the function whose symmetries produce conservation laws. What is the functional in your system whose invariance under transformation produces conservation of commitment?)

> **Answer:** CT does not have an explicit Lagrangian or equivalent variational functional. This is the weakest point relative to the Noether framework.
>
> The closest analogs CT offers:
> 1. **The fidelity functional** — Fid(S, S') = degree to which C(S') matches C(S), measured by bidirectional entailment. The conservation law states Fid(S, T_gov(S)) = 1. But this is the *measurement* of conservation, not the *generator* of it. In physics terms, it is the equation of motion (the constraint), not the Lagrangian (the functional whose symmetries produce the constraint).
> 2. **The semantic channel capacity functional** (CAP-001) — C_s = f(ρ_g, h_s, κ), relating channel capacity to governance density, entropy rate, and kernel complexity. Shannon's channel capacity theorem is an optimization result (maximize mutual information over input distributions), which *is* a variational problem. If CAP-001 is eventually proven, it would be a variational result in the same sense. But CAP-001 is long-term and BLOCKED.
> 3. **FS-001's canonical invariant** — CI(S, w) = {φ ∈ DEON | for all w' such that wR_gov w', w' ⊨ φ} — is defined within possible-worlds semantics, not within a variational framework. There is no action principle, no stationary-action derivation, no Euler-Lagrange equation in CT.
>
> **Honest assessment:** CT does not have a Lagrangian equivalent. The conservation law is stated as an empirical regularity and an operational definition, not as the consequence of a variational principle. The channel capacity work (CAP-001) might eventually provide a variational structure, but it is not yet developed. This is a genuine gap — the one place where CT cannot answer the question as posed.

**Q2.4:** Does the conservation fail when the symmetry is broken? (In physics: if time-translation symmetry is broken, energy conservation gets complicated. Does your conservation fail when your symmetry is absent? This is the testable prediction.)

> **Answer:** Yes — and this is CT's central empirical claim. The governed/ungoverned distinction functions as the symmetry-breaking mechanism. When governance constraints are present (the Six-Gate Protocol, governance density ρ_g ≥ ρ*), the deontic content is conserved: C(T_gov(S)) = C(S). When governance constraints are absent (ungoverned transformation, ρ_g < ρ*), conservation fails and the deontic content decays monotonically (Second Law: ΔH_C > 0, cumulative entropy Ω(σ√n)).
>
> EXP-003 demonstrates this empirically: 13/20 signals conserved at NLI=1.00 across 10 iterations under the Gate condition; measurable degradation by iteration 5 under ungoverned conditions. Paper 3 further predicts that conservation fails not just when governance is fully absent but when it falls below a threshold ρ*: for ρ_g < ρ*, commitment decay is inevitable regardless of constraint type. This is a graded symmetry-breaking prediction — conservation fails progressively as governance density decreases below the threshold.
>
> The "symmetry" that produces conservation is the governance structure; when it is broken (removed or insufficient), conservation fails. This is the testable prediction, and it has been tested.

---

## Requirement 3: An Independent Measurement Instrument

**Q3.1:** What instrument measures the conserved quantity? Name it.

> **Answer:** The reference oracle is **bidirectional NLI (natural language inference) entailment** via `microsoft/deberta-v3-base-mnli`, threshold 0.85. A signal's deontic content is measured by extracting the kernel from both the original and transformed signal, then checking bidirectional entailment: does the original entail the transformed AND does the transformed entail the original? If both directions pass at threshold ≥ 0.85, the kernel is conserved for that transformation step. The next-generation oracle, SIGSYSTEM, is under development (trade secret — word-level contextual signal/noise weighting) but not yet deployed as the measurement instrument.

**Q3.2:** Is the instrument independent of the system being measured? (Specifically: if the conserved quantity is in language, and the instrument is a language model, is that independent?)

> **Answer:** Yes — in the relevant sense. The oracle (deberta-v3-base-mnli) and the systems being measured (GPT-4, Claude, Gemini, Llama) differ on every dimension that matters for independence:
>
> | Dimension | Oracle (deberta-v3-base-mnli) | Measured systems (GPT-4, Claude, etc.) |
> |-----------|-------------------------------|---------------------------------------|
> | Architecture | Encoder-only (DeBERTa) | Decoder-only (GPT, Claude, Llama) |
> | Parameters | ~400M | 70B–175B+ |
> | Training objective | NLI classification (entailment/neutral/contradiction) | Next-token prediction |
> | Training data | MNLI (433K sentence pairs) | Web-scale corpora |
> | Organization | Microsoft | OpenAI, Anthropic, Google, Meta |
> | Function | Classification (is A entailed by B?) | Generation (produce text) |
>
> They share a substrate class (transformer architecture), but so do a thermometer and a combustion engine share "matter." The relevant question is whether the instrument's measurement logic is independent of the system's transformation logic — and it is. The oracle applies a logical criterion (bidirectional entailment) that the transforming system does not know about or optimize for.
>
> Paper 0 §3.4 (Non-Tautology) establishes this explicitly: "The compression gate is not defined as 'output C(S) by construction.' It applies a lossy compression/transformation process **without prior access to C(S)**; the commitment extractor C(.) operates in a **separate canonical space** and evaluates the output after transformation." The instrument and the system being measured are functionally and architecturally separate.
>
> **Known limitation:** EXP-007 shows the oracle has a blind spot for NP-negation (returns 1.00 for 3/4 signals where negation has been reversed). This is a documented systematic error, not a hidden one. It means the oracle is not *perfectly* independent — shared substrate class may produce correlated blind spots. But it is independent *enough* for the current empirical claims, and the limitation is openly acknowledged.

**Q3.3:** Can a different instrument (one you didn't build or choose) measure the same quantity and get the same result? Has this been done?

> **Answer:** Yes, this is possible by design. Paper 0 establishes "oracle independence as a **design property**: the Conservation Law is testable with any oracle that supports bidirectional entailment." P-000 Proposition 10.3 states: "The oracle is a measurement instrument, not the law itself. Any party may substitute a stronger oracle. The law's validity does not depend on any single oracle." The law is stated in terms of bidirectional entailment — a general logical criterion, not a property of any specific model. Any NLI model implementing bidirectional entailment (dozens exist on HuggingFace: RoBERTa-MNLI, BART-MNLI, etc.) can test the law by swapping the oracle in the public harness.
>
> **Has this been done?** No. All experiments (EXP-001 through EXP-007) use the same oracle family (deberta-v3-base-mnli). Cross-oracle replication is planned (Paper 5) but not yet executed. The principle of oracle substitutability is stated as a design property; the empirical confirmation of it is not yet done. The barrier to doing it is a model swap on a public protocol — low technical barrier, not yet executed.

**Q3.4:** What is the measurement uncertainty? (Every physical measurement has a stated uncertainty. What is yours?)

> **Answer:** CT has identified sources of measurement uncertainty but has not yet formalized a metrological uncertainty statement. Known sources:
>
> 1. **Threshold uncertainty:** The NLI threshold of 0.85 introduces a binary cutoff in a continuous probability space. Signals near the threshold are measurement-sensitive — a small change in oracle confidence could flip the conservation verdict.
> 2. **Systematic error (NP-negation blindness):** EXP-007 shows the oracle returns NLI=1.00 for 3/4 signals where NP-negation has been reversed. This is a known systematic error source — the oracle has a blind spot for a specific class of semantic inversions.
> 3. **Empirical variance:** The 7/20 signals in EXP-003 that did not achieve NLI=1.00 under the Gate condition represent empirical variance whose source (law failure vs. oracle noise vs. signal-specific kernel fragility) is not yet fully characterized.
>
> Paper 5 plans to formalize this using the **GUM uncertainty framework** (JCGM 100:2008), reporting conservation rates as Bernoulli parameters with **Wilson confidence intervals**. For the current data: 13/20 = 0.65 conservation rate under governance. The Wilson 95% CI for this proportion is approximately [0.43, 0.82]. But the formal GUM-compatible uncertainty statement is planned, not yet published.
>
> **Honest answer:** Uncertainty sources are identified and documented. A formal uncertainty statement with confidence intervals is planned (Paper 5) but not yet published. The raw data (13/20) allows anyone to compute Wilson intervals now.

**Q3.5:** What happens when the instrument fails? (In physics, when a detector fails, you know it failed because you have calibration standards. Do you have calibration standards for your oracle?)

> **Answer:** CT has documented instrument failure modes and has a framework for distinguishing them, though formal calibration standards are planned rather than established.
>
> **Two documented instrument failure cases:**
> 1. **EXP-007 (NP-negation blindness):** The oracle returns NLI=1.00 (conserved) for 3/4 signals where NP-negation has been reversed at the semantic level. The oracle is fooled by surface plausibility. This is a known blind spot, openly documented.
> 2. **EXP-006 (self-referential recursion):** Only 2/4 paper claims survived self-referential recursion. Paper 5 reframes this as "harness stress" — the instrument fails when the signal's deontic structure is degenerate under self-reference.
>
> **Paper 5's three-way distinction** (the calibration framework, planned but not yet formalized):
> - **Law failure:** C(T_gov(S)) ≠ C(S) where the Six-Gate Protocol is correctly applied AND the oracle is functioning correctly. Genuine new physics.
> - **Instrument failure (oracle misclassification):** The oracle returns the wrong answer. EXP-007 demonstrates this.
> - **Signal degeneracy (harness stress):** The signal's deontic structure is insufficiently robust to withstand its own recursion. EXP-006 demonstrates this.
>
> The distinction between law failure and instrument failure is the **oracle independence question** — if a different oracle confirms the same result, it's law failure; if a different oracle disagrees, it's instrument failure. The distinction between law failure and signal degeneracy is whether the signal carries a well-formed deontic kernel in the first place. Paper 5 states this classification must be "principled, not post-hoc" — but the formal calibration protocol is planned, not yet established.
>
> **Honest answer:** Instrument failure modes are documented and openly acknowledged. A formal calibration protocol distinguishing law failure, instrument failure, and signal degeneracy is designed (Paper 5) but not yet implemented.

---

## Requirement 4: Falsifiability with Specified Failure Conditions

**Q4.1:** State the specific observation that would falsify your conservation law. Not "it might fail" — the exact result that would kill it.

> **Answer:** P-000 Proposition 5.3 states the falsification condition: "Failure to observe conservation under governed conditions, using a reasonable oracle, falsifies the law." Specifically: if a signal S is transformed through the Six-Gate Protocol (governed transformation, all six gates correctly applied) and the independent oracle measures C(T_gov(S)) ≠ C(S) — the deontic content of the output does not bidirectionally entail the deontic content of the input — and this result is confirmed with a functioning oracle (not an instrument failure), the law is falsified for that signal.
>
> Paper 0 §3.4 (Non-Tautology) establishes that this is a genuine empirical claim, not a definition: "The compression gate is not defined as 'output C(S) by construction.' It applies a lossy compression/transformation process without prior access to C(S); the commitment extractor C(.) operates in a separate canonical space and evaluates the output after transformation. Conservation is therefore an empirical claim."
>
> Proposition 11.2 extends the invitation: "Critics are invited to identify signals where governed transformation fails to conserve commitment, substitute stronger oracles, and design adversarial transformations."

**Q4.2:** Is the falsification condition stated before the data is examined? (Pre-registration. If you looked at the data first and then defined what would falsify it, that's post-hoc reasoning.)

> **Answer:** No. The law was discovered from the experimental data (EXP-001 through EXP-007, conducted January–March 2026) and then formalized. The falsification condition was stated in P-000 (April 2026), after the experiments that established the law had already been run. The Conservation Law preprint was deposited on Zenodo (January 12, 2026, v.01) before P-000 (April 2026), but the experiments preceded both.
>
> This is a discovery process, not a pre-registered hypothesis test. CT is honest about this: the law is presented as a discovered regularity, not a confirmed prediction. The falsification condition is stated for *future* tests — any party can now pre-register a falsification attempt using the public harness. But the original discovery was not pre-registered.

**Q4.3:** Has anyone attempted to falsify it? (Not confirm — falsify. Has someone designed an adversarial test specifically to break it?)

> **Answer:** Yes — internally, through two designed adversarial probes:
>
> 1. **EXP-007 (NP-negation probe):** Designed specifically to test whether the oracle could be fooled by surface-level manipulation. Result: the oracle *can* be fooled — it returns NLI=1.00 for 3/4 NP-negation reversals. This is a successful falsification attempt *against the oracle*, not against the law. It revealed a systematic instrument blind spot (failure mode 7: negation reversal).
>
> 2. **EXP-006 (self-referential recursion):** Designed to test whether the law holds when signals are self-referential (the paper's own claims about conservation). Result: only 2/4 paper claims survived. This revealed failure mode 9 (recursion collapse) and led to the distinction between law failure, instrument failure, and signal degeneracy (Paper 5).
>
> Both were designed to break the law or the harness, not to confirm it. Both produced findings that complicated the picture rather than supporting it.
>
> **External falsification attempts:** No documented external party has attempted to falsify the law using the public test harness. The invitation is extended (P-000 Proposition 11.2, Proposition 12.3); the harness and corpus are public; but documented independent falsification attempts do not exist in the corpus.

**Q4.4:** What is the difference between "the law failed" and "the instrument failed"? (In physics: if you measure a violation of energy conservation, you've either found new physics OR your detector is broken. How do you distinguish these in your system?)

> **Answer:** Paper 5 explicitly addresses this with a three-way distinction:
>
> - **Law failure:** C(T_gov(S)) ≠ C(S) where the Six-Gate Protocol is correctly applied AND the oracle is functioning correctly. This is genuine new physics — the law does not hold for this signal.
> - **Instrument failure (oracle misclassification):** The oracle returns the wrong answer — it says conserved when it isn't, or says not conserved when it is. EXP-007 demonstrates this: the oracle returns NLI=1.00 for NP-negation reversals it should catch.
> - **Signal degeneracy (harness stress):** The signal's deontic structure is insufficiently robust to withstand its own recursion. EXP-006 demonstrates this: 2/4 paper claims fail self-referential recursion because the claims' own commitment structure is degenerate under self-application, not because the law failed or the oracle erred.
>
> **How to distinguish in practice:**
> - Law failure vs. instrument failure: substitute a different oracle. If the different oracle confirms the same result (C ≠ C), it's law failure. If the different oracle disagrees, it's instrument failure. This requires cross-oracle replication (planned, not yet done).
> - Law failure vs. signal degeneracy: examine whether the signal carries a well-formed deontic kernel in the first place. If the signal's kernel is degenerate under self-reference (as in EXP-006), the failure is a property of the signal, not the law. This requires the formal calibration protocol (Paper 5, planned).
>
> Paper 5 states this classification must be "principled, not post-hoc" — the concern is that the three-way distinction could be used to explain away any failure. The formal protocol for making this distinction in practice is designed but not yet established.

**Q4.5:** What class of signals does the law NOT apply to? (Every physical law has a scope. Newton's laws don't apply at relativistic speeds. What is your scope boundary?)

> **Answer:** P-000 Proposition 11.3 states: "Current empirical support is strongest for deontic signals. Applicability to other signal classes (narrative, poetic, ambiguous, self-referential) requires further investigation." Proposition 1.7 defines four signal classes: deontic (obligations, prohibitions, permissions), descriptive (states of affairs), narrative (temporal sequences), and self-referential.
>
> The scope boundary is explicit: the law is claimed for **deontic signals** — signals carrying obligations, prohibitions, permissions, and modal constraints. Extension to descriptive, narrative, poetic, ambiguous, and self-referential signals is explicitly marked as unproven and requiring further investigation. EXP-006 (self-referential signals: 2/4 survived) provides preliminary evidence that the law may not hold as strongly for self-referential signals, confirming the scope boundary is real, not just cautious hedging.

---

## Requirement 5: Empirical Asymmetry

**Q5.1:** What is the asymmetry? Under what conditions is the quantity conserved, and under what conditions is it NOT conserved?

> **Answer:** The asymmetry is **governed vs. ungoverned transformation**. Under governed transformation (transformation passing through the Six-Gate Protocol with governance density ρ_g ≥ ρ*), the deontic content is conserved: C(T_gov(S)) = C(S). Under ungoverned transformation (transformation without governance constraints, ρ_g < ρ*), the deontic content decays monotonically: ΔH_C > 0 per step, with cumulative entropy scaling as Ω(σ√n).
>
> This is the First Law / Second Law pair — the core empirical claim of CT. The conditions are distinguishable, operationally defined, and independently manipulable: you either apply the Six-Gate Protocol or you don't. The asymmetry is not a theoretical postulate; it is a measured difference between two conditions.

**Q5.2:** Has the asymmetry been demonstrated empirically? (Not theorized — measured. Do you have data showing conservation under condition A and decay under condition B?)

> **Answer:** Yes. EXP-003 is the primary demonstration:
>
> - **Condition A (governed — Gate condition):** 13/20 signals achieved NLI bidirectional entailment = 1.00 across 10 recursive compression iterations — perfect conservation despite >80% surface compression.
> - **Condition B (ungoverned — Baseline/Compression conditions):** NLI degrades measurably by iteration 5 and sharply by iteration 10.
>
> The Second Law Draft states: "EXP-003, Gate condition: NLI = 1.00 for 13/20 signals at iteration 10 (First Law confirmed). EXP-003, Baseline/Compression: NLI degrades measurably by iteration 5, sharply by iteration 10 (Second Law signature)."
>
> The asymmetry is measured, not theorized. The same 20 signals, the same transformation protocol, the same oracle — the only variable is whether governance is applied. The difference is empirical.

**Q5.3:** Is the asymmetry reproducible? (If someone else sets up condition A and condition B, do they get the same asymmetry?)

> **Answer:** The infrastructure for reproducibility exists: a public test harness (GitHub), a public corpus, and a documented experimental protocol are available. The condition manipulation (apply Six-Gate vs. don't) is operationally specified. The oracle is a public model (deberta-v3-base-mnli on HuggingFace). Anyone with an API key to an LLM can run the experiment.
>
> **Documented independent reproduction:** Not yet in the corpus. All experiments (EXP-001 through EXP-007) were conducted by McHenry. Paper 4 plans cross-provider/architecture reproduction (testing whether the asymmetry holds across GPT-4, Claude, Gemini, Llama), but that paper is not yet executed.
>
> The asymmetry is reproducible *in principle* (public harness, public corpus, specified protocol, public oracle). Independent reproduction *in practice* is not yet documented. The technical barrier to reproduction is low — the harness is public and the protocol is specified.

**Q5.4:** What is the effect size? (In physics, the asymmetry between conservation and violation is infinite — it NEVER happens. What is your asymmetry? 0.94 vs 0.42? What are the confidence intervals?)

> **Answer:** The governed-side number: **13/20 signals (65%)** achieved NLI=1.00 across 10 iterations under the Gate condition. The ungoverned side: NLI degrades measurably by iteration 5 and sharply by iteration 10 — the exact NLI scores per iteration for the ungoverned condition are described qualitatively in the Second Law Draft ("measurably" and "sharply") without giving specific numbers per iteration in the materials I've read.
>
> The Wilson 95% confidence interval for the governed-side proportion (13/20 = 0.65) is approximately **[0.43, 0.82]**. This is wide — 20 signals is a small sample. Paper 5 plans formal Wilson confidence intervals as part of the GUM-compatible metrological framework, but that paper is not yet written.
>
> The asymmetry is 65% perfect conservation (governed) vs. measurable-to-sharp degradation (ungoverned). This is not the physics standard of "infinite asymmetry — it NEVER happens." 7/20 signals did not achieve perfect conservation under governance. The effect size is real and measurable but not absolute. The 7/20 failures are not yet fully characterized — they could be law failures, oracle limitations, or signal-specific kernel fragility (Paper 5's three-way distinction).

**Q5.5:** Does the asymmetry make a novel prediction? (A law that only explains what you've already observed is retrospective. Does your law predict something you haven't tested yet?)

> **Answer:** Yes, several novel predictions that have not yet been tested:
>
> 1. **Cross-provider conservation (Paper 4):** Conservation rates under governance should be statistically indistinguishable across AI providers and architectures (GPT-4, Claude, Gemini, Llama). The law predicts the model performing the transformation doesn't matter — only the governance protocol does. Not yet tested.
>
> 2. **Threshold decay regime (Paper 1):** Commitment decay under ungoverned transformation follows a threshold model — stability in early iterations followed by rapid collapse — rather than smooth linear or exponential degradation. Inferred from EXP-003 data but not yet formally tested with model comparison.
>
> 3. **Governance sparsity bound (Paper 3):** There exists a minimum governance density ρ* below which conservation fails regardless of constraint type. The Six-Gate Protocol is predicted to be one instance of ρ_g ≥ ρ*, not the unique instance. Not yet tested.
>
> 4. **Compression-Fidelity Bound (Paper 2):** Signals will collapse at a specific representation-length threshold — stable above the bound, rapid decay below it. Predicted from EXP-003/EXP-007 compression-boundary signals but not yet formally tested with systematic length variation.
>
> 5. **Post-Turing Test:** A system passing the Post-Turing Test (C(T_gov(S)) = C(S) across arbitrary input types and transformation depths) will preserve deontic content in high-stakes deployment contexts (legal, medical, regulatory) where ungoverned systems will not. A deployment-level prediction not yet tested.
>
> Each prediction is specific, falsifiable, and derivable from the law's structure. None have been tested yet.

---

*This is Pass 2 — revised after stress-testing against primary sources. Do not share with Version 2 solo sessions.*

*Scoring is in a separate file: `CT_SCORING_PASS2.md` — for outside review.*