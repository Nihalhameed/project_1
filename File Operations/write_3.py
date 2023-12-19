#Create a file and read some data of fruits in demo6 file and copy it to another file,
# condition : if apple not in demo6 file

f=open('demo6','r')
g=open('demo7', 'w')
for i in f:
    if 'apple' not in i:
        g.write(i)



