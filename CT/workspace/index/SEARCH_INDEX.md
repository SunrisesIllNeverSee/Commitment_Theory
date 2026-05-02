# Commitment Theory — Searchable Index

Search this file for any term, concept, document, or decision from the session.

---

## Core Terms (CT Vocabulary)

| Term | Definition | First Used | Find In |
|------|-----------|-----------|---------|
| **Commitment Theory (CT)** | The overarching framework. A falsifiable, operational theory of deontic meaning preservation under transformation. Supersedes "CCT." | Naming session, Apr 14 | All documents |
| **Conservation Law of Commitment** | The first law: C(T_gov(S)) = C(S). The commitment kernel is conserved under governed transformation. | Paper 0, Jan 2026 | P-000 §5, Paper 0 |
| **Second Law of Semantic Entropy** | Under ungoverned transformation, commitment decays monotonically. ΔH_C > 0 per step. | Session, Apr 13 | P-000 §6, Second_Law_Draft.md |
| **Commitment kernel** | The minimal identity-preserving deontic invariant of a signal — its obligations, prohibitions, permissions, modal constraints. One of nine empty rooms. | Paper 0 | P-000 §1.3, all |
| **Governed transformation** | A transformation passing through constitutional constraints designed to preserve the commitment kernel. Novel term — zero search results. | Paper 0 | P-000 §1.4 |
| **Ungoverned transformation** | A transformation without such constraints. Subject to semantic entropy. Novel term. | Paper 0 | P-000 §1.5 |
| **Deontic conservation** | Preservation of obligations, prohibitions, permissions across transformation. Novel term. | Session | P-000 §3, Nine_Novel_Concepts.md |
| **Commitment invariance** | Property that C(S) = C(T(S)) for all governed T. Novel term. | Session | P-000 §3 |
| **Signal commitment preservation** | Operational process of ensuring a signal's kernel survives transformation. Novel term. | Session | P-000 §3 |
| **Meaning preservation law** | Plain-language synonym for Conservation Law of Commitment. Novel term. | Session | P-000 §3 |
| **Commitment Governance Test (CGT)** | Five-stage evaluation protocol for assessing commitment conservation. Novel term. | Session | P-000 §3 |
| **Fidelity** | Degree to which commitment kernel of output matches input. Measured by independent oracle. | Paper 0 | P-000 §1.6 |
| **Fidelity Seal** | Cryptographic attestation that a signal passed all six gates and its commitment kernel is conserved. | Session | P-000 §7.3 |
| **Vault Artifact** | A signal that has passed the six-gate protocol, carrying lineage hash, Fidelity Seal, and custody anchor. | Session | P-000 §7.3 |
| **Semantic continuity** | Plain-language synonym for CT's commitment preservation, used in legal papers. | Session | SLRO essay, L-000 |
| **Semantic entropy** | Rate of deontic decay under ungoverned transformation. Distinct from Kuhn et al. (LLM uncertainty). | Session | P-000 §6.4 |

---

## The McHenry Axioms (Constitutional Foundation)

| Axiom | Statement | Find In |
|-------|-----------|---------|
| Law I | Compression Precedes Ignition | P-000 §4.1 |
| Law II | Lineage Resilience | P-000 §4.2 |
| Law III | Input-Response Fidelity | P-000 §4.3 |
| Anchor I | Blackhole Law (consume + metabolize) | P-000 §4.4 |
| Anchor II | Lineage Custody Clause | P-000 §4.5 |
| Clause | Continuity Clause: Theory → Executable Law → Measurable Runtime | P-000 §4.6 |

---

## The Six-Gate Protocol

| Gate | Function | Axiom |
|------|----------|-------|
| G1 | Compression — reduce to commitment kernel | Law I |
| G2 | Lineage Verification — cryptographic chain | Law II |
| G3 | Fidelity Verification — bidirectional entailment | Law III |
| G4 | Recursion Testing — iterative stability | Continuity Clause |
| G5 | Consumption & Metabolism — metabolize + re-emit | Anchor I (Blackhole) |
| G6 | Custodial Sovereignty — bind to origin | Anchor II |

---

## Failure Modes (Nine Documented)

| Mode | Description | Legal Consequence |
|------|-------------|------------------|
| Obligation escalation | "may" → "shall" | Creates liability where none existed |
| Scope widening | "room A" → "any room" | Extends restriction beyond legislative intent |
| Exception dropping | "unless undue hardship" → omitted | Eliminates statutory defense |
| Modal frame inversion | "shall not" → "shall" | Reverses legal obligation |
| Co-degraded invariance | Both anchor and drift elements decay together | Compound harm |
| NP-negation blindness | Jaccard detects surface loss; NLI misses semantic change | Measurement gap |
| Formal collapse | Signal structurally disintegrates under recursion | Total loss |
| Self-referential collapse | Signal describing the law fails application of the law | Gödel-like limit |
| Lexical scope widening | Negation scope expands beyond intended range | Broad interpretation error |

