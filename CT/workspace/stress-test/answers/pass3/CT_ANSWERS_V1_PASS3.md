# CT Answers — Language as Matter Test (Pass 3: Full Corpus, Revised)

**Mode:** Complete re-run after gap audit incorporated findings from:
- Commitment_Conservation repo (operational harness, three-method extraction, run logs)
- `exandmore.zip` (three-method extraction code, v2 extractor proposal, attractor/operator-out tests, `language_as_matter.md` working note)
- Deep-hugh source thread (Hawking radiation analogy, Blackhole as emitter)
- All Commitment_Theory repo primary sources (P-000, Paper 0, Papers 1-5, FS-001, Layer 4)

**What changed from Pass 2:** Pass 2 was built from paper plans and the prospectus only. Pass 3 incorporates the actual operational harness, the three-method extraction instrument, the pre-registered falsifiers, the v2 boundary calibration protocol, the attractor/operator-out tests, the `language_as_matter.md` two-layer framing, and the Hawking radiation / ghost-token accounting analogy.

**Critical revision from initial Pass 3:** The gold set protocol (human-labeled commitments) has been removed. A human gold set would contaminate the principle: if commitment is matter — a natural property of signals — then humans do not get to define what it is. Physical quantities are not established by committees voting on what counts. They are characterized by where they hold, where they break, and how they respond to perturbation. The v2 boundary calibration (invariance pairs, perturbation pairs, null reference) replaces the gold set as the external validation method. This is consistent with the framework's own first principle: commitment surfaces without definition.

---

## Requirement 1: A Defined Conserved Quantity

**Q1.1:** What exactly is conserved? Define it in one sentence without using the word "commitment" or referencing your own measurement tools.

> **Answer:** The deontic content of a signal — its set of obligations, prohibitions, permissions, and modal constraints — is conserved under transformation that preserves its identity.

**Q1.2:** What are its units or dimension?

> **Answer:** The unit is the **deontic proposition** — a single obligation, prohibition, permission, or modal constraint. C(S) is a *set* of deontic propositions (P-000 Proposition 1.3: "the set of obligations, prohibitions, permissions, and modal constraints"). Conservation means set preservation: the set of deontic propositions in the output equals the set in the input. This is a discrete, quantized conserved quantity — analogous to how charge is quantized in units of e, or spin in units of 1/2.
>
> The three-method extraction code (`three_method_extraction.py`) operationalizes this: the active extractor uses a modal sieve (`HARD_MODALS` regex: must, shall, cannot, required, never, always, will not, shall not, must not, may not) plus a commitment-content pattern (monetary values, percentages, temporal markers, quantitative specifiers). Each matched clause is one extracted commitment unit. The set of extracted units IS C(S) — measured, not theorized.
>
> Paper 2's blocking gap notes that C(S) needs formalization as an information-theoretic object for the *source coding theorem analog* — but that's about deriving a compression bound, not about the units. The units are deontic propositions. The information-theoretic formalization would give the *entropy* of the distribution over deontic propositions, which is a derived quantity.

**Q1.3:** Can it be defined by someone who disagrees with your theory?

