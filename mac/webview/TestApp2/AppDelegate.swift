import Cocoa
import SwiftUI

@NSApplicationMain
class AppDelegate: NSObject, NSApplicationDelegate {
    var window: NSWindow!
    var windowController: WindowController!

    func applicationDidFinishLaunching(_ notification: Notification) {
        // Create the window controller and initialize the window
        windowController = WindowController()
        window = windowController.window
        
        // Show the window
        windowController.showWindow(self)
    }

    func applicationWillTerminate(_ notification: Notification) {
        // Insert code here to tear down your application
    }
}

