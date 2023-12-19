#1. How to define?

# dic={}

#Important note:

#Dictionary is a 'key-value' pair
            #whereas list,set,tuples had only values
#key-value ith example:

#id:101 , where id = 'key' & 101 = 'value'
#fname:Nihal , where fname = 'key' & Nihal = 'value'
#lname:Hameed
#age:27 ,where age = 'key' & 27 = 'value'

#Syntax:

dic={'id':101,'fname':'Nihal','lname':'Hameed','age':27} # Nihal and Hameed values are string so denote in singlequotes
print(dic)

#2. Dictionary supports heterogenous data :

dic={'id':101,'fname':'Nihal','lname':'Hameed','age':27,'marks':30.5}
print(dic)      #{'id': 101, 'fname': 'Nihal', 'lname': 'Hameed', 'age': 27, 'marks': 30.5}

#3. It supports duplicate values & not supports duplicate keys

#3.1 Duplicate keys are not supported in dictionary:

dic={'id':101,'fname':'Nihal','lname':'Hameed','age': 27,'age':28}
print(dic)  #{'id': 101, 'fname': 'Nihal', 'lname': 'Hameed', 'age': 28}

#3.2 Duplicate values are supported :
dic={'id':101,'fname':'Nihal','lname':'Hameed','age': 27,'age1':27}
print(dic)   #{'id': 101, 'fname': 'Nihal', 'lname': 'Hameed', 'age': 27, 'age1': 27}

#4. Insertion order is preserved in dictionary

#5. Dictionary is mutable : Can update the keys and values
