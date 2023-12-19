# Print the Largest among 3 numbers:
#30
#40
#50 (1)

#50 (2)
#40
#30

#40
#50 (3)
#30

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
if(num1>num2)&(num1>num3): #20>40 & 20>50 #fail
    print("Number 1 is the largest")
elif(num2>num1)&(num2>num3):
    print("Number2 is the largest") #40>20 & 40>50 #fail , #both 'and' condtions should satisfy to get o/p
else:
    print("Number3 is the largest")
