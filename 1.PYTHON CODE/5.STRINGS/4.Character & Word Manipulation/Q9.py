'''
Swap case: uppercase → lowercase and lowercase → uppercase. 
'''

str = input("Enter string : ")
result = ""
for s in str:
    if s.islower():
        result+=s.upper()
    else:
        result+=s.lower()
print(result)