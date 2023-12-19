11. Convert the temperature in degree centigrade to Fahrenheit

c=input("Enter the Centigrade value: ")
f=(int(c)*9/5)+32
print("Temp in fahrenheit is:",f)

12. Find the circumference and area of a circle with a given radius

pi=3.14
r=float(input("Enter the radius of circle: "))
c=2*pi*r
area=pi*r*r
print("The circumference of circle is: ",c)
print("Area of circle is: ",area)

13.Display all the multiples of 3 within the range 10 to 50

for i in range(10,51):
    if i%3==0:
        print(i)

14.Print Fibonacci series using iteration

a = 0
b = 1
n=int(input("Enter the number of terms in the sequence: "))
print(a,b,end=" ")
while(n-2):
    c=a+b
    a,b = b,c
    print(c,end=" ")
    n=n-1

15. Check if a given string palidrome or not

string=input("enter a string:")
if string[::-1]==string:
    print("Is Palindrome")
else:
    print("Not Palindrome")


