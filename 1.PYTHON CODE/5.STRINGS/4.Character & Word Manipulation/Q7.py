'''
Keep only the first occurrence of each character.
'''

str = input("Enter string : ").lower()
result = ""
for s in str :
    if s not in result:
        result+=s
print(result)
