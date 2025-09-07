#!/usr/bin/env python3
"""
Stereo-call builder – regex-only
• Reads  Customer: / Agent:  transcript
• Keyword-aware digit spelling (CVV, secret code, PO box, ZIP+4, etc.)
• Voicegain TTS per line, merges to stereo WAV  (S1→left, S2→right)
"""
"""
python3 call_builder.py filename.txt

replace filename with path to txt file
"""
"""ZIP":   _handle_zip,
    "DIGIT": _handle_digit,
    "CARD": _handle_card,  #credit card
    "SSN": _handle_ssn_grouped,  #groups numbers into (1 2)-(2)-(2 2)
    "SSNDIGIT": _handle_ssn_digit,  #says each digit clearly
    "PHONE": _handle_phone,  #groups into 3-3-4 digit by digit
    "CVV": _handle_cvv,
    "LAST4": _handle_last4, #says as two numbers
    "ZIP4": _handle_zip_dash  #for ZIP+4"""
import re, os, sys, uuid, argparse, requests
from pathlib import Path
from pydub import AudioSegment
import configparser
import array

# ─── Voicegain settings ─────────────────────────────────────────────
API_URL      = "https://console.ascalon.ai/audio-server/public/synthesis"
SAMPLE_RATE  = 8000
SAMPLE_WIDTH = 2
CHANNELS     = 1

# --- TAG-based number handling ---------------------------------------------
# Pattern: <digits and dashes>{TAG}
TAG_PAT = re.compile(r'(\d[\d\-]*?)\{([A-Z4]+)\}')

def _spell_digits(digits: str) -> str:
    """Return the digits as space-separated single numbers (’7 6 1 6 2’)."""
    return " ".join([d for d in digits if d.isdigit()]) + ", "

def _handle_card(digits: str) -> str:
    print("Handling card number:", digits)
    # strip non-digits (so “1234-1234-…” → “12341234…”)
    nums = [d for d in digits if d.isdigit()]
    # group into 4’s and spell them out with commas between
    chunks = ["".join(nums[i : i+4]) for i in range(0, len(nums), 4)]
    return ", ".join(" ".join(chunk) for chunk in chunks)

def _handle_zip(digits: str) -> str:
    # ZIP codes are always read digit-by-digit
    return _spell_digits(digits)

def _handle_digit(digits: str) -> str:
    # Generic “read each digit” handler
    return _spell_digits(digits)

# Digit-by-digit style:
def _handle_ssn_digit(digits: str) -> str:
    return " ".join([d for d in digits if d.isdigit()])

# Grouped style:
def _handle_ssn_grouped(digits: str) -> str:
        """
        For 123-45-6789 produces:
            "123", "45", "6789"
        ⇒ "123, 45, 6789"
        """
        parts = digits.split('-')
        if len(parts) == 3:
            return _spell_digits(parts[0]) + _spell_digits(parts[1]) + _spell_digits(parts[2])
        # Fallback: try to group by length if no dashes
        nums = [d for d in digits if d.isdigit()]
        if len(nums) == 9:
            group1 = "".join(nums[:3])
            group2 = "".join(nums[3:5])
            group3 = "".join(nums[5:])
            return f"{group1}, {group2}, {group3}"
        return digits

def _handle_phone(digits: str) -> str:
    """
    Spell a US phone number in 3-3-4 groups.
    E.g. "123-456-7890" → "1 2 3, 4 5 6, 7 8 9 0"
    """
    # keep only digits
    nums = [d for d in digits if d.isdigit()]
    # ensure we have at least 10 digits; you could also error or fallback
    if len(nums) < 10:
        return " ".join(nums)
    # take first 10 digits
    area, prefix, line = nums[:3], nums[3:6], nums[6:10]
    # join each group
    groups = [
        " ".join(area),
        " ".join(prefix),
        " ".join(line),
    ]
    # commas between groups for natural pauses
    return ", ".join(groups)

def _handle_cvv(digits: str) -> str:
    """
    Spell out a CVV code digit‐by‐digit.
    E.g. "123" → "1 2 3"
    """
    # strip to just digits and join with spaces
    return " ".join([d for d in digits if d.isdigit()])

