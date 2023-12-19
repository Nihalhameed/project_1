#[0 0 0]
#[0 0 0]
#[0 0 0]
#[0 0 0] (4*3)

#zeros matrix  : zero()

import numpy as np
a=np.zeros([3,3]) # (3,3) is the order of matrix
print(a)
  # output [[0. 0. 0.]
          #  [0. 0. 0.]
           #  [0. 0. 0.]]
 #Need to change the dtype from float from the output

import numpy as np
a=np.zeros([3,3],dtype=int) # (3,3) is the order of matrix
print(a)
#[[0 0 0]
# [0 0 0]
# [0 0 0]]