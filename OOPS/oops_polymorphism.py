#polymorphism: many forms
#1.method oveloading(not supportedin python)
#2. method overriding (support)

#overloading: two classes one iheriting another #same method name,differnt number of arguments

class Add():
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)
class Add1(Add):
    def sum(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        print(self.num1+self.num2+self.num3)

obj=Add1()
obj.sum(2,30)
obj.sum(20,30,11)
        #this will show error since it cant be understnd which method is calling.since python does not suppor
 #overriding : same method name and same number of arguments in  inherting classes


#overriding : same method name and same number of arguments in  inherting classes
class Add():
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("inside parent class",self.num1+self.num2)
class Add1(Add):
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2

        print("inside child class",self.num1+self.num2)

obj=Add1()
obj.sum(2,30)
    #same methods sum with same number of arguments
   #in overriding method which is below will execute.here child class method works but not the parent class.