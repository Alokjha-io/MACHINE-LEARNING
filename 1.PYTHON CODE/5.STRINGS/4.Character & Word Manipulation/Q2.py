'''
Remove all spaces from a string.
'''

str = input("Enter string : ")
result = ""
for s in str:
    if s not in " ":
        result+=s
print(result)