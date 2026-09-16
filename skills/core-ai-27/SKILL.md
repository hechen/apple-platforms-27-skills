---
name: core-ai-27
description: "Deploy and profile custom neural models with Apple Core AI on iOS 27, iPadOS 27, and macOS 27, including aimodel assets, specialization, inference descriptors, caching, and background execution constraints."
---

# Core AI 27

## Choose the correct layer

Use Core AI when the app supplies a neural model and needs on-device execution. For Apple's language model/session features use [foundation-models-27](../foundation-models-27/SKILL.md). Preserve an existing Core ML path where it meets requirements, especially for older deployment targets or non-neural model types; do not migrate solely for the new framework name.

Read Apple's [Core AI overview](https://developer.apple.com/documentation/coreai) and [integration guide](https://developer.apple.com/documentation/coreai/integrating-on-device-ai-models-in-your-app-with-core-ai). The 27 framework uses `.aimodel` source assets, `AIModel`/`AIModelAsset`, and named inference functions. Verify APIs in the actual SDK, including any Clang headers/re-exported module if a Swift interface has no declaration.

## Integration workflow

1. Record source model version/license, expected inputs/outputs, preprocessing, accuracy fixtures, supported hardware, memory, and latency budget.
2. Prepare/convert the model with current Apple tooling. Retain an unoptimized reference and compare numeric outputs/task quality before compression or specialization tuning.
3. Configure Xcode target membership and the Metal toolchain required to build model assets. Preserve a previous known-good model while evaluating updates.
4. Load and specialize asynchronously. Treat function loading as potentially expensive and handle a missing named function explicitly. Verify input names, shapes, scalar types, and image formats from the inference descriptor.
5. Separate specialization caches from user documents. Define download integrity, storage limits, eviction, and update rollback when models are downloaded.
6. Profile cold specialization, warm inference, peak app memory, energy, and cancellation on physical devices. CPU/GPU/Neural Engine selection must be measured rather than assumed.

## Backgrounding

The [iOS 27 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes) describe Neural Engine background restrictions and the `com.apple.developer.background-tasks.continued-processing.inference` entitlement. A background task or an unstructured Swift task is not permission for unlimited inference. Check entitlement eligibility and scheduler support, handle expiration/cancellation, and keep a foreground path when background access is unavailable.

## Acceptance

Test corrupt/missing assets, unsupported shapes, incorrect image orientation, specialization failure, cancellation, cache invalidation, thermal pressure, and model update rollback for the adopted delivery path. Compare output quality against fixed fixtures after every conversion/precision change. Report simulator control-flow checks separately from physical-device inference and performance.
