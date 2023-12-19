#Class is employee
#id,fname,lname,age,prof,company_name

#5 objects:
#bigdata

class Employee:
    prof='bigdata' #static variable
    def setvalue(self,id,fname,lname,age,company_name):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.company_name=company_name
    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age,self.company_name,Employee.prof)

obj1=Employee()
obj1.setvalue(101,'nihal','k',23,'ust')
obj1.printvalue()
print()
obj2=Employee()
obj2.setvalue(102,'n','k',23,'infosys')
obj2.printvalue()
print()
obj3=Employee()
obj3.setvalue(103,'nihal','k',23,'ust')
obj3.printvalue()
print()
obj4=Employee()
obj4.setvalue(104,'nihal','k',23,'ust')
obj4.printvalue()
print()
