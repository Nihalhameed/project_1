#Problem: Reverse a number

#eg: 153 ====>351
#For getting 351 first get 3,
#153%10 = 3
#153//10 = 15 (here floor value is calculated to get next value 5 in 15%10=5)

#15%10=5
#15//10=1(here floor value is calculated to get next value 1 in 1%10=1)

#1%10=1
#Solution:

num=int(input("Enter the number: ")) #153
result=0
while(num!=0):#num should not be 0, #153!=0 15!=0 1!=0
    digit=num%10 #153%10=3 15%10=5 1%10=1
    result=(result*10)+digit # (0*10)+3=3 (3*10)+5=35
    num//=10 #num=num//10 #153//10=15 15//10=1 1//10=0
print(result) #to print the final result we should mention the print statement outside the loop



