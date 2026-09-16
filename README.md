# Apple Platforms 27 Skills

**Apple-documented development guidance for iOS 27, iPadOS 27, macOS 27, and Xcode 27 — packaged as portable agent skills.**

Use these skills with **Claude Code, Cursor, GitHub Copilot, Gemini CLI, Windsurf/Cascade, OpenCode, Cline, Roo Code, Continue, Antigravity, Amp, OpenClaw, Codex**, and other tools that support the [Agent Skills standard](https://agentskills.io/specification).

Eight focused skills help a coding agent make informed platform decisions, check actual SDK declarations, implement the relevant changes, and verify the resulting behavior. The core instructions are plain Markdown with standard YAML metadata. No proprietary agent API, MCP server, or model provider is required to read them.

[Get started](#quick-start) · [Skill catalog](#skill-catalog) · [Installation and compatibility](docs/installation.md) · [Validation](docs/validation.md) · [Contributing](CONTRIBUTING.md)

## Why this exists

A new Apple OS release introduces several different kinds of change at once: consumer features, public framework APIs, compiler behavior, linked-SDK requirements, and services restricted by hardware or account eligibility. Treating all of them as “an iOS 27 API” produces bad migrations.

This collection turns the release into practical implementation guidance:

- **Start with the product goal.** Choose the relevant capability instead of adopting every new framework.
- **Check the API that actually ships.** Confirm spelling, platform exclusions, deployment availability, and runtime readiness.
- **Preserve compatibility.** Keep existing deployment targets, public interfaces, and file formats unless the requested change requires a deliberate migration.
- **Validate the real integration.** Compilation, system discovery, persisted data, device behavior, and service access are separate results.

The collection began with the topics in [MacRumors’ features-to-try introduction](https://www.macrumors.com/guide/ios-27-features-to-try-first/). Technical guidance comes from Apple’s documentation, WWDC26 sessions, release notes, and SDK inspection. The [feature map](skills/apple-platforms-27/references/feature-map.md) connects those consumer topics to public development paths and identifies cases where an equivalent public API was not established.

## Quick start

Run this **from the app project where you want to use the skills**. Requires Node.js/npm:

```sh
npx skills add hechen/apple-platforms-27-skills --skill '*'
```

Select your agent when prompted. Install all eight skills together: their relative links connect the platform guidance to the shared framework guidance.

For a specific agent:

```sh
# Claude Code
npx skills add hechen/apple-platforms-27-skills --skill '*' --agent claude-code

# Cursor
npx skills add hechen/apple-platforms-27-skills --skill '*' --agent cursor

# Multiple agents in one project
npx skills add hechen/apple-platforms-27-skills --skill '*' \
  --agent github-copilot gemini-cli opencode codex
```

The [Skills CLI](https://github.com/vercel-labs/skills) handles each agent’s installation location. For GitHub CLI, manual installation, global scope, Windsurf, and additional agents, see [installation.md](docs/installation.md).

Then ask your agent:

> Use the apple-platforms-27 skill to assess this app for iOS 27, iPadOS 27, and macOS 27 adoption. Preserve the current minimum deployment targets. Implement the changes relevant to this feature and verify them on the affected platforms.

Use your agent’s skill picker or explicit invocation syntax if it does not select the skill automatically. For example, Claude Code supports `/apple-platforms-27`; Codex supports `$apple-platforms-27`. A plain-language request naming the skill is the portable starting point, not a guarantee of identical activation behavior in every host. See [Claude’s skill documentation](https://code.claude.com/docs/en/skills) and your host’s current instructions.

## Skill catalog

| Skill | When to use it | What it helps verify |
|---|---|---|
| [apple-platforms-27](skills/apple-platforms-27/SKILL.md) | Cross-platform planning and upgrade coordination | Public API evidence, feature mapping, deployment and runtime distinctions |
| [ios-27-development](skills/ios-27-development/SKILL.md) | iPhone SDK migration and adaptive layouts | Scene lifecycle, launch metadata, resizing, iPhone Mirroring |
| [ipados-27-development](skills/ipados-27-development/SKILL.md) | iPad productivity and document workflows | Independent windows, keyboard/pointer input, external displays, handwriting |
| [macos-27-development](skills/macos-27-development/SKILL.md) | Native Mac adoption | Commands, focus, AppKit menus/toolbars, documents, window behavior |
| [swiftui-27-adoption](skills/swiftui-27-adoption/SKILL.md) | SwiftUI compilation or feature migration | State/ContentBuilder, platform-specific toolbars, documents, reordering, image caching |
| [app-intents-27](skills/app-intents-27/SKILL.md) | Siri AI, Shortcuts, and Spotlight integration | App Schemas, stable entities, indexing, annotations, system-path tests |
| [foundation-models-27](skills/foundation-models-27/SKILL.md) | AI features inside an app | Image prompts, typed output, Dynamic Profiles, providers, PCC, evaluations |
| [core-ai-27](skills/core-ai-27/SKILL.md) | Running a custom neural model | Model conversion, specialization, descriptors, caching, device performance |

### 1. Plan an upgrade without losing compatibility

The coordinator starts from the project’s targets, selected Xcode, minimum OS versions, entitlements, and requested behavior. It routes to only the relevant skills. An improvement delivered by a compiler upgrade should not automatically raise the deployment target; a runtime-only feature needs an availability boundary and a useful fallback.

### 2. Build for the actual window

The platform skills focus on scene ownership, container-driven layout, keyboard and pointer input, and preservation of editing state. They distinguish native macOS, Catalyst, and iOS apps running on Mac. Document changes include saved-file round trips and existing format compatibility, not just a successful build.

### 3. Adopt SwiftUI with precise availability

SwiftUI guidance addresses source migration and optional feature adoption separately. It records discrepancies between WWDC descriptions and final declarations. For example, the observed SDK uses `toolbarMinimizationBehavior(_:for:)`; mobile pinned/overflow toolbar APIs are explicitly unavailable on macOS. See the [dated API notes](skills/swiftui-27-adoption/references/api-notes.md) and [Apple’s toolbar documentation](https://developer.apple.com/documentation/swiftui/toolbarminimizationbehavior).

### 4. Make app capabilities usable by Siri

App Intents guidance starts with typed actions and entities backed by the app’s authoritative data store. It covers appropriate schemas, index lifecycle, visible/selected content annotations, and integration tests through the system. It does not interpret Siri’s access to personal context as permission for an app to read other apps’ private data.

### 5. Ship an AI feature with explicit boundaries

Foundation Models guidance separates on-device generation, Private Cloud Compute, and third-party providers. It includes availability, quotas, cancellation, structured-output validation, tool authorization, and evaluation. Core AI covers the lower-level custom-model path. Neither skill silently changes an on-device promise into cloud processing.

## Example requests

**Fix an SDK migration**

> Use swiftui-27-adoption to diagnose the Xcode 27 build errors. Keep the existing deployment target and public interfaces. Fix the actual diagnostics and verify both iOS and macOS targets.

**Improve iPad behavior**

> Use ipados-27-development to make this editor work across narrow and wide windows. Keep selection and unsaved edits stable when two windows are open. Verify keyboard navigation and save/reopen behavior.

**Expose a useful Siri action**

> Use app-intents-27 to let people find and update an item in this app. Choose a matching documented schema if one exists, reuse the domain service, and test stale IDs, cancellation, and the saved result.

**Add private image analysis**

> Use foundation-models-27 to extract structured attributes from a selected photo. Keep processing on-device, support model-unavailable states, and require review before saving inferred values.

## Agent compatibility

The same eight `SKILL.md` files serve every agent. Supporting references and the SDK helper use relative paths. The optional `agents/openai.yaml` files provide Codex UI metadata; the actual workflow does not depend on them, and other hosts can ignore them.

We distinguish **format compatibility**, **successful installation**, **agent activation**, and **successful app work**. A successful installer test does not prove that every model and agent version follows every instruction correctly. The exact tested installation routes and limits are in [validation.md](docs/validation.md).

Tools without native Agent Skills support can still read the relevant `SKILL.md` and references as task context. That is a manual fallback, not automatic skill discovery. Do not flatten all eight skills into an always-loaded rule file: select the task-specific material.

## Requirements

- Reading and installing the guidance does not require a Mac.
- Building or type-checking Apple platform code requires a compatible Mac and Xcode with the relevant SDKs.
- The read-only SDK helper requires Python 3 and command-line access to the selected Xcode.
- Framework-specific services, capabilities, accounts, and physical-device checks remain subject to Apple’s current requirements.

Example SDK inspection, run from this repository:

```sh
python3 skills/apple-platforms-27/scripts/sdk_probe.py \
  --sdk iphoneos --framework SwiftUI --symbol toolbarMinimizationBehavior
```

## Repository layout

```text
skills/                 Eight portable skill directories
  <skill>/SKILL.md      Standard metadata and task instructions
  <skill>/references/  Focused technical guidance, where needed
  <skill>/agents/      Optional host UI metadata
docs/                   Installation, sources, and validation
scripts/                Repository validation and SDK compile checks
tests/                  Validation tests and a small Swift compile probe
```

## Sources and maintenance

Initial technical review: **September 15, 2026**. Initial SDK checks: **Xcode 27.0 (27A266a)** with iOS/macOS 27.0 SDKs. These are dated observations; the skills ask the implementing agent to inspect the current environment before relying on them.

Start with Apple’s [iOS guide](https://developer.apple.com/wwdc26/guides/ios/), [iPadOS guide](https://developer.apple.com/wwdc26/guides/ipados/), and [macOS guide](https://developer.apple.com/wwdc26/guides/macos/). [Sources and scope](docs/sources.md) explains how evidence is selected and which consumer capabilities are not established public APIs.

Corrections should include an Apple source, affected SDK/platform, and a focused reproduction when appropriate. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE) for this repository’s original instructions and code. Linked Apple and third-party documentation retains its respective ownership and terms. This is an independent community project, not an Apple or agent-vendor product.