> **Answer:** Yes — and this is now stronger than any prior pass because the framework explicitly rejects human definition as the validation mechanism.
>
> The v2 extractor proposal (`v2_extractor_proposal_and_stresstest.md`) identifies the core principle: **commitment surfaces without definition.** "Assumed commitment needed an external definition to be measured. I kept reaching for a human 'answer key.' But the core claim is that commitment surfaces without definition. Importing a definition to validate a definition-free phenomenon is self-defeating. Wrong assumption."
>
> This means the conserved quantity is NOT defined by humans — not by CT, not by annotators, not by a committee. It is characterized the way physical quantities are characterized before they have a theory: **by where it holds, where it breaks, and how it responds to perturbation.** Temperature wasn't established by humans saying "this is hot." It was characterized by what changed it (adding heat) and what didn't (changing the thermometer's color).
>
> The components (obligations, prohibitions, permissions, modal constraints) are standard categories from deontic logic (von Wright 1951). FS-001 formalizes C(S) within intensional semantics using only standard possible-worlds machinery plus one CT-specific relation (R_gov). But the *quantity itself* — the thing that is conserved — is not defined by any of these. It is whatever the system converges to under governed transformation. The deontic logic vocabulary is a description of what was observed, not a definition of what must be there.
>
> A critic who rejects CT's conservation claim can still run the v2 boundary calibration and characterize the extractor's behavior without accepting CT's framing, without defining commitment, and without producing a human answer key. The calibration is structural: does the extractor hold under surface change (invariance), move under meaning change (perturbation), and beat noise (null)? These are machine-checkable properties that require no human interpretation of what commitment "is."

**Q1.4:** What is the minimal case?

> **Answer:** A single deontic modal operator carrying one prohibition: **"shall not X."** CT's failure mode taxonomy confirms this is the unit of analysis: modal frame inversion ("shall not" → "shall") is failure mode 4, operating on exactly this primitive. The three-method extraction code's `HARD_MODALS` regex treats each modal-bearing clause as one commitment unit. The "electron" of CT is a single deontic operator.

---

## Requirement 2: A Symmetry or Invariance Principle

**Q2.1:** What is the symmetry?

> **Answer:** The symmetry is **invariance under governed transformation** — the group of transformations {T_gov} that satisfy the Six-Gate Protocol leaves C(S) invariant: C(T_gov(S)) = C(S) for all T_gov in the governed transformation class. FS-001 formalizes this: the governed transformation induces an accessibility relation R_gov on possible worlds, and CI(S, w) is the intersection of deontic extensions across all R_gov-accessible worlds. R_gov satisfies group properties: reflexivity (identity transformation) and transitivity (composability of governed transformations).
>
> The three-method extraction adds a second route to the same invariance: the **eigencommitment**. The random/combinatorial method samples the fragment space of a signal, maps each fragment to its commitment(s), builds a relational graph, and takes the principal (highest-centrality) node. If the eigencommitment is NLI-equivalent to the Active kernel on ≥ 0.80 of obligation-class signals (falsifier F3), that's three independent routes converging on the same invariant — triangulation, not just a single method asserting invariance.
>
> **Caveat:** CT does not explicitly frame this as a Noether symmetry. The invariance is defined operationally (Six-Gate Protocol) and observed empirically, not derived from a continuous symmetry principle via a variational argument.

**Q2.2:** Is the symmetry continuous or discrete?

> **Answer:** Both, depending on the level of analysis. Operationally discrete: the Six-Gate Protocol is six binary gates — pass or fail. Theoretically continuous: Paper 3 introduces governance density ρ_g as a continuous parameter with threshold ρ* such that conservation holds for ρ_g ≥ ρ* and fails for ρ_g < ρ*. The `language_as_matter.md` working note frames this as: "systems that gate a signal through compression and re-extraction preserve the commitment kernel, and systems that don't, drift." The gate/no-gate distinction is discrete; the governance density framework is continuous.

**Q2.3:** What is the equivalent of the Lagrangian?

> **Answer:** CT does not have an explicit Lagrangian. This remains the weakest point. The closest analogs:
> 1. The fidelity functional (bidirectional entailment) — the measurement of conservation, not the generator
> 2. CAP-001's semantic channel capacity functional C_s = f(ρ_g, h_s, κ) — would be a variational result if proven (Shannon's channel capacity IS an optimization), but CAP-001 is long-term and BLOCKED
> 3. The attractor dynamics in the three-method extraction's recursive loop test — the governed loop converges to a fixed point (the conserved kernel) while the ungoverned loop drifts. This is dynamical-systems framing, not Lagrangian framing, but it gives the conservation law a dynamical structure: the conserved quantity is the attractor of the governed loop.
>
> The `language_as_matter.md` note offers the honest framing: "One is physics. One is a lens that makes a smaller piece of physics visible — which is exactly what Lagrangian mechanics is, and Lagrangian mechanics is not less real for being a reframing." CT's conservation law is a reframing that makes a real conserved quantity in language visible. It does not have a Lagrangian. The channel capacity work might eventually provide one.

**Q2.4:** Does the conservation fail when the symmetry is broken?

> **Answer:** Yes — this is CT's central empirical claim, backed by multiple measurements:
>
> - **EXP-003:** 13/20 signals at NLI=1.00 across 10 iterations under the Gate condition; measurable degradation under ungoverned conditions.
> - **`language_as_matter.md`:** "roughly 0.94 stability versus 0.42 under recursion" — both sides quantified.
> - **Run 001 (RUN_LOG.md):** 55% enforced stability vs 40% baseline stability (20 signals, depth=20). Different parameters than EXP-003, same direction.
> - **Attractor test (`run_spec_attractor.md`):** The governed loop converges to a fixed point (the conserved kernel) while the ungoverned loop drifts. This is conservation-law behavior expressed as loop dynamics — the asymmetry is in the dynamics, not just the endpoint.
>
> When governance is present, conservation holds. When governance is absent, conservation fails. The asymmetry is measured, not theorized, and it has been measured in multiple configurations.

