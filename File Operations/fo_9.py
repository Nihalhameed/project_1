
#File readings
#Key      :  value
#district :  temperature

#malapuram,25
#ernakulam,30
#palakkad,31
#thrissur,31
#malappuram,30
#ernakulam,34

#algo:
#else:
   # oldtemp=temp (temp=dic[dist],which means to get the value take its corresponding key ) temp is 'value'..its key is 'dic[dist]'
   # if temp>oldtemp:
    #update dic with new temp
   #else
     #update dic with old temp
f=open('/Users/macbook/Downloads/temper','r')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    dist=data[0]
    temp=data[1]
    if dist not in dic:
        dic[dist]=temp #temp is value here
    else:
        oldtemp=dic[dist]
        if temp>oldtemp:
            dic[dist]=temp
        else:
            dic[dist]=oldtemp
for a,b in dic.items():
    print(a,":",b)



