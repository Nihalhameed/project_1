#Based on properties of collections:

#List:

#1.How to define?
#Defined using square brackets >> []

#Syntax :

# variablename=[] #This is an empty list

#Method 1:
# lst=[]  >> creates a list
# print(type(lst))    #This prints the type of variablename 'lst'

#Method 2: use of list function
#lst1=list() >> creates a list



#EXAMPLE FOR LIST :

#lst=[10,15,20,30]
#print(lst)



#2.List supports heterogenous data :

# lst=[10,20.5,'luminar','bigdata',True,False]
# print(lst)

#3.List supports duplicate values :

# lst=[10,20,15,15,'bigdata','bigdata']
# print(lst)

#4.Insertion order is preserved in a list :
# lst=[10,20,30,40]
# print(lst)

#Note :
#Index range : 0 to n-1

#To print a particular value in a list we consider the index:
# lst=[10,20,30,40,50,60,100]
# print(lst[3]) #prints the 4th element with index value 3

#5. List is Mutable :
# Mutable function can be explained only with index.Here we update an element in list by taking the index value.
lst=[10,20,30,40,50,60,100]
#30>>150 & 40>>200
lst[2]=150
lst[3]=200
print(lst)