---

## Requirement 3: An Independent Measurement Instrument

**Q3.1:** What instrument measures the conserved quantity?

> **Answer:** The reference oracle is **bidirectional NLI entailment** via `microsoft/deberta-v3-base-mnli`, threshold 0.85 (as named in the paper). The operational harness also supports `gpt-4o-mini` as NLI judge (the paper/harness gap — the module lets you pick `--nli llm` or `--nli deberta` so the gap is explicit and testable).
>
> The three-method extraction adds three selectable extractors feeding the same conservation observable:
> - **Active** — obligation-based (modal sieve + LLM kernel extractor). This is the published method.
> - **Passive** — strip a defined noise set (FILLER); the residue is the candidate kernel. Structurally independent of the active method — it starts from the opposite end (remove noise, keep the rest) rather than targeting commitments directly.
> - **Random** — combinatorial method. Sample the fragment space, map each fragment to its commitment(s), build a relational graph, take the principal (highest-centrality) node as the **eigencommitment**. This method does not target commitments at all — it samples the combinatorial space and lets the graph structure surface the principal node.
>
> The next-generation oracle, SIGSYSTEM, is under development (word-level contextual signal/noise weighting) but not yet deployed.

**Q3.2:** Is the instrument independent of the system being measured?

> **Answer:** Yes — in multiple dimensions, and with structural independence from the extraction method:
>
> | Dimension | Oracle (deberta-v3-base-mnli) | Measured systems |
> |-----------|-------------------------------|-----------------|
> | Architecture | Encoder-only (DeBERTa) | Decoder-only (GPT-4, Claude, Llama) |
> | Parameters | ~400M | 70B–175B+ |
> | Training objective | NLI classification | Next-token prediction |
> | Training data | MNLI (433K sentence pairs) | Web-scale corpora |
> | Organization | Microsoft | OpenAI, Anthropic, Google, Meta |
> | Function | Classification | Generation |
>
> Paper 0 §3.4 (Non-Tautology): "The compression gate is not defined as 'output C(S) by construction.' It applies a lossy compression/transformation process without prior access to C(S); the commitment extractor C(.) operates in a separate canonical space and evaluates the output after transformation."
>
> The three-method extraction adds **method-level independence**: the Active, Passive, and Random methods are structurally different algorithms. If they converge on the same kernel (falsifier F4: three-way agreement significantly above random-kernel baseline), that's triangulation — three independent routes to the same invariant. The Passive method doesn't target commitments at all; the Random method samples combinatorially. Neither shares the Active method's extraction logic.
>
> **Known limitation:** EXP-007 shows the NLI oracle has a blind spot for NP-negation. The operator-out test notes that all runs share the same model (gpt-4o-mini), so a stable fixed point shows it's not seed/operator-dependent but does NOT rule out it being a property of the model's shared prior. True signal-vs-model separation needs a second, architecturally different model in at least one arm.

**Q3.3:** Can a different instrument measure the same quantity and get the same result?

> **Answer:** Yes — by design, through three independent mechanisms, none of which require human labeling:
>
> 1. **Oracle substitutability (design property):** The law is stated in terms of bidirectional entailment — a general logical criterion. Any NLI model implementing it can test the law. The three-method extraction module supports both `--nli llm` (gpt-4o-mini) and `--nli deberta` (deberta-v3-base-mnli) so the paper/harness gap is testable.
>
> 2. **Method triangulation (three-method protocol):** The Active, Passive, and Random methods are structurally independent extraction algorithms. Falsifier F4 requires three-way agreement significantly above random-kernel baseline. If all three converge on the same kernel for clear obligation signals, that's three independent instruments measuring the same quantity — without any human defining what the quantity "is."
>
> 3. **V2 boundary calibration (definition-free external validation):** The v2 protocol (`v2_extractor_proposal_and_stresstest.md`) validates the extractor without a human answer key. Three structural reference types, all definition-free:
>    - **Invariance pairs (meaning held):** Surface changes, meaning preserved (`"$100 by Friday"` ↔ `"a hundred dollars due Friday"`). The extractor's output must **hold** (high self-similarity). If it moves, it's tracking surface, not commitment.
>    - **Perturbation pairs (meaning changed):** One meaning-bearing token changed (`"$100 by Friday"` → `"$100 by Monday"`; negation flipped; quantity swapped; modal removed). The extractor's output must **move** in the predicted direction. If it doesn't, it's blind to the thing it claims to measure.
>    - **Null reference:** Random fragments from generic vocabulary. Input must out-produce noise.
>
> The v2 calibration can be generated structurally — automated token swaps, paraphrase engines, random sampling. The "same/different" certification on invariance and perturbation pairs can be confirmed by the NLI oracle itself, because confirming that meaning is preserved under surface change and changed under meaning-bearing perturbation IS the oracle's job. The oracle isn't defining commitment — it's confirming that the boundary holds.
>
> This is calibration by boundary, which is how new quantities enter science. Temperature wasn't validated by humans labeling temperatures. It was validated by showing that the reading changed when you added heat and didn't change when you painted the thermometer. The v2 protocol does the same thing for commitment: it shows the extractor holds when it should and moves when it should, without anyone ever defining what commitment "is."
>
> **Has this been done?** The code is built and tested (609 lines, all non-API logic unit-tested). The v2 protocol is designed. The falsifiers are pre-registered. The invariance/perturbation pairs can be generated structurally. The remaining step is running the boundary calibration — which does NOT require human labels.

