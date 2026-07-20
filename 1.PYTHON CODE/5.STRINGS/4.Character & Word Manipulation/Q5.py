'''
Print the string after removing all digits.
'''

str = input("Enter string : ")
result = ""
for s in str:
    if not s.isdigit():
        result+=s
print(result)