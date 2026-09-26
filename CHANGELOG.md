# Changelog

## 2.0.0 — 2026-09-25

- Move iPhone Duo guidance to [hechen/iphone-duo-skills](https://github.com/hechen/iphone-duo-skills). Remove `iphone-duo-development`, `tests/iPhoneDuoProbe.swift`, and the `--duo` option of `scripts/check-sdk.sh`. This is a breaking change for anyone who installed or invoked `iphone-duo-development` from this repository; install it from the new repository instead.
- Route the coordinator, iOS, and SwiftUI skills to the external `iphone-duo-development` skill by name and repository URL, and tell agents to ask for that installation rather than improvise Duo APIs.
- Keep the general 27.1 and 27.2 toolchain facts in the dated release review and recheck them against Apple's release notes.
- Replace the README's iPhone Duo section and illustration with a pointer to the new repository, and update counts, installation, sources, image credits, and validation records for the eight remaining skills.

## 1.1.0 — 2026-09-23

- Add `iphone-duo-development` with layout/bar, camera/scene, and verification references.
- Route the existing iOS/coordinator/SwiftUI skills to Duo guidance while retaining older-device compatibility.
- Record Xcode 27.1/27.2 branch differences, JSON project configuration, and relevant iOS/iPadOS/macOS beta notes.
- Add an opt-in iOS 27.1 API compile probe alongside the existing baseline probe.
- Preserve the same portable skill format and installation routes for all supported agents.

## 1.0.0 — 2026-09-15

- Publish eight Apple-platform development skills with primary Apple sources, SDK checks, and multi-agent installation guidance.
