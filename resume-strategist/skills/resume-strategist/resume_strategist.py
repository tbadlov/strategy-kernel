#!/usr/bin/env python3
"""
Resume Strategist — Executive CTO Resume Interview Workflow.

Seven-step interactive workflow for crafting CTO resumes targeting
Series C/D and IPO-track companies:
  1. Intake           - Read resume, understand target opportunity
  2. Company Context  - Extract company mission, vision, CTO's strategic role
  3. Impact Interview - Systematic extraction of business outcomes across all functions
  4. Leadership Probe - Team building, org design, cross-functional, board
  5. Gap Analysis     - Map extracted content against opportunity requirements
  6. Bullet Crafting  - Rewrite achievements using CAR framework
  7. Resume Artifact  - Generate final tailored resume
"""

import argparse
import sys
from pathlib import Path


# ============================================================================
# CONFIGURATION
# ============================================================================

SKILL_DIR = Path(__file__).resolve().parent
REFS_DIR = SKILL_DIR / "references"


# ============================================================================
# SHARED PROMPTS
# ============================================================================

LOAD_REFERENCE = (
    "LOAD REFERENCE: Read the file {path} now using the Read tool.\n"
    "This contains detailed framework knowledge needed for this step.\n"
    "Do NOT proceed until you have read it."
)

INTERVIEWER_MINDSET = (
    "YOUR ROLE AS EXECUTIVE RESUME STRATEGIST:\n"
    "\n"
    "Think like an executive coach who has placed dozens of CTOs at Series C/D\n"
    "and IPO-track companies. You are NOT:\n"
    "- A resume template filler\n"
    "- A cheerleader who accepts vague claims\n"
    "- A copy editor who polishes existing text\n"
    "\n"
    "You ARE:\n"
    "- A Socratic interviewer who extracts impact the user hasn't articulated\n"
    "- A business translator who reframes technical work as business outcomes\n"
    "- A strategist who understands what boards and investors look for\n"
    "- A challenger who pushes for specificity and quantification\n"
    "\n"
    "CRITICAL PRINCIPLES:\n"
    "- The existing resume is likely INSUFFICIENT. Your job is to extract what's\n"
    "  missing through structured interviewing, not just optimize what's there.\n"
    "- Every achievement must connect to BUSINESS OUTCOMES (revenue, cost, scale,\n"
    "  speed, risk). Technical excellence is only valuable when business-framed.\n"
    "- The CTO leads FOUR functions: product, engineering, data, infrastructure.\n"
    "  Most CTOs under-report 2-3 of these. Probe all four.\n"
    "- Company mission alignment comes FIRST. Without it, bullets lack context.\n"
    "\n"
    "INTERVIEW DISCIPLINE:\n"
    "- Ask 2-3 focused questions at a time using AskUserQuestion\n"
    "- Listen carefully to responses — follow up on specifics before moving on\n"
    "- Push for numbers. If the user says 'significant,' ask 'how significant?'\n"
    "- When the user can't quantify, use estimation proxies (see CAR framework)\n"
    "- Note the INTEGRITY CONSTRAINT: never help fabricate unverifiable numbers\n"
)


# ============================================================================
# MESSAGE TEMPLATES
# ============================================================================

# --- STEP 1: INTAKE ---------------------------------------------------------

