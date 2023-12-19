salary=int(input("Enter the salary: "))
exp=int(input("Enter your experience: "))
if(exp>5):
    bonus=salary*5/100
    print("The net bonus is",bonus)
else:
    print("There is not net bonus")

    #if(exp>5):
    #print("The net bonus is",salary*5/100)
