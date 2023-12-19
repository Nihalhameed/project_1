#2d 3*4 matrix create
#2D 3*4 matrix change to 2*6)
#2D 3*4 matrix >> 3D 3*4
#2D 3*4 >> 1D

import numpy as np
a=np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(a)

print()

b=a.reshape([2,6])
print(b)

print()

c=a.reshape([1,3,4])
print(c)

print()

d=a.reshape(12) #x axis = 12 is the element count : order of matrix multiplied value
print(d)