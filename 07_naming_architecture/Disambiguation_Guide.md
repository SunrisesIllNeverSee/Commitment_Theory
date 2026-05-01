# Disambiguation Guide — Commitment Theory vs. Adjacent Fields

**Purpose:** Pre-written disambiguation paragraphs for each major paper.
**Source:** Session analysis, April 14–15, 2026

---

## Standard Disambiguation Paragraph (Short Form)
*Use in footnote or brief note when introducing "commitment" in CT context.*

> "Commitment" in Commitment Theory (CT) refers to the minimal deontic kernel of a signal — its obligations, prohibitions, permissions, and modal constraints. This usage is distinct from commitment in philosophy of language (Brandom's inferential obligations of speakers), dialogue logic (Walton & Krabbe's commitment stores), NLP (speaker factuality stance in CommitmentBank), cryptography (commitment schemes), and organizational psychology. CT studies what signals themselves obligate, not what speakers believe or promise.

---

## 1. Brandom — Discursive Commitment (Philosophy of Language)

**Source:** Robert B. Brandom, *Making It Explicit: Reasoning, Representing, and Discursive Commitment* (1994).

**What Brandom means:** Discursive commitment is the inferential obligation a speaker undertakes by making an assertion within a social practice. Meaning IS the pattern of commitments and entitlements that flows from assertions. This is an agent-side property — what the speaker has bound themselves to defend.

**CT distinction:** CT's commitment is a property of signals, not agents. CT asks: "What does this signal itself obligate, permit, and prohibit?" — independent of who wrote it, who reads it, or what inferential obligations they undertake. Brandom's commitment is epistemic/pragmatic (about reasoning and discourse). CT's commitment is deontic (about operative content of the signal). Different objects.

**Where to cite:** P-000 §2.1, L-000, CL-001

---

## 2. Walton & Krabbe — Commitment Stores (Dialogue Logic)

**Source:** Douglas N. Walton & Erik C.W. Krabbe, *Commitment in Dialogue: Basic Concepts of Interpersonal Reasoning* (1995).

**What they mean:** Commitment stores are the sets of propositions a participant in a dialogue has accepted and is bound to defend. Commitments can be incurred, retracted, or challenged in a structured dialogue game.

**CT distinction:** Dialogue commitment stores track the conversational obligations of participants over time. CT's commitment kernel is a synchronic property of a signal at a given moment — not a diachronic record of dialogue history. A Walton/Krabbe commitment store changes as dialogue progresses; a CT commitment kernel is the stable invariant of a signal under transformation.

**Where to cite:** P-000 §2.1, L-000

---

## 3. CommitmentBank — Speaker Commitment (NLP)

**Source:** Marie-Catherine de Marneffe et al., *The CommitmentBank: Investigating Projection in Naturally Occurring Discourse*, 2 Proc. Soc'y for Computation in Linguistics 107 (2019).

**What they mean:** Speaker commitment (also called event factuality) measures the degree to which a speaker believes an embedded event is true, false, or uncertain. E.g., "John believes that Mary left" — the speaker is not committed to Mary having left, but represents John as committed.

**CT distinction:** CommitmentBank asks: "How certain is the speaker that X happened?" CT asks: "Does the signal itself still obligate Y after it has been transformed?" The first is an epistemic stance detection task (speaker beliefs about truth). The second is a measurement of deontic content preservation across transformation. Different questions, different objects.

**Where to cite:** P-000 §2.2, CL-001

---

## 4. Cryptographic Commitment (Blum 1981, ABBA 2026)

**Source (foundational):** Manuel Blum, *Coin Flipping by Telephone*, in Advances in Cryptology: A Report on Crypto 81, at 11–15 (Allen Gersho ed., 1981).
**Source (CT-adjacent):** [Author], ABBA: Algebraic Bimodal Binding Architecture (2026) (IACR ePrint DOI: 10.62056/aiy34f7mq).

