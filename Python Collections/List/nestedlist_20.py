#Nested list:   To create a list inside a list

#5 employee details: id,fname,lname,age,profession,salary

# Nested list syntax :
# lst=[[101,'anu','p',19,'bigdata',1000],
#      [102,'nihal','t',25,'python',2000],] (each list is seperated by comma)

# 1.Important interview ques to collect each invidual list from nested list :

for i in lst:
    print(i) #To print each list in invidual manner we use this for loop with print function :
             #output:  #[101, 'anu', 'p', 23, 'bigdata', 1000]
                      #[102, 'nihal', 't', 25, 'python', 2000]

#Collect informations with only data : fname,lname,age,prof

lst=[[101,'anu','p',23,'bigdata',1000],
     [102,'nihal','t',25,'python',2000]]
for i in lst:
    print(i[1],i[2],i[3],i[4])  #by giving index value prints the wanted data only

    #another method :
    print(i[1:5]) #List slicing method to print elements from index 1 to 4

#Collect informations with only data : fname,age,salary :

for i in lst:
    print(i[1:6:2]) #or print(i[1::2])

#3. Collect details for the employees for age above 28 only : fname,lname,age,prof
lst=[[101,'anu','p',19,'bigdata',1000],
     [102,'nihal','t',30,'python',2000]]
for i in lst:
    if(i[3]>28):
        print(i[1:5])

#4, Empployees with data profession >> print their fname,age,salary

lst=[[101,'anu','p',19,'bigdata',1000],
     [102,'nihal','t',30,'python',2000]]
for i in lst:
    if(i[4]=='bigdata'):
        print(i[1::2])

#5. age >29 & big data working two condition need to satisfy>> print their fname,lname,age,prof

lst=[[101,'anu','p',19,'bigdata',1000],
     [102,'nihal','t',30,'python',2000]]
for i in lst:
    if (i[3]>29) and (i[4]=='bigdata'):
        print(i[1:5])

#In data science this type of list and index based problems are used

#end of list programs!