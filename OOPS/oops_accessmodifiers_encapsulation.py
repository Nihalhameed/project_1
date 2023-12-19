

# Public Member: Accessible anywhere from outside oclass.
# Private Member: Accessible within the class
# Protected Member: Accessible within the class and its sub-classes

# In Python, there is no direct access to modifiers like public, private, and protected.
# We can achieve this by using single underscore and double underscores.

#1.  Public member : Accessible anywhere from outside oclass.
class Employee:
    def __init__(self, name, salary):
        # public data members
        self.name = name
        self.salary = salary

    # public instance methods
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

# creating object of a class
emp = Employee('John', 8000)


print("Name: ", emp.name, 'Salary:', emp.salary) # accessing public data members

emp.show() # calling public method of the class