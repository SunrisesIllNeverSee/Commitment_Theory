# MISC Track — Paper Plan Review
**Date:** 2026-05-04
**Reviewer:** academic-paper-reviewer (quick mode)
**Scope:** 12 PAPER_PLAN.md files

---

### CL-001 — Nine Ways Meaning Breaks (Failure Mode Taxonomy)
**Venue fit:** STRONG
**Abstract:** Well-constructed for CL/NLP. NLI-entailment-at-1.00 / negation-reversal finding is the sharpest hook — buried mid-abstract, should be sentence 2.
**Outline:** Section VI ("Implications for NLP Evaluation Methodology") risks being a critique without a constructive contribution. Needs to propose an actual replacement metric or evaluation protocol.
**Key claims:** All anchored to EXP-001-007 and falsifiable. No overclaims.
**Discipline entry:** Very good. Correctly positions against NLI lineage, FactBank, CommitmentBank, BERTScore. Deontic (signal) vs. epistemic (speaker) distinction well handled.
**Fixes needed:**
- Move NLI-at-1.00 finding to sentence 2 of abstract — it's the best hook
- Section VI: propose a specific evaluation protocol, not just flag the gap
- Add related work on hallucination detection and faithfulness evaluation (Maynez et al. 2020, Honovich et al. on factuality probes)
- Ensure "commitment kernel" is self-defined for CL readers who haven't read Paper 0

---

### CL-002 — Three Regimes of Commitment Stability
**Venue fit:** MODERATE-STRONG for NLE; MODERATE for Journal of Semantics (needs deeper formal semantics engagement)
**Abstract:** Solid. Opens with empirical observation before announcing contribution. Correct for NLE register.
**Outline:** CIRCULARITY PROBLEM — classification algorithm trained and evaluated on same CT corpus. Reviewers will flag immediately.
**Key claims:** "Sufficient accuracy for practical deployment" is a placeholder, not a claim — needs a specific figure or range.
**Discipline entry:** Good for NLE. Von Fintel and Kratzer citations are right anchors but need actual engagement (not just citation) for Journal of Semantics.
**Fixes needed:**
- Address circularity: add held-out test partition or explicit cross-validation methodology
- Specify target accuracy figure (or range) for classification algorithm
- CL-002 must self-define the three regime types — ensure it stands alone without CL-001
- If targeting Journal of Semantics: add subsection in Section III engaging Kratzer's modal base/ordering source directly

---

### FS-001 — Commitment as Canonical Invariant (New Formal Primitive)
**Venue fit:** STRONG for Journal of Semantics / Natural Language Semantics; MODERATE for Linguistics and Philosophy
**Abstract:** Excellent discipline entry. Single-sentence deontic/epistemic disambiguation is clear and correct. Shannon analogy appropriate.
**Outline:** Section IV (formal definition using possible worlds / accessibility relations) is load-bearing — plan must sketch the formal definition before writing begins. "Requires theoretical development" is a real blocking status.
**Key claims:** Non-reducibility claim (claim 4) requires proof sketch, not assertion. Shannon analogy (conservation IS isolation) needs formal grounding.
**Discipline entry:** Very strong. Maps existing landscape, identifies gap, names primitive, uses target discipline's language (intensional semantics).
**Fixes needed:**
- At plan stage, write one technical sentence specifying the canonical invariant definition — confirm it is workable before committing to full paper
- Develop proof sketch for non-reducibility from presupposition (presupposition survival under transformation is a live debate — engage directly)
- FS-001 should be the CANONICAL Shannon-analogy treatment for the entire program — all other papers (CL-001, COM-001, CAP-001) should cite FS-001 for this move, not develop it independently
- Do not begin writing until Section IV formal definition is fully worked out

---

