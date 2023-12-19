#Split() function :

#Word Count problem :
#Definition :
  #The line words are given and the number of occurence(count)of each word in the line of words
  #is called a word count problem.



# line='cat rat bat bus cat cat rat bus bus cat rat bus cat rat rat bat' (line by line data)

#Final Output to get in word-count problem:

#cat >> 5
#rat >> 5
#bat >> 2
#bus >> 4

#To convert line by line data into word by word >>  We use split() function :

line='cat rat bat bus cat cat rat bus bus cat rat bus cat rat rat bat'
data=line.split(',') #space >> ' ' is used to seperate the words into a list
#line.split(',') #(',') is used to print it as a single string of elements without seperation in a list
print(data)

#output :
#['cat', 'rat', 'bat', 'bus', 'cat', 'cat', 'rat', 'bus', 'bus', 'cat', 'rat', 'bus', 'cat', 'rat', 'rat', 'bat']
#This is a word by word data.

# Complete Solution :
line='cat rat bat bus cat cat rat bus bus cat rat bus cat rat rat bat'
#Step 1 :
data=line.split(' ') #space >> ' ' is used to seperate the words and make it to a list
#Step 2 :
dic={}
#Step 3 :
for i in data:
    if i not in dic: #i >> list of words
        dic[i]=1
    else:
        dic[i]+=1   #increment i if already present in dictionary
print(dic)  #output : {'cat': 5, 'rat': 5, 'bat': 2, 'bus': 4}

#Logic of above word-count problem :

#1. Split the line by line data to word by word using split()
#2. Create an empty dic (there is no key & value)
#3. for i in data : check at first if 'i=cat' is present or not in dictionary..similary rest of words is checked
    #if i not in dictionary :
           #dic[i] = 1 #dic[i],where i is cat at first...similarly each word is checked
    #else :
       #dic[i]+=1 #increment i if already present in dictionary





