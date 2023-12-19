#2D SLICING :

import numpy as np
a=np.array([[2,3,4,5],[5,4,6,7],[4,3,2,6],[6,5,4,8],[7,4,9,3]]) #5*4
print(a)
#          c0 c1 c2 c3
# 0th row [2 3 4 5]
# 1st row [5 4 6 7]
# 2nd row [4 3 2 6]
# 3rd row [6 5 4 8]
# 4th row [7 4 9 3]

#Syntax :
#     print(a[rows,columns])
print(a[:3,:2]) #rows=0,1,2,column=0,1    [2 3]
 #                                        [5 4]
 #                                        [4 3]

print(a[1:4,:4]) #rows=1,2,3 , col=0,1,2,3
#                                         [5 4 6 7]
#                                         [4 3 2 6]
#                                         [6 5 4 8]

print(a[1:4,2:4]) #rows=1,2,3 col=2,3
# [6 7]
#  [2 6]
#  [4 8]

print(a[1:4:2,2:4]) #rows=1,3 ,col =2,3
#  [6 7]
#  [4 8]
print(a[1::2,::2]) #rows=1,3 col=0,2
 # [5 6]
 # [6 4]


#zeroth row of data :

print(a[0,:])

print()

#zeroth column of data :

print(a[:,0])