### FS-002 — Philosophy of Language (Conservation of Commitment)
**Venue fit:** MODERATE for Mind & Language; MODERATE for Synthese (needs more direct analytic philosophy of language engagement)
**Abstract:** Three-thesis structure well-organized. Deflationary thesis (sidesteps externalism/internalism) is most interesting but asserts rather than demonstrates.
**Outline:** Section V (CT and Gricean Program) needs a precise statement — "complements rather than competes" is evasive. Must say exactly what CT does to Gricean cooperativity.
**Key claims:** Deflationary claim (claim 2) is genuinely original and defensible. Claim 4 (Second Law as property of semantic objects not cognitive processing) is philosophically important and should be foregrounded against Davidson/Grice.
**Discipline entry:** Needs more contemporary philosophy of language engagement — semantic minimalism/contextualism debates (Borg, Recanati) bear directly on "what survives" question.
**Fixes needed:**
- Engage semantic minimalism/contextualism (Borg's minimal semantics, Recanati's contextualism) in Section III or IV
- Section V: state precisely "CT's Second Law establishes a constraint that Gricean maxims operate within but cannot explain" — not "complements"
- Status "long-term" and dependency on FS-001 are both correct — do not begin until FS-001 is published
- Three thesis claims may be three papers — decide which is the organizing contribution before writing

---

### IS-001 — A Conservation Law for Digital Meaning (Information Science)
**Venue fit:** STRONG for JASIST and Journal of Documentation; MODERATE for IP&M
**Abstract:** Excellent. Correctly identifies OAIS/PREMIS/Dublin Core gap (bit-level completeness without semantic criterion). Does not assume CT knowledge.
**Outline:** Section VI (PREMIS connection) is the payoff — CCR-as-missing-semantic-layer for information science. Most important section.
**Key claims:** All achievable from existing CT material. Claim 5 ("semantic preservation is now formally tractable") should be hedged.
**Discipline entry:** Very strong. OAIS, PREMIS, Dublin Core are the right frameworks. Thibodeau (2002) is the right historical anchor.
**Fixes needed:**
- Hedge Claim 5: "provides the formal criterion and operational measurement protocol" not "makes it formally tractable"
- Section VI needs the most development: specify what CCR-PREMIS integration looks like (which PREMIS elements map to which CT constructs)
- Add existing semantic preservation proposals to literature review (Giaretta & Bicarregui on OAIS extensions, Hunter & Choudhury on digital library preservation)
- This paper is ready to draft — highest priority in MISC track alongside CL-001

---

### IS-002 — Commitment Conservation in Digital Archives
**Venue fit:** STRONG for Archival Science; MODERATE for American Archivist (needs empirical archival examples)
**Abstract:** Three-class framework (records/documents/data) is novel and appropriate. Four transformation types are the right ones.
**Outline:** InterPARES triad connection in Section II must be precise: CCR entails (not just "supports") authenticity, reliability, integrity.
**Key claims:** Claim 2 (CCR as formal operationalization of archival triad) is most important and most demanding — requires formal argument, not assertion of correspondence.
**Discipline entry:** Needs more specific InterPARES Trust (2013-2018) engagement — CT is directly relevant to that program's digital preservation authenticity work.
**Fixes needed:**
- Formalize archival triad connection: prove CCR compliance entails (not supports) authenticity/reliability/integrity per InterPARES definitions. If implication doesn't hold strictly, characterize what does.
- For American Archivist: include at least one concrete archival case study illustrating CT governance in a format migration workflow
- Add ISO 16175-1:2023 (requirements for managing records in business systems) — supersedes earlier versions and more relevant to AI-mediated archival transformation
- Correctly dependent on IS-001 — do not begin until IS-001 is published or fully drafted

---

### STS-001 — Who Loses Meaning? (Sociology/STS)
**Venue fit:** STRONG for SSS and STS&HV; MODERATE for Big Data & Society (needs empirical case)
**Abstract:** Excellent. "A physical law with a social distribution" is exactly the right STS entry point.
**Outline:** Section III ("Who Uses Ungoverned AI Systems?") needs at least one documented empirical case — cannot be purely theoretical for SSS reviewers.
**Key claims:** Claim 1 (decay falls disproportionately on low-governance populations) is correct but needs empirical grounding showing low-governance systems are actually deployed in those contexts. Claim 3 (drift as epistemic injustice) engages Fricker directly — strongest theoretical contribution.
**Discipline entry:** Very strong. Co-production framing (Jasanoff) is correct. Winner ("Do Artifacts Have Politics?") citation appropriate.
**Fixes needed:**
- Section III: add at least one documented instance of AI-mediated transformation in administrative/legal context where commitment drift can be identified (Eubanks provides some — needs more)
- Engage FATE/FAccT literature on disparate impact to position CT's contribution (structural governance density, not statistical outcome disparities)
- Claim 5 ("gap between law's requirement and implementation is a sociotechnical fact") needs to specify which "law's requirement" — is this normative or legal?
- This paper can begin now but needs one empirical anchor to be publishable in SSS

