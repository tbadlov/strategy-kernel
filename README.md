# zvika-tools

Personal Claude Code plugin marketplace containing strategic tools for business and product leaders.

Hosted at: https://github.com/tbadlov/strategy-kernel

---

## Installation

Add this marketplace to Claude Code, then install whichever plugins you want:

```bash
# Add the marketplace
claude plugin marketplace add https://github.com/tbadlov/strategy-kernel

# Install strategy-kernel
claude plugin install strategy-kernel

# Install resume-strategist
claude plugin install resume-strategist
```

---

## Plugins

### strategy-kernel

Interactive strategic thought partner grounded in Richard Rumelt's *Good Strategy Bad Strategy* kernel framework. Challenges your thinking through Socratic probing, detects bad strategy patterns, and generates a structured strategy document.

**Invocation:** `/strategize [describe your strategic challenge or context]`

**Workflow:**

| Step | Phase             | What happens                                         |
|------|-------------------|------------------------------------------------------|
| 1    | Intake            | Gather strategic context, understand the situation   |
| 2    | Diagnosis         | Develop sharp diagnosis of the challenge             |
| 3    | Bad Strategy Scan | Check for the 4 hallmarks of bad strategy            |
| 4    | Guiding Policy    | Develop approach to overcome the diagnosed challenge |
| 5    | Coherent Actions  | Define coordinated, feasible action set              |
| 6    | Sources of Power  | Audit strategic leverage points                      |
| 7    | Create-Destroy    | Stress-test the strategy                             |
| 8    | Artifact          | Generate final strategy document                     |

**Reference materials loaded during the workflow:**

| File                    | Contents                                                                          |
|-------------------------|-----------------------------------------------------------------------------------|
| `rumelt-kernel.md`      | The three kernel elements (diagnosis, guiding policy, coherent actions) with tests and interrelationships |
| `bad-strategy.md`       | Four hallmarks of bad strategy with detection tests and root causes               |
| `sources-of-power.md`   | Nine sources of strategic power with audit framework                              |
| `strategist-thinking.md`| Create-destroy discipline, metacognition, anomaly detection, strategy-as-hypothesis |

---

### resume-strategist

Executive resume strategist targeting CTO roles at Series C/D and IPO-track companies. Extracts business-outcome-driven achievements through structured Socratic interviewing and produces a tailored resume using the CAR framework.

**Invocation:** `/resume-strategist [describe the target role or paste a job description]`

**Workflow:**

| Step | Phase           | What happens                                                        |
|------|-----------------|---------------------------------------------------------------------|
| 1    | Intake          | Read resume, understand target opportunity, decode JD               |
| 2    | Company Context | Extract company mission, vision, CTO's strategic role               |
| 3    | Impact Interview| Systematic extraction of business outcomes across all four functions|
| 4    | Leadership Probe| Team building, org design, board, cross-functional, M&A             |
| 5    | Gap Analysis    | Map extracted content against opportunity requirements              |
| 6    | Bullet Crafting | Rewrite achievements using CAR framework, iterate with user         |
| 7    | Resume Artifact | Generate final tailored resume document                             |

**Reference materials loaded during the workflow:**

| File                      | Contents                                                                                      |
|---------------------------|-----------------------------------------------------------------------------------------------|
| `car-framework.md`        | CAR (Challenge, Action, Result) framework: tests, verb hierarchy, metric hierarchy, integrity constraint |
| `cto-impact-dimensions.md`| Four CTO functions (product, engineering, data, infrastructure) with extraction priority guidance |
| `stage-calibration.md`    | What boards and investors assess at Series C, D, IPO-track, and public stages; stage translation guide |
| `interview-playbook.md`   | Evidence-based probing questions by phase with techniques and red flag detection              |

---

## Repository Structure

```
.claude-plugin/
  marketplace.json        # Marketplace manifest listing both plugins
  plugin.json             # strategy-kernel plugin manifest
skills/
  strategize/
    strategize.py         # 8-step workflow orchestrator
    SKILL.md              # Skill trigger and invocation spec
    references/           # Framework reference files (4 documents)
resume-strategist/
  .claude-plugin/
    plugin.json           # resume-strategist plugin manifest
  skills/
    resume-strategist/
      resume_strategist.py  # 7-step workflow orchestrator
      SKILL.md              # Skill trigger and invocation spec
      references/           # Framework reference files (4 documents)
```

---

## Development

Both plugins follow the same pattern:

- **Python orchestrator** (`strategize.py` / `resume_strategist.py`): Accepts a `--step N` argument and prints step-specific instructions including which reference files to load. The script IS the workflow — SKILL.md instructs the agent to run it immediately on activation.
- **SKILL.md**: Defines activation triggers, the slash command name, argument hint, and per-step workflow table. The agent reads this file to understand when and how to invoke the skill.
- **`references/`**: Markdown files containing framework knowledge loaded on demand at the steps where they are relevant. Keeping them separate from the script avoids loading irrelevant context.

To add a new plugin: create a subdirectory with the same structure, add a `.claude-plugin/plugin.json`, and register it in `.claude-plugin/marketplace.json`.

---

## License

Personal tooling. MIT License — use and adapt freely.
