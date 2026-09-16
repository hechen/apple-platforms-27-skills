---
name: foundation-models-27
description: "Implement in-app AI using Foundation Models 27: image prompts, LanguageModel providers, Dynamic Profiles, Private Cloud Compute, tools, context management, and evaluations with explicit availability and privacy boundaries."
---

# Foundation Models 27

## Choose a measured feature

Define the task, expected output, unacceptable failure modes, latency, and data boundary before choosing a model. Keep non-AI editing/search paths usable. Apple's [Foundation Models 27 session](https://developer.apple.com/videos/play/wwdc2026/241/) covers image inputs, model abstraction, profiles, and system tools.

| Requirement | Starting point |
|---|---|
| Supported Apple on-device generation | `SystemLanguageModel` with runtime availability checks |
| More reasoning/context with Apple-hosted processing | Eligible `PrivateCloudComputeLanguageModel`; read [pcc-and-evaluation.md](references/pcc-and-evaluation.md) |
| An existing third-party model requirement | A verified `LanguageModel` provider, explicit auth/billing and data policy |
| Your own neural model execution | [core-ai-27](../core-ai-27/SKILL.md) |
| Siri acting on the app | [app-intents-27](../app-intents-27/SKILL.md), not an in-app chat model |

Do not silently switch an on-device feature to a network model. Record which fields, attachments, and transcript portions can leave the device. Availability of OS 27 alone does not establish model readiness, language support, entitlement approval, or quota.

## Sessions, structured output, and tools

- Use typed generated output where the app needs structured data, then apply semantic validation before persistence. Streaming partial values are preview state, not final saved records.
- Give each conversation/task a defined session lifetime. Serialize requests deliberately; a reentrant Swift actor around an `await` does not by itself prevent overlapping generations. Handle cancellation and stale responses.
- Read model context capacity and token counts from supported APIs. Include instructions, schemas, tools, images, transcript, and output budget; do not hard-code a single token limit for all providers.
- Keep retrieved documents and user text as untrusted content. Tools should expose narrow typed operations with app-side authorization and validation.
- For image inputs, budget image size and latency, retain useful detail, and test unreadable/ambiguous input. Vision OCR/barcode tools may improve extraction; model descriptions are not measured facts.

## Dynamic Profiles

Use `LanguageModelSession.DynamicProfile` only when a session needs to change instructions, tools, or models. A profile resolves to one active configuration; it is not automatic permission to share the transcript with any provider. Keep transitions explicit in the product's data policy. For a simple single-task feature, a conventional session is easier to reason about.

Check the selected SDK and the [Foundation Models documentation](https://developer.apple.com/documentation/foundationmodels) before using new overloads or provider packages. Preserve supported older-OS paths without pretending unavailable features exist.

## Validate

Evaluate representative and adversarial inputs, tool calls, refusal, context overflow, offline behavior, cancellation, and model unavailability. Test on physical target hardware for latency, memory, and readiness. Report output quality separately from compilation and UI acceptance.