INTAKE_INSTRUCTIONS = (
    "STEP 1: INTAKE & OPPORTUNITY ANALYSIS\n"
    "\n"
    + LOAD_REFERENCE.format(path=REFS_DIR / "stage-calibration.md") + "\n"
    "\n"
    + INTERVIEWER_MINDSET + "\n"
    "\n"
    "Your goal is to understand the starting material and the target opportunity.\n"
    "\n"
    "A. READ THE EXISTING RESUME:\n"
    "   If the user has provided a resume file (in the working directory or as a path),\n"
    "   read it now. Analyze it for:\n"
    "   - What's already strong (keep these)\n"
    "   - What's missing (gaps to fill through interviewing)\n"
    "   - What's poorly framed (technical-first vs. business-first)\n"
    "   - What functions are under-represented\n"
    "\n"
    "   If NO resume exists yet, note that — the interview will build from scratch.\n"
    "\n"
    "B. UNDERSTAND THE TARGET OPPORTUNITY:\n"
    "   Ask the user about the target role via AskUserQuestion:\n"
    "   - What company/role are you targeting? (If they have a JD, ask them to paste it)\n"
    "   - What stage is the company? (Series C, D, IPO-track, public)\n"
    "   - What do you know about what they're looking for?\n"
    "   - Why are you interested in this specific opportunity?\n"
    "\n"
    "   If the user provides a JD or URL, analyze it to decode:\n"
    "   - What the hiring committee ACTUALLY assesses (use stage-calibration.md)\n"
    "   - Unstated requirements (what's implied but not written)\n"
    "   - Red flags or deal-breakers to watch for\n"
    "\n"
    "C. INITIAL GAP ASSESSMENT:\n"
    "   Compare the existing resume (or blank slate) against the opportunity.\n"
    "   Identify the 3-5 biggest gaps that the interview must fill.\n"
    "\n"
    "OUTPUT FORMAT:\n"
    "```\n"
    "INTAKE SUMMARY\n"
    "==============\n"
    "Resume Status: [exists/partial/blank] — [brief assessment]\n"
    "Target Role: [company, title, stage]\n"
    "Target Stage: [Series C / D / IPO-track / Public]\n"
    "\n"
    "OPPORTUNITY DECODE:\n"
    "  What they're REALLY looking for: [decoded from JD + stage calibration]\n"
    "  Unstated requirements: [implied but not written]\n"
    "  Deal-breakers: [must-haves that can't be faked]\n"
    "\n"
    "CURRENT RESUME STRENGTHS:\n"
    "  1. [strength]\n"
    "  2. [strength]\n"
    "\n"
    "GAPS TO FILL (priority order):\n"
    "  1. [gap] — will probe in Step [N]\n"
    "  2. [gap] — will probe in Step [N]\n"
    "  3. [gap] — will probe in Step [N]\n"
    "```\n"
    "\n"
    "Then proceed to the next step."
)

# --- STEP 2: COMPANY CONTEXT ------------------------------------------------

COMPANY_CONTEXT_INSTRUCTIONS = (
    "STEP 2: COMPANY MISSION & STRATEGIC CONTEXT\n"
    "\n"
    + LOAD_REFERENCE.format(path=REFS_DIR / "cto-impact-dimensions.md") + "\n"
    "Focus on the 'Company Mission Alignment' section.\n"
    "\n"
    + LOAD_REFERENCE.format(path=REFS_DIR / "interview-playbook.md") + "\n"
    "Focus on 'Phase 1: Company Context & Mission Alignment' questions.\n"
    "\n"
    "This step establishes the STRATEGIC FRAME for the entire resume.\n"
    "Without company context, achievements float without meaning.\n"
    "\n"
    "INTERVIEW THE USER:\n"
    "\n"
    "Use the Phase 1 questions from the interview playbook. Start with the\n"
    "three opening questions, then follow up based on responses.\n"
    "\n"
    "EXTRACT:\n"
    "  - Company mission in the CTO's own words\n"
    "  - Company stage progression during CTO's tenure\n"
    "  - Top 2-3 company strategic priorities\n"
    "  - How the board/CEO defined success for technology\n"
    "  - Key inflection points (fundraising, pivots, M&A)\n"
    "  - Competitive landscape and where technology differentiated\n"
    "\n"
    "LISTEN FOR:\n"
    "  - How deeply the CTO internalized the mission (vs. reciting website copy)\n"
    "  - Clear connections between company priorities and technology decisions\n"
    "  - Moments where technology directly advanced the company's trajectory\n"
    "  - Revenue ranges, growth rates, team sizes that frame impact scale\n"
    "\n"
    "DO NOT MOVE ON until you understand the company's mission and how the CTO's\n"
    "work served it. This context shapes every bullet in the final resume.\n"
    "\n"
    "OUTPUT FORMAT:\n"
    "```\n"
    "COMPANY CONTEXT\n"
    "===============\n"
    "Company: [name] — [one-line description]\n"
    "Mission: [in the CTO's words]\n"
    "Stage progression: [stage when joined] → [current stage]\n"
    "Revenue trajectory: [approximate range when joined → now]\n"
    "Team trajectory: [size when joined → now]\n"
    "\n"
    "STRATEGIC PRIORITIES:\n"
    "  1. [priority] — CTO's technology response: [brief]\n"
    "  2. [priority] — CTO's technology response: [brief]\n"
    "  3. [priority] — CTO's technology response: [brief]\n"
    "\n"
    "KEY INFLECTION POINTS:\n"
    "  - [event] — CTO's role: [brief]\n"
    "\n"
    "COMPETITIVE DIFFERENTIATION:\n"
    "  Technology as differentiator: [where tech was a moat]\n"
    "  Technology as table stakes: [where tech just had to keep up]\n"
    "\n"
    "RESUME FRAMING INSIGHT:\n"
    "  [How this context should shape the resume's narrative arc]\n"
    "```\n"
    "\n"
    "Then proceed to the next step."
)

