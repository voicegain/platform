import json
import re

from railroad import Diagram, Choice, Sequence, Optional, Terminal, NonTerminal, Skip, Comment


def find_grammar_name(json_string):
    try:
        # Parse JSON
        data = json.loads(json_string)

        # Name
        grammar_name = data.get("grammar", None)

        return grammar_name
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {e}"

def find_public_rule(json_string):
    try:
        # Parse JSON
        data = json.loads(json_string)

        # Public
        public_rule = data.get("public", None)

        if public_rule is None:
            return "No public rule found"

        # Angled Brackets in rule name
        updated_public_rule = {f"<{k}>": v for k, v in public_rule.items()}

        return updated_public_rule
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {e}"

def extract_rules(jjsgf_string):
    def replace_tags_with_exclamations(input_dict):
    # Regular expression to match tags inside curly braces
        pattern = r'\{([^{}]*)\}'
    
        # Create a new dictionary to store the processed strings
        processed_dict = {}
    
        for key, value in input_dict.items():
            #print("a")
            # Replace all occurrences of the pattern with '!!' around the captured group
            processed_value = re.sub(pattern, r'!!\1!!', value)
            # Add the processed value to the new dictionary
            processed_dict[key] = processed_value
    
        return processed_dict
    rules = {}
    rules.update(extract_non_public_rules(jjsgf_string))
    public_rules = find_public_rule(jjsgf_string)
    if isinstance(public_rules, dict):
        rules.update(public_rules)
    
    rules=replace_tags_with_exclamations (rules)
    return rules

def extract_non_public_rules(json_string):
    try:
        # Parse the JSON string
        data = json.loads(json_string)

        # Access the rules section
        rules = data.get("rules", None)

        if rules is None:
            return "No rules found"

        # Update the rules dictionary with angle brackets only in keys
        updated_rules = {f"<{k}>": v for k, v in rules.items()}

        return updated_rules
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {e}"

def remove_text_inside_braces(input_dict):
    # Regular expression to match text inside curly braces
    pattern = r'\{.*?\}'

    # Create a new dictionary to store the processed strings
    processed_dict = {}

    for key, value in input_dict.items():
        # Replace all occurrences of the pattern with an empty string
        processed_value = re.sub(pattern, '', value)
        # Add the processed value to the new dictionary
        processed_dict[key] = processed_value

    return processed_dict



def createDiagram(rules):


  # Define the rules as given, given as a dictionary

  def parse_rule(rule):
      def handle_alternatives(content):
          parts = split_outside_parentheses(content, '|')
          return Choice(0, *map(parse_sequence, parts))

      def handle_optional(content):
          parts = split_outside_parentheses(content, '|')
          if len(parts) > 1:
              return Optional(Choice(0, *map(parse_sequence, parts)), skip=Skip())
          else:
              return Optional(parse_sequence(content), skip=Skip())

      def handle_nonterminal(content):
          return NonTerminal(content)

      def handle_terminal(content):
          return Terminal(content)

      def handle_comment(content):
          return Comment(content)

      def parse_sequence(content):
          parts = split_outside_parentheses(content, ' ')
          return Sequence(*[parse_part(part) for part in parts if part])

      def parse_part(part):
          part = part.strip()
          if part.startswith('!!') and part.endswith('!!'):
              return handle_comment(part[2:-2].strip())
          elif part.startswith('(') and part.endswith(')'):
              return handle_alternatives(part[1:-1])
          elif part.startswith('[') and part.endswith(']'):
              return handle_optional(part[1:-1])
          elif part.startswith('<') and part.endswith('>'):
              rule_name = part
              if rule_name in rules:
                  return parse_rule(rules[rule_name])
              else:
                  return handle_nonterminal(rule_name)
          else:
              return handle_terminal(part)

      def split_outside_parentheses(s, delimiter):
          result = []
          current = []
          depth = 0
          in_nonterminal = False
          i = 0
          while i < len(s):
              char = s[i]
              if char == '<':
                  in_nonterminal = True
                  if current and current[-1] != ' ':
                      current.append(' ')
                  current.append(char)
              elif char == '>':
                  in_nonterminal = False
                  current.append(char)
                  if i + 1 < len(s) and s[i + 1] not in ' >':
                      current.append(' ')
              elif in_nonterminal:
                  current.append(char)
              elif char in '([':
                  depth += 1
                  current.append(char)
              elif char in ')]':
                  depth -= 1
                  current.append(char)
              elif char == delimiter and depth == 0 and not in_nonterminal:
                  result.append(''.join(current).strip())
                  current = []
              else:
                  current.append(char)
              i += 1
          result.append(''.join(current).strip())
          return result

      # Check if the top-level should be handled as a choice
      top_level_parts = split_outside_parentheses(rule, '|')
      if len(top_level_parts) > 1:
          return handle_alternatives(rule)
      else:
          return parse_sequence(rule)

  diagrams = {}

  for key, value in rules.items():
      diagrams[key] = Diagram(parse_rule(value))



  for key, diagram in diagrams.items():
      with open(f'{key[1:-1]}.svg', 'w') as f:
          diagram.writeStandalone(f.write)
         # print(diagram)

def jjsgfToRailroad(file_name):
  f = open(file_name, "r")
  jjsgf=f.read()
  all_rules=extract_rules(jjsgf)
  createDiagram(all_rules)
