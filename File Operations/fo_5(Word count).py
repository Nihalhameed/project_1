f=open('wordcount','r')

for i in f:
    data = i.rstrip('\n').split(' ')
    dic={}
    for j in data:
        if j not in dic:
            dic[j]=1
        else:
            dic[j]+=1
    print(dic)



