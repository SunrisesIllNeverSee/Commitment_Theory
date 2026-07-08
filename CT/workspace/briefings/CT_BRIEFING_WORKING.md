# Commitment Theory — Working Briefing

*Saved 2026-07-07. Working document — questions and modifications welcome.*

---

## Commitment Theory (CT)

A falsifiable, operational framework for understanding and enforcing the preservation of deontic meaning under transformation. Built on the Conservation Law of Commitment.

## The Conservation Law of Commitment (First Law)

**C(T_gov(S)) ≈ C(S)**  *(within epsilon — see note below)*

Under governed transformation, the commitment kernel of a signal is conserved. Under ungoverned transformation, it decays monotonically (CT's Second Law of Semantic Entropy — see below).

### On the equation: ≈ not =

The formal *definition* states conservation as exact: C(T_gov(S)) = C(S). But the *empirical observation* is approximate — the commitment kernel is conserved within a measurable tolerance:

> ||C(T(S)) - C(S)||_inf < epsilon

The data shows 13 of 20 signals achieved NLI bidirectional entailment score of 1.00 across 10 recursive iterations under the gate condition. That's perfect conservation for the majority. But the law as *measured* is a double-tilde (≈), not a strict equals. The `=` is the idealization; `≈` within epsilon is what the oracle observes. The epsilon bound is what makes it falsifiable — if drift exceeds epsilon, the law fails.

### Key terms

- **Signal (S)** — a structured sequence of symbols carrying information, capable of bearing deontic content. Text, code, structured data, multimodal.
- **Transformation (T)** — a function mapping a signal to a modified signal. Lossy (compression, summarization, paraphrase) or lossless (reordering, synonym substitution).
- **Commitment kernel C(S)** — the minimal identity-preserving deontic invariant of a signal. The set of obligations, prohibitions, permissions, and modal constraints that must survive transformation for the signal to remain semantically continuous with its source. Not a summary — the irreducible core of operative meaning.
- **Governed transformation** — passes through constitutional constraints (McHenry Axioms, six-gate protocol, MO§ES™) designed to preserve the kernel.
- **Ungoverned transformation** — lacks those constraints. Subject to semantic entropy and commitment decay.
- **Fidelity** — degree to which the output kernel matches the input kernel, measured by an independent oracle (bidirectional entailment, threshold 0.85).

### Real-life example (Conservation Law)

**The bedtime story.** You tell your child a bedtime story. It takes 5 minutes one night, 60 minutes the next — you expand it, add characters, stretch the plot. The surface form changes dramatically (12x longer). But the commitment kernel — the lesson, the promise, the moral obligation embedded in the narrative — is conserved. The child receives the same deontic payload either way. The story's *meaning* is invariant under the transformation of length.

This is what C(T_gov(S)) ≈ C(S) looks like in real life: the surface changes, the kernel doesn't.

### What it's NOT (disambiguation from adjacent fields)

CT's "commitment" is a property of *signals*, not of agents, beliefs, or protocols. It must be distinguished from five established uses of "commitment" in the literature:

- **Not speaker commitment** (Brandom 1994 — discursive commitment is a property of agents in discourse; CT's commitment is a property of signals)
- **Not epistemic commitment** (CommitmentBank, de Marneffe et al. 2019 — that's about belief/factuality of embedded clauses; CT is about deontic survival under transformation)
- **Not cryptographic commitment** (Blum 1981 — that's a binding protocol for hidden values; CT's commitment is the thing being protected, not the protection mechanism)
- **Not organizational commitment** (Meyer & Allen 1991 — employee psychological attachment to an organization; no relation)
- **Not Conservation of Resources** (Hobfoll 1989 — COR uses "conservation" metaphorically for stress/motivation; CT uses "conservation" literally as a formal invariance under transformation)

### What it's NOT (the psychology commitment conversation)

This is the big one that P-000 doesn't currently disambiguate, and it should. "Commitment" has a massive literature in social and organizational psychology spanning 60+ years:

- **Kiesler (1971), *The Psychology of Commitment*** — the foundational monograph. Kiesler studied how behavior links to belief: once a person commits to a position publicly, they resist attitude change. Commitment here is a *psychological state of the agent* — the person becomes "locked in" to a belief by acting on it. 3,878 citations across Kiesler's body of work.
- **Becker (1960), "Notes on the Concept of Commitment"** — the sociological origin. Becker defined commitment as a "side bet" — extraneous interests linked to a consistent line of activity. You commit to a job not because you love it, but because quitting would cost you your pension. 40,674 citations. This is *agent-side* commitment: the person is bound by consequences.
- **Staw (1976/1981), Escalation of Commitment** — the sunk-cost fallacy formalized. People escalate commitment to a failing course of action to justify prior investment. 1,443+ citations. Again, *agent-side*: the decision-maker's behavior, not the signal's content.
- **Festinger (1957), Cognitive Dissonance** — the grandparent theory. Dissonance reduction drives commitment-consistent behavior. Brehm & Cohen (1962) narrowed it: dissonance has motivational force only when the individual is bound by *behavioral commitment* to one of the inconsistent cognitions. *Agent-side*.

**The pattern:** Every major psychology use of "commitment" is about what happens to a *person* — their beliefs, their behavior, their resistance to change, their sunk costs. CT studies what happens to a *signal* — its deontic content, its survival under transformation, its invariance across compression. The object of study is different. The psychology tradition asks: "What does commitment do to the person?" CT asks: "What does transformation do to the commitment?"

This disambiguation should be added to P-000 Proposition 2. The psychology commitment conversation is arguably the most cited body of work using the term, and CT's claim that commitment is a property of signals (not agents) is most directly in tension with it.

### Empirical support

3,950 runs, 57 signals, 181 condition-signal configurations. Governed: 13 of 20 signals achieved perfect fidelity (NLI = 1.00) across 10 recursive compression iterations despite 80%+ surface compression. Ungoverned: fidelity degrades measurably within 3 iterations, sharply by iteration 10.

### Falsifiability

Public test harness and corpus. Anyone may substitute a stronger oracle or design adversarial signals. Failure to observe conservation under governed conditions (drift exceeding epsilon) falsifies the law.

---

## The Second Law of Semantic Entropy (CT's Second Law — not thermodynamics')

**Whose second law?** This is CT's own Second Law of Semantic Entropy, proposed as a candidate law within Commitment Theory. It is *analogous to* the thermodynamic Second Law (entropy increases in an isolated system) but it is a distinct, independent claim about *semantic* degradation, not physical entropy. The analogy is explicit in the source material:

| Thermodynamics | CT |
|---------------|-----|
| First Law: Energy is conserved | First Law: Commitment is conserved under governance |
| Second Law: Entropy increases in isolated system | Second Law: Semantic entropy increases without governance |
| Third Law: Absolute zero unattainable | Candidate Third Law: Compression limit L_min below which conservation fails |

**Statement:** Under ungoverned transformation, the commitment kernel decays monotonically with each iteration. The rate of semantic entropy production is strictly positive:

> ΔH_C > 0 for each step n → n+1

Cumulative entropy after n steps scales as Ω(σ√n), where σ² is the per-step drift variance.

**Irreversibility:** Semantic entropy is irreversible without external governance. Once commitment has decayed, it cannot be recovered by further ungoverned transformation. Recovery requires re-anchoring to a canonical source or metabolism through a governed system.

**Status:** Candidate — needs formal empirical validation. The signature is visible in the data (EXP-003: NLI degrades measurably by iteration 5 under ungoverned conditions, sharply by iteration 10) but the formal statement is still being refined. Target: formalize within Paper 1 (Semantic Entropy Rate) or as a standalone short paper.

**Nine failure modes** (empirical signatures of the Second Law — each is a way deontic content decays through ungoverned transformation):

1. Obligation escalation: "may" → "shall" (modal drift)
2. Scope widening: "room A" → "any room" (quantifier drift)
3. Exception dropping: "unless undue hardship" → omitted (content loss)
4. Modal frame inversion: "shall not" → "shall" (semantic inversion)
5. Co-degraded invariance
6. NP-negation blindness
7. Formal collapse
8. Self-referential collapse
9. Lexical scope widening

### Real-life example (Second Law)

**The telephone game.** You whisper a message to someone, they whisper it to the next person, and so on. By the 10th person, the message is unrecognizable. "The rent is due Friday unless you call the landlord" becomes "The rent is free if you call the landlord." The exception clause dropped out (failure mode #3). The modal frame inverted (failure mode #4). This is ungoverned transformation — no compression gate, no fidelity verification, no lineage. The commitment kernel decays monotonically with each step. ΔH_C > 0 at every hop.

Now compare: if each person had to write down the message, verify it still contained "rent due Friday unless landlord called," and only pass it on if the kernel survived — that's governed transformation. The kernel is conserved. The First Law holds.

---

## The circuit idea (extension — not yet in P-000)

Signals as circuits. A signal opens a circuit when issued, closes when resolved. "Pay $100 by Friday" opens a circuit that closes on payment. The commitment kernel is what must survive while the circuit is open. Once resolved, the signal decays by design — that's completion, not conservation failure. The law governs what happens while the circuit is still open and under stress (transformation).

Low-density signals (e.g., "the weather is nice today") self-close — nothing lingers, nothing to resolve. High-density signals (obligations with conditions, deadlines, amounts) stay open until resolved. Law 2: low density receives low density — meaning preserves where meaning needs to preserve.

### Real-life example (circuit)

**A promise vs. a comment.** "I'll pay you back Tuesday" opens a circuit. It stays open — the commitment kernel (obligation: repay, amount: owed, deadline: Tuesday) must be preserved until Tuesday comes and the debt is settled. If someone paraphrases it as "he said he'd get you back sometime" the kernel is damaged — the deadline is gone, the amount is gone. The circuit is still open but the signal can no longer close it correctly.

Compare: "Nice weather today" — no circuit opens. There's nothing to resolve. The signal is low-density, self-closing, and conservation is trivial because there's nothing to conserve. The law doesn't need to work here. It matters where circuits stay open under stress.

---

*Source: P-000 Propositions of Commitment Theory Prospectus*
*Paper 0: DOI 10.5281/zenodo.18792459 (preprint)*
*Experimental: DOI 10.5281/zenodo.19105225*
*Patent: Serial No. 63/877,177 (Provisional)*
*Second Law draft: CT/papers/paper-0_conservation-law/Second_Law_Draft.md*
