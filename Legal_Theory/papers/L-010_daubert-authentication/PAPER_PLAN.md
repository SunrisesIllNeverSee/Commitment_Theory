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

## Writing Notes

**Kumho Tire — add to Section III alongside Daubert:**
Daubert applies to scientific expert testimony; Kumho Tire Co. v. Carmichael, 526 U.S. 137 (1999) extends the reliability inquiry to all expert testimony, including technical and specialized knowledge. The CT measurement harness is both scientific (falsifiable conservation law) and technical (NLI oracle, harness implementation). Section III must engage both Daubert and Kumho Tire to cover the full scope of the reliability inquiry. This is not optional — a paper on evidentiary authentication that cites Daubert without Kumho Tire will be flagged by law review editors.

**CL-track prerequisite — Paper 5 must exist before L-010:**
L-010's Daubert argument depends on the CT harness being characterized as a scientific instrument with known error rates, calibration standards, and reproducibility data. That characterization is Paper 5's contribution. L-010 cannot credibly make the Daubert reliability argument without citing Paper 5's metrology framework. **Status gate: do not begin writing L-010 until Paper 5's harness characterization (at minimum the GUM uncertainty framework and the EXP-006 reframing) is complete.**

**Division of labor — legal collaborator as primary author:**
L-010 is listed as "collaborator-led." The collaborator should handle: FRE 901 doctrinal analysis (Section II), Daubert/Kumho Tire analysis (Section III), objections and replies (Section VI), and the authentication standard proposal (Section IV). The CT author provides: the technical description of the harness (Section III subsection), the failure-mode-to-evidentiary-defect mapping (Section V), and the MO§ES/Fidelity Seal operational specification (Section IV subsection). This division ensures the paper reads as a legal paper with technical support, not a technical paper with legal dressing.

**MO§ES citability — Key Claim 5 vulnerability:**
Key Claim 5 states "MO§ES-compliant systems produce Fidelity Seals and Lineage DAGs that satisfy the standard's requirements." If the MO§ES architecture paper has not been published or deposited when L-010 is written, this claim is unverifiable. Options: (a) deposit the MO§ES architecture paper before L-010; (b) describe the Fidelity Seal and Lineage DAG functionally in L-010 without citing MO§ES by name; (c) cite the patent application (Serial No. 63/877,177) for the architecture specification. Option (b) is safest for a law review audience.

**Peer review status — same gate as L-006:**
L-010's Daubert argument (Section III) depends on CT's empirical record being peer-reviewed. The same status gate applies: do not submit L-010 until Paper 0 has achieved formal peer review at a recognized venue. If writing before peer review, rely on Daubert's other three factors and state that peer review is pending.

---

## Citation Notes

- **Cites:** Paper 0 (Conservation Law, failure taxonomy, EXP-007); Paper 5 (Measurement Instrument, Daubert factors analysis); L-000 (legal propositions); L-001 (doctrinal entry point); L-002 (empirical data on legal signal corpus); L-003 (CCR standard); L-005 (nine failure modes); MO§ES architecture paper (Fidelity Seal and Lineage DAG); FRE 901; Daubert v. Merrell Dow Pharmaceuticals, 509 U.S. 579 (1993); Kumho Tire Co. v. Carmichael, 526 U.S. 137 (1999)
- **Cited by:** L-008 (capstone synthesizes L-010's evidentiary analysis into the jurisprudence of the record); CAP-002 (monograph)
