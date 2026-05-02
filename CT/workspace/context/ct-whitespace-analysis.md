# Commitment Theory: Whitespace Analysis and Naming Strategy

**Date:** April 15, 2026
**Purpose:** Map every term in the framework against existing usage, identify collisions, and establish clean whitespace for "Commitment Theory" (CT) as the primary name.

---

## COR vs CT: Why "Commitment Conservation Theory" Is the Wrong Brand

| Dimension | COR (Hobfoll, 1989) | CT (McHenry, 2026) |
|---|---|---|
| **Full name** | Conservation of Resources Theory | Commitment Theory / Conservation Law of Commitment |
| **Domain** | Organizational psychology, stress research | Information theory, semantics, AI governance, law |
| **What is conserved** | Psychological resources (self-esteem, energy, status, objects) | Deontic kernel of a signal (obligations, prohibitions, permissions) |
| **Conservation means** | People are motivated to protect resources from loss | A formal invariant quantity survives governed transformation |
| **Type of claim** | Behavioral model — describes human motivation under stress | Conservation law — describes invariance under transformation |
| **Empirical method** | Surveys, longitudinal studies, meta-analyses | Controlled transformation experiments, harness-based falsification |
| **Falsifiable?** | Loosely — principles are directional, not invariant | Yes — C(T_gov(S)) = C(S) is a binary pass/fail |
| **Citation count** | 19,000+ (Hobfoll 1989 alone) | Pre-publication |
| **Abbreviation** | COR | CT (not CCT) |

COR uses "conservation" metaphorically — people try to conserve resources the way you'd try to conserve money. It's a behavioral tendency, not a physical invariance. CT uses "conservation" literally — commitment is conserved under governed transformation the way energy is conserved under physical transformation. Same word, categorically different claims. But anyone searching "commitment conservation" will hit COR first because it has 19,000 citations and 35 years of institutional weight.

**The fix:** The theory is **Commitment Theory (CT)**. The law inside it is the **Conservation Law of Commitment**. The abbreviation is CT, never CCT. "Conservation" appears in the name of the law, not in the name of the theory. This separates you from COR at the brand level while preserving the physics-grade claim at the law level.

---

## Full Whitespace Map: Every Term

### CLEAN — Yours, no collision

| Term | Status | Notes |
|---|---|---|
| **Commitment kernel** | No prior use anywhere | Fully novel. No results in any field. |
| **Conservation Law of Commitment** | No prior use | The full phrase returns nothing. The claim is unique. |
| **Governed transformation** | No prior use in this sense | "Governed" appears in governance literature but never as a formal property of a transformation class. |
| **Ungoverned transformation** | No prior use | Novel framing. |
| **Commitment Theory (CT)** as information-theoretic framework | No collision with same meaning | "Commitment theory" appears in organizational psychology (Meyer & Allen, 1991 — employee commitment) but refers to why employees stay at organizations. Completely different domain, different object, different question. Disambiguation is trivial: one is about employee loyalty, the other is about signal invariance. |
| **Failure mode taxonomy** (obligation escalation, scope widening, exception dropping, modal frame inversion) | No prior formal taxonomy | Individual phenomena recognized informally in translation studies and legal drafting. Nobody has taxonomized them as failure modes of a conservation law. |
| **Commitment Governance Test (CGT)** | No prior use | Clean. |
| **Fidelity seal** | No prior use in this sense | "Fidelity" appears in audio/signal processing but "fidelity seal" as a governance certification is novel. |
| **Signal integrity** (as applied to meaning) | Novel application | The term exists in electrical engineering (Eric Bogatin). Applying it to semantic content is a deliberate bridge, not a collision. |

### NEEDS DISAMBIGUATION — Shared word, different meaning