---

## Disambiguation Terms (What CT Is NOT)

| Term | Collision | CT Distinction | Find In |
|------|-----------|----------------|---------|
| Commitment (Brandom) | Speaker's inferential obligations in discourse | CT commitment = property of signals, not agents | P-000 §2.1 |
| Commitment (Walton & Krabbe) | Dialogue commitment stores | Same as above | P-000 §2.1 |
| Commitment (CommitmentBank) | Speaker factuality stance in NLP | CT = deontic signal property, not epistemic stance | P-000 §2.2 |
| Commitment (cryptographic) | Hiding + binding schemes (Blum 1981, ABBA 2026) | CT commitment = what is protected, not the protection | P-000 §2.3 |
| Commitment (organizational) | Employee attachment (Meyer & Allen 1991) | Unrelated domain | P-000 §2.4 |
| Commitment conservation (COR) | Hobfoll's Conservation of Resources — 19,000 citations | CT uses "conservation" literally (formal invariance), not metaphorically | P-000 §2.5, Naming_Architecture.md |
| Semantic continuity (software) | Database schema migration | CT = deontic content survival through AI pipeline | P-000 §2.6 |
| Semantic entropy (Kuhn et al.) | LLM output uncertainty | CT = rate of deontic decay under transformation | P-000 §6.4 |

---

## People and Publications

| Name / Work | Relevance | Where Cited |
|-------------|-----------|-------------|
| Shannon (1948) | Information Theory precedent; "signal" vocabulary origin | P-000 §1.1 |
| Brandom (1994) | "Making It Explicit" — speaker commitment in discourse | P-000 §2.1, Disambiguation |
| Walton & Krabbe (1995) | "Commitment in Dialogue" — dialogue commitment stores | P-000 §2.1 |
| Hobfoll (1989) | Conservation of Resources (COR) theory — 19k citations; dominates "commitment conservation" search | Naming decision, P-000 §2.5 |
| Blum (1981) | CRYPTO '81 — cryptographic commitment scheme "Coin Flipping by Telephone" | P-000 §2.3 |
| Meyer & Allen (1991) | Organizational commitment theory | P-000 §2.4 |
| de Marneffe et al. (2019) | NLP CommitmentBank | P-000 §2.2 |
| Kuhn et al. (2023) | "Semantic Uncertainty" NeurIPS — LLM entropy (different from CT semantic entropy) | P-000 §6.4 |
| Barocas & Selbst (2016) | "Big Data's Disparate Impact" — algorithmic discrimination | SLRO §1 fn.2 |
| Kroll et al. (2017) | "Accountable Algorithms" | SLRO §1 fn.2 |
| Citron (2008) | "Technological Due Process" | SLRO §2 fn.13 |
| Griggs v. Duke Power (1971) | Business necessity defense, Title VII | SLRO fn.28 |
| Mathews v. Eldridge (1976) | Due process balancing test | SLRO fn.32 |

---

## Key Decisions Made in This Session

| Decision | Rationale | Find In |
|----------|-----------|---------|
| CCT → CT | "Commitment Conservation" owned by Hobfoll COR (19k citations) | Naming_Architecture.md, P-000 intro |
| "Conservation" at law level, not theory level | Keeps theory name clean; law name precise | Naming_Architecture.md |
| Nine empty rooms documented with search methodology | Makes whitespace claim empirical not rhetorical | P-000 Appendix A |
| SLRO essay framing: future of civil rights, not AI governance | Call's primary topic is civil rights; AI is secondary | SLRO_Strategy_Notes.md |
| AI default is neutral (not "AI fixes bias") | Core thesis of SLRO essay | SLRO essay §Intro |
| Blackhole metabolizes, does not delete | Hawking radiation analogy; closed loop not dead end | P-000 §4.4, SLRO §4.B |
| Trade secret for SIGSYSTEM | Long-term competitive advantage without 20-year expiry | Patent_Strategy.md |

---

## Venues by Paper

| Venue | Paper |
|-------|-------|
| Stanford Law Review Online | L-001 (SLRO) |
| Artificial Intelligence and Law (Springer) | L-007 |
| Int'l J. Law & Info. Tech. (Oxford) | L-007 alt |
| Harvard / Yale / Stanford L. Rev. | L-008 |
| NeurIPS / ICML | Paper 2 |
| AAMAS | Paper 3 |
| NeurIPS / Applied AI | Paper 1, Paper 4 |
| Foundations of AI / Philosophy of Info | Paper 5 |
| Zenodo / arXiv | P-000, Paper 0 |
| SSRN / Zenodo | L-000 |
