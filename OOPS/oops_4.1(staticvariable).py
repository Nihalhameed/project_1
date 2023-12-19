#2. Static variables :  Variables in which values that do not change
# If we are having a common value in  a variable we declare it as static variable.
# We dont need to pass value each time to that particular variable
#Eg :
# From  above program having same collage name that is a static variable , then

# steps : 1. Remove collagename(variable) from method 1 : 'setvalue' &
#         2. inside method 2: 'printvalue' set (class.variablename)
#         3. set collagename='value' inside class

class Student:
    collage='luminar'
    def setvalue(self,id,fname,lname,age,course):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.course=course
    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age,self.course,Student.collage)

object1=Student()
object1.setvalue(100,'nihal','h',23,'datascience')
object1.printvalue()
print()

object2=Student()
object2.setvalue(101,'noufal','h',27,'pythondjango')
object2.printvalue()
print()

object3=Student()
object3.setvalue(102,'nikhil','mathew',23,'bigdata')
object3.printvalue()
print()

object4=Student()
object4.setvalue(103,'christo','k',22,'python')
object4.printvalue()