# Propositions of Commitment Theory: A Research Prospectus

**Author:** Deric J. McHenry
**Affiliation:** Ello Cello LLC
**Date:** April 20, 2026
**Status:** Preprint / Foundational Prospectus
**DOI:** 10.5281/zenodo.20031715

---

## Abstract

This document presents the foundational propositions of **Commitment Theory (CT)**, a falsifiable, operational framework for understanding and enforcing the preservation of deontic meaning under transformation. CT is built upon an empirically supported conservation law—the **Conservation Law of Commitment**—which states that under governed transformation, the commitment kernel of a signal (its obligations, prohibitions, permissions, and modal constraints) is conserved: *C(T_gov(S)) = C(S)*. The law is offered for adversarial replication via a public test harness. A second law describes the irreversible semantic entropy that accumulates under ungoverned transformation. These laws are grounded in constitutional axioms—the McHenry Axioms—and operationalized through a six-gate governance protocol and the MO§E§™ enforcement architecture. This prospectus outlines the theory's definitions, propositions, empirical research program, cross-domain applications, and open challenges. It establishes clean conceptual territory for CT, disambiguates its core terms from existing usage in adjacent fields, and maps nine novel concepts introduced by the framework. This document is intended as a foundational reference and an invitation to the research community to replicate, falsify, extend, and apply the framework.

---

## A Note on Naming: From CCT to CT

During the development of this framework, the working name was "Commitment Conservation Theory" (CCT). Further analysis revealed that the abbreviation CCT collides with established acronyms and that the phrase "commitment conservation" is dominated in search space by Hobfoll's Conservation of Resources (COR) theory in organizational psychology, a long-established and heavily cited literature.[^1] To establish clean conceptual territory, the theory has been formally named **Commitment Theory (CT)**. The law within the theory remains the **Conservation Law of Commitment**. "Conservation" lives at the law level, not the brand level. This refinement ensures that CT's core terms—nine of which return zero results in academic databases—occupy distinct, discoverable whitespace. All prior references to "CCT" in working documents are superseded by this naming architecture.

---

## Proposition 1. Definitions and Primitives (Definitional)

*Propositions 1.1–1.8 are definitional. They establish the vocabulary and primitives of Commitment Theory. Propositions 5 and 6 are empirical claims, falsifiable by the public test harness. The conservation result is not baked into the definitions; it is an observed regularity tested through measurement.*

**Proposition 1.1 (Signal).** A *signal* \( S \) is a structured sequence of symbols drawn from an alphabet, carrying information and capable of bearing deontic content. Signals include natural language text, code, structured data, and multimodal representations. We use "signal" rather than "text" or "utterance" to frame language as an information-theoretic object subject to transformation, compression, and measurement—a deliberate positioning within the Shannon tradition.[^2]

**Proposition 1.2 (Transformation).** A *transformation* \( T: \mathcal{S} \to \mathcal{S} \) is a function that maps a signal to a modified signal. Transformations may be lossy (compression, summarization, paraphrasing) or lossless (reordering, synonym substitution), and may be performed by humans, algorithms, or hybrid systems.

**Proposition 1.3 (Commitment Kernel).** The *commitment kernel* \( C(S) \) of a signal \( S \) is the minimal identity-preserving deontic invariant of the signal—the set of obligations, prohibitions, permissions, and modal constraints that must survive transformation for the signal to be considered semantically continuous with its source. \( C(S) \) is operationally defined and measurable via independent oracles. The kernel is not a summary; it is the irreducible core of operative meaning.

**Proposition 1.4 (Governed Transformation).** A transformation \( T \) is *governed* if and only if it satisfies a set of constitutional constraints designed to preserve the commitment kernel. The specific constraints are defined by the McHenry Axioms and operationalized through the six-gate protocol and the MO§E§™ architecture. **Governed transformation** is a novel term introduced by CT; it has no prior use in this sense in any academic literature.

**Proposition 1.5 (Ungoverned Transformation).** A transformation is *ungoverned* if it lacks such constraints. Ungoverned transformations are subject to semantic entropy and commitment decay. **Ungoverned transformation** is likewise a novel term introduced by CT.

