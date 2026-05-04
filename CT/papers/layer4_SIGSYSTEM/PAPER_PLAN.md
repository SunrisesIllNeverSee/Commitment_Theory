# Layer 4 — SIGSYSTEM: A Next-Generation Commitment Fidelity Oracle Based on Contextual Word Weighting

**Track:** CT
**Layer:** 4 (Extension)
**Status:** NOT IN ACTIVE QUEUE — trade secret conflict unresolved; early development
**Target Venue:** TBD — must resolve publication strategy before targeting a venue
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

## Blocking Decision — Publication Strategy

A peer-reviewed paper cannot withhold its central contribution's architecture while claiming academic review. The three options below are mutually exclusive — one must be chosen before SIGSYSTEM enters any publication queue.

**Option A: Publish theoretical framework only — no performance claims**
- Describe the signal/noise distinction (Section II) and the theoretical weighting framework (Section III) fully
- Remove Sections IV–V (evaluation + results) — no performance claims without architecture disclosure
- Contribution: a theoretical paper proposing word-level commitment measurement as a research direction
- Venue: Philosophy of Information, Minds and Machines, or a workshop paper at ACL/EMNLP
- IP risk: LOW — theory papers do not disclose implementation; architecture remains trade secret
- Weakness: reviewers cannot verify the performance claims; paper makes no empirical contribution beyond the theory

**Option B: File patent first, then publish fully**
- Complete SIGSYSTEM development and file a patent application covering the architecture
- After patent publication (18 months post-filing for PCT), publish the full paper including architecture details
- Contribution: a complete empirical paper with architecture, evaluation, and results
- Venue: any AI venue (NeurIPS, ICML, TACL, JAIR) — full peer review possible
- IP risk: LOW — patent filing establishes priority; publication after patent publication is standard practice
- Weakness: delays publication by 18–24 months from current status; MO§ES paper's SIGSYSTEM section must also be held until then

**Option C: Treat SIGSYSTEM as internal MO§ES component only — no standalone paper**
- Remove SIGSYSTEM from the academic publication pipeline entirely
- Describe SIGSYSTEM functionally in the MO§ES architecture paper (Section VI) without claiming it as a separate academic contribution
- Contribution: MO§ES paper gets a stronger functional description; SIGSYSTEM's existence is disclosed but not characterized academically
- IP risk: LOWEST — no academic disclosure at all; full trade secret protection
- Weakness: loses the academic credit for SIGSYSTEM; the word-level signal/noise insight is a genuine theoretical contribution that goes unclaimed in the literature

**Recommended decision point:** If SIGSYSTEM development is 6+ months from completion, Option C is most practical for near-term publication momentum. If SIGSYSTEM is near completion, Option B preserves the full academic contribution. Option A is a reasonable interim step if theoretical development is complete but implementation is not.

**Key Claim 3 reclassification:** "SIGSYSTEM achieves a lower noise floor and higher adversarial sensitivity than the NLI baseline" is currently stated as a Key Claim. This is a hypothesis — the data does not yet exist. Reclassify as hypothesis until Option B's evaluation (Section V) is run.

---

## Citation Notes

- **Cites:** Paper 0 (Conservation Law, oracle design, EXP-001 through EXP-007); Paper 5 (Measurement Instrument, noise floor characterization, oracle independence analysis); MO§ES architecture paper (SIGSYSTEM role within MO§ES); P-000 (CT definitions)
- **Cited by:** MO§ES architecture paper (SIGSYSTEM is the MO§ES oracle); Layer 4 Post-Turing paper (SIGSYSTEM enables the Post-Turing Test measurement protocol); Layer 4 Channel Capacity paper (SIGSYSTEM provides the more precise C(S) measurements needed for the capacity theorem)
