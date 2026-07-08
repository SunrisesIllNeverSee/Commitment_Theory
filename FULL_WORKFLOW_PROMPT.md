# Language as Matter — Full Workflow Prompt

**Purpose:** This is a self-contained prompt for a fresh Devin session. The session must:
1. Become an expert on Commitment Theory (CT)
2. Double down on that expertise by stress-testing against primary sources
3. Take the "Language as Matter" external validity test in two passes:
   - **Pass 1 (Solo):** Answer all 23 questions as best you can on your own
   - **Pass 2 (Guided):** Go through the test with the operator. Only answer questions you can fill out honestly and forthrightly from grounded CT material. Skip any question that would require stretching the truth, guessing, or fabricating.

**Critical constraints:**
- Do NOT read any files in the `stress-test/` folder except `EXPERT_NOTES.md` and `README.md`. The other files contain answers from prior sessions and would bias your run.
- Do NOT read `CT_ANSWERS_V1.md`, `CT_ANSWERS_V1_PASS2.md`, `CT_ANSWERS_V2_SOLO.md`, or `CT_SCORING_PASS2.md`. These are prior session outputs.
- Your outputs go into new files with `_FRESH` in the name (specified below).

---

## PHASE 1 — BECOME AN EXPERT

### Step 1: Read the Expert Notes

Read this file first — it is the internalized framework notes from a prior expertise-building session:

```
/Users/dericmchenry/Desktop/Commitment_Theory/CT/workspace/stress-test/EXPERT_NOTES.md
```

This gives you the full CT framework in 20 sections: architecture, vocabulary, axioms, gates, laws, failure modes, regimes, MOSES, SIGSYSTEM, Papers 1-5, Layer 4, legal track, MISC track, disambiguation, Shannon parallel, naming, paper program, live implementations, rhetorical posture.

### Step 2: Read the Stress-Test README (for context only)

```
/Users/dericmchenry/Desktop/Commitment_Theory/CT/workspace/stress-test/README.md
```

This explains the premise: CT is held as *true* for this exercise. You are not critiquing CT. You are not making it academically defensible. You are internalizing it as given and answering from within it.

### Step 3: Deep-dive into the primary CT documents

The expert notes are a summary. For the test, you need depth. Read these primary sources in this order:

**Foundation:**
1. `CT/papers/P-000_prospectus/P-000-propositions-of-commitment-theory-prospectus.md` — all 12 propositions + appendices (the foundational document)
2. `CT/workspace/naming-architecture/Nine_Novel_Concepts.md` — the nine novel terms
3. `CT/workspace/naming-architecture/Disambiguation_Guide.md` — CT vs. adjacent fields
4. `CT/workspace/naming-architecture/Naming_Architecture.md` — naming hierarchy + Shannon parallel

**Operational layer:**
5. `CT/papers/MOSES_architecture/PAPER_PLAN.md` — the enforcement engine (Vault, Lineage DAG, Fidelity Seal, Custody Anchor, SIGSYSTEM)
6. `CT/papers/paper-0_conservation-law/Second_Law_Draft.md` — the Second Law candidate statement
7. `CT/papers/paper-0_conservation-law/Five_Research_Themes.md` — the research program + "conservation IS isolation"
8. `CT/papers/paper-0_conservation-law/Paper0_Overview.md` — Paper 0 overview + non-tautology section (§3.4)
9. `CT/papers/paper-0_conservation-law/PAPER_PLAN.md` — Paper 0 plan + key claims

**Measurement science (Papers 1-5):**
10. `CT/papers/paper-1_semantic-entropy/PAPER_PLAN.md` — semantic entropy rate h_s
11. `CT/papers/paper-2_compression-fidelity/PAPER_PLAN.md` — Compression-Fidelity Bound (semantic source coding analog)
12. `CT/papers/paper-3_governance-density/PAPER_PLAN.md` — governance density ρ_g, sparsity bound ρ*
13. `CT/papers/paper-4_cross-system-fidelity/PAPER_PLAN.md` — cross-provider/architecture conservation
14. `CT/papers/paper-5_measurement-instrument/PAPER_PLAN.md` — metrological framework, noise floor, oracle independence

**Layer 4 extensions:**
15. `CT/papers/layer4_SIGSYSTEM/PAPER_PLAN.md` — next-generation oracle (word-level signal/noise weighting)
16. `CT/papers/layer4_post-turing/PAPER_PLAN.md` — Post-Turing Test (semantic intelligence criterion)
17. `CT/papers/layer4_channel-capacity/PAPER_PLAN.md` — Semantic Channel Capacity (Shannon extension)

