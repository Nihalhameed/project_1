#Fact of a number
#Method_3:

def fac(num):
    fac=1
    for i in range(1,num+1):
        fac*=i
    return fac #outside for loop it is returned
data=fac(3)
print(data)