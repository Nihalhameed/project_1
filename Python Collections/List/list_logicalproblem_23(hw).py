lst=[1,3,5,6,4,3,5,7,8,9,5,4,2,4,6,7,8,6,4,3,0,4,6,7]
#Generate a new list : lst1=[1,6,3,9,2,8,0]
#Logic of the problem :
  # Whenever a series is decrease or increase the the element just before it  is collected
lst1=[] #initially 1 is inside list
inc=[1,3,5,6]
dec=[4,3]
inc1=[5,7,8,9]
dec1=[5,4,2]
inc2=[4,6,7,8]
dec2=[6,4,3,0]
inc3=[4,6,7]
for i in lst:
    if(lst[0]<lst[1]<lst[2]<lst[3]): #index number is taken
        inc.append(lst[3])
    print(inc)
    elif()


