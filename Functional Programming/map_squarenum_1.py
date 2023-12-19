#Traditional method to use map() :

# lst=[1,2,3,4]
# def square(num):
#     return num**2
# f=list(map(square,lst)) #map() is used,  'square' is defined in def
# print(f)

#latest method :

lst=[1,2,3,4]
f=list(map(lambda num:num**2,lst))
print(f)

#odd numbers and find its cube from given list :

lst=[1,2,3,4,5]
f=list(map(lambda num:num**3 if num%2==1 else "-",lst))
print(f)
