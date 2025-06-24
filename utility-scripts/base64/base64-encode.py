import base64
import sys
import os

# Check if the input file is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python base64-encode.py <input_file>")
    sys.exit(1)

# Get the input file name from the command-line argument
input_file = sys.argv[1]

# Generate the output file name by prefixing "encoded-" to the input file name
output_file = "encoded-" + os.path.basename(input_file)

print("Reading data from:", input_file)
with open(input_file, 'rb') as file:
    file_data = file.read()

print("Encoding data to Base64...")
encoded_data = base64.b64encode(file_data).decode('ascii')

print("Writing Base64 string to:", output_file)
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(encoded_data)

print("Encoding complete.")


