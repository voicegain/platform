#include "WaveFileWriter.h"
#include <iostream>

WaveFileWriter::WaveFileWriter(const std::string& filename)
    : dataChunkSize(0) {
    file.open(filename, std::ios::binary);
    if (!file.is_open()) {
        throw std::runtime_error("Failed to open file");
    }
}

WaveFileWriter::~WaveFileWriter() {
    if (file.is_open()) {
        finalize();
    }
}

void WaveFileWriter::writeData(const uint8_t* data, size_t size) {
    file.write(reinterpret_cast<const char*>(data), size);
    dataChunkSize += size;
}

void WaveFileWriter::finalize() {
    if (!file.is_open()) return;
    file.close();
}
