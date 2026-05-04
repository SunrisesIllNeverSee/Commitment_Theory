# CL-001 — Nine Ways Meaning Breaks: A Taxonomy of Commitment Degradation Under Recursive Language Transformation

**Track:** MISC — Computational Linguistics
**Layer:** 3 (Application)
**Status:** Data complete — can write now
**Target Venue:** Computational Linguistics (MIT Press) / Transactions of the ACL / EMNLP
**Est. Length:** 8,000–12,000 words
**Dependencies:** Paper 0 published

---

## Abstract

NP-negation reversal — a commitment failure mode invisible to Jaccard similarity — persists even when NLI bidirectional entailment scores remain at 1.00, a result that reveals a systematic gap in standard semantic evaluation methodology. This paper presents a taxonomy of nine failure modes through which AI language transformation degrades the commitment kernel of semantic objects — the deontic content that constitutes a text's action-binding meaning. The taxonomy is derived from seven experiments (EXP-001 through EXP-007) conducted using the CT measurement harness and formalized by the Conservation Law of Commitment (Paper 0). The nine modes are: obligation escalation (discretionary becomes mandatory), scope widening (narrow prohibition becomes broad ban), exception dropping (statutory defense or limiting clause disappears), modal flattening ("shall not unless" becomes "should not" becomes "may not"), threshold erasure (quantitative triggers removed), agent substitution (the specified party replaced by an unspecified one), negation reversal (prohibition's negation eliminated at the semantic level while surface plausibility is preserved), compression collapse (commitment kernel lost when representation length crosses the fidelity bound), and recursion drift (cumulative decay across transformation steps). For each mode, we provide: a formal characterization using the CT framework, empirical evidence from the experimental record, a detection protocol using the CT measurement harness, and an analysis of why standard NLI and surface-level metrics fail to detect it. The taxonomy's key contribution to computational linguistics is providing a detection protocol and formal characterization for each mode — including failure modes that standard NLG evaluation metrics (ROUGE, BERTScore, Jaccard) cannot detect — with direct implications for semantic evaluation methodology and NLP system design.

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

## Writing Notes

**Related Work (required for CL / TACL / EMNLP):**

- CommitmentBank (de Marneffe et al. 2019): annotates speaker commitment to embedded clauses — distinguish from CT's signal-deontic commitment in one sentence, then move on
- FactBank (Saurí & Pustejovsky 2009): factual status annotation — same distinction
- NLI benchmarks: SNLI (Bowman et al. 2015), MultiNLI (Williams et al. 2018) — CT uses NLI as an oracle but measures something these benchmarks don't test
- Faithfulness in NLG: Maynez et al. (2020), Honovich et al. (2022) on factual consistency — closest existing work; CT's negation reversal (EXP-007) shows a failure mode these metrics miss
- BERTScore (Zhang et al. 2020): surface similarity metric — EXP-007 demonstrates BERTScore and Jaccard both miss negation reversal; show this with a concrete example in the paper

**Section VI — propose a specific evaluation protocol:**
Do not end with "existing metrics miss commitment degradation." End with a positive contribution: a proposed evaluation protocol. Specifically:

1. Run the full signal through the CT harness (NLI bidirectional) — this is the commitment fidelity score
2. Run ROUGE-L, BERTScore, Jaccard in parallel
3. Report correlation between CT harness score and each surface metric
4. For the negation reversal case: show a signal where ROUGE-L ≈ 0.9, BERTScore ≈ 0.85, Jaccard ≈ 0.8, but CT harness = 0 (commitment lost)

This turns Section VI from a critique into a methodological contribution — an evaluation protocol that NLP systems can adopt.

**Self-contained definition of commitment kernel:**
CL-001 will circulate independently of Paper 0. Define the commitment kernel in Section II in full: "The commitment kernel C(S) of a semantic object S is its deontic content — the set of obligations, prohibitions, permissions, and modal constraints that S imposes, independent of its speaker, context, or surface form." Then cite Paper 0 for the full formal treatment.

## Citation Notes

- **Cites:** Paper 0 (Conservation Law, failure taxonomy, EXP-001 through EXP-007, NP-negation probe); P-000 (CT definitions); de Marneffe et al. CommitmentBank; Saurí & Pustejovsky FactBank; Bowman et al. SNLI; Nie et al. (NLI evaluation); microsoft/deberta-v3-base-mnli
- **Cited by:** CL-002 (regime classification builds on failure mode taxonomy); L-005 (legal failure modes paper cites CL-001 as the NLP-domain parallel); IS-001 (information science preservation paper uses failure taxonomy); CAP-001 (channel capacity capstone)
