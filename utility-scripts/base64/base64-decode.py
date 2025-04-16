import base64
import sys
import os

# Check if the input file is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python base64-decode.py <input_encoded_file>")
    sys.exit(1)

# Get the input file name from the command-line argument
input_file = sys.argv[1]

# Generate the output file name by prefixing "decoded-" to the input file name
output_file = "decoded-" + os.path.basename(input_file)

print("Reading Base64 string from:", input_file)
with open(input_file, 'r') as file:
    base64_data = file.read().strip()

print("Decoding Base64 data...")
decoded_bytes = base64.b64decode(base64_data)
decoded_string = decoded_bytes.decode('utf-8', errors='replace')

print("Writing decoded text to:", output_file)
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(decoded_string)

print("Decoding complete.")


