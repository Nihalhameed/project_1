#2D 4*5 matrix

import numpy as np
a=np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
print(a)

print("*"*50)

# Reshape():
# To change an order of matrix that user already created

b=a.reshape([5,4])
print(b)  #4*5 >> 5*4

#Note :
# When a matrix is reshaped the order changes but the toal elements remains the same