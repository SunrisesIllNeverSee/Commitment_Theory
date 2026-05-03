# Layer 4 — SIGSYSTEM: A Next-Generation Commitment Fidelity Oracle Based on Contextual Word Weighting

**Track:** CT
**Layer:** 4 (Extension)
**Status:** Early development
**Target Venue:** Philosophy of Information / AI venues
**Est. Length:** TBD
**Dependencies:** Papers 1–5 complete; MO§ES architecture paper

---

## Abstract

The CT measurement harness (Paper 5) uses NLI bidirectional entailment as its oracle — a scientifically defensible choice with characterized limitations. SIGSYSTEM is its designed successor: a commitment fidelity oracle based on contextual word weighting that operates at the word level rather than the sentence level. The core insight motivating SIGSYSTEM is that not all words contribute equally to the commitment kernel. In any semantic object, some words are signal — they carry deontic content, modal force, or relational structure that constitutes the commitment kernel — and some words are noise — they contribute to fluency, register, and surface form without contributing to the commitment kernel. Existing language models cannot separate signal from noise because they are trained to predict both simultaneously. SIGSYSTEM addresses this by weighting each word by its contextual signal contribution to the commitment kernel, enabling a more precise measurement of C(S) than is possible with sentence-level NLI. SIGSYSTEM is distinct from SIGRANK, which operates at the behavioral/message level; SIGSYSTEM operates at the word level within a single semantic object. The full architecture of SIGSYSTEM is trade secret; this paper describes the theoretical framework, the evaluation methodology, and the performance results relative to the NLI baseline established in Papers 0 and 5. The paper also describes SIGSYSTEM's role as the oracle within the MO§ES enforcement architecture.

---

## Outline

I. **Introduction: The Limits of Sentence-Level Oracles** — Describes the specific limitations of the NLI-based oracle identified in Paper 5 (noise floor, adversarial sensitivity to surface-level manipulation) and motivates the word-level approach.

II. **The Signal/Noise Distinction in Semantic Objects** — Formalizes the distinction between signal words (deontic-content-carrying) and noise words (fluency/register-contributing); argues this distinction is the missing variable in current NLI-based commitment measurement.

III. **SIGSYSTEM: Theoretical Framework** — Describes the theoretical framework for contextual word weighting without disclosing trade secret architectural details; explains how word-level signal scores aggregate to a sentence-level commitment measure.

IV. **Evaluation Methodology** — Describes the evaluation protocol for comparing SIGSYSTEM against the NLI baseline; uses the EXP-001 through EXP-007 data as a benchmark; introduces new adversarial probes designed specifically to stress-test word-level weighting.

V. **Results** — Reports SIGSYSTEM's performance relative to the NLI baseline on the standard benchmark and on the new adversarial probes; characterizes the specific improvements in noise floor and adversarial sensitivity.

VI. **SIGSYSTEM within MO§ES** — Describes SIGSYSTEM's role as the real-time oracle within the MO§ES enforcement architecture; explains the latency, throughput, and accuracy requirements that SIGSYSTEM must satisfy in a production deployment.

VII. **Implications for CT's Measurement Science** — Discusses how SIGSYSTEM's improved sensitivity changes the empirical picture of commitment conservation; identifies which prior results from Papers 1–5 are strengthened, refined, or complicated by SIGSYSTEM measurements.

---

## Key Claims

- Not all words contribute equally to the commitment kernel; SIGSYSTEM weights words by their contextual signal contribution to deontic content, enabling more precise commitment measurement than sentence-level NLI.
- The signal/noise distinction at the word level is the missing variable that explains why NLI-based oracles have a non-zero noise floor and specific adversarial vulnerabilities identified in Paper 5.
- SIGSYSTEM achieves a lower noise floor and higher adversarial sensitivity than the NLI baseline, as demonstrated on the EXP-001 through EXP-007 benchmark and on new adversarial probes.
- SIGSYSTEM is distinct from SIGRANK: SIGRANK operates at the behavioral/message level; SIGSYSTEM operates at the word level within a single semantic object.
- The full SIGSYSTEM architecture is trade secret; the paper's contribution is the theoretical framework, evaluation methodology, and performance results — sufficient for scientific replication with a different implementation.

---

## Citation Notes

- **Cites:** Paper 0 (Conservation Law, oracle design, EXP-001 through EXP-007); Paper 5 (Measurement Instrument, noise floor characterization, oracle independence analysis); MO§ES architecture paper (SIGSYSTEM role within MO§ES); P-000 (CT definitions)
- **Cited by:** MO§ES architecture paper (SIGSYSTEM is the MO§ES oracle); Layer 4 Post-Turing paper (SIGSYSTEM enables the Post-Turing Test measurement protocol); Layer 4 Channel Capacity paper (SIGSYSTEM provides the more precise C(S) measurements needed for the capacity theorem)
