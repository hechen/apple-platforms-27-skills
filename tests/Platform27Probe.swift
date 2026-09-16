import SwiftUI
import FoundationModels
import AppIntents
import CoreAI

@available(iOS 27.0, macOS 27.0, *)
struct Platform27Probe: View {
    var body: some View {
        NavigationStack {
            ScrollView { Text("Availability probe") }
                .swipeActionsContainer()
                .asyncImageURLSession(.shared)
                #if os(iOS)
                .toolbar {
                    ToolbarItem(placement: .topBarPinnedTrailing) {
                        Button("Share") { }
                    }
                }
                .toolbarOverflowMenu { Button("Archive") { } }
                .toolbarMinimizationBehavior(.onScrollDown, for: .navigationBar)
                #endif
        }
    }
}

@available(iOS 27.0, macOS 27.0, *)
func acceptDocument<T: Document>(_ value: T) { }

@available(iOS 27.0, macOS 27.0, *)
func acceptLanguageModel<T: LanguageModel>(_ value: T) { }