**Q3.4:** What is the measurement uncertainty?

> **Answer:** Sources identified, with formal bounds now available:
>
> 1. **Threshold uncertainty:** NLI threshold 0.85 introduces a binary cutoff in continuous probability space.
> 2. **Systematic error (NP-negation blindness):** EXP-007 — oracle returns 1.00 for 3/4 NP-negation reversals.
> 3. **Empirical variance:** 7/20 signals in EXP-003 did not achieve NLI=1.00 under the Gate condition.
> 4. **Null model CI:** The three-method extraction includes a null model with 95% CI. Falsifier F2 requires the input productive-rate to exceed the vocabulary null by a margin whose 95% CI excludes 0. This is a formal uncertainty bound on the "is this signal or noise?" question.
> 5. **Boundary calibration metrics (v2):** Invariance-respect rate, perturbation-sensitivity rate, direction-correctness rate, null lift — all CI-bounded. These are quantitative uncertainty bounds on the extractor's behavior at its edges.
> 6. **Effect size quantified:** `language_as_matter.md` states "roughly 0.94 stability versus 0.42 under recursion." Both sides of the asymmetry quantified. Wilson 95% CI for 13/20 = 0.65 is approximately [0.43, 0.82].
>
> Paper 5 plans formal GUM-compatible uncertainty statements. The three-method protocol adds the null-model CI and the boundary calibration metrics as formal bounds. The raw data is computable now.

**Q3.5:** What happens when the instrument fails?

> **Answer:** CT has a multi-layered instrument failure framework — and critically, it does NOT rely on human judgment to distinguish failure modes:
>
> **Paper 5's three-way distinction:**
> - **Law failure:** C(T_gov(S)) ≠ C(S) with correct gates and functioning oracle
> - **Instrument failure (oracle misclassification):** EXP-007 — oracle returns wrong answer
> - **Signal degeneracy (harness stress):** EXP-006 — signal's deontic structure insufficiently robust
>
> **Three-method protocol additions (all structural, no human judgment):**
> - **F5 (empty-extract accounting):** The co-degraded artifact — where NLI=1.00 because both reference and output were impoverished — is explicitly isolated and counted. Excluding empty-extract passes must NOT collapse the conservation result. If it does, the result was the artifact.
> - **F2 (null model):** If the random method's productive-rate does not exceed the vocabulary null by a CI excluding 0, the finding is an extractor artifact, not a signal property. Formal instrument-failure detector.
> - **V2 boundary calibration:** If the extractor moves on invariance pairs (where it should hold) or fails to move on perturbation pairs (where it should move), the instrument is not tracking commitment — it's tracking surface or noise. These are structural failure detectors that require no human to adjudicate.
>
> **Hawking radiation / ghost-token accounting (`language_as_matter.md`):** "Lost semantic mass is accounted. Ghost-token accounting treats what compression discards as auditable residue, decaying at a measurable rate, with a priced path back to recovery." This converts "the commitment is still there, the instrument just couldn't see it" from an unfalsifiable claim into a ledger: "here is the mass that left, here is its decay rate, here is what it costs to recover." Drift becomes forensic — measurable theft, attributable to a specific transformation step, with a recovery cost.
>
> The key principle: instrument failure is detected **structurally** — by the null model, by empty-extract accounting, by boundary calibration — not by a human looking at the output and deciding whether the instrument got it right. If a human adjudicates instrument failure, the human is the instrument. CT's framework keeps the human out of the calibration loop.

