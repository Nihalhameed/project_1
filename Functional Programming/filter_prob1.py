#even numbers from given list

lst=[1,2,3,4]
f=list(filter(lambda num:num%2==0,lst))
print(f)

#odd numbers from given list

lst=[1,2,3,4]
f=list(filter(lambda num:num%2==1,lst))
print(f)

#read the cube of odd numbers from given list

lst = [1, 2, 3, 4]
c=list(map(lambda num:num**3, lst))
f=list(filter(lambda num:num%2!=0,c))
print(f)