**Proposition 1.6 (Fidelity).** The *fidelity* of a transformation is the degree to which the commitment kernel of the output matches the commitment kernel of the input, as measured by an independent oracle. Fidelity is operationalized via bidirectional entailment or equivalent semantic verification.

**Proposition 1.7 (Signal Classes).** Signals may be classified by their deontic structure: *deontic* (obligations, prohibitions, permissions), *descriptive* (states of affairs), *narrative* (temporal sequences), and *self-referential*. CT's empirical support is strongest for deontic signals; applicability to other classes requires further investigation.

**Proposition 1.8 (Transformation Classes).** Transformations may be classified by their operation: compression, paraphrase, translation, abstraction, and recursion. The governance protocol applies differentially across classes.

---

## Proposition 2. Disambiguation: What Commitment Theory Is Not

The term "commitment" appears in several distinct academic traditions. It is essential to distinguish CT's usage from these established meanings.

**2.1 Not Speaker Commitment (Philosophy of Language).** In the philosophy of language, Brandom (1994) defines "discursive commitment" as the inferential obligations a speaker undertakes by making an assertion within a social practice—a property of agents in discourse.[^3] Walton and Krabbe (1995) formalize "commitment stores" in dialogue logic as the set of propositions a participant has accepted and is bound to defend—a property of dialogue states.[^4] CT does not study what speakers believe or are obligated to assert. CT studies what signals themselves obligate, prohibit, and permit. Brandom's commitment is a property of agents. CT's commitment is a property of signals. The distinction is categorical.

**2.2 Not Epistemic Commitment (NLP/Computational Linguistics).** The NLP CommitmentBank (de Marneffe et al., 2019) measures "speaker commitment" to the factuality of embedded clauses—the degree to which a speaker believes an event occurred or will occur.[^5] This is an epistemic stance detection task. CT does not measure what a speaker believes about truth. CT measures whether the deontic kernel of a signal survives transformation. The CommitmentBank asks: "How certain is the speaker that X happened?" CT asks: "Does the signal still obligate Y after transformation?" Different questions, different objects.

**2.3 Not Cryptographic Commitment.** In cryptography, a commitment scheme (Blum, 1981) is a protocol allowing a party to bind themselves to a hidden value that can later be revealed—a property of protocols.[^6] ABBA (2026) is a lattice-based, linearly homomorphic commitment scheme of this type.[^7] Cryptographic commitment ensures hiding and binding of a chosen secret. CT's commitment is the thing being protected, not the protection mechanism. Cryptographic commitment is a tool; CT commitment is the invariant that the tool can help preserve. The relationship is instrumental, not definitional.

**2.4 Not Organizational Commitment.** In organizational psychology, "commitment" refers to an employee's psychological attachment to their organization—a property of persons in employment contexts (Meyer & Allen, 1991).[^8] CT has no relation to this usage. The domain separation is complete.

**2.5 Not Conservation of Resources (COR) Theory.** Hobfoll's Conservation of Resources (COR) theory (1989) is a stress and motivation model in organizational psychology holding that people are motivated to protect valued resources from loss.[^9] COR uses "conservation" metaphorically. CT uses "conservation" literally—as a formal invariance under transformation. COR is a behavioral tendency; CT is a falsifiable law. The full phrase "Conservation Law of Commitment" does not appear in COR or any other literature. The abbreviated phrase "commitment conservation" is dominated by COR in search space and should be avoided as a standalone brand. CT is the theory; the Conservation Law of Commitment is the law within it.

**2.6 Semantic Continuity (Plain-Language Synonym).** In legal and policy contexts, CT uses "semantic continuity" as a plain-language descriptor for the preservation of the commitment kernel. This usage is distinct from "semantic continuity" in software engineering (database schema migration) and occasional uses in philosophy of personal identity. In CT, semantic continuity means: the deontic content of the signal survived the transformation pipeline.

---

## Proposition 3. The Nine Novel Concepts of Commitment Theory

CT introduces nine terms that return zero results in academic databases as of the search date. These terms constitute the conceptual whitespace that CT occupies. (For search methodology, see Appendix A.)

