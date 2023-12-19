#Check if given number is positive ,negative , neither positive/negative

num=int(input("Enter the number: "))
if(num>0):
    print("Number is positive")
elif(num==0):
    print("Number is neither positive nor negative")
else:
    print("Number is negative")