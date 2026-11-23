import yaml
import json
import xml.etree.ElementTree as ET
import re 

def parse_yaml():
    with open('db/yaml.yaml','r') as file:
        yaml_string = file.read()
        yaml_data = yaml.safe_load(yaml_string)
        for ani in yaml_data['animal']:
            print(f"id: {ani['id']} and name: {ani['name']}")

def parse_json():
    with open('db/json.json', 'r') as file:
        json_string = file.read()
        json_data = json.loads(json_string)
        for ani in json_data['animal']:
            print(f"id: {ani['id']} and name: {ani['name']}")

def parse_xml():
    tree = ET.parse('db/xml.xml')
    root = tree.getroot()
    
    match = re.match('{.*}', root.tag)
    ns = match.group(0) if match else ""
    
    for ani in root.findall(f'{ns}animal'):
        ani_id = ani.find(f'{ns}id').text
        name = ani.find(f'{ns}name').text
        print(f"id: {ani_id} and name: {name}")

parse_xml()