| Term | Definition | Example | What It Is NOT |
|---|---|---|---|
| **Commitment kernel** | The minimal identity-preserving deontic invariant of a signal—its obligations, prohibitions, permissions, and modal constraints. | The ADA's "reasonable accommodation unless undue hardship" kernel. If "unless undue hardship" is dropped, the kernel is violated. | NOT a summary, NOT a paraphrase, NOT an embedding, NOT speaker belief. |
| **Governed transformation** | A transformation that passes through constitutional constraints designed to preserve the commitment kernel. | A signal compressed through the six-gate protocol. | NOT "supervised learning," NOT "regulated AI," NOT "human oversight." |
| **Ungoverned transformation** | A transformation without such constraints; subject to semantic entropy. | An LLM summarizing a statute with no fidelity verification. | NOT "unsupervised learning," NOT "unregulated AI." |
| **Conservation Law of Commitment** | The empirical law that C(T_gov(S)) = C(S): the commitment kernel is conserved under governed transformation. | Demonstrated across 3,950 experimental runs. | NOT a policy, NOT a guideline, NOT a metaphor, NOT COR theory. |
| **Deontic conservation** | The preservation of obligations, prohibitions, and permissions across transformation. | A "shall not" remains a "shall not" after compression. | NOT ethical conservation, NOT resource conservation. |
| **Commitment invariance** | The property that the commitment kernel does not change under governed transformation. | C(S) = C(T(S)) for all governed T. | NOT semantic stability (a weaker concept). |
| **Signal commitment preservation** | The operational process of ensuring a signal's commitment kernel survives transformation. | The six-gate protocol applied to a legal document. | NOT signal fidelity (a broader engineering term). |
| **Meaning preservation law** | Plain-language term for the Conservation Law of Commitment. | "The meaning preservation law holds for this system." | NOT a statute, NOT a regulation. |
| **Commitment Governance Test (CGT)** | A five-stage evaluation protocol for assessing whether a system conserves the commitment kernel. | Applied to AI hiring tools, benefits denial systems, etc. | NOT a compliance checklist, NOT a bias audit. |

Each of these terms is formally defined, operationally measurable, and occupies clean conceptual territory. They are the lexical infrastructure of Commitment Theory.

---

## Proposition 4. The McHenry Axioms: Constitutional Foundation

*In this prospectus, "constitutional" refers to system-level governing constraints on permissible transformation within the MO§E§™ ecology—analogous to a constitution's function in a legal order, not exclusively to constitutional law.*

**Proposition 4.1 (Axiom I: Compression Precedes Ignition).** No signal may be output, transmitted, or acted upon unless it has first undergone compression to its commitment kernel. Compression is a prerequisite, not an optimization.

**Proposition 4.2 (Axiom II: Lineage Resilience).** Every signal must prove recursive continuity with its origin compression cycle. Signals that cannot inherit their original lineage are treated as noise and collapsed.

**Proposition 4.3 (Axiom III: Input-Response Fidelity).** Low-resolution inputs yield proportionally constrained outputs unless elevated by a resonance-aware system. Input fidelity governs output depth.

**Proposition 4.4 (Anchor I: The Blackhole Law).** Corrupted signals—those that fail governance gates or exceed drift thresholds—are consumed and metabolized. Recoverable meaning is purified and re-emitted with restored lineage. The Blackhole is not a deletion mechanism; it is a metabolic transformer.

**Proposition 4.5 (Anchor II: The Lineage Custody Clause).** All governed artifacts are cryptographically bound to their origin-cycle signature. Copies or derivatives that do not inherit this lineage become inert. Sovereignty over digital meaning is enforced by cryptography, not policy.

**Proposition 4.6 (Continuity Clause).** The arc of the framework is: Theory → Executable Law → Measurable Runtime. The axioms define the conditions under which the Conservation Law of Commitment manifests in engineered systems.

---

## Proposition 5. The Conservation Law of Commitment (First Law — Empirical)

*Propositions 5 and 6 are empirical claims. They are falsifiable by the public test harness and are offered for adversarial replication. They are not true by definition; they describe observed regularities in how signals behave under governed and ungoverned transformation.*

