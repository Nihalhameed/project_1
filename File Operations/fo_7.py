#Each country count :
# f=open('/Users/macbook/Downloads/customer1.txt','r')
# dic={}
# for i in f:
#     data = i.rstrip('\n').split(',')
#     country=data[-1]
#     if country not in dic:
#         dic[country]=1
#     else:
#         dic[country]+=1
# print(dic) #{'india': 21, 'uk': 37, 'us': 78, 'china': 56, 'africa': 90, 'australia': 104, 'ireland': 77}

#print each output in downward format :
f=open('/Users/macbook/Downloads/customer1.txt','r')
dic={}
for i in f:
    data = i.rstrip('\n').split(',')
    country=data[-1]
    if country not in dic:
        dic[country]=1
    else:
        dic[country]+=1
for a,b in dic.items(): #(a,b) is (key,value) .... dic.items() - items  in dictionary #this for loop prints output in key:value pair
    print(a,":",b)



