#OOP - object oriented programming or design.
''' Take a complicated topic and make it into a modular application.
Objects or classes
O - blueprints / prototype; creating and grouping data. Holds data - attributes of a prototype of a blueprint. Uses methods - functions. You pass arguments, a function receives parameters
C - Instance of a class - take a blueprint and create on instance of the objects and have it interact with other objects. Class naming convention is capitalization. Ex. pets
Pet blueprint(class)
attributes in a pet: name, height, size, kind/breed, gender, species, diet, leg number, etc. 
Dog (object) - ("rover", "40'",)
Function - feed_pet, pet_pet, play_pet, walk_pet, etc.
'''

from category import Category

class Store:
    # attributes
    # name
    # categories (departments)

    # constructor - the function that runs every time you create a new instance.
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

        #dunder function uses double __ (underscores)

    def __str__(self): #str - allows us to transform the store object into a string. A built-in function.
        # return a stirng representing the store. Build a string class.\n = new line
        output = f"Welcome to {self.name}!"
        i = 1
        for category in self.categories:
            output += f'\n {i} {str(category)}'
            i += 1
        return f"Welcome to {self.name}! Here are the categories: {self.categories}"

    def __repr__(self):
       # also returns a string.
       # helps developers debug and understand how object is structured. datenow(). Repr classes, represents underlying classes or sub-classes. 
       return f"self.name = {self.name} : self.categories = {self.categories}"

running_category = Category("Running", "All equipment available", [])
biking_category = Category("Biking", "Mountain bikes only", [])
fishing_category = Category("Fishing", "Outdoor only", [])
hiking_category = Category("Hiking", "Outdoor/Mountains only", [])



sports_store = Store("Gander Mountain", ["Running", "Biking", "Fishing", "Hiking"]) 
produce_store = Store("Kroger", ["Dairy", "Produce", "Deli", "Bakery" ]) #create an instance of existing code. 

#str(sports_store)
#print(sports_store)
#print(produce_store)
#print(repr(sports_store))

#print(running_category)

sports_store = Store("Gander Mountain", [running_category, biking_category, fishing_category])
choice = -1

# REPL <- Read, Evaluate, Print, Loop. 

print(sports_store)
print("type q to quit")
while True:
    # Read
    choice = input("Please choose a category (#): ")
    try:
        # Evaluate
        if (choice == "q"):
            break
        choice = int(choice) - 1
        if choice >= 0 and choice < len(sports_store.categories):
            chosen_category = sports_store.categories[choice]
            # Print
            print(chosen_category)
        else: 
            print("The number is out of range.")
    
    except ValueError:
        print("Please enter a valid number.")
         #except Exception: which works as a "catch all" for errors
