#Nested if : if & else condtions inside if

#Problem :

#num1
#num2
#num3

#Print the second largest number



num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

if(num1>num2)&(num1>num3): #num1 is largest in this condition
    if(num2>num3): #Since num1 is greater check for second largest among num2,num3
        print("number 2 is second largest")
    else:
        print("num3 is second largest")
elif(num2>num1)&(num2>num3): #num2 is largest in this condition
    if(num1>num3): #since num2 is greater check for second largest among num1,num3
        print("num1 is second largest")
    else:
        print("num3 is second largest")
elif(num3>num1)&(num3>num2): #num3 is largest in this condition
    if(num1>num2): #since num2 is greater check for second largest number among num1,num2
        print("num1 is second largest")
    else:
        print("num2 is second largest")
else:
    print("Invalid")