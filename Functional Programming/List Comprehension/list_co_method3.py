#Method3 :

#1. For 2 conditions :

#Syntax :

# lst=[print1..if condtion1.. else print2..range]

              #condition1 works only if 'if' is True
              #else condition2
              #range is passed at the end

#2. For more than 2 conditions :

#Syntax :

#lst=[print1.. if condition1 else print2 if condition2 else print3 range]



#1.Print numbers from 1to 30 range of numbers  if even -print square of numbers ,if odd-print cube of numbers :

lst=[(i,i**2) if i%2==0 else (i,i**3 ) for i in range(1,31)]
print(lst)

#2. 1 to 20 range, if even-print even ,if odd-print odd

lst=[(i,"even") if i%2==0 else (i,"odd") for i in range(1,21)]
print(lst)

#3. # 1 to 50 range

#1-15 ===> small
#16-35 ===> medium
#36-50 ===>large

lst=[(i,"small") if i<=15 else (i,"medium") if i>=16 and i<=35 else (i,"large") for i in range(1,51)]
print(lst)