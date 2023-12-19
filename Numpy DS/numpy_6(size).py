#Size :
#   Total number of elements

#Example :
#(4*4) ====> 16 elements
#(5,4) ====> 20
#(3,4) ====> 12

import numpy as np
a=np.array([[[1,2,3,4],[5,6,2,8],[7,8,9,5]]])
print(a)
print(a.ndim)
print(a.shape)
print(a.size) #12 elements
