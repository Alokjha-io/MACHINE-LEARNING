'''
Remove all vowels from a string. 
'''

str = input("Enter string : ").lower()
result = ""
for s in str:
    if s not in "aeiou":
        result+=s
print(result)