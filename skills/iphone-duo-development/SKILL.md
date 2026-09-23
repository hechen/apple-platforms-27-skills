---
name: iphone-duo-development
description: "Build, migrate, or review iPhone Duo apps using SwiftUI, UIKit, and AVFoundation. Use for foldable layouts, inner/outer display transitions, reserved regions, vertical bars, hinge state, Split View, camera direction, and capture scene accessories on iOS 27.1."
---

# iPhone Duo Development

## Establish the baseline

Start with [ios-27-development](../ios-27-development/SKILL.md) for scene lifecycle and general resizing. Inspect the selected Xcode, SDK, runtime, minimum OS, and Catalyst targets. Keep existing deployment targets and a functional non-Duo path.

Evidence refreshed **September 23, 2026** against Apple documentation and **Xcode 27.1 (27A9269), iOS 27.1 SDK**. Apple's [Duo resources](https://developer.apple.com/iphone-duo/) now include tools and a preparation article. The [27.2 beta notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes) currently direct Duo development to **27.1 beta**. Do not assume the highest version number contains the required SDK/runtime.

Build against the Duo-capable 27.1 SDK to adopt its full-screen and vertical-bar behavior; a runtime availability check alone does not change linked-SDK behavior. Put new calls behind iOS 27.1 availability, and isolate unsupported Catalyst source at compile time. Read [release updates](../apple-platforms-27/references/release-updates.md) for dated toolchain caveats.

## Choose the work

| Need | Read |
|---|---|
| Fold avoidance, adaptive containers, toolbar placement | [Layout and bars](references/layout-and-bars.md) |
| Camera choice, mirroring, outer-display capture UI | [Camera and scenes](references/camera-and-scenes.md) |
| Pose transitions, state preservation, release readiness | [Verification](references/verification.md) |

## Implementation workflow

1. Audit fixed screen sizes, orientation/idiom layout branches, symmetric inset arithmetic, and custom bars. Establish a reproducible failing view before changing architecture.
2. Base layout on the current container, traits, and independent safe-area edges. Keep navigation, selection, drafts, and playback state stable while the same scene changes size or display.
3. Use standard navigation and tab containers first. Select an arrangement container only for content that needs an adaptive primary/secondary relationship. Keep essential actions reachable in every pose.
4. For custom layouts, query reserved regions in the local coordinate space. Handle fold divisions separately from camera occlusions; verify active state and right-to-left geometry.
5. Use hinge observations only when the feature needs hinge state. An angle is not a substitute for the available layout region. Handle an absent hinge without disabling ordinary app functionality.
6. Test the actual app through the verification matrix. Report compilation, simulator interaction, physical capture behavior, and distribution readiness separately.

## Hinge and multiple scenes

The checked SwiftUI API is `onHingeChange(isEnabled:_:)`, with **old and new `DeviceHingeContext`** values; the new context's `hinge` is optional. UIKit uses `UIHingeInteraction`, whose update can also have a nil hinge. SwiftUI exposes an `Angle`; UIKit exposes radians. Avoid hard-coded precision or callback-rate assumptions. See [SwiftUI hinge observation](https://developer.apple.com/documentation/swiftui/view/onhingechange(isenabled:_:)) and [UIKit hinge interaction](https://developer.apple.com/documentation/uikit/uihingeinteraction).

Opening a second window needs independent scene presentation state backed by the shared domain model. Do not treat an open inner display as the iPad idiom or assume that a size change creates a new document. Accessory content is system-presented optional UI, not an arbitrary second UIWindow. See Apple's [multiple-display and scene session](https://developer.apple.com/videos/play/tech-talks/111464/).

## Other UI stacks

For Flutter, React Native, game engines, or web-backed UI, first verify the installed framework/plugin's current iOS support. Fix container resizing and safe-area handling in that layer. If it lacks required native information, design a small typed bridge for the specific region or camera capability; document coordinates, units, availability, and lifecycle. Do not assume an Android fold API reports iOS data. This collection does not claim tested adapters for those frameworks.
