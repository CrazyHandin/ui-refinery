# UI Refinery · 界面精炼

[中文](README.md) | **English**

A task-scoped Codex skill for exploring visual directions, reusing interface conventions, covering relevant interaction states, and refining real UI through screenshots and functional evidence.

This repository contains the enhanced version renamed from `distinctive-ai-design`, plus selected design-engineering references adapted from Emil Kowalski's work. The skill name is **`ui-refinery`**. See [NOTICE](NOTICE.md) for provenance and third-party attribution.

## Scope

Use it when the current request explicitly involves designing, implementing, modifying, or reviewing a concrete software interface's layout, visual presentation, or interaction experience.

Backend work, scripts, configuration, documentation, code explanation, and repository analysis without an interface objective do not acquire UI design or screenshot requirements. Reading, installing, or maintaining the skill itself does not start its design workflow. Mixed requests apply the workflow only to their UI portion.

## Install

Ask Codex with `skill-installer`:

```text
Use skill-installer to install the skill at the root of https://github.com/CrazyHandin/ui-refinery, named ui-refinery, in this Codex environment's user skill directory.
```

Or clone into your user skill directory:

```sh
mkdir -p ~/.agents/skills
git clone https://github.com/CrazyHandin/ui-refinery.git ~/.agents/skills/ui-refinery
```

Windows PowerShell:

```powershell
git clone https://github.com/CrazyHandin/ui-refinery.git "$env:USERPROFILE\.agents\skills\ui-refinery"
```

The destination should not already exist. Inspect local changes before updating an existing copy. Project-specific installations can use `.agents/skills/ui-refinery`. If changes are not recognized, start a new session or restart Codex.

A global rule forcing every conversation into UI design is unnecessary. Discovery should follow this skill's specific scope.

## Use

```text
Use $ui-refinery to design the settings page for my desktop tool.
The main task is quickly finding and adjusting common options. Keep the existing stack.
Propose three distinct information structures, choose the most suitable one, and implement it.
Check relevant states and real screenshots, and state what remains unverified.
```

For an isolated fix:

```text
Use $ui-refinery to fix the confirm button being obscured in this narrow-window dialog.
Keep the existing visual conventions and limit changes to the relevant layout and interaction.
Verify the primary action and focus path.
```

Explore alternatives for open-ended new designs. Reuse an established direction. Keep local fixes short and focused. Concept-only requests remain concept-only.

## On-demand references

| Reference | Use for |
| --- | --- |
| [Software UI](references/software-ui.md) | Product structure, design tokens, states, and relevant viewport checks |
| [Review and media](references/review-and-media.md) | Screenshot evidence, bounded visual refinement, and purposeful media |
| [Motion and polish](references/motion-and-polish.md) | Actual motion implementation, feedback, or diagnosis |
| [Realistic data boundaries](references/ui-data-stress.md) | Long content, missing fields, count extremes, and layout failures |
| [Mobile web](references/mobile-web.md) | Touch, scrolling, safe areas, and on-screen keyboards in Web/PWA |
| [Skill evaluation](references/skill-evaluation.md) | Skill changes or explicit comparisons between versions |

Load only what the task needs. Browser access, hardware, independent review, and media generation depend on the available environment and authorization. State missing evidence; screenshots cannot establish motion performance, functional correctness, or complete accessibility conformance.

The execution instructions and detailed references are currently in Chinese. This README documents the same skill rather than a separate English implementation.

## Validation

```sh
python -m pip install -r tests/requirements.txt
python -X utf8 tests/validate_skill.py
python -X utf8 -m unittest discover -s tests -p 'test_*.py' -v
```

See the [validation guide](docs/VALIDATION.md). Structural checks and automated tests do not prove visual improvement. UI generation, screenshot refinement, performance, and real-device behavior need separate evidence.

Historical records under `docs/` retain earlier names and source context. Upstream CI links in those records are not claims about this repository's current CI.

## Sources

Based on [houxin0010/distinctive-ai-design](https://github.com/houxin0010/distinctive-ai-design), retaining its attribution to Anshu Chimala's article. Selected additional references derive from a [pinned emilkowalski/skills revision](https://github.com/emilkowalski/skills/tree/a81dbca07f2217b7103e510c0f13f8d5b017afc9), with the corresponding [MIT notice](references/licenses/emilkowalski-MIT.txt) included. See [NOTICE](NOTICE.md).