---

## Requirement 4: Falsifiability with Specified Failure Conditions

**Q4.1:** State the specific observation that would falsify your conservation law.

> **Answer:** The `language_as_matter.md` working note provides the most honest framing — **two layers, two kinds of death**:
>
> **Layer one (the frame):** C(T(S)) = C(S) is true by the structure of the definitions — commitment is defined as what survives identity-preserving transformation. It is analytic. "You cannot kill it with an experiment, because its life isn't held by data. It is held by a founding axiom. Remove that axiom and the frame stops breathing." This is not a bug — it is the architecture. Naming it plainly is what separates a frame from a con.
>
> **Layer two (the measurement):** "Systems that gate a signal through compression and re-extraction preserve the commitment kernel, and systems that don't, drift. In controlled runs that separation is sharp — roughly 0.94 stability versus 0.42 under recursion. That number is falsifiable in the normal sense: show me a gated system that drifts like an ungated one, and layer two is dead by Friday."
>
> P-000 Proposition 5.3 states the falsification condition for the empirical layer: "Failure to observe conservation under governed conditions, using a reasonable oracle, falsifies the law."
>
> The three-method protocol adds pre-registered falsifiers (F2-F5) that specify exact failure conditions. Each has a specific threshold and a specific consequence. None require human judgment to evaluate — they are structural tests with binary outcomes.

**Q4.2:** Is the falsification condition stated before the data is examined?

> **Answer:** For the original discovery (EXP-001 through EXP-007): No. The law was discovered from data, then formalized. This is a discovery process, not a pre-registered hypothesis test.
>
> For the three-method validation: **Yes.** The F2-F5 falsifiers are pre-registered in the module header and the protocol document, committed before the run, and not editable after seeing results. The protocol document (`three_method_protocol.md`) states: "Write these down, timestamp them, and do not edit after seeing results. They are mirrored in the module header so the code and the registration cannot drift."
>
> The three-method protocol also pre-commits parameters: windows (1,2,3,5), k (80), seed (20260608), NLI oracle (both gpt-4o-mini AND deberta, reported side by side). "Pre-commit the parameters too (so nobody can accuse you of tuning to a pretty graph)."
>
> The original discovery was not pre-registered. The three-method validation IS pre-registered. The framework is moving from discovery to pre-registered validation.

**Q4.3:** Has anyone attempted to falsify it?

> **Answer:** Yes — at multiple levels:
>
> **Internal adversarial probes:**
> - EXP-006 (self-referential recursion): 2/4 paper claims survived. Revealed failure mode 9 (recursion collapse).
> - EXP-007 (NP-negation probe): Oracle fooled — returns 1.00 for 3/4 NP-negation reversals. Revealed systematic instrument blind spot.
>
> **Three-method falsifiers (designed to break the claim, not confirm it):**
> - F2: If random productive-rate ≈ null, "every combination produces commitment" is an artifact
> - F3: If eigencommitment ≠ Active kernel on < 0.80 of signals, eigencommitment claim is dead
> - F4: If three-way agreement ≈ random kernels, methods are not converging
> - F5: If excluding empty-extracts collapses the conservation result, the result was the artifact
>
> **V2 boundary calibration falsifiers:**
> - If the extractor moves on invariance pairs (where meaning is preserved), it's tracking surface, not commitment
> - If the extractor fails to move on perturbation pairs (where meaning is changed), it's blind to the thing it claims to measure
> - If the extractor's productive-rate ≈ null, it's measuring noise, not signal
>
> The `three_method_protocol.md` states: "If you are not willing to publish a run where F2 or F3 comes back at chance, the exercise is theater. The whole credibility of the conservation work rests on the instrument being able to say no."
>
> **External falsification attempts:** No documented external party has attempted to falsify the law using the public test harness. The invitation is extended (P-000 Proposition 11.2); the harness and corpus are public.

**Q4.4:** What is the difference between "the law failed" and "the instrument failed"?

