#Read numbers from lower limit to upper limit
#Problem : print only the even numbers
#Solution:

lower=int(input("Enter the number: "))
upper=int(input("Enter the number: "))

while(lower<=upper):
    if(lower%2==0): #condition for even
        print(lower)
    lower+=1 #this statement works under  while condition


