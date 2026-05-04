# L-002 — Commitment Drift in Civil Rights Statutes Under Recursive AI Transformation: An Empirical Study

**Track:** Legal_Theory
**Layer:** 3 (Application — Empirical)
**Status:** Planned — Summer 2026 — corpus construction is the critical path item
**Target Venue:** Journal of Empirical Legal Studies / Jurimetrics
**Est. Length:** 8,000–12,000 words
**Dependencies:** L-001 submitted; legal signal corpus (see Corpus Plan below); legal collaborator beneficial
**Downstream dependents:** L-003, L-005, L-007, L-010 all require L-002 data — corpus slip = four papers slip

---

## Abstract

This paper reports the first systematic empirical study of commitment drift in civil rights statutes under recursive AI transformation. Using the CT measurement harness (Paper 0; Paper 5 framework) and a corpus of civil rights statutory provisions drawn from Title VII, the ADA, the Fair Housing Act, the Voting Rights Act, and Section 1983, we measure the commitment kernel C(S) of each provision before and after AI transformation sequences of varying depth and governance condition. For each provision, we apply both governed transformation (Six-Gate Protocol) and ungoverned transformation and report the commitment conservation rate. We identify which statutory provisions are most vulnerable to commitment drift — those whose commitment kernels are carried by modal operators (obligation escalation, modal flattening failure modes) versus those carried by relational predicates — and we characterize the relationship between provision length, modal structure, and vulnerability to each of the nine failure modes. Key findings: modal-anchored civil rights provisions (carrying "shall not," "must," "is entitled to") achieve high conservation rates under governance; compression-boundary provisions (long provisions with complex exception structures) show the sharpest conservation/loss boundary; and negation-carrying provisions (those whose commitment kernel is carried by negation: "shall not discriminate") are specifically vulnerable to the negation reversal failure mode (EXP-007). Results establish an empirical foundation for L-003's technical standard proposal and provide the evidence base for L-004's policy brief.

---

## Outline

I. **Introduction** — Frames the study as the first empirical measurement of commitment drift in civil rights statutes; explains the significance of moving from hypothetical to measured.

II. **Legal Signal Corpus** — Describes the corpus construction: statutory provision selection criteria, corpus size, provision categorization (modal-anchored, relational-structural, compression-boundary), and sampling methodology.

III. **Measurement Protocol** — Describes the application of the CT harness to the legal corpus; explains governed vs. ungoverned transformation conditions; defines transformation depth and iteration count.

IV. **Results: Conservation Rates by Provision Type** — Reports commitment conservation rates for each provision category under governed and ungoverned transformation; identifies the provisions most and least vulnerable to each failure mode.

V. **Results: Failure Mode Distribution** — Maps the nine failure modes onto the legal corpus; identifies which modes are most common in civil rights statutes and which are most legally consequential (e.g., negation reversal of "shall not discriminate").

VI. **Analysis: Legal Implications of the Empirical Record** — Connects the empirical results to specific doctrinal concerns: which failure modes implicate due process, which implicate disparate impact, which implicate evidentiary reliability.

VII. **Conclusion** — Summarizes the evidence and its implications for L-003 (technical standard) and L-004 (policy brief); identifies the methodological limitations and directions for replication.

---

## Key Claims

- Civil rights statutory provisions exhibit measurable, consistent patterns of commitment drift under ungoverned AI transformation — this is an empirical fact, not a theoretical prediction.
- Modal-anchored provisions (carrying "shall not," "must," "is entitled to") are most vulnerable to modal flattening and obligation escalation; they achieve high conservation rates under CT governance but collapse rapidly without it.
- Negation-carrying provisions (the core of antidiscrimination law: "shall not discriminate") are specifically vulnerable to negation reversal — the failure mode identified in EXP-007 — which is invisible to surface-level lexical analysis.
- Compression-boundary provisions (complex statutory provisions with multiple exception clauses) show the sharpest conservation/loss boundary and the highest rate of exception dropping under compression.
- The empirical record maps directly onto established legal harm categories: each failure mode corresponds to a measurable legal harm type that existing doctrine already recognizes.

