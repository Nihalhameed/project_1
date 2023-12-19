#Read range from 5 to 29 , it should be a 5*5 matrix

# import numpy as np
# a=np.arange(5,30) #arranges elements from 5 to 29 in a single matrix of 1D by default
# b=a.reshape([5,5]) #reshapes the elements into a 5*5 matrix order =5,5
# print(b)

#can reduce the step :

import numpy as np
a=np.arange(5,30).reshape([5,5])
print(a)