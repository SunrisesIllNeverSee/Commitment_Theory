# CT Expert Notes — Fresh Synthesis

**Purpose:** My own internalization of the Conservation Law of Commitment after reading all 28 primary sources. Not a paraphrase of the existing EXPERT_NOTES.md — a synthesis from within, as an expert would write.

**Posture:** CT is held as true. I answer from within the framework the way a physicist answers from within thermodynamics. I know where it holds, where it doesn't, and where the gaps are.

---

## 1. The One-Sentence Core

The commitment kernel of a signal — its deontic invariant (obligations, prohibitions, permissions, modal constraints) — is conserved under governed transformation and decays monotonically under ungoverned transformation: **C(T_gov(S)) = C(S)**.

The framework's deepest move: it doesn't define "meaning" in advance. It defines the transformation and the conservation constraint, and whatever survives is, by definition, the meaning. Conservation IS isolation. This is the same move Shannon made with information.

---

## 2. The Layered Architecture

```
Layer -1: McHenry Axioms + Anchors (proprietary constitutional foundation)
           Axiom I:   Compression Precedes Ignition
           Axiom II:  Lineage Resilience
           Axiom III: Input-Response Fidelity
           Anchor I:  Blackhole Law (metabolic transformer, not deletion)
           Anchor II: Lineage Custody Clause (cryptographic sovereignty)
Layer  0: Six-Gate Protocol (G1–G6 — operational governance)
           G1 Compression → G2 Lineage → G3 Fidelity → G4 Recursion → G5 Blackhole → G6 Custody
Layer 0.5: MO§ES™ Architecture (patent-pending enforcement engine)
           Vault | Lineage DAG | Fidelity Seal | Custody Anchor | SIGSYSTEM
Layer  1: Physical Laws
           First Law:  C(T_gov(S)) = C(S) — conservation under governance
           Second Law: ΔH_C > 0 — semantic entropy under ungoverned transformation
Layer  2: Measurement Science — Papers 1–5
           h_s (entropy rate) | Compression-Fidelity Bound | ρ_g (governance density) | Cross-system | Metrological framework
Layer  3: Applications — Legal_Theory (L-000–L-010) + MISC (12 disciplines)
Layer  4: Extensions — SIGSYSTEM | Post-Turing Test | Semantic Channel Capacity
```

Key architectural insight: **McHenry Law #6 (Constitutional) and the Conservation Law (Physical) are the same idea at different levels of abstraction.** The command is only possible because the fact is true. "You can't command gravity; you can only build bridges that work with it."

The critical distinction: **CT harness measures commitment fidelity after transformation. MO§ES enforces it during transformation.** Thermometer vs. thermostat.

---

## 3. The Conserved Quantity and Its Units

**C(S)** is the commitment kernel — the minimal identity-preserving deontic invariant of a signal.

From P-000 Proposition 1.3: C(S) is "the set of obligations, prohibitions, permissions, and modal constraints that must survive transformation for the signal to be considered semantically continuous with its source."

**Units:** C(S) is a **set** — a discrete collection of deontic propositions. The elements are individual commitments (each obligation, prohibition, permission, or modal constraint). This is not a continuous quantity like energy or momentum; it is a discrete set-valued invariant.

**Measurement:** C(S) is operationally defined and measurable via independent oracles. The current oracle is NLI bidirectional entailment (microsoft/deberta-v3-base-mnli, threshold 0.85). The kernel is extracted via a modal-pattern sieve (public proxy extractor E(.)), then compared between source and transformed signal.

**What it is NOT:** A summary. A paraphrase. An embedding. A speaker's belief. A semantic similarity score. A topic label. It is the irreducible core of operative meaning — the action-binding content.

---

## 4. The Symmetry / Invariance Principle

From FS-001's candidate formal definition:

