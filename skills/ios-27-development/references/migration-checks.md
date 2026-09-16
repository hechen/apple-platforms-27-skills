# iPhone migration checks

Use a focused source audit as a starting point, not a bulk replacement:

```sh
rg -n 'UIScreen\.main|userInterfaceIdiom|interfaceOrientation|statusBarOrientation|UIRequiresFullScreen|UIApplicationSceneManifest|UISceneDelegate|UILaunchScreen|UILaunchStoryboardName' .
```

Trace why each match exists. Camera rotation, sensor coordinates, and device-specific capabilities may legitimately need information that layout should not use. Keep domain semantics intact.

## Acceptance cases

1. Cold launch the built app after the SDK upgrade; recover any existing restoration state.
2. Resize through the narrowest supported width, intermediate widths, and a wide landscape-like aspect ratio. Trigger this while editing, presenting a sheet, and scrolling.
3. Use Xcode 27's resizable preview/simulator for fast iteration; separately test actual iPhone Mirroring with a paired Mac and device before claiming Mirroring support.
4. Exercise Dynamic Type, VoiceOver order, safe areas, keyboard appearance/dismissal, and accessible overflow actions.
5. Re-run the core flow on the minimum supported OS when deployment remains below 27.

Games that use `UIRequiresFullScreen` need a deliberate discrete-resize strategy. Do not introduce this flag as a workaround for ordinary app layout defects. See [TN3210](https://developer.apple.com/documentation/technotes/tn3210-optimizing-your-app-for-iphone-mirroring).

For launch metadata, consult [TN3208](https://developer.apple.com/documentation/technotes/tn3208-preparing-your-apps-launch-screen-to-meet-app-store-requirements). Validate the final product, not only project settings.