| Term | Collision With | Severity | Action Required |
|---|---|---|---|
| **"Commitment"** | Brandom's discursive commitment (philosophy, 1994) | HIGH | Brandom: commitment = inferential obligation undertaken by a speaker. CT: commitment = deontic kernel of a signal independent of speaker. One is a property of agents. The other is a property of signals. State this distinction in P-000 §2. |
| **"Commitment"** | Walton & Krabbe commitment stores (dialogue logic, 1995) | MEDIUM | W&K: commitment = proposition a dialogue participant has accepted, tracked in a public store. CT: commitment = the irreducible binding content of a signal that must survive transformation. W&K tracks what agents accept. CT tracks what signals obligate. State in P-000. |
| **"Commitment"** | NLP CommitmentBank (de Marneffe et al., 2019) | MEDIUM | CommitmentBank: measures speaker commitment to factuality of embedded clauses. CT: measures whether the deontic kernel of a signal survives transformation. One is epistemic stance detection. The other is deontic invariance testing. Disambiguate in CL-001. |
| **"Commitment"** | Frazier & Rayner "Taking on Semantic Commitments" (psycholinguistics, 1990) | LOW | F&R: "commitment" = point at which a reader commits to one interpretation of an ambiguous word. CT: commitment = the kernel that must be preserved. Different question entirely. Footnote in FS-001 if needed. |
| **"Commitment"** | Cryptographic commitment schemes (Blum, 1981; ABBA, 2026) | LOW for CT users, HIGH for search engines | Cryptographic commitment: a protocol for hiding and later revealing a value. CT commitment: the deontic kernel to be preserved. Cryptographic commitment is the tool. CT commitment is the thing being protected. Already separated in your research notes. State formally in P-000. |
| **"Commitment"** | Meyer & Allen organizational commitment (1991) | LOW | Employee commitment to organizations. Completely different domain. No real confusion risk except in title-level search results. |
| **"Semantic continuity"** | Software engineering (database schema migration) | LOW | Different domain, different meaning. Risk is only in search results. Use as plain-language synonym in legal papers with a footnote clarifying your usage. |
| **"Commitment conservation"** as search phrase | Hobfoll COR theory (1989) | VERY HIGH | COR dominates this search space with 19,000+ citations. Never use "commitment conservation" as a standalone phrase. Always use "Conservation Law of Commitment" (full phrase) or "Commitment Theory." |
| **"Semantic entropy"** | Kuhn et al. "Semantic Uncertainty" (NeurIPS 2023) | MEDIUM | Kuhn: uncertainty in LLM outputs measured by semantic clustering. CT: entropy rate of deontic decay under transformation. Different quantities measured differently. Disambiguate in IS-001. |
| **"Conservation"** applied to meaning | Nothing — clean | N/A | No one has applied the concept of conservation (physics sense) to meaning. This is novel. State the claim in the Zenodo preprint. |

### BORROWED VOCABULARY — Acknowledged, not disambiguated

| Term | Source | Your Usage | Action |
|---|---|---|---|
| Obligations, prohibitions, permissions | Deontic logic (von Wright, 1951) | Standard deontic categories used as components of the commitment kernel | Acknowledge in P-000 §1. CT does not reinvent deontic categories. It asks a new question: are they conserved? |
| Signal | Shannon (1948) | Unit of analysis — a structured carrier of meaning | One sentence in preprint: "We use 'signal' rather than 'text' or 'utterance' to frame language as an information-theoretic object subject to transformation, compression, and measurement." |
| Entropy rate | Shannon (1948) | Applied to the rate of deontic decay under ungoverned transformation | Standard information-theoretic concept applied to a novel domain. No disambiguation needed, just citation. |
| Transformation | Linear algebra, category theory | Any operation that changes a signal's form while potentially preserving or destroying its kernel | Standard mathematical concept. No disambiguation needed. |
| Substrate-agnostic | Materials science, software engineering | The conservation law holds regardless of whether the transformation is human, AI, or hybrid | Common descriptor. No disambiguation needed. |

---

## Naming Architecture

| Level | Name | Abbreviation | Usage |
|---|---|---|---|
| **The theory** | Commitment Theory | CT | All papers, all contexts. Primary brand. |
| **The law** | Conservation Law of Commitment | CLC | Formal scientific claim. Appears inside CT. |
| **The equation** | C(T_gov(S)) = C(S) | — | Technical papers only. |
| **The kernel** | Commitment kernel | CK | The conserved quantity. |
| **The test** | Commitment Governance Test | CGT | The five-stage evaluation protocol. |
| **The harness** | Commitment Conservation Harness | CCH | The empirical testing tool. |
| **The framework** | MO§E§™ | — | The governance enforcement architecture built on CT. |
| **Plain-language synonym** | Semantic continuity | — | Legal papers, policy papers. Defined as equivalent to commitment conservation in legal contexts. |

