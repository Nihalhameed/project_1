#Multiple Inheritance:
# A Single child has more than one parent

class A:
    def printa(self,num1):
        self.num1=num1
        print("Inside class A",self.num1)
class B:
    def printb(self,num2):
        self.num2=num2
        print("Inside class B",self.num2)
class C(B,A): # C inherits both classes A and B
    def printc(self,num3):
        self.num3=num3
        print("Inside class C",self.num3)
obj1=C()
obj1.printc(10)
obj1.printb(20)
obj1.printa(30)