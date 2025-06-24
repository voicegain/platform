#pragma once
#include <fstream>
#include <string>
#include <cstdint> // Include for uint8_t

class WaveFileWriter {
public:
    WaveFileWriter(const std::string& filename);
    ~WaveFileWriter();
    void writeData(const uint8_t* data, size_t size);
    void finalize();

private:
    std::ofstream file;
    size_t dataChunkSize;
};