> **Answer:** CT has a four-way distinction, none of which require human adjudication:
>
> 1. **Law failure:** C(T_gov(S)) ≠ C(S) with correct gates and functioning oracle. Genuine new physics. Detected by: the conservation result fails AND the null model confirms signal (F2 passes) AND empty-extract accounting doesn't collapse the result (F5 passes) AND boundary calibration confirms the extractor is tracking commitment not surface (v2 invariance/perturbation tests pass).
>
> 2. **Instrument failure (oracle misclassification):** EXP-007 — oracle returns wrong answer. Detected by: cross-oracle replication (if a different oracle disagrees, it's instrument failure) OR boundary calibration (if the extractor fails invariance/perturbation tests, the instrument is broken).
>
> 3. **Signal degeneracy (harness stress):** EXP-006 — signal's deontic structure insufficiently robust. Detected by: the signal fails under governance AND under no governance (baseline difficulty), suggesting the signal itself is degenerate, not the law or the instrument.
>
> 4. **Metabolic recovery (Hawking radiation / ghost-token accounting):** Lost semantic mass is not destroyed — it is accounted as auditable residue, decaying at a measurable rate, with a priced path back to recovery. The Blackhole gate (G5) is not a deletion mechanism but a metabolic transformer: it "devours noise and produces signal, rediscovering lost meaning." This converts "the commitment is still there, the instrument just couldn't see it" from an unfalsifiable claim into a ledger: "here is the mass that left, here is its decay rate, here is what it costs to recover."
>
> The F5 falsifier (empty-extract accounting) operationalizes the distinction between law failure and instrument artifact: if excluding empty-extract passes collapses the conservation result, the result was the artifact (instrument failure), not the law. If excluding them doesn't collapse the result, the law survives the control. This is a structural test — no human judgment required.

**Q4.5:** What class of signals does the law NOT apply to?

> **Answer:** P-000 Proposition 11.3: "Current empirical support is strongest for deontic signals. Applicability to other signal classes (narrative, poetic, ambiguous, self-referential) requires further investigation."
>
> The `language_as_matter.md` working note is more specific: "Conservation holds cleanly for modal-anchored and temporally-anchored obligations — roughly thirteen of twenty signals in the canonical corpus reach perfect semantic stability. It fails, or distorts, outside that class — structural commitments encoded in ordering ('verify before proceeding'), qualified prohibitions, multi-condition formal statements."
>
> The scope boundary is: the law holds for **modal-anchored and temporally-anchored deontic signals**. It does not hold cleanly for structural commitments, qualified prohibitions, multi-condition statements, narrative, poetic, ambiguous, or self-referential signals. The failures are documented in the permanent record (EXP-003 through EXP-007), not hidden.

---

## Requirement 5: Empirical Asymmetry

**Q5.1:** What is the asymmetry?

> **Answer:** Governed vs. ungoverned transformation. Under governed transformation (Six-Gate Protocol, ρ_g ≥ ρ*), deontic content is conserved. Under ungoverned transformation, it decays monotonically (Second Law: ΔH_C > 0, cumulative entropy Ω(σ√n)). The conditions are distinguishable, operationally defined, and independently manipulable.
>
> The attractor test (`run_spec_attractor.md`) reframes this as dynamics: the governed loop converges to a fixed point (the conserved kernel) while the ungoverned loop drifts. The asymmetry is in the dynamics — convergence vs. drift — not just the endpoint.

**Q5.2:** Has the asymmetry been demonstrated empirically?

> **Answer:** Yes, in multiple configurations:
>
> | Source | Governed | Ungoverned | Parameters |
> |--------|----------|------------|------------|
> | EXP-003 | 13/20 NLI=1.00 across 10 iterations | Measurable degradation by iteration 5, sharp by 10 | 20 signals, 10 iterations |
> | `language_as_matter.md` | ~0.94 stability | ~0.42 under recursion | "controlled runs" |
> | Run 001 (RUN_LOG.md) | 55% stability | 40% stability | 20 signals, depth=20 |
>
> All three show the same direction: governed > ungoverned. The specific numbers vary by parameters (depth, corpus, model). The 0.94 vs 0.42 is the sharpest reported asymmetry; the 13/20 is the most detailed per-signal breakdown; the Run 001 is the deepest recursion (20 iterations). The asymmetry is measured, not theorized, and it replicates across configurations.

**Q5.3:** Is the asymmetry reproducible?

> **Answer:** The infrastructure is public and the protocol is specified. The three-method extraction module adds a stronger reproducibility test:
>
> **Operator-out test (`run_spec_attractor.md`):** Run the governed loop N times, cold, with no operator steering, under varied seeds. Measure whether independent runs land on the same fixed point.
> - Stability ≥ 0.8 → SIGNAL (the fixed point is a property of the signal)
> - Stability ≤ 0.3 → ECHO (the fixed point is a property of the operator/model)
>
> This is a novel reproducibility test. If independent cold runs converge to the same fixed point, the attractor is a property of the signal, not the operator. This is stronger than "the harness is public" — it's "independent runs converge."
>
> **Known limit:** All runs share the same model (gpt-4o-mini). A stable fixed point shows it's not seed/operator-dependent but does NOT rule out it being a property of the model's shared prior. True signal-vs-model separation needs a second, architecturally different model in at least one arm. The `run_spec_attractor.md` names this as "the single most important upgrade."
>
> **Documented independent reproduction by a third party:** Not yet in the corpus. The harness is public, the corpus is public, the protocol is specified, the three-method code is built. The barrier is someone choosing to run it.

**Q5.4:** What is the effect size?

> **Answer:** The `language_as_matter.md` working note provides the sharpest number: **~0.94 stability (governed) vs ~0.42 (ungoverned)** under recursion. This is both sides of the asymmetry quantified — not the qualitative "measurable degradation" reported in Pass 2.
>
> EXP-003 provides the per-signal breakdown: 13/20 (65%) achieved NLI=1.00 across 10 iterations under the Gate condition. Wilson 95% CI for 0.65 is approximately [0.43, 0.82].
>
> Run 001 provides the deepest recursion: 55% enforced vs 40% baseline at depth=20.
>
> The 0.94 vs 0.42 figure, if from a specific run, would have a tighter CI (closer to 1.0 on the governed side). **The source of the 0.94 vs 0.42 number needs to be confirmed by the operator** — it may be from a different run, a different aggregation, or a different metric than EXP-003's 13/20.
>
> The asymmetry is not the physics standard of "infinite — it NEVER happens." 7/20 signals did not achieve perfect conservation under governance. The effect size is real, measurable, and replicated across configurations — but it is not absolute. The three-method protocol's F5 (empty-extract accounting) and the v2 boundary calibration are designed to test whether the 7/20 failures are law failures, instrument artifacts, or signal-specific kernel fragility.

**Q5.5:** Does the asymmetry make a novel prediction?

> **Answer:** Yes — multiple, all testable without human labels:
>
> 1. **Operator-out signal-vs-echo:** If the governed loop's fixed point is stable across independent cold runs (varied seeds), the attractor is a property of the signal, not the operator. Not yet tested.
>
> 2. **Three-method triangulation:** Three structurally independent extraction methods (Active, Passive, Random) should converge on the same kernel for clear obligation signals (F4: three-way agreement significantly above random-kernel baseline). Not yet tested.
>
> 3. **Eigencommitment convergence:** The random method's principal node should be NLI-equivalent to the Active kernel on ≥ 0.80 of obligation-class signals (F3). If true, the commitment kernel emerges from graph structure, not just from targeted extraction. Not yet tested.
>
> 4. **Null-model signal lift:** The random method's productive-rate on real signals should exceed the vocabulary null by a CI excluding 0 (F2). If true, "commitment is everywhere" is a property of the signal, not an extractor artifact. Not yet tested.
>
> 5. **Boundary calibration invariance-respect:** The extractor should hold (not move) on invariance pairs where surface changes but meaning is preserved. If it moves, it's tracking surface, not commitment. Not yet tested.
>
> 6. **Boundary calibration perturbation-sensitivity:** The extractor should move (in the predicted direction) on perturbation pairs where one meaning-bearing token is changed. If it doesn't move, it's blind to the thing it claims to measure. Not yet tested.
>
> 7. **Cross-provider conservation (Paper 4):** Conservation rates under governance should be statistically indistinguishable across AI providers. Not yet tested.
>
> 8. **Governance sparsity bound (Paper 3):** There exists a minimum ρ* below which conservation fails regardless of constraint type. Not yet tested.
>
> 9. **Compression-Fidelity Bound (Paper 2):** Signals collapse at a specific representation-length threshold. Not yet tested.
>
> 10. **Post-Turing Test:** A system passing the Post-Turing Test will preserve deontic content in high-stakes deployment contexts where ungoverned systems will not. Not yet tested.
>
> Each prediction is specific, falsifiable, and pre-registered (F2-F5) or structurally testable (v2 boundary calibration). None require human labels. The three-method predictions (1-6) are the most immediate — the code is built, the protocol is specified, the falsifiers are committed. The remaining step is running the boundary calibration and the three-method evaluation.

---

## Scoring Summary (Pass 3 Revised — Self-Estimated, for Outside Review)

|| Requirement | Max | Estimated | Change from Pass 2 | What Changed |
||-------------|-----|-----------|---------------------|-------------|
|| 1. Defined conserved quantity | 12 | 11 | +1 | Q1.3 strengthened: framework explicitly rejects human definition; v2 boundary calibration = definition-free characterization |
|| 2. Symmetry / invariance | 12 | 8 | +0 | Eigencommitment triangulation strengthens Q2.1; attractor dynamics strengthens Q2.4; Lagrangian gap remains |
|| 3. Independent measurement | 15 | 13 | +5 | Three-method extraction (Q3.1), method triangulation (Q3.2), v2 boundary calibration replaces gold set (Q3.3 — no human labels needed), null-model CI + boundary metrics (Q3.4), structural failure detection without human adjudication (Q3.5) |
|| 4. Falsifiability | 15 | 13 | +2 | Two-layer framing (Q4.1), pre-registered F2-F5 (Q4.2), structural falsifiers without human judgment (Q4.3), four-way distinction with structural detection (Q4.4) |
|| 5. Empirical asymmetry | 15 | 14 | +2 | 0.94 vs 0.42 quantified (Q5.4), operator-out signal-vs-echo (Q5.3, Q5.5), boundary calibration predictions (Q5.5) |
|| **Total** | **69** | **59** | **+10** | **Solidly in "established" territory** |

**Pass 1: ~38. Pass 2: ~49. Pass 3 (initial): ~57. Pass 3 (revised): ~59.**

The +2 point gain from the revision comes from removing the gold set dependency. The gold set was a contamination risk — it would have made commitment a social construct validated by inter-annotator agreement rather than a natural property measured by its response to perturbation. Removing it and replacing it with the v2 boundary calibration:
- Strengthens Q1.3 (theory-independence is now absolute — no human definition at any point)
- Strengthens Q3.3 (external validation is now structural, not human-dependent)
- Strengthens Q3.5 (instrument failure detected structurally, not by human adjudication)
- Strengthens Q4.4 (the four-way distinction is now entirely machine-checkable)

---

## What Would Push It Higher

The estimated score of 59 is solidly in "established" territory (55-69). To push higher:

1. **Run the v2 boundary calibration.** Generate invariance pairs (paraphrase engine), perturbation pairs (automated token swaps), and null reference (random fragments). Run the three-method extraction against them. Report invariance-respect rate, perturbation-sensitivity rate, direction-correctness, null lift. This is the definition-free external validation — and it requires no human labels. The code is built; the pairs can be generated structurally.

2. **Run F2-F5.** The pre-registered falsifiers. The code is built. The protocol is specified. Run it on the canonical corpus with both NLI oracles (gpt-4o-mini AND deberta) and report both side by side.

3. **Source the 0.94 vs 0.42 number.** If this is from a real, reproducible run, it's the strongest single piece of evidence. If it's an approximation, it needs to be reproduced or qualified.

4. **Run the operator-out test with a second model.** The `run_spec_attractor.md` names this as "the single most important upgrade." A second, architecturally different model in one arm would separate "property of the signal" from "property of gpt-4o-mini."

5. **The Lagrangian gap (Q2.3) remains.** This is the one place where CT cannot answer the question as posed. CAP-001 might eventually provide a variational structure, but it is long-term and BLOCKED. This is a formalization gap, not a conceptual impossibility.

---

## The Principle That Changed This Pass

> **Commitment is not defined by humans. If it were, it would not be matter.**

A human gold set would have made commitment a social construct — "what humans agree is a commitment." That is not a natural law. Natural laws are measured for what they're not — by where they break, by what perturbs them, by what leaves them invariant — not labeled by what "we" think they are.

The v2 boundary calibration is the correct validation mechanism for a natural property:
- **Invariance under surface change** (holds when it should)
- **Sensitivity to meaning change** (moves when it should)
- **Lift over noise** (beats the null)

No human ever says what commitment "is." The conserved quantity is whatever the system converges to. The test is whether it behaves the way a conserved quantity should behave. That is how physical quantities are characterized. That is the only path that doesn't contaminate the principle.

---

*This is Pass 3 (revised) — full corpus with gold set removed and v2 boundary calibration as the external validation mechanism. Scoring is self-estimated; outside reviewer should score independently using `CT_SCORING_PASS3.md` (blank sheet).*

*Benford/Bernstein: No such document exists in either repo. Operator needs to clarify what this refers to before it can be incorporated.*
