import json
import yaml
import xml.etree.ElementTree as ET
import re ##this is for the XML that is needed

def parse_all_format():
    with open('data.json', 'r') as file:
        json_string = file.read()
        json_data = json.loads(json_string)
        
        for book in json_data['library']:
            print(f"ID: {book['id']} | Title: {books['title']}")
            
    with open('data.yaml','r') as file:
        yaml_string = file.read()
        yaml_data = yaml.string(yaml_string)
        
        for book in yaml_data['library']:
            print(f"ID: {book['id']} | Title: {books['title']}")
            
    tree = ET.parse(data.xml)
    root = tree.getroot()

    for book in root.findall('book'):
        book_id = book.find('id').text
        title = book.find('title').text
        print(f"ID: {book_id} | Title: {title}")

def get_XML():
    tree = ET.parse('data.xml')
    root = tree.getroot()
    
    # 2. Extract the namespace (e.g., if your XML has a namespace)
    # Using a try/except just in case your XML doesn't actually have a namespace
    
    #This line uses Regular Expressions (Regex) to search for a specific pattern inside the root tag of the XML.
    match = re.match('{.*}', root.tag)
    
    #This is a conditional assignment (similar to a one-line if/else statement). 
    #It translates to: "If match is not empty, do match.group(0). Otherwise, set ns to an empty string."
    ns = match.group(0) if match else ""
    
    # 3. Add the namespace {} to the tags
    for book in root.findall(f'{ns}book'):
        book_id = book.find(f'{ns}id').text
        title = book.find(f'{ns}title').text
        print(f"ID: {book_id} | Title: {title}")

        
def get_JSON():
    with open('data.json', 'r') as file:
        json_string = file.read()
        json_data = json.loads(json_string) 
        for book in json_data['library']:
            print(f"ID: {book['id']} | Title: {book['title']}")

def get_YAML():
    with open('data.yaml', 'r') as file:
        yaml_string = file.read()
        yaml_data = yaml.safe_load(yaml_string) 
        for book in yaml_data['library']:
            print(f"ID: {book['id']} | Title: {book['title']}")

    
user_choice = input("Please choose 1 for XML, 2 for JSON, or 3 for YAML: ")

if user_choice == "1":
    get_XML()
elif user_choice == "2":
    get_JSON()
elif user_choice == "3":
    get_YAML()
else:
    print("Invalid choice. Please run the program again and choose 1, 2, or 3.")
    