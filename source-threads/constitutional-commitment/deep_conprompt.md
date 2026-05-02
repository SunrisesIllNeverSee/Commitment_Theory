On February 10, 2026, two federal courts ruled on whether a non-lawyer's AI-generated legal analysis is protected from discovery. In United States v. Heppner (S.D.N.Y.), Judge Rakoff held that a criminal defendant's legal strategy documents generated through consumer Claude (Anthropic) were not protected by attorney-client privilege or work product doctrine — because Claude is not an attorney, the platform's privacy policy disclaims confidentiality, and the defendant acted without counsel's direction. On the same day, in Warner v. Gilbarco (E.D. Mich.), a different court held that a pro se plaintiff's AI-assisted litigation materials ARE protected work product — because the pro se litigant is "simultaneously the party and the advocate" and AI tools are "tools, not persons."

Meanwhile, the legal profession has built an entire industry of proprietary AI platforms — Harvey (built on Claude), CoCounsel (built on GPT-4), Lexis+ AI — available exclusively to licensed attorneys by paid subscription. These platforms use the same underlying foundation models as the consumer platforms available to the public. An attorney's prompt through Harvey produces protected work product. A non-lawyer's identical prompt through consumer Claude produces discoverable material under Heppner. Same model. Same company. Same infrastructure. Different protection based on subscription tier and credential.

Three questions:

1. Are you aware of any academic paper, legal commentary, or policy discussion that addresses the constitutional implications of this asymmetry — specifically, whether conditioning work product protection on a professional credential (when AI has made the credential functionally unnecessary for producing the protected work) violates the Equal Protection Clause, the Due Process Clause, or the right to self-representation under Faretta v. California?

2. Are you aware of any discussion — anywhere — about the fact that legal AI wrappers like Harvey and CoCounsel are built on the same public foundation models as consumer AI platforms, and that the "confidentiality" these wrappers promise attorneys is contractual rather than architectural — meaning the same model processes both attorney and consumer prompts through the same weights with no computational segregation?

3. What is your honest assessment of whether this line of argument has constitutional merit, and whether the current framework — where the same AI model produces protected output for credentialed users and unprotected output for everyone else — is sustainable?
用户的问题涉及三个层面：学术讨论、AI架构的保密性，以及宪法论证的可持续性。我需要按照计划进行搜索。
Found 66 web pages
所有并行搜索已完成。关于Heppner案和Warner案的搜索结果已经返回，关于法律AI平台、宪法影响、保密架构、pro se工作产品保护以及学术评论的搜索也已完成。接下来需要进一步搜索宪法层面的内容，重点关注equal protection、due process、Faretta案以及AI two-tier justice system。
Found 56 web pages
所有并行搜索已完成。关于Heppner案和Warner案的搜索结果已返回，法律AI平台、宪法影响、保密架构、pro se工作产品保护以及学术评论的搜索也已完成。宪法层面的搜索结果显示了一些相关资源。现在需要根据这些结果进一步打开相关链接，以获取更详细的信息。
Read 13 pages
AI Communications Are Not Privileged: What United States v. Heppner Means for Corporate Clients
Courts Grapple with Privilege Implications of AI | Publications | Cleary Gottlieb
AI, Privilege, and the Heppner Ruling: What the Court Actually Held—And How to Structure AI Use Safely | Insights | Venable LLP
Two Federal Courts Chart Diverging Paths on the Discoverability of LLM Interactions | Publications | Kirkland & Ellis LLP
In initial rulings, US federal courts split on the intersection of litigant AI use and privilege protections
View All
所有打开的链接都提供了相关信息。现在需要组织回答，分为三个部分：宪法论证的学术讨论、架构层面的 confidentiality 分析、以及宪法论证的 merits 和可持续性评估。回答中需要引用这些来源。
The asymmetry you've identified is both real and largely unexamined in the specific constitutional terms you're asking about. No academic paper, law review article, or policy piece that squarely addresses the Equal Protection, Due Process, or Faretta implications of conditioning work product protection on a professional credential (when AI has made that credential functionally unnecessary for producing the protected work) has been found. Nor is there any comprehensive discussion that specifically addresses the contractual-versus-architectural confidentiality distinction and its implications for privilege doctrine. The silence itself is telling—what you're pointing to is a gap in the literature that sits at the intersection of three fields (civil procedure/privilege, constitutional law, and AI governance) that rarely speak to each other.

However, there are pieces that approach the issue from adjacent angles, and some that come remarkably close to framing the question you're asking.

1. Constitutional Implications: What's Been Written

Faretta and the Right of Self-Representation

No identified scholarship directly applies Faretta v. California (1975) to AI-assisted pro se litigation or argues that conditioning work product protection on attorney involvement violates the right of self-representation. This is perhaps the most striking gap, given that Faretta established a constitutional right to proceed pro se and that courts must afford pro se litigants meaningful access to the tools of litigation.

