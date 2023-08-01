import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

input_dir = r'D:\meeting-audio\\'
output_dir = r'D:\meeting-audio-processed\\'

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

print("Scanning directory for audio files...", flush=True)
for filename in os.listdir(input_dir):
    if filename.endswith(".m4a"):
        audio_file_path = os.path.join(input_dir, filename)

        # Check if output files for this input file already exist
        base_output_file_path = os.path.join(output_dir, os.path.splitext(filename)[0])
        if len([f for f in os.listdir(output_dir) if f.startswith(os.path.splitext(filename)[0])]) > 0:
            print(f"Output files for {filename} already exist. Skipping...", flush=True)
            continue

        print(f"Processing {filename}...", flush=True)
        audio = AudioSegment.from_file(audio_file_path, "m4a")

        # Detect silences longer than 5 seconds. Parameters are tuned according to the problem
        print(f"Detecting silences in the audio file {audio.duration_seconds} seconds long...", flush=True)
        chunks = split_on_silence(
            audio, 
            min_silence_len = 5000,  # length of silence in ms
            silence_thresh = audio.dBFS - 18,  # silence is anything quieter than this
            keep_silence = 2000,  # leave (or remove) 2000 ms of silence at beginning and end of the chunks detected
            seek_step=100
        )

        print(f"Found {len(chunks)} non-silent parts.", flush=True)

        # Export each non-silent part
        for i, chunk in enumerate(chunks):
            output_file_path = os.path.join(
                output_dir, 
                f"{os.path.splitext(filename)[0]}-part-{i}.wav"
            )

            # Convert the sample width and frame rate to ensure 16-bit PCM WAV with sample rate of 16kHz
            chunk = chunk.set_frame_rate(16000)
            chunk = chunk.set_sample_width(2) # 2 bytes = 16 bits

            # Save as WAV file
            print(f"Exporting part {i+1} to {output_file_path}...", flush=True)
            chunk.export(output_file_path, format="wav")

print("All done!", flush=True)
