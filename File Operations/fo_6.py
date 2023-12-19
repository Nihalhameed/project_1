#Reading a file from local machine's path: File read ===> Local machine
#customer text =id,fname,lname,age,prof,country
#Age above 50 data to be collected

# f=open('/Users/macbook/Downloads/customer1.txt','r')
# for i in f:
#     data=i.rstrip('\n').split(',')
#     age=data[3]
#     if age>'50': #50 is a string in output eg : ['4000004', 'Gretchen', 'Hill', '66', 'Computer hardware engineer', 'china']
#         print(data)

#2. Read details : fname,lname,age,prof, whose age > 60 :

# f=open('/Users/macbook/Downloads/customer1.txt','r')
# for i in f:
#     data=i.rstrip('\n').split(',')
#     age=data[3]
#     if age >'60':
#         print(data[1:5])

#3. age less than 30 fname,age,country:

# f=open('/Users/macbook/Downloads/customer1.txt','r')
# for i in f:
#     data=i.rstrip('\n').split(',')
#     age=data[3]
#     if age<'30':
#         print(data[1:6:2])

#4. works in india ..fname,lname,age,prof
#5. works in india...age above 50 fname,age,country
#6. Dancer prof work.. fname,lname,age
#7.works in india and prof dancer ..full data
#8.pilot prof..fname,lname,age
#9. age range 25 to 40 ..fname,lname,age,prof,country

# f=open('/Users/macbook/Downloads/customer1.txt','r')
# for i in f:
#     data=i.rstrip('\n').split(',')
#     country=data[-1]
#     if country =='india':
#         print(data[1:5])

# f=open('/Users/macbook/Downloads/customer1.txt','r')
# for i in f:
#     data=i.rstrip('\n').split(',')
#     country=data[-1]
#     age=data[3]
#     if(country=='india')&(age>'50'):
#         print(data[1::2])

# f=open('/Users/macbook/Downloads/customer1.txt','r')
# for i in f:
#     data=i.rstrip('\n').split(',')
#     prof=data[4]
#     if prof=='Dancer':
#       print(data[1:4])

# f=open('/Users/macbook/Downloads/customer1.txt','r')
# for i in f:
#     data=i.rstrip('\n').split(',')
#     prof=data[4]
#     country=data[-1]
#     if (country=='india') & (prof=='Dancer'):
#         print(data)
#
# f=open('/Users/macbook/Downloads/customer1.txt','r')
# for i in f:
#     data=i.rstrip('\n').split(',')
#     prof=data[-2]
#     if (prof=='Pilot'):
#         print(data[1:4])
#
# f=open('/Users/macbook/Downloads/customer1.txt','r')
# for i in f:
#     data=i.rstrip('\n').split(',')
#     age=data[3]
#     if age>'25' and age<'40':
#         print(data[1:6])

# Read  count of people working in each prof :

f=open('/Users/macbook/Downloads/customer1.txt','r')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    prof=data[4]
    if prof not in dic:
        dic[prof]=1
    else:
        dic[prof]+=1
print(dic)







