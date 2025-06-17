#include "DebugUtils.h"
#include <windows.h>
#include <string>

void DebugOutput(const std::string& msg) {
    std::wstring wmsg(msg.begin(), msg.end());
    OutputDebugString(wmsg.c_str());
}
