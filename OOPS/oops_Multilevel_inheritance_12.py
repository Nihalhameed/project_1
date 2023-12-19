#Multi-level inheritance :
class A:
    def printa(self,num1):
        self.num1=num1
        print("Inside class A",self.num1)
class B(A): #B inherits A
    def printb(self,num2):
        self.num2=num2
        print("Inside class B",self.num2)
class C(B): # C inherits B ,but B inherits A so C also inherits A
    def printc(self,num3):
        self.num3=num3
        print("Inside class C",self.num3)
obj1=C()
obj1.printb(25)
obj1.printa(10)
obj1.printc(20) # C inherits B ,but B inherits A so C also inherits A (so output of a,b,c class )

