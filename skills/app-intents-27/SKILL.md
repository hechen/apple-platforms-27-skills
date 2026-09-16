---
name: app-intents-27
description: "Integrate app content and actions with Siri AI on the 27 releases using App Schemas, indexed entities, view annotations, transferable content, and AppIntentsTesting; retain existing Shortcuts compatibility."
---

# App Intents and Siri 27

## Model useful capabilities

Choose a concrete action and entity before adding Siri integration. Record input types, stable identity, query behavior, domain operation, result, authorization, and navigation destination. Reuse the app's existing domain service; do not duplicate business logic inside `perform()`.

Apple's [App Schemas session](https://developer.apple.com/videos/play/wwdc2026/240/) explains Siri's semantic integration. Match a real documented schema domain and implement its required fields. If no schema matches, retain a useful ordinary App Intent/Shortcut without inventing a schema or promising identical Siri support. The selected 27 SDK renames `AssistantSchema` to `AppSchema`; check existing macro use and deprecation diagnostics.

## Entities, search, and onscreen context

- Model authorized content as lightweight entities with persistent IDs. Queries must handle deleted, stale, and inaccessible IDs.
- Use `IndexedEntity` where indexing fits the dataset; maintain create/update/delete lifecycle. A server-backed string query is a valid alternative, but is not equivalent to system semantic indexing.
- Annotate only the content actually represented by a view. For a single entity inspect `appEntityIdentifier`; for custom canvases/multiple entities inspect `appEntityUIElements` and `AppEntityUIElement`, including selection and visible bounds.
- Use documented `Transferable` representations for cross-app content. Where applicable, `IntentValueRepresentation` conveys semantic values such as people and places instead of flattening everything into an image.

See [Providing contextual cues](https://developer.apple.com/documentation/appintents/providing-contextual-cues-to-apple-intelligence-and-siri). These capabilities participate in the 27 experience, but some symbols predate 27; inspect availability individually.

## Execution correctness

Enforce the same authentication, validation, and permission checks as the app UI. Handle cancellation without partial mutation. Make externally retried actions idempotent where feasible and return the actual saved entity/result. Preserve existing shortcut parameter identifiers and intent types unless an explicit migration is planned.

Keep arbitrary model-generated text separate from executable commands. A Siri request must resolve through the typed intent boundary, not shell execution or a general reflection dispatcher.

## Test through the system

Read [testing.md](references/testing.md). Direct unit calls to `perform()` cannot establish intent discovery, system conversion, indexing, or view annotations. After integration tests, exercise the intended Siri/Shortcuts surface and reopen the changed item. Report Siri service/locale/device availability separately from intent correctness.
