lst=[]
lst.append(4) #append() function is used to add an element to a list
lst.append(10) #for adding another element to a list again append function is called again.
print(lst)

#Note : At a time only single element can be passed as an argument in the list to the append() function

#extend() function :
#To add multiple elements to the list we use extend() function
lst=[]
lst.extend([40,50,60]) #while using extend() function  use [] to store multiple elements
print(lst)