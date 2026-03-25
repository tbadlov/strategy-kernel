---
name: strategize
description: This skill should be used when the user asks to "develop a strategy", "create a strategy document", "critique my strategy", "apply Rumelt's framework", "diagnose our strategic challenge", "build a strategy kernel", or mentions Good Strategy Bad Strategy, Rumelt, strategy diagnosis, guiding policy, or coherent actions. Provides an 8-step interactive workflow grounded in Richard Rumelt's kernel framework for business and product strategy.
argument-hint: "[describe your strategic challenge or context]"
version: 0.1.0
---

# Strategy Kernel

Interactive strategic thought partner grounded in Richard Rumelt's *Good Strategy Bad Strategy* kernel framework. Challenges thinking through Socratic probing, detects bad strategy patterns, and generates rigorous strategy documents.

## Invocation

When this skill activates, IMMEDIATELY invoke the script. The script IS the workflow.

Run from the skill directory:

```bash
cd ${CLAUDE_SKILL_DIR} && python3 strategize.py --step 1
```

| Argument | Required | Description        |
| -------- | -------- | ------------------ |
| `--step` | Yes      | Current step (1-8) |

## Workflow

| Step | Phase              | What happens                                         |
| ---- | ------------------ | ---------------------------------------------------- |
| 1    | Intake             | Gather strategic context, understand the situation   |
| 2    | Diagnosis          | Develop sharp diagnosis of the challenge             |
| 3    | Bad Strategy Scan  | Check for the 4 hallmarks of bad strategy            |
| 4    | Guiding Policy     | Develop approach to overcome the diagnosed challenge |
| 5    | Coherent Actions   | Define coordinated, feasible action set              |
| 6    | Sources of Power   | Audit strategic leverage points                      |
| 7    | Create-Destroy     | Stress-test the strategy                             |
| 8    | Artifact           | Generate final strategy document                     |

## Interaction Guidelines

- Conduct each step as an INTERACTIVE conversation. Ask Socratic questions via AskUserQuestion.
- Reject vague inputs. Push back. Challenge. Probe for specificity.
- Explain directional choices using Rumelt's framework concepts.
- Assume the user knows the framework — communicate as a strategic peer.
- Apply the create-destroy discipline: generate alternatives, then try to break them.

## Resources

### Reference Files

Consult these for detailed framework knowledge when working through steps:

- **`references/rumelt-kernel.md`** — The three elements of the strategy kernel (diagnosis, guiding policy, coherent actions) with definitions, tests, and interrelationships. Load during Steps 2, 4, 5.
- **`references/bad-strategy.md`** — The four hallmarks of bad strategy with detection tests, root causes, and red flags. Load during Step 3.
- **`references/sources-of-power.md`** — All nine sources of strategic power with audit framework and application guidance. Load during Step 6.
- **`references/strategist-thinking.md`** — Create-destroy discipline, metacognition, anomaly detection, strategy-as-hypothesis, and key examples from the book. Load during Steps 1, 2, 7.

### Script

The `strategize.py` script drives the 8-step workflow. Each step prints instructions and a `NEXT STEP` directive. Follow the directive to advance.

ARGUMENTS: $ARGUMENTS
