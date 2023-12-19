#Sort () :

import numpy as np
a=np.array([1,5,3,4,9])
print(np.sort(a))

print(np.sort(a)[::-1]) #Descending order

#2D
print("*"*50)

b=np.array([[5,2,3,4],[4,3,2,1],[7,5,9,8],[2,3,4,1]])
print(np.sort(b))  #2d matrix sorting happens in row-wise manner by default

print("*"*50)

print(np.sort(b,axis=0)) #row -wise sorting when axis=0

