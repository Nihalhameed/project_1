total_class=int(input("Enter the number of classes held: "))
attended=int(input("Enter the number of classes attended: "))
percent=attended/total_class*100 #equation to find percentage
print("Class percentage is",percent)
if(attended>=75):
    print("Eligible for exam")
else:
    print("Not Eligible for exam")
