# Duo verification matrix

Use this as an app-specific acceptance plan. A skill-package compile check does not execute these scenarios.

| Scenario | Evidence to collect |
|---|---|
| Closed outer display, both orientations | Reachable navigation, accurate independent safe-area insets, readable sheets |
| Inner display, tall and wide | Appropriate columns, stable selection, no device-idiom layout assumption |
| Open / close / rotate during editing | Draft, focus, selection, scroll, and presentation preserved |
| Partially folded, book and seated poses | Interactive targets avoid active divisions; media/controls remain usable |
| Split View on each side | Correct control edge and scene-local geometry; no accidental shared navigation state |
| Pinned picture-in-picture / keyboard | Content survives reduced height, focus remains visible |
| Active inner camera | Occlusion changes trigger layout without hiding essential controls |
| RTL, long translations, accessibility sizes | No double mirroring, clipped labels, or unreachable overflow actions |
| VoiceOver and hardware keyboard | Logical traversal and labels after every layout transition |
| Older iPhone / minimum supported OS | Working fallback without hinge, accessory, or 27.1-only API access |
| Camera / accessory on hardware | Direction, rotation, mirroring, capture output, and accessory availability verified |

Use Device Hub's pose controls with the Duo runtime. Record Xcode build, SDK, runtime, and app build alongside observations. The [27.1 beta notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes) currently identify unavailable StandBy and most app-extension debugging in that runtime. A simulator limitation is not an app failure or a passing test.

## Distribution check

As checked September 23, Apple's [screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications) list Duo outer images at 1398 × 2034 and inner images at 2007 × 2853, including transposed landscape sizes. That page says asset upload support will arrive later in the year. Recheck before producing or uploading a release asset set; dimensions alone do not establish that App Store Connect accepts it.

Report untested cases explicitly. Do not label a migration Duo-ready based only on type-checking or a static screenshot.
