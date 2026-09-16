# Sources and scope

## Evidence hierarchy

1. The selected public SDK declarations and a focused compile check establish syntax and platform availability.
2. Current Apple documentation and final release notes establish intended behavior and constraints.
3. Apple WWDC sessions explain design intent and adoption patterns; older examples can differ from the final SDK.
4. Consumer articles identify product topics. They do not establish third-party API access.

Keep disagreements visible. A declaration alone does not prove runtime behavior, a capability entitlement, service eligibility, or performance.

## Apple starting points

- [iOS 27 developer guide](https://developer.apple.com/wwdc26/guides/ios/)
- [iPadOS 27 developer guide](https://developer.apple.com/wwdc26/guides/ipados/)
- [macOS 27 developer guide](https://developer.apple.com/wwdc26/guides/macos/)
- [iOS and iPadOS 27 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- [macOS 27 release notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes)
- [Xcode 27 release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes)

Framework-specific sources are linked next to the guidance inside each skill. The repository contains original instructional summaries, not mirrored Apple manuals or a bundled Apple SDK.

## Consumer feature mapping

The originating [MacRumors article](https://www.macrumors.com/guide/ios-27-features-to-try-first/) covers Siri, visual intelligence, writing, Photos editing, Liquid Glass, Safari, Home, AirPods EQ, and Shortcuts. Read the [feature map](../skills/apple-platforms-27/references/feature-map.md) before treating one of those as a public API request.

For Photos Clean Up/Extend/Reframe, Home intelligence summaries, and system AirPods EQ control, this research did not establish public invocation APIs equivalent to the system experience. This is a scoped research result, not a claim that no future or specialized public API can exist. Recheck when implementing a specific feature.

## Cross-agent format

The core follows the [Agent Skills specification](https://agentskills.io/specification). [Skills CLI](https://github.com/vercel-labs/skills) and [GitHub CLI](https://cli.github.com/manual/gh_skill_install) provide installation across multiple hosts. Format compatibility does not imply identical agent execution or model quality. See [validation](validation.md).

## Research date

The initial review and API snapshot are dated September 15, 2026. Version-sensitive assumptions belong in a dated reference with a source link, not as permanent unconditional rules. Contributions should update evidence when an SDK or service changes.
