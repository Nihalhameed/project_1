#Continue - Never exits loop, but based on condition given it goes back to the loop again.

for i in range(1,51):
    if(i==25):
        continue #prints value from 1 to 24 then 26 to 50 >>> removes 25 based on condition
    print(i)