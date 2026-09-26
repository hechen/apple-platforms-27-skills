# Release update review — September 23, 2026

These are dated findings, not instructions to adopt every beta. Check the exact project toolchain and OS build before acting. The toolchain notes below were rechecked on September 25, 2026.

## Toolchain branches

Xcode 27.1 beta ships the iOS 27.1 SDK; its other platform SDKs stay at 27. iPhone Duo guidance, including its 27.1 APIs and simulator limits, lives in [hechen/iphone-duo-skills](https://github.com/hechen/iphone-duo-skills).

The [Xcode 27.1 beta notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes) identify Catalyst build failures for 27.1-specific APIs. Runtime availability checks do not solve missing declarations: isolate affected code with compile-time platform guards. The notes also describe a separate 27.0 Catalyst deployment setting when the 27.1 iOS target loses its Catalyst destination. Apply this only to the affected configuration, preserving its intended compatibility.

The [Xcode 27.2 beta notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes) direct iPhone Duo work back to Xcode 27.1 beta, so the higher-numbered Xcode is not automatically the right one. They also warn about incorrect 27.1 deployment-target reporting for macOS, watchOS, tvOS, and visionOS, and new-API problems in Catalyst builds. Verify the branch; do not infer platform availability from the numeric version alone.

## Xcode project configuration

Xcode 27.2 introduces a JSON `.xcproj` configuration **inside the existing `.xcodeproj` bundle**. Apple's [format guide](https://developer.apple.com/documentation/xcode/updating-your-xcode-project-configuration-file-format) says Xcode 27 and later can read both formats. Do not rename the outer bundle or hand-convert it by guessing the schema.

Before opting in, check project generators, CI, dependency managers, and scripts that parse `project.pbxproj`. For generated projects, preserve the generator as the authoritative source. Review the format conversion separately, then verify schemes, build settings, signing references, and builds. A skill update does not itself warrant migrating application projects.

## iOS / iPadOS 27.2 beta

The [beta 2 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes) add region-specific ATT prompt requirements and annual re-prompt support. If the app uses tracking, inspect current AppTrackingTransparency documentation for supported APIs and regional rules; do not invent a custom prompt or infer tracking consent from a region.

The notes also record StoreKit testing fixes for clearing transactions/introductory eligibility, storefront updates, and disabled dialogs, plus a remaining subscription-bundle issue. Reproduce StoreKit test failures on the intended SDK/runtime before changing production purchase logic to accommodate a beta test defect.

## macOS 27.2 beta

The [macOS beta 2 notes](https://developer.apple.com/documentation/macos-release-notes/macos-27_2-release-notes) remove `EnablePasteboardPrivacyDeveloperPreview`. Remove reliance on that preview toggle when relevant; exercise real pasteboard access and permission behavior.

The same notes mark the Xcode completion crash fixed, while the Xcode 27.2 notes still list it as known. Record the exact host OS build and reproduction before applying a machine-wide workaround. Treat release-note disagreements as version-specific evidence.

## Scope of this refresh

The fetched iOS/iPadOS 27.0 and macOS 27.0 release-note Markdown matched the September 15 snapshots. This review adds relevant 27.2 beta guidance; it is not an exhaustive audit of every Apple framework. The Duo material it originally included moved to hechen/iphone-duo-skills on September 25. Existing AI/Siri guidance remains subject to per-feature documentation and availability checks.
