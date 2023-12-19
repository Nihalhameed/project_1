#List slicing
#1D : only rows present

import numpy as np
a=np.array([9,7,3,4,1,2,5,6,7,4,7,5])
print(a[2])
print([0])
print(a[1:8]) #index 1 to 7
print(a[1:]) #index 1 to end of list
print(a[:6]) #index 0 to 5
print(a[1:9:3]) #index 1,4,7
print(a[5::2]) #index 5 to end with step  2

