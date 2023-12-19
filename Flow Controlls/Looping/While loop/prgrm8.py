#Multiplication table of a given number

#read a number
#1 to 10 multiplication

#solution:
#table format needed:
#1*6=6
#2*6=12
#......
#10*6=60

num=int(input("Enter a number: "))
i=1
while(i<=10):
    print(i,"*",num,"=",i*num) #num=6
                                #1*6=6(i*num)
    i+=1



