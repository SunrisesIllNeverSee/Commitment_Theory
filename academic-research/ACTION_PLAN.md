# Academic Paper Plan Review — Full Report + Action Plan
**Date:** 2026-05-04
**Reviewer:** academic-paper-reviewer v3.6.8 (quick mode)
**Scope:** All 34 PAPER_PLAN.md files across CT, Legal_Theory, and MISC tracks
**Method:** Three parallel batch reviews; findings consolidated here

---

## Executive Summary

The 34-paper program is internally coherent with a sound dependency chain. No plan contains a fundamental conceptual error. The abstracts are correctly pitched for their target venues; the citation architecture is consistent; the Shannon-CT analogy that runs through the program is a genuine structural contribution.

**Five program-level issues require attention before writing begins on certain papers:**

1. **C(S) information-theoretic formalization gap** — Papers 2, 3, and CAP-001 invoke Shannon-style proofs but do not address how C(S) becomes an information-theoretic object with a probability space. BLOCKING for those papers.
2. **"CT is the only/first" claim inconsistency** — Several papers say "only," some say "first." The defensible formulation is: *"CT is the first AI governance framework grounded in an empirically falsifiable conservation law."* Must be consistent across all 34 papers.
3. **Missing related work sections** — Every venue-targeted paper (NeurIPS, ICML, ACL, IEEE TIT, FAccT) requires a related work section. Its absence triggers desk rejection. Currently missing from all plans.
4. **Shannon analogy treated independently in four papers** — CL-001, FS-001, COM-001, CAP-001 all develop the "conservation IS isolation" analogy independently. FS-001 should be the canonical treatment; all others should cite FS-001.
5. **Trade secret vs. academic publication conflict** — SIGSYSTEM and MO§ES withhold central contributions. Must be resolved before those papers enter any publication queue.

---

## Prioritized Action Plan

Actions are ordered by: (1) blocking status, (2) downstream impact, (3) effort.

### TIER 1 — Immediate (no writing blocked by these)

| # | Action | Paper(s) | Why |
|---|--------|----------|-----|
| 1 | **Change GOV-001 title** to "Governing the Transformation: Commitment Theory and the Missing Semantic Layer in AI Governance Frameworks" | GOV-001 | Current title ("The Only Governance Framework with a Law") reads as advocacy. Desk rejection risk at Nature Machine Intelligence and FAccT. One-word change = publishable frame. |
| 2 | **Standardize "only" → "first"** across all PAPER_PLAN.md files | All 34 | "CT is the only" is an aggressive superlative reviewers will challenge. "CT is the first AI governance framework grounded in an empirically falsifiable conservation law" is accurate, harder to rebut, and consistent. |
| 3 | **Deposit P-000** to Zenodo | P-000 | It's the citation root for every other paper. Nothing else can be formally submitted until this is publicly citable. Missed April 30 soft deadline — still actionable. |
| 4 | **CCT→CT naming update in L-000** + deposit to SSRN/Zenodo | L-000 | L-000 is the citation root for all legal papers. L-001 (submitted) already uses CT naming. L-000 deposit should have preceded L-001 submission — do it now. |
| 5 | **Move NLI-at-1.00 finding to sentence 2** of CL-001 abstract | CL-001 | It is the single most compelling hook for a computational linguistics reviewer. Currently buried mid-abstract. Trivial fix, significant impact on first impression. |
| 6 | **Soften P-000 Key Claim 5**: "categorically" not "permanently" | P-000 | The deontic/epistemic distinction is categorical, not permanent — every reader who encounters CT in a linguistics context will ask the same question again regardless of one sentence. |

---

### TIER 2 — Before Writing Those Papers (blocking for specific papers)

