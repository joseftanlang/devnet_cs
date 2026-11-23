import re
import xml.etree.ElementTree as ET
import json
import yaml

class Book:
    # This runs automatically every time you create a new Book
    def __init__(self, book_id, title, author):
        self.id = book_id
        self.title = title
        self.author = author

# Let's create one book object
book1 = Book(1, "The Great Gatsby", "F. Scott Fitzgerald")

# Print the data using the object's properties
print(f"Book ID: {book1.id}")
print(f"Title: {book1.title}")