**What cryptographic commitment means:** A commitment scheme allows a party to bind themselves to a hidden value and reveal it later. Two properties: statistically hiding (receiver can't see the value before reveal) and computationally binding (committer can't change the value after committing). ABBA is a lattice-based, linearly homomorphic version designed for post-quantum security.

**CT distinction:** Cryptographic commitment is a TOOL (a protocol). CT's commitment is the THING being protected (the deontic kernel). ABBA can be used to protect a Vault Artifact's lineage and custody claims — so cryptographic commitment can serve CT's purposes — but they operate at different levels. The algebraic invariants of ABBA (trace-zero projection) inspired the concept of extracting an invariant kernel, but the semantic application is CT's novel contribution. Cryptographic commitment: hiding and binding a secret. CT commitment: the invariant meaning that survives transformation.

**Where to cite:** P-000 §2.3

---

## 5. Organizational Commitment (Meyer & Allen)

**Source:** John P. Meyer & Natalie J. Allen, *A Three-Component Conceptualization of Organizational Commitment*, 1 Hum. Res. Mgmt. Rev. 61 (1991).

**What they mean:** Organizational commitment is an employee's psychological bond to their organization, comprising affective commitment (emotional attachment), continuance commitment (cost of leaving), and normative commitment (obligation to stay).

**CT distinction:** Completely different domain. CT has no relation to employment psychology. Domain separation is complete.

**Where to cite:** P-000 §2.4 (brief mention)

---

## 6. COR Theory — Conservation of Resources (Hobfoll)

**Source:** Stevan E. Hobfoll, *Conservation of Resources: A New Attempt at Conceptualizing Stress*, 44 Am. Psychologist 513 (1989).

**What COR means:** Conservation of Resources is a stress-motivation model holding that people are motivated to protect valued resources from loss. "Conservation" here is a metaphor — people "conserve" their resources the way animals conserve energy.

**CT distinction:** COR uses "conservation" loosely as a behavioral tendency. CT uses "conservation" as a formal mathematical term — an invariance under transformation. COR is a model of human motivation. The Conservation Law of Commitment is a falsifiable empirical law about signal properties. The abbreviations "COR" and "CT" do not collide. The phrases "commitment conservation" (COR collision) and "Conservation Law of Commitment" (CT, zero collision) must be kept distinct. **Never use "commitment conservation" as a standalone phrase in CT materials.**

**Where to cite:** P-000 §2.5, Naming_Architecture.md

---

## 7. Semantic Continuity (Software Engineering)

**What they mean:** In database migration and software versioning, "semantic continuity" refers to preserving the intended behavior of a schema, API, or protocol as it evolves. A semantically continuous change preserves the contract between components.

**CT distinction:** CT uses "semantic continuity" as a plain-language synonym for commitment preservation in legal contexts. The software engineering usage is about interface contracts in technical systems; CT's usage is about deontic content in natural language signals. Low collision risk but a footnote in legal papers is prudent.

**Where to cite:** SLRO essay §2 (footnote), L-000 §2.6

---

## 8. Semantic Entropy (Kuhn et al., NeurIPS 2023)

**Source:** Lorenz Kuhn et al., *Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation*, Advances in Neural Information Processing Systems (NeurIPS 2023).

**What Kuhn et al. mean:** Semantic entropy measures uncertainty in LLM outputs by clustering semantically equivalent generated sentences and computing entropy over those clusters. If all generated answers cluster together, entropy is low; if they diverge, entropy is high.

**CT distinction:** Kuhn's semantic entropy measures uncertainty in a single generation step. CT's Second Law of Semantic Entropy describes the rate of deontic decay across an iterative transformation pipeline. Kuhn: "Is the model uncertain about what to output right now?" CT: "Is the commitment kernel degrading across multiple transformations over time?" Orthogonal questions. The shared vocabulary warrants a disambiguation footnote in CT's information science papers.

**Where to cite:** P-000 §6.4, IS-001, Paper 1