| # | Action | Paper(s) | Why |
|---|--------|----------|-----|
| 7 | **Resolve C(S) information-theoretic formalization** — define the probability space, source distribution, and coding scheme | Paper 2, Paper 3, CAP-001 | Without this, the Shannon source coding analog (Paper 2), the sparsity bound proof (Paper 3), and the channel capacity theorem (CAP-001) cannot be formally stated. These are not stylistic choices — they are the load-bearing mathematical steps. No writing can begin until this is resolved. |
| 8 | **Specify formal economic model type** (principal-agent, incomplete contracting, or search/matching) | ECON-001 | The entire ECON-001 paper rests on a model that does not yet exist. The model type determines the formal development. Cannot write without it. |
| 9 | **Sketch formal definition of canonical invariant** for FS-001 (one technical sentence using possible worlds / accessibility relations) | FS-001 | FS-001 is the canonical formal semantics paper. Section IV (the formal definition) is the entire paper. The definition must be worked out before writing begins or the paper cannot proceed. |
| 10 | **Resolve SIGSYSTEM trade secret vs. publication conflict** — choose: (a) publish theoretical framework without performance claims, (b) file patent first then publish fully, or (c) treat as MO§ES internal component only | SIGSYSTEM, MOSES | A systems paper withholding its central component's architecture is not fully peer-reviewable. This is unresolved and SIGSYSTEM is currently in the active publication queue — it should not be. Remove from active queue until resolved. |
| 11 | **Address CL-002 circularity** — add held-out test partition or cross-validation methodology for classification algorithm | CL-002 | Classification algorithm trained and evaluated on the same CT corpus. Reviewers will reject on this basis. Must be fixed at the plan stage, not the writing stage. |
| 12 | **Scope Paper 4** to one primary generalization dimension (recommend: cross-provider) | Paper 4 | Current scope (providers + architectures + languages + domains + modalities) = 4 papers, not 1. An 8-10 page ACL paper cannot cover all of these. Scope reduction is required before writing begins. |
| 13 | **Write corpus planning note for L-002** — target 40-60 provisions, selection criteria (all provisions containing "shall," "must," "shall not," "is entitled to"), classification methodology | L-002 | L-002 is the empirical spine of the entire Legal Theory track. L-003, L-005, L-007, and L-010 all depend on its data. The corpus is described as "needed" but not yet planned. If summer 2026 construction slips, four papers slip with it. This is the highest-impact planning gap in the program. |

---

### TIER 3 — During Writing (structural fixes to apply while drafting)

| # | Action | Paper(s) | Why |
|---|--------|----------|-----|
| 14 | **Add Related Work sections** to all venue-targeted papers | Paper 0, Paper 1, Paper 2, Paper 3, Paper 4, Paper 5, CL-001, CL-002, FS-001, L-007, GOV-001 | Absence of related work triggers desk rejection at NeurIPS, ICML, ACL, EMNLP, IEEE TIT, FAccT. Not a stylistic choice — a structural requirement. |
| 15 | **Add oracle rationale** to Paper 0 — why DeBERTa-v3-base-mnli specifically? What are its known failure modes? | Paper 0 | This will be a focal point for reviewers at NeurIPS/ICML. Needs to be addressed directly, not deflected. |
| 16 | **Clarify the 7/20 result** in Paper 0 — what happened to the signals that did not achieve NLI=1.00? | Paper 0 | Currently the abstract says "13/20" without addressing the other 7. Reviewers will ask. |
| 17 | **Resolve Paper 1 rhetorical posture** — pick one: "we find evidence of a threshold regime" OR "we ask which model fits best" | Paper 1 | The abstract and outline are currently in conflict. Must be resolved before writing. |
| 18 | **Address stationarity assumption** in Paper 1 — does the semantic commitment process satisfy conditions for entropy rate to be well-defined? | Paper 1 | IEEE TIT and NeurIPS reviewers will raise this. |
| 19 | **Reframe MO§ES in L-003** — not "MO§ES as reference implementation" but "CCR-compliant systems satisfying the CT governance density bound" | L-003 | Law reviews do not publish branded implementations. MO§ES goes in a footnote. |
| 20 | **EXP-006 reframing criteria** in Paper 5 — what would a genuine Conservation Law failure look like vs. harness stress? | Paper 5 | The reinterpretation (2/4 result as harness stress, not CT failure) is the most consequential interpretive move in the program. Reviewers will be skeptical unless explicit distinguishing criteria are provided. |
| 21 | **Engage Floridi, Barwise/Perry, Dretske** in L-007 and FS-001 — "semantic information theory" literature is the most likely objection to CT's novelty claim | L-007, FS-001 | The claim that CT is a new approach will fail if it doesn't distinguish itself from situation theory (Barwise/Perry) and Floridi's General Definition of Information. |
| 22 | **Turing (1950) precision** in Post-Turing paper — don't mischaracterize what Turing actually claimed | Post-Turing | Turing himself doubted the imitation game was sufficient for intelligence. The paper needs to engage what he actually said. |
| 23 | **Specify Fidelity Seal cryptographic primitive** in MO§ES paper | MOSES | "Cryptographic certificate" without specifying the scheme is too vague for reviewers. |
| 24 | **Hart & Sacks engagement** in L-008 — legal process theory's institutional competence framework bears directly on which institution enforces commitment conservation | L-008 | L-008 cites Hart & Sacks in citation notes but it's not in the outline. HLR/YLJ will expect this engagement. |
| 25 | **Common law scope note** in L-008 — CT applies most directly to statutory/regulatory text, not common law rules evolving through precedent | L-008 | Without this scope note, reviewers will correctly object that CT cannot handle judge-made law. |
| 26 | **Paper 0 peer review gate** — L-006 and L-010 should be held until Paper 0 achieves formal peer review | L-006, L-010 | Daubert's peer-review factor (L-010) and the "established science" framing (L-006) require actual peer review, not preprint status. |
| 27 | **Section VI operational detail** in L-005 — practitioners who cannot run the CT harness need proxy checks, not just pointers to CT gates | L-005 | Law and Contemporary Problems is a practitioner venue. If Section VI only says "use the CT harness," it fails its audience. |
| 28 | **FS-001 as canonical Shannon treatment** — all other papers cite FS-001 for the "conservation IS isolation" analogy rather than developing it independently | FS-001, CL-001, COM-001, CAP-001 | Four papers currently invoke this analogy independently. Reviewers at each venue will notice the same move in parallel papers. FS-001 is the formal paper that should establish this; all others should cite it. |
| 29 | **Deontic/epistemic disambiguation** should be one sentence + footnote citing P-000 and FS-001 in each paper — not a paragraph | All MISC track | Currently each plan handles the disambiguation independently. This will produce 12 redundant paragraphs across the track. |

