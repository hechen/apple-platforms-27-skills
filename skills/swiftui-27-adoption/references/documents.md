# Adopting the document infrastructure

Apple's [SwiftUI 27 session](https://developer.apple.com/videos/play/wwdc2026/269/) and [DocumentGroup documentation](https://developer.apple.com/documentation/swiftui/documentgroup) introduce URL access, asynchronous reading/writing, progress, and observation-aware configuration. Use final declarations for `DocumentReader`, `DocumentWriter`, `ReadableDocument`, `WritableDocument`, and `Document`; do not adapt old `FileDocument` examples by renaming their protocols.

Before migration, record file/package format, supported content types, undo semantics, autosave behavior, security-scoped URL lifetime, external changes, and current large-file performance. Changing document infrastructure need not change the on-disk schema.

Separate model mutation from snapshot creation and asynchronous I/O. Respect the actual actor isolation and `Sendable`/`sending` contracts. Do not silence errors with unchecked sendability on a live mutable document. A snapshot must remain valid while the user continues editing.

Define cancellation, write failures, partial writes, and conflicts explicitly. Preserve the last good document; don't report save success before completion. For package documents, verify incremental writes don't drop unchanged children. Adopt custom creation sources or a template flow only when the product has such a flow, checking platform-specific APIs.

Acceptance fixture: open a previous-version document, edit, undo/redo, save, close, reopen, and compare semantic data plus required assets. Add interrupted-save and external-edit cases where supported. Profile a representative large document before claiming a performance improvement.
