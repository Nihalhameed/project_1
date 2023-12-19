class Person:
    def setvalue(self,fname,lname,age,loc): #method1: setvalue
        self.fname=fname #variable is changed to instance variable  so that it can be used in next method
        self.lname=lname
        self.age=age
        self.loc=loc
    def printvalue(self):  #method2: printvalue
        print(self.fname)
        print(self.lname)
        print(self.age)
        print(self.loc)
object1=Person()
object1.setvalue('nihal','hameed',23,'trivandrum')
object1.printvalue()
print()
object2=Person()
object2.setvalue('noufal','hameed',27,'trivandrum')
object2.printvalue()