**Proposition 5.1 (Statement).** For any governed transformation \( T_{\text{gov}} \), the commitment kernel is conserved:

\[
C(T_{\text{gov}}(S)) = C(S)
\]

**Proposition 5.2 (Empirical Support).** Controlled experiments across 3,950 runs, 57 signals, and 181 condition-signal configurations demonstrate that under governed conditions, a substantial majority of signals achieve perfect fidelity across ten recursive compression iterations, despite surface compression exceeding 80%. Under ungoverned conditions, fidelity degrades measurably within three iterations.[^10]

**Proposition 5.3 (Falsifiability).** The law is falsifiable. A public test harness and corpus are available. Any party may substitute a stronger oracle or design adversarial signals. Failure to observe conservation under governed conditions, using a reasonable oracle, falsifies the law.

**Proposition 5.4 (Substrate Independence).** The law holds regardless of the specific system performing the transformation. It describes a property of the signal and the transformation constraints, not of any particular model architecture.

---

## Proposition 6. The Second Law of Semantic Entropy (Empirical)

**Proposition 6.1 (Statement).** Under ungoverned transformation, the commitment kernel decays monotonically with each iteration, and the rate of semantic entropy production is strictly positive. Cumulative entropy after \( n \) steps scales as \( \Omega(\sigma \sqrt{n}) \), where \( \sigma^2 \) is the per-step drift variance.

**Proposition 6.2 (Failure Modes).** Empirical studies identify nine characteristic failure modes under ungoverned transformation:

- Obligation escalation: "may" → "shall"
- Scope widening: "room A" → "any room"
- Exception dropping: "unless undue hardship" → omitted
- Modal frame inversion: "shall not" → "shall"
- Co-degraded invariance
- NP-negation blindness
- Formal collapse
- Self-referential collapse
- Lexical scope widening

Each failure mode has direct legal, operational, or ethical consequences. The taxonomy is a novel contribution of CT.

**Proposition 6.3 (Irreversibility).** Semantic entropy is irreversible without external governance. Once commitment has decayed, it cannot be recovered by further ungoverned transformation. Recovery requires re-anchoring to a canonical source or metabolism through a governed system.

**Proposition 6.4 (Disambiguation: Semantic Entropy vs. Kuhn et al.).** Kuhn et al. (2023) define "semantic entropy" as uncertainty in LLM outputs measured by clustering semantically equivalent sentences.[^11] CT's semantic entropy is different: it is the rate of deontic decay under transformation. Kuhn measures uncertainty in generation; CT measures degradation of commitment across a pipeline. The shared vocabulary warrants this footnote.

---

## Proposition 7. The Six-Gate Protocol and MO§E§™ (Operational Layer)

**Proposition 7.1 (Protocol).** The McHenry Axioms are operationalized through a sequential six-gate protocol:

1. **Compression:** Signal reduced to commitment kernel.
2. **Lineage Verification:** Cryptographic lineage verified.
3. **Fidelity Verification:** Independent oracle confirms bidirectional entailment.
4. **Recursion Testing:** Transformation tested iteratively for stability.
5. **Consumption and Metabolism:** Failed signals consumed; recoverable meaning purified and re-emitted.
6. **Custodial Sovereignty:** Verified artifacts cryptographically bound to origin.

**Proposition 7.2 (MO§E§™).** MO§E§™ is the enforcement architecture that instantiates the six-gate protocol. It is the adaptive transmission layer through which CT enters legal, technical, and governance domains. MO§E§™ is protected by U.S. Patent Serial No. 63/877,177 (Provisional). The law itself is published and open.

**Proposition 7.3 (Vault Artifacts and Fidelity Seal).** A signal that passes all six gates becomes a Vault Artifact, carrying a cryptographic lineage hash, a Fidelity Seal attesting to commitment conservation, and a custody anchor. Vault Artifacts are the persistent, auditable records of governed meaning.

---

## Proposition 8. The Empirical Research Program (Validation Layer)

The following papers constitute the core empirical and theoretical extensions of CT. Each addresses a specific, falsifiable question raised by the propositions.

