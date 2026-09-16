# From the introduction to implementation

Reviewed 2026-09-15. This is a developer interpretation, not a claim that every consumer capability has an API.

The [MacRumors introduction](https://www.macrumors.com/guide/ios-27-features-to-try-first/) supplies the topics below. Apple's [iOS](https://www.apple.com/os/ios/), [iPadOS](https://www.apple.com/os/ipados/), and [macOS](https://www.apple.com/os/macos/) pages establish product context; developer references establish API support.

| Consumer topic | Development path | Boundary |
|---|---|---|
| Siri conversations, personal context, actions | App Intents, matching App Schemas, indexed entities, view annotations | Expose the app's own authorized content. Siri's personal context is not an API to read other apps' private stores. |
| Visual Intelligence / Camera Siri mode | App Intents discovery where supported; Foundation Models image prompts or Vision for in-app analysis | Camera's Siri mode is a system experience. Verify the exact integration surface; don't invent a Camera Siri API. |
| Write with Siri | System text controls and documented Writing Tools integration; Foundation Models for an app-owned feature | Editing support and generating text within your own app are different integrations. |
| Photos Clean Up, Extend, Reframe | PhotoKit for authorized assets; documented image editing/model APIs for the requested operation | No public invocation API for these exact Photos tools was established in this research. Verify before promising equivalent behavior. |
| Liquid Glass adjustment | Standard SwiftUI/UIKit/AppKit controls and documented materials | Respect system appearance; do not imitate the system slider with a hard-coded blur. |
| Safari generated extensions and page monitoring | Safari Web Extensions / WebKit for a developer-owned extension or browser experience | Consumer generation/Notify Me does not establish an automation API. |
| Home camera intelligence | Existing HomeKit/Matter APIs where they expose the requested data | Home intelligence and subscription access do not imply a third-party API for its summaries. |
| AirPods EQ | Documented audio frameworks for the app's own audio | No system AirPods EQ control API was established here. App audio processing is not an AirPods setting change. |
| Natural-language Shortcuts creation | Well-modeled App Intents with typed inputs, outputs, and entity queries | Make useful composable actions; don't depend on a private Shortcuts-generation interface. |

"Not established" means this skillset did not verify a public API; it is not proof that one can never exist. Search current documentation when one of these areas becomes the actual task.

## Additional platform priorities

Apple's [iOS guide](https://developer.apple.com/wwdc26/guides/ios/), [iPadOS guide](https://developer.apple.com/wwdc26/guides/ipados/), and [macOS guide](https://developer.apple.com/wwdc26/guides/macos/) also cover Core AI, resizable apps, document infrastructure, handwriting, and web/media technologies. The bundled skills cover the core app-development paths. For games, spatial content, media, or specialized hardware, follow the relevant guide to the specific framework rather than loading every skill.

Safari extension work starts with Apple's [Safari Web Extensions documentation](https://developer.apple.com/documentation/safariservices/safari-web-extensions): verify host permissions, extension packaging, messaging, and support on each selected platform. Test actual installed extension behavior, including revoked website access.
