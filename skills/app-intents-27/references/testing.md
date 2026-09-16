# AppIntentsTesting acceptance

Use Apple's [Testing your App Intents code](https://developer.apple.com/documentation/appintentstesting/testing-your-app-intents-code) and [WWDC26 testing session](https://developer.apple.com/videos/play/wwdc2026/295/).

Tests live in a UI Testing bundle, with the same signing team as the app. `IntentDefinitions` discovers definitions by bundle identifier and string names; the runner and app are separate processes. Tests use real App Intents infrastructure without needing to click every UI control. Confirm names and parameter types against extracted metadata, not guessed Swift member names.

Cover intent execution/results, query resolution, enum conversion, intent chaining, transferable content, Spotlight results, and visible/selected annotations for the adopted features. Test name collisions, deleted IDs, access revocation, missing inputs, cancellation, and repeated execution where it can cause duplicate writes.

Use isolated test fixtures. Debug-only nondiscoverable setup intents must not ship as a hidden database-reset capability, and fixture cleanup must never clear the user's normal store. A nondiscoverable intent is not itself a security barrier.

Read the final 27 App Intents release notes before changing schemas. `.photos.asset` gained required properties, and `calendar.deleteEvents` was renamed to `calendar.deleteEvent`; migrate only affected code, with the necessary availability boundary.

An index submission is not proof of a searchable result. Wait for observable indexing completion, query it, then update/delete the item and verify the result follows. To validate onscreen context, present known fixtures and inspect `viewAnnotations()` against what is visible and selected. Finish with at least one real user flow on the requested system surface.
