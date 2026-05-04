# IS-001 — A Conservation Law for Digital Meaning: Formal Foundations for Semantic Preservation in Information Systems

**Track:** MISC — Information Science
**Layer:** 3 (Application)
**Status:** Can write from existing material
**Target Venue:** JASIST / Journal of Documentation / Information Processing & Management
**Est. Length:** TBD
**Dependencies:** Paper 0 published

---

## Abstract

Information science has grappled for decades with the problem of semantic preservation: as digital objects migrate across formats, systems, and time, does their meaning survive? Existing frameworks — OAIS (Open Archival Information System), PREMIS (Preservation Metadata: Implementation Strategies), Dublin Core — provide metadata schemas and preservation strategies but lack a formal criterion for semantic preservation. They can tell you whether a file has migrated successfully at the bit level; they cannot tell you whether the meaning of the content has survived. The Conservation Law of Commitment provides the missing foundation. CT defines semantic preservation formally as C(T_gov(S)) = C(S) — the commitment kernel of a semantic object must be conserved across every transformation step — and provides an operational measurement protocol (the CT harness) for verifying whether preservation has occurred. This paper introduces CT to the information science community, argues that the Commitment Conservation Requirement (CCR) is the missing semantic layer above OAIS and PREMIS's bit-level preservation framework, and demonstrates how the CCR can be operationalized within existing information systems infrastructure. The paper also applies the failure mode taxonomy (nine modes from CL-001) to the specific transformation types common in digital preservation: format migration, system migration, transcription, summarization for discovery, and AI-mediated description. Each failure mode maps onto a specific preservation risk that information scientists already recognize but have lacked the formal vocabulary to characterize.

---

## Outline

I. **Introduction: The Semantic Layer Information Science Has Lacked** — Frames the gap: existing digital preservation frameworks are complete at the bit level but silent at the semantic level; CT provides the missing layer.

II. **Existing Frameworks and Their Limits** — Reviews OAIS, PREMIS, and Dublin Core; identifies the specific gap each leaves at the semantic level; demonstrates that none provides a formal criterion for meaning preservation.

III. **The Conservation Law of Commitment: Introduction for Information Scientists** — Introduces CT's framework (commitment kernel, conservation law, second law, oracle) for an information science audience; connects the framework to information science's existing vocabulary (information, document, record, authenticity).

IV. **The Commitment Conservation Requirement as a Preservation Standard** — Proposes the CCR as the semantic preservation standard above OAIS and PREMIS; describes what CCR compliance requires in information systems terms.

V. **Applying the Failure Taxonomy to Preservation Contexts** — Maps the nine failure modes onto digital preservation transformation types (format migration, system migration, transcription, summarization, AI description); identifies which preservation operations are most vulnerable to which failure modes.

VI. **Implementation: CT within Existing Information Systems Infrastructure** — Describes how the CCR can be operationalized within OAIS-compliant systems; connects the Lineage DAG to PREMIS provenance metadata; discusses the measurement oracle's role in automated preservation workflows.

VII. **Conclusion: Semantic Preservation as a Solvable Problem** — Argues that CT makes semantic preservation formally tractable for the first time; invites the information science community to test, extend, and contest the framework.

---

## Key Claims

- Existing digital preservation frameworks (OAIS, PREMIS, Dublin Core) are complete at the bit level but lack a formal criterion for semantic preservation; CT provides the missing semantic layer.
- The Commitment Conservation Requirement (C(T_gov(S)) = C(S)) is the formal semantic preservation standard that information science has lacked; it is operationally measurable using the CT harness.
- The nine failure modes from CL-001 map directly onto digital preservation transformation types; information scientists can use the taxonomy to identify which preservation operations pose the greatest semantic risk.
- CT's Lineage DAG (from MO§ES) is implementable within OAIS's provenance metadata framework (PREMIS), enabling CCR compliance within existing digital preservation infrastructure.
- Semantic preservation is now a formally tractable problem: CT provides the criterion, the measurement protocol, and the governance architecture needed to address it systematically.

---

## Writing Notes

**Hedge Claim 5 — "formally tractable" is an overclaim without a proof:**
Claim 5 states "semantic preservation is now a formally tractable problem." This is true only if the commitment kernel can be reliably extracted from arbitrary digital objects — which the current harness cannot do (it works on natural language text, not images, audiovisual material, or structured data). Hedge to: "For text-based digital objects with deontic content, semantic preservation is now a formally tractable problem; extension to non-textual digital objects is a research frontier."

**PREMIS mapping — provide specific crosswalk in Section VI:**
The claim that CT's Lineage DAG maps onto PREMIS provenance metadata must be supported by a concrete mapping. Provide a crosswalk table:
- PREMIS Event → CT transformation step (T_i)
- PREMIS Agent → CT oracle / governance engine identifier
- PREMIS Object → CT semantic object (S)
- PREMIS Rights → CT commitment kernel (C(S))
This crosswalk makes the implementation claim concrete and gives information scientists something they can evaluate against their existing infrastructure.

**Related Work — add existing semantic preservation proposals:**
The paper claims CT is the first formal criterion for semantic preservation. Anticipate the objection that semantic preservation has been discussed before:
- Thibodeau (2002) on "macro-preservation" (preserving the ability to reproduce intellectual content) — similar goal but no formal criterion or measurement protocol
- Rothenberg (1999) on emulation as preservation strategy — addresses format obsolescence but not semantic fidelity
- Heslop et al. (2002) on "significant properties" — the closest existing work; CT's commitment kernel is a formalization of "significant properties" for deontic content specifically

---

## Citation Notes

- **Cites:** Paper 0 (Conservation Law, failure taxonomy, harness); CL-001 (failure mode taxonomy); P-000 (CT definitions); MO§ES architecture paper (Lineage DAG, PREMIS connection); OAIS (CCSDS 650.0-M-2); PREMIS Data Dictionary; Dublin Core Metadata Initiative; Thibodeau (2002) on digital preservation
- **Cited by:** IS-002 (archival application extends IS-001 to archives specifically); CAP-002 (monograph information science chapter)
