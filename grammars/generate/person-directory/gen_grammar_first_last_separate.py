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

PROMPT = """For the provided name, which may be not English of origin, generate an alternative spelling, so that when read by an average English speaker it sounds close to the original. 
Do not generate alternative spellings with hyphens/dashes, so not like e.g. Dee-eh-go, but instead generate equivalents without any hyphens, e.g. Deehego.
Do not add explanations. 
Try to provide at least 3 alternative spellings if possible, and list them separated by commas.

{}
"""

def rewrite_one_word(name):
    print(f"\tLLM request for {name}", flush=True)
    
    # First request
    response1 = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": PROMPT.format(name)
            }
        ],
        temperature=0.0
    )
    resp1 = response1.choices[0].message.content
    print(f"\tLLM response 1: {resp1}", flush=True)
    
    # Second request
    response2 = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": PROMPT.format(name)
            }
        ],
        temperature=0.33
    )
    resp2 = response2.choices[0].message.content
    print(f"\tLLM response 2: {resp2}", flush=True)

    # Third request
    response3 = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": PROMPT.format(name)
            }
        ],
        temperature=0.66
    )
    resp3 = response3.choices[0].message.content
    print(f"\tLLM response 3: {resp3}", flush=True)

    # Combine results
    combined_responses = resp1 + "," + resp2 + "," + resp3
    result = set([r.strip().replace(".", "") for r in combined_responses.split(",") if "-" not in r])
    print(f"\tLLM combined response: {result}", flush=True)
    return result

def rewrite_one_full_name(full_name):
    full_name_split = full_name.split()
    full_name_rewrite_list = []

    for name in full_name_split:
        name_rewrite_set = rewrite_one_word(name)
        name_rewrite_set.add(name)
        full_name_rewrite_list.append(name_rewrite_set)

    return full_name_rewrite_list

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
grammar_jsgf = "#JSGF V1.0;\n\ngrammar person_directory;\n\n"
grammar_jsgf += "#JSGF V1.0 ISO 639-1:en-US;\n"
grammar_jsgf += "tag-format: semantics/1.0;\n\n"
private_rules = []
for name, data in persons.items():
    rule_name = name.lower().replace(" ", "_")
    rewrites = " ".join([
        f"(/0.66/({original}) | /0.33/(" + " | ".join(rewrite_set - {original}) + "))"
        for original, rewrite_set in zip(name.split(), data["rewrites"])
    ])
    grammar_jsgf += f"<{rule_name}> = ({rewrites}) {{ out.name=\"{name}\"; out.ext=\"{data['extension']}\" }};\n"
    private_rules.append(f"<{rule_name}>")

grammar_jsgf += "\npublic <person> = " + " | ".join([f"({rule} {{ name=rules.{rule[1:-1]}.name; ext=rules.{rule[1:-1]}.ext; }})" for rule in private_rules]) + ";"

print(grammar_jsgf, flush=True)

# Generate GRXML grammar
grammar_grxml = '<?xml version="1.0" encoding="UTF-8"?>\n'
grammar_grxml += '<grammar version="1.0" xml:lang="en-US" root="person" xmlns="http://www.w3.org/2001/06/grammar" tag-format="semantics/1.0">\n'
for name, data in persons.items():
    rule_name = name.lower().replace(" ", "_")
    rewrites = " ".join([
        f'<one-of><item weight="0.66">{original}</item><item weight="0.33">' + "</item><item weight=\"0.33\">".join(rewrite_set - {original}) + "</item></one-of>"
        for original, rewrite_set in zip(name.split(), data["rewrites"])
    ])
    grammar_grxml += f'<rule id="{rule_name}"><item>{rewrites}<tag>out.name="{name}"; out.ext="{data["extension"]}";</tag></item></rule>\n'

grammar_grxml += '<rule id="person"><one-of>'
for rule_name in private_rules:
    grammar_grxml += f'<item><ruleref uri="#{rule_name[1:-1]}"/><tag>out.name=rules.{rule_name[1:-1]}.name; out.ext=rules.{rule_name[1:-1]}.ext;</tag></item>'
grammar_grxml += '</one-of></rule>\n'
grammar_grxml += '</grammar>'

print(grammar_grxml, flush=True)