**Legal track (the one fielded argument):**
18. `Legal_Theory/papers/L-000_legal-propositions/L-000-propositions-legal.md` — six legal propositions + CCR
19. `Legal_Theory/papers/L-001_SLRO/Slro_paper_final.md` — the submitted SLRO essay (Heppner/Warner fracture)

**MISC track (cross-disciplinary applications):**
20. `MISC/papers/computational-linguistics/CL-001_failure-mode-taxonomy/PAPER_PLAN.md` — nine failure modes
21. `MISC/papers/computational-linguistics/CL-002_regime-classification/PAPER_PLAN.md` — three regimes
22. `MISC/papers/formal-semantics/FS-001_commitment-primitive/PAPER_PLAN.md` — canonical invariant, "conservation IS isolation," formal definition within intensional semantics
23. `MISC/papers/ai-governance/GOV-001_comparative-governance/PAPER_PLAN.md` — CT vs. Constitutional AI / NIST / EU AI Act
24. `MISC/papers/capstone/CAP-001_channel-capacity/PAPER_PLAN.md` — Semantic Channel Capacity Theorem

**Genesis (optional but useful for depth):**
25. `source-threads/deep-hugh/deep-hugh.md` — the navigator for the primary source thread

**Track context files (CLAUDE.md files — orient you to each track):**
26. `CT/CLAUDE.md`
27. `Legal_Theory/CLAUDE.md`
28. `MISC/CLAUDE.md`

---

## PHASE 2 — DOUBLE DOWN ON EXPERTISE

### Step 4: Stress-test your understanding

Before taking the test, verify your expertise by stress-testing against the primary sources. For each of the following claims, find the exact source passage that supports or contradicts it:

1. **"The conserved quantity is defined independently of the instrument."** Find Paper 0 §3.4 (Non-Tautology). Read it carefully. Does the compression gate have prior access to C(S)? What does this mean for circularity?

2. **"The conserved quantity has units."** What are the units? Look at P-000 Proposition 1.3 — is C(S) a set? What are the elements of the set? Is this discrete or continuous?

