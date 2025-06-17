import SwiftUI

struct ContentView: View {
    var body: some View {
        WebView(url: URL(string: "https://demo.voicegain.ai/voicebot")!)
            .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

