#count the no of vowels in string using list comprehension:

string='luminar technolab'
vowels='aeiouAEIOU'
lst=len([i for i in string if i in vowels])
print("count of vowels:" ,lst)

#count the no of consonants in string using list comprehension:

string='luminar technolab'
vowels='aeiouAEIOU'
lst=len([i for i in string if i not in vowels])
print("count of consonants:" ,lst)
