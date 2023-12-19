#Note :

#Numpy has many fucntions,but only suitable functions needed for Data Science is needed
#Numpy functions for Data Science -its working need to be studied, no program based problems are needed


import numpy as np
a=np.array([1,2,3,4,5])
print(type(a)) # <class 'numpy.ndarray'> (ndimensional array)
#When an array is created using numpy its class is called an 'ndimensional array'

#Dimension >> No: of axis

#1D : 1 axis (x)  >> there is only a 'row' or 'colum' of data

#2D : 2 axis (x,y) >> there is both rows and columns

#3D : 3 axis (z,x,y)    i.e in numpy library axis of 3D is in the order : z,x,y

#ndim  function : >> ndim is used for checking dimension
print(a.ndim)

#Order = No. of rows * No. of columns

#[3,4,5]
#[2,3,4]
#[3,4,5]
#[5,6,7]

# Shape function :Order of matrix = rows*columns

print(a.shape) #order of array here :
                      # (5,)  >>