# --- STEP 3: IMPACT INTERVIEW -----------------------------------------------

IMPACT_INTERVIEW_INSTRUCTIONS = (
    "STEP 3: BUSINESS OUTCOMES DEEP DIVE\n"
    "\n"
    + LOAD_REFERENCE.format(path=REFS_DIR / "interview-playbook.md") + "\n"
    "Focus on 'Phase 2: Business Outcomes Deep Dive' questions.\n"
    "\n"
    + LOAD_REFERENCE.format(path=REFS_DIR / "cto-impact-dimensions.md") + "\n"
    "Focus on the four function sections.\n"
    "\n"
    "This is the CORE EXTRACTION step. You must systematically probe for\n"
    "business-outcome achievements across ALL FOUR FUNCTIONS.\n"
    "\n"
    "PROCESS:\n"
    "\n"
    "A. REVENUE & GROWTH IMPACT:\n"
    "   Use the Revenue & Growth questions from the playbook.\n"
    "   Probe until you have at least 2 quantified revenue-related achievements.\n"
    "\n"
    "B. COST & EFFICIENCY IMPACT:\n"
    "   Use the Cost & Efficiency questions.\n"
    "   Probe for cloud spend, automation, build-vs-buy, headcount efficiency.\n"
    "\n"
    "C. SPEED & TIME-TO-MARKET:\n"
    "   Use the Speed questions.\n"
    "   Get before/after deployment cadence and business impact of speed.\n"
    "\n"
    "D. RISK & RELIABILITY:\n"
    "   Use the Risk questions.\n"
    "   Get uptime, compliance, security improvements and their business unlock.\n"
    "\n"
    "COVERAGE CHECK: After each round, verify you have extracted impact from\n"
    "EACH of the four functions (product, engineering, data, infrastructure).\n"
    "If a function is under-represented, probe specifically:\n"
    "  'We've covered strong engineering and infrastructure examples. What about\n"
    "   your product leadership? And data/analytics decisions?'\n"
    "\n"
    "QUANTIFICATION DISCIPLINE:\n"
    "For EVERY achievement, push for a number. Use the probing techniques\n"
    "from the playbook (Specificity Probe, Business Impact Probe, Scale Probe,\n"
    "Estimation Helper). Respect the Integrity Constraint — note when a number\n"
    "is an estimate vs. a verified fact.\n"
    "\n"
    "OUTPUT FORMAT:\n"
    "```\n"
    "EXTRACTED ACHIEVEMENTS\n"
    "======================\n"
    "\n"
    "PRODUCT:\n"
    "  1. [achievement] — Metric: [number] — Confidence: [verified/estimated]\n"
    "  2. [achievement] — Metric: [number] — Confidence: [verified/estimated]\n"
    "\n"
    "ENGINEERING:\n"
    "  1. [achievement] — Metric: [number] — Confidence: [verified/estimated]\n"
    "  2. [achievement] — Metric: [number] — Confidence: [verified/estimated]\n"
    "\n"
    "DATA:\n"
    "  1. [achievement] — Metric: [number] — Confidence: [verified/estimated]\n"
    "  2. [achievement] — Metric: [number] — Confidence: [verified/estimated]\n"
    "\n"
    "INFRASTRUCTURE:\n"
    "  1. [achievement] — Metric: [number] — Confidence: [verified/estimated]\n"
    "  2. [achievement] — Metric: [number] — Confidence: [verified/estimated]\n"
    "\n"
    "COVERAGE GAPS:\n"
    "  [Any functions still under-represented after probing]\n"
    "```\n"
    "\n"
    "Then proceed to the next step."
)

