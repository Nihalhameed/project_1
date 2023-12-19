#Ones matrix  one() : complete elements in a matrix should be 1
# [ 1 1 1 ]
# [ 1 1 1 ]
# [ 1 1 1 ]
# [ 1 1 1 ]  (4*3)

# [1 1]
# [1 1] (2*2)

import numpy as np
a=np.ones([4,4],dtype=int)
print(a)  #[[1 1 1 1]
#           # [1 1 1 1]
#           # [1 1 1 1]
#           # [1 1 1 1]]


#1D ones matrix
import numpy as np
a=np.ones([4],dtype=int)
print(a)

#3D ones matrix
import numpy as np
a=np.ones([1,4,4],dtype=int)
print(a)