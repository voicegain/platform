import Cocoa
import SwiftUI

class WindowController: NSWindowController {
    convenience init() {
        self.init(window: nil)
        let contentView = ContentView()
        let window = NSWindow(
            contentRect: NSRect(x: 0, y: 0, width: 10000, height: 10000), // Set initial size here
            styleMask: [.titled, .closable, .resizable, .miniaturizable],
            backing: .buffered, defer: false)
        window.center()
        window.setFrameAutosaveName("Main Window")
        window.contentView = NSHostingView(rootView: contentView)
        self.window = window
    }
    
    override func windowDidLoad() {
        super.windowDidLoad()
        window?.title = "My WebView App" // Set the title of the window
        window?.styleMask.insert(.resizable) // Allow the window to be resizable
    }
}

