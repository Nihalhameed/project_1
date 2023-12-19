#Factorial of a number
#Method_1
def fact():
    num=int(input("Enter the number: "))
    fac=1 #fac*i= 0*1 is equal to 0 so fac=0 not taken
    for i in range(1,num+1):
        fac*=i  # fact=fact*i
    print(fac)
fact() #call functions outsilde