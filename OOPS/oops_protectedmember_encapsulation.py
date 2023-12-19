# To define a protected variable, prefix the member name with a single underscore

# Protected data members are used when we implement 'inheritance' and want to allow
# data members access to only child classes.

# parent class
class Company:
    def __init__(self):
        # Protected member
        self.__project = "xyz"

# child class
class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Employee name :", self.name)
        # Accessing protected member in child class
        print("Working on project :", self._project)

c = Employee("Nihal")
c.show()

print('Project:', c._project) # Direct access protected data member