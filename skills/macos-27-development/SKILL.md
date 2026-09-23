---
name: macos-27-development
description: "Implement and migrate native Mac apps for macOS 27, with AppKit and SwiftUI window, menu, toolbar, document, and input behavior. Distinguish native macOS from Catalyst and iPhone Mirroring."
---

# macOS 27 Development

## Establish the target

Confirm native AppKit/SwiftUI versus Catalyst or an iOS app running on Mac. Inspect the supported architectures and deployment target in the actual project; don't delete architecture support based on an OS headline. Read the [macOS 27 guide](https://developer.apple.com/wwdc26/guides/macos/) and [final release notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes).

## Native interaction

- Keep commands and menu validation tied to the focused window's selection and edit state. Verify shortcuts, undo/redo, first responder changes, and toolbar customization.
- Maintain independent navigation/inspector state per window; changes to shared data must still propagate between windows.
- Test narrow resizing, inactive windows, full screen, reopened windows, and sheets. A passing SwiftUI preview does not establish AppKit responder behavior.
- Menu image visibility changed and depends on the SDK used to link the app. Read the final AppKit notes, including later corrections. For genuinely necessary images, inspect `NSMenuItem.preferredImageVisibility`; do not force every icon back on.
- AppKit's `NSRefreshController` and semantic tab roles on toolbar/segmented controls are opt-in tools. Use them only for matching behavior; verify VoiceOver semantics.

## SwiftUI and AppKit boundaries

Use [swiftui-27-adoption](../swiftui-27-adoption/SKILL.md) for the new document protocols and compiler migration. Some mobile toolbar APIs are explicitly unavailable on macOS: use native toolbar placements/customization rather than relying on `#available(macOS 27, *)` to make them valid.

After SDK changes, avoid depending on an undocumented AppKit backing class for a SwiftUI control. Inspect public APIs or bridge an owned AppKit view when its behavior is required.

## Documents and files

Preserve open/save, autosave, undo, existing file formats, security-scoped access, and atomic write behavior. Before replacing document infrastructure, establish a fixture that can open, edit, save, and reopen an existing document. Test Finder-open, New from Template, duplicate windows, a failed save, and conflict handling when those flows exist.

In the new document API, the macOS `newDocument` environment action can accept an in-memory readable document. Check the selected SDK's signature rather than copying a mobile document-launch flow.

## Optional integrations

Siri/Spotlight work belongs in [app-intents-27](../app-intents-27/SKILL.md); in-app model work in [foundation-models-27](../foundation-models-27/SKILL.md). Apple's Mac guide links Safari 27, media, and Spatial Preview APIs; follow those only when requested. None grants arbitrary access to other apps' data.

## September 23 refresh

Consult [dated release updates](../apple-platforms-27/references/release-updates.md) for relevant 27.2 beta and toolchain caveats. Check the exact SDK and runtime before applying a beta workaround.
