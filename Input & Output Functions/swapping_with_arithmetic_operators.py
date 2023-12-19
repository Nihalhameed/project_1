num1=10
num2=20

print("Before swapping")
print("number 1 is",num1)
print("number 2 is",num2)

num1=num1+num2 #num1=30
num2=num1-num2 #num2=30-20
num1=num1-num2 #num1=30-10=20
#num1 takes the final value from last line i.e is 20, since python follows line by line interpretation
print("After swapping")
print("number 1 is",num1)
print("number 2 is",num2)