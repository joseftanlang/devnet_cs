class Location:
    def __init__(self, name, country):
        # Store attributes
        self.person = name
        self.country = country  # Use consistent naming

    def myLocation(self):
        # Method to print location info
        print(f"Hi, my name is {self.person} and I am from {self.country}!")

# Create an instance
loc = Location("naaaaa", "lobseter")

# Access attributes
print(loc.person)   # Output: naaaaa
print(loc.country)  # Output: lobseter

# Call method
loc.myLocation()    # Output: Hi, my name is naaaaa and I am from lobseter!

