from openai import OpenAI
import os
import configparser
import csv

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = config['DEFAULT']['OPENAI_API_KEY']
input_file = config['DEFAULT']['INPUT_DIRECTORY']

client = OpenAI()

PROMPT = """Please rewrite the following name so that they sound correct when pronounced by an average English speaker. 
Do not use hyphens or add explanations. 
Try to provide at least 3 pronunciations if possible, and list them separated by commas.

{}
"""

def rewrite_one_word(name):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": PROMPT.format(name)
            }
        ],
        temperature=0
    )
    resp = response.choices[0].message.content
    print(f"\tLLM response: {resp}", flush=True)
    return set([r.strip() for r in resp.split(",") if "-" not in r])

def rewrite_one_full_name(full_name):
    full_name_split = full_name.split()
    full_name_rewrite_list = [""]

    for name in full_name_split:
        new_full_name_rewrite_list = []
        name_rewrite_set = rewrite_one_word(name)
        name_rewrite_set.add(name)
        for i in full_name_rewrite_list:
            for new_n in name_rewrite_set:
                new_full_name_rewrite_list.append(i + " " + new_n)
        full_name_rewrite_list = new_full_name_rewrite_list

    full_name_rewrite_set = set([i.strip() for i in full_name_rewrite_list])
    if full_name in full_name_rewrite_set:
        full_name_rewrite_set.remove(full_name)
    return full_name_rewrite_set

# Read names and extensions from input file
persons = {}
with open(input_file, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        name, extension = row
        print(f"Processing {name}...", flush=True)
        persons[name] = {
            "extension": extension,
            "rewrites": rewrite_one_full_name(name)
        }

# Generate JSGF grammar
grammar = "#JSGF V1.0;\n\ngrammar person_directory;\n\n"
grammar += "#JSGF V1.0 ISO 639-1:en-US;\n"
grammar += "tag-format: semantics/1.0;\n\n"
private_rules = []
for name, data in persons.items():
    rule_name = name.lower().replace(" ", "_")
    rewrites = " | ".join(data["rewrites"])
    grammar += f"<{rule_name}> = ({rewrites}) {{ out=\"{name}\"; ext=\"{data['extension']}\" }};\n"
    private_rules.append(f"<{rule_name}>")

grammar += "\npublic <person> = " + " | ".join(private_rules) + ";"

print(grammar, flush=True)
