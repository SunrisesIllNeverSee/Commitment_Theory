# GOV-001 — Governing the Transformation: Commitment Theory and the Missing Semantic Layer in AI Governance Frameworks

**Track:** MISC — AI Governance
**Layer:** 3 (Application)
**Status:** Conceptual
**Target Venue:** Nature Machine Intelligence / AI & Society / ACM FAccT
**Est. Length:** TBD
**Dependencies:** Paper 0 published

---

## Abstract

Every major AI governance framework — Constitutional AI (Anthropic), the NIST AI Risk Management Framework, the EU AI Act, IEEE Ethically Aligned Design — operates as policy, guidelines, or regulation. Each specifies what AI systems should do or avoid doing; none is grounded in a falsifiable physical law with an empirical record. Commitment Theory is the first AI governance framework grounded in an empirically falsifiable conservation law. This paper conducts a systematic comparison of CT against the four major governance frameworks on five dimensions: (1) the level at which governance operates (system vs. transformation), (2) the empirical grounding of the framework's claims (falsifiable vs. normative), (3) the measurement protocol for compliance verification (operational vs. procedural), (4) the prediction the framework makes about ungoverned systems (quantitative vs. qualitative), and (5) the falsification conditions (specified vs. unspecified). The comparison reveals CT's categorical distinction: CT does not compete with Constitutional AI or NIST AI RMF at the policy level — it operates at the level of physical law that these policy frameworks must be consistent with, the same way thermodynamics constrains engine design policy without replacing it. The governance literature's missing variable: all current frameworks govern the system; CT governs the transformation. The paper also addresses the question of whether CT's governance requirements are compatible with existing frameworks, demonstrating that any system satisfying Constitutional AI, NIST AI RMF, or EU AI Act requirements could satisfy them while also failing CT's conservation law — meaning the existing frameworks are insufficient rather than competing.

---

## Outline

I. **Introduction: The Missing Foundation** — Frames the gap in AI governance: all existing frameworks are normative; none is grounded in a falsifiable physical law; CT fills this gap.

II. **Review of the Major Frameworks** — Systematically describes Constitutional AI, NIST AI RMF, EU AI Act, and IEEE Ethically Aligned Design; identifies their governance level, empirical grounding, measurement protocol, predictions, and falsification conditions (or lack thereof).

III. **CT's Framework: The Conservation Law as Governance Foundation** — Presents CT's governance framework in terms comparable to the existing frameworks; describes the Conservation Law, governance density bound, CCR, and MO§ES as CT's governance architecture.

IV. **Five-Dimension Comparison** — Applies the five comparison dimensions to all five frameworks (CT + four existing); presents the results in a structured comparison table; demonstrates CT's categorical distinction on each dimension.

V. **The Missing Variable: Governing the Transformation** — Develops the core argument: existing frameworks govern the system (what the AI does); CT governs the transformation (what happens to meaning when the AI does it); the two operate at different levels and are not in competition.

VI. **Compatibility and Sufficiency** — Demonstrates that satisfying existing governance frameworks is compatible with violating CT's Conservation Law; therefore, existing frameworks are insufficient (they do not require commitment conservation) rather than competing (they do not address the same governance level).

VII. **Conclusion: What the Governance Literature Needs** — Argues that the AI governance field needs a physical-law-grounded foundation; CT provides it; the existing frameworks should be built on top of it rather than treated as sufficient on their own.

---

## Key Claims

- CT is the first AI governance framework grounded in an empirically falsifiable conservation law with a public empirical record; all existing major frameworks are normative policy documents.
- The missing variable in all existing governance frameworks is the transformation level: they govern what the AI system does (system-level), not what happens to meaning when it does it (transformation-level).
- Existing governance frameworks are insufficient rather than competing with CT: a system can satisfy Constitutional AI, NIST AI RMF, or EU AI Act requirements while violating CT's Conservation Law.
- CT operates at the physical-law level that constrains policy; existing frameworks operate at the policy level; the relationship is analogous to thermodynamics and engine design policy — the law constrains the policy without replacing it.
- CT's comparative position can be stated precisely: CT is not a better AI governance policy than Constitutional AI or NIST AI RMF; it is the foundation that any adequate AI governance policy must be consistent with.

---

## Writing Notes

**Related Work (required for FAccT / AI & Society):**

- Jobin et al. (2019): inventory of 84 AI ethics guidelines — the largest meta-analysis of AI governance frameworks; CT's contribution is providing the physical-law foundation that none of these frameworks have
- Hagendorff (2020): "The Ethics of AI Ethics" — critiques the gap between principles and implementation; CT addresses this gap with a measurable standard
- Raji et al. (2020) on model cards / audit frameworks; Gebru et al. on data sheets — these are documentation standards; CT is a measurement standard; complementary, not competing
- Doshi-Velez & Kim (2017) on interpretability — interpretability addresses the "why" question; CT addresses the "what was preserved" question; different but related

**Section VI — the worked example is the paper's falsifiable contribution:**
Identify a real or realistic AI system that satisfies all of Constitutional AI, NIST AI RMF, and EU AI Act requirements while producing measurable commitment drift. Candidate: a summarization system for legal documents that (1) has been evaluated on constitutional AI principles (helpful, harmless, honest), (2) passes NIST AI RMF's risk management documentation requirements, (3) complies with EU AI Act's transparency requirements — but (4) when applied to a civil rights statute, produces the exception dropping failure mode. Show this with a concrete example using the CT harness. This is the paper's empirical contribution.

**Title: do not use "The Only Governance Framework with a Law" even as a subtitle or section heading.** The new title ("Governing the Transformation") is correct. Do not reintroduce the old framing anywhere in the paper.

## Citation Notes

- **Cites:** Paper 0 (Conservation Law, empirical record); Paper 3 (governance density bound); MO§ES architecture paper (CT governance architecture); P-000 (CT definitions); Bai et al. (Constitutional AI, 2022); NIST AI RMF (2023); EU AI Act (2024); IEEE Ethically Aligned Design; Post-Turing paper (CT evaluation criterion); L-003 (CCR as legal governance standard)
- **Cited by:** CAP-002 (monograph AI governance chapter); L-004 (policy brief uses GOV-001's comparative analysis)
