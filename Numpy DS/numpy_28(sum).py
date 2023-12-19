# Sum() function :

import numpy as np
a=np.array([2,3,4,5]) #1D
b=np.sum(a)
print(b)

print("*"*50)

b=np.array([[1,2,3,4],[2,3,4,5]]) #2D
print(np.sum(b))

#[1,2,3,4]

#[2,3,4,5]

print("*"*50)

#for 1d  there is only rows so total sum is printed directly,
#but in 2d there are rows and columns so sum of total elements in row
#as well as total elements in column must be calculated

#axis()
 # - used to get rows and columns seperately

 #axis =0 or axis=1 can be passed as values

#axis =0 ,
print(np.sum(b,axis=0)) #Sum of columns  is printed  #[1,2,3,4]
#                                                         +      = [3 5 7 9]
                                                     #[2,3,4,5]
#[1,2,3,4]

#[2,3,4,5]

print(np.sum(b,axis=1)) #Sum of Rows is printed       #[1,2,3,4]
#                                                          +        = [10 14]
                                                      #[2,3,4,5]


