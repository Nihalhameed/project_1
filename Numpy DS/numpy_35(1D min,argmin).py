#min():

#1d min,argmin
#2d column min ,row min
#2d column argmin,row argmin



#1d min,argmin:

import numpy as np
a=np.array([5,4,3,2,1,9,5,7,10,4])
print(a)

print(np.min(a)) #min element = 1

print()

print(np.argmin(a)) #index = 4