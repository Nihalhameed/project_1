#Floor ,ceil, round

import numpy as np
a=np.array([[1.1,2.5,3.5,4.1],[2.2,3.1,4.5,5.1],[5.4,4.2,3.1,2.1],[4.3,5.1,6.2,7.5]])
print(a)

print("*"*50)

#Floor : discards the decimal part ,mapping is done to the lowest integer value:

# [1.1 2.5 3.5 4.1] >> [1 3 4 4]
# [2.2 3.1 4.5 5.1] >> [2 3 4 5]
# [5.4 4.2 3.1 2.1] >> [5 4 3 2]
# [4.3 5.1 6.2 7.1] >> [4 5 6 7]
c=np.floor(a) #dtype is float  by default
print("Floor",c)

print("*"*50)

#Ceil : If there is a decimal part in a number, it maps to highest integer value

c=np.ceil(a)
print("Ceil",c)

print("*"*50)



#Round : decimal part (if 0.5 below = round to lowest integer) & decimal part (if 0.5 above = round to highest integer)

#Important :

#if in decimal part>> 0.5 comes with Odd number= maps  number to highest value
#if in decimal part >> 0.5 comes with Even number = maps  number to lowest value
c=np.round(a)
print("Round",c)
# [1. 2. 4. 4.]
#  [2. 3. 4. 5.]
#  [5. 4. 3. 2.]
#  [4. 5. 6. 8.]



