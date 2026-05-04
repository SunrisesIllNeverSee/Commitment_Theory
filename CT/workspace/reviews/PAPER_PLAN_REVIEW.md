# CT Track — Paper Plan Review
**Date:** 2026-05-04
**Reviewer:** academic-paper-reviewer (quick mode)
**Scope:** 11 PAPER_PLAN.md files

---

### P-000 — Propositions of Commitment Theory: A Research Prospectus
**Venue fit:** STRONG
**Abstract:** Correctly frames P-000 as a timestamped origin document. Whitespace claim will be scrutinized — needs explicit date-of-deposit scope limitation in abstract text (implied but not stated).
**Outline:** Well-suited. Section VI needs to specify search databases used.
**Key claims:** "Permanently" in claim 5 should be "categorically" — the distinction is categorical, not permanent.
**Fixes needed:**
- Add "at the time of deposit" explicitly to whitespace claim in abstract
- Change "permanently" → "categorically" in Key Claim 5
- Section VI: list specific databases searched (Google Scholar, Semantic Scholar, ACL Anthology, PhilPapers, SSRN, IEEE Xplore)

---

### Paper 0 — Conservation Law of Commitment
**Venue fit:** MODERATE for NeurIPS/ICML; STRONG for TACL/JAIR
**Abstract:** Strongest in program — results with numbers, distinguishes commitment from surface form, states falsifiability.
**Outline:** Missing related work section — will trigger desk rejection at NeurIPS/ICML.
**Key claims:** "13/20" needs clarification — what happened to the other 7 signals?
**Fixes needed:**
- Add Related Work section: faithfulness metrics in NLG, semantic textual similarity, logical consistency in summarization, constitutional/preference alignment
- Add oracle rationale: why DeBERTa-v3-base-mnli specifically? Known failure modes?
- For NeurIPS/ICML: plan baseline comparison vs. ROUGE/BERTScore on same signals
- Clarify what happened to the 7/20 signals that did not achieve NLI=1.00

---

