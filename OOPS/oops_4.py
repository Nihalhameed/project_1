#Student id the class with details : create 4 objects
#id,fname,lname,age,course,collagename

class Student:
    def setvalue(self,id,fname,lname,age,course,collage):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.course=course
        self.collage=collage
    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age,self.course,self.collage)

object1=Student()
object1.setvalue(100,'nihal','h',23,'datascience','luminar')
object1.printvalue()
print()

object2=Student()
object2.setvalue(101,'noufal','h',27,'pythondjango','luminar')
object2.printvalue()
print()

object3=Student()
object3.setvalue(102,'nikhil','mathew',23,'bigdata','luminar')
object3.printvalue()
print()

object4=Student()
object4.setvalue(103,'christo','k',22,'python','luminar')
object4.printvalue()






