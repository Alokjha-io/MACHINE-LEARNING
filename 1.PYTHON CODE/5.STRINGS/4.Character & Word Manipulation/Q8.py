'''
Remove consecutive duplicate characters (e.g., “aaabb” → “ab”).
'''

str = input("Enter string : ").lower()
result = str[0]
for i in range(1,len(str)):
    if str[i] != str[i-1]:
        result+=str[i]
print(result)