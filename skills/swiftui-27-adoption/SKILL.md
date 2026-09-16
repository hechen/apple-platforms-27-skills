---
name: swiftui-27-adoption
description: "Adopt SwiftUI changes from Xcode 27 and the 27 OS releases, including State/ContentBuilder migration, toolbar availability, document protocols, reorderable content, and AsyncImage caching."
---

# SwiftUI 27 Adoption

## Evidence before edits

Separate compiler changes, linked-SDK changes, and runtime availability. Keep the app's existing deployment target until a product decision requires otherwise. Read [api-notes.md](references/api-notes.md) for observed declarations and source discrepancies.

## Compiler migration

Use [TN3211](https://developer.apple.com/documentation/technotes/tn3211-resolving-swiftui-source-incompatibilities-for-state-and-contentbuilder) to resolve actual diagnostics. `@State` becomes a macro and result builders consolidate under `ContentBuilder` in Xcode 27. Do not mechanically rewrite all state or builders.

- When initial state comes from an initializer, avoid an inline default that would take precedence; initialize other stored properties before assigning to state.
- Don't stack property wrappers on `@State`. Add explicit initializers where synthesized initializers no longer apply.
- For builder ambiguities, qualify colliding module types or use closure forms of `background`/`overlay` as appropriate. Preserve the intended overload semantics.
- Prefer generic view composition over depending on concrete builder output shapes such as `TupleView` internals.

Lazy state initialization is back-deployed; it does not require raising the deployment target to 27. Test initial state, view identity changes, and observation updates after migration.

## Adopt features selectively

| Need | Implementation direction | Verification |
|---|---|---|
| Adaptive toolbar | Priorities, mobile overflow/pinning, supported minimization behavior | Resize through overflow thresholds; actions remain accessible |
| Document performance | `ReadableDocument`, `WritableDocument`, or combined `Document` | Existing file round trip; cancellation; failed save; large documents |
| Reorder custom layouts | Reorderable items and a reorder container with stable IDs | Move across boundaries, persist order, undo, reopen |
| Swipe actions beyond lists | Supported `swipeActionsContainer` | Gesture arbitration, accessibility alternatives |
| Remote images | HTTP caching and request/session customization | Cache headers, errors, changed resources, account switching |

For documents, read [documents.md](references/documents.md). For all other rows, inspect the exact declaration in the target SDK before coding. A shared SwiftUI module does not imply equal API availability on iOS and macOS.

## Visual acceptance

Standard controls inherit the refined Liquid Glass appearance. Test actual system transparency/contrast preferences, light/dark appearance, toolbar legibility, and inactive windows. Avoid fixed overlays that defeat the system treatment. Check text-selection gestures against custom gestures, and ensure selected tabs remain visible when tab availability changes.