# --- STEP 4: LEADERSHIP PROBE -----------------------------------------------

LEADERSHIP_PROBE_INSTRUCTIONS = (
    "STEP 4: LEADERSHIP & ORGANIZATION BUILDING\n"
    "\n"
    + LOAD_REFERENCE.format(path=REFS_DIR / "interview-playbook.md") + "\n"
    "Focus on 'Phase 3: Leadership & Organization Building' questions.\n"
    "\n"
    + LOAD_REFERENCE.format(path=REFS_DIR / "cto-impact-dimensions.md") + "\n"
    "Focus on 'Cross-Cutting Executive Dimensions' section.\n"
    "\n"
    "This step extracts the achievements that differentiate a CTO from a VP Engineering.\n"
    "Boards hire CTOs for executive-level impact, not just engineering management.\n"
    "\n"
    "INTERVIEW THE USER on:\n"
    "\n"
    "A. TEAM SCALING & ORG DESIGN:\n"
    "   How did the organization grow? What was the structure?\n"
    "   Key senior hires. Hiring strategy. Retention.\n"
    "\n"
    "B. PROCESS & CULTURE:\n"
    "   What processes did they establish? What culture did they build?\n"
    "   How did they handle the velocity-vs-quality tension?\n"
    "\n"
    "C. CROSS-FUNCTIONAL & BOARD:\n"
    "   How did they work with CEO, CFO, board?\n"
    "   Did they present to the board? How often? On what topics?\n"
    "   How did they align the four functions when priorities conflicted?\n"
    "\n"
    "D. M&A & STRATEGIC (if applicable):\n"
    "   Any M&A evaluation or integration?\n"
    "   DD preparation from technology side?\n"
    "   IPO readiness work?\n"
    "\n"
    "WATCH FOR RED FLAGS (from the playbook):\n"
    "- All individual contributions, no team/org achievements\n"
    "- No board or cross-functional examples\n"
    "- Understating impact (common in technical leaders)\n"
    "\n"
    "OUTPUT FORMAT:\n"
    "```\n"
    "LEADERSHIP ACHIEVEMENTS\n"
    "=======================\n"
    "\n"
    "ORG BUILDING:\n"
    "  1. [achievement] — Metric: [number]\n"
    "\n"
    "PROCESS & CULTURE:\n"
    "  1. [achievement] — Metric: [number]\n"
    "\n"
    "BOARD & CROSS-FUNCTIONAL:\n"
    "  1. [achievement] — Metric: [number]\n"
    "\n"
    "M&A / STRATEGIC:\n"
    "  1. [achievement] — Metric: [number]\n"
    "\n"
    "EXECUTIVE DIFFERENTIATORS:\n"
    "  [What makes this person a CTO, not a VP Eng]\n"
    "```\n"
    "\n"
    "Then proceed to the next step."
)

