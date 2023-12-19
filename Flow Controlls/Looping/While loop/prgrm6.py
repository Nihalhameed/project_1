#print a number from lower to upper limit

#lower limit & upper limit read from console,
#lower limit is where it starts
#upper limit denotes the number where loop ends

lower=int(input("Enter a number: ")) #acts as initialization step (lower = i)
upper=int(input("Enter a number: "))

while(lower<=upper):
    print(lower)
    lower+=1