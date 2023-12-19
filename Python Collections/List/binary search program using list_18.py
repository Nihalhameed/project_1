#Binary search algorithm using list :
#1. It is used to overcome drawbacks of Linear search algorithm
#2. Reduces Time Complexity

lst=[4,9,1,10,15,20,13,14,21]
lst.sort()
num=int(input("Enter a number: "))
low=0
flag=0
upper=len(lst)-1
while(low<=upper):
    mid=(low+upper)//2  #find the mid value
    if(num>lst[mid]):      #condition 1
        low=mid+1
    elif(num<lst[mid]):    #condition 2
        upper=mid-1
    elif(num==lst[mid]):   #condition 3
        flag=1
        break
if(flag>0):
    print("Element found")
else:
    print("Element not found")