#1.

# f=open('story','r')
# count=0
# for i in f :
#     data = i.rstrip('\n').split(',')
#     if 'T' not in data[0]:
#         count+=1
# print(count)
#

#2.
# def displayword():
#     a=open('story', 'r')
#     for i in a:
#         data = i.rstrip('\n').split(' ')
#         for i in data:
#             if len(i)<=4:
#                 print(i)
# displayword()
#3.

# def words():
#     f = open('story', 'r')
#     count=0
#     for i in f:
#         data=i.rstrip('\n').split(' ')
#         for j in data:
#             if 'e' in j[-1]:
#                 print(j)
#                 count+=1
#     print(count)
# words()

#4.

# lst=int(input("Enter the number of elements: "))
# lst1=[]
# for i in range(lst):
#     element=int(input("Enter an element:"))
#     lst.append(element)
# print(lst[::2])

#5.

# lst=int(input("Enter the number of elements: "))
# lst1=[]
# for i in range(lst):
#     element = int(input("Enter an element:"))
# lst1.append(element)
# largest_num=0
# for i in lst1:
#     if i > largest_num:
#         largest_num+=i
# print(largest_num)

#6.
# string=input("Enter a string: ")
# word=input("Enter the word to remove from string: ")
# for i in string:
#     data=string.split(' ')
#     for i in data:
#         if word in data:
#             data.remove(word)
# print(data)

# string=input("Enter a string: ")
# word=input("Enter the word to remove from string: ")
# a=''
# for i in string:
#     data=string.split(' ')
#     for i in data:
#         if word in data:
#             a+=i
#         else:
#             a+=''
# print(a)





















