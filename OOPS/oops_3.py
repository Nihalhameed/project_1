#Employee class to be defined with their details :
#id,fname,lname,age,prof,salary

class Employee:
    def setvalue(self,id,fname,lname,age,prof,salary):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.prof=prof
        self.salary=salary
    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age,self.prof,self.salary)

object1=Employee() #object is defined
object1.setvalue(100,'nihal','hameed',23,'bigdata',50000)    #reference
object1.printvalue()       #reference
print()
object2=Employee()
object2.setvalue(101,'n','k',27,'python',55000)
object2.printvalue()
print()
object3=Employee()
object3.setvalue(102,'anu','s',26,'python',35000)
object3.printvalue()
print()
object4=Employee()
object4.setvalue(103,'anamika','a',22,'python django',45000)
object4.printvalue()
print()
object5=Employee()
object5.setvalue(104,'y','kk',27,'python',55000)
object5.printvalue()
print()