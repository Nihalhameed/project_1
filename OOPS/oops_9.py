#Inherutance based problem :

#Person:
#fname,lname,age,location
#Employee:
#id,prof,dept,salary


#final : id,fname,lname,age,prof,dept,location,salary

class Person:
    def setvalue(self,fname,lname,age,location):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.location=location
class Employee(Person):
    def setvalue1(self,id,prof,dept,salary):
        self.id=id
        self.prof=prof
        self.dept=dept
        self.salary=salary
    def printvalue(self):
        print(self.id,self.fname,self.age,self.prof,self.dept,self.location,self.salary)
object1=Employee()
object1.setvalue('nihal','h',23,'ekm')
object1.setvalue1(101,'bigdata','engineer',25000)
object1.printvalue()



