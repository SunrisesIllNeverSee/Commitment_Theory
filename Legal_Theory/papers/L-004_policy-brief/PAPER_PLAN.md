# L-004 — Commitment Conservation Requirements for AI in Civil Rights Enforcement: A Policy Framework

**Track:** Legal_Theory
**Layer:** 3 (Application — Policy)
**Status:** Planned — parallel with L-002/L-003
**Target Venue:** Brookings / Stanford HAI / Berkman Klein Center / Georgetown ITLP
**Est. Length:** 3,000–5,000 words
**Dependencies:** L-001 submitted

---

## Abstract

This policy brief translates Commitment Theory's empirical and legal findings into actionable policy recommendations for agencies, regulators, and legislators responsible for governing AI systems deployed in civil rights enforcement contexts. The brief addresses three audiences: federal agencies deploying AI in benefits administration, employment regulation, and housing enforcement (EEOC, HUD, SSA, DOJ Civil Rights Division); state and local governments deploying AI in public benefits, criminal justice, and education; and Congress and the FTC considering AI governance legislation. The central recommendation is a Commitment Conservation Requirement (CCR) — mandating that AI systems operating on civil rights statutory text must preserve the commitment kernel (obligations, prohibitions, modal constraints) of that text across every transformation step, verified by a validated measurement oracle and documented in an auditable lineage record. The brief explains the CCR in non-technical terms, provides three concrete implementation scenarios, addresses cost and feasibility concerns, and distinguishes the CCR from existing AI governance requirements (NIST AI RMF, EU AI Act, state AI laws). The CCR is not technically burdensome: minimum governance (the CT sparsity bound) is sufficient, and right-sized implementations already exist. The brief concludes that commitment conservation is not a luxury for well-resourced agencies — it is the minimum standard that existing civil rights doctrine requires of AI-mediated legal processes.

---

## Outline

I. **The Problem in Plain Language** — Explains commitment drift to a non-technical policy audience using the two anchor scenarios from L-001 (the Title VII algorithm and the benefits-denial notice); establishes the scale of the problem.

II. **What the Law Already Requires** — Explains, in non-technical terms, the doctrinal implications of Mathews v. Eldridge, Griggs, and FRE 901 for AI-mediated civil rights enforcement; connects existing doctrine to the CCR without requiring legal expertise to follow.

III. **The Commitment Conservation Requirement: Policy Statement** — States the CCR as a policy standard; explains what compliance requires in operational terms; addresses what agencies must do, what they must not do, and how compliance is verified.

IV. **Three Implementation Scenarios** — Provides three concrete scenarios: (1) EEOC AI-assisted complaint screening, (2) SSA benefits eligibility AI processing, (3) DOJ Civil Rights Division document review AI; describes CCR compliance in each context.

V. **Cost, Feasibility, and Existing Solutions** — Addresses the feasibility and cost concerns directly; explains that minimum governance (CT sparsity bound) is sufficient; describes existing CCR-compliant architectures.

VI. **Recommendations** — Provides specific, actionable recommendations for federal agencies, state governments, and Congress; distinguishes mandatory minimums from best practices.

---

## Key Claims

- AI systems deployed in civil rights enforcement contexts routinely degrade the commitment kernel of the legal standards they are designed to apply — this is measurable, predictable, and preventable.
- The Commitment Conservation Requirement is the minimum standard that existing civil rights doctrine requires of AI-mediated legal processes; it is not a new regulatory burden but a formalization of existing obligations.
- CCR compliance is achievable with minimum governance (CT sparsity bound); agencies need not adopt maximally constrained systems, only sufficiently constrained ones.
- The populations most exposed to commitment drift — benefits claimants, unrepresented parties, pro se litigants — are the populations existing civil rights law was designed to protect; the governance failure and the doctrinal gap align.
- Existing CCR-compliant architectures (MO§ES-compliant systems) demonstrate that the technical requirements are feasible for realistic agency deployment contexts.

---

## Writing Notes

**Structural revision — collapse Sections II and III:**
Sections II ("What the Law Already Requires") and III ("The Commitment Conservation Requirement: Policy Statement") currently overlap. For a policy brief at Brookings/Stanford HAI/Berkman Klein, combine into a single section: "The Legal Standard and What It Requires" — state the doctrinal basis and the CCR together in policy language. This tightens the brief and avoids the impression that the legal argument and the policy recommendation are separate.

**Section V — add concrete cost/burden estimate:**
The feasibility claim must include at least one concrete figure. Options: (a) estimate the per-document cost of running the CT harness on a statutory provision (compute time, oracle API cost); (b) estimate the compliance overhead as a percentage of existing AI system deployment costs; (c) cite comparable compliance costs from existing regulatory frameworks (HIPAA compliance costs per entity, GDPR compliance survey data). Without a number, the "not technically burdensome" claim is an assertion, not evidence.

**Timing flag — if published before L-002:**
If L-004 is published before L-002's empirical data is available, all claims must rest on Paper 0's experimental record and L-001's doctrinal scenarios only. Do not cite L-002 results that do not yet exist. Add a note in the introduction: "Empirical validation of commitment drift in specific civil rights statutory provisions is the subject of ongoing work (L-002); this brief's recommendations rest on the general empirical record established in [Paper 0] and the doctrinal analysis in [L-001]."

---

## Citation Notes

- **Cites:** Paper 0 (Conservation Law, empirical record); L-000 (legal propositions); L-001 (doctrinal framework); L-002 (empirical evidence when available); L-003 (CCR technical standard); P-000 (CT definitions); NIST AI RMF; EU AI Act; Mathews v. Eldridge; Griggs; FRE 901
- **Cited by:** L-006 (amicus briefs cite L-004 for policy context); L-008 (capstone uses L-004 as evidence of CT's policy penetration); GOV-001 (comparative governance analysis cites L-004 as a CT policy application)
