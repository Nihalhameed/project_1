1.Write a Python program to calculate the area of a circle.

radius=int(input("Enter the radius:"))
pi=3.14
area= pi*radius*radius
print("Area of a circle is: ",area)

2.Create a program that checks if a given number is a perfect square.

num=int(input("Enter the number : "))
flag=0
for i in range(1,num):
    if num//i==i:
        flag=1
if flag>0:
    print(num,"is a perfect square") #1, 4, 9, 16, 25, 36, 49, 64, 81 and 100.
else:
    print(num,"is not a perfect square")

3. Write a program to find the square root of a number.

import math
num=int(input("Enter the number : "))
print(math.sqrt(num))  #sqrt() function is used

4. Find lcm of two numbers

import math
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))

    (first calculate the hcf and find the largest common divisor )
hcf=math.gcd(num1,num2) #gcd is used to find the greatest common divisor

lcm=(num1*num2)//hcf #equation to find lcm

print("LCM of",num1,"&",num2,"is: ",lcm)

5.Create a program to check if a string contains only alphabetic characters.

string='hello'
if string.isalpha():   #isalpha() - checks if the string contains only alphabetic characters
    print("The string contains only alphabetic characters")
else:
    print("The string contains non-alphanumeric characters")

6. Write a program that calculates the power of a number (a^b).

num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
print(num1**num2)

or

import math
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
print(math.pow(num1,num2)) #pow function is used

7. Create a program to calculate the sum of all natural numbers up to a given N.

num=int(input("Enter a number: "))
sum=0
for i in range(1,num+1):
    sum+=i
print(sum)

8.Write a Python program to find the factorial of a number using a loop.

num=int(input("Enter a number: "))
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)

9. Create a program to check if a string is a valid email address

email=input("Enter email address: ")
if ('@' in email)&(email[-4:]==".com")&(email[-5]!="@")&(email[0]!='@'):
    print("Valid Email")
else:
    print("Invalid Email")

10. Write a program to reverse a list in Python.

lst=[1,2,3,4,5] [::-1]
print(lst)





