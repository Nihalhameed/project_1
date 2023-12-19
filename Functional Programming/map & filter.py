#Create a list and find the sqaure of each element in list and append those elements to new list

lst=[1,2,3,4,5,6,7,8,9,10]
lst1=[]
for i in lst:
    i**=2
    lst1.append(i)
print(lst1)

#Map :  If every element in the list needs same operation to be performed , we can use map
# [1,2,3,4,5,6,7,8,9,10] ===> [1,4,9,16,25....100]

#Filter : When a condition  is passed to a list , only results based on those condtion the elements are passed to output
# [1,2,3,4,5,6,7,8,9,10] ===> [2,4,6,8,10]

#Syntax of map & filter :

   #variablename=list(map(argument1,argument2))

       # argument1-function
       # argument2-listname

   #variablename=list(filter(argument1,argument2))

         # argument1-function to perform
         # argument2-listname