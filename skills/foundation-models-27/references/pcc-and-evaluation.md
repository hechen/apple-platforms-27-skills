# Private Cloud Compute and evaluation

Apple's [PCC integration guide](https://developer.apple.com/documentation/foundationmodels/adding-server-side-intelligence-with-private-cloud-compute) documents `PrivateCloudComputeLanguageModel`, runtime availability, daily quota, and reasoning controls. [Accessing PCC](https://developer.apple.com/private-cloud-compute/) defines current eligibility and managed entitlement requirements; verify those before committing a product dependency.

At research time (2026-09-15), Apple's PCC access page requires Small Business Program enrollment, an assigned entitlement, and fewer than two million first-time downloads for any of the developer's apps. If any app exceeds the threshold, or program enrollment ends, Apple describes a six-month migration period after notification. Verify current eligibility rather than interpreting a guide's shorthand as an aggregate download rule. This is conditional access, not unlimited inference for every developer or user.

Inspect `availability` and `quotaUsage`, and handle a quota-limit error during generation even if a preflight check passed. Daily quota exhaustion is different from short-term throttling; do not retry it in a loop. Use known reset information when present, offer an allowed local/manual path, and preserve the user's work. Xcode provides simulated quota states for exercising this UI. PCC requires networking; fallback is a product choice, not permission to transmit to another provider.

Start reasoning at the level the task requires and measure quality versus latency/cost. Keep diagnostic transcripts free of unnecessary private content. Changing profiles/models must respect provider context and modality constraints.

## Evaluation design

Use the [Evaluations framework](https://developer.apple.com/documentation/evaluations) for nondeterministic feature quality alongside deterministic tests of parsing, policy, and persistence. Freeze a small representative dataset before prompt tuning. Evaluate correct results, appropriate abstention, tool choice, invalid tool arguments, privacy boundary adherence, and time-to-useful-output. Avoid judging a prompt on the same cases used to optimize it.

For tools that mutate state, first evaluate with isolated fixtures or a dry-run domain adapter. Test that rejected/partial generations cannot commit a transaction. When changing a model, prompt, tool schema, or OS-provided model version, rerun the relevant dataset and record the environment. A few pleasing responses do not establish feature reliability.
