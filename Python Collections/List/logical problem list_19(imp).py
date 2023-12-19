#Calculate the sum of the list and create a new list and then add the elements
# to the new list in the following format:
#lst1=[85,97,88,70,85,88,87]

lst=[15,3,12,30,15,12,13] # each element in list is 'i'
lst1=[]
res=sum(lst) #stores the sum in a variable
for i in lst:
    lst1.append(res-i) #100-15=85,100-3=97,100-12=88.....100-13=87
print(lst1)