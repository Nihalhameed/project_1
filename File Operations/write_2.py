#Create a file with contents and copy the contents of that file to another file :

f=open('demo4','r')
w=open('demo5','w')
for i in f:
    w.write(i) # writes the content into the file, no need to perform additional print operation
