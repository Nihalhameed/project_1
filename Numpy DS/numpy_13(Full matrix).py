#Full matrix : full()
# If all elements in a matrix is created with same elements that a user give,
# then that matrix is called a full matrix

#2D  full matrix with element filling the matrix with 3:

import numpy as np
a=np.full([3,5],3)
print(a)

#3D 4*4 matrix,with all elements filled with 5

import numpy as np
a=np.full([1,4,4],5) #z=
print(a)

#1D 10 elements,with all elements filled with 7

import numpy as np
a=np.full([10],7) #  10 elements
print(a)