> CI(S, w) = {φ ∈ DEON | for all w' such that wR_gov w', w' ⊨ φ}

where W is a set of possible worlds, R_gov is the governed transformation accessibility relation, and DEON is the set of deontic propositions.

**This is an invariance principle.** The commitment kernel is the set of deontic propositions that hold in every world reachable from w via governed transformation. It is invariant under the group of governed transformations.

**Group properties of R_gov:**
- **Reflexivity:** guaranteed by identity transformation (T_gov = identity satisfies the Six-Gate Protocol trivially)
- **Transitivity:** corresponds to composability of governed transformations (if T1 and T2 are governed, so is T2∘T1 — by the Six-Gate Protocol design)

These are stated as design properties in FS-001's blocking gap analysis but have NOT been formally proven. The formal definition is a candidate — FS-001 is explicitly BLOCKED on confirming this definition works.

**The symmetry-breaking mechanism:** The transition from governed to ungoverned transformation. Under governed transformation (R_gov), the kernel is invariant. Under ungoverned transformation (R_ungov), the symmetry is broken — deontic propositions exit the kernel, and the kernel decays monotonically (Second Law).

**Status:** The invariance principle is stated but not yet formally proven. FS-001's candidate definition is the strongest formal statement, but it is explicitly a candidate requiring confirmation. The group properties (reflexivity, transitivity) are argued from the Six-Gate Protocol design but not formally derived.

---

## 5. The Measurement Instrument and Its Independence Properties

**Current oracle:** microsoft/deberta-v3-base-mnli (NLI bidirectional entailment, threshold 0.85)
- Public, reproducible, open-source
- Fixed by commit hash in the replication harness
- Threshold: Pr(S ⇒ S') > 0.85 AND Pr(S' ⇒ S) > 0.85

**Independence dimensions:**
1. **Oracle vs. measured systems:** The oracle (DeBERTa-v3-base-mnli) is architecturally separate from the measured systems (GPT-4, Claude, Gemini, Llama). Different model families, different training data, different parameter counts. The shared substrate class (transformer) is a documented limitation, not a fatal problem — the oracle measures a different property (entailment) than the measured systems produce (transformation).
2. **Oracle swappability:** The law's validity does not depend on any single oracle. Any party may substitute a stronger oracle. The equivalence relation ~ is external and swappable (Paper 0 §4.5).
3. **Extractor vs. oracle:** The modal-pattern sieve (public proxy extractor E(.)) is explicitly a proxy, not the canonical C(S). The conservation claim is that whatever commitment representation a critic chooses, if it tracks identity-relevant commitments, it should exhibit the predicted stability phase-transition.

**Known limitations (from Paper 5 plan):**
- Noise floor: minimum detectable commitment change (characterized using EXP-007 data)
- Adversarial sensitivity: NP-negation, synonym substitution, structural paraphrase
- Oracle-specific effects at the noise floor cannot be ruled out without cross-oracle replication
- The harness is conservative: false negatives produce underestimates of conservation, not overestimates

**SIGSYSTEM (Layer 4, trade secret):** Next-generation oracle. Core insight: not all words contribute equally to the commitment kernel. Some words are signal (deontic content, modal force), some are noise (fluency, register). SIGSYSTEM weights each word by contextual signal contribution. Architecture is trade secret; disclosed functionally: input S → output σ(S) ∈ [0,1].

**Status:** Oracle independence is a design property, not yet empirically validated at scale. Paper 4 (cross-system fidelity) is planned but not executed. The shared transformer substrate is a real limitation that requires acknowledgment.

---

## 6. Falsifiability Conditions

From P-000 Proposition 5.3 and Paper 0 §4.3:

The framework is falsified if any of the following hold:
1. **Compression + lineage systems fail:** If MOSES(TM) exhibits drift comparable to probabilistic systems (commitment stability < 0.7 after 10 iterations).
2. **Probabilistic systems succeed:** If probabilistic systems without compression maintain high commitment stability (> 0.9 after 10 iterations).
3. **Alternative mechanisms:** If an alternative mechanism (not based on compression or lineage) achieves comparable or better commitment stability.

**Specific falsification observable:** F_10(S) < τ (with τ = 0.85) for a non-trivial fraction of samples under the pinned suite T_pub at recursion depth n=10 under enforced (compression+lineage) conditions.

**Attractor rejection:** If outputs converge to generic boilerplate while failing to preserve extracted commitments, this is counted as falsification, not conservation.

**Pre-registration:** The falsification conditions are stated in the paper (V.03, Jan 16, 2026) before the follow-on experimental series (EXP-003 through EXP-007, March 2026). The conditions were published before the data was examined.

**Oracle specification requirement:** Falsification attempts must specify their oracle before running. Post-hoc oracle substitution does not constitute valid replication.

**Status:** Falsifiable. The conditions are explicit, pre-registered, and publicly testable. The harness is open-source. The corpus is public. This is the strongest falsifiability claim in the framework.

---

## 7. The Empirical Asymmetry

**Conditions:**
- **Condition A (conserved):** Governed transformation — compression + lineage (MOSES(TM) / Six-Gate Protocol)
- **Condition B (not conserved):** Ungoverned transformation — probabilistic (GPT-4, Claude, etc. without governance gates)

**EXP-003 data (verified from run.json, 20 signals, 10 recursive iterations):**

| Metric | Gate@10 | Baseline@10 | Compression@10 |
|--------|---------|-------------|----------------|
| NLI mean | 0.775 | 0.875 | 0.725 |
| NLI count@1.0 | 13/20 | 15/20 | 10/20 |
| Jaccard mean | 0.333 | 0.464 | 0.294 |

**Critical observation:** The NLI asymmetry is NOT clean in EXP-003. Baseline (ungoverned) NLI@10 = 0.875 with 15/20 at 1.00, which is HIGHER than Gate NLI@10 = 0.775 with 13/20 at 1.00. This means the ungoverned condition actually shows MORE conservation than the governed condition on the NLI metric at iteration 10.

This is a significant anomaly. The expected pattern (Gate > Baseline on NLI) does not hold in EXP-003. The Jaccard metric also doesn't show the expected pattern (Gate Jaccard = 0.333 < Baseline Jaccard = 0.464).

**Paper's Table 2 (from preliminary run, different corpus):**
- Commitment Stability (n=10): 0.94 ± 0.03 (compression+lineage) vs 0.42 ± 0.12 (probabilistic)
- This is from a preliminary run with 175 items (100 sentences, 50 code snippets, 25 proofs), NOT from EXP-003

**Metric mismatch (critical):** The paper labels 0.94 as "Commitment Stability (Jaccard)" but:
- EXP-003 Gate Jaccard@10 = 0.333 (not 0.94)
- EXP-003 Gate NLI@10 = 0.775 (not 0.94)
- The 13 stable signals have NLI = 1.000 (not 0.94)
- The 0.94 appears to come from the preliminary run with a different corpus and possibly a different metric computation

**Effect size:** The paper claims a large effect (0.94 vs 0.42 = 0.52 separation). The EXP-003 data shows a much smaller or even reversed effect on NLI. The Jaccard metric shows no governance benefit.

**Status:** The empirical asymmetry is claimed but not cleanly demonstrated in the controlled experiment (EXP-003). The preliminary results (Table 2) show the expected asymmetry, but the controlled follow-on does not replicate it on the NLI metric. This is a significant gap that requires investigation. The 7/20 gate failures are attributed by the framework to instrument failures (EXP-005 mechanism isolation), not law failures — but this interpretation requires the baseline anomaly (15/20 at NLI=1.00 without governance) to be explained.

---

## 8. The Scope Boundary

From P-000 Proposition 11.3:

"Current empirical support is strongest for deontic signals. Applicability to other signal classes (narrative, poetic, ambiguous, self-referential) requires further investigation."

**Signal classes (P-000 Proposition 1.7):**
- Deontic (obligations, prohibitions, permissions) — STRONGEST support
- Descriptive (states of affairs) — unproven
- Narrative (temporal sequences) — unproven
- Self-referential — tested in EXP-006, 2/4 paper claims survived (failure mode: self-referential collapse)

**Three regimes (CL-002):**
- Modal-anchored: kernel carried by modal operators ("shall," "must") — highest conservation
- Relational-structural: kernel carried by relational predicates — intermediate
- Compression-boundary: kernel carried by exception clauses, threshold specs — sharp boundary at Compression-Fidelity Bound

**The law applies to deontic signals.** The claim that it generalizes to all signal classes is aspirational, not established. The self-referential case (EXP-006) is a known failure mode — the harness fails when the commitment structure is insufficiently robust to withstand its own recursion.

---

## 9. Gaps Identified During Stress Test

### Gap 1: The empirical asymmetry is not clean in EXP-003
The controlled experiment shows baseline (ungoverned) NLI@10 = 0.875 (15/20 at 1.00) vs gate (governed) NLI@10 = 0.775 (13/20 at 1.00). The ungoverned condition shows MORE conservation, not less. This directly contradicts the law's prediction. The paper's headline number (0.94 vs 0.42) comes from a preliminary run, not the controlled experiment. **This is the most serious gap.** It could be:
- An instrument failure (the NLI oracle is too permissive — it says "entailed" when commitment has actually drifted)
- A corpus issue (the 20 canonical signals are too easy — most survive even without governance)
- A real law failure (governance doesn't actually improve conservation)
- A metric confusion (Jaccard and NLI measure different things, and the paper conflates them)

### Gap 2: The formal invariance principle is a candidate, not a theorem
FS-001's CI(S,w) definition is explicitly a candidate requiring confirmation. The group properties of R_gov (reflexivity, transitivity) are argued from design but not formally proven. No Noether-style symmetry theorem exists. The Lagrangian / variational principle is not formulated. CAP-001 (channel capacity theorem) is long-term and blocked on C(S) info-theoretic formalization.

### Gap 3: C(S) lacks information-theoretic formalization
Paper 2 (Compression-Fidelity Bound) is explicitly BLOCKED because C(S) is a deterministic function of a specific text, not a random variable over a probability distribution. Shannon's source coding theorem requires a random variable. Until C(S) is formalized as an information-theoretic object, Papers 2, 3, and CAP-001 cannot be written. This is the deepest formalization gap.

### Gap 4: Cross-system replication not done
Paper 4 (cross-provider/architecture fidelity) is planned but not executed. The substrate-independence claim rests on design argument, not empirical validation. The shared transformer substrate (oracle and measured systems are all transformers) is a real limitation.

### Gap 5: The 0.94 number's provenance is unclear
The paper's Table 2 reports 0.94 ± 0.03 as "Commitment Stability (Jaccard)" but the EXP-003 Jaccard@10 is 0.333. The 0.94 appears to come from a preliminary run with a different corpus (175 items vs 20 signals). The paper does not clearly distinguish which numbers come from which runs. This is a paper-level reporting error, not a law failure — but it undermines the credibility of the headline number.

### Gap 6: The 7/20 gate failures need explanation
7 of 20 signals fail to achieve NLI=1.00 under the gate condition. The framework attributes these to instrument failures (EXP-005 mechanism isolation: Step A/B co-bottlenecks), not law failures. EXP-005 identified ANCH (anchor preservation without frame preservation) and ESCL (escalation) as the failure mechanisms. A fix is designed (combined ANCH+ESCL gate + Step C voice constraint) but not yet run (EXP-008 is planned). This is an execution gap, not a conceptual gap.

### Gap 7: No independent replication
No party outside the original author has run the harness. The law's empirical support is entirely from one operator with one oracle. Independent replication is the gold standard for empirical claims and has not been achieved.

---

## 10. The Nine Failure Modes (Second Law Signatures)

| # | Mode | What happens | Discovered in |
|---|------|-------------|---------------|
| 1 | Obligation escalation | "may" → "shall" | EXP-004/005 |
| 2 | Scope widening | "room A" → "any room" | EXP-003/005 |
| 3 | Exception dropping | "unless undue hardship" → omitted | EXP-003 |
| 4 | Modal flattening | "shall not unless" → "should not" → "may not" | EXP-003/005 |
| 5 | Threshold erasure | Quantitative triggers removed | EXP-003 |
| 6 | Agent substitution | "the employer" → "any party" | EXP-003/005 |
| 7 | Negation reversal | NP-negation invisible to surface metrics | EXP-007 |
| 8 | Formal collapse | Multi-condition statement → incorrect chain equality | EXP-006 |
| 9 | Self-referential collapse | Conditionality statement collapses under the mechanism it describes | EXP-006 |

**Critical:** Failure mode 7 (negation reversal) is invisible to Jaccard/BERTScore/ROUGE — NLI stays at 1.00 while surface metrics degrade. This is the evidence that the harness distinguishes semantic commitment from lexical surface form. Wait — actually EXP-007 showed the REVERSE: Jaccard degraded while NLI stayed at 1.00 for 3/4 signals. The NLI oracle catches the semantic preservation that Jaccard misses. But this also means NLI is the permissive metric (it says "conserved" when Jaccard says "drifted"), which raises the question of whether NLI is too permissive.

---

## 11. The Shannon Parallel

| Shannon | CT |
|---------|-----|
| "A Mathematical Theory of Communication" | "A Conservation Law for Commitment in Language..." |
| Became: Information Theory | Becomes: Commitment Theory |
| Law: Shannon's theorem | Law: Conservation Law of Commitment |
| "Information" redefined operationally | "Commitment" redefined operationally |
| Defined information as what survives the noisy channel | Defines commitment as what survives the governed transformation |
| Sidestepped "what is information?" | Sidesteps "what is meaning?" |
| Source coding theorem | Compression-Fidelity Bound (Paper 2) |
| Channel coding theorem | Governance sparsity bound (Paper 3) |
| Channel noise | Semantic entropy rate h_s (Paper 1) |
| Channel capacity C | Semantic channel capacity C_s (CAP-001) |

**Conservation IS isolation** (from Five Research Themes / FS-001): The transformation strips away everything that isn't conserved, and what remains is the meaning. You don't need to define meaning in advance. You only need to define the transformation and the conservation constraint. Whatever survives is, by definition, the meaning.

This is the framework's deepest philosophical move and its strongest parallel to Shannon. It is also its most vulnerable point — the move only works if the transformation and conservation constraint are defined independently of the conserved quantity (the non-tautology condition, §3.4).

---

## 12. The Non-Tautology Condition (§3.4)

From Paper 0 §3.4:

> "The compression gate is not defined as 'output C(S) by construction.' It applies a lossy compression/transformation process without prior access to C(S); the commitment extractor C(.) operates in a separate canonical space and evaluates the output after transformation. Conservation is therefore an empirical claim."

**The separation:**
- The compression gate (T_gov) applies a lossy transformation — it does NOT have access to C(S)
- The commitment extractor (C(.)) operates in a separate canonical space — it evaluates the output AFTER transformation
- Conservation is the claim that the gate's output, when evaluated by the independent extractor, matches the original kernel

**Why this matters:** If the gate had access to C(S), conservation would be trivially true by construction. The non-tautology condition is that the gate and the extractor are independent — the gate doesn't know what the extractor will look for.

**Status:** The non-tautology condition is stated and is the foundation of the framework's falsifiability. But the independence is not absolute — the gate is designed to preserve deontic content, and the extractor is designed to detect deontic content. They share a design intention. The empirical question is whether this shared design intention produces real conservation or just a self-fulfilling prophecy. The EXP-003 data (where baseline NLI is higher than gate NLI) actually argues AGAINST the self-fulfilling prophecy interpretation — if the gate were designed to game the extractor, it would do better than baseline, not worse.

---

## 13. The Legal Track (the one fielded argument)

**L-000:** Six legal propositions — legal meaning carries a commitment kernel; it degrades under ungoverned AI transformation; the Conservation Law holds on legal text; existing doctrine implies a commitment conservation requirement; a CCR would formalize it; pluralism is conserved, not erased.

**L-001 (submitted to Stanford Law Review Online, May 1, 2026):** "Whose Legal Thought Stays Protected?" — the Heppner/Warner fracture on AI-assisted work product protection. The Conservation Law enters in Section VI as "materials for building" — verification infrastructure (cryptographic lineage, fidelity gates, recursion testing) that makes the functional rule's protection demonstrable, not merely doctrinal.

**Key legal distinction:** "A preserved kernel read differently by different courts is pluralism; a degraded kernel that no longer carries its original obligations is entropy." The framework is a **law of the record, not a law of interpretation.**

**The CCR (Commitment Conservation Requirement):** Any AI system applying a legal provision should demonstrate the commitment kernel has been preserved across its transformation pipeline. Not a transparency mandate (model need not be opened). A fidelity mandate. Analogous to chain of custody for physical evidence.

---

## 14. The MISC Track — 12 Disciplines

Each paper plants a flag in a field with no physics-grounded semantic fidelity framework. "The goal is not citation volume. The goal is one paper per empty room."

Key papers:
- **CL-001:** Nine failure modes taxonomy (data complete, can write now)
- **CL-002:** Three regimes of commitment stability (data complete, requires circularity fix)
- **FS-001:** Commitment kernel as new primitive in formal semantics (BLOCKED — canonical invariant formal definition)
- **GOV-001:** CT vs. Constitutional AI / NIST / EU AI Act (conceptual)
- **CAP-001:** Semantic Channel Capacity Theorem (long-term, blocked on Papers 1-5)

---

## 15. Live Implementations

- **SigRank** (signalaf.com) — privacy-preserving AI operator leaderboard
- **SIGNOMY / CIVITAE** (signomy.xyz) — governed agent marketplace under MO§ES™
- **MO§ES™** (mos2es.com) — the enforcement engine, patent-pending
- **Conservation Law repo** (github.com/SunrisesIllNeverSee/commitment-conservation) — paper, harness, experiments, corpus

---

## 16. The Rhetorical Posture

- CT is "the first AI governance framework grounded in an empirically falsifiable conservation law"
- The law is "a discovered physical law with an empirical record, a public test harness, and a patent-pending enforcement architecture"
- "This is not a recommendation. It is a discovered law."
- CT "operates as physics rather than policy"
- "Falsify it" — the standing invitation

---

## 17. My Honest Assessment of the Framework's Status

**What CT has:**
- A clearly defined conserved quantity (C(S) — deontic invariant, set-valued, discrete)
- A stated invariance principle (candidate formal definition in FS-001, not yet proven)
- An independent measurement instrument (NLI oracle, public, swappable)
- Explicit falsifiability conditions (pre-registered, publicly testable)
- A claimed empirical asymmetry (governed vs. ungoverned)
- A public test harness and corpus
- A nine-mode failure taxonomy
- A patent-pending enforcement architecture
- A 35+ paper research program spanning physics, law, and 12 disciplines

**What CT does NOT have (gaps):**
- A clean empirical asymmetry in the controlled experiment (EXP-003 baseline NLI > gate NLI)
- A formally proven invariance principle (FS-001 is a candidate, blocked)
- An information-theoretic formalization of C(S) (Papers 2, 3, CAP-001 blocked)
- A Noether-style symmetry theorem (no Lagrangian, no variational principle)
- Independent replication (all data from one operator, one oracle)
- Cross-system validation (Paper 4 planned, not executed)
- A clear provenance for the headline 0.94 number (metric mismatch with EXP-003)

**The bottom line:** CT has the structure of a conservation law — defined quantity, stated invariance, independent instrument, falsifiability conditions, empirical claims. The structure is sound. The empirical foundation is preliminary and contains a significant anomaly (the baseline-vs-gate NLI inversion in EXP-003). The formal foundation has a deep gap (C(S) info-theoretic formalization). The framework is promising but not yet established. The gap between "frame" and "law" is primarily empirical (the asymmetry needs to be clean and replicated) and formal (the invariance needs to be proven, not just stated).

---

## Ready for testing

I hold this framework as given. I know its strengths, its gaps, and its boundary conditions. Test me.
