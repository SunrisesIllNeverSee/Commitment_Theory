# FS-001 — Commitment as Canonical Invariant: A New Primitive for Formal Semantics

**Track:** MISC — Formal Semantics
**Layer:** 3 (Application)
**Status:** BLOCKED — canonical invariant formal definition must be worked out before writing begins
**Target Venue:** Linguistics and Philosophy / Journal of Semantics / Natural Language Semantics
**Est. Length:** TBD
**Dependencies:** Paper 0 published

---

## Abstract

Formal semantics has rich accounts of propositional content, illocutionary force, presupposition, and implicature — but no account of what survives transformation. This paper argues that the phenomenon CT identifies — the deontic core of a semantic object that is conserved under governed transformation — deserves status as a new primitive in formal semantics: the canonical invariant. Existing formal semantic treatments of "commitment" are uniformly epistemic and speaker-relative. Brandom's inferentialism treats commitment as a score in a language game. Walton and Krabbe's dialogue theory treats commitment as a position a speaker incurs through speech acts. de Marneffe et al.'s CommitmentBank treats commitment as an author's epistemic attitude toward an embedded proposition. Saurí and Pustejovsky's FactBank treats commitment as an event's factual status in a text. All of these are properties of speakers or authors relative to propositions; none is a property of the semantic object itself. CT's commitment kernel is categorically distinct: it is a property of signals — the deontic content that the signal carries — independent of any speaker, extractable by a measurement oracle, and conserved under governed transformation. One sentence separates them: all existing uses treat commitment as a property of speakers (epistemic); CT treats it as a property of signals (deontic). This paper formalizes CT's commitment kernel as a canonical invariant, places it within the intensional semantics framework (possible worlds, accessibility relations, deontic modality), and argues that its conservation under transformation reveals something fundamental about semantic structure — that meaning has an invariant core that can be isolated by the act of transformation, without requiring a prior definition of meaning in general.

---

## Outline

I. **Introduction: What Formal Semantics Lacks** — Argues that formal semantics has not needed an account of what survives transformation because it has not modeled AI transformation as a semantic process; CT's empirical program makes this gap consequential.

II. **Existing Treatments of Commitment in Formal Semantics** — Reviews Brandom, Walton & Krabbe, CommitmentBank, FactBank, and related frameworks; demonstrates that all treat commitment as an epistemic property of speakers.

III. **The Categorical Distinction** — Provides the single-sentence disambiguation: CT's commitment kernel is a property of signals (deontic), not speakers (epistemic); elaborates the distinction formally and illustrates it with examples.

IV. **The Canonical Invariant: Formal Definition** — Defines the canonical invariant within the intensional semantics framework; characterizes it as the deontic content that is accessible across all transformation-related possible worlds in the governed transformation relation.

V. **Conservation as Isolation** — Develops the key insight: conservation IS isolation; the canonical invariant is identified by the act of transformation, not defined prior to it; connects this to Shannon's sidestepping of "what is information?" by defining it as what survives the channel.

VI. **Implications for Formal Semantics** — Discusses the canonical invariant's relationship to existing primitives (propositional content, illocutionary force, presupposition); argues it is genuinely novel and not reducible to any existing primitive.

VII. **Conclusion: An Invitation to Formal Semantics** — Invites formal semanticists to engage CT's empirical program; identifies the most important theoretical extensions.

---

## Key Claims

- CT's commitment kernel is a property of signals (deontic content), not speakers (epistemic attitude) — a categorical distinction from all existing formal semantic treatments of "commitment."
- The canonical invariant is the formal primitive that CT's empirical program reveals: the deontic content of a semantic object that is conserved under governed transformation, identifiable by the act of transformation itself.
- Conservation IS isolation: the canonical invariant is not defined prior to transformation but revealed by it — the same move Shannon made when he defined information as what survives the channel.
- The canonical invariant is not reducible to propositional content, illocutionary force, presupposition, or any existing formal semantic primitive; it deserves status as a new primitive in formal semantics.
- Formal semantics' intensional framework (possible worlds, accessibility relations, deontic modality) provides the right tools for formalizing the canonical invariant; no new formal machinery is required.

---

## Writing Notes

**FS-001 is the canonical treatment of the Shannon "conservation IS isolation" analogy for the entire CT program:**
Every other paper that invokes this analogy (CL-001, COM-001, CAP-001) should cite FS-001 for it — not develop it independently. FS-001 must develop the analogy formally and completely. The other papers get one sentence and a citation.

The formal statement of the analogy:
Shannon defined information as what survives the noisy channel — he did not need a prior definition of "information" to build information theory. CT defines commitment as what survives the governed transformation — it does not need a prior definition of "meaning" to build the measurement framework. The canonical invariant CI(S,w) is isolated by the act of transformation, not defined prior to it.

**Semantic minimalism / contextualism (add to Section IV or VI):**