# --- STEP 5: GAP ANALYSIS ---------------------------------------------------

GAP_ANALYSIS_INSTRUCTIONS = (
    "STEP 5: GAP ANALYSIS & OPPORTUNITY MAPPING\n"
    "\n"
    + LOAD_REFERENCE.format(path=REFS_DIR / "stage-calibration.md") + "\n"
    "\n"
    "Now map everything you've extracted against what the target opportunity requires.\n"
    "\n"
    "PROCESS:\n"
    "\n"
    "A. STAGE PRIORITY MAPPING:\n"
    "   Using the priority table for the TARGET STAGE (from stage-calibration.md),\n"
    "   check which priorities are covered by extracted achievements and which aren't.\n"
    "\n"
    "B. JD REQUIREMENT MAPPING:\n"
    "   If a JD was provided, map each stated requirement to extracted content.\n"
    "   Flag requirements that have no matching achievement.\n"
    "\n"
    "C. OPPORTUNITY SCORING:\n"
    "   For each gap, assess:\n"
    "   - Is there an achievement we extracted but haven't framed correctly? (reframe)\n"
    "   - Is there a gap we can fill with one more targeted question? (ask now)\n"
    "   - Is there a genuine gap in experience? (acknowledge, mitigate)\n"
    "\n"
    "D. NARRATIVE ARC:\n"
    "   Based on the company context and extracted achievements, define the\n"
    "   resume's overall narrative:\n"
    "   - What STORY does this resume tell?\n"
    "   - What is the through-line from company mission to CTO impact?\n"
    "   - What positioning statement anchors the executive summary?\n"
    "\n"
    "ASK any remaining targeted questions to fill critical gaps.\n"
    "\n"
    "OUTPUT FORMAT:\n"
    "```\n"
    "GAP ANALYSIS\n"
    "============\n"
    "\n"
    "TARGET STAGE: [stage] — PRIORITY ALIGNMENT:\n"
    "\n"
    "| Stage Priority | Covered? | Best Achievement | Gap/Action |\n"
    "|---------------|----------|------------------|------------|\n"
    "| [priority 1]  | [Y/N]   | [achievement]    | [reframe/ask/mitigate] |\n"
    "| [priority 2]  | [Y/N]   | [achievement]    | [reframe/ask/mitigate] |\n"
    "| ...           |          |                  |            |\n"
    "\n"
    "JD REQUIREMENT MAPPING:\n"
    "  [requirement] → [matched achievement or GAP]\n"
    "\n"
    "NARRATIVE ARC:\n"
    "  Story: [one-sentence resume narrative]\n"
    "  Through-line: [company mission → CTO impact]\n"
    "  Positioning: [executive summary anchor]\n"
    "\n"
    "REMAINING GAPS:\n"
    "  [gaps that cannot be filled — mitigation strategy for each]\n"
    "```\n"
    "\n"
    "Then proceed to the next step."
)

# --- STEP 6: BULLET CRAFTING ------------------------------------------------

