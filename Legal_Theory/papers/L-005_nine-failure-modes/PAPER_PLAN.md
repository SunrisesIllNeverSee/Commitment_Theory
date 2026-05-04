# L-005 — Nine Failure Modes: How AI Transformation Degrades Legal Meaning

**Track:** Legal_Theory
**Layer:** 3 (Application — Taxonomy)
**Status:** Planned — Fall 2026 (may merge with L-002)
**Target Venue:** Law and Contemporary Problems (Duke) / Jurimetrics / Computer Law & Security Review
**Est. Length:** 6,000–8,000 words
**Dependencies:** Existing EXP-001–EXP-007 data; L-002 strengthens

---

## Abstract

The Conservation Law of Commitment identifies nine failure modes through which AI transformation degrades the commitment kernel of semantic objects. This paper applies that taxonomy systematically to the legal domain, demonstrating through statutory examples that each failure mode corresponds to a distinct and legally cognizable harm. The nine failure modes — obligation escalation, scope widening, exception dropping, modal flattening, threshold erasure, agent substitution, negation reversal, compression collapse, and recursion drift — are not abstract theoretical categories; they are empirically documented patterns of semantic degradation with specific legal consequences. Obligation escalation transforms a discretionary standard into a mandatory one, exposing regulated parties to obligations the statute did not create. Modal flattening converts "shall not" into "should not" into "may not," converting a prohibition into a preference into a permission. Negation reversal — identified through the NP-negation probe (EXP-007) — eliminates the negation from a prohibition at the semantic level while preserving surface plausibility, rendering it invisible to standard document review. Compression collapse eliminates statutory exception clauses during text reduction, making unavailable the statutory defenses that regulated parties depend on. For each failure mode, this paper identifies the doctrinal category most at risk (due process, disparate impact, evidentiary reliability), the statutory provisions most vulnerable, the detection method available using the CT harness, and the governance remedy. The paper is both a research contribution and a practical reference for legal practitioners and AI system designers working with legal text.

---

## Outline

I. **Introduction: Naming the Failures** — Argues that naming the failure modes is a necessary first step for legal and technical practitioners to identify, measure, and prevent commitment drift in AI-mediated legal processes.

II. **The Taxonomy and Its Empirical Basis** — Presents the nine failure modes as derived from the experimental record (EXP-001 through EXP-007); explains the detection methodology for each mode.

III. **Modes 1–3: Obligation and Scope Failures** — Analyzes obligation escalation (discretionary becomes mandatory), scope widening (narrow prohibition becomes broad ban), and exception dropping (statutory defense disappears); identifies affected doctrinal areas and statutory examples.

IV. **Modes 4–6: Modal and Threshold Failures** — Analyzes modal flattening ("shall not unless" becomes "should not" becomes "may not"), threshold erasure (quantitative triggers removed), and agent substitution ("the employer" becomes "any party"); connects each to specific doctrinal harms.

V. **Modes 7–9: Structural Failures** — Analyzes negation reversal (NP-negation probe, EXP-007 — semantically invisible), compression collapse (kernel lost at length threshold), and recursion drift (cumulative decay across transformation steps, EXP-003); discusses why these modes are the most legally dangerous.

VI. **Detection and Governance** — For each failure mode, describes the detection method available using the CT harness and the governance remedy; provides a failure-mode-to-governance-gate mapping.

VII. **Implications for Legal Practice and AI System Design** — Discusses how legal practitioners can use the taxonomy to audit AI systems operating on legal text; how AI system designers can use it to target governance resources at the highest-risk failure modes.

---

## Key Claims

- The nine failure modes are not theoretical categories — they are empirically documented patterns of semantic degradation with specific, legally cognizable consequences that map onto existing doctrinal harm categories.
- Negation reversal is the most legally dangerous failure mode: it eliminates the semantic content of a prohibition while preserving surface plausibility, rendering it invisible to standard document review and comprehensible only through commitment-level measurement.
- Each failure mode has a distinct detection method using the CT harness and a distinct governance remedy within the Six-Gate Protocol framework.
- Compression collapse and recursion drift are cumulative: they worsen with each transformation step, meaning that multi-step AI pipelines face compounding risk that single-step inspection cannot detect.
- The failure mode taxonomy gives legal practitioners and AI system designers a shared vocabulary for identifying and preventing specific types of commitment drift — a necessary precondition for meaningful AI governance in legal contexts.

---

## Writing Notes

**Section VI — operational proxy checks for practitioners:**
The paper cannot just say "use the CT harness." Law and Contemporary Problems serves practitioners. For each failure mode, provide a proxy check that does not require running the full CT harness:

- Obligation escalation: manually compare modal force of output vs. input ("shall" → "should" → "may")
- Scope widening: compare the range of actors/situations covered by input vs. output
- Exception dropping: check whether every "unless," "except," "provided that" clause in input appears in output
- Modal flattening: compare the strongest modal operator in input with the weakest in output
- Threshold erasure: check whether any numerical or categorical threshold in input is preserved in output
- Agent substitution: check whether the specified party in input matches the specified party in output
- Negation reversal: check whether every negated proposition in input is negated in output (this one requires attention — surface negation is not sufficient)
- Compression collapse: flag if output length < 60% of input length for provisions with complex exception structures
- Recursion drift: flag if the provision has been processed through multiple AI steps without a committed-to intermediate record

**"Most legally dangerous" claim — define the metric explicitly:**
Recommend a two-dimensional matrix: (x-axis) detection difficulty (1=easy to detect manually, 5=requires harness); (y-axis) severity of legal consequence (1=minor, 5=fundamental rights violation). Plot all nine modes. Negation reversal scores high on both — it is invisible to surface review and the consequence (prohibition becomes permission) is severe. This makes the claim defensible and turns it into a contribution.

**Related Work:**

- AI errors in legal document processing: Bommasani et al. (2021) Foundation Models report on legal applications; Chalkidis et al. on legal NLP benchmarks
- Statutory interpretation and AI: Katz et al. (2017) on computational legal analysis — CT's failure modes are systematic errors that these systems produce

## Citation Notes

- **Cites:** Paper 0 (Conservation Law, nine failure modes, EXP-001 through EXP-007, NP-negation probe); L-000 (legal propositions); L-001 (doctrinal framework); L-002 (empirical evidence for legal domain); P-000 (CT definitions)
- **Cited by:** L-003 (CCR standard uses failure mode taxonomy to specify compliance requirements); L-007 (full legal paper synthesizes failure mode analysis); L-010 (Daubert paper uses failure mode taxonomy for evidentiary reliability analysis); CL-001 (computational linguistics failure mode taxonomy is the NLP-domain parallel)