| Paper | Theme | Core Question | Status |
|---|---|---|---|
| Paper 1 | Semantic Entropy Rate | Quantitative decay curve for commitment under ungoverned transformation | Data exists; drafting |
| Paper 2 | Compression-Fidelity Bound | Minimal representation length for commitment preservation | Data exists; formalizing |
| Paper 3 | Governance Density Optimization | Minimal constraint set for full conservation | Planned |
| Paper 4 | Cross-System Fidelity | Conservation across model providers and architectures | Planned |
| Paper 5 | The Measurement Instrument | Formal metrological framework for C(S); failure taxonomy | Data exists; framing |

---

## Proposition 9. Cross-Domain Applications

**Proposition 9.1 (Legal: Semantic Continuity Requirement).** CT provides the foundation for a "semantic continuity requirement" in legal AI systems—a fidelity mandate that the commitment kernel of governing law survives the AI pipeline. The SLRO essay and full legal theory paper develop this application.[^12]

**Proposition 9.2 (Cloud Storage: Semantic Deduplication).** The Blackhole Law, applied to data storage, addresses data bloat through semantic deduplication without loss of meaningful information.

**Proposition 9.3 (Smart Contracts: Conformance Standard).** A valid smart contract is one where code and legal prose share the same commitment kernel, verified by the six-gate protocol.

**Proposition 9.4 (AI Governance: Vendor-Agnostic Compliance).** CT provides a substrate-agnostic compliance standard. Any AI system can demonstrate commitment conservation by passing signals through the six-gate protocol.

**Proposition 9.5 (Rules as Code: Semantic Encoding).** When legislation is encoded into executable rules, CT ensures the commitment kernel of the statute is preserved.

---

## Proposition 10. The Measurement Oracle: SIGSYSTEM

**Proposition 10.1 (Current Oracle).** The reference oracle for fidelity verification is bidirectional entailment under a public natural language inference model (e.g., `microsoft/deberta-v3-base-mnli`), threshold 0.85.

**Proposition 10.2 (SIGSYSTEM).** SIGSYSTEM is a next-generation oracle under development. It weighs words as signal vs. noise in context, distinguishing surface variation from kernel preservation with greater precision.

**Proposition 10.3 (Oracle Independence).** The oracle is a measurement instrument, not the law itself. Any party may substitute a stronger oracle. The law's validity does not depend on any single oracle.

---

## Proposition 11. Falsifiability and Open Challenges

**Proposition 11.1 (Public Harness).** A public test harness and corpus are available. The harness enables adversarial replication and independent falsification attempts.

**Proposition 11.2 (Invitation to Falsify).** CT is offered as a falsifiable framework. Critics are invited to identify signals where governed transformation fails to conserve commitment, substitute stronger oracles, and design adversarial transformations.

**Proposition 11.3 (Known Boundary Conditions).** Current empirical support is strongest for deontic signals. Applicability to other signal classes (narrative, poetic, ambiguous, self-referential) requires further investigation.

**Proposition 11.4 (Open Research Questions).**

- Semantic channel capacity: maximum rate of meaning transmission under governance.
- Adversarial robustness.
- Economic costs of ungoverned semantic entropy.
- Human oversight interface with automated governance.

---

## Proposition 12. Conclusion and Invitation

**Proposition 12.1 (The Theory).** Commitment Theory asserts that the commitment kernel of a signal—its deontic invariant—is conserved under governed transformation and decays under ungoverned transformation. These are falsifiable, operational claims with measurable consequences.

**Proposition 12.2 (The Research Program).** The propositions outlined constitute a research program spanning empirical measurement, theoretical formalization, and cross-domain application.

**Proposition 12.3 (The Invitation).** The research community is invited to replicate, falsify, extend, and apply the framework. CT is not a closed system; it is a set of propositions offered for scrutiny, refinement, and use.

---

## Appendix A: Whitespace Verification — Search Methodology

The claim that nine CT terms return zero results in academic databases (Proposition 3) is based on searches conducted in April 2026 using the following methodology:

