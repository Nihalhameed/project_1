#read lower limit,upper limit
#read numbers from lower to upper and get the even numbers.
#problem statement: Print the sum of even numbers

#Note:Always set 0 for sum based problems(sum=0)

lower=int(input("Enter the number: "))
upper=int(input("Enter the number: "))
sum=0
while(lower<=upper):
    if(lower%2==0):
        sum+=lower
    lower+=1
print(sum) #sum is printed outside while loop always to get the total of sum
