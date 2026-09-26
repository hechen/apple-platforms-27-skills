---
name: apple-platforms-27
description: "Plan and coordinate adoption of iOS 27, iPadOS 27, macOS 27, and Xcode 27; verify public API availability and route to focused platform skills. Use for cross-platform upgrades or feature planning based on the 27 releases."
---

# Apple Platforms 27 Development

Coordinate an evidence-based upgrade while preserving the app's deployment targets, document formats, and public interfaces unless the user requests a change.

## Start with the actual project

1. Inspect project instructions, targets, schemes, deployment versions, package constraints, entitlements, and the selected Xcode. Distinguish native macOS, Mac Catalyst, and iPhone/iPad apps running on Mac.
2. Run `xcodebuild -version`, `xcodebuild -showsdks`, and inspect build settings for the affected targets. Xcode version, SDK version, minimum OS, actual runtime, hardware eligibility, and service availability are separate facts.
3. For a consumer feature request, read [feature-map.md](references/feature-map.md). Treat MacRumors as discovery context; use Apple documentation and the selected SDK to establish implementation support.
4. Choose the smallest set of skills below. For a migration, first repair build/launch regressions, then adopt optional features with clear product value.

## Routing

| Work | Skill |
|---|---|
| iPhone scenes, resizing, Mirroring, launch requirements | [ios-27-development](../ios-27-development/SKILL.md) |
| iPhone Duo folds, vertical bars, hinge, camera, display transitions | `iphone-duo-development` from [hechen/iphone-duo-skills](https://github.com/hechen/iphone-duo-skills), a separate collection |
| iPad windows, input, external displays, handwriting | [ipados-27-development](../ipados-27-development/SKILL.md) |
| Native Mac windows, commands, AppKit, documents | [macos-27-development](../macos-27-development/SKILL.md) |
| SwiftUI source migration, toolbars, documents, interactions | [swiftui-27-adoption](../swiftui-27-adoption/SKILL.md) |
| Siri, App Schemas, semantic indexing, Shortcuts | [app-intents-27](../app-intents-27/SKILL.md) |
| In-app generation, image prompts, PCC, model providers | [foundation-models-27](../foundation-models-27/SKILL.md) |
| Deploying your own neural models on Apple silicon | [core-ai-27](../core-ai-27/SKILL.md) |

iPhone Duo guidance is not part of this bundle. When the work involves iPhone Duo and `iphone-duo-development` is not installed, ask the user to install that collection (`npx skills add hechen/iphone-duo-skills --skill '*'`) instead of improvising Duo-specific APIs.

Read only the relevant skill. These are release-specific additions to existing framework skills, not a mandate to refactor unrelated code. Framework-specific skills such as CloudKit, StoreKit, WidgetKit, and accessibility remain appropriate for their normal tasks.

Read [release-updates.md](references/release-updates.md) for the dated 27.1 and 27.2 beta review, including toolchain branch differences and project-format compatibility.

## Establish API evidence

Read [verification.md](references/verification.md) when resolving availability, SDK differences, or release readiness. Recheck current Apple docs for changed APIs. Prefer final release notes over old beta examples; use the installed SDK declaration and a compile probe for spelling and platform availability. Record disagreements instead of silently treating one source as universally correct.

The read-only helper `scripts/sdk_probe.py` prints the selected toolchain and optionally declaration context:

```sh
python3 scripts/sdk_probe.py --sdk iphoneos --framework SwiftUI --symbol toolbarMinimizationBehavior
python3 scripts/sdk_probe.py --sdk macosx --framework SwiftUI --symbol topBarPinnedTrailing
```

Paths above are relative to this skill directory. The helper does not prove runtime behavior, entitlements, or App Store eligibility.

## Deliver

Report the changed behavior, verified platforms/builds, compatibility path, and remaining concrete limitations. Keep compile success, interactive QA, saved data, cross-device sync, uploaded build, and release availability separate. Do not publish or change signing/distribution configuration merely because this skill was selected.
