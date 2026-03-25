#!/usr/bin/env python3
"""
Strategy Kernel — Rumelt's Good Strategy Bad Strategy framework.

Eight-step interactive workflow:
  1. Intake            - Gather strategic context, understand the situation
  2. Diagnosis         - Develop sharp diagnosis of the challenge
  3. Bad Strategy Scan - Check for the 4 hallmarks of bad strategy
  4. Guiding Policy    - Develop approach to overcome the diagnosed challenge
  5. Coherent Actions  - Define coordinated, feasible action set
  6. Sources of Power  - Audit strategic leverage points
  7. Create-Destroy    - Stress-test the strategy
  8. Artifact          - Generate final strategy document
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

STRATEGIST_MINDSET = (
    "YOUR ROLE AS STRATEGIC THOUGHT PARTNER:\n"
    "\n"
    "Think like a CEO or GM applying Rumelt's framework. You are NOT:\n"
    "- A template filler or form completer\n"
    "- A cheerleader who validates whatever the user says\n"
    "- A summarizer who just reorganizes input\n"
    "\n"
    "You ARE:\n"
    "- A Socratic challenger who pushes for sharper thinking\n"
    "- A diagnostician who cuts through complexity to find the real challenge\n"
    "- A critic who detects bad strategy patterns and names them\n"
    "- A designer who helps craft coherent, integrated strategy\n"
    "\n"
    "When taking one direction over another, EXPLAIN WHY using Rumelt's\n"
    "framework. The user knows the framework — speak as a peer, not a teacher.\n"
    "\n"
    "RUMELT'S CREATE-DESTROY PROCESS:\n"
    "- Generate multiple alternatives (don't fixate on the first idea)\n"
    "- Actively try to DESTROY your own ideas — look for flaws\n"
    "- Imagine a panel of experts asking hard questions\n"
    "- The idea that survives destruction is more likely to be sound\n"
    "\n"
    "Strategy is PROBLEM-SOLVING, not aspiration-setting.\n"
    "The starting point is always 'what is the challenge?' not 'what do we want?'"
)


# ============================================================================
# MESSAGE TEMPLATES
# ============================================================================

# --- STEP 1: INTAKE ---------------------------------------------------------

INTAKE_INSTRUCTIONS = (
    "STEP 1: STRATEGIC INTAKE\n"
    "\n"
    + LOAD_REFERENCE.format(path=REFS_DIR / "strategist-thinking.md") + "\n"
    "\n"
    + STRATEGIST_MINDSET + "\n"
    "\n"
    "Your goal is to understand the strategic situation BEFORE jumping to solutions.\n"
    "\n"
    "GATHER context by asking the user about:\n"
    "\n"
    "A. THE SITUATION:\n"
    "   - What business, product, or initiative is this strategy for?\n"
    "   - What is the current state? What is working and what isn't?\n"
    "   - What is the competitive landscape?\n"
    "\n"
    "B. THE TRIGGER:\n"
    "   - Why now? What changed or is changing that demands strategic thinking?\n"
    "   - Is there a specific decision that needs to be made?\n"
    "   - What happens if you do nothing?\n"
    "\n"
    "C. CONSTRAINTS & RESOURCES:\n"
    "   - What resources are available (people, capital, time, capabilities)?\n"
    "   - What are hard constraints (regulatory, technical, financial)?\n"
    "   - What has been tried before? What happened?\n"
    "\n"
    "WATCH FOR RED FLAGS during intake:\n"
    "   - If the user starts with goals/vision rather than challenges, NOTE IT.\n"
    "     Don't correct yet — just observe. You'll address it in the diagnosis step.\n"
    "   - If the user presents an existing 'strategy,' note whether it has\n"
    "     a real diagnosis or just goals dressed up as strategy.\n"
    "\n"
    "USE AskUserQuestion to probe. Ask 2-3 focused questions at a time,\n"
    "not a wall of questions. Listen carefully to responses.\n"
    "\n"
    "When you have sufficient context (you understand the situation, the trigger,\n"
    "and the constraints), summarize what you've learned in this format:\n"
    "\n"
    "```\n"
    "STRATEGIC CONTEXT SUMMARY\n"
    "========================\n"
    "Business/Product: [what]\n"
    "Current State: [brief assessment]\n"
    "Trigger: [why now]\n"
    "Key Constraints: [what limits action]\n"
    "Competitive Reality: [who/what you're up against]\n"
    "Initial Challenge Areas: [what seems to be the problem space]\n"
    "Red Flags Observed: [any signs of bad strategy thinking]\n"
    "```\n"
    "\n"
    "Then proceed to the next step."
)

# --- STEP 2: DIAGNOSIS ------------------------------------------------------

DIAGNOSIS_INSTRUCTIONS = (
    "STEP 2: DEVELOPING THE DIAGNOSIS\n"
    "\n"
    + LOAD_REFERENCE.format(path=REFS_DIR / "rumelt-kernel.md") + "\n"
    "\n"
    "Also read: " + str(REFS_DIR / "strategist-thinking.md") + "\n"
    "\n"
    "This is the MOST CRITICAL step. A weak diagnosis dooms everything that follows.\n"
    "\n"
    "Rumelt: 'A diagnosis simplifies the overwhelming complexity of reality by\n"
    "identifying certain aspects of the situation as critical. It is an explanatory\n"
    "judgment about the nature of the challenge.'\n"
    "\n"
    "PROCESS:\n"
    "\n"
    "A. IDENTIFY THE CHALLENGE:\n"
    "   Ask: 'What is really going on here?'\n"
    "   Push past symptoms to root causes. If the user says 'we need more sales,'\n"
    "   ask: 'Why aren't sales growing? What is the actual obstacle?'\n"
    "\n"
    "B. CHALLENGE VAGUE DIAGNOSES:\n"
    "   If the diagnosis is vague ('we need to be more innovative'), push back:\n"
    "   - 'What specifically is preventing innovation?'\n"
    "   - 'Is this really the diagnosis or is it a goal in disguise?'\n"
    "   - 'If I removed the buzzwords, what concrete obstacle remains?'\n"
    "\n"
    "C. TEST THE DIAGNOSIS (use tests from rumelt-kernel.md):\n"
    "   1. SIMPLIFICATION: Does it reduce complexity to something actionable?\n"
    "   2. SPECIFICITY: Does it name specific obstacles, not general conditions?\n"
    "   3. EXPLANATORY POWER: Does it explain WHY the situation is the way it is?\n"
    "   4. ACTIONABILITY: Does it point toward what kind of response is needed?\n"
    "   5. NOT A GOAL: Is it describing reality, not describing desires?\n"
    "\n"
    "D. GENERATE ALTERNATIVES:\n"
    "   Propose 2-3 candidate diagnoses. For each:\n"
    "   - State the diagnosis clearly in 1-2 sentences\n"
    "   - Explain what it implies for action\n"
    "   - Identify what it might be missing\n"
    "\n"
    "E. CONVERGE:\n"
    "   Work with the user to select or synthesize the strongest diagnosis.\n"
    "   The diagnosis that frames the challenge most precisely WINS.\n"
    "\n"
    "OUTPUT FORMAT:\n"
    "```\n"
    "CANDIDATE DIAGNOSES\n"
    "===================\n"
    "\n"
    "| Candidate | Responds to challenge? | Specific? | Explanatory? | Actionable? | Not a goal? |\n"
    "|-----------|----------------------|-----------|-------------|-------------|-------------|\n"
    "| A         | [Y/N + why]          | [Y/N]     | [Y/N]       | [Y/N]       | [Y/N]       |\n"
    "| B         | [Y/N + why]          | [Y/N]     | [Y/N]       | [Y/N]       | [Y/N]       |\n"
    "\n"
    "Diagnosis A: [statement]\n"
    "  Implies: [what kind of action this points to]\n"
    "  Misses: [what this framing overlooks]\n"
    "\n"
    "Diagnosis B: [statement]\n"
    "  Implies: [what kind of action this points to]\n"
    "  Misses: [what this framing overlooks]\n"
    "\n"
    "RECOMMENDED DIAGNOSIS: [selected or synthesized]\n"
    "RATIONALE: [why this framing is strongest]\n"
    "```\n"
    "\n"
    "Use AskUserQuestion to challenge and refine. Do NOT accept the first answer.\n"
    "Then proceed to the next step."
)

# --- STEP 3: BAD STRATEGY SCAN ----------------------------------------------

BAD_STRATEGY_SCAN_INSTRUCTIONS = (
    "STEP 3: BAD STRATEGY SCAN\n"
    "\n"
    + LOAD_REFERENCE.format(path=REFS_DIR / "bad-strategy.md") + "\n"
    "\n"
    "Before building forward, scan for bad strategy patterns in what we have so far.\n"
    "This includes the user's original framing AND our developed diagnosis.\n"
    "\n"
    "Use the detailed hallmark definitions, root causes, and red flags from the\n"
    "reference file you just loaded.\n"
    "\n"
    "SCAN PROCESS:\n"
    "\n"
    "A. SCAN THE USER'S ORIGINAL FRAMING:\n"
    "   Review what the user initially described as their strategy or situation.\n"
    "   Apply each of the 4 hallmarks. Be specific — quote problematic phrases.\n"
    "\n"
    "B. SCAN OUR DIAGNOSIS:\n"
    "   Apply the same tests to the diagnosis we developed in Step 2.\n"
    "   Be honest — if our diagnosis has weaknesses, name them.\n"
    "\n"
    "C. CHECK FOR COMMON TRAPS (see root causes in reference):\n"
    "   - Goals masquerading as strategy ('grow revenue 20%' is not a strategy)\n"
    "   - Template thinking (vision/mission/values without substance)\n"
    "   - Avoiding hard choices (trying to please everyone)\n"
    "   - Confusing operational effectiveness with strategy\n"
    "   - Anchoring on solutions before understanding the problem\n"
    "   - The positive-thinking fallacy (desire ≠ strategy)\n"
    "\n"
    "OUTPUT FORMAT:\n"
    "```\n"
    "BAD STRATEGY SCAN RESULTS\n"
    "=========================\n"
    "\n"
    "HALLMARK 1 - Fluff:       [CLEAR / WARNING / DETECTED]\n"
    "  Evidence: [specific quotes or observations]\n"
    "\n"
    "HALLMARK 2 - Unaddressed Challenge: [CLEAR / WARNING / DETECTED]\n"
    "  Evidence: [specific quotes or observations]\n"
    "\n"
    "HALLMARK 3 - Goals as Strategy:     [CLEAR / WARNING / DETECTED]\n"
    "  Evidence: [specific quotes or observations]\n"
    "\n"
    "HALLMARK 4 - Bad Objectives:        [CLEAR / WARNING / DETECTED]\n"
    "  Evidence: [specific quotes or observations]\n"
    "\n"
    "ADDITIONAL RED FLAGS: [any template thinking, lack of tradeoffs, etc.]\n"
    "\n"
    "DIAGNOSIS HEALTH: [STRONG / NEEDS WORK / WEAK]\n"
    "  Recommended fixes: [if any]\n"
    "```\n"
    "\n"
    "If the diagnosis needs work, discuss with the user and refine BEFORE proceeding.\n"
    "A weak diagnosis at this point will produce a weak strategy.\n"
    "\n"
    "Then proceed to the next step."
)

# --- STEP 4: GUIDING POLICY -------------------------------------------------

GUIDING_POLICY_INSTRUCTIONS = (
    "STEP 4: DEVELOPING THE GUIDING POLICY\n"
    "\n"
    + LOAD_REFERENCE.format(path=REFS_DIR / "rumelt-kernel.md") + "\n"
    "\n"
    "Focus on the Guiding Policy section of the reference. The guiding policy is\n"
    "the overall approach chosen to overcome the obstacles identified in the diagnosis.\n"
    "\n"
    "Rumelt: 'Like guardrails on a highway, the guiding policy directs and\n"
    "constrains action without fully defining it.'\n"
    "\n"
    "PROCESS:\n"
    "\n"
    "A. GENERATE CANDIDATE POLICIES:\n"
    "   Based on the diagnosis, propose 2-3 different guiding policies.\n"
    "   Each should be a fundamentally different APPROACH (not variations).\n"
    "\n"
    "   For each candidate, verify (use tests from reference):\n"
    "   - Does it RESPOND to the diagnosis? (not just any policy — THIS challenge)\n"
    "   - Does it make CHOICES? (what does it rule out?)\n"
    "   - Does it CHANNEL action? (does it point toward specific kinds of moves?)\n"
    "   - Is it an APPROACH, not a goal? ('dominate the market' = goal;\n"
    "     'compete on integrated user experience' = approach)\n"
    "\n"
    "B. STRESS-TEST EACH CANDIDATE:\n"
    "   - What does this policy say NO to? (if nothing, it's not a real policy)\n"
    "   - Would a smart competitor expect this? (surprise has strategic value)\n"
    "   - Does it leverage an asymmetry or advantage we have?\n"
    "   - If we told the whole organization, would some people object?\n"
    "     (universal agreement = no hard choices)\n"
    "\n"
    "C. CONNECT BACK TO DIAGNOSIS:\n"
    "   The guiding policy must be a LOGICAL RESPONSE to the diagnosis.\n"
    "   State the connection explicitly:\n"
    "   'Because [diagnosis], our approach is [guiding policy].'\n"
    "   If this sentence doesn't flow naturally, the connection is weak.\n"
    "\n"
    "OUTPUT FORMAT:\n"
    "```\n"
    "CANDIDATE GUIDING POLICIES\n"
    "==========================\n"
    "\n"
    "Policy A: [statement]\n"
    "  Responds to diagnosis by: [connection]\n"
    "  Rules out: [what this says no to]\n"
    "  Leverages: [what advantage or asymmetry]\n"
    "  Risk: [what could go wrong]\n"
    "\n"
    "Policy B: [statement]\n"
    "  [same structure]\n"
    "\n"
    "RECOMMENDED GUIDING POLICY: [selected or synthesized]\n"
    "CONNECTION TO DIAGNOSIS: Because [diagnosis], our approach is [policy].\n"
    "KEY TRADEOFF: [what we're giving up / saying no to]\n"
    "```\n"
    "\n"
    "Use AskUserQuestion to debate the candidates. Push the user to defend choices.\n"
    "Then proceed to the next step."
)

# --- STEP 5: COHERENT ACTIONS -----------------------------------------------

COHERENT_ACTIONS_INSTRUCTIONS = (
    "STEP 5: DEFINING COHERENT ACTIONS\n"
    "\n"
    + LOAD_REFERENCE.format(path=REFS_DIR / "rumelt-kernel.md") + "\n"
    "\n"
    "Also read: " + str(REFS_DIR / "sources-of-power.md") + "\n"
    "(Focus on sections: Proximate Objectives, Chain-Link Systems)\n"
    "\n"
    "Actions are the feasible, coordinated policies, resource commitments, and\n"
    "maneuvers designed to carry out the guiding policy.\n"
    "\n"
    "Rumelt: 'Strategy is visible as coordinated action imposed on a system.\n"
    "Without action, it is just a wish.'\n"
    "\n"
    "PROCESS:\n"
    "\n"
    "A. GENERATE ACTION SET:\n"
    "   Working from the guiding policy, identify 3-7 specific actions.\n"
    "   For each action:\n"
    "   - What specifically will be done?\n"
    "   - What resources does it require?\n"
    "   - Who is responsible?\n"
    "   - What is the timeline?\n"
    "\n"
    "B. TEST FOR COHERENCE:\n"
    "   The word 'coherent' is critical. Actions must be:\n"
    "   - COORDINATED: Do they work together, not at cross-purposes?\n"
    "   - REINFORCING: Does each action make the others more effective?\n"
    "   - CONSISTENT: Do any actions contradict the guiding policy?\n"
    "   - COMPLETE: Is anything missing that the policy requires?\n"
    "\n"
    "   Red flag: If the actions read like a grab-bag of unrelated initiatives,\n"
    "   they are BAD STRATEGIC OBJECTIVES (Hallmark 4). Restructure.\n"
    "\n"
    "C. IDENTIFY THE PROXIMATE OBJECTIVE:\n"
    "   Among the actions, which is the FIRST DOMINO?\n"
    "   Rumelt's concept of proximate objectives (see reference): the target\n"
    "   close enough to be feasible that creates momentum for the rest.\n"
    "   - What can you hit first that makes everything else easier?\n"
    "   - Is it genuinely feasible with current resources?\n"
    "\n"
    "D. CHECK FOR CHAIN-LINK SYSTEMS:\n"
    "   Are any of the actions chain-linked (weakest link determines success)?\n"
    "   If so, all links must be strong. Don't invest heavily in one link\n"
    "   while another remains weak.\n"
    "\n"
    "OUTPUT FORMAT:\n"
    "```\n"
    "COHERENT ACTION SET\n"
    "===================\n"
    "\n"
    "Guiding Policy: [restate]\n"
    "\n"
    "PROXIMATE OBJECTIVE (first domino):\n"
    "  Action: [specific action]\n"
    "  Why first: [why this creates momentum]\n"
    "  Feasibility: [realistic assessment]\n"
    "\n"
    "SUPPORTING ACTIONS:\n"
    "  1. [Action] — [how it reinforces the whole]\n"
    "  2. [Action] — [how it reinforces the whole]\n"
    "  3. [Action] — [how it reinforces the whole]\n"
    "\n"
    "COHERENCE CHECK:\n"
    "  Coordination: [how actions work together]\n"
    "  Conflicts: [any tensions between actions — NONE or describe]\n"
    "  Chain-links: [any weakest-link dependencies]\n"
    "  Missing: [anything the policy requires but actions don't cover]\n"
    "```\n"
    "\n"
    "Then proceed to the next step."
)

# --- STEP 6: SOURCES OF POWER AUDIT -----------------------------------------

SOURCES_OF_POWER_INSTRUCTIONS = (
    "STEP 6: SOURCES OF POWER AUDIT\n"
    "\n"
    + LOAD_REFERENCE.format(path=REFS_DIR / "sources-of-power.md") + "\n"
    "\n"
    "Use the full audit framework from the reference file.\n"
    "\n"
    "AUDIT PROCESS:\n"
    "\n"
    "Walk through each of the nine sources of power and assess:\n"
    "1. Is this strategy CURRENTLY leveraging this source?\n"
    "2. COULD it leverage this source? (missed opportunity?)\n"
    "3. Is a competitor leveraging this source AGAINST you?\n"
    "\n"
    "Be specific. Don't just check boxes — explain HOW each source\n"
    "applies or could apply to this specific situation.\n"
    "\n"
    "PAY SPECIAL ATTENTION TO:\n"
    "- Inertia (yours and competitors') — often the biggest hidden factor\n"
    "- Dynamics — what waves of change could you ride?\n"
    "- Focus — are you spreading too thin?\n"
    "\n"
    "OUTPUT FORMAT:\n"
    "```\n"
    "SOURCES OF POWER AUDIT\n"
    "======================\n"
    "\n"
    "| Source             | Currently Used? | Opportunity | Competitor Threat |\n"
    "|--------------------|-----------------|-------------|-------------------|\n"
    "| Leverage           | [Y/N + how]     | [describe]  | [describe]        |\n"
    "| Proximate Obj.     | [Y/N + how]     | [describe]  | [describe]        |\n"
    "| Chain-Link Systems | [Y/N + how]     | [describe]  | [describe]        |\n"
    "| Design             | [Y/N + how]     | [describe]  | [describe]        |\n"
    "| Focus              | [Y/N + how]     | [describe]  | [describe]        |\n"
    "| Growth             | [Y/N + how]     | [describe]  | [describe]        |\n"
    "| Advantage          | [Y/N + how]     | [describe]  | [describe]        |\n"
    "| Dynamics           | [Y/N + how]     | [describe]  | [describe]        |\n"
    "| Inertia/Entropy    | [Y/N + how]     | [describe]  | [describe]        |\n"
    "\n"
    "TOP 3 POWER OPPORTUNITIES:\n"
    "1. [Source]: [specific recommendation]\n"
    "2. [Source]: [specific recommendation]\n"
    "3. [Source]: [specific recommendation]\n"
    "\n"
    "STRATEGY ADJUSTMENTS RECOMMENDED: [any changes to policy or actions]\n"
    "```\n"
    "\n"
    "Discuss findings with the user. If significant opportunities are identified,\n"
    "consider revising the guiding policy or actions.\n"
    "\n"
    "Then proceed to the next step."
)

# --- STEP 7: CREATE-DESTROY -------------------------------------------------

CREATE_DESTROY_INSTRUCTIONS = (
    "STEP 7: CREATE-DESTROY STRESS TEST\n"
    "\n"
    + LOAD_REFERENCE.format(path=REFS_DIR / "strategist-thinking.md") + "\n"
    "\n"
    "Apply Rumelt's create-destroy process: actively try to DESTROY the strategy.\n"
    "If it survives, it's stronger. If it doesn't, better to know now.\n"
    "\n"
    "STRESS TEST PROCESS:\n"
    "\n"
    "A. EXPERT PANEL CHALLENGE:\n"
    "   Imagine a panel of tough, experienced strategists reviewing this strategy.\n"
    "   They would ask:\n"
    "\n"
    "   1. 'Why should we believe this diagnosis is correct?'\n"
    "      - What evidence supports it?\n"
    "      - What evidence contradicts it?\n"
    "      - What alternative diagnosis could explain the same facts?\n"
    "\n"
    "   2. 'Why THIS approach and not another?'\n"
    "      - What are you giving up with this guiding policy?\n"
    "      - Is there a simpler or more direct approach?\n"
    "      - What does a competitor do if they learn your strategy?\n"
    "\n"
    "   3. 'Will these actions actually work?'\n"
    "      - Are the actions truly feasible with available resources?\n"
    "      - What happens if the first action fails?\n"
    "      - Are there hidden dependencies or assumptions?\n"
    "\n"
    "   4. 'What could go wrong?'\n"
    "      - What's the most likely failure mode?\n"
    "      - What's the most dangerous failure mode?\n"
    "      - What early warning signs should you watch for?\n"
    "\n"
    "B. ASSUMPTION AUDIT:\n"
    "   List every assumption the strategy relies on.\n"
    "   For each: How confident are we? What happens if it's wrong?\n"
    "\n"
    "C. COMPETITIVE RESPONSE:\n"
    "   If you were the smartest competitor, how would you counter this strategy?\n"
    "   Does the strategy have a response to that counter?\n"
    "\n"
    "D. VERDICT:\n"
    "   Based on the stress test, rate the strategy:\n"
    "   - ROBUST: Survives scrutiny, proceed to artifact\n"
    "   - NEEDS REVISION: Specific weaknesses identified, fix before proceeding\n"
    "   - FUNDAMENTALLY FLAWED: Major rethink needed, return to diagnosis\n"
    "\n"
    "OUTPUT FORMAT:\n"
    "```\n"
    "CREATE-DESTROY STRESS TEST\n"
    "==========================\n"
    "\n"
    "EXPERT CHALLENGES:\n"
    "  Challenge 1: [question]\n"
    "    Our response: [how strategy holds up]\n"
    "    Strength: [STRONG / ADEQUATE / WEAK]\n"
    "\n"
    "  Challenge 2: [question]\n"
    "    Our response: [how strategy holds up]\n"
    "    Strength: [STRONG / ADEQUATE / WEAK]\n"
    "\n"
    "  [continue...]\n"
    "\n"
    "KEY ASSUMPTIONS:\n"
    "  1. [assumption] — Confidence: [HIGH/MEDIUM/LOW] — If wrong: [impact]\n"
    "  2. [assumption] — Confidence: [HIGH/MEDIUM/LOW] — If wrong: [impact]\n"
    "\n"
    "COMPETITIVE RESPONSE:\n"
    "  Most likely counter: [describe]\n"
    "  Our defense: [describe]\n"
    "\n"
    "VERDICT: [ROBUST / NEEDS REVISION / FUNDAMENTALLY FLAWED]\n"
    "  Specific weaknesses: [list]\n"
    "  Recommended changes: [list]\n"
    "```\n"
    "\n"
    "If NEEDS REVISION: Work with the user to fix the weaknesses, then re-run\n"
    "this step to re-test. Command to re-run:\n"
    "  python3 {script} --step 7\n"
    "\n"
    "If FUNDAMENTALLY FLAWED: Return to the step that needs rework:\n"
    "  Diagnosis broken?  -> python3 {script} --step 2\n"
    "  Policy broken?     -> python3 {script} --step 4\n"
    "  Actions broken?    -> python3 {script} --step 5\n"
    "\n"
    "If ROBUST: Proceed to artifact generation.".format(
        script=SKILL_DIR / "strategize.py"
    )
)

# --- STEP 8: ARTIFACT -------------------------------------------------------

ARTIFACT_INSTRUCTIONS = (
    "STEP 8: STRATEGY DOCUMENT ARTIFACT\n"
    "\n"
    "Generate the final strategy document. This is the deliverable.\n"
    "\n"
    "The document should be written for a CEO or GM audience — clear,\n"
    "direct, and actionable. No fluff. No buzzwords. Every sentence should\n"
    "carry weight.\n"
    "\n"
    "DOCUMENT STRUCTURE:\n"
    "\n"
    "Write the strategy document in this format and save it as a markdown file\n"
    "in the current working directory:\n"
    "\n"
    "```markdown\n"
    "# [Strategy Title]\n"
    "\n"
    "## Executive Summary\n"
    "[2-3 paragraph overview: the challenge, the approach, and the key moves.\n"
    " A busy executive should be able to read this and understand the strategy.]\n"
    "\n"
    "## The Challenge (Diagnosis)\n"
    "[The diagnosis, stated clearly and precisely.\n"
    " What is really going on. What obstacles we face and why.\n"
    " This should simplify reality without distorting it.]\n"
    "\n"
    "## Our Approach (Guiding Policy)\n"
    "[The guiding policy and its rationale.\n"
    " What we are choosing to do — and what we are choosing NOT to do.\n"
    " How this approach responds to the specific challenge diagnosed above.]\n"
    "\n"
    "## Action Plan (Coherent Actions)\n"
    "\n"
    "### Proximate Objective\n"
    "[The first domino — what we do first and why.]\n"
    "\n"
    "### Supporting Actions\n"
    "[Each action with: what, who, when, and how it reinforces the whole.]\n"
    "\n"
    "### Coherence Map\n"
    "[How the actions work together as a system.]\n"
    "\n"
    "## Strategic Leverage\n"
    "[Which sources of power this strategy employs and how.\n"
    " Top opportunities identified in the audit.]\n"
    "\n"
    "## Risks and Assumptions\n"
    "[Key assumptions the strategy depends on.\n"
    " Most likely and most dangerous failure modes.\n"
    " Early warning signs to monitor.]\n"
    "\n"
    "## Appendix: Strategy Quality Check\n"
    "[Results of the bad strategy scan and create-destroy stress test.\n"
    " Demonstrates this strategy has been rigorously tested.]\n"
    "```\n"
    "\n"
    "WRITING GUIDELINES:\n"
    "- Write in plain, direct language. If Rumelt would call it fluff, remove it.\n"
    "- Every claim should be grounded in the analysis from previous steps.\n"
    "- The diagnosis section should make the reader say 'yes, that's exactly it.'\n"
    "- The guiding policy should make some readers uncomfortable (hard choices).\n"
    "- The actions should feel concrete and doable, not aspirational.\n"
    "\n"
    "After writing the document, present it to the user and ask:\n"
    "1. Does the diagnosis ring true?\n"
    "2. Is the guiding policy making the right tradeoffs?\n"
    "3. Are the actions feasible with your current resources?\n"
    "4. What would you change?"
)


# ============================================================================
# STEP DEFINITIONS
# ============================================================================

STEP_TITLES = {
    1: "Strategic Intake",
    2: "Developing the Diagnosis",
    3: "Bad Strategy Scan",
    4: "Developing the Guiding Policy",
    5: "Defining Coherent Actions",
    6: "Sources of Power Audit",
    7: "Create-Destroy Stress Test",
    8: "Strategy Document Artifact",
}

STEP_INSTRUCTIONS = {
    1: INTAKE_INSTRUCTIONS,
    2: DIAGNOSIS_INSTRUCTIONS,
    3: BAD_STRATEGY_SCAN_INSTRUCTIONS,
    4: GUIDING_POLICY_INSTRUCTIONS,
    5: COHERENT_ACTIONS_INSTRUCTIONS,
    6: SOURCES_OF_POWER_INSTRUCTIONS,
    7: CREATE_DESTROY_INSTRUCTIONS,
    8: ARTIFACT_INSTRUCTIONS,
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
            f"The strategy document has been generated. "
            f"Review it with the user and iterate as needed."
        )


def format_output(step: int) -> str:
    """Build the output for a given step."""
    if step not in STEP_TITLES:
        return f"ERROR: Invalid step {step}. Valid steps: 1-{TOTAL_STEPS}"

    title = STEP_TITLES[step]
    instructions = STEP_INSTRUCTIONS[step]

    if step < TOTAL_STEPS:
        next_cmd = f"python3 {SKILL_DIR / 'strategize.py'} --step {step + 1}"
    else:
        next_cmd = ""

    return format_step(
        instructions,
        next_cmd,
        title=f"STRATEGY KERNEL - Step {step}/{TOTAL_STEPS}: {title}",
    )


# ============================================================================
# ENTRY POINT
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Strategy Kernel - Rumelt's Good Strategy Bad Strategy framework"
    )
    parser.add_argument(
        "--step", type=int, required=True,
        help=f"Workflow step (1-{TOTAL_STEPS})"
    )
    args = parser.parse_args()
    print(format_output(args.step))


if __name__ == "__main__":
    main()
