# Availability and validation

Research date: 2026-09-15. Authoring toolchain observed: Xcode 27.0, build 27A266a, with iPhoneOS, iPhoneSimulator, and macOS 27.0 SDKs. Re-run discovery on the machine performing the implementation.

## Authoritative sources

- [iOS & iPadOS 27 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- [macOS 27 release notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes)
- [Xcode 27 release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes)
- [Xcode support and deployment targets](https://developer.apple.com/support/xcode/)
- [Apple documentation updates](https://developer.apple.com/documentation/updates)

If the documentation HTML is only a JavaScript shell, follow its Markdown link. If the browser reader cannot consume `text/markdown`, fetch that same Apple URL with an HTTP client, or use the documentation JSON representation. A shell page is not evidence that an API is undocumented.

## Per-feature record

Record: desired behavior; public symbol/module; introduced OS per platform; compile-time platform exclusions; deployment fallback; runtime capability/authorization; entitlement or account eligibility; source URL and date; validation performed.

Use `#if os(...)` for APIs explicitly unavailable on another platform, `#if canImport(...)` for module presence, and `#available` for runtime versioning. `canImport` does not prove deployment availability; `#available` cannot make an unavailable platform API legal. iPadOS normally uses the iOS Swift availability annotation.

Classify the change as compiler/SDK behavior, runtime OS behavior, or optional feature adoption. Back-deployed improvements should not force a deployment-target increase. Never treat all WWDC26 features as having identical 27.0 availability.

## Validation scaled to the change

- Compile the actual target for each supported platform and its existing minimum deployment target. A small probe can resolve a symbol question; it is not an app build.
- For UI changes, exercise compact/wide layouts, keyboard focus, accessibility, and state preservation across resize. Record the screen and runtime that were tested.
- For document/persistence changes, reopen the saved artifact; preserve old format compatibility and test cancellation or a failed write.
- For system integrations, execute through the relevant system surface and verify the result in the app.
- For AI, test availability and failure UI independently from model output quality and physical-device performance.

Read release notes for the selected runtime/build. "Resolved issue" entries are historical fixes, not current blockers. Do not accumulate obsolete beta workarounds without a reproduction.
