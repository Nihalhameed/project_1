#rate above 100000 15%

#50000 <=100000 10%

#below 50000 5%

cost=int(input("Enter the price: "))
if(cost>100000):
    tax=cost*15/100
    print("Tax to be paid is: ",tax)
elif(cost>50000)&(cost<=100000):
    tax=cost*10/100
    print("Tax to be paid is: ",tax)
else:
    tax=cost*5/100
    print("Tax to be paid is: ",tax)
