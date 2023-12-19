
#1D

import numpy as np
a=np.array([2,3,4,5])
b=np.array([6,5,4,8])


#function used for joining two arrays : concatenate ()
c=np.concatenate((a,b))
print(c)   #[2 3 4 5 6 5 4 8]

#2D


b=np.array([[2,4,5],[5,4,6],[4,3,6]])
c=np.array([[6,4,3],[9,2,6],[1,7,5]])

d=np.concatenate((b,c))
print(d)

#  [2 4 5]     [6 4 3]
#  [5 4 6]     [9 2 6]
#  [4 3 6]     [1 7 5]

#output : column wise joining takes place by default in 2D
#  [2 4 5]
#  [5 4 6]
#  [4 3 6]
#  [6 4 3]
#  [9 2 6]
#  [1 7 5]

d=np.concatenate((b,c),axis=1)
print(d)

#output : row wise joining takes place 
 # [2 4 5 6 4 3]
 # [5 4 6 9 2 6]
 # [4 3 6 1 7 5]
