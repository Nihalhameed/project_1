#2D
import numpy as np
a=np.array([[2,3,4,5],[5,4,6,7],[4,3,2,6],[6,5,4,8]])
print(a)
#  [2 3 4 5]
#  [5 4 6 7]
#  [4 3 2 6]
#  [6 5 4 8]

print(np.max(a)) #8 >> index of max element

print()

#colum-wise :
print(np.max(a,axis=0))

#  [2 3 4 5]
#  [5 4 6 7]  >> column wise max : [6 5 6 8]
#  [4 3 2 6]
#  [6 5 4 8]

#row-wise :

print(np.max(a,axis=1))

#  [2 3 4 5]
#  [5 4 6 7]  >> row wise max : [5 7 6 8]
#  [4 3 2 6]
#  [6 5 4 8]


#argmax() :

print(np.argmax(a))

#column -wise :

print(np.argmax(a,axis=0))

#  [2 3 4 5]
#  [5 4 6 7]  >> column wise argmax (based on index) : [3 3 1 3]
#  [4 3 2 6]
#  [6 5 4 8]


#row-wise :

print(np.argmax(a,axis=1))

#  [2 3 4 5]
#  [5 4 6 7]  >> row-wise argmax (based on index) : [3 3 3 3]
#  [4 3 2 6]
#  [6 5 4 8]