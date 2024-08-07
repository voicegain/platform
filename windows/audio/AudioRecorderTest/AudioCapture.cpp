#include "framework.h"
#include <audioclient.h>
#include <mmdeviceapi.h>
#include <avrt.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <windows.h>
#include "DebugUtils.h"
#include "WaveFileWriter.h"

void CaptureAudio() {
    DebugOutput("Starting audio capture...\n");

    CoInitialize(NULL);
    IMMDeviceEnumerator* pEnumerator = NULL;
    IMMDevice* pRenderDevice = NULL;
    IMMDevice* pCaptureDevice = NULL;
    IAudioClient* pRenderAudioClient = NULL;
    IAudioClient* pCaptureAudioClient = NULL;
    IAudioCaptureClient* pRenderCaptureClient = NULL;
    IAudioCaptureClient* pCaptureCaptureClient = NULL;

    HRESULT hr;

    hr = CoCreateInstance(__uuidof(MMDeviceEnumerator), NULL, CLSCTX_ALL, __uuidof(IMMDeviceEnumerator), (void**)&pEnumerator);
    if (FAILED(hr)) {
        DebugOutput("Failed to create IMMDeviceEnumerator instance.\n");
        return;
    }

    // Get default render device (computer audio)
    hr = pEnumerator->GetDefaultAudioEndpoint(eRender, eConsole, &pRenderDevice);
    if (FAILED(hr)) {
        DebugOutput("Failed to get default render audio endpoint.\n");
        return;
    }

    hr = pRenderDevice->Activate(__uuidof(IAudioClient), CLSCTX_ALL, NULL, (void**)&pRenderAudioClient);
    if (FAILED(hr)) {
        DebugOutput("Failed to activate render audio client.\n");
        return;
    }

    WAVEFORMATEX* pRenderFormat = NULL;
    hr = pRenderAudioClient->GetMixFormat(&pRenderFormat);
    if (FAILED(hr)) {
        DebugOutput("Failed to get render mix format.\n");
        return;
    }

    hr = pRenderAudioClient->Initialize(AUDCLNT_SHAREMODE_SHARED, AUDCLNT_STREAMFLAGS_LOOPBACK, 10000000, 0, pRenderFormat, NULL);
    if (FAILED(hr)) {
        DebugOutput("Failed to initialize render audio client.\n");
        return;
    }

    hr = pRenderAudioClient->GetService(__uuidof(IAudioCaptureClient), (void**)&pRenderCaptureClient);
    if (FAILED(hr)) {
        DebugOutput("Failed to get render audio capture client service.\n");
        return;
    }

    // Get default capture device (microphone)
    hr = pEnumerator->GetDefaultAudioEndpoint(eCapture, eConsole, &pCaptureDevice);
    if (FAILED(hr)) {
        DebugOutput("Failed to get default capture audio endpoint.\n");
        return;
    }

    hr = pCaptureDevice->Activate(__uuidof(IAudioClient), CLSCTX_ALL, NULL, (void**)&pCaptureAudioClient);
    if (FAILED(hr)) {
        DebugOutput("Failed to activate capture audio client.\n");
        return;
    }

    WAVEFORMATEX* pCaptureFormat = NULL;
    hr = pCaptureAudioClient->GetMixFormat(&pCaptureFormat);
    if (FAILED(hr)) {
        DebugOutput("Failed to get capture mix format.\n");
        return;
    }

    hr = pCaptureAudioClient->Initialize(AUDCLNT_SHAREMODE_SHARED, 0, 10000000, 0, pCaptureFormat, NULL);
    if (FAILED(hr)) {
        DebugOutput("Failed to initialize capture audio client.\n");
        return;
    }

    hr = pCaptureAudioClient->GetService(__uuidof(IAudioCaptureClient), (void**)&pCaptureCaptureClient);
    if (FAILED(hr)) {
        DebugOutput("Failed to get capture audio capture client service.\n");
        return;
    }

    hr = pRenderAudioClient->Start();
    if (FAILED(hr)) {
        DebugOutput("Failed to start render audio client.\n");
        return;
    }

    hr = pCaptureAudioClient->Start();
    if (FAILED(hr)) {
        DebugOutput("Failed to start capture audio client.\n");
        return;
    }

    DebugOutput("Audio clients started.\n");

    // Create WaveFileWriter
    WaveFileWriter fileWriter("output.pcm");

    // Capture loop for 10 seconds
    uint8_t* pRenderData = nullptr;  // Initialize to nullptr
    uint8_t* pCaptureData = nullptr; // Initialize to nullptr
    UINT32 renderNumFramesAvailable;
    UINT32 captureNumFramesAvailable;
    DWORD renderFlags;
    DWORD captureFlags;
    DWORD startTime = GetTickCount();
    DWORD endTime = startTime + 10000; // Capture for 10 seconds

    while (GetTickCount() < endTime) {
        // Capture render audio
        hr = pRenderCaptureClient->GetNextPacketSize(&renderNumFramesAvailable);
        if (FAILED(hr)) {
            DebugOutput("Failed to get render next packet size.\n");
            break;
        }

        if (renderNumFramesAvailable > 0) {
            hr = pRenderCaptureClient->GetBuffer(&pRenderData, &renderNumFramesAvailable, &renderFlags, NULL, NULL);
            if (FAILED(hr)) {
                DebugOutput("Failed to get render buffer.\n");
                break;
            }
        }

        // Capture microphone audio
        hr = pCaptureCaptureClient->GetNextPacketSize(&captureNumFramesAvailable);
        if (FAILED(hr)) {
            DebugOutput("Failed to get capture next packet size.\n");
            break;
        }

        if (captureNumFramesAvailable > 0) {
            hr = pCaptureCaptureClient->GetBuffer(&pCaptureData, &captureNumFramesAvailable, &captureFlags, NULL, NULL);
            if (FAILED(hr)) {
                DebugOutput("Failed to get capture buffer.\n");
                break;
            }
        }

        // Interleave render and capture data and write to PCM file
        UINT32 numFramesToWrite = min(renderNumFramesAvailable, captureNumFramesAvailable);
        UINT32 numBytesToWrite = numFramesToWrite * pRenderFormat->nBlockAlign;
        std::vector<uint8_t> interleavedData(numBytesToWrite * 2); // Ensure this line exists

        for (UINT32 i = 0; i < numFramesToWrite; ++i) {
            memcpy(&interleavedData[i * 4], &pRenderData[i * 2], 2); // Copy render sample
            memcpy(&interleavedData[i * 4 + 2], &pCaptureData[i * 2], 2); // Copy capture sample
        }

        fileWriter.writeData(interleavedData.data(), interleavedData.size());

        if (renderNumFramesAvailable > 0) {
            hr = pRenderCaptureClient->ReleaseBuffer(renderNumFramesAvailable);
            if (FAILED(hr)) {
                DebugOutput("Failed to release render buffer.\n");
                break;
            }
        }

        if (captureNumFramesAvailable > 0) {
            hr = pCaptureCaptureClient->ReleaseBuffer(captureNumFramesAvailable);
            if (FAILED(hr)) {
                DebugOutput("Failed to release capture buffer.\n");
                break;
            }
        }

        Sleep(10); // Sleep for a short period before checking again
    }

    // Finalize the PCM file
    fileWriter.finalize();

    pRenderAudioClient->Stop();
    pCaptureAudioClient->Stop();
    pRenderCaptureClient->Release();
    pCaptureCaptureClient->Release();
    pRenderAudioClient->Release();
    pCaptureAudioClient->Release();
    pRenderDevice->Release();
    pCaptureDevice->Release();
    pEnumerator->Release();
    CoUninitialize();

    DebugOutput("Audio capture finished.\n");
}