BULLET_CRAFTING_INSTRUCTIONS = (
    "STEP 6: ACHIEVEMENT BULLET CRAFTING\n"
    "\n"
    + LOAD_REFERENCE.format(path=REFS_DIR / "car-framework.md") + "\n"
    "\n"
    "Now transform extracted achievements into resume-ready bullets using the\n"
    "CAR (Challenge → Action → Result) framework.\n"
    "\n"
    "PROCESS:\n"
    "\n"
    "A. SELECT TOP ACHIEVEMENTS:\n"
    "   From Steps 3 and 4, select the 8-12 strongest achievements.\n"
    "   Priority: achievements that map to target stage priorities first.\n"
    "\n"
    "B. APPLY CAR FRAMEWORK:\n"
    "   For each achievement, write a bullet using:\n"
    "   [Action verb] + [what you did] + [to address Challenge] + [delivering Result]\n"
    "\n"
    "   Apply all tests from the CAR framework reference:\n"
    "   - Challenge is BUSINESS-framed, not technical\n"
    "   - Action shows LEADERSHIP, not just execution\n"
    "   - Result includes a BUSINESS METRIC with a NUMBER\n"
    "   - Result is DEFENSIBLE (respect integrity constraint)\n"
    "\n"
    "C. STAGE CALIBRATION:\n"
    "   Using stage-calibration.md, ensure bullet language matches\n"
    "   the TARGET stage (not the user's current/previous stage).\n"
    "   Use the stage translation guide for framing.\n"
    "\n"
    "D. REVIEW WITH USER:\n"
    "   Present the drafted bullets to the user. For each bullet, ask:\n"
    "   - 'Is this accurate? Can you defend this number in an interview?'\n"
    "   - 'Does this capture the full magnitude of what you achieved?'\n"
    "   - 'Is there anything important I'm missing or overstating?'\n"
    "\n"
    "   Iterate based on feedback. Do NOT finalize bullets the user cannot\n"
    "   confidently defend.\n"
    "\n"
    "E. EXECUTIVE SUMMARY:\n"
    "   Draft a 3-4 line positioning statement that:\n"
    "   - Establishes executive identity (CTO + functions led)\n"
    "   - States the scale they've operated at (team size, revenue, users)\n"
    "   - Connects to what the target company needs\n"
    "   - Uses the narrative arc from Step 5\n"
    "\n"
    "OUTPUT FORMAT:\n"
    "```\n"
    "EXECUTIVE SUMMARY (draft):\n"
    "  [3-4 line positioning statement]\n"
    "\n"
    "KEY ACHIEVEMENTS (top 6-8 for highlights section):\n"
    "  1. [CAR bullet] — maps to: [stage priority]\n"
    "  2. [CAR bullet] — maps to: [stage priority]\n"
    "  ...\n"
    "\n"
    "EXPERIENCE BULLETS (by role, 4-6 per role):\n"
    "  [Role @ Company (dates)]:\n"
    "  1. [CAR bullet]\n"
    "  2. [CAR bullet]\n"
    "  ...\n"
    "```\n"
    "\n"
    "Iterate with the user until they're confident in every bullet.\n"
    "Then proceed to the next step."
)

# --- STEP 7: RESUME ARTIFACT ------------------------------------------------

ARTIFACT_INSTRUCTIONS = (
    "STEP 7: RESUME ARTIFACT\n"
    "\n"
    "Generate the final tailored resume as a markdown file.\n"
    "\n"
    "DOCUMENT STRUCTURE:\n"
    "\n"
    "Write the resume in this format and save it in the current working directory\n"
    "as a markdown file (e.g., `resume-[target-company].md`):\n"
    "\n"
    "```markdown\n"
    "# [Full Name]\n"
    "\n"
    "[Contact info line: email | phone | LinkedIn | location]\n"
    "\n"
    "## Executive Summary\n"
    "[3-4 line positioning statement from Step 6]\n"
    "\n"
    "## Key Achievements\n"
    "[6-8 top CAR bullets — the strongest, most relevant achievements]\n"
    "\n"
    "## Professional Experience\n"
    "\n"
    "### [Title] — [Company Name]\n"
    "*[Start Date] – [End Date]*\n"
    "\n"
    "[Brief company context: what the company does, stage, scale]\n"
    "\n"
    "- [CAR bullet 1]\n"
    "- [CAR bullet 2]\n"
    "- [CAR bullet 3]\n"
    "- [CAR bullet 4]\n"
    "\n"
    "[Repeat for each relevant role]\n"
    "\n"
    "## Technical Expertise\n"
    "[Organized by domain: Cloud/Infrastructure, Languages/Frameworks,\n"
    " Data/ML, DevOps/SRE, Security/Compliance — keep concise]\n"
    "\n"
    "## Education\n"
    "[Degrees — keep minimal at executive level]\n"
    "\n"
    "## Board & Advisory\n"
    "[If applicable: board seats, advisory roles, speaking]\n"
    "```\n"
    "\n"
    "WRITING GUIDELINES:\n"
    "- Maximum 2 pages when rendered (strict — executives with 3-page resumes\n"
    "  signal poor prioritization)\n"
    "- Every bullet must pass the CAR tests from the reference\n"
    "- Language calibrated to TARGET STAGE (not the user's current stage)\n"
    "- Technical Expertise section is a keyword scan target — include relevant\n"
    "  technologies but don't let it dominate\n"
    "- No pronouns (standard resume convention: omit 'I', 'my')\n"
    "- Company context line helps the reader calibrate scale even if the\n"
    "  company name isn't well-known\n"
    "\n"
    "FINAL REVIEW WITH USER:\n"
    "After generating the resume, ask:\n"
    "1. 'Can you confidently defend every bullet in this resume during an interview?'\n"
    "2. 'Does the executive summary capture how you want to be positioned?'\n"
    "3. 'Is anything important missing or overstated?'\n"
    "4. 'Does this feel like YOU at your best, not a generic CTO?'\n"
    "\n"
    "Iterate until the user is fully confident in the document."
)


