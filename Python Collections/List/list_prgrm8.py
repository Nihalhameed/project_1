#Find the square of the list and add those eleents to a new list :

lst=[3,1,5,7,4,10,9,8]
lst1=[]
for i in lst:
    i**=2 #i=i**2 #3**2,1**2....8**2  >> '**' is used for squaring
    lst1.append(i)
print(lst1)