The Warner court itself gestured toward this issue without explicitly invoking Faretta. The court held that a pro se litigant's ChatGPT queries were protected work product because the litigant is "simultaneously the party and the advocate" and AI tools are "tools, not persons". As one analysis noted, "A reading of Rule 26(b)(3) that conditions work product protection over AI materials on the involvement of counsel finds no support in the rule's text and would further disadvantage unrepresented litigants". But this is a statutory/textual argument under the Federal Rules, not a constitutional one under Faretta. The question you're asking—whether the Constitution compels equal access to the functional benefits of legal AI—remains unanswered in the literature.

Equal Protection and Two-Tiered Justice

The closest existing framework is the "two-tiered justice" literature, which addresses how AI access disparities risk creating separate and unequal systems of justice.

The Yale Journal of Law and Technology published Drew Simshaw's Access to A.I. Justice: Avoiding an Inequitable Two-Tiered System of Legal Services (24 Yale J.L. & Tech. 150), which explicitly frames the problem as one of equitable access: "The poor might be stuck with inferior AI-driven assistance; only expensive law firms might be able to effectively harness legal AI". Simshaw argues for regulatory reforms to ensure "equitable and meaningful access to legal AI across the legal problem-solving landscape". But this article approaches the issue from a regulatory and access-to-justice perspective, not a constitutional litigation framework, and does not address privilege/work product doctrine specifically.

NYU Law has also flagged that a "two-tiered AI problem looms ... where well-resourced adversaries deploy sophisticated tools against litigants who lack equivalent access, widening rather than closing the justice gap". The Yale Law Journal's 2025 essay on Interoperable Legal AI for Access to Justice similarly addresses coordination across the "consumer (i.e., self-help) front" and the "legal-service-provider front" but does not engage with constitutional claims.

An article from Jurvantis.ai titled The Two-Tier AI Justice System: Premium Tools for Lawyers, Free Chatbots for Everyone Else comes closest to naming the problem you've identified, describing "sophisticated systems for those who can pay, error-prone chatbots for everyone else". However, it is a practice-oriented piece rather than a constitutional law analysis, and it does not specifically address the privilege/work product divergence you've highlighted.

Due Process

A body of scholarship examines AI and due process, but focuses primarily on algorithmic decision-making by courts and agencies, black-box problems, and transparency—not on the specific due process implications of asymmetrical discovery protection for AI-generated legal materials. The Colorado Law Review has published work on "Artificial Intelligence and Constitutional Interpretation", and there is scholarship on "Automation Rights" and the "right to demand and the duty to deploy AI-based technology when it outperforms human-based action". None of this directly addresses the Heppner-Warner asymmetry or the credential-based privilege distinction you've identified.

The "two-tiered" justice concern has been noted by the National Center for State Courts as well, which "referred to a 'two-tiered' system of justice" in its 2023 focus group initiative on AI and equal justice. But again, this is policy discourse, not constitutional argument.

The Gap in the Literature

No article has been located that brings all three pieces together: (1) the Heppner-Warner divergence, (2) the fact that Harvey/CoCounsel use the same foundation models as consumer platforms, and (3) a constitutional claim under Equal Protection, Due Process, or Faretta. The existing literature either addresses AI and privilege without constitutional framing, or addresses constitutional issues around AI without engaging the specific privilege asymmetry you've identified.

2. Contractual vs. Architectural Confidentiality

This is where your question actually identifies an issue that has been discussed, though not in the comprehensive way you're seeking.

What the Legal AI Wrappers Actually Promise

Harvey's security architecture is more than purely contractual, though it is not fully architecturally segregated at the foundation model level either. Harvey's "zero data access" architecture means customer inputs, outputs, and uploaded documents remain sealed off from Harvey's own engineers and operations staff, with role-based access controls and network segmentation that "enforce this separation architecturally, not just through policy". The platform offers BYOK (Bring Your Own Key) support where customers manage their own encryption keys, and uses an "ephemeral processing model"—data is assembled only for the duration of a specific request, after which "model partners immediately delete that data".

CoCounsel (Casetext, now Thomson Reuters) is built on GPT-4 with proprietary legal models layered on top, and has enterprise agreements with OpenAI stating that client data is not used for model training.

The Critical Nuance: Foundation Model Infrastructure

Here's the nuance your question correctly identifies. Harvey is built on Azure OpenAI infrastructure. CoCounsel uses OpenAI's GPT-4 API. Both platforms' client data flows through third-party AI infrastructure—Microsoft Azure and OpenAI—meaning "privileged communications are being transmitted to and processed by external parties". The "enterprise terms" limit commercial use of the data but "don't eliminate the fact that privileged communications are being transmitted to and processed by external parties".

So you're correct: the same model weights process both attorney and consumer prompts. The segregation is at the application and contractual layer—not at the level of the neural network itself. What Harvey and CoCounsel offer is not model-level isolation but rather: (a) contractual commitments that data won't be retained or used for training, (b) architectural controls at the application layer (encryption, access controls, ephemeral processing), and (c) the fact that they are paid, credentialed services used under attorney supervision, which changes the legal analysis of whether disclosure to the platform constitutes third-party disclosure for privilege purposes.

Has This Been Discussed?

