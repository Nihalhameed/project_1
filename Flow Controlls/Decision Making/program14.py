#integer data example:

#if(age>18):
#if(num%2==0):
#if(num>0):

#string data shoud be in format:
 #if(city=='Delhi') #assign string data in single quotes in condition

city=input("Enter the city name: ")
if(city=='Delhi'):
    monument='Fort Mahal'
    print("The monument of the city is",monument)
elif(city=='Agra'):
    monument='Taj mahal'
    print("The monument of the city is", monument)
elif(city=='Jaipur'):
    monument='Jal mahal'
    print("The monument of the city is", monument)
else:
    print("Invalid")
