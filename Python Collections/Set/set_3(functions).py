#delete an element from the set :
st={10,20,30,40,50,60,70,80}
 #remove() : used to delete any element from the set by denoting the element
 #discard() : used to delete any element from the set by denoting the element
st.remove(50) #st.discard(50)
print(st)

#difference between remove and discard :
st.remove(100)
print(st) #KeyError: 100 #return type



