tu=(10,20,30,40,50,60,70,80,90,100)

#Update 50 to 250 from the tuple above: #we know tuple cannot update values i.e is immutable
lst=list(tu)
lst.remove(50)
lst.insert(4,250)

tu1=tuple(lst)
print(tu1)