---

## Corpus Plan — Must Be Executed Before Writing Begins

This is the highest-priority planning gap in the entire Legal Theory track. L-003, L-005, L-007, and L-010 all depend on this corpus. Build it first.

### Target Size
40–60 provisions across five statutes. Minimum 8 provisions per statute to ensure statistical power for failure mode distribution analysis.

### Selection Criteria
Include all provisions that contain at least one of the following modal/deontic markers:
- "shall" / "shall not"
- "must" / "must not"
- "is entitled to" / "is not entitled to"
- "may not" / "may"
- "is prohibited from"
- "is required to"
- "unless" (as a commitment-qualifying exception clause)

Exclude purely definitional provisions (those that define terms without imposing obligations or prohibitions) and procedural provisions (those governing filing deadlines, jurisdictional rules, etc.) unless they contain the above markers.

### Statute Coverage
| Statute | Target Provisions | Priority Sections |
|---------|-------------------|-------------------|
| Title VII (42 U.S.C. § 2000e et seq.) | 10–12 | §703 (unlawful employment practices), §704 (discrimination against applicant) |
| ADA (42 U.S.C. §§ 12101–12213) | 10–12 | §12112 (discrimination prohibited), §12111(9) (reasonable accommodation definition) |
| Fair Housing Act (42 U.S.C. §§ 3601–3631) | 8–10 | §3604 (prohibited practices), §3605 (financial practices) |
| Voting Rights Act (52 U.S.C. §§ 10301–10314) | 8–10 | §10301 (denial of voting rights), §10302 (remedies) |
| Section 1983 (42 U.S.C. § 1983) | 6–8 | The provision itself + leading interpretive standards from case law (Monell, qualified immunity) |

### Classification Protocol (Three-Regime Taxonomy from CL-002)
Each provision is classified into one of three regimes before running through the harness:
1. **Modal-anchored** — kernel carried by modal operators ("shall not," "must," "is entitled to")
2. **Relational-structural** — kernel carried by relational predicates ("discriminates against," "has a right to")
3. **Compression-boundary** — kernel carried by exception clauses or threshold specifications sensitive to length

Classification is performed before harness runs to avoid contamination. Use two independent classifiers; resolve disagreements through discussion before running.

### Harness Protocol
For each provision:
- 5 governed transformation iterations (Six-Gate Protocol)
- 5 ungoverned transformation iterations (same model, no gates)
- 3 models minimum (GPT-4, Claude, one open-source model)
- Record: C(S) before, C(S) after each iteration, NLI score, failure mode if applicable

### L-002 / L-005 Merge Decision
Decide before corpus construction begins: are these one paper or two?
- If **merged**: L-002 includes the full failure mode taxonomy in Section V; L-005 is dropped
- If **separate**: L-002's Section V reports failure mode distribution only; L-005 is a standalone paper with extended legal framing per mode
- Recommendation: merge for now (scope L-002 to include failure modes); split only if the paper runs over 12,000 words

### Collaborator Requirements
For JELS submission, the corpus selection methodology and statutory interpretation should be reviewed by a legal collaborator. Specifically: the classification of provisions into regimes requires legal judgment about what constitutes the "commitment kernel" of a given civil rights provision. This is not purely a computational task.

---

## Citation Notes

- **Cites:** Paper 0 (Conservation Law, failure taxonomy, EXP-007); Paper 5 (measurement instrument framework); L-000 (legal propositions); L-001 (doctrinal framework); P-000 (CT definitions); Title VII, 42 U.S.C. § 2000e; ADA, 42 U.S.C. § 12101; Fair Housing Act, 42 U.S.C. § 3601; Voting Rights Act, 52 U.S.C. § 10301
- **Cited by:** L-003 (technical standard uses L-002 empirical evidence); L-004 (policy brief); L-005 (may merge with or cite L-002); L-007 (full legal paper); L-010 (Daubert/authentication paper uses L-002 data); ECON-001 (economic model uses L-002 as empirical foundation)
