#Private member : Accessible only within the class, and we can’t access them directly from the class objects.

# To define a private variable,
# add two underscores as a prefix at the start of a variable name.
class Employee:
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary #Uses two underscores as a prefix at the start of a variable name.

# creating object of a class
emp = Employee('Anjana', 10000)


print('Salary:',emp.__salary) # accessing private data members

#output : AttributeError: 'Employee' object has no attribute '__salary'

# Reason : Salary is a private variable.
#  Since we cant access the private variable from the outside of that class.