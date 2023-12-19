#Read the numbers from file 'numbers' and add the numbers to a list and do sum total of list

# f=open('numbers','r')
#
# lst=[]
# for i in f:
#     lst.append(i)
# print(lst)  #['100\n', '101\n', '102\n', '103\n', '104\n', '105\n', '106\n', '107\n', '108\n', '109\n', '110\n']
               # \n appears because of pressing enter key in file 'numbers' after each number going to next line

# rstrip() function - used to delete any character or element in a string from right side


# data='hello\n'
# data1=data.rstrip('o\n') #removes 'o' and '\n'
# print(data1) #hell

# f=open('numbers','r')
#
# lst=[]
# for i in f:
#     lst.append((i.rstrip('\n'))
# print(lst)  #['100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110'] is string,so cannot find sum


f=open('numbers','r')

lst=[]
for i in f:
    lst.append(int(i.rstrip('\n')))
print(lst)
print("Sum is: ",sum(lst)) # [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
                           # Sum is:  1155
