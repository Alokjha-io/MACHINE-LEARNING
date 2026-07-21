'''
Remove duplicate characters from a string.
'''

str = input("Enter string : ")
result = ""
for s in str:
    if str.count(s) == 1:
        result+=s
print(result)

