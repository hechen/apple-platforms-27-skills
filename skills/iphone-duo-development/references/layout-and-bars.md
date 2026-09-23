# Layout and bars

Evidence: September 23, 2026; iOS 27.1 SDK declarations and Apple sources below. These are adoption guidelines, not fixed hardware breakpoints.

## Container and safe-area audit

Search for `UIScreen.main`, cached screen bounds, orientation locks used as layout logic, `.phone`/`.pad` branches, hard-coded bar heights, and doubled left/right insets. Replace only the assumptions responsible for a demonstrated problem.

The outer display uses compact horizontal size class; the inner display can provide regular width while retaining the phone idiom. Multitasking changes the space again. Use both current traits and actual container geometry. Test independent edge insets, including controls on either side in Split View. Keep decorative backgrounds and interactive content's safe-area policies separate. Apple's [preparation talk](https://developer.apple.com/videos/play/tech-talks/111461/) explains the linked-SDK tiers and size classes.

## Reserved regions

Use `GeometryProxy.reservedRegions(kind:options:layoutDirectionBehavior:)` or `UIView.reservedRegions(kind:options:)`. Query `.division` for a fold and `.occlusion` for obscured content. Do not infer either from a midpoint or a particular hinge angle.

For current avoidance, explicitly filter `isActive`. Use `.includeInactive` when studying potential regions; don't let an inactive fold reserve permanent blank space. The current overview wording and query-option naming are not fully aligned about inactive results, so test the selected runtime rather than relying on an implicit default.

Region frames already include their margins: avoid adding those margins twice. SwiftUI mirrors region geometry by default for RTL-aware layout; use `.fixed` only when deliberately working in fixed coordinates. Keep geometry in one coordinate system when testing intersections. See [ReservedRegion](https://developer.apple.com/documentation/swiftui/reservedregion) and the [query API](https://developer.apple.com/documentation/swiftui/geometryproxy/reservedregions(kind:options:layoutdirectionbehavior:)).

Prefer relocating a button or adapting a panel over forcing every pixel away from the fold. Continuous scrolling content can cross it; critical touch targets should remain comfortable to reach. See [Design for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111466/).

## Arrangement containers

`ArrangementView` and `UIArrangementViewController` are available in the checked iOS 27.1 SDK. Choose `.split` for adjacent content or `.overlay` for controls over content that separate when folded. Constrain axes only when hiding/repositioning secondary content is intentional. Test access to everything the constrained layout hides. See [ArrangementView](https://developer.apple.com/documentation/swiftui/arrangementview).

Do not blanket-wrap an existing navigation split view, list, or scroll view in another arrangement. Apple's [preparation article](https://developer.apple.com/documentation/technologyoverviews/preparing-your-app-for-iphone-duo) warns that container nesting can make content inaccessible. Inspect the full hierarchy before adding one.

## Vertical bars

Use `NavigationStack`, `NavigationSplitView`, and navigation-controller-owned toolbar items so system adaptation can occur. Hand-built `UIToolbar` or navigation-bar lookalikes do not gain equivalent behavior merely by linking the new SDK.

- Supply an accessible label and symbol for actions. Text-only and custom-view items need deliberate handling in vertical layouts.
- Start with automatic axis behavior. SwiftUI's `ToolbarContent.axisBehavior(_:)` and UIKit's `UIBarButtonItem.axisBehavior` support `.horizontalOnly` and `.verticalPreferred`; horizontal-only actions can disappear when no horizontal bar exists.
- Preserve important completion/navigation actions, then use visibility priority and overflow for secondary actions. Test larger text, localization, and competition with system UI.
- Query `toolbarVerticalEdge` or UIKit's `verticalBarEdge` rather than assuming the controls are always on the right.
- Inspect sheet placement and inspectors independently; bars do not use one universal axis across all containers.

See Apple's [bar session](https://developer.apple.com/videos/play/tech-talks/111462/) and [axis behavior](https://developer.apple.com/documentation/swiftui/toolbaritemaxisbehavior). Use [SwiftUI 27 adoption](../../swiftui-27-adoption/SKILL.md) for shared toolbar availability and earlier migration guidance.
