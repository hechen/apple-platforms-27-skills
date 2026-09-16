# Validation and compatibility evidence

Initial validation: September 15, 2026. These results describe the checked artifact and tool versions, not every future agent or SDK release.

## Checks performed

| Check | Evidence |
|---|---|
| Standard skill packaging | Eight skill entrypoints with names/descriptions, optional UI metadata, and eight supporting references |
| Original skill format validation | All eight passed the authoring validator |
| Portable repository validation | Metadata, sibling/reference links, optional UI prompts, and absence of machine-specific home paths |
| Validator regression checks | Valid references, missing references, mismatched discovery name, invalid YAML shape, escaping file link |
| Skills CLI installation | Version 1.5.26; all eight skills installed for 13 selected agent IDs in an isolated project |
| Installed content integrity | Every skill file matched the source byte-for-byte across all six distinct destination roots |
| GitHub CLI installation | Version 2.97.0; local discovery and full-set installation into an isolated custom directory |
| SDK compile probe | Xcode 27.0 (27A266a); selected APIs type-checked for arm64 iOS 27.0 and macOS 27.0 |
| Read-only SDK helper | Inventory, known symbol, missing symbol, and incomplete arguments checked |

## Tested agent installation routes

The Skills CLI smoke check selected:

```text
claude-code cursor github-copilot gemini-cli windsurf opencode
cline roo continue antigravity amp openclaw codex
```

The installer resolved these 13 IDs into six project roots: `.agents/skills`, `.claude/skills`, `.windsurf/skills`, `.roo/skills`, `.continue/skills`, and `skills`. Each contained all eight skills and their supporting resources. Several agents intentionally share `.agents/skills`; the number of folders is not the number of supported hosts.

This proves installer recognition and preservation of the bundle, including relative sibling references. It does **not** prove that all 13 agent applications were launched, that every agent version discovers every directory, or that every underlying model follows the instructions correctly. Activation and application behavior should be verified in the actual host used for a task.

## Reproduce repository checks

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
.venv/bin/python -m unittest discover -s tests -v
```

The GitHub Actions workflow runs these portable checks on Linux. They do not require Xcode or agent credentials.

On a compatible Mac:

```sh
bash scripts/check-sdk.sh
```

The Swift source is [Platform27Probe.swift](../tests/Platform27Probe.swift). It checks selected shared modifiers and protocol constraints, plus an iOS-only toolbar branch. It does not compile every API discussed by the skills and does not run an app.

## Remaining runtime verification

No production app, Siri integration, model generation, managed entitlement, physical-device benchmark, document migration, or App Store release was executed as part of authoring this collection. Those checks depend on a real application and remain explicit steps in the relevant skill.

A source link that resolves is not proof that its content will never change. Research dates and SDK observations are recorded in the technical references; implementing agents must refresh changing assumptions.
