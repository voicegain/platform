#!/usr/bin/env python3
"""
De-annotate transcript
• Input: transcript file with {TAG} annotations
• Output: same text with {TAG} parts removed completely
• Output filename = input_stem + "_deannotated.txt"
"""

import re, argparse
from pathlib import Path

BRACE_PAT = re.compile(r"\{[^}]*\}")

def strip_tags(text: str) -> str:
    return BRACE_PAT.sub("", text)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("infile", type=Path)
    args = ap.parse_args()

    infile = args.infile
    outfile = infile.with_name(infile.stem + "_cleaned" + infile.suffix)

    with infile.open(encoding="utf-8") as fh, outfile.open("w", encoding="utf-8") as out:
        for line in fh:
            out.write(strip_tags(line))

    print(f"✅ Wrote {outfile}")

if __name__ == "__main__":
    main()
