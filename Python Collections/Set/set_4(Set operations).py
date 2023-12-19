#Set operations :
 # 3 TYPE OF Operations in a set :
   #1. Union
   #2. Intersection
   #3. Difference

st1={1,2,3,4,5,6,7,8,9,10}
st2={6,7,8,9,10,11,12,13,14,15}

#1. Union ==>> result : {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
#   Gives the combined result of two sets ( all elements in both set ,without duplicate values as by properties of set)

# Syntax :
st3=st1.union(st2)
print(st3)            # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

#2. Intersection ==>  result : {6, 7, 8, 9, 10}
# Gives the common elements from both sets
# Syntax :

st3=st1.intersection(st2)
print(st3)          # {6, 7, 8, 9, 10}

#3. Difference :

#A-B : Element present in A & not present in B
#B-A : Element present in B & not present in A

#st1-st2 : {1,2,3,4,5}
# Syntax :
st3=st1.difference(st2)
print(st3)        #{1, 2, 3, 4, 5}

#st2-st1 :   {11, 12, 13, 14, 15}
#Syntax :
st3=st2.difference(st1)
print(st3)        #{11, 12, 13, 14, 15}

