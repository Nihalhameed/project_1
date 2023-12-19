#To add a single element at a time in a set : use variablename.add() function

st={2,4,5,6}
st.add(100)
print(st)  # {2, 100, 4, 5, 6} #inseetion order is not preserved in set

#To add multiple elements at a time in a set : use update()function

st={2,5,6,7}
st.update([50,10,20])
print(st)     # {2, 5, 6, 7, 10, 50, 20}
