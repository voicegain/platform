from collections import defaultdict
import re
import json
import copy


def generateBaseGrammar(sentences):


  class TreeNode:
      def __init__(self):
          self.children = defaultdict(TreeNode)
          self.is_end = False

  def add_sentence(root, sentence):
      node = root
      for word in sentence.split():
          node = node.children[word]
      node.is_end = True

  def find_common_suffix(branches):
      split_branches = [branch.split() for branch in branches]
      reversed_branches = list(zip(*[reversed(branch) for branch in split_branches]))

      common_suffix = []
      for words in reversed_branches:
          if len(set(words)) == 1:
              common_suffix.append(words[0])
          else:
              break
      common_suffix.reverse()

      common_length = len(common_suffix)
      stripped_branches = [' '.join(branch.split()[:-common_length]) if common_length > 0 else branch for branch in branches]

      return common_suffix, stripped_branches

  def generate_grammar(node):
      if not node.children:
          return ""

      branches = []
      for word, child in node.children.items():
          sub_grammar = generate_grammar(child)
          if sub_grammar:
              branch = f"{word} {sub_grammar}".strip()
          else:
              branch = word
          branches.append(branch)

      common_suffix, stripped_branches = find_common_suffix(branches)
      if common_suffix:
          common_suffix_str = ' '.join(common_suffix)
          branches = stripped_branches

      if len(branches) == 1:
          combined_branch = branches[0]
      else:
          combined_branch = "(" + " | ".join(branches) + ")"

      if common_suffix:
          combined_branch += " " + common_suffix_str

      # Handle optional elements in brackets for more compact grammar
      if len(branches) == 2 and branches[0] == '':
          combined_branch = f"[{branches[1]}]" + " " + common_suffix_str

      return combined_branch

  def sentences_to_grammar(sentences):
      root = TreeNode()
      for sentence in sentences:
          add_sentence(root, sentence)

      return generate_grammar(root)

  
  grammar = sentences_to_grammar(sentences)
  return grammar


def get_jjsgf(grammar):
  def generate_rule_name(base_name, count):
    return f"{base_name}_{count}"

  def process_grammar(grammar):
      rule_counter = 1
      rules = {}
      main_rule_components = []

      # Regular expressions for detecting optional elements and alternatives
      optional_pattern = re.compile(r'\[([^\[\]]+)\]')
      alternative_pattern = re.compile(r'\(([^\(\)]+)\)')
      or_pattern = re.compile(r'([^|]+)')

      def process_alternatives(alternatives):
          nonlocal rule_counter
          local_rules = []
          for alt in alternatives:
              rule_name = generate_rule_name("rule", rule_counter)
              rule_counter += 1
              rules[rule_name] = alt.strip()
              local_rules.append(f"<{rule_name}>")
          return local_rules

      def recursive_process(grammar_segment):
          nonlocal rule_counter
          while True:
              match = alternative_pattern.search(grammar_segment)
              if not match:
                  break
              alt_text = match.group(1)
              local_rules = process_alternatives(or_pattern.findall(alt_text))
              rule_name = generate_rule_name("rule", rule_counter)
              rule_counter += 1
              rules[rule_name] = f"({' | '.join(local_rules)})"
              grammar_segment = grammar_segment.replace(f"({alt_text})", f"<{rule_name}>", 1)
          return grammar_segment

      # Process the entire grammar recursively
      grammar = recursive_process(grammar)

      # Handle remaining | elements in the main grammar
      if "|" in grammar:
          main_rule_components.extend(process_alternatives(or_pattern.findall(grammar)))
      else:
          main_rule_components.append(grammar.strip())

      main_rule = f"{' | '.join(main_rule_components)}"

      return rules, main_rule

  def generate_jjsgf(rules, main_rule):
      jjsgf = {
          "type": "JJSGF",
          "parameters": {
              "tag-format": "semantics/1.0"
          },
          "grammar": "com.acme.command",
          "public": {
              "main_rule": f"{main_rule}"
          },
          "rules": {}
      }
      for rule_name, rule_content in rules.items():
          jjsgf["rules"][rule_name] = rule_content
      return json.dumps(jjsgf, indent=3)
  rules, main_rule = process_grammar(grammar)
  return generate_jjsgf(rules, main_rule)  




