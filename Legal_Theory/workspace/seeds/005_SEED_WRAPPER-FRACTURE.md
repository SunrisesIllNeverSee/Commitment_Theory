# DOC 005 | THE WRAPPER FRACTURE: PRIVATIZED PROTECTION ON PUBLIC INFRASTRUCTURE

**Date:** 2026-04-20  
**Document ID:** 005_SEED_WRAPPER-FRACTURE  

---

## The Architecture

Every major legal AI platform runs on publicly available foundation models.

**Harvey** — Built on Claude (Anthropic). $11 billion valuation as of March 2026. $760 million raised in 2025 alone. Sequoia, Andreessen Horowitz, GIC, Kleiner Perkins. Available to law firms by enterprise subscription. The underlying model is the same Claude available to any consumer at claude.ai for $20/month.

**CoCounsel** — Built on GPT-4 (OpenAI). Thomson Reuters product. Acquired Casetext for $650 million (August 2023). Integrated with Westlaw. Holds the federal judiciary contract (April 2025) providing access to 25,000+ federal legal professionals. The underlying model is the same GPT-4 available to any consumer through ChatGPT.

**Lexis+ AI / Protégé** — LexisNexis product. Uses multiple foundation models including partnerships with major AI providers. Available to LexisNexis subscribers.

**Spellbook** — Built on GPT-4. Contract drafting AI. Runs as a Microsoft Word add-in.

