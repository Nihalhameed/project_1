#Find the count of consonants in the string :
string='luminartechnolab'
vowels='aeiouAEIOU'
lst=[]
for i in string:
    if i not in vowels: #to consider consonants
        lst.append(i) #['l', 'm', 'n', 'r', 't', 'c', 'h', 'n', 'l', 'b']
print(len(lst))
