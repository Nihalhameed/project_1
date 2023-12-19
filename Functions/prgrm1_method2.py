#Factorial of a number
#Method_2

def fact(num):
    fac = 1  # fact*i= 0*1 is equal to 0 so fact=0 not taken
    for i in range(1, num + 1):
        fac *= i  # fac=fac*i
    print(fac)
fact(4)
