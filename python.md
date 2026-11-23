# Python Reference

## 1. Python Basics

- **Check Version**: `python3 -V`
- **Interactive Interpreter**: Type `python3` in the terminal and look for the `>>>` prompt.
- **Exit Interpreter**: `quit()` or `Ctrl+D`
- **Run a Script**: `python3 myscript.py`
- **Math Operators**: `+` (add), `-` (subtract), `*` (multiply), `/` (divide), `**` (exponent).

## 2. Data Types & Variables

Python is dynamically typed, but you can check types using `type()`.

- **`int`**: Whole numbers (for example, `98`)
- **`float`**: Decimals (for example, `98.6`)
- **`str`**: Text in single or double quotes (for example, `"Hi!"`)
- **`bool`**: `True` or `False`

### Variables & Casting

```python
x = 3              # Assignment
x_str = str(x)     # Cast integer to string
x_int = int("5")   # Cast string to integer
```

### Formatting Strings

```python
num = 22 / 7

# Round to 2 decimal places
print("Pi is {:.2f}".format(num))
# Output: Pi is 3.14

# Or use f-strings (modern Python)
print(f"Pi is {num:.2f}")
```

## 3. Lists (Arrays)

Lists are ordered, changeable collections that use square brackets `[]`.

```python
hostnames = ["R1", "R2", "R3", "S1", "S2"]

print(hostnames[0])      # Output: R1 (first item)
print(hostnames[-1])     # Output: S2 (last item)
print(len(hostnames))    # Output: 5 (length)

hostnames[0] = "RTR1"    # Change first item
del hostnames[3]          # Delete 4th item ("S1")
```

## 4. Dictionaries

Dictionaries store **key-value** pairs and use curly braces `{}`.

```python
ipAddress = {"R1": "10.1.1.1", "R2": "10.2.2.1"}

print(ipAddress["R1"])   # Output: 10.1.1.1

# Add a new key-value pair
ipAddress["S1"] = "10.1.1.10"
```

## 5. Control Flow (If, Elif, Else)

Python requires consistent indentation, conventionally **4 spaces**.

```python
aclNum = int(input("Enter ACL number: "))

if aclNum >= 1 and aclNum <= 99:
	print("Standard ACL")
elif aclNum >= 100 and aclNum <= 199:
	print("Extended ACL")
else:
	print("Not a standard or extended ACL")
```

## 6. Loops

### For Loops

```python
devices = ["R1", "R2", "S1", "S2"]

for item in devices:
	print(item)

# For loop with an if statement
switches = []
for item in devices:
	if "S" in item:
		switches.append(item)
```

### While Loops

```python
x = 1
while x <= 5:
	print(x)
	x = x + 1  # Be careful not to create an infinite loop.
```

## 7. User Input

The `input()` function pauses the script and waits for input. It always returns a string.

```python
firstName = input("What is your name? ")
print("Hello " + firstName + "!")
```

## 8. File Access

### Read a File

```python
with open("file.txt", "r") as file:
	data = file.read()
	print(data)
```

### Write to a File

Writing with mode `w` overwrites an existing file.

```python
with open("file.txt", "w") as file:
	file.write("Hello World")
```

### Append to a File

Appending with mode `a` adds content to the end of a file.

```python
with open("file.txt", "a") as file:
	file.write("\nNew line")
```

## 9. Python Installation and Executable Path

- **Check Python Version**:

  ```bash
  python3 -V
  ```

- **Find the Python Executable Path**:

  ```bash
  which python3
  ```

This typically outputs `/usr/bin/python3`.

## 10. Python Virtual Environments (`venv`)

Virtual environments keep project dependencies isolated so that packages installed for one project do not affect another.

### Create an Environment

```bash
python3 -m venv devfun
```

### Activate the Environment

The terminal prompt will show the active environment, for example `(devfun)`.

```bash
source devfun/bin/activate
```

### Deactivate the Environment

```bash
deactivate
```

## 11. Using PIP

Inside an active virtual environment, `pip3` installs packages into that environment.

### Install a Package

```bash
pip3 install requests
```

### List Installed Packages

```bash
pip3 freeze
```

### Check System-Wide Packages

```bash
python3 -m pip freeze
```

### Search for a Package

```bash
python3 -m pip freeze | grep requests
```

## 12. Sharing an Environment with a Requirements File

### Export Requirements

Make sure the virtual environment is active, then save the package versions:

```bash
pip3 freeze > requirements.txt
```

### Install from a Requirements File

Create and activate a virtual environment, then install the listed packages:

```bash
pip3 install -r requirements.txt
```

## 13. Functions vs. Methods vs. Classes

- **Function**: An independent, reusable block of code. It does not belong to an object.
- **Class**: A blueprint for creating objects (instances). It bundles data (properties) and behaviors (methods).
- **Method**: A function defined inside a class. It is called on an object created from that class.

## 14. Defining and Calling Functions

Functions are standalone and reusable.

```python
# Define the function
def myCity(city):
	print("I live in " + city + ".")

# Call the function with arguments
myCity("Tokyo")
myCity("Salzburg")
```

## 15. Defining a Class with `__init__`

The `__init__` method is the constructor. It runs automatically when you create an object.

- **`self`**: The first parameter of a method; it refers to the specific object.
- **Instantiation**: Creating an object from a class blueprint.

```python
class Location:
	def __init__(self, name, country):
		self.name = name
		self.country = country

# Instantiate (create) an object
loc1 = Location("Tomas", "Portugal")

# Access a property
print(loc1.name)    # Output: Tomas
```

## 16. Adding Methods to a Class

Methods allow an object to perform actions using its own properties.

```python
class Location:
	def __init__(self, name, country):
		self.name = name
		self.country = country

	def myLocation(self):
		print("Hi, my name is " + self.name + " and I live in " + self.country + ".")

# Instantiate and call the method
loc1 = Location("Ying", "China")
loc1.myLocation()
# Output: Hi, my name is Ying and I live in China.
```

## 17. Complete Circle Example

This example combines a class, a constructor, a method that returns a value, and a method that prints the result.

```python
class Circle:
	def __init__(self, radius):
		self.radius = radius

	def circumference(self):
		pi = 3.14
		circumferenceValue = pi * self.radius * 2
		return circumferenceValue

	def printCircumference(self):
		myCircumference = self.circumference()
		print(
			"Circumference of a circle with a radius of "
			+ str(self.radius)
			+ " is "
			+ str(myCircumference)
		)

# Instantiate and call
circle1 = Circle(5)
circle1.printCircumference()
# Output: Circumference of a circle with a radius of 5 is 31.400000000000002
```