---

### TIER 4 — Long-term / Milestone-gated

| # | Action | Paper(s) | Why |
|---|--------|----------|-----|
| 30 | **Identify legal collaborators** for L-002 (beneficial), L-008 (essential), L-010 (primary author) | L-002, L-008, L-010 | Three of the eleven legal papers require collaborators not yet identified. HLR/YLJ/SLR will scrutinize author lists carefully. This is a milestone, not a background task. |
| 31 | **Paper 0 peer review submission** | Paper 0 | Multiple downstream papers (L-006, L-007, L-010) depend on Paper 0 having formal peer review. Submitting to a CS/AI journal is the highest-leverage single action in the program. |
| 32 | **Expand experimental record** beyond EXP-003 for Papers 1-3 | Paper 1, Paper 2, Paper 3 | 20 signals, 10 steps is sufficient for a proof of concept. Model comparison (linear vs. exponential vs. threshold) requires more data. Either expand or frame Papers 1-3 explicitly as pilot studies. |
| 33 | **Resolve L-002/L-005 merge decision** before corpus construction | L-002, L-005 | The corpus design and failure mode analysis methodology are different depending on whether these are one paper or two. Decide first. |
| 34 | **Watchlist for L-006/L-009 triggers** — identify pending proceedings (EEOC AI rulemaking, FTC algorithmic accountability, pending circuit court cases on AI document authentication) | L-006, L-009 | Both papers are opportunistic. Without a watchlist, no trigger is ever acted on. |

---

## Full Review — CT Track

### P-000 — Propositions of Commitment Theory: A Research Prospectus
**Venue fit:** STRONG (Zenodo/arXiv deposit)

