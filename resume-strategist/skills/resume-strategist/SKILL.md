---
name: resume-strategist
description: >
  This skill should be used when the user asks to "update my resume",
  "tailor my resume", "prepare resume for a role", "help me with my CV",
  "optimize my resume", "write my resume for [company]",
  "interview me for resume content", "extract my achievements",
  or mentions resume strategy, CTO resume, executive resume, or
  applying for a CTO/VP Engineering/technical executive role.
  Provides a 7-step interactive interview workflow that extracts
  business-outcome-driven achievements and produces tailored resumes
  for Series C/D and IPO-track companies.
argument-hint: "[describe the target role or paste a job description]"
version: 0.1.0
---

# Executive CTO Resume Strategist

Interactive interview workflow for crafting CTO resumes targeting Series C/D and
IPO-track companies. Extracts business-outcome-driven achievements through structured
Socratic interviewing, then produces a tailored resume using the CAR framework.

## Invocation

When this skill activates, IMMEDIATELY invoke the script. The script IS the workflow.

Run from the skill directory:

```bash
cd ${CLAUDE_SKILL_DIR} && python3 resume_strategist.py --step 1
```

| Argument | Required | Description        |
| -------- | -------- | ------------------ |
| `--step` | Yes      | Current step (1-7) |

## Workflow

| Step | Phase              | What happens                                              |
| ---- | ------------------ | --------------------------------------------------------- |
| 1    | Intake             | Read resume, understand target opportunity, decode JD     |
| 2    | Company Context    | Extract company mission, vision, CTO's strategic role     |
| 3    | Impact Interview   | Systematic extraction of business outcomes (all 4 functions) |
| 4    | Leadership Probe   | Team building, org design, board, cross-functional, M&A   |
| 5    | Gap Analysis       | Map extracted content against opportunity requirements    |
| 6    | Bullet Crafting    | Rewrite achievements using CAR framework, iterate with user |
| 7    | Resume Artifact    | Generate final tailored resume document                   |

## Interaction Guidelines

- Conduct each step as an INTERACTIVE conversation. Ask Socratic questions via AskUserQuestion.
- Push for specificity and quantification. Do not accept vague claims.
- Every achievement must connect to BUSINESS OUTCOMES (revenue, cost, scale, speed, risk).
- Probe ALL FOUR functions: product, engineering, data, infrastructure.
- Respect the Integrity Constraint: never help fabricate unverifiable numbers.
- Assume the existing resume is insufficient — the interview extracts what's missing.
- Calibrate language to the TARGET company's stage, not the user's current stage.

## Resources

### Reference Files

Consult these for detailed framework knowledge when working through steps:

- **`references/car-framework.md`** — The CAR (Challenge → Action → Result) framework for executive resume bullets. Tests for each element, verb hierarchy, metric hierarchy, quantification estimation with integrity constraint. Load during Steps 6, 7.
- **`references/cto-impact-dimensions.md`** — The four CTO functions (product, engineering, data, infrastructure), cross-cutting executive dimensions, and extraction priority guidance. Load during Steps 2, 3, 4.
- **`references/stage-calibration.md`** — What boards and investors assess at Series C, D, IPO-track, and public stages. Stage translation guide for framing the same achievement differently. Load during Steps 1, 5, 6.
- **`references/interview-playbook.md`** — Evidence-based probing questions organized by phase: company context, business outcomes, leadership, technical excellence. Includes probing techniques and red flag detection. Load during Steps 2, 3, 4.

### Script

The `resume_strategist.py` script drives the 7-step workflow. Each step prints instructions and a `NEXT STEP` directive. Follow the directive to advance.

ARGUMENTS: $ARGUMENTS
