#0 1 2 3 4 5
#0 1 2 3 4
#0 1 2 3
#0 1 2
#0 1
for i in range(1,6):        #for i in range(5,0,-1)
    for j in range(0,7-i):  #for j in range(0,i+1)
        print(j,end=' ')
    print()