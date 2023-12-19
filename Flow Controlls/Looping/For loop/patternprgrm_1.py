#Pattern problem

for i in range(1,4):
    for j in range(1,4): #inner loop works completely first to go back to outer loop
        print(i,end=' ') #end=' ' is used to print giving spaces each time in a single line
    print() #this print statement is used to print the pattern for every  j in new line