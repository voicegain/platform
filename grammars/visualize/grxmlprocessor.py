import xml.etree.ElementTree as ET
import re
from railroad import Diagram, Choice, Sequence, Optional, Terminal, NonTerminal, Skip, Comment



def find_grammar_name(root):
    return root.attrib.get('version')

def find_public_rule(root, ns):
    rules = root.findall('.//rule', ns)
    public_rule = {}
    for rule in rules:
        if rule.attrib.get('scope') == 'public':
            rule_id = rule.attrib.get('id')
            public_rule[f"<{rule_id}>"] = rule_to_string(rule, ns)
    if not public_rule:
        return "No public rule found"
    return public_rule

def extract_rules(xml_string):
    def parse_grxml_from_string(xml_string):
        root = ET.fromstring(xml_string)
        ns = {'': 'http://www.w3.org/2001/06/grammar'}
        return root, ns
    root, ns = parse_grxml_from_string(xml_string)
    rules = extract_non_public_rules(root, ns)
    public_rules = find_public_rule(root, ns)
    if isinstance(public_rules, dict):
        rules.update(public_rules)
    return rules

def extract_non_public_rules(root, ns):
    rules = root.findall('.//rule', ns)
    non_public_rules = {}
    for rule in rules:
        if rule.attrib.get('scope') != 'public':
            rule_id = rule.attrib.get('id')
            non_public_rules[f"<{rule_id}>"] = rule_to_string(rule, ns)
    if not non_public_rules:
        return "No rules found"
    return non_public_rules

def rule_to_string(rule, ns, indent=0):
    def parse_element(element, level):
        spaces = '    ' * level
        if element.tag.endswith('item'):
            if len(element):
                item_content = ' '.join(parse_element(e, level) for e in element)
                return item_content.strip()
            else:
                return element.text.strip() if element.text else ''
        elif element.tag.endswith('one-of'):
            one_of_items = [parse_element(item, level + 1).strip() for item in element.findall('item', ns)]
            return '(' + ' | '.join(one_of_items) + ')'
        elif element.tag.endswith('ruleref'):
            return f"<{element.attrib.get('uri', '').replace('#', '')}>"
        elif element.tag.endswith('tag'):
            return f" !!{element.text.strip()}!!" if element.text else ''
        else:
            return element.text.strip() if element.text else ''

    elements = [parse_element(e, indent) for e in rule]
    return ' '.join(elements)

def remove_text_inside_braces(input_dict):
    pattern = r'\{.*?\}'
    processed_dict = {key: re.sub(pattern, '', value) for key, value in input_dict.items()}
    return processed_dict

def replace_tags_with_exclamations(input_dict):
    pattern = r'\{([^{}]*)\}'
    processed_dict = {key: re.sub(pattern, r'!!\1!!', value) for key, value in input_dict.items()}
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
          #print(diagram)



def grxmlToRailroad(file_name):
  f = open(file_name, "r")
  grxml_content=f.read()
  all_rules = extract_rules(grxml_content)
  createDiagram(all_rules)