**Abstract:** Correctly frames P-000 as a timestamped origin document rather than a traditional paper, which is the right self-description for a Zenodo preprint. The "invitation to falsify" language is appropriate and strengthens scientific credibility. One risk: the whitespace claim ("zero academic collision") will be scrutinized closely by any reader who checks independently — the abstract should note the date-of-deposit scope limitation more explicitly (it implies this, but doesn't state it).

**Outline:** The seven-section structure is well-suited to a prospectus. Section V (disambiguation from linguistic commitment) is critically important and well-placed. Section VI (whitespace claim) would benefit from noting the specific search databases used, since the credibility of the claim depends entirely on methodology.

**Key claims:** All five claims are appropriately scoped for a definitional/prospectus document. The claim that CT's "commitment" is "permanently" separated from linguistic commitment by one sentence is slightly overconfident — a single sentence establishes the distinction but does not insulate CT from terminological challenges in peer review.

**Fixes needed:**
- Add explicit scope phrase to whitespace claim in abstract: "at the time of deposit"
- Change "permanently" → "categorically" in Key Claim 5
- Section VI: list specific databases searched (Google Scholar, Semantic Scholar, ACL Anthology, PhilPapers, SSRN, IEEE Xplore)

---

### Paper 0 — A Conservation Law for Commitment in Language Under Recursive AI Transformation
**Venue fit:** MODERATE for NeurIPS/ICML; STRONG for TACL/JAIR

**Abstract:** The strongest abstract in the program — it states results with numbers (13/20, 10 steps, EXP-007), distinguishes commitment from surface form, and explicitly states falsifiability conditions. NeurIPS/ICML will ask "why is NLI bidirectional entailment the right oracle?" with greater skepticism. For an AI journal, this is exactly the right framing.

**Outline:** Missing related work section — will trigger desk rejection at NeurIPS/ICML. Placement of failure taxonomy (Section VI) after theorem proof (Section V) is logical.

**Key claims:** All five defensible and tied to specific experimental results. "Candidate Second Law" language correctly hedges the thermodynamic analogy. Falsifiability claim is a genuine strength.

**Fixes needed:**
- Add Related Work: faithfulness metrics in NLG, semantic textual similarity benchmarks, logical consistency in summarization, constitutional/preference alignment literature
- Strengthen oracle rationale: why DeBERTa-v3-base-mnli specifically? Known failure modes?
- Plan baseline comparison vs. ROUGE/BERTScore on same signals (for NeurIPS/ICML)
- Address what happened to the 7/20 signals that did not achieve NLI=1.00

---

### Paper 1 — Semantic Entropy Rate
**Venue fit:** MODERATE for NeurIPS/ICML

**Abstract:** Threshold regime finding ("stability then rapid collapse") is the most interesting empirical claim and well-foregrounded. Shannon analogy appropriate but will require careful treatment — information theorists will scrutinize whether h_s satisfies technical requirements for an entropy rate (stationarity, ergodicity).

**Outline:** EXP-003's 10-step, 20-signal dataset is thin for fitting three models. Section VI (relationship to channel capacity) forward-references a Layer 4 paper that doesn't exist — creates circular dependency risk.

**Key claims:** Conflicting rhetorical posture — abstract says "we find evidence" while outline "asks which model fits." Must be resolved.

**Fixes needed:**
- Address stationarity assumption: does the semantic commitment process satisfy conditions for entropy rate to be well-defined?
- Expand empirical basis or explicitly frame as pilot result with power analysis
- Resolve rhetorical posture throughout
- Restructure Section VI as "Toward Future Work" subsection, not a full section

---

### Paper 2 — The Compression-Fidelity Bound
**Venue fit:** STRONG for IEEE TIT; MODERATE for NeurIPS/ICML

**Abstract:** Most technically ambitious claim — a formal proof analogous to Shannon's source coding theorem. Correctly hedged with "information-theoretic lower bound."

**Outline:** CRITICAL GAP — Section III claims to state and prove the Compression-Fidelity Bound but does not address how C(S) is formalized as an information-theoretic object suitable for a coding theorem proof. This is the central intellectual challenge of the paper and the plan treats it as already solved.

**Key claims:** Key Claim 1 is simultaneously a theorem (requiring proof machinery) and an empirical observation (requiring data). The plan claims both simultaneously.

**Fixes needed:**
- BLOCKING: Address how C(S) is formalized as an information-theoretic source (probability space, source distribution, coding scheme)
- Add semantic communication literature (Bao et al. 2011, Shi et al. 2021) as related work — must be distinguished from CT
- Characterize whether "sharp transition" is universal or signal-dependent
- Address distinction between "representation length" and "semantic length"

---

### Paper 3 — Governance Density Optimization
**Venue fit:** STRONG for FAccT/AIES; MODERATE for AAMAS

**Abstract:** Governance density framing (ρ_g, sparsity bound ρ*) is a genuinely useful engineering contribution. "CT-compliant systems need not be maximally constrained, only sufficiently constrained" will resonate with FAccT practitioners.

**Outline:** Algorithm in Section V doesn't specify what it operates on. Key Claim 3 ("full space of valid instances") overclaims.

**Key claims:** Key Claim 5 (computational tractability) is unsubstantiated in the plan.

**Fixes needed:**
- Define what the algorithm operates on (transformation pipeline formalization required first)
- Scope Key Claim 3: "characterizes a class" not "the full space"
- Add FAccT section on governance degradation when ρ* cannot be achieved
- Operationalize ρ_g for empirical validation

---

### Paper 4 — Cross-System Fidelity
**Venue fit:** STRONG for ACL/EMNLP

**Abstract:** Right paper for ACL/EMNLP. Cross-language finding (conservation degrades for "underspecified modal systems") is most interesting theoretical prediction.

**Outline:** Scope is far too broad for 8-10 pages — multiple providers + architectures + languages + domains + modalities is 4 papers, not 1.

**Key claims:** "Languages with underspecified modal systems" requires linguistic characterization not currently in CT framework. Operationalization unclear.

**Fixes needed:**
- SCOPE REDUCTION: One primary dimension (cross-provider recommended). Others → companion paper or "toward" section
- Define "underspecified modal system" with modal typology literature backing
- Add confound analysis: architecture effect vs. training data effect
- Cross-lingual NLI oracle validation required per target language

---

### Paper 5 — The Commitment Measurement Instrument
**Venue fit:** MODERATE for JMLR; venue target should be sharpened

**Abstract:** Metrology framing (noise floor, sensitivity, calibration) is novel. EXP-006 reinterpretation as harness stress test rather than anomaly is important for CT's internal consistency.

**Outline:** Forward reference to SIGSYSTEM (early development) is a structural risk.

**Key claims:** EXP-006 reframing (2/4 as stress test) is the most consequential interpretive move — reviewers will be skeptical without explicit distinguishing criteria.

**Fixes needed:**
- Sharpen venue to JMLR specifically
- EXP-006 reframing must provide explicit criteria: what would a genuine Conservation Law failure look like vs. harness stress?
- Hard dependency on Paper 4 data — publication sequence must reflect this
- Address GUM (JCGM 100:2008) uncertainty propagation for discrete categorical NLI outputs

---

### MOSES Architecture — MO§ES™ Enforcement Architecture
**Venue fit:** MODERATE (patent-pending complicates standard peer review)

**Abstract:** Thermostat/thermometer distinction is effective. Five components at right abstraction level.

**Outline:** "SIGSYSTEM withheld as trade secret" is the central tension — a systems paper withholding its central component's architecture is not fully reviewable.

**Key claims:** Key Claim 4 (operating at "physical-law level") requires Paper 0's reception as established science — sequence dependency.

**Fixes needed:**
- Specify what WILL be disclosed: API, input/output contract, performance characteristics
- Specify Fidelity Seal cryptographic primitive
- Resolve SIGSYSTEM/MO§ES circular dependency
- Coordinate arXiv deposit with patent publication timeline

---

### Layer 4 — SIGSYSTEM
**Venue fit:** WEAK — not in active publication queue

**Abstract:** Signal/noise word-level insight is genuine. Honest about trade secret limitation.

**Key claims:** Key Claim 3 (SIGSYSTEM outperforms NLI baseline) is a hypothesis — data doesn't exist yet.

**Fixes needed:**
- Resolve academic vs. trade secret tension BEFORE entering any publication queue
- Move to long-term, not active queue
- Reclassify Key Claim 3 as hypothesis, not claim

---

### Layer 4 — Post-Turing Test
**Venue fit:** MODERATE-STRONG for AI venues and philosophy of AI

**Abstract:** Most legible to general AI audience. Reframe from "fool a human" to "preserve meaning under pressure" is compelling.

**Key claims:** "Behavioral imitation largely solved" is contestable — scope to NLG specifically. "Only criterion grounded in a physical law" is aggressive superlative.

**Fixes needed:**
- Hedge Claim 1: "behavioral imitation in NLG is no longer the binding constraint"
- Soften Claim 4: "only evaluation criterion grounded in an empirically verified conservation law"
- Section II: engage Turing (1950) with precision
- Add scope note: Post-Turing Test is a necessary condition, not sufficient condition for intelligence

---

### Layer 4 — Channel Capacity (CT-track)
**Venue fit:** STRONG for IEEE TIT if proof holds

**Abstract:** Most technically precise. Shannon-CT correspondence table is an excellent structural contribution and publishable immediately as a position paper.

**Outline:** Section IV requires formal channel model, coding theorem proof, and achievability result — none yet addressed.

**Key claims:** All well-stated. Key Claim 1 is a conjecture at current status.

**Fixes needed:**
- Shared blocking gap with Paper 2: C(S) information-theoretic formalization first
- Consider publishing the correspondence table as a near-term position paper before full theorem
- Engage semantic communications literature (Qin et al. 2021, Xie et al. 2021)
- Propagate Paper 1's empirical limitations into C_s estimation

---

## Full Review — Legal Theory Track

### L-000 — Propositions of Commitment Theory for Legal Applications
**Venue fit:** STRONG (SSRN/Zenodo deposit)

**Abstract:** Six propositions clear. Pluralism-preservation claim is a genuine differentiator. "CT is the only governance foundation" is the most aggressive claim.

**Fixes needed:**
- Hedge: "CT provides the first" rather than "CT is the only"
- Anticipate ISO/IEC 42001, IEEE 7010, RAIL-M in Proposition 3
- Confirm complete CCT→CT naming update before deposit

---

### L-001 — The Uncertainty That Invites Building (SUBMITTED)
**Venue fit:** STRONG

Documentation review only — paper submitted May 1, 2026 to Stanford Law Review Online Vol. 79. Abstract, outline, and key claims are well-constructed for the venue. No fixes needed.

---

### L-002 — Commitment Drift in Civil Rights Statutes (Empirical Study)
**Venue fit:** STRONG for JELS; MODERATE for Jurimetrics

**Abstract:** Excellent for empirical study. Corpus design is well-chosen.

**Critical gap:** Corpus construction is described as "needed" but not planned. This is the highest-impact planning gap in the entire Legal Theory track.

**Fixes needed:**
- URGENT corpus planning: 40-60 provisions across five statutes; selection criteria ("shall," "must," "shall not," "is entitled to"); classification methodology for three categories
- "Legal collaborator beneficial" may need to be "required" for JELS
- Decide merge/standalone with L-005 BEFORE corpus construction begins

---

### L-003 — A Commitment Conservation Requirement (Technical Standard)
**Venue fit:** STRONG for Yale JL&T and Stanford TLR

**Abstract:** Strong. Three-doctrine structure (Mathews / FRE 901-Daubert / Griggs) grounds CCR in existing doctrine.

**Key claims:** "Commitment drift as Griggs disparate impact mechanism" conflates statistical disparities and a new doctrinal harm category — requires clarification.

**Fixes needed:**
- Clarify Section V: statistical disparities argument vs. new doctrinal harm category — these are different papers
- Remove branded "MO§ES" from main text, place in footnote; use "CCR-compliant systems satisfying CT governance density bound"
- Confirm Paper 3 and Paper 5 are citable before L-003 submission

---

### L-004 — Commitment Conservation Requirements (Policy Brief)
**Venue fit:** STRONG for Brookings/Stanford HAI/Berkman Klein

**Abstract:** Well-calibrated for policy register.

**Fixes needed:**
- Collapse Sections II and III into one
- Add concrete cost/burden estimate to Section V
- Flag that if published before L-002: claims must rest on Paper 0 + L-001 scenarios only

---

### L-005 — Nine Failure Modes: How AI Transformation Degrades Legal Meaning
**Venue fit:** STRONG for Law and Contemporary Problems

**Abstract:** Excellent. "Negation reversal invisible to standard document review" is the most compelling hook.

**Fixes needed:**
- Section VI: describe operational proxy checks for practitioners without the full harness
- Clarify merge/standalone decision with L-002
- Define "most legally dangerous" with explicit metric (detection difficulty × severity of consequence)

---

### L-006 — Amicus Brief / Regulatory Comment (Opportunistic)
**Venue fit:** MODERATE

**Key claims:** "Peer-reviewed (or under review)" parenthetical is vulnerable — Daubert's peer-review factor does not treat "under review" as satisfying it.

**Fixes needed:**
- Add status gate: only trigger after Paper 0 achieves formal peer review or conference acceptance
- Add watchlist of pending proceedings
- Note standing requirements for amicus filings

---

### L-007 — From Information to Commitment (Full Legal Paper)
**Venue fit:** STRONG for AI and Law (Springer)

**Abstract:** Shannon framing excellent. "Law cannot afford the same avoidance" is a strong thesis sentence.

**Fixes needed:**
- Section note for Section VI: engage situation theory (Barwise/Perry) and Floridi's Phi as primary objections to CT novelty
- Reframe: "first AI and Law framework grounded in an empirically falsifiable conservation law"
- Specify which empirical claims require L-002 vs. which rest on Paper 0 alone

---

### L-008 — Jurisprudence of the Record (Legal Theory Capstone)
**Venue fit:** STRONG ambition; MODERATE without essential legal co-author

**Abstract:** "Jurisprudence of the record" is a genuine conceptual contribution.

**Fixes needed:**
- Add Hart & Sacks legal process theory as fifth engagement in outline
- Add scope note: CT applies to statutory/regulatory text, not common law adjudication
- Specify co-author's role in the author agreement

---

### L-009 — Law Review Comment (Opportunistic)
**Venue fit:** MODERATE

**Fixes needed:**
- Add timing note: L-001, L-000, Paper 0 must be publicly citable before any trigger is acted on
- Identify 1-2 likely near-term trigger categories

---

### L-010 — Evidentiary Authentication (Daubert/FRE 901)
**Venue fit:** STRONG for evidence law-focused general law reviews

**Abstract:** FRE 901 anchor is precise. Daubert four-factor analysis is the strongest section.

**Fixes needed:**
- Specify division of labor with legal co-author explicitly
- Flag that CL-track papers may need to be published first to establish "general acceptance" (Daubert factor 3)
- Confirm MO§ES architecture paper will be publicly citable before L-010 submission
- Add Kumho Tire to key claims discussion

---

## Full Review — MISC Track

### CL-001 — Nine Ways Meaning Breaks (Failure Mode Taxonomy)
**Venue fit:** STRONG

**Abstract:** Well-constructed. NLI-at-1.00 / negation-reversal finding is the sharpest hook — currently buried, should be sentence 2.

**Discipline entry:** Very good. Correctly positions against NLI lineage, FactBank, CommitmentBank, BERTScore.

**Fixes needed:**
- Move NLI-at-1.00 finding to sentence 2 of abstract
- Section VI: propose specific evaluation protocol, not just flag the gap
- Add related work on hallucination detection (Maynez et al. 2020, Honovich et al.)
- Ensure "commitment kernel" is self-defined for CL readers

---

### CL-002 — Three Regimes of Commitment Stability
**Venue fit:** MODERATE-STRONG for NLE; MODERATE for Journal of Semantics

**Abstract:** Solid. Opens with empirical observation correctly.

**Critical gap:** Classification algorithm trained and evaluated on same CT corpus = circularity. Reviewers will reject on this basis.

**Fixes needed:**
- BLOCKING: Add held-out test partition or cross-validation methodology
- Specify target accuracy figure for classification algorithm
- Self-define regime types without assuming CL-001 has been read

---

### FS-001 — Commitment as Canonical Invariant (Formal Primitive)
**Venue fit:** STRONG for Journal of Semantics / Natural Language Semantics

**Abstract:** Excellent discipline entry. Deontic/epistemic disambiguation is clear and correct.

**Critical gap:** Formal definition of canonical invariant in Section IV is the entire paper — must be worked out before writing begins.

**Discipline entry:** Very strong.

**Fixes needed:**
- Write one technical sentence specifying canonical invariant definition at plan stage — confirm it's workable
- Develop proof sketch for non-reducibility from presupposition
- Designate FS-001 as canonical Shannon-analogy treatment for entire program
- Do not begin writing until Section IV definition is fully worked out

---

### FS-002 — Philosophy of Language (Conservation of Commitment)
**Venue fit:** MODERATE for Mind & Language; MODERATE for Synthese

**Abstract:** Three-thesis structure. Deflationary thesis is most interesting.

**Fixes needed:**
- Engage semantic minimalism/contextualism (Borg, Recanati) in Section III/IV
- Section V: state precisely what CT does to Gricean cooperativity
- Depends on FS-001 — do not begin until FS-001 published

---

### IS-001 — A Conservation Law for Digital Meaning (Information Science)
**Venue fit:** STRONG for JASIST and Journal of Documentation

**Abstract:** Excellent. Correctly identifies OAIS/PREMIS/Dublin Core gap.

**Discipline entry:** Very strong. Thibodeau (2002) is the right historical anchor.

**Fixes needed:**
- Hedge Claim 5: "provides the formal criterion and operational measurement protocol" not "makes tractable"
- Section VI (PREMIS connection): specify which PREMIS elements map to which CT constructs
- Add existing semantic preservation proposals to literature review
- Ready to draft — highest priority in MISC track alongside CL-001

---

### IS-002 — Commitment Conservation in Digital Archives
**Venue fit:** STRONG for Archival Science; MODERATE for American Archivist

**Abstract:** Three-class framework (records/documents/data) is novel and appropriate.

**Fixes needed:**
- Formalize archival triad connection: CCR compliance entails (not supports) authenticity/reliability/integrity
- Add at least one concrete archival case study for American Archivist
- Add ISO 16175-1:2023
- Depends on IS-001

---

### STS-001 — Who Loses Meaning? (Sociology/STS)
**Venue fit:** STRONG for Social Studies of Science

**Abstract:** Excellent. "A physical law with a social distribution" is exactly the right STS entry.

**Fixes needed:**
- Section III: add at least one documented empirical case of AI-mediated transformation with identifiable commitment drift
- Engage FATE/FAccT literature on disparate impact
- Clarify whether Claim 5 is normative or legal
- Can begin now but needs one empirical anchor

---

### COM-001 — Can Meaning Be Measured? (Communication Studies)
**Venue fit:** MODERATE-STRONG for Journal of Communication

**Abstract:** Good. Shannon bridge is the strongest conceptual move.

**Key claims:** Claim 4 ("Shannon + CT = complete account of communicative fidelity") is overclaimed.

**Fixes needed:**
- Hedge Claim 4: CT completes the framework "for deontic content in high-stakes communication" — not communicative fidelity simpliciter
- Add CMC and AI-mediated communication literature (Walther, Hancock)
- Section V: explicitly cite Weaver's commentary acknowledging the meaning gap CT fills

---

### ECON-001 — The Price of Drift (Economics)
**Venue fit:** WEAK for Journal of Economic Theory; MODERATE for Information Economics and Policy

**Abstract:** Well-framed. Market failure / externality framing is correct.

**Critical gap:** Formal model type unspecified. Cannot begin writing until model exists and generates three claimed results.

**Fixes needed:**
- BLOCKING: Specify formal model type (principal-agent, incomplete contracting, or search/matching)
- Remove Journal of Economic Theory from primary venue list
- Cannot begin until model exists
- Specify drift probability distribution parameters

---

### GOV-001 — Comparative Governance Analysis
**Venue fit:** STRONG for ACM FAccT / AI & Society; MODERATE for Nature Machine Intelligence

**Abstract:** Strategically sharp but title is a liability.

**Fixes needed:**
- CHANGE TITLE to "Governing the Transformation: Commitment Theory and the Missing Semantic Layer in AI Governance Frameworks"
- Section VI: add worked example — system satisfying Constitutional AI/NIST/EU AI Act while producing measurable commitment drift
- For FAccT: engage Jobin et al. 2019 and Hagendorff 2020

---

### CAP-001 — Semantic Channel Capacity (Capstone)
**Venue fit:** MODERATE for IEEE TIT (aspirationally correct)

**Abstract:** Most technically precise Shannon analogy use in MISC track. Three corollaries recovering Papers 1-3 is the right unifying move.

**Fixes needed:**
- Specify functional form of C_s and provide informal proof sketch
- Shared blocking gap with Paper 2: C(S) information-theoretic formalization first
- Consider ISIT as first venue for shorter proof

---

### CAP-002 — Commitment Theory (Monograph)
**Venue fit:** STRONG aspiration (OUP/CUP/MIT Press)

**Abstract:** Appropriately structured as prospectus.

**Fixes needed:**
- Identify target series at each press before approaching
- Ensure Part II adds interpretive synthesis, not just compilation
- Give Chapter 16 (Open Questions) explicit planning attention
- Gated on full evidence base — do not begin until all track papers are complete

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Total papers reviewed | 34 |
| No fixes needed | 1 (L-001 — submitted) |
| Tier 1 fixes (immediate) | 6 actions |
| Tier 2 fixes (blocking for specific papers) | 7 actions |
| Tier 3 fixes (during writing) | 16 actions |
| Tier 4 fixes (long-term / milestone-gated) | 5 actions |
| Papers ready to write now (no blockers) | 3 (CL-001, IS-001, P-000 deposit) |
| Papers blocked pending formalization | 3 (Paper 2, Paper 3, CAP-001) |
| Papers blocked pending model | 1 (ECON-001) |
| Papers not in active queue | 1 (SIGSYSTEM) |
