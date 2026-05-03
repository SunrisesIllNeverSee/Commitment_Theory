# L-010 — Evidentiary Authentication in the Age of AI: Applying Daubert and FRE 901 to AI-Transformed Legal Texts

**Track:** Legal_Theory
**Layer:** 3 (Application — Evidence Law)
**Status:** Conceptual — collaborator-led
**Target Venue:** General law reviews
**Est. Length:** 8,000–15,000 words
**Dependencies:** L-002 empirical data; legal collaborator as primary author

---

## Abstract

AI systems routinely transform legal texts — contracts, statutes, regulations, judicial opinions, administrative records — before those texts enter legal proceedings. The evidentiary authenticity of AI-transformed legal texts has not been systematically analyzed under FRE 901 (authentication) or the Daubert standard for scientific reliability. This paper applies both frameworks to AI-transformed legal texts and argues that commitment conservation — in the CT sense, C(T_gov(S)) = C(S) — is a necessary condition for evidentiary authenticity and scientific reliability in this context. Under FRE 901, a document is authenticated when it is "what the proponent claims it is." An AI-transformed legal text that has suffered commitment drift is not what the proponent claims it is: its commitment kernel — the deontic content that the text was adduced to prove — has been altered. Under Daubert, expert testimony regarding AI-transformed legal texts must satisfy the reliability requirements of falsifiability, peer review, known error rate, and general acceptance. The CT measurement harness satisfies all four: the Conservation Law is falsifiable, Paper 0 is peer-reviewed (or under review), the failure taxonomy provides an error rate framework, and the empirical record establishes a basis for general acceptance. The paper proposes a commitment conservation authentication standard — an operational test that courts and practitioners can apply to AI-transformed legal texts — and addresses the objections from courts skeptical of novel evidentiary standards.

---

## Outline

I. **Introduction: The Authentication Gap** — Frames the evidentiary gap: courts lack an authentication standard for AI-transformed legal texts; existing standards (chain of custody, digital forensics) do not address semantic drift.

II. **FRE 901 and the Identity of AI-Transformed Legal Texts** — Analyzes FRE 901's authentication requirement; demonstrates that commitment drift means an AI-transformed legal text may not be "what the proponent claims it is" at the semantic level even if it is authentic at the documentary level.

III. **Daubert and the Scientific Reliability of Commitment Measurement** — Applies Daubert's four factors to the CT measurement harness; demonstrates that the harness satisfies falsifiability, peer review, known error rate, and general acceptance requirements.

IV. **The Commitment Conservation Authentication Standard** — Proposes a concrete operational standard: an AI-transformed legal text is authentically the text it purports to be if and only if C(T_gov(S)) = C(S), verified by an oracle satisfying the Paper 5 framework, with an auditable Lineage DAG.

V. **Failure Mode Taxonomy as Evidentiary Framework** — Applies the nine failure modes as categories of evidentiary defect; demonstrates that each failure mode corresponds to a specific FRE 901 or Daubert concern.

VI. **Objections and Replies** — Addresses objections from courts skeptical of novel evidentiary standards; from parties who argue commitment measurement is too technical for lay juries; from those who argue the standard imposes excessive pre-admission burdens.

VII. **Conclusion** — Summarizes the authentication standard and its doctrinal basis; calls for early adoption in federal rulemaking or model rules development.

---

## Key Claims

- Commitment drift in AI-transformed legal texts constitutes an FRE 901 authentication failure: the document is not "what the proponent claims it is" if its commitment kernel has been altered by AI transformation.
- The CT measurement harness satisfies Daubert's four scientific reliability factors: the Conservation Law is falsifiable, the paper record is peer-reviewed, the failure taxonomy provides an error rate framework, and the empirical record establishes general acceptance grounds.
- A commitment conservation authentication standard — C(T_gov(S)) = C(S) verified by a Daubert-qualified oracle — provides courts with an operationally precise test for AI-transformed text authenticity.
- The nine failure modes map directly onto specific FRE 901 and Daubert concerns, providing a failure-mode-to-evidentiary-defect framework that courts and practitioners can apply.
- The authentication standard is achievable: MO§ES-compliant systems produce Fidelity Seals and Lineage DAGs that satisfy the standard's requirements, making CCR-compliant AI systems automatically capable of producing authenticatable outputs.

---

## Citation Notes

- **Cites:** Paper 0 (Conservation Law, failure taxonomy, EXP-007); Paper 5 (Measurement Instrument, Daubert factors analysis); L-000 (legal propositions); L-001 (doctrinal entry point); L-002 (empirical data on legal signal corpus); L-003 (CCR standard); L-005 (nine failure modes); MO§ES architecture paper (Fidelity Seal and Lineage DAG); FRE 901; Daubert v. Merrell Dow Pharmaceuticals, 509 U.S. 579 (1993); Kumho Tire Co. v. Carmichael, 526 U.S. 137 (1999)
- **Cited by:** L-008 (capstone synthesizes L-010's evidentiary analysis into the jurisprudence of the record); CAP-002 (monograph)
