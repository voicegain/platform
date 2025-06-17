import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

def split_audio_on_silence(input_file, silence_thresh=-90, min_silence_len=4500, output_prefix="use-case"):
    # Load the audio file
    audio = AudioSegment.from_wav(input_file)
    
    # Split the audio where silence is longer than min_silence_len
    chunks = split_on_silence(audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh)
    
    # Get the directory of the input file
    input_dir = os.path.dirname(input_file)
    
    # Export each chunk as a separate file in the same directory as the input file
    for i, chunk in enumerate(chunks):
        output_file = os.path.join(input_dir, f"{output_prefix}-{i+1:02d}.wav")
        chunk.export(output_file, format="wav")
        print(f"Exported {output_file}")

if __name__ == "__main__":
    input_file = "../data/sutherland-redact/kathy-webex-test-cases-non-redacted-gaps-16k.wav"  # Replace with your input file path
    split_audio_on_silence(input_file)