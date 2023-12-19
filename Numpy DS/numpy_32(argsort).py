#argsort() : 1) First elements are sorted by normal sorting.
#            2) Secondly sorted elements are given index values :
                  # ( index values are taken by considering the matrix of the given data)

#1D

import numpy as np
a=np.array([15,8,5,1,2,6,8,7,4])
print(np.argsort(a))
print()
# based on index argsort is done :
# 15 -> 0
# 8 -> 1
# 5 -> 2
# 1 -> 3
# 2 -> 4
# 6 -> 5
# 8 -> 6
# 7 -> 7
# 4 -> 8
#normal sorting  = [ 1  2  4  5  6  7  8  8 15]
# [3 4 8 2 5 7 1 6 0] #this is the output which gives the index value of each elements

#argsort()

#2D :

b=np.array([[2,3,4,5],[5,3,2,1],[5,7,8,5],[4,3,2,1],[5,2,3,4]])
print(np.argsort(b))
print()

 # [2 3 4 5]  >>  [2 3 4 5] =  [0 1 2 3]
 # [5 3 2 1]  >>  [1 2 3 5]  = [3 2 1 0]
 # [5 7 8 5]  >>  [5 5 7 8]  = [0 3 1 2]
 # [4 3 2 1]  >>  [1 2 3 4]  = [3 2 1 0]
 # [5 2 3 4]  >>  [2 3 4 5]  = [1 2 3 0]

#Above 2D sorting takes in row-wise manner


b=np.argsort(a,axis=0)
print(np.argsort(b))