---

### COM-001 — Can Meaning Be Measured? (Communication Studies)
**Venue fit:** MODERATE-STRONG for Journal of Communication; MODERATE for Communication Theory; MODERATE for HCR
**Abstract:** Good. Shannon bridge (Shannon defined information as what survives the channel; CT defines commitment as what survives the governed channel) is the paper's strongest move.
**Outline:** Section V ("Shannon Completed") risks overclaim — CT completes the fidelity picture for deontic content, not meaning-in-general. Weaver's commentary in Shannon & Weaver (1949) deliberately left meaning aside.
**Key claims:** Claim 4 ("Shannon + CT = complete account of communicative fidelity") is overclaimed.
**Discipline entry:** Adequate but needs more CMC and AI-mediated communication literature (Walther, Hancock) to show why CT matters beyond Shannon for current AI communication research.
**Fixes needed:**
- Hedge Claim 4: CT completes the framework "for deontic content in high-stakes communication" — not communicative fidelity simpliciter
- Add CMC and AI-mediated communication literature (Walther's Social Information Processing, Hancock, emerging AI chatbot/agent communication)
- Section V: explicitly cite Weaver's commentary acknowledging the meaning gap — CT fills it for a defined class of content
- Consider whether full EXP-001-007 record (not just EXP-003, EXP-007) can be summarized in communication-theoretic terms for Journal of Communication

---

### ECON-001 — The Price of Drift (Economics)
**Venue fit:** WEAK for Journal of Economic Theory (requires rigorous proofs); MODERATE for Information Economics and Policy
**Abstract:** Well-framed. Market failure / externality framing is correct. Akerlof analogy appropriate.
**Outline:** Section II ("Formal Setup") is critical — model type is unspecified. "Stylized economy" is too vague for economics reviewers.
**Key claims:** Claims 1-3 require a working formal model before they can be assessed. Drift probability distribution (claim 2) needs specification.
**Discipline entry:** Coase/Akerlof/Arrow/Tirole citations appropriate. Needs contract theory engagement (Hart & Moore, Holmstrom) for underinvestment claims.
**Fixes needed:**
- BLOCKING: Specify formal model type before writing — principal-agent, incomplete contracting, or search/matching? Choice determines entire formal development
- Remove Journal of Economic Theory from primary venue list — add RAND Journal of Economics or JL&E&O as alternates; keep IEP as primary
- Status "requires economic modeling" is accurate — cannot begin until model exists and generates three claimed results
- Specify drift probability distribution parameters — estimate from CT experimental corpus or acknowledge as parameter to be estimated
- L-002 empirical data dependency should be flagged as stronger (needed for ex post cost model parameterization)

---

### GOV-001 — Comparative Governance Analysis
**Venue fit:** MODERATE for Nature Machine Intelligence; STRONG for AI & Society; STRONG for ACM FAccT
**Abstract:** Strategically sharp but title is a liability — "The Only Governance Framework with a Law" reads as polemical to peer reviewers. Five-dimension comparison is right methodological move.
**Outline:** Section VI (Compatibility and Sufficiency) is the key logical contribution — needs a worked example showing a system that satisfies Constitutional AI / NIST / EU AI Act while violating CT's Conservation Law.
**Key claims:** Claim 1 ("only framework with a law") needs to be demonstrated through the comparison, not asserted. Claim 3 (existing frameworks insufficient rather than competing) is the most defensible organizing thesis.
**Discipline entry:** FAccT audience is most appropriate. Paper needs to engage Jobin et al. 2019 (AI ethics guidelines inventory), Hagendorff 2020 (AI ethics meta-analysis) to position CT against existing governance comparisons.
**Fixes needed:**
- CHANGE TITLE: "Governing the Transformation: Commitment Theory and the Missing Semantic Layer in AI Governance Frameworks"
- Section VI needs a worked example: real or hypothetical AI system satisfying all Constitutional AI/NIST/EU AI Act requirements while producing measurable commitment drift
- For Nature Machine Intelligence: needs a technical component (measurement study) to be considered beyond perspective section
- Engage Jobin et al. 2019 and Hagendorff 2020 meta-analyses as prior work

---

### CAP-001 — Semantic Channel Capacity (Capstone)
**Venue fit:** MODERATE for IEEE TIT (aspirationally correct; requires mathematically complete proof)
**Abstract:** Shannon analogy stated precisely — most technically rigorous use of Shannon bridge across MISC track. Three corollaries recovering Papers 1-3 is the right unifying move.
**Outline:** Section IV (Theorem Statement and Proof) is the entire paper. Functional form C_s = f(ρ_g, h_s, κ) needs to be specified — additive? Multiplicative? Log-linear?
**Key claims:** Claim 1 parameters (ρ_g, h_s, κ) are specified — better than most plans. But functional form C_s undetermined.
**Discipline entry:** IEEE TIT reviewers are pure information theorists — must demonstrate C(S) is a well-defined mathematical object with channel-capacity semantics isomorphic to Shannon's formulation, not just analogically similar.
**Fixes needed:**
- Specify functional form of C_s and provide informal proof sketch — without this, "long-term" is optimistic
- Clarify whether h_s is derived from information-theoretic entropy or defined operationally from CT harness — IEEE TIT requires rigorous definition
- Consider ISIT (IEEE International Symposium on Information Theory) as a first venue for a shorter proof before full journal treatment
- Shared blocking gap with Paper 2: C(S) must be formalized as info-theoretic object first

---

### CAP-002 — Commitment Theory (Monograph)
**Venue fit:** STRONG aspiration (OUP/CUP/MIT Press appropriate); not assessable at plan stage
**Abstract:** Appropriately structured as prospectus. Four-part organization (foundations/architecture/applications/extensions) is correct. "Falsify It" conclusion is right intellectual positioning.
**Outline:** Chapter 12 synthesis (STS-001, COM-001, ECON-001 → "Social Distribution of Semantic Entropy") is a good synthesis move. Part II (MO§ES, SIGSYSTEM, Governance Density) must add synthetic value beyond compilation.
**Key claims:** All five monograph-level claims appropriate. Claim 3 (interdisciplinary scope) is the organizing thesis.
**Discipline entry:** Not applicable — determined by press's peer review assignment.
**Fixes needed:**
- Identify target series at each press (MIT Press Linguistics/Cognitive Science vs. MIT Press Information Policy — different audiences)
- Ensure Part II adds interpretive synthesis across MO§ES/SIGSYSTEM/Governance Density, not just republication
- Chapter 16 (Open Questions) is potentially the most valuable chapter — give it explicit planning attention now, not just a placeholder title
- Correctly gated on "full evidence base complete" — do not begin until all track papers are complete or drafted

---

## MISC Track Summary

**Strongest plans — ready to write or nearly so:**
1. **CL-001** — Most immediately executable with most compelling empirical hook. Write first.
2. **IS-001** — Clean discipline entry, existing material maps directly, ready to draft.
3. **STS-001** — Excellent theoretical framing; needs one empirical anchor, otherwise publication-ready in conception.
4. **FS-001** — Best-positioned formal paper; blocked only by the canonical invariant definition needing to be worked out.

**Plans needing most work before writing:**
1. **ECON-001** — Cannot be written until formal economic model exists. Model type unspecified = blocking gap.
2. **CAP-001** — Entire paper rests on formal proof not yet sketched. Theorem functional form must be specified.
3. **FS-002** — Depends on FS-001; needs deeper contemporary philosophy of language engagement.
4. **CL-002** — Classification algorithm circularity problem must be addressed at plan stage, not during writing.

**Cross-track issues:**
- Shannon analogy appears in CL-001, FS-001, COM-001, CAP-001 independently. FS-001 should be canonical — all others cite rather than develop it independently.
- GOV-001 title change is the single highest-return fix (one word → publishable frame).
- Deontic/epistemic disambiguation appears in nearly every plan. Should be one-sentence footnote citing P-000 and FS-001, not a paragraph in each paper.
