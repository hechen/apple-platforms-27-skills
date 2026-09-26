#!/usr/bin/env bash
set -euo pipefail

skillset_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
xcodebuild -version
for skillset_spec in 'macosx arm64-apple-macos27.0' 'iphoneos arm64-apple-ios27.0'; do
  read -r skillset_sdk skillset_target <<< "$skillset_spec"
  skillset_sdk_path="$(xcrun --sdk "$skillset_sdk" --show-sdk-path)"
  xcrun swiftc -typecheck -sdk "$skillset_sdk_path" -target "$skillset_target" \
    "$skillset_root/tests/Platform27Probe.swift"
  printf 'Type-check passed: %s\n' "$skillset_target"
done

# The iPhone Duo API probe moved to https://github.com/hechen/iphone-duo-skills (scripts/check-sdk.sh there).
