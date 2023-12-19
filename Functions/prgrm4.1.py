#Syntax :
#import packagename.module
#variablename=packagename.modulename.fncall()

import Functions.prgrm4
data=Functions.prgrm4.add(20,10)
print(data)

data1=Functions.prgrm4.sub(40,10)
print(data1)

data2=Functions.prgrm4.mul(2,10)
print(data2)

data3=Functions.prgrm4.div(30,10)
print(data3)

#For this method above , each time we should call the module name and package to perform the operations

#So we will be using another method to import all the functions in a single line.

#Syntax:
#from.packagename.module import *
#data=add(20,10)
#data1=sub(40,10)
#data2=mul(2,10)
#data3=div(30,10)


