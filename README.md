<div align="center">

# Apple Platforms 27 Skills

**Build for iPhone, iPad, Mac — and iPhone Duo.**

Nine portable coding-agent skills grounded in Apple documentation and checked against real SDKs.

[Install](#install) · [Explore the skills](#skill-catalog) · [iPhone Duo](#iphone-duo) · [What's new](CHANGELOG.md) · [Validation](docs/validation.md)

</div>

<table>
  <tr>
    <td width="33%" align="center"><a href="https://developer.apple.com/ios/"><img src="https://developer.apple.com/ios/images/hero-vx-ios_2x.png" alt="Apple's iOS 27 interface preview" width="260"></a><br><strong>iOS 27</strong><br>Adaptive iPhone experiences</td>
    <td width="33%" align="center"><a href="https://developer.apple.com/ipados/"><img src="https://developer.apple.com/ipados/images/hero-ipad-m4-ipados27-light_2x.jpg" alt="Apple's iPadOS 27 interface preview" width="260"></a><br><strong>iPadOS 27</strong><br>Windows, documents, and input</td>
    <td width="33%" align="center"><a href="https://developer.apple.com/macos/"><img src="https://developer.apple.com/macos/images/screen-macos27-large_2x.jpg" alt="Apple's macOS 27 desktop preview" width="260"></a><br><strong>macOS 27</strong><br>Native desktop interactions</td>
  </tr>
</table>

<sub>Platform previews © Apple Inc., linked from Apple's developer pages. [Image credits](docs/image-credits.md).</sub>

## Give your agent the platform context it needs

Apple releases combine new APIs, compiler changes, linked-SDK requirements, and capabilities that depend on hardware or service eligibility. These skills help an agent distinguish those cases, choose the right implementation path, and verify the result in your app.

- **Build adaptive interfaces.** Preserve navigation and editing state across resizing, windows, and Duo display transitions.
- **Use the right API.** Check declarations, platform exclusions, deployment availability, and runtime readiness before adopting a feature.
- **Integrate useful intelligence.** Expose typed actions to Siri or build app-owned AI with explicit availability and privacy boundaries.
- **Keep existing apps working.** Preserve deployment targets, document formats, and public interfaces unless the requested migration requires a change.

Use the same instructions with **Claude Code, Cursor, GitHub Copilot, Gemini CLI, Windsurf, OpenCode, Cline, Roo Code, Continue, Antigravity, Amp, OpenClaw, and Codex**. The core is standard `SKILL.md` Markdown; no particular model, MCP server, or agent vendor is required.

## Install

From the app repository where you want to use the skills:

```sh
npx skills add hechen/apple-platforms-27-skills --skill '*'
```

Select your agent when prompted. Install all **nine** skills together so their shared references remain available.

<details>
<summary><strong>Choose specific agents or install globally</strong></summary>

```sh
# Claude Code
npx skills add hechen/apple-platforms-27-skills --skill '*' --agent claude-code

# Cursor
npx skills add hechen/apple-platforms-27-skills --skill '*' --agent cursor

# Several agents in one project
npx skills add hechen/apple-platforms-27-skills --skill '*' \
  --agent github-copilot gemini-cli opencode codex

# User-wide Codex installation
npx skills add hechen/apple-platforms-27-skills --skill '*' --agent codex --global
```

Requires Node.js/npm. [Installation and compatibility](docs/installation.md) covers GitHub CLI, manual installation, additional hosts, updates, and activation.

</details>

Then give your agent a concrete task:

> Use apple-platforms-27 to assess this app for iOS 27, iPadOS 27, and macOS 27. Preserve our minimum deployment targets, implement the changes relevant to this feature, and verify each affected platform.

Explicit invocation depends on the host. For example, Codex uses `$apple-platforms-27`; Claude Code supports `/apple-platforms-27`. Naming the skill in plain language is the portable starting point.

## Skill catalog

| Skill | Use it for | Main checks |
|---|---|---|
| [apple-platforms-27](skills/apple-platforms-27/SKILL.md) | Planning an upgrade across platforms | API evidence, feature mapping, deployment and runtime boundaries |
| [ios-27-development](skills/ios-27-development/SKILL.md) | Modernizing an iPhone app | Scene lifecycle, launch metadata, resizing, iPhone Mirroring |
| [iphone-duo-development](skills/iphone-duo-development/SKILL.md) | Adapting to the foldable iPhone | Reserved regions, vertical bars, hinge state, scenes, cameras |
| [ipados-27-development](skills/ipados-27-development/SKILL.md) | Building iPad productivity workflows | Independent windows, keyboard/pointer input, external displays, handwriting |
| [macos-27-development](skills/macos-27-development/SKILL.md) | Delivering a native Mac experience | Commands, focus, AppKit, documents, window behavior |
| [swiftui-27-adoption](skills/swiftui-27-adoption/SKILL.md) | Migrating or adopting SwiftUI APIs | State/ContentBuilder, toolbars, documents, reordering, image caching |
| [app-intents-27](skills/app-intents-27/SKILL.md) | Integrating Siri, Shortcuts, and Spotlight | Schemas, stable entities, indexing, annotations, system-path tests |
| [foundation-models-27](skills/foundation-models-27/SKILL.md) | Building AI features inside an app | Image prompts, typed output, Dynamic Profiles, providers, PCC, evaluations |
| [core-ai-27](skills/core-ai-27/SKILL.md) | Running your own neural models | Conversion, specialization, descriptors, caching, device performance |

Start with the coordinator when the scope is broad. Load a focused skill directly when the task is already clear.

## iPhone Duo

<a href="https://developer.apple.com/iphone-duo/">
  <img src="https://developer.apple.com/iphone-duo/images/main_2x.png" alt="Apple's iPhone Duo opened to show its large inner display and central fold" width="900">
</a>

<sub>iPhone Duo illustration © Apple Inc. Source: [Get ready for iPhone Duo](https://developer.apple.com/iphone-duo/). This is Apple's device illustration, not an app built or tested by this project.</sub>

**New in v1.1:** dedicated guidance for the layout and lifecycle changes a folding display introduces.

| Area | What the skill helps you do |
|---|---|
| **Adaptive layout** | Use container geometry, independent safe-area edges, and appropriate arrangement containers |
| **Fold and camera regions** | Distinguish divisions from occlusions; handle active state and right-to-left coordinates |
| **Vertical bars** | Adapt standard navigation, symbols, axis preferences, priorities, and overflow |
| **Hinge and scenes** | Handle optional hinge state and preserve app state as displays and windows change |
| **Camera experiences** | Choose cameras by direction, handle preview mirroring, and add optional capture accessories |
| **Verification** | Exercise closed/open/folded poses, Split View, accessibility, older devices, and physical capture |

> Use iphone-duo-development to audit this editor. Keep drafts and selection stable while opening, closing, and rotating the device. Fix inaccessible controls around the fold, and report which transitions were actually tested.

**Toolchain note — September 23, 2026:** Apple's Xcode 27.2 beta notes direct Duo development to **Xcode 27.1 beta** for its SDK and simulator support. Selected Duo APIs in this repository compile with **Xcode 27.1 (27A9269)**. See the [dated release review](skills/apple-platforms-27/references/release-updates.md) and [Apple's release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes).

## More ways to use the skills

### Fix an SDK migration

> Use swiftui-27-adoption to diagnose these Xcode 27 build errors. Keep our deployment target and public interfaces. Fix the actual diagnostics and verify both iOS and macOS targets.

### Improve iPad behavior

> Use ipados-27-development to make this editor work in narrow and wide windows. Keep selection and unsaved edits stable with two windows open. Verify keyboard navigation and save/reopen behavior.

### Expose an action to Siri

> Use app-intents-27 to let people find and update an item. Choose a matching documented schema, reuse our domain service, and test stale IDs, cancellation, and the saved result.

### Add private image analysis

> Use foundation-models-27 to extract structured attributes from a selected photo. Keep processing on-device, handle model-unavailable states, and require review before saving inferred values.

## Evidence and compatibility

The skills combine **Apple documentation**, **release notes**, **WWDC/Tech Talk sessions**, and **SDK inspection**. Consumer features are mapped to public development paths in the [feature map](skills/apple-platforms-27/references/feature-map.md).

| Verified for this update | Scope |
|---|---|
| Portable packaging | Nine skill entrypoints, linked resources, optional host metadata |
| Installation | Skills CLI 1.5.26 recognized 13 selected agents; copied files matched across six destination roots |
| Baseline API probe | Selected APIs type-checked for iOS 27.0 and macOS 27.0 deployment targets |
| Duo API probe | Selected SwiftUI, UIKit, and AVKit calls type-checked for iOS 27.1 |

Installation does not prove activation in every agent. Compilation does not prove an app's behavior on a device. The skills require task-specific verification; camera capture and accessory presentation still need physical-device testing. [Full validation record](docs/validation.md).

The same core files serve every host. Optional `agents/openai.yaml` files add Codex UI metadata; other agents can ignore them. Tools without native skill discovery can read a selected entrypoint and its references as ordinary task context. See [installation](docs/installation.md).

## Development and maintenance

Reading the skills does not require a Mac. Building Apple-platform code requires a compatible Mac and the relevant Xcode SDKs. The read-only SDK helper requires Python 3:

```sh
python3 skills/apple-platforms-27/scripts/sdk_probe.py \
  --sdk iphoneos --framework SwiftUI --symbol toolbarMinimizationBehavior
```

```text
skills/     Nine portable skills, focused references, optional UI metadata
docs/       Installation, source policy, image credits, validation
scripts/    Packaging validation and SDK compile checks
tests/      Validator regression tests and Swift API probes
```

**Latest review:** September 23, 2026. The update covers Duo and relevant 27.2 beta changes, including the JSON project configuration format and Catalyst caveats. The original iOS/iPadOS 27.0 and macOS 27.0 release notes matched the September 15 research snapshots. [Changelog](CHANGELOG.md) · [Sources and scope](docs/sources.md) · [Contributing](CONTRIBUTING.md).

The collection began with [MacRumors' iOS 27 introduction](https://www.macrumors.com/guide/ios-27-features-to-try-first/); technical instructions rely on primary Apple sources. Corrections should identify the source, affected SDK, and a focused reproduction when appropriate.

## License and credits

[MIT](LICENSE) covers this repository's original instructions and code. Apple images are remotely embedded from Apple's sites, credited in [image credits](docs/image-credits.md), and are **not covered by this repository's MIT license**. Linked documentation retains its respective ownership and terms.

An independent community project, not affiliated with or endorsed by Apple or any agent vendor.
