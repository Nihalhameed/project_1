#read number from lower limit to upper limit to print the odd numbers
#Solution:
lower=int(input("Enter the number: "))
upper=int(input("Enter the number: "))
while(lower<=upper): #works from lower to upper
    if(lower%2!=0): #condition for odd number | ->> can also use if(lower%2==0)
        print(lower)
    lower+=1
