#create total of 2 matrices of 3*3 order  2D

import numpy as np
a=np.array([[1,2,3],[2,3,4],[5,6,7]])
b=np.array([[1,4,3],[2,5,4],[8,9,7]])


  # [1 2 3]       # [1 4 3]
  # [2 3 4]       # [2 5 4]
  # [5 6 7]       # [8 9 7]

c=np.add(a,b) #adds each element correspondingly from 2 matrices
print(c)
print()

#Note : Order of 2 matrix should be same to get the output matrix with their sum as shown below :

# import numpy as np
# a=np.array([[1,2,3],[2,3,4],[5,6,7],[2,5,6]])
# b=np.array([[1,4,3],[2,5,4],[8,9,7]])
# c=np.add(a,b)
# print(c)  #error >> operands could not be broadcast together with shapes (4,3) (3,3)

#Subtraction :
# import numpy as np
# a=np.array([[1,2,3],[2,3,4],[5,6,7]])
# b=np.array([[1,4,3],[2,5,4],[8,9,7]])
# c=np.subtract(a,b)
# print(c)


#Multiplication :

# import numpy as np
# a=np.array([[1,2,3],[2,3,4],[5,6,7]])
# b=np.array([[1,4,3],[2,5,4],[8,9,7]])
# c=np.multiply(a,b)
# # print(c)
# print()

#Division :

# import numpy as np
# a=np.array([[1,2,3],[2,3,4],[5,6,7]])
# b=np.array([[1,4,3],[2,5,4],[8,9,7]])
# c=np.division(a,b)
# print(c)
# print()

#To find square  >>  square() function :

import numpy as np
a=np.array([[1,2,3],[2,3,4],[5,6,7]])

c=np.square(a)
print(c)


# To find square root >>  sqrt() function :

import numpy as np
a=np.array([[1,2,3],[2,3,4],[5,6,7]])
c=np.sqrt(a)
print(c)

#1d list : slicing