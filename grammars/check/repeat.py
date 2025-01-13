import argparse
import xml.etree.ElementTree as ET
import xml.dom.minidom
import sys

def pretty_print_xml_to_file(elem, filename):
    # Convert the ElementTree element to a string
    rough_string = ET.tostring(elem, 'utf-8')
    # Parse the string with xml.dom.minidom
    parsed = xml.dom.minidom.parseString(rough_string)
    # Get the pretty-printed XML as a string
    pretty_xml = parsed.toprettyxml(indent="  ")
    # Write the pretty-printed XML to a file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(pretty_xml)


def analyze_grxml(file_path):
    # Parse the GRXML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    # Namespace used in GRXML
    ns = {'ns': 'http://www.w3.org/2001/06/grammar'}
    # Find all <one-of> elements
    one_of_elements = root.findall('.//ns:one-of', namespaces=ns)
    # List to store results
    repeat_elements = []
    # Iterate over <one-of> elements
    for one_of in one_of_elements:
        print("Processing <one-of> element...")
        # Find all child elements of the <one-of> element
        for child in one_of.findall('./ns:item', namespaces=ns):
            if 'repeat' in child.attrib:
                print(f"  Found <item> with repeat: {child.attrib['repeat']}")
                print("  The <item> in question:")
                print(f'    <{child.tag.split("}")[1]} repeat="{child.attrib['repeat']}">')
                for c in child:
                    if 'ruleref' in c.tag:
                        print(f'      <{c.tag.split("}")[1]} {next(iter(c.attrib))}={c.attrib[next(iter(c.attrib))]}/>')
                    elif c.attrib != {}:
                        print(f'      <{c.tag.split("}")[1]} {next(iter(c.attrib))}={c.attrib[next(iter(c.attrib))]}>{c.text}</{c.tag.split("}")[1]}>')
                    else:
                        print(f'      <{c.tag.split("}")[1]}>{c.text}</{c.tag.split("}")[1]}>')
                print(f'    </{child.tag.split("}")[1]}>')
                #print(f"    Tag: {c.tag.split('}')[1]}; Text: {c.text}; Attributes: {c.attrib}")
                repeat_elements.append(child)
    for l in repeat_elements:
        #print(l.attrib['repeat'])
        if '-' in l.attrib['repeat']:
            if l.attrib['repeat'][-1] == '-':
                repeats = l.attrib['repeat'][0]
            else:
                repeats = l.attrib['repeat'][-1]
        else:
            repeats = l.attrib['repeat']
        repeats = int(repeats)
        item_to_repeat = ET.Element('item')
        for child in l:
            #print(child)
            item_to_repeat.append(child)
        for child in l:
            l.remove(child)
        for child in l:
            l.remove(child)
        i = 0
        while i < repeats:
            l.append(item_to_repeat)
            i = i + 1
        l.attrib = {}
        if args.output != None:
            print(pretty_print_xml_to_file(root, args.output))
        else:
            pass
    return repeat_elements
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Finds <items> with a repeat attribute, that are direct children of <one-of> elements. It can also correct the mistake and output new grammar to a file.')
    parser.add_argument("-i", "--input", help="the input file to check", type=str)
    parser.add_argument("-o", "--output", help="the output file to save the corrected input file", type=str)
    args = parser.parse_args()
    print(args)
    ns = 'http://www.w3.org/2001/06/grammar'
    ET.register_namespace("",ns)
    # Example usage
    grxml_file_path = args.input
    analyze_grxml(grxml_file_path)
    print("Processing compleated!")