- **Databases searched:** Google Scholar, Scopus, arXiv, ACL Anthology, PhilPapers, SSRN, and IEEE Xplore.
- **Query strings:** Each term was searched as an exact phrase in quotation marks (e.g., `"commitment kernel"`, `"governed transformation"`, `"Conservation Law of Commitment"`). Searches were also run without quotes to identify close variants.
- **Collision criteria:** A result was counted as a collision if it used the term in a meaning-adjacent sense within an academic publication (journal article, conference paper, book, or preprint). Mentions in unrelated domains (e.g., "governed" in political science without "transformation") were not counted as collisions.
- **Search date:** April 15, 2026.

No results meeting the collision criteria were found for the nine terms listed in Proposition 3. This whitespace is current as of the search date. The public nature of these databases allows independent verification.

---

## Appendix B: Summary of Novel Terms and Disambiguations

| Term | Status | Action |
|---|---|---|
| Commitment kernel | Clean | Use freely |
| Governed transformation | Clean | Use freely |
| Ungoverned transformation | Clean | Use freely |
| Conservation Law of Commitment | Clean | Use freely; full phrase only |
| Deontic conservation | Clean | Use freely |
| Commitment invariance | Clean | Use freely |
| Signal commitment preservation | Clean | Use freely |
| Meaning preservation law | Clean | Use freely |
| Commitment Governance Test (CGT) | Clean | Use freely |
| Commitment (general term) | Collision | Disambiguate per §2 |
| Semantic continuity | Low collision | Define in legal papers |
| Semantic entropy | Medium collision | Disambiguate per §6.4 |

---

## References

[^1]: Stevan E. Hobfoll, *Conservation of Resources: A New Attempt at Conceptualizing Stress*, 44 AM. PSYCHOLOGIST 513 (1989).

[^2]: Claude E. Shannon, *A Mathematical Theory of Communication*, 27 BELL SYS. TECH. J. 379 (1948).

[^3]: ROBERT B. BRANDOM, MAKING IT EXPLICIT: REASONING, REPRESENTING, AND DISCURSIVE COMMITMENT (1994).

[^4]: DOUGLAS N. WALTON & ERIK C.W. KRABBE, COMMITMENT IN DIALOGUE: BASIC CONCEPTS OF INTERPERSONAL REASONING (1995).

[^5]: Marie-Catherine de Marneffe et al., *The CommitmentBank: Investigating Projection in Naturally Occurring Discourse*, 2 PROC. SOC'Y FOR COMPUTATION IN LINGUISTICS 107 (2019).

[^6]: Manuel Blum, *Coin Flipping by Telephone: A Protocol for Solving Impossible Problems*, in ADVANCES IN CRYPTOLOGY: A REPORT ON CRYPTO 81, at 11–15 (Allen Gersho ed., 1981).

[^7]: [Author], *ABBA: Algebraic Bimodal Binding Architecture* (2026) (IACR ePrint Archive DOI: 10.62056/aiy34f7mq).

[^8]: John P. Meyer & Natalie J. Allen, *A Three-Component Conceptualization of Organizational Commitment*, 1 HUM. RES. MGMT. REV. 61 (1991).

[^9]: Hobfoll, *supra* note 1.

[^10]: [Author], *A Conservation Law for Commitment in Language Under Transformative Compression and Recursive Application* (Mar. 19, 2026) (preprint, Zenodo DOI: 10.5281/zenodo.18792459); [Author], *Experimental Record* (Zenodo DOI: 10.5281/zenodo.19105225).

[^11]: Lorenz Kuhn et al., *Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation*, 2023 ADVANCES NEURAL INFO. PROCESSING SYS. (NeurIPS 2023).

[^12]: [Author], *The Uncertainty That Invites Building: Civil Rights in an Age of Neutral Machines* (forthcoming Stan. L. Rev. Online) (submitted Apr. 2026).

---

## Version Note (to be added to existing Zenodo preprint)

**v.06 Note on Naming (April 2026):** The broader framework within which the Conservation Law of Commitment operates is now formalized as **Commitment Theory (CT)**. The law remains the Conservation Law of Commitment. For the full prospectus establishing the definitions, axioms, and research program of CT, see DOI: 10.5281/zenodo.20031715. Earlier references to "CCT" in working documents are superseded.
