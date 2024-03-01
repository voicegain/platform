import logging
import time
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

# Set up basic configuration for logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class FileWithLogging:
    def __init__(self, file_path, mode):
        self.file = open(file_path, mode)
        self.file_path = file_path
        logging.debug(f"File {file_path} opened in {mode} mode.")
    
    def read(self, size=-1):
        logging.debug(f"Attempting to read {size} bytes from {self.file_path}")
        # Simulate reading from a slow stream by introducing a delay and reading only a small chunk of data.
        if(size == -1):
            size = 8096
        chunk_size = size if size < 8096 else 8096  # You can adjust the chunk size as needed
        delay = 0.01  # DELAY in seconds to simulate slow reading
        
        chunk = self.file.read(chunk_size)
        time.sleep(delay)  # Introduce a delay to simulate slow streaming
        
        if chunk:
            logging.debug(f"Read {len(chunk)} bytes from {self.file_path}")
        else:
            logging.debug(f"End of file reached for {self.file_path}")
        return chunk
    
    def write(self, data):
        logging.debug(f"Writing data to {self.file_path}")
        return self.file.write(data)
    
    def close(self):
        logging.debug(f"Closing file {self.file_path}")
        return self.file.close()
    
    # To ensure compatibility with context manager (the "with" statement)
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    
    # To ensure other file methods and properties are accessible
    def __getattr__(self, name):
        return getattr(self.file, name)
    


def upload_file_with_logging(url, file_path, form_field_name='file', file_name="sample.wav", mime_type='audio/wav'):
    with FileWithLogging(file_path, 'rb') as f:
        # Create a MultipartEncoder object
        m = MultipartEncoder(
            fields={form_field_name: (file_name, f, mime_type)},
            boundary="----12345678900987654321----"
        )
        
        # Modify the request to use the MultipartEncoder
        headers = {'Content-Type': m.content_type}
        response = requests.post(url, data=m, headers=headers)
        logging.debug(f"Server responded with: {response.status_code}, {response.text}")

# Example usage
url = 'http://127.0.0.1:8888/upload'
file_path = '../data/pii_redaction/NERs-1685138553912.mp3'
upload_file_with_logging(url, file_path)