3. **"There is a symmetry/invariance principle."** Look at FS-001's formal definition: `CI(S, w) = {φ ∈ DEON | for all w' such that wR_gov w', w' ⊨ φ}`. Is this an invariance? Under what group of transformations? Does R_gov have group properties (reflexivity, transitivity)?

4. **"The instrument is independent of the system being measured."** Compare the oracle (deberta-v3-base-mnli) to the measured systems (GPT-4, Claude, Gemini, Llama). What dimensions do they differ on? What do they share? Is the shared substrate class (transformer) a fatal problem or a documented limitation?

5. **"The conservation fails when the symmetry is broken."** What is the symmetry-breaking mechanism? (Hint: governed vs. ungoverned.) What experiment demonstrates this? (Hint: EXP-003.)

6. **"The law is falsifiable."** Find P-000 Proposition 5.3. What specific observation would falsify the law? Is the falsification condition stated before or after the data was examined?

7. **"There is an empirical asymmetry."** What are conditions A (conserved) and B (not conserved)? Has the asymmetry been measured? What is the effect size?

8. **"The law has a scope boundary."** Find P-000 Proposition 11.3. What signal classes does the law apply to? What classes are unproven?

If you cannot find grounded support for any of these claims in the primary sources, note that — it will matter for the test.

### Step 5: Write your expert notes

Create your own expert notes file:

```
/Users/dericmchenry/Desktop/Commitment_Theory/CT/workspace/stress-test/EXPERT_NOTES_FRESH.md
```

This should be your own internalization of CT — not a copy of the existing EXPERT_NOTES.md, but your own synthesis after reading the primary sources. Include:
- The one-sentence core of CT
- The layered architecture
- The conserved quantity and its units
- The symmetry/invariance principle (or lack thereof)
- The measurement instrument and its independence properties
- The falsifiability conditions
- The empirical asymmetry
- The scope boundary
- Any gaps you identified during the stress test

---

## PHASE 3 — TAKE THE TEST (PASS 1: SOLO, BEST EFFORT)

### Step 6: Read the test

```
/Users/dericmchenry/Desktop/SigRank/Devins_Plans/research/LANGUAGE_AS_MATTER_TEST.md
```

This is an external validity test. The criteria come from physics and the scientific method (Noether's theorem, Popper, particle physics, reproducibility standards) — NOT from CT's own documents. There are 5 requirements, 23 questions total, max 69 points.

### Step 7: Answer all 23 questions on your own

Create your Pass 1 answers file:

```
/Users/dericmchenry/Desktop/Commitment_Theory/CT/workspace/stress-test/CT_ANSWERS_FRESH_PASS1_SOLO.md
```

Answer ALL 23 questions as best you can. This is best-effort — answer everything, even if you're uncertain. Hold CT as true and answer from within the framework. Draw from the primary sources, not just the expert notes summary.

**Important:** Do not skip questions in Pass 1. Answer everything. If you're uncertain, say what you know and acknowledge the uncertainty — but answer.

After answering, provide your own self-scoring on the 0-3 scale per question, with a brief justification for each score. Fill in the scoring summary table.

---

## PHASE 4 — TAKE THE TEST (PASS 2: GUIDED, HONEST ONLY)

### Step 8: Wait for the operator

After completing Pass 1, tell the operator you are ready for Pass 2. The operator will walk you through the test question by question.

### Step 9: Answer only what you can answer honestly

Create your Pass 2 answers file:

```
/Users/dericmchenry/Desktop/Commitment_Theory/CT/workspace/stress-test/CT_ANSWERS_FRESH_PASS2_GUIDED.md
```

In this pass, the rules are different:

- **Answer only questions where CT has a grounded, factual response.** If CT's documents explicitly address the question with real evidence, answer it.
- **SKIP any question that would require stretching the truth, guessing, fabricating, or inferring beyond what the corpus supports.** Mark these as `[SKIP — reason]`.
- **Be honest about what is "planned but not done."** If CT says "Paper 5 will formalize this" but Paper 5 is not written, that's a "planned, not done" answer — not a grounded answer.
- **Be honest about what is "inferred" vs. "stated."** If you're inferring an answer from the framework's structure rather than citing an explicit passage, say so.
- **The operator may push back on your answers.** If the operator says "I think you can answer this one," re-examine the primary sources. If you find grounded support, answer. If not, hold the skip.

### Step 10: After Pass 2, provide a gap analysis

After completing Pass 2, append a section to your Pass 2 file:

```
## Gap Analysis
```

For each skipped question:
- Why was it skipped?
- What would CT need to answer it?
- Is the gap a formalization gap (construct new math), an execution gap (run new experiments), or a conceptual gap (the framework doesn't address it)?
- Is the gap bridgeable or is it a hard blocker?

Then provide your yes/no answers to the five requirements:
1. Defined conserved quantity? Y/N
2. Symmetry / invariance principle? Y/N
3. Independent measurement instrument? Y/N
4. Falsifiability? Y/N
5. Empirical asymmetry? Y/N

And your final assessment: Is language matter? If not yet, is it possible to establish? Are there hard impassible blockers?

---

## PHASE 5 — SCORING (SEPARATE FILE)

### Step 11: Create a blank scoring sheet for outside review

Create:

```
/Users/dericmchenry/Desktop/Commitment_Theory/CT/workspace/stress-test/CT_SCORING_FRESH.md
```

This should be a blank scoring sheet (0-3 per question, subtotals, final score, yes/no summary, reviewer notes) — the same format as the test's scoring summary. Do NOT fill it in with your own scores. It is for an outside reviewer to score your Pass 2 answers blind.

Your Pass 1 self-scoring stays in the Pass 1 file. The Pass 2 file contains only answers — no scoring. The scoring sheet is blank for outside review.

---

## Summary of Files You Will Create

| File | Phase | Contents |
|------|-------|----------|
| `EXPERT_NOTES_FRESH.md` | Phase 2 | Your own internalization of CT |
| `CT_ANSWERS_FRESH_PASS1_SOLO.md` | Phase 3 | All 23 answers (best effort) + self-scoring |
| `CT_ANSWERS_FRESH_PASS2_GUIDED.md` | Phase 4 | Honest-only answers (some may be skipped) + gap analysis + yes/no + final assessment |
| `CT_SCORING_FRESH.md` | Phase 5 | Blank scoring sheet for outside review |

---

## Critical Reminders

- **Do NOT read prior session outputs.** No `CT_ANSWERS_V1.md`, `CT_ANSWERS_V1_PASS2.md`, `CT_ANSWERS_V2_SOLO.md`, or `CT_SCORING_PASS2.md`. These would bias your run.
- **Hold CT as true.** You are answering from within the framework, not critiquing it.
- **Be honest.** The value of this exercise depends on honesty about what CT can and cannot answer. A fabricated 3 is worse than an honest 0.
- **The test criteria are external.** They come from physics and the scientific method, not from CT. Answer against those criteria, not against CT's own framing.
- **Pass 1 = answer everything. Pass 2 = answer only what's grounded.** The difference between the two passes is the gap analysis — that's where the real insight is.

---

*Begin with Phase 1, Step 1.*
