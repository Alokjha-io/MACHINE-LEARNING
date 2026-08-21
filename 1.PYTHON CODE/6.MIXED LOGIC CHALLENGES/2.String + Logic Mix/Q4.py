'''
Replace every vowel in a string with its position (a=1, e=2...).
'''

s = input("Enter a string : ").lower()
new_str = ""
vowels = ['a','e','i','o','u']
for ch in s:
    if ch in vowels:
        new_str += str(vowels.index(ch)+1)
    else:
        new_str += ch
print(new_str)
    
