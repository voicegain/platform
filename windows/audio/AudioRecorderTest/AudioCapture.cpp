#include "framework.h"
#include "AudioCapture.h"
#include <audioclient.h>
#include <mmdeviceapi.h>
#include <avrt.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
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
    WaveFileWriter waveFileWriter("output.wav", pRenderFormat);

    // Capture loop for 10 seconds
    BYTE* pRenderData;
    BYTE* pCaptureData;
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

            UINT32 renderNumBytes = renderNumFramesAvailable * pRenderFormat->nBlockAlign;
            waveFileWriter.writeData(pRenderData, renderNumBytes);

            hr = pRenderCaptureClient->ReleaseBuffer(renderNumFramesAvailable);
            if (FAILED(hr)) {
                DebugOutput("Failed to release render buffer.\n");
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

            UINT32 captureNumBytes = captureNumFramesAvailable * pCaptureFormat->nBlockAlign;
            waveFileWriter.writeData(pCaptureData, captureNumBytes);

            hr = pCaptureCaptureClient->ReleaseBuffer(captureNumFramesAvailable);
            if (FAILED(hr)) {
                DebugOutput("Failed to release capture buffer.\n");
                break;
            }
        }

        Sleep(10); // Sleep for a short period before checking again
    }

    // Finalize the WAV file
    waveFileWriter.finalize();

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
