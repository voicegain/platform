#include "WaveFileWriter.h"
#include <iostream>

WaveFileWriter::WaveFileWriter(const std::string& filename, WAVEFORMATEX* format)
    : format(format), dataChunkSize(0), fileSize(0) {
    file.open(filename, std::ios::binary);
    if (!file.is_open()) {
        throw std::runtime_error("Failed to open file");
    }

    // Write WAV header placeholders
    file.write("RIFF", 4);
    file.write("\0\0\0\0", 4); // Placeholder for file size
    file.write("WAVE", 4);
    file.write("fmt ", 4);
    uint32_t fmtChunkSize = 16;
    file.write(reinterpret_cast<const char*>(&fmtChunkSize), 4);
    file.write(reinterpret_cast<const char*>(format), sizeof(WAVEFORMATEX));
    file.write("data", 4);
    file.write("\0\0\0\0", 4); // Placeholder for data chunk size
    std::cout << "Header written" << std::endl;
}

WaveFileWriter::~WaveFileWriter() {
    if (file.is_open()) {
        finalize();
    }
}

void WaveFileWriter::writeData(const BYTE* data, size_t size) {
    std::cout << "Writing data of size: " << size << std::endl;
    file.write(reinterpret_cast<const char*>(data), size);
    dataChunkSize += size;
}

void WaveFileWriter::finalize() {
    if (!file.is_open()) return;

    // Update file size
    file.seekp(4, std::ios::beg);
    fileSize = 36 + dataChunkSize;
    file.write(reinterpret_cast<const char*>(&fileSize), 4);
    std::cout << "Final File Size: " << fileSize << std::endl;

    // Update data chunk size
    file.seekp(40, std::ios::beg);
    file.write(reinterpret_cast<const char*>(&dataChunkSize), 4);
    std::cout << "Final Data Chunk Size: " << dataChunkSize << std::endl;

    file.close();
}
