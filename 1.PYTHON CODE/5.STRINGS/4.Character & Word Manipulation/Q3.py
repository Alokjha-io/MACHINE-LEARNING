'''
Replace all vowels with ‘*’. 
'''

str = input("Enter string : ").lower()

for i in range(len(str)):
    if str[i] in "aeiou":
        str = str.replace(str[i],'*')
print(str)