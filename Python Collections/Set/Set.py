#Properties:
#1. How to define?
# >>  st={} >> empty curly braces machine reads it as dictionary

# st={}
# print(type(st)) #<class 'dict'>

#Method 1 to define:
#1.1) But, If values are given inside curly braces machine reads it as a set :

# st={1,2,3,4}
# print(type(st))   <class 'set'>

#Method 2 to define:
#1.2) How to define an empty set :

# st=set()
# print(st) #set() function is used to define an empty set

#2.Set supports heterogenous data :
# st={10,10.5,'bigdata','True'}
# print(st)

#3. Inseertion order is not preserved :
# st={10,10.5,'bigdata','True'}
#  print(st)                    #{'bigdata', 10, 10.5, 'True'}

#4. Set doesnt support duplicate values:

# st={10,10,20,50,'python','python','bigdata'}
# print(st) #{50, 20, 'python', 10, 'bigdata'}

#4.1 When 1,0 ,true,false occurs at a time  in a set ,it takes only values single time to give output
# st={1,0,True,False}    #{1,0,1,0}
# print(st)              #{0,1}

#5. Set is mutable :
         #Values can be updated in  a set

