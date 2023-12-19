#To take each element in the list of array : use of for loop

#1D
import numpy as np
# a=np.array([5,4,3,2,1,9,5,7,10,4])
#
#
# for i in a:
#     print(i)

#2D
b=np.array([[2,3,4,5],[5,4,6,7],[4,3,2,6],[6,5,4,8]])


for i in b:
    for j in i:
        print(j)

