#Identity Matrix : eye() or identity()

#Diagonal elements in the matrix will be 1 and rest of the elements will be 0
# It should be in a square matrix form
# eye() function is used >> when eye function is used it takes  a single value => value of one axis

#example :
#[1 0 0]
#[0 1 0]
#[0 0 1] (3*3) < order

#example 2:
# [1 0 0 0]
# [0 1 0 0]
# [0 0 1 0]
# [0 0 0 1] (4*4)

import numpy as np
a=np.eye(4,dtype=int)
print(a)

print('*'* 50)

import numpy as np
a=np.identity(3,dtype=int)
print(a)