#Sum of n numbers

num=int(input("Enter a number: "))
sum=0 #initialize sum to 0
i=1
while(i<=num): #1<=10 , 2<=10 ,3<=10 , 4<=10
     sum+=i #0+1 =1 , 1+2=3 , 3+3=6, 6+4=10 #sum=sum+i
     i+=1
print(sum) # here sum is to be  printed outside loop just to show the total sum
# else if print statement  mentioned inside while loop its showing the sum total till the end value is reached
#eg:
#while(i<=num):
     #sum+=i
     #i+=1
     #print(sum)