
class Category: #add an _ to the variable _Category, keeps it private. Python is public. No need to export. 
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

    def __str__(self):
        return f"{self.name}: {self.description}"