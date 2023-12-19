#Check given number is prime or not?
#Prime factors: A number is said to be prime if that number has 1 and that number itself as factors

num=int(input("Enter the number: ")) #9
flag=0 #set a variable as 0 in value
for i in range(2,num): #(2,9) 2 to 8
    if(num%i==0): #if number(num) is divisible (i.e remainder is 0) then its not prime 2%2==0
        flag=1 #when num is divisible by i flag is 1 (then its not prime)
if(flag>0):
    print("Not prime")
else:
    print("Prime")


