#create an empty list and add elements from 1 to 100 .then add even numbers to a list also odd numbers to a list.
#Print the sum of the main list(lst),print the even and odd list

# lst=[]
# even_lst=[]
# odd_lst=[]
# for i in range(1,101):
#     lst.append(i)
#     if (i%2==0):
#         even_lst.append(i)
#     else:
#         odd_lst.append(i)
# print(lst)
# print(odd_lst)
# print(even_lst)
# print("sum of list",sum(even_lst))

lst=[]
odd_lst=[]
even_lst=[]
for i in range(1,101):
    lst.append(i)
print(lst) # prints the list elements from 1,2,....100

for j in lst:
    if(j%2==0):
        even_lst.append(j)
    else:
        odd_lst.append(j)
print(even_lst)
print(odd_lst)
print("Sum of list: ",sum(lst))

