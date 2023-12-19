#To read selected data based on condition :

import numpy as np
a=np.array([42,43,44,45,46,47])


b=a>42

 #comparing main array 'a' with conditon in 'b'( b=a>42)
print(b)

#output : [False  True  True  True  True  True]

#But we need to get the elements greater than 42 from the array 'a'

import numpy as np
a=np.array([42,43,44,45,46,47])


b=a>42

c=a[b]  #comparing main array 'a' with conditon in 'b'( b=a>42)
print(c)

#output : [43 44 45 46 47]

