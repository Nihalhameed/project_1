#class Personal_data

  #fname,lname,age,location

# class professional_data
 #qualification,pass_out_year,experience

 #class Employee

   #id,prof,gender,salary
#id,fname,lname,age,prof,qualification,experience,salary

class Personal:
    def detail1(self,fname,lname,age,location):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.location=location
class Professional:
    def detail2(self,qual,passyear,exp):
        self.qual=qual
        self.passyear=passyear
        self.exp=exp
class Employee(Professional,Personal):
    def detail3(self,id,prof,gender,salary):
        self.id=id
        self.prof=prof
        self.gender=gender
        self.salary=salary
    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age,self.prof,self.qual,self.exp,self.salary)
obj1=Employee()
obj1.detail1('nihal','h',23,'ekm')
obj1.detail2('btech',2023,2)
obj1.detail3(101,'bigdata','male',50000)
obj1.printvalue()