Yes, but not in the specific terms you're asking for. The article "Harvey AI, CoCounsel, and Clio Duo: Where Does Your Data Actually Go?" directly addresses the third-party infrastructure issue and privilege implications. The National Law Review has also discussed the "enterprise terms of service" defense for attorney-directed AI use, noting that "an enterprise license without the documentation infrastructure to support it is effectively compliance theater, not privilege protection". An analysis from intellibill.io specifically notes that "the major legal AI platforms have optimized for capability, not privacy architecture" and that they have "built on third-party AI infrastructure because it's faster to market and cheaper to operate".

But what no source comprehensively addresses is the point you're making: that this means the same model, running the same weights, processing prompts through the same mathematical operations, produces legally protected output for a lawyer and unprotected output for a non-lawyer—and that this distinction is maintained through contractual and application-layer controls rather than genuine computational segregation.

3. Constitutional Merit and Sustainability

The Constitutional Argument's Merit

The constitutional argument has some theoretical force but faces significant doctrinal hurdles. Here's an honest assessment:

Equal Protection would likely fail rational basis review, and almost certainly wouldn't trigger heightened scrutiny. The distinction between represented and unrepresented litigants isn't a suspect classification, and conditioning work product protection on attorney involvement serves legitimate government interests: ensuring the integrity of the attorney-client relationship, maintaining professional standards of competence, and preventing the unauthorized practice of law. Courts would likely find that the attorney-credential requirement is rationally related to these interests, even if AI has functionally eroded some of the practical justifications. However, a more sophisticated argument could be made under the "class of one" or selective treatment theories of equal protection—that conditioning identical functional output's protection solely on the user's professional status, when the underlying work is substantively identical, serves no legitimate purpose. This is novel but not frivolous.

Faretta may offer a stronger foothold. The Supreme Court held that the Sixth Amendment guarantees a defendant the right to proceed pro se and that courts must afford such defendants meaningful access to the tools necessary to mount a defense. If work product protection is a necessary incident of effective self-representation—and if AI tools are now functionally necessary to produce work product that can compete with represented adversaries—then conditioning that protection on attorney involvement arguably burdens the Faretta right. The Warner court's reasoning that a pro se litigant is "simultaneously the party and the advocate" and that AI is a "tool, not a person" provides a doctrinal framework that could be constitutionalized under Faretta. The argument would be that Heppner's rule—denying work product protection to a represented defendant's AI-generated materials while granting it to a pro se litigant's identical materials—creates an irrational and unconstitutional disparity. But note the asymmetry works in both directions: Heppner denied protection to a represented defendant's unsupervised AI use, while Warner granted it to a pro se plaintiff's use. The constitutional claim might be that the pro se litigant is actually better off under current doctrine than the represented client who acts without counsel direction—which is a different problem than the credential-based disparity you've identified.

Due Process would be the hardest sell. Procedural due process requires notice and an opportunity to be heard, not equal access to discovery protections. Unless you can frame work product protection as a fundamental right necessary to meaningful access to courts (a stretch under current doctrine), due process claims are unlikely to succeed.

Sustainability of the Current Framework

The current framework is not sustainable in the long term, but not primarily for constitutional reasons. It will change because of the untenable practical and doctrinal consequences:

Doctrinal Incoherence: As the National Law Review observed, "the real tension is not in the outcomes—it is in the reasoning. The courts adopted incompatible frameworks for how AI tools relate to privilege and work product doctrine". Heppner treats AI as a third party whose involvement destroys privilege unless directed by counsel; Warner treats AI as a neutral tool whose use doesn't waive protection. Both can't be right as a matter of consistent doctrine. When courts apply irreconcilable frameworks to identical technology, the law becomes unpredictable and eventually must be harmonized—either through appellate review, rulemaking, or legislative intervention.

Functional Reality: The distinction between "consumer" and "enterprise" AI is already eroding. As foundation models become commoditized and the same weights power both, the credential-based distinction becomes harder to justify on anything other than formalistic grounds. The privilege analysis should turn on the reasonable expectation of confidentiality and the purpose of the communication, not on whether the user paid a subscription fee or holds a bar card.

Access-to-Justice Pressure: Courts and bar associations are increasingly concerned about the access-to-justice gap. A rule that systematically disadvantages unrepresented litigants by denying them the functional equivalent of work product protection (while represented parties can obtain it through counsel-directed use of the same underlying technology) will face mounting pressure from access-to-justice advocates, legal aid organizations, and eventually from courts themselves.

The likely trajectory is not a constitutional revolution but rather a doctrinal evolution: courts will increasingly adopt Warner's "AI as a tool" framework over Heppner's "AI as a third party" framework, at least for work product purposes. Attorney-client privilege will remain tied to the attorney-client relationship (as it always has been), but work product protection—which doesn't require an attorney, only "anticipation of litigation"—will likely expand to cover AI-assisted materials regardless of the user's professional status, so long as the use is confidential and the materials reflect the litigant's own mental impressions.

What you've identified—the constitutional implications of conditioning functionally identical AI output's protection on a professional credential—is a genuinely underexplored area. The existing literature has not yet caught up to the questions you're asking, but those questions are likely to become central as the Heppner-Warner divergence works its way through the courts.
