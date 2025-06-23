from openai import OpenAI
import os
import configparser

# ── config & client ────────────────────────────────────────────────────────────
config = configparser.ConfigParser()
config.read("config.ini")

os.environ["OPENAI_API_KEY"] = config["DEFAULT"]["OPENAI_API_KEY"]
input_file  = config["DEFAULT"]["INPUT_DIRECTORY"]
output_file = config["DEFAULT"]["OUTPUT_DIRECTORY"]

client = OpenAI()

PROMPT = """For the provided name, which may be not English of origin, generate an
alternative spelling so that when read by an average English speaker it sounds
close to the original. Do not generate spellings with hyphens/dashes (e.g.
Dee-eh-go); instead give equivalents without any hyphens (e.g. Deehego).  
Do not add explanations.  
Try to provide at least 3 alternative spellings if possible and list them
separated by commas.

{}
"""

# ── helpers ────────────────────────────────────────────────────────────────────
def rewrite_one_word(name: str) -> set[str]:
    print(f"\tLLM request for {name}", flush=True)

    temperatures = (0.0, 0.33, 0.66)
    responses = []
    for t in temperatures:
        resp = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": PROMPT.format(name)}],
            temperature=t,
        ).choices[0].message.content
        print(f"\tLLM response @T={t}: {resp}", flush=True)
        responses.append(resp)

    combined = ",".join(responses)
    return {
        r.strip().replace(".", "")
        for r in combined.split(",")
        if "-" not in r and r.strip()
    }


def rewrite_one_full_name(full_name: str) -> list[set[str]]:
    parts = full_name.split()
    rewritten = []
    for part in parts:
        s = rewrite_one_word(part)
        s.add(part)          # keep the original spelling
        rewritten.append(s)
    print(f"\tFull name rewrite list: {rewritten}", flush=True)
    return rewritten


# ── load all names ─────────────────────────────────────────────────────────────
persons: dict[str, list[set[str]]] = {}

if input_file.endswith(".txt"):
    with open(input_file, "r", encoding="utf-8") as fh:
        names = [line.strip() for line in fh if line.strip()]

    for name in names:                       # ← removed the accidental “break”
        print(f"Processing {name}…", flush=True)
        persons[name] = rewrite_one_full_name(name)

# ── write nicely-formatted YAML ────────────────────────────────────────────────
with open(output_file, "w", encoding="utf-8") as fh:
    for full_name, variants in persons.items():
        fh.write(f"{full_name}:\n")
        for alt_set in variants:
            # convert set → list so order is deterministic; sorted() is optional
            alt_list = ", ".join(sorted(alt_set))
            fh.write(f"  - [{alt_list}]\n")

print(f"✅  Finished. YAML saved to {output_file}")
