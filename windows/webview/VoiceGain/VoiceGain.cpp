#include <windows.h>
#include <wrl.h>
#include <WebView2.h>
#include "config.h" // Include the config header file

using namespace Microsoft::WRL;

ComPtr<ICoreWebView2Controller> webViewController;
ComPtr<ICoreWebView2> webViewWindow;

void InitializeWebView(HWND hwnd)
{
    CreateCoreWebView2EnvironmentWithOptions(
        nullptr, nullptr, nullptr,
        Callback<ICoreWebView2CreateCoreWebView2EnvironmentCompletedHandler>(
            [hwnd](HRESULT result, ICoreWebView2Environment* env) -> HRESULT {
                if (env != nullptr) {
                    env->CreateCoreWebView2Controller(
                        hwnd, Callback<ICoreWebView2CreateCoreWebView2ControllerCompletedHandler>(
                            [hwnd](HRESULT result, ICoreWebView2Controller* controller) -> HRESULT {
                                if (controller != nullptr) {
                                    webViewController = controller;
                                    webViewController->get_CoreWebView2(&webViewWindow);
                                }

                                if (webViewWindow != nullptr) {
                                    ICoreWebView2Settings* Settings;
                                    webViewWindow->get_Settings(&Settings);
                                    Settings->put_IsScriptEnabled(TRUE);
                                    Settings->put_AreDefaultScriptDialogsEnabled(TRUE);
                                    Settings->put_IsWebMessageEnabled(TRUE);

                                    RECT bounds;
                                    GetClientRect(hwnd, &bounds);
                                    webViewController->put_Bounds(bounds);

                                    // Set the zoom level
                                    webViewController->put_ZoomFactor(ZOOM_LEVEL);

                                    // Navigate to the URL
                                    webViewWindow->Navigate(NAVIGATE_URL);
                                }

                                return S_OK;
                            }).Get());
                }
                return S_OK;
            }).Get());
}

LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch (uMsg)
    {
    case WM_CLOSE:
        if (MessageBox(hwnd, L"Are you sure you want to exit?", L"Confirmation", MB_OKCANCEL | MB_ICONQUESTION) == IDOK) {
            DestroyWindow(hwnd);
        }
        return 0; // Prevent the default WM_CLOSE behavior
    case WM_SIZE:
        if (webViewController != nullptr) {
            RECT bounds;
            GetClientRect(hwnd, &bounds);
            webViewController->put_Bounds(bounds);
        }
        break;
    case WM_DESTROY:
        PostQuitMessage(0);
        return 0;
    }
    return DefWindowProc(hwnd, uMsg, wParam, lParam);
}

int APIENTRY wWinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPWSTR lpCmdLine, int nCmdShow)
{
    CoInitialize(NULL);

    const wchar_t CLASS_NAME[] = L"WebView2Sample";

    WNDCLASS wc = { };
    wc.lpfnWndProc = WindowProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = CLASS_NAME;

    RegisterClass(&wc);

    HWND hwnd = CreateWindowEx(
        0,
        CLASS_NAME,
        WINDOW_TITLE,
        WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU,
        CW_USEDEFAULT, CW_USEDEFAULT, WINDOW_WIDTH, WINDOW_HEIGHT,
        NULL,
        NULL,
        hInstance,
        NULL
    );

    if (hwnd == NULL)
    {
        return 0;
    }

    ShowWindow(hwnd, nCmdShow);

    InitializeWebView(hwnd);

    MSG msg = { };
    while (GetMessage(&msg, NULL, 0, 0))
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    CoUninitialize();
    return 0;
}