def _handle_last4(digits: str) -> str:
    """
    For a 4-digit string, split into two 2-digit numbers and
    return them as whole numbers, comma-separated.
    E.g. "7716" → "77, 16"
    """
    nums = [d for d in digits if d.isdigit()]
    if len(nums) == 4:
        first  = "".join(nums[:2])
        second = "".join(nums[2:])
        # int() drops any leading zero so "07" → "7" (reads "seven")
        return f"{int(first)}, {int(second)}"
    # otherwise leave it unchanged (braces get stripped elsewhere)
    return digits

def _handle_zip_dash(digits: str) -> str:
    """
    Spell out each digit and say “dash” for any hyphen.
    E.g. "76162-1234" → "7 6 1 6 2 dash 1 2 3 4"
    """
    print("Handling ZIP+4:", digits)
    tokens = []
    for ch in digits:
        if ch.isdigit():
            tokens.append(ch)
        elif ch == "-":
            tokens.append("dash")
        # ignore any other chars
    return " ".join(tokens)

# Register all handlers here.  To add a new tag, just drop another entry.
TAG_HANDLERS: dict[str, callable] = {
    "ZIP":   _handle_zip,
    "DIGIT": _handle_digit,
    "CARD": _handle_card,
    "SSN": _handle_ssn_grouped,
    "SSNDIGIT": _handle_ssn_digit,
    "PHONE": _handle_phone,
    "CVV": _handle_cvv,
    "LAST4": _handle_last4,
    "ZIP4": _handle_zip_dash
}

def process_tags(text: str) -> str:
    """
    Replace every   <number>{TAG}   with whatever the TAG demands,
    and strip the braces so nothing weird reaches Voicegain.
    """
    print(f"Processing tags in: {text}")
    def repl(match: re.Match[str]) -> str:
        num, tag = match.groups()
        print(f"Handling {tag}:", num)
        return TAG_HANDLERS.get(tag, lambda x: x)(num)
    # fall back = leave number unchanged
    return TAG_PAT.sub(repl, text)
# ---------------------------------------------------------------------------


def _spell(d: str) -> str:
    return " ".join(d)

# ─── Per-line normaliser (regex only) ───────────────────────────────
PUNCT = '.,?!'

# ─── Byte-accurate silence segment matching another segment length ──
def blank_like(seg: AudioSegment) -> AudioSegment:
    return AudioSegment(
        data=b"\x00" * len(seg.raw_data),
        sample_width=SAMPLE_WIDTH,
        frame_rate=SAMPLE_RATE,
        channels=CHANNELS,
    )

# ─── Voicegain TTS helper ───────────────────────────────────────────
def fetch_tts(ssml_text: str, voice: str) -> AudioSegment:
    print(f"Fetching TTS for voice {voice}: {ssml_text[:60]}...")
    jwt = os.getenv("VG_TOKEN")
    if not jwt:
        ## read from config.ini
        config = configparser.ConfigParser()
        config.read("config.ini")
        jwt = config.get("CLOUD-DEV", "JWT")
    params = {
        "sid": str(uuid.uuid4()),
        "voice": voice,
        "cmd": "speak",
        "dataType": "ssml",
        "format": "wav",
        "data": f"<speak>{ssml_text}</speak>",
    }
    
    # Retry TTS request up to 3 times on failure
    for attempt in range(3):
        try:
            r = requests.get(API_URL, headers={"Authorization": f"Bearer {jwt}"}, params=params)
            if r.status_code != 200 or "audio" not in r.headers.get("Content-Type", ""):
                print(f"TTS attempt {attempt + 1} failed: {r.status_code}: {r.text[:120]}")
                if attempt == 2:  # Last attempt
                    sys.exit(f"TTS error {r.status_code}: {r.text[:120]}")
                continue
            
            # Check if response content is valid (should be at least a few hundred bytes for WAV)
            if len(r.content) < 100:
                print(f"TTS attempt {attempt + 1} returned suspiciously small response: {len(r.content)} bytes")
                if attempt == 2:  # Last attempt
                    sys.exit(f"TTS returned invalid response size: {len(r.content)} bytes")
                continue
            
            # Load TTS audio from bytes, letting pydub handle WAV header
            from io import BytesIO
            return AudioSegment.from_file(BytesIO(r.content), format="wav")
            
        except Exception as e:
            print(f"TTS attempt {attempt + 1} failed with exception: {e}")
            if attempt == 2:  # Last attempt
                print(f"Failed text: '{ssml_text}'")
                sys.exit(f"TTS failed after 3 attempts: {e}")
            continue