- Borg's minimal semantics: sentence meaning is fixed by grammar + lexicon; context contributes only to pragmatics. CT's canonical invariant is closer to Borg's minimal content than to context-enriched content — CI(S,w) captures what the sentence commits to by its deontic structure, independent of speaker context. This is a useful ally for FS-001's claims.
- Recanati's contextualism: sentence meaning requires pragmatic enrichment to determine truth conditions. CT's challenge: negation reversal (EXP-007) shows that surface-level pragmatic enrichment cannot recover the commitment kernel once it is lost — supporting the claim that CI(S,w) is a real semantic object, not a pragmatic inference.

**Engage Floridi, Barwise & Perry, and Dretske (Section IV or VI):**
These are the most likely objections from philosophy of information and formal semantics reviewers:
- Floridi's General Definition of Information (Φ): defines meaningful, well-formed data. CT's commitment kernel is not "meaningful data" in Floridi's sense — it is specifically deontic content. Floridi's GDI does not address transformation or conservation. One sentence distinguishes them.
- Barwise & Perry (1983) situation theory: proposes "situations" as truth-makers; the canonical invariant could be read as a special case of situation-theoretic constraints. Distinguish: situation theory characterizes what makes propositions true; CT characterizes what survives transformation. Different problems.
- Dretske (1981) information theory: defines information in terms of what a signal carries. CT's commitment kernel is closer to Dretske's "informational content" than to Floridi's GDI, but CT adds the conservation law and operational measurement. Engage Dretske as an intellectual ancestor — CT provides what Dretske's framework lacked (an operational measurement protocol and a discovered conservation law).

**Non-reducibility proof sketch (Section VI):**
For each existing primitive, provide a distinguishing case:

- Not propositional content: a sentence with the same propositional content can have different CI (a factual assertion vs. a legal obligation with the same surface truth conditions)
- Not illocutionary force: two sentences with the same force (both directives) can have different CI (one carries "shall not" with an exception clause; one carries "should not" — different CI under CT)
- Not presupposition: presuppositions are speaker-relative and defeasible; CI is signal-relative and preserved under governed transformation

## Blocking Gap — Formal Definition Must Exist Before Writing

The entire paper rests on Section IV. Until the canonical invariant has a workable formal definition, writing cannot begin.

**Candidate definition (to be confirmed or revised):**

Let W be a set of possible worlds and let T_gov be a governed transformation that induces an accessibility relation R_gov on W, where wR_gov w' iff w' is reachable from w via a transformation satisfying the Six-Gate Protocol.

The canonical invariant of a semantic object S at world w is:

CI(S, w) = {φ ∈ DEON | for all w' such that wR_gov w', w' ⊨ φ}

where DEON is the set of deontic propositions (obligations, prohibitions, permissions, modal constraints) expressible in the object language.

In plain terms: CI(S, w) is the set of deontic propositions that hold in every world reachable from w via a governed transformation of S. It is the deontic content that survives all governed transformations — the invariant core.

**Why this definition works:**
- It is entirely within the intensional semantics framework — no new formal machinery required
- It connects directly to deontic modality (von Fintel, Kratzer): deontic operators (shall, must, may not) scope over accessible worlds; CI(S,w) is the intersection of the deontic extensions across all governed-transformation-accessible worlds
- It recovers the CT empirical result: EXP-003's NLI=1.00 result means the NLI oracle is detecting logical entailment in both directions — consistent with CI(S,w) being preserved across transformations
- It makes the non-reducibility argument tractable: CI(S,w) ≠ propositional content (which spans all worlds, not just governed-transformation-accessible ones), ≠ presupposition (which is speaker-relative), ≠ illocutionary force (which is act-relative)

**What still needs to be confirmed before writing:**
1. Does the definition recover the failure modes correctly? (Exception dropping = a deontic proposition exits CI(S,w) after ungoverned transformation — check this formally)
2. Does R_gov satisfy the right modal axioms? (Reflexivity is guaranteed by identity transformation; transitivity corresponds to composability of governed transformations — both should hold by the Six-Gate Protocol design)
3. Is DEON separable from the non-deontic content in natural language? (The claim is that it is — this is the empirical claim Paper 0 supports, and FS-001 should reference EXP-007 as evidence)

**Decision gate:** Confirm or revise the definition above. Run it through one example (a legal provision with a "shall not unless" exception). If it correctly identifies the exception as part of CI(S,w) and correctly predicts that exception dropping produces a world where CI(S,w') ≠ CI(S,w), the definition is workable. Then begin writing.

---

## Citation Notes

- **Cites:** Paper 0 (Conservation Law, commitment kernel definition, empirical record); P-000 (CT definitions, disambiguation table); Brandom, *Making It Explicit*; Walton & Krabbe, *Commitment in Dialogue*; de Marneffe et al. CommitmentBank; Saurí & Pustejovsky FactBank; von Fintel (deontic modality); Kratzer (modality in natural language); Shannon (1948) (for the isolation analogy)
- **Cited by:** FS-002 (philosophy of language extension); CL-001 (failure taxonomy uses formal semantic framework from FS-001); CAP-002 (monograph formal semantics chapter)
