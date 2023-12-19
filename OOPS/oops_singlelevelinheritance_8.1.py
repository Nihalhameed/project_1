#Inheritance:  One class will inherit the other class.

# Single-level inherritance ==>  A Child has a single parent

# class A ===> Parent

# class B ===> Child

class A:
    def printa(self,num1):   #method1 : printa
        self.num1=num1
        print("inside class A : ",self.num1)
class B(A): #B inherits A
    def printb(self,num2):
        self.num2=num2
        print("inside class B: ",self.num2)
obj2=B()
obj2.printb(10)
obj2.printa(20)

