#Factorial of a given number?

#eg: 3! = 1*2*3

num=int(input("Enter the number: "))
fact=1 #fact*i= 0*1 is equal to 0 so (fact=0 is not taken)
for i in range(1,num+1):
    fact*=i #fact=fact*i
print(fact) #printed always outside loop to get final result only

