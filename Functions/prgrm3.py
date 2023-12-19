#Create a simple calculator using functions:
#1.Additiom #2. Subtraction 3. multiplication 4.division

#Enter your choice:
#num1 read from console
#num2 read from console

def add(num1,num2):
    sum=num1+num2
    return sum

def sub(num1,num2):

    diff=num1-num2
    return diff

def mul(num1,num2):

    product=num1*num2
    return product

def div(num1,num2):
    division=num1/num2
    return division
print("Select choice:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
choice=int(input("Enter the choice of operation 1/2/3/4: "))
num1=int(input("Enter number1: "))
num2=int(input("Enter number2: "))
if(choice==1):
    print(num1,"+",num2,'=',add(num1,num2))
elif(choice==2):
    print(num1,"-",num2,"=",sub(num1,num2))
elif(choice==3):
    print(num1,"*",num2,"=",mul(num1,num2))
elif(choice==4):
    print(num1,"/",num2,"=",div(num1,num2))
else:
    print("Invalid")








