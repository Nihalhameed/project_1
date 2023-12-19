#1.
# num=(input("Enter number:"))
# if num==str(num)[::-1]:
#     print("Is Palindrome")
# else:
#     print("Not Palindrome")

#2. Write a Python program to count the number of words in a paragraph.

# f=open('sample','r')
#
# for i in f:
#     data=i.rstrip('\n').split(' ')
#
#     dic={}
#     for j in data:
#         if j not in dic:
#             dic[j]=1
#         else:
#             dic[j]+=1
#     print(dic)

#3. Create a program to find and print the Fibonacci sequence up to N terms.

# a=0
# b=1
# num=int(input("Enter a number: "))
# for i in range (0,num):
#     print(a,end=' ')
#     a,b=b,a+b

#4. Write a program to check if a list is sorted in ascending order.

# lst=[5,4,3,2,1,8]
# lst1=lst[:] #creates the default list(lst) again and stored in lst1
# lst.sort() #sorts default list(lst) in ascending order
# if lst==lst1:
#     print("Sorted in ascending order")
# else:
#     print("Not sorted in ascending order")

#5. Area of a triangle :

# b=int(input("Enter a number: "))
# h=int(input("Enter a number: "))
# area=0.5*b*h
# print(area)

#6. Write a Python program to find the GCD (Greatest Common Divisor) of two numbers.

# import math
# num1=int(input("Enter a number: "))
# num2=int(input("Enter a number: "))
# hcf=math.gcd(num1,num2)
# print("Greatest Common Divisor is : ,",hcf)

#7.

# char = input("Enter a character: ") #ord() function is used
# print(ord(char)) # output: 97

#ord() function in Python is used to convert a single Unicode character into its integer representation

# In this program, we define a variable char and assign it the value 'a'.
# Then, we use the ord() function to get the ASCII value of the character, and print it to the console.
#
# The ord() function takes a character as input and returns its ASCII value as an integer.
# This means that the output of the program will be the ASCII value of the character a, which is 97.


#8.Write a program to find and print all prime numbers up to N.

# num=int(input("Enter the limit:"))
# for i in range(0,num+1):
#     if (i>1):
#         for j in range(2,i):
#             if(i%j==0):
#                 break
#             else:
#                 print(i,end=' ')

#9. Create a program that converts a decimal number to binary:

# One of the methods to convert decimal to binary is by dividing the given decimal number recursively by 2.
# Then, the remainders are noted down till we get 0 as the final quotient.

# digit=int(input("Enter a number: "))
# binary='' #empty string
#
# while digit>0:
#     conversion=digit%2 #divides the number by 2 > condition to convert decimal to binary
#     binary=binary+str(conversion)
#     digit//=2 #recursively dividing the number by 2
# print(binary[::-1])

#10.
#Write a Python program to find the minimum and maximum elements in a list.

# lst=[1,7,5,4,3,5,8,9,10]
# print(min(lst))
# print(max(lst))









