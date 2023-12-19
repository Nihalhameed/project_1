num1=input("Enter number 1: ") #10 ==>'10' is a string
num2=input("Enter number 2: ") #20  ==>'20' is a string

sum=num1+num2 #output: 1020
#'10' + '20' is concatenated string which gives the output in console as '1020'
print(sum)
#input ==> string i.e while mentioning anything inside input() it defaultly takes the value as string
#So while reading the input here mention the datatype , here it is 'int'

#Correct format
num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
sum=num1+num2 #output: 30
print(sum)