**fleetAI** — Dentons (world's largest law firm by lawyer count). Built on GPT-4.

**DWT Prose** — Davis Wright Tremaine. Integrates "multiple commercially available LLMs alongside custom AI models developed in-house."

As of March 2026, Legaltech Hub mapped 1,014 generative AI product placements in legal tech. The vast majority are wrappers around the same small set of foundation models: Claude (Anthropic), GPT-4/GPT-5 (OpenAI), Gemini (Google). Some add proprietary legal training data. Some add document management infrastructure. Some add Westlaw or LexisNexis integration. All of them process their users' prompts through foundation model infrastructure owned and operated by the same companies that serve the public consumer platforms.

---

## The Poison Well

The metaphor is precise. Every user of Claude — whether through Harvey's $50,000+/year enterprise subscription or through claude.ai's $20/month consumer plan — is drinking from the same well. The water is the model. The model's weights, architecture, training data, and reasoning capabilities are the same across both access tiers.

The enterprise agreement between Harvey and Anthropic adds a contractual layer. Anthropic's enterprise API terms typically include commitments not to train on enterprise customer data, data processing addendums, SOC 2 compliance, data retention controls, and confidentiality provisions. These are contractual promises about how the data will be handled by the company.

They are NOT architectural guarantees about how the model processes the data.

The same model weights that process a Harvey attorney's privileged case strategy memo process a consumer user's identical legal research. There is no Harvey partition inside the model. There is no enterprise memory wall that segregates attorney prompts from consumer prompts. The model processes each prompt through the same weights, the same layers, the same architecture. The enterprise terms promise that Anthropic won't extract the attorney's data for training purposes. But the model itself — the computational artifact that generates the output — is shared.

The contracts between the wrappers and the model providers are almost certainly structured as commercial licensing agreements — IP access, usage rights, SLAs, data handling commitments. They are NOT structured as architectural segregation guarantees. The distinction matters because the Heppner court's reasoning was based on the platform's structural characteristics — the privacy policy, the data handling practices, the third-party disclosure potential. If the structural characteristics are the basis for the ruling, those characteristics apply to the shared infrastructure regardless of the contractual layer sitting on top.

**No publicly available contract between any legal AI wrapper and its underlying model provider has been examined to determine whether it addresses:**

— Whether model weights trained on or influenced by one customer's data can affect outputs for other customers
— Whether there is computational segregation between enterprise and consumer data paths
— Whether the "confidentiality" the wrapper promises its attorney users is a contractual commitment or an architectural guarantee
— Whether the model provider's obligations under the contract survive a government subpoena for data processed through the enterprise API
— Whether the enterprise agreement explicitly addresses the work product doctrine or merely addresses commercial data confidentiality (which is a different legal concept)

Until these contracts are examined, the entire legal AI industry's work product protection is built on an assumption — that the enterprise wrapper creates sufficient confidentiality to preserve privilege — that has never been tested against the Heppner court's reasoning.

---

## The Privatization of Public Capability

The foundation models are public. Claude is available to anyone. ChatGPT is available to anyone. Gemini is available to anyone. The capability — legal research, statutory analysis, case law interpretation, strategic reasoning — is a public capability delivered through a publicly accessible tool.

The legal AI wrappers took this public capability and privatized the protection layer. They built subscription-only interfaces, added proprietary legal data integrations, and marketed the result as confidential attorney tools. The capability is the same. The model is the same. What they sell is the wrapper — and the wrapper is what the system recognizes as the basis for work product protection.

The wrapper is not a technology product. It is a credentialing product. It says: this is an attorney tool, used by attorneys, for attorney work. Therefore the output is attorney work product. The same model, accessed through the consumer platform by a non-attorney, produces output that is not work product — because the access tier identifies the user as a non-attorney.

The protection follows the subscription, not the work.

---

## The Constitutional Implications

### 1. Equal Protection — Fourteenth Amendment

The wrapper creates two tiers of constitutional protection for identical work performed on identical infrastructure:

— Attorney using Harvey (Claude) → protected work product
— Non-attorney using Claude (Claude) → discoverable under Heppner

The classification (subscription tier / credential) does not serve the government interest the work product doctrine claims to protect (thorough case preparation / adversarial integrity). It serves the commercial interest of the wrapper companies and the credentialing interest of the legal profession. When a classification in the exercise of constitutional rights serves commercial or guild interests rather than legitimate government interests, it is subject to heightened equal protection scrutiny.

### 2. Due Process — Fifth and Fourteenth Amendments

The adversarial system requires a structurally level playing field. When one side's AI-assisted preparation is protected (because it passed through a paid wrapper) and the other side's AI-assisted preparation is discoverable (because it passed through the consumer version of the same model), the playing field is structurally tilted. The tilt is not based on the quality of the work, the nature of the analysis, or the purpose of the preparation. It is based on the access tier. That is not due process. That is economic stratification of constitutional protection.

### 3. First Amendment — Right to Petition / Access to Courts

Meaningful access to the courts requires the ability to prepare. AI is the most powerful preparation tool ever made available to the public. If using the public version of the tool strips the preparation of constitutional protection — while the privatized version of the same tool preserves it — then meaningful access is conditioned on the ability to pay for the privatized version. The right to petition becomes a right to petition if you can afford the enterprise subscription.

### 4. Civil Rights — Access to Justice

The access-to-justice implications extend beyond constitutional doctrine into civil rights. The populations most affected by the protection asymmetry are the populations civil rights law is designed to protect: indigent defendants, crime victims without counsel, persons navigating the legal system without professional representation, communities historically underserved by the legal profession. AI offered these populations the first real opportunity to close the capability gap with represented parties. The wrapper model — and the Heppner ruling — threaten to convert that opportunity into a new form of disadvantage: you can do the work, but the work is not protected unless you paid for the right wrapper.

---

## The Unfair Advantage — Mapped

### What attorneys have access to that the public does not:

**1. Westlaw AI / CoCounsel** — AI-powered legal research with live connection to the Westlaw database. Complete federal and state case law, statutes, regulations, secondary sources. AI-synthesized research memos with verified citations. The public has no equivalent. Free legal databases (Google Scholar, CourtListener, Public.Law) lack the comprehensiveness, currency, and AI synthesis capabilities. CoCounsel holds the federal judiciary contract — the federal courts themselves use the tool that is available only to subscribers.

**2. Harvey** — AI-powered document analysis, contract review, due diligence, compliance, legal research. Trained on legal-specific data in addition to the foundation model. Enterprise confidentiality terms. No public equivalent.

**3. Lexis+ AI / Protégé** — AI-powered Shepardize citation verification, agentic research workflows, automated case analysis. Available only to LexisNexis subscribers.

**4. Practice management AI** — Clio Manage AI, Smokeball Archie, and similar tools automating case calendaring, document assembly, client communication, billing. Designed for law firms. No public equivalent for non-lawyers managing legal matters.

**5. Enterprise confidentiality terms** — Data processing addendums, zero-retention training policies, matter-specific isolation, SOC 2 compliance. Available only through enterprise subscriptions that cost thousands to tens of thousands of dollars annually.

### What the public has access to:

**1. Consumer AI** — Claude, ChatGPT, Gemini. Same foundation models. Same reasoning capabilities. No legal-specific training data integration. No live case law database connection. Privacy policies that — per Heppner — strip confidentiality from non-lawyer use.

**2. Free legal databases** — Google Scholar (incomplete case law), CourtListener (nonprofit, limited), Public.Law (state statutes, no AI). No AI synthesis. No citation verification. No research memos.

**3. Public law libraries** — Physical access. No AI. No digital search optimization. Declining funding and availability.

**4. Legal aid clinics** — Means-tested. Subject-matter-restricted. Wait-listed. Available in limited jurisdictions. Insufficient to meet demand.

### The gap:

The attorney has AI tools that produce protected analysis from a comprehensive, verified legal database with enterprise confidentiality and citation verification. The public has AI tools that produce unprotected analysis from general training data with no legal database integration and a privacy policy the court has ruled strips confidentiality. The capability of the underlying models is comparable. Everything else — database access, confidentiality, protection status — is gated by subscription and credential.

---

## Is Anyone Discussing This?

### As of April 20, 2026: No.

No academic paper, law review article, legal commentary, bar association publication, policy brief, advocacy organization report, or judicial opinion addresses the constitutional implications of the legal AI wrapper model — specifically, the privatization of constitutional work product protection through proprietary wrappers built on public foundation model infrastructure.

The legal AI discourse as of April 2026 focuses on:
— Product capabilities and benchmarks (VLAIR report, February 2025)
— Market consolidation (Thomson Reuters / Casetext, Harvey / LexisNexis partnership, Clio / vLex acquisition)
— Enterprise adoption rates (26% of legal organizations actively using generative AI per Thomson Reuters April 2025 survey)
— Agentic AI and workflow automation
— Confidentiality terms and data handling (addressed as a commercial/risk management question, not a constitutional question)

The closest any commentary has come:
— Proskauer's one-sentence observation about Warner's "access-to-justice implications" (March 2026)
— Sidley Austin's one-sentence reference to "questions about access to justice for unrepresented litigants" (April 2026)
— No commentary addresses the shared infrastructure problem, the contractual vs. architectural confidentiality distinction, the wrapper as a credentialing product, or the constitutional equal protection implications of tiered AI access producing tiered constitutional protection

The field is empty. The argument does not exist in the literature. This document is first.

---

*This document maps the wrapper fracture: the privatization of constitutional work product protection through proprietary legal AI platforms built on publicly available foundation model infrastructure. It connects to DOC 001 (The Constitutional Fracture), DOC 002 (The Claim), DOC 003 (Actionable Paths), and DOC 004 (The Pre-AI Landscape). Together, these five documents form a complete seed package identifying a constitutional gap that the legal profession, the AI industry, the academic literature, and the advocacy community have not yet identified.*
