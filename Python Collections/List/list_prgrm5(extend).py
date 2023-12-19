#Create an empty list and add elements from 1 to 100 :

lst=[]
for i in range(1,101):
    lst.extend([i]) #or lst.append(i)
print(lst)