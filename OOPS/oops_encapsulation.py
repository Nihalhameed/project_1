#Encapsulation in Python describes the concept of bundling data and methods within a single unit.

class Employee:
    def __init__(self, name, salary, project):
        # data members
        self.name = name
        self.salary = salary
        self.project = project


    # to display employee's details
    def show(self): # method
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

    def work(self): # method
        print(self.name, 'is working on', self.project)

# creating object of a class
emp = Employee('Anu', 12000, 'bigdata')

# calling public method of the class
emp.show()
emp.work()

#Note :

# Using encapsulation, we can hide an object’s internal representation from the outside.
# This is called information hiding.

