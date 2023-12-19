#Using constructor instead of 'method'
#class person wtih data :fname,lname,age,location

class Person:
    def __init__(self,fname,lname,age,location): # __init__ is the constructor  used instead of method
        self.fname=fname
        self.lname=lname
        self.age=age
        self.location=location
    def printvalue(self):
        print(self.fname,self.lname,self.age,self.location)
object1=Person('vinay','k',28,'ernakulam')
object1.printvalue()