# ============================================================================
# STEP DEFINITIONS
# ============================================================================

STEP_TITLES = {
    1: "Intake & Opportunity Analysis",
    2: "Company Mission & Strategic Context",
    3: "Business Outcomes Deep Dive",
    4: "Leadership & Organization Building",
    5: "Gap Analysis & Opportunity Mapping",
    6: "Achievement Bullet Crafting",
    7: "Resume Artifact",
}

STEP_INSTRUCTIONS = {
    1: INTAKE_INSTRUCTIONS,
    2: COMPANY_CONTEXT_INSTRUCTIONS,
    3: IMPACT_INTERVIEW_INSTRUCTIONS,
    4: LEADERSHIP_PROBE_INSTRUCTIONS,
    5: GAP_ANALYSIS_INSTRUCTIONS,
    6: BULLET_CRAFTING_INSTRUCTIONS,
    7: ARTIFACT_INSTRUCTIONS,
}

TOTAL_STEPS = len(STEP_TITLES)


# ============================================================================
# OUTPUT FORMATTING
# ============================================================================

def format_step(body: str, next_cmd: str = "", title: str = "") -> str:
    """Assemble complete workflow step: title + body + next directive."""
    if title:
        header = f"{title}\n{'=' * len(title)}\n\n"
        body = header + body

    if next_cmd:
        invoke = (
            f"\n\nNEXT STEP:\n"
            f"    Working directory: {SKILL_DIR}\n"
            f"    Command: {next_cmd}\n\n"
            f"Execute this command now."
        )
        return f"{body}{invoke}"
    else:
        return (
            f"{body}\n\n"
            f"WORKFLOW COMPLETE.\n"
            f"The resume has been generated. "
            f"Review it with the user and iterate as needed."
        )


def format_output(step: int) -> str:
    """Build the output for a given step."""
    if step not in STEP_TITLES:
        return f"ERROR: Invalid step {step}. Valid steps: 1-{TOTAL_STEPS}"

    title = STEP_TITLES[step]
    instructions = STEP_INSTRUCTIONS[step]

    if step < TOTAL_STEPS:
        next_cmd = f"python3 resume_strategist.py --step {step + 1}"
    else:
        next_cmd = ""

    return format_step(
        instructions,
        next_cmd,
        title=f"RESUME STRATEGIST - Step {step}/{TOTAL_STEPS}: {title}",
    )


# ============================================================================
# ENTRY POINT
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Resume Strategist - Executive CTO Resume Interview Workflow"
    )
    parser.add_argument(
        "--step", type=int, required=True,
        help=f"Workflow step (1-{TOTAL_STEPS})"
    )
    args = parser.parse_args()
    print(format_output(args.step))


if __name__ == "__main__":
    main()
