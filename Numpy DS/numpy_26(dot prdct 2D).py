#2D :

#Note :
#dot product is possible to do only when :
      # first matrix columns = second matrix rows
      # Its not necessary for the order of matrix to be same

import numpy as np
a=np.array([[1,2,3,4],[1,2,3,5],[2,3,4,5],[4,3,2,1]])   #4*4 matrix
b=np.array([[4,3,2,1],[2,3,4,5],[1,2,3,4],[5,4,2,1]])
#[1,2,3,4]       [4,3,2,1]
#[1,2,3,5]       [2,3,4,5]
#[2,3,4,5]       [1,2,3,4]
#[4,3,2,1]       [5,4,2,1]
c=np.dot(a,b)
print(c)



#[1*4+2*2+3*1+4*5 etc