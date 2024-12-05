import os
import pandas as pd
from pydub import AudioSegment

from pydub.utils import make_chunks

def process_audio(csv_file, data_dir):
    # Load the CSV file
    df = pd.read_csv(csv_file)
    
    for index, row in df.iterrows():
        try:
            print(f"Processing row {index + 1}/{len(df)}...", flush=True)
            
            # Construct file paths
            src_file_path = os.path.join(data_dir, row['src_file'])
            audio_file_path = os.path.join(data_dir, row['audio_file'])
            position = int(row['position'])  # Ensure position is an integer
            
            # Validate files exist
            if not os.path.exists(src_file_path) or not os.path.exists(audio_file_path):
                raise FileNotFoundError(f"File not found: {src_file_path} or {audio_file_path}")
            
            # Load the source and audio files
            src_audio = AudioSegment.from_wav(src_file_path)
            audio = AudioSegment.from_wav(audio_file_path)
            
            # Verify sample rate and channels
            if src_audio.frame_rate != 16000 or audio.frame_rate != 16000:
                raise ValueError(f"Sample rates must be 16 kHz: {src_file_path} ({src_audio.frame_rate} Hz) and {audio_file_path} ({audio.frame_rate} Hz)")
            if src_audio.channels != 1 or audio.channels != 1:
                raise ValueError(f"Both files must be mono: {src_file_path} has {src_audio.channels} channels, {audio_file_path} has {audio.channels} channels")
            
            # Validate position
            if position < 0 or position > len(src_audio):
                raise ValueError(f"Position {position} is out of bounds for {src_file_path} (length: {len(src_audio)} ms)")
            
            # Insert a silence gap into the right channel at "position"
            audio_length = len(audio)
            right_channel = src_audio[:position] + AudioSegment.silent(duration=audio_length) + src_audio[position:]
            
            # Create left channel with the inserted audio
            left_channel = AudioSegment.silent(duration=len(right_channel))
            left_channel = left_channel.overlay(audio, position=position)
            
            # Adjust sample lengths explicitly
            left_samples = left_channel.get_array_of_samples()
            right_samples = right_channel.get_array_of_samples()
            
            # Ensure both arrays are of the same size
            if len(left_samples) < len(right_samples):
                left_samples.extend([0] * (len(right_samples) - len(left_samples)))
            elif len(left_samples) > len(right_samples):
                right_samples.extend([0] * (len(left_samples) - len(right_samples)))
            
            # Convert adjusted arrays back to AudioSegments
            left_channel = AudioSegment(
                data=bytes(left_samples),
                sample_width=left_channel.sample_width,
                frame_rate=left_channel.frame_rate,
                channels=1
            )
            right_channel = AudioSegment(
                data=bytes(right_samples),
                sample_width=right_channel.sample_width,
                frame_rate=right_channel.frame_rate,
                channels=1
            )
            
            # Combine left and right channels into stereo audio
            stereo_audio = AudioSegment.from_mono_audiosegments(left_channel, right_channel)
            
            # Export the output
            output_file_path = os.path.join(data_dir, f"stereo-{row['src_file']}")
            os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
            stereo_audio.export(output_file_path, format="wav")
            print(f"Processed {output_file_path}", flush=True)
        
        except Exception as e:
            print(f"Error processing row {index + 1}: {e}", flush=True)

if __name__ == "__main__":
    csv_file = "./left-channel-insert.csv"  # Replace with your CSV file path
    data_dir = "../data/sutherland-redact"  # Replace with your data directory
    process_audio(csv_file, data_dir)
