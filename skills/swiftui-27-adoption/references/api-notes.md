# SwiftUI 27 API notes

Snapshot verified against local Xcode 27.0 (27A266a), 2026-09-15. Recheck when Xcode changes. iPadOS follows iOS annotations.

| API | Observed availability / detail |
|---|---|
| `ToolbarContent.visibilityPriority(_:)` | iOS 27.0; macOS 26.1 in declaration. Check argument type availability too. |
| `View.toolbarOverflowMenu(content:)` | iOS 27.0; explicitly unavailable on macOS |
| `ToolbarItemPlacement.topBarPinnedTrailing` | iOS 27.0; explicitly unavailable on macOS |
| `View.toolbarMinimizationBehavior(_:for:)` | Declaration uses `anyAppleOS 27.0`; individual behaviors/placements need their own checks |
| `ReadableDocument`, `WritableDocument`, `Document` | iOS/macOS 27.0; `Document` combines the two protocols |
| `View.reorderContainer(...)` | iOS/macOS 27.0; overloads carry item/collection identity constraints |
| `View.swipeActionsContainer()` | iOS/macOS 27.0 |
| `View.asyncImageURLSession(_:)` | `anyAppleOS 27.0` |

The [WWDC26 SwiftUI guide](https://developer.apple.com/wwdc26/guides/swiftui/) uses `toolbarMinimizeBehavior`; the shipped interface and [ToolbarMinimizationBehavior documentation](https://developer.apple.com/documentation/swiftui/toolbarminimizationbehavior) use `toolbarMinimizationBehavior(_:for:)`. Use the latter after checking the target SDK. WWDC shorthand is not a compilable signature.

[`AsyncImage`](https://developer.apple.com/documentation/swiftui/asyncimage) gains HTTP caching, custom requests, and session configuration. Treat this as transport caching, not durable offline storage or a privacy boundary. Define cache behavior for authenticated/user-specific images and test logout/account switching.

[What's new in SwiftUI](https://developer.apple.com/videos/play/wwdc2026/269/) introduces broader reordering and presentation changes. Keep authoritative ordering in the model; the UI reports a move rather than becoming a second store. Availability on item-bound alerts/dialogs may be back-deployed: inspect the overload instead of blanket-gating to 27.

For runtime changes and final corrections, inspect [iOS/iPadOS release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes) or [macOS release notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes). In particular, verify visible-tab selection and menu icon behavior in the actual target.
