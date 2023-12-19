#read lower limit & upper limit
#check for even or odd and print the sum of even and sum of odd numbers

lower=int(input("Enter the number: "))
upper=int(input("Enter the number: "))
even_sum=0
odd_sum=0
for i in range(lower,upper+1):
    if(i%2==0): #condition for even number
        even_sum+=i #condition for sum of even numbers
    else:
        odd_sum+=i

print("The sum of even numbers is: ",even_sum)
print("The sum of even numbers is: ",odd_sum)