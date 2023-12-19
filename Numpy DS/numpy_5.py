#3D (3*4) >> generate output  in (z,x,y) >> (1*3*4)

import numpy as np
a=np.array([[[1,2,3,4],[5,6,2,8],[7,8,9,5]]]) #square brackets count denote the number of axis(ndim) >>  here its z,x,y
print(a)
print(a.ndim) # 3 dimension
print(a.shape)