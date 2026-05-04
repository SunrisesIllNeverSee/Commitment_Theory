https://github.com/Imbad0202/academic-research-skills

1:27 AM
Claude responded: This is directly relevant to your Stanford Law Review submission and the broader CT publication roadmap.

Identified academic relevance and structured comprehensive breakdown
Identified academic relevance and structured comprehensive breakdown
This is directly relevant to your Stanford Law Review submission and the broader CT publication roadmap. Here's the breakdown:

What it is: A Claude Code skill suite by Cheng-I Wu — four coordinated SKILL.md files covering the full academic pipeline from research through publication. Multi-agent architecture, integrity verification built in, LaTeX output.

The four skills:

deep-research — 13 agents, includes Socratic guided mode, PRISMA systematic review, risk-of-bias, meta-analysis. Seven modes.
academic-paper — 12 agents, LaTeX/DOCX/PDF output (APA 7.0, IEEE, Chicago), visualization, revision coaching. Nine modes.
academic-paper-reviewer — 7 agents including Devil's Advocate, 0–100 quality rubrics, EIC + 3 reviewers. Maps scores to Accept/Minor/Major/Reject decisions.
academic-pipeline — 10-stage orchestrator with mandatory integrity verification at Stage 2.5 and 4.5, Socratic coaching between review and revision, collaboration quality scoring at the end.
The integrity verification is the standout feature. The showcase shows it caught 15 fabricated references and 3 statistical errors in a real run. That's the failure mode that destroys academic credibility — hallucinated citations. Having a dedicated pre-review integrity agent with an audit trail is architectural discipline, not a nice-to-have.

What's directly useful for you:

The SLRO submission is a law review essay, not an empirical paper, so the full 10-stage pipeline is overkill. But the academic-paper-reviewer skill in standalone mode is immediately deployable — running the Devil's Advocate + EIC + three reviewer simulation on the CT essay before submission would give you a structured read on where blind reviewers will push back, which is exactly what you need before the Hannah Dahleen submission window.

The deep-research systematic-review mode is relevant for the 31-paper publication roadmap — specifically for literature searches around CT's nine novel terms to confirm whitespace before filing.

Installation for your setup: Method 4 (upload to claude.ai project) is the path that requires no Claude Code. Drop the four SKILL.md files into a Project Knowledge base and run conversations there. The limitation noted is no parallel multi-agent execution, but for review and research tasks you're doing sequentially anyway, that's fine.

Worth cloning.

You said: What do you mean for my set up.
What do you mean for my set up... 

How would I set up in vs code for repo writing papers. Please note the repo is already built

1:30 AM
Claude responded: Since the repo is already cloned, you just need to wire it into Claude Code as a skill source.

Deciphered VS Code setup requirements for academic paper repository
Deciphered VS Code setup requirements for academic paper repository
Since the repo is already cloned, you just need to wire it into Claude Code as a skill source. Two steps:

1. Place the skills where Claude Code can find them

Copy or move the cloned repo into your project's skills directory:

bash
mkdir -p /path/to/your/project/.claude/skills
cp -r /path/to/academic-research-skills /path/to/your/project/.claude/skills/
Or if you want it available globally across all projects:

bash
mkdir -p ~/.claude/skills
cp -r /path/to/academic-research-skills ~/.claude/skills/
2. Merge the CLAUDE.md

The repo has a .claude/CLAUDE.md — open it and copy its contents into your project's existing .claude/CLAUDE.md (or create one if it doesn't exist). This is what tells Claude Code the skills exist and how to activate them.

Then in VS Code:

Open the project folder in VS Code, open the integrated terminal, and run claude to start a Claude Code session. The skills load automatically when Claude Code detects the .claude/skills/ directory.

From there you just talk naturally:

"Guide my research on X"          → triggers deep-research socratic mode
"Help me write a paper on X"      → triggers academic-paper plan mode  
"Review this paper" + paste text  → triggers academic-paper-reviewer
One thing to confirm first — do you have Claude Code installed? And is the repo currently sitting somewhere on your machine, or did you just look at it on GitHub?

You said: Its on my machine.
Its on my machine... code is installed desktop as well as vs code ext

1:34 AM
Claude responded: Then you're one terminal command away.

Assessed user's local setup and installation status
Assessed user's local setup and installation status
Then you're one terminal command away. Open VS Code, open your paper project folder, then in the integrated terminal:

bash
mkdir -p .claude/skills
cp -r /path/to/academic-research-skills .claude/skills/
Replace /path/to/academic-research-skills with wherever you cloned it. If you're not sure where it is:

bash
find ~ -name "academic-research-skills" -type d 2>/dev/null
Then merge the CLAUDE.md — open .claude/skills/academic-research-skills/.claude/CLAUDE.md and paste its contents into .claude/CLAUDE.md at your project root (create that file if it doesn't exist).

After that, just open the Claude Code panel in VS Code (or run claude in terminal) and say "guide my research on X" or "help me write a paper" and it activates.

What's the paper project folder called so we can confirm the path?

