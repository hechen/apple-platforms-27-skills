---
name: ipados-27-development
description: "Build and migrate iPad apps for iPadOS 27: resizable scenes, multiwindow state, menus, external displays, keyboard and pointer interaction, and PencilKit handwriting adoption."
---

# iPadOS 27 Development

## Start from the scene

Identify whether the target is a native iPad app or an iPhone app running on iPad. Inspect scene lifecycle, deployment target, and document architecture. Use the [iPadOS 27 developer guide](https://developer.apple.com/wwdc26/guides/ipados/) for feature discovery and the [release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes) for linked-SDK behavior.

## Windows and input

- Treat compact, intermediate, and wide windows as normal states. Derive layouts from container geometry and size classes, including for an iPhone-only target that retains the phone idiom.
- Keep each scene's navigation path, selection, inspector, sheets, and draft ownership separate. Use the authoritative data store for durable content; two windows editing the same item need conflict handling or explicit shared-edit semantics.
- Provide keyboard commands and menu actions with selection-aware enablement. Maintain focus after list changes, inspector toggles, and window activation. Supply discoverable alternatives to gesture-only actions.
- Test pointer interactions, keyboard navigation, touch, drag/drop, and external displays. Do not treat an iPad simulator screenshot as evidence for physical keyboard, Pencil, or external-display behavior.
- Review menu icon visibility and toolbar overflow after linking the new SDK. Never rely on an icon alone to identify a command that the system might hide.

For shared toolbar/document APIs, use [swiftui-27-adoption](../swiftui-27-adoption/SKILL.md). For scene lifecycle and launch checks, use the relevant portions of [ios-27-development](../ios-27-development/SKILL.md).

## External displays

If the app presents noninteractive external content, inspect the 27 release-note change to external scenes. UIKit now uses registered scene accessories; SwiftUI offers `.sceneAccessory` with `ExternalNonInteractiveAccessory`. Verify exact declarations and target availability before implementation. Keep interactive multiwindow support conceptually separate.

## Handwriting when the product needs it

Read [handwriting.md](references/handwriting.md) for PencilKit recognition and persistence. Use PaperKit only when a paper-like annotation surface serves the requested workflow; do not replace a custom editor simply because it is newly available.

## Acceptance

Exercise a real editing flow in two windows, resize both, move focus and selection, background/reopen, and verify the saved result. Add physical-device Pencil and external-display checks only for adopted capabilities. Preserve existing file compatibility when newer ink or recognition data is introduced.
