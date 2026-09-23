# Camera and scene accessories

Evidence refreshed September 23, 2026. Physical-device capture validation remains necessary.

## Choose camera ownership deliberately

For ordinary front capture, the virtual front camera follows the active display. Camera-centric apps can select the physical inner/outer cameras, but then own switching and capability differences. Do not assume camera `position` expresses its current direction relative to the preview.

`AVCaptureDeviceDirectionCoordinator` is in **AVKit**. Retain it for the preview view's lifetime and use one per relevant view. Its initial map can be empty until the first callback. The callback runs on the main actor: hand its Sendable descriptors to the actor owning capture, then resolve and configure devices there. Handle stale descriptors and failed resolution. Prefer replacing one input when simultaneous capture has no product requirement.

When switching, mask stale preview frames until new frames arrive. Derive preview mirroring from direction; disable automatic mirroring before applying a manual override. Reapply after replacing an input, and recreate the rotation coordinator for the selected device. Verify recorded media separately from preview appearance. See Apple's [camera-direction guide](https://developer.apple.com/documentation/avkit/choosing-a-camera-by-the-direction-it-faces).

## Add optional outer-display capture content

Use SwiftUI `sceneAccessory` with `CameraCaptureAccessory`, or UIKit `UISceneAccessory.cameraCapture(sceneConfiguration:)` and registration on the capture controller. Keep essential controls on the main interface. The system decides whether to present the accessory; registration is not proof of visibility.

Share the existing observable capture model. Keep availability separate from the person's enable/disable preference, and preserve state outside transient accessory views. In UIKit, retain the registration and unregister when the feature ends; don't invent a scene-manifest entry for this accessory role.

Exercise capture stopping, backgrounding, navigation away, closing the device, another registration taking precedence, and the user disabling content. Simulator can check view layout; camera-dependent presentation requires a device. See Apple's [capture-accessory guide](https://developer.apple.com/documentation/avfoundation/registering-a-camera-capture-accessory-on-iphone-duo).

`ExternalNonInteractiveAccessory` serves a different role from `CameraCaptureAccessory`. Do not use a noninteractive external-display API to promise arbitrary interactive UI on both displays. Check [sceneAccessory](https://developer.apple.com/documentation/swiftui/view/sceneaccessory(content:)) and the platform exclusions in the installed SDK.
