# CL-001 — Nine Ways Meaning Breaks: A Taxonomy of Commitment Degradation Under Recursive Language Transformation

**Track:** MISC — Computational Linguistics
**Layer:** 3 (Application)
**Status:** Data complete — can write now
**Target Venue:** Computational Linguistics (MIT Press) / Transactions of the ACL / EMNLP
**Est. Length:** 8,000–12,000 words
**Dependencies:** Paper 0 published

---

## Abstract

We present a systematic taxonomy of nine failure modes through which AI language transformation degrades the commitment kernel of semantic objects — the deontic content that constitutes a text's action-binding meaning. The taxonomy is derived from seven experiments (EXP-001 through EXP-007) conducted using the CT measurement harness and formalized by the Conservation Law of Commitment (Paper 0). The nine modes are: obligation escalation (discretionary becomes mandatory), scope widening (narrow prohibition becomes broad ban), exception dropping (statutory defense or limiting clause disappears), modal flattening ("shall not unless" becomes "should not" becomes "may not"), threshold erasure (quantitative triggers removed), agent substitution (the specified party replaced by an unspecified one), negation reversal (prohibition's negation eliminated at the semantic level while surface plausibility is preserved), compression collapse (commitment kernel lost when representation length crosses the fidelity bound), and recursion drift (cumulative decay across transformation steps). For each mode, we provide: a formal characterization using the CT framework, empirical evidence from the experimental record, a detection protocol using the CT measurement harness, and an analysis of why standard NLI and surface-level metrics fail to detect it. The taxonomy's key contribution to computational linguistics is the demonstration that NP-negation failure mode (negation reversal) is invisible to Jaccard similarity and can persist even when NLI bidirectional entailment scores remain at 1.00 — a result with significant implications for semantic evaluation methodology.

---

## Outline

I. **Introduction: The Problem of Invisible Degradation** — Frames the taxonomy as a response to a methodological gap: standard NLP evaluation metrics do not detect commitment degradation; the failure modes are invisible to surface-level analysis.

II. **Background: Commitment Kernel and the Conservation Law** — Introduces the CT framework (commitment kernel, conservation law, oracle) at a level appropriate for a computational linguistics audience; situates CT within NLP's existing semantic frameworks (NLI, FactBank, CommitmentBank).

III. **Failure Modes 1–3: Deontic Scope Failures** — Formally characterizes obligation escalation, scope widening, and exception dropping; reports empirical evidence and detection protocol for each.

IV. **Failure Modes 4–6: Modal and Relational Failures** — Formally characterizes modal flattening, threshold erasure, and agent substitution; reports empirical evidence and detection protocol for each; discusses the implications for modal logic and semantic role labeling.

V. **Failure Modes 7–9: Structural and Cumulative Failures** — Formally characterizes negation reversal (EXP-007 NP-negation probe), compression collapse (EXP-003 compression-boundary signals), and recursion drift (EXP-003 10-step recursion); reports empirical evidence for each; demonstrates why negation reversal is invisible to surface metrics.

VI. **Implications for NLP Evaluation Methodology** — Argues that the failure taxonomy reveals a systematic gap in standard NLP evaluation: metrics that measure surface similarity or sentence-level entailment miss commitment-level degradation; proposes commitment-aware evaluation as a necessary complement.

VII. **Conclusion** — Summarizes the taxonomy and its implications; releases the detection protocol and experimental data; invites replication and extension.

---

## Key Claims

- The nine failure modes are empirically documented patterns of commitment degradation, each with a formal characterization, an experimental evidence base, and a detection protocol.
- Negation reversal (failure mode 7) is specifically invisible to surface-level metrics: Jaccard similarity degrades while NLI bidirectional entailment remains at 1.00, confirming that the degradation operates at the commitment level rather than the surface level.
- Standard NLP evaluation metrics (BLEU, ROUGE, METEOR, BERTScore, sentence-level NLI) do not detect commitment degradation; commitment-aware evaluation is a necessary complement for tasks that require semantic fidelity.
- Recursion drift (failure mode 9) is cumulative: it compounds across transformation steps, meaning that single-step evaluation is insufficient for multi-step AI pipelines.
- The failure taxonomy provides a shared vocabulary for computational linguists, legal practitioners, and AI system designers to identify and communicate about specific types of semantic degradation.

---

## Citation Notes

- **Cites:** Paper 0 (Conservation Law, failure taxonomy, EXP-001 through EXP-007, NP-negation probe); P-000 (CT definitions); de Marneffe et al. CommitmentBank; Saurí & Pustejovsky FactBank; Bowman et al. SNLI; Nie et al. (NLI evaluation); microsoft/deberta-v3-base-mnli
- **Cited by:** CL-002 (regime classification builds on failure mode taxonomy); L-005 (legal failure modes paper cites CL-001 as the NLP-domain parallel); IS-001 (information science preservation paper uses failure taxonomy); CAP-001 (channel capacity capstone)
