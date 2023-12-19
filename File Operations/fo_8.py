File readings format :#id,name,release_year,rating,duration

#1. Above 2005 release movie name,year,rating
#2. rating above 4 name,year,rating,duration
#3. rating above 3 and year above 2007 name,year,rating
#4. 1975-2000 range name,year,rating
#5. rating 4 to 4.5 name,year,rating,duration
#6. each year movie count

#1.

# f=open('/Users/macbook/Downloads/movies_cleaned_pandas.csv','r')
# dic={}
# for i in f:
#     data=i.rstrip('/n').split(',')
#     year=data[2]
#     if year>'2005':
#         print(data[1:4])

#2.

# f=open('/Users/macbook/Downloads/movies_cleaned_pandas.csv','r')
# dic={}
# for i in f:
#     data=i.rstrip('/n').split(',')
#     rating=data[-2]
#     if rating > '4':
#         print(data[1:5])

#3.

# f=open('/Users/macbook/Downloads/movies_cleaned_pandas.csv','r')
# dic={}
# for i in f:
#     data=i.rstrip('/n').split(',')
#     rating=data[-2]
#     year=data[2]
#     if rating > '3' and year>'2007':
#         print(data[1:4])

#4.

# f=open('/Users/macbook/Downloads/movies_cleaned_pandas.csv','r')
# dic={}
# for i in f:
#     data=i.rstrip('/n').split(',')
#     year=data[2]
#     if year>'1975' and year<'2000':
#         print(data[1:4])

#5.
# f=open('/Users/macbook/Downloads/movies_cleaned_pandas.csv','r')
# dic={}
# for i in f:
#     data=i.rstrip('/n').split(',')
#     rating=data[-2]
#     if rating >'4' and rating<'4.5':
#         print(data[1:5])

#6.
f=open('/Users/macbook/Downloads/movies_cleaned_pandas.csv','r')
dic={}
for i in f:
    data=i.rstrip('/n').split(',')
    year=data[2]
    if year not in dic:
        dic[year]=1
    else:
        dic[year]+=1
for a,b in dic.items():
    print(a,":",b)




