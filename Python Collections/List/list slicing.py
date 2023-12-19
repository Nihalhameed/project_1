#List slicing: Taking any part of a list in needed format

lst=[10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]
#[start:end]
print(lst[3:8]) #3:8 is the range of index value, here it prints from index 3 to 7 [25,30,35,40,45]
print(lst[2:6]) #index=2 to 5
print(lst[1:8])#index=1 to 7

print(lst[4:])#starting index is defined..Prints elements from ,(index = 4 to the  end of list)
print(lst[6:])

print(lst[:7]) #ending index is defined..Prints elements upto 6 ,( index= 0 to 6)

print(lst[:]) #no starting and end postion, (full list is printed)

#[start:end:step] , step denotes by how many times it increments
print(lst[2:8:2]) #prints values of (index=2,4,6) i.e is 20,30,40
print(lst[1:9:3]) #prints values of index=1,4,7
#[start::step]
print(lst[2::4]) #prints values of index=2,6,10,14
#[:end:step]
print(lst[:7:2]) #index=0,2,4,6
#[::step]
print(lst[::4]) #index=0,4,8,12

#Note:
#lst=[10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]

#Positive indexing ===> 0 to n-1
#Negative indexing ===> -1 to -n
#Example:
print(lst[-1]) #80 is the end value with -1 as index (-1 to -n)
print(lst[-3]) #70