def fix_jjsgf(jjsgf):
  def find_duplicate_rules(rules):
    """Find duplicate rules and return a mapping from old rule names to new rule names."""
    rule_map = {}
    reverse_map = {}
    for rule_name, rule_value in rules.items():
        if rule_value in reverse_map:
            rule_map[rule_name] = reverse_map[rule_value]
        else:
            reverse_map[rule_value] = rule_name
            rule_map[rule_name] = rule_name
    return rule_map

  def replace_rule_references(rules, rule_map):
      """Replace rule references in the rules with their merged counterparts."""
      new_rules = {}
      for rule_name, rule_value in rules.items():
          new_value = rule_value
          for old_rule, new_rule in rule_map.items():
              if old_rule != new_rule:
                  new_value = new_value.replace(f"<{old_rule}>", f"<{new_rule}>")
          new_rules[rule_map[rule_name]] = new_value
      return new_rules

  def merge_duplicate_rules(grammar):
      """Merge duplicate rules in the JJSGF grammar recursively."""
      rules = grammar["rules"]
      previous_rules = None

      while rules != previous_rules:
          previous_rules = rules.copy()
          rule_map = find_duplicate_rules(rules)
          if not any(old != new for old, new in rule_map.items()):
              break  # No more changes can be made
          rules = replace_rule_references(rules, rule_map)

      grammar["rules"] = rules
      return grammar
  def find_common_endings(rules):
    endings = defaultdict(list)
    for rule_name, rule_body in rules.items():
        ending = rule_body.split()[-2:]
        ending = ' '.join(ending)
        endings[ending].append(rule_name)
    return {k: v for k, v in endings.items() if len(v) > 1}

  def update_grammar_with_common_endings(grammar):
      rules = grammar["rules"]
      common_endings = find_common_endings(rules)

      rule_counter = max(int(re.search(r'\d+', rule).group()) for rule in rules.keys()) + 1

      for ending, rule_names in common_endings.items():
          # Find the rule(s) where these rules are OR-ed together
          for rule_name, rule_body in rules.items():
              if all(f"<{rn}>" in rule_body for rn in rule_names):
                  # Create new combined rule
                  new_rule_name = f"rule_{rule_counter}"
                  combined_rules = " | ".join([rules[rn].rsplit(' ', 2)[0] for rn in rule_names])
                  new_rule_body = f"({combined_rules}) {ending}"
                  rules[new_rule_name] = new_rule_body

                  # Update the original rule to use the new combined rule
                  for rn in rule_names:
                      rule_body = rule_body.replace(f"<{rn}> | ", "").replace(f" | <{rn}>", "").replace(f"<{rn}>", "")
                  rule_body = rule_body.replace("  ", " ")
                  if rule_body.endswith(" |"):
                      rule_body = rule_body[:-2]
                  elif rule_body.startswith("| "):
                      rule_body = rule_body[2:]
                  rule_body = rule_body.strip(" ()")
                  rule_body = f"({rule_body} | <{new_rule_name}>)"
                  rules[rule_name] = rule_body

                  rule_counter += 1
                  break

      return grammar

  # Parse the JSON string
  grammar = json.loads(jjsgf)

  grammar=merge_duplicate_rules(grammar)


  prevGrammar=copy.copy(grammar)

  while True:
    prevGrammar=copy.copy(grammar)
    grammar = update_grammar_with_common_endings(grammar)
    grammar=merge_duplicate_rules(grammar)
    if (prevGrammar==grammar):
      break



  # Convert the updated grammar back to a JSON string
  updated_jjsgf = json.dumps(grammar, indent=3)

  return updated_jjsgf

def sentences_to_jjsgf_grammar(sentences):
  grammar=generateBaseGrammar(sentences)
  jjsgf=get_jjsgf(grammar)
  return fix_jjsgf(jjsgf)

