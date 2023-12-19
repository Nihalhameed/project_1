#1. lst=[4,9,11,13,15,20,25]

#Create an identical list from above using list comprehension

lst=[4,9,11,13,15,20,25]
lst1=[i for i in lst]
print(lst1)

#2. Create a list from the element of range from
#    1200 to 2000 with step of 130,using list comp

lst=[i for i in range(1200,2001,130)]
print(lst)

#3. Use a list comprehension to construct a new list but add 6 to each item : [3,6,7,8,10,15,21]

lst=[3,6,7,8,10,15,21]
lst1=[i+6 for i in lst]
print(lst1)

#4. Using list comprehension construct a new list from the
#   square of each element in the list : [1,5,10,15,2,3,4,6]

lst=[1,5,10,15,2,3,4,6]
lst1=[i**2 for i in lst]
print(lst1)

#5. [1,6,9,10,3,5,15,20]
 #print the squares of element greater than 40

lst=[1,6,9,10,3,5,15,20]
lst1=[i**2 for i in lst if i**2>40]
print(lst1)



