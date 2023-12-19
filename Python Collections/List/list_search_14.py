#Create a list and read a number from console .List search for a number
# and if the number is present in the list then print element found , else print element not found
#(same concept as prime number)

lst=[4,14,32,12,3,11,6]
num=int(input("Enter a number: "))
flag=0
for i in lst:
    if (i == num):
            flag = 1
            break
if (flag > 0):
        print("Element Found")
else:
        print("Element not found")

# The above program follows Linear Search Algorithm
# Checks every element in the list
        # Drawback:- Time consuming >> eg: If a large number is given as input many number of iterations in for loop
#                    need to be performed till the element is found


# To overcome drawbacks of linear search algorithm we use Binary search Algorithm
       # >>> It reduces time complexity