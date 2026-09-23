---
name: ios-27-development
description: "Implement or migrate iPhone apps for iOS 27 and Xcode 27, focusing on scene lifecycle, resizable iPhone Mirroring layouts, launch requirements, and UIKit integration changes."
---

# iOS 27 Development

## Scope and evidence

Use this for iPhone-specific 27 adoption. Inspect the selected SDK, existing deployment target, app lifecycle, and app/extension targets first. Preserve support for older OS versions unless a change is requested.

Apple's [Modernize your UIKit app](https://developer.apple.com/videos/play/wwdc2026/278/) explains the resizable iPhone model. Validate implementation details against [TN3210](https://developer.apple.com/documentation/technotes/tn3210-optimizing-your-app-for-iphone-mirroring) and the [27 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes).

## Launch and layout migration

- Apps linked with the latest SDK need the scene-based lifecycle. Check scene configuration and scene delegates for UIKit; don't add a parallel UIKit lifecycle to an already correct SwiftUI `App`.
- Verify a supported launch-screen entry in the built Info.plist: `UILaunchStoryboardName`, `UILaunchStoryboards`, `UILaunchScreen`, or `UILaunchScreens`. Inspect generated settings rather than assuming the source plist is the shipped one.
- Audit `UIScreen.main`, screen bounds, orientation branching, and `userInterfaceIdiom` used for layout. Base layout on container size and traits. Use the actual window scene's screen only when screen information is necessary.
- An iPhone app can stay in the phone idiom while its window becomes wide in Mirroring or on iPad. Device category is not the available layout width.
- Preserve navigation selection, drafts, scroll position, and presented content through size changes. Scope window-specific state to its scene; keep persistent domain data shared.

## Targeted UIKit checks

When relevant, inspect presentation trait overrides, search/navigation bar layout, and external-display scene setup. Siri may load drag representations without a physical drag: keep representation loading free of UI side effects. Put actual drag animations in the appropriate movement callback, not unconditionally in `sessionWillBegin`.

Read [migration-checks.md](references/migration-checks.md) for focused searches and acceptance cases.

## iPhone Duo and later betas

For iPhone Duo, use [iphone-duo-development](../iphone-duo-development/SKILL.md): general resizability alone does not cover fold regions, vertical bars, camera direction, or capture accessories. Check [dated release updates](../apple-platforms-27/references/release-updates.md) when using 27.1 or 27.2 beta SDKs.

## Related work

For SwiftUI migration, read [swiftui-27-adoption](../swiftui-27-adoption/SKILL.md). For Siri use [app-intents-27](../app-intents-27/SKILL.md); for app-owned generation use [foundation-models-27](../foundation-models-27/SKILL.md). A system Siri rollout and availability of an in-app model are separate checks.
