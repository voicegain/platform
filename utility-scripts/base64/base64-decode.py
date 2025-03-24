import base64

# Define input and output file paths.
input_file = 'base64_input.txt'
output_file = 'decoded_output.txt'

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
