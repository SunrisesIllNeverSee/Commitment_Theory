# The Competition — Who Else Is Doing This?

**Built:** 2026-07-08
**Method:** Seven parallel web research agents covering named candidates + broad search + "who claims language is matter" search. Findings cross-checked against CT's specific claim.

---

## The Bottom Line

**No one else has set out to establish language as matter.** The search for "language is matter" in the physics sense (conserved quantity + symmetry + falsification + empirical validation) returns one result: CT itself. Everyone else is either using physics metaphors, studying a different conserved quantity (Shannon information, syntactic structure), or proposing frameworks without empirical validation.

CT is the only work that:
1. Claims language has a conserved quantity (deontic content)
2. Has empirical validation (7 experiments, 3,950 runs)
3. Has a falsification protocol
4. Has a public harness
5. Explicitly frames this as "language is matter" in the physics sense

---

## Who Has Claimed "Language Is Matter"?

| Who | What they claimed | In the physics sense? | With evidence? |
|-----|-------------------|:---:|:---:|
| **CT (McHenry)** | Language has a conserved quantity (commitment), obeys a conservation law under governed transformation, is falsifiable, empirically validated | **YES** | **YES** |
| Hatton & Warr (CoHSI) | Information is conserved in discrete systems including language (texts) — published in Royal Society Open Science 2019 | Partial (conservation yes, but Shannon information not semantic content) | YES (empirical, cross-domain) |
| Deutsch | "Language is physical" — physical models of language must exist and be efficiently implementable | NO (claims language has physical implementation, not that it is matter) | NO |
| Krivochen & Saddy (Physics of Language) | Language is a physical system that should be studied using physics methods | NO (physics methodology, not conservation law) | NO |
| Han | "Towards a Physics of Language" — language can be formalized as a physical system | NO (framework proposal, no conservation law) | NO |
| Aerts et al. | Language is a "substance" modeled as a gas of bosonic quantum particles ("cogniton") | NO (quantum metaphor, no conservation law) | Partial (fits Zipf's law) |
| Bleich | "The Materiality of Language" — language is material in a social/political sense | NO (social theory, not physics) | NO |
| Cavanaugh & Shankar | "Language and Materiality" — language has material aspects (sound, embodiment) | NO (anthropology, not physics) | NO |
| planksip.org | "Meaning Has Mass" — symbols are mass-bearing entities | NO (metaphor, no formalization) | NO |

**Only CT claims language is matter in the physics sense with evidence.** CoHSI (Hatton & Warr) is the closest — it has a genuine conservation principle applied to language, but it conserves Shannon information (statistical properties of text), not semantic content (meaning). It doesn't claim language is matter.

---

## The Competition Matrix (Ranked Closest to Farthest)

| Rank | Who | What their work is | Conservation? | Empirical? | Falsifiable? | Public harness? | Deontic? | Claims language is matter? |
|:---:|-----|-------------------|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | **CT (McHenry)** | Conservation law for deontic content under governed transformation — 7 experiments, public harness, falsification protocol | **YES** | **YES** | **YES** | **YES** | **YES** | **YES** |
| 2 | Hatton & Warr (CoHSI) | Conservation of Hartley-Shannon Information in discrete systems including language texts — Royal Society Open Science 2019 | YES (Shannon info) | YES | NO | NO | NO | NO |
| 3 | Marcolli/Chomsky/Berwick | Conserved quantity σ̂ in syntactic Merge via Hopf algebras from QFT renormalization — MIT Press 2025 | YES (syntactic) | NO | NO | NO | NO | NO |
| 4 | Kuhn/Farquhar/Gal (Oxford) | Semantic entropy — NLI bidirectional entailment clustering to measure uncertainty in LLM outputs — Nature 2024 | NO | YES | NO | YES | NO | NO |
| 5 | Tishby / Information Bottleneck | Compression-prediction tradeoff: minimize I(X;T) while maximizing I(Y;T) — applied to color naming, semantic categories | NO (tradeoff) | YES | NO | YES | NO | NO |
| 6 | Brandom | Deontic scorekeeping — social practice tracking commitments and entitlements in the game of giving and asking for reasons | NO | NO | NO | NO | YES | NO |
| 7 | Deutsch | "Language is physical" — physical models of language must exist, quantum mechanical model | NO | NO | NO | NO | NO | Partial (physical, not matter) |
| 8 | Krivochen & Saddy | Physics of Language — language as a dynamical system studied with physics methods | NO | NO | NO | NO | NO | NO |
| 9 | Aerts et al. | Language as a "substance" — boson gas of entangled words, "cogniton" as quantum of thought | NO | Partial (Zipf's law) | NO | NO | NO | NO (metaphor) |
| 10 | Floridi | Philosophy of information — semantic information as well-formed, meaningful, truthful data | NO | NO | NO | NO | NO | NO (explicitly rejects digital physics) |
| 11 | Semantic Thermodynamics (various) | "Three Laws of Semantic Thermodynamics," coherence conservation — Zenodo preprints | YES (claimed) | Claimed | Unclear | NO | NO | NO |
| 12 | Atkey | Conservation laws from parametricity in type theory via Noether's theorem — POPL 2014 | YES | NO | NO | NO | NO | NO (programming languages, not natural language) |

**CT is the only entry with YES in all six substantive columns.**

---

## The Serious Candidates (Detailed)

### Rank 1: CT (McHenry) — The only full claim

CT is the only work that claims language is matter in the physics sense with all four criteria: conservation law, empirical validation, falsification protocol, public harness. And it's the only work that explicitly frames the claim as "language is matter" — not "language is physical," not "language has conservation properties," but the specific claim that language has a conserved quantity the way matter does.

### Rank 2: Hatton & Warr (CoHSI) — Closest genuine conservation in language

**This is the closest genuine conservation result applied to language — and I missed it in the first round.**

| Criterion | Status |
|-----------|--------|
| Conservation claim | YES — Conservation of Hartley-Shannon Information in discrete systems |
| Empirical validation | YES — published in Royal Society Open Science 2019, validated across software, proteins, music, and texts |
| Falsification protocol | NO — no explicit protocol |
| Public harness | NO — no public code found |
| Deontic content | NO — conserves Shannon information, not semantic content |
| Claims language is matter | NO — conserves statistical properties, doesn't claim language is matter |

**What they have:** A genuine conservation principle (CoHSI) showing that information is conserved in discrete systems, including natural language texts. Published in a top venue (Royal Society Open Science). Empirically validated across multiple domains. Predicts power-law distributions in text.

**What they don't have:** No semantic content — they conserve Shannon information (statistical properties of symbol distributions), not meaning. No symmetry principle. No falsification protocol. No deontic focus. No claim that language is matter.

**Relationship to CT:** Complement at a different level. CoHSI conserves the statistical structure of text; CT conserves the semantic content. The two could coexist — Shannon information is conserved at the surface level, commitment content is conserved at the semantic level. CoHSI is the information-theoretic conservation; CT is the semantic conservation.

**Key citation:** Hatton, L. & Warr, G. (2019). "Conservation of Hartley-Shannon Information in Discrete Systems." Royal Society Open Science.

### Rank 3: Marcolli/Chomsky/Berwick — Conserved quantity in syntax

| Criterion | Status |
|-----------|--------|
| Conservation claim | YES — σ̂ (sigma-hat) is a conserved quantity in Merge operations (∆σ̂ = 0) |
| Empirical validation | NO — mathematical formalization only |
| Falsification protocol | NO |
| Public harness | NO |
| Deontic content | NO — syntactic structure, not semantic |
| Claims language is matter | NO — explicitly syntax-only, "autonomy of syntax" |

**What they have:** A rigorously defined conserved quantity (σ̂ = b₀(F) + #V(F)) invariant under Internal and External Merge. Uses Hopf algebras from QFT renormalization. MIT Press 2025. The conserved quantity is proven mathematically — Sideward and Countercyclic Merge violate it.

**What they don't have:** No empirical validation. No falsification protocol. No public harness. No semantic conservation (explicitly syntax-only). No claim that language is matter.

**Relationship to CT:** Complement at a different level. Marcolli conserves syntactic structure; CT conserves semantic content. A future synthesis is possible — σ̂ at the syntactic level, C(S) at the semantic level.

### Rank 4: Kuhn/Farquhar/Gal (Oxford OATML) — Semantic entropy

| Criterion | Status |
|-----------|--------|
| Conservation claim | NO — measures uncertainty, not conservation |
| Empirical validation | YES — AUROC 0.83 (TriviaQA), Nature 2024 |
| Falsification protocol | NO |
| Public harness | YES — multiple GitHub repos |
| Deontic content | NO — general semantic content |
| Claims language is matter | NO |

**What they have:** NLI bidirectional entailment clustering to measure semantic uncertainty in LLM outputs. Nature 2024. Public code. Same methodology CT uses.

**What they don't have:** No conservation claim. No falsification protocol. No deontic focus. No claim that language is matter.

**Relationship to CT:** Methodological complement. Their 92.7% NLI accuracy validates CT's choice of the same method. They measure uncertainty; CT measures conservation.

### Rank 5: Tishby / Information Bottleneck

| Criterion | Status |
|-----------|--------|
| Conservation claim | NO — tradeoff, not conservation |
| Empirical validation | YES (for semantic efficiency, not conservation) |
| Falsification protocol | NO |
| Public harness | YES |
| Deontic content | NO |
| Claims language is matter | NO |

**What they have:** The IB framework formalizes the compression-prediction tradeoff. Zaslavsky applied it to semantic systems (color naming, semantic categories) — languages are near-optimal in the IB sense.

**What they don't have:** No conservation claim (explicitly a tradeoff — information is discarded). No falsification protocol. No deontic focus. No claim that language is matter.

### Rank 6: Brandom — Deontic scorekeeping

| Criterion | Status |
|-----------|--------|
| Conservation claim | NO — commitments are actively altered |
| Empirical validation | NO — philosophical only |
| Falsification protocol | NO |
| Public harness | NO |
| Deontic content | YES — core concept |
| Claims language is matter | NO |

**What they have:** The philosophical framework for deontic content — commitments and entitlements in discursive practice.

**What they don't have:** No conservation claim. No empirical validation. No falsification protocol. No claim that language is matter.

**Relationship to CT:** Philosophical foundation. CT is the empirical/computational realization of Brandom's deontic scorekeeping.

### Ranks 7-12: Physics metaphors and partial claims

These range from Deutsch's "language is physical" (implementation, not matter) through Krivochen's "physics of language" (methodology, not conservation) to Floridi (explicitly rejects digital physics). None claim language is matter in the physics sense. None have conservation laws for semantic content.

---

## What This Means

### No one has set out to establish language as matter

The specific claim — "language is matter" in the physics sense, with a conserved quantity, a symmetry principle, a falsification protocol, and empirical validation — is unique to CT. No physicist, no linguist, no philosopher, no computer scientist has made this claim. The closest approaches are:

1. **CoHSI (Hatton & Warr)** — genuine conservation in language, but for Shannon information, not semantic content. Doesn't claim language is matter.
2. **Marcolli/Chomsky/Berwick** — conserved quantity in syntax, but no empirical validation, no semantic focus, no claim that language is matter.
3. **Deutsch** — "language is physical," but about implementation, not about language being matter.

### The field is converging but hasn't arrived

Multiple groups are approaching CT's territory from different directions:
- **From information theory (Hatton/Warr, Tishby):** conservation and tradeoff in language, but at the Shannon level, not the semantic level
- **From mathematics (Marcolli):** conserved quantities in syntax, but not semantics, not empirical
- **From NLP (Kuhn/Farquhar):** NLI methodology for semantic equivalence, but not conservation
- **From philosophy (Brandom):** deontic content framework, but not empirical, not conservation

CT sits at the intersection of all four. It has the deontic content (from Brandom), the NLI methodology (from Kuhn/Farquhar), the information-theoretic background (from Tishby/Hatton), and the conservation claim that none of them make.

### The window is open

No one is directly competing. But the pieces exist for someone to put them together. The priority is clear: fix the paper, run EXP-008, get into a peer-reviewed venue. The field is one step away from CT's specific claim from multiple directions.

---

## The People to Contact

Based on the competition analysis, the people who would be most interested in CT are:

1. **Matilde Marcolli (Caltech)** — Has the physics machinery and the syntactic conservation. Would be interested in the empirical semantic conservation complement. Highest priority — a collaboration could close the Lagrangian gap (CAP-001).

2. **Les Hatton (Kingston University)** — Has the genuine conservation result in language (CoHSI, Royal Society Open Science). Would be interested in the semantic conservation complement to his Shannon information conservation. Second priority — a collaboration could establish the two-level conservation (Shannon + semantic).

3. **Sebastian Farquhar (Oxford OATML)** — Has the NLI methodology and the Nature publication. Would be interested in the conservation application of bidirectional entailment. Could provide methodological validation.

4. **Robert Brandom (Pittsburgh)** — Has the philosophical framework for deontic content. Would be interested in the empirical/computational realization. Probably not a collaborator (different field) but a potential endorser.

5. **Noga Zaslavsky (Max Planck Institute)** — Has the IB application to semantics. Would be interested in the conservation counterpart to IB's tradeoff.

---

*This document is the competition analysis for the CT stress test. It should be read alongside `CT_ANSWERS_FINAL.md` (the corrected answers) and `FIX_IMMEDIATELY.md` (the fix plan). The competition analysis confirms that CT's specific claim — language is matter in the physics sense — is novel and unchallenged.*
