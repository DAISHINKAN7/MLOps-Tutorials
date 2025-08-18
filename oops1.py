# Initiating a class in Python
class Employee:
    # special function/magic method/dundder functions- constructor
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000 
        self.designation = "SDE"
        print("Attributes/data have been initiated")

    def travel(self, destination):
        print("This travel function was called manually")
        print(f"Employee is now travelling to {destination}")

# Creating an object/instance of the class
sam = Employee()

# Calling a method
sam.travel(destination="Italy")

# Printing the attributes
print(sam.salary)
print(type(sam))