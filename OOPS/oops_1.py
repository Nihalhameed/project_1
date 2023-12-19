#Rule of class :

#1.
# class Person      # class name to be defined starts with Capital letter

#2.
# Multiple methods can be used in a single class

#Rule of object:
# Object is created using class name

#Method : the functions  defined inside a class is called 'method'

#self:  instance keyword

# Instance keyword is used for creating ('instance variables ')
# 2 types of variables:

#1. Instance vairables (keep changing variable values) :
#      i.e, Variables can also be used in another 'method' by changing the variable to instance variable :
#                                                >> (self.variablename=variablename)




#Syntax :
class Person: #class
    def reading(self):  #method1 : reading
        print("Reading a book")
    def writting(self):  #method2 : writting
        print("Writting a book")
obj1=Person() #object
obj1.reading() #reference
obj1.writting() #reference (mode of operation)

obj2=Person()
obj2.writting()







