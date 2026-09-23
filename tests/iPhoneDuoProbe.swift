import SwiftUI
import UIKit
import AVKit
import AVFoundation

// Syntax/availability probe only; this does not run camera or layout behavior.
@available(iOS 27.1, *)
struct DuoArrangementProbe: View {
    var body: some View {
        ArrangementView {
            Button("Pause", systemImage: "pause") { }
        } secondary: {
            Color.black
        }
        .arrangementViewStyle(.overlay)
        .onHingeChange { _, context in
            _ = context.hinge?.angle
            _ = context.hinge?.status
        }
        .sceneAccessory {
            CameraCaptureAccessory { Text("Capture status") }
                .onAvailabilityChange { _ in }
        }
        .toolbar {
            ToolbarItem { Button("Save", systemImage: "checkmark") { } }
                .axisBehavior(.verticalPreferred)
        }
    }
}

@available(iOS 27.1, *)
func activeDivisions(_ geometry: GeometryProxy) -> [ReservedRegion] {
    geometry.reservedRegions(kind: .division, options: .includeInactive)
        .filter(\.isActive)
}

@available(iOS 27.1, *)
@MainActor
func configureUIKitProbe(_ view: UIView) -> UIArrangementViewController {
    _ = view.reservedRegions(kind: .occlusion).filter(\.isActive)
    view.addInteraction(UIHingeInteraction { _, update in
        _ = update.hinge?.angle
    })
    let controller = UIArrangementViewController()
    controller.setViewController(UIViewController(), for: .primary)
    controller.setViewController(UIViewController(), for: .secondary)
    controller.updateArrangement(.split.axes(.horizontal))
    let item = UIBarButtonItem(title: "Save", style: .plain, target: nil, action: nil)
    item.axisBehavior = .verticalPreferred
    controller.navigationItem.rightBarButtonItem = item
    return controller
}

@available(iOS 27.1, *)
@MainActor
func cameraDirectionProbe(_ preview: UIView) -> AVCaptureDeviceDirectionCoordinator {
    AVCaptureDeviceDirectionCoordinator(
        view: preview,
        deviceTypes: [.builtInOuterUltraWideCamera, .builtInInnerUltraWideCamera]
    ) { directions in
        _ = directions.forwardFacingDeviceDescriptors
        _ = directions.backwardFacingDeviceDescriptors
    }
}
