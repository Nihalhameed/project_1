#Method 1

#Function without arguments and no return type:

#Sum of two numbers :

def add(): #since no arguments in functions , no values are inside arguments, so need to read number from console
    num1=int(input("Enter number 1: "))
    num2=int(input("Enter number 2: "))
    sum=num1+num2
    print(sum)
add()
add() #function can be called here more than one time, if used more than one time it performs the same action again
    #Here function add() is called two times so that it performs the addition operation twice to give the output

