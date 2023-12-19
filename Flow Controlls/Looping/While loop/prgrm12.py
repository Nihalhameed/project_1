#Read lower limit and upper limit
#Print the sum of even numbers as well as the sum of odd numbers
lower=int(input("Enter the number: "))
upper=int(input("Enter the number: "))
even_sum=0
odd_sum=0
while(lower<=upper):
    if(lower%2==0):
        even_sum+=lower
    else:
        odd_sum+=lower
    lower+=1
print("The even sum is: ",even_sum)
print("The odd sum is: ",odd_sum)

