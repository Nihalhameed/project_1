#Write a program to calculate the electricity bill

#Accept number of unit from the user according to following criteria
#first 100  ==> free of cost
#100-200 ===> unit ===>5rs charge per unit
#above 200 ===> unit ===> 10rs charge per unit

#Example : 350unit used.Calculate the bill===>
#solution:
#first 100 unit free
#100-200(100 unit) : 100*5 = 500 (till 200 unit 500rs)
#150 (150 unit above 200 now) = 150*10 = 1500
#total = 2000 charge

unit=int(input("Enter the amount of unit consumed: "))
if(unit<=100):
    print("No charge")
elif(unit>100)&(unit<=200): #eg : 150unit
    amount=(unit-100)*5     #since first 100 unit is free we should subtract it from unit
    print("Charge obtained is: ",amount)
else: #eg:350unit
    amount=(unit-200)*10+500 #350-200 = 150*10 = 1500+(500)
    #first 100 free,100-200 is 500rs charge,200 subtract,remaining 150
    print("Charge obtained is: ",amount)



