# ECON-001 — The Price of Drift: Quantifying the Economic Cost of Ungoverned Commitment Degradation

**Track:** MISC — Economics
**Layer:** 3 (Application)
**Status:** BLOCKED — formal model type must be specified before writing
**Target Venue:** Information Economics and Policy / RAND Journal of Economics / Journal of Law, Economics & Organization
**Est. Length:** TBD
**Dependencies:** Paper 0 published; L-002 empirical data beneficial

---

## Abstract

Commitment drift in AI-mediated contractual, regulatory, and legal processes has measurable economic costs. This paper develops a formal economic model of the costs of ungoverned commitment degradation — the first such model grounded in a physical law (the Conservation Law of Commitment) rather than in behavioral assumptions or institutional design choices. The model identifies three categories of economic cost. Ex ante costs arise when parties cannot contract on preserved meaning: when AI transformation is known to degrade commitment kernels stochastically, rational parties cannot rely on their agreements to carry their intended obligations, creating underinvestment in legally binding commitments and over-reliance on costly enforcement mechanisms. Ex post costs arise from enforcement failures: when a legal standard, contractual term, or regulatory requirement has been commitment-drifted during AI-mediated processing, enforcement fails not because of bad faith but because the text being enforced no longer carries the commitment it was written to carry. Systemic costs arise from institutional trust erosion: when AI systems routinely degrade commitment kernels in legal and regulatory processes, the legitimacy of those processes depends on an empirically false assumption of semantic continuity. The model connects the Second Law of Semantic Entropy (ΔH_C > 0) to classic results in the economics of information: commitment drift is analogous to information asymmetry, but the asymmetry is between the commitment the text was intended to carry and the commitment the text actually carries after AI transformation — an asymmetry that no amount of ex ante disclosure can eliminate without a CCR-compliant governance architecture.

---

## Outline

I. **Introduction: Commitment Drift as an Economic Problem** — Frames commitment drift in economic terms; argues that the Conservation Law identifies a market failure — the cost of ungoverned commitment degradation is not internalized by AI system operators.

II. **Formal Setup: The Commitment Drift Economy** — Defines the model: a stylized economy with AI-mediated legal and contractual processes; defines commitment drift as a stochastic tax on legal meaning; connects the Second Law to a drift probability distribution.

III. **Ex Ante Costs: The Contracting Problem** — Models ex ante costs: when commitment drift probability is positive, rational parties face a mean-field uncertainty about what their agreements will carry after AI processing; derives the underinvestment result.

IV. **Ex Post Costs: Enforcement Failure** — Models ex post costs: when a commitment-drifted text is enforced, the enforcement error rate is a function of the drift magnitude and the failure mode distribution; derives the enforcement cost using L-002's empirical failure mode data.

V. **Systemic Costs: Institutional Trust Erosion** — Models systemic costs using repeated game theory: when AI-mediated legal processes have a positive commitment drift rate, the equilibrium trust level in those processes is reduced; derives the institutional cost.

VI. **The Value of CCR Compliance** — Derives the economic value of CCR compliance: a CCR-compliant system eliminates ex ante costs (parties can contract on preserved meaning), reduces ex post costs to zero under perfect governance, and restores institutional trust; estimates the CCR compliance premium.

VII. **Implications for AI Governance Policy** — Discusses the policy implications: commitment drift is a negative externality that market mechanisms will not correct without regulatory intervention; the CCR is the minimum intervention required to internalize the cost.

---

## Key Claims

- Commitment drift in AI-mediated legal and contractual processes has three economically distinct cost categories: ex ante contracting costs, ex post enforcement costs, and systemic institutional trust erosion costs.
- The Second Law of Semantic Entropy (ΔH_C > 0) generates a stochastic drift probability distribution that can be modeled as a tax on legal meaning — a market failure that AI system operators do not currently internalize.
- CCR compliance eliminates ex ante contracting costs (parties can rely on meaning preservation), reduces ex post enforcement costs, and restores institutional trust — generating an economic value premium for CCR-compliant systems.
- Commitment drift is analogous to information asymmetry but cannot be corrected by ex ante disclosure: the asymmetry between intended and actual commitment cannot be eliminated without governance-level intervention.
- The economic case for the CCR is a market failure argument: commitment drift is a negative externality, and without regulatory intervention, it will be underaddressed by market mechanisms.

---

## Blocking Gap — Model Type Must Be Decided First

The paper cannot be written until Section II ("Formal Setup") specifies which class of economic model generates the three cost results. The choice is not stylistic — it determines the proof structure and what data is needed.

**Three candidate model families — pick one:**

**Option A: Incomplete contracting model (Hart & Moore 1988 / Holmstrom & Milgrom)**
- Models commitment drift as a non-contractible contingency — parties cannot write complete contracts because the meaning of their agreement will be transformed by an AI system not under their control
- Ex ante cost: underinvestment in relationship-specific assets (Holmstrom-style)
- Ex post cost: renegotiation inefficiency when drifted text is enforced
- Systemic cost: equilibrium incompleteness of AI-mediated contracts
- Strength: connects directly to Hart's Nobel-recognized framework; IEP and RAND JE audiences know it
- Data needed: estimate ρ (probability of commitment drift) from EXP-003; no L-002 data required for core model

**Option B: Principal-agent model with moral hazard**
- AI system operator = agent; parties relying on AI-mediated legal processes = principals
- Commitment drift = hidden action (operator chooses governance density ρ_g; principals observe output not governance)
- Ex ante cost: adverse selection (principals cannot distinguish CCR-compliant from non-compliant operators)
- Ex post cost: monitoring cost + enforcement failure probability
- Systemic cost: market for AI governance collapses to low-governance equilibrium (Akerlof lemons)
- Strength: cleanest connection to Akerlof analogy in abstract; most legible to information economics audience
- Data needed: governance density ρ_g distribution across deployed AI systems (not currently available — would need to be modeled parametrically)

**Option C: Repeated game / institutional trust model**
- Models the systemic cost first, treats ex ante and ex post as special cases
- AI-mediated legal process = long-run game between state/institutions and parties
- Commitment drift rate = defection probability in a cooperation game
- Trust equilibrium: derived from Folk Theorem — trust is sustained iff drift rate < critical threshold
- Strength: makes the systemic cost claim (Section V) the paper's centerpiece, which is the most original contribution
- Data needed: EXP-003 drift rate data sufficient for parametric illustration

**Recommendation:** Option A (incomplete contracting) for IEP/RAND JE; Option B (principal-agent) if the goal is maximum connection to Akerlof framing in the abstract. Option C is structurally the most original but requires the most technical machinery.

**Decision gate:** Choose the model type, specify the formal setup in Section II (2-3 equations), confirm the three cost results follow from that setup — then begin writing.

---

## Citation Notes

- **Cites:** Paper 0 (Conservation Law, Second Law); P-000 (CT definitions); L-001 (doctrinal framing); L-002 (empirical failure mode distribution); STS-001 (population distribution of commitment drift costs); Coase (externalities); Akerlof (information asymmetry); Arrow (information economics); Tirole & Laffont (regulation theory)
- **Cited by:** L-004 (policy brief uses ECON-001's market failure argument for CCR regulation); CAP-002 (monograph economics chapter)
