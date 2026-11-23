import re
import xml.etree.ElementTree as ET
import yaml
import json

def read_json():
    with open('json.json', 'r') as file:
        json_string = file.read()
        json_data = json.loads(json_string)
        
        for item in json_data['foods']:
            print(f"Name: {item['name']} and price: ${item['price']}")
            
def read_yaml():
    with open('yaml.yaml', 'r') as cen:
        yaml_string = cen.read()
        yaml_data = yaml.safe_load(yaml_string)
        
        for things in yaml_data['foods']:
            print(f"Name: {things['name']} and price: ${things['price']}")
            
def read_xml():
    tree = ET.parse('xml.xml')
    root = tree.getroot()
    
    match = re.match('{.*}',root.tag)
    
    ns = match.group(0) if match else ""
    
    for alien in root.findall(f'{ns}food'):
        naming = alien.find(f'{ns}name').text
        price = alien.find(f'{ns}price').text
        print(f"Name: {naming} and price: ${price}")


read_xml()