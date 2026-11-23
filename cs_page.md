# DEVASC All-In-One Cheat Sheet

## 1. Virtual Lab Environment & Linux

- **`sudo`**: Run as administrator (`sudo apt update`). Never use `sudo pip install`.
- **File Navigation**: `pwd` (where am I), `ls -l` (list files), `cd ..` (up one directory).
- **Permissions**: `chmod +x script.sh` (make executable), `chown root file` (change owner).
- **Search & Pipe**: `cat /etc/passwd | grep devasc` (find lines containing "devasc").
- **Output**: `>` (overwrite), `>>` (append), `|` (pipe output to next command).

## 2. Python Basics & Classes

- **Data Types**: `int`, `float`, `str`, `bool`, `list` `[]`, `dict` `{}`.
- **Casting**: `str(5)` (to text), `int("5")` (to number).
- **Formatting**: `f"Hello {name}"` or `"Hello {}".format(name)`.
- **Classes (`self` is mandatory)**:

```python
class Location:
    def __init__(self, name, country): # Constructor
        self.name = name
        self.country = country

    def printMe(self):                 # Method
        print(f"Hi {self.name}")
```

## 3. Python Dev Tools & Data Parsing

- **Virtual Env**: Create `python3 -m venv myenv`, Activate `source myenv/bin/activate`, Deactivate `deactivate`.
- **PIP**: Install `pip3 install requests`, Share `pip3 freeze > requirements.txt`, Install share `pip3 install -r requirements.txt`.
- **JSON**: `import json` -> `json.loads(string)` or `json.load(file)`.
- **YAML**: `import yaml` -> `yaml.safe_load(file)`.
- **XML**: `import xml.etree.ElementTree as ET` -> `tree = ET.parse('file.xml')` -> `root.find('tag').text`.

## 4. REST APIs (Postman, cURL, Python)

- **Methods**: `GET` (read), `POST` (create), `PUT` (update), `DELETE` (remove).
- **Status Codes**: `200` (OK), `201` (Created), `400` (Bad Request), `401` (Unauthorized), `404` (Not Found).
- **cURL**: `curl -X GET "http://url" -H "accept: application/json"`
- **Postman**: `Auth` tab for tokens, `Headers` for API keys (`X-API-KEY`), `Body` (raw/JSON) for data.
- **Python API Request**:

```python
import requests
import urllib.parse

url = "https://graphhopper.com/api/1/geocode?" + urllib.parse.urlencode({"q": "Washington", "key": key})
reply = requests.get(url)

if reply.status_code == 200:
    data = reply.json()
    lat = data["hits"][0]["point"]["lat"]
```

## 5. Git Version Control

- **Setup**: `git config --global user.name "Name"` and `git config --global user.email "email"`.
- **Workflow**: `git status` -> `git add .` -> `git commit -m "msg"` -> `git push origin main`.
- **Sync**: `git pull origin main` (always pull before pushing).
- **Branches**: `git checkout -b new-branch` (create & switch), `git merge branch-name`.
- **Fixes**: `git restore --staged file` (unstage), `git reset --hard HEAD~1` (undo last commit & delete changes).
- **Ignore**: Add files to `.gitignore` so they aren't tracked (e.g., `venv/`, `.env`).