**Never use "CCT" as an abbreviation.** It collides with too many existing acronyms and invites confusion with COR. CT is clean.

---

## Disambiguation Paragraphs Needed

### For P-000 / Zenodo Preprint (§2 or equivalent)

"The term 'commitment' is used in several distinct academic traditions. In the philosophy of language, Brandom (1994) defines commitment as the inferential obligations a speaker undertakes by making an assertion — a property of agents in discourse. In dialogue logic, Walton and Krabbe (1995) formalize commitment as propositions a participant has accepted, tracked in a public commitment store — a property of dialogue states. In cryptography, a commitment scheme (Blum, 1981) is a protocol allowing a party to bind themselves to a hidden value — a property of protocols. In organizational psychology, commitment refers to an employee's attachment to their organization (Meyer & Allen, 1991) — a property of persons. None of these uses the term as it is used here. In Commitment Theory, commitment is a property of signals — the minimal, identity-preserving deontic kernel comprising a signal's obligations, prohibitions, permissions, and modal constraints. The question CT asks is whether this kernel is conserved under transformation. This question has not been asked in any of the traditions listed above."

### For Legal Papers (L-001 onward)

"This Essay uses 'commitment' to refer to the operative core of a legal signal — the obligations, prohibitions, and permissions it creates. This usage draws on deontic logic (von Wright, 1951) for its categories but asks a distinct question: whether the deontic content of a legal standard survives the transformation from statute to system output. The term 'semantic continuity' is used interchangeably as a plain-language descriptor."

### For Computational Linguistics Papers (CL-001 onward)

"Commitment Theory (CT) is distinct from the NLP CommitmentBank (de Marneffe et al., 2019), which measures speaker commitment to the factuality of embedded clauses. CT does not measure epistemic stance. It measures whether the deontic kernel of a signal — its binding obligations and constraints — is preserved through transformation. The CommitmentBank asks what a speaker believes. CT asks what a signal obligates."

---

## Search Collision Matrix

What happens when someone searches for your work:

| Search Term | What They'll Find | CT Visibility |
|---|---|---|
| "commitment theory" | Meyer & Allen (org psych) dominates | LOW until you publish and get citations |
| "commitment conservation" | Hobfoll COR dominates | ZERO — avoid this phrase |
| "conservation law of commitment" | Nothing currently | HIGH — this phrase is yours |
| "commitment kernel" | Nothing | HIGH — this phrase is yours |
| "semantic commitment" | Frazier & Rayner, NLP factuality | MEDIUM — need to outrank with citations |
| "commitment conservation theory" | Hobfoll COR first, then nothing | LOW — avoid this as brand name |
| "deontic conservation" | Nothing | HIGH — consider using as secondary descriptor |
| "signal commitment preservation" | Nothing | HIGH — potential keyword |
| "meaning preservation law" | Nothing relevant | HIGH — potential keyword |
| "commitment invariance" | Nothing | HIGH — potential keyword |

**SEO strategy:** Your discoverable phrases are "Conservation Law of Commitment," "commitment kernel," "deontic conservation," and "commitment invariance." These return zero results today and will be entirely yours once published. Seed these phrases in titles, abstracts, and keywords across all papers.

---

## Final Assessment

"Commitment Theory" has clean whitespace. The core claim — that the deontic kernel of a signal is a conserved quantity under governed transformation — has no precedent in any field. The individual terms borrow from established traditions (deontic logic, information theory, speech act theory) but the combination and the conservation question are novel.

The naming collision with Meyer & Allen's organizational commitment is real but trivially disambiguated by domain. The search collision with Hobfoll's COR is severe but only affects the phrase "commitment conservation" — which you should never use as a standalone brand.

The theory is CT. The law is the Conservation Law of Commitment. The kernel is yours. The taxonomy is yours. The question is yours. The clean space exists. Occupy it.
