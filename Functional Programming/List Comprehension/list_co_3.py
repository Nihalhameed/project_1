#key : vehicle_name
#value : weight

dic={'bike':500,'car':2500,'cycle':100,'bus':5000,'van':3500}
# read the name of vehicles weight above 30000
lst=[i for i in dic if dic[i]>3000]
print(lst)

# for printing upper() case :

dic={'bike':500,'car':2500,'cycle':100,'bus':5000,'van':3500}
# read the name of vehicles weight above 30000
lst=[i.upper() for i in dic if dic[i]>3000] #uses upper()
print(lst)

