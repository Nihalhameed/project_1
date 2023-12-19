#A string is given , find the count of vowels in that string :
string='luminar technolab'
vowels='aeiouAEIOU'
lst=[]
for i in string:
    if i in vowels:
        lst.append(i) # ['u', 'i', 'a', 'e', 'o', 'a']
print(len(lst)) #count is printed which is 6