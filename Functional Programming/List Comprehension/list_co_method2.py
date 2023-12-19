#Method 2 :

#Syntax:

#lst=[print..range..if condition]
#                 (print denotes-what to print ,then range ,then if condition)




#1. print from 1 to 50 range of even numbers :

lst=[i for i in range(1,51) if i%2==0] #'i'- print element,range,if condition
print(lst)

#2.print from 1 to 30 range of odd numbers :

lst=[i for i in range(1,31) if i%2!=0]
print(lst)

#3. print from 1 to 50 range of numbers divible by 5 :

lst=[i for i in range(1,51)if i%5==0]
print(lst)

#4. print from 1 to 20 range of odd numbers with its cube

lst=[i**3 for i in range(1,21) if i%2==1 ]
print(lst)

#4.1 print from 1 to 20 range of odd numbers sepreated with cube of the odd numbers :

lst=[(i,i**3) for i in range(1,21) if i%2==1]
print(lst)

#5. print from 1 to 20 range ,of even numbers, and print the total sum of even numbers only

lst=[i for i in range(1,21) if i%2==0]
print(sum(lst))

#or

lst=sum([i for i in range(1,21) if i%2==0])
print(lst)
