#index based problem :
lst=[10,15,20,25,30,10,50]
print(lst[1]+lst[3]) #prints the sum of elements in index 1 and index 3
print(lst[3]+lst[-1])
#Interview based question :
#  print(lst[1]+lst[-0]) = ?
print(lst[1]+lst[-0])  #0 takes neither positive or negative values  so its lst[-0] >> lst[0]