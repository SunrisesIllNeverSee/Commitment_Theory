# Deep-Dive Loop — One Requirement at a Time

Each requirement gets its own focused session. The goal of each session is to:
1. Re-read every relevant source for that requirement
2. Identify the strongest possible answer
3. Identify what would make the answer stronger (what's missing)
4. Identify what would break the answer (what an adversary would attack)
5. Produce a clean, final answer for that requirement

The deep-dive order goes from strongest to weakest — start where the work is most solid, end where the gaps are.

---

## Session 1: Requirement 5 — Empirical Asymmetry (strongest)

**Why first:** This is CT's strongest requirement. The asymmetry is measured, replicated across configurations, and published. The 0.94 ± 0.03 vs 0.42 ± 0.12 is in the paper. The attractor test adds dynamical structure. This is where the work is most defensible.

**Questions:** Q5.1 (what is the asymmetry), Q5.2 (demonstrated empirically), Q5.3 (reproducible), Q5.4 (effect size), Q5.5 (novel predictions)

**Sources to re-read:**
- clawRxiv paper (Table 2: 0.94 ± 0.03 vs 0.42 ± 0.12, 92% vs 38%, drift rate 0.006 vs 0.058)
- EXP-003 through EXP-007 (Zenodo archives)
- RUN_LOG.md (Run 001: 55% vs 40% at depth=20)
- `run_spec_attractor.md` (governed convergence vs ungoverned drift, operator-out signal-vs-echo)
- `language_as_matter.md` (the two-layer framing, the "dead by Friday" line)
- `three_method_protocol.md` (F2-F5 falsifiers)

**What to produce:** A clean, sourced answer to all 5 questions with specific numbers, confidence intervals, and the full list of novel predictions. Identify what independent replication would look like.

---

## Session 2: Requirement 1 — Defined Conserved Quantity (strong)

**Why second:** The quantity is well-defined (deontic content), the units are clear (deontic propositions), the minimal case is identified (single modal operator), and the theory-independence argument is now strong (v2 boundary calibration — no human definition).

**Questions:** Q1.1 (what is conserved), Q1.2 (units/dimension), Q1.3 (theory-independent), Q1.4 (minimal case)

**Sources to re-read:**
- P-000 Proposition 1.3 (definition of C(S))
- FS-001 (formalization in intensional semantics)
- `three_method_extraction.py` (HARD_MODALS regex — the operational definition)
- `v2_extractor_proposal_and_stresstest.md` (definition-free calibration, the five wrong assumptions)
- `language_as_matter.md` ("the part that binds")
- von Wright 1951 / Kratzer 1991 (deontic logic — the theory-independent vocabulary)

**What to produce:** A clean answer that distinguishes between the object (deontic content — theory-independent) and the claim (it is conserved — CT-specific). Show that the v2 boundary calibration characterizes the object without defining it.

---

## Session 3: Requirement 4 — Falsifiability (strong, with honest caveats)

**Why third:** The two-layer framing is the most honest thing in the corpus. The pre-registered F2-F5 falsifiers are real. The four-way failure distinction (law failure, instrument failure, signal degeneracy, metabolic recovery) is well-developed. But the original discovery was not pre-registered, and no external party has attempted falsification.

**Questions:** Q4.1 (specific falsifying observation), Q4.2 (pre-registered), Q4.3 (anyone attempted), Q4.4 (law vs instrument failure), Q4.5 (scope boundary)

**Sources to re-read:**
- `language_as_matter.md` (two layers, two kinds of death — the key passage)
- P-000 Proposition 5.3 (falsification condition)
- `three_method_protocol.md` (F2-F5, pre-registration section)
- `v2_extractor_proposal_and_stresstest.md` (boundary calibration falsifiers)
- EXP-006 (self-referential recursion — the law described its own measurement boundary)
- EXP-007 (NP-negation — instrument failure documented)
- Deep-hugh source thread (Hawking radiation, ghost-token accounting, metabolic recovery)
- `EXPERT_NOTES.md` (Blackhole Law as G5)

**What to produce:** A clean answer that states the two-layer framing plainly, lists every falsifier with its threshold, and is honest about what is pre-registered (F2-F5) vs what is not (the original discovery).

---

## Session 4: Requirement 3 — Independent Measurement Instrument (medium, with known gaps)

**Why fourth:** The instrument exists (NLI oracle + three-method extraction). The independence argument is multi-dimensional (architecture, parameters, training, organization). The v2 boundary calibration provides definition-free external validation. But: the paper/harness oracle gap is real, EXP-007 shows a systematic blind spot, and no independent party has run the harness.

**Questions:** Q3.1 (what instrument), Q3.2 (independent of system), Q3.3 (different instrument, same result), Q3.4 (measurement uncertainty), Q3.5 (instrument failure / calibration)

**Sources to re-read:**
- Paper 0 §3.4 (Non-Tautology)
- `three_method_extraction.py` (three extractors, two NLI oracles, null model)
- `run_spec_attractor.md` (operator-out — the signal-vs-echo test, the "single most important upgrade")
- EXP-007 (NP-negation blind spot)
- `v2_extractor_proposal_and_stresstest.md` (boundary calibration as calibration standard)
- `three_method_protocol.md` (F2 null model, F5 empty-extract accounting)

**What to produce:** A clean answer that is honest about the oracle gap, the NP-negation blind spot, and the fact that the three-method validation is built but not yet run. Identify exactly what running it would prove.

---

## Session 5: Requirement 2 — Symmetry / Invariance Principle (weakest)

**Why last:** This is where CT has the most significant gap. The invariance is defined operationally (Six-Gate Protocol) and observed empirically (the asymmetry), but it is not derived from a continuous symmetry principle via a variational argument. There is no Lagrangian. The eigencommitment and attractor dynamics add structure, but they don't close the Noether gap.

**Questions:** Q2.1 (the symmetry), Q2.2 (continuous or discrete), Q2.3 (Lagrangian equivalent), Q2.4 (conservation fails when symmetry broken)

**Sources to re-read:**
- FS-001 (R_gov accessibility relation, group properties)
- Paper 3 (governance density ρ_g, threshold ρ*)
- `three_method_extraction.py` (eigencommitment — the random method's principal node)
- `run_spec_attractor.md` (attractor dynamics — the governed loop converges, ungoverned drifts)
- `language_as_matter.md` ("a lens that makes a smaller piece of physics visible — which is exactly what Lagrangian mechanics is")
- CAP-001 (semantic channel capacity — the candidate for a variational principle)
- Marcolli/Chomsky/Berwick (σ̂ as conserved quantity in syntax — the precedent)
- Semantic Noether Principle wiki page (the idea CT is missing, but as an unvalidated wiki stub)

**What to produce:** An honest answer that says: "The invariance is operational and empirical, not derived from a Noether symmetry. The Lagrangian gap is real. Here is why this might not be fatal (lepton number was conserved empirically before the Standard Model explained it). Here is what would close it (CAP-001, or a collaboration with someone like Marcolli)."

---

## After All Five Sessions

- Compile the five clean answers into a final `CT_ANSWERS_FINAL.md`
- Create a fresh `CT_SCORING_FINAL.md` blank sheet
- The final answers should be the ones an outside reviewer scores
- The score the outside reviewer gives is the real score — not my self-estimate
