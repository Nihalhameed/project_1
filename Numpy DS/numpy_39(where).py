#where () : checks for element based on condition and reads the index value corresponding to it

#1D

import numpy as np
a=np.array([2,3,4,5,1,7,8,7,9])


print(np.where(a==7))  #checks where  eleemnt '7' is in array(a)

#output : #(array([5, 7]),) ===>> 5 and 7 are index values

print(np.where(a>5))

#2D



b=np.array([[2,1,4,5],[1,4,6,7],[4,3,1,6],[6,5,4,8]])
print(np.where(b==1))

# (row number,column number) ==>> (0,1) (1,0) (2,2)
#(array([0, 1, 2]), array([1, 0, 2])) ==> array([row number]),array([column number])
