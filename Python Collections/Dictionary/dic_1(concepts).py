dic={'id':101,'fname':'nihal','lname':'hameed','age':23,'prof':'intern','salary':75000}
print(dic)
#1.
#To read any 'value' from the dictionary, consider its corresponding 'key' :

#Syntax :

print(dic['fname'])  #nihal  ( dic[key] = value )  # 'fname' = key & 'nihal' = value
print(dic['prof']) #intern

#2. To print key value pair indvidually :

#Format to read :

#id 101
#fname nihal
#lname hameed
#age 23
#prof intern


# for i in dic :
#     print(i) #only key is printed >> (i=key)

#Syntax :
dic={'id':101,'fname':'nihal','lname':'hameed','age':23,'prof':'intern','salary':75000}
for i in dic:
    print(i,dic[i]) #i=key, dic[i] = all 'values' of key

#3.
#How to update a value in dictionary? :

#Update age 23 to 30

#Syntax :

#dic['key']=new value

dic['age']=30
print(dic)  #{'id': 101, 'fname': 'nihal', 'lname': 'hameed', 'age': 30, 'prof': 'intern', 'salary': 75000}

#Another method :
#Update  age 30 to 35 :
dic['age']+=5
print(dic) #{'id': 101, 'fname': 'nihal', 'lname': 'hameed', 'age': 35, 'prof': 'intern', 'salary': 75000}

#4. To check whether a key is present in dictionary : True or False

dic={'id':101,'fname':'nihal','lname':'hameed','age':23,'prof':'intern','income':75000}
print('income' not in dic)      #False
print('fname' in dic)           #True

#5. To add a new key-value pair to the exisiting dictionary :

dic['hobby']='playing'
print(dic) # {'id': 101, 'fname': 'nihal', 'lname': 'hameed', 'age': 23, 'prof': 'intern', 'salary': 75000, 'hobby': 'playing'}

#6. To delete a key-value from dictionary : use del & dic['key']

del dic['id']
print(dic)  #{'fname': 'nihal', 'lname': 'hameed', 'age': 23, 'prof': 'intern', 'salary': 75000, 'hobby': 'playing'}
