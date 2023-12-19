import numpy as np
a=np.array([[2,3,4,5],[5,4,6,7],[4,3,2,6],[6,5,4,8]])
print(a)

print()

print(np.min(a))

print()

#column-wise:

print(np.min(a,axis=0))

#row-wise :

print(np.min(a,axis=1))



print(np.argmin(a))

print(np.argmin(a,axis=0))

print(np.min(a,axis=1))