### Paper 1 — Semantic Entropy Rate
**Venue fit:** MODERATE for NeurIPS/ICML
**Abstract:** Threshold regime finding is the most interesting claim and well-foregrounded.
**Outline:** 20 signals insufficient for fitting three models and declaring a winner — degree-of-freedom problem. Section VI forward-references Layer 4 channel capacity (doesn't exist yet).
**Key claims:** Conflicting rhetorical posture — abstract says "we find evidence" while outline "asks which model fits." Pick one.
**Fixes needed:**
- Address stationarity assumption: does the semantic commitment process satisfy conditions for entropy rate to be well-defined?
- Expand empirical basis or frame as pilot result with explicit power analysis
- Resolve rhetorical posture throughout (reporting a finding vs. asking a question)
- Restructure Section VI as "Toward Future Work" subsection, not a full section

---

### Paper 2 — Compression-Fidelity Bound
**Venue fit:** STRONG for IEEE TIT; MODERATE for NeurIPS/ICML
**Abstract:** Most technically ambitious claim — Shannon source coding analog. Correctly hedged.
**Outline:** CRITICAL GAP — Section III claims to prove a theorem but doesn't address how C(S) is formalized as an information-theoretic object with a probability space. This is the load-bearing step and it's unresolved.
**Key claims:** Key Claim 1 is simultaneously a theorem (requiring proof) and an empirical observation (requiring data) — needs to choose one.
**Fixes needed:**
- BLOCKING: Address how C(S) is formalized as an information-theoretic source (probability space, source distribution, coding scheme)
- Add semantic communication literature (Bao et al. 2011, Shi et al. 2021) as related work
- Characterize whether the "sharp transition" is universal across signals or signal-dependent
- Address distinction between "representation length" and "semantic length"

---

### Paper 3 — Governance Density Optimization
**Venue fit:** STRONG for FAccT/AIES; MODERATE for AAMAS
**Abstract:** Governance density framing (ρ_g, sparsity bound ρ*) is genuinely useful and well-articulated.
**Outline:** Algorithm in Section V doesn't specify what it operates on.
**Key claims:** Key Claim 3 ("full space of valid instances") overclaims — should be "characterizes a class of valid instances." Key Claim 5 (computational tractability) unsubstantiated.
**Fixes needed:**
- Define what the minimum governance set algorithm operates on (transformation pipeline formalization)
- Scope Key Claim 3: "characterizes a class" not "the full space"
- For FAccT: add section on governance degradation behavior when ρ* cannot be achieved
- Operationalize ρ_g for the empirical validation section

---

### Paper 4 — Cross-System Fidelity
**Venue fit:** STRONG for ACL/EMNLP
**Abstract:** Right paper for ACL/EMNLP. Cross-language finding (conservation degrades for "underspecified modal systems") is most interesting prediction.
**Outline:** Scope is far too broad for 8-10 pages — multiple providers + architectures + languages + domains + modalities = 4 papers, not 1.
**Key claims:** Key Claim 3 ("languages with underspecified modal systems") requires linguistic characterization not currently in CT framework. Key Claim 4 (cross-modality requires higher ρ_g) needs theoretical grounding.
**Fixes needed:**
- SCOPE REDUCTION: Pick one primary generalization dimension (cross-provider is most tractable) for 8-10 page paper. Others → companion paper or "toward" section
- Define "underspecified modal system" with cross-linguistic backing (modal typology literature)
- Add confound analysis: architecture effect vs. training data effect
- Cross-lingual NLI oracle validation required for each target language

---

### Paper 5 — The Commitment Measurement Instrument
**Venue fit:** MODERATE for JMLR; WEAK for "Philosophy of Information" (too broad)
**Abstract:** Metrology framing (noise floor, sensitivity, calibration) is novel and distinctive. EXP-006 reinterpretation as harness stress test is important.
**Outline:** Forward reference to SIGSYSTEM (early development) is a structural risk.
**Key claims:** Key Claim 2 (EXP-006 as stress test not failure) is the most consequential interpretive move — reviewers will be skeptical of reframing a 2/4 result.
**Fixes needed:**
- Sharpen venue to JMLR specifically
- EXP-006 reframing MUST provide explicit criteria: what would a genuine Conservation Law failure look like vs. harness stress?
- Hard dependency on Paper 4 data — publication sequence must reflect this
- Address how GUM (JCGM 100:2008) uncertainty propagation adapts for discrete categorical NLI outputs

---

### MOSES Architecture — MO§ES™ Enforcement Architecture
**Venue fit:** MODERATE (patent-pending complicates peer review at standard venues)
**Abstract:** Thermostat/thermometer distinction is effective. Five components described at right abstraction level.
**Outline:** "SIGSYSTEM withheld as trade secret" creates core tension — a systems paper withholding its central component's architecture is not fully reviewable.
**Key claims:** Key Claim 4 requires Paper 0's reception as established science — sequence dependency.
**Fixes needed:**
- Address trade secret problem: what WILL be disclosed? (API, input/output contract, performance characteristics)
- Specify the Fidelity Seal cryptographic primitive
- Resolve SIGSYSTEM/MO§ES circular dependency — either MO§ES describes SIGSYSTEM functionally without citing the SIGSYSTEM paper, or co-submit
- Coordinate arXiv deposit date with patent publication (PCT requirements)

---

### Layer 4 — SIGSYSTEM
**Venue fit:** WEAK (trade secret architecture + TBD venue + early development = not publication-ready)
**Abstract:** Signal/noise word-level insight is genuine. Honest about trade secret limitation.
**Outline:** "Theoretical framework without disclosing trade secret" = not a standard academic paper.
**Key claims:** Key Claim 3 (SIGSYSTEM outperforms NLI baseline) is a hypothesis, not a claim — data doesn't exist yet.
**Fixes needed:**
- Resolve academic vs. trade secret tension BEFORE this enters any publication queue. Options: (a) publish theoretical framework without performance claims, defer empirical until after patent; (b) file patent first then publish fully; (c) treat as internal MO§ES component only
- Move to long-term, not active queue
- Reclassify Key Claim 3 as hypothesis

---

### Layer 4 — Post-Turing Test
**Venue fit:** MODERATE-STRONG for AI venues and philosophy of AI
**Abstract:** Most legible to general AI audience. Shift from "fool a human" to "preserve meaning under pressure" is compelling.
**Outline:** Objections and Replies section (VII) is a sign of mature argumentation. ISO/IEC 42001 / EU AI Act bridge is smart.
**Key claims:** Key Claim 1 ("behavioral imitation largely solved") is contestable — scope to "natural language text." Key Claim 4 ("only criterion grounded in a physical law") is aggressive superlative — VC dimension, PAC learning will be raised.
**Fixes needed:**
- Hedge Claim 1: "behavioral imitation in NLG is no longer the binding constraint"
- Soften Claim 4: "only evaluation criterion grounded in an empirically verified conservation law"
- Section II must engage Turing (1950) with precision — don't mischaracterize what Turing actually claimed
- Add section on what Post-Turing Test does NOT evaluate (necessary condition, not sufficient)

---

### Layer 4 — Channel Capacity (CT-track)
**Venue fit:** STRONG for IEEE TIT (if proof holds)
**Abstract:** Most technically precise. Shannon-CT correspondence table is an excellent structural contribution.
**Outline:** Section IV (Semantic Channel Capacity C_s) requires: (a) formal channel model, (b) coding theorem proof or bound, (c) achievability result — none yet addressed in plan.
**Key claims:** All five well-stated and mutually consistent. Key Claim 1 is a conjecture at this stage.
**Fixes needed:**
- Shared blocking gap with Paper 2: C(S) must be formalized as info-theoretic object before coding theorem can be proved
- Shannon-CT correspondence table is publishable immediately as a position paper — consider this as a near-term output before the full theorem
- Engage semantic communications literature (Qin et al. 2021, Xie et al. 2021) — CT must be distinguished from that literature
- Propagate Paper 1's empirical limitations into the C_s estimation section

---

## CT Track Summary

**Program-level strengths:**
1. Empirical record (EXP-001 through EXP-007) is a genuine asset — CT has numbers, harness is public
2. Failure taxonomy (nine modes) is the most practically useful contribution — undermarketed across plans
3. Falsifiability framing maintained consistently — correct scientific posture

**Three program-level weaknesses:**
1. **Information-theoretic formalization gap** — Papers 2, 3, CAP-001 all invoke Shannon-style reasoning but none address how C(S) becomes an info-theoretic object with a probability space. BLOCKING for Papers 2 and 3.
2. **Trade secret / academic publication conflict** — SIGSYSTEM and MO§ES withheld central contributions. Must be resolved before those papers enter any publication queue.
3. **Thin empirical basis** — Papers 1, 2, 3 all rest primarily on EXP-003 (10 steps, 20 signals). Model comparison from this dataset faces degree-of-freedom problems. Need either expanded data collection or consistent framing as pilot studies.

**Priority before writing Papers 1-3:** (1) Resolve C(S) info-theoretic formalization. (2) Expand experimental record. (3) Resolve SIGSYSTEM trade secret conflict. (4) Add related work sections to all venue-targeted papers.