# ─── Build stereo WAV with cross-line guard ─────────────────────────
def build_stereo(dialogue, v1, v2):
    left  = AudioSegment.silent(0, frame_rate=SAMPLE_RATE)
    right = AudioSegment.silent(0, frame_rate=SAMPLE_RATE)
    prev_kw = False

    for spk, raw in dialogue:
        # If no text, generate 1 second of silence
        if not raw.strip():
            seg = AudioSegment.silent(duration=1000, frame_rate=SAMPLE_RATE)
            seg = seg.set_sample_width(SAMPLE_WIDTH).set_channels(CHANNELS)
        else:
            clean = process_tags(raw)
            seg = fetch_tts(clean, v1 if spk == 1 else v2)
        # Add 500ms silence at the beginning of every speaker turn, matching seg properties
        pre_silence = AudioSegment.silent(duration=500, frame_rate=seg.frame_rate)
        pre_silence = pre_silence.set_sample_width(seg.sample_width).set_channels(seg.channels)
        seg_with_silence = pre_silence + seg
        # For the other channel, generate silence with the same duration and properties as seg_with_silence
        silent_seg = AudioSegment.silent(duration=len(seg_with_silence), frame_rate=seg.frame_rate)
        silent_seg = silent_seg.set_sample_width(seg.sample_width).set_channels(seg.channels)

        if spk == 1:
            left  += seg_with_silence
            right += silent_seg
        else:
            left  += silent_seg
            right += seg_with_silence

    # Pad left and right to the same sample count
    left_samples = len(left.get_array_of_samples())
    right_samples = len(right.get_array_of_samples())
    if left_samples < right_samples:
        pad_samples = right_samples - left_samples
        pad_array = array.array(left.array_type, [0] * pad_samples)
        pad = AudioSegment(
            pad_array,
            frame_rate=left.frame_rate,
            sample_width=left.sample_width,
            channels=left.channels
        )
        left += pad
    elif right_samples < left_samples:
        pad_samples = left_samples - right_samples
        pad_array = array.array(right.array_type, [0] * pad_samples)
        pad = AudioSegment(
            pad_array,
            frame_rate=right.frame_rate,
            sample_width=right.sample_width,
            channels=right.channels
        )
        right += pad
    return AudioSegment.from_mono_audiosegments(left, right)

# ─── Parse "Speaker 1:" / "Speaker 2:" transcript ───────────────────
def parse_dialogue(path: Path):
    #pat = re.compile(r"^\s*Speaker\s*0?([12])\s*[:\-–—]\s*(.*)$", re.I)
    ## we now use Agent: and Customer: instead of Speaker 1: and Speaker 2:
    pat = re.compile(r"^\s*(Agent|Customer)\s*:\s*(.*)$", re.I)

    with path.open(encoding="utf-8") as fh:
        for line in fh:
            m = pat.match(line)
            if m:
                yield 1 if m.group(1) == "Agent" else 2, m.group(2).strip()

# ─── CLI / main ─────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("infile", type=Path)
    ap.add_argument("--voice1", default="emma")
    ap.add_argument("--voice2", default="david")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    dialogue = list(parse_dialogue(args.infile))
    if not dialogue:
        sys.exit("Transcript missing Speaker lines")

    stereo = build_stereo(dialogue, args.voice1, args.voice2)
    # Ensure the audio is exported at 8kHz sample rate
    stereo = stereo.set_frame_rate(SAMPLE_RATE)

    # Append 3 seconds of silence at the end
    silence = AudioSegment.silent(duration=3000, frame_rate=SAMPLE_RATE)
    stereo = stereo + silence

    if args.out:
        out_path = args.out
    else:
        out_path = f"{args.infile.stem}.wav"

    stereo.export(out_path, format="wav")
    print("✅  Wrote", out_path)

if __name__ == "__main__":
    main()
